# Research conversation: Search the web for these two papers that are claimed to be competitors in VLA token operations / representation preserva

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad18a3361d14d917e.jsonl`
- **Structured JSON:** [`e4a77d7c5d7d11b7b8f9.json`](../../sessions/e4/e4a77d7c5d7d11b7b8f9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-13T04:57:56.379Z_

Search the web for these two papers that are claimed to be competitors in VLA token operations / representation preservation:

1. "See What Matters" / GridS by Feng et al., claimed as ICML 2026. Differentiable grid sample pruning for generalizable VLA. Search:
   - "See What Matters differentiable grid sample pruning VLA"
   - "GridS VLA ICML 2026 Feng"
   - "token pruning VLA generalization ICML 2026"

2. "Knowledge Insulating Vision-Language-Action Models" by Driess et al., Physical Intelligence, arXiv 2505.23705 (May 2025). Gradient insulation approach. Search:
   - "Knowledge Insulation VLA arXiv 2505.23705"
   - "Physical Intelligence VLA gradient insulation"
   - "Knowledge Insulating Vision-Language-Action train fast run fast"

For each paper: verify it exists, summarize the approach, and note its relationship to token masking for VLA generalization. Use WebFetch on the arXiv pages if found. Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "b4bb2252-b127-4b21-abcf-879d9b0b56ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T04:57:56.382Z_

```json
{
  "parentUuid": "b4bb2252-b127-4b21-abcf-879d9b0b56ec",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "5e1650f1-cfb7-4818-a208-f7f2e8d2fffb",
  "timestamp": "2026-05-13T04:57:56.382Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T04:57:59.730Z_



I'll search for both papers. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e1650f1-cfb7-4818-a208-f7f2e8d2fffb",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011CayyYmX2r7FpNJLVe4V8v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fd8a01a-c4e3-45aa-8bf3-a9801400f8e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsvhgPfy1NgPff8HN98pPD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 788,
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

_source line 4 · 2026-05-13T04:57:59.885Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DZ5rT6zSR7sBBV4HV4yBfQ`</summary>

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
  "parentUuid": "7fd8a01a-c4e3-45aa-8bf3-a9801400f8e2",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011CayyYmX2r7FpNJLVe4V8v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be903637-53eb-423f-9be7-998ce5125dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsvhgPfy1NgPff8HN98pPD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 7304,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 788
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 788,
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

_source line 5 · 2026-05-13T04:57:59.889Z_

<details><summary>↩ Tool result · `toolu_01DZ5rT6zSR7sBBV4HV4yBfQ`</summary>

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
  "parentUuid": "be903637-53eb-423f-9be7-998ce5125dfd",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "100a5f64-2502-47cf-9423-02854a77825d",
  "sourceToolAssistantUUID": "be903637-53eb-423f-9be7-998ce5125dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T04:58:13.117Z_



Now let me search for both papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "100a5f64-2502-47cf-9423-02854a77825d",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011CayyZ2c912Q68q63o7DL1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adf5bba2-1260-4c63-a15a-a60bd6fc9b37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mDAw5RSTMpPSaXavKmiqZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 7 · 2026-05-13T04:58:14.210Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GseT3wthXWdmRKFYmHDxLr`</summary>

```json
{
  "query": "See What Matters differentiable grid sample pruning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adf5bba2-1260-4c63-a15a-a60bd6fc9b37",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011CayyZ2c912Q68q63o7DL1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "407fb4e5-73b2-488d-a497-1cafa6eefacb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mDAw5RSTMpPSaXavKmiqZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 8 · 2026-05-13T04:58:14.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SCfuirwQszddJcn2d3RTBQ`</summary>

```json
{
  "query": "GridS VLA ICML 2026 Feng"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "407fb4e5-73b2-488d-a497-1cafa6eefacb",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011CayyZ2c912Q68q63o7DL1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fba86ca9-48cc-4d47-808d-e83c3d7c4ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mDAw5RSTMpPSaXavKmiqZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 9 · 2026-05-13T04:58:15.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017SieEq6miP5VXmxrELoodC`</summary>

```json
{
  "query": "Knowledge Insulation VLA arXiv 2505.23705"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fba86ca9-48cc-4d47-808d-e83c3d7c4ec4",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011CayyZ2c912Q68q63o7DL1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae273858-0a3d-4462-a052-50a92113b81f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mDAw5RSTMpPSaXavKmiqZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 10 · 2026-05-13T04:58:15.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0148Lpn4kHbEheW9cYk88qLP`</summary>

```json
{
  "query": "Physical Intelligence VLA gradient insulation Driess"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae273858-0a3d-4462-a052-50a92113b81f",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011CayyZ2c912Q68q63o7DL1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcf8fcb1-90e5-4ee7-aea5-453a7d8bb153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mDAw5RSTMpPSaXavKmiqZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8092,
      "output_tokens": 216,
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
          "output_tokens": 216,
          "cache_read_input_tokens": 8092,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1911,
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

_source line 11 · 2026-05-13T04:58:21.031Z_

<details><summary>↩ Tool result · `toolu_01GseT3wthXWdmRKFYmHDxLr`</summary>

```text
Web search results for query: "See What Matters differentiable grid sample pruning VLA"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"Differentiable Gradient Sampling for Learning Implicit 3D Scene Reconstructions from a Single Image | OpenReview","url":"https://openreview.net/forum?id=U8pbd00cCWB"},{"title":"PDP: Parameter-free Differentiable Pruning is All You Need Minsik Cho","url":"https://arxiv.org/pdf/2305.11203v3"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"PDP: Parameter-free Differentiable Pruning is All You Need","url":"https://arxiv.org/pdf/2305.11203"},{"title":"Separate, Dynamic and Differentiable (SMART) Pruner for Block/Output Channel Pruning on Computer Vision Tasks","url":"https://arxiv.org/html/2403.19969v1"}]

