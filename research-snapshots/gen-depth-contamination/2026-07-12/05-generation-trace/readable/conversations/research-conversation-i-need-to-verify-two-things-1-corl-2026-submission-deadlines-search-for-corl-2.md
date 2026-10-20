# Research conversation: I need to verify two things: 1. **CoRL 2026 submission deadlines** - Search for "CoRL 2026 submission deadline" or "CoRL

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aab29a10692718339.jsonl`
- **Structured JSON:** [`c644d1009b680dc19f8a.json`](../../sessions/c6/c644d1009b680dc19f8a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-10T19:37:11.439Z_

I need to verify two things:

1. **CoRL 2026 submission deadlines** - Search for "CoRL 2026 submission deadline" or "CoRL 2026 call for papers". The proposal claims abstract deadline May 26, paper deadline May 29, 2026, conference in Austin Nov 9-12.

2. **Being-H0.7** (arXiv 2605.00078, May 2026) - "Being-H0.7: A Latent World-Action Model from Egocentric Videos". Claims: latent queries at 3-4ms/step, no video generation, 99.2% on LIBERO, drops to 82.1% on LIBERO-Plus under distributional shift. Verify this paper exists and check the specific claims.

3. **Fast-WAM** (arXiv 2603.16666, March 2026) - Claims competitive results without test-time video generation. Verify existence.

4. **WorldCache** (arXiv 2603.06331, March 2026) - Claims 3.7x speedup for world models via heterogeneous token caching. Verify existence.

Use WebSearch for each and try to fetch key details from arxiv pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "a998cc73-452b-4aa6-b39a-132d24048147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:37:11.442Z_

```json
{
  "parentUuid": "a998cc73-452b-4aa6-b39a-132d24048147",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
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
  "uuid": "8d2b0c20-0183-4186-bfcc-53ff869c48be",
  "timestamp": "2026-05-10T19:37:11.442Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:37:15.299Z_



I'll search for all four items in parallel to verify these claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d2b0c20-0183-4186-bfcc-53ff869c48be",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTApgAfseVNPeYWDqGy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c25c867-bb48-48e0-a869-3ac7091bb78e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011frMBHn3KLd25tQTarPDfn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 833,
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

_source line 4 · 2026-05-10T19:37:15.471Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EHiZoyfVRa813SJqGqVaNo`</summary>

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
  "parentUuid": "1c25c867-bb48-48e0-a869-3ac7091bb78e",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTApgAfseVNPeYWDqGy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa4426b5-ca6e-440c-a643-6f535b53d810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011frMBHn3KLd25tQTarPDfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 8223,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 833,
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

_source line 5 · 2026-05-10T19:37:15.474Z_

<details><summary>↩ Tool result · `toolu_01EHiZoyfVRa813SJqGqVaNo`</summary>

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
  "parentUuid": "fa4426b5-ca6e-440c-a643-6f535b53d810",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "21113497-9b8f-417a-979a-cc81639e804c",
  "sourceToolAssistantUUID": "fa4426b5-ca6e-440c-a643-6f535b53d810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:37:17.942Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21113497-9b8f-417a-979a-cc81639e804c",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTB8TFC427AvPrNVqcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b71a163-e073-4d23-a372-3f7d63beeb3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrQSG7FQeGNNxdmuv5Zya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 9056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 7 · 2026-05-10T19:37:18.458Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014qDXvoFZkUsRdqnqF9bmMF`</summary>

```json
{
  "query": "CoRL 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b71a163-e073-4d23-a372-3f7d63beeb3e",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTB8TFC427AvPrNVqcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "137e6289-bc10-45bf-8da1-eb93e0e812a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrQSG7FQeGNNxdmuv5Zya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 9056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 8 · 2026-05-10T19:37:19.866Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JSgba3V3fLwNmDsFkLhLEr`</summary>

```json
{
  "query": "Being-H0.7 latent world-action model egocentric videos arXiv 2605.00078"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "137e6289-bc10-45bf-8da1-eb93e0e812a7",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTB8TFC427AvPrNVqcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53cd6c3c-3bed-43e2-9998-ad1e538179dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrQSG7FQeGNNxdmuv5Zya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 9056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 9 · 2026-05-10T19:37:20.975Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016ynsJdUCqkstNxzwRpiwww`</summary>

```json
{
  "query": "Fast-WAM arXiv 2603.16666 world action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53cd6c3c-3bed-43e2-9998-ad1e538179dc",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTB8TFC427AvPrNVqcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9b5841a-3ab6-43ca-a73a-1ed2e4513630",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrQSG7FQeGNNxdmuv5Zya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 9056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 10 · 2026-05-10T19:37:21.221Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TvCzmcoKbc7BXXTfBJGFxU`</summary>

```json
{
  "query": "WorldCache arXiv 2603.06331 heterogeneous token caching world models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9b5841a-3ab6-43ca-a73a-1ed2e4513630",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTB8TFC427AvPrNVqcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "152d8c7d-3840-4da4-85d8-b20131346dc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrQSG7FQeGNNxdmuv5Zya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 9056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

### Tool result

_source line 11 · 2026-05-10T19:37:24.498Z_

<details><summary>↩ Tool result · `toolu_014qDXvoFZkUsRdqnqF9bmMF`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline call for papers"

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"}]

Based on the search results, here's information about CoRL 2026 submission deadlines and the call for papers:

## Key Submission Deadlines

Abstract submission is due May 25, 2026, and full paper submission is due May 28, 2026. Note that there are slight variations in the reported dates across sources—some sources indicate the abstract deadline as May 26, 2026 and paper deadline as May 29, 2026, both at 11:59 UTC.

## Conference Details

CoRL is an annual international conference focusing on the intersection of robotics and machine learning, and CoRL 2026 will be held in Austin, Texas, US. The conference is scheduled for November 9-12 in Austin, TX.

## Submission Requirements

Papers may be submitted through OpenReview, and the page limit is 8 pages for the main paper, with acknowledgments, references, and appendix not counting towards the page limit. All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments.

For more detailed information about submission guidelines and requirements, you can visit the official CoRL 2026 website at corl.org or the OpenReview submission portal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "137e6289-bc10-45bf-8da1-eb93e0e812a7",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "51f5f7f6-afdd-422b-b8f1-9241349a3cfb",
  "sourceToolAssistantUUID": "137e6289-bc10-45bf-8da1-eb93e0e812a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:37:27.344Z_

<details><summary>↩ Tool result · `toolu_01JSgba3V3fLwNmDsFkLhLEr`</summary>

```text
Web search results for query: "Being-H0.7 latent world-action model egocentric videos arXiv 2605.00078"

Links: [{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"GitHub - BeingBeyond/Being-H: Being-H is BeingBeyond's family of human-centric embodied foundation models. · GitHub","url":"https://github.com/BeingBeyond/Being-H"},{"title":"human-motion-arxiv-daily/README.md at main · AndrewDing616/human-motion-arxiv-daily","url":"https://github.com/AndrewDing616/human-motion-arxiv-daily/blob/main/README.md"},{"title":"Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos","url":"https://arxiv.org/html/2507.15597v1"},{"title":"Scalable Vision-Language-Action Model Pretraining for ​Robotic Manipulation with Real-Life Human Activity Videos","url":"https://arxiv.org/html/2510.21571v1"},{"title":"Being-H0: Vision-Language-Action Model | PDF | Learning | Cognitive Science","url":"https://www.scribd.com/document/900573442/Being-H0"},{"title":"Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization","url":"https://arxiv.org/html/2601.12993v1"},{"title":"[2507.15597] Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos","url":"https://arxiv.org/abs/2507.15597"},{"title":"Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/being-h0-vision-language-action-pretraining-large"},{"title":"GitHub - Lyman-Smoker/Awesome_Ego_Action: A curated list of Egocentric Action Understanding resources · GitHub","url":"https://github.com/Lyman-Smoker/Awesome_Ego_Action"}]

I found the paper you're looking for! Here's the information about Being-H0.7:

## Overview

Being-H0.7 is a latent world-action model pretrained from large-scale egocentric videos.

## Key Innovation

Instead of predicting future frames, Being-H0.7 introduces a small set of learnable latent queries between the multimodal context and the action tokens. During model propagation, these dedicated reasoning slots attend to the instruction, observation history, and robot state, aggregate task- and interaction-relevant information, and form a compact latent state before actions are generated.

## Architecture Approach

Being-H0.7 is a latent world-action model that uses learnable latent queries as an explicit reasoning interface between perception and action. A future-informed posterior branch supervises this interface during training, while the deployable prior branch infers the latent predictive state from the current context alone.

## Performance

Pretrained on large-scale egocentric videos, Being-H0.7 achieves strong performance across diverse robot tasks.

The paper (arXiv:2605.00078) was published on April 30, 2026, and represents an approach that improves upon traditional world-action models by operating in latent space rather than pixel space for more efficient and effective robot control learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53cd6c3c-3bed-43e2-9998-ad1e538179dc",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "93de47d9-179b-4bb3-b0db-a908fb862999",
  "sourceToolAssistantUUID": "53cd6c3c-3bed-43e2-9998-ad1e538179dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:37:28.083Z_

<details><summary>↩ Tool result · `toolu_01TvCzmcoKbc7BXXTfBJGFxU`</summary>

```text
Web search results for query: "WorldCache arXiv 2603.06331 heterogeneous token caching world models"

Links: [{"title":"[2603.06331] WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching","url":"https://arxiv.org/abs/2603.06331"},{"title":"WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching","url":"https://arxiv.org/html/2603.06331"},{"title":"Paper page - WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching","url":"https://huggingface.co/papers/2603.06331"},{"title":"(PDF) WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching","url":"https://www.researchgate.net/publication/401692389_WorldCache_Accelerating_World_Models_for_Free_via_Heterogeneous_Token_Caching"},{"title":"WorldCache: Content-Aware Caching for Accelerated Video World Models","url":"https://arxiv.org/html/2603.22286"},{"title":"GitHub - umair1221/WorldCache: WorldCache: Content-Aware Caching for Accelerated Video World Models · GitHub","url":"https://github.com/umair1221/WorldCache"},{"title":"[2603.22286] WorldCache: Content-Aware Caching for Accelerated Video World Models","url":"https://arxiv.org/abs/2603.22286"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/Awesome-World-Models"},{"title":"Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep","url":"https://arxiv.org/html/2603.24260v1"},{"title":"A Generative Caching System for Large Language Models Arun Iyengar","url":"https://arxiv.org/pdf/2503.17603"}]

Based on the search results, I found the paper you're looking for:

## WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching

WorldCache is a caching framework tailored to diffusion world models. Diffusion-based world models have shown strong potential for unified world simulation, but the iterative denoising remains too costly for interactive use and long-horizon rollouts.

### Key Technical Contribution

The framework introduces Curvature-guided Heterogeneous Token Prediction, which uses a physics-grounded curvature score to estimate token predictability and applies a Hermite-guided damped predictor for chaotic tokens with abrupt direction changes.

### Motivation

Policies designed for single-modal diffusion transfer poorly to world models due to two world-model-specific obstacles: token heterogeneity from multi-modal coupling and spatial variation, and non-uniform temporal dynamics where a small set of hard tokens drives error growth, making uniform skipping either unstable or overly conservative.

### Performance Results

WorldCache delivers up to 3.7× end-to-end speedups while maintaining 98% rollout quality, demonstrating the vast advantages and practicality of WorldCache in resource-constrained scenarios.

The paper was submitted to arXiv on March 6, 2026, with authors including Weilun Feng, Guoxin Fan, Haotong Qin, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "152d8c7d-3840-4da4-85d8-b20131346dc8",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "709d9339-09d6-4c99-8066-66a3bd7a8c9b",
  "sourceToolAssistantUUID": "152d8c7d-3840-4da4-85d8-b20131346dc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:37:28.259Z_

<details><summary>↩ Tool result · `toolu_016ynsJdUCqkstNxzwRpiwww`</summary>

```text
Web search results for query: "Fast-WAM arXiv 2603.16666 world action model"

Links: [{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"Paper page - Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://huggingface.co/papers/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination? | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.16666"},{"title":"Fast-WAM: Rethinking Test-Time Imagination","url":"https://www.emergentmind.com/papers/2603.16666"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"},{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"}]

## Results for Fast-WAM arXiv 2603.16666

I found detailed information about this paper. Here's a summary:

**Paper Overview:**

World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action.

**Main Research Question:**

Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising, yet it remains unclear whether explicit future imagination is actually necessary for strong action performance. The paper asks whether WAMs need explicit future imagination at test time, or whether their benefit comes primarily from video modeling during training.

**Proposed Solution:**

Fast-WAM is a WAM architecture that retains video co-training during training but skips future prediction at test time.

**Key Findings:**

Fast-WAM remains competitive with imagine-then-execute variants, while removing video co-training causes a much larger performance drop. Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin) and real-world tasks, without embodied pretraining, and runs in real time with 190 ms latency, over 4× faster than existing imagine-then-execute WAMs.

