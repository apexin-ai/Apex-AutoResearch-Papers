# Research conversation: Search for concurrent and recent work (2025-2026) on online schema adaptation for information extraction, test-time sche

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5ed62ae593f18051.jsonl`
- **Structured JSON:** [`b6ff4ea17d20f9d41c07.json`](../../sessions/b6/b6ff4ea17d20f9d41c07.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-10T06:56:29.800Z_

Search for concurrent and recent work (2025-2026) on online schema adaptation for information extraction, test-time schema refinement, and schema-domain mismatch detection. Use WebSearch for these queries:

1. "online schema adaptation information extraction 2026"
2. "test-time schema refinement information extraction LLM 2025 2026"
3. "schema mismatch detection named entity recognition feedback loop"
4. "arXiv schema optimization information extraction 2026"
5. Search OpenReview for ICML 2026 or NeurIPS 2026 submissions on schema adaptation IE

Report all relevant papers found including titles, venues, years, and brief descriptions of their approaches. Be specific about what each paper does vs what the proposed approach does.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "fdc9def7-7914-4046-bcb8-4552ac18f3b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T06:56:29.805Z_

```json
{
  "parentUuid": "fdc9def7-7914-4046-bcb8-4552ac18f3b0",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f48c785c-ab2e-424e-9228-9cae8977613d",
  "timestamp": "2026-05-10T06:56:29.805Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T06:56:31.803Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019VJ2fAuiyavwHuwpQ1kHPL`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f48c785c-ab2e-424e-9228-9cae8977613d",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTAPmTMdeCNpfJXSEFc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a667e25-6520-41e0-a81a-78d6999b19f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01X1KeUc3vQZpHe264Edku14",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8803,
      "cache_read_input_tokens": 0,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8803,
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

_source line 4 · 2026-05-10T06:56:31.808Z_

<details><summary>↩ Tool result · `toolu_019VJ2fAuiyavwHuwpQ1kHPL`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a667e25-6520-41e0-a81a-78d6999b19f7",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "512a9d57-5bd8-4c01-a705-ec3c28cd186d",
  "sourceToolAssistantUUID": "6a667e25-6520-41e0-a81a-78d6999b19f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T06:56:33.741Z_

I'll run all five searches in parallel to gather comprehensive results efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "512a9d57-5bd8-4c01-a705-ec3c28cd186d",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTAXwqZHbBYoigCKY7T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f796b33-c347-4770-96f1-e59dc21e1f2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017uvqrm5AfZa9h7YQaKa3Su",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-10T06:56:34.125Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cx1dw7Q2xaB14AMYbNFG6h`</summary>

```json
{
  "query": "online schema adaptation information extraction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f796b33-c347-4770-96f1-e59dc21e1f2c",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTAXwqZHbBYoigCKY7T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0adeef34-90bc-491e-820f-d3599c6197f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017uvqrm5AfZa9h7YQaKa3Su",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-10T06:56:34.922Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RD4mMAJSFmWEzZMTyA9C78`</summary>

```json
{
  "query": "test-time schema refinement information extraction LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0adeef34-90bc-491e-820f-d3599c6197f1",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTAXwqZHbBYoigCKY7T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "554a5ad8-45d1-4e8f-a0ec-0ed15bb248dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017uvqrm5AfZa9h7YQaKa3Su",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-10T06:56:35.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VfMzATR6pzP3XR85ywcADV`</summary>

```json
{
  "query": "schema mismatch detection named entity recognition feedback loop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "554a5ad8-45d1-4e8f-a0ec-0ed15bb248dd",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTAXwqZHbBYoigCKY7T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b88746d-6314-4adb-820b-46138f06daf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017uvqrm5AfZa9h7YQaKa3Su",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8803,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 169,
          "cache_read_input_tokens": 8803,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 9 · 2026-05-10T06:56:41.229Z_

<details><summary>↩ Tool result · `toolu_01Cx1dw7Q2xaB14AMYbNFG6h`</summary>

```text
Web search results for query: "online schema adaptation information extraction 2026"

Links: [{"title":"Paper page - ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images","url":"https://huggingface.co/papers/2602.12203"},{"title":"ExtractLabel: Schema-driven unstructured data extraction with Fabric AI Functions","url":"https://blog.fabric.microsoft.com/en-US/blog/extractlabel-schema-driven-unstructured-data-extraction-with-fabric-ai-functions/"},{"title":"OCR or Not? Rethinking Document Information Extraction in the MLLMs Era with Real-World Large-Scale Datasets - ACL Anthology","url":"https://aclanthology.org/2026.eacl-industry.28/"},{"title":"Schema as Parameterized Tools for Universal Information ...","url":"https://arxiv.org/pdf/2506.01276"},{"title":"LLMs for Structured Data Extraction from PDFs in 2026","url":"https://unstract.com/blog/comparing-approaches-for-using-llms-for-structured-data-extraction-from-pdfs/"},{"title":"Schema-Driven Information Extraction from Heterogeneous Tables","url":"https://arxiv.org/html/2305.14336v3"},{"title":"[2602.12203] ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images","url":"https://arxiv.org/abs/2602.12203"},{"title":"ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction","url":"https://arxiv.org/html/2602.15189"},{"title":"OCR or Not? Rethinking Document Information Extraction in the MLLMs Era with Real-World Large-Scale Datasets","url":"https://arxiv.org/html/2603.02789v1"},{"title":"Schema-Driven Information Extraction from Heterogeneous ...","url":"https://aclanthology.org/2024.findings-emnlp.600.pdf"}]

I've performed the web search for "online schema adaptation information extraction 2026". Here are the relevant findings:

## Key Research Areas

**Schema Adaptation Challenges:**
Current VLMs still struggle with schema adaptation, underspecified queries, and answer localization. ExStrucTiny introduces a new benchmark for structured information extraction from document images that unifies key entity extraction, relation extraction, and visual question answering across diverse input schemas and document types.

**Schema-Driven Extraction Approaches:**
ExtractLabel is a class in AI Functions library that lets you define a schema contract for what you want to extract, providing structured objects that match your specification instead of loose key-value pairs. Research demonstrates that carefully designed schema, exemplars, and instructions can further enhance MLLMs performance.

**Recent Benchmarks and Datasets:**
ScrapeGraphAI-100k is a large-scale, real-world dataset for LLM-based web extraction containing paired content, prompts, schemas, and model outputs, with schema-centric diagnostics to support failure analysis under increasing task complexity.

**Universal Information Extraction:**
A framework integrates three key components: schema retrieval, generation, and infilling, enabling adaptive and universal IE capabilities.

The search results show active research in 2026 on making information extraction systems more adaptive to schema variations, particularly using vision language models and large language models with structured output guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0adeef34-90bc-491e-820f-d3599c6197f1",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "0c4c503f-9b78-419a-9148-beb98a22b059",
  "sourceToolAssistantUUID": "0adeef34-90bc-491e-820f-d3599c6197f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T06:56:42.953Z_

<details><summary>↩ Tool result · `toolu_01VfMzATR6pzP3XR85ywcADV`</summary>

```text
Web search results for query: "schema mismatch detection named entity recognition feedback loop"

Links: [{"title":"Frontiers | Assessing named entity recognition by using geoscience domain schemas: the case of mineral systems","url":"https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2025.1530004/full"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"},{"title":"Improving Named Entity Recognition using Deep Learning with Human in the Loop","url":"https://openproceedings.org/2019/conf/edbt/EDBT19_paper_330.pdf"},{"title":"Named Entity Recognition (NER) — DeepPavlov 1.7.0 documentation","url":"http://docs.deeppavlov.ai/en/master/features/models/NER.html"},{"title":"Preparing data and designing a schema for custom named entity recognition (NER) - Azure AI services | Microsoft Learn","url":"https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-named-entity-recognition/how-to/design-schema"},{"title":"[2004.03287] A Corpus Study and Annotation Schema for Named Entity Recognition and Relation Extraction of Business Products","url":"https://arxiv.org/abs/2004.03287"},{"title":"Named Entity Recognition (NER): The Complete Guide for 2024","url":"https://vife.ai/blog/guide-to-named-entity-recognition-ner-models"},{"title":"User-in-the-Loop Named Entity Recognition by Counterfactual Learning Tong Yu","url":"https://neurips2021-nlp.github.io/papers/29/CameraReady/camera_User_in_the_Loop_Named_Entity_Recognition.pdf"},{"title":"Named Entity Recognition - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/named-entity-recognition/"},{"title":"AI Center - Custom Named Entity Recognition","url":"https://docs.uipath.com/ai-center/automation-cloud/latest/user-guide/custom-named-entity-recognition"}]

Based on the web search results, here's what I found regarding schema mismatch detection, named entity recognition, and feedback loops:

## Key Findings

### Feedback Loops in NER Systems

A continuous feedback loop, where domain experts validate and refine the model's outputs, can help improve its accuracy and reliability over time. This is particularly important in specialized domains like geosciences.

### Human-in-the-Loop Approaches

Based on user corrections, the NER model can learn and improve, and users can demand to incrementally update the pre-trained deep NER model or build a new one. For critical applications, implementing a workflow where low-confidence predictions are flagged for human review not only prevents errors but creates a feedback loop that creates new training data to improve the model over time.

### Schema-Related Challenges

Ambiguity happens when entity types selected are similar to each other, and the more ambiguous the schema, the more labeled data needed to differentiate between different entity types. Additionally, the importance of schema training data diversity in enhancing NER model performance has been highlighted.

### Selection Bias in Feedback Loops

An important technical challenge exists: Directly training on data collected from user feedback may be problematic due to a selection bias between distributions of displayed and non-displayed entities. Without handling non-displayed entities, the NER model updated over time may have a strong bias and inaccurate predictions, resulting in the NER model learning not being sample efficient and accurate over time.

These findings highlight the importance of well-designed schemas and careful consideration of bias when implementing feedback loops for NER systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b88746d-6314-4adb-820b-46138f06daf5",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "3fc3e7fe-468f-4302-8845-0e6246a08fab",
  "sourceToolAssistantUUID": "2b88746d-6314-4adb-820b-46138f06daf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T06:56:44.296Z_

<details><summary>↩ Tool result · `toolu_01RD4mMAJSFmWEzZMTyA9C78`</summary>

```text
Web search results for query: "test-time schema refinement information extraction LLM 2025 2026"

Links: [{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable ...","url":"https://aclanthology.org/2025.emnlp-industry.184.pdf"},{"title":"Structured data extraction from unstructured content using LLM schemas","url":"https://simonwillison.net/2025/Feb/28/llm-schemas/"},{"title":"SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema","url":"https://arxiv.org/html/2512.12337"},{"title":"[2510.08623] PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/abs/2510.08623"},{"title":"StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs","url":"https://arxiv.org/html/2505.20139v1"},{"title":"PARSE: LLM driven schema optimization for reliable entity extraction - Amazon Science","url":"https://www.amazon.science/publications/parse-llm-driven-schema-optimization-for-reliable-entity-extraction"},{"title":"Large language model driven transferable key information extraction mechanism for nonstandardized tables | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-15627-z"},{"title":"Structured Outputs: Reliable Schema-Validated Data Extraction from Language Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/structured-outputs-schema-validated-data-extraction-language-models"}]

I found comprehensive information about test-time schema refinement for information extraction with LLMs in 2025-2026. Here are the key findings:

## Key Research Areas

**PARSE Framework (October 2025)**: PARSE is a novel system with two synergistic components: ARCHITECT, which autonomously optimizes JSON schemas for LLM consumption while maintaining backward compatibility through RELAY (an integrated code generation system), and SCOPE, which implements reflection-based extraction with combined static and LLM-based guardrails. The system achieves up to 64.7% improvement in extraction accuracy on SWDE with combined framework improvements reaching 10% across models, while reducing extraction errors by 92% within the first retry.

**SCIR Framework (December 2025)**: The SCIR framework enhances extraction quality through iterative refinement, consisting of four core components: (1) an information extraction module, (2) an iterative pruning module, (3) a dual-path self-correcting module, and (4) a feedback-driven optimization module, operating in a synergistic pipeline to progressively improve extraction results through coordinated interactions.

**SLOT Framework (November 2025)**: SLOT addresses limitations by decoupling output formatting from the natural language task, offering a model-agnostic solution.

## Core Challenges & Solutions

Self-correction techniques enhance LLM reliability through Chain-of-Thought reasoning, self-verification, and iterative refinement mechanisms. The Feedback-Driven Optimization module implements a closed-loop refinement system by injecting detection results into adaptive prompts, with three diagnostic feedback streams generating specialized prompts: Redundancy Prompt, Missing Prompt, and FormatError Prompt.

## Structured Output Evaluation

Evaluating structured output has become a focal point for understanding LLM's limitations. Recent work includes benchmarking frameworks like StructEval and others to assess LLMs' capabilities across various structured output formats.

These approaches represent the state-of-the-art in test-time schema refinement for information extraction using large language models in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "554a5ad8-45d1-4e8f-a0ec-0ed15bb248dd",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "611a384e-9747-4cf5-bc6a-c2f43d21b09f",
  "sourceToolAssistantUUID": "554a5ad8-45d1-4e8f-a0ec-0ed15bb248dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T06:56:48.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WaRnVAPosh3CgLciH6iirt`</summary>

```json
{
  "query": "arXiv schema optimization information extraction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "611a384e-9747-4cf5-bc6a-c2f43d21b09f",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTBT2wYwmvnVvRWkNQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31470805-518b-4b7e-b674-4bde26c2d806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LproJSSih2aQojmkwzZhLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 2045,
      "cache_read_input_tokens": 10195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2045,
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

_source line 13 · 2026-05-10T06:56:48.789Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QqPraPPbvCzjr9ZFu9NsGS`</summary>

```json
{
  "query": "site:openreview.net schema adaptation information extraction ICML NeurIPS 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31470805-518b-4b7e-b674-4bde26c2d806",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTBT2wYwmvnVvRWkNQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e977efe-3326-4d26-b5be-fbb59ad2dc8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LproJSSih2aQojmkwzZhLf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 2045,
      "cache_read_input_tokens": 10195,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2045
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 931,
          "output_tokens": 116,
          "cache_read_input_tokens": 10195,
          "cache_creation_input_tokens": 2045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2045,
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

_source line 14 · 2026-05-10T06:56:54.180Z_

<details><summary>↩ Tool result · `toolu_01QqPraPPbvCzjr9ZFu9NsGS`</summary>

```text
Web search results for query: "site:openreview.net schema adaptation information extraction ICML NeurIPS 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=KR1PsFVRYo"},{"title":"ICML 2026 | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026"},{"title":"NeurIPS 2026 | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026"},{"title":"2nd DeLTa Workshop Proposal @ ICLR 2026","url":"https://openreview.net/pdf?id=hTFpY3Nc8s"},{"title":"ICLR 2026 Workshop on Representational Alignment (Re4-Align)","url":"https://openreview.net/pdf?id=7tNhq0H39L"},{"title":"Principled Design for Trustworthy AI:","url":"https://openreview.net/pdf?id=6RfpxuxqYu"},{"title":"ICLR 2026 Workshop on AI with Recursive Self-Improvement 1 Workshop Summary","url":"https://openreview.net/pdf?id=OsPQ6zTQXV"},{"title":"AI&PDE: ICLR 2026 WORKSHOP ON AI AND PARTIAL","url":"https://openreview.net/pdf?id=med7qzMIaG"},{"title":"NeurIPS 2026 Evaluations and Datasets Track | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FEvaluations_and_Datasets_Track"},{"title":"Time Series Workshop NeurIPS 2025","url":"https://openreview.net/pdf?id=dN9Sxy675T"}]

Based on the web search results from OpenReview, I found several workshop proposals and papers from ICML 2026 and NeurIPS 2026, though the search didn't return specific results specifically matching "schema adaptation information extraction" on OpenReview.

The search revealed various ICLR 2026 and related 2026 workshops on OpenReview, including:

- A World Model Workshop proposal at ICLR 2026
- An AI with Recursive Self-Improvement workshop at ICLR 2026
- A workshop on Representational Alignment (Re4-Align) at ICLR 2026
- An AI&PDE workshop at ICLR 2026
- A Trustworthy AI workshop proposal
- A Time Series workshop at ICLR 2026
- General OpenReview pages for ICML 2026 and NeurIPS 2026

However, the specific query about "schema adaptation information extraction" doesn't appear in these results. The search results show various workshops and papers across ICML, NeurIPS, and ICLR 2026, but none specifically focused on the schema adaptation and information extraction topic you're looking for.

If you're looking for papers on schema adaptation or information extraction specifically, you may want to try refining your search with different keywords or checking the main conference submissions directly on OpenReview rather than using the site-specific search operator.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e977efe-3326-4d26-b5be-fbb59ad2dc8c",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "b67ae2c4-cff8-4492-8840-ba310f5a0879",
  "sourceToolAssistantUUID": "8e977efe-3326-4d26-b5be-fbb59ad2dc8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T06:57:00.650Z_

<details><summary>↩ Tool result · `toolu_01WaRnVAPosh3CgLciH6iirt`</summary>

```text
Web search results for query: "arXiv schema optimization information extraction 2026"

Links: [{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"[2510.08623] PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/abs/2510.08623"},{"title":"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/html/2505.14992v1"},{"title":"SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema","url":"https://arxiv.org/html/2512.12337"},{"title":"[2505.14992v1] Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/abs/2505.14992v1"},{"title":"OCR or Not? Rethinking Document Information Extraction in the MLLMs Era with Real-World Large-Scale Datasets","url":"https://arxiv.org/html/2603.02789v1"},{"title":"Schema-Driven Information Extraction from Heterogeneous Tables","url":"https://arxiv.org/html/2305.14336v3"},{"title":"[2604.06571v1] LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources","url":"https://arxiv.org/abs/2604.06571v1"},{"title":"[2603.02789] OCR or Not? Rethinking Document Information Extraction in the MLLMs Era with Real-World Large-Scale Datasets","url":"https://arxiv.org/abs/2603.02789"},{"title":"ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction","url":"https://arxiv.org/html/2602.12247v2"}]

Based on the search results, here are some recent arXiv papers on schema optimization and information extraction from 2026:

## Key Papers Found:

**1. PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction**
PARSE introduces ARCHITECT, an automated schema optimization framework that iteratively refines JSON schemas for LLM consumption by analyzing extraction performance, adding detailed entity descriptions and validation rules, and restructuring schemas for clearer representation. The framework achieves up to 64.7% improvement in extraction accuracy compared to state-of-the-art baselines on SWDE.

**2. DLISC: Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models**
DLISC is a two-stage information extraction approach adapted for on-device LLMs that adopts an Identification LoRA module for retrieving the most relevant schemas to a given query, and an Extraction LoRA module for performing information extraction based on the previously selected schemas.

**3. SCIR: A Self-Correcting Iterative Refinement Framework**
SCIR proposes a fine-tuning-free IE paradigm that achieves exceptional generalization via integrating Dual-Path Self-Correcting and Feedback-Driven Optimization mechanisms.

**4. OCR or Not? Rethinking Document Information Extraction in the MLLMs Era**
The research demonstrates that carefully designed schema, exemplars, and instructions can further enhance MLLMs performance.

**5. ExtractBench: A Benchmark for Complex Structured Extraction**
ExtractBench is an open-source benchmark and evaluation framework for PDF-to-JSON structured extraction that pairs 35 PDF documents with JSON Schemas and human-annotated gold labels.

These papers represent recent advances in making schema-based information extraction more efficient, reliable, and suitable for large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31470805-518b-4b7e-b674-4bde26c2d806",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "5e57d6ef-1b3d-4e06-9758-ac0313e138c1",
  "sourceToolAssistantUUID": "31470805-518b-4b7e-b674-4bde26c2d806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T06:57:05.054Z_

Now let me do a few deeper follow-up searches to get more detail on the most relevant papers found, and probe OpenReview more specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e57d6ef-1b3d-4e06-9758-ac0313e138c1",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTCf8VT6NTvQUwfiKcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af227b70-2dbe-429c-a1c2-451e8674f3a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NYJrAwLToKrSFpwkQQbKun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 12240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
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

_source line 17 · 2026-05-10T06:57:05.961Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ECJfXmeY7VE6KEvQJRhYdU`</summary>

```json
{
  "query": "SCIR self-correcting iterative refinement information extraction schema feedback 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af227b70-2dbe-429c-a1c2-451e8674f3a1",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTCf8VT6NTvQUwfiKcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fca5cbd-4a21-4d2f-b8c9-863ddc63469d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NYJrAwLToKrSFpwkQQbKun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 12240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
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

_source line 18 · 2026-05-10T06:57:07.110Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016RZ5o2SdLhZJtAZGmzVLsJ`</summary>

```json
{
  "query": "schema-variable structured extraction domain shift adaptation LLM 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fca5cbd-4a21-4d2f-b8c9-863ddc63469d",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTCf8VT6NTvQUwfiKcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2a988f6-7fa2-4902-abfb-2ead5b39197f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NYJrAwLToKrSFpwkQQbKun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 12240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
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

_source line 19 · 2026-05-10T06:57:07.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SKo9gftsPaawJbUBm4zyAH`</summary>

```json
{
  "query": "openreview ICML 2026 information extraction schema test time adaptation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2a988f6-7fa2-4902-abfb-2ead5b39197f",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTCf8VT6NTvQUwfiKcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06c1d8e1-9c60-4b69-8ebc-247db0d04040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NYJrAwLToKrSFpwkQQbKun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 12240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
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

_source line 20 · 2026-05-10T06:57:12.310Z_

<details><summary>↩ Tool result · `toolu_01SKo9gftsPaawJbUBm4zyAH`</summary>

```text
Web search results for query: "openreview ICML 2026 information extraction schema test time adaptation"

Links: [{"title":"ICML 2026 | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026"},{"title":"ICML 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FConference"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"ICML 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop"},{"title":"ICML 2026 – ICML Blog","url":"https://blog.icml.cc/category/icml-2026/"},{"title":"Test Time Adaptation Using Adaptive Quantile Recalibration | OpenReview","url":"https://openreview.net/forum?id=vaYroILsQj"},{"title":"ICML 2026 Workshop Forecast | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FForecast"},{"title":"ICML | OpenReview","url":"https://openreview.net/group?id=ICML.cc"},{"title":"ICML 2026 Workshop SCALE | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FSCALE"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"}]

The search results show information about ICML 2026 on OpenReview, along with various related papers and workshops. However, the results don't contain specific information about a paper on "information extraction schema test time adaptation" at ICML 2026.

The search returned:

- The OpenReview homepage for ICML 2026 Conference
- Information about various ICML 2026 workshops including Foundation Models for Structured Data (FMSD @ ICML 2026)
- A paper on test-time adaptation (though from ICML 2025, not 2026)

If you're looking for a specific paper on information extraction schema adaptation, you may want to:
1. Visit the ICML 2026 Conference page directly on OpenReview (openreview.net/group?id=ICML.cc/2026/Conference)
2. Use the OpenReview search functionality with more specific paper titles or author names
3. Check if the paper has been accepted and published yet, as not all submissions may be available in the search results

Would you like me to search with different keywords or help you find something more specific?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c1d8e1-9c60-4b69-8ebc-247db0d04040",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "a1c083ae-f7b4-4998-9a88-2f8d1822bffa",
  "sourceToolAssistantUUID": "06c1d8e1-9c60-4b69-8ebc-247db0d04040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T06:57:13.096Z_

<details><summary>↩ Tool result · `toolu_01ECJfXmeY7VE6KEvQJRhYdU`</summary>

```text
Web search results for query: "SCIR self-correcting iterative refinement information extraction schema feedback 2025 arXiv"

Links: [{"title":"[2512.12337] SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema","url":"https://arxiv.org/abs/2512.12337"},{"title":"SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced","url":"https://www.arxiv.org/pdf/2512.12337"},{"title":"SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema","url":"https://arxiv.org/html/2512.12337"},{"title":"SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40326"},{"title":"(PDF) SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema","url":"https://www.researchgate.net/publication/398720721_SCIR_A_Self-Correcting_Iterative_Refinement_Framework_for_Enhanced_Information_Extraction_Based_on_Schema"},{"title":"Improving the Robustness of Large Language Models in ...","url":"https://assets-eu.researchsquare.com/files/rs-6255894/v1_covered_d497b03f-a7a3-4240-84b4-dacfd2ec22a8.pdf"},{"title":"SELF-REFINE: Iterative Refinement with Self-Feedback","url":"https://openreview.net/pdf?id=S37hOerQLB"},{"title":"Notebook for the CheckThat! Lab at CLEF 2025","url":"https://ceur-ws.org/Vol-4038/paper_92.pdf"},{"title":"Self-Reﬁnement Strategies for LLM-based Product Attribute Value Extraction","url":"https://madoc.bib.uni-mannheim.de/70816/1/BTW2025-132.pdf"},{"title":"Exploring LLMs for Scientific Information Extraction using the SciEx Framework","url":"https://arxiv.org/pdf/2512.10004"}]

I found information about the SCIR paper. Here are the key findings:

## SCIR: Self-Correcting Iterative Refinement Framework

The Self-Correcting Iterative Refinement (SCIR) framework is a novel universal IE paradigm accompanied by a Multi-task Bilingual (Chinese-English) Self-Correcting (MBSC) dataset containing over 100,000 entries.

### Framework Architecture and Design

The architecture consists of four core components: (1) an information extraction module, (2) an iterative pruning module, (3) a dual-path self-correcting module, and (4) a feedback-driven optimization module.

### Key Features

The SCIR framework achieves plug-and-play compatibility with existing LLMs and IE systems through its Dual-Path Self-Correcting module and feedback-driven optimization, thereby significantly reducing training costs.

The Dual-Path Self-Correcting mechanism verifies the completeness of extraction results through two pathways: redundancy detection and missing detection. The Feedback-Driven Optimization mechanism generates iterative prompts based on verification results to drive a context-learning-based iterative generation process.

### Performance Results

Through comprehensive zero-shot transfer evaluations across 11 multilingual benchmarks, SCIR demonstrates outstanding effectiveness with an 5.27% average F1-score increase, underscoring its potential to revolutionize IE by providing a plug-and-play solution that cuts training costs while maintaining high performance.

The paper was published on arXiv on December 13, 2025 (arXiv:2512.12337) and has also been published in the AAAI-26 conference proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fca5cbd-4a21-4d2f-b8c9-863ddc63469d",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "9aa36554-e11d-406d-822a-dda5777843a6",
  "sourceToolAssistantUUID": "1fca5cbd-4a21-4d2f-b8c9-863ddc63469d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T06:57:17.207Z_

<details><summary>↩ Tool result · `toolu_016RZ5o2SdLhZJtAZGmzVLsJ`</summary>

```text
Web search results for query: "schema-variable structured extraction domain shift adaptation LLM 2025 2026 arXiv"

Links: [{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"EXSTRUCTINY: A Benchmark for Schema-Variable Structured Information Extraction","url":"https://arxiv.org/pdf/2602.12203"},{"title":"ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images","url":"https://arxiv.org/html/2602.12203v1"},{"title":"[2510.08623] PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/abs/2510.08623"},{"title":"ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction","url":"https://arxiv.org/html/2602.15189v1"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/html/2510.20345v1"},{"title":"Tackling Distribution Shift in LLM via KILO","url":"https://arxiv.org/pdf/2508.03571"},{"title":"arXiv:2505.18458v3 [cs.DB] 1 Jun 2025 1 A Survey of LLM × DATA","url":"https://arxiv.org/pdf/2505.18458"},{"title":"Structured Outputs: Reliable Schema-Validated Data Extraction from Language Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/structured-outputs-schema-validated-data-extraction-language-models"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"}]

I've completed the web search for your query about schema-variable structured extraction, domain shift adaptation, and LLMs from 2025-2026 arXiv papers. Here are the key findings:

## Main Results:

**ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction** (February 2026)
ExStrucTiny mathematically formalizes the structured extraction task to highlight its distinction from traditional KEE, RE, and VQA in VRDU. Most efforts in this direction produce only single-span extractive questions restricted by the fixed schema of the source datasets, making them fail to capture the complexity and diversity of real-world extractive queries.

**PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction** (October 2025)
Current approaches apply large language models directly to extraction tasks using existing JSON schemas, often with constraint decoding or reinforcement learning approaches to ensure syntactic validity, but treat JSON schemas as static contracts designed for human developers, leading to suboptimal extraction performance, frequent hallucinations, and unreliable agent behavior when schemas contain ambiguous or incomplete specifications. PARSE achieves up to 64.7% improvement in extraction accuracy on SWDE with combined framework improvements reaching 10% across models, while reducing extraction errors by 92% within the first retry.

**ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction** (February 2026)
ScrapeGraphAI-100k provides a standardized testbed for evaluating extraction robustness across varying task complexity, and the rich structural metadata enables stratified evaluation showing empirical breakpoints where systems fail, such as when schema depth exceeds 7 levels or key count surpasses 200.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2a988f6-7fa2-4902-abfb-2ead5b39197f",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "5d9ee707-7d5d-49a1-a4d7-0123bc34150a",
  "sourceToolAssistantUUID": "f2a988f6-7fa2-4902-abfb-2ead5b39197f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T06:57:19.345Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ppMsdvL5s87UkAsJz7VbD`</summary>

```json
{
  "query": "\"schema as parameterized tools\" universal information extraction arXiv 2506"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d9ee707-7d5d-49a1-a4d7-0123bc34150a",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTDsm2jz2VRFKLurysB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "108a7fc4-caac-43ab-bb56-d0ebf2b28094",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016qiSn9SZMtaXRqAMgNNyqx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 774,
      "cache_creation_input_tokens": 3016,
      "cache_read_input_tokens": 14244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3016,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T06:57:20.145Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K7vByiBse6qX6DwsoMQtSY`</summary>

```json
{
  "query": "ExStrucTiny schema-variable structured information extraction document images 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "108a7fc4-caac-43ab-bb56-d0ebf2b28094",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTDsm2jz2VRFKLurysB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "033ba7f8-f612-485b-9f4f-aacf03ae7cf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016qiSn9SZMtaXRqAMgNNyqx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 774,
      "cache_creation_input_tokens": 3016,
      "cache_read_input_tokens": 14244,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3016
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 774,
          "output_tokens": 118,
          "cache_read_input_tokens": 14244,
          "cache_creation_input_tokens": 3016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3016,
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

_source line 25 · 2026-05-10T06:57:25.876Z_

<details><summary>↩ Tool result · `toolu_017ppMsdvL5s87UkAsJz7VbD`</summary>

```text
Web search results for query: ""schema as parameterized tools" universal information extraction arXiv 2506"

Links: [{"title":"[2506.01276] Schema as Parameterized Tools for Universal Information Extraction","url":"https://arxiv.org/abs/2506.01276"},{"title":"Schema as Parameterized Tools for Universal Information Extraction","url":"https://arxiv.org/html/2506.01276v1"},{"title":"Schema as Parameterized Tools for Universal Information ...","url":"https://arxiv.org/pdf/2506.01276"},{"title":"Schema as Parameterized Tools for Universal Information Extraction | OpenReview","url":"https://openreview.net/forum?id=yoPtjKVtoX"},{"title":"Schema as Parameterized Tools for Universal Information Extraction","url":"https://openreview.net/pdf?id=yoPtjKVtoX"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction","url":"https://arxiv.org/html/2403.07969v2"},{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/abs/2301.03282"},{"title":"From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction","url":"https://arxiv.org/html/2604.27906"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"[Literature Review] Schema as Parameterized Tools for Universal Information Extraction","url":"https://www.themoonlight.io/en/review/schema-as-parameterized-tools-for-universal-information-extraction"}]

I found the paper you were looking for! Here are the key details:

## Schema as Parameterized Tools for Universal Information Extraction

The paper proposes a unified adaptive text-to-structure generation framework, called Schema as Parameterized Tools (SPT), which reimagines the tool-calling capability of LLMs by treating predefined schemas as parameterized tools for tool selection and parameter filling.

**Background Problem:**
Universal information extraction (UIE) primarily employs an extractive generation approach with large language models (LLMs), typically outputting structured information based on predefined schemas such as JSON or tables. UIE suffers from a lack of adaptability when selecting between predefined schemas and on-the-fly schema generation within the in-context learning paradigm, especially when there are numerous schemas to choose from.

**Key Approach:**
The SPT method can be applied to unify closed, open, and on-demand IE tasks by adopting Schema Retrieval by fetching the relevant schemas from a predefined pool, Schema Filling by extracting information and filling slots as with tool parameters, or Schema Generation by synthesizing new schemas with uncovered cases.

**Results:**
Experiments show that the SPT method can handle four distinct IE tasks adaptively, delivering robust schema retrieval and selection performance. SPT also achieves comparable extraction performance to LoRA baselines and current leading UIE systems with significantly fewer trainable parameters.

**Paper Details:** arXiv:2506.01276, published June 2, 2025


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "108a7fc4-caac-43ab-bb56-d0ebf2b28094",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "f99bf26f-3f4d-43c9-b8bc-47b08b37499d",
  "sourceToolAssistantUUID": "108a7fc4-caac-43ab-bb56-d0ebf2b28094",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T06:57:27.024Z_

<details><summary>↩ Tool result · `toolu_01K7vByiBse6qX6DwsoMQtSY`</summary>

```text
Web search results for query: "ExStrucTiny schema-variable structured information extraction document images 2026"

Links: [{"title":"[2602.12203] ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images","url":"https://arxiv.org/abs/2602.12203"},{"title":"ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images","url":"https://arxiv.org/html/2602.12203"},{"title":"ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.265/"},{"title":"(PDF) ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images","url":"https://www.researchgate.net/publication/400741599_ExStrucTiny_A_Benchmark_for_Schema-Variable_Structured_Information_Extraction_from_Document_Images"},{"title":"Paper page - ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images","url":"https://huggingface.co/papers/2602.12203"},{"title":"EXSTRUCTINY: A Benchmark for Schema-Variable Structured Information Extraction","url":"https://arxiv.org/pdf/2602.12203"},{"title":"EXSTRUCTINY Synthetic Data Generation Pipeline | Download Scientific Diagram","url":"https://www.researchgate.net/figure/EXSTRUCTINY-Synthetic-Data-Generation-Pipeline_fig3_400741599"},{"title":"An overview of the SAFEPASSAGE pipeline. A generative language model... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/An-overview-of-the-SAFEPASSAGE-pipeline-A-generative-language-model-generates-a-list-of_fig1_396094099"},{"title":"\"Daily Huggingface Papers!\" ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images - 2026-02-12 (Podcast Episode) - IMDb","url":"https://www.imdb.com/title/tt39997814/"},{"title":"Crops from three sample documents demonstrating the challenges of the... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Crops-from-three-sample-documents-demonstrating-the-challenges-of-the-dataset-with_fig1_397457617"}]

Based on the search results, here's what I found about ExStrucTiny:

## Overview

ExStrucTiny is a new structured IE benchmark dataset from document images, comprising 304 closed and on-demand IE query-answer pairs and spanning 110 multi-page documents.

## Purpose and Scope

ExStrucTiny is a new benchmark dataset for structured Information Extraction (IE) from document images, unifying aspects of KEE, RE, and VQA. Although generalist Vision Language Models (VLMs) perform well on established document understanding benchmarks, their ability to conduct holistic, fine-grained structured extraction across diverse document types and flexible schemas is not well studied, as existing Key Entity Extraction (KEE), Relation Extraction (RE), and Visual Question Answering (VQA) datasets are limited by narrow entity ontologies, simple queries, or homogeneous document types.

## Construction and Methodology

Built through a novel pipeline combining manual plus synthetic human-validated samples, ExStrucTiny covers more varied document types and extraction scenarios, and is constructed through a novel pipeline combining manual annotations and LLM-generated, human-validated samples across forms, financial reports, slide decks, and webpage screenshots.

## Key Challenges Identified

The analysis of open and closed VLMs on this benchmark highlights challenges such as schema adaptation, query under-specification, and answer localization.

The paper was published in February 2026 and appears in the proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "033ba7f8-f612-485b-9f4f-aacf03ae7cf2",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "fd6616ce-8e4d-4784-8827-31d63ff32914",
  "sourceToolAssistantUUID": "033ba7f8-f612-485b-9f4f-aacf03ae7cf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T06:57:30.261Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KbQ1DfQqoms4ZmLtMKUrPE`</summary>

```json
{
  "query": "DLISC on-device schema-aware information extraction LoRA identification extraction modules 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd6616ce-8e4d-4784-8827-31d63ff32914",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTEbprnBBpPTGdYsd88",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "521a4813-ae0f-4730-b4d6-48df5f091d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GK6Bja7CaxczYckRGXuSxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2727,
      "cache_read_input_tokens": 17260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2727,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-10T06:57:30.927Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PRq1Jbh1v2NuRrsNAWCt3t`</summary>

```json
{
  "query": "\"schema-guided\" OR \"schema-grounded\" information extraction iterative refinement feedback 2025 2026 NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "521a4813-ae0f-4730-b4d6-48df5f091d0e",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTEbprnBBpPTGdYsd88",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23729526-b144-4607-9437-a5eaee1a4b64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GK6Bja7CaxczYckRGXuSxx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2727,
      "cache_read_input_tokens": 17260,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2727
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 17260,
          "cache_creation_input_tokens": 2727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2727,
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

_source line 29 · 2026-05-10T06:57:35.975Z_

<details><summary>↩ Tool result · `toolu_01KbQ1DfQqoms4ZmLtMKUrPE`</summary>

```text
Web search results for query: "DLISC on-device schema-aware information extraction LoRA identification extraction modules 2025"

Links: [{"title":"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/html/2505.14992v1"},{"title":"[2505.14992v1] Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/abs/2505.14992v1"},{"title":"[2505.14992] Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/abs/2505.14992"},{"title":"Effective and Efficient Schema-aware Information ...","url":"https://www.arxiv.org/pdf/2505.14992"},{"title":"Effective and Efficient Schema-aware Information Extraction Using","url":"https://openreview.net/pdf?id=lW7nJDWWz4"},{"title":"The characteristics of DL models in different IE tasks. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-characteristics-of-DL-models-in-different-IE-tasks_tbl2_363894835"},{"title":"Mixture of LoRA Experts for Continual Information ...","url":"https://aclanthology.org/2025.findings-emnlp.718.pdf"},{"title":"Physical layer identification of LoRa devices using constellation trace figure | EURASIP Journal on Wireless Communications and Networking | Full Text","url":"https://jwcn-eurasipjournals.springeropen.com/articles/10.1186/s13638-019-1542-x"},{"title":"A Comprehensive Survey on Deep Learning-Based LoRa Radio Frequency Fingerprinting Identification - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11244599/"},{"title":"StolenLoRA: Exploring LoRA Extraction Attacks via Synthetic ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_StolenLoRA_Exploring_LoRA_Extraction_Attacks_via_Synthetic_Data_ICCV_2025_paper.pdf"}]

Based on the search results, here's what I found about DLISC:

DLISC (Dual-LoRA with Incremental Schema Caching) is a two-stage information extraction approach adapted for on-device LLMs. 

The architecture of DLISC includes an Identification LoRA for identifying the most relevant schemas to the query, an Extraction LoRA for performing the information extraction with the matched schemas, and Incremental Schema Caching for accelerating the extraction inference.

DLISC adopts an Identification LoRA module for retrieving the most relevant schemas to a given query, and an Extraction LoRA module for performing information extraction based on the previously selected schemas.

The key benefits of DLISC include:
- By decomposing the information extraction task into two stages—Identification and Extraction—the multi-LoRA structure of on-device LLMs can be fully leveraged to optimize each stage separately, thereby improving overall extraction performance
- By incrementally caching previously inferenced schemas, redundant calculations can be avoided, thereby boosting the extraction inference efficiency

Extensive experiments across multiple information extraction datasets demonstrate notable improvements in both effectiveness and efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "521a4813-ae0f-4730-b4d6-48df5f091d0e",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "6a0af9ea-f85a-4f01-b56f-e448e6881148",
  "sourceToolAssistantUUID": "521a4813-ae0f-4730-b4d6-48df5f091d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T06:57:38.806Z_

<details><summary>↩ Tool result · `toolu_01PRq1Jbh1v2NuRrsNAWCt3t`</summary>

```text
Web search results for query: ""schema-guided" OR "schema-grounded" information extraction iterative refinement feedback 2025 2026 NLP"

Links: [{"title":"SCHEMA-MINERpro: Agentic AI for Ontology Grounding over","url":"https://www.semantic-web-journal.net/system/files/swj3871.pdf"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable ...","url":"https://aclanthology.org/2025.emnlp-industry.184.pdf"},{"title":"Exploring LLMs for Scientific Information Extraction using the SciEx Framework","url":"https://arxiv.org/pdf/2512.10004"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"Schema-Driven Information Extraction from Heterogeneous Tables","url":"https://arxiv.org/html/2305.14336v3"},{"title":"LOGOS: LLM-DRIVEN END-TO-END GROUNDED THEORY DEVELOPMENT AND SCHEMA INDUCTION","url":"https://arxiv.org/pdf/2509.24294"},{"title":"Structured Extraction from Business Process Diagrams Using","url":"https://arxiv.org/pdf/2511.22448"},{"title":"SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40326"},{"title":"LOGOS: LLM-Driven End-to-End Grounded Theory Development and Schema Induction For Qualitative Reseach | OpenReview","url":"https://openreview.net/forum?id=ZJn0TMTy8C"},{"title":"SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced","url":"https://www.arxiv.org/pdf/2512.12337"}]

I found several recent papers and systems (2025-2026) on schema-guided/schema-grounded information extraction with iterative refinement and feedback mechanisms. Here are the key findings:

## Recent Systems and Frameworks

**PARSE (2025)**: A framework with ARCHITECT for schema refinement and SCOPE for extraction, which processes unoptimized schemas through iterative optimization.

**SCIR (2026)**: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema, published at AAAI-26. It performs preliminary information extraction on raw text using basic instruction templates, while subsequent iterations dynamically refine results through optimized prompts filtered by the detection module.

**SciEx Framework (2025)**: This uses a closed-loop retrieval–extraction–verification cycle that continues until convergence is achieved, ensuring that final outputs are both semantically consistent and empirically grounded in the retrieved evidence.

**LOGOS (2025-2026)**: An end-to-end framework that integrates LLM-driven coding, semantic clustering, graph reasoning, and a novel iterative refinement process to build highly reusable codebooks.

## Iterative Refinement Approaches

Feedback is provided in descriptive and direct-edit modes and is incorporated into iterative runs, with measurable impact on output quality in schema-guided systems. Self-correction techniques enhance LLM reliability through Chain-of-Thought reasoning, self-verification, and iterative refinement mechanisms.

The search results reveal a clear trend toward human-in-the-loop and automated iterative refinement approaches for schema-based information extraction in NLP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23729526-b144-4607-9437-a5eaee1a4b64",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a5ed62ae593f18051",
  "type": "user",
  "uuid": "86f8ce32-621c-459c-9bcd-78132804ba9c",
  "sourceToolAssistantUUID": "23729526-b144-4607-9437-a5eaee1a4b64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T06:58:48.386Z_

I now have comprehensive results across all five search dimensions. Here is the full report:

---

## Survey of Concurrent and Recent Work (2025-2026): Online Schema Adaptation, Test-Time Schema Refinement, and Schema-Domain Mismatch for Information Extraction

---

### 1. PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction
- **Venue/Year:** EMNLP 2025 (Industry Track); arXiv:2510.08623 (October 2025); also published at Amazon Science
- **Approach:** PARSE has two main sub-systems. ARCHITECT autonomously optimizes JSON schemas for LLM consumption — it analyzes extraction failures, adds entity descriptions, inserts validation rules, and restructures schemas for clarity, iterating offline on held-out examples. RELAY is an integrated code-generation system that maintains backward compatibility during schema evolution. SCOPE then implements reflection-based extraction at inference time, combining static and LLM-based guardrails. Errors trigger automatic retries with revised prompts.
- **Key results:** Up to 64.7% improvement in extraction accuracy on SWDE; 92% reduction in extraction errors within the first retry.
- **Distinction from purely "online" adaptation:** PARSE's schema optimization (ARCHITECT) is an offline process run before deployment. SCOPE handles test-time correction through retries, but schema structure itself is pre-optimized, not adapted in real time to incoming data distribution shifts.

---

### 2. SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema
- **Venue/Year:** AAAI 2026 (accepted); arXiv:2512.12337 (December 2025)
- **Approach:** A four-component pipeline: (1) an IE module for initial extraction; (2) an iterative pruning module that removes low-quality candidates; (3) a Dual-Path Self-Correcting module that checks for both redundancy (over-extraction) and missing entities (under-extraction) in two parallel streams; (4) a Feedback-Driven Optimization module that converts detection signals into three types of specialized adaptive prompts — Redundancy Prompt, Missing Prompt, and FormatError Prompt — which are injected into a context-learning loop for re-extraction. Ships with a Multi-task Bilingual (Chinese-English) Self-Correcting dataset of 100k+ entries.
- **Key results:** +5.27% average F1 across 11 multilingual zero-shot benchmarks; plug-and-play compatible with any LLM; no fine-tuning required at inference.
- **Distinction:** SCIR operates at test time through schema-conditioned feedback, but its feedback loop targets extraction quality (redundancy/missing), not schema-level concept mismatch or domain drift. It refines predictions, not the schema itself.

---

### 3. Schema as Parameterized Tools (SPT) for Universal Information Extraction
- **Venue/Year:** arXiv:2506.01276 (June 2025); also on OpenReview
- **Approach:** SPT reframes schemas as parameterized tool definitions compatible with LLM tool-calling APIs. The framework unifies three IE modes: (a) Schema Retrieval — selecting the right schema from a predefined pool via retrieval; (b) Schema Filling — extracting information by filling schema slots like tool parameters; (c) Schema Generation — synthesizing new schemas on demand for cases not covered by the pool. This makes the system adaptive between closed-IE, open-IE, and on-demand IE tasks within a single framework.
- **Key results:** Robust schema retrieval and selection performance; comparable extraction to LoRA fine-tuned baselines with far fewer trainable parameters.
- **Distinction:** SPT supports dynamic schema selection and on-the-fly schema generation, which is closer to online adaptation than PARSE. However, it does not explicitly detect domain-schema mismatch or learn from extraction errors over time.

---

### 4. DLISC: Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models
- **Venue/Year:** arXiv:2505.14992 (May 2025); also on OpenReview
- **Approach:** A two-stage Dual-LoRA with Incremental Schema Caching architecture. An Identification LoRA first retrieves the most relevant schema(s) from a large schema pool for a given query. An Extraction LoRA then performs the actual extraction using the matched schema. Incremental Schema Caching stores intermediate KV-cache results per schema, avoiding redundant computation when the same schemas appear repeatedly across queries.
- **Key results:** Improved effectiveness and efficiency across multiple IE benchmarks; specifically designed for resource-constrained on-device deployment.
- **Distinction:** The primary contribution is efficient schema selection and caching for edge LLMs. The system selects among pre-defined schemas adaptively, but does not refine or modify schemas based on extraction feedback or domain mismatch signals.

---

### 5. ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images
- **Venue/Year:** EACL 2026 (Long paper); arXiv:2602.12203 (February 2026)
- **Approach:** A new benchmark of 304 closed and on-demand IE query-answer pairs spanning 110 multi-page documents (forms, financial reports, slide decks, webpage screenshots). It unifies Key Entity Extraction (KEE), Relation Extraction (RE), and Visual Question Answering (VQA) into a single schema-variable task. Construction used a pipeline combining human annotation with LLM-generated, human-validated synthetic samples. The benchmark explicitly evaluates schema adaptation capability, query under-specification handling, and answer localization.
- **Key results:** Analysis of open and closed VLMs reveals that current models systematically fail on schema adaptation and underspecified queries — providing a diagnostic framework rather than a solution.
- **Distinction:** This is a benchmark/evaluation contribution, not an adaptive system. It quantifies the problem of schema variability and mismatch in document IE but does not propose an online adaptation mechanism.

---

### 6. ScrapeGraphAI-100k: Large-Scale Dataset for LLM-Based Web Information Extraction
- **Venue/Year:** arXiv:2602.15189 (February 2026)
- **Approach:** A large dataset pairing web content with prompts, schemas, and model outputs. Includes schema-centric diagnostics that identify empirical failure thresholds (e.g., schema depth > 7 levels, key count > 200). Supports stratified evaluation of extraction robustness under increasing schema complexity.
- **Distinction:** Primarily a dataset/benchmark contribution. Does not propose adaptive schema mechanisms but does characterize schema-domain mismatch failure modes quantitatively.

---

### 7. LOGOS: LLM-Driven End-to-End Grounded Theory Development and Schema Induction
- **Venue/Year:** arXiv:2509.24294 (September 2025); also on OpenReview
- **Approach:** Integrates LLM-driven qualitative coding, semantic clustering, graph reasoning, and iterative refinement to build reusable schema/codebook structures from raw text. Oriented toward grounded theory / qualitative research schema induction rather than IE per se, but directly addresses the problem of schema emergence from data.
- **Distinction:** Targets schema induction from scratch via iterative LLM reasoning, not adaptation of an existing schema to a new domain. No extraction feedback loop or mismatch detection.

---

### 8. Schema-Grounded Memory via Iterative Schema-Aware Extraction
- **Venue/Year:** arXiv:2604.27906 (April 2026)
- **Approach:** Focuses on converting unstructured AI memory/conversation history into schema-grounded structured records via iterative, schema-aware extraction. Applies iterative refinement to ensure extracted memory entries conform to a target schema.
- **Distinction:** Domain is AI memory management, not general IE. Schema is fixed; the iterative process refines extraction fidelity, not the schema itself.

---

### 9. NER with Feedback Loops / Human-in-the-Loop (Background Context)
- **Venue/Year:** NeurIPS 2021 Workshop (User-in-the-Loop NER by Counterfactual Learning); EDBT 2019 (Human-in-the-Loop NER with Deep Learning)
- **Approach:** These older works address feedback-driven NER model updates based on user corrections, including handling of selection bias (non-displayed entities). Relevant to schema-mismatch detection in that they recognize systematic entity-type boundary ambiguity as a schema-level problem.
- **Distinction:** These are not 2025-2026 works but remain the primary prior art on feedback loop NER. No 2025-2026 paper specifically framing schema mismatch detection as a first-class problem for NER was found.

---

### 10. OpenReview / ICML 2026 / NeurIPS 2026 Submissions
- **Finding:** The ICML 2026 and NeurIPS 2026 OpenReview portals are live but do not yet surface accepted or public paper lists specifically on schema adaptation for IE. ICML 2026 submissions are still in review as of May 2026. No specific paper on online schema adaptation for IE was found via OpenReview search. The SPT paper (item 3 above) has an OpenReview entry, suggesting it may be under review for a conference.

---

### Summary Table

| Paper | Year | Venue | Schema Adaptation Type | Online/Test-Time | Mismatch Detection |
|---|---|---|---|---|---|
| PARSE | Oct 2025 | EMNLP 2025 | Offline schema optimization + test-time retry | Partial (retry) | No — error-rate proxy |
| SCIR | Dec 2025 | AAAI 2026 | Test-time extraction refinement via feedback | Yes (extraction loop) | Partial (redundancy/missing) |
| SPT | Jun 2025 | arXiv/OpenReview | Dynamic schema selection + on-demand generation | Yes (schema selection) | No |
| DLISC | May 2025 | arXiv/OpenReview | Schema selection for on-device LLMs | No (selection only) | No |
| ExStrucTiny | Feb 2026 | EACL 2026 | Benchmark: schema-variable IE evaluation | N/A | Implicit (benchmark) |
| ScrapeGraphAI-100k | Feb 2026 | arXiv | Dataset: schema complexity diagnostics | N/A | Partial (failure thresholds) |
| LOGOS | Sep 2025 | arXiv/OpenReview | Schema induction from scratch | No | No |

---

### Key Gap Identified

None of the found papers fully addresses all three components simultaneously: (1) detecting that an existing schema is mismatched to the incoming data domain at test time, (2) automatically refining the schema in response, and (3) doing so in an online loop without human intervention or offline re-optimization. SCIR comes closest to a feedback loop but targets extraction quality, not schema-concept alignment. PARSE optimizes schemas offline. SPT generates schemas on demand but without a mismatch signal. This gap represents the clearest area of novelty for a proposed approach combining schema-domain mismatch detection with online schema refinement.

---

Sources:
- [PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (arXiv:2510.08623)](https://arxiv.org/abs/2510.08623)
- [PARSE at EMNLP 2025 Industry Track](https://aclanthology.org/2025.emnlp-industry.184.pdf)
- [PARSE at Amazon Science](https://www.amazon.science/publications/parse-llm-driven-schema-optimization-for-reliable-entity-extraction)
- [SCIR: A Self-Correcting Iterative Refinement Framework (arXiv:2512.12337)](https://arxiv.org/abs/2512.12337)
- [SCIR at AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40326)
- [Schema as Parameterized Tools for Universal IE (arXiv:2506.01276)](https://arxiv.org/abs/2506.01276)
- [SPT on OpenReview](https://openreview.net/forum?id=yoPtjKVtoX)
- [DLISC: Effective and Efficient Schema-aware IE on On-Device LLMs (arXiv:2505.14992)](https://arxiv.org/abs/2505.14992)
- [DLISC on OpenReview](https://openreview.net/pdf?id=lW7nJDWWz4)
- [ExStrucTiny: Schema-Variable Structured IE Benchmark (arXiv:2602.12203)](https://arxiv.org/abs/2602.12203)
- [ExStrucTiny at EACL 2026](https://aclanthology.org/2026.eacl-long.265/)
- [ScrapeGraphAI-100k (arXiv:2602.15189)](https://arxiv.org/html/2602.15189v1)
- [LOGOS: LLM-Driven Schema Induction (arXiv:2509.24294)](https://arxiv.org/pdf/2509.24294)
- [Schema-Grounded Memory via Iterative Extraction (arXiv:2604.27906)](https://arxiv.org/html/2604.27906)
- [ICML 2026 on OpenReview](https://openreview.net/group?id=ICML.cc%2F2026%2FConference)
- [NeurIPS 2026 on OpenReview](https://openreview.net/group?id=NeurIPS.cc%2F2026)
- [User-in-the-Loop NER by Counterfactual Learning (NeurIPS 2021 Workshop)](https://neurips2021-nlp.github.io/papers/29/CameraReady/camera_User_in_the_Loop_Named_Entity_Recognition.pdf)
- [Frontiers: NER with domain schemas in geoscience (2025)](https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2025.1530004/full)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86f8ce32-621c-459c-9bcd-78132804ba9c",
  "isSidechain": true,
  "agentId": "a5ed62ae593f18051",
  "requestId": "req_011CatTFU8n6d6pEpfr65wwu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97b3d895-6809-47c0-8388-e3330dcd357b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016jK2S42yXFjkKfL3dJv15y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 19987,
      "output_tokens": 3486,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3486,
          "cache_read_input_tokens": 19987,
          "cache_creation_input_tokens": 1938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1938,
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