Based on the search results, I found information about "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model":

## Overview

Vision-Language-Action (VLA) models have shown remarkable promise in robotics manipulation, yet their high computational cost hinders real-time deployment. 

## The Proposed Solution

The research proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA.

## Key Problem It Addresses

Existing token pruning methods suffer from a fundamental trade-off: aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation, which forces a compromise and limits the achievable compression rate.

## How GridS Works

By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression (with fewer than 10%).

The paper was presented at ICML 2026 and represents an approach to making VLA models more efficient while maintaining critical spatial information for robotic tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "407fb4e5-73b2-488d-a497-1cafa6eefacb",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "ad953ddc-37a0-4c33-a773-7c3492a39694",
  "sourceToolAssistantUUID": "407fb4e5-73b2-488d-a497-1cafa6eefacb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T04:58:22.042Z_

<details><summary>↩ Tool result · `toolu_01SCfuirwQszddJcn2d3RTBQ`</summary>

```text
Web search results for query: "GridS VLA ICML 2026 Feng"

Links: [{"title":"GitHub - InternRobotics/InstructVLA: [ICLR 2026] InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation · GitHub","url":"https://github.com/InternRobotics/InstructVLA"},{"title":"ICLR 2026 Workshops","url":"https://iclr.cc/virtual/2026/events/workshop"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10109"},{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICML 2026 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/icml-statistics/icml-2026-statistics/"},{"title":"GitHub - wlfeng0509/Fast-SAM3D: [ICML 2026] Official Repo for Fast-SAM3D: 3Dfy Anything in Images but Faster · GitHub","url":"https://github.com/wlfeng0509/Fast-SAM3D"},{"title":"ICLR 2026 Thursday 04/23","url":"https://iclr.cc/virtual/2026/day/4/23"},{"title":"2026 Conference","url":"https://iclr.cc/"}]

Based on the search results, I found information related to your query about Vision-Language-Action (VLA) models at ICLR 2026 with Feng as an author:

InstructVLA is a VLA architecture and training pipeline that emphasizes the importance of language capability in VLAs by efficiently preserving pretrained vision-language knowledge from VLMs while integrating manipulation as a component of instruction following. One of the authors on this ICLR 2026 paper is Feng Zhao from the University of Science and Technology of China and Zhejiang University.

However, I did not find specific information about a paper called "GridS VLA" or its connection to ICML 2026 in these search results. The search results show VLA research at ICLR 2026 rather than ICML 2026. If you're looking for a specific GridS VLA paper at ICML 2026, you might want to refine your search or provide additional details about what you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fba86ca9-48cc-4d47-808d-e83c3d7c4ec4",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "070b34a4-003f-486b-9da0-b776ed231a75",
  "sourceToolAssistantUUID": "fba86ca9-48cc-4d47-808d-e83c3d7c4ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T04:58:23.992Z_

<details><summary>↩ Tool result · `toolu_0148Lpn4kHbEheW9cYk88qLP`</summary>

```text
Web search results for query: "Physical Intelligence VLA gradient insulation Driess"

