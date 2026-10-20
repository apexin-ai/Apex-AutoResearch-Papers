# Research conversation: I'm revising a research paper and need to understand what a "Qwen3-8B zero-shot baseline" for event argument extraction 

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a7c514e05221cacf5.jsonl`
- **Structured JSON:** [`3a7b3cc514ca0774bc16.json`](../../sessions/3a/3a7b3cc514ca0774bc16.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-10T10:03:53.389Z_

I'm revising a research paper and need to understand what a "Qwen3-8B zero-shot baseline" for event argument extraction (EAE) would look like. Specifically:

1. Search for any reported performance of Qwen3-8B (or similar 8B models) on RAMS or WikiEvents event argument extraction in zero-shot mode.
2. Search for any papers from 2025-2026 reporting zero-shot EAE results with instruction-tuned LLMs (no fine-tuning) on RAMS/WikiEvents.
3. Look for the LtGaE paper (arXiv:2603.02909) results — it reports 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki — is there a zero-shot LLM baseline in that paper?

The context: CompSchema-IE fine-tunes Qwen3-8B on synthetic data. A reviewer says we need a "Qwen3-8B zero-shot (no fine-tuning)" baseline row to show that synthetic supervision actually helps over just using the model directly.

Search queries:
- "Qwen3 zero-shot event argument extraction RAMS WikiEvents"
- "LLM zero-shot EAE RAMS WikiEvents 2025 2026"  
- arXiv 2603.02909 (LtGaE) — does it include a GPT/Qwen zero-shot baseline?
- "instruction tuned LLM zero-shot event argument extraction performance"

Return: estimated performance range for a zero-shot Qwen3-8B on EAE, any reported numbers, and whether existing papers include such baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "e60e3249-d5f9-4fae-94a1-7b8c979fd196",
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

_source line 2 · 2026-05-10T10:03:54.518Z_

I'll search for information about zero-shot performance of Qwen3-8B and other instruction-tuned LLMs on event argument extraction tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e60e3249-d5f9-4fae-94a1-7b8c979fd196",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathTCFGiaAYMCxfmxGZc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f60b37a0-651e-4211-a19d-44fd85998841",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0129VT4AKb5mqn4bbm8CvVnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 829,
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

_source line 3 · 2026-05-10T10:03:54.747Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MjrgBMbmxhsgTnuohaSSg5`</summary>

```json
{
  "query": "Qwen3 zero-shot event argument extraction RAMS WikiEvents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f60b37a0-651e-4211-a19d-44fd85998841",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathTCFGiaAYMCxfmxGZc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "37370431-b298-44d1-948c-14a52c0594ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0129VT4AKb5mqn4bbm8CvVnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 829,
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

_source line 4 · 2026-05-10T10:03:54.971Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013m4Cw6cLSuabnuV1Z7HeTd`</summary>

```json
{
  "query": "LLM zero-shot EAE RAMS WikiEvents 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37370431-b298-44d1-948c-14a52c0594ac",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathTCFGiaAYMCxfmxGZc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ebbec5c1-a755-4f53-a985-9d68eef1ddf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0129VT4AKb5mqn4bbm8CvVnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 829,
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

_source line 5 · 2026-05-10T10:03:55.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KuaWiBy4GyqzhbKNWXLhPv`</summary>

```json
{
  "query": "arXiv 2603.02909 LtGaE event argument extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebbec5c1-a755-4f53-a985-9d68eef1ddf2",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathTCFGiaAYMCxfmxGZc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b706eada-843b-4858-8269-e88772654b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0129VT4AKb5mqn4bbm8CvVnA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 16155,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 254,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 829,
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

_source line 6 · 2026-05-10T10:03:55.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N3sW6YH8rveXTTXYm5taaY`</summary>

```json
{
  "query": "instruction tuned LLM zero-shot event argument extraction performance RAMS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b706eada-843b-4858-8269-e88772654b33",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathTCFGiaAYMCxfmxGZc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8983337e-661b-484a-8636-536a2320a0e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0129VT4AKb5mqn4bbm8CvVnA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 16155,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 254,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 829,
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

_source line 7 · 2026-05-10T10:04:01.054Z_

<details><summary>↩ Tool result · `toolu_01MjrgBMbmxhsgTnuohaSSg5`</summary>

```text
Web search results for query: "Qwen3 zero-shot event argument extraction RAMS WikiEvents"

Links: [{"title":"Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/html/2603.02909v2"},{"title":"[2104.05919] Document-Level Event Argument Extraction by Conditional Generation","url":"https://arxiv.org/abs/2104.05919"},{"title":"Bi-directional feature learning-based approach for zero-shot event argument extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325001402"},{"title":"[2603.02909] Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/abs/2603.02909"},{"title":"[2603.02909v2] Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/abs/2603.02909v2"},{"title":"Document-Level Event Argument Extraction by Conditional Generation - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.69/"},{"title":"(Open Access) Document-Level Event Argument Extraction by Conditional Generation. (2021) | Sha Li | 3 Citations","url":"https://scispace.com/papers/document-level-event-argument-extraction-by-conditional-mfikfuamyh"},{"title":"Generating Uncontextualized and Contextualized Questions for Document-Level Event Argument Extraction","url":"https://arxiv.org/html/2404.04770"},{"title":"GitHub - mayubo2333/PAIE: ACL'2022: Prompt for Extraction? PAIE: Prompting Argument Interaction for Event Argument Extraction","url":"https://github.com/mayubo2333/paie"},{"title":"Statistics of RAMS and WikiEvents datasets. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Statistics-of-RAMS-and-WikiEvents-datasets_tbl2_383452545"}]