**Authors:** Tianyuan Yuan, Zibin Dong, Yicheng Liu, and Hang Zhao (IIIS, Tsinghua University and Galaxea AI)

The paper was submitted on March 17, 2026, with the latest revision on March 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9b5841a-3ab6-43ca-a73a-1ed2e4513630",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "1763ec63-8038-4137-a698-06dcdeb87484",
  "sourceToolAssistantUUID": "e9b5841a-3ab6-43ca-a73a-1ed2e4513630",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T19:37:30.821Z_

Good, I found all four items. Now let me fetch the specific pages to verify the detailed claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1763ec63-8038-4137-a698-06dcdeb87484",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTC4c6YqjYWSWxHdeMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "575153b7-1a96-49a7-91b8-71cd6df256d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wy4sbpJaftPMGmxCHYAxb1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 2832,
      "cache_read_input_tokens": 10960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2832,
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

_source line 16 · 2026-05-10T19:37:32.921Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Aa5TbA9jK875Q5EMSaRRKz`</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract the exact submission deadlines: abstract deadline date, full paper deadline date, and conference dates/location. List them precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "575153b7-1a96-49a7-91b8-71cd6df256d0",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTC4c6YqjYWSWxHdeMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a54ee43-5352-46ae-9922-ad147d66d4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wy4sbpJaftPMGmxCHYAxb1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 2832,
      "cache_read_input_tokens": 10960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2832,
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

_source line 17 · 2026-05-10T19:37:35.555Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JJ6j1ErGBRMNq6JDdzaAs6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.00078",
  "prompt": "Extract the full title, authors, submission date, and abstract. Look for any mentions of: latent queries speed (3-4ms/step), no video generation, LIBERO benchmark score (99.2%), LIBERO-Plus score (82.1%), distributional shift results. Include all specific numbers and claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a54ee43-5352-46ae-9922-ad147d66d4a9",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTC4c6YqjYWSWxHdeMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "237db975-57f9-4fe4-a0a5-df4639ba358b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wy4sbpJaftPMGmxCHYAxb1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 2832,
      "cache_read_input_tokens": 10960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2832,
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

_source line 18 · 2026-05-10T19:37:35.693Z_

<details><summary>↩ Tool result · `toolu_01Aa5TbA9jK875Q5EMSaRRKz`</summary>

```text
Based on the provided web page content, I cannot extract the specific submission deadlines or conference dates/location. 