Links: [{"title":"VLAs that Train Fast, Run Fast, and Generalize Better","url":"https://www.pi.website/research/knowledge_insulation"},{"title":"Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://arxiv.org/html/2505.23705v1"},{"title":"Knowledge Insulating Vision-Language-Action Models","url":"https://www.physicalintelligence.company/download/pi05_KI.pdf"},{"title":"Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better | Request PDF","url":"https://www.researchgate.net/publication/392204240_Knowledge_Insulating_Vision-Language-Action_Models_Train_Fast_Run_Fast_Generalize_Better"},{"title":"[2505.23705] Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://arxiv.org/abs/2505.23705"},{"title":"Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better | OpenReview","url":"https://openreview.net/forum?id=cb0xbZ3APM"},{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"Knowledge Insulating Vision-Language-Action Models","url":"https://neurips2025.pages.dev/explainers/knowledge_insulating_vision_language/"},{"title":"NeurIPS Poster Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117079"},{"title":"𝜋^∗_0.6: a VLA That Learns From Experience","url":"https://arxiv.org/html/2511.14759"}]

Based on the search results, here's what I found about Physical Intelligence's VLA gradient insulation research:

## Overview

This research by Danny Driess and colleagues at Physical Intelligence addresses Vision-Language-Action (VLA) models, which provide a powerful approach to training control policies for physical systems like robots by combining end-to-end learning with transfer of semantic knowledge from web-scale vision-language model (VLM) training.

## The Problem

When adapting a VLM to a VLA with an action expert design, the VLM backbone representations are exposed to gradients from the action expert, which leads to unfavorable learning dynamics resulting in much slower learning and causing the VLM backbone to lose some of the knowledge acquired during web-scale pre-training.

## The Solution: Knowledge Insulation

The key idea behind knowledge insulation is to fine-tune the VLM backbone with discretized actions while simultaneously adapting an action expert to produce continuous actions (e.g., via flow matching or diffusion) without propagating its gradients back into the VLM backbone.

This approach results in a VLA that trains quickly, runs fast at inference time, and generalizes well by maintaining the pre-trained knowledge of the backbone VLM.

## Results

The approach allows researchers to graft action experts onto VLMs without loss of pre-trained web-scale knowledge, resulting in fast training, good semantic generalization, and precise motor control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcf8fcb1-90e5-4ee7-aea5-453a7d8bb153",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "8c485ac5-ee8e-4919-a9d6-ff3f1c7821e4",
  "sourceToolAssistantUUID": "bcf8fcb1-90e5-4ee7-aea5-453a7d8bb153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T04:58:26.852Z_

<details><summary>↩ Tool result · `toolu_017SieEq6miP5VXmxrELoodC`</summary>

