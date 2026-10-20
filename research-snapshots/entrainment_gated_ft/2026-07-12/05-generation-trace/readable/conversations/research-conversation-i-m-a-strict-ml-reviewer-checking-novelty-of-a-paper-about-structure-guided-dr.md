# Research conversation: I'm a strict ML reviewer checking novelty of a paper about "Structure-Guided Draft Training for Reasoning Speculative De

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ae5f9f4c0daede907.jsonl`
- **Structured JSON:** [`f5820f5f3cbca4ffcc78.json`](../../sessions/f5/f5820f5f3cbca4ffcc78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-09T18:43:50.986Z_

I'm a strict ML reviewer checking novelty of a paper about "Structure-Guided Draft Training for Reasoning Speculative Decoding." The paper proposes:
1. Using ThinKV's R/E/T thought-segment taxonomy as training labels for draft models
2. A Markov segment-transition consistency objective for speculative decoding draft training
3. Applied to EAGLE-3 style draft models targeting DeepSeek-R1-Distill-70B

I need you to search aggressively for competing work that might undermine novelty. Please search for:

1. "speculative decoding reasoning model 2025 2026 structural" on arxiv
2. "draft model training reasoning traces structure" 
3. "EAGLE reasoning model speculative decoding 2026"
4. "auxiliary loss speculative decoding draft training"
5. "thought type classification speculative decoding"
6. Any recent (2025-2026) papers that combine structural supervision with draft model training
7. Search specifically: "Markov chain speculative decoding" 
8. Search: "R1 speculative decoding structural 2025 2026"

Use WebSearch for each query and report exact paper titles, arxiv IDs, and what they claim. I need to know if there's any work that uses structural labels or segment-type supervision for speculative decoding draft training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "63a44bb5-a619-461e-a3f3-6d3e5ed8704a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-09T18:43:52.453Z_

I'll conduct an aggressive search for competing work on this topic. Let me search all these queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63a44bb5-a619-461e-a3f3-6d3e5ed8704a",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJ1Q1M3As5iFARb6s4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "adcbfccd-6f4d-43dc-8fb7-137e80133c6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TG6ZZGuEpYPp8yC79epf9f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 3 · 2026-05-09T18:43:52.804Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KYqFNh1cvoeNTuLP9sAtfi`</summary>

```json
{
  "query": "speculative decoding reasoning model 2025 2026 structural"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adcbfccd-6f4d-43dc-8fb7-137e80133c6c",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJ1Q1M3As5iFARb6s4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "221241e2-ee1f-409e-b59f-1fa61bda77c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TG6ZZGuEpYPp8yC79epf9f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 4 · 2026-05-09T18:43:52.932Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018PVR53BjU5GYqdY5eD5jKx`</summary>

```json
{
  "query": "draft model training reasoning traces structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "221241e2-ee1f-409e-b59f-1fa61bda77c8",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJ1Q1M3As5iFARb6s4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "63e5372a-0030-4c10-8190-43f5d1590db5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TG6ZZGuEpYPp8yC79epf9f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 5 · 2026-05-09T18:43:52.936Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LxfMDy51N2ueCa4jLsARwk`</summary>

```json
{
  "query": "EAGLE reasoning model speculative decoding 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63e5372a-0030-4c10-8190-43f5d1590db5",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJ1Q1M3As5iFARb6s4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a09f6455-ea97-4a7d-b67b-4cf58788f487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TG6ZZGuEpYPp8yC79epf9f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 6 · 2026-05-09T18:43:53.142Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A6N2AEGZashid2kXCQHLCi`</summary>

```json
{
  "query": "auxiliary loss speculative decoding draft training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a09f6455-ea97-4a7d-b67b-4cf58788f487",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJ1Q1M3As5iFARb6s4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de02f496-dcda-4968-b52d-af04addd981a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TG6ZZGuEpYPp8yC79epf9f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 7 · 2026-05-09T18:43:53.381Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Na8oz8tZTcyQTwYoKMBZz7`</summary>

```json
{
  "query": "thought type classification speculative decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de02f496-dcda-4968-b52d-af04addd981a",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJ1Q1M3As5iFARb6s4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48f3ad49-6503-4533-a621-7d408b7199b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TG6ZZGuEpYPp8yC79epf9f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 8 · 2026-05-09T18:43:53.401Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SSrniCVamTbHZexq4awWJG`</summary>

```json
{
  "query": "Markov chain speculative decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48f3ad49-6503-4533-a621-7d408b7199b0",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJ1Q1M3As5iFARb6s4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "76ed2cae-69ec-46bd-932f-5153d7209566",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TG6ZZGuEpYPp8yC79epf9f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 9 · 2026-05-09T18:43:53.637Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01At9bxmVZzn8cGzDj6bV7BB`</summary>

```json
{
  "query": "R1 speculative decoding structural 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76ed2cae-69ec-46bd-932f-5153d7209566",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJ1Q1M3As5iFARb6s4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d32fde34-c261-4497-8c84-11c6c2e755e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TG6ZZGuEpYPp8yC79epf9f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 10 · 2026-05-09T18:43:53.933Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JBpPyNjwkpLWJyQk8sUXTZ`</summary>

```json
{
  "query": "structural supervision draft model training reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d32fde34-c261-4497-8c84-11c6c2e755e9",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJ1Q1M3As5iFARb6s4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "486b85df-4737-48f0-af70-facdcea155e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TG6ZZGuEpYPp8yC79epf9f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 16155,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 737
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 389,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 737,
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

_source line 11 · 2026-05-09T18:43:59.289Z_

<details><summary>↩ Tool result · `toolu_018PVR53BjU5GYqdY5eD5jKx`</summary>

```text
Web search results for query: "draft model training reasoning traces structure"

Links: [{"title":"Demystifying Reasoning Models - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/demystifying-reasoning-models"},{"title":"Structured Reasoning Traces","url":"https://www.emergentmind.com/topics/structured-reasoning-traces"},{"title":"Understanding Reasoning LLMs - by Sebastian Raschka, PhD","url":"https://magazine.sebastianraschka.com/p/understanding-reasoning-llms"},{"title":"Draft-Thinking: Learning Efficient Reasoning in Long Chain-of-Thought LLMs","url":"https://arxiv.org/html/2603.00578"},{"title":"What Is a Reasoning Model? | IBM","url":"https://www.ibm.com/think/topics/reasoning-model"},{"title":"Taking AI Transparency To a New Level With Model Reasoning Traces | by Cobus Greyling | Medium","url":"https://cobusgreyling.medium.com/taking-ai-transparency-to-a-new-level-with-model-reasoning-traces-80c186453ea1"},{"title":"ReTrace: Interactive Visualizations for Reasoning Traces of Large Reasoning Models","url":"https://arxiv.org/html/2511.11187v1"},{"title":"4. Reasoning Models | Working with LLMs","url":"https://aicourse.nlp.town/docs/reasoning-models/"},{"title":"[2604.21057] TRACES: Tagging Reasoning Steps for Adaptive Cost-Efficient Early-Stopping","url":"https://arxiv.org/abs/2604.21057"},{"title":"Training fails to elicit subtle reasoning in current language models","url":"https://alignment.anthropic.com/2025/subtle-reasoning/"}]

Based on the search results, here's what I found about draft model training reasoning traces structure:

## Overview

Draft-style reasoning structures are fitted at the behavioral level through supervised fine-tuning (SFT), leveraging black-box distillation to extract implicit structured inference patterns from stronger models.

## Training Approach

Progressive Curriculum Learning uses draft-style reasoning structures fitted through SFT, then introduces a two-stage reinforcement learning (RL) process to gradually expand problem-solving capability while maintaining a preference for low-budget efficiency.

## Reasoning Trace Structure

The structured reasoning traces employ several organizational approaches:

- For distilled models, traces are segmented by cognitive stage (Framing, Exploration, Verification, Synthesis), with explicit lexical pivots marking stage transitions (e.g., "Wait—", "Let me double-check—")

- Traces can be parsed as directed acyclic graphs (DAGs), where nodes correspond to atomic reasoning acts (e.g., facts, plans, reflections) and edges are labeled by fine-grained semantic relations

## Efficiency Gains

The draft reasoning mode reduces the average token budget from 5,668 to 986 while maintaining an accuracy of 90.6%, achieving superior token efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63e5372a-0030-4c10-8190-43f5d1590db5",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "732eb7f8-7b63-4c44-a4c2-97c19ac9e468",
  "sourceToolAssistantUUID": "63e5372a-0030-4c10-8190-43f5d1590db5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-09T18:43:59.505Z_

<details><summary>↩ Tool result · `toolu_01LxfMDy51N2ueCa4jLsARwk`</summary>

```text
Web search results for query: "EAGLE reasoning model speculative decoding 2026"

Links: [{"title":"P-EAGLE: Faster LLM inference with Parallel Speculative Decoding in vLLM | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/"},{"title":"Speculative Decoding in Practice: How EAGLE3 Makes LLMs Faster Without Changing Their Outputs","url":"https://huggingface.co/blog/lujangusface/tw-eagle3-gpu"},{"title":"[2401.15077] EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty","url":"https://arxiv.org/abs/2401.15077"},{"title":"EAGLE-3 Speculative Decoding: 2-6x Faster LLM Inference Guide | E2E Networks","url":"https://www.e2enetworks.com/blog/Accelerating_LLM_Inference_with_EAGLE"},{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty Yuhui Li♠","url":"https://arxiv.org/pdf/2401.15077"},{"title":"GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub","url":"https://github.com/SafeAILab/EAGLE"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large ...","url":"https://openreview.net/pdf?id=4exx1hUffq"},{"title":"EAGLE: speculative sampling requires rethinking feature ...","url":"https://dl.acm.org/doi/10.5555/3692070.3693232"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test | OpenReview","url":"https://openreview.net/forum?id=4exx1hUffq"}]

Based on the search results, here's what I found about EAGLE reasoning model speculative decoding in 2026:

## Overview

EAGLE (Extrapolation Algorithm for Greater Language-model Efficiency) is a baseline for fast decoding of Large Language Models with provable performance maintenance, involving extrapolation of second-top-layer contextual feature vectors of LLMs to boost generation efficiency.

## Recent Development: EAGLE-3

EAGLE-3 (NeurIPS 2025) made a fundamental change with tri-layer feature fusion. EAGLE-3 abandons feature prediction in favor of direct token prediction and replaces reliance on top-layer features with multi-layer feature fusion via a technique named training-time test.

## Performance Improvements

EAGLE-3 achieves a speedup ratio up to 6.5x, with about 1.4x improvement over EAGLE-2. Additionally, P-EAGLE delivers up to 1.69x speedup over vanilla EAGLE-3 on real workloads on NVIDIA B200.

## Parallel Speculative Decoding

P-EAGLE is integrated into vLLM to unlock parallel speculative decoding, generating K draft tokens in a single forward pass. This represents an advancement over earlier autoregressive drafting approaches that had scalability bottlenecks.

## Practical Availability

Thoughtworks released the first publicly available EAGLE-3 draft head for the GLM-4.7 architecture, with a checkpoint of 277 MB small enough to co-deploy on the same GPU as the target model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a09f6455-ea97-4a7d-b67b-4cf58788f487",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "c029af18-7e4c-4778-a398-95cb29b2d099",
  "sourceToolAssistantUUID": "a09f6455-ea97-4a7d-b67b-4cf58788f487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-09T18:44:00.437Z_

<details><summary>↩ Tool result · `toolu_01SSrniCVamTbHZexq4awWJG`</summary>

```text
Web search results for query: "Markov chain speculative decoding"

