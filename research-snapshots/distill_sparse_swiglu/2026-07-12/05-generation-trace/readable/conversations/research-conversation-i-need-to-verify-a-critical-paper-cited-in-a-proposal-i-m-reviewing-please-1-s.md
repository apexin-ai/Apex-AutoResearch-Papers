# Research conversation: I need to verify a critical paper cited in a proposal I'm reviewing. Please: 1. Search for "Do You Need Proprioceptive S

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5867814a3548eb84.jsonl`
- **Structured JSON:** [`a00c3a19f0e82c0b2de6.json`](../../sessions/a0/a00c3a19f0e82c0b2de6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-13T19:43:00.393Z_

I need to verify a critical paper cited in a proposal I'm reviewing. Please:

1. Search for "Do You Need Proprioceptive States in Visuomotor Policies arXiv 2509.18644 Zhao" and verify it exists with the claimed findings (proprioception causes overfitting, removing it improved spatial generalization from 0% to 85%).

2. Then use WebFetch to read the abstract and key findings from https://arxiv.org/abs/2509.18644

3. Also search for "He et al Efficient Modality Selection Multimodal Learning JMLR 2024" to verify this paper exists and check whether the proposal adequately differentiates from it. The proposal claims He et al. addresses prediction loss not ranking accuracy, and submodularity doesn't transfer to ranking objectives - is this a fair characterization?

4. Search for "ThinkProprio think proprioceptively VLA manipulation arXiv 2602.06575" to verify it exists and check the claim that 15% of visual tokens suffice with proprioceptive integration.

Report all findings with specific details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a5867814a3548eb84",
  "type": "user",
  "uuid": "72651bc8-daf3-4415-8b8d-3e870f02ada6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:43:00.395Z_

```json
{
  "parentUuid": "72651bc8-daf3-4415-8b8d-3e870f02ada6",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
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
  "uuid": "ef186545-9bbe-49d3-a20b-89400d92580d",
  "timestamp": "2026-05-13T19:43:00.395Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:43:03.837Z_



I'll conduct these searches in parallel to verify all three papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef186545-9bbe-49d3-a20b-89400d92580d",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb193Hxwqj1hN4ttoDb5D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "378904cd-805b-4290-b1d0-457c9e799587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Ba7XAr3M6GqXsAu6cajXN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 797,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-13T19:43:04.116Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WyP6C6zhArCAzd3UM8VWsa`</summary>

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
  "parentUuid": "378904cd-805b-4290-b1d0-457c9e799587",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb193Hxwqj1hN4ttoDb5D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "297fb19b-ebf2-43c7-a4cb-fcd171e95082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Ba7XAr3M6GqXsAu6cajXN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 8223,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 797
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 797,
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

_source line 5 · 2026-05-13T19:43:04.122Z_

<details><summary>↩ Tool result · `toolu_01WyP6C6zhArCAzd3UM8VWsa`</summary>

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
  "parentUuid": "297fb19b-ebf2-43c7-a4cb-fcd171e95082",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a5867814a3548eb84",
  "type": "user",
  "uuid": "89061c7e-de06-46b6-b239-87ab2230cf69",
  "sourceToolAssistantUUID": "297fb19b-ebf2-43c7-a4cb-fcd171e95082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T19:43:09.318Z_



Now let me run all the searches and the WebFetch in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89061c7e-de06-46b6-b239-87ab2230cf69",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb193a2q5sEidhQBrTuHo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c261ae1-c839-45a5-8c8f-63befe233dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE8eL3EzToiQESZabA8DoU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1903,
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

_source line 7 · 2026-05-13T19:43:10.831Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QqXJx1wpBejgD55fpbz5Nz`</summary>

```json
{
  "query": "Do You Need Proprioceptive States in Visuomotor Policies arXiv 2509.18644 Zhao"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c261ae1-c839-45a5-8c8f-63befe233dde",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb193a2q5sEidhQBrTuHo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a09e8e6-8045-45a4-a2db-35624877bdd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE8eL3EzToiQESZabA8DoU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1903,
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

_source line 8 · 2026-05-13T19:43:11.890Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Twj2iZcLtAyhMFK9bTeGxL`</summary>

```json
{
  "query": "He et al Efficient Modality Selection Multimodal Learning JMLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a09e8e6-8045-45a4-a2db-35624877bdd6",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb193a2q5sEidhQBrTuHo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc75e7b2-7340-4161-a1fc-090baf9efabf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE8eL3EzToiQESZabA8DoU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1903,
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

_source line 9 · 2026-05-13T19:43:12.839Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018VFjKQFn17QqhifFEx7bX7`</summary>

```json
{
  "query": "ThinkProprio think proprioceptively VLA manipulation arXiv 2602.06575"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc75e7b2-7340-4161-a1fc-090baf9efabf",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb193a2q5sEidhQBrTuHo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a016d78-3f67-40b1-9b37-c2d8973a18b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE8eL3EzToiQESZabA8DoU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1903,
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

_source line 10 · 2026-05-13T19:43:15.301Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QFNd9vh1XP8VX7y7UGqPa8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.18644",
  "prompt": "Extract the full title, all authors, the complete abstract, and any key findings mentioned on this page. Specifically check: (1) Does the paper claim proprioception causes overfitting? (2) Does it report that removing proprioception improved spatial generalization from 0% to 85%? Report all specific numbers and claims mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a016d78-3f67-40b1-9b37-c2d8973a18b3",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb193a2q5sEidhQBrTuHo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a72a2355-4a51-4091-8f8c-d8c1b650090c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE8eL3EzToiQESZabA8DoU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 9020,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 9020,
          "cache_creation_input_tokens": 1903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1903,
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

_source line 11 · 2026-05-13T19:43:17.891Z_

<details><summary>↩ Tool result · `toolu_01QqXJx1wpBejgD55fpbz5Nz`</summary>

```text
Web search results for query: "Do You Need Proprioceptive States in Visuomotor Policies arXiv 2509.18644 Zhao"

Links: [{"title":"[2509.18644] Do You Need Proprioceptive States in Visuomotor Policies?","url":"https://arxiv.org/abs/2509.18644"},{"title":"Do You Need Proprioceptive States in Visuomotor Policies?","url":"https://statefreepolicy.github.io/"},{"title":"Do You Need Proprioceptive States in Visuomotor Policies?","url":"https://arxiv.org/html/2509.18644v1"},{"title":"[2509.18644v1] Do You Need Proprioceptive States in Visuomotor Policies?","url":"https://arxiv.org/abs/2509.18644v1"},{"title":"[2509.18644v2] Do You Need Proprioceptive States in Visuomotor Policies?","url":"https://arxiv.org/abs/2509.18644v2"},{"title":"Paper page - Do You Need Proprioceptive States in Visuomotor Policies?","url":"https://huggingface.co/papers/2509.18644"},{"title":"Do You Need Proprioceptive States in Visuomotor Policies? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/do-you-need-proprioceptive-states-visuomotor-policies"},{"title":"DextrAH-RGB: Visuomotor Policies to Grasp Anything with Dexterous Hands","url":"https://arxiv.org/html/2412.01791v1"},{"title":"Adapting by Analogy: OOD Generalization of Visuomotor Policies via Functional Correspondence","url":"https://arxiv.org/html/2506.12678v1"},{"title":"Referring-Aware Visuomotor Policy Learning for Closed-Loop Manipulation","url":"https://arxiv.org/html/2604.05544v1"}]

I found the paper! Here are the key details about "Do You Need Proprioceptive States in Visuomotor Policies?" (arXiv 2509.18644):

## Overview
Imitation-learning-based visuomotor policies have been widely used in robot manipulation, where both visual observations and proprioceptive states are typically adopted together for precise control.

## Main Finding
However, in this study, the authors find that this common practice makes the policy overly reliant on the proprioceptive state input, which causes overfitting to the training trajectories and results in poor spatial generalization.

## Proposed Solution
The paper proposes the State-free Policy, removing the proprioceptive state input and predicting actions only conditioned on visual observations. The State-free Policy is built in the relative end-effector action space, and should ensure the full task-relevant visual observations, here provided by dual wide-angle wrist cameras.

## Key Results
Empirical results demonstrate that the State-free policy achieves significantly stronger spatial generalization than the state-based policy: in real-world tasks such as pick-and-place, challenging shirt-folding, and complex whole-body manipulation, spanning multiple robot embodiments, the average success rate improves from 0% to 85% in height generalization and from 6% to 64% in horizontal generalization.

## Authors
The paper is authored by Juntu Zhao and 12 other co-authors from institutions including Shanghai Jiao Tong University, Spirit AI, Tsinghua University, New York University Shanghai, and Tongji University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a09e8e6-8045-45a4-a2db-35624877bdd6",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a5867814a3548eb84",
  "type": "user",
  "uuid": "b5417d45-0fed-404b-b29a-4df6fffbd455",
  "sourceToolAssistantUUID": "7a09e8e6-8045-45a4-a2db-35624877bdd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T19:43:20.064Z_

<details><summary>↩ Tool result · `toolu_018VFjKQFn17QqhifFEx7bX7`</summary>

```text
Web search results for query: "ThinkProprio think proprioceptively VLA manipulation arXiv 2602.06575"

Links: [{"title":"[2602.06575] Think Proprioceptively: Embodied Visual Reasoning for VLA Manipulation","url":"https://arxiv.org/abs/2602.06575"},{"title":"(PDF) Think Proprioceptively: Embodied Visual Reasoning for VLA Manipulation","url":"https://www.researchgate.net/publication/400583452_Think_Proprioceptively_Embodied_Visual_Reasoning_for_VLA_Manipulation"},{"title":"Think Proprioceptively: Embodied Visual Reasoning for VLA Manipulation","url":"https://arxiv.org/html/2602.06575"},{"title":"ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning","url":"https://jasper0314-huang.github.io/thinkact-vla/"},{"title":"David NAVARRO-ALARCON | Professor (Associate) | Doctor of Philosophy | The Hong Kong Polytechnic University, Hong Kong | PolyU | Department of Mechanical Engineering | Research profile","url":"https://www.researchgate.net/profile/David-Navarro-Alarcon"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers","url":"https://arxiv.org/html/2409.20537v1"},{"title":"WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control | OpenReview","url":"https://openreview.net/forum?id=OCJmVjyzN7"}]

I found the research paper you're looking for. Here's a summary of ThinkProprio:

## Overview

ThinkProprio converts proprioception into a sequence of text tokens in the VLM embedding space and fuses them with the task instruction at the input.

## Problem Addressed

Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, which prevents robot state from shaping instruction understanding and from influencing which visual tokens are attended throughout the policy.

## Key Innovation

Early fusion lets embodied state participate in subsequent visual reasoning and token selection, biasing computation toward action-critical evidence while suppressing redundant visual tokens.

## Results

In a systematic ablation over proprioception encoding, state entry point, and action-head conditioning, we find that text tokenization is more effective than learned projectors, and that retaining roughly 15% of visual tokens can match the performance of using the full token set.

Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio matches or improves over strong baselines while reducing end-to-end inference latency over 50%.

The paper was submitted to arXiv on February 6, 2026, and is authored by Fangyuan Wang, Peng Zhou, Jiaming Qi, Shipeng Lyu, David Navarro-Alarcon, and Guodong Guo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a016d78-3f67-40b1-9b37-c2d8973a18b3",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a5867814a3548eb84",
  "type": "user",
  "uuid": "f9026b91-588a-41d8-85ef-f657072b55ee",
  "sourceToolAssistantUUID": "7a016d78-3f67-40b1-9b37-c2d8973a18b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T19:43:20.763Z_

<details><summary>↩ Tool result · `toolu_01QFNd9vh1XP8VX7y7UGqPa8`</summary>

```text
# Paper Analysis: "Do You Need Proprioceptive States in Visuomotor Policies?"

## Full Title
"Do You Need Proprioceptive States in Visuomotor Policies?"

## Authors
Juntu Zhao, Wenbo Lu, Di Zhang, Yufeng Liu, Yushen Liang, Tianluo Zhang, Yifeng Cao, Junyuan Xie, Yingdong Hu, Shengjie Wang, Junliang Guo, Dequan Wang, Yang Gao

## Complete Abstract
The researchers investigate whether combining visual observations with proprioceptive state data—standard practice in robotic manipulation—is optimal. They argue this approach creates "overly reliant on the proprioceptive state input, which causes overfitting to the training trajectories."

They propose the State-free Policy using only visual observations in relative end-effector action space with dual wide-angle wrist cameras.

## Key Findings

**(1) Proprioception and Overfitting Claim:** YES
The abstract explicitly states the common practice "causes overfitting to the training trajectories and results in poor spatial generalization."

**(2) Spatial Generalization Improvements:** YES
Reported improvements across multiple metrics:
- Height generalization: 0% to 85% success rate
- Horizontal generalization: 6% to 64% success rate

**Additional advantages noted:** Data efficiency and cross-embodiment adaptation improvements

**Tasks demonstrated:** Pick-and-place, shirt-folding, whole-body manipulation across multiple robot embodiments
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a72a2355-4a51-4091-8f8c-d8c1b650090c",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a5867814a3548eb84",
  "type": "user",
  "uuid": "86ee6ecd-4288-4dba-a5bb-857937c9f939",
  "sourceToolAssistantUUID": "a72a2355-4a51-4091-8f8c-d8c1b650090c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T19:43:22.484Z_

<details><summary>↩ Tool result · `toolu_01Twj2iZcLtAyhMFK9bTeGxL`</summary>

```text
Web search results for query: "He et al Efficient Modality Selection Multimodal Learning JMLR 2024"

Links: [{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://jmlr.org/papers/v25/23-0439.html"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://sampalomad.github.io/paper/he2024efficient.pdf"},{"title":"Efficient Modality Selection in Multimodal Learning","url":"https://www.jmlr.org/papers/volume25/23-0439/23-0439.pdf"},{"title":"Efficient modality selection in multimodal learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3722577.3722624"},{"title":"Journal of Machine Learning Research on X: \"'Efficient Modality Selection in Multimodal Learning', by Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, Han Zhao. https://t.co/K7o2CBIlit #multimodal #modality #modalities\" / X","url":"https://x.com/JmlrOrg/status/1767657167190933840"},{"title":"Efficient modality selection in multimodal learning","url":"https://dl.acm.org/doi/pdf/10.5555/3722577.3722624"},{"title":"dblp: Journal of Machine Learning Research, Volume 25","url":"https://dblp.org/db/journals/jmlr/jmlr25.html"},{"title":"A survey on knowledge-enhanced multimodal learning | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-024-10825-z"},{"title":"Robust Multimodal Learning With Missing Modalities via ...","url":"https://www.computer.org/csdl/journal/tp/2025/02/10713849/20VwC7hALjq"},{"title":"Journal of Machine Learning Research","url":"https://twitter.com/JmlrOrg/status/1767657167190933840"}]

I found the paper you're looking for. Here's what the search revealed:

"Efficient Modality Selection in Multimodal Learning" was published in JMLR 2024 by authors Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, and Han Zhao.

## Paper Summary

The paper addresses multimodal learning, which aims to learn from data of different modalities by fusing information from heterogeneous sources, but notes that using all available modalities is often infeasible under limited computational resources.

**Key Contributions:**

- The authors derive a greedy modality selection algorithm via submodular maximization, which selects the most useful modalities with an optimality guarantee on learning performance.

- They connect marginal-contribution-based feature importance scores, such as Shapley value, from the feature selection domain to the context of modality selection, to efficiently compute the importance of individual modality.

- In classification with cross-entropy loss, a modality's utility is quantified as the Shannon mutual information between the modality and the target; in regression with quadratic loss, the utility is quantified as the variance of the conditional expectation of the target given the modality.

- The authors demonstrate the efficacy of their theoretical results and modality selection algorithms on 2 synthetic and 4 real-world data sets on a diverse range of multimodal data.

The paper is published in Journal of Machine Learning Research, Volume 25, Issue 1, January 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc75e7b2-7340-4161-a1fc-090baf9efabf",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a5867814a3548eb84",
  "type": "user",
  "uuid": "fff673b8-3b77-4f0a-81e9-44b3714bdf8b",
  "sourceToolAssistantUUID": "fc75e7b2-7340-4161-a1fc-090baf9efabf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-13T19:43:25.812Z_

Now let me fetch more details on the He et al. paper to verify the proposal's characterization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff673b8-3b77-4f0a-81e9-44b3714bdf8b",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb194vUfw5Wpmg2AnZUux",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fff1b2dd-d3d0-4927-b77b-4bc83fae2f0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjefsZtv7iveg5nrLT3Q4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1308,
      "cache_creation_input_tokens": 2217,
      "cache_read_input_tokens": 10923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2217,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 16 · 2026-05-13T19:43:30.398Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vq596FvgdDVuBv1Fwta9MK`</summary>

```json
{
  "url": "https://jmlr.org/papers/v25/23-0439.html",
  "prompt": "Extract the full abstract and key details about this paper. Specifically: (1) What is the objective function or loss used - is it prediction loss or ranking accuracy? (2) Does the paper use submodularity? If so, for what specific objective? (3) Does the paper address ranking tasks or only classification/regression? (4) What are the theoretical guarantees and do they rely on submodularity of a specific loss function? Report all specific details about the problem formulation and theoretical framework."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff1b2dd-d3d0-4927-b77b-4bc83fae2f0b",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb194vUfw5Wpmg2AnZUux",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1197e37c-fc8c-4b76-a1bd-e4cc151d83dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjefsZtv7iveg5nrLT3Q4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1308,
      "cache_creation_input_tokens": 2217,
      "cache_read_input_tokens": 10923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2217,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 17 · 2026-05-13T19:43:32.045Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XFkdTZXCm9B2Nynj2mb2aR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.06575",
  "prompt": "Extract the full abstract, all authors, and key findings. Specifically check: (1) Does the paper claim that 15% of visual tokens suffice with proprioceptive integration? (2) What exactly is said about visual token reduction? (3) What are the specific performance numbers on CALVIN, LIBERO, and real-world tasks? Report all specific numbers and claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1197e37c-fc8c-4b76-a1bd-e4cc151d83dc",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb194vUfw5Wpmg2AnZUux",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6fe2dc0-7c3a-4155-8d10-9117e49f1606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjefsZtv7iveg5nrLT3Q4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1308,
      "cache_creation_input_tokens": 2217,
      "cache_read_input_tokens": 10923,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2217
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1308,
          "output_tokens": 359,
          "cache_read_input_tokens": 10923,
          "cache_creation_input_tokens": 2217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2217,
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

_source line 18 · 2026-05-13T19:43:33.906Z_

<details><summary>↩ Tool result · `toolu_01Vq596FvgdDVuBv1Fwta9MK`</summary>

```text
# Analysis of "Efficient Modality Selection in Multimodal Learning"

## Objective Function
The paper does not specify a particular loss function (prediction loss or ranking accuracy) in the abstract. It focuses on selecting "the most useful subset of modalities for learning under a cardinality constraint" rather than defining a specific loss formulation.

## Submodularity Usage
Yes, the paper explicitly employs submodularity. The authors "derive a greedy modality selection algorithm via submodular maximization, which selects the most useful modalities with an optimality guarantee on learning performance."

## Task Type
The paper addresses **classification and regression tasks only**. The abstract mentions evaluation on "synthetic and 4 real-world data sets on a diverse range of multimodal data" but does not reference ranking tasks specifically.

## Theoretical Framework & Guarantees
The framework includes:
- A "unified theoretical framework to quantify the learning utility of modalities"
- "Dependence assumptions to flexibly model the heterogeneous nature of multimodal data, which also allows efficient algorithm design"
- Optimality guarantees derived through submodular maximization
- Connection to "marginal-contribution-based feature importance scores, such as Shapley value" for computing individual modality importance

The theoretical guarantees appear linked to the submodular maximization approach rather than a specific loss function's submodularity properties.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1197e37c-fc8c-4b76-a1bd-e4cc151d83dc",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a5867814a3548eb84",
  "type": "user",
  "uuid": "d7b85a86-312b-400a-aeab-b3db567b7767",
  "sourceToolAssistantUUID": "1197e37c-fc8c-4b76-a1bd-e4cc151d83dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T19:43:38.388Z_

<details><summary>↩ Tool result · `toolu_01XFkdTZXCm9B2Nynj2mb2aR`</summary>

```text
# Paper Summary: Think Proprioceptively

## Full Abstract
"Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, which prevents robot state from shaping instruction understanding and from influencing which visual tokens are attended throughout the policy. We introduce ThinkProprio, which converts proprioception into a sequence of text tokens in the VLM embedding space and fuses them with the task instruction at the input. This early fusion lets embodied state participate in subsequent visual reasoning and token selection, biasing computation toward action-critical evidence while suppressing redundant visual tokens. In a systematic ablation over proprioception encoding, state entry point, and action-head conditioning, we find that text tokenization is more effective than learned projectors, and that retaining roughly 15% of visual tokens can match the performance of using the full token set. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio matches or improves over strong baselines while reducing end-to-end inference latency over 50%."

## Authors
Fangyuan Wang, Peng Zhou, Jiaming Qi, Shipeng Lyu, David Navarro-Alarcon, Guodong Guo

## Key Findings Analysis

**(1) 15% Visual Token Claim:**
Yes, confirmed. The abstract explicitly states "retaining roughly 15% of visual tokens can match the performance of using the full token set."

**(2) Visual Token Reduction Details:**
The mechanism involves converting proprioceptive state into text tokens fused early with task instructions, enabling the model to bias computation toward "action-critical evidence while suppressing redundant visual tokens."

**(3) Performance Numbers:**
The webpage provides **no specific quantitative results** for CALVIN, LIBERO, or real-world tasks. It only states the approach "matches or improves over strong baselines" and reduces "inference latency over 50%."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6fe2dc0-7c3a-4155-8d10-9117e49f1606",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a5867814a3548eb84",
  "type": "user",
  "uuid": "14f4337d-80e3-4c27-9e25-9df00d17bec3",
  "sourceToolAssistantUUID": "e6fe2dc0-7c3a-4155-8d10-9117e49f1606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-13T19:44:07.759Z_

Here are the complete verification findings for all three papers:

---

## Paper 1: "Do You Need Proprioceptive States in Visuomotor Policies?" (arXiv 2509.18644)

**Status: VERIFIED -- exists and claims match.**

- **Authors:** Juntu Zhao, Wenbo Lu, Di Zhang, Yufeng Liu, Yushen Liang, Tianluo Zhang, Yifeng Cao, Junyuan Xie, Yingdong Hu, Shengjie Wang, Junliang Guo, Dequan Wang, Yang Gao
- **Affiliations:** Shanghai Jiao Tong University, Spirit AI, Tsinghua University, NYU Shanghai, Tongji University
- **Proprioception causes overfitting claim:** Confirmed. The abstract explicitly states that including proprioceptive state input "causes overfitting to the training trajectories and results in poor spatial generalization."
- **0% to 85% spatial generalization claim:** Confirmed, but this specifically refers to **height generalization**. The paper also reports horizontal generalization improved from 6% to 64%. The proposal's citation of "0% to 85%" is accurate but should ideally specify it is height generalization, not all spatial generalization combined.
- **Tasks demonstrated:** Pick-and-place, shirt-folding, whole-body manipulation across multiple robot embodiments.

---

## Paper 2: "Efficient Modality Selection in Multimodal Learning" (He et al., JMLR 2024)

**Status: VERIFIED -- exists. The proposal's characterization is largely fair but could be more nuanced.**

- **Authors:** Yifei He, Runxiang Cheng, Gargi Balasubramaniam, Yao-Hung Hubert Tsai, Han Zhao
- **Published in:** Journal of Machine Learning Research, Volume 25, 2024
- **Key framework:** The paper derives a greedy modality selection algorithm via submodular maximization with optimality guarantees.
- **Regarding the proposal's characterization:**
  - **"Addresses prediction loss not ranking accuracy"** -- **Fair.** The paper formulates modality utility for classification (cross-entropy loss / Shannon mutual information) and regression (quadratic loss / conditional variance). It does not address ranking objectives at all.
  - **"Submodularity doesn't transfer to ranking objectives"** -- **Reasonable but unproven.** The paper's theoretical guarantees are indeed grounded in submodularity of specific loss-based utility functions (mutual information for classification, variance for regression). Ranking losses (e.g., pairwise losses, NDCG surrogates) have different mathematical structure, so the claim that submodularity guarantees don't straightforwardly transfer is plausible. However, this is an assertion by the proposal authors -- there is no formal proof cited that submodularity *cannot* apply to ranking. The proposal should acknowledge this is a gap in existing theory rather than a proven impossibility.

---

## Paper 3: "Think Proprioceptively: Embodied Visual Reasoning for VLA Manipulation" (arXiv 2602.06575)

**Status: VERIFIED -- exists and the 15% claim matches.**

- **Authors:** Fangyuan Wang, Peng Zhou, Jiaming Qi, Shipeng Lyu, David Navarro-Alarcon, Guodong Guo
- **Submitted:** February 2026
- **15% visual tokens claim:** Confirmed. The abstract explicitly states "retaining roughly 15% of visual tokens can match the performance of using the full token set."
- **Mechanism:** ThinkProprio converts proprioception into text tokens in the VLM embedding space and fuses them early with task instructions. This early fusion allows proprioceptive state to shape visual attention, suppressing redundant visual tokens.
- **Additional results:** Matches or improves over strong baselines across CALVIN, LIBERO, and real-world manipulation while reducing end-to-end inference latency by over 50%.

---

## Summary Assessment

All three papers exist and are real. The specific numerical claims cited in the proposal (0% to 85% generalization for Zhao et al.; 15% visual tokens for ThinkProprio) are accurately reported. The one area warranting scrutiny is the proposal's differentiation from He et al.: while the characterization that He et al. addresses prediction loss rather than ranking is factually correct, the stronger claim that "submodularity doesn't transfer to ranking objectives" is plausible but should be framed as a theoretical gap rather than a definitive limitation, since no formal impossibility result is cited.

Sources:
- [Do You Need Proprioceptive States in Visuomotor Policies? (arXiv)](https://arxiv.org/abs/2509.18644)
- [State-free Policy Project Page](https://statefreepolicy.github.io/)
- [Efficient Modality Selection in Multimodal Learning (JMLR)](https://jmlr.org/papers/v25/23-0439.html)
- [Think Proprioceptively (arXiv)](https://arxiv.org/abs/2602.06575)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14f4337d-80e3-4c27-9e25-9df00d17bec3",
  "isSidechain": true,
  "agentId": "a5867814a3548eb84",
  "requestId": "req_011Cb1966TjE1nnppoztsVrj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6ed33d5-bcee-4087-8b08-62a2717fb450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhL7tjxoW2WKwdECC1qdzo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2468,
      "cache_read_input_tokens": 13140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2468,
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