```text
Web search results for query: "Knowledge Insulation VLA arXiv 2505.23705"

Links: [{"title":"[2505.23705] Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://arxiv.org/abs/2505.23705"},{"title":"Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better | Request PDF","url":"https://www.researchgate.net/publication/392204240_Knowledge_Insulating_Vision-Language-Action_Models_Train_Fast_Run_Fast_Generalize_Better"},{"title":"Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://arxiv.org/html/2505.23705v1"},{"title":"Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better | OpenReview","url":"https://openreview.net/forum?id=cb0xbZ3APM"},{"title":"[PDF] Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Knowledge-Insulating-Vision-Language-Action-Models:-Driess-Springenberg/f8a3331421b98c7d4065ecf55c4013e6306359f2"},{"title":"AR-VLA: True Autoregressive Action Expert for Vision–Language–Action Models","url":"https://arxiv.org/html/2603.10126v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training","url":"https://arxiv.org/html/2512.24125v2"},{"title":"LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer","url":"https://arxiv.org/html/2602.10556v1"},{"title":"FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies","url":"https://arxiv.org/html/2509.04996v1"}]

Based on the search results, here's what I found about this paper:

## Knowledge Insulating Vision-Language-Action Models

Vision-language-action (VLA) models provide a powerful approach to training control policies for physical systems, such as robots, by combining end-to-end learning with transfer of semantic knowledge from web-scale vision-language model (VLM) training. However, the constraints of real-time control are often at odds with the design of VLMs: the most powerful VLMs have tens or hundreds of billions of parameters, presenting an obstacle to real-time inference, and operate on discrete tokens rather than the continuous-valued outputs that are required for controlling robots.

### Key Problem and Solution

The paper shows that naively including continuous diffusion or flow matching action experts significantly harms both training speed and knowledge transfer. To address this, the researchers provide an extensive analysis of various design choices, their impact on performance and knowledge transfer, and propose a technique for insulating the VLM backbone during VLA training that mitigates this issue.

### Paper Details

The paper was submitted on May 29, 2025 by Danny Driess and 10 other authors. Videos and open-source model weights are available at https://pi.website/research/knowledge_insulation and https://github.com/Physical-Intelligence/openpi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae273858-0a3d-4462-a052-50a92113b81f",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "72cafaeb-e66e-4509-a91c-2d148482563f",
  "sourceToolAssistantUUID": "ae273858-0a3d-4462-a052-50a92113b81f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-13T04:58:32.028Z_

Good, both papers are confirmed to exist. Let me now fetch detailed content from the key pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72cafaeb-e66e-4509-a91c-2d148482563f",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011Cayyb1naVSRYqZQuoCkw9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0e26622-c47c-4955-b433-70469dfe283a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lerp8UvotD1uDPYVwBmsiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 874,
      "cache_creation_input_tokens": 2756,
      "cache_read_input_tokens": 10003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2756,
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

### Tool call

_source line 16 · 2026-05-13T04:58:34.398Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LqN6CKimxWyMt6Vp8ERj9V`</summary>

```json
{
  "url": "https://icml.cc/virtual/2026/poster/65010",
  "prompt": "Extract all details about this paper: title, authors, abstract, key method (GridS), claims about compression rate, generalization, and any comparisons to other token pruning/masking methods for VLA."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e26622-c47c-4955-b433-70469dfe283a",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011Cayyb1naVSRYqZQuoCkw9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1b95bc2-91bc-4bac-9492-133d49223ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lerp8UvotD1uDPYVwBmsiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 874,
      "cache_creation_input_tokens": 2756,
      "cache_read_input_tokens": 10003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2756,
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

### Tool call

_source line 17 · 2026-05-13T04:58:35.619Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JT87ynS8b38oxtuurKZyhD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.23705",
  "prompt": "Extract all details: full title, all authors with affiliations, abstract, key method (knowledge insulation), how gradient insulation works, results on generalization, and any relationship to token masking or token-level operations in VLA models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1b95bc2-91bc-4bac-9492-133d49223ebc",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011Cayyb1naVSRYqZQuoCkw9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b49546eb-785d-45e8-bfdb-4ec16c7d3f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lerp8UvotD1uDPYVwBmsiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 874,
      "cache_creation_input_tokens": 2756,
      "cache_read_input_tokens": 10003,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2756
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 874,
          "output_tokens": 262,
          "cache_read_input_tokens": 10003,
          "cache_creation_input_tokens": 2756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2756,
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

_source line 18 · 2026-05-13T04:58:38.675Z_

<details><summary>↩ Tool result · `toolu_01LqN6CKimxWyMt6Vp8ERj9V`</summary>

```text
# Paper Summary: Differentiable Grid Sample Pruning for VLA

## Title
"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

## Authors
Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

## Core Method: GridS (Differentiable Grid Sampler)
GridS is described as "a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA." The approach adaptively identifies minimal salient coordinates and extracts features through differentiable interpolation to maintain spatial information.

## Key Claims

**Compression Performance:**
The authors report achieving "a 76% reduction in FLOPs with no degradation in the success rate" while using "fewer than 10% original visual tokens."

**Problem Being Addressed:**
Traditional token pruning methods create a problematic trade-off where aggressive compression removes "critical geometric details like contact points, leading to severe performance degradation."

**Validation:**
Experiments on both the LIBERO benchmark and real robotic platforms reportedly demonstrate "the lowest feasible visual token count reported to date."