The page states: "For paper submission format and timeline, see: Instruction for Authors" but does not provide the actual deadline dates on this particular page. The information you're seeking is referenced as being located on the "Instruction for Authors" page, which is not included in the content provided.

To obtain the exact abstract deadline, full paper deadline, and conference dates/location, you would need to visit the [Instruction for Authors](/contributions/instruction-for-authors) section of the CoRL 2026 website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a54ee43-5352-46ae-9922-ad147d66d4a9",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "2bb525d3-397c-42b0-80f1-a5830875dae6",
  "sourceToolAssistantUUID": "4a54ee43-5352-46ae-9922-ad147d66d4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T19:37:37.175Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AuASaPCxH2Me2QEPy6yYWS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16666",
  "prompt": "Extract the full title, authors, submission date, and abstract. Look for claims about competitive results without test-time video generation, latency numbers, and benchmark results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bb525d3-397c-42b0-80f1-a5830875dae6",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTC4c6YqjYWSWxHdeMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f671c94-6deb-42fa-936f-478e175d5ad2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wy4sbpJaftPMGmxCHYAxb1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 2832,
      "cache_read_input_tokens": 10960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2832,
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

_source line 20 · 2026-05-10T19:37:37.740Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015bx2MufchXfGj6pGqGTg6Y`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.06331",
  "prompt": "Extract the full title, authors, submission date, and abstract. Look for claims about 3.7x speedup, heterogeneous token caching, and any specific benchmark results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f671c94-6deb-42fa-936f-478e175d5ad2",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTC4c6YqjYWSWxHdeMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "547f35ff-517a-4caf-810c-eabb4236f24d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wy4sbpJaftPMGmxCHYAxb1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 2832,
      "cache_read_input_tokens": 10960,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2832
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 917,
          "output_tokens": 463,
          "cache_read_input_tokens": 10960,
          "cache_creation_input_tokens": 2832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2832,
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

_source line 21 · 2026-05-10T19:37:40.124Z_

<details><summary>↩ Tool result · `toolu_01JJ6j1ErGBRMNq6JDdzaAs6`</summary>

```text
# Being-H0.7 Paper Summary

