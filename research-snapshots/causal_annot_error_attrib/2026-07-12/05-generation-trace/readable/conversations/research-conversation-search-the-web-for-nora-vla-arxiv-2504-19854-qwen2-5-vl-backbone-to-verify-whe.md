# Research conversation: Search the web for "NORA VLA arXiv 2504.19854 Qwen2.5-VL backbone" to verify whether NORA uses Qwen2.5-VL-3B and its cur

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 8
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7bb7cc854d46b15a.jsonl`
- **Structured JSON:** [`4ba2fce7425fa3efb44f.json`](../../sessions/4b/4ba2fce7425fa3efb44f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

8 recorded events

### User

_source line 1 · 2026-05-18T19:54:22.640Z_

Search the web for "NORA VLA arXiv 2504.19854 Qwen2.5-VL backbone" to verify whether NORA uses Qwen2.5-VL-3B and its current status. Report the backbone model, training approach, and any venue acceptance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "de7b063e-e998-4f8b-bec5-7e5f2e4ba93e",
  "agentId": "a7bb7cc854d46b15a",
  "type": "user",
  "uuid": "a6d89165-9eae-41ba-ad9e-5d9feeccd900",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d60dc2fe-5124-410c-b46b-84f3dc0aa976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-18T19:54:24.274Z_

I'll search the web for information about NORA VLA and the specific arXiv paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6d89165-9eae-41ba-ad9e-5d9feeccd900",
  "isSidechain": true,
  "agentId": "a7bb7cc854d46b15a",
  "requestId": "req_011CbAcxARREG1yjvPC5PZVB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f69c8a45-18a9-40a7-9453-2c651f01db98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d60dc2fe-5124-410c-b46b-84f3dc0aa976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NjCnquarZcNy8sXfQP3NWR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16649,
      "cache_read_input_tokens": 0,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16649
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16649,
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

### Tool call

_source line 3 · 2026-05-18T19:54:24.337Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S6GF1mTife9CEu1eMzxieQ`</summary>

```json
{
  "query": "NORA VLA arXiv 2504.19854 Qwen2.5-VL backbone"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f69c8a45-18a9-40a7-9453-2c651f01db98",
  "isSidechain": true,
  "agentId": "a7bb7cc854d46b15a",
  "requestId": "req_011CbAcxARREG1yjvPC5PZVB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5271a578-3c3b-4964-bfb6-81e111a9a6bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d60dc2fe-5124-410c-b46b-84f3dc0aa976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NjCnquarZcNy8sXfQP3NWR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16649,
      "cache_read_input_tokens": 0,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16649
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16649,
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

_source line 4 · 2026-05-18T19:54:31.198Z_

<details><summary>↩ Tool result · `toolu_01S6GF1mTife9CEu1eMzxieQ`</summary>

```text
Web search results for query: "NORA VLA arXiv 2504.19854 Qwen2.5-VL backbone"

Links: [{"title":"[2504.19854] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/abs/2504.19854"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/html/2504.19854"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks","url":"https://arxiv.org/pdf/2504.19854"},{"title":"declare-lab/nora · Hugging Face","url":"https://huggingface.co/declare-lab/nora"},{"title":"GitHub - ehaller00/NORA-VLA: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub","url":"https://github.com/ehaller00/NORA-VLA"},{"title":"Qwen2.5-VL: Architecture, Data, Benchmarks and Inference","url":"https://debuggercafe.com/qwen2-5-vl/"},{"title":"NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards","url":"https://arxiv.org/pdf/2511.14659"},{"title":"GitHub - declare-lab/nora: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub","url":"https://github.com/declare-lab/nora"},{"title":"Qwen2.5-VL Technical Report","url":"https://arxiv.org/pdf/2502.13923"}]

Based on the search results, here's what I found about NORA VLA with the Qwen2.5-VL backbone:

## Overview

NORA is a 3B-parameter model designed to reduce computational overhead while maintaining strong task performance, adopting the Qwen-2.5-VL-3B multimodal model as its backbone to enhance visual reasoning and action grounding.

## Key Characteristics

Existing VLA models face limitations in visual encoding that can result in failures during tasks such as object grasping, and typically suffer from high computational overhead due to their large sizes, often exceeding 7B parameters. NORA addresses these issues through its more efficient 3B architecture.

## Architecture and Training

NORA is trained on 970k real-world robot demonstrations and equipped with the FAST+ tokenizer for efficient action sequence generation. The Qwen-2.5-VL-3B backbone was chosen due to its outstanding performance in vision-language understanding, providing significant gains in multimodal reasoning and task execution.

## Functionality

NORA is an open vision-language-action model trained on robot manipulation episodes from the Open X-Embodiment dataset, taking language instructions and camera images as input to generate robot actions.