## Comparative Context
The abstract positions GridS as superior to "existing token pruning methods" by reframing compression as "geometry-aware, continuous token resampling" rather than simple token elimination.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1b95bc2-91bc-4bac-9492-133d49223ebc",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "1faa8066-38cc-48fa-9294-3f97dbe56931",
  "sourceToolAssistantUUID": "a1b95bc2-91bc-4bac-9492-133d49223ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T04:58:41.317Z_

<details><summary>↩ Tool result · `toolu_01JT87ynS8b38oxtuurKZyhD`</summary>

```text
# Knowledge Insulating Vision-Language-Action Models: Analysis

## Title & Authors
**Full Title:** "Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better"

**Authors:** Danny Driess, Jost Tobias Springenberg, Brian Ichter, Lili Yu, Adrian Li-Bell, Karl Pertsch, Allen Z. Ren, Homer Walke, Quan Vuong, Lucy Xiaoyang Shi, and Sergey Levine

*(Affiliations not provided in the source document)*

## Abstract Summary
The paper addresses a fundamental tension in VLA design: powerful vision-language models with billions of parameters enable semantic knowledge transfer but conflict with real-time robotic control requirements. The researchers observe that "naively including such experts significantly harms both training speed and knowledge transfer" when adding continuous action modules to pretrained VLM backbones.

## Key Method: Knowledge Insulation
The core contribution involves a technique for "insulating the VLM backbone during VLA training." This approach mitigates performance degradation caused by naive integration of specialized action modules (diffusion or flow-matching experts) with pretrained vision-language components.

## Gradient Insulation Mechanism
The document does not explicitly describe how gradient insulation operates mechanically.

## Generalization Results
The paper promises improvements in three dimensions: training velocity, inference speed, and generalization capability—reflected in the subtitle. However, specific quantitative results aren't detailed in this abstract.

## Token-Level Operations
No information regarding token masking or token-level VLA operations appears in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b49546eb-785d-45e8-bfdb-4ec16c7d3f84",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "02c1a98a-35ce-43b3-867e-88f370331065",
  "sourceToolAssistantUUID": "b49546eb-785d-45e8-bfdb-4ec16c7d3f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-13T04:58:43.838Z_

Let me get more detail on the Knowledge Insulation paper's actual method.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02c1a98a-35ce-43b3-867e-88f370331065",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011Cayyc5eH57rN6zHDHt6to",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e5de106-d17e-41c6-999a-67b803bd0e6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbBcuRWwEpKnjSVVXDSDn3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 12759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1987,
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

### Tool call

_source line 21 · 2026-05-13T04:58:47.889Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WMMXdg8HDHHYRNhtaDVshA`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.23705v1",
  "prompt": "Extract the detailed technical method of knowledge insulation: How exactly does gradient insulation work? What is the architecture - does it stop gradients from the action expert flowing back into the VLM backbone? How does this relate to token representations - does it preserve VLM token representations? What are the key experimental results (benchmarks, success rates, comparisons)? Is there any discussion of token pruning or token masking approaches? List the author affiliations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e5de106-d17e-41c6-999a-67b803bd0e6a",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011Cayyc5eH57rN6zHDHt6to",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edf13c39-ed9c-43ee-9f5e-9e4192d7016f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbBcuRWwEpKnjSVVXDSDn3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 12759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1987,
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

### Tool call