**Full Title:** Being-H0.7: A Latent World-Action Model from Egocentric Videos

**Authors:** Hao Luo, Wanpeng Zhang, Yicheng Feng, Sipeng Zheng, Haiweng Xu, Chaoyi Xu, Ziheng Xi, Yuhui Fu, Zongqing Lu

**Submission Date:** April 30, 2026

**Abstract Summary:**
The research introduces a model that combines future-aware reasoning with robot control policies. Rather than generating predicted video frames, the system uses "learnable latent queries between perception and action as a compact reasoning interface." It employs dual-branch training where a deployable branch infers states from current observations while a training-only posterior branch uses future embeddings. The authors claim their approach achieves "state-of-the-art or comparable performance" across simulation benchmarks and real-world tasks.

**Note on Requested Metrics:**
The provided webpage content does not include specific performance numbers such as latent query speeds (3-4ms/step), LIBERO benchmark scores (99.2%), LIBERO-Plus scores (82.1%), or distributional shift results. These details would require access to the full paper PDF or additional documentation not contained in this webpage excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "237db975-57f9-4fe4-a0a5-df4639ba358b",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "0705961b-4ff1-4677-a8a6-89565db862d9",
  "sourceToolAssistantUUID": "237db975-57f9-4fe4-a0a5-df4639ba358b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:37:41.673Z_

