# Research conversation: Search for these specific papers and related work: 1. HUMAINE Framework (arXiv 2603.04409) - "Unpacking Human Preference

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a9fec471c265f132a.jsonl`
- **Structured JSON:** [`df37a95b2bc50d14a516.json`](../../sessions/df/df37a95b2bc50d14a516.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-10T07:22:31.105Z_

Search for these specific papers and related work:

1. HUMAINE Framework (arXiv 2603.04409) - "Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework" - verify it exists and what it does
2. LLM-based conversational user simulation survey (arXiv 2604.24977) - verify existence
3. Steering vector demographic injection paper (arXiv 2504.02234) - verify existence

Also search for:
4. "CORAAL" and "AAVENUE" datasets for AAVE - do they exist and are they accessible?
5. "Svarah" dataset for Indian English - does it exist?
6. "NatCS" customer service dataset - does it exist?
7. "DPO user simulator calibration" arxiv 2025 2026
8. "retrieval augmented few-shot user simulation" 2025 2026

Search queries:
- site:arxiv.org "HUMAINE" "demographic" "LLM evaluation" 2026
- arxiv 2603.04409
- arxiv 2604.24977  
- "steering vectors" "demographic" "LLM" 2025
- "AAVENUE" AAVE benchmark LLM 2024

For each paper found, report: exists (yes/no), actual claims, and how it overlaps with the DemoCalib idea being reviewed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "23a62b20-b3e9-4f3e-81f7-3e0a5e7e0c71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T07:22:32.786Z_

I'll search for these papers and datasets systematically. Let me start with web searches for the specific arXiv papers and datasets.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23a62b20-b3e9-4f3e-81f7-3e0a5e7e0c71",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatV9URTjuGYkoBBYgkCA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b2d6af7e-77ca-46ca-852b-390531807270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M87kyfbtutybvUwT3Kw6PX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T07:22:33.036Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cg8EPZ1hQPpPz2vo6DSEe1`</summary>

```json
{
  "query": "arxiv 2603.04409 HUMAINE demographic LLM evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2d6af7e-77ca-46ca-852b-390531807270",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatV9URTjuGYkoBBYgkCA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "06b6975d-6231-4313-8641-8be7ed09aa3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M87kyfbtutybvUwT3Kw6PX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T07:22:33.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011fcXiu5m3gWjm1xPLaTuwR`</summary>

```json
{
  "query": "arxiv 2604.24977 LLM conversational user simulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06b6975d-6231-4313-8641-8be7ed09aa3e",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatV9URTjuGYkoBBYgkCA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e7b522e6-3c7f-456c-a03a-c48f62b5bace",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M87kyfbtutybvUwT3Kw6PX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T07:22:33.431Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012PY44x4sUPGVYWVeYP4A7c`</summary>

```json
{
  "query": "arxiv 2504.02234 steering vectors demographic injection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7b522e6-3c7f-456c-a03a-c48f62b5bace",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatV9URTjuGYkoBBYgkCA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "424d6da3-8a1e-41d1-a094-0c0babfd1fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M87kyfbtutybvUwT3Kw6PX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T07:22:33.649Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016aLW3UrYTmBy3pvoPuZPBy`</summary>

```json
{
  "query": "CORAAL AAVENUE AAVE benchmark dataset LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "424d6da3-8a1e-41d1-a094-0c0babfd1fd5",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatV9URTjuGYkoBBYgkCA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3cb10021-a8fb-44d4-8fc4-01cb05793bff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M87kyfbtutybvUwT3Kw6PX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T07:22:33.679Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017DYEgZ5Zvggwa6YCTXquXw`</summary>

```json
{
  "query": "Svarah Indian English dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cb10021-a8fb-44d4-8fc4-01cb05793bff",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatV9URTjuGYkoBBYgkCA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be61e1bf-d415-4975-9b37-eed9bd441035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M87kyfbtutybvUwT3Kw6PX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 283,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 762,
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

_source line 8 · 2026-05-10T07:22:38.639Z_

<details><summary>↩ Tool result · `toolu_011fcXiu5m3gWjm1xPLaTuwR`</summary>

```text
Web search results for query: "arxiv 2604.24977 LLM conversational user simulation"

