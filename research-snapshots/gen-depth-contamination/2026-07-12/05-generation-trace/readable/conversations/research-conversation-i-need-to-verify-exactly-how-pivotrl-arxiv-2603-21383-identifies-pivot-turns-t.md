# Research conversation: I need to verify exactly how PivotRL (arXiv 2603.21383) identifies pivot turns. The paper under review (STAG) describes 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a0c58030a7eaa1d6b.jsonl`
- **Structured JSON:** [`ab17f0ba396fedbca9ef.json`](../../sessions/ab/ab17f0ba396fedbca9ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-12T02:05:46.055Z_

I need to verify exactly how PivotRL (arXiv 2603.21383) identifies pivot turns. The paper under review (STAG) describes PivotRL as using "static offline profiling of reference-policy outcome variance" and "identifies pivot turns via static offline profiling of reference policy outcome variance."

My reference verification agent found this may be inaccurate - that PivotRL uses "on-policy rollouts with mixed-outcome filtering" instead.

Please search for "PivotRL arXiv 2603.21383" and use WebFetch to read the abstract and methodology section. Report:
1. How exactly does PivotRL identify pivot turns?
2. Is the identification done "offline" with a "reference policy" (static, one-time), or is it done "online" during training (dynamic, updated)?
3. Does PivotRL use "outcome variance" specifically?

This distinction matters because STAG claims to be "online" vs PivotRL's "static" approach - if PivotRL is actually online too, this claimed differentiation is false.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "235226b7-c9fb-47cc-955c-3ec137490437",
  "agentId": "a0c58030a7eaa1d6b",
  "type": "user",
  "uuid": "61f55908-2ea5-4b89-ae3c-7f09786506fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T02:05:46.058Z_

```json
{
  "parentUuid": "61f55908-2ea5-4b89-ae3c-7f09786506fd",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
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
  "uuid": "d1856c0e-3843-4f45-826a-b18abcce5e83",
  "timestamp": "2026-05-12T02:05:46.058Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T02:05:49.137Z_



I'll search for the PivotRL paper and fetch its content to verify the methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1856c0e-3843-4f45-826a-b18abcce5e83",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrcMuFyC4RcLtJCxFXo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58e83648-6019-4fa6-b806-320501d37108",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuvPGzqr2NBkVQcsZJR1L4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 792,
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

_source line 4 · 2026-05-12T02:05:49.426Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YarNrz3N4NBYwh5npubzcF`</summary>

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
  "parentUuid": "58e83648-6019-4fa6-b806-320501d37108",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrcMuFyC4RcLtJCxFXo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2405a5a-8cbd-4309-9fec-9d8ac4f70808",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuvPGzqr2NBkVQcsZJR1L4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 8223,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 792
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 792,
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

_source line 5 · 2026-05-12T02:05:49.430Z_

<details><summary>↩ Tool result · `toolu_01YarNrz3N4NBYwh5npubzcF`</summary>

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
  "parentUuid": "b2405a5a-8cbd-4309-9fec-9d8ac4f70808",
  "isSidechain": true,
  "promptId": "235226b7-c9fb-47cc-955c-3ec137490437",
  "agentId": "a0c58030a7eaa1d6b",
  "type": "user",
  "uuid": "83505953-c017-4cf5-b360-76f8d7573467",
  "sourceToolAssistantUUID": "b2405a5a-8cbd-4309-9fec-9d8ac4f70808",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T02:05:53.648Z_



Now let me search for the PivotRL paper and fetch its content from arXiv.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83505953-c017-4cf5-b360-76f8d7573467",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrccUbxgvoMCphWDXLZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae15995c-1394-4545-bb82-ccf2e0529807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfJz1ER6Yb6RjpX8d77HLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 7 · 2026-05-12T02:05:54.287Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016PdYFSX3ZNx7K3pioW5qgg`</summary>

```json
{
  "query": "PivotRL arXiv 2603.21383 pivot turns reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae15995c-1394-4545-bb82-ccf2e0529807",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrccUbxgvoMCphWDXLZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd1ad0e1-3a74-41df-aaa9-e24d07c21195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfJz1ER6Yb6RjpX8d77HLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 8 · 2026-05-12T02:05:56.762Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VTFkq9csx7m81mBs8HfJ4x`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.21383",
  "prompt": "Extract the full abstract and any methodology description visible on this page. I need to understand: 1) How does PivotRL identify pivot turns? 2) Is it done offline with a reference policy or online during training? 3) Does it use \"outcome variance\" specifically? Look for any details about the pivot turn identification mechanism."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd1ad0e1-3a74-41df-aaa9-e24d07c21195",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrccUbxgvoMCphWDXLZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c20062d4-ef27-4dc7-b7f5-9386829f6c70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfJz1ER6Yb6RjpX8d77HLj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9015,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 9015,
          "cache_creation_input_tokens": 1909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1909,
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

_source line 9 · 2026-05-12T02:06:00.977Z_

<details><summary>↩ Tool result · `toolu_01VTFkq9csx7m81mBs8HfJ4x`</summary>

```text
# PivotRL Pivot Turn Identification

Based on the page content, here's what's disclosed about the pivot mechanism:

## Pivot Identification Method

The abstract states that PivotRL "executes local, on-policy rollouts and filters for pivots: informative intermediate turns where sampled actions exhibit high variance in outcomes."

## Key Details

**Timing**: The mechanism operates **during training** through on-policy rollouts, not offline with a reference policy.

**Variance Approach**: Yes, the method specifically uses "high variance in outcomes" as the criterion for identifying which turns are pivots—the informative decision points worth optimizing.

**Two-Part Framework**:
1. Local on-policy rollouts generate trajectory samples
2. Filtering identifies pivots where action choices produce notably divergent results

The paper emphasizes that PivotRL works on "existing SFT trajectories," suggesting it leverages supervised fine-tuning data as initialization, then applies selective on-policy optimization at these high-variance decision points to improve both in-domain and out-of-domain accuracy while maintaining computational efficiency compared to end-to-end reinforcement learning.

The page doesn't provide implementation details beyond this conceptual description.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c20062d4-ef27-4dc7-b7f5-9386829f6c70",
  "isSidechain": true,
  "promptId": "235226b7-c9fb-47cc-955c-3ec137490437",
  "agentId": "a0c58030a7eaa1d6b",
  "type": "user",
  "uuid": "708f8081-1f5e-44fa-9cab-059564155f52",
  "sourceToolAssistantUUID": "c20062d4-ef27-4dc7-b7f5-9386829f6c70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T02:06:01.758Z_

<details><summary>↩ Tool result · `toolu_016PdYFSX3ZNx7K3pioW5qgg`</summary>

```text
Web search results for query: "PivotRL arXiv 2603.21383 pivot turns reinforcement learning"

Links: [{"title":"PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost","url":"https://arxiv.org/html/2603.21383"},{"title":"[2603.21383] PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost","url":"https://arxiv.org/abs/2603.21383"},{"title":"2026-3-24 PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost","url":"https://arxiv.org/pdf/2603.21383"},{"title":"Paper page - PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost","url":"https://huggingface.co/papers/2603.21383"},{"title":"PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.21383"},{"title":"[2109.13097] Towards Reinforcement Learning for Pivot-based Neural Machine Translation with Non-autoregressive Transformer","url":"https://arxiv.org/abs/2109.13097"},{"title":"Deep Dense Exploration for LLM Reinforcement Learning via Pivot-Driven Resampling","url":"https://arxiv.org/html/2602.14169v1"},{"title":"[1703.00472] Reinforcement Learning for Pivoting Task","url":"https://ar5iv.labs.arxiv.org/html/1703.00472"},{"title":"[2602.14169] Deep Dense Exploration for LLM Reinforcement Learning via Pivot-Driven Resampling","url":"https://arxiv.org/abs/2602.14169"},{"title":"Reinforcement Learning for Pivoting Task - ADS","url":"https://ui.adsabs.harvard.edu/abs/2017arXiv170300472A/abstract"}]

Based on the search results, here's what I found about PivotRL:

## PivotRL Overview

PivotRL is a novel framework that operates on existing SFT trajectories to combine the compute efficiency of SFT with the OOD accuracy of E2E RL.

## Key Mechanisms

PivotRL executes local, on-policy rollouts and filters for pivots: informative assistant turns where sampled actions exhibit mixed outcomes (i.e., both successes and failures). It utilizes rewards for functional-equivalent actions rather than demanding strict string matching with the SFT data demonstration.

## Problem It Solves

Post-training for long-horizon agentic tasks has a tension between compute efficiency and generalization. While supervised fine-tuning (SFT) is compute efficient, it often suffers from out-of-domain (OOD) degradation. Conversely, end-to-end reinforcement learning (E2E RL) preserves OOD capabilities, but incurs high compute costs due to many turns of on-policy rollout.

## Performance Results

On agentic coding tasks, PivotRL achieves competitive accuracy with E2E RL with 4× fewer rollout turns.

## Production Deployment

PivotRL is adopted by NVIDIA's Nemotron-3-Super-120B-A12B, acting as the workhorse in production-scale agentic post-training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd1ad0e1-3a74-41df-aaa9-e24d07c21195",
  "isSidechain": true,
  "promptId": "235226b7-c9fb-47cc-955c-3ec137490437",
  "agentId": "a0c58030a7eaa1d6b",
  "type": "user",
  "uuid": "b1bd5b57-f538-4ffc-b46a-304e7965ba35",
  "sourceToolAssistantUUID": "cd1ad0e1-3a74-41df-aaa9-e24d07c21195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-12T02:06:04.704Z_

Good, I have some initial information. The abstract mentions "on-policy rollouts" and "high variance in outcomes." Let me now fetch the full HTML version of the paper to read the detailed methodology section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1bd5b57-f538-4ffc-b46a-304e7965ba35",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrdWwzyxtrAzidtM5na",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12e9042c-acad-48fc-8d09-95d19f648737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XSQ9zm7a8DWjxLdTu33X1Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 297,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 10924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
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

_source line 12 · 2026-05-12T02:06:11.241Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0131N9VnUTrQMtQNE6U8xvtw`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.21383",
  "prompt": "I need the DETAILED methodology for how PivotRL identifies pivot turns. Please extract:\n\n1. The exact mechanism for identifying pivot turns - is it done via 'on-policy rollouts' or 'offline profiling with a reference policy'?\n2. Does it use a FIXED/FROZEN reference policy, or the CURRENT training policy (on-policy)?\n3. The exact role of 'outcome variance' - is it variance of outcomes from a reference policy, or from the current policy's rollouts?\n4. Is the pivot identification a one-time static/offline step, or is it done dynamically during training?\n5. Any mention of 'mixed outcomes' vs 'outcome variance' - what exact terminology does the paper use?\n6. Look for sections titled 'Method', 'Methodology', 'Approach', 'Algorithm', 'Pivot Identification', or similar.\n7. Any algorithm pseudocode or step-by-step description of the training loop.\n\nPlease be very precise and quote directly from the paper where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12e9042c-acad-48fc-8d09-95d19f648737",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrdWwzyxtrAzidtM5na",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01375e7b-080d-4a40-be22-7987c740f325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XSQ9zm7a8DWjxLdTu33X1Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 297,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 10924,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 297,
          "output_tokens": 357,
          "cache_read_input_tokens": 10924,
          "cache_creation_input_tokens": 1101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1101,
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

_source line 13 · 2026-05-12T02:06:18.187Z_

<details><summary>↩ Tool result · `toolu_0131N9VnUTrQMtQNE6U8xvtw`</summary>

```text
# PivotRL Pivot Identification Methodology

## 1. Mechanism: Offline Profiling with Frozen Reference Policy

PivotRL identifies pivots through **offline profiling**, not on-policy rollouts during training:

> "We estimate the informativeness of each extracted turn under a frozen reference policy π₀"

The reference policy is "typically the policy used to initialize PivotRL."

## 2. Fixed vs. Current Policy

The pivot identification uses a **FROZEN/FIXED reference policy** (π₀), not the current training policy:

> "Sample K local rollouts from π₀(·|s)" and "We estimate the informativeness...under a frozen reference policy π₀"

This occurs **before** RL training begins.

## 3. Outcome Variance Role

The paper uses **outcome variance** (specifically reward variance) from the reference policy:

> "compute μ̂(s)...and σ̂²(s)...reward standard deviation"

Turns are retained where "σ̂²(s) > 0" (nonzero variance).

## 4. Timing: One-Time Offline Step

Pivot identification is a **static, one-time offline preprocessing step**:

> "Extract turns 𝒟_cand...Profile each s ∈ 𝒟_cand...Set 𝒟_pivot ← 𝒟_adv" (Algorithm 1, lines 2-4)

This happens **before** the training loop (lines 5-14).

## 5. Terminology: "Mixed Outcomes" and "Reward Variance"

The paper uses both terms interchangeably to mean **variance in binary rewards**:

> "mixed-outcome turns" and "turns with nonzero empirical reward variance"

Specifically: "only rollout groups with positive reward variance can contribute"

## 6. Algorithm Pseudocode

**Algorithm 1** (lines 2-4) shows the offline pivot selection pipeline:

1. Extract candidate turns from trajectories
2. Profile variance/mean using K frozen-policy rollouts
3. Filter to states where σ̂²(s) > 0 AND μ̂(s) < λ_diff
4. Train exclusively on retained pivot set
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01375e7b-080d-4a40-be22-7987c740f325",
  "isSidechain": true,
  "promptId": "235226b7-c9fb-47cc-955c-3ec137490437",
  "agentId": "a0c58030a7eaa1d6b",
  "type": "user",
  "uuid": "478d6a5c-c4cb-46cb-b120-da469512dafd",
  "sourceToolAssistantUUID": "01375e7b-080d-4a40-be22-7987c740f325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-12T02:06:21.268Z_

This is very revealing. Let me get even more detail from the full paper to understand whether there is any dynamic/online component.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "478d6a5c-c4cb-46cb-b120-da469512dafd",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrejQ8XHyiZyRs6t4VW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e46b8d6-24a9-440a-9549-183e3ef94bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APVsfxbj6vgP8RdDFCMV8u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 12025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1190,
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

_source line 15 · 2026-05-12T02:06:25.758Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018JuixG2eg2es9EmGhrTEvJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.21383",
  "prompt": "Please look specifically for:\n\n1. After the offline pivot identification step, what happens during the actual RL training? Does the set of pivot turns get updated during training, or does it remain fixed?\n2. During training (the RL loop), are NEW rollouts generated from the CURRENT/EVOLVING policy, or does it only use the frozen reference policy rollouts?\n3. Is there any 'on-policy' component at all? The abstract says 'on-policy rollouts' - does this refer to the pivot identification phase or the training phase?\n4. Quote the exact abstract sentence about 'on-policy rollouts'.\n5. Look for any discussion comparing PivotRL to other methods regarding online vs offline pivot identification.\n6. What exactly happens in Algorithm 1 lines 5-14 (the training loop)?\n\nPlease quote directly from the paper wherever possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e46b8d6-24a9-440a-9549-183e3ef94bc2",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrejQ8XHyiZyRs6t4VW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdfcfa7a-700e-403e-9751-19f1a5afa925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APVsfxbj6vgP8RdDFCMV8u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 12025,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1190
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 12025,
          "cache_creation_input_tokens": 1190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1190,
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

_source line 16 · 2026-05-12T02:06:33.069Z_

<details><summary>↩ Tool result · `toolu_018JuixG2eg2es9EmGhrTEvJ`</summary>

```text
# PivotRL: On-Policy vs Offline Pivot Selection Analysis

## Key Findings

**1. Pivot Set Remains Fixed During Training**

The pivot set is determined entirely offline before training begins. As stated: "Profile each s∈𝒟cand with Eq. (4)" followed by "Set 𝒟pivot←𝒟adv" happens before the training loop starts (Algorithm 1, lines 3-4). The subsequent training loop (lines 5-14) samples exclusively from this pre-computed set.

**2. Training Uses Current Policy Rollouts**

During the RL training loop, new rollouts ARE generated from the evolving policy: "Sample {ab,i}i=1^G∼πθold(⋅∣sb)" (Algorithm 1, line 8). However, πθold represents the current policy checkpoint, not the frozen reference policy π₀.

**3. Limited On-Policy Component**

The "on-policy" aspect refers specifically to the training phase, not pivot identification. The abstract states: "it executes local, on-policy rollouts and filters for pivots: informative intermediate turns."

**4. Exact Abstract Language**

The abstract describes the method as executing "local, on-policy rollouts" during training—meaning sampling actions from the training policy at selected states, not from a frozen baseline.

**5. Key Distinction from Other Methods**

Unlike pure offline approaches, PivotRL generates new rollouts during training from intermediate states, making it a hybrid: offline pivot selection + on-policy local training. This reduces computational cost versus end-to-end RL while maintaining adaptation benefits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdfcfa7a-700e-403e-9751-19f1a5afa925",
  "isSidechain": true,
  "promptId": "235226b7-c9fb-47cc-955c-3ec137490437",
  "agentId": "a0c58030a7eaa1d6b",
  "type": "user",
  "uuid": "798fbcd2-ec72-4ed8-8627-cf9cfb38581b",
  "sourceToolAssistantUUID": "fdfcfa7a-700e-403e-9751-19f1a5afa925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T02:06:41.980Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GiDFYdUmndmcPiuSNz15Ls`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.21383",
  "prompt": "I need to clarify the exact two-phase structure of PivotRL. Please find and quote:\n\n1. The exact definition of 'pivot turn' from the paper.\n2. Section 3 or equivalent methodology section - what are the subsections and what does each describe?\n3. Equation (4) - what exactly does it compute?\n4. The filtering criteria: what conditions must a turn satisfy to be a pivot? Quote the exact conditions.\n5. The phrase 'static offline profiling' - does this phrase appear anywhere in the paper? Or is it only used to describe PivotRL by other papers?\n6. The phrase 'reference policy outcome variance' - does this exact phrase appear?\n7. Any sentence that describes the pivot identification as 'offline' or 'static'.\n\nI need verbatim quotes to verify whether specific characterizations are accurate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "798fbcd2-ec72-4ed8-8627-cf9cfb38581b",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrfpqajQCKom3buBarG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ce17613-d5af-4132-bb0e-2b69d97c7a55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CX7K1pj85wGRzFiMKqQnP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 13215,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 681
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 13215,
          "cache_creation_input_tokens": 681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 681,
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

_source line 18 · 2026-05-12T02:06:48.846Z_

<details><summary>↩ Tool result · `toolu_01GiDFYdUmndmcPiuSNz15Ls`</summary>

```text
# PivotRL: Two-Phase Structure Analysis

## 1. Definition of 'Pivot Turn'

The paper does not explicitly define "pivot turn" as a standalone term. Instead, it uses:

**"informative assistant turns where sampled actions exhibit high variance in outcomes"** (Abstract)

And later: **"pivots: informative intermediate turns where sampled actions exhibit mixed outcomes"** (Section 3 introduction)

## 2. Section 3 Structure

Section 3 "PivotRL" contains two subsections:
- **3.1 Method** (with two sub-parts: "Offline turn selection" and "Verifier-based local reward")
- **3.2 Theoretical analysis for PivotRL**

## 3. Equation (4) Definition

**"μ̂(s)=1/K∑ʳ_func(s,a^(k)), σ̂²(s)=1/K∑(r_func(s,a^(k))−μ̂(s))²"**

This computes the mean and variance of functional rewards across K reference policy rollouts at state s.

## 4. Filtering Criteria (Equation 5)

**"𝒟_adv={(s,a*)∈𝒟_cand: σ̂²(s)>0, μ̂(s)<λ_diff}"**

Conditions: nonzero empirical reward variance AND low reward mean below difficulty threshold λ_diff.

## 5. "Static Offline Profiling"

This exact phrase **does not appear** in the paper. The paper uses: **"Profile turns offline"** (Algorithm 1, line 3).

## 6. "Reference Policy Outcome Variance"

This exact phrase **does not appear**. The paper says: **"Var_a∼π_s,β(r(s,a))"** or informal variants like "reward variance."

## 7. Offline/Static Description

**"We estimate the informativeness of each extracted turn under a frozen reference policy π₀"** (Section 3.1, "Offline turn selection" heading)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ce17613-d5af-4132-bb0e-2b69d97c7a55",
  "isSidechain": true,
  "promptId": "235226b7-c9fb-47cc-955c-3ec137490437",
  "agentId": "a0c58030a7eaa1d6b",
  "type": "user",
  "uuid": "4b065e89-6962-4785-b6bc-35abbea887fa",
  "sourceToolAssistantUUID": "1ce17613-d5af-4132-bb0e-2b69d97c7a55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-12T02:06:52.769Z_

Now I have a very clear picture. Let me do one final check to understand the full training loop and confirm the on-policy aspect.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b065e89-6962-4785-b6bc-35abbea887fa",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrgzGtef2eGujMhPxnX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1860b079-387c-4d35-b1f3-f792eab8e1e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8LHXa9uXX2fnDyp9FkrL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 13896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 787,
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

_source line 20 · 2026-05-12T02:06:57.040Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vs1jHsQKUPbJ9wSc8L9Jep`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.21383",
  "prompt": "Please extract Algorithm 1 in full detail, line by line. Also extract any text from Section 3.1 that describes the training loop (after pivot selection). Specifically I need to understand:\n\n1. After pivots are selected offline, does the training loop at each iteration sample NEW rollouts from the CURRENT policy at the pivot states?\n2. Is the pivot SET ever re-profiled or updated during training, or is it truly fixed once computed?\n3. Does the paper explicitly call this a 'two-phase' approach or 'hybrid'?\n4. Any comparison to methods that do online/dynamic pivot identification?\n\nQuote the relevant text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1860b079-387c-4d35-b1f3-f792eab8e1e5",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011CawrgzGtef2eGujMhPxnX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd217ef0-4966-4a34-a07f-be5b12990f33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8LHXa9uXX2fnDyp9FkrL8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 13896,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 787
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 13896,
          "cache_creation_input_tokens": 787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 787,
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

_source line 21 · 2026-05-12T02:07:10.466Z_

<details><summary>↩ Tool result · `toolu_01Vs1jHsQKUPbJ9wSc8L9Jep`</summary>

````text
# PivotRL Algorithm and Training Loop Analysis

## Algorithm 1 (Full Line-by-Line):

```
1: Require: expert trajectories D_sft, reference policy π₀, 
   initial policy π_θ, verifier V, rollout group size G, 
   difficulty threshold λ_diff

2: Extract turns D_cand = {(s_t, a_t*)} from D_sft

3: Profile each s ∈ D_cand with Eq. (4)

4: Set D_pivot ← D_adv

5: for k = 1, …, K_train do

6:   Sample minibatch {s_b}_{b=1}^B ~ D_pivot

7:   for each s_b do

8:    Sample {a_{b,i}}_{i=1}^G ~ π_{θ_old}(·|s_b)

9:    Execute the short rollout needed to score each a_{b,i}

10:   r_{b,i} ← r_func(s_b, a_{b,i}) for i = 1, …, G

11:   Compute A^_{b,i} ← (r_{b,i} - (1/G)Σ r_{b,j}) / (std(...) + ε_std)

12:  end for

13:  Update θ using the objective in Eq. (7)

14: end for
```

## Key Findings:

**1. NEW rollouts at each iteration:** Yes. Line 8 explicitly states the algorithm "Sample {a_{b,i}}_{i=1}^G ~ π_{θ_old}(·|s_b)" at each training step k, meaning the training loop generates fresh on-policy rollouts from the current (or most recent) policy at fixed pivot states.

**2. Fixed pivot set:** The paper confirms: "pivot candidates are extracted once from the demonstration traces, profiled offline, and filtered before RL training; training then samples only from the retained set" (Appendix A.2). The pivot set is never re-profiled during training.

**3. Terminology:** The paper does not explicitly use "two-phase" or "hybrid." Instead, it describes the approach as operating "offline" then "online": "Offline turn selection...Verifier-based local reward."

**4. Dynamic pivot comparison:** The paper does NOT compare to methods with online/dynamic pivot identification. The conclusion notes: "explore online reward profiling approaches such as dynamic sampling" as future work, suggesting this is absent from the current implementation.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd217ef0-4966-4a34-a07f-be5b12990f33",
  "isSidechain": true,
  "promptId": "235226b7-c9fb-47cc-955c-3ec137490437",
  "agentId": "a0c58030a7eaa1d6b",
  "type": "user",
  "uuid": "c9fd0aa7-9306-451e-8d5d-0d88a9afcef8",
  "sourceToolAssistantUUID": "bd217ef0-4966-4a34-a07f-be5b12990f33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-12T02:07:39.618Z_

Excellent. Now I have all the evidence needed to provide a thorough answer. Here is my report:

---

## Findings: How PivotRL (arXiv 2603.21383) Identifies Pivot Turns

### 1. Exact Mechanism for Pivot Identification

PivotRL identifies pivots through a **two-step offline process before training begins**:

- **Step 1 (Extract):** Candidate turns are extracted from existing SFT (supervised fine-tuning) demonstration trajectories.
- **Step 2 (Profile):** Each candidate turn/state `s` is profiled by running K rollouts from a **frozen reference policy** (pi_0, typically the initialization policy). For each state, the paper computes the mean and variance of functional rewards across those K rollouts (Equation 4). A turn qualifies as a "pivot" if it satisfies two conditions (Equation 5): (a) nonzero empirical reward variance (sigma-squared > 0), AND (b) low mean reward below a difficulty threshold (mu < lambda_diff).

The pivot set is computed **once** and remains **fixed** throughout training. Quoting the paper: "pivot candidates are extracted once from the demonstration traces, profiled offline, and filtered before RL training; training then samples only from the retained set." The paper's own Section 3.1 subsection is explicitly titled **"Offline turn selection."**

### 2. Offline vs. Online

The pivot **identification** is genuinely offline and static, using a frozen reference policy pi_0. The paper states: "We estimate the informativeness of each extracted turn under a frozen reference policy pi_0."

However, the **training phase** that follows IS on-policy. At each training iteration, the algorithm samples new rollouts from the **current evolving policy** (pi_theta_old) at the pre-selected pivot states (Algorithm 1, line 8). So PivotRL is a hybrid: offline pivot selection followed by on-policy local RL training at those fixed pivot states.

The abstract's phrase "on-policy rollouts" is somewhat ambiguous -- it refers to the training loop generating actions from the current policy, but the pivot selection itself was done offline with a frozen policy. Notably, the paper itself lists "explore online reward profiling approaches such as dynamic sampling" as **future work**, explicitly confirming that PivotRL does NOT do online/dynamic pivot identification.

### 3. Does PivotRL Use "Outcome Variance"?

**Yes, substantially.** The paper computes reward variance (sigma-squared) across rollouts from the reference policy and filters for turns with nonzero variance. The paper uses the terminology "high variance in outcomes," "mixed-outcome turns," and "nonzero empirical reward variance" interchangeably. So characterizing PivotRL as using "outcome variance" is accurate.

### Assessment of STAG's Characterization

STAG describes PivotRL as using **"static offline profiling of reference-policy outcome variance."** Based on the actual paper:

- **"Static offline profiling"**: The exact phrase "static offline profiling" does NOT appear in PivotRL, but it is a **fair and accurate characterization**. The paper's own section is titled "Offline turn selection," uses a "frozen reference policy," and the pivot set is computed once before training.
- **"Reference-policy outcome variance"**: This exact phrase also doesn't appear verbatim, but it is **accurate** -- the profiling uses rollouts from the reference policy pi_0 and computes reward variance.
- **"Identifies pivot turns via static offline profiling"**: **Accurate.** This is precisely what PivotRL does.

**The STAG paper's characterization of PivotRL appears to be correct.** PivotRL's pivot identification IS static/offline, and if STAG performs dynamic/online pivot identification during training, that IS a genuine methodological difference. The reference verification agent's concern that PivotRL uses "on-policy rollouts with mixed-outcome filtering" conflates two distinct phases: the on-policy aspect is in the training loop (generating actions at pivot states), not in the pivot identification step. The identification step is offline with a frozen policy.

### Summary

| Aspect | PivotRL (actual) | STAG's description | Accurate? |
|---|---|---|---|
| Pivot identification timing | Offline, before training | "Static offline" | Yes |
| Policy used for identification | Frozen reference policy pi_0 | "Reference policy" | Yes |
| Criterion | Reward variance > 0 | "Outcome variance" | Yes |
| Pivot set updated during training? | No (fixed) | Implied "static" | Yes |

Sources:
- [PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost (Abstract)](https://arxiv.org/abs/2603.21383)
- [PivotRL: Full HTML Paper](https://arxiv.org/html/2603.21383)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9fd0aa7-9306-451e-8d5d-0d88a9afcef8",
  "isSidechain": true,
  "agentId": "a0c58030a7eaa1d6b",
  "requestId": "req_011Cawriaj6ojYPSDjGrihaz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc50d0ce-393c-4b92-bf5c-7a8d54f8302a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "283d6351-5ef7-4e15-8ceb-bae22e467cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UircUWcyHUxfHVNfRzTm5B",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 14683,
      "output_tokens": 1149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 866
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1149,
          "cache_read_input_tokens": 14683,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 866,
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