<details><summary>↩ Tool result · `toolu_01AuASaPCxH2Me2QEPy6yYWS`</summary>

```text
# Fast-WAM Research Summary

**Full Title:** Fast-WAM: Do World Action Models Need Test-time Future Imagination?

**Authors:** Tianyuan Yuan, Zibin Dong, Yicheng Liu, Hang Zhao

**Submission Date:** March 17, 2026 (v1); revised March 23, 2026 (v2)

## Key Claims

**Core Finding:** The researchers propose that video prediction's primary value in World Action Models occurs during training rather than at inference time.

**Performance Without Test-time Generation:** Fast-WAM "remains competitive with imagine-then-execute variants" despite eliminating future prediction steps at deployment.

**Latency Improvement:** The system operates "in real time with 190ms latency, over 4× faster than existing imagine-then-execute WAMs."

**Benchmark Results:** The approach achieves competitive performance on both simulation (LIBERO and RoboTwin) and real-world robotics tasks without requiring embodied pretraining.

**Training Emphasis:** Analysis reveals that "removing video co-training causes a much larger performance drop" than eliminating test-time imagination, suggesting video modeling during training substantially improves world representations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f671c94-6deb-42fa-936f-478e175d5ad2",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "846b193e-ff58-49a2-8f2e-be3aa75523e7",
  "sourceToolAssistantUUID": "7f671c94-6deb-42fa-936f-478e175d5ad2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T19:37:43.269Z_

<details><summary>↩ Tool result · `toolu_015bx2MufchXfGj6pGqGTg6Y`</summary>

```text
# WorldCache Paper Summary

**Full Title:** WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching

**Authors:** Weilun Feng, Guoxin Fan, Haotong Qin, Chuanguang Yang, Mingqiang Wu, Yuqi Li, Xiangqi Li, Zhulin An, Libo Huang, Dingrui Wang, Longlong Liao, Michele Magno, Yongjun Xu

**Submission Date:** March 6, 2026

**Key Claims:**
The paper reports achieving "up to **3.7× end-to-end speedups while maintaining 98% rollout quality**" on diffusion-based world models. The research introduces two main techniques:

1. *Curvature-guided Heterogeneous Token Prediction* — uses physics-informed curvature scoring to identify token predictability and applies specialized handling for "chaotic tokens with abrupt direction changes"

2. *Chaotic-prioritized Adaptive Skipping* — accumulates normalized drift signals and selectively recomputes "only when bottleneck tokens begin to drift"

**Abstract Highlight:** The work addresses "token heterogeneity from multi-modal coupling and spatial variation, and non-uniform temporal dynamics" that prevent standard caching approaches from working effectively with world models. The framework demonstrates practical utility "in resource-constrained scenarios."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "547f35ff-517a-4caf-810c-eabb4236f24d",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "e2062259-5837-48ca-9c18-3813e2dfbacf",
  "sourceToolAssistantUUID": "547f35ff-517a-4caf-810c-eabb4236f24d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T19:37:46.473Z_

Let me now fetch the Being-H0.7 HTML page to check the specific numerical claims, and the CoRL instruction page for exact deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2062259-5837-48ca-9c18-3813e2dfbacf",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTDApvkRWnBp5w71Lai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcfb369e-349b-443f-9e18-ac1009e08a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZiXnrRo1EGqbBXUNZp8Ri",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2614,
      "cache_read_input_tokens": 13792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2614,
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

_source line 25 · 2026-05-10T19:37:49.141Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MPoQnihuG6y6y5xP9L68XC`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.00078v1",
  "prompt": "Look for these SPECIFIC numbers and claims: (1) latent query inference speed of 3-4ms per step, (2) LIBERO benchmark score of 99.2%, (3) LIBERO-Plus score of 82.1% under distributional shift, (4) any mention of not requiring video generation at test time. Extract exact numbers and the context around them."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcfb369e-349b-443f-9e18-ac1009e08a36",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTDApvkRWnBp5w71Lai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56872093-cbd8-4d15-b57f-786a3483ab00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZiXnrRo1EGqbBXUNZp8Ri",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2614,
      "cache_read_input_tokens": 13792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2614,
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

_source line 26 · 2026-05-10T19:37:50.158Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E3x2zoPy4Xm3MZhDJBox4Z`</summary>