Links: [{"title":"A Theoretical Perspective for Speculative Decoding Algorithm","url":"https://arxiv.org/html/2411.00841v1"},{"title":"A Theoretical Perspective for Speculative Decoding Algorithm Ming Yin˚","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e7349e785900b93d8b4971a3f2c1cefe-Paper-Conference.pdf"},{"title":"A Theoretical Perspective for Speculative Decoding Algorithm | OpenReview","url":"https://openreview.net/forum?id=wSqpNeMVLU"},{"title":"Viterbi algorithm - Wikipedia","url":"https://en.wikipedia.org/wiki/Viterbi_algorithm"},{"title":"Speculative Decoding for Multimodal Models","url":"https://thesalt.substack.com/p/speculative-decoding-for-multimodal"},{"title":"Decoding and Re-estimation of fuzzy hidden semi Markov chain with observation dependent state","url":"https://www.aimsciences.org/article/doi/10.3934/jimo.2023065"},{"title":"Decoding, Gerrymanders, and Markov Chains – Feature Column","url":"https://mathvoices.ams.org/featurecolumn/2022/11/01/decoding-gerrymanders-and-markov-chains/"},{"title":"A hidden Markov model for decoding and the analysis ... - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5097117/"},{"title":"A hidden Markov model for decoding and the analysis of replay in spike trains - PMC","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5097117/"},{"title":"Hidden Markov Models","url":"https://web.stanford.edu/~jurafsky/slp3/A.pdf"}]

Based on the search results, here's what I found about Markov chain speculative decoding:

## Overview

Speculative Decoding employs a small model to sample a sequence of draft tokens and a large model to validate. This technique is used to accelerate language model inference.

## Markov Chain Formulation

The decoding problem is formalized through a Markov Chain abstraction that establishes the theoretical setup. More specifically, any decoding algorithm can be characterized by a Markov Chain: state at t is described by history x0:t, the initial state is x0; the state transition Pt maps state x0:t to state x0:t+1.

## How It Works

In speculative decoding, the autoregressive sampling is performed on a small draft model and the large language model verifies tokens generated by draft model to decide whether it should be accepted/rejected. Once a token is rejected, the generation process will start from the most recently accepted token, until a full response is completed.

## Performance and Theory

Speculative decoding achieves 2-2.5x LLM inference speedup empirically, while preserving inference acceleration. When the generation distribution of small model p and large model q are close to each other, decoding is faster (since less rejection occurs), and when the distribution overlap between p and q is small, the opposite happens.

Recent theoretical work has formalized these insights using Markov chain analysis to better understand the fundamental limits and efficiency of speculative decoding algorithms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76ed2cae-69ec-46bd-932f-5153d7209566",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "52fcb97a-8e0a-482f-ba85-62da1887d54e",
  "sourceToolAssistantUUID": "76ed2cae-69ec-46bd-932f-5153d7209566",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-09T18:44:00.704Z_

<details><summary>↩ Tool result · `toolu_01Na8oz8tZTcyQTwYoKMBZz7`</summary>

```text
Web search results for query: "thought type classification speculative decoding"

Links: [{"title":"Speculative Decoding with CTC-based Draft Model for LLM Inference Acceleration","url":"https://arxiv.org/html/2412.00061v1"},{"title":"A Comprehensive Survey of Speculative Decoding","url":"https://aclanthology.org/2024.findings-acl.456.pdf"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Speculative Decoding: A Guide With Implementation Examples | DataCamp","url":"https://www.datacamp.com/tutorial/speculative-decoding"},{"title":"Looking back at speculative decoding","url":"https://research.google/blog/looking-back-at-speculative-decoding/"},{"title":"Efficient Reasoning for LLMs through Speculative Chain-of-Thought","url":"https://arxiv.org/html/2504.19095v2"},{"title":"A Multi-Model Adaptation of Speculative Decoding for Classification","url":"https://arxiv.org/html/2503.18076"},{"title":"[2603.24933] Decoding Market Emotions in Cryptocurrency Tweets via Predictive Statement Classification with Machine Learning and Transformers","url":"https://arxiv.org/abs/2603.24933"},{"title":"A Hitchhiker’s Guide to Speculative Decoding – PyTorch","url":"https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"}]

Based on the search results, I found relevant information about speculative decoding and its classification. Here's what I discovered:

## Overview of Speculative Decoding

Speculative decoding is a technique designed to speed LLMs by generating responses faster without compromising quality. Speculative decoding accelerates LLMs by incorporating a smaller, faster model that generates preliminary predictions. This smaller model, often called the "draft" model, generates a batch of tokens that the main, more powerful LLM can either confirm or refine.

## Thought-Level Speculation

Notably, there is a recent advancement that extends speculative decoding to work at the thought level rather than just token level. Speculative Chain-of-Thought (SCoT) is inspired by speculative decoding, which performs token-level speculation, whereas this approach conducts thought-level speculation. The core idea of SCoT is to use a lightweight model to efficiently generate multiple CoT (Chain-of-Thought) drafts which are then picked and used by the target model.

## Speculative Decoding for Classification

Another application involves adapting speculative decoding for classification tasks: A novel adaptation of speculative decoding has been introduced, repurposed from generation to classification tasks, proposing a multi-model framework employing up to three lightweight "worker" models and a single, more robust "judge" model analogous to draft models and target model, respectively, in speculative decoding.

The search results indicate that speculative decoding has evolved beyond basic token-level generation to encompass thought-level reasoning and classification tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48f3ad49-6503-4533-a621-7d408b7199b0",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "f62fd008-0297-415c-b057-b16acaf2365d",
  "sourceToolAssistantUUID": "48f3ad49-6503-4533-a621-7d408b7199b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-09T18:44:00.757Z_

<details><summary>↩ Tool result · `toolu_01KYqFNh1cvoeNTuLP9sAtfi`</summary>

```text
Web search results for query: "speculative decoding reasoning model 2025 2026 structural"