Based on the search results, I found relevant information about zero-shot event argument extraction using RAMS and WikiEvents datasets, though the specific focus on "Qwen3" doesn't appear in the results. However, there is closely related research:

## Key Findings:

Research has constructed three zero-shot settings based on the two most widely used document-level event argument extraction (DEAE) datasets, RAMS and WikiEvents, with settings named RAMS2RAMS, RAMS2Wiki, and Wiki2Wiki.

Recent work using LLMs for zero-shot event argument extraction has employed LLaMA3.1-8B and Qwen2.5-7B as generation agents, fine-tuned via LoRA for parameter-efficient adaptation.

A multi-agent collaboration framework for zero-shot document-level event argument extraction includes a generation agent that synthesizes data for unseen events by leveraging knowledge from seen events, and an evaluation agent that extracts arguments from synthetic data and assesses their semantic consistency.

Methods based on LLaMA and Qwen consistently outperform existing DEAE models across all three zero-shot settings, with results showing overall F1 scores of 32.38 and 46.96 in RAMS2Wiki and Wiki2Wiki respectively.

The search results show that Qwen2.5 (rather than Qwen3) has been used in recent zero-shot event argument extraction research on these datasets, with promising results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37370431-b298-44d1-948c-14a52c0594ac",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "a0b14c26-d6a2-4972-b63c-9378a25c8927",
  "sourceToolAssistantUUID": "37370431-b298-44d1-948c-14a52c0594ac",
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

_source line 8 · 2026-05-10T10:04:01.263Z_

<details><summary>↩ Tool result · `toolu_01KuaWiBy4GyqzhbKNWXLhPv`</summary>

```text
Web search results for query: "arXiv 2603.02909 LtGaE event argument extraction"

Links: [{"title":"[2603.02909] Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/abs/2603.02909"},{"title":"Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/html/2603.02909"},{"title":"[2603.02909v2] Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/abs/2603.02909v2"},{"title":"Learning to Generate and Extract: A Multi-Agent Collaboration Framework For","url":"https://arxiv.org/pdf/2603.02909"},{"title":"Enhancing Document-level Argument Extraction with Definition-augmented Heuristic-driven Prompting for LLMs","url":"https://arxiv.org/html/2409.00214v1"},{"title":"[2105.00477] Event Argument Extraction using Causal Knowledge Structures","url":"https://arxiv.org/abs/2105.00477"},{"title":"Event Argument Extraction with Enriched Prompts","url":"https://arxiv.org/html/2501.06825v1"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"[2306.00502] Revisiting Event Argument Extraction: Can EAE Models Learn Better When Being Aware of Event Co-occurrences?","url":"https://arxiv.org/abs/2306.00502"},{"title":"[2501.06825] Event Argument Extraction with Enriched Prompts","url":"https://arxiv.org/abs/2501.06825"}]

Based on the search results, here's what I found about arXiv paper 2603.02909:

The paper is titled "Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction", and it was submitted on March 3, 2026 with a revised version on March 4, 2026.

**Overview:**

Document-level event argument extraction (DEAE) is essential for knowledge acquisition, aiming to extract participants of events from documents. In the zero-shot setting, existing methods employ LLMs to generate synthetic data to address the challenge posed by the scarcity of annotated data.

**The Problem:**

Relying solely on Event-type-only prompts makes it difficult for the generated content to accurately capture the contextual and structural relationships of unseen events, and ensuring the reliability and usability of synthetic data remains a significant challenge due to the absence of quality evaluation mechanisms.

**The Solution:**

The paper introduces a multi-agent collaboration framework for zero-shot document-level event argument extraction (ZS-DEAE), which simulates the human collaborative cognitive process of "Propose-Evaluate-Revise," and the framework comprises a generation agent and an evaluation agent.

The paper appears to be a recent contribution addressing the challenge of extracting event arguments in zero-shot settings using a novel multi-agent approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b706eada-843b-4858-8269-e88772654b33",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "6b9bb45d-ccce-4c44-820e-862b28ce0b8e",
  "sourceToolAssistantUUID": "b706eada-843b-4858-8269-e88772654b33",
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

_source line 9 · 2026-05-10T10:04:01.504Z_

<details><summary>↩ Tool result · `toolu_013m4Cw6cLSuabnuV1Z7HeTd`</summary>

```text
Web search results for query: "LLM zero-shot EAE RAMS WikiEvents 2025 2026"

