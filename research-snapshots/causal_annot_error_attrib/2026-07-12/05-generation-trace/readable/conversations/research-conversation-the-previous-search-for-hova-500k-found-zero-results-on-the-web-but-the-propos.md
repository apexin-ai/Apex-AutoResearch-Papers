# Research conversation: The previous search for "HOVA-500K" found zero results on the web. But the proposal claims HOVA-500K comes from the GLOV

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a38c2c1b9b5a75841.jsonl`
- **Structured JSON:** [`77dcd8057b626f733f0a.json`](../../sessions/77/77dcd8057b626f733f0a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-18T19:28:56.175Z_

The previous search for "HOVA-500K" found zero results on the web. But the proposal claims HOVA-500K comes from the GLOVER++ paper (arXiv 2505.11865, CoRL 2025). It's possible the dataset name is internal to the paper and not separately indexed.

Use WebFetch to read https://arxiv.org/abs/2505.11865 and search for:
1. Does the paper mention "HOVA-500K" by that exact name?
2. What is the actual dataset name and scale described in the paper?
3. Is the dataset publicly available?

Also try WebSearch for "GLOVER++ dataset affordance" and "GLOVER++ HOVA" to cross-check.

Report under 150 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a38c2c1b9b5a75841",
  "type": "user",
  "uuid": "c43f1150-f431-44b8-bbb2-8c5a440029ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T19:28:56.180Z_

```json
{
  "parentUuid": "c43f1150-f431-44b8-bbb2-8c5a440029ef",
  "isSidechain": true,
  "agentId": "a38c2c1b9b5a75841",
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
      "TodoWrite",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b65aa9fb-b9c3-45fe-ae45-cb3b8259f2e2",
  "timestamp": "2026-05-18T19:28:56.180Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T19:28:58.816Z_



Let me load the WebFetch and WebSearch tool schemas first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b65aa9fb-b9c3-45fe-ae45-cb3b8259f2e2",
  "isSidechain": true,
  "agentId": "a38c2c1b9b5a75841",
  "requestId": "req_011CbAb1e89jh2KoTC1WrKas",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43269d70-d130-4e4f-be3b-cc3b1854f00a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016W8Y6U7ag1jcBrwb22Cjri",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 730,
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

_source line 4 · 2026-05-18T19:28:58.902Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018T1AMLfnTWoUuPSV96qctJ`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43269d70-d130-4e4f-be3b-cc3b1854f00a",
  "isSidechain": true,
  "agentId": "a38c2c1b9b5a75841",
  "requestId": "req_011CbAb1e89jh2KoTC1WrKas",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c70ba23b-5c63-4d7a-a54f-2cc9c9c63daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016W8Y6U7ag1jcBrwb22Cjri",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 730,
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

### Tool result

_source line 5 · 2026-05-18T19:28:58.906Z_

<details><summary>↩ Tool result · `toolu_018T1AMLfnTWoUuPSV96qctJ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "c70ba23b-5c63-4d7a-a54f-2cc9c9c63daf",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a38c2c1b9b5a75841",
  "type": "user",
  "uuid": "7b3a7bed-ea4f-400d-b70d-bed197dd8d3c",
  "sourceToolAssistantUUID": "c70ba23b-5c63-4d7a-a54f-2cc9c9c63daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T19:29:02.737Z_



Now let me fetch the arXiv page and run the web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b3a7bed-ea4f-400d-b70d-bed197dd8d3c",
  "isSidechain": true,
  "agentId": "a38c2c1b9b5a75841",
  "requestId": "req_011CbAb1qyYCDa4gGZwWgiZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82ae28be-d089-4d13-a110-db6aa551f27f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5MdoHCLK49D1zmu1DxtFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 7 · 2026-05-18T19:29:05.717Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019oSwcoFhrHE62DKyFvSyYC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.11865",
  "prompt": "Search the full page for: 1) Any mention of \"HOVA-500K\" exactly. 2) What dataset name and scale (number of samples) is described in this paper? 3) Is the dataset publicly available or released? 4) What is the paper's title and what does it cover? Report all dataset-related details you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82ae28be-d089-4d13-a110-db6aa551f27f",
  "isSidechain": true,
  "agentId": "a38c2c1b9b5a75841",
  "requestId": "req_011CbAb1qyYCDa4gGZwWgiZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d66e3143-71cf-4dd7-a231-2fefa7f6151f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5MdoHCLK49D1zmu1DxtFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 8 · 2026-05-18T19:29:05.795Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011kAqxyVV2bPNjnWqwDnuQn`</summary>

```json
{
  "query": "GLOVER++ dataset affordance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d66e3143-71cf-4dd7-a231-2fefa7f6151f",
  "isSidechain": true,
  "agentId": "a38c2c1b9b5a75841",
  "requestId": "req_011CbAb1qyYCDa4gGZwWgiZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d95a89a-8ac6-4c89-bd2f-19530b6a0039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5MdoHCLK49D1zmu1DxtFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 9 · 2026-05-18T19:29:05.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014mm6R8YQx862rBHNuvz5fw`</summary>

```json
{
  "query": "GLOVER++ HOVA dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d95a89a-8ac6-4c89-bd2f-19530b6a0039",
  "isSidechain": true,
  "agentId": "a38c2c1b9b5a75841",
  "requestId": "req_011CbAb1qyYCDa4gGZwWgiZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99b96a0b-f3d0-4684-93f8-7f643f03f0cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5MdoHCLK49D1zmu1DxtFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

### Tool result

_source line 10 · 2026-05-18T19:29:09.494Z_

<details><summary>↩ Tool result · `toolu_019oSwcoFhrHE62DKyFvSyYC`</summary>

```text
# Dataset Analysis: GLOVER++ Paper

## 1. HOVA-500K Mentions
Yes, "HOVA-500K" is mentioned exactly multiple times throughout the abstract and document.

## 2. Dataset Details
The paper introduces **HOVA-500K**, described as a large-scale, affordance-annotated dataset containing:
- **500,000 images**
- **1,726 object categories**
- **675 actions**

## 3. Public Availability
The abstract states the authors "release" both the dataset and benchmarking suite, suggesting public availability, though specific access details aren't provided on this arXiv page.

## 4. Paper Title and Coverage
**Title:** "GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation"

**Coverage:** The paper addresses learning robotic manipulation skills from human demonstration videos through actionable affordances. It tackles challenges including "lack of large-scale datasets with precise affordance annotations" and develops a global-to-local training framework for knowledge transfer to robotic tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d66e3143-71cf-4dd7-a231-2fefa7f6151f",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a38c2c1b9b5a75841",
  "type": "user",
  "uuid": "1c259f31-cd26-4776-bdc9-100cf7ca5063",
  "sourceToolAssistantUUID": "d66e3143-71cf-4dd7-a231-2fefa7f6151f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T19:29:10.201Z_

<details><summary>↩ Tool result · `toolu_011kAqxyVV2bPNjnWqwDnuQn`</summary>

```text
Web search results for query: "GLOVER++ dataset affordance"

Links: [{"title":"GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=HT34hQcU91"},{"title":"[2505.11865] GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation","url":"https://arxiv.org/abs/2505.11865"},{"title":"(PDF) GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation","url":"https://www.researchgate.net/publication/391876906_GLOVER_Unleashing_the_Potential_of_Affordance_Learning_from_Human_Behaviors_for_Robotic_Manipulation"},{"title":"GLOVER++ | Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation","url":"https://teleema.github.io/projects/GLOVER++/"},{"title":"GLOVER++: Unleashing the Potential of Affordance ...","url":"https://arxiv.org/pdf/2505.11865"},{"title":"GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/glover-unleashing-potential-affordance-learning-human-behaviors"},{"title":"Zifan Wang","url":"https://www.catalyzex.com/author/Zifan%20Wang"},{"title":"GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation","url":"https://arxiv.org/html/2505.11865v1"},{"title":"Jia Zheng","url":"https://www.catalyzex.com/author/Jia%20Zheng"}]

Based on the search results, here's what I found about the GLOVER++ dataset and affordance learning:

## GLOVER++ Overview

GLOVER++ is a global-to-local affordance training framework built upon HOVA-500K that effectively transfers actionable affordance knowledge from human demonstrations to downstream open-vocabulary reasoning tasks.

## HOVA-500K Dataset

HOVA-500K is a large-scale, affordance-annotated dataset comprising 500,000 images across 1,726 object categories and 675 actions. The dataset offers three key advantages: 1) its unprecedented scale in terms of images and object/action categories enables large-scale affordance training, 2) the diversity of scenarios and views ensures broad coverage of real-world interaction contexts, 3) precise annotation of affordable points eliminates the ambiguity of the mask/region boundary and aligns better with robotic execution.

## Performance and Applications

GLOVER++ achieves state-of-the-art results on the HOVA-500K benchmark and demonstrates strong generalization across diverse downstream robotic manipulation tasks. By explicitly modeling actionable affordances, GLOVER++ facilitates robust transfer across scenes, modalities, and tasks.

The framework is designed to address the challenge of learning generalizable robotic manipulation skills from human demonstrations by focusing on actionable affordances—the specific ways objects can be interacted with for manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d95a89a-8ac6-4c89-bd2f-19530b6a0039",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a38c2c1b9b5a75841",
  "type": "user",
  "uuid": "4a983f67-7e45-4eb9-9b6e-75ee2143889c",
  "sourceToolAssistantUUID": "3d95a89a-8ac6-4c89-bd2f-19530b6a0039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T19:29:11.559Z_

<details><summary>↩ Tool result · `toolu_014mm6R8YQx862rBHNuvz5fw`</summary>

```text
Web search results for query: "GLOVER++ HOVA dataset"

Links: [{"title":"GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=HT34hQcU91"},{"title":"GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/glover-unleashing-potential-affordance-learning-human-behaviors"},{"title":"GLOVER++ | Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation","url":"https://teleema.github.io/projects/GLOVER++/"},{"title":"GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation","url":"https://arxiv.org/html/2505.11865v1"},{"title":"GLOVER++: Unleashing the Potential of Affordance ...","url":"https://arxiv.org/pdf/2505.11865"},{"title":"[2505.11865] GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation","url":"https://arxiv.org/abs/2505.11865"},{"title":"GitHub - TeleeMa/GLOVER: This is the official code repo for GLOVER and GLOVER++.","url":"https://github.com/TeleeMa/GLOVER"},{"title":"(PDF) GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation","url":"https://www.researchgate.net/publication/391876906_GLOVER_Unleashing_the_Potential_of_Affordance_Learning_from_Human_Behaviors_for_Robotic_Manipulation"}]

Based on the search results, here's what I found about GLOVER++ and the HOVA dataset:

## GLOVER++ and HOVA-500K Dataset

HOVA-500K is a large-scale, affordance-annotated dataset comprising 500,000 images across 1,726 object categories and 675 actions.

GLOVER++ is a global-to-local affordance training framework that effectively transfers actionable affordance knowledge from human demonstrations to downstream open-vocabulary reasoning tasks.

### Key Features:

HOVA-500K offers three key advantages: 1) its unprecedented scale in terms of images and object/action categories enables large-scale affordance training, 2) the diversity of scenarios and views ensures broad coverage of real-world interaction contexts, 3) precise annotation of affordable points eliminates the ambiguity of the mask/region boundary and aligns better with robotic execution.