```json
{
  "url": "https://www.corl.org/",
  "prompt": "Extract the exact conference dates, location, and any submission deadlines mentioned on this homepage. Look for abstract deadline, paper deadline, and conference dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56872093-cbd8-4d15-b57f-786a3483ab00",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTDApvkRWnBp5w71Lai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e559b9b9-3367-4969-a018-7230a8b875e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZiXnrRo1EGqbBXUNZp8Ri",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2614,
      "cache_read_input_tokens": 13792,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2614
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 13792,
          "cache_creation_input_tokens": 2614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2614,
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

_source line 27 · 2026-05-10T19:37:52.642Z_

<details><summary>↩ Tool result · `toolu_01E3x2zoPy4Xm3MZhDJBox4Z`</summary>

```text
# CoRL 2026 Key Information

**Conference Dates:**
"November 9-12, 2026" with workshops on November 9 and the main conference running "November 10-12"

**Location:**
"JW Marriott Austin" situated at "110 E 2nd St, Austin, TX 78701 USA"

**Submission Deadlines:**
The homepage does not specify abstract or paper submission deadlines. While the page mentions "The Call for Papers...are now available" (dated January 25), no specific submission closure dates are provided on this landing page.

**Recent Updates:**
The most recent announcements include a workshop call (April 29), author instructions update regarding AI policy (April 17), and a sponsorship request (February 26).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e559b9b9-3367-4969-a018-7230a8b875e2",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "9d18ac3e-79eb-4226-b3ee-30a73e4c5420",
  "sourceToolAssistantUUID": "e559b9b9-3367-4969-a018-7230a8b875e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T19:37:54.352Z_

<details><summary>↩ Tool result · `toolu_01MPoQnihuG6y6y5xP9L68XC`</summary>

```text
# Being-H0.7: Key Performance Claims

## Performance Metrics

**LIBERO Benchmark:** The model achieves "a 99.2% average success rate" across all task suites in the standard LIBERO evaluation.

**LIBERO-Plus (Distributional Shift):** Under environmental perturbations, Being-H0.7 "secures a 82.1% zero-shot success rate, which further improves to 84.8% after fine-tuning."

## Inference Efficiency

**Latency:** The deployment operates "in the 3–4 ms/step regime" through Universal Async Chunking (UAC), enabling responsive control without test-time computational overhead.

## No Video Generation Requirement

A critical distinction: "At inference, Being-H0.7 discards the posterior branch and performs no visual rollout." The model achieves predictive reasoning through "a latent reasoning space" rather than pixel-level future prediction, avoiding the "heavy training cost of video generation" that characterizes competing world-action approaches.

The latent representations prove sufficiently rich that they can later be "used jointly as conditions for a video generation model to synthesize future task states," though this visualization occurs post-hoc rather than during deployment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56872093-cbd8-4d15-b57f-786a3483ab00",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "a9392e7d-81a8-4a5d-aaa1-28004ec70b0f",
  "sourceToolAssistantUUID": "56872093-cbd8-4d15-b57f-786a3483ab00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-10T19:37:56.946Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BSpcqL9Wf33bis6Ei2qubR`</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract the EXACT submission deadlines: abstract submission deadline date and time, full paper submission deadline date and time. List every deadline mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9392e7d-81a8-4a5d-aaa1-28004ec70b0f",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTDzAFwoKKSkuKJH68L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9df70c3c-7c38-4b43-b1b1-824592be9fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E6hWYh1Q9YnHSEw4XCS8nf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 204,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 16406,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 599
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 204,
          "output_tokens": 111,
          "cache_read_input_tokens": 16406,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 599,
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

_source line 30 · 2026-05-10T19:38:00.837Z_

<details><summary>↩ Tool result · `toolu_01BSpcqL9Wf33bis6Ei2qubR`</summary>

```text
# CoRL 2026 Submission Deadlines

Based on the provided content, **specific deadline dates and times are not explicitly stated** in this instruction page. 

The document mentions:

- "Please keep in mind that the deadlines are final" and references an "abstract submission deadline" and "paper deadline"
- A note about the "paper submission deadline is Thursday (5/28) EOD rather than Friday"
- "Camera-ready version of your paper is due by Oct 12, 2026 (23:59 Anywhere on Earth)"
- A "rebuttal deadline" is referenced but no date is provided

**The only complete deadline stated is:** Camera-ready submissions by October 12, 2026, 23:59 AOE.

The abstract and full paper deadlines appear to be listed in a "Key Dates" section, but the actual dates are not populated in the content provided. The mention of "Thursday (5/28)" likely refers to May 28, but the year and exact times for abstract/paper submission are not specified in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9df70c3c-7c38-4b43-b1b1-824592be9fd8",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "848c7839-5222-421d-acbd-907904112853",
  "sourceToolAssistantUUID": "9df70c3c-7c38-4b43-b1b1-824592be9fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T19:38:04.457Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015SYkibcYuCnbyB9aFU9KBq`</summary>