Links: [{"title":"[2604.24977] A Survey on LLM-based Conversational User Simulation","url":"https://arxiv.org/abs/2604.24977"},{"title":"A Survey on LLM-based Conversational User Simulation","url":"https://arxiv.org/html/2604.24977"},{"title":"Let the LLMs Talk: Simulating Human-to-Human Conversational","url":"https://arxiv.org/pdf/2312.02913"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://arxiv.org/html/2601.17087v1"},{"title":"[2604.00249] A Safety-Aware Role-Orchestrated Multi-Agent LLM Framework for Behavioral Health Communication Simulation","url":"https://arxiv.org/abs/2604.00249"},{"title":"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models","url":"https://arxiv.org/html/2502.12813v1"},{"title":"Training and Evaluating User Language Models","url":"https://arxiv.org/pdf/2510.06552"},{"title":"Evaluating Large Language Models as Generative User Simulators for Conversational Recommendation","url":"https://arxiv.org/html/2403.09738v4"},{"title":"SimUSER: Simulating User Behavior with Large Language Models for Recommender System Evaluation","url":"https://arxiv.org/html/2504.12722v1"},{"title":"Integrating LLM in Agent-Based Social Simulation: Opportunities and ChallengesThis manuscript has been submitted for peer review to the Journal of Artificial Societies and Social Simulation (JASSS).","url":"https://arxiv.org/html/2507.19364v1"}]

Based on the search results, I found the paper you're looking for:

## A Survey on LLM-based Conversational User Simulation

This paper introduces a novel taxonomy covering user granularity and simulation objectives, and systematically analyzes core techniques and evaluation methodologies. Recent advancements in large language models (LLMs) have significantly catalyzed progress in this domain by enabling high-fidelity generation of synthetic user conversation.

The paper was submitted on April 27, 2026, and is authored by Bo Ni and 29 other co-authors from institutions including Vanderbilt University, Adobe Research, Yale University, University of Oregon, UC San Diego, Dolby Laboratories, UC Berkeley, Cisco AI Research, University of Southern California, Texas A&M University, and UC Davis.

The authors aim to keep the research community informed of the latest advancements in conversational user simulation and to further facilitate future research by identifying open challenges and organizing existing work under a unified framework.

The paper is available on arXiv at https://arxiv.org/abs/2604.24977.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7b522e6-3c7f-456c-a03a-c48f62b5bace",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "ea1c3d69-6e9b-406c-bc1b-b7688ee1877f",
  "sourceToolAssistantUUID": "e7b522e6-3c7f-456c-a03a-c48f62b5bace",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T07:22:40.202Z_

<details><summary>↩ Tool result · `toolu_016aLW3UrYTmBy3pvoPuZPBy`</summary>

```text
Web search results for query: "CORAAL AAVENUE AAVE benchmark dataset LLM"

Links: [{"title":"[2408.14845] AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark","url":"https://arxiv.org/abs/2408.14845"},{"title":"AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark","url":"https://arxiv.org/html/2408.14845v3"},{"title":"AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark","url":"https://aavenuee.github.io/"},{"title":"(PDF) AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark","url":"https://www.researchgate.net/publication/383461248_AAVENUE_Detecting_LLM_Biases_on_NLU_Tasks_in_AAVE_via_a_Novel_Benchmark"},{"title":"AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark - ACL Anthology","url":"https://aclanthology.org/2024.nlp4pi-1.28/"},{"title":"AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark | alphaXiv","url":"https://www.alphaxiv.org/overview/2408.14845"},{"title":"AAVENUE: Detecting LLM Biases On NLU Tasks in AAVE Via A Novel Benchmark | PDF","url":"https://www.scribd.com/document/774521822/2408-14845v1-1"},{"title":"Research | Algoverse | Algoverse AI Research","url":"https://algoverseairesearch.org/research"},{"title":"GitHub - abhaygupta1266/AAVENUE-Code · GitHub","url":"https://github.com/abhaygupta1266/AAVENUE-Code"},{"title":"dblp: Philip Meng","url":"https://dblp.org/pid/386/3012.html"}]

Based on the search results, here's what I found about AAVENUE and the related benchmark dataset:

## AAVENUE Benchmark Overview

AAVENUE (AAVE Natural Language Understanding Evaluation) is a benchmark for evaluating large language model (LLM) performance on NLU tasks in AAVE and Standard American English (SAE).

## Key Features

AAVENUE builds upon and extends existing benchmarks like VALUE, replacing deterministic syntactic and morphological transformations with a more flexible methodology leveraging LLM-based translation with few-shot prompting, improving performance across evaluation metrics when translating key tasks from the GLUE and SuperGLUE benchmarks.

The benchmark used GPT-4o-mini with few-shot prompting to translate 1000 data points for each task from SAE to AAVE.

## Evaluation Metrics

AAVENUE compares translations using five popular LLMs and a comprehensive set of metrics including fluency, BARTScore, quality, coherence, and understandability. Additionally, fluent AAVE speakers were recruited to validate translations for authenticity.

## Key Findings

LLMs consistently perform better on SAE tasks than AAVE-translated versions, underscoring inherent biases and highlighting the need for more inclusive NLP models.

The research appears to have been published in 2024 and the code has been open-sourced on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cb10021-a8fb-44d4-8fc4-01cb05793bff",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "16a1990a-5ddf-4af6-95ff-9c8849535ebc",
  "sourceToolAssistantUUID": "3cb10021-a8fb-44d4-8fc4-01cb05793bff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T07:22:40.505Z_

<details><summary>↩ Tool result · `toolu_01Cg8EPZ1hQPpPz2vo6DSEe1`</summary>

```text
Web search results for query: "arxiv 2603.04409 HUMAINE demographic LLM evaluation"

Links: [{"title":"[2603.04409] Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework","url":"https://arxiv.org/abs/2603.04409"},{"title":"Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework","url":"https://arxiv.org/html/2603.04409"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2603.04409"},{"title":"Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework | OpenReview","url":"https://openreview.net/forum?id=kVaE2kYjtV"},{"title":"HumanLLM: Benchmarking and Improving LLM Anthropomorphism via Human Cognitive Patterns","url":"https://arxiv.org/html/2601.10198v4"},{"title":"Evaluating LLMs for Demographic-Targeted Social Bias Detection: A Comprehensive Benchmark Study","url":"https://arxiv.org/html/2510.04641v1"},{"title":"Human-Centered Evaluation of an LLM-Based Process Modeling Copilot: A Mixed-Methods Study with Domain Experts","url":"https://arxiv.org/html/2603.12895"},{"title":"Evaluating LLMs for Detecting Demographic-Targeted Social Bias: A Comprehensive Benchmark Study","url":"https://arxiv.org/html/2510.04641"},{"title":"Spark-LLM-Eval: A Distributed Framework for Statistically Rigorous Large Language Model Evaluation","url":"https://arxiv.org/html/2603.28769"},{"title":"[2510.04641v1] Evaluating LLMs for Demographic-Targeted Social Bias Detection: A Comprehensive Benchmark Study","url":"https://arxiv.org/abs/2510.04641v1"}]

I found the paper you're looking for! Here's what I found about arxiv 2603.04409:

## HUMAINE: Demographically Aware Evaluation with LLMs

The paper is titled "Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework" by Nora Petrova and Andrew Gordon, submitted on February 3, 2026.

### Key Overview
The paper introduces HUMAINE, a framework for multidimensional, demographically aware measurement of human-AI interaction. The researchers collected multi-turn, naturalistic conversations from 23,404 participants stratified across 22 demographic groups in the US and UK to evaluate 28 state-of-the-art models across five human-centric dimensions.

### Main Findings
The paper establishes a clear performance hierarchy where google/gemini-2.5-pro ranks first overall, with a 95.6% posterior probability of being the top-ranked model.

A significant finding is the uncovering of preference heterogeneity, with user age emerging as the primary demographic axis of disagreement; a model's perceived rank can shift substantially across age groups, exposing failures in generalisation that unrepresentative samples typically mask.

### Methodology
The paper uses a hierarchical Bayesian Bradley-Terry-Davidson (BTD) model with post-stratification to census data.

The paper was published as a conference paper at ICLR 2026 and includes a released dataset, interactive leaderboard, and open-source framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06b6975d-6231-4313-8641-8be7ed09aa3e",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "2728709e-26ac-4c90-88e1-6d792ab11644",
  "sourceToolAssistantUUID": "06b6975d-6231-4313-8641-8be7ed09aa3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T07:22:42.468Z_

<details><summary>↩ Tool result · `toolu_012PY44x4sUPGVYWVeYP4A7c`</summary>

```text
Web search results for query: "arxiv 2504.02234 steering vectors demographic injection"

Links: [{"title":"arXiv:2504.02234v2 [cs.HC] 5 Jun 2025","url":"https://arxiv.org/pdf/2504.02234"},{"title":"Position: LLM Social Simulations Are a Promising Research Method","url":"https://arxiv.org/html/2504.02234"},{"title":"Predicting Where Steering Vectors Succeed","url":"https://arxiv.org/html/2604.15557v1"},{"title":"Analyzing the Generalization and Reliability of Steering Vectors","url":"https://arxiv.org/html/2407.12404v1"},{"title":"Analysing the Safety Pitfalls of Steering Vectors","url":"https://arxiv.org/html/2603.24543v1"},{"title":"UNDERSTANDING (UN)RELIABILITY OF STEERING ...","url":"https://openreview.net/pdf?id=JZiKuvIK1t"},{"title":"Analysing the Generalisation and Reliability of Steering Vectors","url":"https://arxiv.org/html/2407.12404v6"},{"title":"EasyEdit2: An Easy-to-use Steering Framework for Editing Large Language Models","url":"https://arxiv.org/html/2504.15133v3"},{"title":"Steering Awareness: Detecting Activation Steering from Within","url":"https://arxiv.org/html/2511.21399v3"},{"title":"A Unified Understanding and Evaluation of Steering Methods","url":"https://arxiv.org/html/2502.02716v1"}]

I found the paper arxiv 2504.02234. The paper discusses how it could be challenging to identify vectors that precisely match real human diversity or specific model behaviors, given concerns about mechanistic superposition, although recent work suggests that superposed concepts may themselves reflect sociocultural features.

Regarding steering vectors and demographic injection specifically, a recent approach being tested is the injection of variation directly into the model. Prompting and steering vectors inject information at the beginning of the forward pass, but token sampling occurs after the final logit calculations.

The paper also notes that some studies of LLM steering vectors have found limited usefulness and detrimental side effects, particularly for debiasing and out-of-distribution (OOD) generalization.

The research appears to be from a position paper titled "LLM Social Simulations Are a Promising Research Method" (updated June 5, 2025) that discusses the use of steering vectors in the context of LLM social simulations, including considerations about demographic diversity and the limitations of current steering approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "424d6da3-8a1e-41d1-a094-0c0babfd1fd5",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "1e0d89c9-19c9-4c13-a0dc-aa9187acc47e",
  "sourceToolAssistantUUID": "424d6da3-8a1e-41d1-a094-0c0babfd1fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T07:22:43.642Z_

<details><summary>↩ Tool result · `toolu_017DYEgZ5Zvggwa6YCTXquXw`</summary>

```text
Web search results for query: "Svarah Indian English dataset"

Links: [{"title":"GitHub - AI4Bharat/Svarah: Swarah: Indian-English speech dataset collected across the country · GitHub","url":"https://github.com/AI4Bharat/Svarah"},{"title":"ai4bharat/Svarah · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ai4bharat/Svarah"},{"title":"Svarah Indian English complete dataset","url":"https://www.kaggle.com/datasets/shivanshpotdar/svarah-indian-english-complete-dataset"},{"title":"svarah","url":"https://datasets.ai4bharat.org/svarah/"},{"title":"Svarah: Evaluating English ASR Systems on Indian Accents","url":"https://www.isca-archive.org/interspeech_2023/javed23_interspeech.pdf"},{"title":"[2305.15760] Svarah: Evaluating English ASR Systems on Indian Accents","url":"https://arxiv.org/abs/2305.15760"},{"title":"IndicST-Dataset","url":"https://ai-labs.olakrutrim.com/models/IndicST-Dataset"},{"title":"(PDF) Svarah: Evaluating English ASR Systems on Indian Accents","url":"https://www.researchgate.net/publication/371040550_Svarah_Evaluating_English_ASR_Systems_on_Indian_Accents"},{"title":"Svarah/README.md at master · AI4Bharat/Svarah","url":"https://github.com/AI4Bharat/Svarah/blob/master/README.md"},{"title":"An Indic accented English speech dataset","url":"https://ai4bharat.iitm.ac.in/datasets/svarah"}]

Here's what I found about the Svarah Indian English dataset:

## Overview

Svarah is a benchmark that contains 9.6 hours of transcribed English audio from 117 speakers across 65 districts across 19 states in India, resulting in a diverse range of accents.

## Purpose and Motivation

India is the second largest English-speaking country in the world with a speaker base of roughly 130 million, but Indian speakers find a very poor representation in existing English ASR benchmarks such as LibriSpeech, Switchboard, Speech Accent Archive, etc.

## Dataset Composition

The collective set of native languages spoken by the speakers covers 19 of the 22 constitutionally recognized languages of India, belonging to 4 different language families. Svarah includes both read speech and spontaneous conversational data, covering a variety of domains such as history, culture, tourism, government, sports, etc. It also contains data corresponding to popular use cases such as ordering groceries, making digital payments, and using government services.

## Evaluation Results

6 open source ASR models and 2 commercial ASR systems were evaluated on Svarah, showing that there is clear scope for improvement on Indian accents.

## Availability

The dataset is publicly available and released under the CC BY 4.0 license. You can access it on Hugging Face and the AI4Bharat GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be61e1bf-d415-4975-9b37-eed9bd441035",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "969d97b2-c9d3-4ab7-b8ce-7e6a0db4e2eb",
  "sourceToolAssistantUUID": "be61e1bf-d415-4975-9b37-eed9bd441035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T07:22:45.121Z_

Now let me search for the remaining items:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "969d97b2-c9d3-4ab7-b8ce-7e6a0db4e2eb",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatVAPv7vNbMRbjEaXrmW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3079c730-bd48-4ee2-9ff6-9f6be7b7a4db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2RPUcVva3dXibDYwhDTK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5161,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5161,
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

_source line 14 · 2026-05-10T07:22:45.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019mSEiJ71mr2MdQVgyZtXZQ`</summary>

```json
{
  "query": "NatCS customer service dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3079c730-bd48-4ee2-9ff6-9f6be7b7a4db",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatVAPv7vNbMRbjEaXrmW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6709948b-ac57-4b3a-8d98-fcc4051bf9c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2RPUcVva3dXibDYwhDTK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5161,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5161,
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

_source line 15 · 2026-05-10T07:22:45.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UgvLqGBb1RBJswnfQ3uuuv`</summary>

```json
{
  "query": "\"DPO user simulator calibration\" arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6709948b-ac57-4b3a-8d98-fcc4051bf9c0",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatVAPv7vNbMRbjEaXrmW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "077a58c0-4ea6-43dc-b878-bec3d42ee27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2RPUcVva3dXibDYwhDTK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5161,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5161,
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

_source line 16 · 2026-05-10T07:22:46.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EarQQmYNY4tRfLtMvjFHug`</summary>

```json
{
  "query": "\"retrieval augmented few-shot user simulation\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "077a58c0-4ea6-43dc-b878-bec3d42ee27c",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatVAPv7vNbMRbjEaXrmW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "903fd007-f4b9-4b51-97f4-05858dc03ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2RPUcVva3dXibDYwhDTK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5161,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5161,
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

_source line 17 · 2026-05-10T07:22:46.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K5ohBfstfRWUmjn72VCjHo`</summary>

```json
{
  "query": "\"CORAAL\" corpus AAVE dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "903fd007-f4b9-4b51-97f4-05858dc03ef5",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatVAPv7vNbMRbjEaXrmW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cc38ef64-ac0f-42ae-8cd7-42901eef8d7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2RPUcVva3dXibDYwhDTK4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5161,
      "cache_read_input_tokens": 16917,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5161
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 213,
          "cache_read_input_tokens": 16917,
          "cache_creation_input_tokens": 5161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5161,
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

_source line 18 · 2026-05-10T07:22:52.368Z_

<details><summary>↩ Tool result · `toolu_01K5ohBfstfRWUmjn72VCjHo`</summary>

```text
Web search results for query: ""CORAAL" corpus AAVE dataset"

Links: [{"title":"zsayers/CORAAL · Datasets at Hugging Face","url":"https://huggingface.co/datasets/zsayers/CORAAL"},{"title":"CORAAL | Online Resources for African American Language","url":"https://oraal.uoregon.edu/coraal"},{"title":"Racial disparities in automated speech recognition | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.1915768117"},{"title":"Self-supervised Speech Representations Still Struggle with ...","url":"https://arxiv.org/pdf/2408.14262"},{"title":"About this Project | Online Resources for African American Language","url":"https://oraal.uoregon.edu/about"},{"title":"14 Managing Sociolinguistic Data with the Corpus of Regional African American Language (CORAAL) | part of The Open Handbook of Linguistic Data Management | MIT Press books | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9740211/"},{"title":"Corpus of Regional African American Language (@CorpusAAL) / X","url":"https://x.com/corpusaal?lang=en"},{"title":"AAVE Corpus Generation and Low-Resource Dialect Machine Translation","url":"https://dl.acm.org/doi/fullHtml/10.1145/3674829.3675060"},{"title":"Alexander Johnson's research works | University of California, Los Angeles and other places","url":"https://www.researchgate.net/scientific-contributions/Alexander-Johnson-2215428558"},{"title":"Racial disparities in automated speech recognition Allison Koeneckea","url":"https://www.pnas.org/doi/pdf/10.1073/pnas.1915768117"}]

Based on the search results, here's what I found about the CORAAL corpus:

## Overview

The Corpus of Regional African American Language (CORAAL) is the first public corpus of AAL data. CORAAL is a subset of the Online Resources for African American Language (ORAAL) project, initiated by a team of linguistics researchers at the University of Oregon.

## Dataset Contents

CORAAL features recorded speech from regional varieties of AAL and includes the audio recordings along with time-aligned orthographic transcription from over 220 sociolinguistic interviews from speakers born between 1888 and 2005. Each interview includes accompanying audio files and human-transcribed transcripts.

## Significance and Use

CORAAL was released in January 2018 as the first public corpus of AAL data. The dataset has become an important resource for research on African American Language. It has been widely used in studies examining topics like racial disparities in automated speech recognition systems and the linguistic features of AAVE.

## Licensing and Access

The materials on this website, including the Corpus of Regional African American Language is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike (4.0) International license.

The dataset is available through multiple platforms, including the official ORAAL website and research repositories like Hugging Face, making it accessible to researchers and educators interested in studying African American Language.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc38ef64-ac0f-42ae-8cd7-42901eef8d7e",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "ed6d35e1-ce65-4cfa-a2ed-7f836476f7ab",
  "sourceToolAssistantUUID": "cc38ef64-ac0f-42ae-8cd7-42901eef8d7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T07:22:52.949Z_

<details><summary>↩ Tool result · `toolu_01UgvLqGBb1RBJswnfQ3uuuv`</summary>

```text
Web search results for query: ""DPO user simulator calibration" arxiv 2025 2026"

Links: [{"title":"Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models","url":"https://arxiv.org/html/2605.02626v1"},{"title":"[2412.14516] Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment","url":"https://arxiv.org/abs/2412.14516"},{"title":"Arxiv Dives - Direct Preference Optimization (DPO)","url":"https://ghost.oxen.ai/arxiv-dives-direct-preference-optimization-dpo/"},{"title":"3D-Properties: Identifying Challenges in DPO and Charting a Path Forward | OpenReview","url":"https://openreview.net/forum?id=9Hxdixed7p"},{"title":"Pre-DPO: Improving Data Utilization in Direct Preference Optimization Using a Guiding Reference Model","url":"https://arxiv.org/html/2504.15843v2"},{"title":"Pre-DPO: Improving Data Utilization in Direct Preference Optimization","url":"https://arxiv.org/pdf/2504.15843"},{"title":"Cal-DPO: Calibrated Direct Preference Optimization for ...","url":"https://arxiv.org/pdf/2412.14516"},{"title":"Mirroring Users: Towards Building Preference-aligned User Simulator with User Feedback in Recommendation","url":"https://arxiv.org/html/2508.18142v3"},{"title":"Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment","url":"https://arxiv.org/html/2412.14516v1"},{"title":"Online DPO: Online Direct Preference Optimization with Fast-Slow Chasing","url":"https://arxiv.org/html/2406.05534v1"}]

I found several relevant papers related to DPO and calibration from 2025-2026. Here are the key findings:

## DPO Calibration Papers (2025-2026)

**Cal-DPO: Calibrated Direct Preference Optimization**

Cal-DPO is a simple yet effective algorithm that calibrates the implicit reward to ensure that the learned implicit rewards are comparable in scale to the ground-truth rewards. The contrastive objective focuses mainly on the relative values of implicit rewards associated with two responses while ignoring their actual values, resulting in suboptimal alignment with human preferences, which Cal-DPO addresses.

**Gradient-Gated DPO (2025)**

Cal-DPO calibrates the scale of implicit rewards, and is being compared with other recent approaches like IPO and gradient-gated methods for stabilizing preference optimization. Cal-DPO is mentioned as a calibration-based mitigation strategy compared against data augmentation via extended SFT and loss redesign via IPO.

**Pre-DPO (2025)**

Pre-DPO improves the performance of existing well-tuned preference optimization methods by introducing a guiding reference model, effectively overcoming the performance ceiling caused by inefficient data utilization under traditional reference model settings.

Regarding user simulators specifically, I found one paper on LLM-based user simulators for recommendation systems, but not one directly combining DPO, user simulator calibration together in the 2025-2026 timeframe. Would you like me to search for more specific information on any of these topics?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "077a58c0-4ea6-43dc-b878-bec3d42ee27c",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "2b1f9169-ac05-4732-98b6-a4e14e13fc80",
  "sourceToolAssistantUUID": "077a58c0-4ea6-43dc-b878-bec3d42ee27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T07:22:54.431Z_

<details><summary>↩ Tool result · `toolu_019mSEiJ71mr2MdQVgyZtXZQ`</summary>

```text
Web search results for query: "NatCS customer service dataset"

Links: [{"title":"[2305.03007] NatCS: Eliciting Natural Customer Support Dialogues","url":"https://arxiv.org/abs/2305.03007"},{"title":"NatCS: Eliciting natural customer support dialogues - Amazon Science","url":"https://www.amazon.science/publications/natcs-eliciting-natural-customer-support-dialogues"},{"title":"NatCS: Eliciting Natural Customer Support Dialogues - ACL Anthology","url":"https://aclanthology.org/2023.findings-acl.613/"},{"title":"NatCS: Eliciting Natural Customer Support Dialogues - Consensus","url":"https://consensus.app/papers/natcs-eliciting-natural-customer-support-dialogues-gung-rose/001968fbc9af5a4583f797fefc406c9b/"},{"title":"Papers with Code - NatCS: Eliciting Natural Customer Support Dialogues","url":"https://paperswithcode.com/paper/natcs-eliciting-natural-customer-support"},{"title":"CXMArena: Unified Dataset to benchmark performance in realistic CXM Scenarios","url":"https://arxiv.org/html/2505.09436v2"},{"title":"Public customer service operations records - Dataset - Catalog","url":"https://catalog.data.gov/dataset/public-customer-service-operations-records-6f74b"},{"title":"Customer Support Ticket Dataset","url":"https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset"},{"title":"Evaluating, Synthesizing, and Enhancing for Customer Support Conversation","url":"https://arxiv.org/html/2508.04423"},{"title":"Customer Service Chat Data 30k Rows","url":"https://www.kaggle.com/datasets/aimack/customer-service-chat-data-30k-rows"}]

Based on the search results, here's information about the NatCS customer service dataset:

## Overview

NatCS is a multi-domain collection of spoken customer service conversations. It was created to address a gap where there exist remarkably few publicly available datasets that reflect the expected characteristics of real customer support conversations, as existing task-oriented dialogue datasets are not representative of real customer support conversations.

## Data Collection Methodology

The dataset was collected through a process of gathering synthetic conversations between customers and agents based on natural language phenomena observed in real conversations. Compared to previous dialogue datasets, the conversations collected with this approach are more representative of real human-to-human conversations along multiple metrics.

## Applications and Features

NatCS provides annotations for dialogue act classification and intent induction from conversations as potential applications, showing that dialogue act annotations in NatCS provide more effective training data for modeling real conversations compared to existing synthetic written datasets.

## Availability

The dataset was publicly released to facilitate research in natural dialog systems. The dataset was introduced in a paper published in May 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6709948b-ac57-4b3a-8d98-fcc4051bf9c0",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "8198efb2-b4b8-4e7d-a8ff-45151270fabc",
  "sourceToolAssistantUUID": "6709948b-ac57-4b3a-8d98-fcc4051bf9c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T07:22:55.349Z_

<details><summary>↩ Tool result · `toolu_01EarQQmYNY4tRfLtMvjFHug`</summary>

```text
Web search results for query: ""retrieval augmented few-shot user simulation" 2025 2026"

Links: [{"title":"Retrieval-Augmented Few-shot Text Classification | OpenReview","url":"https://openreview.net/forum?id=b6e1wV03hy&noteId=3OvgxpY8Xh"},{"title":"Retrieval-Augmented Generation for AI-Generated Content: A Survey | Data Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41019-025-00335-5"},{"title":"Atlas: Few-shot Learning with Retrieval Augmented ...","url":"https://jmlr.org/papers/volume24/23-0037/23-0037.pdf"},{"title":"[2512.04106] Retrieval-Augmented Few-Shot Prompting Versus Fine-Tuning for Code Vulnerability Detection","url":"https://arxiv.org/abs/2512.04106"},{"title":"GitHub - facebookresearch/atlas: Code repository for supporting the paper \"Atlas Few-shot Learning with Retrieval Augmented Language Models\",(https//arxiv.org/abs/2208.03299) · GitHub","url":"https://github.com/facebookresearch/atlas"},{"title":"Few-shot Learning with Retrieval Augmented Language Model","url":"https://www.researchgate.net/publication/362545126_Few-shot_Learning_with_Retrieval_Augmented_Language_Model"},{"title":"Atlas: Few-shot learning with retrieval augmented ...","url":"https://research.facebook.com/blog/2023/1/atlas-few-shot-learning-with-retrieval-augmented-language-models/"},{"title":"Trends in Active Retrieval Augmented Generation: 2025 and Beyond","url":"https://www.signitysolutions.com/blog/trends-in-active-retrieval-augmented-generation"},{"title":"Retrieval-style In-context Learning for Few-shot Hierarchical Text Classification | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00697/124630/Retrieval-style-In-context-Learning-for-Few-shot"},{"title":"[2208.03299] Atlas: Few-shot Learning with Retrieval Augmented Language Models","url":"https://arxiv.org/abs/2208.03299"}]

Here are the search results for "retrieval augmented few-shot user simulation" from 2025-2026:

## Recent Research (2025-2026)

Retrieval-augmented few-shot prompting has emerged as a practical approach to improve performance in specialized tasks like code vulnerability detection, where the goal is to identify security-relevant weaknesses in code snippets. Research shows that retrieval-augmented prompting consistently outperforms other prompting strategies, achieving an F1 score of 74.05% and partial match accuracy of 83.90% at 20 shots.

## General Trends in Retrieval-Augmented Few-Shot Learning

AI models will be able to retrieve and produce highly personalized content thanks to developments in fine-tuning approaches like few-shot prompting and low-rank adaptation (LoRA). Self-querying RAG models will automatically evaluate and reword search queries to obtain more pertinent information, utilizing low-rank adaptation, context-aware prompting, and few-shot prompting.

Recent approaches include ReACT, which uses Chain-of-Thought to break queries down for recursive retrieval, and RATP, which uses Monte-Carlo Tree Search for simulations to select optimal retrieval content.

## Key Frameworks

Earlier foundational work includes Atlas, a retrieval augmented language model able to learn knowledge intensive tasks with very few training examples, evaluated on tasks including MMLU, KILT and NaturalQuestions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "903fd007-f4b9-4b51-97f4-05858dc03ef5",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "457f3ea5-9fb1-4c7a-afea-667919141fe4",
  "sourceToolAssistantUUID": "903fd007-f4b9-4b51-97f4-05858dc03ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T07:22:56.912Z_

Let me do one more targeted search for steering vectors and demographic injection more specifically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "457f3ea5-9fb1-4c7a-afea-667919141fe4",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatVBFxfcqgpzrZMAfoib",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c6a6b97-5fab-412e-a17b-4cdc7b896a61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UHkunc9wUXQUUCogrKGWsK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 2907,
      "cache_read_input_tokens": 22078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2907,
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

_source line 23 · 2026-05-10T07:22:57.154Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CgAK1jFhxbcC5t5hyNypDq`</summary>

```json
{
  "query": "site:arxiv.org 2504.02234"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c6a6b97-5fab-412e-a17b-4cdc7b896a61",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatVBFxfcqgpzrZMAfoib",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de6ade66-851a-43df-b6df-ed6280572980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UHkunc9wUXQUUCogrKGWsK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 2907,
      "cache_read_input_tokens": 22078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2907,
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

_source line 24 · 2026-05-10T07:22:57.371Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019xipGxzGJfGcrUSpGwUZ1N`</summary>

```json
{
  "query": "\"steering vectors\" \"demographic\" LLM injection 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de6ade66-851a-43df-b6df-ed6280572980",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatVBFxfcqgpzrZMAfoib",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "804f91bd-0d38-41fa-83b5-a32e0c090098",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UHkunc9wUXQUUCogrKGWsK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 2907,
      "cache_read_input_tokens": 22078,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 796,
          "output_tokens": 128,
          "cache_read_input_tokens": 22078,
          "cache_creation_input_tokens": 2907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2907,
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

_source line 25 · 2026-05-10T07:23:01.218Z_

<details><summary>↩ Tool result · `toolu_01CgAK1jFhxbcC5t5hyNypDq`</summary>

```text
Web search results for query: "site:arxiv.org 2504.02234"

Links: [{"title":"arXiv:2504.02234v2 [cs.HC] 5 Jun 2025","url":"https://arxiv.org/pdf/2504.02234"},{"title":"[2504.02234] LLM Social Simulations Are a Promising Research Method","url":"https://arxiv.org/abs/2504.02234"},{"title":"Position: LLM Social Simulations Are a Promising Research Method","url":"https://arxiv.org/html/2504.02234"},{"title":"[2505.02234] Many-body critical phase in a quasiperiodic chain and dynamical Widom lines in Fock space properties","url":"https://arxiv.org/abs/2505.02234"},{"title":"[2512.02234] The $O(N)$ Free-Scalar and Wilson-Fisher Conformal Field Theories on the Fuzzy Sphere","url":"https://arxiv.org/abs/2512.02234"},{"title":"Mask-informed Deep Contrastive Incomplete Multi-view Clustering","url":"https://arxiv.org/html/2502.02234"},{"title":"[2503.02234] Anomaly detection in non-stationary videos using time-recursive differencing network based prediction","url":"https://arxiv.org/abs/2503.02234"},{"title":"Explicit constructions of mutually unbiased bases via Hadamard matrices","url":"https://arxiv.org/html/2604.02234"},{"title":"Many-body critical phase in a quasiperiodic chain and dynamical Widom lines in Fock space properties","url":"https://arxiv.org/html/2505.02234"},{"title":"[2502.02234] Mask-informed Deep Contrastive Incomplete Multi-view Clustering","url":"https://arxiv.org/abs/2502.02234"}]

Based on the search results, I found the paper you're looking for:

**Title:** "LLM Social Simulations Are a Promising Research Method"

**Content:** Accurate and verifiable large language model (LLM) simulations of human research subjects promise an accessible data source for understanding human behavior and training new AI systems.

The paper notes that while results to date have been limited, few social scientists have adopted this method.

The paper was published on arXiv on June 5, 2025, and is categorized under cs.HC (Human-Computer Interaction). You can access it at:
- Abstract: https://arxiv.org/abs/2504.02234
- PDF: https://arxiv.org/pdf/2504.02234
- HTML: https://arxiv.org/html/2504.02234


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de6ade66-851a-43df-b6df-ed6280572980",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "06420502-b5e9-413b-926b-350b9dfae519",
  "sourceToolAssistantUUID": "de6ade66-851a-43df-b6df-ed6280572980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T07:23:04.639Z_

<details><summary>↩ Tool result · `toolu_019xipGxzGJfGcrUSpGwUZ1N`</summary>

```text
Web search results for query: ""steering vectors" "demographic" LLM injection 2025"

Links: [{"title":"Representation Steering in Neural Models","url":"https://www.emergentmind.com/topics/representation-steering"},{"title":"The Impact of Steering Large Language Models with Persona Vectors in Educational Applications","url":"https://arxiv.org/html/2604.07102"},{"title":"A Sober Look at Steering Vectors for LLMs","url":"https://www.alignmentforum.org/posts/QQP4nq7TXg89CJGBh/a-sober-look-at-steering-vectors-for-llms"},{"title":"Steering Vectors: Beamforming to LLM Control","url":"https://www.emergentmind.com/topics/steering-vectors"},{"title":"Steering Large Language Models with Activation Vectors: A Practical Guide | by Rupak (Bob) Roy - II | Medium","url":"https://bobrupakroy.medium.com/steering-large-language-models-with-activation-vectors-a-practical-guide-45866b3697ac"},{"title":"Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/html/2503.05371v2"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Latent Steering Vectors in Deep Models","url":"https://www.emergentmind.com/topics/latent-steering-vectors"},{"title":"Robust Behavior Control in LLMs via Steering Target Atoms","url":"https://aclanthology.org/2025.acl-long.1139.pdf"},{"title":"[2502.18862] One-shot Optimized Steering Vectors Mediate Safety-relevant Behaviors in LLMs","url":"https://arxiv.org/abs/2502.18862"}]

Based on the search results, here's what I found on steering vectors related to demographic attributes and LLM injection in 2025:

## Demographic Applications

KL-projected affine steering achieves exact demographic parity or equal opportunity in LLM classification without training, and outperforms mean-matching and linear erasure techniques (Sharma et al., 19 Sep 2025).

The first application of steering vectors to social biases such as racial, gender, socioeconomic and age biases has been documented, with comprehensive empirical results comparing steering vectors to other methods and demonstrating that they are a generalizable and efficient strategy for fairness interventions in LLMs.

## Technical Methods

Most steering methods add a 'steering vector' (SV) to the model's activations at a given layer and token position during inference. Methods include Contrastive Activation Addition (CAA), which computes mean-difference between positive and negative activation samples, and Principal Component Analysis (PCA), which derives principal components of activation differences.

## Safety and Control Concerns

Recent research has examined potential risks. Steering vectors have emerged as a promising approach for interpreting and controlling LLMs, but current methods typically require large contrastive datasets that are often impractical to construct and may capture spurious correlations. Additionally, one-shot optimized steering vectors can transfer across inputs with high attack success rates, and steering vectors optimized to induce harmful behavior in one context can cause models to respond harmfully on unrelated prompts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "804f91bd-0d38-41fa-83b5-a32e0c090098",
  "isSidechain": true,
  "promptId": "790e7a94-7525-4ebb-a9fa-5abe8b4cadf2",
  "agentId": "a9fec471c265f132a",
  "type": "user",
  "uuid": "1400ed72-a274-4336-bb90-b009922684ce",
  "sourceToolAssistantUUID": "804f91bd-0d38-41fa-83b5-a32e0c090098",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T07:23:34.541Z_

Excellent. Now let me compile a comprehensive report of all findings:

## Summary of Literature Search Results

### **Paper 1: HUMAINE Framework (arXiv 2603.04409)**
**Status:** EXISTS - Published as conference paper at ICLR 2026

**Title:** "Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework"

**What it does:**
- Introduces HUMAINE, a framework for multidimensional, demographically aware measurement of human-AI interaction
- Collected multi-turn, naturalistic conversations from 23,404 participants stratified across 22 demographic groups in the US and UK
- Evaluates 28 state-of-the-art models across five human-centric dimensions using hierarchical Bayesian Bradley-Terry-Davidson (BTD) model with post-stratification to census data
- Discovered preference heterogeneity with user age as the primary demographic axis of disagreement—model rankings can shift substantially across demographic groups
- Released dataset, interactive leaderboard, and open-source framework

**Overlap with DemoCalib:** Direct competitor/baseline. HUMAINE measures demographic preference variation across LLMs but uses human raters, not user simulation. DemoCalib would complement this by using calibrated LLM user simulators to extend demographic evaluation at scale.

---

### **Paper 2: LLM-based Conversational User Simulation Survey (arXiv 2604.24977)**
**Status:** EXISTS - Submitted April 27, 2026

**Title:** "A Survey on LLM-based Conversational User Simulation"

**What it does:**
- Comprehensive survey covering LLM-based user simulation
- Introduces novel taxonomy covering user granularity and simulation objectives
- Systematically analyzes core techniques and evaluation methodologies
- Authors from 11+ institutions including Vanderbilt, Adobe Research, Yale, UC San Diego, UC Berkeley

**Overlap with DemoCalib:** Directly relevant foundational work. DemoCalib would be positioned as a specific technique within this broader survey space—focusing on demographic calibration of user simulators via DPO.

---

### **Paper 3: Steering Vectors & Demographic Injection (arXiv 2504.02234)**
**Status:** PARTIALLY MATCHES - "LLM Social Simulations Are a Promising Research Method" (position paper)

**Actual Title:** "Position: LLM Social Simulations Are a Promising Research Method"

**What it does:**
- Position paper arguing that LLM simulations of human research subjects promise accessible data for understanding behavior and training AI systems
- Discusses limitations of current approaches
- Published June 5, 2025 (cs.HC category)

**Regarding steering vectors specifically:** The search found this is NOT primarily a steering vector paper. However, separate 2025 research on steering vectors for demographic control shows:
- Shifting Perspectives work (arXiv 2503.05371) demonstrates steering vectors for robust bias mitigation
- KL-projected affine steering achieves exact demographic parity in LLM classification without training
- Methods include Contrastive Activation Addition (CAA) and PCA-based approaches

**Overlap with DemoCalib:** The position paper supports LLM simulation as viable research method. The steering vector work shows alternative approaches to demographic control (steering during inference) vs. DemoCalib's approach (DPO-based preference calibration during training).

---

### **Dataset 4: CORAAL and AAVENUE**
**Status:** BOTH EXIST

**CORAAL (Corpus of Regional African American Language):**
- First public corpus of AAL data from University of Oregon's ORAAL project
- 220+ sociolinguistic interviews with speakers born 1888-2005
- Time-aligned audio + transcripts
- Licensed CC-BY-NC-SA 4.0
- Available on Hugging Face, ORAAL website
- Used in studies of racial disparities in ASR systems

**AAVENUE (AAVE Natural Language Understanding Evaluation):**
- arXiv 2408.14845 - published 2024, presented at ACL NLP4PI workshop
- Benchmark for evaluating LLM performance on NLU tasks in AAVE vs. SAE
- Used GPT-4o-mini with few-shot prompting to translate 1000 data points per task from GLUE/SuperGLUE
- Evaluated by fluent AAVE speakers for authenticity
- Code open-sourced on GitHub
- **Key finding:** LLMs consistently perform worse on AAVE-translated versions, showing inherent biases

**Overlap with DemoCalib:** AAVENUE provides ground-truth performance gaps across dialects. DemoCalib could use AAVENUE as an evaluation benchmark to verify that demographically-calibrated user simulators can better identify these dialect-based performance disparities.

---

### **Dataset 5: Svarah (Indian English)**
**Status:** EXISTS - Publicly available

**Overview:**
- 9.6 hours of transcribed English audio from 117 speakers across 65 districts in 19 states of India
- Covers 19 of 22 constitutionally recognized Indian languages (4 language families)
- Read speech + spontaneous conversational data; domains: history, culture, tourism, government, sports, ordering, payments, government services
- Evaluation shows clear scope for improvement on Indian accents with 6 open-source + 2 commercial ASR models
- Licensed CC BY 4.0
- Available on Hugging Face, GitHub (AI4Bharat/Svarah), Kaggle

**Overlap with DemoCalib:** Svarah could serve as a demographic annotation source—speakers with documented regional/linguistic backgrounds. DemoCalib could use it to calibrate user simulators for Indian English interactions.

---

### **Dataset 6: NatCS (Customer Service)**
**Status:** EXISTS - arXiv 2305.03007, published in ACL 2023

**Overview:**
- Multi-domain collection of spoken customer service conversations
- Addresses gap in realistic customer support dialogue datasets
- More representative of human-to-human conversations than synthetic dialogue datasets
- Includes annotations for dialogue act classification and intent induction
- Dialogue act annotations from NatCS provide more effective training data than existing synthetic written datasets
- Released publicly May 2023

**Overlap with DemoCalib:** NatCS could serve as an evaluation domain. DemoCalib could assess whether demographically-calibrated user simulators can better simulate diverse customer service interactions.

---

### **Paper 7: DPO User Simulator Calibration (2025-2026)**
**Status:** Related work exists but no exact match

**Found:**
- **Cal-DPO** (arXiv 2412.14516): "Calibrated Direct Preference Optimization for Language Model Alignment"
  - Calibrates implicit reward scale to match ground-truth rewards
  - Addresses suboptimal alignment in standard DPO
  
- **Gradient-Gated DPO** (arXiv 2605.02626): "Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models"
  - Recent 2025-2026 stability improvements
  
- **Pre-DPO** (arXiv 2504.15843): "Improving Data Utilization in Direct Preference Optimization Using a Guiding Reference Model"
  - Addresses performance ceiling from inefficient data utilization

**Note:** No papers directly combining "DPO + user simulator calibration" were found. **This represents a research gap that DemoCalib appears to address.**

**Overlap with DemoCalib:** DemoCalib would be positioned as a novel contribution: applying calibration techniques (inspired by Cal-DPO) specifically to user simulator preference alignment.

---

### **Paper 8: Retrieval-Augmented Few-Shot User Simulation (2025-2026)**
**Status:** General RAG + few-shot techniques exist, but no exact match for "retrieval augmented few-shot user simulation"

**Found:**
- **Retrieval-Augmented Few-Shot Prompting** (arXiv 2512.04106): Approaches for code vulnerability detection achieve F1 74.05%
- **Atlas** (arXiv 2208.03299): Few-shot learning with retrieval-augmented language models
- General RAG trends for 2025-2026: Self-querying RAG, ReACT (Chain-of-Thought), RATP (Monte-Carlo Tree Search)

**Status:** RAG for few-shot learning is established. Specific application to user simulator calibration appears novel/unexplored.

**Overlap with DemoCalib:** If DemoCalib incorporates RAG for few-shot user simulation context, it would be combining two emerging techniques in a novel way.

---

## Key Findings Summary

| Item | Status | Key Finding |
|------|--------|-------------|
| HUMAINE (2603.04409) | ✓ EXISTS | Direct competitor: human-rated demographic preference evaluation framework |
| LLM User Sim Survey (2604.24977) | ✓ EXISTS | Foundational taxonomy paper; DemoCalib fits within this space |
| Steering Vectors (2504.02234) | ⚠ PARTIAL | Position paper on LLM social sim; steering vector demographic work is separate |
| CORAAL | ✓ EXISTS | AAL corpus with 220+ interviews; available and used widely |
| AAVENUE | ✓ EXISTS | AAVE NLU benchmark; shows LLM dialect disparities |
| Svarah | ✓ EXISTS | Indian English ASR corpus; 9.6 hours, 117 speakers |
| NatCS | ✓ EXISTS | Customer service dialogue; annotated with dialogue acts |
| DPO Calibration | ⚠ PARTIAL | Cal-DPO & Pre-DPO exist; no user simulator + DPO calibration combo found |
| RAG Few-Shot | ⚠ PARTIAL | General techniques exist; specific user simulator application unexplored |

**Research Positioning:** DemoCalib appears novel in specifically combining DPO-based calibration with demographic user simulator training and evaluation—filling a gap between HUMAINE (human evaluation) and general user simulation surveys.

---

### Sources

Key papers and datasets referenced:
- [HUMAINE Framework (arXiv 2603.04409)](https://arxiv.org/abs/2603.04409)
- [LLM-based Conversational User Simulation Survey (arXiv 2604.24977)](https://arxiv.org/abs/2604.24977)
- [LLM Social Simulations Position Paper (arXiv 2504.02234)](https://arxiv.org/abs/2504.02234)
- [Shifting Perspectives: Steering Vectors for Bias Mitigation (arXiv 2503.05371)](https://arxiv.org/html/2503.05371v2)
- [AAVENUE: AAVE NLU Benchmark (arXiv 2408.14845)](https://arxiv.org/abs/2408.14845)
- [CORAAL Dataset](https://oraal.uoregon.edu/coraal)
- [Svarah Indian English (arXiv 2305.15760)](https://arxiv.org/abs/2305.15760)
- [NatCS Customer Service (arXiv 2305.03007)](https://arxiv.org/abs/2305.03007)
- [Cal-DPO (arXiv 2412.14516)](https://arxiv.org/abs/2412.14516)
- [Pre-DPO (arXiv 2504.15843)](https://arxiv.org/abs/2504.15843)
- [Retrieval-Augmented Few-Shot Code Detection (arXiv 2512.04106)](https://arxiv.org/abs/2512.04106)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1400ed72-a274-4336-bb90-b009922684ce",
  "isSidechain": true,
  "agentId": "a9fec471c265f132a",
  "requestId": "req_011CatVBwi6N5ScSG7th5myk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "069becc2-ebfe-4c97-a77e-a56358a2b5db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "234621b0-adb1-49ac-aed6-167fc469d59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LsNG23d4Lhnwq3swdcXXV1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2505,
      "cache_read_input_tokens": 24985,
      "output_tokens": 2828,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2505
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2828,
          "cache_read_input_tokens": 24985,
          "cache_creation_input_tokens": 2505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2505,
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
