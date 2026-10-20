# Research conversation: Search for the latest FOLIO benchmark results and neurosymbolic NL reasoning papers from late 2025 through May 2026. I n

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 117
- **Recorded user turns:** 1
- **Tool calls:** 53
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6f7b669ced9ecb73.jsonl`
- **Structured JSON:** [`bc259c77041efc1accfa.json`](../../sessions/bc/bc259c77041efc1accfa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

117 recorded events

### User

_source line 1 · 2026-05-10T21:09:21.670Z_

Search for the latest FOLIO benchmark results and neurosymbolic NL reasoning papers from late 2025 through May 2026. I need to understand how crowded the FOLIO landscape is.

Search queries to try:
1. "FOLIO benchmark 2026 neurosymbolic reasoning" 
2. "FOLIO first-order logic natural language reasoning state of the art 2026"
3. "Papers with Code FOLIO leaderboard"
4. "neurosymbolic logical reasoning FOLIO 2025 2026"

For each paper/system found, I need: name, accuracy on FOLIO, model used, key technique, and date.

Also search for any recent work on counterexample-guided or CEGAR-based approaches to NL reasoning:
5. "counterexample guided NL reasoning 2025 2026"
6. "CEGAR natural language logical reasoning"
7. "solver feedback iterative premise generation NLP"

Use WebSearch and WebFetch to verify claims. I need accurate, up-to-date information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "627c1af5-7fad-4d60-af4f-47ed4d718cae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T21:09:21.673Z_

```json
{
  "parentUuid": "627c1af5-7fad-4d60-af4f-47ed4d718cae",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
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
  "uuid": "556c1e88-6e42-4b3f-9cb9-1568dbdaa55d",
  "timestamp": "2026-05-10T21:09:21.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T21:09:23.974Z_



I'll start by loading the WebSearch and WebFetch tools, then conduct the searches systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "556c1e88-6e42-4b3f-9cb9-1568dbdaa55d",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaCUqgUDmNK1h3ZjrBN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "515a3c1c-6f6c-4c33-9b30-7147686023aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jv1LHgM9hqAzVgJ6qaNN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 791,
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

_source line 4 · 2026-05-10T21:09:24.285Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Y9GjfVUxY32zJfhTjjTAmb`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "515a3c1c-6f6c-4c33-9b30-7147686023aa",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaCUqgUDmNK1h3ZjrBN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "332feaf4-1a66-44b7-b88a-e03540aceb18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jv1LHgM9hqAzVgJ6qaNN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 791,
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

_source line 5 · 2026-05-10T21:09:24.289Z_

<details><summary>↩ Tool result · `toolu_01Y9GjfVUxY32zJfhTjjTAmb`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "332feaf4-1a66-44b7-b88a-e03540aceb18",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "18dd19dc-f6c4-40c0-be6c-d59d6b2f6de7",
  "sourceToolAssistantUUID": "332feaf4-1a66-44b7-b88a-e03540aceb18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T21:09:26.654Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18dd19dc-f6c4-40c0-be6c-d59d6b2f6de7",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaCge6CVQgviHttgt1M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85ed4238-4b48-4586-a539-1ff24770cf29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErQTShFJFe8gymfYCpJGtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T21:09:27.132Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K5stRYPQXQCDQo9D19ndkp`</summary>

```json
{
  "query": "FOLIO benchmark 2026 neurosymbolic reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85ed4238-4b48-4586-a539-1ff24770cf29",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaCge6CVQgviHttgt1M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "250f4a45-f9c4-43a9-a042-fbb20dec1fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErQTShFJFe8gymfYCpJGtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T21:09:28.291Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RieBd95m5U1vbPd1acuL9b`</summary>

```json
{
  "query": "FOLIO first-order logic natural language reasoning state of the art 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "250f4a45-f9c4-43a9-a042-fbb20dec1fd8",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaCge6CVQgviHttgt1M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46218baf-db12-431f-8d40-c7c2807e92ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErQTShFJFe8gymfYCpJGtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T21:09:28.616Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012316QSCeCpEQ97wrnVTTJi`</summary>

```json
{
  "query": "Papers with Code FOLIO leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46218baf-db12-431f-8d40-c7c2807e92ce",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaCge6CVQgviHttgt1M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffbdf081-2f65-468d-8a9c-b67702378cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErQTShFJFe8gymfYCpJGtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T21:09:28.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Se4WbYyULD1nHgD2JCGdLT`</summary>

```json
{
  "query": "neurosymbolic logical reasoning FOLIO 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffbdf081-2f65-468d-8a9c-b67702378cd7",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaCge6CVQgviHttgt1M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d259bed-8422-4889-9307-50c9f856c99b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErQTShFJFe8gymfYCpJGtd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9014,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1911
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 221,
          "cache_read_input_tokens": 9014,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1911,
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

_source line 11 · 2026-05-10T21:09:34.350Z_

<details><summary>↩ Tool result · `toolu_01RieBd95m5U1vbPd1acuL9b`</summary>

```text
Web search results for query: "FOLIO first-order logic natural language reasoning state of the art 2026"

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection","url":"https://arxiv.org/html/2405.02318v1/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://github.com/Yale-LILY/FOLIO"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"[PDF] FOLIO: Natural Language Reasoning with First-Order Logic | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FOLIO:-Natural-Language-Reasoning-with-First-Order-Han-Schoelkopf/5581bf85386737bd3378eec68189759a05280bea"}]

Based on the search results, here's what I found about FOLIO and the state of first-order logic natural language reasoning:

## FOLIO Overview

FOLIO is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations. FOLIO consists of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

## Current State of the Art (2024-2026)

For both NL reasoning and NL-FOL translation, researchers benchmark multiple state-of-the-art language models, and results show that a subset of FOLIO presents a challenge for one of the most capable Large Language Model (LLM) publicly available, GPT-4.

More specifically, approximately 65% of the time, the model struggles to construct accurate reasoning chains for complex problems with intricate steps, indicating a limited ability to solve problems with long reasoning chains. Additionally, in 25% of cases, erroneous derivations occur within certain reasoning steps, highlighting potential inaccuracies and flaws in logical deductions.

## Key Findings

The search results indicate that despite advances in large language models, there remains a significant gap in their ability to perform complex logical reasoning tasks. FOLIO was published at EMNLP 2024, making it a recent benchmark that continues to challenge state-of-the-art models in formal logical reasoning over natural language.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46218baf-db12-431f-8d40-c7c2807e92ce",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "facec993-251c-49c1-b1d7-7dbd1c9479f7",
  "sourceToolAssistantUUID": "46218baf-db12-431f-8d40-c7c2807e92ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T21:09:34.447Z_

<details><summary>↩ Tool result · `toolu_01K5stRYPQXQCDQo9D19ndkp`</summary>

```text
Web search results for query: "FOLIO benchmark 2026 neurosymbolic reasoning"

Links: [{"title":"NSORN: Designing a Benchmark Dataset for Neurosymbolic Ontology Reasoning with Noise | Neurosymbolic Artificial Intelligence","url":"https://neurosymbolic-ai-journal.com/paper/nsorn-designing-benchmark-dataset-neurosymbolic-ontology-reasoning-noise-2"},{"title":"Intermediate Languages Matter: Formal Languages and LLMs affect Neurosymbolic Reasoning","url":"https://arxiv.org/html/2509.04083v1"},{"title":"Formal Languages and LLMs affect Neurosymbolic ...","url":"https://ceur-ws.org/Vol-4064/kgnesy-paper3.pdf"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"Robustness of Neurosymbolic Reasoners on First-Order Logic Problems","url":"https://arxiv.org/html/2509.17377"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning ...","url":"https://aclanthology.org/2023.emnlp-main.313.pdf"},{"title":"Robustness of Neurosymbolic Reasoners on First-Order Logic Problems","url":"https://alta2025.alta.asn.au/assets/papers/1.pdf"},{"title":"Neurosymbolic approaches to general logical reasoning in ...","url":"https://openreview.net/pdf/b9cf1005d2770c37ff97daf5154df9dd4deb833c.pdf"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"CFP: Neurosymbolic Learning and Reasoning (NeSy 2026)","url":"https://groups.google.com/g/ML-news/c/fjFddCxV9s4"}]

Based on the search results, I found relevant information about FOLIO and neurosymbolic reasoning:

## FOLIO Benchmark Overview

FOLIO is a dataset where premises are paired with different conclusions which either logically follow from the premises (True), or they don't (False), or a conclusion cannot be drawn given the information in the premises (Uncertain), with the task of models being to classify the given natural language premises and conclusion into one of these three labels.

## FOLIO in Neurosymbolic Reasoning Research

FOLIO is one of three logical reasoning datasets used in empirical studies of formal languages across neurosymbolic LLM reasoning, along with ProntoQA and ProofWriter, evaluated with seven different LLMs.

FOLIO offers rich diversity in natural language expressions and more complex logic rules, but is limited in size due to the extensive human effort needed for creation.

## Recent Neurosymbolic Research on FOLIO

Recent studies have examined neurosymbolic approaches on FOLIO:

- Neurosymbolic methods outperform purely neural methods in terms of robustness, while pure neural methods, particularly with CoT reasoning, are stronger in terms of accuracy.

- The LINC approach uses an LLM as a semantic parser to translate natural language premises and conclusions into FOL statements, which are then passed into a logic solver called Prover9 to predict the classification label.

The FOLIO benchmark continues to be a standard evaluation dataset for assessing neurosymbolic reasoning systems in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "250f4a45-f9c4-43a9-a042-fbb20dec1fd8",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "8d0ede8a-2cd5-45d7-b7ba-a14243cce9ce",
  "sourceToolAssistantUUID": "250f4a45-f9c4-43a9-a042-fbb20dec1fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T21:09:36.361Z_

<details><summary>↩ Tool result · `toolu_012316QSCeCpEQ97wrnVTTJi`</summary>

```text
Web search results for query: "Papers with Code FOLIO leaderboard"

Links: [{"title":"An Introduction to Papers With Code: What It is And How to Use It | DataCamp","url":"https://www.datacamp.com/blog/introduction-papers-with-code"},{"title":"LEGOBench: Leaderboard Generation Benchmark for Scientific Models","url":"https://arxiv.org/html/2401.06233v1"},{"title":"tutorials/add_results.md at main · paperswithcode/tutorials","url":"https://github.com/paperswithcode/tutorials/blob/main/add_results.md"},{"title":"Papers with Code","url":"https://paperswithcode.co/"},{"title":"Papers with Code is Dead — Best Alternatives 2026 by Use Case | Codesota | CodeSOTA","url":"https://www.codesota.com/papers-with-code"},{"title":"Papers with code · GitHub","url":"https://github.com/paperswithcode"},{"title":"GitHub - paperswithcode/paperswithcode-client: API Client for paperswithcode.com","url":"https://github.com/paperswithcode/paperswithcode-client"},{"title":"An Exploratory Study of Foundation Model Leaderboards","url":"https://www.computer.org/csdl/journal/ts/2025/04/10855627/23QQWoayUFy"},{"title":"Papers with Code 2020 : A Year in Review | by Ross Taylor | PapersWithCode | Medium","url":"https://medium.com/paperswithcode/papers-with-code-2020-review-938146ab9658"},{"title":"Paper With Code Shuts Down, Open-Source Community Calls for a New All-in-One Resource Hub | News | HyperAI","url":"https://hyper.ai/en/news/42900"}]

Based on the search results, I found important information about Papers with Code:

Papers with Code was shut down by Meta in July 2025 and now redirects to Hugging Face. The 9,327 benchmark leaderboards, 79,817 paper-to-code linkages and 5,628 datasets that had been tracked are no longer served from the canonical URL.

The search results do not contain specific information about a FOLIO leaderboard on Papers with Code. Given that Papers with Code no longer operates as an independent platform, any leaderboards that were previously hosted there are no longer available at the original location.

If you're looking for information about a specific FOLIO leaderboard, it may have been:
- Rescued by the community as JSON dumps on GitHub, as the pwc-archive on Hugging Face, and as 2021-era imports into the Open Research Knowledge Graph.
- Available through Hugging Face, which has trending papers and some leaderboards like Open LLM Leaderboard

Would you like me to search for more specific information about the FOLIO leaderboard or FOLIO benchmark dataset?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffbdf081-2f65-468d-8a9c-b67702378cd7",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "8353a22c-da7f-487b-af3d-5b2bb9b32b67",
  "sourceToolAssistantUUID": "ffbdf081-2f65-468d-8a9c-b67702378cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T21:09:36.736Z_

<details><summary>↩ Tool result · `toolu_01Se4WbYyULD1nHgD2JCGdLT`</summary>

```text
Web search results for query: "neurosymbolic logical reasoning FOLIO 2025 2026"

Links: [{"title":"Intermediate Languages Matter: Formal Languages and LLMs affect Neurosymbolic Reasoning","url":"https://arxiv.org/html/2509.04083v1"},{"title":"A Comparative Study of Neurosymbolic AI Approaches to Interpretable Logical Reasoning | OpenReview","url":"https://openreview.net/forum?id=uO0oaNY9fC"},{"title":"On the Potential of Logic and Reasoning in Neurosymbolic Systems Using OWL-Based Knowledge Graphs - David Herron, Ernesto Jiménez-Ruiz, Tillman Weyde, 2025","url":"https://journals.sagepub.com/doi/10.1177/29498732251320043"},{"title":"AI Reasoning in Deep Learning Era: From Symbolic AI to Neural–Symbolic AI","url":"https://www.mdpi.com/2227-7390/13/11/1707"},{"title":"A Comprehensive Review of Neuro-symbolic AI for Robustness, Uncertainty Quantification, and Intervenability | Arabian Journal for Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13369-025-10887-3"},{"title":"A Comparative Study of Neurosymbolic AI Approaches to ...","url":"https://www.arxiv.org/pdf/2508.03366"},{"title":"Neuro-Symbolic Verification for Preventing LLM Hallucinations in Process Control","url":"https://www.mdpi.com/2227-9717/14/2/322"},{"title":"Neurosymbolic Language Reasoning as Satisfiability Modulo Theory","url":"https://arxiv.org/html/2602.18095"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning ...","url":"https://aclanthology.org/2023.emnlp-main.313.pdf"},{"title":"Frontiers | Putting reasons back into reasoning: how genuine reasoning is inference-based and why neuro-symbolic NLI could achieve it","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1801094/full"}]

Based on the search results, here's what I found about neurosymbolic logical reasoning and FOLIO in 2025-2026:

## Recent Research on Neurosymbolic Logical Reasoning with FOLIO

Researchers have conducted empirical studies of formal languages across three logical reasoning datasets including FOLIO and seven different LLMs (8B–671B parameters). 

Research shows that the choice of formal language for neurosymbolic LLM reasoning affects reasoning performance, with first-order logic outperforming logic programming languages.

### Key Approaches in 2025-2026

**Hybrid vs. Integrative Approaches:** The hybrid approach is more promising for developing general logical reasoning because its reasoning chain is more interpretable and it retains the capabilities and advantages of existing LLMs.

**Neurosymbolic Methods:** Neurosymbolic LLM reasoning works by using LLMs as translators from natural to formal languages and symbolic solvers for deriving correct results. The approach translates a natural language-posed logical reasoning problem into a formal intermediate language using in-context learning, and then a symbolic reasoner solves the translated problem.

### Recent Developments

A neurosymbolic language called Logitext represents documents as natural language text constraints, with an algorithm that integrates LLM-based constraint evaluation with satisfiability modulo theory (SMT) solving for joint textual-logical reasoning.

Neural–Symbolic AI is a paradigm that integrates symbolic logic with neural computation to unify reasoning and learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d259bed-8422-4889-9307-50c9f856c99b",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "61f605d6-bbf7-474c-a9db-bb388021339f",
  "sourceToolAssistantUUID": "2d259bed-8422-4889-9307-50c9f856c99b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T21:09:40.707Z_

Good, now let me run the CEGAR/counterexample-guided searches and also fetch some of the most promising papers for details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61f605d6-bbf7-474c-a9db-bb388021339f",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaDbVJgJK3s8cfxm9jd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "229ba041-9c76-4d9c-bafb-43674cb2456e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189yeMW4egC17qop3ztg3KA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 10925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3806,
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

_source line 16 · 2026-05-10T21:09:41.205Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012CTYyHfccKXH6fiWwQ75jD`</summary>

```json
{
  "query": "counterexample guided NL reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "229ba041-9c76-4d9c-bafb-43674cb2456e",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaDbVJgJK3s8cfxm9jd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5f01ccf-3088-42d4-bb9e-9d537d10907c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189yeMW4egC17qop3ztg3KA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 10925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3806,
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

_source line 17 · 2026-05-10T21:09:41.656Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HwmzR6LE3FgfJ84m9c77cN`</summary>

```json
{
  "query": "CEGAR natural language logical reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5f01ccf-3088-42d4-bb9e-9d537d10907c",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaDbVJgJK3s8cfxm9jd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c88be7f0-e186-45e6-a356-5778215dae76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189yeMW4egC17qop3ztg3KA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 10925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3806,
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

_source line 18 · 2026-05-10T21:09:42.596Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QLhugkjQrLVX4R9Kb7rgC2`</summary>

```json
{
  "query": "solver feedback iterative premise generation NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c88be7f0-e186-45e6-a356-5778215dae76",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaDbVJgJK3s8cfxm9jd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "151c9a29-2288-4014-b8b2-3591fffaebab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189yeMW4egC17qop3ztg3KA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 10925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3806,
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

_source line 19 · 2026-05-10T21:09:42.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RV5zaow9aXhxYddM6eWC8b`</summary>

```json
{
  "query": "FOLIO benchmark accuracy results leaderboard 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "151c9a29-2288-4014-b8b2-3591fffaebab",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaDbVJgJK3s8cfxm9jd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e5bdcc7-60bf-4fe5-b2bb-29fc2906c7ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189yeMW4egC17qop3ztg3KA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 10925,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3806
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 10925,
          "cache_creation_input_tokens": 3806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3806,
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

_source line 20 · 2026-05-10T21:09:49.680Z_

<details><summary>↩ Tool result · `toolu_01HwmzR6LE3FgfJ84m9c77cN`</summary>

```text
Web search results for query: "CEGAR natural language logical reasoning"

Links: [{"title":"Logical reasoning - Wikipedia","url":"https://en.wikipedia.org/wiki/Logical_reasoning"},{"title":"Logical reasoning in natural language: It is all about knowledge | Minds and Machines | Springer Nature Link","url":"https://link.springer.com/article/10.1007/BF00974107"},{"title":"Natural Language Reasoning, A Survey","url":"https://arxiv.org/pdf/2303.14725"},{"title":"Language and Natural Reasoning | Center for the Study of Language and Information","url":"https://csli.stanford.edu/projects/language-and-natural-reasoning"},{"title":"Improved Decision Procedures for Multi-modal Tense Logic Using CEGAR-Tableaux | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-06085-3_13"},{"title":"Logical Reasoning over Natural Language as Knowledge Representation: A Survey","url":"https://arxiv.org/html/2303.12023v2"},{"title":"Probabilistic CEGAR | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-540-70545-1_16"},{"title":"Reasoning is about giving reasons","url":"https://arxiv.org/html/2508.14488"},{"title":"(PDF) Natural Language Processing by Reasoning and Learning","url":"https://www.researchgate.net/publication/262162261_Natural_Language_Processing_by_Reasoning_and_Learning"},{"title":"Efficient CEGAR-tableaux for Non-classical Logics | ANU School of Computing","url":"https://comp.anu.edu.au/study/projects/efficient-cegar-tableaux-for-non-classical-logics/"}]

Based on the search results, I found information about CEGAR in the context of formal logic and automated reasoning, though the connection to natural language logical reasoning specifically appears limited in these results.

## CEGAR Overview

Counterexample-guided abstraction refinement (CEGAR) has been in vogue for the automatic verification of very large systems in the past years. CEGAR uses a SAT-solver and the standard counter-example guided abstraction refinement methodology to search for a rooted Kripke model for a given formula in modal clausal normal form.

## CEGAR Applications to Logical Systems

The search results show CEGAR has been applied to various logical systems:

- CEGAR has been used with SAT-solvers and tableaux calculus methods to search for Kripke models for formulas in modal clausal normal form.
- CEGAR-tableaux were developed to improve existing decision procedures for non-classical logics by combining two well-known existing methods.

## Natural Language and Logical Reasoning

While the search results discuss natural language logical reasoning extensively, they do not specifically connect CEGAR methodology to natural language reasoning tasks. The general field involves classical logical reasoning, natural language inference, multi-hop question answering, and commonsense reasoning, but CEGAR does not appear to be a prominent technique in this domain based on these search results.

If you're looking for information about how CEGAR specifically applies to natural language logical reasoning, you may want to search for more specialized research papers in that intersection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c88be7f0-e186-45e6-a356-5778215dae76",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "122c368b-058c-47eb-8441-9616d4e3457b",
  "sourceToolAssistantUUID": "c88be7f0-e186-45e6-a356-5778215dae76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T21:09:50.203Z_

<details><summary>↩ Tool result · `toolu_012CTYyHfccKXH6fiWwQ75jD`</summary>

```text
Web search results for query: "counterexample guided NL reasoning 2025 2026"

Links: [{"title":"[2309.16436] Neuro Symbolic Reasoning for Planning: Counterexample Guided Inductive Synthesis using Large Language Models and Satisfiability Solving","url":"https://arxiv.org/abs/2309.16436"},{"title":"[2502.10454] One Example Shown, Many Concepts Known! Counterexample-Driven Conceptual Reasoning in Mathematical LLMs","url":"https://arxiv.org/abs/2502.10454"},{"title":"One Example Shown, Many Concepts Known! Counterexample-Driven Conceptual Reasoning in Mathematical LLMs | OpenReview","url":"https://openreview.net/forum?id=A31Ep22iQ7"},{"title":"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models","url":"https://arxiv.org/html/2601.22642v1"},{"title":"Counterexample-Guided Abstraction Refinement for Assumption-based Argumentation","url":"https://proceedings.kr.org/2025/67/kr2025-0067-lagniez-et-al.pdf"},{"title":"[2509.25666] Nudging the Boundaries of LLM Reasoning","url":"https://arxiv.org/abs/2509.25666"},{"title":"Toward large reasoning models: A survey of reinforced reasoning with large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666389925002181"},{"title":"GitHub - LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy: ✨✨Latest Advances on Neuro-Symbolic Learning in the era of Large Language Models","url":"https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy"},{"title":"Top 10 Open-source Reasoning Models in 2026","url":"https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"},{"title":"Empowering LLMs with Logical Reasoning: A Comprehensive Survey","url":"https://www.ijcai.org/proceedings/2025/1155.pdf"}]

Based on the web search results, here's what I found about counterexample-guided NL reasoning in 2025-2026:

## Recent Research on Counterexample-Guided Reasoning

**Mathematical Reasoning with Counterexamples (2025)**

A 2025 work aims to enhance LLMs' ability to conduct mathematical reasoning and proof through counterexamples, inspired by the pedagogical method of "proof by counterexamples" commonly used in human mathematics education. Researchers manually created CounterMATH, a high-quality, university-level mathematical benchmark, which requires LLMs to prove mathematical statements by providing counterexamples.

Extensive experiments and detailed analyses demonstrate that COUNTERMATH is challenging, indicating that LLMs, such as OpenAI o1, have insufficient counterexample-driven proof capabilities. Strengthening LLMs' counterexample-driven conceptual reasoning abilities is crucial for improving their overall mathematical capabilities.

**Neuro-Symbolic Reasoning Approaches (2023-2025)**

Research has shown that satisfiability modulo theory (SMT) solvers can be used as deductive reasoning engines to analyze generated solutions from LLMs, produce counterexamples when solutions are incorrect, and provide feedback to LLMs, where this interaction between inductive LLMs and deductive SMT solvers can iteratively steer the LLM to generate the correct response.

These approaches represent a growing trend of combining counterexample-driven feedback with natural language reasoning in LLMs to improve their logical and mathematical capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5f01ccf-3088-42d4-bb9e-9d537d10907c",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "abd78606-44f0-4154-8829-9e8dcbaa2b7a",
  "sourceToolAssistantUUID": "e5f01ccf-3088-42d4-bb9e-9d537d10907c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T21:09:53.720Z_

<details><summary>↩ Tool result · `toolu_01RV5zaow9aXhxYddM6eWC8b`</summary>

```text
Web search results for query: "FOLIO benchmark accuracy results leaderboard 2024 2025"

Links: [{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Leaderboards - ForecastBench","url":"https://www.forecastbench.org/leaderboards/"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"2025-2026 AI Computer-Use Benchmarks & Top AI Agents ...","url":"https://o-mega.ai/articles/the-2025-2026-guide-to-ai-computer-use-benchmarks-and-top-ai-agents"},{"title":"Benchmark Leaderboard 2025","url":"https://llm-stats.com/benchmarks/table"},{"title":"The FACTS Leaderboard: A Comprehensive Benchmark for ...","url":"https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf"},{"title":"The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality","url":"https://arxiv.org/html/2512.10791v1"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"}]

The search results don't show specific information about the FOLIO benchmark. Let me search more specifically for FOLIO.

Links: [{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"[PDF] FOLIO: Natural Language Reasoning with First-Order Logic | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FOLIO:-Natural-Language-Reasoning-with-First-Order-Han-Schoelkopf/5581bf85386737bd3378eec68189759a05280bea"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.20973"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/html/2505.14932v2"}]

Let me search for specific accuracy results and leaderboard scores for FOLIO:

Links: [{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"AI Model Performance Benchmark Comparison 2024","url":"https://photes.io/notes/53c87b44-0fcf-4a24-a97a-1cc34ad7c14a/ai-model-performance-benchmark-comparison-2024"},{"title":"LLM Benchmarks 2026 — Compare AI Model Scores & Rankings | Price Per Token","url":"https://pricepertoken.com/leaderboards/benchmark"},{"title":"AI Benchmarks 2026: Top Evaluations and Their Limits","url":"https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough"},{"title":"Credit Scores: Performance and Equity","url":"https://ideas.repec.org/p/arx/papers/2409.00296.html"},{"title":"Finance Agent v1.1","url":"https://www.vals.ai/benchmarks/finance_agent"},{"title":"LLM Benchmarks: Measuring AI’s Performance & Accuracy","url":"https://tensorwave.com/blog/llm-benchmarks"},{"title":"AI model benchmarks March 2026 Guide | Logic","url":"https://logic.inc/resources/ai-model-benchmarks-guide"},{"title":"Measuring the performance of our models on real-world tasks | OpenAI","url":"https://openai.com/index/gdpval/"}]

Based on my search results, I found information about the FOLIO benchmark, though a comprehensive leaderboard with specific 2024-2025 accuracy scores wasn't readily available in the search results. Let me provide you with what I found:

## FOLIO Benchmark Overview

FOLIO is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations. It consists of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

## Benchmark Design

The logical correctness of the premises and conclusions is ensured by their FOL annotations, which are automatically verified by an FOL inference engine. In addition to the main NL reasoning task, NL-FOL pairs in FOLIO constitute a new NL-FOL translation dataset.

## Performance Results

The available search results indicate that a subset of FOLIO presents a challenge for one of the most capable Large Language Models (LLM) publicly available, GPT-4. Additionally, researchers benchmarked the performance of several state-of-the-art language models, including GPT-4, on both the natural language reasoning task and the natural language to first-order logic translation task, and while the models perform well on some aspects of the tasks, a subset of the FOLIO dataset presents a significant challenge, even for the powerful GPT-4 model.

Unfortunately, the search results did not contain detailed numerical accuracy scores or a comprehensive leaderboard comparing multiple models' performance on FOLIO for 2024-2025. For the most up-to-date and specific performance metrics, you may want to consult the official FOLIO benchmark documentation or the paper directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e5bdcc7-60bf-4fe5-b2bb-29fc2906c7ad",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "649447bd-6f4e-448c-a5e3-940a73c695d8",
  "sourceToolAssistantUUID": "4e5bdcc7-60bf-4fe5-b2bb-29fc2906c7ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T21:09:54.871Z_

<details><summary>↩ Tool result · `toolu_01QLhugkjQrLVX4R9Kb7rgC2`</summary>

```text
Web search results for query: "solver feedback iterative premise generation NLP"

Links: [{"title":"PRefLexOR: preference-based recursive language modeling for exploratory optimization of reasoning and agentic thinking | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-025-00003-z"},{"title":"Natural Language Inference Model","url":"https://www.emergentmind.com/topics/natural-language-inference-nli-model"},{"title":"Iterative improvements from feedback for language models","url":"https://yuxili.substack.com/p/iterative-improvements-from-feedback"},{"title":"CPSCoach: The Design and Implementation of Intelligent Collaborative Problem Solving Feedback | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-36272-9_58"},{"title":"[2410.13191v2] MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback","url":"http://arxiv.org/abs/2410.13191v2"},{"title":"Jason Eisner's publications - Johns Hopkins Computer Science","url":"https://www.cs.jhu.edu/~jason/papers/"},{"title":"Natural Language Inference with Transformer Ensembles and Explainability Techniques","url":"https://www.mdpi.com/2079-9292/13/19/3876"},{"title":"Building Feedback Loops for Continuous Improvement","url":"https://apxml.com/courses/mlops-for-large-models-llmops/chapter-5-llm-monitoring-observability-maintenance/llm-feedback-loops"},{"title":"Linear Feedback Control Systems for Iterative Prompt Optimization in Large Language Models","url":"https://arxiv.org/html/2501.11979v1"},{"title":"Nli in Nlp - Practical Guide for 2025 | ShadeCoder","url":"https://www.shadecoder.com/topics/nli-in-nlp-a-comprehensive-guide-for-2025"}]

I've performed a web search for "solver feedback iterative premise generation NLP". Here are the key findings:

## Overview of Results

The search revealed several relevant areas in NLP research related to iterative feedback and reasoning:

### Self-Improving Reasoning Systems
PRefLexOR is a framework that integrates preference optimization with reinforcement learning for self-improving scientific reasoning, employing a recursive approach that refines intermediate steps before producing final outputs. Recursive optimization guided by feedback loops refines reasoning, enabling models to learn from feedback in an iterative manner.

### Natural Language Inference (NLI) with Iterative Methods
Multi-turn inference networks conduct iterative reasoning across multiple matching perspectives (e.g., joint, difference, similarity), employing a memory component to integrate information across reasoning turns. LLMs can generate commonsense axioms for premise–hypothesis pairs, and explicitly generated axioms can significantly aid discrimination of entailments, though overgeneralization or misalignment can limit efficacy.

### Iterative Retrieval and Feedback
Iterative retrieval is a framework that empowers retrievers to make iterative decisions through policy optimization to solve the combinatorial optimization problem of finding an optimal portfolio of retrieved items. LLMs can improve their accuracy through iteratively refining and revising their output based on feedback, though revisions can introduce errors and typically use the same reasoning method that produced the initial answer.

### Prompt Optimization with Feedback Control
A novel approach draws parallels between iterative prompt optimization in LLMs and feedback control systems, iteratively refining the prompt by treating the deviation between LLM output and the desired result as an error term.

These approaches all involve iterative improvement mechanisms that use feedback—whether from solvers, humans, or automatic evaluations—to refine both the generation of premises/reasoning and the overall quality of NLP system outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "151c9a29-2288-4014-b8b2-3591fffaebab",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "0e52d3cc-5653-4fe1-97ad-7e3c6386a8ce",
  "sourceToolAssistantUUID": "151c9a29-2288-4014-b8b2-3591fffaebab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T21:09:57.687Z_

Let me now fetch specific papers to get concrete accuracy numbers and details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e52d3cc-5653-4fe1-97ad-7e3c6386a8ce",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaEvjyHDNdvAVqnK1xu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa0a08a8-151e-41d5-a38c-f8093ed1a27a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yo86nQdh6Kn7d8o3LNiZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 2973,
      "cache_read_input_tokens": 14731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2973,
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

_source line 25 · 2026-05-10T21:09:59.676Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015eUyvSyZ1Mu3JMLg3WWthJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2309.16436",
  "prompt": "Extract the paper title, authors, date, key technique (especially CEGAR/counterexample-guided aspects), and any FOLIO benchmark results or accuracy numbers mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa0a08a8-151e-41d5-a38c-f8093ed1a27a",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaEvjyHDNdvAVqnK1xu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b3a297f-dab1-4c0c-9c29-5a01450ce5a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yo86nQdh6Kn7d8o3LNiZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 2973,
      "cache_read_input_tokens": 14731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2973,
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

_source line 26 · 2026-05-10T21:10:01.589Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S1fuJPkuV1E3ZaTQYfQhRw`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.04083v1",
  "prompt": "Extract the paper title, authors, date, key technique, and all FOLIO benchmark accuracy numbers for each model/approach tested. List every accuracy result in a table format if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b3a297f-dab1-4c0c-9c29-5a01450ce5a0",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaEvjyHDNdvAVqnK1xu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25d58d82-d8d9-4cca-9ea6-b01ef10d126f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yo86nQdh6Kn7d8o3LNiZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 2973,
      "cache_read_input_tokens": 14731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2973,
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

_source line 27 · 2026-05-10T21:10:02.534Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sy4y4ukL9ka6UqTAW6mTf3`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.17377",
  "prompt": "Extract the paper title, authors, date, key technique, and all FOLIO benchmark accuracy numbers for each model/approach tested. What are the main findings about robustness of neurosymbolic reasoners?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25d58d82-d8d9-4cca-9ea6-b01ef10d126f",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaEvjyHDNdvAVqnK1xu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b84ec66-3137-4293-8570-3f403a9231a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yo86nQdh6Kn7d8o3LNiZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 2973,
      "cache_read_input_tokens": 14731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2973,
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

_source line 28 · 2026-05-10T21:10:03.648Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PYYDCwnWA36e1e3WToKXca`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.18095",
  "prompt": "Extract the paper title, authors, date, key technique, and all FOLIO benchmark accuracy numbers for each model/approach tested. What is the Logitext/SMT approach and how does it perform?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b84ec66-3137-4293-8570-3f403a9231a0",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaEvjyHDNdvAVqnK1xu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52649b4e-6aa2-4ca5-a185-929b9b8497c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yo86nQdh6Kn7d8o3LNiZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 2973,
      "cache_read_input_tokens": 14731,
      "output_tokens": 455,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2973
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1812,
          "output_tokens": 455,
          "cache_read_input_tokens": 14731,
          "cache_creation_input_tokens": 2973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2973,
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

_source line 29 · 2026-05-10T21:10:04.193Z_

<details><summary>↩ Tool result · `toolu_015eUyvSyZ1Mu3JMLg3WWthJ`</summary>

```text
# Paper Summary

**Title:** "Neuro Symbolic Reasoning for Planning: Counterexample Guided Inductive Synthesis using Large Language Models and Satisfiability Solving"

**Authors:** Sumit Kumar Jha, Susmit Jha, Patrick Lincoln, Nathaniel D. Bastian, Alvaro Velasquez, Rickard Ewetz, Sandeep Neema

**Date:** Submitted September 28, 2023

**Key Technique:** The approach employs counterexample-guided inductive synthesis (CEGIS) by combining LLMs with SMT solvers. The researchers describe their method as using "satisfiability modulo theory (SMT) solvers as deductive reasoning engines to analyze the generated solutions from the LLMs, produce counterexamples when the solutions are incorrect, and provide that feedback to the LLMs."

**Accuracy/Benchmark Results:** The content provided does not include specific FOLIO benchmark results or numerical accuracy metrics. The abstract focuses on methodology rather than quantitative outcomes, noting only that the approach was evaluated using "planning over the domain of blocks" with various models (GPT-4, GPT-3.5 Turbo, and others) paired with Z3 as the SMT solver.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b3a297f-dab1-4c0c-9c29-5a01450ce5a0",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "8dc8a8e3-fcd2-43d8-934f-df4e208f90c4",
  "sourceToolAssistantUUID": "7b3a297f-dab1-4c0c-9c29-5a01450ce5a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T21:10:07.023Z_

<details><summary>↩ Tool result · `toolu_01S1fuJPkuV1E3ZaTQYfQhRw`</summary>

```text
# Paper Summary

**Title:** "Intermediate Languages Matter: Formal Languages and LLMs affect Neurosymbolic Reasoning"

**Authors:** Alexander Beiser (TU Wien), David Penz (Johannes Kepler University Linz), Nysret Musliu (TU Wien)

**Date:** 2025

**Key Technique:** The research introduces the "intermediate language challenge"—demonstrating that the choice of formal language significantly impacts neurosymbolic reasoning performance when LLMs translate natural language problems into formal representations for symbolic solvers.

---

## FOLIO Benchmark Results

The paper notes that "ASP and Pyke...cannot be measured" on FOLIO because those languages cannot effectively encode required classical logic concepts. Therefore, only NLTK and FOL results are available:

| Model | NLTK | FOL |
|-------|------|-----|
| GPT-4o-mini | Not specified separately | Not specified separately |
| Ministral-8B | Not specified separately | Not specified separately |
| Llama-8B | Not specified separately | Not specified separately |
| DeepSeek-8B | Not specified separately | Not specified separately |
| DeepSeek-32B | Not specified separately | Not specified separately |
| DeepSeek-V3 | Not specified separately | Not specified separately |
| DeepSeek-R1 | Not specified separately | Not specified separately |

**Note:** The paper presents aggregated results across datasets (ProntoQA, ProofWriter, FOLIO combined) rather than FOLIO-specific breakdowns by individual model in the tables provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25d58d82-d8d9-4cca-9ea6-b01ef10d126f",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "2edc4423-3806-4850-be99-453b63160ce9",
  "sourceToolAssistantUUID": "25d58d82-d8d9-4cca-9ea6-b01ef10d126f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T21:10:11.469Z_

<details><summary>↩ Tool result · `toolu_01PYYDCwnWA36e1e3WToKXca`</summary>

```text
# Neurosymbolic Language Reasoning as Satisfiability Modulo Theory

**Title:** Neurosymbolic Language Reasoning as Satisfiability Modulo Theory

**Authors:** Hyunseok Oh, Sam Stern, Youngki Lee, Matthai Philipose

**Date:** 2025 (arXiv:2602.18095v1)

**Key Technique:** Logitext - a neurosymbolic language combining natural language text constraints (NLTCs) with SMT solving through an integrated propose-verify-refine loop.

## The Logitext/SMT Approach

Logitext extends prompts into hybrid text/logic documents by annotating textual clauses with logical operators. The system treats LLM reasoning as an SMT theory, enabling iterative interleaving of:

1. **Logical solver (Z3)** proposing Boolean variable assignments satisfying formal constraints
2. **NLSolver** (LLM-based) generating text satisfying semantic constraints while maintaining Boolean consistency
3. **Refinement loops** when text doesn't satisfy required constraints

This addresses two reasoning gaps in LLMs:
- **Compositional gap:** narrows with model scale but persists
- **Combinatorial gap:** remains severe even in frontier models (GPT-5 recovers <1% of satisfying assignments vs. SMT solvers)

## Performance Results

The paper doesn't report FOLIO benchmark results. Instead, it evaluates on:

- **Content Moderation (CMOD):** Five multi-page policies with 6-22 clauses
- **LegalBench:** Five legal reasoning tasks
- **Super-NaturalInstructions:** Five instruction-following tasks

**Key findings:**
- Text Instance Generation: Logitext achieves near-saturation performance, outperforming direct prompting
- Text Coverage Generation: Significantly broader coverage under fixed time budgets
- Task Execution: Improves on CMOD/NaturalInstructions; mixed results on LegalBench (7/10 tasks successful)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52649b4e-6aa2-4ca5-a185-929b9b8497c7",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "512def58-4c7a-4a90-b789-3bcec2bebb75",
  "sourceToolAssistantUUID": "52649b4e-6aa2-4ca5-a185-929b9b8497c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T21:11:22.752Z_

<details><summary>↩ Tool result · `toolu_01Sy4y4ukL9ka6UqTAW6mTf3`</summary>

```text
# Paper Summary

**Title:** Robustness of Neurosymbolic Reasoners on First-Order Logic Problems

**Authors:** Hannah Bansal, Kemal Kurniawan, Lea Frermann

**Date:** 2024 (arxiv 2509.17377v2)

**Key Technique:** NSCoT (Neurosymbolic Chain-of-Thought) - combines LLM-based natural language to first-order logic parsing with a symbolic solver (Prover9), enhanced with intermediate reasoning chains

## Main Findings on Robustness

The research demonstrates that "neurosymbolic methods are more robust but achieve lower performance than purely neural methods." Key insights:

- **Robustness advantage:** LINC maintained accuracy differences under 5% between default and counterfactual tasks (statistically insignificant), while purely neural approaches showed 10%+ drops
- **Performance trade-off:** Neural methods with CoT consistently outperformed neurosymbolic approaches in overall accuracy
- **NSCoT improvement:** Adding reasoning chains improved neurosymbolic performance while maintaining robustness, though still lagging behind pure CoT

## FOLIO Benchmark Results (Table 2)

Results on full FOLIO validation set (204 samples):

| Model | Naïve | CoT | LINC | NSCoT |
|-------|-------|-----|------|-------|
| Mistral 0.3 7B | 53.43 | 56.37 | 52.94 | 53.92 |
| Qwen 2.5 7B | 59.31 | 70.59 | 58.33 | 66.67 |
| Qwen 2.5 32B | 66.18 | 75.49 | 68.14 | 71.08 |
| Llama 3.1 8B | 33.33 | 70.59 | 58.33 | 68.14 |
| Gemma 3 12B | 64.22 | 77.45 | 57.35 | 63.24 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b84ec66-3137-4293-8570-3f403a9231a0",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "901df318-8df3-4c0d-97b1-ffb9e3ac8823",
  "sourceToolAssistantUUID": "0b84ec66-3137-4293-8570-3f403a9231a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T21:11:25.524Z_

Excellent, I'm getting concrete numbers now. Let me fetch more papers for additional FOLIO results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "901df318-8df3-4c0d-97b1-ffb9e3ac8823",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaMQTkv57ExVWFPtY36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ff4bbba-7497-4e2a-a9bd-59ddb9bdcc4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQ714jZZCx8Tu5sy3vFFDz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 506,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 17704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3503,
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

_source line 34 · 2026-05-10T21:11:26.467Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TKx7LZbS4ZKgT83AeRkLzR`</summary>

```json
{
  "query": "LINC FOLIO accuracy GPT-4 neurosymbolic 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ff4bbba-7497-4e2a-a9bd-59ddb9bdcc4d",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaMQTkv57ExVWFPtY36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bb9b9f0-7d70-48a9-9a5d-35dacfe4eca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQ714jZZCx8Tu5sy3vFFDz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 506,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 17704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3503,
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

_source line 35 · 2026-05-10T21:11:27.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XjgsyoxJptSpka8mdsHBbJ`</summary>

```json
{
  "query": "NL2FOL FOLIO accuracy results logical fallacy detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bb9b9f0-7d70-48a9-9a5d-35dacfe4eca8",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaMQTkv57ExVWFPtY36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb1c44d1-2082-4fad-9406-e2adb17a6c90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQ714jZZCx8Tu5sy3vFFDz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 506,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 17704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3503,
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

_source line 36 · 2026-05-10T21:11:28.001Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NHM1pCXaFXU41FsAFmjSAg`</summary>

```json
{
  "query": "FOL-Traces FOLIO first-order logic reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb1c44d1-2082-4fad-9406-e2adb17a6c90",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaMQTkv57ExVWFPtY36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0272dbf4-8215-4fe8-a909-044e3b7a9d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQ714jZZCx8Tu5sy3vFFDz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 506,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 17704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3503,
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

_source line 37 · 2026-05-10T21:11:28.524Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QRCm97oAy1tNMAAy2r44o9`</summary>

```json
{
  "query": "\"FOLIO\" accuracy \"chain of thought\" GPT-4 o1 reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0272dbf4-8215-4fe8-a909-044e3b7a9d7c",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaMQTkv57ExVWFPtY36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9941b10-0b3b-42ec-b172-d5cb5c8762b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQ714jZZCx8Tu5sy3vFFDz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 506,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 17704,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3503
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 506,
          "output_tokens": 249,
          "cache_read_input_tokens": 17704,
          "cache_creation_input_tokens": 3503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3503,
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

_source line 38 · 2026-05-10T21:11:33.428Z_

<details><summary>↩ Tool result · `toolu_01TKx7LZbS4ZKgT83AeRkLzR`</summary>

```text
Web search results for query: "LINC FOLIO accuracy GPT-4 neurosymbolic 2024"

Links: [{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining","url":"https://arxiv.org/pdf/2310.15164"},{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"[2310.15164] LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers","url":"https://arxiv.org/abs/2310.15164"},{"title":"Robustness of Neurosymbolic Reasoners on First-Order Logic Problems","url":"https://arxiv.org/html/2509.17377"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning ...","url":"https://aclanthology.org/2023.emnlp-main.313.pdf"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers | OpenReview","url":"https://openreview.net/forum?id=h00GHjWDEp"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.313/"},{"title":"Intermediate Languages Matter: Formal Languages and LLMs affect Neurosymbolic Reasoning","url":"https://arxiv.org/html/2509.04083v1"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers","url":"https://www.researchgate.net/publication/376394657_LINC_A_Neurosymbolic_Approach_for_Logical_Reasoning_by_Combining_Language_Models_with_First-Order_Logic_Provers"},{"title":"LTRAG: Enhancing Autoformalization and Self-refinement ...","url":"https://aclanthology.org/2025.findings-acl.126.pdf"}]

I found research on LINC, a neurosymbolic approach for logical reasoning. Here are the key findings related to your query:

## LINC Overview
LINC (Logical Inference via Neurosymbolic Computation) reformulates logical reasoning tasks as modular neurosymbolic programming, where the LLM acts as a semantic parser, translating premises and conclusions from natural language to expressions in first-order logic, and these expressions are then offloaded to an external theorem prover, which symbolically performs deductive inference.

## Performance on FOLIO with GPT-4
The results on the FOLIO dataset show mixed performance with GPT-4: When used with GPT-4, LINC scores 26% higher than CoT on ProofWriter while performing comparatively on FOLIO. For GPT-4, the trend reverses: LINC underperforms CoT.

## Broader Performance Insights
The approach shows significant performance gains on FOLIO and a balanced subset of ProofWriter for three different models in nearly all experimental conditions evaluated. Additionally, on ProofWriter, augmenting the comparatively small open-source StarCoder+ (15.5B parameters) with LINC even outperforms GPT-3.5 and GPT-4 with Chain-of-Thought prompting by an absolute 38% and 10%, respectively.

The original LINC paper was published in 2023, making it one of the notable neurosymbolic approaches from that period combining language models with formal logic reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bb9b9f0-7d70-48a9-9a5d-35dacfe4eca8",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "ddad0504-82c9-4bdd-8bf1-51a2ff122020",
  "sourceToolAssistantUUID": "3bb9b9f0-7d70-48a9-9a5d-35dacfe4eca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T21:11:33.584Z_

<details><summary>↩ Tool result · `toolu_01XjgsyoxJptSpka8mdsHBbJ`</summary>

```text
Web search results for query: "NL2FOL FOLIO accuracy results logical fallacy detection"

Links: [{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection","url":"https://arxiv.org/html/2405.02318v1/"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection | OpenReview","url":"https://openreview.net/forum?id=lBc3MXcGqZ"},{"title":"[2405.02318] Autoformalizing Natural Language to First-Order Logic: A Case Study in Logical Fallacy Detection","url":"https://arxiv.org/abs/2405.02318"},{"title":"Autoformalizing Natural Language to First-Order Logic","url":"https://aclanthology.org/2025.findings-ijcnlp.8.pdf"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection","url":"https://www.emergentmind.com/papers/2405.02318"},{"title":"[Literature Review] Autoformalizing Natural Language to First-Order Logic: A Case Study in Logical Fallacy Detection","url":"https://www.themoonlight.io/en/review/autoformalizing-natural-language-to-first-order-logic-a-case-study-in-logical-fallacy-detection"},{"title":"[2405.02318v1] NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection","url":"https://arxiv.org/abs/2405.02318v1"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic","url":"https://openreview.net/pdf?id=lBc3MXcGqZ"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NL2FOL:-Translating-Natural-Language-to-First-Order-Lalwani-Kim/f56614b0b188f4b53bfc63b134220ed4167024a4"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection - Paper Detail","url":"https://deeplearn.org/arxiv/582469/nl2fol:-translating-natural-language-to-first-order-logic-for-logical-fallacy-detection"}]

Based on the search results, here's information about NL2FOL and its accuracy results for logical fallacy detection:

## Overview

NL2FOL is a process designed to reliably detect logical fallacies by translating natural language to First-order Logic (FOL) step-by-step using Large Language Models (LLMs). The system utilizes Satisfiability Modulo Theory (SMT) solvers to reason about the validity of the formula and classify inputs as either a fallacy or valid statement.

## Accuracy Results

The NL2FOL framework demonstrates strong performance on multiple datasets:

- On the LOGIC dataset, NL2FOL achieves an F1-score of 78%, while generalizing effectively to the LOGICCLIMATE dataset with an F1-score of 80%.

In comparison to end-to-end LLMs, the classifier achieves an F1-score of 71% on the Logic dataset, and achieves an F1-score of 73% on the challenge set, LogicClimate, outperforming state-of-the-art models by 21% despite its much smaller size.

## Key Features

The approach is robust, interpretable and does not require training data or fine-tuning. Additionally, the model provides a novel means of utilizing LLMs to interpret the output of the SMT solver, offering insights into the counter-examples that illustrate why a given sentence is considered a logical fallacy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb1c44d1-2082-4fad-9406-e2adb17a6c90",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "29fc25c0-5fd7-4247-a6b5-a19a20f053a3",
  "sourceToolAssistantUUID": "eb1c44d1-2082-4fad-9406-e2adb17a6c90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T21:11:35.751Z_

<details><summary>↩ Tool result · `toolu_01NHM1pCXaFXU41FsAFmjSAg`</summary>

```text
Web search results for query: "FOL-Traces FOLIO first-order logic reasoning 2025"

Links: [{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/html/2505.14932v2"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale | Isabelle Lee","url":"https://iglee.me/papers/fol-traces/"},{"title":"[2505.14932] FOL-Pretrain: A complexity annotated corpus of first-order logic","url":"https://arxiv.org/abs/2505.14932"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOL-Pretrain: A complexity annotated corpus of first-order logic","url":"https://arxiv.org/html/2505.14932v1"},{"title":"[PDF] FOLIO: Natural Language Reasoning with First-Order Logic | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FOLIO:-Natural-Language-Reasoning-with-First-Order-Han-Schoelkopf/5581bf85386737bd3378eec68189759a05280bea"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"}]

Based on the search results, here's what I found about FOL-Traces and FOLIO:

## FOL-Traces (2025)

FOL-Traces is the first large-scale dataset of programmatically verified reasoning traces, enabling rigorous evaluation of structured logical inference. FOL-Traces combines programmatic verification with pretraining-scale size, enabling systematic study of logical reasoning.

The dataset addresses a significant gap in reasoning evaluation: Natural-language traces are unverifiable, symbolic datasets too small, and most benchmarks conflate heuristics with inference.

The researchers propose two challenging and comprehensive diagnostic tasks—masked operation prediction and step completion—that directly probe syntactic awareness and process fidelity. Systematic experiments with 5 reasoning LLMs show that the dataset remains challenging: models only reach around 45.7% accuracy on masked operation prediction and around 27% on two-step completion. The work was published in May 2025 and appears in EACL 2026.

## FOLIO (Earlier Benchmark)

FOLIO is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations. FOLIO consists of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

The logical correctness of the premises and conclusions is ensured by their FOL annotations, which are automatically verified by an FOL inference engine. A subset of FOLIO presents a challenge for one of the most capable LLM publicly available, GPT-4.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0272dbf4-8215-4fe8-a909-044e3b7a9d7c",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "8f87f10c-f5e5-4cbc-a417-f105a7ae321e",
  "sourceToolAssistantUUID": "0272dbf4-8215-4fe8-a909-044e3b7a9d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T21:11:36.538Z_

<details><summary>↩ Tool result · `toolu_01QRCm97oAy1tNMAAy2r44o9`</summary>

```text
Web search results for query: ""FOLIO" accuracy "chain of thought" GPT-4 o1 reasoning 2025"

Links: [{"title":"Learning to reason with LLMs | OpenAI","url":"https://openai.com/index/learning-to-reason-with-llms/"},{"title":"A comparative evaluation of chain-of-thought-based prompt engineering techniques for medical question answering - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0010482525009655"},{"title":"Chain of Thought Prompting (CoT): Everything you need to know","url":"https://www.vellum.ai/blog/chain-of-thought-prompting-cot-everything-you-need-to-know"},{"title":"Reasoning Models Struggle to Control their Chains of Thought","url":"https://arxiv.org/html/2603.05706v1"},{"title":"Structured Output and Chain of Thought: Enhancing GPT-4o Completions | by Dario Fabiani | Medium","url":"https://medium.com/@dario.fabiani/structured-output-and-chain-of-thought-revolutionizing-gpt-4o-interactions-90f60ce75186"},{"title":"Analysis and prediction in SCR experiments using GPT-4 with an effective chain-of-thought prompting strategy - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2589004224006722"},{"title":"Chain-of-Thought Reasoning: The Magic Behind the o1 Model – Founding Minds","url":"https://www.foundingminds.com/chain-of-thought-reasoning-the-magic-behind-the-o1-model/"},{"title":"OpenAI GPT-4.5 System Card OpenAI February 27, 2025 1 Introduction","url":"https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf"},{"title":"Everything you should know about GPT-5 [September 2026]","url":"https://botpress.com/blog/everything-you-should-know-about-gpt-5"},{"title":"Deductive Verification of Chain-of-Thought Reasoning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/72393bd47a35f5b3bee4c609e7bba733-Supplemental-Conference.pdf"}]

Based on the search results, I found information related to your query about chain of thought reasoning and o1 models, though the specific "FOLIO" benchmark wasn't explicitly mentioned in the results. Here's what I found:

## o1 Model and Chain of Thought Performance

The o1 model uses a chain of thought when attempting to solve problems, and through reinforcement learning, o1 learns to hone its chain of thought and refine the strategies it uses.

The o1 model significantly outperforms GPT-4o on the vast majority of reasoning-heavy tasks. For example, OpenAI reported that in a qualifying exam for the International Mathematics Olympiad (IMO), GPT-4 solved only 13% of the problems, while the o1 reasoning model scored an impressive 83%.

## Chain of Thought in 2025 Research

Recent 2025 research indicates that model capabilities proved more crucial than prompting methods, with o1-mini leading performance in medical reasoning tasks. Additionally, if you're using reasoning-native models like OpenAI's o1/o3 series or Anthropic's latest Claude, test carefully, as they already handle many reasoning tasks without explicit CoT, so you may not need to add it at all.

The search results don't contain specific information about the FOLIO benchmark. If you'd like more targeted information about FOLIO specifically, I'd be happy to search for that separately.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9941b10-0b3b-42ec-b172-d5cb5c8762b1",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "394b6112-2dee-4e83-988e-000f96646492",
  "sourceToolAssistantUUID": "d9941b10-0b3b-42ec-b172-d5cb5c8762b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T21:11:39.471Z_

Let me fetch more specific papers and leaderboard data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "394b6112-2dee-4e83-988e-000f96646492",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaNRToiV4Vf4fQttwzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15f612b9-94b4-4547-947f-bcb53df71f76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7ubF8E3dPLcUtU3BbHhwM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4588,
      "cache_read_input_tokens": 21207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4588,
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

_source line 43 · 2026-05-10T21:11:41.557Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011i8LkvtTwzRCrSVr13HhG5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2310.15164",
  "prompt": "Extract all FOLIO accuracy numbers from this LINC paper. What accuracy does LINC achieve on FOLIO with GPT-4, GPT-3.5, and other models? What does Chain-of-Thought achieve on FOLIO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15f612b9-94b4-4547-947f-bcb53df71f76",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaNRToiV4Vf4fQttwzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8760d739-1ac8-40c2-82c0-cf0bfe0dbbe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7ubF8E3dPLcUtU3BbHhwM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4588,
      "cache_read_input_tokens": 21207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4588,
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

_source line 44 · 2026-05-10T21:11:43.098Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013dkrbvVxC1WY8vJZvHVZbD`</summary>

```json
{
  "url": "https://arxiv.org/html/2405.02318v1/",
  "prompt": "Extract all FOLIO accuracy results from this NL2FOL paper. What accuracy numbers do they report on FOLIO? What models and techniques are compared?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8760d739-1ac8-40c2-82c0-cf0bfe0dbbe7",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaNRToiV4Vf4fQttwzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "826fb19d-e04e-42c6-b8a1-288255b9a255",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7ubF8E3dPLcUtU3BbHhwM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4588,
      "cache_read_input_tokens": 21207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4588,
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

_source line 45 · 2026-05-10T21:11:44.096Z_

<details><summary>↩ Tool result · `toolu_011i8LkvtTwzRCrSVr13HhG5`</summary>

```text
I cannot extract specific FOLIO accuracy numbers from the provided content. While the abstract mentions that LINC achieves "significant performance gains on FOLIO and a balanced subset of ProofWriter," it does not provide the actual accuracy percentages for FOLIO results with GPT-4, GPT-3.5, or other models.

The document only states: "When used with GPT-4, LINC scores 26% higher than CoT on ProofWriter while performing comparatively on FOLIO." This indicates comparable rather than superior performance on FOLIO, but no specific accuracy figures are given.

To find the actual FOLIO accuracy numbers, you would need to access the full PDF paper rather than this abstract summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8760d739-1ac8-40c2-82c0-cf0bfe0dbbe7",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "432387eb-1906-48f3-979a-cfe996cdc1b4",
  "sourceToolAssistantUUID": "8760d739-1ac8-40c2-82c0-cf0bfe0dbbe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-10T21:11:44.632Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HK6qLKTeFsUH8TriMeFytK`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.14932v2",
  "prompt": "Extract any FOLIO benchmark results from this FOL-Traces paper. What accuracy numbers are reported? What models are tested?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "432387eb-1906-48f3-979a-cfe996cdc1b4",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaNRToiV4Vf4fQttwzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de76467e-e111-449c-8744-157a04722a39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7ubF8E3dPLcUtU3BbHhwM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4588,
      "cache_read_input_tokens": 21207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4588,
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

_source line 47 · 2026-05-10T21:11:44.720Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LsxgT8d4YuqAWbcimu4E3a`</summary>

```json
{
  "query": "LTRAG FOLIO accuracy autoformalization self-refinement logical reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de76467e-e111-449c-8744-157a04722a39",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaNRToiV4Vf4fQttwzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41a8aa25-73ef-4293-970e-0e63ae14d70c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7ubF8E3dPLcUtU3BbHhwM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4588,
      "cache_read_input_tokens": 21207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4588,
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

_source line 48 · 2026-05-10T21:11:47.491Z_

<details><summary>↩ Tool result · `toolu_013dkrbvVxC1WY8vJZvHVZbD`</summary>

```text
# NL2FOL Paper: FOLIO Results

Based on my review of the provided content, **the paper does not report any results on FOLIO**. 

The document discusses experiments on three datasets:

1. **Logic** - contains 2,449 logical fallacies
2. **LogicClimate** - contains 1,079 climate-related fallacies
3. **SNLI Corpus** - contains 170,000+ valid sentences

The main results table (Table 2) shows the model achieved "an F1-score of 71%" on the Logic+SNLI combined dataset, outperforming zero-shot approaches but underperforming some large language models like GPT-4 and Claude 3 Opus.

The paper makes no mention of FOLIO as an evaluation benchmark. If you're looking for FOLIO results from this work, they appear not to be included in this research paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "826fb19d-e04e-42c6-b8a1-288255b9a255",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "05468752-89c7-4b66-b9e6-f025dfd9b4cd",
  "sourceToolAssistantUUID": "826fb19d-e04e-42c6-b8a1-288255b9a255",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T21:11:49.475Z_

<details><summary>↩ Tool result · `toolu_01HK6qLKTeFsUH8TriMeFytK`</summary>

```text
# FOL-Traces Paper: FOLIO Benchmark Results

Based on my review of the provided document, **no FOLIO benchmark results with specific accuracy numbers are reported in this paper.**

The paper mentions FOLIO only once in the context of dataset construction: "We leverage existing benchmarks such as LogicBench...and FOLIO...as sources of human-annotated logical forms and prompts."

## What the Paper Actually Tests

Instead of FOLIO, the authors conduct their own experiments with:

**Models Tested:**
- Phi-3 family (phi-3.5-mini, phi-3-medium-128k)
- Qwen-2.5 family (7b, 14b, 32b)
- GPT-2-small (125M, for pretraining validation)

**Tasks and Results:**
- **Task 1 (Masked Operation Prediction):** Overall accuracy of ~45.7% across models
- **Task 2 (Step Completion):** ~27% on two-step completion; best model (Qwen2.5-32B) reached 76% on 1-step, but only 40% on 2-step

The paper uses FOLIO as a resource for generating its own FOL-Traces dataset rather than evaluating against FOLIO's benchmark directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de76467e-e111-449c-8744-157a04722a39",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "9f9d73c3-229c-41c2-8c67-49903d55ace4",
  "sourceToolAssistantUUID": "de76467e-e111-449c-8744-157a04722a39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T21:11:52.054Z_

<details><summary>↩ Tool result · `toolu_01LsxgT8d4YuqAWbcimu4E3a`</summary>

```text
Web search results for query: "LTRAG FOLIO accuracy autoformalization self-refinement logical reasoning"

Links: [{"title":"LTRAG: Enhancing Autoformalization and Self-refinement ...","url":"https://aclanthology.org/2025.findings-acl.126.pdf"},{"title":"LTRAG: Enhancing autoformalization and self-refinement for logical reasoning with Thought-Guided RAG | OpenReview","url":"https://openreview.net/forum?id=6WQZCc9qQ1"},{"title":"LTRAG: Enhancing Autoformalization and Self-refinement for Logical Reasoning with Thought-Guided RAG - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.126/"},{"title":"LTRAG: Enhancing Autoformalization and Self-refinement for Logical","url":"https://ymliu-sysu.github.io/papers/ACL25.pdf"},{"title":"LTRAG: Enhancing autoformalization and self-refinement for ...","url":"https://openreview.net/pdf?id=6WQZCc9qQ1"},{"title":"Aclanthology","url":"https://aclanthology.org/2025.findings-acl.126.bib"},{"title":"HetaRAG: Hybrid Deep Retrieval-Augmented Generation ...","url":"https://arxiv.org/pdf/2509.21336"},{"title":"dblp: Yeliang Xiu","url":"https://dblp.org/pid/245/4789.html"},{"title":"dblp: Ruikang Hu","url":"https://dblp.org/pid/394/8215.html"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"}]

Based on the search results, here's what I found about LTRAG:

## Overview

LTRAG is a framework to enhance autoformalization and self-refinement for logical reasoning with Retrieval-Augmented Generation (RAG), by building knowledge bases of thought-guided examples.

## Performance on FOLIO and Key Accuracy Metrics

LTRAG achieves an accuracy gain of 8% over Logic-LM and LINC on GPT-3.5-turbo and FOLIO, and 13% on GPT-4 and AR-LSAT. Experimental results on FOLIO and AR-LSAT show that LTRAG consistently outperforms Logic-LM and LINC across different models.

## Technical Approach

Neuro-symbolic methods like Logic-LM and LINC enhance performance by integrating formalization with LLMs and symbolic solvers, though these methods still struggle with accurate formalization of complex natural language problems. LTRAG addresses this challenge by leveraging thought-guided examples for both formalization and refinement processes.

## Publication

The paper was published in the Findings of the Association for Computational Linguistics (ACL) 2025, authored by Hu, Ruikang; Lin, Shaoyu; Xiu, Yeliang; and Liu, Yongmei from Sun Yat-sen University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41a8aa25-73ef-4293-970e-0e63ae14d70c",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "4b7aecb3-2347-4a42-8d36-408a99187e03",
  "sourceToolAssistantUUID": "41a8aa25-73ef-4293-970e-0e63ae14d70c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T21:11:56.875Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E7dxv6kgc8vXZQHCigQzEz`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-acl.126.pdf",
  "prompt": "Extract ALL FOLIO accuracy numbers from this LTRAG paper. What specific accuracy does LTRAG, Logic-LM, LINC, and Chain-of-Thought achieve on FOLIO? List every number for each model (GPT-3.5, GPT-4, etc.). Also extract any details about the self-refinement or iterative correction process."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b7aecb3-2347-4a42-8d36-408a99187e03",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaPa22uZUWG8R1TCj9g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edc15921-3e19-4c7e-a078-534f3c54ccfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPCvUpUnrqcBNKRFQEp2hK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1988,
      "cache_read_input_tokens": 25795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-10T21:11:56.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RPHjsTvVXBkbuaiiuSJTs2`</summary>

```json
{
  "query": "Logic-LM FOLIO accuracy GPT-4 results neurosymbolic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edc15921-3e19-4c7e-a078-534f3c54ccfe",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaPa22uZUWG8R1TCj9g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b2aa75b-4c62-4891-8d9f-90f634c9d48e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPCvUpUnrqcBNKRFQEp2hK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1988,
      "cache_read_input_tokens": 25795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-10T21:11:57.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013jdna4EGuC84FHaFMMjNT3`</summary>

```json
{
  "query": "\"FOLIO\" accuracy score table comparison models 2024 2025 neurosymbolic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b2aa75b-4c62-4891-8d9f-90f634c9d48e",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaPa22uZUWG8R1TCj9g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ced74ca4-41de-47d8-b9b2-34107d1046ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPCvUpUnrqcBNKRFQEp2hK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1988,
      "cache_read_input_tokens": 25795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-10T21:12:02.850Z_

<details><summary>↩ Tool result · `toolu_01E7dxv6kgc8vXZQHCigQzEz`</summary>

```text
I've reviewed the PDF content provided, but I cannot extract the specific FOLIO accuracy numbers you're requesting. The document appears to be a compressed PDF file with embedded objects, and the text content is largely garbled or encoded in a way that makes it unreadable.

To properly answer your question about LTRAG, Logic-LM, LINC, and Chain-of-Thought performance on FOLIO benchmarks, I would need:

1. A properly decoded or OCR'd version of the paper
2. Direct access to readable text sections containing the results tables
3. Clear performance metrics for each model variant

**What I can tell you:** The visible metadata indicates this is paper 550.pdf from a findings repository, appearing to span 7 pages with multiple font resources and embedded graphics. However, the actual numerical accuracy results are not legible in the current format.

I recommend obtaining a cleaner version of the paper (either the original PDF from an academic repository or a reformatted text version) to extract the precise accuracy metrics you need for your analysis.

[Binary content (application/pdf, 297.4KB) also saved to /home/ubuntu/.claude-account-2/projects/-/04847dfd-3c66-4e9a-b430-c3ae68322c95/tool-results/webfetch-1778447518844-bws9b5.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edc15921-3e19-4c7e-a078-534f3c54ccfe",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "a7ec2f69-8306-4a51-a57e-886394ce83a2",
  "sourceToolAssistantUUID": "edc15921-3e19-4c7e-a078-534f3c54ccfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-10T21:12:03.575Z_

<details><summary>↩ Tool result · `toolu_01RPHjsTvVXBkbuaiiuSJTs2`</summary>

```text
Web search results for query: "Logic-LM FOLIO accuracy GPT-4 results neurosymbolic"

Links: [{"title":"Logic-LM: Symbolic Solvers Enhance LLM Logic","url":"https://www.emergentmind.com/papers/2305.12295"},{"title":"Intermediate Languages Matter: Formal Languages and LLMs affect Neurosymbolic Reasoning","url":"https://arxiv.org/html/2509.04083v1"},{"title":"Prototype-then-Refine: A Neurosymbolic Approach for ...","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/BassemAkoushHashemElezabi.pdf"},{"title":"Robustness of Neurosymbolic Reasoners on First-Order Logic Problems","url":"https://arxiv.org/pdf/2509.17377"},{"title":"Formal Languages and LLMs affect Neurosymbolic ...","url":"https://arxiv.org/pdf/2509.04083"},{"title":"Making LLMs Reason? The Intermediate Language Problem in Neurosymbolic Approaches","url":"https://arxiv.org/html/2502.17216v1"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning ...","url":"https://aclanthology.org/2023.emnlp-main.313.pdf"},{"title":"LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification","url":"https://arxiv.org/html/2602.21044v1"},{"title":"Alignment Methods for Formal Logical Reasoning","url":"https://aclanthology.org/2025.mathnlp-main.8.pdf"},{"title":"GitHub - teacherpeterpan/Logic-LLM: The project page for \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\" · GitHub","url":"https://github.com/teacherpeterpan/Logic-LLM"}]

I've found comprehensive results about Logic-LM, FOLIO accuracy, and neurosymbolic approaches. Here's a summary of the key findings:

## Logic-LM Performance Overview

Logic-LM was evaluated on five logical reasoning datasets including FOLIO, and achieved a significant performance boost of 39.2% over standard prompting and 18.4% over chain-of-thought prompting.

## FOLIO Dataset Results

Logic-LM's effectiveness was demonstrated on the FOLIO dataset using the entire test set consisting of 204 examples. The results show that Logic-LM achieves up to 39.2% improvement over standard prompting on complex tasks through its three-module design for problem formulation, symbolic reasoning, and result interpretation.

## GPT-4 Accuracy Results

Averaged over five logical reasoning datasets, Logic-LM achieves a performance boost of 18.4% compared to Chain of Thought using GPT-4. On the more challenging AR-LSAT dataset, the overall accuracy of Logic-LM with GPT-4 on AR-LSAT is 43.04%.

## Neurosymbolic Approach

Logic-LM is a framework that integrates LLMs with symbolic solvers to enhance logical reasoning. Neurosymbolic approaches help by constraining the probabilistic nature to the translation step of a natural language-posed problem into a formal language, so the reasoning step itself is not affected by the probabilistic nature of LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b2aa75b-4c62-4891-8d9f-90f634c9d48e",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "9d9eb823-5f3e-4f22-9d45-f288218ce51b",
  "sourceToolAssistantUUID": "4b2aa75b-4c62-4891-8d9f-90f634c9d48e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-10T21:12:05.353Z_

<details><summary>↩ Tool result · `toolu_013jdna4EGuC84FHaFMMjNT3`</summary>

```text
Web search results for query: ""FOLIO" accuracy score table comparison models 2024 2025 neurosymbolic"

Links: [{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"Empowering LLMs with Logical Reasoning: A Comprehensive Survey","url":"https://www.ijcai.org/proceedings/2025/1155.pdf"},{"title":"Neurosymbolic AI for Safe and Trustworthy High-Stakes Applications[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202511.1342"},{"title":"Neuro-Symbolic Artificial Intelligence: A Task-Directed ...","url":"https://www.ijcai.org/proceedings/2025/1157.pdf"},{"title":"Neuro-Symbolic AI: A Foundational Analysis of the Third Wave’s Hybrid Core | by Greg Robison | Medium","url":"https://gregrobison.medium.com/neuro-symbolic-ai-a-foundational-analysis-of-the-third-waves-hybrid-core-cc95bc69d6fa"},{"title":"[2501.05435] Neuro-Symbolic AI in 2024: A Systematic Review","url":"https://arxiv.org/abs/2501.05435"},{"title":"Prototype-then-Refine: A Neurosymbolic Approach for ...","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/BassemAkoushHashemElezabi.pdf"},{"title":"Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation and","url":"https://arxiv.org/pdf/2506.04810"},{"title":"A Comparative Study of Neurosymbolic AI Approaches to ...","url":"https://www.arxiv.org/pdf/2508.03366"}]

The search results contain relevant information about FOLIO and neurosymbolic approaches to logical reasoning. Here's what I found:

## FOLIO Overview

FOLIO provides a first-order logic annotated benchmark for natural language reasoning, where conclusions are formally verified via an FOL inference engine to assess the reasoning ability of LLMs.

## Research Context (2024-2025)

FOLIO offers rich diversity in natural language expressions and more complex logic rules, but is limited in size due to the extensive human effort needed for creation. FOLIO does not provide any reasoning chains, while ProofWriter and RuleTaker include reasoning chains, but they are not readily accessible and require users to implement additional code to extract them for each problem.

## Neurosymbolic Approaches

Recent work has been exploring neurosymbolic methods for logical reasoning. LLMSymbolic views LLMs as implicit neurosymbolic reasoners, aligning neural representations with symbolic inference through iterative self-distillation. 

Analysis demonstrates that the hybrid approach is more promising for developing general logical reasoning because its reasoning chain is more interpretable, and it retains the capabilities and advantages of existing LLMs.

The search results reference FOLIO as a benchmark dataset for evaluating logical reasoning in natural language, but do not contain specific accuracy score comparison tables. For detailed accuracy metrics across specific models on FOLIO, you may need to consult the original FOLIO paper or recent papers that directly benchmark models on this dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ced74ca4-41de-47d8-b9b2-34107d1046ba",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "94159c60-8154-4438-bbb9-a7fe2362ad7b",
  "sourceToolAssistantUUID": "ced74ca4-41de-47d8-b9b2-34107d1046ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-10T21:12:10.775Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MQtDQAbpzQ57eppjeXXNo1`</summary>

```json
{
  "url": "https://www.emergentmind.com/papers/2305.12295",
  "prompt": "Extract ALL FOLIO accuracy numbers from the Logic-LM paper. What specific accuracy does Logic-LM achieve on FOLIO? List accuracy for each model variant (GPT-3.5, GPT-4, standard prompting, CoT, Logic-LM, Logic-LM++). Include any comparison table data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94159c60-8154-4438-bbb9-a7fe2362ad7b",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaQYghPNpU4f9WKY3MG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "202667b0-1633-4d0b-8732-cd76de289626",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrKw7XcnY5xnh72xEUMwFT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2467,
      "cache_read_input_tokens": 27783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2467,
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

_source line 58 · 2026-05-10T21:12:12.235Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0171qtWwJWNm54erMh59rpLH`</summary>

```json
{
  "url": "https://www.arxiv.org/pdf/2508.03366",
  "prompt": "Extract ALL FOLIO accuracy numbers and comparison tables from this comparative study paper. What approaches are compared? What accuracy does each approach achieve on FOLIO? List every number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "202667b0-1633-4d0b-8732-cd76de289626",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaQYghPNpU4f9WKY3MG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a88dba2-126e-41e4-9e4c-af60f0e54110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrKw7XcnY5xnh72xEUMwFT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2467,
      "cache_read_input_tokens": 27783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2467,
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

_source line 59 · 2026-05-10T21:12:13.296Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013PaseXrrKRF2xX8abq3D6K`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.20973",
  "prompt": "Extract the paper title, authors, date, key technique, and ALL FOLIO accuracy numbers. What models are tested? What are the results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a88dba2-126e-41e4-9e4c-af60f0e54110",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaQYghPNpU4f9WKY3MG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc4dad27-8a3e-45f0-b972-a3a8810cf443",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrKw7XcnY5xnh72xEUMwFT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2467,
      "cache_read_input_tokens": 27783,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2467
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 27783,
          "cache_creation_input_tokens": 2467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2467,
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

_source line 60 · 2026-05-10T21:12:14.089Z_

<details><summary>↩ Tool result · `toolu_01MQtDQAbpzQ57eppjeXXNo1`</summary>

```text
# FOLIO Accuracy Data from Logic-LM Paper

Based on the provided web page content, **specific FOLIO accuracy numbers are not included**. 

The page mentions that Logic-LM was evaluated on "five logical reasoning datasets: ProofWriter, PrOntoQA, FOLIO, LogicalDeduction, and AR-LSAT" and notes that the framework demonstrates "particularly evident" effectiveness "on more complex datasets such as FOLIO."

However, the actual accuracy metrics for FOLIO—including model-specific results for GPT-3.5, GPT-4, standard prompting, chain-of-thought, Logic-LM, or Logic-LM++—are not presented in this summary page.

To obtain these detailed FOLIO accuracy numbers, you would need to access the full paper PDF or the researchers' GitHub repository at https://github.com/teacherpeterpan/Logic-LLM, where the complete experimental results tables are likely available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "202667b0-1633-4d0b-8732-cd76de289626",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "fb1fe9c1-a3ae-4ab3-a2f6-78b0824803f3",
  "sourceToolAssistantUUID": "202667b0-1633-4d0b-8732-cd76de289626",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-10T21:12:17.048Z_

<details><summary>↩ Tool result · `toolu_0171qtWwJWNm54erMh59rpLH`</summary>

```text
# FOLIO Accuracy Results from Neurosymbolic AI Comparative Study

I examined the PDF content provided, which appears to be "A Comparative Study of Neurosymbolic AI Approaches to Interpretable Logical Reasoning" by Michael K. Chen (arXiv:2508.03366).

## Key Finding

Unfortunately, the PDF content provided consists primarily of the document structure (PDF metadata, object definitions, and encoded streams) rather than readable text. The actual performance numbers and comparison tables are contained within compressed/encoded content streams that cannot be reliably extracted from this raw PDF data.

## What I Can Confirm

The document discusses:
- **Neurosymbolic AI approaches** for logical reasoning
- **FOLIO dataset** (referenced in metadata as a destination anchor)
- Multiple comparison frameworks across different model architectures

## Recommendation

To obtain the specific FOLIO accuracy numbers and comparison tables, you would need:
1. A text-extracted version of the paper
2. The rendered PDF viewed in a standard reader
3. The paper accessed directly from arXiv (https://arxiv.org/abs/2508.03366v1)

I apologize that I cannot provide the specific numerical results from the encoded content without proper text extraction capabilities.

[Binary content (application/pdf, 762.7KB) also saved to /home/ubuntu/.claude-account-2/projects/-/04847dfd-3c66-4e9a-b430-c3ae68322c95/tool-results/webfetch-1778447532487-ma38x9.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a88dba2-126e-41e4-9e4c-af60f0e54110",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "89bfed8d-7397-4263-b337-9b71feabde3f",
  "sourceToolAssistantUUID": "0a88dba2-126e-41e4-9e4c-af60f0e54110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-10T21:12:19.638Z_

<details><summary>↩ Tool result · `toolu_013PaseXrrKRF2xX8abq3D6K`</summary>

```text
# Paper Analysis

**Title:** "Linear Reasoning vs. Proof by Cases: Obstacles for Large Language Models in FOL Problem Solving"

**Authors:** Yuliang Ji, Fuchen Shen, Jian Wu, Qiujie Xie, Yue Zhang (from Nanjing University of Science and Technology, Westlake University, and Zhejiang University)

**Date:** 2026 (AISTATS submission)

**Key Technique:** Probabilistic graphical model analysis using mathematical assumptions about LLM reasoning capabilities to explain performance gaps between linear and case-based reasoning tasks.

## Models Tested

The research evaluates these models:
- **Proprietary:** GPT-4o, GPT-4.1, o4-mini
- **Open-source:** Llama-3.3-70B, DeepSeek-V3, Qwen3 (various sizes), DeepSeek-R1

## Key Results (PC-FOL Dataset)

The paper demonstrates substantial accuracy gaps between linear-reasoning and proof-by-cases problems:

| Model | Linear Reasoning | Proof-by-Cases | Gap |
|-------|-----------------|-----------------|-----|
| GPT-4o (0-shot) | 85.13% | 51.08% | -34.05% |
| GPT-4.1 (0-shot) | 89.24% | 69.86% | -19.38% |
| o4-mini (0-shot) | 90.80% | 79.84% | -10.96% |
| DeepSeek-V3 (0-shot) | 89.63% | 76.71% | -12.92% |

Manual evaluation revealed that for proof-by-cases problems, "fewer than half of samples with correct labels actually get correct proofs," highlighting fundamental reasoning limitations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc4dad27-8a3e-45f0-b972-a3a8810cf443",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "a6730467-0f2d-44be-a604-eb664ba25cfb",
  "sourceToolAssistantUUID": "bc4dad27-8a3e-45f0-b972-a3a8810cf443",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-10T21:12:24.159Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KVqhLXpmc9q4sak34TUpZq`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.04083v1",
  "prompt": "I need ALL specific accuracy numbers for the FOLIO dataset. Look for any tables that show FOLIO results separated by dataset. Also look for aggregate results that include FOLIO. What are the exact accuracy percentages for each model on FOLIO specifically? Also what formal languages were tested (FOL, NLTK, ASP, Pyke)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6730467-0f2d-44be-a604-eb664ba25cfb",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaRbjXXCXFEk5xA5XEo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23d0783d-7f6d-4a97-86ae-36310c7b2ac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w95YbqfZzmx2RYjLCQayG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 30250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-10T21:12:24.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sz2oNfoAL8day42bgWLaRG`</summary>

```json
{
  "query": "LogicGraph FOLIO benchmark multi-path logical reasoning neuro-symbolic 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23d0783d-7f6d-4a97-86ae-36310c7b2ac4",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaRbjXXCXFEk5xA5XEo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb27852d-5e44-49d0-a42f-3a64c051a002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w95YbqfZzmx2RYjLCQayG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 30250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-10T21:12:25.414Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Y7FgMv5kgJAh771fMujtX`</summary>

```json
{
  "query": "\"efficient translation\" NL FOL FOLIO accuracy 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb27852d-5e44-49d0-a42f-3a64c051a002",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaRbjXXCXFEk5xA5XEo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ff137e0-f4eb-4967-b310-1dba994018ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w95YbqfZzmx2RYjLCQayG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 30250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-10T21:12:28.609Z_

<details><summary>↩ Tool result · `toolu_01KVqhLXpmc9q4sak34TUpZq`</summary>

```text
# FOLIO Dataset Results

Based on the paper's content, **specific per-model accuracy numbers for FOLIO are not provided in this excerpt**. The document states that experiments were conducted on FOLIO, but the detailed results table (Table 1) only shows comprehensive data for ProntoQA and ProofWriter datasets.

## What We Know About FOLIO Testing:

**Formal languages tested on FOLIO:**
The paper indicates that "We do not use ASP and Pyke on FOLIO, as FOLIO instances require classical logic concepts which are effectively impossible to encode in standard logic programming." Therefore, only **FOL and NLTK** were evaluated on this dataset.

**Dataset characteristics:**
- 204 samples in the test set
- Open-world assumption (OWA) with 33% random baseline accuracy

**General findings:**
The authors mention in the results section that "the largest improvements w.r.t. to the baselines" occurred on smaller models, but they don't break down FOLIO-specific accuracy percentages separately in the provided excerpt. The paper's full version (referenced as a longer work) likely contains the detailed FOLIO performance breakdowns by model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23d0783d-7f6d-4a97-86ae-36310c7b2ac4",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "7448dd2b-b5ea-4337-ac09-42f1680662b6",
  "sourceToolAssistantUUID": "23d0783d-7f6d-4a97-86ae-36310c7b2ac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-10T21:12:32.424Z_

<details><summary>↩ Tool result · `toolu_01Sz2oNfoAL8day42bgWLaRG`</summary>

```text
Web search results for query: "LogicGraph FOLIO benchmark multi-path logical reasoning neuro-symbolic 2026"

Links: [{"title":"[2602.21044] LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification","url":"https://arxiv.org/abs/2602.21044"},{"title":"LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification","url":"https://arxiv.org/html/2602.21044v1"},{"title":"LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification | Request PDF","url":"https://www.researchgate.net/publication/401177871_LogicGraph_Benchmarking_Multi-Path_Logical_Reasoning_via_Neuro-Symbolic_Generation_and_Verification"},{"title":"GitHub - kkkkarry/LogicGraph: The resource code of LogicGraph · GitHub","url":"https://github.com/kkkkarry/LogicGraph"},{"title":"LogicGraph: Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification / LogicGraph: 通过神经符号生成与验证的多路径逻辑推理基准 | Alan Hou","url":"https://alanhou.org/blog/arxiv-logicgraph-benchmarking-multi-path-logical-reasoning/"},{"title":"Improving LLM Reasoning via Symbolic Inference over Logic Graphs | OpenReview","url":"https://openreview.net/forum?id=lSGFavwaAm"},{"title":"Discourse-Aware Graph Networks for Textual Logical ...","url":"https://www.computer.org/csdl/journal/tp/2023/10/10136812/1NsFSpQJ9xC"},{"title":"Pengyu Li","url":"https://www.catalyzex.com/author/Pengyu%20Li"},{"title":"Paper page - MM-CondChain: A Programmatically Verified Benchmark for Visually Grounded Deep Compositional Reasoning","url":"https://huggingface.co/papers/2603.12266"},{"title":"“Less but more efficient ”: Using less data to achieve better logical reasoning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231225018259"}]

Based on the search results, here's what I found about LogicGraph:

## Overview

LogicGraph is the first benchmark aimed to systematically evaluate multi-path logical reasoning, constructed via a neuro-symbolic framework that leverages backward logic generation and semantic instantiation.

## Key Features

**Multi-Path Reasoning**: Each query in LogicGraph admits 2 to 19 valid proof paths. The benchmark features an average reasoning depth of 6.01 steps.

**Construction Method**: The framework synthesizes premises from the conclusion upwards using fundamental argument forms, creating a symbolic logic Directed Acyclic Graph (DAG) that is subsequently verbalized.

**Exhaustive Ground Truth**: Each instance is associated with an exhaustive set of minimal proofs.

**Built-in Distractions**: The dataset introduces structural distractions where a premise can be crucial for one valid path yet distracting for another.

## Evaluation Framework

A reference-free neuro-symbolic evaluator translates generated natural language steps into formal logic and verifies them using a symbolic solver (Prover9), achieving high agreement with human experts (98.80% Step Accuracy and 95.22% Proof Accuracy).

## Key Findings

Experiments on state-of-the-art language models reveal a common limitation: models tend to commit early to a single route and fail to explore alternatives, and the coverage gap grows substantially with reasoning depth.

The paper was published on February 24, 2026, and code and data are available at https://github.com/kkkkarry/LogicGraph.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb27852d-5e44-49d0-a42f-3a64c051a002",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "74833079-7f31-41c6-b907-b7c125d1b8c2",
  "sourceToolAssistantUUID": "cb27852d-5e44-49d0-a42f-3a64c051a002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-10T21:12:33.750Z_

<details><summary>↩ Tool result · `toolu_012Y7FgMv5kgJAh771fMujtX`</summary>

```text
Web search results for query: ""efficient translation" NL FOL FOLIO accuracy 2025 arxiv"

Links: [{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"},{"title":"[2506.18383] LOGICPO: Efficient Translation of NL-based Logical Problems to FOL using LLMs and Preference Optimization","url":"https://arxiv.org/abs/2506.18383"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/html/2409.16461v1"},{"title":"Do LLMs Really Struggle at NL-FOL Translation? ...","url":"https://arxiv.org/pdf/2511.11816"},{"title":"[2506.18383v1] LOGICPO: Efficient Translation of NL-based Logical Problems to FOL using LLMs and Preference Optimization","url":"https://arxiv.org/abs/2506.18383v1"},{"title":"Do LLMs Really Struggle at NL-FOL Translation? Revealing their Strengths via a Novel Benchmarking Strategy","url":"https://arxiv.org/html/2511.11816v1"},{"title":"Advancing Natural Language Formalization to First Order ...","url":"https://arxiv.org/pdf/2509.22338"},{"title":"[2511.11816] Do LLMs Really Struggle at NL-FOL Translation? Revealing their Strengths via a Novel Benchmarking Strategy","url":"https://arxiv.org/abs/2511.11816"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://arxiv.org/pdf/2502.06563"}]

Based on the search results, I found several recent papers on efficient translation of Natural Language (NL) to First-Order Logic (FOL), particularly focused on the FOLIO dataset. Here are the key findings:

## Recent Papers (2025)

A paper titled "LOGICPO: Efficient Translation of NL-based Logical Problems to FOL using LLMs and Preference Optimization" proposes using fine-tuning on a preference optimization dataset with techniques such as Direct Preference Optimization (DPO) and Kahneman-Tversky optimization (KTO) to fine-tune open-source LLMs. The best model with Phi-3.5 consistently outperforms GPT-3.5-turbo's (8-shot) by producing 10% more logically correct translations with 14% less syntax errors.

## Earlier Work (2024)

Another approach proposes incremental techniques where the model is trained to first produce predicates of premises and conclusions, then produce the FOL for each statement one by one, which improves predictive accuracy on FOLIO. Additionally, separate T5 models are trained to verify predicates and FOLs on-the-fly and apply necessary corrections when needed.

For few-shot performance, the Mixtral model achieved the highest accuracy with the FOLIO dataset at 42%, while LLaMA-2 13B models improved from 24% to 34% when fine-tuned, becoming on-par with the much larger LLaMA-2 70B.

## Broader Context

A recent paper critically examines existing datasets and evaluation protocols for NL-FOL translation, proposing a novel evaluation protocol designed to distinguish genuine semantic-level logical understanding from superficial pattern recognition. Using this approach, state-of-the-art dialogue-oriented LLMs demonstrate strong NL-FOL translation skills.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ff137e0-f4eb-4967-b310-1dba994018ee",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "4cabe480-7153-42de-845a-49b6a216395f",
  "sourceToolAssistantUUID": "9ff137e0-f4eb-4967-b310-1dba994018ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-10T21:12:39.298Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016BfFEK8bfwoGEjaTN5xKF3`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.21044v1",
  "prompt": "Extract ALL FOLIO accuracy results from this LogicGraph paper, if any. Also extract the key accuracy numbers on the LogicGraph benchmark for each model tested. List models, their accuracy, and any comparison to FOLIO results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cabe480-7153-42de-845a-49b6a216395f",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaSe2iYMGL1B663Lw1u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5459c3c7-f06f-43bb-8679-46047061f6b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3YyLZpQQoNEkMf58wdGwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2514,
      "cache_read_input_tokens": 31699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2514,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-10T21:12:42.633Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JMCQ2A5Vr6svgPnyGJ9yo4`</summary>

```json
{
  "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf",
  "prompt": "Extract the paper title, authors, date, key technique, and ALL FOLIO accuracy numbers. This appears to be an ICLR 2025 paper about LLMs and logical reasoning. What models are tested on FOLIO? What accuracy scores are reported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5459c3c7-f06f-43bb-8679-46047061f6b3",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaSe2iYMGL1B663Lw1u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd5546e3-f48d-4f72-82a6-9e3100a59c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3YyLZpQQoNEkMf58wdGwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2514,
      "cache_read_input_tokens": 31699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2514,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-10T21:12:42.913Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WiDDearaZr4aP29EZqKPcD`</summary>

```json
{
  "query": "LLMSymbolic FOLIO self-distillation symbolic reasoning accuracy 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd5546e3-f48d-4f72-82a6-9e3100a59c56",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaSe2iYMGL1B663Lw1u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50c31652-8307-43f0-a2c9-83ca7e0cbd42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3YyLZpQQoNEkMf58wdGwo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2514,
      "cache_read_input_tokens": 31699,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2514
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 338,
          "cache_read_input_tokens": 31699,
          "cache_creation_input_tokens": 2514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2514,
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

_source line 72 · 2026-05-10T21:12:44.647Z_

<details><summary>↩ Tool result · `toolu_016BfFEK8bfwoGEjaTN5xKF3`</summary>

```text
# LogicGraph Paper: Accuracy Results

## FOLIO Results
The paper does **not provide FOLIO accuracy results**. FOLIO is mentioned only as a comparison benchmark in Table 1, which notes it has "3.4" average depth and "1" path, but no performance metrics are given.

## LogicGraph Benchmark Results

The paper evaluates multiple models using **convergent metrics** (Success Rate, Precision, Shortest Path Finding Rate) rather than a single "accuracy" score. Here are key findings:

**Top Performing Models:**
- **Gemini-3-Pro-Preview**: 96.11% Success Rate, 90.10% Precision, 80.33% Shortest Path
- **Deepseek-V3.2-Exp-T (Thinking)**: 88.00% Success Rate, 76.96% Precision
- **Gemini-2.5-Pro**: 87.78% Success Rate, 73.38% Precision

**Divergent Thinking Metrics** (solution exploration) show substantially lower performance:
- Gemini-3-Pro achieves 59.60% Diversity and 79.44% Versatility
- Best models fail to enumerate multiple valid reasoning paths

The paper emphasizes: "top models remain concentrated on a narrow subset of valid reasoning paths" despite achieving high convergent metrics, revealing gaps between single-solution correctness and true multi-path reasoning capability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5459c3c7-f06f-43bb-8679-46047061f6b3",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "3c6533be-eeac-400a-abe3-59aaa158c70f",
  "sourceToolAssistantUUID": "5459c3c7-f06f-43bb-8679-46047061f6b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-10T21:12:51.233Z_

<details><summary>↩ Tool result · `toolu_01WiDDearaZr4aP29EZqKPcD`</summary>

```text
Web search results for query: "LLMSymbolic FOLIO self-distillation symbolic reasoning accuracy 2025"

Links: [{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"Techrxiv","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176538331.19733376/v1"},{"title":"A Survey on Symbolic Knowledge Distillation of Large Language Models","url":"https://arxiv.org/html/2408.10210v1"},{"title":"LLM to Symbolic: Neuro-Symbolic Integration","url":"https://www.emergentmind.com/topics/llm-to-symbolic"},{"title":"Chain-of-Thought Curriculum Distillation: Teaching Smaller Models to Reason Step-by-Step | Proceedings of the 2025 2nd International Symposium on Artificial Intelligence for Education","url":"https://dl.acm.org/doi/10.1145/3775073.3775200"},{"title":"Cognitive Flow: An LLM-Automated Framework for ...","url":"https://aclanthology.org/2025.inlg-main.36.pdf"},{"title":"Self-Distilled Reasoner in LLMs","url":"https://www.emergentmind.com/topics/self-distilled-reasoner"},{"title":"LLMs & Symbolic Solvers: A Neuro-Symbolic Approach","url":"https://www.emergentmind.com/topics/llms-with-symbolic-solvers"},{"title":"Metacognitive symbolic distillation framework for multi-choice machine reading comprehension - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705125001777"},{"title":"Adaptive Chain-of-Thought Distillation Based on LLM Performance on Original Problems","url":"https://www.mdpi.com/2227-7390/13/22/3646"}]

Based on the search results, here's what I found about LLMSymbolic and related self-distillation approaches for symbolic reasoning:

## LLMSymbolic Overview

LLMSymbolic (Fang et al. 2024) views LLMs as implicit neurosymbolic reasoners, aligning neural representations with symbolic inference through iterative self-distillation. This enables LLMs to efficiently acquire symbolic reasoning capabilities with minimal supervision.

## FOLIO and Symbolic Reasoning Benchmarks

FOLIO has been widely adopted to benchmark reasoning depth and solver-interfacing capabilities. This dataset is commonly used to evaluate how well LLMs can perform logical reasoning tasks when combined with symbolic solvers.

## Symbolic Reasoning Accuracy Improvements

The research shows multiple approaches achieving strong results on symbolic reasoning tasks:

- On composite reasoning benchmarks, adaptive symbolic language selection delivered 96% accuracy, exceeding the best single-language baseline by up to 25%.

- DSER achieves Cons@64 accuracy of 89.3% on AIME 2024.

- NPR achieves state-of-the-art performance and 4x–5x inference speedup on parallel-structured math and logic tasks.

## Integration with Symbolic Solvers

LLMs translate natural language statements to FOL formulas, which are then checked for entailment by solvers like Prover9 or Z3, with the LLM handling semantic interpretation while the solver carries out formal inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50c31652-8307-43f0-a2c9-83ca7e0cbd42",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "6b1a2631-a589-4c15-a9eb-6934e638f073",
  "sourceToolAssistantUUID": "50c31652-8307-43f0-a2c9-83ca7e0cbd42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-10T21:12:51.745Z_

<details><summary>↩ Tool result · `toolu_01JMCQ2A5Vr6svgPnyGJ9yo4`</summary>

```text
I appreciate your question, but I need to be transparent about the content you've provided. The text you've shared appears to be raw PDF binary data (compressed/encoded streams from a PDF file), not readable paper content. The streams contain encoded fonts, images, and text that cannot be directly extracted and parsed without proper PDF decompression.

To accurately extract the paper title, authors, FOLIO accuracy numbers, and other details you're requesting, I would need:

1. **A readable text version** of the paper (plain text, markdown, or properly extracted PDF text)
2. **A direct PDF file link** that I could reference
3. **The paper's HTML or published version** from a venue like ICLR, arXiv, or similar

**What I can tell you:** Based on your description mentioning "ICLR 2025 paper about LLMs and logical reasoning" with "FOLIO accuracy," you're likely referring to research on formal logic benchmarking. FOLIO (First-Order Logic Induction) is a known benchmark for testing LLMs' logical reasoning capabilities.

**To help you effectively:**
- Please share the paper in a readable format (plain text extraction, arXiv link, or DOI)
- Or provide the specific model names and accuracy scores you're interested in verifying

I'm happy to extract and analyze the information once readable content is available.

[Binary content (application/pdf, 1.4MB) also saved to /home/ubuntu/.claude-account-2/projects/-/04847dfd-3c66-4e9a-b430-c3ae68322c95/tool-results/webfetch-1778447564196-nca04a.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd5546e3-f48d-4f72-82a6-9e3100a59c56",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "08e26090-b53c-42cd-84a7-00227840d467",
  "sourceToolAssistantUUID": "dd5546e3-f48d-4f72-82a6-9e3100a59c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-10T21:12:58.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GV5d3V9ESETfspdcbq7jwZ`</summary>

```json
{
  "query": "FOLIO dataset GPT-4 accuracy 72 74 76 78 80 percent benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08e26090-b53c-42cd-84a7-00227840d467",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaTxzWa8DJtJvTSnpHp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "146b6c15-7b24-4c07-bcd4-a0711071435a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEv6gu3hgoZHjQA7iN8PAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 920,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 34213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-10T21:12:59.029Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D4MiMZpwBjE7JQXzXqGukK`</summary>

```json
{
  "query": "\"pushing boundaries\" \"formal logic verification\" FOLIO accuracy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "146b6c15-7b24-4c07-bcd4-a0711071435a",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaTxzWa8DJtJvTSnpHp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "825c0a3c-75b1-4a71-8d8f-874c62e1217f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEv6gu3hgoZHjQA7iN8PAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 920,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 34213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-10T21:12:59.803Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KwDskYACAxjPGVTjHRbDUt`</summary>

```json
{
  "query": "Logic-LM FOLIO 58 62 67 accuracy GPT-4 GPT-3.5 table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "825c0a3c-75b1-4a71-8d8f-874c62e1217f",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaTxzWa8DJtJvTSnpHp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a76137f-f1a6-4c72-a482-49362938cd18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEv6gu3hgoZHjQA7iN8PAY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 920,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 34213,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1099
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 920,
          "output_tokens": 187,
          "cache_read_input_tokens": 34213,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1099,
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

_source line 78 · 2026-05-10T21:13:05.328Z_

<details><summary>↩ Tool result · `toolu_01KwDskYACAxjPGVTjHRbDUt`</summary>

```text
Web search results for query: "Logic-LM FOLIO 58 62 67 accuracy GPT-4 GPT-3.5 table"

Links: [{"title":"Alignment Methods for Formal Logical Reasoning","url":"https://aclanthology.org/2025.mathnlp-main.8.pdf"},{"title":"LOGIC-LM++: Multi-Step Refinement for Symbolic Formulations","url":"https://arxiv.org/html/2407.02514v1"},{"title":"LogicBench: Towards Systematic Evaluation of Logical ...","url":"https://aclanthology.org/2024.acl-long.739.pdf"},{"title":"Improving accuracy of GPT-3/4 results on biomedical data using a retrieval-augmented language model - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11338460/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"Evaluation of LLMs for mathematical problem solving","url":"https://arxiv.org/html/2506.00309v2"},{"title":"Introducing GPT-5.5 | OpenAI","url":"https://openai.com/index/introducing-gpt-5-5/"},{"title":"Evaluating Logical and Reasoning Capabilities in GPT-3.5 and 4","url":"https://tatsoft.com/blog-evaluating-logical-and-reasoning-capabilities-in-gpt-3-5-and-gpt-4/"},{"title":"GPT-3.5, GPT-4, or BARD? Evaluating LLMs reasoning ability in zero-shot setting and performance boosting through prompts - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949719123000298"},{"title":"All models | OpenAI API","url":"https://developers.openai.com/api/docs/models/all"}]

Based on the web search results, I found relevant information about Logic-LM and FOLIO accuracy metrics. Here's what I found:

According to a table from LOGIC-LM++: Multi-Step Refinement for Symbolic Formulations, the accuracy results on FOLIO show GPT-3.5 Turbo achieving 45.09% with Standard prompting, 57.35% with Chain-of-Thought (CoT), and 62.80% with Logic-LM, compared to GPT-4 achieving 69.11% with Standard, 70.58% with CoT, and 78.92% with Logic-LM.

Additionally, in the original FOLIO paper, GPT-3.5 achieves 58.34% accuracy on the FOLIO test set, while Logic-LM with GPT-4 achieves more than a 13% increase over few-shot prompting GPT-4.

The search results indicate that the specific accuracy figures of 58, 62, and 67 you mentioned align with results from Logic-LM studies on the FOLIO dataset, showing performance improvements when using Logic-LM methodology compared to standard and chain-of-thought prompting approaches on both GPT-3.5 and GPT-4 models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a76137f-f1a6-4c72-a482-49362938cd18",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "ca298930-53f6-4998-b581-a97012c9ac98",
  "sourceToolAssistantUUID": "9a76137f-f1a6-4c72-a482-49362938cd18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-10T21:13:06.210Z_

<details><summary>↩ Tool result · `toolu_01D4MiMZpwBjE7JQXzXqGukK`</summary>

```text
Web search results for query: ""pushing boundaries" "formal logic verification" FOLIO accuracy 2026"

Links: [{"title":"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models","url":"https://arxiv.org/html/2601.22642"},{"title":"[2601.22642] Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification","url":"https://arxiv.org/abs/2601.22642"},{"title":"Formal Verification of Transcompiled Mobile Applications Using First-Order Logic | MDPI","url":"https://www.mdpi.com/2227-7080/13/12/580"},{"title":"LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification","url":"https://arxiv.org/html/2602.21044v1"},{"title":"Frontiers | Formal methods for safety-critical machine learning: a systematic literature review","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1749956/full"},{"title":"Alignment Methods for Formal Logical Reasoning","url":"https://aclanthology.org/2025.mathnlp-main.8.pdf"},{"title":"Formal Verification – Why It Matters | PQShield","url":"https://pqshield.com/formal-verification-why-it-matters/"},{"title":"Verification Horizons","url":"https://verificationacademy.com/verification-horizons/"},{"title":"The Future For Formal Verification","url":"https://semiengineering.com/the-future-for-formal-verification/"},{"title":"Formal Methods in Industry | Formal Aspects of Computing","url":"https://dl.acm.org/doi/full/10.1145/3689374"}]

Based on the web search results, here are the key findings related to your query about "pushing boundaries," "formal logic verification," and FOLIO accuracy in 2026:

## Main Research Paper

A research paper from January 2026 titled "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models" demonstrates that a formal verification framework substantially enhances reasoning accuracy, highlighting the potential of formal verification to push the performance boundaries of LLM reasoning.

Extensive evaluation on six benchmarks spanning mathematical, logical, and general reasoning demonstrates that their 7B and 14B models outperform state-of-the-art baselines by average margins of 10.4% and 14.2%.

## Framework Details

The research introduces a formal logic verification-guided training framework comprising two stages: Supervised Fine-tuning (SFT) employing a hierarchical data synthesis pipeline with execution-based validation, and Reinforcement Learning (RL) utilizing Group Relative Policy Optimization (GRPO) with a composite reward function to enforce structural integrity and penalize logical fallacies.

## FOLIO Benchmark

The FOLIO benchmark is referenced in the search results as part of the broader landscape of logical reasoning datasets. FOLIO is characterized as having symbolic notation, a depth of 3.4 on average, 1 path, and 1.0 reuse ratio, used for binary evaluation tasks without stepwise evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "825c0a3c-75b1-4a71-8d8f-874c62e1217f",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "a4e52f02-ad73-4497-8f29-49c1c774095b",
  "sourceToolAssistantUUID": "825c0a3c-75b1-4a71-8d8f-874c62e1217f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-10T21:13:11.154Z_

<details><summary>↩ Tool result · `toolu_01GV5d3V9ESETfspdcbq7jwZ`</summary>

```text
Web search results for query: "FOLIO dataset GPT-4 accuracy 72 74 76 78 80 percent benchmark results"

Links: [{"title":"GPT-4 shows comparable performance to human examiners in ranking open-text answers | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-21572-8"},{"title":"GPT-4 Technical Report","url":"https://arxiv.org/html/2303.08774v6"},{"title":"GPT-4 | OpenAI","url":"https://openai.com/index/gpt-4-research/"},{"title":"GPT-4 Technical Report OpenAI∗ Abstract","url":"https://cdn.openai.com/papers/gpt-4.pdf"},{"title":"Full article: Evaluating large language models on geospatial tasks: a multiple geospatial task benchmarking study","url":"https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2480268"},{"title":"Evaluation of the performance of GPT-3.5 and GPT-4 on the Polish Medical Final Examination | Scientific Reports","url":"https://www.nature.com/articles/s41598-023-46995-z"},{"title":"GPT 4.5 Released: Here Are the Benchmarks","url":"https://www.helicone.ai/blog/gpt-4.5-benchmarks"},{"title":"GPT-ImgEval: A Comprehensive Benchmark for Diagnosing GPT4o in Image Generation","url":"https://arxiv.org/html/2504.02782v1"},{"title":"GPT-4 as an X data annotator: Unraveling its performance on a stance classification task - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11326574/"},{"title":"Introducing GPT-4.1 in the API | OpenAI","url":"https://openai.com/index/gpt-4-1/"}]

The search results don't contain specific information about the FOLIO dataset with the exact accuracy percentages you mentioned (72, 74, 76, 78, 80%). Let me search more specifically for the FOLIO dataset.

Links: [{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - DEV Community","url":"https://dev.to/aimodels-fyi/folio-natural-language-reasoning-with-first-order-logic-3hb1"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"[PDF] FOLIO: Natural Language Reasoning with First-Order Logic | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FOLIO:-Natural-Language-Reasoning-with-First-Order-Han-Schoelkopf/5581bf85386737bd3378eec68189759a05280bea"},{"title":"GitHub - gblackout/LogicLLaMA: Large language model and dataset for natural language to first-order logic translation","url":"https://github.com/gblackout/LogicLLaMA"}]

Let me search for more specific accuracy numbers from the FOLIO paper.

Links: [{"title":"Performance of ChatGPT-3.5 and GPT-4 in national licensing examinations for medicine, pharmacy, dentistry, and nursing: a systematic review and meta-analysis - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11406751/"},{"title":"GPT-4 performance on querying scientific publications: reproducibility, accuracy, and impact of an instruction sheet | BMC Medical Research Methodology | Springer Nature Link","url":"https://link.springer.com/article/10.1186/s12874-024-02253-y"},{"title":"GPT-4 performance on querying scientific publications: reproducibility, accuracy, and impact of an instruction sheet - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11197181/"},{"title":"GPT-4 Technical Report","url":"https://arxiv.org/html/arXiv:2303.08774v6"},{"title":"Comparison of the Performance of GPT-3.5 and GPT-4 With That of Medical Students on the Written German Medical Licensing Examination: Observational Study - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10884900/"},{"title":"GPT-4 Technical Report OpenAI∗ Abstract","url":"https://cdn.openai.com/papers/gpt-4.pdf"},{"title":"Comparative analysis of GPT-4-based ChatGPT’s diagnostic performance with radiologists using real-world radiology reports of brain tumors | European Radiology | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00330-024-11032-8"},{"title":"GPT-4 in Education: Evaluating Aptness, Reliability, and Loss of Coherence in Solving Calculus Problems and Grading Submissions | International Journal of Artificial Intelligence in Education | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40593-024-00403-3"},{"title":"Comparison table for the accuracy of GPT-3.5 and GPT-4 | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Comparison-table-for-the-accuracy-of-GPT-35-and-GPT-4_tbl1_370547416"},{"title":"GPT-4 performance on querying scientific publications: reproducibility, accuracy, and impact of an instruction sheet - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/38918736/"}]

Let me search for the specific FOLIO paper with benchmark results table.

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"}]

Based on my search results, I found information about the FOLIO dataset and GPT-4's performance on it. However, I should note that the specific accuracy percentages you mentioned (72, 74, 76, 78, 80 percent) don't appear in the search results I retrieved. Instead, here's what the research shows:

FOLIO is a human-annotated dataset for natural language reasoning equipped with first-order logic (FOL) annotations, consisting of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

Regarding GPT-4's performance on FOLIO:

GPT-3.5 achieves 58.34% accuracy, while GPT-4 achieves the best results among GPT series models. Chain-of-thought prompting achieves more than a 4% increase over GPT-4.

The results show that a subset of FOLIO presents a challenge for one of the most capable Large Language Models publicly available, GPT-4. BERT-large has a 2.2% improvement over BERT-base, RoBERTa-large improves 3.1% over BERT-large, and Flan-T5-Large achieves the highest performance in the fine-tuning setting with 65.7% accuracy.

If you're looking for specific benchmark results with the exact percentages you mentioned, those particular figures don't appear in the publicly available search results for the FOLIO dataset paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "146b6c15-7b24-4c07-bcd4-a0711071435a",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "db471ff1-a505-4fc1-a612-f1b8e83d3d76",
  "sourceToolAssistantUUID": "146b6c15-7b24-4c07-bcd4-a0711071435a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-10T21:13:13.352Z_

Now let me get the Logic-LM++ and the "Pushing Boundaries" paper details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db471ff1-a505-4fc1-a612-f1b8e83d3d76",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaVPxiN8ZB9VtcKAGP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f57be754-fd05-456a-83f2-068ce4fa18d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaRpQ8G54rvHrSu8dZPwko",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1674,
      "cache_creation_input_tokens": 3294,
      "cache_read_input_tokens": 35312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3294,
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

_source line 82 · 2026-05-10T21:13:15.894Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015EcTyaV1wSDs4212jFpsTL`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.02514v1",
  "prompt": "Extract ALL FOLIO accuracy numbers from this LOGIC-LM++ paper. List every accuracy number for each approach (Standard, CoT, Logic-LM, Logic-LM++) and each model (GPT-3.5, GPT-4, etc.) on FOLIO. Include the full comparison table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f57be754-fd05-456a-83f2-068ce4fa18d7",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaVPxiN8ZB9VtcKAGP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32d6e1ca-6a4d-4c39-b965-30d8cbc301e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaRpQ8G54rvHrSu8dZPwko",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1674,
      "cache_creation_input_tokens": 3294,
      "cache_read_input_tokens": 35312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3294,
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

_source line 83 · 2026-05-10T21:13:17.839Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SV6LsX6KifhQxGSyt5bKpw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.22642",
  "prompt": "Extract the paper title, authors, date, key technique, and any FOLIO accuracy numbers. What accuracy do the 7B and 14B models achieve on FOLIO specifically? List all benchmark results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32d6e1ca-6a4d-4c39-b965-30d8cbc301e7",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaVPxiN8ZB9VtcKAGP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01e87c37-29c6-46c0-84d6-81618db8dea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaRpQ8G54rvHrSu8dZPwko",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1674,
      "cache_creation_input_tokens": 3294,
      "cache_read_input_tokens": 35312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3294,
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

_source line 84 · 2026-05-10T21:13:18.701Z_

<details><summary>↩ Tool result · `toolu_015EcTyaV1wSDs4212jFpsTL`</summary>

```text
# FOLIO Accuracy Results from LOGIC-LM++

Based on Table 1 in the paper, here are all the FOLIO accuracy numbers:

## GPT-3.5 Turbo
- Standard Prompting: 45.09%
- Chain of Thought (CoT): 57.35%
- Logic-LM: 62.80%
- Logic-LM++: 62.25%

## GPT-4
- Standard Prompting: 69.11%
- Chain of Thought (CoT): 70.58%
- Logic-LM: 78.92%
- Logic-LM++: 84.80%

## Key Finding

The paper reports that "Logic-LM++ show an average improvement of 13.5% on standard prompting, 11% on chain of thought prompting and 5% on Logic-LM." The most substantial gains appear with GPT-4, where Logic-LM++ achieved 84.80% accuracy compared to Logic-LM's 78.92%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32d6e1ca-6a4d-4c39-b965-30d8cbc301e7",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "f7c4912d-b445-4c59-9fd9-eea8f6d9d354",
  "sourceToolAssistantUUID": "32d6e1ca-6a4d-4c39-b965-30d8cbc301e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-10T21:13:18.766Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PunzPg4i4MfFkBCS661owg`</summary>

```json
{
  "query": "LOGICPO preference optimization FOLIO accuracy 2025 Phi-3.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7c4912d-b445-4c59-9fd9-eea8f6d9d354",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaVPxiN8ZB9VtcKAGP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "615e6532-23b1-45ca-bc49-36c3aa8a61a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaRpQ8G54rvHrSu8dZPwko",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1674,
      "cache_creation_input_tokens": 3294,
      "cache_read_input_tokens": 35312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3294,
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

_source line 86 · 2026-05-10T21:13:19.109Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RR3S9uvTtjiwb9SkCgLt88`</summary>

```json
{
  "query": "counterexample guided abstraction refinement natural language inference NLI 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "615e6532-23b1-45ca-bc49-36c3aa8a61a3",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaVPxiN8ZB9VtcKAGP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52892ecb-d1d2-48d8-93c4-f2a6530439c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaRpQ8G54rvHrSu8dZPwko",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1674,
      "cache_creation_input_tokens": 3294,
      "cache_read_input_tokens": 35312,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3294
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1674,
          "output_tokens": 390,
          "cache_read_input_tokens": 35312,
          "cache_creation_input_tokens": 3294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3294,
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

_source line 87 · 2026-05-10T21:13:22.530Z_

<details><summary>↩ Tool result · `toolu_01SV6LsX6KifhQxGSyt5bKpw`</summary>

```text
# Paper Analysis

**Title:** "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification"

**Authors:** Chuxue Cao, Jinluan Yang, Haoran Li, Kunhao Pan, Zijian Zhao, Zhengyu Chen, Yuchen Tian, Lijun Wu, Conghui He, Sirui Han, Yike Guo

**Date:** Submitted January 30, 2026

**Key Technique:** The framework "dynamically interleaves formal symbolic verification with the natural language generation process," combining supervised fine-tuning and policy optimization in a two-stage training approach.

**FOLIO-Specific Results:** The webpage does not provide FOLIO benchmark performance numbers for the 7B or 14B models.

**Overall Benchmark Results:** The abstract states the models "outperform state-of-the-art baselines by average margins of 10.4% and 14.2%, respectively" across six benchmarks covering mathematical, logical, and general reasoning. However, individual benchmark breakdowns—including FOLIO specifically—are not detailed in this excerpt.

**Note:** Complete benchmark results appear in the full paper PDF, which would require accessing the document directly for specific dataset performance metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01e87c37-29c6-46c0-84d6-81618db8dea0",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "f94f5bd7-4bf6-4ee0-9dce-0af4c993b639",
  "sourceToolAssistantUUID": "01e87c37-29c6-46c0-84d6-81618db8dea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-10T21:13:25.793Z_

<details><summary>↩ Tool result · `toolu_01RR3S9uvTtjiwb9SkCgLt88`</summary>

```text
Web search results for query: "counterexample guided abstraction refinement natural language inference NLI 2025 2026"

Links: [{"title":"Natural Language Inference (NLI)","url":"https://www.emergentmind.com/topics/natural-language-inference-nli"},{"title":"25 Years of Counterexample Guided Abstraction Refinement – ACM SIGBED","url":"https://sigbed.org/2026/01/13/fmsdcfp/"},{"title":"Model Checking as Program Verification by Abstract Interpretation","url":"https://drops.dagstuhl.de/storage/00lipics/lipics-vol348-concur2025/LIPIcs.CONCUR.2025.8/LIPIcs.CONCUR.2025.8.pdf"},{"title":"Semantic knowledge abstraction: Consistent reasoning in large language models for natural language inference - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705125018635"},{"title":"Guiding Natural Language Inference through Lexical Inference Types","url":"https://arxiv.org/html/2308.03581v2"},{"title":"[1006.5896] Counterexample Guided Abstraction Refinement Algorithm for Propositional Circumscription","url":"https://arxiv.org/abs/1006.5896"},{"title":"Counterexample-Guided Abstraction Refinement for Assumption-based Argumentation","url":"https://proceedings.kr.org/2025/67/kr2025-0067-lagniez-et-al.pdf"},{"title":"Counterexample-guided abstraction refinement - Wikipedia","url":"https://en.wikipedia.org/wiki/Counterexample-guided_abstraction_refinement"},{"title":"Natural Language Inference - Practical Guide 2025 | ShadeCoder","url":"https://www.shadecoder.com/topics/natural-language-inference-a-comprehensive-guide-for-2025"},{"title":"Inferring Latent Intentions: Attributional Natural Language Inference in LLM Agents","url":"https://arxiv.org/html/2601.08742"}]

Based on the search results, here's what I found regarding counterexample-guided abstraction refinement and natural language inference in 2025-2026:

## Counterexample-Guided Abstraction Refinement (CEGAR)

Counterexample-guided abstraction refinement (CEGAR) is a technique for symbolic model checking. While this is a well-established technique in formal methods and verification, the search results show it is still an active area of research. There is a special issue in Springer FMSD (Formal Methods in System Design) dedicated to "25 Years of Counterexample Guided Abstraction Refinement" with a submission deadline of February 28, 2026.

## Recent Developments in NLI (2025-2026)

Recent work in natural language inference has been exploring semantic abstraction approaches. A 2026 paper introduces the Semantic Knowledge Abstraction (SKA) methodological framework to discover and compensate for semantic knowledge gaps of Large Language Models (LLMs) in Natural Language Inference (NLI). The method guides the LLM's reasoning process, revealing its weaknesses and inconsistencies, which are compensated for by explainable decision strategies that improve NLI accuracy by up to 15 % for some models.

However, the search results do not show a direct application of counterexample-guided abstraction refinement specifically to NLI tasks in 2025-2026. The CEGAR technique appears to remain primarily in the formal methods domain, while NLI research is pursuing alternative abstraction-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52892ecb-d1d2-48d8-93c4-f2a6530439c4",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "79d656f4-9f49-4e52-9677-4df210c94be6",
  "sourceToolAssistantUUID": "52892ecb-d1d2-48d8-93c4-f2a6530439c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-10T21:13:26.165Z_

<details><summary>↩ Tool result · `toolu_01PunzPg4i4MfFkBCS661owg`</summary>

```text
Web search results for query: "LOGICPO preference optimization FOLIO accuracy 2025 Phi-3.5"

Links: [{"title":"[2506.18383] LOGICPO: Efficient Translation of NL-based Logical Problems to FOL using LLMs and Preference Optimization","url":"https://arxiv.org/abs/2506.18383"},{"title":"arXiv:2506.18383v1 [cs.LG] 23 Jun 2025","url":"https://arxiv.org/pdf/2506.18383"},{"title":"[2506.18383v1] LOGICPO: Efficient Translation of NL-based Logical Problems to FOL using LLMs and Preference Optimization","url":"https://arxiv.org/abs/2506.18383v1"},{"title":"Efficient Conversion of NL-based Logical Problems to FOL using LLMs and Preference Optimization | OpenReview","url":"https://openreview.net/forum?id=oWEKBFsJ4Q"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=1875&show=2000"},{"title":"PREFERENCE OPTIMIZATION FOR REASONING WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf"},{"title":"phi3","url":"https://ollama.com/library/phi3"},{"title":"Listwise Preference Optimization through Learning-to-Rank","url":"https://aclanthology.org/2025.naacl-long.121.pdf"},{"title":"Fine-Tuning Phi-3.5 on E-Commerce Classification Dataset | DataCamp","url":"https://www.datacamp.com/tutorial/fine-tuning-phi-3-5"},{"title":"T-REG: Preference Optimization with Token-Level Reward ...","url":"https://aclanthology.org/2025.acl-long.1353.pdf"}]

Based on the search results, here's what I found about LOGICPO, preference optimization, FOLIO accuracy, and Phi-3.5:

## Overview

LOGICPO is a new supervised and preference optimization dataset introduced to help LLMs learn to parse and represent natural language problems as logical programs, using techniques such as Direct Preference Optimization (DPO) and Kahneman-Tversky optimization (KTO) to finetune open-source LLMs.

## Performance Results

The best model with Phi-3.5 consistently outperforms GPT-3.5-turbo's (8-shot) by producing 10% more logically correct outputs and with 14% less syntax errors.

## FOLIO Dataset Performance

The Phi-3.5 models achieve the highest syntactic correctness when evaluated on the FOLIO dataset. Additionally, the best finetuned models obtain similar scores (F1) across various tables, bolstering the generalizability of LOGICPO, and the high improvement of the preference optimized models underlines the generalizability of the LOGICPO dataset even when tested on different datasets.

## Key Improvements

There is a huge decrease in syntax errors in these models compared to baselines, with an 83.33% decrease from Logic-LM and 61.11% decrease from LINC, leading to a huge jump in executability of the programs generated by the models.

The research appears to have been published in June 2025 as an arXiv paper focusing on improving LLMs' ability to translate natural language logical problems into First Order Logic (FOL).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "615e6532-23b1-45ca-bc49-36c3aa8a61a3",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "b150ae61-9e30-42a2-8f41-b459c6d0e314",
  "sourceToolAssistantUUID": "615e6532-23b1-45ca-bc49-36c3aa8a61a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-10T21:13:31.740Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KZEJDLJVBRRVfcqzNEjkcW`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.22642",
  "prompt": "Extract ALL benchmark accuracy results from this paper. Specifically look for FOLIO results. List accuracy for each model size (7B, 14B) and each benchmark dataset tested. Look for tables with numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b150ae61-9e30-42a2-8f41-b459c6d0e314",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaWWCHqzPvNcysrSrBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0627404a-debe-4b38-8c58-c0c3300061a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01353qJsMWzwEKRFVESPCZV7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 3568,
      "cache_read_input_tokens": 38606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3568,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-10T21:13:33.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015AzdDxVGV1HHSLAQDU9DYK`</summary>

```json
{
  "query": "\"Alignment Methods for Formal Logical Reasoning\" FOLIO accuracy DPO 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0627404a-debe-4b38-8c58-c0c3300061a6",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaWWCHqzPvNcysrSrBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c35e055-5e78-48e1-b62f-d123c010c92b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01353qJsMWzwEKRFVESPCZV7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 3568,
      "cache_read_input_tokens": 38606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3568,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-10T21:13:33.561Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017fiJeHhrt147nBAg22Ffp8`</summary>

```json
{
  "query": "iterative solver feedback loop LLM FOL translation correction FOLIO 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c35e055-5e78-48e1-b62f-d123c010c92b",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaWWCHqzPvNcysrSrBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4c3df0a-43f9-4156-b366-1fc6afc7075c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01353qJsMWzwEKRFVESPCZV7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 3568,
      "cache_read_input_tokens": 38606,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3568
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 935,
          "output_tokens": 237,
          "cache_read_input_tokens": 38606,
          "cache_creation_input_tokens": 3568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3568,
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

_source line 93 · 2026-05-10T21:13:38.792Z_

<details><summary>↩ Tool result · `toolu_01KZEJDLJVBRRVfcqzNEjkcW`</summary>

```text
# Benchmark Accuracy Results from Paper

Based on the content provided, here are the key accuracy results:

## 7B Model Performance (FLV-RL)
- KOR-Bench (Logical): 51.0%
- BBH (Logical): 70.0%
- MATH-500 (Mathematical): 78.6%
- AIME24 (Mathematical): 20.8%
- GPQA-Diamond (General): 35.4%
- TheoremQA (General): 55.7%
- **Average: 51.9%**

## 14B Model Performance (FLV-RL)
- KOR-Bench (Logical): 57.0%
- BBH (Logical): 78.0%
- MATH-500 (Mathematical): 81.4%
- AIME24 (Mathematical): 30.2%
- GPQA-Diamond (General): 41.4%
- TheoremQA (General): 63.5%
- **Average: 58.6%**

**Note:** The paper does not include FOLIO results. The benchmarks tested span three reasoning domains—logical, mathematical, and general—but FOLIO is not among the evaluation datasets presented in the tables or text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0627404a-debe-4b38-8c58-c0c3300061a6",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "ee910625-f7de-435a-aa2a-48753a80b495",
  "sourceToolAssistantUUID": "0627404a-debe-4b38-8c58-c0c3300061a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-10T21:13:40.479Z_

<details><summary>↩ Tool result · `toolu_015AzdDxVGV1HHSLAQDU9DYK`</summary>

```text
Web search results for query: ""Alignment Methods for Formal Logical Reasoning" FOLIO accuracy DPO 2025"

Links: [{"title":"Alignment Methods for Formal Logical Reasoning","url":"https://aclanthology.org/2025.mathnlp-main.8.pdf"},{"title":"Into The Limits of Logic: Alignment Methods for Formal Logical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.mathnlp-main.8/"},{"title":"Alignment-Weighted DPO: A principled reasoning approach to improve safety alignment","url":"https://arxiv.org/html/2602.21346"},{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"Insights into Alignment: Evaluating DPO and its Variants Across Multiple Tasks - ACL Anthology","url":"https://aclanthology.org/2025.acl-srw.26/"},{"title":"1 Reasoning Beyond Limits: Advances and Open Problems for LLMs","url":"https://arxiv.org/pdf/2503.22732"},{"title":"Adaptive Thinking Mode Switching for Efficient Reasoning","url":"https://aclanthology.org/2025.findings-emnlp.310.pdf"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"Evaluating DPO and its Variants Across Multiple Tasks","url":"https://aclanthology.org/2025.acl-srw.26.pdf"},{"title":"DaGRPO: Rectifying Gradient Conflict in Reasoning via ...","url":"https://arxiv.org/pdf/2512.06337"}]

I found research on alignment methods for formal logical reasoning. Here's what the search revealed:

A 2025 paper implements Large Language Model Alignment algorithms to formal logic reasoning tasks involving natural-language (NL) to first-order logic (FOL) translation, formal logic inference, and premise retranslation. These methodologies were implemented using task-specific preference datasets created based on the FOLIO datasets and LLM generations, with alignment based on DPO (Direct Preference Optimization).

The DPO algorithm was implemented and tested on off-the-shelf and pre-aligned models, showing promising results for higher quality NL-FOL parsing, as well as general alignment strategies. The results show that LLMs still struggle with logical inference, however alignment benefits semantic parsing and retranslation of results from formal logic to natural language.

Additionally, a new similarity metric (LogicSim) was introduced that measures logic-relevant information such as premise count and overlap between answers and expands evaluation of NL-FOL translation pipelines.

The research appears to be published in the proceedings of The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025), suggesting this is very recent work in the field addressing the intersection of alignment methods, formal logical reasoning, and the FOLIO dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c35e055-5e78-48e1-b62f-d123c010c92b",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "61ee5f9e-3a30-4b5c-8ca7-7e7c4c5e7209",
  "sourceToolAssistantUUID": "6c35e055-5e78-48e1-b62f-d123c010c92b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-10T21:13:41.697Z_

<details><summary>↩ Tool result · `toolu_017fiJeHhrt147nBAg22Ffp8`</summary>

```text
Web search results for query: "iterative solver feedback loop LLM FOL translation correction FOLIO 2025 2026"

Links: [{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"LLMLOOP: Improving LLM-Generated Code and Tests ...","url":"https://valerio-terragni.github.io/assets/pdf/ravi-icsme-2025.pdf"},{"title":"Alignment Methods for Formal Logical Reasoning","url":"https://aclanthology.org/2025.mathnlp-main.8.pdf"},{"title":"LTRAG: Enhancing Autoformalization and Self-refinement ...","url":"https://aclanthology.org/2025.findings-acl.126.pdf"},{"title":"Published as a conference paper at ICLR 2026 MAD-LOGIC:","url":"https://openreview.net/pdf/9efc07a23e82c4f96fe3a0b53efc9cc078940f48.pdf"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"S2R: Teaching LLMs to Self-verify and Self-correct via ...","url":"https://aclanthology.org/2025.acl-long.1104.pdf"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2509.22819"},{"title":"Do LLMs Really Struggle at NL-FOL Translation? Revealing their Strengths via a Novel Benchmarking Strategy","url":"https://arxiv.org/html/2511.11816v1"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"}]

Based on the web search results, I found several relevant papers and research related to your query on iterative solver feedback loops, LLM-to-FOL translation, and error correction. Here are the key findings:

## Logic-LM and Self-Refinement Feedback Loop

Logic-LM (Pan et al. 2023) formulates natural-language logical problems into symbolic representations (e.g., FOL, CSP, SAT) and delegates inference to external solvers such as Prover9 and Z3, with a self-refinement loop that leverages solver feedback to iteratively correct symbolic errors.

## FOLIO Dataset and Related Work

FOLIO is a dataset for natural language reasoning with first-order logic, and it has been central to recent work on LLM-FOL translation. FOLIO judges translations via an SMT solver's verdict, which relates to the iterative correction paradigm you're interested in.

## LTRAG Framework (2025)

Recent work like LTRAG enhances autoformalization and self-refinement for logical reasoning tasks. The framework shows performance comparison on FOLIO and AR-LSAT datasets, with a Refiner module for error correction.

## Multi-Agent Approaches

In the translation stage, multiple agents are employed, with each agent responsible for translating NL to a specific SL, and then correcting translation errors through mutual refinement, ultimately enhancing the accuracy of the translation.

## Theorem Proving with Feedback

Feedback from Lean is used to iteratively refine incorrect proofs, demonstrating how formal verification systems can drive iterative refinement loops in LLM-based reasoning.

These approaches collectively represent the cutting edge of combining LLMs with symbolic reasoning and formal verification systems through iterative feedback mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4c3df0a-43f9-4156-b366-1fc6afc7075c",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "0565fdb7-1bd6-4ffb-ac3e-c37dc426127a",
  "sourceToolAssistantUUID": "c4c3df0a-43f9-4156-b366-1fc6afc7075c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-10T21:13:46.007Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fum2buT6GLU3GeGPsDxeSF`</summary>

```json
{
  "url": "https://openreview.net/pdf/9efc07a23e82c4f96fe3a0b53efc9cc078940f48.pdf",
  "prompt": "Extract the paper title, authors, date, key technique, and ALL FOLIO accuracy numbers. This appears to be MAD-LOGIC, an ICLR 2026 paper. What models are tested? What accuracy does each achieve on FOLIO? Include the full results table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0565fdb7-1bd6-4ffb-ac3e-c37dc426127a",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaXeZcGAXTA2kNf3Lge",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "180018bc-3197-47cc-9115-cbb771d3fd1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2kUWVb6LfWecv5X6szTdW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3298,
      "cache_read_input_tokens": 42174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3298,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-10T21:13:46.176Z_

<details><summary>↩ Tool result · reported error · `toolu_01Fum2buT6GLU3GeGPsDxeSF`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "180018bc-3197-47cc-9115-cbb771d3fd1e",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "24ab80ed-852d-4a4e-b899-97b6bbaea093",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "180018bc-3197-47cc-9115-cbb771d3fd1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-10T21:13:46.626Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BdNQ6nP3EPVYZahYjKrYLm`</summary>

```json
{
  "query": "MAD-LOGIC FOLIO multi-agent debate logical reasoning ICLR 2026 accuracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24ab80ed-852d-4a4e-b899-97b6bbaea093",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaXeZcGAXTA2kNf3Lge",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0a9f689-e853-483b-b51c-ecdb6c53393a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2kUWVb6LfWecv5X6szTdW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3298,
      "cache_read_input_tokens": 42174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3298,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-10T21:13:52.967Z_

<details><summary>↩ Tool result · `toolu_01BdNQ6nP3EPVYZahYjKrYLm`</summary>

```text
Web search results for query: "MAD-LOGIC FOLIO multi-agent debate logical reasoning ICLR 2026 accuracy"

Links: [{"title":"ICLR Poster MAD-Logic: Multi-Agent Debate Enhances Symbolic Translation and Reasoning","url":"https://iclr.cc/virtual/2026/poster/10007131"},{"title":"MAD-LOGIC: MULTI-AGENT DEBATE ENHANCES ...","url":"https://openreview.net/pdf/9efc07a23e82c4f96fe3a0b53efc9cc078940f48.pdf"},{"title":"GitHub - HongduanTian/MAD-MM: [ICLR 2026] \"Multi-Agent Debate with Memory Masking\" · GitHub","url":"https://github.com/HongduanTian/MAD-MM"},{"title":"MAD-Logic: Multi-Agent Debate Enhances Symbolic Translation and Reasoning | OpenReview","url":"https://openreview.net/forum?id=rdE9qxGfIv"},{"title":"ICLR Poster Multi-Agent Debate with Memory Masking","url":"https://iclr.cc/virtual/2026/poster/10010659"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"ICLR Poster Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate","url":"https://iclr.cc/virtual/2025/poster/28079"},{"title":"ENCOURAGING CRITICAL THINKING FOR MULTI","url":"https://openreview.net/pdf/e4e36f9dc875aba53ed372517357cb765839bfa5.pdf"},{"title":"Free-MAD: Consensus-Free Multi-Agent Debate","url":"https://arxiv.org/html/2509.11035v1"},{"title":"GitHub - MraDonkey/DMAD: [ICLR 2025] Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate · GitHub","url":"https://github.com/MraDonkey/DMAD"}]

I found relevant information about MAD-LOGIC and FOLIO. Here are the key findings:

## MAD-LOGIC Overview

MAD-LOGIC is the first multi-agent debate framework to leverage the strengths of different symbolic languages and reasoning methods, achieving better performance in both translation and reasoning stages.

## How It Works

In the translation stage, multiple agents translate natural language into different symbolic languages and refine translations through debate. In the reasoning stage, multiple agents based on symbolic language (obtained by the corresponding solver) and natural language debate multiple rounds, with the final answer determined by majority vote.

## FOLIO Dataset

The method was evaluated on three real-world benchmarks including FOLIO (along with AR-LSAT and Chinese LogiQA-V2).

## Performance and Efficiency

To address the inefficiency of multi-agent debates, the method introduces an adaptive sparse communication strategy that prunes unnecessary interactions based on agent confidence and information gains. Extensive experiments on three datasets show that the method enhances logical QA performance while reducing computational cost.

However, the search results do not contain specific accuracy numbers for the FOLIO dataset. For detailed accuracy metrics, you would need to access the full paper on OpenReview or ICLR 2026's official website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0a9f689-e853-483b-b51c-ecdb6c53393a",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "539d548f-3f99-4518-bb1c-753fe720680b",
  "sourceToolAssistantUUID": "d0a9f689-e853-483b-b51c-ecdb6c53393a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-10T21:14:00.060Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01838bfp5zyr9M1QC2EsjPfh`</summary>

```json
{
  "url": "https://openreview.net/forum?id=rdE9qxGfIv",
  "prompt": "Extract ALL FOLIO accuracy numbers from the MAD-LOGIC paper. What specific accuracy does each approach achieve on FOLIO? What models are used? Include any comparison tables with baseline results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "539d548f-3f99-4518-bb1c-753fe720680b",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaYUqVRZFA9GMEoxVeX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00b86006-a60e-4886-82f2-42b2acf6855a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147Wv62SCKSSQk6n2rCNe8o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 45472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1114,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-10T21:14:01.214Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JVnh1jWBpR4EEavWEf98mC`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.22819",
  "prompt": "Extract the paper title, authors, date, key technique, and ALL FOLIO accuracy numbers. This appears to be an ICLR 2026 paper. What models are tested? What accuracy does each achieve on FOLIO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b86006-a60e-4886-82f2-42b2acf6855a",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaYUqVRZFA9GMEoxVeX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8fe9d46-2391-45f3-afac-d5a879d74e8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147Wv62SCKSSQk6n2rCNe8o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 45472,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1114
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 45472,
          "cache_creation_input_tokens": 1114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1114,
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

_source line 102 · 2026-05-10T21:14:01.228Z_

<details><summary>↩ Tool result · reported error · `toolu_01JVnh1jWBpR4EEavWEf98mC`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8fe9d46-2391-45f3-afac-d5a879d74e8a",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "2f89f3bd-b966-4f19-8778-b2b01eeaaf70",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "f8fe9d46-2391-45f3-afac-d5a879d74e8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-10T21:14:02.346Z_

<details><summary>↩ Tool result · `toolu_01838bfp5zyr9M1QC2EsjPfh`</summary>

```text
I cannot extract specific FOLIO accuracy numbers from the provided content. The webpage excerpt contains only the paper's abstract and metadata from OpenReview, which does not include detailed experimental results, accuracy metrics, model specifications, or comparison tables.

To obtain this information, you would need to access the full paper PDF, which is available for download on the OpenReview page (indicated by the "Download PDF" button). The abstract mentions that "extensive experiments on three datasets show that our method enhances logical QA performance," but specific numerical results are not provided in the publicly visible portion shown here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00b86006-a60e-4886-82f2-42b2acf6855a",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "0f724f1b-2560-4a53-bf48-766e6aba8c0e",
  "sourceToolAssistantUUID": "00b86006-a60e-4886-82f2-42b2acf6855a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-10T21:14:07.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ti1ux4wxPactnRUF2DFk6c`</summary>

```json
{
  "query": "MAD-LOGIC FOLIO accuracy 80 85 results multi-agent symbolic translation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f724f1b-2560-4a53-bf48-766e6aba8c0e",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaZKHYEYNgQ8zAfP8n3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eed08aa9-97c5-4258-81c6-757455a8957a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCCXFFQo42L68HG1p7HZNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 396,
      "cache_read_input_tokens": 46586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 396,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-10T21:14:08.988Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QkUAS7XDU9TNWsMTUMCb8c`</summary>

```json
{
  "url": "https://openreview.net/forum?id=6WQZCc9qQ1",
  "prompt": "Extract ALL FOLIO accuracy numbers from the LTRAG paper reviews or abstract. What accuracy does LTRAG achieve on FOLIO compared to baselines like Logic-LM and LINC?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eed08aa9-97c5-4258-81c6-757455a8957a",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaZKHYEYNgQ8zAfP8n3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35ea0541-8a5d-4d94-9fa8-5f4eed8d42bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCCXFFQo42L68HG1p7HZNw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 396,
      "cache_read_input_tokens": 46586,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 396
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 39,
          "output_tokens": 186,
          "cache_read_input_tokens": 46586,
          "cache_creation_input_tokens": 396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 396,
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

_source line 106 · 2026-05-10T21:14:11.538Z_

<details><summary>↩ Tool result · `toolu_01QkUAS7XDU9TNWsMTUMCb8c`</summary>

```text
I cannot extract FOLIO accuracy numbers from the LTRAG paper because the web page content provided only shows the OpenReview login and navigation interface. It does not contain any paper reviews, abstracts, or technical content about LTRAG, FOLIO benchmarks, or comparisons with Logic-LM and LINC baselines.

To find this information, you would need to access the actual LTRAG paper or its reviews on OpenReview.net by navigating to the specific paper page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35ea0541-8a5d-4d94-9fa8-5f4eed8d42bb",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "fe986ca2-ce14-4c21-b752-9ea1dcb5d86d",
  "sourceToolAssistantUUID": "35ea0541-8a5d-4d94-9fa8-5f4eed8d42bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-10T21:14:13.654Z_

<details><summary>↩ Tool result · `toolu_01Ti1ux4wxPactnRUF2DFk6c`</summary>

```text
Web search results for query: "MAD-LOGIC FOLIO accuracy 80 85 results multi-agent symbolic translation"

Links: [{"title":"MAD-Logic: Multi-Agent Debate Enhances Symbolic Translation and Reasoning | OpenReview","url":"https://openreview.net/forum?id=rdE9qxGfIv"},{"title":"MAD-LOGIC: MULTI-AGENT DEBATE ENHANCES ...","url":"https://openreview.net/pdf/9efc07a23e82c4f96fe3a0b53efc9cc078940f48.pdf"},{"title":"ICLR Poster MAD-Logic: Multi-Agent Debate Enhances Symbolic Translation and Reasoning","url":"https://iclr.cc/virtual/2026/poster/10007131"},{"title":"Improving Symbolic Translation of Language Models for Logical Reasoning","url":"https://arxiv.org/html/2601.09446v1"},{"title":"GitHub - teacherpeterpan/Logic-LLM: The project page for \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\" · GitHub","url":"https://github.com/teacherpeterpan/Logic-LLM"},{"title":"Logic-based technologies for multi-agent systems: a systematic literature review | Autonomous Agents and Multi-Agent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10458-020-09478-3"},{"title":"LARGE LANGUAGE MODELS MEET SYMBOLIC ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation","url":"https://arxiv.org/html/2502.06563"},{"title":"Towards symbolic model checking for multi-agent systems via OBDD’S","url":"https://ntrs.nasa.gov/api/citations/20050137709/downloads/20050137709.pdf"}]

Based on the search results, I found information about MAD-Logic, a multi-agent debate framework for symbolic translation and reasoning:

## Overview

MAD-Logic proposes a multi-agent debate framework to leverage the strengths of different symbolic languages (SLs) and reasoning methods, achieving better performance in both translation and reasoning stages.

## Approach

In the translation stage, multiple agents translate natural language into different symbolic languages and refine translations through debate. In the reasoning stage, multiple agents based on symbolic language (obtained by the corresponding solver) and natural language debate multiple rounds, with the final answer determined by majority vote.

## Efficiency Optimization

To address the inefficiency of multi-agent debates, an adaptive sparse communication strategy is introduced that prunes unnecessary interactions based on agent confidence and information gains.

## Results

Extensive experiments on three datasets show that the method enhances logical QA performance while reducing computational cost.

The search results I retrieved don't contain specific accuracy percentages in the 80-85% range that you mentioned. The results focus on the methodology and general improvements rather than those particular benchmark numbers. If you need specific accuracy metrics, you may want to consult the full paper directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eed08aa9-97c5-4258-81c6-757455a8957a",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "3f522fe2-d466-49ef-82ec-d9a8454bd6f4",
  "sourceToolAssistantUUID": "eed08aa9-97c5-4258-81c6-757455a8957a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-10T21:14:17.421Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SttxPH6MF76ffbMEyo2owk`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.09446v1",
  "prompt": "Extract the paper title, authors, date, key technique, and ALL FOLIO accuracy numbers. What models are tested on FOLIO? What are the specific accuracy scores for each method/model?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f522fe2-d466-49ef-82ec-d9a8454bd6f4",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011Cauaa1AA6U4U7BvQg7fRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78c36201-d5ce-40bb-92ab-e70edbb12c8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4ts1ZF5JFSUVqGunDHdAg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 137,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 46982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-10T21:14:18.516Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016Un7qn1QUZMQTKrRKCRNwJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.06563",
  "prompt": "Extract the paper title, authors, date, key technique, and ALL FOLIO accuracy numbers. This appears to be an ICLR 2025 paper about LLMs meeting symbolic provers. What models are tested on FOLIO? What accuracy does each achieve?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78c36201-d5ce-40bb-92ab-e70edbb12c8e",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011Cauaa1AA6U4U7BvQg7fRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8021f7d-85c0-4b95-8a80-b46d2b828839",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4ts1ZF5JFSUVqGunDHdAg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 137,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 46982,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1108
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 137,
          "output_tokens": 248,
          "cache_read_input_tokens": 46982,
          "cache_creation_input_tokens": 1108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1108,
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

_source line 110 · 2026-05-10T21:14:23.238Z_

<details><summary>↩ Tool result · `toolu_01SttxPH6MF76ffbMEyo2owk`</summary>

```text
# Paper Analysis

**Title:** "Improving Symbolic Translation of Language Models for Logical Reasoning"

**Authors:** Ramya Keerthy Thatikonda, Jiuzhou Han, Wray Buntine, Ehsan Shareghi

**Date:** January 14, 2026

**Key Technique:** The authors introduce "incremental inference," a two-stage process that separates predicate generation from full FOL translation, combined with supervised fine-tuning on synthesized data and a verification module for error correction.

## FOLIO Accuracy Results

**Models tested on FOLIO:**
- Gemma-3-4B-Instruct
- Phi-4-mini-Instruct
- Qwen2.5-3B-Instruct
- Qwen3-4B-Instruct-2507

**Accuracy scores by method and model:**

| Model | In-Context Learning | SFT+ | Incremental |
|-------|-------------------|------|-------------|
| Gemma-3-4B | 33.00% | 36.95% | 40.89% |
| Phi-4-mini | 28.08% | 38.92% | 38.92% |
| Qwen2.5-3B | 19.21% | 30.05% | 30.54% |
| Qwen3-4B | 3.45% | 40.39% | 38.42% |

Incremental inference generally improved performance, with the most substantial gains observed for Gemma-3-4B.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78c36201-d5ce-40bb-92ab-e70edbb12c8e",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "79ebee3d-5dbb-46ae-8bd3-2d1d7d5e6238",
  "sourceToolAssistantUUID": "78c36201-d5ce-40bb-92ab-e70edbb12c8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-10T21:14:23.970Z_

<details><summary>↩ Tool result · `toolu_016Un7qn1QUZMQTKrRKCRNwJ`</summary>

```text
# Paper Analysis

**Title:** "Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation"

**Authors:** Chengwen Qi, Ren Ma, Bowen Li, He Du, Binyuan Hui, Jinwang Wu, Yuanjun Laili, Conghui He

**Date:** February 2025 (arxiv version 2502.06563v2)

**Key Technique:** The ProverGen framework combines LLM generative capabilities with symbolic prover (Prover9) rigor through a three-stage pipeline: background story generation, logic skeleton construction via top-down reasoning, and statement translation.

## FOLIO Accuracy Results

According to Table 2, the following models achieved these accuracies on FOLIO:

- **GPT-4o (Standard):** 69.66%
- **GPT-4o (CoT):** 77.18%
- **Claude-3.5-Sonnet (Standard):** 69.58%
- **Claude-3.5-Sonnet (CoT):** 81.91%
- **Llama3.1-8B-Instruct (Standard):** 46.18%
- **Llama3.1-8B-Instruct (CoT):** 59.30%
- **Llama3.1-70B-Instruct (Standard):** 65.28%
- **Llama3.1-70B-Instruct (CoT):** 75.21%
- **Mistral-7B-Instruct (Standard):** 47.90%
- **Mistral-7B-Instruct (CoT):** 55.93%
- **Mistral-Large-Instruct (Standard):** 68.65%
- **Mistral-Large-Instruct (CoT):** 79.38%
- **Mixtral-8x22B-Instruct (Standard):** 58.58%
- **Mixtral-8x22B-Instruct (CoT):** 68.81%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8021f7d-85c0-4b95-8a80-b46d2b828839",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "b765b547-06b6-47d5-bbc6-b5abad1c3417",
  "sourceToolAssistantUUID": "a8021f7d-85c0-4b95-8a80-b46d2b828839",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 112 · 2026-05-10T21:14:28.469Z_

Now I have a comprehensive dataset. Let me do one final round of searches to find any remaining CEGAR-specific and very recent 2026 work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b765b547-06b6-47d5-bbc6-b5abad1c3417",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaamJFNe7v4uuGkgJpt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf5e8d05-5e2d-4c98-8ba2-adec68bf5829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTQL6C98rLwdtNkurTaHYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 48090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1312,
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

_source line 113 · 2026-05-10T21:14:29.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XegEkDP48gK3wVNnFoDdAq`</summary>

```json
{
  "query": "neuro symbolic CEGIS counterexample LLM solver feedback natural language reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf5e8d05-5e2d-4c98-8ba2-adec68bf5829",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaamJFNe7v4uuGkgJpt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c070b7e9-92e1-40b0-b85f-750b5810ab00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTQL6C98rLwdtNkurTaHYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 48090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1312,
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

_source line 114 · 2026-05-10T21:14:30.025Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NBGAANpJbeZQjkrauDw7Uy`</summary>

```json
{
  "query": "FOLIO benchmark o1 o3 DeepSeek-R1 reasoning model accuracy 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c070b7e9-92e1-40b0-b85f-750b5810ab00",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011CauaamJFNe7v4uuGkgJpt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "252ff056-31ce-4afb-a335-714467388d5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTQL6C98rLwdtNkurTaHYx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 48090,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1312
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 48090,
          "cache_creation_input_tokens": 1312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1312,
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

_source line 115 · 2026-05-10T21:14:35.844Z_

<details><summary>↩ Tool result · `toolu_01NBGAANpJbeZQjkrauDw7Uy`</summary>

```text
Web search results for query: "FOLIO benchmark o1 o3 DeepSeek-R1 reasoning model accuracy 2025 2026"

Links: [{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/deepseek-r1"},{"title":"OpenAI o3 vs DeepSeek r1: Which Reasoning Model is Best?","url":"https://blog.promptlayer.com/openai-o3-vs-deepseek-r1-an-analysis-of-reasoning-models/"},{"title":"DeepSeek-R1 Paper Updated: What’s New | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/deepseek-r1-paper-updated-whats-new-2598d766c822"},{"title":"DeepSeek-R1 outperforms Gemini 2.0 Pro, OpenAI o1, and o3-mini in bilingual complex ophthalmology reasoning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2667376225000290"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"DeepSeek R1 vs OpenAI o3: Ultimate 2026 Reasoning Model Comparison","url":"https://www.humai.blog/deepseek-r1-vs-openai-o3-ultimate-2026-reasoning-model-comparison/"},{"title":"DeepSeek R1: Complete Guide to the Open Reasoning Model","url":"https://chat-deep.ai/models/deepseek-r1/"},{"title":"Comparative performance of GPT-4, GPT-o3, GPT-5, Gemini-3-Flash, and DeepSeek-R1 in ophthalmology question answering - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12894337/"},{"title":"DeepSeek-R1: The Open-Source Reasoning Model","url":"https://www.sitepoint.com/deepseek-r1-open-source-reasoning/"}]

I've performed a web search for your query about FOLIO benchmark performance on reasoning models. However, the search results don't contain specific information about FOLIO benchmark scores for o1, o3, or DeepSeek-R1 models. 

The search returned extensive information about these reasoning models' performance on other benchmarks instead, including:

- OpenAI o3 achieved 96.7% accuracy on AIME (American Invitational Mathematics Examination)
- DeepSeek-R1-0528 improved performance on AIME 2025 from 70.0% to 87.5%
- o3 scored 71.7% on SWE-bench Verified, surpassing DeepSeek R1 (49.2%) and OpenAI's O1 (48.9%)

If you're specifically looking for FOLIO (First-Order Logic) benchmark results, you may need to check research papers, technical documentation, or specialized AI benchmarking databases that focus on formal reasoning tasks. Would you like me to search for more specific information about FOLIO benchmark results with these models?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "252ff056-31ce-4afb-a335-714467388d5a",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "7cc7cd7d-8dfc-45c0-8df8-400de15d3b3b",
  "sourceToolAssistantUUID": "252ff056-31ce-4afb-a335-714467388d5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-10T21:14:38.598Z_

<details><summary>↩ Tool result · `toolu_01XegEkDP48gK3wVNnFoDdAq`</summary>

```text
Web search results for query: "neuro symbolic CEGIS counterexample LLM solver feedback natural language reasoning 2025 2026"

Links: [{"title":"[2309.16436] Neuro Symbolic Reasoning for Planning: Counterexample Guided Inductive Synthesis using Large Language Models and Satisfiability Solving","url":"https://ar5iv.labs.arxiv.org/html/2309.16436"},{"title":"A Comparative Study of Neurosymbolic AI Approaches to ...","url":"https://www.arxiv.org/pdf/2508.03366"},{"title":"LLM to Symbolic: Neuro-Symbolic Integration","url":"https://www.emergentmind.com/topics/llm-to-symbolic"},{"title":"GitHub - LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy: ✨✨Latest Advances on Neuro-Symbolic Learning in the era of Large Language Models","url":"https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy"},{"title":"Neuro-Symbolic Artificial Intelligence: Towards Improving ...","url":"https://www.ijcai.org/proceedings/2025/1195.pdf"},{"title":"Improving Rule-based Reasoning in LLMs using ...","url":"https://aclanthology.org/2025.emnlp-main.1556.pdf"},{"title":"An Evaluation of Open Source LLMs for Neuro-Symbolic Integration","url":"https://ceur-ws.org/Vol-4003/paper03.pdf"},{"title":"Neuro-Symbolic Verification for Preventing LLM Hallucinations in Process Control","url":"https://www.mdpi.com/2227-9717/14/2/322"},{"title":"Enhancing Large Language Models through Neuro-Symbolic Integration and Ontological Reasoning","url":"https://arxiv.org/html/2504.07640v1"},{"title":"Neuro-Symbolic Artificial Intelligence: Towards Improving the Reasoning Abilities of Large Language Models","url":"https://arxiv.org/html/2508.13678v1"}]

I found comprehensive results on neuro-symbolic AI approaches combining LLMs with formal reasoning systems. Here's what the search revealed:

## Key Research Findings (2025-2026)

**CEGIS with LLM Solvers:**

Recent work uses LLMs as the learner in a CEGIS (Counterexample-Guided Inductive Synthesis) architecture with a formal verification engine as the oracle, adopting the CEGIS architecture and locating the LLM as a scalable learner within it. This interaction leverages SMT solvers as deductive reasoning engines to analyze generated solutions from LLMs, produce counterexamples when solutions are incorrect, and provide that feedback to LLMs, where this interaction between inductive LLMs and deductive SMT solvers can iteratively steer the LLM to generate the correct response.

**Natural Language Reasoning Integration:**

One approach allows users to communicate planning problems in natural language, with formulations of queries to SMT solvers automatically generated from natural language. Robust frameworks introduce self-refinement modules which use feedback from downstream symbolic solvers to iteratively correct syntactic or semantic errors in the translated logic expressions.

**Current Paradigms (2025):**

Neuro-Symbolic methods demonstrate superior performance, aiming to integrate the strengths of symbolic AI, which excels in complex reasoning, with neural networks, which are adept at learning from large datasets, enabling AI systems that not only learn from large datasets but also handle complex reasoning tasks in a human-like manner.

Recent efforts review symbolic feedback approaches, including symbolic formatted reasoning, differential symbolic modules, and symbolic feedback mechanisms.

**Latest Applications (January 2026):**

Recent research investigates hallucination as a failure of abductive reasoning, developing neuro-symbolic frameworks where Abductive Logic Programming evaluates the coherence of model-generated explanations in process control domains.

The research indicates a strong trend toward combining LLM capabilities with formal verification and symbolic reasoning systems for improved reliability and interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c070b7e9-92e1-40b0-b85f-750b5810ab00",
  "isSidechain": true,
  "promptId": "f6f1e2f4-e418-4595-8a03-3df59638732f",
  "agentId": "a6f7b669ced9ecb73",
  "type": "user",
  "uuid": "f7abffb4-a779-4ed5-bb7a-4f01695e4cdf",
  "sourceToolAssistantUUID": "c070b7e9-92e1-40b0-b85f-750b5810ab00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 117 · 2026-05-10T21:16:05.269Z_

I now have enough data to compile a comprehensive report. Here is my analysis:

---

## FOLIO Benchmark Landscape: Late 2025 through May 2026

### What is FOLIO

FOLIO is a human-annotated dataset for natural language reasoning with first-order logic (FOL) annotations. It has 1,430 examples (unique conclusions) paired with 487 premise sets. The test set has 204 samples. It uses an open-world assumption with 3 labels (True/False/Unknown), giving a 33% random baseline. FOLIO was published at EMNLP 2024.

**Note:** Papers with Code shut down in July 2025 (Meta discontinued it), so the canonical FOLIO leaderboard no longer exists. Results must be pieced together from individual papers.

---

### Consolidated FOLIO Accuracy Table

Below is every concrete accuracy number I was able to verify across published papers. All results are on the FOLIO validation/test set (204 samples) unless noted.

#### Pure Neural / Chain-of-Thought Approaches

| Model | Method | Accuracy | Source |
|---|---|---|---|
| GPT-4 | Standard (few-shot) | 69.11% | Logic-LM++ (2024) |
| GPT-4 | Chain-of-Thought | 70.58% | Logic-LM++ (2024) |
| GPT-4o | Standard | 69.66% | ProverGen (ICLR 2025) |
| GPT-4o | CoT | 77.18% | ProverGen (ICLR 2025) |
| Claude-3.5-Sonnet | Standard | 69.58% | ProverGen (ICLR 2025) |
| Claude-3.5-Sonnet | CoT | **81.91%** | ProverGen (ICLR 2025) |
| Mistral-Large | CoT | 79.38% | ProverGen (ICLR 2025) |
| Llama-3.1-70B | CoT | 75.21% | ProverGen (ICLR 2025) |
| Qwen 2.5 32B | CoT | 75.49% | Bansal et al. (2024/25) |
| Gemma 3 12B | CoT | 77.45% | Bansal et al. (2024/25) |
| Qwen 2.5 7B | CoT | 70.59% | Bansal et al. (2024/25) |
| Llama 3.1 8B | CoT | 70.59% | Bansal et al. (2024/25) |
| GPT-3.5 | Standard | 45.09% | Logic-LM++ (2024) |
| GPT-3.5 | CoT | 57.35% | Logic-LM++ (2024) |
| Flan-T5-Large | Fine-tuned | 65.7% | FOLIO paper (EMNLP 2024) |

#### Neurosymbolic Approaches (LLM + Symbolic Solver)

| System | Model | Accuracy | Key Technique | Source |
|---|---|---|---|---|
| Logic-LM | GPT-4 | 78.92% | NL-to-FOL + Prover9/Z3 + self-refinement | Logic-LM++ (2024) |
| **Logic-LM++** | **GPT-4** | **84.80%** | Multi-step refinement of symbolic formulations | Logic-LM++ (Jul 2024) |
| Logic-LM | GPT-3.5 | 62.80% | Same pipeline, weaker parser | Logic-LM++ (2024) |
| LINC | GPT-4 | ~70% (comparable to CoT) | NL-to-FOL + Prover9 | LINC (EMNLP 2023) |
| LINC | Qwen 2.5 32B | 68.14% | NL-to-FOL + Prover9 | Bansal et al. (2024/25) |
| NSCoT | Qwen 2.5 32B | 71.08% | LINC + reasoning chains | Bansal et al. (2024/25) |
| LTRAG | GPT-3.5 | ~71% (Logic-LM + 8%) | Thought-guided RAG for autoformalization + self-refinement | LTRAG (ACL Findings 2025) |
| MAD-LOGIC | GPT-4 (multi-agent) | Not publicly reported (ICLR 2026) | Multi-agent debate across symbolic languages + adaptive pruning | MAD-LOGIC (ICLR 2026) |
| LOGICPO | Phi-3.5 (fine-tuned) | Outperforms GPT-3.5 8-shot by 10% | DPO/KTO preference optimization for NL-FOL translation | LOGICPO (Jun 2025) |

#### Small Model FOL Translation (not end-to-end reasoning accuracy)

| Model | Method | FOLIO Translation Accuracy | Source |
|---|---|---|---|
| Gemma-3-4B | Incremental Inference | 40.89% | Thatikonda et al. (Jan 2026) |
| Qwen3-4B | SFT+ | 40.39% | Thatikonda et al. (Jan 2026) |
| Phi-4-mini | SFT+ / Incremental | 38.92% | Thatikonda et al. (Jan 2026) |

---

### Key Papers and Systems (Chronological)

1. **LINC** (EMNLP 2023) -- Olausson et al. Pioneering neurosymbolic: LLM parses NL to FOL, Prover9 reasons. Comparable to CoT on FOLIO with GPT-4 but much stronger on ProofWriter.

2. **Logic-LM** (2023) -- Pan et al. Three-module design: formulation, symbolic reasoning, result interpretation. +18.4% over CoT averaged across 5 datasets with GPT-4.

3. **Logic-LM++** (Jul 2024) -- Multi-step refinement of symbolic formulations. Achieves **84.80%** on FOLIO with GPT-4, the highest verified neurosymbolic score I found.

4. **ProverGen** (ICLR 2025) -- Qi et al. Generates synthetic training data via LLM + Prover9 pipeline. Tests many models; Claude-3.5-Sonnet CoT achieves **81.91%** (best pure-neural result found).

5. **Robustness of Neurosymbolic Reasoners** (2024/25) -- Bansal et al. Shows neurosymbolic methods are more robust (less accuracy drop on counterfactuals) but lower absolute accuracy than neural CoT. NSCoT bridges the gap.

6. **LTRAG** (ACL Findings 2025) -- Hu et al. Thought-guided RAG for autoformalization + refinement. +8% over Logic-LM/LINC on FOLIO with GPT-3.5; +13% on AR-LSAT with GPT-4.

7. **Intermediate Languages Matter** (2025) -- Beiser et al. Shows formal language choice matters: FOL outperforms logic programming (ASP/Pyke) on FOLIO. Tests 7 LLMs (8B-671B).

8. **LOGICPO** (Jun 2025) -- Preference optimization for NL-FOL translation. Fine-tuned Phi-3.5 beats GPT-3.5-turbo 8-shot; 83% reduction in syntax errors vs. Logic-LM.

9. **Alignment Methods for Formal Logical Reasoning** (MathNLP 2025) -- DPO-based alignment for NL-FOL parsing on FOLIO. Introduces LogicSim metric.

10. **MAD-LOGIC** (ICLR 2026) -- Multi-agent debate across symbolic languages with adaptive sparse communication. Tested on FOLIO, AR-LSAT, LogiQA-V2. Specific numbers not publicly available yet outside the paper.

11. **Improving Symbolic Translation** (Jan 2026) -- Thatikonda et al. Incremental inference (predicate-then-FOL) for small models (3B-4B). Improves Gemma-3-4B from 33% to 40.89% on FOLIO.

12. **PC-FOL / Linear vs. Proof-by-Cases** (2026, AISTATS) -- Ji et al. New FOLIO-derived benchmark showing models (GPT-4o: 85%/51%, o4-mini: 91%/80%) struggle with proof-by-cases reasoning even when linear reasoning is strong.

13. **FOL-Traces** (EACL 2026) -- Lee et al. Large-scale verified FOL reasoning traces. Uses FOLIO as source data. Models reach only ~46% on masked-operation prediction.

14. **Logitext** (2025) -- Oh et al. SMT-based neurosymbolic language with propose-verify-refine loop. Not tested on FOLIO directly but demonstrates GPT-5 recovers <1% of satisfying assignments vs. SMT solvers on combinatorial reasoning.

15. **LogicGraph** (Feb 2026) -- New benchmark for multi-path reasoning. Gemini-3-Pro achieves 96% convergent success but <60% divergent diversity, revealing models fixate on single proof paths.

---

### Counterexample-Guided / CEGAR Approaches to NL Reasoning

The CEGAR paradigm has **not** been directly applied to NL reasoning benchmarks like FOLIO in any published work I found. However, closely related iterative solver-feedback approaches exist:

1. **CEGIS for Planning** (Jha et al., Sep 2023) -- Uses LLM + Z3 SMT solver in a counterexample-guided inductive synthesis loop. Tested on blocks-world planning, not FOLIO. The SMT solver generates counterexamples when LLM solutions are incorrect, feeding them back iteratively.

2. **Logic-LM's self-refinement module** -- Uses solver error messages as feedback to iteratively correct FOL translations. This is a lightweight version of the CEGAR concept applied to FOLIO.

3. **Logic-LM++ multi-step refinement** -- Extends Logic-LM's refinement with multiple correction rounds, achieving 84.80% on FOLIO. Closest to a CEGAR-like iterative approach on FOLIO.

4. **LTRAG's Refiner** -- Uses thought-guided examples to refine autoformalization errors, a retrieval-augmented form of iterative correction.

5. **NL2FOL** (Lalwani et al., 2024) -- Uses SMT solver (Z3) for validity checking + LLM to interpret counterexamples. Achieves 78-80% F1 on logical fallacy detection (not FOLIO). The counterexample interpretation is notably CEGAR-like.

6. **Logitext** (Oh et al., 2025) -- Propose-verify-refine loop with Z3 SMT solver. The verification step generates counterexamples that drive refinement. Not tested on FOLIO.

7. **Semantic Knowledge Abstraction (SKA)** (2026) -- Framework discovering/compensating for LLM semantic knowledge gaps in NLI. Improves accuracy by up to 15%. Abstraction-refinement inspired but not strictly CEGAR.

**Bottom line on CEGAR for NL reasoning:** The space is open. Solver-feedback loops exist (Logic-LM, NL2FOL, Logitext) but none frame themselves as CEGAR or implement the full abstraction-refinement cycle for natural language logical reasoning. A principled CEGAR-based approach to FOLIO would be novel.

---

### How Crowded is the FOLIO Landscape?

**Moderately crowded and actively growing.** Key observations:

- **~15 systems** have been evaluated on FOLIO since 2023, with publication rate accelerating in 2025-2026.
- **The SoTA is around 84-85%** (Logic-LM++ with GPT-4), with pure-neural CoT approaching 82% (Claude-3.5-Sonnet).
- **The gap between neurosymbolic and pure neural is narrowing:** Claude-3.5 CoT (81.91%) nearly matches Logic-LM (78.92%) without any symbolic component, though Logic-LM++ (84.80%) still leads.
- **The frontier is shifting** from "can we beat CoT?" to robustness, multi-path reasoning, small-model translation quality, and reasoning model evaluation (o1/o3/R1 on FOL-derived tasks).
- **No published reasoning-model (o1/o3/DeepSeek-R1) results on FOLIO** were found -- a notable gap.
- **ICLR 2026 has at least 2 FOLIO-relevant papers** (MAD-LOGIC, LogicGraph), confirming continued top-venue interest.
- **CEGAR/counterexample-guided approaches to FOLIO are absent**, making this a differentiation opportunity.

Sources:
- [FOLIO: Natural Language Reasoning with First-Order Logic](https://arxiv.org/abs/2209.00840)
- [LINC: A Neurosymbolic Approach (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.313/)
- [Logic-LM++ Multi-Step Refinement](https://arxiv.org/html/2407.02514v1)
- [ProverGen: LLMs Meet Symbolic Provers (ICLR 2025)](https://arxiv.org/html/2502.06563)
- [Robustness of Neurosymbolic Reasoners](https://arxiv.org/html/2509.17377)
- [Intermediate Languages Matter](https://arxiv.org/html/2509.04083v1)
- [LTRAG (ACL Findings 2025)](https://aclanthology.org/2025.findings-acl.126/)
- [LOGICPO: Preference Optimization for NL-FOL](https://arxiv.org/abs/2506.18383)
- [Alignment Methods for Formal Logical Reasoning (MathNLP 2025)](https://aclanthology.org/2025.mathnlp-main.8/)
- [MAD-LOGIC (ICLR 2026)](https://openreview.net/forum?id=rdE9qxGfIv)
- [Improving Symbolic Translation (Jan 2026)](https://arxiv.org/html/2601.09446v1)
- [PC-FOL: Linear vs. Proof-by-Cases (2026)](https://arxiv.org/html/2602.20973)
- [FOL-Traces (EACL 2026)](https://arxiv.org/html/2505.14932v2)
- [Logitext: Neurosymbolic Language as SMT](https://arxiv.org/html/2602.18095)
- [LogicGraph: Multi-Path Reasoning Benchmark (Feb 2026)](https://arxiv.org/abs/2602.21044)
- [CEGIS with LLMs and SMT Solving](https://arxiv.org/abs/2309.16436)
- [NL2FOL: Logical Fallacy Detection](https://arxiv.org/html/2405.02318v1/)
- [Pushing Boundaries: Formal-Logic Verification (Jan 2026)](https://arxiv.org/abs/2601.22642)
- [Papers with Code Shutdown](https://www.codesota.com/papers-with-code)
- [CounterMATH: Counterexample-Driven Reasoning](https://arxiv.org/abs/2502.10454)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7abffb4-a779-4ed5-bb7a-4f01695e4cdf",
  "isSidechain": true,
  "agentId": "a6f7b669ced9ecb73",
  "requestId": "req_011Cauabqp8y3zqVRVqqqHRB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b1216a2-8469-485a-b07a-ec578cf8c3a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04847dfd-3c66-4e9a-b430-c3ae68322c95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qn15tZ1dbTZf5z69bTevgM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 948,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 49402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1195,
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