```json
{
  "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf",
  "prompt": "Extract the exact CoRL 2026 submission deadlines - abstract deadline and paper deadline dates with times."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "848c7839-5222-421d-acbd-907904112853",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTETurnGNBzsbVJJici",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34db51e0-6473-451a-8194-ddbbac3626e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JnZyYTczui9P9F62vsm3kt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 17005,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 560
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 17005,
          "cache_creation_input_tokens": 560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 560,
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

_source line 32 · 2026-05-10T19:38:06.667Z_

<details><summary>↩ Tool result · `toolu_015SYkibcYuCnbyB9aFU9KBq`</summary>

```text
# CoRL 2026 Submission Deadlines

Based on the commit changes shown, here are the exact submission deadlines for CoRL 2026:

## Abstract Submission Deadline
- **Date & Time:** May 26, 2026 at 11:59 UTC
- **Format:** `2026-05-26 11:59:00` (UTC)

## Paper Submission Deadline
- **Date & Time:** May 29, 2026 at 11:59 UTC
- **Format:** `2026-05-29 11:59:00` (UTC)

## Additional Conference Details
- **Conference Dates:** November 9-12, 2026
- **Venue:** JW Marriott Austin, 110 E 2nd St, Austin, TX 78701
- **Note:** Workshops on Nov 9, main conference Nov 10-12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34db51e0-6473-451a-8194-ddbbac3626e8",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "2909ee17-6dd6-40c6-a0e0-cdd4cc259405",
  "sourceToolAssistantUUID": "34db51e0-6473-451a-8194-ddbbac3626e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T19:38:10.707Z_

Now I have all the data. Let me also check an important detail -- the CoRL instruction page mentioned the paper deadline is "Thursday (5/28)" but the HuggingFace deadline tracker says May 29. Let me check which day of the week May 28 and 29 fall on.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2909ee17-6dd6-40c6-a0e0-cdd4cc259405",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTEtqZBqvQJeHL4xGFd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50643f72-b9eb-4fa8-b52e-75a9b8ea9be0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JbQURDAYn3x71vSdF4LcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 17565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 351,
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