Links: [{"title":"One Small and One Large for Document-level Event Argument Extraction","url":"https://arxiv.org/pdf/2411.05895"},{"title":"A framework for robotic manipulation tasks based on multiple zero shot models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-17015-z"},{"title":"Prompt engineering techniques: Top 6 for 2026","url":"https://www.k2view.com/blog/prompt-engineering-techniques/"},{"title":"2025: The year in LLMs","url":"https://simonwillison.net/2025/Dec/31/the-year-in-llms/"},{"title":"Structure-Aware Lightweight Document-Level Event Extraction via Code-Based Large Language Models","url":"https://www.mdpi.com/2079-9292/15/6/1187"},{"title":"The End of LLMs As We Know Them: Why 2026 Marks the Beginning of AI’s Next Architecture Revolution | by Aftab | Medium","url":"https://medium.com/@aftab001x/the-end-of-llms-as-we-know-them-why-2026-marks-the-beginning-of-ais-next-architecture-revolution-902ee29484f7"},{"title":"Large Language Model (LLM) conferences 2026 / 2027","url":"https://dev.events/llm"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"Using a Local LLM as a Zero-Shot Classifier ~ Data On","url":"https://www.daton.app/2026/04/using-local-llm-as-zero-shot-classifier.html"},{"title":"ICLR 2026 Workshop Proposal MemAgents: Memory for LLM-Based Agentic Systems","url":"https://openreview.net/pdf?id=U51WxL382H"}]

Based on the web search results, I found relevant information about LLM zero-shot Event Argument Extraction (EAE) on the RAMS and WikiEvents datasets:

## Key Findings

Recent research demonstrates that LLM-based approaches significantly outperform representative supervised and general LLM baselines in cross-task zero-shot and few-shot transfer settings on established news-domain benchmarks (RAMS and WikiEvents), surpassing supervised baselines by over 7% in F1 score.

One approach called SALE (Structure-Aware Lightweight DEE) leverages Code-Based LLMs and formulates event extraction as a Python 3.9 class instantiation task to bridge the gap between semantic understanding and structural adherence.

This method employs a two-stage training paradigm: a Structure-Aware Fine-tuning stage that injects structural knowledge via diverse code-style instruction tasks, followed by an Event Extraction Alignment stage using reinforcement-learning-inspired objectives to optimize trigger and argument extraction while mitigating hallucinations in long-context reasoning.

Additional research includes methods that develop prompts for LLMs on WikiEvents and applies data processing techniques from TextEE to both WikiEvents and RAMS datasets.

The research indicates that zero-shot and few-shot learning approaches with LLMs are proving effective for document-level event argument extraction tasks on these benchmark datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebbec5c1-a755-4f53-a985-9d68eef1ddf2",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "db2c214d-09cf-4549-906f-7c9c77125a72",
  "sourceToolAssistantUUID": "ebbec5c1-a755-4f53-a985-9d68eef1ddf2",
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

_source line 10 · 2026-05-10T10:04:07.973Z_

<details><summary>↩ Tool result · `toolu_01N3sW6YH8rveXTTXYm5taaY`</summary>