_source line 22 · 2026-05-13T04:58:48.635Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T7Fcm7RcqxYXkBd1QcgKsd`</summary>

```json
{
  "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/117079",
  "prompt": "Extract details about the Knowledge Insulation paper: was it accepted to NeurIPS 2025? What venue was it presented at?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edf13c39-ed9c-43ee-9f5e-9e4192d7016f",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011Cayyc5eH57rN6zHDHt6to",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31e24638-288c-4b60-8902-0371b147e194",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbBcuRWwEpKnjSVVXDSDn3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 12759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1987,
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

### Tool result

_source line 23 · 2026-05-13T04:58:56.046Z_

<details><summary>↩ Tool result · `toolu_01T7Fcm7RcqxYXkBd1QcgKsd`</summary>

```text
# Knowledge Insulation Paper Details

**Acceptance Status:** Yes, the paper was accepted to NeurIPS 2025.

**Presentation Venue:** The work was presented as a "Spotlight Poster" on Friday, December 5, 2025, from 4:30 PM – 7:30 PM PST in San Diego.

The page clearly identifies this as a "Spotlight Poster" presentation at the NeurIPS 2025 conference, indicating it received recognition as a notable contribution among the accepted papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31e24638-288c-4b60-8902-0371b147e194",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "351c0cee-56c1-441e-8e41-f6fd4cff7469",
  "sourceToolAssistantUUID": "31e24638-288c-4b60-8902-0371b147e194",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T04:58:58.942Z_

<details><summary>↩ Tool result · `toolu_01WMMXdg8HDHHYRNhtaDVshA`</summary>

```text
# Knowledge Insulation in Vision-Language-Action Models

## Technical Method: Gradient Insulation

The core innovation involves **stopping gradient flow from the action expert to the VLM backbone** during training. Specifically:

**Architecture Design:**
The method modifies attention mechanisms to prevent backpropagation through certain pathways. Using stop-gradient operators (sg), the authors implement:

> "sg denotes the stop-gradient operator that restricts gradient-flow through this part of the computation"

This is achieved by applying `sg(K_b(X_b)^T)` when action expert features attend to backbone features, and `sg(V_b(X_b))` in value computations. The attention matrix decomposes into separate blocks: backbone-to-backbone, action-to-backbone (with stopped gradients), and action-to-action interactions.

**Token Representation Preservation:**
The VLM backbone trains on **discretized action tokens** (using FAST tokenization) rather than continuous actions. This ensures the backbone receives a learning signal independent of the randomly-initialized action expert. Discrete tokens provide what the authors call "a substitute learning signal unaffected by the uninitialized weights of the action expert."

## Key Experimental Results

**Performance Benchmarks:**
- **LIBERO-90:** 96.0% success rate (state-of-the-art)
- **LIBERO-Spatial:** 98.0% success rate (state-of-the-art)
- **DROID:** 0.55±0.09 score versus π₀'s 0.49±0.09

**Real-World Tasks:**
- "Items in Drawer" (held-out environments): Substantially outperforms all baselines
- "Table Bussing": Achieves task completion with 2× faster inference than π₀-FAST
- Mobile manipulation tasks: Consistent improvements across four tasks

**Training Speed:**
The method trains "7.5 times" faster than π₀ (flow-matching only), achieving convergence speed comparable to π₀-FAST while maintaining superior language following.

**Language Following:**
Critical finding: models without gradient insulation (joint-training without stop-gradient) show significantly degraded ability to follow language instructions, measured through task-specific language comprehension tests.

## Co-Training Strategy

The approach combines three simultaneous objectives:
1. Autoregressive next-token prediction on **discretized actions**
2. Flow-matching loss on **continuous actions** (action expert)
3. General VLM data (image captioning, VQA, planning tasks)

The loss function prevents discrete action tokens from attending to continuous action tokens:

> "no discrete FAST action token can attend to continuous action tokens and vice-versa"

## Architectural Components—No Token Pruning Mentioned

The paper does **not discuss token pruning or masking approaches**. Instead, it uses attention masking to segregate information flow between modalities.

## Author Affiliations

**Physical Intelligence:**
- Danny Driess
- Jost Tobias Springenberg
- Brian Ichter
- Lili Yu
- Adrian Li-Bell
- Karl Pertsch
- Allen Z. Ren
- Homer Walke
- Quan Vuong
- Lucy Xiaoyang Shi
- Sergey Levine
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edf13c39-ed9c-43ee-9f5e-9e4192d7016f",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ad18a3361d14d917e",
  "type": "user",
  "uuid": "2ceeeefe-8d97-418f-93de-2fad0e9351c7",
  "sourceToolAssistantUUID": "edf13c39-ed9c-43ee-9f5e-9e4192d7016f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T04:59:36.696Z_

Now I have comprehensive information on both papers. Here is my report:

---

## Paper 1: "See What Matters" / GridS

**Status: CONFIRMED to exist.** Accepted at ICML 2026.

- **Full title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"
- **Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu
- **Venue:** ICML 2026 (poster: [https://icml.cc/virtual/2026/poster/65010](https://icml.cc/virtual/2026/poster/65010))

**Approach:** GridS is a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA models. Rather than discretely pruning/masking tokens (which discards critical geometric details like contact points), GridS adaptively predicts a minimal set of salient spatial coordinates and extracts features via differentiable bilinear interpolation. This reframes token compression as geometry-aware continuous resampling rather than binary keep/discard decisions.

**Key claims:** Achieves 76% FLOPs reduction with no degradation in success rate, using fewer than 10% of original visual tokens -- reportedly the lowest feasible visual token count to date. Validated on LIBERO benchmark and real robotic platforms.

**Relationship to token masking for VLA generalization:** This paper is a direct competitor in the VLA token efficiency space. It argues that conventional token pruning/masking methods create a destructive trade-off (aggressive masking kills geometric precision), and proposes continuous resampling as an alternative that avoids this problem while achieving more extreme compression.

---

## Paper 2: "Knowledge Insulating Vision-Language-Action Models"

**Status: CONFIRMED to exist.** arXiv 2505.23705 (May 29, 2025). Accepted as a **Spotlight Poster at NeurIPS 2025** (not just arXiv-only).

- **Full title:** "Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better"
- **Authors:** Danny Driess, Jost Tobias Springenberg, Brian Ichter, Lili Yu, Adrian Li-Bell, Karl Pertsch, Allen Z. Ren, Homer Walke, Quan Vuong, Lucy Xiaoyang Shi, Sergey Levine (all Physical Intelligence)
- **Pages:** [arXiv](https://arxiv.org/abs/2505.23705), [PI website](https://www.pi.website/research/knowledge_insulation), [NeurIPS 2025 poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/117079)

**Approach:** The paper identifies that naively grafting continuous action experts (diffusion/flow-matching heads) onto a pretrained VLM backbone causes harmful gradient flow that (a) slows training dramatically and (b) degrades the VLM's pretrained knowledge (especially language following). The solution -- "knowledge insulation" -- uses **stop-gradient operators** to block gradients from the action expert from flowing back into the VLM backbone. The VLM backbone instead trains on **discretized action tokens** (via FAST tokenization), providing a clean learning signal unaffected by the randomly-initialized action expert. A co-training strategy combines: (1) autoregressive next-token prediction on discrete actions, (2) flow-matching loss on continuous actions for the action expert, and (3) general VLM data (captioning, VQA, planning). Attention masking segregates discrete and continuous action token streams.

**Key results:** LIBERO-90: 96.0% success (SOTA); LIBERO-Spatial: 98.0% (SOTA); trains 7.5x faster than pi-zero; 2x faster inference than pi-zero-FAST; superior language-following ability compared to models without gradient insulation.

**Relationship to token masking for VLA generalization:** This paper does **not** do token pruning or masking in the visual-compression sense. Its contribution is orthogonal: it addresses how to preserve the VLM backbone's pretrained representations during VLA fine-tuning via gradient isolation. The "insulation" operates at the gradient/optimization level (stop-gradient on attention cross-paths), not at the token selection level. However, both papers share the overarching goal of preserving the quality of VLM representations when adapting to robotic action -- GridS does it by choosing which visual tokens to keep, while Knowledge Insulation does it by controlling which gradients can modify the backbone. They are complementary rather than directly competing approaches to VLA generalization, though both would be relevant competitors to any method that uses token-level masking to improve VLA efficiency and generalization.

---

Sources:
- [ICML 2026 Poster - See What Matters](https://icml.cc/virtual/2026/poster/65010)
- [arXiv 2505.23705 - Knowledge Insulating VLA Models](https://arxiv.org/abs/2505.23705)
- [arXiv HTML - Knowledge Insulation full paper](https://arxiv.org/html/2505.23705v1)
- [Physical Intelligence - Knowledge Insulation](https://www.pi.website/research/knowledge_insulation)
- [NeurIPS 2025 Poster - Knowledge Insulation](https://neurips.cc/virtual/2025/loc/san-diego/poster/117079)
- [Semantic Scholar - Knowledge Insulation](https://www.semanticscholar.org/paper/Knowledge-Insulating-Vision-Language-Action-Models:-Driess-Springenberg/f8a3331421b98c7d4065ecf55c4013e6306359f2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ceeeefe-8d97-418f-93de-2fad0e9351c7",
  "isSidechain": true,
  "agentId": "ad18a3361d14d917e",
  "requestId": "req_011CayydZrCRCdTF7jexVqDX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43091142-84d2-4cb8-b97c-d5ef00ee7d2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtZAY5JeBDngiXs44v8Ec7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 148,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 14746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1089,
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