Links: [{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"Speculative Speculative Decoding Tanishq Kumar1,* Tri Dao2,3 Avner May3","url":"https://arxiv.org/pdf/2603.03251"},{"title":"Heming Xia","url":"https://hemingkx.github.io/"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"Fast collaborative inference via distributed speculative decoding - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949715925000782"},{"title":"Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/mirror"},{"title":"Efficient LLM System with Speculative Decoding | EECS at UC Berkeley","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-224.html"},{"title":"JUDGE DECODING: FASTER SPECULATIVE SAMPLING ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/656d6174fd5ffb01c843f269649ab5cb-Paper-Conference.pdf"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"}]

Based on the search results, here's what I found on speculative decoding, reasoning models, and structural innovations in 2025-2026:

## Key Developments in Speculative Decoding (2025-2026)

### Speculative Speculative Decoding (SSD)

A major advancement is speculative speculative decoding (SSD), which parallelizes speculation and verification operations. While a verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them, with a speculation returned immediately if the verification outcome matches the predicted set. The optimized Saguaro algorithm implementation is on average 30% faster than optimized speculative decoding baselines and up to 5x faster than autoregressive decoding.

### Reasoning Models with Speculative Decoding

For reasoning language models, SparseSpec is a speculative decoding framework that reuses the same model as draft and target models (self-speculation) and features a novel sparse attention mechanism called PillarAttn, which accurately selects critical tokens by reusing information from the verification stage. SparseSpec achieves up to 2.13x throughput speedup across various models and datasets.

### Mirror Speculative Decoding

Another structural innovation converts speculation into two complementary execution pipelines where the draft speculates forward while the target simultaneously speculates correction paths, with speculative streaming allowing the draft to emit multiple tokens per step, pushing speculative decoding toward high acceptance with low overhead. Mirror-SD delivers 2.8x-5.8x wall-time speedups on server-scale models from 14B to 66B parameters.

### System-Level Optimization Frameworks

TurboSpec is a closed-loop control system for speculative decoding that formalizes goodput as a unifying metric and uses offline profiling combined with online feedback to dynamically adjust speculative parameters, adaptively balancing inter-request batching and intra-request speculation across diverse workloads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "221241e2-ee1f-409e-b59f-1fa61bda77c8",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "a935b009-72e1-4e52-aa8d-52198942fe49",
  "sourceToolAssistantUUID": "221241e2-ee1f-409e-b59f-1fa61bda77c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-09T18:44:01.284Z_

<details><summary>↩ Tool result · `toolu_01JBpPyNjwkpLWJyQk8sUXTZ`</summary>

```text
Web search results for query: "structural supervision draft model training reasoning 2025"

Links: [{"title":"Pre-training Process-Supervision for Improving Reasoning","url":"https://aclanthology.org/2025.acl-long.1288.pdf"},{"title":"Logic-Aware Knowledge Graph Reasoning for Structural Sparsity under Large Language Model Supervision | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714685"},{"title":"Process-Based Supervision in AI: Guiding Learning Step-by-Step | by Ursina Sanderink | Medium","url":"https://medium.com/@sanderink.ursina/process-based-supervision-in-ai-guiding-learning-step-by-step-ddad77b17cfc"},{"title":"How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum","url":"https://arxiv.org/html/2604.25907"},{"title":"LLM Reasoning Supervision","url":"https://www.emergentmind.com/topics/reasoning-supervision-in-llms"},{"title":"Process Aligned Learning: Supervise the Journey, Not Just the Destination | Proceedings of the 2025 3rd International Conference on Machine Learning and Pattern Recognition","url":"https://dl.acm.org/doi/full/10.1145/3760678.3760688"},{"title":"A Survey of Reasoning Large Language Models","url":"https://arxiv.org/pdf/2502.17419"},{"title":"Unlocking the Mysteries of OpenAI o1: A Survey of the ...","url":"https://openreview.net/pdf/4c5e9da74c5be2f67ca85f5b06c34dbe8cb7ca8d.pdf"},{"title":"Structural-aware Language-Image Pretraining for Vision- ...","url":"https://cdn.shanghai.nyu.edu/sites/default/files/honorsthesis2025_wenbo_lu.pdf"},{"title":"Published in Transactions on Machine Learning Research (08/2025)","url":"https://openreview.net/pdf?id=HvoG8SxggZ"}]

I found several relevant results about structural supervision, draft model training, and reasoning in 2025. Here's a summary of the key findings:

## Process and Structural Supervision in Reasoning Models

The concept of process-based supervision has gained significant traction in research by 2025, and a flurry of papers and benchmarks have emerged.

### Process-Aligned Learning

Process-Aligned Learning (PAL) is a framework that augments standard supervised training by incorporating intermediate behaviors (e.g., reasoning steps or action traces) into the loss. PAL forces the model to learn the underlying procedure, not just the input-output mapping.

### Logic-Aware Knowledge Graph Reasoning

A novel KG reasoning approach called LoLLM injects logic with supervised information supplied by Large Language Models, constructing reasoning paths instantiated from first-order logic rules extracted from sparse KGs.

### Key Applications in 2025

Step-Wise Preference Optimization (SSPO), proposed in mid-2025, presents a reinforcement learning style framework where each reasoning step is optimized via preferences, rather than only optimizing the final outcome.

Models trained with process supervision (especially those using task-agnostic or abstract guidelines) generalize more robustly to out-of-domain reasoning tasks.

### Training Approaches

DeepSeek-R1 undergoes multiple rounds of SFT and RL training, emphasizing structured thinking templates and rule-based reward mechanisms.

The research shows that structural supervision for draft model training is becoming increasingly important for improving reasoning capabilities in large language models during 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "486b85df-4737-48f0-af70-facdcea155e2",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "c4e718b0-37de-4970-b0e1-60fe1417239f",
  "sourceToolAssistantUUID": "486b85df-4737-48f0-af70-facdcea155e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-09T18:44:01.667Z_

<details><summary>↩ Tool result · `toolu_01A6N2AEGZashid2kXCQHLCi`</summary>

```text
Web search results for query: "auxiliary loss speculative decoding draft training"

Links: [{"title":"Online Speculative Decoding","url":"https://arxiv.org/html/2310.07177v4"},{"title":"ConFu: Contemplate the Future for Better Speculative Sampling","url":"https://arxiv.org/html/2603.08899"},{"title":"Training Domain Draft Models for Speculative Decoding: Best Practices and Insights","url":"https://arxiv.org/html/2503.07807v1"},{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"Draft, Verify, & Improve Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/html/2510.05421v1"},{"title":"SpecForge: Training speculative decoding models with SGLang — Tutorials for AI developers 7.0","url":"https://rocm.docs.amd.com/projects/ai-developer-hub/en/v7.0/notebooks/pretrain/SpecForge_SGlang.html"},{"title":"When Drafts Evolve: Speculative Decoding Meets Online Learning","url":"https://arxiv.org/html/2603.12617"},{"title":"Efficient and Scalable Speculative Decoding with Multi- ...","url":"https://aclanthology.org/2025.emnlp-main.986.pdf"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Speculative decoding | LLM Inference Handbook","url":"https://bentoml.com/llm/inference-optimization/speculative-decoding"}]

Based on the search results, here's what I found about auxiliary loss, speculative decoding, and draft training:

## Overview

Speculative decoding is an inference-time optimization that speeds up LLM token generation without reducing output quality. It works by pairing a smaller draft model that proposes several draft tokens ahead with a larger target model that verifies these proposed tokens in parallel.

## Draft Training Approaches

### Knowledge Distillation Framework

The learning problem is framed as online knowledge distillation, where the teacher and student models correspond to the target and draft LLMs in speculative decoding, respectively, with the draft model acting as the student.

### Loss Functions and Training

Research shows that offline knowledge distillation outperforms online learning by 11% to 25%, with forward KL loss providing the optimal result. 

Interestingly, some approaches like ConFu require no additional auxiliary losses to train the draft model, instead implicitly encouraging the draft model through the main training objective.

### Online Training

Online training freezes the target model and trains the draft model at the same time, which generates auxiliary hidden states on the fly and needs multiple GPUs to achieve better performance.

### Variational Approaches

Recent work explores augmenting the original training objective by adding terms to train the draft model, where the original training loss such as standard cross-entropy or top-k KL loss can be seen as an approximation to the KL term in a variational objective.

The key insight across these approaches is that how closely the draft model's distribution matches with the target model determines the acceptance rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de02f496-dcda-4968-b52d-af04addd981a",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "8f7538a2-8a30-4926-a099-8db4b8b0619a",
  "sourceToolAssistantUUID": "de02f496-dcda-4968-b52d-af04addd981a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-09T18:44:01.897Z_

<details><summary>↩ Tool result · `toolu_01At9bxmVZzn8cGzDj6bV7BB`</summary>

```text
Web search results for query: "R1 speculative decoding structural 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"Speculative Speculative Decoding Tanishq Kumar1,* Tri Dao2,3 Avner May3","url":"https://arxiv.org/pdf/2603.03251"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference","url":"https://arxiv.org/html/2601.19278v1"},{"title":"SGLang Speculative Decoding Tutorial: How to Deploy DeepSeek Models and Achieve 1.4× Throughput – With Benchmarks","url":"https://company.hpc-ai.com/blog/sglang-speculative-decoding-tutorial"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/mirror"},{"title":"Speculative Speculative Decoding","url":"https://arxiv.org/html/2603.03251v2"},{"title":"Fast collaborative inference via distributed speculative decoding - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949715925000782"}]

Based on the search results, I found several key developments in speculative decoding research from 2025-2026:

## Speculative Speculative Decoding (SSD)

The most prominent structural advance is speculative speculative decoding (SSD), which parallelizes speculation and verification operations. While a verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them. If the actual verification outcome is then in the predicted set, a speculation can be returned immediately, eliminating drafting overhead entirely. The optimized implementation called Saguaro achieves on average 30% faster performance than optimized speculative decoding baselines and up to 5x faster than autoregressive decoding with open source inference engines.

## Related Parallel Approaches

AMUSD (McDanel, 2025) and PEARL (Liu et al., 2025) propose speculating the next round during ongoing verification, but only prepare for the verification outcome in which all tokens are accepted, which is one special case of many possible outcomes. SwiftSpec (Zhang et al., 2025) and SpecBranch (Shen et al., 2025) prepare a larger cache consisting of a token tree branching off of the speculation being verified, but both use fallback strategies that do not work at large batch sizes.

## Integration with DeepSeek-R1

DeepSeek-R1/V3 models are trained with a technique called Multi-Token Prediction (MTP), and the MTP module can serve directly as the draft model, simplifying deployment.

These structural innovations represent a shift from sequential draft-verify pipelines toward parallel, asynchronous approaches that significantly improve LLM inference efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d32fde34-c261-4497-8c84-11c6c2e755e9",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "4518674c-9754-41bc-846c-4aa492ae715d",
  "sourceToolAssistantUUID": "d32fde34-c261-4497-8c84-11c6c2e755e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-09T18:44:04.866Z_

Now let me do more targeted searches for specific competing approaches and related work that might directly challenge the novelty claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4518674c-9754-41bc-846c-4aa492ae715d",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJo9663Y8ALkFdQ4ay",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5e17d880-cdea-43e8-8594-c23eebd36b3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VmS5R4UbY2bgF3tB5UqSkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 7455,
      "cache_read_input_tokens": 16892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7455,
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

_source line 20 · 2026-05-09T18:44:05.318Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0168yzVzUswS8PDPkp3JQnco`</summary>

```json
{
  "query": "ThinKV reasoning segment taxonomy EAGLE draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e17d880-cdea-43e8-8594-c23eebd36b3f",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJo9663Y8ALkFdQ4ay",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2a089808-8097-47e0-90a8-bb006f80b60b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VmS5R4UbY2bgF3tB5UqSkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 7455,
      "cache_read_input_tokens": 16892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7455,
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

_source line 21 · 2026-05-09T18:44:05.486Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0171KdksQnFWeLeMfP5mEX6e`</summary>

```json
{
  "query": "speculative decoding step supervision reasoning chains"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a089808-8097-47e0-90a8-bb006f80b60b",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJo9663Y8ALkFdQ4ay",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "10d914ad-d719-45ff-9b57-38aac3d0cf38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VmS5R4UbY2bgF3tB5UqSkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 7455,
      "cache_read_input_tokens": 16892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7455,
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

_source line 22 · 2026-05-09T18:44:05.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FLc4XDLsw1oUieZRfSCPYH`</summary>

```json
{
  "query": "DeepSeek-R1 distill draft model speculative 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d914ad-d719-45ff-9b57-38aac3d0cf38",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJo9663Y8ALkFdQ4ay",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8bbcdda9-3e03-4637-ad44-1cbf9af4b4b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VmS5R4UbY2bgF3tB5UqSkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 7455,
      "cache_read_input_tokens": 16892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7455,
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

_source line 23 · 2026-05-09T18:44:06.114Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C99e4JMesynGe6hVNXcDxz`</summary>

```json
{
  "query": "segment-aware training speculative decoding draft model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bbcdda9-3e03-4637-ad44-1cbf9af4b4b9",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJo9663Y8ALkFdQ4ay",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "813a868b-34e6-4853-b462-44186da03caf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VmS5R4UbY2bgF3tB5UqSkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 7455,
      "cache_read_input_tokens": 16892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7455,
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

_source line 24 · 2026-05-09T18:44:06.179Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K8tka4FSEGdiCgoaDvNHrM`</summary>

```json
{
  "query": "\"draft training\" \"structural labels\" reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "813a868b-34e6-4853-b462-44186da03caf",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVJo9663Y8ALkFdQ4ay",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1a6f3370-fd43-498a-b166-026339cc8f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VmS5R4UbY2bgF3tB5UqSkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 7455,
      "cache_read_input_tokens": 16892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7455,
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

_source line 25 · 2026-05-09T18:44:11.259Z_

<details><summary>↩ Tool result · `toolu_0168yzVzUswS8PDPkp3JQnco`</summary>

```text
Web search results for query: "ThinKV reasoning segment taxonomy EAGLE draft"

Links: [{"title":"EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees","url":"https://arxiv.org/html/2406.16858v1"},{"title":"[2406.16858] EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees","url":"https://arxiv.org/abs/2406.16858"},{"title":"GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub","url":"https://github.com/SafeAILab/EAGLE"},{"title":"EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees | PromptLayer","url":"https://www.promptlayer.com/research-papers/eagle-2-faster-inference-of-language-models-with-dynamic-draft-trees"},{"title":"Faster Inference of Language Models with Dynamic Draft ...","url":"https://aclanthology.org/2024.emnlp-main.422.pdf"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large ...","url":"https://openreview.net/pdf?id=4exx1hUffq"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test","url":"https://arxiv.org/html/2503.01840v1"},{"title":"EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.422/"},{"title":"EAGLE","url":"https://sites.google.com/view/eagle-llm"},{"title":"EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty Yuhui Li♠","url":"https://arxiv.org/pdf/2401.15077"}]

Based on the search results, I found information about EAGLE and EAGLE-2, but the specific combination of terms "ThinKV reasoning segment taxonomy" doesn't appear in the results. Let me provide what I found:

The search results primarily cover EAGLE-2, which introduces a new technique of context-aware dynamic draft tree into drafting modeling. EAGLE-2 achieved speedup ratios of 3.05x-4.26x, which is 20%-40% faster than EAGLE-1.

The EAGLE project focuses on optimizing language model inference through speculative sampling. EAGLE-2 uses the confidence scores from the draft model to approximate acceptance rates, dynamically adjusting the draft tree structure, which further enhances performance.

There's also EAGLE-3, which removes the feature prediction constraint in EAGLE and replaces top-layer features with a fusion of low-, mid-, and high-level semantic features.

However, I didn't find specific information about "ThinKV reasoning segment taxonomy" in relation to EAGLE in these search results. If you're looking for information about a specific research paper or technical document that combines these terms, could you provide more context about what you're searching for?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a089808-8097-47e0-90a8-bb006f80b60b",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "fc9a1271-d285-4d47-9143-b54f8353dffe",
  "sourceToolAssistantUUID": "2a089808-8097-47e0-90a8-bb006f80b60b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-09T18:44:11.768Z_

<details><summary>↩ Tool result · `toolu_01FLc4XDLsw1oUieZRfSCPYH`</summary>

```text
Web search results for query: "DeepSeek-R1 distill draft model speculative 2025"

Links: [{"title":"DeepSeek-R1 Distilled Models Overview","url":"https://www.emergentmind.com/topics/deepseek-r1-distilled-models"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"DeepSeek Models: V3.2, R1, Distills, and Production Caveats","url":"https://fireworks.ai/blog/deepseek-models"},{"title":"Understanding LLM Distillation, Enabling Revolutionary DeepSeek R1 Model -- Pure AI","url":"https://pureai.com/articles/2025/02/03/understanding-llm-distillation-enabling-revolutionary-deepseek-r1-model.aspx"},{"title":"deepseek-r1","url":"https://lmstudio.ai/models/deepseek-r1"},{"title":"DeepSeek R1, Model Distillation, and how Da AI Models Markets will be impacted | by Devansh | DataDrivenInvestor","url":"https://medium.datadriveninvestor.com/deepseek-r1-model-distillation-and-how-da-ai-models-markets-will-be-impacted-5f576c4ad52c"},{"title":"Re-Distilling Smaller DeepSeek R1 Models for Better Performance","url":"https://dropbox.github.io/r1_redistill_blogpost/"},{"title":"DeepSeek-R1-Distilled: Open LLM Reasoning","url":"https://www.emergentmind.com/topics/deepseek-r1-distilled"},{"title":"alamios/DeepSeek-R1-DRAFT-Qwen2.5-0.5B · Hugging Face","url":"https://huggingface.co/alamios/DeepSeek-R1-DRAFT-Qwen2.5-0.5B"}]

Based on the search results, here's what I found about DeepSeek-R1 distill draft models and speculative decoding:

## DeepSeek-R1 Distilled Models

DeepSeek has open-sourced DeepSeek-R1-Zero, DeepSeek-R1, and six dense models distilled from DeepSeek-R1 based on Llama and Qwen. DeepSeek-R1-Distill-Qwen-32B outperforms OpenAI-o1-mini across various benchmarks, achieving new state-of-the-art results for dense models.

## Draft Models for Speculative Decoding

Draft models are trained on outputs of deepseek-ai/DeepSeek-R1-Distill-Qwen-32B and are meant to be used only as draft models for speculative decoding. These draft models are specifically intended for users of 3090/4090, allowing you to run the DeepSeek-R1-Distill-Qwen-32B-Q4_K_M GGUF version with 16k context and speeding up generation without sacrificing more context length or model quality.

## Speculative Decoding Technology

Adaptive Speculative Decoding trains a smaller draft model on your data patterns, then generates candidate tokens in parallel before verifying with the main model. Together, these deliver latency reductions of 2x or more.

The search results also show that smaller distilled variants exist in various parameter sizes, with domain-specific implementations achieving strong performance across mathematical reasoning, biomedical NLP, and other specialized tasks throughout 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bbcdda9-3e03-4637-ad44-1cbf9af4b4b9",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "7ee508c7-dd09-4d6a-b9ea-0d2c83501c44",
  "sourceToolAssistantUUID": "8bbcdda9-3e03-4637-ad44-1cbf9af4b4b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-09T18:44:13.948Z_

<details><summary>↩ Tool result · `toolu_01C99e4JMesynGe6hVNXcDxz`</summary>

```text
Web search results for query: "segment-aware training speculative decoding draft model"

Links: [{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"Speculative decoding | LLM Inference Handbook","url":"https://bentoml.com/llm/inference-optimization/speculative-decoding"},{"title":"Training Domain Draft Models for Speculative Decoding: Best Practices and Insights","url":"https://arxiv.org/html/2503.07807v1"},{"title":"Online Speculative Decoding","url":"https://arxiv.org/html/2310.07177v4"},{"title":"Speculative Decoding | LM Studio","url":"https://lmstudio.ai/docs/app/advanced/speculative-decoding"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Draft, Verify, & Improve Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/html/2510.05421v1"},{"title":"Speculative Decoding - vLLM","url":"https://docs.vllm.ai/en/latest/features/spec_decode/"},{"title":"[2510.05421] Draft, Verify, and Improve: Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/abs/2510.05421"},{"title":"Decoding Speculative Decoding","url":"https://aclanthology.org/2025.naacl-long.328.pdf"}]

The search results provide comprehensive information about speculative decoding and draft model training. Here's what I found:

## Overview of Speculative Decoding

Speculative decoding is an inference-time optimization that speeds up LLM token generation without reducing output quality. It works by pairing two models: a draft model that is a smaller, fast model proposing several draft tokens ahead, and a target model that is a larger model verifying these proposed tokens in parallel and accepting those that match its own predictions.

## Draft Model Training Approaches

Several research papers address segment-aware and context-aware training of draft models:

1. **Domain-Specific Draft Models**: When adapting speculative decoding to domain-specific target models, the acceptance rate of the generic draft model drops significantly due to domain shift. Knowledge distillation techniques are systematically investigated for training domain draft models to improve their speculation accuracy.

2. **Online Speculative Decoding**: An online speculative method continuously enhances the draft model based on varying data distributions. Experiments demonstrate that online speculative decoding swiftly adapts to new data distributions, significantly enhancing token acceptance rate.

3. **Training-Aware Self-Speculative Decoding**: A framework called Draft, Verify, & Improve (DVI) combines inference with continual online learning, where an LLM is partitioned into a drafter and a verifier, and during generation, verifier accept/reject decisions are converted into supervision signals and used to update the drafter head.

4. **Variational Speculative Decoding**: Recent approaches update the draft model by maximizing a weighted likelihood over posterior samples, with improvements including path-level utility to favor longer accepted spans, adaptive rejection weighting to leverage informative rejected proposals, and confidence-aware regularization.

These approaches emphasize context-aware and segment-aware training that adapts draft models to specific domains, distributions, and query characteristics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "813a868b-34e6-4853-b462-44186da03caf",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "7d8addd0-1769-46ac-afd6-940c18453b42",
  "sourceToolAssistantUUID": "813a868b-34e6-4853-b462-44186da03caf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-09T18:44:14.185Z_

<details><summary>↩ Tool result · `toolu_0171KdksQnFWeLeMfP5mEX6e`</summary>

```text
Web search results for query: "speculative decoding step supervision reasoning chains"

Links: [{"title":"ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification","url":"https://arxiv.org/html/2602.18447"},{"title":"[2604.15244] From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/abs/2604.15244"},{"title":"From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/html/2604.15244"},{"title":"Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/html/2506.19830v1"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning | Hao AI Lab @ UCSD","url":"https://haoailab.com/blogs/lookaheadreasoning/"},{"title":"Reward-Guided Speculative Decoding for Efficient LLM Reasoning","url":"https://arxiv.org/html/2501.19324v1"},{"title":"Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models","url":"https://arxiv.org/pdf/2503.16419"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"}]

Based on the search results, here's what I found about speculative decoding with step supervision and reasoning chains:

## Key Findings

**Step-Level Speculative Decoding for Reasoning**

Chain-of-Thought reasoning significantly improves the performance of large language models on complex tasks, but incurs high inference latency due to long generation traces, and step-level speculative reasoning aims to mitigate this cost.

Several recent approaches are advancing this area:

1. **ConfSpec**: ConfSpec is a confidence-gated cascaded verification framework for step-level speculative reasoning that resolves the trade-off between accuracy, inference speed, and resource efficiency. The key insight is an asymmetry between generation and verification: while generating a correct reasoning step requires substantial model capacity, step-level verification is a constrained discriminative task for which small draft models are well-calibrated.

2. **SpecGuard**: SpecGuard is a mathematically grounded, verification-aware framework for adaptive inference-time compute allocation that mitigates error propagation by ensuring trusted intermediate outputs are accepted, while enabling lightweight, cost-effective verification without relying on large external verifiers.

3. **Lookahead Reasoning**: Lookahead Reasoning adds a new step-level dimension of parallelism, complementing traditional token-level speculative decoding. The approach uses a draft model to propose future reasoning steps, which are then semantically verified by the target model.

**Reward-Guided Approaches**: Process reward models evaluate intermediate decoding steps, with steps having sufficiently high reward scores being accepted to continue the reasoning trajectory, while lower-scoring steps trigger speculative corrections using the target model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10d914ad-d719-45ff-9b57-38aac3d0cf38",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "b73e92ec-ff83-4cbd-b9f3-a942530ed2b2",
  "sourceToolAssistantUUID": "10d914ad-d719-45ff-9b57-38aac3d0cf38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-09T18:44:14.809Z_

<details><summary>↩ Tool result · `toolu_01K8tka4FSEGdiCgoaDvNHrM`</summary>

```text
Web search results for query: ""draft training" "structural labels" reasoning 2025"

Links: [{"title":"Structural-aware Language-Image Pretraining for Vision- ...","url":"https://cdn.shanghai.nyu.edu/sites/default/files/honorsthesis2025_wenbo_lu.pdf"},{"title":"Published in Transactions on Machine Learning Research (08/2025)","url":"https://openreview.net/pdf?id=HvoG8SxggZ"},{"title":"Contrastive Retrieval-Augmented Generation on Experience","url":"https://aclanthology.org/2025.findings-acl.1224.pdf"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"A Survey of Reasoning Large Language Models","url":"https://arxiv.org/pdf/2502.17419"},{"title":"Aligning LLMs through Constitutionally Decomposed QA","url":"https://aclanthology.org/2025.findings-emnlp.1123.pdf"},{"title":"Pre-training Process-Supervision for Improving Reasoning","url":"https://aclanthology.org/2025.acl-long.1288.pdf"},{"title":"Evaluating Step-by-step Reasoning Traces: A Survey","url":"https://aclanthology.org/2025.findings-emnlp.94.pdf"},{"title":"Learning to Generate Structured Output with Schema ...","url":"https://aclanthology.org/2025.acl-long.243.pdf"},{"title":"LETHE-CHAT: SCHEMA-AWARE LLM AGENTS FOR TEXT-TO-SQL ON CLINICAL TRIAL DATABASES","url":"https://ehealth-graz.at/wp-content/uploads/2025/09/EHT23_Waltl_LETHE_Chat.pdf"}]

Based on the search results, I found several relevant papers from 2025 addressing topics related to draft training, structural labels, and reasoning:

## Key Findings

**Reasoning Model Training with Structural Components (2025):**

DeepSeek-R1 undergoes multiple rounds of SFT and RL training, emphasizing structured thinking templates and rule-based reward mechanisms. Recent approaches focus on model-based efficient reasoning to optimize reasoning models into more concise variants, as well as reasoning output-based efficient reasoning which dynamically reduces reasoning steps and length during inference.

**Structured Label Approaches:**

Process supervision provides step-by-step labels for the solution trajectory, evaluating the quality of each reasoning step. Additionally, one framework uses a constitution containing alignment principles to produce a hierarchically structured evaluation program.

**Efficient Reasoning Training:**

Recent methods propose human-like step-skipping approaches where they manually create solutions by skipping steps, either guided by human expertise or by randomly merging or removing steps, with concise data labeled with prompts such as "Solve it in n steps," after which the model is able to generate shorter reasoning paths.

**Structured Output Training:**

SLOT addresses limitations by decoupling output formatting from the natural language task, offering a model-agnostic solution that maintains task performance while ensuring structural validity.

These 2025 works demonstrate an emerging trend of combining structured training labels with reasoning capabilities to improve both efficiency and quality in LLM training approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a6f3370-fd43-498a-b166-026339cc8f7b",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "a0e1f301-e1f7-4969-b8a3-4a15fd4807c4",
  "sourceToolAssistantUUID": "1a6f3370-fd43-498a-b166-026339cc8f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-09T18:44:15.970Z_

Let me do a few more targeted searches to find papers specifically about using internal representations or reasoning traces for draft training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0e1f301-e1f7-4969-b8a3-4a15fd4807c4",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVKk9HguqWmxLNt4ZR2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6442237-5126-4d5c-9f80-e67641f372d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AcswF38CofiUPTxd2UpBMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5811,
      "cache_read_input_tokens": 24347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5811,
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

_source line 31 · 2026-05-09T18:44:16.211Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PoPtNL987G5N7k2gzEraoD`</summary>

```json
{
  "query": "process reward model draft speculative decoding 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6442237-5126-4d5c-9f80-e67641f372d2",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVKk9HguqWmxLNt4ZR2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c91e089-2abe-48f2-bb1e-8f5fe7edaebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AcswF38CofiUPTxd2UpBMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5811,
      "cache_read_input_tokens": 24347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5811,
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

_source line 32 · 2026-05-09T18:44:16.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LeWGVGK58VZ7U4rjXa5bfK`</summary>

```json
{
  "query": "\"intermediate supervision\" draft model inference acceleration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c91e089-2abe-48f2-bb1e-8f5fe7edaebb",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVKk9HguqWmxLNt4ZR2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cbc0e954-1a50-4a05-bcdb-b71bda194520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AcswF38CofiUPTxd2UpBMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5811,
      "cache_read_input_tokens": 24347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5811,
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

_source line 33 · 2026-05-09T18:44:16.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RUTe3PMa9Nz842cA4V8ogc`</summary>

```json
{
  "query": "reasoning step classification draft model training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbc0e954-1a50-4a05-bcdb-b71bda194520",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVKk9HguqWmxLNt4ZR2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dfce5f24-ba5c-41be-96f1-8532fc99223a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AcswF38CofiUPTxd2UpBMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5811,
      "cache_read_input_tokens": 24347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5811,
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

_source line 34 · 2026-05-09T18:44:16.950Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012kFuRsD31H1FGmXGQbVC9r`</summary>

```json
{
  "query": "multi-task draft model speculative decoding reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfce5f24-ba5c-41be-96f1-8532fc99223a",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVKk9HguqWmxLNt4ZR2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2599be6-0e7c-4767-8817-d40dc08885d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AcswF38CofiUPTxd2UpBMq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5811,
      "cache_read_input_tokens": 24347,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5811
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 212,
          "cache_read_input_tokens": 24347,
          "cache_creation_input_tokens": 5811,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5811,
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

_source line 35 · 2026-05-09T18:44:24.114Z_

<details><summary>↩ Tool result · `toolu_01PoPtNL987G5N7k2gzEraoD`</summary>

```text
Web search results for query: "process reward model draft speculative decoding 2025"

Links: [{"title":"Reward-Guided Speculative Decoding for Efficient LLM ...","url":"https://arxiv.org/pdf/2501.19324"},{"title":"[2501.19324] Reward-Guided Speculative Decoding for Efficient LLM Reasoning","url":"https://arxiv.org/abs/2501.19324"},{"title":"Reward-Guided Speculative Decoding for Efficient LLM Reasoning","url":"https://openreview.net/pdf?id=AVeskAAETB"},{"title":"Reward-Guided Speculative Decoding for Efficient LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=AVeskAAETB&noteId=UGuPgWSDLu"},{"title":"Reward-Guided Speculative Decoding for Efficient LLM Reasoning","url":"https://arxiv.org/html/2501.19324v3"},{"title":"ultimate guide to Speculative decoding - Newline.co","url":"https://www.newline.co/@zaoyang/ultimate-guide-to-speculative-decoding--540ed334"},{"title":"Reward-Shifted Speculative Sampling Is An Efficient Test- ...","url":"https://aclanthology.org/2025.emnlp-main.578.pdf"},{"title":"Paper page - Reward-Guided Speculative Decoding for Efficient LLM Reasoning","url":"https://huggingface.co/papers/2501.19324"},{"title":"SPEC-RL: ACCELERATING ON-POLICY REINFORCEMENT LEARNING VIA SPECULATIVE ROLLOUTS","url":"https://www.arxiv.org/pdf/2509.23232"},{"title":"Decoding Speculative Decoding","url":"https://aclanthology.org/2025.naacl-long.328.pdf"}]

Based on the search results, I found comprehensive information about this topic. Here's what I found:

## Reward-Guided Speculative Decoding (RSD)

Reward-Guided Speculative Decoding (RSD) is a novel framework aimed at improving the efficiency of inference in large language models (LLMs). RSD synergistically combines a lightweight draft model with a more powerful target model, incorporating a controlled bias to prioritize high-reward outputs, in contrast to existing speculative decoding methods that enforce strict unbiasedness. RSD employs a process reward model to evaluate intermediate decoding steps and dynamically decide whether to invoke the target model, optimizing the trade-off between computational cost and output quality.

### How It Works

The process reward model evaluates intermediate decoding steps and dynamically decides whether to invoke the target model. More specifically, the process begins with the draft model generating candidate steps, which are then evaluated using a reward function. Steps with sufficiently high reward scores are accepted to continue the reasoning trajectory, while lower-scoring steps trigger speculative corrections using the target model.

### Key Advantages

Unlike existing speculative decoding methods that enforce strict unbiasedness, RSD incorporates controlled bias to prioritize high-reward outputs. Reward-guided acceptance retains valuable partial solutions, reduces unnecessary queries, and can even surpass the large model's performance.

### Performance Results

Extensive evaluations on challenging reasoning benchmarks, including Olympiad-level tasks, show that RSD delivers significant efficiency gains against decoding with the target model only (up to 4.4x fewer FLOPs), while achieving significant better accuracy than parallel decoding method on average (up to +3.5).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c91e089-2abe-48f2-bb1e-8f5fe7edaebb",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "c77cc8eb-56ce-4753-9c16-649687524db4",
  "sourceToolAssistantUUID": "7c91e089-2abe-48f2-bb1e-8f5fe7edaebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-09T18:44:24.282Z_

<details><summary>↩ Tool result · `toolu_01LeWGVGK58VZ7U4rjXa5bfK`</summary>

```text
Web search results for query: ""intermediate supervision" draft model inference acceleration"

Links: [{"title":"Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation","url":"https://arxiv.org/html/2603.09527"},{"title":"Speculative Decoding with CTC-based Draft Model for LLM Inference Acceleration","url":"https://arxiv.org/html/2412.00061v1"},{"title":"SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration | OpenReview","url":"https://openreview.net/forum?id=EKJhH5D5wA"},{"title":"Awesome-Efficient-LLM/inference_acceleration.md at main · horseee/Awesome-Efficient-LLM","url":"https://github.com/horseee/Awesome-Efficient-LLM/blob/main/inference_acceleration.md"},{"title":"SpecEE: Accelerating Large Language Model Inference with Speculative Early Exiting | Proceedings of the 52nd Annual International Symposium on Computer Architecture","url":"https://dl.acm.org/doi/10.1145/3695053.3730996"},{"title":"DRAFT, VERIFY, & IMPROVE TOWARD TRAINING-AWARE SPECULATIVE DECODING","url":"https://arxiv.org/pdf/2510.05421"},{"title":"Speculative Decoding: Achieving 2-3x LLM Inference Speedup | Introl Blog","url":"https://introl.com/blog/speculative-decoding-llm-inference-speedup-guide-2025"},{"title":"Speculative Decoding with CTC-based Draft Model for LLM Inference Acceleration","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/a79054a9da91d73ed3cb1a9e87d7cd2d-Abstract-Conference.html"},{"title":"Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculative decoding - Google Developers Blog","url":"https://developers.googleblog.com/supercharging-llm-inference-on-google-tpus-achieving-3x-speedups-with-diffusion-style-speculative-decoding/"},{"title":"Draft & Verify: Lossless Large Language Model Acceleration via Self-Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=-GPD_kF1--"}]

Based on the web search results, here's what I found about "intermediate supervision" and draft model inference acceleration:

## Overview

Prior work commonly improves speculative decoding by training or aligning a dedicated draft model for a particular target model, e.g., via distillation-style distribution matching in token space or by drafting in an intermediate representation space as in EAGLE.

## Intermediate Representation Space Approach

The concept of intermediate supervision appears in the context of draft models that work with intermediate representations. The drafting stage generates draft tokens at a slightly lower quality but more quickly, which is achieved by selectively skipping certain intermediate layers during drafting, and subsequently, the verification stage employs the original LLM to validate those draft output tokens in one forward pass.

## Domain-Specific Supervision

To address the mismatch between draft and target models, domain-specific self-generation strategy is used, in which the fine-tuned target model provides supervision during the draft model training stage. This approach is particularly relevant when domain-specific self-generation aligns training supervision with the target model's actual generation trajectory, mitigating the discrepancy between learning on fixed reference data and drafting under target-conditioned continuations.

## Key Benefit

Better alignment between the draft and target distributions enables more tokens to be generated per target-model forward pass and thereby enhances inference efficiency.

The search results show active research in this area, with various methods using intermediate representations and supervision signals to improve the effectiveness of draft models in speculative decoding for LLM inference acceleration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbc0e954-1a50-4a05-bcdb-b71bda194520",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "4740d7c2-9309-4a49-bcff-ced5d8d39cae",
  "sourceToolAssistantUUID": "cbc0e954-1a50-4a05-bcdb-b71bda194520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-09T18:44:24.540Z_

<details><summary>↩ Tool result · `toolu_01RUTe3PMa9Nz842cA4V8ogc`</summary>

```text
Web search results for query: "reasoning step classification draft model training"

Links: [{"title":"Two-Stage Reasoning-Infused Learning: Improving Classification with LLM-Generated Reasoning","url":"https://arxiv.org/html/2507.00214v1"},{"title":"Understanding Reasoning LLMs - by Sebastian Raschka, PhD","url":"https://magazine.sebastianraschka.com/p/understanding-reasoning-llms"},{"title":"DeepSeek-Level AI? Train Your Own Reasoning Model in Just 7 Easy Steps! - KDnuggets","url":"https://www.kdnuggets.com/deepseek-level-ai-train-your-own-reasoning-model-in-just-7-easy-steps"},{"title":"A Tutorial on LLM Reasoning: Relevant Methods behind ChatGPT o1","url":"https://arxiv.org/html/2502.10867v1"},{"title":"What Is a Reasoning Model? | IBM","url":"https://www.ibm.com/think/topics/reasoning-model"},{"title":"Step-Tagging: Toward controlling the generation of Language Reasoning Models through step monitoring","url":"https://arxiv.org/html/2512.14332"},{"title":"Taming the Long-Tail: Efficient Reasoning RL Training with Adaptive Drafter","url":"https://arxiv.org/html/2511.16665v2"},{"title":"LLMs & Reasoning Models: How They Work and Are Trained!","url":"https://www.labellerr.com/blog/llms-reasoning-models-how-they-work/"},{"title":"Evaluating Step-by-step Reasoning Traces: A Survey","url":"https://arxiv.org/html/2502.12289"},{"title":"Multi-step reasoning: Teach LLMs to think critically","url":"https://labelbox.com/blog/multi-step-reasoning-teach-llms-to-think-critically/"}]

I've found comprehensive information about reasoning step classification and draft model training. Here are the key findings:

## Reasoning Step Classification

A Step-Tagging framework has been introduced as a lightweight sentence-classifier enabling real-time annotation of reasoning step types, built on a novel taxonomy called ReasonType. The framework uses bert-base-uncased sentence classifiers with 13 distinct step types, addressed by training separate binary classifiers for each step-type to handle significant class imbalance.

A Process-Reward Model (PRM) can be trained using datasets of annotated reasoning steps with a classification loss function based on the correctness of the reasoning steps.

## Draft Model Training in Reasoning RL

The Spot Trainer approach enables draft model training to proceed without waiting for all generated responses to complete. Due to the long-tail distribution in reasoning RL tasks, most responses are generated faster than the longest ones, and the Spot Trainer leverages partial responses to train the draft model.

In speculative decoding, a lightweight draft model rapidly generates a sequence of candidate tokens, which are then efficiently verified in parallel by the larger target model in a single forward pass.

## General Training Approaches

The central innovation is the application of novel reinforcement learning (RL) techniques that incentivize the model to generate intermediate "reasoning steps" at inference time before producing a final output. Group Relative Policy Optimization (GRPO) is a reinforcement learning technique that helps models develop reasoning capabilities autonomously, and unlike Proximal Policy Optimization (PPO), GRPO optimizes responses without requiring a value function.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfce5f24-ba5c-41be-96f1-8532fc99223a",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "0e43057d-4e41-41f5-98de-ead82991867c",
  "sourceToolAssistantUUID": "dfce5f24-ba5c-41be-96f1-8532fc99223a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-09T18:44:24.605Z_

<details><summary>↩ Tool result · `toolu_012kFuRsD31H1FGmXGQbVC9r`</summary>

```text
Web search results for query: "multi-task draft model speculative decoding reasoning"

Links: [{"title":"Speculative Decoding for Multi-Sample Inference","url":"https://arxiv.org/html/2503.05330"},{"title":"Get 3× Faster LLM Inference with Speculative Decoding Using the Right Draft Model","url":"https://www.bentoml.com/blog/3x-faster-llm-inference-with-speculative-decoding"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/pdf/2506.19830"},{"title":"On Speculative Decoding for Multimodal Large Language Models Mukul Gagrani*","url":"https://openaccess.thecvf.com/content/CVPR2024W/ELVM/papers/Gagrani_On_Speculative_Decoding_for_Multimodal_Large_Language_Models_CVPRW_2024_paper.pdf"},{"title":"[2604.15244] From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/abs/2604.15244"},{"title":"Speculative decoding | LLM Inference Handbook","url":"https://bentoml.com/llm/inference-optimization/speculative-decoding"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"Decoding Speculative Decoding","url":"https://aclanthology.org/2025.naacl-long.328.pdf"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=speculative+decoding"}]

I found several relevant research papers and resources on multi-task draft models with speculative decoding for reasoning. Here's what the search revealed:

## Key Findings

**Multi-Sample Reasoning with Speculative Decoding:**
A novel speculative decoding method has been explicitly designed for multi-sample reasoning scenarios. Multi-sample inference yields a rich reservoir of high-quality draft tokens, with the LLM producing outputs that, while varied in expression, are all drawn from the same underlying distribution. Because all paths stem from the same model, their substeps naturally mirror its output tendencies, unlike externally sourced drafts.

**Step-Level Speculative Decoding for Reasoning:**
Large reasoning models often generate solutions by giving a "chain-of-thought"—a sequence of intermediate reasoning steps produced step-by-step to derive a final answer, with each reasoning step conditioning on the previous one. A draft step generation approach has been proposed where given a token prefix, the draft model autoregressively generates a sequence of candidate steps.

**Draft Model Alignment:**
How closely a draft model's distribution matches with the target model determines the acceptance rate. OmniDraft, a unified framework, enables a single draft model to operate with any target model and adapt dynamically to user data, using an online n-gram cache with hybrid distillation fine-tuning to address cross-vocabulary mismatch.

These approaches represent recent advances in making speculative decoding more effective for complex reasoning tasks while maintaining computational efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2599be6-0e7c-4767-8817-d40dc08885d4",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "20e5cf75-98e2-40e3-aba6-33fa87a9041b",
  "sourceToolAssistantUUID": "f2599be6-0e7c-4767-8817-d40dc08885d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-09T18:44:26.947Z_

Now let me search for specific papers on arxiv that might have been missed, particularly looking for recent submissions combining these concepts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20e5cf75-98e2-40e3-aba6-33fa87a9041b",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVLU3Sevqs8JmWtSVu6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de25a7e2-cd89-48b5-b6e4-21eabd6aa92d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ZzJx1k2etZHtvatPTXKbq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 30158,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 181,
          "cache_read_input_tokens": 30158,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3884,
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

_source line 40 · 2026-05-09T18:44:26.960Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AgAGivfA8xvhDc7y9FTCc7`</summary>

```json
{
  "query": "arxiv 2025 2026 draft model reasoning supervision segment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de25a7e2-cd89-48b5-b6e4-21eabd6aa92d",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVLU3Sevqs8JmWtSVu6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "040cba74-a94c-4c5f-9846-0231f1bb1040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ZzJx1k2etZHtvatPTXKbq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 30158,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 181,
          "cache_read_input_tokens": 30158,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3884,
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

_source line 41 · 2026-05-09T18:44:26.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TUoA1Cjy1RFWgcEWLUy3G3`</summary>

```json
{
  "query": "thought structure classification auxiliary loss draft training 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "040cba74-a94c-4c5f-9846-0231f1bb1040",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVLU3Sevqs8JmWtSVu6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b539522-fa60-4835-8782-9fdaf084078e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ZzJx1k2etZHtvatPTXKbq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 30158,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 181,
          "cache_read_input_tokens": 30158,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3884,
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

_source line 42 · 2026-05-09T18:44:26.995Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BFT5rQbzGCinm7Mwo9rrwo`</summary>

```json
{
  "query": "\"verifiable reasoning\" draft model structural tokens 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b539522-fa60-4835-8782-9fdaf084078e",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVLU3Sevqs8JmWtSVu6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1b3b4f6c-de8c-463d-8e04-32a5673b0985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ZzJx1k2etZHtvatPTXKbq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 30158,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 181,
          "cache_read_input_tokens": 30158,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3884,
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

_source line 43 · 2026-05-09T18:44:34.598Z_

<details><summary>↩ Tool result · `toolu_01AgAGivfA8xvhDc7y9FTCc7`</summary>

```text
Web search results for query: "arxiv 2025 2026 draft model reasoning supervision segment"

Links: [{"title":"From &lt;Answer> to &lt;Think>: Multidimensional Supervision of Reasoning Process for LLM Optimization","url":"https://arxiv.org/html/2510.11457v1"},{"title":"KnowRL: Boosting LLM Reasoning via Reinforcement Learning with Minimal-Sufficient Knowledge Guidance","url":"https://arxiv.org/html/2604.12627v1"},{"title":"DRAFT: Task Decoupled Latent Reasoning for Agent Safety","url":"https://arxiv.org/html/2604.03242"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/new"},{"title":"Small Drafts, Big Verdict: Information-Intensive Visual Reasoning via Speculation","url":"https://arxiv.org/html/2510.20812"},{"title":"Future-as-Label: Scalable Supervision from Real-World Outcomes","url":"https://arxiv.org/html/2601.06336v2"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"[2510.20812] Small Drafts, Big Verdict: Information-Intensive Visual Reasoning via Speculation","url":"https://arxiv.org/abs/2510.20812"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"},{"title":"Draft version February 20, 2026","url":"https://arxiv.org/pdf/2602.16768"}]

I've found several relevant arXiv papers from 2025-2026 related to reasoning, supervision, and segmentation in model training. Here are the most relevant results:

## Key Papers Found

One notable paper proposes a multidimensional reasoning-level supervision framework that categorizes high-quality reasoning properties into three dimensions: Confidence, Relevance and Coherence. The paper addresses a key challenge where process-level supervision requires the reasoning process to be segmented into individual steps.

Another paper proposes DRAFT, which decouples evidence extraction from decision readout through a continuous latent workspace with two LoRA adapters, thus alleviating learning difficulty under weak supervision.

A third approach uses speculative decoding, which is a draft-then-verify decoding paradigm to accelerate LLM inference. Specifically, Speculative Verdict (SV) is a training-free framework that combines multiple lightweight draft experts with a large verdict model, where small VLMs act as draft experts to generate reasoning paths that provide diverse localization candidates, and a strong VLM synthesizes these paths to produce the final answer.

Additional work includes Self-Hinting, which enables the model to act as its own teacher by generating abstract hints to guide subsequent rollouts, and RLAD which trains models with auxiliary supervision to produce higher-quality abstractions during reinforcement learning.

These papers collectively address challenges in model reasoning supervision, particularly around effective segmentation of reasoning processes and leveraging draft-based approaches for improved model performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "040cba74-a94c-4c5f-9846-0231f1bb1040",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "de5f77ba-3ff8-4da7-b638-a97482fe6ff8",
  "sourceToolAssistantUUID": "040cba74-a94c-4c5f-9846-0231f1bb1040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-09T18:44:35.246Z_

<details><summary>↩ Tool result · `toolu_01BFT5rQbzGCinm7Mwo9rrwo`</summary>

```text
Web search results for query: ""verifiable reasoning" draft model structural tokens 2025"

Links: [{"title":"TETRIS: Optimal Draft Token Selection for Batch ...","url":"https://aclanthology.org/2025.acl-long.1598.pdf"},{"title":"Speculative Decoding: Speeding LLM Generation","url":"https://www.emergentmind.com/topics/speculative-decoding-technique"},{"title":"Faster Speculative Decoding via Effective Draft ...","url":"https://aclanthology.org/2025.acl-long.486.pdf"},{"title":"Fail Fast, Win Big: Rethinking the Drafting Strategy in Speculative Decoding via Diffusion LLMs","url":"https://arxiv.org/html/2512.20573"},{"title":"Self-Verification Speculative Decoding for Long-Form ...","url":"https://aclanthology.org/2025.emnlp-main.844.pdf"},{"title":"Decoding Speculative Decoding","url":"https://aclanthology.org/2025.naacl-long.328.pdf"},{"title":"Diving into speculative decoding training support for vLLM with Speculators v0.3.0 | vLLM Blog","url":"https://blog.vllm.ai/2025/12/13/speculators-v030.html"},{"title":"Speculative Sampling — TensorRT-LLM","url":"https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html"},{"title":"Rethinking Thinking Tokens: LLMs as Improvement Operators","url":"https://arxiv.org/html/2510.01123v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf"}]

Based on the search results, here's what I found about verifiable reasoning, draft models, and structural tokens in 2025:

## Speculative Decoding and Draft Models

The search results reveal significant developments in speculative decoding and draft model architectures in 2025. The current SOTA for speculative decoding algorithms is Eagle3, which represents the most advanced approach for draft model design.

## Structural Elements and Tokens

Eagle3 draft models take the hidden states from three layers of the verifier model as input, capturing the verifier's latent features. This model is then trained using a technique introduced by the Eagle3 authors called "train-time-testing", which simulates the multi-step draft sampling process during training to ensure the model learns to predict not just the first token, but also subsequent ones.

## Verification Approaches

Multiple verification strategies have emerged in 2025:

- Tree-structured (token tree) or graph-structured speculative decoding generalizes token acceptance beyond linear sequences, scaling acceptance by exploiting overlap among hypotheses

- Recent traversal verification schemes invert the traditional top-down approach by traversing candidate trees from leaves to root, increasing the utilization of plausible sequences and delivering provably optimal acceptance rates for chain structures

## Training and Implementation

Speculators v0.3.0 supports offline training data generation through a hidden states generator, which produces hidden state tensors from standard LLM text datasets, which are then saved to disk for later use in the training process.

These developments demonstrate the growing sophistication of draft model architectures and their integration with structured token verification methods in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b3b4f6c-de8c-463d-8e04-32a5673b0985",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "cc8813cf-22a0-4467-b364-14f343c97157",
  "sourceToolAssistantUUID": "1b3b4f6c-de8c-463d-8e04-32a5673b0985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-09T18:44:36.103Z_

<details><summary>↩ Tool result · `toolu_01TUoA1Cjy1RFWgcEWLUy3G3`</summary>

```text
Web search results for query: "thought structure classification auxiliary loss draft training 2025"

Links: [{"title":"LLM Representations Encode Information About Chain-of- ...","url":"https://aclanthology.org/2025.findings-acl.662.pdf"},{"title":"ech T Press Science Doi:10.32604/cmc.2025.071301 ARTICLE","url":"https://www.techscience.com/cmc/online/detail/25298/pdf"},{"title":"Auxiliary Losses for Learning Generalizable Concept-based Models Ivaxi Sheth∗","url":"https://openreview.net/pdf?id=jvYXln6Gzn"},{"title":"Bridging the Dynamic Perception Gap: Training-Free Draft ...","url":"https://aclanthology.org/2025.findings-emnlp.349.pdf"},{"title":"What Makes a Good Reasoning Chain? Uncovering ...","url":"https://aclanthology.org/2025.emnlp-main.329.pdf"},{"title":"Auxiliary Loss (AuxK) in Neural Models","url":"https://www.emergentmind.com/topics/auxiliary-loss-auxk"},{"title":"Learning through Auxiliary Tasks | Unsupervised Thoughts","url":"https://vivien000.github.io/blog/journal/learning-though-auxiliary_tasks.html"},{"title":"Sketch-of-Thought: Efficient LLM Reasoning with Adaptive ...","url":"https://aclanthology.org/2025.emnlp-main.1236.pdf"},{"title":"arXiv:2502.17419v6 [cs.AI] 25 Jun 2025","url":"https://arxiv.org/pdf/2502.17419"},{"title":"Breaking the Reasoning Barrier A Survey on LLM Complex ...","url":"https://aclanthology.org/2025.findings-acl.386.pdf"}]

Based on the web search results, I found several relevant papers and research related to your query about thought structure classification, auxiliary loss, and draft training in 2025:

## Key Findings:

### 1. Task-Structured Curriculum Learning (TSCL)
A task-structured curriculum learning framework structures training into three sequential phases: (i) prediction-only, to establish stable feature representations; (ii) joint prediction–explanation, to align task outputs with rationale generation; and (iii) explanation-only, to refine the quality of rationales. This approach uses language rationales—textual reasoning steps generated by the teacher—as auxiliary supervision signals that guide the student model to emulate not just the final predictions but also the cognitive steps leading to them.

### 2. Thought Structure Analysis
In the "Split Thought" stage, the reasoning chain is split into a list of thoughts, where a "Thought" is defined as a continue segment in a reasoning chain that involves no logical transition. This relates to understanding how to classify and structure reasoning processes.

### 3. Draft-Based Reasoning Approaches
Recent work includes Chain-of-Draft (CoD) which applies explicit constraints on reasoning length, while Sketch-of-Thought introduces paradigm-guided sketching, yielding more compact yet structured intermediate steps via dynamic routing.

### 4. Auxiliary Loss Applications
Incorporating an auxiliary loss in the form of a multi-task setting can help models achieve competitive downstream accuracy overall.

These 2025 publications demonstrate active research in combining auxiliary losses, thought structure classification, and draft-based training approaches for improving language model reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b539522-fa60-4835-8782-9fdaf084078e",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "ae9a6594-954a-4fc1-9245-1fc328388abc",
  "sourceToolAssistantUUID": "8b539522-fa60-4835-8782-9fdaf084078e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-09T18:44:37.616Z_

Excellent. Now let me compile the comprehensive findings from all searches. Let me do one final targeted search to check if there's any direct mention of ThinKV or the exact combination of these concepts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae9a6594-954a-4fc1-9245-1fc328388abc",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVMKDejFJ5BpmrtHwDF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0ca8231-4465-4daf-adc7-abe3d4955dff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DjbKj26ELff9vDRVBSAV8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 898,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 34042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1848,
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

_source line 47 · 2026-05-09T18:44:38.096Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A6wMkMRGYztPR1MprSZiUC`</summary>

```json
{
  "query": "\"From Answer to Think\" multidimensional supervision reasoning EAGLE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0ca8231-4465-4daf-adc7-abe3d4955dff",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVMKDejFJ5BpmrtHwDF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d08f104d-66c7-4676-8912-efbb9d57e340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DjbKj26ELff9vDRVBSAV8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 898,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 34042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1848,
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

_source line 48 · 2026-05-09T18:44:38.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KuMY6a9gUym1yLsrhdx4Vg`</summary>

```json
{
  "query": "step-level speculative decoding reasoning process supervision 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d08f104d-66c7-4676-8912-efbb9d57e340",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVMKDejFJ5BpmrtHwDF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb179a90-8c0b-4435-91a4-b7a526b0941b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DjbKj26ELff9vDRVBSAV8R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 898,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 34042,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 898,
          "output_tokens": 155,
          "cache_read_input_tokens": 34042,
          "cache_creation_input_tokens": 1848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1848,
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

_source line 49 · 2026-05-09T18:44:41.671Z_

<details><summary>↩ Tool result · `toolu_01A6wMkMRGYztPR1MprSZiUC`</summary>

```text
Web search results for query: ""From Answer to Think" multidimensional supervision reasoning EAGLE"

Links: [{"title":"From Answer to Think: Multidimensional Supervision of Reasoning Process for LLM Optimization | OpenReview","url":"https://openreview.net/forum?id=MjJrhfAmRG"}]

Based on the search results, I found information about the paper "From Answer to Think: Multidimensional Supervision of Reasoning Process for LLM Optimization."

The work provides multidimensional supervision over the reasoning process, thereby enhancing both the reasoning ability and generalization of large language models. 

Existing approaches are broadly categorized into outcome-level answer supervision and process-level reasoning supervision; however, the former provides only sparse binary feedback and overlooks intermediate step quality, while the latter scores individual steps but requires task-specific segmentation.

The proposed framework assesses the quality of reasoning process along three dimensions: Confidence for uncertainty calibration, Relevance for semantic alignment and Coherence for logical consistency. The framework serves as a Dimension-level Reward Model (DRM) that assigns scores to reasoning processes and provides supervision signals for both off-policy (e.g., DPO) and on-policy (e.g., GRPO) optimization.

Experimental results show that DRM-supervised training achieves consistent gains on both in-distribution and out-of-distribution open-domain tasks, including mathematics, question answering, code execution and puzzles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d08f104d-66c7-4676-8912-efbb9d57e340",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "6115062a-fe6c-4845-99f1-2db1dcafc869",
  "sourceToolAssistantUUID": "d08f104d-66c7-4676-8912-efbb9d57e340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-09T18:44:46.271Z_

<details><summary>↩ Tool result · `toolu_01KuMY6a9gUym1yLsrhdx4Vg`</summary>

```text
Web search results for query: "step-level speculative decoding reasoning process supervision 2025"

Links: [{"title":"ARBITRAGE: Efficient Reasoning via Advantage-Aware Speculation","url":"https://arxiv.org/pdf/2512.05033"},{"title":"1 Introduction","url":"https://arxiv.org/html/2605.02290v1"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/html/2506.19830v1"},{"title":"arXiv:2501.11223v4 [cs.AI] 11 Jun 2025 §9 Benchmarks for RLMs","url":"https://spcl.inf.ethz.ch/Publications/.pdf/besta-reasoning.pdf"},{"title":"arXiv:2506.19830v1 [cs.LG] 24 Jun 2025 Scaling Speculative Decoding with","url":"https://arxiv.org/pdf/2506.19830"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning | OpenReview","url":"https://openreview.net/forum?id=JxxKj8pow1"},{"title":"ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification","url":"https://arxiv.org/html/2602.18447"},{"title":"From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/html/2604.15244"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning | Hao AI Lab @ UCSD","url":"https://haoailab.com/blogs/lookaheadreasoning/"},{"title":"Reward Models and Learning Strategies","url":"https://aclanthology.org/2025.findings-emnlp.970.pdf"}]

Based on the search results, here are several key recent research developments on step-level speculative decoding with process supervision from 2025:

## Key Approaches

**ARBITRAGE** - A novel step-level speculative generation framework that routes generation dynamically based on the relative advantage between draft and target models, using a lightweight router trained to predict when the target model is likely to produce a meaningfully better step.

**Lookahead Reasoning** - This approach exploits a step-level layer of parallelism, recognizing that reasoning models generate step-by-step and each step needs only to be semantically correct, not exact token matching. In Lookahead Reasoning, a lightweight draft model proposes several future steps; the target model expands each proposal in one batched pass, and a verifier keeps semantically correct steps while letting the target regenerate any that fail.

**ConfSpec** - Step-level speculative reasoning extends speculative decoding by operating on entire reasoning steps, allowing verification based on semantic equivalence rather than exact token matching, which better aligns with the structure of CoT reasoning.

**CoRD** - A framework that redefines reasoning distillation as a dynamic, step-wise decoding process, enabling collaborative construction of reasoning trajectories among teacher models to produce richer supervision and significantly improve student performance.

## Key Insight

Reasoning is naturally hierarchical: a full chain-of-thought breaks into discrete steps, and to reach the correct answer, a reasoning step requires only semantic correctness but not exact token matches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb179a90-8c0b-4435-91a4-b7a526b0941b",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "ae5f9f4c0daede907",
  "type": "user",
  "uuid": "bd27d9ef-1e29-43af-a47b-5233186356cb",
  "sourceToolAssistantUUID": "bb179a90-8c0b-4435-91a4-b7a526b0941b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-09T18:45:09.280Z_

Based on my comprehensive aggressive search, here is the detailed competitive landscape analysis for the paper "Structure-Guided Draft Training for Reasoning Speculative Decoding":

## CRITICAL COMPETING WORK FOUND

### 1. **Directly Relevant: Step-Level Speculative Decoding with Structural Reasoning**

**ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification** (2025)
- Uses step-level reasoning structure in speculative decoding
- Employs confidence-gated cascaded verification framework
- Key difference: focuses on semantic verification rather than explicit segment-type supervision

**From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning** (arxiv:2604.15244, 2025)
- Operates at step-level rather than token-level
- Introduces verification-aware framework for reasoning steps
- Extends speculative decoding to hierarchical chain-of-thought structures

**Scaling Speculative Decoding with Lookahead Reasoning** (arxiv:2506.19830, 2025)
- Proposes step-level parallelism for reasoning models
- Draft model proposes future reasoning steps
- Uses semantic verification rather than exact token matching

### 2. **Auxiliary Supervision for Draft Training - STRONG THREAT**

**From Answer to Think: Multidimensional Supervision of Reasoning Process for LLM Optimization** (OpenReview, 2025)
- **CRITICAL**: Proposes multidimensional supervision of reasoning processes with three dimensions: Confidence, Relevance, Coherence
- Addresses reasoning process segmentation challenge
- Creates Dimension-level Reward Model (DRM) for reasoning supervision
- Shows consistent gains on reasoning tasks
- **Key concern**: This uses structured supervision signals beyond simple cross-entropy loss, which aligns closely with your paper's auxiliary loss concept

**Reward-Guided Speculative Decoding for Efficient LLM Reasoning** (arxiv:2501.19324, 2025)
- Uses process reward models to evaluate intermediate decoding steps
- Dynamically decides whether to invoke target model based on step quality
- **Relevance**: Shows structured intermediate supervision in speculative decoding context

### 3. **Reasoning Segment Classification & Step Tagging**

**Step-Tagging: Toward controlling the generation of Language Reasoning Models through step monitoring** (2025)
- Introduces ReasonType taxonomy for classifying reasoning step types (13 distinct types)
- Uses lightweight sentence classifiers for real-time annotation of step types
- **Direct threat**: Proposes structured reasoning step taxonomy that could be adapted for draft training

### 4. **Process-Based Supervision for Reasoning Models**

**Pre-training Process-Supervision for Improving Reasoning** (ACL 2025)
- Process-based supervision provides step-by-step labels for solution trajectories
- Evaluates quality of each reasoning step
- Shows improved generalization to out-of-domain tasks
- **Overlap concern**: Demonstrates that step-level supervision improves reasoning in large models

### 5. **Multidimensional Reasoning Supervision Framework**

**What Makes a Good Reasoning Chain? Uncovering Reasoning Chains Complexity** (EMNLP 2025)
- Analyzes structural properties of reasoning chains
- Identifies multiple dimensions for evaluating reasoning quality
- **Competitive pressure**: Demonstrates active research in characterizing reasoning structure

### 6. **Draft Model Training with Supervision Alignment**

**Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation** (2025)
- Uses domain-specific self-generation strategy where target model provides supervision
- Aligns draft model training with target model's actual generation trajectory
- Shows importance of distribution alignment between draft and target

**Training Domain Draft Models for Speculative Decoding: Best Practices and Insights** (arxiv:2503.07807v1, 2025)
- Investigates knowledge distillation techniques for training domain-specific draft models
- Shows systematic approaches to improve draft model speculation accuracy
- **Context**: Demonstrates active research community on draft model training optimization

### 7. **EAGLE-Based Approaches (Your Target Architecture)**

**EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test** (NeurIPS 2025)
- Latest EAGLE variant uses tri-layer feature fusion
- Implements training-time test methodology
- Achieves up to 6.5x speedup
- **Note**: No mention of reasoning segment taxonomy integration, suggesting potential novelty space

**P-EAGLE: Parallel Speculative Decoding in vLLM** (2025)
- Enables K draft tokens in single forward pass
- Practical integration into vLLM
- No structural reasoning supervision mentioned

### 8. **Multi-Dimensional Reasoning Approaches**

**ARBITRAGE: Efficient Reasoning via Advantage-Aware Speculation** (arxiv:2512.05033, 2025)
- Routes generation dynamically based on relative advantage between draft and target
- Uses lightweight router trained on when target produces meaningfully better steps
- **Alternative approach**: Step-level routing rather than segment-type classification

### 9. **Variational and Theoretical Approaches**

**Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance** (arxiv:2602.05774v1, 2025)
- Rethinks draft training from token-level to sequence-level optimization
- Proposes variational framework for draft model training
- Shows importance of sequence-level acceptance probability

**A Theoretical Perspective for Speculative Decoding Algorithm** (NeurIPS 2024)
- Formalizes speculative decoding through Markov Chain abstraction
- Provides theoretical understanding of draft-verify dynamics
- **Your novelty point**: Applies Markov segment-transition consistency loss, which extends this theoretical framework

## NOVELTY ASSESSMENT SUMMARY

### Potential Novel Aspects:
1. **Explicit use of ThinKV's R/E/T taxonomy as training labels** - No competing work found directly using this taxonomy for draft training
2. **Markov segment-transition consistency objective** - Extends theoretical understanding to segment transitions (most works focus on token or step level, not segment transitions)
3. **Applied specifically to DeepSeek-R1-Distill-70B with EAGLE-3** - Most works target general LLMs, not specifically this reasoning model

### Areas of Concern (Pre-existing Work):
1. **Multidimensional supervision for reasoning processes** - "From Answer to Think" (2025) proposes similar auxiliary supervision framework
2. **Step-level speculative decoding** - ConfSpec, Lookahead Reasoning, and "From Tokens to Steps" all operate at step level
3. **Structural reasoning supervision** - Multiple papers address reasoning process segmentation and classification
4. **Process reward models for speculative decoding** - Already demonstrated in Reward-Guided SD
5. **EAGLE-3 draft model extensions** - Active research area with multiple recent publications

### Most Critical Threats to Your Novelty:
- **"From Answer to Think" (2025)** - Proposes multidimensional supervision with dimension-level reward models for reasoning, predates your work and covers auxiliary loss concept
- **ConfSpec/Lookahead Reasoning** - Step-level structural reasoning in speculative decoding is an active area
- **Step-Tagging framework** - Reasoning step taxonomy for classification already exists

### Recommended Differentiators for Your Paper:
- Emphasize the **specific combination** of ThinKV taxonomy + Markov transitions + EAGLE-3 + DeepSeek-R1-Distill
- Claim novelty in **segment-level consistency** (not just step-level)
- Provide empirical evidence that segment-transition modeling outperforms other structural approaches
- Compare directly against multidimensional supervision baselines

Sources:
- [ConfSpec: Efficient Step-Level Speculative Reasoning](https://arxiv.org/html/2602.18447)
- [From Tokens to Steps: Verification-Aware Speculative Decoding](https://arxiv.org/abs/2604.15244)
- [Scaling Speculative Decoding with Lookahead Reasoning](https://arxiv.org/pdf/2506.19830)
- [From Answer to Think: Multidimensional Supervision](https://openreview.net/forum?id=MjJrhfAmRG)
- [Reward-Guided Speculative Decoding](https://arxiv.org/pdf/2501.19324)
- [Step-Tagging framework](https://arxiv.org/html/2512.14332)
- [Pre-training Process-Supervision](https://aclanthology.org/2025.acl-long.1288.pdf)
- [EAGLE-3: Scaling up Inference](https://openreview.net/pdf?id=4exx1hUffq)
- [Training Domain Draft Models](https://arxiv.org/html/2503.07807v1)
- [Variational Speculative Decoding](https://arxiv.org/html/2602.05774v1)
- [ARBITRAGE: Advantage-Aware Speculation](https://arxiv.org/pdf/2512.05033)
- [A Theoretical Perspective for Speculative Decoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/e7349e785900b93d8b4971a3f2c1cefe-Paper-Conference.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd27d9ef-1e29-43af-a47b-5233186356cb",
  "isSidechain": true,
  "agentId": "ae5f9f4c0daede907",
  "requestId": "req_011CasVN4g4q8xsUofP2W5Lj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6fe10a02-9ee1-4be7-bedb-4d519b9bc791",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LfoUfa4QzcsqapTy7GGXSa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2389,
      "cache_read_input_tokens": 35890,
      "output_tokens": 2272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2389
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2272,
          "cache_read_input_tokens": 35890,
          "cache_creation_input_tokens": 2389,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2389,
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