```text
Web search results for query: "instruction tuned LLM zero-shot event argument extraction performance RAMS"

Links: [{"title":"Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://arxiv.org/html/2502.16377v1"},{"title":"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_50"},{"title":"[2305.11159] Aligning Instruction Tasks Unlocks Large Language Models as Zero-Shot Relation Extractors","url":"https://arxiv.org/abs/2305.11159"},{"title":"Harnessing the Zero-Shot Power of Instruction-Tuned Large Language Model for Guiding End-to-End Speech Recognition","url":"https://arxiv.org/html/2309.10524"},{"title":"Evaluating the Zero-shot Robustness of Instruction-tuned Language Models | OpenReview","url":"https://openreview.net/forum?id=g9diuvxN6D"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"[2309.10524] Harnessing the Zero-Shot Power of Instruction-Tuned Large Language Model in End-to-End Speech Recognition","url":"https://arxiv.org/abs/2309.10524"},{"title":"Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://www.researchgate.net/publication/394270737_Instruction-Tuning_LLMs_for_Event_Extraction_with_Annotation_Guidelines"},{"title":"Instruction-Tuning LLMs for Event Extraction with ...","url":"https://aclanthology.org/2025.findings-acl.677.pdf"},{"title":"Harnessing the Zero-Shot Power of Instruction-Tuned Large","url":"https://arxiv.org/pdf/2309.10524"}]

I found search results related to instruction-tuned LLMs for event extraction. However, I notice that the results don't contain specific information about the RAMS dataset mentioned in your query. Let me search more specifically for that:

Links: [{"title":"Document-Level Event Argument Extraction via Optimal ...","url":"https://aclanthology.org/2022.findings-acl.130.pdf"},{"title":"Closed-Domain Event Extraction Literature Review January 2025 v1.0","url":"https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf"},{"title":"GitHub - jeremytanjianle/event-extraction-oneie: Event extraction of ACE05 dataset","url":"https://github.com/jeremytanjianle/event-extraction-oneie"},{"title":"A Study on the RAMS Dataset","url":"https://aclanthology.org/2020.blackboxnlp-1.1.pdf"},{"title":"A Multi-Format Transfer Learning Model for Event Argument Extraction","url":"https://arxiv.org/pdf/2208.13017"},{"title":"Roles Across Multiple Sentences (RAMS)","url":"https://nlp.jhu.edu/rams/"},{"title":"SpeechEE: A Novel Benchmark for Speech Event Extraction","url":"https://arxiv.org/html/2408.09462"},{"title":"TextEE: A Standardized, Fair, and Reproducible Benchmark for Event Extraction","url":"https://khhuang.me/TextEE/"},{"title":"Document-level event argument extraction with dual-paradigm fusion strategy | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00350-6"},{"title":"DocEE: A Large-Scale Dataset for Document-level Event Extraction","url":"https://openreview.net/pdf?id=t5zJTjgwngX"}]

Based on the web search results, I can provide you with information about instruction-tuned LLMs and their performance on event argument extraction, including on the RAMS dataset:

## RAMS Dataset Overview

RAMS (Roles Across Multiple Sentences) is a dataset associated with Multi-Sentence Argument Linking that contains 9,124 annotated events from news based on an ontology of 139 event types and 65 roles. The RAMS dataset has more argument types compared to other benchmarks like ACE-2005, making it a more challenging task.

## Zero-Shot Event Argument Extraction Performance

Existing LLM-based information extraction methods generally fall into two categories: In-Context Learning (ICL) and Supervised Fine-Tuning (SFT). ICL-based approaches rely on providing a few-shot context within prompts, enabling LLMs to infer structured information without explicit parameter updates.

Recent studies focusing on instruction-tuning an LLM with predefined event schemas note that real-world applications often require handling previously unseen event types, and investigating how structured guidelines can aid zero-shot or few-shot event extraction remains an important avenue for future research.

## Performance Benchmarks

For the RAMS dataset, the highest argument classification F1 score reported is 52.2. This demonstrates that event argument extraction on RAMS remains a challenging task, particularly compared to sentence-level datasets like ACE-2005 where higher scores are achieved.

The research indicates that instruction-tuned LLMs show promise for zero-shot event extraction tasks, though achieving strong performance on complex datasets like RAMS with its large number of event types and argument roles continues to present challenges for the field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8983337e-661b-484a-8636-536a2320a0e3",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "1d6a5e47-5366-4db4-b2cc-2d4b1729fa3e",
  "sourceToolAssistantUUID": "8983337e-661b-484a-8636-536a2320a0e3",
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

_source line 11 · 2026-05-10T10:04:09.604Z_

Let me fetch the LtGaE paper directly to check for specific baseline numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d6a5e47-5366-4db4-b2cc-2d4b1729fa3e",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathUGcUc1itBB7Sj9RX7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2a56983-e418-41fd-9c3e-526229cd139c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018Kdo2bY567qiXbdFNHssdq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5114,
      "cache_read_input_tokens": 16984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5114,
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

_source line 12 · 2026-05-10T10:04:10.750Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0158ZsCYnhyAvXNo1kjNy7qa`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.02909",
  "prompt": "What are the zero-shot baseline results reported? Does the paper include a Qwen or GPT zero-shot baseline without fine-tuning? What are the specific F1 scores reported for RAMS2RAMS, RAMS2Wiki, and Wiki2Wiki settings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2a56983-e418-41fd-9c3e-526229cd139c",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathUGcUc1itBB7Sj9RX7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df6b834a-bbde-4f1c-95f3-0ae4f75b050b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018Kdo2bY567qiXbdFNHssdq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5114,
      "cache_read_input_tokens": 16984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5114,
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

_source line 13 · 2026-05-10T10:04:11.385Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UuqJyLL1UiekUtGvnJVoLX`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.16377v1",
  "prompt": "Does this paper report zero-shot performance of instruction-tuned LLMs on RAMS or WikiEvents event argument extraction? What are the specific F1 scores reported without fine-tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df6b834a-bbde-4f1c-95f3-0ae4f75b050b",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathUGcUc1itBB7Sj9RX7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0260861b-0457-48ce-a9f6-b21ce2e5e4a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018Kdo2bY567qiXbdFNHssdq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5114,
      "cache_read_input_tokens": 16984,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5114
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 267,
          "cache_read_input_tokens": 16984,
          "cache_creation_input_tokens": 5114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5114,
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

_source line 14 · 2026-05-10T10:04:12.779Z_

<details><summary>↩ Tool result · `toolu_0158ZsCYnhyAvXNo1kjNy7qa`</summary>

```text
Based on the provided arXiv page content, I cannot find the specific zero-shot baseline results, F1 scores for RAMS2RAMS, RAMS2Wiki, and Wiki2Wiki settings, or information about Qwen or GPT baseline performance.

The abstract states that the method "achieves improvements both in data generation quality and argument extraction performance" across "three zero-shot scenarios constructed from the RAMS and WikiEvents datasets," but it does not include the actual numerical results or specific baseline comparisons you're asking about.

To obtain these details, you would need to access the full paper PDF or HTML version linked on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df6b834a-bbde-4f1c-95f3-0ae4f75b050b",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "53dea5a5-ffd8-4d27-b064-87bc4ccb27e2",
  "sourceToolAssistantUUID": "df6b834a-bbde-4f1c-95f3-0ae4f75b050b",
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

_source line 15 · 2026-05-10T10:04:14.971Z_

<details><summary>↩ Tool result · `toolu_01UuqJyLL1UiekUtGvnJVoLX`</summary>

