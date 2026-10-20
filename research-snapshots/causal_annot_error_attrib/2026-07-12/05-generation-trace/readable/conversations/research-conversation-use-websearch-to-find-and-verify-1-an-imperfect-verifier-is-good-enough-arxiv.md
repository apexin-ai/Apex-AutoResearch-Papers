# Research conversation: Use WebSearch to find and verify: 1. "An Imperfect Verifier is Good Enough" arXiv 2604.07666 (April 2026) — this paper r

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-abf0f5ee5f5120153.jsonl`
- **Structured JSON:** [`6e7c1fec3f1f4669b57b.json`](../../sessions/6e/6e7c1fec3f1f4669b57b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-18T04:11:44.581Z_

Use WebSearch to find and verify:

1. "An Imperfect Verifier is Good Enough" arXiv 2604.07666 (April 2026) — this paper reportedly shows that RLVR training is robust to verifier noise rates up to 15%. Does it exist? What does it claim exactly? If it exists, this could undermine the urgency of breaking the "verification ceiling."

2. Search for "CURE co-evolving coder unit tester" or "CURE co-evolution code LLM" — this is reportedly a paper about co-evolving a code generator and unit test generator. Find it and describe what it does.

3. Search for "G-Zero verifier-free co-evolution" arXiv 2605.09959 — reportedly a verifier-free approach.

Report what you find for each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b590861c-9ae0-462b-9344-394cda6aa41d",
  "agentId": "abf0f5ee5f5120153",
  "type": "user",
  "uuid": "8db9c669-3836-4192-a94f-39825ac7761f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T04:11:44.587Z_

```json
{
  "parentUuid": "8db9c669-3836-4192-a94f-39825ac7761f",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
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
  "uuid": "127891a5-dc9c-4298-b9e2-32a15a79b5d2",
  "timestamp": "2026-05-18T04:11:44.587Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T04:11:47.127Z_



I'll search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "127891a5-dc9c-4298-b9e2-32a15a79b5d2",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
  "requestId": "req_011Cb9P52UFAFfHikaZzoVbC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c5e4b2f-6df1-463a-bbd6-d6bcdbc2148e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SapRD2ePFsRPpShmKbkpna",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 740,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 740,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T04:11:47.501Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GF5GXuKmpoiK7n3J1cKHSA`</summary>

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
  "parentUuid": "3c5e4b2f-6df1-463a-bbd6-d6bcdbc2148e",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
  "requestId": "req_011Cb9P52UFAFfHikaZzoVbC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01f9f373-b707-49bf-b353-6fcbda405552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SapRD2ePFsRPpShmKbkpna",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 740,
      "cache_read_input_tokens": 8223,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 740
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 740,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T04:11:47.507Z_

<details><summary>↩ Tool result · `toolu_01GF5GXuKmpoiK7n3J1cKHSA`</summary>

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
  "parentUuid": "01f9f373-b707-49bf-b353-6fcbda405552",
  "isSidechain": true,
  "promptId": "b590861c-9ae0-462b-9344-394cda6aa41d",
  "agentId": "abf0f5ee5f5120153",
  "type": "user",
  "uuid": "8f4b8567-0be3-435f-b3e1-e846267fe0b8",
  "sourceToolAssistantUUID": "01f9f373-b707-49bf-b353-6fcbda405552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T04:11:51.650Z_



Now let me search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f4b8567-0be3-435f-b3e1-e846267fe0b8",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
  "requestId": "req_011Cb9P5FFSv2xVHoEnoFuLd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16484e6e-d3f3-411e-b602-1511dce7535d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hqVNpJ4c2WnabiimMFxYG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T04:11:52.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KTJMWBBCNmGd3vMkgStXcJ`</summary>

```json
{
  "query": "arXiv 2604.07666 \"An Imperfect Verifier is Good Enough\" RLVR verifier noise 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16484e6e-d3f3-411e-b602-1511dce7535d",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
  "requestId": "req_011Cb9P5FFSv2xVHoEnoFuLd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f515e56-099d-4c7d-8ff5-8a1544ee7b14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hqVNpJ4c2WnabiimMFxYG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T04:11:53.070Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ez9jqEhdn1kLyGUbZnYxdY`</summary>

```json
{
  "query": "CURE co-evolving coder unit tester co-evolution code LLM paper 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f515e56-099d-4c7d-8ff5-8a1544ee7b14",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
  "requestId": "req_011Cb9P5FFSv2xVHoEnoFuLd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43bb1d4a-114b-4886-be86-e8a121c2b12b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hqVNpJ4c2WnabiimMFxYG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T04:11:53.190Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CDzvTrRpXocRwigmvL84Vs`</summary>

```json
{
  "query": "arXiv 2605.09959 \"G-Zero\" verifier-free co-evolution 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43bb1d4a-114b-4886-be86-e8a121c2b12b",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
  "requestId": "req_011Cb9P5FFSv2xVHoEnoFuLd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06ea96a4-f776-4488-88e5-78b1d6458bd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hqVNpJ4c2WnabiimMFxYG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8963,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 8963,
          "cache_creation_input_tokens": 1404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1404,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T04:11:58.986Z_

<details><summary>↩ Tool result · `toolu_01CDzvTrRpXocRwigmvL84Vs`</summary>

```text
Web search results for query: "arXiv 2605.09959 "G-Zero" verifier-free co-evolution 2026"

Links: [{"title":"[2605.09959v1] G-Zero: Self-Play for Open-Ended Generation from Zero Data","url":"https://arxiv.org/abs/2605.09959v1"},{"title":"G-Zero: Self-Play for Open-Ended Generation from Zero Data","url":"https://arxiv.org/html/2605.09959v1"},{"title":"RemoteZero: Geospatial Reasoning with Zero Human Annotations","url":"https://arxiv.org/html/2605.04451"},{"title":"ZeroCoder: Can LLMs Improve Code Generation Without Ground-Truth Supervision?","url":"https://arxiv.org/html/2604.07864v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=332&show=1000"},{"title":"Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning","url":"https://arxiv.org/html/2511.16043v1"},{"title":"Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data","url":"https://arxiv.org/html/2602.21320v1"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/html/2508.05004v1"},{"title":"TacoMAS: Test-Time Co-Evolution of Topology and Capability in LLM-based Multi-Agent Systems","url":"https://arxiv.org/html/2605.09539v1"},{"title":"A Survey of Zero-Knowledge Proof Based Verifiable Machine Learning","url":"https://arxiv.org/html/2502.18535v2"}]

I found the paper! Here's the information about arXiv paper 2605.09959:

**Title:** G-Zero: Self-Play for Open-Ended Generation from Zero Data

**Key Concept:** G-Zero is a verifier-free, co-evolutionary framework for autonomous self-improvement.

**Problem Addressed:** Self-evolving LLMs excel in verifiable domains but struggle in open-ended tasks, where reliance on proxy LLM judges introduces capability bottlenecks and reward hacking.

**Core Innovation:** The core innovation is Hint-δ, an intrinsic reward that quantifies the predictive shift between a Generator model's unassisted response and its response conditioned on a self-generated hint.

**How It Works:** A Proposer model is trained via GRPO to continuously target the Generator's blind spots by synthesizing challenging queries and informative hints, while the Generator is concurrently optimized via DPO to internalize these hint-guided improvements.

**Submission Date:** The paper was submitted on May 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06ea96a4-f776-4488-88e5-78b1d6458bd7",
  "isSidechain": true,
  "promptId": "b590861c-9ae0-462b-9344-394cda6aa41d",
  "agentId": "abf0f5ee5f5120153",
  "type": "user",
  "uuid": "a5679abf-42b8-4dff-9f83-f8fd948b6d69",
  "sourceToolAssistantUUID": "06ea96a4-f776-4488-88e5-78b1d6458bd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T04:11:59.769Z_

<details><summary>↩ Tool result · `toolu_01KTJMWBBCNmGd3vMkgStXcJ`</summary>

```text
Web search results for query: "arXiv 2604.07666 "An Imperfect Verifier is Good Enough" RLVR verifier noise 2026"

Links: [{"title":"[2604.07666] An Imperfect Verifier is Good Enough: Learning with Noisy Rewards","url":"https://arxiv.org/abs/2604.07666"},{"title":"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards","url":"https://arxiv.org/html/2604.07666"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/html/2510.00915v1"},{"title":"[2510.00915] Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/abs/2510.00915"},{"title":"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/html/2604.15149"},{"title":"Inference Scaling FLaws: The Limits of LLM Resampling with Imperfect Verifiers","url":"https://arxiv.org/html/2411.17501v1"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards ...","url":"https://www.arxiv.org/pdf/2510.00915"},{"title":"Rate or Fate? RLVεR: Reinforcement Learning with Verifiable Noisy Rewards","url":"https://arxiv.org/html/2601.04411v1"},{"title":"[2604.15149] LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/abs/2604.15149"},{"title":"BEING CORRECT IS NOT ENOUGH: EFFICIENT VERIFICATION USING","url":"https://arxiv.org/pdf/2102.11991"}]

Based on the search results, I found the paper you're looking for:

## arXiv 2604.07666: "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards"

The paper was submitted on April 9, 2026, by Andreas Plesner, Francisco Guzmán, and Anish Athalye.

### Key Findings:

The paper addresses Reinforcement Learning with Verifiable Rewards (RLVR), a prominent method for post-training Large Language Models, noting that verifiers are rarely error-free and that the extent to which RLVR is robust to noise and what verifier accuracy is required for effective training remain unresolved questions.

**Main Results:**
The researchers investigated these questions in the domains of code generation and scientific reasoning by introducing noise into RL training, finding that noise rates up to 15% yield peak validation accuracy within 2 percentage points of the clean baseline, with these findings consistent across controlled and model-based noise types, three model families (Qwen3, GLM4, Llama 3.1), and model sizes from 4B to 9B.

**Conclusion:**
The results indicate that imperfect verification does not constitute a fundamental barrier to RLVR. Additionally, a model-based verifier with approximately 85% accuracy and precision recovers most of the ground-truth training signal, and RLVR tolerates up to 15% controlled noise with no significant performance loss.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f515e56-099d-4c7d-8ff5-8a1544ee7b14",
  "isSidechain": true,
  "promptId": "b590861c-9ae0-462b-9344-394cda6aa41d",
  "agentId": "abf0f5ee5f5120153",
  "type": "user",
  "uuid": "ccdf8a1b-27bc-4572-872d-a73f7f5ab260",
  "sourceToolAssistantUUID": "9f515e56-099d-4c7d-8ff5-8a1544ee7b14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T04:12:00.239Z_

<details><summary>↩ Tool result · `toolu_01Ez9jqEhdn1kLyGUbZnYxdY`</summary>

```text
Web search results for query: "CURE co-evolving coder unit tester co-evolution code LLM paper 2026"

Links: [{"title":"[2506.03136] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/abs/2506.03136"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=wPdBe9zxNr"},{"title":"GitHub - Gen-Verse/CURE: [NeurIPS 2025 Spotlight] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning · GitHub","url":"https://github.com/Gen-Verse/CURE"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/html/2506.03136v2"},{"title":"Paper page - Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://huggingface.co/papers/2506.03136"},{"title":"[2506.03136v1] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/abs/2506.03136v1"},{"title":"[Literature Review] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://www.themoonlight.io/en/review/co-evolving-llm-coder-and-unit-tester-via-reinforcement-learning"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/392372360_Co-Evolving_LLM_Coder_and_Unit_Tester_via_Reinforcement_Learning"},{"title":"CURE: Co-Evolving Coders and Unit Testers via Reinforcement Learning","url":"https://openreview.net/pdf/6be4b1f5dff8b39f2e222dc06ccafec29b4f4ec0.pdf"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning Yinjie Wang1∗,","url":"https://openreview.net/pdf/f11013ca9dbe05459e89557ddb9b09d292b6f6ba.pdf"}]

Based on the web search results, I found comprehensive information about the CURE paper:

## CURE: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning

CURE is a novel reinforcement learning framework with a dedicated reward design that co-evolves coding and unit test generation capabilities based on their interaction outcomes, without any ground-truth code as supervision.

### Key Features

This approach enables flexible and scalable training and allows the unit tester to learn directly from the coder's mistakes. CURE constructs a pairwise reward matrix based on interactions between generated codes and generated tests, enabling mutual supervision and continuous improvement.

### Research Results

The derived ReasonFlux-Coder-7B and 14B models improve code generation accuracy by 5.3% and Best-of-N accuracy by 9.0% after optimization on Qwen2.5-Instruct models, outperforming similarly sized Qwen-Coder, DeepSeek-Coder, and Seed-Coder.

They naturally extend to downstream tasks such as test-time scaling and agentic coding—achieving a 8.1% improvement over the base model.

### Publication and Availability

The paper was published on September 18, 2025 as a NeurIPS 2025 spotlight. The authors have made everything publicly available—including models, comprehensive evaluation benchmarks, training and testing datasets, and training codes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43bb1d4a-114b-4886-be86-e8a121c2b12b",
  "isSidechain": true,
  "promptId": "b590861c-9ae0-462b-9344-394cda6aa41d",
  "agentId": "abf0f5ee5f5120153",
  "type": "user",
  "uuid": "5417bf39-cfdf-421d-8e7e-b51355fd1ebb",
  "sourceToolAssistantUUID": "43bb1d4a-114b-4886-be86-e8a121c2b12b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-18T04:12:03.579Z_

Let me get more detail on the G-Zero paper to confirm whether it is specifically about "verifier-free co-evolution" in the way described.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5417bf39-cfdf-421d-8e7e-b51355fd1ebb",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
  "requestId": "req_011Cb9P6BNZQLD9TiEKCnLpw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6ab39c0-9323-4464-9852-00f634fef8c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177eHmFQxq4H5LrVyaKkVS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 2101,
      "cache_read_input_tokens": 10367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2101,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T04:12:04.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ALGjg7sm5iCbjum1QzXYn`</summary>

```json
{
  "query": "G-Zero self-play open-ended generation zero data arXiv 2605.09959 details results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6ab39c0-9323-4464-9852-00f634fef8c2",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
  "requestId": "req_011Cb9P6BNZQLD9TiEKCnLpw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f0be77e-22ca-4358-9e83-ffcaff774ab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177eHmFQxq4H5LrVyaKkVS8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 2101,
      "cache_read_input_tokens": 10367,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 747,
          "output_tokens": 108,
          "cache_read_input_tokens": 10367,
          "cache_creation_input_tokens": 2101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2101,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T04:12:11.245Z_

<details><summary>↩ Tool result · `toolu_015ALGjg7sm5iCbjum1QzXYn`</summary>

```text
Web search results for query: "G-Zero self-play open-ended generation zero data arXiv 2605.09959 details results"

Links: [{"title":"[2605.09959v1] G-Zero: Self-Play for Open-Ended Generation from Zero Data","url":"https://arxiv.org/abs/2605.09959v1"},{"title":"G-Zero: Self-Play for Open-Ended Generation from Zero Data","url":"https://arxiv.org/html/2605.09959v1"},{"title":"‪Absolute zero: Reinforced self-play reasoning with zero data‬","url":"https://scholar.google.com/citations?view_op=view_citation&hl=en&user=9sDx70IAAAAJ&citation_for_view=9sDx70IAAAAJ:J_g5lzvAfSwC"},{"title":"Absolute Zero: Reinforced Self-play Reasoning with Zero Data | OpenReview","url":"https://openreview.net/forum?id=neZSGqhxDa"},{"title":"October 17, 2025 Absolute Zero: Reinforced Self-play Reasoning with Zero Data","url":"https://arxiv.org/pdf/2505.03335"},{"title":"1 Absolute Zero Reasoner (AZR) achieves state-of-the-art performance with ZERO DATA. Without relying on any gold labels or human-defined queries, Absolute Zero Reasoner trained using our proposed self-play approach demonstrates impressive general reasoning capabilities improvements in both math and coding, despite operating entirely out-of-distribution. Remarkably, AZR surpasses models trained on tens of thousands of expert-labeled in-domain examples in the combined average score across both domains.","url":"https://arxiv.org/html/2505.03335v2"},{"title":"NeurIPS Poster Absolute Zero: Reinforced Self-play Reasoning with Zero Data","url":"https://neurips.cc/virtual/2025/poster/116121"},{"title":"[Literature Review] Absolute Zero: Reinforced Self-play Reasoning with Zero Data","url":"https://www.themoonlight.io/en/review/absolute-zero-reinforced-self-play-reasoning-with-zero-data"},{"title":"Absolute Zero: Reinforced Self-play Reasoning with Zero Data Andrew Zhao1","url":"https://openreview.net/pdf/34a1a72a0a54db41248d9ad8862c78e55ac789d9.pdf"},{"title":"Paper page - Absolute Zero: Reinforced Self-play Reasoning with Zero Data","url":"https://huggingface.co/papers/2505.03335"}]

Based on the search results, here are the details about the G-Zero paper (arXiv 2605.09959):

## Paper Overview

G-Zero is a verifier-free, co-evolutionary framework for autonomous self-improvement.

## Problem Statement

Self-evolving LLMs excel in verifiable domains but struggle in open-ended tasks, where reliance on proxy LLM judges introduces capability bottlenecks and reward hacking.

## Key Innovation: Hint-δ Reward

The core innovation is Hint-δ, an intrinsic reward that quantifies the predictive shift between a Generator model's unassisted response and its response conditioned on a self-generated hint.

## Methodology

A Proposer model is trained via GRPO to continuously target the Generator's blind spots by synthesizing challenging queries and informative hints. The Generator is concurrently optimized via DPO to internalize these hint-guided improvements.

## Theoretical Results

The paper proves a best-iterate suboptimality guarantee for an idealized standard-DPO version of G-Zero, provided that the Proposer induces sufficient exploration coverage and the data filteration keeps pseudo-label score noise low.

## Authors and Affiliation

The paper was submitted on May 11, 2026 by authors from Washington University in St. Louis, University of Virginia, University of Maryland, and University of North Carolina at Chapel Hill.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f0be77e-22ca-4358-9e83-ffcaff774ab8",
  "isSidechain": true,
  "promptId": "b590861c-9ae0-462b-9344-394cda6aa41d",
  "agentId": "abf0f5ee5f5120153",
  "type": "user",
  "uuid": "2a8f9c06-497f-4282-ac6b-27dad17d4f73",
  "sourceToolAssistantUUID": "0f0be77e-22ca-4358-9e83-ffcaff774ab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-18T04:12:37.261Z_

Here is a report on all three papers.

---

## 1. "An Imperfect Verifier is Good Enough" (arXiv 2604.07666)

**Status: Confirmed to exist.**

This paper was submitted on April 9, 2026 by Andreas Plesner, Francisco Guzman, and Anish Athalye. Its full title is "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards."

**What it claims:** The paper investigates how robust RLVR (Reinforcement Learning with Verifiable Rewards) is to verifier noise in the domains of code generation and scientific reasoning. The key findings are:

- Noise rates up to **15%** yield peak validation accuracy within **2 percentage points** of the clean (noise-free) baseline.
- These findings are consistent across controlled and model-based noise types, three model families (Qwen3, GLM4, Llama 3.1), and model sizes from 4B to 9B parameters.
- A model-based verifier with approximately **85% accuracy and precision** recovers most of the ground-truth training signal.
- The overall conclusion is that **imperfect verification does not constitute a fundamental barrier to RLVR**.

The claim that it "shows RLVR training is robust to verifier noise rates up to 15%" is accurate. This does indeed suggest that the "verification ceiling" is less urgent than one might assume -- moderate verifier imperfection does not significantly degrade training outcomes.

---

## 2. CURE: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning (arXiv 2506.03136)

**Status: Confirmed to exist.**

CURE was published as a **NeurIPS 2025 Spotlight** paper (submitted June 2025). Authors include Yinjie Wang and others. Code and models are publicly available on GitHub (Gen-Verse/CURE).

**What it does:**

- CURE is a reinforcement learning framework that **co-evolves a code generator (Coder) and a unit test generator (Tester)** using their interaction outcomes as mutual supervision, with **no ground-truth code** required.
- It constructs a **pairwise reward matrix** based on interactions between generated codes and generated tests, enabling mutual supervision and continuous improvement.
- The resulting models (ReasonFlux-Coder-7B and 14B, built on Qwen2.5-Instruct) improve code generation accuracy by **5.3%** and Best-of-N accuracy by **9.0%**, outperforming similarly-sized Qwen-Coder, DeepSeek-Coder, and Seed-Coder.
- The approach naturally extends to downstream tasks such as test-time scaling and agentic coding, achieving an **8.1% improvement** over the base model.

This is indeed a co-evolution approach where the coder and unit tester train each other without ground-truth labels.

---

## 3. G-Zero (arXiv 2605.09959)

**Status: Confirmed to exist, but the description "verifier-free co-evolution" is only partially accurate.**

The paper's full title is **"G-Zero: Self-Play for Open-Ended Generation from Zero Data"**, submitted May 11, 2026. Authors are from Washington University in St. Louis, University of Virginia, University of Maryland, and UNC Chapel Hill.

**What it does:**

- G-Zero is a **verifier-free, co-evolutionary framework** for autonomous self-improvement in **open-ended generation tasks** (not just verifiable domains like math/code).
- The core innovation is **Hint-delta**, an intrinsic reward that measures the predictive shift between a Generator model's unassisted response and its response conditioned on a self-generated hint. This replaces external verifiers or LLM judges entirely.
- A **Proposer** model (trained via GRPO) synthesizes challenging queries and informative hints targeting the Generator's blind spots, while the **Generator** (trained via DPO) is concurrently optimized to internalize these hint-guided improvements.
- The paper provides a theoretical best-iterate suboptimality guarantee under certain conditions (sufficient exploration coverage from the Proposer and low pseudo-label noise from data filtration).

It is accurate to call this "verifier-free co-evolution" -- the two components (Proposer and Generator) co-evolve without any external reward model or verifier. However, note that it is focused on open-ended generation rather than code or math specifically. It builds on the lineage of Absolute Zero (arXiv 2505.03335, NeurIPS 2025), extending zero-data self-play to non-verifiable domains.

---

Sources:
- [An Imperfect Verifier is Good Enough (2604.07666)](https://arxiv.org/abs/2604.07666)
- [CURE: Co-Evolving LLM Coder and Unit Tester (2506.03136)](https://arxiv.org/abs/2506.03136)
- [CURE on GitHub (Gen-Verse/CURE)](https://github.com/Gen-Verse/CURE)
- [CURE on OpenReview (NeurIPS 2025)](https://openreview.net/forum?id=wPdBe9zxNr)
- [G-Zero: Self-Play for Open-Ended Generation (2605.09959)](https://arxiv.org/abs/2605.09959v1)
- [Absolute Zero: Reinforced Self-play Reasoning (2505.03335)](https://arxiv.org/abs/2505.03335)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a8f9c06-497f-4282-ac6b-27dad17d4f73",
  "isSidechain": true,
  "agentId": "abf0f5ee5f5120153",
  "requestId": "req_011Cb9P6zUzWTThqUX58ZEWM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83fa78d2-7b2f-4e10-a314-fc9c7e530211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a277b0d2-5348-491e-9e77-1eef95e729f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTvSSihom9CgwZzsgYcRaY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1839,
      "cache_read_input_tokens": 12468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1839,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
