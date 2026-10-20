# Research conversation: I'm reviewing a research proposal called LACVLA that proposes "self-supervised language-affordance consistency objective

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a68964433f38e0acc.jsonl`
- **Structured JSON:** [`267ccc83162e0f129a8f.json`](../../sessions/26/267ccc83162e0f129a8f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-18T19:18:26.828Z_

I'm reviewing a research proposal called LACVLA that proposes "self-supervised language-affordance consistency objectives within an end-to-end VLA (vision-language-action model) for zero-shot cross-category manipulation." The key claim is that NO existing work combines (a) end-to-end affordance-within-VLA training, (b) open-vocabulary language conditioning of affordance, and (c) self-supervised consistency objectives.

I need you to do an exhaustive search for competing/concurrent work that may invalidate this gap claim. Use WebSearch for each query.

Search queries to run (run ALL of these):
1. "end-to-end affordance VLA 2025 2026" site:arxiv.org
2. "open vocabulary affordance manipulation" 2025 2026
3. "affordance consistency self-supervised robot" 2025 2026
4. "language conditioned affordance robot manipulation" 2026
5. "affordance vision language action model" 2026
6. "self-supervised affordance learning manipulation" 2025 2026
7. "contrastive affordance robot" 2025 2026
8. "paraphrase consistency robot policy" OR "instruction invariance robot"
9. "affordance bottleneck VLA" OR "affordance attention VLA"
10. site:openreview.net "affordance" "vision language action" 2026

For each search, report the most relevant papers found that the proposal did NOT cite. Focus on papers from 2025-2026 that could be direct competitors. Report paper titles, arXiv IDs, and a one-line description of relevance. Keep report under 500 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "d1995672-7f3d-4b67-9c05-ec9ac79aeec4",
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

_source line 2 · 2026-05-18T19:18:26.849Z_

```json
{
  "parentUuid": "d1995672-7f3d-4b67-9c05-ec9ac79aeec4",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
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
  "uuid": "f49c1657-ad54-4e9f-bd3f-fd0f4e40f3a9",
  "timestamp": "2026-05-18T19:18:26.849Z",
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

_source line 3 · 2026-05-18T19:18:30.473Z_



I'll run all 10 searches in parallel now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f49c1657-ad54-4e9f-bd3f-fd0f4e40f3a9",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaDFUqjpevQa3bt6NNW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b79b3c73-0421-493c-b679-b2dc6ea43d15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBnK1g1SqjNEzu9a59J6Dc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 937,
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

_source line 4 · 2026-05-18T19:18:30.835Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011N8EXQbA2z71qbTeGioSJs`</summary>

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
  "parentUuid": "b79b3c73-0421-493c-b679-b2dc6ea43d15",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaDFUqjpevQa3bt6NNW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f46bd5bc-c1ce-4ceb-b743-853fbb882c51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBnK1g1SqjNEzu9a59J6Dc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 8223,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 937
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 937,
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

_source line 5 · 2026-05-18T19:18:30.839Z_

<details><summary>↩ Tool result · `toolu_011N8EXQbA2z71qbTeGioSJs`</summary>

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
  "parentUuid": "f46bd5bc-c1ce-4ceb-b743-853fbb882c51",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "ed7cdbdd-d6be-4c6e-a5ef-293290202a7b",
  "sourceToolAssistantUUID": "f46bd5bc-c1ce-4ceb-b743-853fbb882c51",
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

_source line 6 · 2026-05-18T19:18:33.235Z_



Now I'll run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed7cdbdd-d6be-4c6e-a5ef-293290202a7b",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaDYotQNrGkVwawiAKG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "934ffb89-03c3-4118-ade4-990c586be598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FnYAxvTjwaocZ9te4CUNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 7 · 2026-05-18T19:18:33.534Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Lkp3WguiYji9bRDNC2Emi`</summary>

```json
{
  "query": "\"end-to-end affordance VLA 2025 2026\" site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "934ffb89-03c3-4118-ade4-990c586be598",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaDYotQNrGkVwawiAKG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78bbb6c4-3a78-451e-a2e9-e73769fafa2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FnYAxvTjwaocZ9te4CUNA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 9160,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1406
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 9160,
          "cache_creation_input_tokens": 1406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1406,
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

_source line 8 · 2026-05-18T19:18:40.533Z_

<details><summary>↩ Tool result · `toolu_014Lkp3WguiYji9bRDNC2Emi`</summary>

```text
Web search results for query: ""end-to-end affordance VLA 2025 2026" site:arxiv.org"

Links: [{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"𝐴₀: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://arxiv.org/html/2504.12636v1"},{"title":"End-to-End Affordance Learning for Robotic Manipulation","url":"https://arxiv.org/pdf/2209.12941"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10109"},{"title":"[2504.12636] A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://arxiv.org/abs/2504.12636"}]

I found several relevant papers on arXiv related to end-to-end affordance and Vision-Language-Action (VLA) models from 2025-2026:

1. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance** (December 2024)
   - This work advances Vision-Language-Action (VLA) models, showing that training with internet-scale data can empower end-to-end policy learning models to outperform non-VLA models. The approach prompts the model to consider four types of affordances before taking action: object affordance, grasp affordance, spatial affordance, and movement affordance, transforming each into visual and textual formats.

2. **Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation** (2025)
   - This paper addresses limitations in end-to-end VLA design, which lacks explicit 3D spatial reasoning and prevents reliable identification of actionable regions in unfamiliar environments. It introduces Affordance Field Intervention (AFI), a lightweight hybrid framework that uses 3D Spatial Affordance Fields as an on-demand plugin to guide VLA behavior.

3. **A₀: An Affordance-Aware Hierarchical Model for General Robotic Manipulation** (April 2025)
   - This work addresses critical challenges in understanding spatial affordances for complex manipulation tasks, introducing an object-centric hierarchical model that learns embodiment-agnostic affordance representation.

These papers represent recent advances in combining affordance reasoning with end-to-end VLA models for robotic manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78bbb6c4-3a78-451e-a2e9-e73769fafa2e",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "6be0b5ab-57eb-4399-ad44-8a6941ed1485",
  "sourceToolAssistantUUID": "78bbb6c4-3a78-451e-a2e9-e73769fafa2e",
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

### Tool call

_source line 9 · 2026-05-18T19:18:42.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013XSJceDcyddcNAZDbsAg2P`</summary>

```json
{
  "query": "\"open vocabulary affordance manipulation\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6be0b5ab-57eb-4399-ad44-8a6941ed1485",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaEFxeTXwy7zjkBWB4q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46cdde7e-5e76-4e1f-8e5a-d614571bb585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfbWMTy6zkgeQ2Xwxegr2m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 10566,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 842
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 10566,
          "cache_creation_input_tokens": 842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 842,
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

_source line 10 · 2026-05-18T19:18:49.938Z_

<details><summary>↩ Tool result · `toolu_013XSJceDcyddcNAZDbsAg2P`</summary>

```text
Web search results for query: ""open vocabulary affordance manipulation" 2025 2026"

Links: [{"title":"Open-Vocabulary Mobile Manipulation","url":"https://www.emergentmind.com/topics/open-vocabulary-mobile-manipulation-ovmm"},{"title":"Open-Vocabulary 3D Affordance Understanding via ...","url":"https://eprints.gla.ac.uk/360521/2/360521.pdf"},{"title":"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot   Manipulation through LLM Affordance-Grounding","url":"https://arxiv.org/pdf/2404.11000"},{"title":"(PDF) Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation","url":"https://www.researchgate.net/publication/397480634_Affordance-Guided_Coarse-to-Fine_Exploration_for_Base_Placement_in_Open-Vocabulary_Mobile_Manipulation"},{"title":"GitHub - hq-King/Awesome-Affordance-Learning · GitHub","url":"https://github.com/hq-King/Awesome-Affordance-Learning"},{"title":"Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation","url":"https://arxiv.org/pdf/2511.06240"},{"title":"AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary","url":"https://arxiv.org/pdf/2503.00778"}]

Based on the search results, here's what I found about open vocabulary affordance manipulation research from 2025-2026:

## Recent Research Developments

An affordance-guided approach from November 2025 introduces a two-stage zero-shot base placement pipeline that explicitly bridges semantic intent and geometric feasibility for open-vocabulary mobile manipulation tasks.

A paper titled "Open-Vocabulary 3D Affordance Understanding via Functional Text Enhancement and Multilevel Representation Alignment" was published in October 2025 at the ACM International Conference on Multimedia, which enables agents to highlight relevant points on 3D objects based on query text for fine-grained and context-specific operations.

## Key Research Challenges

A major challenge is enabling robots to reason jointly about geometric feasibility and semantic intent—identifying collision-free locations that align with task-relevant affordances, such as positioning in front of a cabinet to open it.

## Notable Works

Recent papers in this area include:
- Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale (2025)
- AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models (AAAI 2026)

These works represent active research in combining vision-language models with affordance understanding for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46cdde7e-5e76-4e1f-8e5a-d614571bb585",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "2aa7bf28-4f8b-4037-823c-98ad84b06b5b",
  "sourceToolAssistantUUID": "46cdde7e-5e76-4e1f-8e5a-d614571bb585",
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

### Tool call

_source line 11 · 2026-05-18T19:18:52.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NiBdUrN9dSxAoN4wmPZVGX`</summary>

```json
{
  "query": "\"affordance consistency self-supervised robot\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aa7bf28-4f8b-4037-823c-98ad84b06b5b",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaExCLdDDvKZzqRkxWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f663888-59f4-4859-af3e-ba007e3d2cb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrafhyQJQriLU3aiVTCwSp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 11408,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 772
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 11408,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 772,
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

_source line 12 · 2026-05-18T19:18:59.832Z_

<details><summary>↩ Tool result · `toolu_01NiBdUrN9dSxAoN4wmPZVGX`</summary>

```text
Web search results for query: ""affordance consistency self-supervised robot" 2025 2026"

Links: [{"title":"HRP: Human Affordances for Robotic Pre-Training","url":"https://arxiv.org/pdf/2407.18911"},{"title":"Affordance Learning from Play for Sample-Efficient Policy Learning","url":"https://arxiv.org/pdf/2203.00352"},{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Learning_Precise_Affordances_from_Egocentric_Videos_for_Robotic_Manipulation_ICCV_2025_paper.pdf"},{"title":"Learning Affordances from Interactive Exploration using an Object-level   Map","url":"https://arxiv.org/pdf/2501.06047"},{"title":"Visual Affordances: Enabling Robots to Understand Object Functionality","url":"https://arxiv.org/html/2505.05074v1"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

I found several relevant research papers and resources on affordance learning and self-supervised approaches for robotic manipulation from 2025-2026:

## Key Recent Work

Self-supervised visual foundation models like DINOv2 have been demonstrated to be highly effective for data-limited affordance learning. Recent work has focused on addressing limitations such as affordance predictions being too coarse, which are less accurate when applied in the real world.

Self-supervised learning is being leveraged to create robot-specific, scene-level affordance datasets without relying on manual labels. Additionally, research in assistive robot manipulation has focused on efficiently adapting large-scale models to downstream scene affordance understanding tasks, especially in daily living scenarios.

## Notable 2025-2026 Papers

Several related affordance-based approaches have been published recently:
- RT-Affordance, a hierarchical model that proposes an affordance plan given task language and can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories
- Methods employing self-supervised visual foundation models with parameter-efficient fine-tuning approaches like LoRA to adapt models across different domains without modifying original parameters

The search results also indicate there are multiple 2025-2026 papers on related topics including affordance distillation, vision-language models for robotic manipulation, and affordance-aware hierarchical models for robotic manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f663888-59f4-4859-af3e-ba007e3d2cb4",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "08d8989b-4c0f-4f73-b51f-3f74516c8a68",
  "sourceToolAssistantUUID": "2f663888-59f4-4859-af3e-ba007e3d2cb4",
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

### Tool call

_source line 13 · 2026-05-18T19:19:02.669Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EkJvKEkwUSteufaVq3T4qk`</summary>

```json
{
  "query": "\"language conditioned affordance robot manipulation\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08d8989b-4c0f-4f73-b51f-3f74516c8a68",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaFgVJPLFttCsddGdYJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a51714cd-a9a1-4d3c-8104-4b92d0879436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgE8NQp1KQuC55LsCm6fd1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 12180,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 12180,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 839,
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

_source line 14 · 2026-05-18T19:19:11.777Z_

<details><summary>↩ Tool result · `toolu_01EkJvKEkwUSteufaVq3T4qk`</summary>

```text
Web search results for query: ""language conditioned affordance robot manipulation" 2026"

Links: [{"title":"RoboAfford: A Dataset and Benchmark for Enhancing Object and Spatial Affordance Learning in Robot Manipulation | Request PDF","url":"https://www.researchgate.net/publication/396941670_RoboAfford_A_Dataset_and_Benchmark_for_Enhancing_Object_and_Spatial_Affordance_Learning_in_Robot_Manipulation"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"Improving Generalization of Language-Conditioned Robot Manipulation","url":"https://arxiv.org/html/2508.02405v1"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.researchgate.net/publication/385560182_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"},{"title":"RT-Affordance: Reasoning about Robotic Manipulation with Affordances","url":"https://openreview.net/pdf?id=s8VMLXKH1X"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot","url":"https://openreview.net/pdf?id=y4KugwU0qU"},{"title":"Empowering Large Language Models on Robotic Manipulation with Affordance Prompting","url":"https://arxiv.org/html/2404.11027v1"},{"title":"Empowering Large Language Models on Robotic Manipulation with Affordance   Prompting","url":"https://arxiv.org/pdf/2404.11027"},{"title":"Knowledge enhanced bottom-up affordance grounding for robotic interaction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11232630/"}]

Based on the web search results, here's what I found about language-conditioned affordance robot manipulation research in 2026:

## Recent Research Developments

RT-Affordance is a policy conditioned on both language specifications and visual affordances, where visual affordances show the pose of the robot end effector at key stages of the task visually projected onto the image input, providing precise yet concise guidance on how to manipulate objects.

BEACON is a language-conditioned navigation affordance prediction framework from March 2026 that requires a robot to infer a nearby traversable target location from its current observation and an open-vocabulary, relational instruction. It predicts an ego-centric Bird's-Eye View (BEV) affordance heatmap over a bounded local region including occluded areas.

## Multi-Modal Approaches

Research has explored obtaining goal-conditioned affordance values from large language models that describe the priorities of object executable parts for interaction, allowing LLMs to decompose human instructions into high-level sub-tasks feasible in the physical world.

Affordance maps represent a probability distribution over potential manipulation places, indicating not only the target objects but also the most suitable areas for robotic interaction.

These developments show the field is moving toward more sophisticated, multi-modal approaches that combine language instructions, visual understanding, and spatial affordance prediction for robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a51714cd-a9a1-4d3c-8104-4b92d0879436",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "f6f85cfd-7e2e-4c65-90fb-8be43bfb7aa6",
  "sourceToolAssistantUUID": "a51714cd-a9a1-4d3c-8104-4b92d0879436",
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

### Tool call

_source line 15 · 2026-05-18T19:19:14.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J4ktCxkARvuer3WpyGhJ4x`</summary>

```json
{
  "query": "\"affordance vision language action model\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6f85cfd-7e2e-4c65-90fb-8be43bfb7aa6",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaGZZMrrMWgZtejvUKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c31e4363-d1b9-4b8b-92f9-7fbb4cda473c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sqf9Dxh3JkiNEzTGNBUbo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 13019,
      "output_tokens": 62,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 62,
          "cache_read_input_tokens": 13019,
          "cache_creation_input_tokens": 887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 887,
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

_source line 16 · 2026-05-18T19:19:22.774Z_

<details><summary>↩ Tool result · `toolu_01J4ktCxkARvuer3WpyGhJ4x`</summary>

```text
Web search results for query: ""affordance vision language action model" 2026"

Links: [{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Paper page - DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation","url":"https://huggingface.co/papers/2601.22153"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"AffordanceLLM: Grounding affordance from vision language models - Amazon Science","url":"https://www.amazon.science/publications/affordancellm-grounding-affordance-from-vision-language-models"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://chain-of-affordance.github.io/"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"Affordance Perception by a Knowledge-Guided Vision-Language Model with   Efficient Error Correction","url":"https://arxiv.org/pdf/2407.13368"}]

I found several relevant results about affordance vision-language-action models from 2026 and recent 2025 research. Here's what the search uncovered:

## Key Findings

Recent research from 2026 includes models like RoboReward for general-purpose vision-language reward models in robotics, as well as 2025 work on affordance distillation for robotic manipulation and affordance detection in 3D worlds.

A prominent recent approach is Chain-of-Affordance (CoA-VLA), which incorporates reasoning in the format of sequential robot affordances to facilitate task completion. This model considers four types of affordances before taking action: object affordance (what object to manipulate and where), grasp affordance (the specific object part to grasp), spatial affordance (optimal space to place the object), and movement affordance (collision-free path for movement).

CoA demonstrates superior performance compared to state-of-the-art robot foundation models like OpenVLA and Octo, with strong generalization to unseen object poses and the ability to identify free space while avoiding obstacles in novel environments.

Vision-Language-Action (VLA) models have become a dominant paradigm for robotic manipulation, where a large-scale Vision-Language Model compresses multimodal observations into a latent representation, and an action head maps this latent into continuous motor commands.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c31e4363-d1b9-4b8b-92f9-7fbb4cda473c",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "377cc3ea-7607-4f56-b5ad-42767a094ff7",
  "sourceToolAssistantUUID": "c31e4363-d1b9-4b8b-92f9-7fbb4cda473c",
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

### Tool call

_source line 17 · 2026-05-18T19:19:25.323Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JYHxCF84apU8KZqpW7BYsg`</summary>

```json
{
  "query": "\"self-supervised affordance learning manipulation\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "377cc3ea-7607-4f56-b5ad-42767a094ff7",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaHNbad7m39gZhEzqzD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e984770-6348-4f78-a65f-5d76b9a5c96a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQN4DuSNFn8k3MuVggp7LW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 13906,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 980
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 13906,
          "cache_creation_input_tokens": 980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 980,
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

_source line 18 · 2026-05-18T19:19:33.586Z_

<details><summary>↩ Tool result · `toolu_01JYHxCF84apU8KZqpW7BYsg`</summary>

```text
Web search results for query: ""self-supervised affordance learning manipulation" 2025 2026"

Links: [{"title":"[2305.17565] Self-Supervised Learning of Action Affordances as Interaction Modes","url":"https://ar5iv.labs.arxiv.org/html/2305.17565"},{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://arxiv.org/pdf/2408.10123"},{"title":"Affordance Learning from Play for Sample-Efficient Policy Learning","url":"https://arxiv.org/pdf/2203.00352"},{"title":"Learning Foresightful Dense Visual Affordance for Deformable Object   Manipulation","url":"https://arxiv.org/pdf/2303.11057"},{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Learning_Precise_Affordances_from_Egocentric_Videos_for_Robotic_Manipulation_ICCV_2025_paper.pdf"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"}]

Here are the search results for "self-supervised affordance learning manipulation" from 2025-2026:

**Recent Work (2025)**

A 2025 ICCV paper on learning precise affordances from egocentric videos employs the self-supervised visual foundation model DINOv2, which has been demonstrated to be highly effective for data-limited affordance learning. The approach introduces LoRA to fine-tune the model without modifying the parameters of the original DINOv2.

**Other Recent Developments (2024)**

A December 2024 framework for assistive robot manipulation addresses efficiently adapting large-scale models to downstream scene affordance understanding tasks, especially in daily living scenarios. The work employs a parameter-efficient prompt tuning method for predicting manipulation affordances in multi-task scenarios and proposes learning robot trajectories guided by affordances using a supervised Flow Matching method.

Earlier research has also explored extracting self-supervised visual affordance models from human teleoperated play data to enable efficient policy learning and motion planning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e984770-6348-4f78-a65f-5d76b9a5c96a",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "820c5d88-5e89-400d-8fd8-ade883b68a47",
  "sourceToolAssistantUUID": "2e984770-6348-4f78-a65f-5d76b9a5c96a",
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

### Tool call

_source line 19 · 2026-05-18T19:19:35.872Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MkHUR27aimTZYJY8A51GmZ`</summary>

```json
{
  "query": "\"contrastive affordance robot\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "820c5d88-5e89-400d-8fd8-ade883b68a47",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaJApgvrzxB4oxFiXKX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "914734b1-e2a1-4b38-9b24-5b33c29ef394",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLk7Y5pysKtYaMYfSCgYpC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 14886,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 639
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 14886,
          "cache_creation_input_tokens": 639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 639,
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

_source line 20 · 2026-05-18T19:19:43.929Z_

<details><summary>↩ Tool result · `toolu_01MkHUR27aimTZYJY8A51GmZ`</summary>

```text
Web search results for query: ""contrastive affordance robot" 2025 2026"

Links: [{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Learning_Precise_Affordances_from_Egocentric_Videos_for_Robotic_Manipulation_ICCV_2025_paper.pdf"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/html/2411.02704v1"},{"title":"RT-Affordance: Reasoning about Robotic Manipulation with Affordances","url":"https://openreview.net/pdf?id=s8VMLXKH1X"},{"title":"Visual Affordances: Enabling Robots to Understand Object Functionality","url":"https://arxiv.org/html/2505.05074v1"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"},{"title":"Learning Environment-Aware Affordance for 3D Articulated Object Manipulation under Occlusions","url":"https://arxiv.org/pdf/2309.07510"}]

I found several relevant results about contrastive affordance learning for robots from 2025 and 2024. Here are the key findings:

## Recent Research on Contrastive Affordance for Robots

A novel contrastive affordance learning framework has been developed that can train on scenes containing a single occluder and generalize to scenes with complex occluder combinations, addressing challenges in 3D articulated object manipulation under occlusions.

One approach uses a contrastive loss that encourages pixel-level embeddings within annotated object masks to align with corresponding linguistic features, enabling robots to understand object functionality through visual affordances.

## Applications in Robot Manipulation

Affordance-conditioned policies paired with oracle human-provided affordances achieve 76% performance on grasping tasks, and when employing an affordance prediction model to infer affordances automatically, achieve a 68% success rate.

Recent work extracts both graspable and functional affordances with precise segmentation masks, enabling tool grasping, tool-object interaction, and robot-to-human interactions.

Another framework employs parameter-efficient prompt tuning to predict manipulation affordances in multi-task scenarios, and proposes learning robot trajectories guided by affordances using Flow Matching methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "914734b1-e2a1-4b38-9b24-5b33c29ef394",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "53f9fe4d-c5cd-477f-9b23-424b3c77b566",
  "sourceToolAssistantUUID": "914734b1-e2a1-4b38-9b24-5b33c29ef394",
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

### Tool call

_source line 21 · 2026-05-18T19:19:46.665Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LGkZ9u8gBdyRusPZxJdekB`</summary>

```json
{
  "query": "\"paraphrase consistency robot policy\" OR \"instruction invariance robot\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53f9fe4d-c5cd-477f-9b23-424b3c77b566",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaJw2kVASiawqLougpr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9d45649-af68-4224-b9d3-bdc07c19baf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGPBjCKsZ68shZmci161Uc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 15525,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 838
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 15525,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 838,
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

_source line 22 · 2026-05-18T19:19:52.936Z_

<details><summary>↩ Tool result · `toolu_01LGkZ9u8gBdyRusPZxJdekB`</summary>

```text
Web search results for query: ""paraphrase consistency robot policy" OR "instruction invariance robot""

Links: [{"title":"Ctrl-World: A Controllable Generative World Model for Robot Manipulation","url":"https://arxiv.org/html/2510.10125v1"},{"title":"Salience-Invariant Consistent Policy Learning for Generalization","url":"https://arxiv.org/pdf/2502.08336"},{"title":"Invariance Co-training for Robot Visual Generalization","url":"https://arxiv.org/pdf/2512.05230"},{"title":"Consistency Policy: Accelerated Visuomotor Policies via Consistency   Distillation","url":"https://arxiv.org/pdf/2405.07503"},{"title":"Symmetry Considerations for Learning Task Symmetric Robot Policies","url":"https://arxiv.org/pdf/2403.04359"},{"title":"Hybrid Consistency Policy: Decoupling Multi-Modal Diversity and Real-Time Efficiency in Robotic Manipulation","url":"https://arxiv.org/pdf/2510.26670"}]

I've completed the web search for your query. Here are the relevant results:

The search returned several papers related to robot policies and consistency mechanisms:

1. **Ctrl-World: A Controllable Generative World Model for Robot Manipulation** - This work uses paraphrase instructions for robots, such as transforming "place glove in box" into "pick up the cloth and put it inside the box", demonstrating instruction paraphrasing for consistency.

2. **Salience-Invariant Consistent Policy Learning for Generalization** - This paper focuses on salience-invariant consistent policy learning in visual reinforcement learning, with a policy consistency module that maintains consistency in action distributions.

3. **Invariance Co-training for Robot Visual Generalization** - This work presents a method for aligning robot policy encoder representations to improve generalization across multiple observational axes including camera viewpoint, lighting variation, and distractor clutter.

4. **Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation** - This paper proposes Consistency Policy as a faster alternative to Diffusion Policy for learning visuomotor robot control.

5. **Hybrid Consistency Policy: Decoupling Multi-Modal Diversity and Real-Time Efficiency in Robotic Manipulation** - This work proposes the Hybrid Consistency Policy (HCP) which performs time-varying consistency distillation with trajectory-consistency objectives to keep neighboring predictions coherent.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9d45649-af68-4224-b9d3-bdc07c19baf7",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "d7809619-521a-481c-8db3-c74ef581c2f7",
  "sourceToolAssistantUUID": "b9d45649-af68-4224-b9d3-bdc07c19baf7",
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

### Tool call

_source line 23 · 2026-05-18T19:19:55.524Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CKFrmDAo6suNH6nN6gJwc5`</summary>

```json
{
  "query": "\"affordance bottleneck VLA\" OR \"affordance attention VLA\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7809619-521a-481c-8db3-c74ef581c2f7",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaKbazNZcB77ZFHZQ1S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40386dec-9202-4ed0-97bb-0f328da1abd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdTECq17425T4iSoA27eHs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 16363,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 683
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 16363,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 683,
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

_source line 24 · 2026-05-18T19:20:02.748Z_

<details><summary>↩ Tool result · `toolu_01CKFrmDAo6suNH6nN6gJwc5`</summary>

```text
Web search results for query: ""affordance bottleneck VLA" OR "affordance attention VLA""

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"PokéVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance","url":"https://arxiv.org/html/2604.20834v1"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"}]

Based on the search results, I found several relevant papers about affordances in Vision-Language-Action (VLA) models:

## Key Findings:

**1. CoA-VLA (Chain-of-Affordance VLA)**
Chain-of-Affordance (CoA-VLA) is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion. The FiLM-based conditioning acts as a bottleneck, distilling only the most salient affordance cues to guide action generation, thereby avoiding overfitting to redundant visual or linguistic signals.

**2. VLA-IAP (Interaction-Aligned Pruning)**
This framework breaks the Perception-First bottleneck prevalent in existing VLA pruning methods—namely, the over-reliance on the static attention weights of pre-trained Vision-Language Models (VLMs).

**3. Affordance Field Intervention**
3D Spatial Affordance Fields (SAFs) provide a geometric representation that highlights where interactions are physically feasible, and Affordance Field Intervention (AFI) is a lightweight hybrid framework that uses SAFs as an on-demand plugin to guide VLA behavior.

**4. PokéVLA**
An effective embodied pre-training data system includes grounding data to improve language-scene matching generalization, affordance data to enhance action execution robustness, and reasoning data to deepen task understanding.

These papers address different aspects of how affordances and attention mechanisms can improve Vision-Language-Action models for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40386dec-9202-4ed0-97bb-0f328da1abd2",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "82ffe2d9-18cb-4278-8941-e92e932989bb",
  "sourceToolAssistantUUID": "40386dec-9202-4ed0-97bb-0f328da1abd2",
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

### Tool call

_source line 25 · 2026-05-18T19:20:05.698Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BvLLiL5Cs2J7MUtEp9WC6`</summary>

```json
{
  "query": "site:openreview.net \"affordance\" \"vision language action\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82ffe2d9-18cb-4278-8941-e92e932989bb",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaLKXcz2k5TeDNkyP5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e749537-87cb-4052-bf49-c6964ab6594b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AofQghhmH9FeHPYDXSkZLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 17046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 854,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 26 · 2026-05-18T19:20:11.687Z_

<details><summary>↩ Tool result · `toolu_011BvLLiL5Cs2J7MUtEp9WC6`</summary>

```text
Web search results for query: "site:openreview.net "affordance" "vision language action" 2026"

Links: [{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/pdf/2401.06341"},{"title":"3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation | OpenReview","url":"https://openreview.net/forum?id=dT45OMevL5"},{"title":"Context-Dependent Affordance Computation in Vision-Language Models","url":"https://arxiv.org/pdf/2603.04419"},{"title":"Affordance Perception by a Knowledge-Guided Vision-Language Model with   Efficient Error Correction","url":"https://arxiv.org/pdf/2407.13368"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/pdf/2507.01925"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/pdf/2505.04769"},{"title":"Phrase-Based Affordance Detection via Cyclic Bilateral Interaction","url":"https://arxiv.org/pdf/2202.12076"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"}]

The search returned several relevant results about affordance, vision-language models, and vision-language-action (VLA) models. Here are the most relevant papers:

1. **3DS-VLA: A 3D Spatial-Aware Vision Language Action Model** - This work enhances pretrained 2D vision-language models with comprehensive 3D awareness to predict robust end-effector poses, and learns sequential 3D spatial constraints that define affordance-relevant 3D keypoints on objects.

2. **Context-Dependent Affordance Computation in Vision-Language Models** - This January 2026 paper characterizes context-dependent affordance computation in vision-language models, demonstrating through a large-scale study that over 90% of lexical scene description is context-dependent.

3. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance** - This approach incorporates reasoning in the format of sequential robot affordances, prompting the model to consider four types of affordances: object affordance, grasp affordance, spatial affordance, and movement affordance.

4. **A Survey on Vision-Language-Action Models: An Action Tokenization Perspective** - This comprehensive survey covers affordance as one approach to action tokenization in VLA models.

These papers represent recent research connecting affordance perception with vision-language-action models in robotic manipulation and perception tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e749537-87cb-4052-bf49-c6964ab6594b",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "b22fb47f-fa42-4fd7-97a5-b9d3b28e24b5",
  "sourceToolAssistantUUID": "6e749537-87cb-4052-bf49-c6964ab6594b",
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

_source line 27 · 2026-05-18T19:20:14.834Z_

Now let me run a few more targeted searches to find any papers that might specifically combine all three elements (end-to-end affordance-within-VLA, open-vocabulary language conditioning, and self-supervised consistency).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b22fb47f-fa42-4fd7-97a5-b9d3b28e24b5",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaLyin567sQWGVin5WZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aaf01726-31d4-441b-b7b1-96129ea09231",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPuSgmFuPXM1eBHiRuHLYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 17900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 790,
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

_source line 28 · 2026-05-18T19:20:15.624Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CZQq84ix9p7SgwTt91AtkM`</summary>

```json
{
  "query": "RT-Affordance arxiv 2411.02704 end-to-end VLA affordance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaf01726-31d4-441b-b7b1-96129ea09231",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaLyin567sQWGVin5WZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16c75aa8-2666-44b7-96ae-6c846fce5565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPuSgmFuPXM1eBHiRuHLYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 17900,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 790
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 17900,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 790,
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

_source line 29 · 2026-05-18T19:20:22.756Z_

<details><summary>↩ Tool result · `toolu_01CZQq84ix9p7SgwTt91AtkM`</summary>

```text
Web search results for query: "RT-Affordance arxiv 2411.02704 end-to-end VLA affordance"

Links: [{"title":"[2411.02704] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/abs/2411.02704"},{"title":"RT-Affordance: Affordances are Versatile","url":"https://i-newcar.com/uploads/ueditor/20241225/2-24122510155CF.pdf"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/html/2411.02704"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.researchgate.net/publication/385560182_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"},{"title":"RT-Affordance: Reasoning about Robotic Manipulation with Affordances","url":"https://openreview.net/pdf?id=s8VMLXKH1X"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"}]

Based on the search results, here's what I found about RT-Affordance (arxiv 2411.02704):

## Overview

RT-Affordance is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation.

## Key Approach

The method conditions policies on affordances, which capture the pose of the robot at key stages of the task. Affordances provide precise spatial guidance on how to perform a manipulation task, and they are easy for humans to specify.

## Advantages Over Existing Methods

Existing representations such as language, goal images, and trajectory sketches have been shown to be helpful, but these representations either do not provide enough context or provide over-specified context that yields less robust policies. In contrast, the paper shows that affordances offer a better balance.

## Performance Results

When compared to state-of-the-art VLAs including language-conditioned and goal-conditioned policies that achieve success rates under 30%, the affordance-conditioned policy with oracle human-provided affordances achieves 76% performance, and when employing an affordance prediction model to infer affordance automatically, a 68% success rate is observed.

The paper was submitted on November 5, 2024, and explores how affordances can serve as versatile intermediate representations for improving robot manipulation capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16c75aa8-2666-44b7-96ae-6c846fce5565",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "bfb6041f-c152-4566-88a9-3436f2ff2490",
  "sourceToolAssistantUUID": "16c75aa8-2666-44b7-96ae-6c846fce5565",
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

### Tool call

_source line 30 · 2026-05-18T19:20:26.441Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YEGUUKP1c5q3uormtTs4Gr`</summary>

```json
{
  "query": "A0 affordance-aware hierarchical model 2504.12636 zero-shot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfb6041f-c152-4566-88a9-3436f2ff2490",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaMo2NhKdxHBtL3XTvD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "951f0a56-f2d0-48b1-8c7d-1997b09f4f1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017q84rMshcA2uSCDdTTq851",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 18690,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 834
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 18690,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 834,
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

_source line 31 · 2026-05-18T19:20:32.483Z_

<details><summary>↩ Tool result · `toolu_01YEGUUKP1c5q3uormtTs4Gr`</summary>

```text
Web search results for query: "A0 affordance-aware hierarchical model 2504.12636 zero-shot manipulation"

Links: [{"title":"250412636 — Grokipedia","url":"https://grokipedia.com/page/250412636"},{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://arxiv.org/pdf/2504.12636"},{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation | Request PDF","url":"https://www.researchgate.net/publication/390892539_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation"},{"title":"[2504.12636] A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://arxiv.org/abs/2504.12636"},{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulatione","url":"https://a-embodied.github.io/A0/"},{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation_ICCV_2025_paper.pdf"},{"title":"[Literature Review] A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://www.themoonlight.io/en/review/a0-an-affordance-aware-hierarchical-model-for-general-robotic-manipulation"},{"title":"dblp: A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation.","url":"https://dblp.org/rec/journals/corr/abs-2504-12636.html"}]

Based on the web search results, here's what I found about the A0 affordance-aware hierarchical model (arXiv preprint 2504.12636):

## Overview

A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation is a 2025 computer science paper submitted on April 29, 2025, authored by Rongtao Xu, Jian Zhang, Minghao Guo, Youpeng Wen, Haoting Yang, Min Yang, and Xiaodan Liang. It was accepted for presentation at the International Conference on Computer Vision (ICCV) 2025.

## Key Innovation

The key innovation of A0 lies in its affordance-aware hierarchy, which facilitates zero-shot and few-shot adaptation to new objects and tasks without extensive retraining, marking a step toward more autonomous robotic systems.

## Technical Approach

A0 is a hierarchical affordance-aware diffusion model that decomposes manipulation tasks into high-level spatial affordance understanding and low-level action execution. A0 leverages the Embodiment-Agnostic Affordance Representation, which captures object-centric spatial affordances by predicting contact point and post-contact trajectories. A0 is pre-trained on 1 million contact points data and fine-tuned on annotated trajectories, enabling generalization across platforms.

## Performance

The method achieves an average success rate of 62.50% on Franka and 53.75% on Kinova, outperforming the strongest baselines on both platforms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "951f0a56-f2d0-48b1-8c7d-1997b09f4f1a",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "3043b182-59cf-4f88-9c74-3dc2100e00ce",
  "sourceToolAssistantUUID": "951f0a56-f2d0-48b1-8c7d-1997b09f4f1a",
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

### Tool call

_source line 32 · 2026-05-18T19:20:35.282Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cqm2i1omg9FEqbHr6vEAKV`</summary>

```json
{
  "query": "\"affordance\" \"language grounding\" \"self-supervised\" OR \"contrastive\" \"end-to-end\" robot 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3043b182-59cf-4f88-9c74-3dc2100e00ce",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaNWdAvSrnBxnsa98bf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7444f38-282c-4daa-b3d6-cf68e81dbb87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfNfPiswLHhhQXGMpP5KMZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 19524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 965,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 33 · 2026-05-18T19:20:42.403Z_

<details><summary>↩ Tool result · `toolu_01Cqm2i1omg9FEqbHr6vEAKV`</summary>

```text
Web search results for query: ""affordance" "language grounding" "self-supervised" OR "contrastive" "end-to-end" robot 2025 2026 arxiv"

Links: [{"title":"[2508.06206] Affordance-R1: Reinforcement Learning for Generalizable Affordance Reasoning in Multimodal Large Language Model","url":"https://arxiv.org/abs/2508.06206"},{"title":"[2508.07877v1] Selective Contrastive Learning for Weakly Supervised Affordance Grounding","url":"https://arxiv.org/abs/2508.07877v1"},{"title":"Grounding Language with Visual Affordances over Unstructured Data","url":"https://arxiv.org/pdf/2210.01911"},{"title":"[2210.01911] Grounding Language with Visual Affordances over Unstructured Data","url":"https://ar5iv.labs.arxiv.org/html/2210.01911"},{"title":"[2508.07877] Selective Contrastive Learning for Weakly Supervised Affordance Grounding","url":"https://arxiv.org/abs/2508.07877"},{"title":"O3Afford: One-Shot 3D Object-to-Object Affordance Grounding for Generalizable Robotic Manipulation","url":"https://arxiv.org/html/2509.06233v1"},{"title":"[PDF] Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Do-As-I-Can,-Not-As-I-Say:-Grounding-Language-in-Ahn-Brohan/cb5e3f085caefd1f3d5e08637ab55d39e61234fc"}]

I found several recent arxiv papers matching your search criteria. Here are the key results:

## Recent Papers (2025-2026)

**1. Affordance-R1: Reinforcement Learning for Generalizable Affordance Reasoning in Multimodal Large Language Model**
- arXiv: 2508.06206 (August 2025)
- Focuses on affordance grounding to predict specific regions of objects associated with robot actions
- Trained via reinforcement learning with GRPO without explicit reasoning data, achieving zero-shot generalization

**2. Selective Contrastive Learning for Weakly Supervised Affordance Grounding**
- arXiv: 2508.07877 (August 2025)
- Seeks to learn from third-person demonstrations without pixel-level annotations
- Introduces selective prototypical and pixel contrastive objectives to learn affordance-relevant cues at part and object levels

**3. O3Afford: One-Shot 3D Object-to-Object Affordance Grounding for Generalizable Robotic Manipulation**
- arXiv: 2509.06233 (September 2025)
- Recent work on generalizable robotic affordance grounding

## Earlier Related Work (2022-2024)

**4. Grounding Language with Visual Affordances over Unstructured Data**
- arXiv: 2210.01911 (March 2024)
- Proposes learning language-conditioned robot skills from unstructured, offline and reset-free data using a self-supervised visuo-lingual affordance model

These papers cover the intersection of affordance, language grounding, self-supervised/contrastive learning, and end-to-end robot learning you're researching.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7444f38-282c-4daa-b3d6-cf68e81dbb87",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "a1986d2a-968a-4947-9737-1d6fe0f88e29",
  "sourceToolAssistantUUID": "d7444f38-282c-4daa-b3d6-cf68e81dbb87",
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

### Tool call

_source line 34 · 2026-05-18T19:20:45.201Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T1RN8Z4SrZmk1VVw3Qp6cy`</summary>

```json
{
  "query": "2602.10109 arxiv ICLR 2026 affordance VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1986d2a-968a-4947-9737-1d6fe0f88e29",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaPF2LRMU6eYxokrGwd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75469497-d3ce-416d-ba5f-74962498383f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WvLi9HSj7bwanqmkiUrkKf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 969,
      "cache_read_input_tokens": 20489,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 969
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 20489,
          "cache_creation_input_tokens": 969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 969,
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

_source line 35 · 2026-05-18T19:20:52.929Z_

<details><summary>↩ Tool result · `toolu_01T1RN8Z4SrZmk1VVw3Qp6cy`</summary>

```text
Web search results for query: "2602.10109 arxiv ICLR 2026 affordance VLA"

Links: [{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10109"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"Context-Dependent Affordance Computation in Vision-Language Models","url":"https://arxiv.org/pdf/2603.04419"},{"title":"[2602.10109] ST4VLA: Spatially Guided Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.10109"},{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"}]

Based on the search results, I found the paper you're looking for:

ST4VLA is a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs. ST4VLA includes two stages: spatial grounding pre-training, which equips the VLM with transferable priors via scalable point, box, and trajectory prediction from both web-scale and robot-specific data, and spatially guided action post-training, which encourages the model to produce richer spatial priors to guide action generation via spatial prompting.

Empirically, ST4VLA achieves substantial improvements over vanilla VLA, with performance increasing from 66.1 → 84.6 on Google Robot and from 54.7 → 73.2 on WidowX Robot, establishing new state-of-the-art results on SimplerEnv. It also demonstrates stronger generalization to unseen objects and paraphrased instructions, as well as robustness to long-horizon perturbations in real-world settings.

The paper (arxiv 2602.10109) was published as a conference paper at ICLR 2026 and focuses on improving Vision-Language-Action models through spatially guided training with affordance-related capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75469497-d3ce-416d-ba5f-74962498383f",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "e655ea68-c1fd-4c26-b65d-8f74ca8de078",
  "sourceToolAssistantUUID": "75469497-d3ce-416d-ba5f-74962498383f",
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

### Tool call

_source line 36 · 2026-05-18T19:20:55.503Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SMp1iQQbcyS3nZe13gtqSz`</summary>

```json
{
  "query": "Affordance Field Intervention 2512.07472 VLA memory traps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e655ea68-c1fd-4c26-b65d-8f74ca8de078",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaQ1znN1yAtCETjVcba",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19941f59-249c-42f3-87a9-f02c694ee6d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019e2K65DREfLJGrMwfkHAfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 21458,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 742
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 21458,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 742,
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

_source line 37 · 2026-05-18T19:21:00.820Z_

<details><summary>↩ Tool result · `toolu_01SMp1iQQbcyS3nZe13gtqSz`</summary>

```text
Web search results for query: "Affordance Field Intervention 2512.07472 VLA memory traps"

Links: [{"title":"[2512.07472] Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://www.arxiv.org/abs/2512.07472"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/html/2512.07472v1"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in","url":"https://www.arxiv.org/pdf/2512.07472"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"Volatile memory cell with interface charge traps","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5608250"}]

Based on the search results, here's what I found about the paper arxiv 2512.07472:

## Paper Overview

Vision-Language-Action (VLA) models have shown great performance in robotic manipulation by mapping visual observations and language instructions directly to actions. However, the paper addresses a critical limitation.

## The Memory Trap Problem

VLAs often remain brittle under distribution shifts: when test scenarios change, VLAs often reproduce memorized trajectories instead of adapting to the updated scene, which is a failure mode referred to as the "Memory Trap". This limitation stems from the end-to-end design, which lacks explicit 3D spatial reasoning and prevents reliable identification of actionable regions in unfamiliar environments.

## The Solution: Affordance Field Intervention (AFI)

To compensate for this missing spatial understanding, 3D Spatial Affordance Fields (SAFs) can provide a geometric representation that highlights where interactions are physically feasible. The authors introduce Affordance Field Intervention (AFI), a lightweight hybrid framework that uses SAFs as an on-demand plug-in to guide VLA behavior.

The system detects memory traps through proprioception, repositions the robot to recent high-affordance regions, and proposes affordance-driven waypoints that anchor VLA-generated actions. A SAF-based scorer then selects trajectories with the highest cumulative affordance.

## Results

The method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19941f59-249c-42f3-87a9-f02c694ee6d3",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "603a7e4c-f4dc-4fa2-be52-74a4b840ba13",
  "sourceToolAssistantUUID": "19941f59-249c-42f3-87a9-f02c694ee6d3",
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

### Tool call

_source line 38 · 2026-05-18T19:21:03.999Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VUJqyuu7aTajYfdUQLoKUw`</summary>

```json
{
  "query": "\"3DS-VLA\" OR \"Affogato\" OR \"AffordBot\" affordance VLA open vocabulary 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "603a7e4c-f4dc-4fa2-be52-74a4b840ba13",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaQbn32ForepVh6Nzfk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd57f2e1-80d7-45a3-8ab7-897b64e16e8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3msAkNDLpY5VFwA9TNA8Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 22200,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 726
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 22200,
          "cache_creation_input_tokens": 726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 726,
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

_source line 39 · 2026-05-18T19:21:12.536Z_

<details><summary>↩ Tool result · `toolu_01VUJqyuu7aTajYfdUQLoKUw`</summary>

```text
Web search results for query: ""3DS-VLA" OR "Affogato" OR "AffordBot" affordance VLA open vocabulary 2025 2026"

Links: [{"title":"3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation","url":"https://proceedings.mlr.press/v305/li25g.html"},{"title":"3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation | OpenReview","url":"https://openreview.net/forum?id=dT45OMevL5"},{"title":"(PDF) Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale","url":"https://www.researchgate.net/publication/392716806_Affogato_Learning_Open-Vocabulary_Affordance_Grounding_with_Automated_Data_Generation_at_Scale"},{"title":"Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale","url":"https://arxiv.org/pdf/2506.12009"},{"title":"GitHub - hq-King/Awesome-Affordance-Learning · GitHub","url":"https://github.com/hq-King/Awesome-Affordance-Learning"}]

I found information about two of the three models you searched for. Here are the results:

## 3DS-VLA

3DS-VLA is a 3D Spatial-Aware Vision Language Action Model that enhances pretrained 2D vision-language models with comprehensive 3D awareness, enabling the prediction of robust end-effector poses. The model learns sequential 3D spatial constraints that define affordance-relevant 3D keypoints on objects, ensuring robust interactions. The research was published at the 9th Conference on Robot Learning in 2025.

## Affogato

Affogato is a large-scale benchmark comprising 150K instances, annotated with open-vocabulary text descriptions and corresponding 3D affordance heatmaps across a diverse set of objects and interactions. The dataset is automatically generated by the Affogato-Engine pipeline, which leverages multi-view renderings and state-of-the-art vision-language models to create high-quality affordance annotations with diverse object categories. Models trained with the Affogato dataset achieve promising performance on existing 2D and 3D benchmarks and show effectiveness in open-vocabulary cross-domain generalization.

## AffordBot

I did not find specific information about "AffordBot" in the search results. Would you like me to perform another search specifically for that model?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd57f2e1-80d7-45a3-8ab7-897b64e16e8d",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "a68964433f38e0acc",
  "type": "user",
  "uuid": "8b9ba367-f408-4fcd-8509-669cce9dfa33",
  "sourceToolAssistantUUID": "cd57f2e1-80d7-45a3-8ab7-897b64e16e8d",
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

_source line 40 · 2026-05-18T19:21:38.709Z_

Here is my consolidated report on potentially competing/concurrent work that may challenge the LACVLA gap claim.

---

## Exhaustive Search Results: Competing Work for LACVLA

### HIGH-THREAT papers (touch 2+ of the 3 claimed novelty axes)

**1. CoA-VLA** (arXiv [2412.20451](https://arxiv.org/abs/2412.20451), ICCV 2025)
Integrates affordance reasoning directly inside a VLA via a "chain-of-affordance" that produces four affordance types (object, grasp, spatial, movement) as intermediate representations before action prediction. Uses FiLM-based conditioning as a bottleneck. Hits axes (a) end-to-end affordance-within-VLA and (b) language-conditioned affordance. Does NOT use self-supervised consistency objectives. **Strongest single competitor -- must be cited and differentiated.**

**2. RT-Affordance** (arXiv [2411.02704](https://arxiv.org/abs/2411.02704))
Language-conditioned affordance plan predicts end-effector poses at key task stages; a downstream policy is conditioned on these affordances. Covers (a) affordance as intermediate VLA representation and (b) language conditioning. Two-stage (not fully end-to-end) and no self-supervised consistency, but very close in spirit.

**3. ST4VLA** (arXiv [2602.10109](https://arxiv.org/abs/2602.10109), ICLR 2026)
Spatial grounding pre-training + spatially guided action post-training inside a VLA. Reports robustness to paraphrased instructions (touching axis (c) implicitly). Does not frame this as a self-supervised consistency loss, but the paraphrase-robustness result may weaken the novelty claim.

**4. A0** (arXiv [2504.12636](https://arxiv.org/abs/2504.12636), ICCV 2025)
Affordance-aware hierarchical diffusion model with embodiment-agnostic affordance representation enabling zero-shot/few-shot cross-category transfer. Covers (a) and partly (b). No self-supervised consistency.

### MODERATE-THREAT papers (touch 1 axis strongly, relevant context)

**5. Affordance Field Intervention (AFI)** (arXiv [2512.07472](https://arxiv.org/abs/2512.07472))
Plugs 3D spatial affordance fields into VLAs at inference time. Not end-to-end training, but shows affordance-VLA integration is an active line.

**6. Affogato** (arXiv [2506.12009](https://arxiv.org/abs/2506.12009))
150K-instance open-vocabulary affordance benchmark with cross-domain generalization. Covers axis (b) strongly. No VLA integration or consistency loss.

**7. Selective Contrastive Learning for Weakly-Supervised Affordance Grounding** (arXiv [2508.07877](https://arxiv.org/abs/2508.07877))
Contrastive objectives for affordance learning without pixel annotations. Touches axis (c) (self-supervised/contrastive affordance) but not within a VLA.

**8. Affordance-R1** (arXiv [2508.06206](https://arxiv.org/abs/2508.06206))
RL-based affordance reasoning in a multimodal LLM achieving zero-shot generalization. Covers (b) open-vocab affordance; no VLA action head or consistency loss.

**9. 3DS-VLA** ([OpenReview](https://openreview.net/forum?id=dT45OMevL5), CoRL 2025)
3D spatial affordance keypoints inside a VLA. Covers (a); limited open-vocabulary scope.

### Assessment of the Gap Claim

No single paper found combines all three axes: (a) end-to-end affordance-within-VLA training, (b) open-vocabulary language conditioning of affordance, AND (c) self-supervised consistency objectives. The gap claim appears **defensible but narrow**. CoA-VLA and RT-Affordance cover (a)+(b); contrastive affordance papers cover (c) outside VLAs. The proposal must explicitly position against CoA-VLA (strongest overlap) and ST4VLA (paraphrase robustness). If any of these papers are missing from the LACVLA related-work section, they should be added immediately.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b9ba367-f408-4fcd-8509-669cce9dfa33",
  "isSidechain": true,
  "agentId": "a68964433f38e0acc",
  "requestId": "req_011CbAaRTw2rQbb2oa47ur1r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "098d2e7d-aed8-4968-93a1-537d04442363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTCNQrsfZfTbqJYAeqQpLA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 22926,
      "output_tokens": 1092,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 834
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1092,
          "cache_read_input_tokens": 22926,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 834,
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