### Applications:

GLOVER++ demonstrates potential in diverse tasks, including zero-shot manipulation, imitation learning, long-horizon and bimanual manipulation. Thanks to its spatial reasoning capabilities, GLOVER++ can interpret positional cues (e.g., "left/right", "top/bottom") to enable dual-arm affordance reasoning.

The project appears to be a recent research contribution aimed at improving robotic manipulation by learning from human demonstrations, with comprehensive code and dataset resources made publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99b96a0b-f3d0-4684-93f8-7f643f03f0cf",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a38c2c1b9b5a75841",
  "type": "user",
  "uuid": "dadd8400-5e33-4053-8548-6adbf13c0f63",
  "sourceToolAssistantUUID": "99b96a0b-f3d0-4684-93f8-7f643f03f0cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-18T19:29:18.539Z_

Here is the report:

**HOVA-500K is real and confirmed.** The arXiv paper (2505.11865) titled "GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation" introduces HOVA-500K by that exact name. It is a large-scale affordance-annotated dataset of 500,000 images spanning 1,726 object categories and 675 actions, with precise "affordable point" annotations. The authors state they release the dataset and benchmarking suite publicly; an official GitHub repo exists at [TeleeMa/GLOVER](https://github.com/TeleeMa/GLOVER). The earlier web search likely returned zero results because the name is specific to this paper and not a standalone, separately indexed resource. The proposal's citation of HOVA-500K from the GLOVER++ paper checks out.

Sources:
- [arXiv 2505.11865](https://arxiv.org/abs/2505.11865)
- [OpenReview](https://openreview.net/forum?id=HT34hQcU91)
- [Project page](https://teleema.github.io/projects/GLOVER++/)
- [GitHub repo](https://github.com/TeleeMa/GLOVER)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dadd8400-5e33-4053-8548-6adbf13c0f63",
  "isSidechain": true,
  "agentId": "a38c2c1b9b5a75841",
  "requestId": "req_011CbAb2msWeTZaS6VFisyGC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb6ba322-334f-4c24-be0e-23880243a528",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fxb8VagPvxKsKGY3ZSnxcQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2212,
      "cache_read_input_tokens": 10857,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2212
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 10857,
          "cache_creation_input_tokens": 2212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2212,
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