The paper (arXiv 2504.19854) was published on April 28, 2025, and the model is openly available under an MIT License on Hugging Face and GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5271a578-3c3b-4964-bfb6-81e111a9a6bf",
  "isSidechain": true,
  "promptId": "de7b063e-e998-4f8b-bec5-7e5f2e4ba93e",
  "agentId": "a7bb7cc854d46b15a",
  "type": "user",
  "uuid": "cf899ac5-0748-4f39-8aff-1109bdaf2225",
  "sourceToolAssistantUUID": "5271a578-3c3b-4964-bfb6-81e111a9a6bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d60dc2fe-5124-410c-b46b-84f3dc0aa976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-18T19:54:36.440Z_

Let me fetch the arXiv paper details to get more specific information about the backbone model and training approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf899ac5-0748-4f39-8aff-1109bdaf2225",
  "isSidechain": true,
  "agentId": "a7bb7cc854d46b15a",
  "requestId": "req_011CbAcxo5opvebwQNVyfSzA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9fdc35d2-6de1-4e88-971b-89b24143c6b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d60dc2fe-5124-410c-b46b-84f3dc0aa976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VD319XSx1QohateKhPLA5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 16649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1688,
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

_source line 6 · 2026-05-18T19:54:36.876Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lxxrko5kPBcRSgHLvuojYF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.19854",
  "prompt": "What is the backbone model used? What is the training approach? Has this paper been accepted at a venue?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fdc35d2-6de1-4e88-971b-89b24143c6b1",
  "isSidechain": true,
  "agentId": "a7bb7cc854d46b15a",
  "requestId": "req_011CbAcxo5opvebwQNVyfSzA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "338bd310-1ec4-4b83-9b35-3799f9474c07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d60dc2fe-5124-410c-b46b-84f3dc0aa976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VD319XSx1QohateKhPLA5e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 16649,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1688
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 127,
          "cache_read_input_tokens": 16649,
          "cache_creation_input_tokens": 1688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1688,
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

_source line 7 · 2026-05-18T19:54:40.450Z_

<details><summary>↩ Tool result · `toolu_01Lxxrko5kPBcRSgHLvuojYF`</summary>

```text
# NORA Paper Summary

**Backbone Model:**
The model uses "Qwen-2.5-VL-3B multimodal model as its backbone, leveraging its superior visual-semantic understanding."

**Training Approach:**
NORA was trained on 970k real-world robot demonstrations and employs "the FAST+ tokenizer for efficient action sequence generation."

**Venue Acceptance:**
The document does not indicate this paper has been accepted at a conference or journal. It was submitted to arXiv on April 28, 2025, and is currently in preprint status with no acceptance information provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "338bd310-1ec4-4b83-9b35-3799f9474c07",
  "isSidechain": true,
  "promptId": "de7b063e-e998-4f8b-bec5-7e5f2e4ba93e",
  "agentId": "a7bb7cc854d46b15a",
  "type": "user",
  "uuid": "3241c555-92ae-4c9b-80b3-e7bd9fee68b1",
  "sourceToolAssistantUUID": "338bd310-1ec4-4b83-9b35-3799f9474c07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d60dc2fe-5124-410c-b46b-84f3dc0aa976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-18T19:54:44.453Z_

## Summary

Based on my search and verification of the arXiv paper (2504.19854):

**Backbone Model:**
NORA uses **Qwen2.5-VL-3B** as its backbone, specifically the Qwen-2.5-VL multimodal model with 3 billion parameters. This was chosen for its superior visual-semantic understanding and outstanding performance in vision-language understanding.

**Training Approach:**
- Trained on **970k real-world robot demonstrations** from the Open X-Embodied dataset
- Uses the **FAST+ tokenizer** for efficient action sequence generation
- Designed for robot manipulation tasks, taking language instructions and camera images as input to generate robot actions

**Venue Acceptance:**
The paper (arXiv 2504.19854) was posted on April 28, 2025, and **is currently in preprint status with no conference or journal acceptance indicated**. The model is openly available under an MIT License on Hugging Face and GitHub repositories maintained by declare-lab.

**Current Status:**
NORA is actively maintained as an open-source project with public repositories and model releases available for use.

Sources:
- [NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks (arXiv 2504.19854)](https://arxiv.org/abs/2504.19854)
- [NORA HTML Version](https://arxiv.org/html/2504.19854)
- [NORA on Hugging Face](https://huggingface.co/declare-lab/nora)
- [NORA on GitHub](https://github.com/declare-lab/nora)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3241c555-92ae-4c9b-80b3-e7bd9fee68b1",
  "isSidechain": true,
  "agentId": "a7bb7cc854d46b15a",
  "requestId": "req_011CbAcyUWspWBf7iF4v94qa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c687ac6b-2fe0-436e-84f7-d6ade44e9623",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d60dc2fe-5124-410c-b46b-84f3dc0aa976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cug9etNknPtRE99zE92hyA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 18337,
      "output_tokens": 391,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 275
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 391,
          "cache_read_input_tokens": 18337,
          "cache_creation_input_tokens": 275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 275,
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
