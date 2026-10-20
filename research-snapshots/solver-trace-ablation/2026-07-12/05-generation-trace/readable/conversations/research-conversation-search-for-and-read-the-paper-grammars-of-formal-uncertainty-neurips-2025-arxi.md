# Research conversation: Search for and read the paper "Grammars of Formal Uncertainty" (NeurIPS 2025, arXiv 2505.20047). I need to understand: 1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7d48587cdf77f8e1.jsonl`
- **Structured JSON:** [`a3787e5326824c33f3c4.json`](../../sessions/a3/a3787e5326824c33f3c4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-12T00:33:14.949Z_

Search for and read the paper "Grammars of Formal Uncertainty" (NeurIPS 2025, arXiv 2505.20047). I need to understand:

1. What exactly did they find about SMT-based autoformalization on FOLIO? The claim is it HURTS accuracy by -44.5%.
2. What models did they test? (o3-mini, DeepSeek-R1, Gemini mentioned)
3. Was this problem-level autoformalization or step-level?
4. What was their explanation for why autoformalization hurts?
5. Did they test on other benchmarks besides FOLIO and ProntoQA?
6. Are there any conditions under which autoformalization helped?

Use WebSearch to find the paper, then WebFetch to read its abstract and key sections. I need precise numbers and methodology details, not just summaries. Report in under 400 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a7d48587cdf77f8e1",
  "type": "user",
  "uuid": "48161ada-fb7e-46e5-acf6-46c09df8e0ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:33:14.955Z_

```json
{
  "parentUuid": "48161ada-fb7e-46e5-acf6-46c09df8e0ef",
  "isSidechain": true,
  "agentId": "a7d48587cdf77f8e1",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "5a26793a-0f41-41a1-bacc-cf2402728c0d",
  "timestamp": "2026-05-12T00:33:14.955Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:33:17.381Z_



I'll search for this paper and fetch its details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a26793a-0f41-41a1-bacc-cf2402728c0d",
  "isSidechain": true,
  "agentId": "a7d48587cdf77f8e1",
  "requestId": "req_011CawjZAbDYy1a2jh577K2K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27c506e7-a92c-4f0f-9c1a-693f7465bb2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g3SDqSgrM2vJd7WEZSHhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8037,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8037,
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

_source line 4 · 2026-05-12T00:33:18.057Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013iDproMRUrD3A5e8KdwgV6`</summary>

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
  "parentUuid": "27c506e7-a92c-4f0f-9c1a-693f7465bb2c",
  "isSidechain": true,
  "agentId": "a7d48587cdf77f8e1",
  "requestId": "req_011CawjZAbDYy1a2jh577K2K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd58bfd0-3135-4ab4-b587-a04ba47f165d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g3SDqSgrM2vJd7WEZSHhL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8037,
      "cache_read_input_tokens": 0,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8037,
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

_source line 5 · 2026-05-12T00:33:18.061Z_

<details><summary>↩ Tool result · `toolu_013iDproMRUrD3A5e8KdwgV6`</summary>

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
  "parentUuid": "cd58bfd0-3135-4ab4-b587-a04ba47f165d",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a7d48587cdf77f8e1",
  "type": "user",
  "uuid": "2a7b1810-4a76-45f7-9c6b-79170b4198f1",
  "sourceToolAssistantUUID": "cd58bfd0-3135-4ab4-b587-a04ba47f165d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-12T00:33:21.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BioFRDNGicETXN66eD9vkp`</summary>

```json
{
  "query": "Grammars of Formal Uncertainty NeurIPS 2025 arXiv 2505.20047 autoformalization FOLIO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a7b1810-4a76-45f7-9c6b-79170b4198f1",
  "isSidechain": true,
  "agentId": "a7d48587cdf77f8e1",
  "requestId": "req_011CawjZQ4LRfFQBfWUX6Qqs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44312b49-4af5-475c-bf32-9d24c7c4294a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Knv9tRKxg5ixkUVeGPUmZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1901,
      "cache_read_input_tokens": 8037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1901,
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

_source line 7 · 2026-05-12T00:33:23.049Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012tx6SbPXARP4v4J6BjvCT6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.20047",
  "prompt": "Extract the full abstract, author names, and any key claims about autoformalization hurting accuracy on FOLIO. Include all specific numbers and percentages mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44312b49-4af5-475c-bf32-9d24c7c4294a",
  "isSidechain": true,
  "agentId": "a7d48587cdf77f8e1",
  "requestId": "req_011CawjZQ4LRfFQBfWUX6Qqs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1befbd1-600c-4fbe-a93c-225db855b74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Knv9tRKxg5ixkUVeGPUmZM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1901,
      "cache_read_input_tokens": 8037,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1901
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 182,
          "cache_read_input_tokens": 8037,
          "cache_creation_input_tokens": 1901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1901,
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

_source line 8 · 2026-05-12T00:33:29.963Z_

<details><summary>↩ Tool result · `toolu_01BioFRDNGicETXN66eD9vkp`</summary>

```text
Web search results for query: "Grammars of Formal Uncertainty NeurIPS 2025 arXiv 2505.20047 autoformalization FOLIO"

Links: [{"title":"[2505.20047] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/abs/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in ...","url":"https://arxiv.org/pdf/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/html/2505.20047"},{"title":"NeurIPS Poster Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118114"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks | OpenReview","url":"https://openreview.net/forum?id=QfKpJ00t2L"},{"title":"GitHub - DebarghaG/grammars-formal-uncertainty: [NeurIPS 2025] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://github.com/DebarghaG/grammars-formal-uncertainty"},{"title":"[2505.23854] Revisiting Uncertainty Estimation and Calibration of Large Language Models","url":"https://arxiv.org/abs/2505.23854"},{"title":"Revisiting Uncertainty Estimation and Calibration of Large Language Models","url":"https://openreview.net/pdf?id=Q9CreVjHH7"},{"title":"Position: Uncertainty Quantification Needs Reassessment for Large-language Model Agents","url":"https://arxiv.org/html/2505.22655v1"},{"title":"Efficient semantic uncertainty quantification in language models via diversity-steered sampling | OpenReview","url":"https://openreview.net/forum?id=IiEtQPGVyV"}]

I've found detailed information about the paper you're looking for. Here's what I found:

## "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks"

The paper addresses a fundamental tension in using LLMs for automated reasoning: while LLMs show remarkable promise for democratizing automated reasoning by generating formal specifications, they are probabilistic while formal verification demands deterministic guarantees. The work comprehensively investigates failure modes and uncertainty quantification in LLM-generated formal artifacts.

### Key Contributions

A systematic evaluation of five frontier LLMs reveals that Satisfiability Modulo Theories (SMT) based autoformalization has domain-specific impacts on accuracy, ranging from +34.8% improvement on logical tasks to -44.5% degradation on factual ones, with known uncertainty quantification techniques like token probability entropy failing to identify these errors.

The authors introduce a probabilistic context-free grammar (PCFG) framework to model LLM outputs, yielding a refined uncertainty taxonomy. They find that uncertainty signals are task-dependent—for example, grammar entropy for logic tasks achieves AUROC >0.93.

A lightweight fusion of these signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention, transforming LLM-driven formalization into a reliable engineering discipline.

### Publication Details

This is a NeurIPS 2025 poster paper, and the work is available on arXiv as 2505.20047. There's also a GitHub repository available at DebarghaG/grammars-formal-uncertainty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44312b49-4af5-475c-bf32-9d24c7c4294a",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a7d48587cdf77f8e1",
  "type": "user",
  "uuid": "841bf021-eb3c-4983-a25c-069023fa9a13",
  "sourceToolAssistantUUID": "44312b49-4af5-475c-bf32-9d24c7c4294a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T00:33:30.094Z_

<details><summary>↩ Tool result · `toolu_012tx6SbPXARP4v4J6BjvCT6`</summary>

```text
# Research Summary

**Full Abstract:**
"Large language models (LLMs) show remarkable promise for democratizing automated reasoning by generating formal specifications. However, a fundamental tension exists: LLMs are probabilistic, while formal verification demands deterministic guarantees. This paper addresses this epistemological gap by comprehensively investigating failure modes and uncertainty quantification (UQ) in LLM-generated formal artifacts. Our systematic evaluation of five frontier LLMs reveals Satisfiability Modulo Theories (SMT) based autoformalization's domain-specific impact on accuracy (from +34.8% on logical tasks to -44.5% on factual ones), with known UQ techniques like the entropy of token probabilities failing to identify these errors. We introduce a probabilistic context-free grammar (PCFG) framework to model LLM outputs, yielding a refined uncertainty taxonomy. We find uncertainty signals are task-dependent (e.g., grammar entropy for logic, AUROC>0.93). Finally, a lightweight fusion of these signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention, transforming LLM-driven formalization into a reliable engineering discipline."

**Authors:**
Debargha Ganguly, Vikash Singh, Sreehari Sankar, Biyao Zhang, Xuecen Zhang, Srinivasan Iyengar, Xiaotian Han, Amit Sharma, Shivkumar Kalyanaraman, Vipin Chaudhary

**Key Claims on Autoformalization Accuracy:**
The research demonstrates SMT-based autoformalization produces contradictory results depending on task type: "accuracy (from +34.8% on logical tasks to -44.5% on factual ones)". This 79.3 percentage-point variance indicates autoformalization significantly harms performance on factual reasoning compared to logical domains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1befbd1-600c-4fbe-a93c-225db855b74a",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a7d48587cdf77f8e1",
  "type": "user",
  "uuid": "87fd9c86-9c0f-4cb0-bf21-4ea45678b3e6",
  "sourceToolAssistantUUID": "f1befbd1-600c-4fbe-a93c-225db855b74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-12T00:33:33.157Z_

Now let me fetch the full HTML version of the paper for detailed methodology, model specifics, and benchmark details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87fd9c86-9c0f-4cb0-bf21-4ea45678b3e6",
  "isSidechain": true,
  "agentId": "a7d48587cdf77f8e1",
  "requestId": "req_011CawjaHEMBdyYMUpkyoaRj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e3841dd-c11f-40e9-9902-dacab8b1a8ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTovSV36eCZ7HpKBdBo9yS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 9938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1577,
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

_source line 11 · 2026-05-12T00:33:38.399Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0166GH6ECfofH5uoQ9nVfA31`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.20047",
  "prompt": "Extract ALL of the following details precisely:\n1. Which specific models were tested? List all model names.\n2. Which benchmarks were used beyond FOLIO and ProntoQA? List all benchmarks.\n3. Was this problem-level or step-level autoformalization?\n4. What was their explanation for WHY autoformalization hurts on FOLIO specifically? Quote or paraphrase their reasoning.\n5. What were the exact accuracy numbers for each model on FOLIO with and without autoformalization?\n6. Under what conditions did autoformalization HELP? Which benchmarks/tasks?\n7. What is the -44.5% number specifically referring to — which model, which benchmark?\n8. Any tables with accuracy results — reproduce key numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e3841dd-c11f-40e9-9902-dacab8b1a8ed",
  "isSidechain": true,
  "agentId": "a7d48587cdf77f8e1",
  "requestId": "req_011CawjaHEMBdyYMUpkyoaRj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32ee6354-c7ce-45d4-aaae-d3f332258ea8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTovSV36eCZ7HpKBdBo9yS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 9938,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 9938,
          "cache_creation_input_tokens": 1577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1577,
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

_source line 12 · 2026-05-12T00:33:47.104Z_

<details><summary>↩ Tool result · `toolu_0166GH6ECfofH5uoQ9nVfA31`</summary>

```text
# Paper Analysis: Grammars of Formal Uncertainty

## 1. Models Tested
- o3-mini
- DeepSeekR1 (with CoT enabled)
- DeepSeek-v3-0324
- Gemini Flash 2.0
- Gemini Flash 2.0 Lite

## 2. Benchmarks Used
- StrategyQA
- ProntoQA
- ProofWriter
- FOLIO

## 3. Autoformalization Level
Problem-level autoformalization (generating SMT-LIB programs for entire problems, not individual steps).

## 4. Why Autoformalization Hurt on FOLIO

The paper suggests the degradation stems from **knowledge-intensive reasoning demands**. On datasets requiring world knowledge, the overhead introduced during translation to formal specifications outweighs benefits. The authors note that "direct textual reasoning consistently outperformed SMT across most models" on FOLIO, indicating formalization became a bottleneck rather than an aid.

## 5. FOLIO Accuracy Numbers

| Model | Text | SMT | Delta |
|-------|------|-----|-------|
| o3-mini | 0.9450 | 0.5000 | -0.4450 |
| DeepSeekv3 | 0.9333 | 0.5961 | -0.3372 |
| DeepSeek R1 | 0.9252 | 0.5200 | -0.4052 |
| Flash 2.0 | 0.9010 | 0.5625 | -0.3385 |
| Flash 2.0 Lite | 0.9017 | 0.7321 | -0.1696 |

## 6. When Autoformalization Helped

**ProofWriter** showed substantial improvements, particularly for struggling models. The task's explicit premises benefited from isolating deductive reasoning. O3-mini gained +5.24% accuracy; Flash 2.0 Lite improved +34.8%.

## 7. The -44.5% Reference

This represents **o3-mini's decline on FOLIO** (from 94.50% text accuracy to 50.00% with SMT formalization). The magnitude reflects complete formalization failure on factual reasoning.

## 8. Key Accuracy Table

Shown above under Section 5. The paper demonstrates **task-dependency**: formal logic tasks (ProofWriter) benefit; knowledge-heavy tasks (FOLIO, StrategyQA) suffer from formalization overhead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32ee6354-c7ce-45d4-aaae-d3f332258ea8",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a7d48587cdf77f8e1",
  "type": "user",
  "uuid": "86e05cad-a9c7-402a-8f7d-f67eb46fb212",
  "sourceToolAssistantUUID": "32ee6354-c7ce-45d4-aaae-d3f332258ea8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T00:34:01.594Z_

Here are the precise findings from the paper.

---

**Paper:** "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks" (Ganguly et al., NeurIPS 2025, arXiv 2505.20047)

**1. SMT-based autoformalization on FOLIO:** It devastates accuracy across all five models. The headline -44.5% is o3-mini dropping from 94.50% (direct text reasoning) to 50.00% (SMT formalization). Every model suffered large drops on FOLIO:

| Model | Text | SMT | Delta |
|---|---|---|---|
| o3-mini | 94.50% | 50.00% | -44.50% |
| DeepSeek-v3 | 93.33% | 59.61% | -33.72% |
| DeepSeek-R1 | 92.52% | 52.00% | -40.52% |
| Gemini Flash 2.0 | 90.10% | 56.25% | -33.85% |
| Gemini Flash 2.0 Lite | 90.17% | 73.21% | -16.96% |

**2. Models tested:** o3-mini, DeepSeek-R1 (with CoT), DeepSeek-v3-0324, Gemini Flash 2.0, Gemini Flash 2.0 Lite -- five frontier LLMs total.

**3. Autoformalization level:** Problem-level (whole-problem SMT-LIB program generation), not step-level.

**4. Why it hurts:** FOLIO requires world/factual knowledge. The translation overhead into formal specifications becomes a bottleneck -- the model loses information or introduces errors when formalizing knowledge-intensive reasoning. Direct textual reasoning consistently outperformed SMT on FOLIO across all models because the task demands knowledge the formal representation cannot capture.

**5. Other benchmarks:** Four total -- FOLIO, ProntoQA, ProofWriter, and StrategyQA. StrategyQA (also knowledge-heavy) similarly suffered from formalization.

**6. When autoformalization helped:** On ProofWriter, where premises are explicitly stated and the task is pure deductive logic. Gemini Flash 2.0 Lite gained +34.8%, o3-mini gained +5.24%. The benefit appeared specifically on tasks with explicit premises requiring isolated deductive reasoning, not world knowledge.

Sources:
- [arXiv Abstract - 2505.20047](https://arxiv.org/abs/2505.20047)
- [Full HTML Paper](https://arxiv.org/html/2505.20047)
- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/118114)
- [GitHub Repository](https://github.com/DebarghaG/grammars-formal-uncertainty)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86e05cad-a9c7-402a-8f7d-f67eb46fb212",
  "isSidechain": true,
  "agentId": "a7d48587cdf77f8e1",
  "requestId": "req_011CawjbXyeMLxo3TBDQEhnV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22db88f7-48df-4e10-bcd1-524d7eb8b407",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AoNqwFRonE75RibuZdzyYv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 11515,
      "output_tokens": 712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 885
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 712,
          "cache_read_input_tokens": 11515,
          "cache_creation_input_tokens": 885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 885,
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