```text
Based on my review of the provided content, **this paper does not report zero-shot performance on RAMS or WikiEvents datasets**. 

The research focuses exclusively on two datasets: ACE05 and RichERE. The authors state they "perform experiments on two standard EE datasets: ACE05 and RichERE," with no mention of RAMS or WikiEvents evaluation.

Additionally, the paper emphasizes supervised fine-tuning rather than zero-shot approaches. The methodology involves "instruction-tuning open-weight LLMs" on annotated training data, not evaluating models without fine-tuning on these alternative datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0260861b-0457-48ce-a9f6-b21ce2e5e4a3",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "3ae6299c-cc73-46fb-a1c8-3726c242dcb1",
  "sourceToolAssistantUUID": "0260861b-0457-48ce-a9f6-b21ce2e5e4a3",
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

_source line 16 · 2026-05-10T10:04:16.293Z_

Let me fetch the PDF of the LtGaE paper to get the actual baseline numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ae6299c-cc73-46fb-a1c8-3726c242dcb1",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathUnaHTGaJcXK4TVhNk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9a155f3-3214-4ee7-81c7-422b1b7a4f35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013gGKmGVMiGFhdHmE6EZDTs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 22098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 603,
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

_source line 17 · 2026-05-10T10:04:17.206Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QVWjbMAixUXphG6Y4kv76h`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2603.02909",
  "prompt": "Report all zero-shot baseline results and F1 scores reported in tables. What are the results for RAMS2RAMS, RAMS2Wiki, and Wiki2Wiki? Are there any LLM baselines (GPT, Qwen, LLaMA) without fine-tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9a155f3-3214-4ee7-81c7-422b1b7a4f35",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathUnaHTGaJcXK4TVhNk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35483871-584f-4e22-870d-e563360c565d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013gGKmGVMiGFhdHmE6EZDTs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 22098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 603,
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

_source line 18 · 2026-05-10T10:04:17.522Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GWdZkXgxAPSUPWCc6mPsAK`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.02909",
  "prompt": "Show me the performance tables with baseline results. What are the zero-shot baseline numbers for RAMS2RAMS, RAMS2Wiki, and Wiki2Wiki? Are there any unadjusted LLM results reported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35483871-584f-4e22-870d-e563360c565d",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathUnaHTGaJcXK4TVhNk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6b7cdfbe-77eb-4425-b7c9-5a80f0d314e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013gGKmGVMiGFhdHmE6EZDTs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 22098,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 280,
          "cache_read_input_tokens": 22098,
          "cache_creation_input_tokens": 603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 603,
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

_source line 19 · 2026-05-10T10:04:20.253Z_

<details><summary>↩ Tool result · `toolu_01QVWjbMAixUXphG6Y4kv76h`</summary>

```text
I apologize, but the provided content appears to be a PDF file in binary format that hasn't been properly converted to readable text. The material shows PDF structure codes rather than the actual document content, making it impossible for me to extract the specific baseline results, F1 scores, or information about RAMS2RAMS, RAMS2Wiki, Wiki2Wiki comparisons, or LLM baseline performance.

To accurately report the zero-shot results and model comparisons you're asking about, I would need access to the paper's actual readable text content, particularly the results tables. Could you provide the document in a more accessible format, such as plain text or a properly extracted PDF?

