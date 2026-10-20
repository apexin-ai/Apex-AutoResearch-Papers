# Research conversation: Search the web for concurrent and recent work on benchmark contamination calibration, provenance tracking for LLM benchm

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a8ff5f0005b6f3661.jsonl`
- **Structured JSON:** [`c1d980f9356cb1766e97.json`](../../sessions/c1/c1d980f9356cb1766e97.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-11T22:43:17.796Z_

Search the web for concurrent and recent work on benchmark contamination calibration, provenance tracking for LLM benchmarks, and score adjustment methods. I need to know if anyone is already doing this specific thing: building a system that takes a model's benchmark score + contamination exposure and outputs a calibrated/adjusted score.

Perform these searches:
1. WebSearch: "benchmark contamination calibration score adjustment 2026"
2. WebSearch: "provenance tracking benchmark contamination LLM 2026"
3. WebSearch: "arxiv benchmark contamination calibration 2025 2026"
4. WebSearch: "openreview benchmark contamination score calibration ICML NeurIPS 2026"
5. WebSearch: "semantic decontamination benchmark LLM paraphrase 2025 2026"
6. WebSearch: "contamination aware evaluation LLM calibrated scores"

For each search, report the key findings. Specifically note:
- Any paper that proposes calibrating/adjusting benchmark scores based on contamination levels
- Any paper doing provenance tracking for training data vs benchmark items
- Any system that produces "adjusted scores with uncertainty bounds"
- Papers from 2025-2026 on semantic near-duplicate detection for benchmarks

Report findings concisely but comprehensively. Include paper titles, venues, dates, and URLs where possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "9c222dc6-963c-446a-aed0-d84e8f0ecebd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T22:43:17.800Z_

```json
{
  "parentUuid": "9c222dc6-963c-446a-aed0-d84e8f0ecebd",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
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
  "uuid": "4dcfa63f-3a77-45e4-80bb-624ce3329141",
  "timestamp": "2026-05-11T22:43:17.800Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T22:43:20.211Z_



I'll load the WebSearch tool first, then run all six searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dcfa63f-3a77-45e4-80bb-624ce3329141",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbArpLnorhvKgPAQmws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea812475-c5ee-471c-86ec-8ae52509af54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHrHGKs5fS2cY9gK5UjxQb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8130,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8130,
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

_source line 4 · 2026-05-11T22:43:20.483Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CaZQa4WKgwYYgug7SFygjW`</summary>

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
  "parentUuid": "ea812475-c5ee-471c-86ec-8ae52509af54",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbArpLnorhvKgPAQmws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "517a8d5b-6e2b-4548-ba6a-80f335374ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHrHGKs5fS2cY9gK5UjxQb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8130,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8130,
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

_source line 5 · 2026-05-11T22:43:20.486Z_

<details><summary>↩ Tool result · `toolu_01CaZQa4WKgwYYgug7SFygjW`</summary>

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
  "parentUuid": "517a8d5b-6e2b-4548-ba6a-80f335374ebc",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "6d59d370-cbc2-4e74-aeb4-63ca20e27bf9",
  "sourceToolAssistantUUID": "517a8d5b-6e2b-4548-ba6a-80f335374ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T22:43:24.071Z_



Now I'll run all six searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d59d370-cbc2-4e74-aeb4-63ca20e27bf9",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbB4zKZ18wSS2su2Bdb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c1e6ba8-e596-4dcd-9ff5-d41801aa86d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhVbDcD22taB6xDMxtPRLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 7 · 2026-05-11T22:43:24.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DvQWsNTLBiU79QLRsNG3WY`</summary>

```json
{
  "query": "benchmark contamination calibration score adjustment 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c1e6ba8-e596-4dcd-9ff5-d41801aa86d6",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbB4zKZ18wSS2su2Bdb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73695569-5bf6-4b2f-ae1a-8c42d0f15448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhVbDcD22taB6xDMxtPRLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 8 · 2026-05-11T22:43:25.027Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SxqTuuQWPhyguWR1gynuAX`</summary>

```json
{
  "query": "provenance tracking benchmark contamination LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73695569-5bf6-4b2f-ae1a-8c42d0f15448",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbB4zKZ18wSS2su2Bdb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b546db5a-8b69-4c93-b935-2de2537e1f1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhVbDcD22taB6xDMxtPRLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 9 · 2026-05-11T22:43:25.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JgFug7cZ7y8da6cdMhbJYA`</summary>

```json
{
  "query": "arxiv benchmark contamination calibration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b546db5a-8b69-4c93-b935-2de2537e1f1f",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbB4zKZ18wSS2su2Bdb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb6632bb-ba9f-4f6e-b4d9-0d10b22be547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhVbDcD22taB6xDMxtPRLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 10 · 2026-05-11T22:43:26.441Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q24Lv3Wuy1EUv3Pd8nC2ae`</summary>

```json
{
  "query": "openreview benchmark contamination score calibration ICML NeurIPS 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb6632bb-ba9f-4f6e-b4d9-0d10b22be547",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbB4zKZ18wSS2su2Bdb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75033ff3-7d13-4509-9343-da6c41df6ff6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhVbDcD22taB6xDMxtPRLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 11 · 2026-05-11T22:43:26.910Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mi6FBLxUrzcTE4Ra9pgdvZ`</summary>

```json
{
  "query": "semantic decontamination benchmark LLM paraphrase 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75033ff3-7d13-4509-9343-da6c41df6ff6",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbB4zKZ18wSS2su2Bdb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59bfbec7-e23a-4c7c-904a-21532c8e3393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhVbDcD22taB6xDMxtPRLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 12 · 2026-05-11T22:43:27.451Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NHQdzeFaD3NGYbjTUk9XfP`</summary>

```json
{
  "query": "contamination aware evaluation LLM calibrated scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59bfbec7-e23a-4c7c-904a-21532c8e3393",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbB4zKZ18wSS2su2Bdb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6668accd-0f13-4fcd-8613-0990fe107239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhVbDcD22taB6xDMxtPRLj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8130,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1409
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 315,
          "cache_read_input_tokens": 8130,
          "cache_creation_input_tokens": 1409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1409,
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

_source line 13 · 2026-05-11T22:43:31.966Z_

<details><summary>↩ Tool result · `toolu_01DvQWsNTLBiU79QLRsNG3WY`</summary>

```text
Web search results for query: "benchmark contamination calibration score adjustment 2026"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"},{"title":"OpenAI o3 SWE-Bench Score: What Engineers Aren't Told","url":"https://neuralwired.com/2026/04/13/openai-o3-swe-bench-benchmark/"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"2026-advance-notice.pdf","url":"https://www.cms.gov/files/document/2026-advance-notice.pdf"},{"title":"GitHub - LiveCodeBench/LiveCodeBench: Official repository for the paper \"LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code\" · GitHub","url":"https://github.com/livecodebench/livecodebench"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"Particle Counter Calibration Guidance","url":"https://www.beckman.com/support/faq/industry-standards/particle-counter-calibration-guidance"},{"title":"Chapter 4 BQSR | A practical introduction to GATK 4 on Biowulf (NIH HPC)","url":"https://hpc.nih.gov/training/gatk_tutorial/bqsr.html"},{"title":"Claude Benchmarks (2026): Every Score for Opus 4.6, Sonnet 4.6 & Haiku","url":"https://www.morphllm.com/claude-benchmarks"},{"title":"A Benchmark, Expand, and Calibration (BenchExCal) Trial Emulation Approach for Using Real-World Evidence to Support Indication Expansions: Design and Process for a Planned Empirical Evaluation - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40067205/"}]

Based on the search results, I found relevant information about benchmark contamination and score adjustment in 2026, particularly in the context of large language model (LLM) evaluation:

## Key Findings on Benchmark Contamination and Score Adjustment (2026)

**Data Contamination Issues:**

OpenAI's own February 2026 deprecation post identified training-data contamination, defective tests, and benchmark saturation as reasons the score no longer reliably measures frontier capability.

**SWE-Bench Verification Concerns:**

The company declared that benchmark contaminated, saturated, and no longer fit for frontier measurement on February 22, 2026. Specifically, OpenAI's internal audit of 138 problems found defective tests, arbitrarily narrow pass criteria, and evidence of training data contamination.

**Calibration and Adjustment Frameworks:**

The DCR Factor represents the calculated data contamination risk, with Accadj representing the result adjusted using the DCR Factor. The DCR Factor not only diagnoses contamination severity but also yields calibrated, contamination-aware metrics that enable fairer cross-model comparisons.

**Broader Impact on Benchmarking:**

Benchmark scores fail to predict production performance for two reasons: saturation and data contamination. In response, LiveCodeBench uses rolling updates to stay contamination-resistant, with new programming questions added monthly from competitive programming platforms, so models cannot be trained on the test set.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73695569-5bf6-4b2f-ae1a-8c42d0f15448",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "2523a3a4-42b7-4a6c-93d1-344434e0eeb9",
  "sourceToolAssistantUUID": "73695569-5bf6-4b2f-ae1a-8c42d0f15448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T22:43:33.474Z_

<details><summary>↩ Tool result · `toolu_01SxqTuuQWPhyguWR1gynuAX`</summary>

```text
Web search results for query: "provenance tracking benchmark contamination LLM 2026"

Links: [{"title":"LLM Benchmark Confidence & Contamination Flags — Which Scores Can You Trust? | BenchLM.ai","url":"https://benchlm.ai/benchmark-confidence"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"MMLU Benchmark for LLM Evaluation","url":"https://www.emergentmind.com/topics/mmlu-benchmark"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"GitHub - LiveBench/LiveBench: LiveBench: A Challenging, Contamination-Free LLM Benchmark · GitHub","url":"https://github.com/LiveBench/LiveBench"},{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark | OpenReview","url":"https://openreview.net/forum?id=sKYHBTAxVa"},{"title":"CodeCleaner: Mitigating Data Contamination for LLM Benchmarking | Proceedings of the 16th International Conference on Internetware","url":"https://dl.acm.org/doi/10.1145/3755881.3755901"},{"title":"When Benchmarks Lie: Why Contamination Breaks LLM Evaluation | by Anna Alexandra Grigoryan | Medium","url":"https://thegrigorian.medium.com/when-benchmarks-lie-why-contamination-breaks-llm-evaluation-1fa335706f32"},{"title":"A Survey from Static to Dynamic Evaluation","url":"https://aclanthology.org/2025.emnlp-main.511.pdf"}]

Based on the search results, here's what I found about provenance tracking, benchmark contamination, and LLMs in 2026:

## Provenance Tracking in Benchmarking

BenchLM tracks two key signals: (1) benchmark provenance — whether each score is a hand-entered public row ("manual") or was generated/inferred from related data, and (2) benchmark freshness — older benchmarks that haven't been updated are more likely to have been contaminated through training data inclusion. Manual scores are hand-entered public rows, while "generated" scores were inferred from related models or interpolated.

## Contamination Detection Methods

In 2026, five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

## Contamination-Resistant Benchmarks

Several approaches address contamination:

- SWE-bench Verified is highly resistant to contamination because the problems come from real-world software development work.
- LiveBench is designed with test set contamination in mind and limits potential contamination by releasing new questions monthly, with questions based on recently-released datasets, arXiv papers, news articles, and IMDb movie synopses.
- MMLU-CF (Contamination-Free) reconstructs the benchmark to eliminate memorization artifacts via systematic decontamination: statement rephrasing, option shuffling, "None of the other choices" injection, and maintaining a closed-source test.

The field has developed sophisticated methods for both tracking provenance and mitigating contamination risks in LLM benchmarking as of 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b546db5a-8b69-4c93-b935-2de2537e1f1f",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "b2b21450-f271-40b6-86d1-9fcbb53930f9",
  "sourceToolAssistantUUID": "b546db5a-8b69-4c93-b935-2de2537e1f1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T22:43:33.620Z_

<details><summary>↩ Tool result · `toolu_01JgFug7cZ7y8da6cdMhbJYA`</summary>

```text
Web search results for query: "arxiv benchmark contamination calibration 2025 2026"

Links: [{"title":"[2311.09783] Investigating Data Contamination in Modern Benchmarks for Large Language Models","url":"https://arxiv.org/abs/2311.09783"},{"title":"[2406.04244] Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/abs/2406.04244"},{"title":"Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/html/2406.04244v1"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"How Much Can We Forget about Data Contamination?","url":"https://arxiv.org/html/2410.03249v4"},{"title":"[2502.17521] Recent Advances in Large Langauge Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation","url":"https://arxiv.org/abs/2502.17521"},{"title":"Agent Island: A Saturation- and Contamination-Resistant Benchmark from Multiagent Games","url":"https://arxiv.org/html/2605.04312v1"},{"title":"[2406.19314] LiveBench: A Challenging, Contamination-Limited LLM Benchmark","url":"https://arxiv.org/abs/2406.19314"},{"title":"[2502.17259] Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/abs/2502.17259"}]

Based on the search results, I found several relevant papers and resources related to benchmark contamination and calibration in LLM research from 2025-2026:

## Key Recent Papers on Benchmark Contamination

Data contamination has received increasing attention in the era of large language models (LLMs) due to their reliance on vast Internet-derived training corpora, and LLM benchmarking has undergone a transformation from static to dynamic benchmarking to mitigate the risk of potential data contamination.

Benchmark Data Contamination (BDC) occurs when language models inadvertently incorporate evaluation benchmark information from their training data, leading to inaccurate or unreliable performance during the evaluation phase.

## Dynamic vs. Static Benchmarking Approaches

Dynamic methods aim to reduce contamination risk either by continuously updating benchmark datasets based on LLM training timestamps or by regenerating test data to reconstruct and replace original benchmarks.

## Notable Recent Benchmarks (2024-2025)

- **LiveBench**: Contains questions based on recently-released math competitions, arXiv papers, news articles, and datasets, with harder, contamination-limited versions of tasks from previous benchmarks.

- **Watermarking Approach**: A solution involves watermarking benchmarks before their release by reformulating the original questions with a watermarked LLM, in a way that does not alter the benchmark utility.

- **Agent Island**: A multiplayer simulation environment where language-model agents compete in a game of interagent cooperation, conflict, and persuasion, yielding a dynamic benchmark designed to mitigate both saturation and contamination.

## Calibration and Data Contamination

Calibration can be skewed if the model's confidence scores are based on contaminated data, giving a false sense of reliability.

The research from 2025-2026 shows an active shift toward dynamic benchmarking methods to address contamination issues in LLM evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb6632bb-ba9f-4f6e-b4d9-0d10b22be547",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "ae79de7d-613b-4a90-99dd-791fc16c3665",
  "sourceToolAssistantUUID": "eb6632bb-ba9f-4f6e-b4d9-0d10b22be547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T22:43:34.663Z_

<details><summary>↩ Tool result · `toolu_01NHQdzeFaD3NGYbjTUk9XfP`</summary>

```text
Web search results for query: "contamination aware evaluation LLM calibrated scores"

Links: [{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.722/"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"[2310.18018] NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark","url":"https://arxiv.org/abs/2310.18018"},{"title":"Contamination-Free Evaluation","url":"https://www.emergentmind.com/topics/contamination-free-evaluation"},{"title":"Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?","url":"https://arxiv.org/html/2411.03923v1"},{"title":"When Benchmarks Lie: Why Contamination Breaks LLM Evaluation | by Anna Alexandra Grigoryan | Medium","url":"https://thegrigorian.medium.com/when-benchmarks-lie-why-contamination-breaks-llm-evaluation-1fa335706f32"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"CodeCleaner: Mitigating Data Contamination for LLM Benchmarking | Proceedings of the 16th International Conference on Internetware","url":"https://dl.acm.org/doi/10.1145/3755881.3755901"},{"title":"[2411.03923] Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?","url":"https://arxiv.org/abs/2411.03923"},{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark | OpenReview","url":"https://openreview.net/forum?id=sKYHBTAxVa"}]

I found several highly relevant results on contamination-aware evaluation of LLMs with calibrated scores. Here's what the research shows:

## Key Findings on Contamination-Aware Evaluation

Data contamination occurs when a Large Language Model is trained on the test split of a benchmark and then evaluated on the same benchmark, causing an overestimation of the model's performance compared to non-contaminated counterparts.

### Calibrated Score Approaches

Some contamination-resistant evaluation frameworks use calibrated LLMs (often validated against expert labels) to evaluate output quality, achieving high alignment with human raters.

### Contamination Detection via Distribution Calibration

CDD (Contamination Detection via output Distribution) detects data contamination by identifying the peakedness of an LLM's output distribution, while TED (Trustworthy Evaluation via output Distribution) mitigates the impact of contamination based on the correction of an LLM's output distribution.

### Context-Based Calibration (CoDeC)

Contamination Detection via Context (CoDeC) is a dataset-level method that detects data contamination via in-context learning. The design ensures that calibration is based specifically on the properties and knowledge of the model being investigated, measuring how much a model's predictions rely on memorized patterns rather than genuine reasoning.

### Empirical Assessment Framework (ConTAM)

Contamination metrics can be assessed based on whether models benefit from examples they mark as contaminated, and ConTAM is a novel analysis method showing how n-gram based contamination metrics can be better understood across multiple benchmarks and models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6668accd-0f13-4fcd-8613-0990fe107239",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "6316255d-500f-4116-97d6-2d05cd9e6195",
  "sourceToolAssistantUUID": "6668accd-0f13-4fcd-8613-0990fe107239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T22:43:34.969Z_

<details><summary>↩ Tool result · `toolu_01Mi6FBLxUrzcTE4Ra9pgdvZ`</summary>

```text
Web search results for query: "semantic decontamination benchmark LLM paraphrase 2025 2026"

Links: [{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"Rethinking Benchmark and Contamination for Language Models with","url":"https://arxiv.org/pdf/2311.04850"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/html/2404.00699v4"},{"title":"GitHub - lm-sys/llm-decontaminator: Code for the paper \"Rethinking Benchmark and Contamination for Language Models with Rephrased Samples\"","url":"https://github.com/lm-sys/llm-decontaminator"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"[2311.04850] Rethinking Benchmark and Contamination for Language Models with Rephrased Samples","url":"https://arxiv.org/abs/2311.04850"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://openreview.net/pdf?id=O3rnGt7DK7"},{"title":"Identifying Data Contamination in LLMs for Mathematical Benchmarks DIPLOMARBEIT","url":"https://repositum.tuwien.at/bitstream/20.500.12708/216244/1/Mathis%20Tobias%20Gallus%20-%202025%20-%20Identifying%20Data%20Contamination%20in%20LLMs%20for...pdf"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"}]

Based on the search results, here's what I found about semantic decontamination benchmarks for LLMs with paraphrase detection in 2025-2026:

## Key Methods and Approaches

A hybrid approach combining embedding similarity search with GPT-4 powered semantic analysis detects paraphrased samples, enabling proactive benchmark decontamination. This LLM decontaminator method first uses embedding similarity search to get the top-k samples with the highest similarity with a given test sample and then prompts a strong LLM such as GPT-4 to examine whether any of the top-k samples is too close to the test case.

## Recent Research (2024-2025)

Clean-Eval was proposed to purify contaminated benchmarks by paraphrasing and back-translating data into semantically equivalent but lexically distinct forms. Additionally, the MMLU-CF dataset was constructed by collecting diverse questions, cleaning data, sampling difficulty reasonably, checking data integrity with LLMs, and applying rewriting methods such as rephrasing questions and shuffling options to ensure the dataset remains contamination-free.

## 2026 Developments

Five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

The research emphasizes that simple variations of test data such as paraphrasing and translation can easily bypass string-matching decontamination measures, making semantic-level detection increasingly important for fair LLM evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59bfbec7-e23a-4c7c-904a-21532c8e3393",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "974ab85c-6c56-4c84-a3c2-55a0db737b10",
  "sourceToolAssistantUUID": "59bfbec7-e23a-4c7c-904a-21532c8e3393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T22:43:36.045Z_

<details><summary>↩ Tool result · `toolu_01Q24Lv3Wuy1EUv3Pd8nC2ae`</summary>

```text
Web search results for query: "openreview benchmark contamination score calibration ICML NeurIPS 2026"

Links: [{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"NeurIPS 2026 Evaluations & Datasets FAQ","url":"https://neurips.cc/Conferences/2026/EvaluationsDatasetsFAQ"},{"title":"NeurIPS 2025 Datasets & Benchmarks Track Call for Papers","url":"https://neurips.cc/Conferences/2025/CallForDatasetsBenchmarks"},{"title":"ICML 2026 – ICML Blog","url":"https://blog.icml.cc/category/icml-2026/"},{"title":"Measuring what Matters: Construct Validity in Large Language Model Benchmarks","url":"https://openreview.net/pdf?id=mdA5lVvNcU"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"ICML 2026 Reviewer Instructions","url":"https://icml.cc/Conferences/2026/ReviewerInstructions"},{"title":"Introducing the Evaluations & Datasets Track at NeurIPS 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/03/23/introducing-the-evaluations-datasets-track-at-neurips-2026/"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"Revisiting the Calibration of Modern Neural Networks | OpenReview","url":"https://openreview.net/forum?id=QRBvLayFXI"}]

Based on the search results, I found relevant information related to your query about benchmark contamination, calibration, and the conferences mentioned:

## Key Findings:

**Benchmark Contamination in NeurIPS/ICML Context:**

NeurIPS workshops and tracks welcome benchmarks on new or existing datasets, as well as benchmarking tools, including novel benchmarking methodologies and designs, with approaches to mitigate LLM contamination.

Benchmark contamination occurs both by direct contamination of benchmark items and by memorisation of partial answers or closely-related information, and is likely to occur even with model developers acting in good faith.

**NeurIPS 2026 Evaluations & Datasets Track:**

The Datasets & Benchmarks Track at NeurIPS 2026 has been officially renamed the Evaluations & Datasets (ED) Track, introducing an expanded scope that explicitly positions evaluation as a scientific object of study.

The ED Track welcomes contributions that advance the science of AI evaluation, including work that analyzes strengths, limitations, or failure modes of existing benchmarks or evaluation practices, and studies benchmark saturation or overfitting and their impact on scientific conclusions.

**Score Calibration (ICML 2026):**

The Isotonic Mechanism is a computationally efficient approach to enhancing the accuracy of noisy review scores by incorporating authors' self-rankings of their submissions, where authors with multiple submissions are asked to rank their papers in descending order of perceived quality, and the pre-rebuttal scores are then calibrated to be consistent with these rankings.

The search results show how both ICML and NeurIPS 2026 are addressing evaluation methodology challenges, including contamination detection and score calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75033ff3-7d13-4509-9343-da6c41df6ff6",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "3e58f362-b924-4e77-817b-48acd992b6c5",
  "sourceToolAssistantUUID": "75033ff3-7d13-4509-9343-da6c41df6ff6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-11T22:43:39.509Z_

Let me run a few more targeted searches to drill deeper into the specific "adjusted score" angle and the DCR paper that appeared.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e58f362-b924-4e77-817b-48acd992b6c5",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbCCo9jGUnF5Vtr6wwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c50c4f68-1a85-47c2-920c-2add1409b468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnBVwMxgevq9PqiamtFCkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1890,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 9539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4046,
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

_source line 20 · 2026-05-11T22:43:40.518Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0182iWPzACLRJB2XLygSAfuD`</summary>

```json
{
  "query": "DCR data contamination risk factor adjusted accuracy benchmark LLM paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c50c4f68-1a85-47c2-920c-2add1409b468",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbCCo9jGUnF5Vtr6wwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc5315f8-9004-4b66-a594-684ac8d6c316",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnBVwMxgevq9PqiamtFCkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1890,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 9539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4046,
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

_source line 21 · 2026-05-11T22:43:40.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cwvu7y36ZUc2r6HezWagQw`</summary>

```json
{
  "query": "TED trustworthy evaluation output distribution contamination correction calibrated score"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc5315f8-9004-4b66-a594-684ac8d6c316",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbCCo9jGUnF5Vtr6wwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a30d588-cabe-44f7-bf9e-216d647a7b5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnBVwMxgevq9PqiamtFCkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1890,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 9539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4046,
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

_source line 22 · 2026-05-11T22:43:41.507Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Fe3STYZmNaGXcjHyKBhZ4`</summary>

```json
{
  "query": "BenchLM benchmark confidence contamination flags provenance score adjustment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a30d588-cabe-44f7-bf9e-216d647a7b5c",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbCCo9jGUnF5Vtr6wwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99eb1376-1e26-4488-adaa-8454855bf995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnBVwMxgevq9PqiamtFCkg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1890,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 9539,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4046
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1890,
          "output_tokens": 188,
          "cache_read_input_tokens": 9539,
          "cache_creation_input_tokens": 4046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4046,
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

_source line 23 · 2026-05-11T22:43:47.026Z_

<details><summary>↩ Tool result · `toolu_01Cwvu7y36ZUc2r6HezWagQw`</summary>

```text
Web search results for query: "TED trustworthy evaluation output distribution contamination correction calibrated score"

Links: [{"title":"Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.716/"},{"title":"Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models","url":"https://arxiv.org/html/2402.15938v1"},{"title":"[2402.15938] Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models","url":"https://arxiv.org/abs/2402.15938"},{"title":"Evaluating Data Contamination for Large Language Models","url":"https://web.stanford.edu/~zhangxm/Generalization_or_Memorization__Evaluating_Data_Contamination_for_Large_Language_Models.pdf"},{"title":"Data Contamination and Trustworthy Evaluation for Large ...","url":"https://aclanthology.org/2024.findings-acl.716.pdf"},{"title":"[Literature Review] Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models","url":"https://www.themoonlight.io/en/review/generalization-or-memorization-data-contamination-and-trustworthy-evaluation-for-large-language-models"},{"title":"[Quick Review] Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models","url":"https://liner.com/review/generalization-or-memorization-data-contamination-and-trustworthy-evaluation-for-large"},{"title":"[PDF] Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Generalization-or-Memorization:-Data-Contamination-Dong-Jiang/1ea243f1b697aae22e6f0349fa64857780a6108a"},{"title":"Generalization or Memorization- Data Contamination and Trustworthy Evaluation for Large Language Models | PDF | Applied Mathematics | Artificial Intelligence","url":"https://www.scribd.com/document/907411452/Generalization-or-Memorization-Data-Contamination-and-Trustworthy-Evaluation-for-Large-Language-Models"},{"title":"TED: A Tolerant Edit Distance for segmentation evaluation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1046202316305072"}]

Based on the search results, I found information about your query. The results primarily refer to a research paper on data contamination in large language models.

## TED: Trustworthy Evaluation via output Distribution

TED is a method designed to mitigate the impact of data contamination in evaluation, based on the correction of LLM's output distribution.

### How TED Works

TED includes two rules to correct the LLM's output distribution: exclude peakedness and remove duplicates. More specifically:

- **Exclude Peakedness**: This aims to restore the uncontaminated sampling results by excluding the peakedness in the LLM's output distribution, while excluding the greedy text which is most likely to represent the leaked data potentially memorized by the LLM.

- **Remove Duplicates**: This aims to remove the duplicate sampling results, especially those differing from the most likely output, which are also less likely to duplicately occur in the uncontaminated sampling results.

### Performance and Impact

TED successfully mitigates the impact of data contamination in evaluation across various scenarios. Additionally, TED substantially mitigates performance improvements up to 66.9% attributed to data contamination across various contamination setups.

The method represents part of a broader research effort to detect and mitigate data contamination issues in large language models through analyzing output distribution patterns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a30d588-cabe-44f7-bf9e-216d647a7b5c",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "beb14ec9-7f05-402a-8630-eed3464616ed",
  "sourceToolAssistantUUID": "6a30d588-cabe-44f7-bf9e-216d647a7b5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-11T22:43:49.420Z_

<details><summary>↩ Tool result · `toolu_019Fe3STYZmNaGXcjHyKBhZ4`</summary>

```text
Web search results for query: "BenchLM benchmark confidence contamination flags provenance score adjustment"

Links: [{"title":"LLM Benchmark Confidence & Contamination Flags — Which Scores Can You Trust? | BenchLM.ai","url":"https://benchlm.ai/benchmark-confidence"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/html/2603.21636"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"[2406.18326] PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2406.18326"},{"title":"The Anatomy of an LLM Benchmark - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/llm-bench"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"livebench:achallenging, contamination-limited llm benchmark","url":"https://arxiv.org/pdf/2406.19314"},{"title":"When Benchmarks Lie: Why Contamination Breaks LLM Evaluation | by Anna Alexandra Grigoryan | Medium","url":"https://thegrigorian.medium.com/when-benchmarks-lie-why-contamination-breaks-llm-evaluation-1fa335706f32"},{"title":"LiveBench","url":"https://livebench.ai/"}]

Based on the search results, here's what I found about BenchLM's approach to benchmark confidence, contamination flags, and provenance:

## Benchmark Provenance and Confidence Ratings

BenchLM tracks two key signals: (1) benchmark provenance — whether each score is a hand-entered public row ("manual") or was generated/inferred from related data, and (2) benchmark freshness — older benchmarks that haven't been updated are more likely to have been contaminated through training data inclusion.

Models with mostly generated data or stale benchmarks receive lower confidence ratings.

## Provenance Categories

"Manual" scores are hand-entered public rows from BenchLM's dataset work. "Generated" scores were inferred from related models or interpolated. Generated rows are excluded from all public ranking logic.

Manual rows are now split again into sourced rows for the verified leaderboard and source-unverified rows that can still appear in provisional mode.

## Confidence Indicators

The confidence indicator (1-4 dots) shows how much sourced benchmark coverage supports each model's score. A 4-dot score is backed by 20+ sourced benchmark rows across 7+ categories. A 1-dot score relies on limited sourced coverage, and the provisional leaderboard may still include source-unverified non-generated rows.

## Ranking Structure

The provisional leaderboard uses rankable non-generated rows; the verified leaderboard uses sourced rows only.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99eb1376-1e26-4488-adaa-8454855bf995",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "5feec5c5-3e86-4673-a228-f4fe922a43e7",
  "sourceToolAssistantUUID": "99eb1376-1e26-4488-adaa-8454855bf995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T22:43:50.933Z_

<details><summary>↩ Tool result · `toolu_0182iWPzACLRJB2XLygSAfuD`</summary>

```text
Web search results for query: "DCR data contamination risk factor adjusted accuracy benchmark LLM paper"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/html/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"},{"title":"[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/abs/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"A Survey from Static to Dynamic Evaluation","url":"https://aclanthology.org/2025.emnlp-main.511.pdf"},{"title":"Identifying Data Contamination in LLMs for Mathematical Benchmarks DIPLOMARBEIT","url":"https://repositum.tuwien.at/bitstream/20.500.12708/216244/1/Mathis%20Tobias%20Gallus%20-%202025%20-%20Identifying%20Data%20Contamination%20in%20LLMs%20for...pdf"},{"title":"[2406.04244] Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/abs/2406.04244"},{"title":"Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/html/2406.04244v1"},{"title":"GitHub - yale-nlp/lm-contamination-survey: This is the repo for ACL 2024 Finding paper - Unveiling the Spectrum of Data Contamination in Language Model: A Survey from Detection to Remediation · GitHub","url":"https://github.com/yale-nlp/lm-contamination-survey"}]

Based on the search results, I found the paper you're looking for:

## DCR: Quantifying Data Contamination in LLMs Evaluation

The paper introduces the Data Contamination Risk (DCR) framework, a lightweight, interpretable pipeline designed to detect and quantify benchmark data contamination (BDC) risk across four granular levels: semantic, informational, data, and label.

### Key Innovation: DCR Factor

By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance.

### Validation and Results

The DCR framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, reliably diagnosing contamination severity with accuracy adjusted using the DCR Factor to within 4% average error across the three benchmarks compared to the uncontaminated baseline.

### Publication

The paper was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025). You can find it on:
- [arXiv (2507.11405)](https://arxiv.org/abs/2507.11405)
- [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1173/)

The authors are Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, and Tahar Kechadi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc5315f8-9004-4b66-a594-684ac8d6c316",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "77282d55-6a88-4d39-9297-0593610a7850",
  "sourceToolAssistantUUID": "dc5315f8-9004-4b66-a594-684ac8d6c316",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-11T22:43:55.021Z_

Let me grab the one very promising hit -- the "Silicon Bureaucracy" paper from arxiv (2603.21636) which appears to be exactly on topic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77282d55-6a88-4d39-9297-0593610a7850",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbDJTzuXYATnw2hbW29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e7f6923-73ae-4913-bd01-0f9639da6ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYAamwcsSb73icKvQSV1WL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1799,
      "cache_creation_input_tokens": 3042,
      "cache_read_input_tokens": 13585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3042,
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

_source line 27 · 2026-05-11T22:43:55.857Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LuujvssdFDibGtzqDj3aUJ`</summary>

```json
{
  "query": "arxiv 2603.21636 \"Silicon Bureaucracy\" contamination sensitivity score confidence LLM benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e7f6923-73ae-4913-bd01-0f9639da6ca1",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbDJTzuXYATnw2hbW29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8782a575-4e9a-4602-a9b3-211ceb36148e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYAamwcsSb73icKvQSV1WL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1799,
      "cache_creation_input_tokens": 3042,
      "cache_read_input_tokens": 13585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3042,
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

_source line 28 · 2026-05-11T22:43:56.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PnkRTpk2aNWD9b7RiJwb8g`</summary>

```json
{
  "query": "\"contamination adjusted score\" OR \"decontaminated score\" OR \"corrected benchmark score\" LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8782a575-4e9a-4602-a9b3-211ceb36148e",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbDJTzuXYATnw2hbW29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fd83012-0095-463e-945d-9c28b8130228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYAamwcsSb73icKvQSV1WL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1799,
      "cache_creation_input_tokens": 3042,
      "cache_read_input_tokens": 13585,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3042
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1799,
          "output_tokens": 176,
          "cache_read_input_tokens": 13585,
          "cache_creation_input_tokens": 3042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3042,
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

_source line 29 · 2026-05-11T22:44:02.840Z_

<details><summary>↩ Tool result · `toolu_01LuujvssdFDibGtzqDj3aUJ`</summary>

```text
Web search results for query: "arxiv 2603.21636 "Silicon Bureaucracy" contamination sensitivity score confidence LLM benchmarks"

Links: [{"title":"[2603.21636] Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/abs/2603.21636"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/html/2603.21636"},{"title":"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues | Request PDF","url":"https://www.researchgate.net/publication/384215139_MT-Bench-101_A_Fine-Grained_Benchmark_for_Evaluating_Large_Language_Models_in_Multi-Turn_Dialogues"},{"title":"Rescaling Confidence: What Scale Design Reveals About LLM Metacognition","url":"https://arxiv.org/html/2603.09309"},{"title":"Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/html/2406.04244v1"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models","url":"https://arxiv.org/html/2406.18326"},{"title":"The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination | OpenReview","url":"https://openreview.net/forum?id=TuvDxubEfE"},{"title":"The Emperor’s New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination","url":"https://arxiv.org/html/2503.16402v1"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"}]

The web search found the paper you're looking for. Here are the key details:

## Paper: Silicon Bureaucracy and AI Test-Oriented Education (arXiv:2603.21636)

Public benchmarks increasingly govern how large language models (LLMs) are ranked, selected, and deployed. The researchers frame this benchmark-centered regime as "Silicon Bureaucracy and AI Test-Oriented Education," arguing that it rests on a fragile assumption: that benchmark scores directly reflect genuine generalization.

### Core Argument
In practice, such scores may conflate exam-oriented competence with principled capability, especially when contamination and semantic leakage are difficult to exclude from modern training pipelines.

### Proposed Framework
The authors propose an audit framework for analyzing contamination sensitivity and score confidence in LLM benchmarks. Using a router-worker setup, they compare a clean-control condition with noisy conditions in which benchmark problems are systematically deleted, rewritten, and perturbed before being passed downstream. For a genuinely clean benchmark, noisy conditions should not consistently outperform the clean-control baseline.

### Paper Details
The paper was submitted on March 23, 2026, and was authored by Yiliang Song, Hongjun An, Jiangan Chen, Xuanchen Yan, Huan Song, Jiawei Shao, and Xuelong Li.

You can access the full paper at: https://arxiv.org/abs/2603.21636


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8782a575-4e9a-4602-a9b3-211ceb36148e",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "cddedd30-0509-40aa-b1d8-3b683f1e8297",
  "sourceToolAssistantUUID": "8782a575-4e9a-4602-a9b3-211ceb36148e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-11T22:44:04.479Z_

<details><summary>↩ Tool result · `toolu_01PnkRTpk2aNWD9b7RiJwb8g`</summary>

```text
Web search results for query: ""contamination adjusted score" OR "decontaminated score" OR "corrected benchmark score" LLM 2025 2026"

Links: [{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"LLM evaluation benchmarks and safety datasets for 2025 | RAIL Score Knowledge Hub","url":"https://responsibleailabs.ai/knowledge-hub/articles/llm-evaluation-benchmarks-2025"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark | OpenReview","url":"https://openreview.net/forum?id=sKYHBTAxVa"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"GitHub - LiveBench/LiveBench: LiveBench: A Challenging, Contamination-Free LLM Benchmark · GitHub","url":"https://github.com/LiveBench/LiveBench"},{"title":"A Survey from Static to Dynamic Evaluation","url":"https://aclanthology.org/2025.emnlp-main.511.pdf"},{"title":"[2406.19314] LiveBench: A Challenging, Contamination-Limited LLM Benchmark","url":"https://arxiv.org/abs/2406.19314"},{"title":"livebench:achallenging, contamination-limited llm benchmark","url":"https://arxiv.org/pdf/2406.19314"},{"title":"LiveBench: A Challenging, Contamination-Free LLM Benchmark","url":"https://livebench.ai/livebench.pdf"}]

I found relevant information about LLM benchmark contamination and related scoring approaches in 2025-2026. Here are the key findings:

## Contamination Detection and Adjustment Methods

Five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

## Decontamination Approaches

Inference-Time Decontamination (ITD) addresses this issue by detecting and rewriting leaked samples without altering their difficulties. ITD can mitigate performance inflation caused by memorizing leaked benchmarks, reducing inflated accuracy by 22.9% on GSM8K and 19.0% on MMLU.

## Corrected/Adjusted Benchmark Scores

A 2026 paper titled "Quantifying the Effect of Test Set Contamination on Generative Evaluations" showed a clean dose-response curve: contamination matters most when model capacity is high and the unique pretraining corpus is small.

## Contamination-Resistant Benchmarks

Rather than adjusting scores post-hoc, recent approaches focus on contamination-resistant benchmarks. The fix is contamination-resistant benchmarks: LiveCodeBench, FrontierMath, MMLU-Pro, LiveBench.

LiveBench contains frequently-updated questions from recent information sources, scores answers automatically according to objective ground-truth values, and contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fd83012-0095-463e-945d-9c28b8130228",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "8e82e115-61f1-4fa8-a215-76174e4e5e18",
  "sourceToolAssistantUUID": "1fd83012-0095-463e-945d-9c28b8130228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-11T22:44:08.018Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sq4Yub2ou2t3hCVbAf7xTN`</summary>

```json
{
  "query": "\"inference time decontamination\" ITD leaked samples rewriting benchmark score arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e82e115-61f1-4fa8-a215-76174e4e5e18",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbEJQJWkdTv7yQmqtcX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0fb4e00-400b-4c0a-a66a-9cc452be3f72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178vremmGexMgrMqajzJBKH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3843,
      "cache_read_input_tokens": 16627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3843,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-11T22:44:08.812Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UM9aUpe8fcACivTHQxTTK8`</summary>

```json
{
  "query": "CodeCleaner mitigating data contamination benchmarking 2025 score correction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0fb4e00-400b-4c0a-a66a-9cc452be3f72",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbEJQJWkdTv7yQmqtcX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c4fab52-2964-48ed-94fb-bdee1df32712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178vremmGexMgrMqajzJBKH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3843,
      "cache_read_input_tokens": 16627,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3843
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 16627,
          "cache_creation_input_tokens": 3843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3843,
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

_source line 33 · 2026-05-11T22:44:15.077Z_

<details><summary>↩ Tool result · `toolu_01UM9aUpe8fcACivTHQxTTK8`</summary>

```text
Web search results for query: "CodeCleaner mitigating data contamination benchmarking 2025 score correction"

Links: [{"title":"CodeCleaner: Mitigating Data Contamination for LLM Benchmarking | Proceedings of the 16th International Conference on Internetware","url":"https://dl.acm.org/doi/10.1145/3755881.3755901"},{"title":"CodeCleaner: Mitigating Data Contamination for LLM Benchmarking (Internetware 2025 - Research Track) - Internetware 2025","url":"https://conf.researchr.org/details/internetware-2025/internetware-2025-research-track/20/CodeCleaner-Mitigating-Data-Contamination-for-LLM-Benchmarking"},{"title":"(PDF) CODECLEANER: Elevating Standards with A Robust Data Contamination Mitigation Toolkit","url":"https://www.researchgate.net/publication/385920941_CODECLEANER_Elevating_Standards_with_A_Robust_Data_Contamination_Mitigation_Toolkit"},{"title":"CodeCleaner: Elevating Standards with A Robust Data Contamination Mitigation Toolkit","url":"https://arxiv.org/html/2411.10842v1"},{"title":"CodeCleaner: Mitigating Data Contamination for LLM ...","url":"https://dl.acm.org/doi/pdf/10.1145/3755881.3755901"},{"title":"[2411.10842] CODECLEANER: Elevating Standards with A Robust Data Contamination Mitigation Toolkit","url":"https://arxiv.org/abs/2411.10842"},{"title":"GitHub - ArabelaTso/CodeCleaner-v1: Code refactoring for resolving data contamination","url":"https://github.com/ArabelaTso/CodeCleaner-v1"},{"title":"AI Benchmarks Are a Game Now — And the Industry Is Cheating to Win","url":"https://ucstrategies.com/news/ai-benchmarks-are-a-game-now-and-the-industry-is-cheating-to-win/"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"A Survey from Static to Dynamic Evaluation","url":"https://aclanthology.org/2025.emnlp-main.511.pdf"}]

Based on the search results, here's what I found about CodeCleaner and data contamination mitigation:

## CodeCleaner Overview

CodeCleaner is an automated code refactoring toolkit for mitigating data contamination in evaluating code language models (CLMs). It performs code refactoring to resolve data contamination following the idea of disrupting the consecutive characters/tokens as much as possible while maintaining the semantic unchanged.

## Key Features and Results

CodeCleaner includes 11 operators for Python in multiple scales and 4 for Java. Applying all operators contributes to a dramatic drop of 75% overlap ratio, demonstrating operators' exceptional capabilities in addressing data contamination.

The toolkit employs different types of refactoring operators. Semantic operators are generally much more effective than syntactic ones.

## Performance Impact

Operators cause an average drop of 19% in LLMs' accuracy in code completion task. This indicates that while CodeCleaner effectively reduces data contamination, it also impacts model performance metrics.

## Availability

CodeCleaner is made online available to facilitate applications and further studies.

The research represents the first systematic study of code refactoring operators for mitigating data contamination across multiple programming languages and scales.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c4fab52-2964-48ed-94fb-bdee1df32712",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "f3ab297f-4d52-46c3-9cc5-075dd4e07cbc",
  "sourceToolAssistantUUID": "1c4fab52-2964-48ed-94fb-bdee1df32712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-11T22:44:15.337Z_

<details><summary>↩ Tool result · `toolu_01Sq4Yub2ou2t3hCVbAf7xTN`</summary>

```text
Web search results for query: ""inference time decontamination" ITD leaked samples rewriting benchmark score arxiv"

Links: [{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://arxiv.org/html/2406.13990v1"},{"title":"[2406.13990] Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://arxiv.org/abs/2406.13990"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240613990Z/abstract"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"Reusing Leaked Benchmarks for Large Language Model ...","url":"https://aclanthology.org/2024.findings-emnlp.532.pdf"},{"title":"[2601.19334] When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/abs/2601.19334"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.532/"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation | Request PDF","url":"https://www.researchgate.net/publication/386183526_Inference-Time_Decontamination_Reusing_Leaked_Benchmarks_for_Large_Language_Model_Evaluation"}]

Based on the search results, I found comprehensive information about Inference-Time Decontamination (ITD):

## Overview

Inference-Time Decontamination (ITD) is proposed to address test data contamination in LLMs by detecting and rewriting leaked samples without altering their difficulties.

## The Problem

Leakage of benchmarks can prevent the accurate assessment of LLMs' true performance. ITD can mitigate performance inflation caused by memorizing leaked benchmarks.

## Methodology

ITD uses a detector to screen for potentially leaked samples and then rewrites these samples, attempting to mitigate the impact of memorizing answers, without changing the sample's difficulty. For different types of benchmarks, the approach varies:

- For knowledge-related benchmarks like MMLU, it keeps the knowledge points tested by the original sample unchanged and rewrites the phrasing of the questions.
- For math benchmarks related to model reasoning abilities like GSM8K, it maintains the specific numbers and calculations involved in the original data unchanged, but rewrites the background of the questions.

## Results

ITD reduces inflated accuracy by 22.9% on GSM8K and 19.0% on MMLU. On MMLU, using Inference-time Decontamination can lead to a decrease in the results of Phi3 and Mistral by 6.7% and 3.6% respectively.

The paper was published in the Findings of the Association for Computational Linguistics (EMNLP 2024) and is available on arXiv as paper 2406.13990.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0fb4e00-400b-4c0a-a66a-9cc452be3f72",
  "isSidechain": true,
  "promptId": "ee485cf2-1c16-4b1e-a4cb-fbc2a9ba09d4",
  "agentId": "a8ff5f0005b6f3661",
  "type": "user",
  "uuid": "630b44a1-96ad-4e8e-92df-db1be6fa2979",
  "sourceToolAssistantUUID": "f0fb4e00-400b-4c0a-a66a-9cc452be3f72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-11T22:45:32.057Z_

Here is the comprehensive report across all searches.

---

## Results: Prior and Concurrent Work on Benchmark Contamination Calibration

### 1. CLOSEST MATCH: DCR (Data Contamination Risk) -- Score Adjustment System

**"DCR: Quantifying Data Contamination in LLMs Evaluation"**
- Venue: EMNLP 2025 (Main Conference)
- Authors: Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, Tahar Kechadi
- Links: [arXiv 2507.11405](https://arxiv.org/abs/2507.11405) | [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1173/)

This is the most directly relevant prior work. DCR is a pipeline that:
- Detects contamination at four granular levels: semantic, informational, data, and label
- Synthesizes contamination scores via a **fuzzy inference system** into a unified **DCR Factor**
- Uses the DCR Factor to produce an **adjusted accuracy (Acc_adj)** -- i.e., it takes raw benchmark score + contamination exposure and outputs a calibrated score
- Validated on 9 LLMs (0.5B--72B) across sentiment analysis, fake news detection, and arithmetic reasoning
- Achieves adjusted scores within **4% average error** of uncontaminated baselines

**This is doing essentially the same thing you described**: model benchmark score + contamination exposure -> calibrated/adjusted score. However, it uses a fuzzy inference system rather than (potentially) a more principled statistical framework, and it does not appear to produce uncertainty bounds on the adjusted score.

---

### 2. TED (Trustworthy Evaluation via output Distribution) -- Distribution-Level Correction

**"Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models"**
- Venue: ACL 2024 Findings
- Authors: Yicheng Dong, Yue Jiang, et al.
- Links: [arXiv 2402.15938](https://arxiv.org/abs/2402.15938) | [ACL Anthology](https://aclanthology.org/2024.findings-acl.716/)

TED corrects output distributions by:
- Detecting peakedness in the LLM's output distribution (a contamination signal)
- Excluding greedy-decoded text (most likely to represent memorized leaked data)
- Removing duplicate sampling results
- Reports mitigating up to **66.9%** of performance inflation due to contamination

This is a score-correction method but operates at inference time on the output distribution rather than taking a contamination measurement as input. No uncertainty bounds.

---

### 3. Inference-Time Decontamination (ITD) -- Rewriting Leaked Samples

**"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation"**
- Venue: EMNLP 2024 Findings
- Links: [arXiv 2406.13990](https://arxiv.org/abs/2406.13990) | [ACL Anthology](https://aclanthology.org/2024.findings-emnlp.532/)

Also a 2026 follow-up: **"When Benchmarks Leak: Inference-Time Decontamination for LLMs"** ([arXiv 2601.19334](https://arxiv.org/abs/2601.19334), January 2026).

ITD:
- Detects potentially leaked samples at inference time
- Rewrites them (changing phrasing for knowledge benchmarks, changing background for math benchmarks) while preserving difficulty
- Reduces inflated accuracy by **22.9% on GSM8K** and **19.0% on MMLU**

This is a decontamination-at-evaluation-time approach rather than a post-hoc score adjustment with uncertainty.

---

### 4. Silicon Bureaucracy -- Audit Framework for Score Confidence (March 2026)

**"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks"**
- Date: March 23, 2026
- Authors: Yiliang Song, Hongjun An, Jiangan Chen, Xuanchen Yan, Huan Song, Jiawei Shao, Xuelong Li
- Link: [arXiv 2603.21636](https://arxiv.org/abs/2603.21636)

This is very recent and relevant. It:
- Proposes an **audit framework** for contamination sensitivity and **score confidence**
- Uses a router-worker setup comparing clean-control vs. noisy conditions (benchmark problems deleted, rewritten, perturbed)
- Tests whether noisy conditions outperform clean-control (which would signal contamination)
- Frames benchmark evaluation as "AI Test-Oriented Education" where scores may conflate exam-oriented competence with genuine capability

This paper addresses score confidence but does not appear to output a single calibrated adjusted score with uncertainty bounds.

---

### 5. BenchLM.ai -- Provenance Tracking Platform (Commercial, 2026)

**BenchLM Benchmark Confidence & Contamination Flags**
- Link: [benchlm.ai/benchmark-confidence](https://benchlm.ai/benchmark-confidence)

A live platform that:
- Tracks **benchmark provenance**: whether scores are hand-entered ("manual"), sourced-and-verified, or generated/interpolated
- Tracks **benchmark freshness**: older benchmarks flagged as higher contamination risk
- Assigns **confidence indicators** (1--4 dots) based on sourced benchmark coverage
- Separates "provisional" and "verified" leaderboards
- Generated rows excluded from public ranking logic

This is the closest thing to an operational provenance-tracking system for benchmark scores, though it tracks score provenance (where did the reported number come from?) rather than training data provenance (which benchmark items appeared in training data).

---

### 6. Semantic Near-Duplicate Detection (2024--2026)

Several relevant systems:

- **LLM Decontaminator** (LMSYS, 2023--ongoing): Hybrid approach using embedding similarity search + GPT-4 semantic analysis to detect paraphrased benchmark items. [arXiv 2311.04850](https://arxiv.org/abs/2311.04850) | [GitHub](https://github.com/lm-sys/llm-decontaminator)

- **MMLU-CF (Contamination-Free)**: Reconstructed MMLU with statement rephrasing, option shuffling, "None of the other choices" injection, and closed-source test set.

- **Clean-Eval**: Purifies contaminated benchmarks via paraphrasing and back-translation into semantically equivalent but lexically distinct forms.

- **CodeCleaner** (Internetware 2025): 11 code refactoring operators for Python to disrupt token overlap while preserving semantics. Achieves 75% reduction in overlap ratio. [ACL DL](https://dl.acm.org/doi/10.1145/3755881.3755901) | [arXiv 2411.10842](https://arxiv.org/abs/2411.10842)

- **Detecting Benchmark Contamination Through Watermarking** (Feb 2025): Watermarks benchmarks before release using reformulation. [arXiv 2502.17259](https://arxiv.org/abs/2502.17259)

---

### 7. Other Relevant Detection Methods

- **CDD (Contamination Detection via output Distribution)**: Detects contamination by measuring peakedness of output distributions.
- **CoDeC (Contamination Detection via Context)**: Uses in-context learning to measure how much predictions rely on memorized patterns vs. genuine reasoning. [arXiv 2510.27055](https://arxiv.org/abs/2510.27055)
- **ConStat**: Detects contamination via performance gaps on rephrased samples.
- **PaCoST**: Paired confidence significance testing for benchmark contamination detection. [arXiv 2406.18326](https://arxiv.org/abs/2406.18326)
- **"The Emperor's New Clothes in Benchmarking?"**: Rigorous examination of mitigation strategies for LLM benchmark data contamination. [arXiv 2503.16402](https://arxiv.org/abs/2503.16402) | [OpenReview](https://openreview.net/forum?id=TuvDxubEfE)

---

### 8. Venue Context: NeurIPS 2026

NeurIPS 2026 has renamed its Datasets & Benchmarks Track to the **"Evaluations & Datasets (ED) Track"**, explicitly welcoming work that "analyzes strengths, limitations, or failure modes of existing benchmarks or evaluation practices" and "studies benchmark saturation or overfitting." This is a clear signal that contamination-aware evaluation methodology is a first-class topic at a top venue.

---

## Summary Assessment: Gap Analysis

| Capability | Who's doing it? | Gap remaining? |
|---|---|---|
| Contamination detection (binary) | Many methods (CDD, CoDeC, ConStat, Min-K%, etc.) | Mature area |
| Contamination quantification (continuous score) | **DCR** (EMNLP 2025) | DCR does this but uses fuzzy inference |
| Score adjustment given contamination | **DCR** (Acc_adj), **TED**, **ITD** | DCR is closest; TED/ITD work at inference time |
| Adjusted scores **with uncertainty bounds** | **Nobody found** | This appears to be a clear gap |
| Training data provenance tracking (which items appeared in training) | Partial: watermarking (2502.17259), canary GUIDs | No full end-to-end system found |
| Benchmark score provenance tracking | **BenchLM.ai** | Tracks reporting provenance, not data provenance |
| Semantic near-duplicate detection for benchmarks | LLM Decontaminator, Clean-Eval, MMLU-CF, CodeCleaner | Active area but mostly one-off tools, not integrated systems |
| End-to-end system: benchmark score + contamination exposure -> calibrated score with uncertainty | **Nobody found doing exactly this** | **Clear open niche** |

**Bottom line**: DCR (EMNLP 2025) is the closest existing work -- it takes contamination measurements and outputs adjusted accuracy. However, it uses fuzzy inference rather than statistical modeling, does not produce uncertainty bounds, and was validated on limited benchmarks. The idea of building a principled system that takes (score, contamination exposure) and outputs (calibrated score, confidence interval) does not appear to exist yet. The March 2026 "Silicon Bureaucracy" paper discusses score confidence but does not implement the input-output pipeline you described. This looks like an open and timely research direction, especially given NeurIPS 2026's new ED Track.

Sources:
- [DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)](https://arxiv.org/abs/2507.11405)
- [DCR at ACL Anthology](https://aclanthology.org/2025.emnlp-main.1173/)
- [Generalization or Memorization: TED (ACL 2024 Findings)](https://arxiv.org/abs/2402.15938)
- [Inference-Time Decontamination (EMNLP 2024 Findings)](https://arxiv.org/abs/2406.13990)
- [When Benchmarks Leak: ITD (Jan 2026)](https://arxiv.org/abs/2601.19334)
- [Silicon Bureaucracy (March 2026)](https://arxiv.org/abs/2603.21636)
- [BenchLM Benchmark Confidence & Contamination Flags](https://benchlm.ai/benchmark-confidence)
- [LLM Decontaminator / Rethinking Benchmark and Contamination](https://arxiv.org/abs/2311.04850)
- [Detecting Benchmark Contamination Through Watermarking](https://arxiv.org/abs/2502.17259)
- [CoDeC: Contamination Detection via In-Context Learning](https://arxiv.org/abs/2510.27055)
- [PaCoST: Paired Confidence Significance Testing](https://arxiv.org/abs/2406.18326)
- [The Emperor's New Clothes in Benchmarking?](https://arxiv.org/abs/2503.16402)
- [CodeCleaner (Internetware 2025)](https://dl.acm.org/doi/10.1145/3755881.3755901)
- [LiveBench](https://arxiv.org/abs/2406.19314)
- [Recent Advances in LLM Benchmarks: Static to Dynamic Evaluation (EMNLP 2025)](https://arxiv.org/abs/2502.17521)
- [Benchmark Data Contamination Survey](https://arxiv.org/abs/2406.04244)
- [NeurIPS 2026 Evaluations & Datasets Track](https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets)
- [awesome-data-contamination GitHub](https://github.com/lyy1994/awesome-data-contamination)
- [LiveCodeBench GitHub](https://github.com/livecodebench/livecodebench)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "630b44a1-96ad-4e8e-92df-db1be6fa2979",
  "isSidechain": true,
  "agentId": "a8ff5f0005b6f3661",
  "requestId": "req_011CawbF6q4cprQXcZ1PGwSA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d874e75f-0187-4c28-97ec-78ae303a5761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d1b4105-418a-4afa-98c3-1d4311b55b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8gax57Sm1rponGTtY53QK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 1090,
      "cache_read_input_tokens": 20470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1090,
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