_source line 34 · 2026-05-10T19:38:11.338Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QFJofT5HcA6nkuxyozNkt2`</summary>

```json
{
  "command": "date -d \"2026-05-28\" +%A && date -d \"2026-05-29\" +%A",
  "description": "Check day of week for May 28 and 29, 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50643f72-b9eb-4fa8-b52e-75a9b8ea9be0",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTEtqZBqvQJeHL4xGFd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "322abcc0-3434-40b5-8d7d-cde819362268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JbQURDAYn3x71vSdF4LcS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 17565,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 351
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 17565,
          "cache_creation_input_tokens": 351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 351,
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

_source line 35 · 2026-05-10T19:38:11.495Z_

<details><summary>↩ Tool result · `toolu_01QFJofT5HcA6nkuxyozNkt2`</summary>

```text
Thursday
Friday
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "322abcc0-3434-40b5-8d7d-cde819362268",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "aab29a10692718339",
  "type": "user",
  "uuid": "92000cd9-d25b-482d-844d-ad814736d51e",
  "sourceToolAssistantUUID": "322abcc0-3434-40b5-8d7d-cde819362268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-10T19:38:46.035Z_

Interesting -- the official CoRL instruction page says the paper deadline is "Thursday (5/28)" but the HuggingFace deadline tracker lists May 29. Here are the consolidated findings:

---

## 1. CoRL 2026 Submission Deadlines

**Verdict: PARTIALLY MATCHES, with discrepancies in the exact dates.**

The proposal claims:
- Abstract deadline: May 26, 2026
- Paper deadline: May 29, 2026
- Conference in Austin: Nov 9-12

What I found:
- The **HuggingFace AI-deadlines tracker** lists the abstract deadline as **May 26, 2026 at 11:59 UTC** and paper deadline as **May 29, 2026 at 11:59 UTC** -- matching the proposal exactly.
- However, the **official CoRL instruction-for-authors page** references the paper submission deadline as **"Thursday (5/28)"**, which is May 28 (Thursday), not May 29 (Friday). This is a one-day discrepancy between the official page and the third-party tracker.
- Conference dates of **November 9-12, 2026** in **Austin, TX** (JW Marriott Austin) are confirmed.

The proposal's dates match the HuggingFace tracker but the official CoRL page suggests the paper deadline may actually be May 28, not May 29. The abstract deadline discrepancy is less clear (some sources say May 25, others May 26). The conference dates and location are correct.

---

## 2. Being-H0.7 (arXiv 2605.00078)

**Verdict: CONFIRMED -- all specific claims verified.**

- **Paper exists**: Yes, at [arxiv.org/abs/2605.00078](https://arxiv.org/abs/2605.00078), submitted April 30, 2026.
- **Title**: "Being-H0.7: A Latent World-Action Model from Egocentric Videos" -- matches exactly.
- **Latent queries at 3-4ms/step**: Confirmed. The paper states it operates "in the 3-4 ms/step regime" through Universal Async Chunking (UAC).
- **No video generation**: Confirmed. "At inference, Being-H0.7 discards the posterior branch and performs no visual rollout."
- **99.2% on LIBERO**: Confirmed. "a 99.2% average success rate" across all LIBERO task suites.
- **82.1% on LIBERO-Plus under distributional shift**: Confirmed. "secures a 82.1% zero-shot success rate" under environmental perturbations (further improves to 84.8% after fine-tuning).

All four specific numerical claims check out.

---

## 3. Fast-WAM (arXiv 2603.16666)

**Verdict: CONFIRMED.**

- **Paper exists**: Yes, at [arxiv.org/abs/2603.16666](https://arxiv.org/abs/2603.16666), submitted March 17, 2026.
- **Title**: "Fast-WAM: Do World Action Models Need Test-time Future Imagination?" 
- **Competitive results without test-time video generation**: Confirmed. Fast-WAM "remains competitive with imagine-then-execute variants" while skipping future prediction at test time. Runs at 190ms latency, over 4x faster than existing imagine-then-execute WAMs.
- **Authors**: Tianyuan Yuan, Zibin Dong, Yicheng Liu, Hang Zhao (Tsinghua University / Galaxea AI).

---

## 4. WorldCache (arXiv 2603.06331)

**Verdict: CONFIRMED.**

- **Paper exists**: Yes, at [arxiv.org/abs/2603.06331](https://arxiv.org/abs/2603.06331), submitted March 6, 2026.
- **Title**: "WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching" -- matches.
- **3.7x speedup**: Confirmed. "up to 3.7x end-to-end speedups while maintaining 98% rollout quality."
- **Heterogeneous token caching**: Confirmed. Uses Curvature-guided Heterogeneous Token Prediction and Chaotic-prioritized Adaptive Skipping.

---

## Summary

| Claim | Status |
|-------|--------|
| CoRL 2026 dates & location (Austin, Nov 9-12) | Confirmed |
| CoRL abstract deadline May 26 | Matches HF tracker; official page less clear |
| CoRL paper deadline May 29 | Matches HF tracker; official page says May 28 (Thursday) |
| Being-H0.7 (2605.00078) exists | Confirmed |
| Being-H0.7: 3-4ms/step latent queries | Confirmed |
| Being-H0.7: no video generation | Confirmed |
| Being-H0.7: 99.2% LIBERO | Confirmed |
| Being-H0.7: 82.1% LIBERO-Plus | Confirmed |
| Fast-WAM (2603.16666) exists | Confirmed |
| Fast-WAM: competitive without test-time video gen | Confirmed |
| WorldCache (2603.06331) exists | Confirmed |
| WorldCache: 3.7x speedup | Confirmed |

The only point of uncertainty is the exact CoRL paper deadline (May 28 vs May 29), where the official instructions page and third-party tracker disagree by one day.

Sources:
- [CoRL 2026 Homepage](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [HuggingFace AI-deadlines CoRL 2026 entry](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)
- [Being-H0.7 (arXiv 2605.00078)](https://arxiv.org/abs/2605.00078)
- [Fast-WAM (arXiv 2603.16666)](https://arxiv.org/abs/2603.16666)
- [WorldCache (arXiv 2603.06331)](https://arxiv.org/abs/2603.06331)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92000cd9-d25b-482d-844d-ad814736d51e",
  "isSidechain": true,
  "agentId": "aab29a10692718339",
  "requestId": "req_011CauTFFZV7zD3PbLXkTQWt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8eaf37f5-d6fe-4228-8a5b-9fc7eba3da74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016aLFY9iS9ACExuS5arnEPk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 17916,
      "output_tokens": 1600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 194
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1600,
          "cache_read_input_tokens": 17916,
          "cache_creation_input_tokens": 194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 194,
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