[Binary content (application/pdf, 1MB) also saved to /home/ubuntu/.claude-account-1/projects/-/463e5fa5-38e0-4ede-baf8-cbc603cf470f/tool-results/webfetch-1778407457225-si4ev3.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35483871-584f-4e22-870d-e563360c565d",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "6c1ca6f9-b247-4cd7-a0bd-3b2634d9ca67",
  "sourceToolAssistantUUID": "35483871-584f-4e22-870d-e563360c565d",
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

_source line 20 · 2026-05-10T10:04:22.670Z_

<details><summary>↩ Tool result · `toolu_01GWdZkXgxAPSUPWCc6mPsAK`</summary>

```text
# Zero-Shot Baseline Performance Results

## Main Results Summary

Table 1 presents comprehensive baseline comparisons across three zero-shot settings:

**RAMS2RAMS:**
- Bart-Gen (strongest zero-shot baseline): 38.53 overall F1
- EEQA: 26.86 F1
- Distar: 18.98 F1

**RAMS2Wiki:**
- Bart-Gen: 28.52 overall F1
- EEQA: 18.24 F1
- Distar: 10.60 F1

**Wiki2Wiki:**
- Bart-Gen: 40.82 overall F1
- EEQA: 21.50 F1
- Distar: 17.51 F1

## LLM Results (Unadjusted)

The paper reports unadjusted LLM performance using both zero-shot and Chain-of-Thought prompting:

**Representative LLM performance (Wiki2Wiki):**
- GPT-4o: 11.36 F1 (zero-shot), 9.65 with CoT
- LLaMA-3.1 (70B): 10.55 F1 (zero-shot), 8.87 with CoT
- DeepSeek-R1: 12.84 F1 (zero-shot), 10.40 with CoT

The paper notes that "LLMs perform significantly worse in Span-F1" and struggle with "precise argument span" identification despite strong language understanding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b7cdfbe-77eb-4425-b7c9-5a80f0d314e4",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "38345e8f-0815-471b-91ef-4d735a13763f",
  "sourceToolAssistantUUID": "6b7cdfbe-77eb-4425-b7c9-5a80f0d314e4",
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

_source line 21 · 2026-05-10T10:04:24.181Z_

Excellent! Now let me search for more specific information about Qwen performance and any other recent LLM baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38345e8f-0815-471b-91ef-4d735a13763f",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathVMRj2uJbV7soCBo1t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d4d27d7-bac3-4e22-9c2c-d7331e785486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hn8bSpDqJHxnDPEthPJDxQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 22701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1029,
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

_source line 22 · 2026-05-10T10:04:24.636Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CkFD3DZXq5ZYDh9x7CL9fy`</summary>

```json
{
  "query": "Qwen2.5 LLaMA3.1 zero-shot event argument extraction RAMS WikiEvents performance F1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d4d27d7-bac3-4e22-9c2c-d7331e785486",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathVMRj2uJbV7soCBo1t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "407e3518-42a9-44ce-a4de-e6135c1becb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hn8bSpDqJHxnDPEthPJDxQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 22701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1029,
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

_source line 23 · 2026-05-10T10:04:24.944Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F73T6YSq5jEBjUDNabKWGp`</summary>

```json
{
  "query": "\"zero-shot\" \"event argument extraction\" RAMS 2025 2026 baseline LLM performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "407e3518-42a9-44ce-a4de-e6135c1becb2",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathVMRj2uJbV7soCBo1t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "62ff3bbf-e4a0-4cd6-8d1e-c6a9e58c02e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hn8bSpDqJHxnDPEthPJDxQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 22701,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1029
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 164,
          "cache_read_input_tokens": 22701,
          "cache_creation_input_tokens": 1029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1029,
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

_source line 24 · 2026-05-10T10:04:30.938Z_

<details><summary>↩ Tool result · `toolu_01CkFD3DZXq5ZYDh9x7CL9fy`</summary>

```text
Web search results for query: "Qwen2.5 LLaMA3.1 zero-shot event argument extraction RAMS WikiEvents performance F1"

Links: [{"title":"Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/html/2603.02909v2"},{"title":"One Small and One Large for Document-level Event Argument Extraction","url":"https://arxiv.org/html/2411.05895"},{"title":"Generating Uncontextualized and Contextualized Questions for Document-Level Event Argument Extraction","url":"https://arxiv.org/html/2404.04770"},{"title":"(Open Access) Document-Level Event Argument Extraction by Conditional Generation. (2021) | Sha Li | 3 Citations","url":"https://scispace.com/papers/document-level-event-argument-extraction-by-conditional-mfikfuamyh"},{"title":"A Multi-Format Transfer Learning Model for Event Argument Extraction","url":"https://arxiv.org/pdf/2208.13017"},{"title":"Table 4 from Context-Aware Prompt for Generation-based Event Argument Extraction with Diffusion Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Context-Aware-Prompt-for-Generation-based-Event-Luo-Xu/2ca83225b45f8ce3f5ed48df2a1494f7fdfd8058/figure/4"},{"title":"Textual Entailment for Event Argument Extraction: Zero- and Few-Shot with Multi-Source Learning | DeepAI","url":"https://deepai.org/publication/textual-entailment-for-event-argument-extraction-zero-and-few-shot-with-multi-source-learning"},{"title":"GitHub - hiyouga/LlamaFactory: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) · GitHub","url":"https://github.com/hiyouga/LlamaFactory"},{"title":"Closed-Domain Event Extraction Literature Review January 2025 v1.0","url":"https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf"},{"title":"arXiv:2205.00498v1 [cs.CL] 1 May 2022","url":"https://arxiv.org/pdf/2205.00498"}]

Based on the search results, I found relevant information about your query. Here are the key findings:

LLaMA3.1-8B and Qwen2.5-7B were selected as generation agents and fine-tuned via LoRA for parameter-efficient adaptation in a multi-agent collaboration framework for zero-shot document-level event argument extraction.

The LLaMA-based method exceeded the strongest baseline DEEIA by 6.57, 5.57, and 7.82 F1 on seen roles, unseen roles, and overall in RAMS2RAMS, and achieved the highest overall F1 scores of 32.38 and 46.96 in RAMS2Wiki and Wiki2Wiki settings.

The Wiki2Wiki setting follows the same protocol as RAMS2RAMS, where WikiEvents is split into seen and unseen event types.

The evaluation metrics used Span-F1 as the primary metric, where a prediction is correct only if the span exactly matches the gold span.

The method based on LLaMA and Qwen consistently outperforms existing DEAE models across all three zero-shot settings.

The research appears to be from a recent paper (March 2026) that specifically evaluates Qwen2.5 and LLaMA3.1 models for zero-shot event argument extraction on the RAMS and WikiEvents datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "407e3518-42a9-44ce-a4de-e6135c1becb2",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "ff336947-069f-474c-84fd-c3d6980d807d",
  "sourceToolAssistantUUID": "407e3518-42a9-44ce-a4de-e6135c1becb2",
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

_source line 25 · 2026-05-10T10:04:35.753Z_

<details><summary>↩ Tool result · `toolu_01F73T6YSq5jEBjUDNabKWGp`</summary>

```text
Web search results for query: ""zero-shot" "event argument extraction" RAMS 2025 2026 baseline LLM performance"

Links: [{"title":"Bi-directional feature learning-based approach for zero-shot event argument extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325001402"},{"title":"Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/html/2603.02909"},{"title":"Optimizing Low-Resource Zero-Shot Event Argument ...","url":"https://thesai.org/Downloads/Volume15No8/Paper_2-Optimizing_Low_Resource_Zero_Shot_Event_Argument.pdf"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for","url":"https://arxiv.org/pdf/2511.13118"},{"title":"Zero-shot event argument extraction by disentangling trigger from argument and role | International Journal of Machine Learning and Cybernetics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13042-024-02446-3"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction","url":"https://arxiv.org/html/2511.13118v1"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Event Argument Extraction with Enriched Prompts","url":"https://arxiv.org/html/2501.06825"},{"title":"Large Language Model Is Not a Good Few-shot ...","url":"https://aclanthology.org/2023.findings-emnlp.710.pdf"},{"title":"Large Language Models are Zero-Shot Reasoners Takeshi Kojima","url":"https://openreview.net/pdf?id=e2TBb5y0yFf"}]

Based on the search results, I found relevant information about zero-shot event argument extraction on the RAMS dataset and LLM performance:

## Key Findings

### BiTer Model Performance on RAMS
BiTer achieves state-of-the-art performance in the zero-shot setting on RAMS with an F1 improvement of 4.6% over the baseline model. The RAMS dataset consists of 9124 annotated events extracted from online news articles in English, covering 139 different types of events and 65 roles for arguments.

### LLM Baseline Performance
Recent research shows that LLMs perform significantly worse in Span-F1 measurements, with generally low performance levels, partly because strict boundary matching is required by Span-F1, and although LLMs demonstrate strong language understanding, they often struggle to accurately identify precise argument spans.

### Multi-Agent Collaboration Approaches
Methods based on LLaMA and Qwen consistently outperform existing DEAE models across zero-shot settings, achieving improvements in both data generation quality and argument extraction performance on the RAMS and WikiEvents datasets.

### Recent Advanced Methods (2025-2026)
A multi-agent framework (AEC) consistently achieves the best overall performance across all benchmarks, substantially outperforming competitive baselines, with gains of +7.8% and +6.0% on ACE 2005 with Llama3-8B in trigger identification and classification metrics.

The search results indicate that while baseline LLMs struggle with zero-shot event argument extraction, specialized approaches combining data generation, multi-agent decomposition, and schema-aware constraints significantly improve performance on the RAMS dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62ff3bbf-e4a0-4cd6-8d1e-c6a9e58c02e6",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "28e278b2-ade8-4417-a28c-7f57c2caff41",
  "sourceToolAssistantUUID": "62ff3bbf-e4a0-4cd6-8d1e-c6a9e58c02e6",
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

_source line 26 · 2026-05-10T10:04:37.064Z_

Let me fetch one more paper that directly compares small and large models on event extraction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28e278b2-ade8-4417-a28c-7f57c2caff41",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathWKNEQ9wwRMxtaQcfc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "74a3d420-7cb1-47a8-b735-7f27e7dc458a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R8XurD5Md5vB4GgEF4enTP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2081,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2081,
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

_source line 27 · 2026-05-10T10:04:37.669Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Da7Di3jEyybxb9on8c6VYb`</summary>

```json
{
  "url": "https://arxiv.org/html/2411.05895",
  "prompt": "What zero-shot baselines are reported? What is the performance of 8B models without fine-tuning on RAMS or WikiEvents? Report specific F1 scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74a3d420-7cb1-47a8-b735-7f27e7dc458a",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathWKNEQ9wwRMxtaQcfc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b4e6720b-a518-4ad2-8ea5-bac3b17cd081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R8XurD5Md5vB4GgEF4enTP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2081,
      "cache_read_input_tokens": 23730,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2081
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 137,
          "cache_read_input_tokens": 23730,
          "cache_creation_input_tokens": 2081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2081,
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

_source line 28 · 2026-05-10T10:04:42.396Z_

<details><summary>↩ Tool result · `toolu_01Da7Di3jEyybxb9on8c6VYb`</summary>

```text
# Zero-Shot Baselines and 8B Model Performance

## Zero-Shot Baselines Reported

The paper reports zero-shot performance using In-Context Learning (ICL) with large language models:

**On RAMS:**
- GPT-3.5: Arg-I 34.30, Arg-C 27.64
- GPT-4o-mini: Arg-I 35.47, Arg-C 30.04
- GPT-4o: Arg-I 41.58, Arg-C 35.70
- Llama3: Arg-I 23.05, Arg-C 18.79

**On WikiEvents:**
- GPT-3.5: Arg-I 18.12, Arg-C 16.04
- GPT-4o-mini: Arg-I 20.42, Arg-C 17.99
- GPT-4o: Arg-I 25.58, Arg-C 23.37
- Llama3: Arg-I 10.34, Arg-C 9.50

## 8B Models Without Fine-Tuning

For the 8B Llama3 base model without fine-tuning, the paper only reports ICL results (shown above). The authors note that "instruct-type models have shown relatively poor performance during ICL," with Llama3-Instruct achieving 0% F1 on both RAMS and WikiEvents under zero-shot conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4e6720b-a518-4ad2-8ea5-bac3b17cd081",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a7c514e05221cacf5",
  "type": "user",
  "uuid": "f7bef874-1534-48e8-a34c-c74c801941ab",
  "sourceToolAssistantUUID": "b4e6720b-a518-4ad2-8ea5-bac3b17cd081",
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

_source line 29 · 2026-05-10T10:04:56.241Z_

Perfect! Now I have enough information. Let me compile the findings.

## Summary: Zero-Shot Qwen3-8B and LLM Baselines for Event Argument Extraction

Based on my search across recent literature (2025-2026), here are my findings:

### 1. **Direct Qwen3-8B Zero-Shot Baseline**

I could **not find specific reported numbers for Qwen3-8B in zero-shot mode (no fine-tuning)** on RAMS or WikiEvents. However, the search results indicate:

- **Qwen2.5-7B has been used** in recent zero-shot EAE research (arXiv:2603.02909, March 2026), but these papers focus on Qwen2.5 **with LoRA fine-tuning**, not pure zero-shot.
- No papers appear to report pure zero-shot (unadjusted) Qwen3-8B results yet.

### 2. **Reported Zero-Shot LLM Baselines (Most Relevant)**

The **LtGaE paper (arXiv:2603.02909)** you referenced does include unadjusted LLM baselines **without fine-tuning**:

**Wiki2Wiki Setting (Span-F1):**
- GPT-4o: **11.36** (zero-shot), 9.65 with CoT
- LLaMA-3.1 (70B): **10.55** (zero-shot)
- DeepSeek-R1: **12.84** (zero-shot)

**Important note:** The paper mentions that "LLMs perform significantly worse in Span-F1" and struggle with precise argument span identification despite strong language understanding.

The other comprehensive baseline study (arXiv:2411.05895, November 2024) reported:

**RAMS Dataset (zero-shot ICL, Arg-Identification & Arg-Classification):**
- Llama3-Instruct: **0% F1** (completely fails)
- Llama3-base (non-instruct): Arg-I 23.05, Arg-C 18.79

**WikiEvents Dataset:**
- Llama3-base: Arg-I 10.34, Arg-C 9.50

### 3. **Papers with Zero-Shot EAE Baselines (2025-2026)**

Yes, **multiple recent papers include zero-shot LLM baselines:**

1. **LtGaE (2603.02909, March 2026)** — Direct LLM baselines with unadjusted results
2. **arXiv:2411.05895 (November 2024)** — Comprehensive GPT-3.5/GPT-4o/Llama3 zero-shot comparison
3. **arXiv:2501.06825** — "Event Argument Extraction with Enriched Prompts" (January 2025)
4. **arXiv:2511.13118** — "Extracting Events Like Code" (multi-agent framework, November 2025)
5. **Papers on "BiTer" approach and "SALE" (Structure-Aware Lightweight DEE)**

### 4. **Estimated Performance Range for Qwen3-8B Zero-Shot**

Based on the available data:

- **Conservative estimate (based on Llama3 Instruct failure):** 0-5% Span-F1
- **More realistic estimate (based on LLaMA-3.1-70B baseline):** 8-15% Span-F1 on RAMS/WikiEvents
- **If using base Llama3 as proxy:** ~10% Arg-Identification F1, ~18-20% for Arg-Classification

The dramatic gap between GPT-4o (11.36%) and Llama3 (10.55%) in the LtGaE paper suggests **8B instruction-tuned models like Qwen3 would likely fall in the 5-12% range** for Span-F1, depending on prompt engineering and instruction quality.

### 5. **Key Takeaway for Your Review**

**You have good motivation for a zero-shot baseline:** The LtGaE paper explicitly demonstrates that unadjusted LLM performance is very weak (10-12% Span-F1), and one study showed Llama3-Instruct achieving **0% F1** in zero-shot ICL mode. This makes a strong case that synthetic supervision via fine-tuning meaningfully improves over the raw model. The reviewer's request is reasonable and aligns with how recent papers report baselines.

---

Sources:
- [Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction (arXiv:2603.02909)](https://arxiv.org/abs/2603.02909)
- [One Small and One Large for Document-level Event Argument Extraction (arXiv:2411.05895)](https://arxiv.org/html/2411.05895)
- [Event Argument Extraction with Enriched Prompts (arXiv:2501.06825)](https://arxiv.org/abs/2501.06825)
- [Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction (arXiv:2511.13118)](https://arxiv.org/html/2511.13118v1)
- [Structure-Aware Lightweight Document-Level Event Extraction via Code-Based Large Language Models](https://www.mdpi.com/2079-9282/15/6/1187)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7bef874-1534-48e8-a34c-c74c801941ab",
  "isSidechain": true,
  "agentId": "a7c514e05221cacf5",
  "requestId": "req_011CathWom2wyzahNsq8nqQH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8544dc70-a856-470c-bdf0-f2ba7466724a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Zrw1gSmFMhEoigFFKBPfv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 25811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 500,
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
