# Research conversation: I'm reviewing a VLA robustness paper idea. I need to find competing work the generator may have missed. Search for: 1. "

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 1
- **Tool calls:** 31
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8b4d08ae6a7b69fc.jsonl`
- **Structured JSON:** [`0cdcad3d9109a7a2a1e7.json`](../../sessions/0c/0cdcad3d9109a7a2a1e7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

67 recorded events

### User

_source line 1 · 2026-05-14T05:36:07.895Z_

I'm reviewing a VLA robustness paper idea. I need to find competing work the generator may have missed. Search for:

1. "VLA robustness 2026" — any recent methods (not just benchmarks) for improving VLA robustness
2. "vision language action model generalization perturbation 2026" 
3. "token selection robustness manipulation 2026"
4. "information bottleneck visual representation robot 2025 2026"
5. "latent space augmentation robot learning 2025 2026"
6. "adaptive token selection action prediction"
7. Search specifically for work from Physical Intelligence (pi), Google DeepMind, or Berkeley on VLA robustness methods in 2025-2026

Also search for:
8. "RoboPro VLA" — mentioned in the user's landscape as existing work
9. "FastVLA token merging" — mentioned as existing efficiency-only work
10. Any paper that combines information bottleneck with token pruning/selection in ANY domain

Report all findings with titles, venues, and how they relate to the proposed idea. Focus on papers that could undermine the novelty claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "24ca0666-70ad-48b8-9427-3b5b3d991ba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T05:36:07.898Z_

```json
{
  "parentUuid": "24ca0666-70ad-48b8-9427-3b5b3d991ba8",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
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
  "uuid": "97c07ba9-12ff-455e-9c96-0a3837544e26",
  "timestamp": "2026-05-14T05:36:07.898Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-14T05:36:15.322Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BUEfU6A4HmphJdBddLreVP`</summary>

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
  "parentUuid": "97c07ba9-12ff-455e-9c96-0a3837544e26",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vGbqpuC3iAA1M1yjpv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83a2f084-fa01-4a07-9e78-ae49160af37a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCZvwtSKFKFp68wazXHsmk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 811,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 811
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 811,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 811,
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

_source line 4 · 2026-05-14T05:36:15.325Z_

<details><summary>↩ Tool result · `toolu_01BUEfU6A4HmphJdBddLreVP`</summary>

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
  "parentUuid": "83a2f084-fa01-4a07-9e78-ae49160af37a",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "a8fe67bb-3d97-4e88-bd3d-bb9535e3ea98",
  "sourceToolAssistantUUID": "83a2f084-fa01-4a07-9e78-ae49160af37a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-14T05:36:18.706Z_



I'll run all 10 searches in parallel to gather comprehensive results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8fe67bb-3d97-4e88-bd3d-bb9535e3ea98",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vHA8Y1yzntF8GUg3hP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7977263-a03e-4dbe-bf65-14f61f104eb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1gJQqNR6DG21gJXe3xPg7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-14T05:36:19.152Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JruJ1nZncN1GuzMUmoZwzb`</summary>

```json
{
  "query": "VLA robustness 2026 methods improving vision language action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7977263-a03e-4dbe-bf65-14f61f104eb3",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vHA8Y1yzntF8GUg3hP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26a01bd6-b3eb-472c-871f-dc4e5a43629f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1gJQqNR6DG21gJXe3xPg7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9034,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 83,
          "cache_read_input_tokens": 9034,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-14T05:36:28.361Z_

<details><summary>↩ Tool result · `toolu_01JruJ1nZncN1GuzMUmoZwzb`</summary>

```text
Web search results for query: "VLA robustness 2026 methods improving vision language action model"

Links: [{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations | OpenReview","url":"https://openreview.net/forum?id=cS6xizdYD5"},{"title":"Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks | Proceedings of the 2025 Workshop on Large AI Systems and Models with Privacy and Security Analysis","url":"https://dl.acm.org/doi/10.1145/3733800.3763262"},{"title":"[2602.01158] Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/abs/2602.01158"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness","url":"https://arxiv.org/pdf/2509.18953"},{"title":"Improving Robustness of Vision-Language-Action Models ...","url":"https://arxiv.org/pdf/2602.01158"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"},{"title":"VTLA: Vision-Tactile-Language-Action model with preference learning for insertion manipulation | Request PDF","url":"https://www.researchgate.net/publication/403926332_VTLA_Vision-Tactile-Language-Action_model_with_preference_learning_for_insertion_manipulation"},{"title":"ON ROBUSTNESS OF VISION-LANGUAGE-ACTION ...","url":"https://openreview.net/pdf/4c9de20f29e6aad53dfd1f3b339230208e43a2ff.pdf"}]

Based on the web search results, I found several recent methods and approaches for improving Vision-Language-Action (VLA) model robustness in 2026:

## Key Methods for Improving VLA Robustness

**Multi-Modal Robustness Approaches:**

Recent research evaluates and enhances the robustness of VLAs under 17 uncertainties in 4 modalities, recognizing that robustness to real-world perturbations is critical for VLA model deployment. RobustVLA addresses perturbations in VLA inputs and outputs, performing offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective.

**Corruption Restoration Approach:**

The Corruption Restoration Transformer (CRT) is a plug-and-play and model-agnostic vision transformer designed to immunize VLA models against sensor disturbances. CRT uses an adversarial training objective to restore clean observations from corrupted inputs without requiring computationally expensive fine-tuning of the underlying model.

**Architectural Improvements:**

Hierarchical and late fusion architectures achieve the highest manipulation success and generalization, with diffusion-based decoders demonstrating superior cross-domain transfer and robustness compared to autoregressive heads.

**Reinforcement Learning-Based Post-Training:**

RobustVLA introduces a lightweight online RL post-training method with two key regularizations: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations.

**Defense Mechanisms:**

Recommended approaches include incorporating spatial augmentation with systematic rotation and translation variations during training coupled with multi-view consistency, and employing illumination-invariant visual encoders pre-trained on diverse illumination conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26a01bd6-b3eb-472c-871f-dc4e5a43629f",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "01b63e16-9758-4945-912f-7840c6254c4d",
  "sourceToolAssistantUUID": "26a01bd6-b3eb-472c-871f-dc4e5a43629f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T05:36:31.929Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SPngYmmAcvJ6eghAgNMozd`</summary>

```json
{
  "query": "vision language action model generalization perturbation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01b63e16-9758-4945-912f-7840c6254c4d",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vJ7LPXvj7hw7r38tzw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8115219f-871d-472c-8300-31c624155ad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzQQ84wCG9iDVM41L23wv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 10426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1095,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 9 · 2026-05-14T05:36:31.939Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JmfjJdCicugHtEonEBe83m`</summary>

```json
{
  "query": "token selection robustness manipulation 2026 robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8115219f-871d-472c-8300-31c624155ad8",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vJ7LPXvj7hw7r38tzw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64b59fdd-75c3-4918-8155-5ddd97e5bd85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzQQ84wCG9iDVM41L23wv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 10426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1095,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 10 · 2026-05-14T05:36:32.401Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Eug49EMoiP6ZN766qPQmY`</summary>

```json
{
  "query": "information bottleneck visual representation robot learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64b59fdd-75c3-4918-8155-5ddd97e5bd85",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vJ7LPXvj7hw7r38tzw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0127dfb-f780-4285-9465-a8a12c5ac84a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzQQ84wCG9iDVM41L23wv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 10426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1095,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 11 · 2026-05-14T05:36:32.920Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q7JrHYQfazkgVKqbip6tTb`</summary>

```json
{
  "query": "latent space augmentation robot learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0127dfb-f780-4285-9465-a8a12c5ac84a",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vJ7LPXvj7hw7r38tzw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2435341a-1f77-4219-b37a-2cd390d10220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzQQ84wCG9iDVM41L23wv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 10426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1095,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 12 · 2026-05-14T05:36:33.280Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kv7nbSWvwzx2YZ4wsPU1ip`</summary>

```json
{
  "query": "adaptive token selection action prediction VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2435341a-1f77-4219-b37a-2cd390d10220",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vJ7LPXvj7hw7r38tzw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7fd66a0-7595-4a28-bb3d-4f2b51663758",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzQQ84wCG9iDVM41L23wv7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 10426,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1095
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 10426,
          "cache_creation_input_tokens": 1095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1095,
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

_source line 13 · 2026-05-14T05:36:39.748Z_

<details><summary>↩ Tool result · `toolu_01JmfjJdCicugHtEonEBe83m`</summary>

```text
Web search results for query: "token selection robustness manipulation 2026 robot"

Links: [{"title":"Workshop on Manipulation Robustness: Towards Human-Level Robustness under Real-World Challenges","url":"https://manipulation-robustness.github.io/icra2026/"},{"title":"Token Bottleneck: One Token to Remember Dynamics | OpenReview","url":"https://openreview.net/forum?id=x7t7B5CFHm"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://arxiv.org/html/2602.19313v1"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"Robustness-Aware Tool Selection and Manipulation ...","url":"https://arxiv.org/pdf/2506.03362"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding | OpenReview","url":"https://openreview.net/forum?id=k6nTUFoqeT"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"}]

I've completed the web search for "token selection robustness manipulation 2026 robot". Here are the results:

The search returned several relevant research areas and papers from 2025-2026:

1. **Workshop on Manipulation Robustness (ICRA 2026)**: A workshop bringing together robotics researchers to advance the study of manipulation robustness, with the goal of identifying underlying principles that enable manipulation robustness comparable to humans and animals.

2. **Token Bottleneck (ToBo)**: A self-supervised learning pipeline that squeezes a scene into a bottleneck token and predicts the subsequent scene using minimal patches as hints. The approach demonstrates superiority in sequential tasks including robot manipulation, and when deployed on physical robots confirms robustness and effectiveness in real-world environments.

3. **TOPReward**: A method that in real-world deployment on six single-arm SO-100 manipulation tasks consistently improved success rates over standard behavior cloning, achieving up to 10 out of 10 successes on challenging tasks where baseline behavior cloning reaches only 7 out of 10.

4. **Robustness-Aware Tool Selection**: A robustness-aware framework that jointly selects tools and plans contact-rich manipulation trajectories, explicitly optimizing for robustness against environmental disturbances.

5. **Vision-Language-Action (VLA) Models**: These models establish unified token-based policies spanning vision, language, and robotic control with strong zero-shot transfer capabilities.

These results cover recent advances in making robotic manipulation more robust through various token-based and selection mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64b59fdd-75c3-4918-8155-5ddd97e5bd85",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "e74c75be-3fdb-4a77-87ec-3c848349182d",
  "sourceToolAssistantUUID": "64b59fdd-75c3-4918-8155-5ddd97e5bd85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T05:36:39.850Z_

<details><summary>↩ Tool result · `toolu_017Eug49EMoiP6ZN766qPQmY`</summary>

```text
Web search results for query: "information bottleneck visual representation robot learning 2025 2026"

Links: [{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"Revisiting the Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=w10KdRwcMk"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"A Data-Centric Revisit of Pre-Trained Vision Models for Robot Learning Xin Wen1","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Wen_A_Data-Centric_Revisit_of_Pre-Trained_Vision_Models_for_Robot_Learning_CVPR_2025_paper.pdf"},{"title":"Pengxiang Ding 丁鹏翔 - Pengxiang Ding","url":"https://dingpx.github.io/"},{"title":"(PDF) Learning Robust Representations via Multi-View Information Bottleneck","url":"https://www.researchgate.net/publication/339323546_Learning_Robust_Representations_via_Multi-View_Information_Bottleneck"},{"title":"A GENERALIZED INFORMATION BOTTLENECK THEORY OF DEEP LEARNING","url":"https://arxiv.org/pdf/2509.26327"},{"title":"[2509.26327] A Generalized Information Bottleneck Theory of Deep Learning","url":"https://arxiv.org/abs/2509.26327"},{"title":"Representation Learning and the Information Bottleneck Approach","url":"https://www.inference.vc/representation-learning-and-compression-with-the-information-bottleneck/"}]

I've found several relevant results on information bottleneck approaches in robot learning. Here are the key findings:

## Information Bottleneck in Robot Learning (2025-2026)

A recent work addresses "Bridging the Sim-to-Real Gap from the Information Bottleneck Perspective" and proposes the Historical Information Bottleneck (HIB) method to narrow the sim-to-real gap for legged locomotion.

There is also research on "Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation", which applies information bottleneck principles specifically to robot manipulation tasks.

## Recent Vision-Language-Action Models in Robotics

The field has seen significant advances in visual representation learning for robots. Research introduces a semantic bottleneck that reduces the number of prototypes to encourage semantic understanding at patch-level token representations, with attentive pooling over learned patch-level features used to group patches into object-level slots.

## Computational Bottlenecks in Robot Learning

Conventional VLA models using autoregressive decoding introduce a major computational bottleneck due to inherent sequential dependency, which severely restricts response speed in latency-sensitive applications such as high-frequency human-robot interaction or real-time robotic control.

The central challenge in model-data co-design for robotics is data inefficiency, an imbalance between the exponential growth of data volume and the limited computational or memory budgets of embodied agents.

The search results indicate active research into both theoretical information bottleneck frameworks and practical applications in robot learning systems during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0127dfb-f780-4285-9465-a8a12c5ac84a",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "7c0718a6-8f30-4fec-9bce-5faca6fb8d31",
  "sourceToolAssistantUUID": "e0127dfb-f780-4285-9465-a8a12c5ac84a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T05:36:39.883Z_

<details><summary>↩ Tool result · `toolu_01SPngYmmAcvJ6eghAgNMozd`</summary>

```text
Web search results for query: "vision language action model generalization perturbation 2026"

Links: [{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v3"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"Rethinking the Practicality of Vision-language-action Model:","url":"https://arxiv.org/pdf/2602.22663"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"Exploring the Limits of Vision-Language-Action Manipulation in Cross-task Generalization | OpenReview","url":"https://openreview.net/forum?id=h6xQClTm4W"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"DiSCo: Disrupting Semantic Consistency for Transferable Cross-Modal Adversarial Attacks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-6957-1_2"}]

I found several relevant research papers on vision-language-action (VLA) models, generalization, and perturbation analysis from 2025-2026. Here's a summary of key findings:

## Recent Research on VLA Robustness and Generalization

**LIBERO-Plus Analysis (2025)**

Recent comprehensive studies have identified seven core dimensions of perturbation for testing VLA robustness: objects layout, environment background sampling, light variations, camera-view shifts, robot-arm initialization perturbations, LLM-based language rewrites, and image noise.

Current VLAs exhibit brittle generalization across all perturbation factors. However, language perturbations result in the second smallest average performance drop (-25.3) across most models, which is counterintuitive.

**Key Weaknesses Identified**

Current VLA models suffer from: vulnerability to visual shifts due to over-reliance on fixed visual features; inadequate kinematic reasoning with limited generalization across different initial robot configurations; and superficial language interaction where linguistic inputs are often underutilized or ignored.

**Architectural Factors**

Models incorporating a first-person wrist camera demonstrate superior generalization, especially to camera viewpoint changes, compared to those reliant solely on a third-person view.

**Preserving Pretrained Representations (2025)**

Directly finetuning pretrained VLMs on robot data leads to significant representation degradation, with background changes and instruction paraphrases causing large performance drops.

**Cross-Task Generalization (2025)**

Current VLA models, despite being trained on diverse datasets, struggle to generalize effectively to unseen tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8115219f-871d-472c-8300-31c624155ad8",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "994913c1-53b9-49f2-ad2a-50fcd6f98794",
  "sourceToolAssistantUUID": "8115219f-871d-472c-8300-31c624155ad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T05:36:42.930Z_

<details><summary>↩ Tool result · `toolu_01Kv7nbSWvwzx2YZ4wsPU1ip`</summary>

```text
Web search results for query: "adaptive token selection action prediction VLA"

Links: [{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/html/2605.07931v1"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175v2"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/803c4427-374f-4604-8e9e-01a4ba26ea19.pdf"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation ...","url":"https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257"},{"title":"(PDF) VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://www.researchgate.net/publication/388685612_VLA-Cache_Towards_Efficient_Vision-Language-Action_Model_via_Adaptive_Token_Caching_in_Robotic_Manipulation/fulltext/67a2d84c8311ce680c52f13c/VLA-Cache-Towards-Efficient-Vision-Language-Action-Model-via-Adaptive-Token-Caching-in-Robotic-Manipulation.pdf?origin=scientificContributions"},{"title":"𝐴₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/html/2604.05672"}]

Based on the search results, I found several relevant papers and approaches related to adaptive token selection for action prediction in Vision-Language-Action (VLA) models:

## Key Findings:

### VLA-Cache: Adaptive Token Caching
VLA-Cache reduces redundant computation while preserving high-fidelity action predictions by selectively updating only task-relevant tokens. The approach includes dynamic token selection to identify and filter task-relevant tokens, with the fraction of reused tokens dynamically adjusted at each layer based on attention distribution.

### VLA-IAP: Interaction-First Token Pruning
VLA-IAP is a training-free visual token pruning framework that shifts embodied visual compression from a passive Perception-First bias to an explicit Interaction-First paradigm. This method leverages motion-aware spatiotemporal dynamics and geometric structures for pruning, achieving efficient inference while improving task success rates.

### OneWM-VLA: Single-Token Bottleneck
A lightweight Adaptive Attention Pooling distills each view into a single semantic latent token per frame, maintaining per-frame visual bandwidth at one token. Research found that per-frame visual bandwidth can be reduced to a single token without compromising long-horizon performance.

### TTF-VLA: Temporal Token Fusion
A training-free temporal token fusion framework intelligently integrates historical and current visual representations, combining efficient grayscale pixel difference analysis with attention-guided semantic relevance assessment.

These approaches collectively demonstrate advances in making VLA models more efficient through intelligent token selection and adaptation mechanisms for action prediction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7fd66a0-7595-4a28-bb3d-4f2b51663758",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "784928f3-d1bd-42a9-89da-33bbe020288d",
  "sourceToolAssistantUUID": "e7fd66a0-7595-4a28-bb3d-4f2b51663758",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T05:36:43.188Z_

<details><summary>↩ Tool result · `toolu_01Q7JrHYQfazkgVKqbip6tTb`</summary>

```text
Web search results for query: "latent space augmentation robot learning 2025 2026"

Links: [{"title":"GitHub - YU-deep/Awesome-Latent-Space: A paper list of Awesome Latent Space. · GitHub","url":"https://github.com/YU-deep/Awesome-Latent-Space"},{"title":"[2601.15419] Learning a Unified Latent Space for Cross-Embodiment Robot Control","url":"https://arxiv.org/abs/2601.15419"},{"title":"Latent Action Robot Foundation World Models for Cross-Embodiment Adaptation | OpenReview","url":"https://openreview.net/forum?id=vEZgPr1deb"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"LeWorldModel and the Case for Stable Latent World Models | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/leworldmodel-and-the-case-for-stable-latent-world-models-0e4c33ca0f3c"},{"title":"The Latent Space: Foundation, Evolution, Mechanism, Ability, and Outlook","url":"https://arxiv.org/html/2604.02029v1"},{"title":"Feature 14 IEEE CIRCUITS AND SYSTEMS MAGAZINE FOURTH QUARTER 2025","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Embodied%20AI%20from%20LLMs%20to%20World%20Models.pdf"},{"title":"GitHub - Dstate/LBP: [ICML 2025] The Official Implementation of \"Efficient Robotic Policy Learning via Latent Space Backward Planning\" · GitHub","url":"https://github.com/Dstate/LBP"},{"title":"Current Research Trends in Latent Space – AI Critique","url":"https://www.aicritique.org/us/2026/04/20/current-research-trends-in-latent-space/"}]

Based on the search results, here's what's happening in latent space augmentation for robot learning in 2025-2026:

## Recent Developments in Latent Space Robot Learning

**Vision-Language-Action Models with Latent Spaces**

Vision-language-action models combine a vision-language encoder (vision transformer), which translates an image observation and a natural language description into a distribution within a latent space, with an action decoder that transforms this representation into continuous output actions, directly executable on the robot.

**Cross-Embodiment Learning**

A scalable framework for cross-embodiment humanoid robot control learns a shared latent representation that unifies motion across humans and diverse humanoid platforms by constructing a decoupled latent space that captures localized motion patterns across different body parts using contrastive learning. The trained policy can be directly deployed on multiple robots without any adaptation, and the method supports the efficient addition of new robots to the latent space by learning only a lightweight, robot-specific embedding layer.

**Unified Latent Action Spaces**

A robot foundation world model (LAC-WM) operates within a learned unified latent action space shared across diverse embodiments and explores how this unified action space improves the world model's performance when adapted to previously unseen robot embodiments. The latent action-conditioned model achieves up to a 46.7% improvement in performance over baseline models, and the unified latent action space allows downstream performance to scale positively with the number of embodiments used during pretraining.

**Whole-Body Loco-Manipulation**

WholeBodyVLA is a unified Vision-Language-Action framework for large-space humanoid loco-manipulation that learns unified latent actions from action-free egocentric videos through a Latent Action Model and employs a loco-manipulation-oriented RL policy, encoding egocentric images and language instructions into latent action tokens which are decoded into dual-arm joint actions and locomotion commands.

**Latent Space Planning**

A Latent Space Backward Planning scheme balances efficiency, accuracy and sufficient future guidance by grounding tasks into final latent goals, followed by recursively predicting intermediate subgoals closer to the current state.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2435341a-1f77-4219-b37a-2cd390d10220",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "8f18c469-0d79-4103-8a2c-2d2be6bd6b61",
  "sourceToolAssistantUUID": "2435341a-1f77-4219-b37a-2cd390d10220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T05:36:47.495Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X54bNfhNLJ5h5nNXZ8M37B`</summary>

```json
{
  "query": "Physical Intelligence Google DeepMind Berkeley VLA robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f18c469-0d79-4103-8a2c-2d2be6bd6b61",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vKCjbsAfjrRpDgvLoU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d25870a3-da87-4801-821a-5c948e70aa1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJLjNwwJRjgTrNSGJJ6oD2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1095,
      "cache_creation_input_tokens": 4169,
      "cache_read_input_tokens": 11521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4169,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 19 · 2026-05-14T05:36:48.677Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018vWzc2UBvWMrKNWmmeurwu`</summary>

```json
{
  "query": "RoboPro VLA robustness visual perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d25870a3-da87-4801-821a-5c948e70aa1f",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vKCjbsAfjrRpDgvLoU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bb3adef-9c26-44da-ad63-4a6faaea2a19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJLjNwwJRjgTrNSGJJ6oD2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1095,
      "cache_creation_input_tokens": 4169,
      "cache_read_input_tokens": 11521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4169,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 20 · 2026-05-14T05:36:48.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MV1mnPQrCR1tJGC5P7e2nL`</summary>

```json
{
  "query": "FastVLA token merging efficiency robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bb3adef-9c26-44da-ad63-4a6faaea2a19",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vKCjbsAfjrRpDgvLoU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e4f5b7f-0d3d-4849-8792-2ecf96c0af6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJLjNwwJRjgTrNSGJJ6oD2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1095,
      "cache_creation_input_tokens": 4169,
      "cache_read_input_tokens": 11521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4169,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 21 · 2026-05-14T05:36:49.435Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PsSaSJFj48qCwuAiver5R2`</summary>

```json
{
  "query": "information bottleneck token pruning selection combined any domain 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e4f5b7f-0d3d-4849-8792-2ecf96c0af6b",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vKCjbsAfjrRpDgvLoU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecded804-35a5-43f4-8eb4-cd75626fc4d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJLjNwwJRjgTrNSGJJ6oD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1095,
      "cache_creation_input_tokens": 4169,
      "cache_read_input_tokens": 11521,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4169
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1095,
          "output_tokens": 210,
          "cache_read_input_tokens": 11521,
          "cache_creation_input_tokens": 4169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4169,
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

_source line 22 · 2026-05-14T05:36:54.536Z_

<details><summary>↩ Tool result · `toolu_018vWzc2UBvWMrKNWmmeurwu`</summary>

```text
Web search results for query: "RoboPro VLA robustness visual perturbation"

Links: [{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"}]

Based on the search results, I found information about Vision-Language-Action (VLA) model robustness to visual perturbations, though the results focus primarily on the LIBERO-Plus benchmark and related research rather than a specific model called "RoboPro VLA."

Here are the key findings about VLA robustness to visual perturbations:

## Key Vulnerabilities

VLA models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

Models are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception.

## Perturbation Testing

Systematic vulnerability analysis has been conducted by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Surprising Findings

Models are relatively insensitive to changes in the background setting. Additionally, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

## Addressing Robustness

Recent work has explored improving VLA robustness. RobustVLA achieves absolute gains of 12.6% on the π0 backbone and 10.4% on the OpenVLA backbone across 17 perturbations.

If you were looking for information about a specific "RoboPro VLA" model, it wasn't prominently featured in these search results. Would you like me to search for more specific information about that model?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bb3adef-9c26-44da-ad63-4a6faaea2a19",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "3589562b-db2e-4734-b516-2fdfa1788f3d",
  "sourceToolAssistantUUID": "1bb3adef-9c26-44da-ad63-4a6faaea2a19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T05:36:55.366Z_

<details><summary>↩ Tool result · `toolu_01X54bNfhNLJ5h5nNXZ8M37B`</summary>

```text
Web search results for query: "Physical Intelligence Google DeepMind Berkeley VLA robustness 2025 2026"

Links: [{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"[2503.20020] Gemini Robotics: Bringing AI into the Physical World","url":"https://arxiv.org/abs/2503.20020"},{"title":"Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks | Proceedings of the 2025 Workshop on Large AI Systems and Models with Privacy and Security Analysis","url":"https://dl.acm.org/doi/10.1145/3733800.3763262"},{"title":"Physical Intelligence (π)","url":"https://www.pi.website/"},{"title":"awesome-physical-ai/README.md at main · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/blob/main/README.md"},{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"},{"title":"Publications — Google DeepMind","url":"https://deepmind.google/research/publications/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"A Survey: Learning Embodied Intelligence from Physical Simulators and World Models","url":"https://arxiv.org/html/2507.00917v1"},{"title":"A Comprehensive Survey on Embodied Intelligence: Advancements, Challenges, and Future Perspectives","url":"https://www.sciopen.com/article/10.26599/AIR.2024.9150042"}]

I've completed a web search for your query about Physical Intelligence, Google DeepMind, Berkeley VLA, and robustness in 2025-2026. Here's a summary of what I found:

## Key Findings:

**Physical Intelligence (π) Models:**
Physical Intelligence's pi0 framework uses a pre-trained VLM which connects to a smaller "action export" model, which uses a flow matching loss to predict actions. Their latest generalist policy, π0.5, extends π0 and enables open-world generalization, allowing robots to control a mobile manipulator to clean up entirely new kitchens or bedrooms.

**Vision-Language-Action (VLA) Robustness:**
VLAs leverage general-purpose features learned from a broad mixture of training data, enabling models which are substantially more robust to variation than previous methods. However, current VLA models possess inherent vulnerabilities to sensor attacks, exhibiting varying degrees of susceptibility depending on the specific task, attack modality, and model architecture.

**Google DeepMind's Gemini Robotics:**
Gemini Robotics is an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots, executing smooth and reactive movements to tackle a wide range of complex manipulation tasks while being robust to variations in object types and positions.

**Ongoing Challenges:**
Although current VLA models have made significant progress, several critical challenges still remain, as these models often struggle to reliably handle tasks or environments they have not encountered before.

The search results show active development across multiple organizations in 2025-2026, with emphasis on improving robustness and generalization of VLA models for robotics applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d25870a3-da87-4801-821a-5c948e70aa1f",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "546edd6f-b32c-409d-8b69-f1bfe9a14e48",
  "sourceToolAssistantUUID": "d25870a3-da87-4801-821a-5c948e70aa1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T05:36:56.954Z_

<details><summary>↩ Tool result · `toolu_01PsSaSJFj48qCwuAiver5R2`</summary>

```text
Web search results for query: "information bottleneck token pruning selection combined any domain 2025 2026"

Links: [{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference","url":"https://arxiv.org/html/2601.07667v2"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"TopV: Compatible Token Pruning with Inference Time Optimization for Fast","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_TopV_Compatible_Token_Pruning_with_Inference_Time_Optimization_for_Fast_CVPR_2025_paper.pdf"},{"title":"TokenSkipping: A Practical and Robust KV Cache Pruning Method for Long-Context LLM Inference | Proceedings of the 13th International Conference on Information Technology: IoT and Smart City","url":"https://dl.acm.org/doi/10.1145/3787330.3787361"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"[2601.07667] Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference","url":"https://arxiv.org/abs/2601.07667"},{"title":"Instruction-Guided Cross-Modal Clustering for Training-Free Visual Token Pruning in Vision-Language Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/38212"},{"title":"Structured Token Pruning Strategy","url":"https://www.emergentmind.com/topics/structured-token-pruning-strategy"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"}]

Based on the web search results, here's what I found about information bottleneck token pruning selection combined approaches in 2025-2026:

## Key Research Areas

**Information Bottleneck-Guided Approaches:**

CompTrack, presented at AAAI'26, applies Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking. Additionally, the Information Bottleneck (IB) principle has been applied to token merging in vision transformers, with a novel and separable variational upper bound for the IB loss derived.

**Cross-Modal Information Bottleneck:**

Recent work uses the cross-modal information bottleneck attribution (CIBA) method to identify effective informational cues for guiding pruning, revealing the presence of noun anchors in vision-language models for visual token pruning.

**Combined Selection Strategies:**

Many pipelines apply multiple selection layers—such as core pivots plus diversity MIS extension (D²Pruner), or GSP followed by QCSP (Script)—to ensure that both importance and diversity constraints are enforced at each step.

**Multi-Domain Applications:**

The research spans multiple domains including:
- Vision transformers, diffusion models, speech processing, and video understanding with various token reduction techniques published at major 2025-2026 conferences (ICML'25, NeurIPS'25, ICCV'25, AAAI'26)

**Adaptive Methods:**

ASL is a training-free method that adaptively chooses the selection layer for KV cache reduction, exploiting the variance of token ranks ordered by attention score for language model inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecded804-35a5-43f4-8eb4-cd75626fc4d2",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "bc1b4d70-61ef-40cb-bd64-f0f6e510c27d",
  "sourceToolAssistantUUID": "ecded804-35a5-43f4-8eb4-cd75626fc4d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T05:36:57.083Z_

<details><summary>↩ Tool result · `toolu_01MV1mnPQrCR1tJGC5P7e2nL`</summary>

```text
Web search results for query: "FastVLA token merging efficiency robot"

Links: [{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.pi.website/download/fast.pdf"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://arxiv.org/html/2501.09747v1"},{"title":"Token Expand-Merge: Training-Free Compression Accelerates Billion-Parameter Vision-Language-Action Model Inference","url":"https://quantumzeitgeist.com/training-token-expand-merge-free-compression-accelerates-billion-parameter/"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation ...","url":"https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175v2"},{"title":"FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding | OpenReview","url":"https://openreview.net/forum?id=k6nTUFoqeT"},{"title":"(PDF) FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/388081369_FAST_Efficient_Action_Tokenization_for_Vision-Language-Action_Models"},{"title":"Paper page - FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://huggingface.co/papers/2501.09747"}]

Based on the search results, here's what I found about FastVLA and related token merging efficiency approaches for robots:

## FAST: Efficient Action Tokenization

FAST (Frequency-space Action Sequence Tokenization) enables training of autoregressive VLA policies via simple next token prediction for highly dexterous and high-frequency tasks where standard discretization methods fail entirely. 

FAST uses discrete cosine transform (DCT), a frequency-space transform that represents a continuous signal as a sum of cosine elements of various frequencies, where low frequencies capture the overall shape of the signal and high-frequency components reflect sharp jumps, providing strong compression properties on practical images.

### Performance and Efficiency

When integrated with the π0 VLA, FAST-based tokenization matches the performance of the state-of-the-art π0 diffusion VLA on dexterous and long-horizon manipulation tasks, while training 5x faster. When combined with the pi0 VLA, the method can scale to training on 10k hours of robot data and match the performance of diffusion VLAs, while reducing training time by up to 5x.

## Token Merging Approaches

The search results also reveal several token merging and compression methods for efficient robotic control:

- Token Expand-and-Merge-VLA is a technique that intelligently compresses information within models during operation by dynamically expanding key details and then merging redundant information, achieving a significant speed boost while maintaining and improving the success rate of complex robotic tasks.

- VLA-Cache is a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames, while selectively re-computing task-relevant tokens that are environmentally sensitive to maintain action precision.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e4f5b7f-0d3d-4849-8792-2ecf96c0af6b",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "abac2489-c6c5-4e85-8676-ded78ff5dc0c",
  "sourceToolAssistantUUID": "3e4f5b7f-0d3d-4849-8792-2ecf96c0af6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T05:37:00.750Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MVQJinpp3RFDGC7mkCc2u3`</summary>

```json
{
  "query": "RobustVLA robustness-aware reinforcement post-training VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abac2489-c6c5-4e85-8676-ded78ff5dc0c",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vLE8xzKG3oHASjsvKK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fe72aa9-19fc-46e6-863e-5fd21de8beee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRW5uQoMHNoBC3VHRFbFfv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 989,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 15690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4132,
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

### Tool call

_source line 27 · 2026-05-14T05:37:01.664Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019UUkystn2nz2EomregA4LH`</summary>

```json
{
  "query": "\"Token Bottleneck\" ToBo robot manipulation self-supervised 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fe72aa9-19fc-46e6-863e-5fd21de8beee",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vLE8xzKG3oHASjsvKK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e469e81-1910-4ace-ae1e-dc32ec645680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRW5uQoMHNoBC3VHRFbFfv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 989,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 15690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4132,
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

### Tool call

_source line 28 · 2026-05-14T05:37:02.658Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QLQHiTPUEnL3R86ihvSawZ`</summary>

```json
{
  "query": "\"Corruption Restoration Transformer\" CRT VLA sensor 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e469e81-1910-4ace-ae1e-dc32ec645680",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vLE8xzKG3oHASjsvKK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fff94008-d69c-43a3-9cb3-c300d322d0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRW5uQoMHNoBC3VHRFbFfv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 989,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 15690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4132,
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

### Tool call

_source line 29 · 2026-05-14T05:37:03.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YPvW1AzgJeUktfksqXehRY`</summary>

```json
{
  "query": "VLA-IAP interaction alignment token pruning vision language action 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff94008-d69c-43a3-9cb3-c300d322d0d8",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vLE8xzKG3oHASjsvKK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f87e48fa-18f7-475f-bf4e-a1d53ed691cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRW5uQoMHNoBC3VHRFbFfv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 989,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 15690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4132,
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

### Tool call

_source line 30 · 2026-05-14T05:37:03.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kyb3DCk6YWZTXhY5361qUt`</summary>

```json
{
  "query": "\"information bottleneck\" token merging vision transformer efficient 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f87e48fa-18f7-475f-bf4e-a1d53ed691cd",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vLE8xzKG3oHASjsvKK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0df6e1db-74ce-480c-a530-4d18f82e72eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRW5uQoMHNoBC3VHRFbFfv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 989,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 15690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4132,
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

_source line 31 · 2026-05-14T05:37:06.907Z_

<details><summary>↩ Tool result · `toolu_01MVQJinpp3RFDGC7mkCc2u3`</summary>

```text
Web search results for query: "RobustVLA robustness-aware reinforcement post-training VLA 2026"

Links: [{"title":"[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.01331"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331v2"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=9g7UXLqD4B"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"},{"title":"ROBUSTVLA: ROBUSTNESS-AWARE REINFORCE","url":"https://openreview.net/pdf/2bafb81d5a78f0a3f53ce01659677059882f5f7f.pdf"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for...","url":"https://arxiv.org/abs/2603.26666"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666"}]

Based on the search results, here's what I found about RobustVLA:

## Overview

RobustVLA is a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models.

## Problem It Addresses

Vision-Language-Action (VLA) models have recently emerged as powerful general-purpose policies for robotic manipulation, but they often fail to generalize reliably in out-of-distribution deployments, where unavoidable disturbances such as observation noise, sensor errors, or actuation perturbations become prevalent. While recent Reinforcement Learning (RL)-based post-training provides a practical means to adapt pre-trained VLA models, existing methods mainly emphasize reward maximization and overlook robustness to environmental uncertainty.

## Technical Approach

Through a systematic robustness analysis, RobustVLA identifies two key regularizations: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations.

## Results

Extensive experiments across diverse robotic environments demonstrate that RobustVLA significantly outperforms prior state-of-the-art methods in robustness and reliability.

The paper was submitted for review at ICLR 2026 and is authored by Hongyin Zhang and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fe72aa9-19fc-46e6-863e-5fd21de8beee",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "c19b4d7e-660e-45bb-ae3d-29aa397f11e2",
  "sourceToolAssistantUUID": "7fe72aa9-19fc-46e6-863e-5fd21de8beee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T05:37:07.932Z_

<details><summary>↩ Tool result · `toolu_019UUkystn2nz2EomregA4LH`</summary>

```text
Web search results for query: ""Token Bottleneck" ToBo robot manipulation self-supervised 2025 2026"

Links: [{"title":"GitHub - naver-ai/tobo: Official PyTorch implementation of \"Token Bottleneck: One Token to Remember Dynamics\"","url":"https://github.com/naver-ai/tobo"},{"title":"Token Bottleneck: One Token to Remember Dynamics","url":"https://arxiv.org/html/2507.06543"},{"title":"[2507.06543] Token Bottleneck: One Token to Remember Dynamics","url":"https://arxiv.org/abs/2507.06543"},{"title":"Paper page - Token Bottleneck: One Token to Remember Dynamics","url":"https://huggingface.co/papers/2507.06543"},{"title":"Token Bottleneck: One Token to Remember Dynamics | OpenReview","url":"https://openreview.net/forum?id=x7t7B5CFHm"},{"title":"Token Bottleneck: One Token to Remember Dynamics Taekyung Kim1 Dongyoon Han1","url":"https://arxiv.org/pdf/2507.06543"},{"title":"NeurIPS Poster Token Bottleneck: One Token to Remember Dynamics","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/115268"},{"title":"Token Bottleneck: One Token to Remember Dynamics Taekyung Kim1 Dongyoon Han1","url":"https://openreview.net/pdf/fe822a21593b2e97fa54432a8f40a47deec0146d.pdf"},{"title":"Tactile beyond pixels: Multisensory touch representations for robot manipulation","url":"https://akashsharma02.github.io/sparsh-x-ssl/"},{"title":"Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning","url":"https://arxiv.org/html/2602.08167v1"}]

Based on the search results, here's what I found about Token Bottleneck (ToBo):

## Overview

Token Bottleneck (ToBo) is a self-supervised learning pipeline that squeezes a scene into a bottleneck token and predicts the subsequent scene using minimal patches as hints.

## How It Works

The ToBo pipeline facilitates the learning of sequential scene representations by conservatively encoding the reference scene into a compact bottleneck token during the squeeze step, and in the expansion step, it guides the model to capture temporal dynamics by predicting the target scene using the bottleneck token along with few target patches as hints.

## Applications and Results

Extensive experiments in diverse sequential tasks, including video label propagation and robot manipulation in simulated environments demonstrate the superiority of ToBo over baselines, and deploying the pre-trained model on physical robots confirms its robustness and effectiveness in real-world environments.

The model is evaluated on three robotics benchmarks: FrankaKitchen, CortexBench, and RLBench.

## Publication Status

Token Bottleneck was published as an arXiv preprint (arXiv:2507.06543) in 2025, and the research is from NAVER Cloud Corp. The code is publicly available on GitHub at https://github.com/naver-ai/tobo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e469e81-1910-4ace-ae1e-dc32ec645680",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "4e0c7db3-bf68-4b46-b5a9-ae4b354b1514",
  "sourceToolAssistantUUID": "3e469e81-1910-4ace-ae1e-dc32ec645680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T05:37:09.039Z_

<details><summary>↩ Tool result · `toolu_01QLQHiTPUEnL3R86ihvSawZ`</summary>

```text
Web search results for query: ""Corruption Restoration Transformer" CRT VLA sensor 2026"

Links: [{"title":"Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/html/2602.01158"},{"title":"Need help substituting a flyback transformer for a CRT monitor | Electronics Forum (Circuits, Projects and Microcontrollers)","url":"https://www.electro-tech-online.com/threads/need-help-substituting-a-flyback-transformer-for-a-crt-monitor.149112/"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v2"},{"title":"Source for aftermarket replacement flyback xfmrs?","url":"https://forums.arcade-museum.com/threads/source-for-aftermarket-replacement-flyback-xfmrs.472366/"},{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"® U.S. Registered Trademark EN0B-0568GE51 R0717","url":"https://prod-edam.honeywell.com/content/dam/honeywell-edam/hbt/en-us/documents/literature-and-specs/datasheets/bms-from-hco-030923/hbt-bms-en0b0568-ge51r0717.pdf"},{"title":"How to test a CRT flyback transformer - Quora","url":"https://www.quora.com/How-do-you-test-a-CRT-flyback-transformer"},{"title":"A Guide to High Voltage Flyback Transformer by Custom Coils","url":"https://www.customcoils.com/guide-to-the-flyback-transformer/"},{"title":"crt transformer: Find Reliable Suppliers & Types","url":"https://www.accio.com/plp/crt-transformer"},{"title":"Replacements for Brooksonic/Emerson Flyback (IHVT Intermediate High Voltage Transformer) Transformer for CRT Televisions","url":"https://jayso.com/products/replacements-for-brooksonic-emerson-flyback-ihvt-intermediate-high-voltage-transformer-transformer-for-crt-televisions"}]

Based on the search results, I found relevant information about the Corruption Restoration Transformer (CRT) in the context of Vision-Language-Action (VLA) models:

## Corruption Restoration Transformer (CRT) for VLA Models

The Corruption Restoration Transformer (CRT) is a plug-and-play and model-agnostic vision transformer designed to immunize VLA models against sensor disturbances.

### Purpose and Problem it Solves

Sensor-level artifacts, ranging from electronic noise and dead pixels to lens contaminants, directly compromise the integrity of the visual signal, causing state-of-the-art VLAs to suffer catastrophic performance degradation, dropping from 90% success rates to as low as 2%, under common signal artifacts.

### How it Works

CRT is designed as a modular unit upstream of the VLA that acts as a specialized, lightweight module that restores observations before they reach the policy network, rather than requiring retraining or fine-tuning from scratch a VLA, which would be computationally prohibitive.

### Performance Impact

CRT introduces a negligible overhead while increasing the robustness of the underlying model.

The research appears to be from February 2026 according to the publication date on the arxiv paper, addressing a critical vulnerability in current Vision-Language-Action models related to their lack of robustness to image corruptions caused by sensor disturbances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fff94008-d69c-43a3-9cb3-c300d322d0d8",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "d6e6d6f7-1882-42b4-9cbc-f43e0d285393",
  "sourceToolAssistantUUID": "fff94008-d69c-43a3-9cb3-c300d322d0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T05:37:09.888Z_

<details><summary>↩ Tool result · `toolu_01YPvW1AzgJeUktfksqXehRY`</summary>

```text
Web search results for query: "VLA-IAP interaction alignment token pruning vision language action 2026"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"GitHub - chen7086/VLA-ADP: Action aware Dynamic Pruning for Efficient Vision Language Action Manipulation · GitHub","url":"https://github.com/chen7086/VLA-ADP"},{"title":"Paper page - HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System","url":"https://huggingface.co/papers/2604.14125"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"[2602.20566] BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/abs/2602.20566"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"}]

Based on the search results, I found relevant information about VLA-IAP:

## VLA-IAP: Interaction-Aligned Pruning for Vision-Language-Action Models

VLA-IAP is the Interaction-Aligned Pruning framework designed to address efficiency challenges in Vision-Language-Action models. 

### Key Problem and Approach

The framework breaks the Perception-First bottleneck prevalent in existing VLA pruning methods—namely, the over-reliance on the static attention weights of pre-trained Vision-Language Models (VLMs). Existing visual token pruning methods mainly rely on semantic saliency or simple temporal cues, overlooking the continuous physical interaction, a fundamental property of VLA tasks, and consequently often prune visually sparse yet structurally critical regions that support manipulation, leading to unstable behavior during early task phases.

### Technical Solution

VLA-IAP introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment. This enables a conservative-to-aggressive transition, ensuring robustness during early uncertainty and efficiency once interaction is locked.

### Performance Results

VLA-IAP achieves a 97.8% success rate with a 1.54× speedup while maintaining performance comparable to the unpruned backbone. The method demonstrates superior and consistent performance across multiple model architectures and three different simulation environments, as well as a real robot platform, validating its strong generalization capability and practical applicability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f87e48fa-18f7-475f-bf4e-a1d53ed691cd",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "71909d4f-7b3e-4f49-be82-22702b5521cb",
  "sourceToolAssistantUUID": "f87e48fa-18f7-475f-bf4e-a1d53ed691cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T05:37:10.755Z_

<details><summary>↩ Tool result · `toolu_01Kyb3DCk6YWZTXhY5361qUt`</summary>

```text
Web search results for query: ""information bottleneck" token merging vision transformer efficient 2025 2026"

Links: [{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"Efficient Visual Transformer by Learnable Token Merging - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40663671/"},{"title":"EFFICIENT VISION TRANSFORMER BY INFORMATION ...","url":"https://openreview.net/pdf?id=Jwgw3znxT3"},{"title":"1 Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/pdf/2407.15219"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219v1"},{"title":"[2407.15219] Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/abs/2407.15219"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Efficient Vision Transformer via Token Merger | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10183862/"},{"title":"Efficient Vision Transformer via Token Merger","url":"https://www.researchgate.net/publication/372343417_Efficient_Vision_Transformer_via_Token_Merger"},{"title":"Efficient Token Compression for Vision Transformer with Spatial Information Preserved","url":"https://arxiv.org/html/2503.23455v1"}]

I've found several relevant results on information bottleneck-inspired token merging in vision transformers. Here's a summary of the key findings:

## Recent Research on Information Bottleneck Token Merging

A novel transformer block called IBTM (Transformer with Information Bottleneck inspired Token Merging) performs token merging in a learnable scheme. IBTM is compatible with many popular and compact transformer networks, such as MobileViT and EfficientViT, and it reduces the FLOPs and the inference time of the vision transformers while maintaining or even improving the prediction accuracy.

Another related approach is the Learnable Token Merging (LTM) transformer block, which performs token merging in a learnable scheme. The LTM-Transformer is motivated by reduction of Information Bottleneck, and a novel separable variational upper bound for the IB loss is derived, with the mask module architecture designed to reduce this upper bound for the IB loss.

The principle of Information Bottleneck is to maximize the mutual information between merged tokens and class labels while minimizing the mutual information between merged tokens and the input. Extensive results on computer vision tasks evidence that LTM-Transformer renders compact and efficient visual transformers with comparable or much better prediction accuracy than the original visual transformers.

The search results also indicate there's ongoing work in this area at major 2025-2026 conferences, with several token reduction and compression papers being presented at CVPR 2026 and ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0df6e1db-74ce-480c-a530-4d18f82e72eb",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "06d1d238-3074-44b0-b063-77a392bec17e",
  "sourceToolAssistantUUID": "0df6e1db-74ce-480c-a530-4d18f82e72eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T05:37:15.124Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016yLZmUCWrY5tbFMgjyuaLq`</summary>

```json
{
  "query": "Compressor-VLA instruction-guided visual token compression robotic manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06d1d238-3074-44b0-b063-77a392bec17e",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vMEeFkoqLfdkiChq41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ae88605-045d-4790-bd45-188f72728540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtYY75QZZD7Y5tTm62VW3D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5788,
      "cache_read_input_tokens": 19822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5788,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 37 · 2026-05-14T05:37:15.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NyjyK5dzF9Cn9uFzXYeboD`</summary>

```json
{
  "query": "\"Rethinking Latent Representations\" \"Information Bottleneck\" robot manipulation behavior cloning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ae88605-045d-4790-bd45-188f72728540",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vMEeFkoqLfdkiChq41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3394ab73-ba96-4282-b2f2-49f7cb4276e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtYY75QZZD7Y5tTm62VW3D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5788,
      "cache_read_input_tokens": 19822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5788,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 38 · 2026-05-14T05:37:15.932Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U9HL8YSwFYnHN6n8jE51iL`</summary>

```json
{
  "query": "VLA-Pruner temporal-aware dual-level visual token pruning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3394ab73-ba96-4282-b2f2-49f7cb4276e7",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vMEeFkoqLfdkiChq41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2998b4ca-6d7c-43f4-ac78-95038f7ffebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtYY75QZZD7Y5tTm62VW3D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5788,
      "cache_read_input_tokens": 19822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5788,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 39 · 2026-05-14T05:37:16.852Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UYVeTfocZxWNEWPB2LuAjD`</summary>

```json
{
  "query": "\"Do World Action Models Generalize Better than VLAs\" robustness study 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2998b4ca-6d7c-43f4-ac78-95038f7ffebb",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vMEeFkoqLfdkiChq41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a1be514-5b51-4df7-97e6-eb70480fafba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtYY75QZZD7Y5tTm62VW3D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5788,
      "cache_read_input_tokens": 19822,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5788
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 19822,
          "cache_creation_input_tokens": 5788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5788,
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

_source line 40 · 2026-05-14T05:37:20.996Z_

<details><summary>↩ Tool result · `toolu_01NyjyK5dzF9Cn9uFzXYeboD`</summary>

```text
Web search results for query: ""Rethinking Latent Representations" "Information Bottleneck" robot manipulation behavior cloning"

Links: [{"title":"[2502.02853] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/abs/2502.02853"},{"title":"Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/html/2502.02853v1"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://proceedings.mlr.press/v267/bai25e.html"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=N2Dey442PJ"},{"title":"GitHub - BaiShuanghao/BC-IB: [ICML 2025] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://github.com/BaiShuanghao/BC-IB"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/html/2502.02853v5"},{"title":"Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation | Request PDF","url":"https://www.researchgate.net/publication/388754555_Rethinking_Latent_Representations_in_Behavior_Cloning_An_Information_Bottleneck_Approach_for_Robot_Manipulation"},{"title":"ICML Poster Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://icml.cc/virtual/2025/poster/45521"},{"title":"[Literature Review] Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://www.themoonlight.io/en/review/rethinking-latent-representations-in-behavior-cloning-an-information-bottleneck-approach-for-robot-manipulation"},{"title":"BC-IB for Robot Manipulation - GitHub Pages","url":"https://baishuanghao.github.io/BC-IB.github.io/"}]

I found several relevant results about this research topic. Here's what the search returned:

## Overview

The paper "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation" addresses behavior cloning (BC), which is a widely adopted visual imitation learning method in robot manipulation.

## The Problem

Current BC methods overlook whether learned representations contain redundant information and lack a solid theoretical foundation to guide the learning process. The findings show that latent representations in standard BC are not optimal.

## The Proposed Solution

The researchers incorporate the Information Bottleneck (IB) principle into BC, which extends the idea of reducing redundancy by providing a structured framework for compressing irrelevant information while preserving task-relevant features. They adopt an information-theoretic perspective and introduce mutual information to quantify and mitigate redundancy in latent representations.

## Results

Extensive experiments and analyses on the CortexBench and LIBERO benchmarks show consistent performance improvements with IB across various settings, underscoring the importance of reducing input data redundancy and highlighting its practical value for real-world applications.

## Publication

This work was presented at ICML 2025 and is authored by Shuanghao Bai and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3394ab73-ba96-4282-b2f2-49f7cb4276e7",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "f4b118d5-624e-4b9f-b1a9-c4e80fe170dc",
  "sourceToolAssistantUUID": "3394ab73-ba96-4282-b2f2-49f7cb4276e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T05:37:22.232Z_

<details><summary>↩ Tool result · `toolu_016yLZmUCWrY5tbFMgjyuaLq`</summary>

```text
Web search results for query: "Compressor-VLA instruction-guided visual token compression robotic manipulation"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"Jing Zhang's research works","url":"https://www.researchgate.net/scientific-contributions/Jing-Zhang-2300690329"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"http://paperreading.club/page?id=357953"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Visual Resolution Compressor (VRC)","url":"https://www.emergentmind.com/topics/visual-resolution-compressor-vrc"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"}]

I found comprehensive information about Compressor-VLA. Here's what the research shows:

## Overview

Compressor-VLA is a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models.

## The Problem It Addresses

The significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment. While standard token pruning techniques can alleviate this, these task-agnostic methods struggle to preserve task-critical visual information.

## Technical Architecture

The proposed Compressor-VLA framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information.

## Key Results

Experimentally, extensive evaluations demonstrate that Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline. The real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability and practical applicability.

## Novel Contribution

Instead of directly pruning tokens in previous works, the key insight is using a hybrid instruction-guided compressor to reconstruct a compact set of tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ae88605-045d-4790-bd45-188f72728540",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "491ba114-f020-4bbc-89c6-f6d684302fbe",
  "sourceToolAssistantUUID": "3ae88605-045d-4790-bd45-188f72728540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T05:37:23.261Z_

<details><summary>↩ Tool result · `toolu_01U9HL8YSwFYnHN6n8jE51iL`</summary>

```text
Web search results for query: "VLA-Pruner temporal-aware dual-level visual token pruning 2025"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766"}]

Based on the search results, I found comprehensive information about VLA-Pruner:

## VLA-Pruner: Overview

Vision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment. VLA-Pruner is a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation.

## The Dual-Level Approach

VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance.

## Key Advantage Over Existing Methods

Previous VLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution. Consequently, these methods bias token retention toward semantic cues, discard critical information for action generation, and significantly degrade VLA performance.

## Performance

VLA-Pruner proposes a novel dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens for both semantic understanding and action execution under given compute budget. Experiments show that VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks.

The paper (arXiv:2511.16449) was submitted in November 2025 and represents a significant advancement in efficient VLA inference through temporal-aware token pruning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2998b4ca-6d7c-43f4-ac78-95038f7ffebb",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "1cd9de83-0cad-4bc9-9bbd-cddaea66863c",
  "sourceToolAssistantUUID": "2998b4ca-6d7c-43f4-ac78-95038f7ffebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T05:37:26.699Z_

<details><summary>↩ Tool result · `toolu_01UYVeTfocZxWNEWPB2LuAjD`</summary>

```text
Web search results for query: ""Do World Action Models Generalize Better than VLAs" robustness study 2026"

Links: [{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"Paper page - Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://huggingface.co/papers/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://www.wispaper.ai/en/user-blog/world-action-models-generalize-better-than-vlas-20260324/eng"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69d44b615127ff45a9dee58a"},{"title":"Training data of VLAs and WAMs across different training stages.... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Training-data-of-VLAs-and-WAMs-across-different-training-stages-Training-stages-Policy_tbl1_403072709"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"}]

I found the paper you're asking about. Here's an overview of the study:

## "Do World Action Models Generalize Better than VLAs? A Robustness Study"

This is a comparative study of prominent state-of-the-art VLA policies and recently released WAMs, evaluating their performance on the LIBERO-Plus and RoboTwin 2.0-Plus benchmarks under various visual and language perturbations.

### Key Findings

WAMs achieve strong robustness, with LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus. WAMs generally demonstrate strong robustness to noise, lighting and layout perturbations in both single-arm and bimanual settings, with this robustness believed to be at least partially attributable to the spatiotemporal priors inherited from their world model backbones.

However, the results are nuanced. While VLAs such as π₀.₅ can achieve comparable robustness on certain tasks, they typically require extensive training with diverse robotic datasets and varied learning objectives. WAMs show reduced consistency and struggle with geometric perturbations, specifically variations in camera viewpoint and the robot's initial state, with LingBot-VA's success rate dropping to 28.9% for camera and 36.2% for robot initial state perturbations on RoboTwin 2.0-Plus.

### Notable Limitation

The high inference overhead of WAMs remains a major challenge that limits their deployment in real-world robotic systems, with a single inference step being at least 4.8 times slower.

The paper was published on arXiv in March 2026 and is authored by researchers from Huawei Technologies and the University of Toronto.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a1be514-5b51-4df7-97e6-eb70480fafba",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "190e1c53-e2ad-47c4-b19e-be33893366c4",
  "sourceToolAssistantUUID": "7a1be514-5b51-4df7-97e6-eb70480fafba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T05:37:30.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H33tv2U9B7b5tiEscDXZDd`</summary>

```json
{
  "query": "OneWM-VLA \"One Token Per Frame\" adaptive attention pooling world model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "190e1c53-e2ad-47c4-b19e-be33893366c4",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vNQhGkfFd7vZe8w7fL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c466ca24-8891-4214-8778-804a7041d3ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQkzJRq8ufwFAED1KvXbna",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 25610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4139,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 45 · 2026-05-14T05:37:31.705Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E4JgEHqJp8JBoHzKkxCUTN`</summary>

```json
{
  "query": "\"Token Expand-Merge\" VLA training-free compression acceleration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c466ca24-8891-4214-8778-804a7041d3ba",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vNQhGkfFd7vZe8w7fL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "504f9190-edf0-4ec6-9ee0-b9f722c716e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQkzJRq8ufwFAED1KvXbna",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 25610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4139,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 46 · 2026-05-14T05:37:32.338Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Qgd3nU94z52vFQNyk7ooa`</summary>

```json
{
  "query": "\"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "504f9190-edf0-4ec6-9ee0-b9f722c716e9",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vNQhGkfFd7vZe8w7fL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09b1899b-5ca4-48b7-9682-bdb898d83748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQkzJRq8ufwFAED1KvXbna",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 25610,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4139
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 25610,
          "cache_creation_input_tokens": 4139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4139,
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

_source line 47 · 2026-05-14T05:37:36.912Z_

<details><summary>↩ Tool result · `toolu_01H33tv2U9B7b5tiEscDXZDd`</summary>

```text
Web search results for query: "OneWM-VLA "One Token Per Frame" adaptive attention pooling world model 2026"

Links: [{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/html/2605.07931v1"},{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World...","url":"https://arxiv.org/abs/2605.07931v1"},{"title":"One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding | OpenReview","url":"https://openreview.net/forum?id=bythzT0b81"},{"title":"One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding","url":"https://arxiv.org/html/2604.14149"},{"title":"[2604.14149] One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding","url":"https://arxiv.org/abs/2604.14149"}]

Based on the search results, I found relevant information about OneWM-VLA:

## OneWM-VLA Overview

OneWM-VLA compresses each view into a single semantic token per frame through an Adaptive Attention Pooling, and produces the resulting latent stream and the action trajectory under a single flow-matching objective rather than connecting them through a separate decoder.

## Key Design Features

The design realizes a bottleneck-rollout coupling through a single visual token per frame produced by Adaptive Attention Pooling, and a joint flow-matching objective that generates the future latent stream together with the future action sequence rather than predicting them through separate heads.

## Technical Components

A lightweight Adaptive Attention Pooling distills each view into a single semantic latent token per frame, so that per-frame visual bandwidth is held at one token and the per-step world-module budget remains horizon-invariant. A joint flow-matching objective then generates the future latent stream and the future action trajectory under one model, so the predicted latent stream serves as a structural prior on the action trajectory rather than a side channel produced by a separate decoder.

## Performance

Per-frame visual bandwidth can be reduced to a single token without compromising long-horizon performance under their setup. The paper appears to have been published recently (as of May 2026) and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c466ca24-8891-4214-8778-804a7041d3ba",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "e3ad5622-aae0-41fe-af31-b79ef07232da",
  "sourceToolAssistantUUID": "c466ca24-8891-4214-8778-804a7041d3ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T05:37:39.273Z_

<details><summary>↩ Tool result · `toolu_01E4JgEHqJp8JBoHzKkxCUTN`</summary>

```text
Web search results for query: ""Token Expand-Merge" VLA training-free compression acceleration 2025 2026"

Links: [{"title":"Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.09927"},{"title":"Token Expand-Merge: Training-Free Compression Accelerates Billion-Parameter Vision-Language-Action Model Inference","url":"https://quantumzeitgeist.com/training-token-expand-merge-free-compression-accelerates-billion-parameter/"},{"title":"[2512.09927] Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2512.09927"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"flashvid: efficient video large language models via training- ...","url":"https://arxiv.org/pdf/2602.08024"},{"title":"FlashVID: Efficient Video Large Language Models via Training-free Tree-Based Spatiotemporal Token Merging","url":"https://arxiv.org/html/2602.08024v1"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"[2506.05709] Token Transforming: A Unified and Training-Free Token Compression Framework for Vision Transformer Acceleration","url":"https://arxiv.org/abs/2506.05709"},{"title":"Token Transforming: A Unified and Training-Free Token Compression Framework for Vision Transformer Acceleration","url":"https://arxiv.org/html/2506.05709v1"}]

I found research on Token Expand-Merge (TEAM-VLA) for Vision-Language-Action models. Here are the key findings:

## Token Expand-Merge: Training-Free VLA Compression

Token Expand-and-Merge-VLA (TEAM-VLA) is a training-free token compression framework that accelerates VLA inference while preserving task performance.

### How It Works

TEAM-VLA accelerates inference through a dual strategy of early pruning and mid-layer merging. After the sensory encoder extracts visual features, it first performs context pruning and similarity expansion to discard redundant background tokens before they enter the LLM backbone, removing a large portion of spatially uninformative tokens at the earliest stage.

TEAM-VLA introduces a dynamic token expansion mechanism that identifies and samples additional informative tokens in the spatial vicinity of attention-highlighted regions, enhancing contextual completeness. These expanded tokens are then selectively merged in deeper layers under action-aware guidance, effectively reducing redundancy while maintaining semantic coherence.

### Key Advantages

Unlike prior training-free methods that prune only in deeper layers (where token counts are already low), the dual-reduction design eliminates redundancy both before and within the backbone, enabling substantially greater speed-up without sacrificing task performance.

### Performance

Extensive experiments on the LIBERO benchmark demonstrate that TEAM-VLA achieves an excellent success–latency trade-off, substantially accelerating inference while maintaining strong execution performance.

The research paper was published on arXiv in December 2025, making it a very recent advancement in efficient VLA model acceleration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "504f9190-edf0-4ec6-9ee0-b9f722c716e9",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "bb763c00-9b6c-4fe2-bc60-5cb8134a051e",
  "sourceToolAssistantUUID": "504f9190-edf0-4ec6-9ee0-b9f722c716e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T05:37:40.353Z_

<details><summary>↩ Tool result · `toolu_014Qgd3nU94z52vFQNyk7ooa`</summary>

```text
Web search results for query: ""On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations" ICLR 2026"

Links: [{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"ON ROBUSTNESS OF VISION-LANGUAGE-ACTION ...","url":"https://openreview.net/pdf/4c9de20f29e6aad53dfd1f3b339230208e43a2ff.pdf"},{"title":"ON ROBUSTNESS OF VISION-LANGUAGE-ACTION MODEL ...","url":"https://openreview.net/pdf/24afaa89d3b5edf893bafacccbf39c79e5ed2973.pdf"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations | OpenReview","url":"https://openreview.net/forum?id=cS6xizdYD5"},{"title":"[2510.00037] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037"},{"title":"[2510.00037v4] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037v4"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"},{"title":"ON ROBUSTNESS OF VISION-LANGUAGE-ACTION MODEL AGAINST MULTI-MODAL PERTURBATIONS","url":"https://arxiv.org/pdf/2510.00037"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/460a1d8eac34125dad453b28d6d64446-Paper-Conference.pdf"}]

I found the paper you're looking for! Here are the search results for "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations" at ICLR 2026:

## Paper Overview

The paper addresses robustness in Vision–Language–Action (VLA) models to real-world perturbations, noting that existing methods target simple visual disturbances while overlooking broader multi-modal perturbations that arise in actions, instructions, environments, and observations.

## Key Findings

The authors evaluate the robustness of mainstream VLAs against 17 uncertainties across four modalities, finding that: (1) action is the most fragile modality, (2) existing visual-robust VLAs do not show improvements in other modalities, and (3) π0 demonstrates superior robustness, outperforming OpenVLA and π0-FAST by large margins.

## Proposed Method

The authors propose RobustVLA against perturbations in VLA inputs and outputs, performing offline robust optimization against worst-case action noise. To account for multiple perturbations, they formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise.

## Results

On the LIBERO benchmark, RobustVLA delivers absolute gains over baselines of 12.6% on the π0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs. On a real-world FR5 robot under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming π0 by 65.6% success rate with 25 demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09b1899b-5ca4-48b7-9682-bdb898d83748",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "d60999df-17a5-4cd3-a3ad-b781fc38eb41",
  "sourceToolAssistantUUID": "09b1899b-5ca4-48b7-9682-bdb898d83748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T05:37:43.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ADszZvcGWjTqdGRFjzcZWh`</summary>

```json
{
  "query": "SpecPrune-VLA action-aware self-speculative pruning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d60999df-17a5-4cd3-a3ad-b781fc38eb41",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vPR9LZzyLK3h5ZLn2T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5dccb15-3633-4502-ac15-074c1e4944be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fsih3B4j9cdqHp8FuT6Dbn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2761,
      "cache_read_input_tokens": 29749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2761,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 51 · 2026-05-14T05:37:44.870Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sb4wpj6AiMXfRioT5hsjRn`</summary>

```json
{
  "query": "ETA-VLA temporal fusion intra-LLM sparsification token adaptation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5dccb15-3633-4502-ac15-074c1e4944be",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vPR9LZzyLK3h5ZLn2T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "526774e2-8826-4353-b6cd-e71199a63f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fsih3B4j9cdqHp8FuT6Dbn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2761,
      "cache_read_input_tokens": 29749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2761,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 52 · 2026-05-14T05:37:45.737Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MMxhWEaaoDKTfg5XhrRwoh`</summary>

```json
{
  "query": "BC-IB information bottleneck behavior cloning ICML 2025 details method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "526774e2-8826-4353-b6cd-e71199a63f20",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vPR9LZzyLK3h5ZLn2T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7619cc0b-1822-4aa9-9935-da27144b932b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fsih3B4j9cdqHp8FuT6Dbn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2761,
      "cache_read_input_tokens": 29749,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2761
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 29749,
          "cache_creation_input_tokens": 2761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2761,
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

_source line 53 · 2026-05-14T05:37:51.522Z_

<details><summary>↩ Tool result · `toolu_01ADszZvcGWjTqdGRFjzcZWh`</summary>

```text
Web search results for query: "SpecPrune-VLA action-aware self-speculative pruning 2025"

Links: [{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | Request PDF","url":"https://www.researchgate.net/publication/395354566_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via_Action-Aware_Self-Speculative_Pruning"},{"title":"Specprune-vla Boosts Vision-Language-Action Models, Avoiding Over 20% Success Rate Drops With Smart Pruning","url":"https://quantumzeitgeist.com/faster-models-performance-specprune-vla-boosts-vision-language-action-avoiding-success/"},{"title":"SPECPRUNE-VLA:","url":"https://openreview.net/pdf/f898de78034757b0bb38f30b7b6fd21bca97b4ad.pdf"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"GitHub - KwanWaiPang/Awesome-VLA: Paper Survey for Visual Language Action · GitHub","url":"https://github.com/KwanWaiPang/Awesome-VLA"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the search results, here's what I found about SpecPrune-VLA:

## Overview

SpecPrune-VLA is a method for accelerating Vision-Language-Action models via action-aware self-speculative pruning. The technique has been applied to accelerate VLA model inference, addressing limitations in existing acceleration methods that focus on local information from current action steps while ignoring global context, which can lead to >20% success rate drops and limited speedup.

## Key Innovation

The method is based on the observation of spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and proposes that token selection should combine local information with global context of the model.

## Technical Approach

SpecPrune-VLA uses three main components: (1) Action-level static pruning leveraging global history and local attention to statically reduce visual tokens per action, (2) Layer-level dynamic pruning to prune tokens adaptively per layer based on layer-wise importance, and (3) a lightweight action-aware controller that classifies actions as coarse- or fine-grained by the speed of the end effector and adjusts pruning aggressiveness accordingly.

## Performance Results

Extensive experiments show that SpecPrune-VLA achieves up to 1.57× speedup in LIBERO simulation and 1.70× on real-world tasks, with negligible success rate degradation. The paper was last updated on February 10, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5dccb15-3633-4502-ac15-074c1e4944be",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "f4326b3b-6527-40e2-b206-2ba90493efdb",
  "sourceToolAssistantUUID": "d5dccb15-3633-4502-ac15-074c1e4944be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T05:37:52.253Z_

<details><summary>↩ Tool result · `toolu_01MMxhWEaaoDKTfg5XhrRwoh`</summary>

```text
Web search results for query: "BC-IB information bottleneck behavior cloning ICML 2025 details method"

Links: [{"title":"GitHub - BaiShuanghao/BC-IB: [ICML 2025] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://github.com/BaiShuanghao/BC-IB"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=N2Dey442PJ"},{"title":"ICML Poster Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://icml.cc/virtual/2025/poster/45521"},{"title":"BC-IB for Robot Manipulation - GitHub Pages","url":"https://baishuanghao.github.io/BC-IB.github.io/"},{"title":"[2502.02853] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/abs/2502.02853"},{"title":"BC-IB/documents/DOWNLOAD_MODEL.md at main · BaiShuanghao/BC-IB","url":"https://github.com/BaiShuanghao/BC-IB/blob/main/documents/DOWNLOAD_MODEL.md"},{"title":"Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/html/2502.02853v1"},{"title":"Behavioral Cloning in Imitation Learning","url":"https://www.emergentmind.com/topics/behavioral-cloning-bc"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://proceedings.mlr.press/v267/bai25e.html"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/html/2502.02853"}]

I found detailed information about the BC-IB paper. Here are the key details:

## Paper Overview

BC-IB is an ICML 2025 paper titled "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation" by authors including Shuanghao Bai, Wanqi Zhou, Pengxiang Ding, Wei Zhao, Donglin Wang, and Badong Chen.

## Main Method

The approach applies the Information Bottleneck (IB) principle to reduce the mutual information between the input and the latent space, aiming to remove task-irrelevant features. The Information Bottleneck principle is incorporated into BC, which extends the idea of reducing redundancy by providing a structured framework for compressing irrelevant information while preserving task-relevant features.

## Key Contributions

This work presents the first comprehensive study on redundancy in latent representations across various methods, backbones, and experimental settings, while extending the generalizability of the IB to BC. The paper provides a detailed theoretical analysis explaining why IB enhances the transferability of BC methods.

## Experimental Results

Extensive experiments and analyses on the CortexBench and LIBERO benchmarks show consistent performance improvements with IB across various settings, underscoring the importance of reducing input data redundancy and highlighting its practical value for real-world applications. For example, in LIBERO-Goal, IB reduces mutual information to one-quarter of its original value and yields a 7.7% increase in success rate.

The paper is available on arXiv (2502.02853) and has an associated GitHub repository at BaiShuanghao/BC-IB with implementation code and benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7619cc0b-1822-4aa9-9935-da27144b932b",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "240a8163-7936-47d8-b359-a63adf7a4107",
  "sourceToolAssistantUUID": "7619cc0b-1822-4aa9-9935-da27144b932b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T05:37:53.820Z_

<details><summary>↩ Tool result · `toolu_01Sb4wpj6AiMXfRioT5hsjRn`</summary>

```text
Web search results for query: "ETA-VLA temporal fusion intra-LLM sparsification token adaptation 2026"

Links: [{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766v1"},{"title":"[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.25766"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.19257"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for","url":"https://arxiv.org/pdf/2508.19257"},{"title":"[PDF] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TTF-VLA:-Temporal-Token-Fusion-via-Pixel-Attention-Liu-Zhang/02462f0f53d1b48867e35eae8901d75996e5a662"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"}]

I found relevant information about ETA-VLA. Here are the search results:

## ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification

ETA-VLA is an Efficient Token Adaptation framework for VLA (Vision-Language-Action) models that processes past n frames of multi-view images and introduces a novel Intra-LLM Sparse Aggregator (ILSA).

### Key Components

The framework includes two complementary components: a Temporal Fusion Module (TFM) and an Intra-LLM Sparse Aggregator (ILSA).

**Temporal Fusion Module (TFM):** TFM operates on visual encoder features before the LLM to mitigate the linear growth of token count with time. It adaptively fuses multi-frame historical features into a concise representation via transformer and learnable weights, effectively compressing the temporal dimension while preserving critical motion cues.

**Intra-LLM Sparse Aggregator (ILSA):** ILSA dynamically identifies and prunes redundant visual tokens guided by textual queries and temporal consistency. It utilizes a text-guided scoring mechanism alongside a diversity-preserving sparsification strategy to select a sparse subset of critical tokens.

### Performance Results

ETA-VLA establishes a new state-of-the-art with an EPDMS score of 85.0 on the NAVSIM v2 Navtest benchmark with 35% token pruning, significantly outperforming established baselines such as VADv2 (76.6), Transfuser (76.7), and DiffusionDrive (84.3).

The method prunes 85% of visual tokens and reduces inference FLOPs by 61%, while still retaining 94% of the original accuracy on the NAVSIM v2 benchmark.

The paper was published on arXiv on March 26, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "526774e2-8826-4353-b6cd-e71199a63f20",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "72405714-4a68-4587-abb2-04d15b57fd8a",
  "sourceToolAssistantUUID": "526774e2-8826-4353-b6cd-e71199a63f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-14T05:37:57.988Z_

Now let me search for a few more specific items to complete the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72405714-4a68-4587-abb2-04d15b57fd8a",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vQQmnkrhB65n2Tw7BG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c855966-05d1-4c24-b39a-549083efb577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KimV3AAv1L8Lq9PDbchQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1029,
      "cache_creation_input_tokens": 2356,
      "cache_read_input_tokens": 32510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2356,
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

_source line 57 · 2026-05-14T05:37:58.465Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BVf6JZ1ua3ub3RSHKaA5Vu`</summary>

```json
{
  "query": "\"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c855966-05d1-4c24-b39a-549083efb577",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vQQmnkrhB65n2Tw7BG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95ae9385-6d87-431c-b8ee-9a3b50953f59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KimV3AAv1L8Lq9PDbchQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1029,
      "cache_creation_input_tokens": 2356,
      "cache_read_input_tokens": 32510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2356,
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

_source line 58 · 2026-05-14T05:37:59.566Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T4RcdtRwMqax93XoMMZyHV`</summary>

```json
{
  "query": "pi0 pi0.5 robustness perturbation Physical Intelligence 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95ae9385-6d87-431c-b8ee-9a3b50953f59",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vQQmnkrhB65n2Tw7BG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4415534f-6d5b-442e-b25f-5587dd4fd256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KimV3AAv1L8Lq9PDbchQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1029,
      "cache_creation_input_tokens": 2356,
      "cache_read_input_tokens": 32510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2356,
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

_source line 59 · 2026-05-14T05:38:00.098Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QQLXZTJ8nF4DMg9ZhcGXge`</summary>

```json
{
  "query": "\"A1\" truncated VLA adaptive efficient transparent open-source 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4415534f-6d5b-442e-b25f-5587dd4fd256",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vQQmnkrhB65n2Tw7BG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fc35fd5-f152-4a32-b53c-6314b7ee5b75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KimV3AAv1L8Lq9PDbchQz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1029,
      "cache_creation_input_tokens": 2356,
      "cache_read_input_tokens": 32510,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2356
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1029,
          "output_tokens": 201,
          "cache_read_input_tokens": 32510,
          "cache_creation_input_tokens": 2356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2356,
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

_source line 60 · 2026-05-14T05:38:07.619Z_

<details><summary>↩ Tool result · `toolu_01QQLXZTJ8nF4DMg9ZhcGXge`</summary>

```text
Web search results for query: ""A1" truncated VLA adaptive efficient transparent open-source 2026"

Links: [{"title":"[2604.05672] A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/abs/2604.05672"},{"title":"𝐴₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/html/2604.05672"},{"title":"解决VLA模型落地难，普通硬件也能跑！全透明全开源的高效VLA模型把推理成本砍掉76%_搜狐网","url":"https://m.sohu.com/a/1008080361_610300?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334"},{"title":"NVIDIA Announces Alpamayo Family of Open-Source AI Models and Tools to Accelerate Safe, Reasoning-Based Autonomous Vehicle Development | NVIDIA Newsroom","url":"https://nvidianews.nvidia.com/news/alpamayo-autonomous-vehicle-development"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of...","url":"https://openreview.net/forum?id=p1UF73ZvE0"},{"title":"NVIDIA Alpamayo: Open AI for Level 4 Autonomous Vehicles","url":"https://www.nvidia.com/en-us/solutions/autonomous-vehicles/alpamayo/"},{"title":"Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks | Proceedings of the 2025 Workshop on Large AI Systems and Models with Privacy and Security Analysis","url":"https://dl.acm.org/doi/10.1145/3733800.3763262"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"}]

Based on the search results, here's what I found about A1:

A1 is a fully open-source and transparent VLA (Vision-Language-Action) framework designed for low-cost, high-throughput inference without sacrificing manipulation success.

## Key Features and Performance

The model monitors action consistency across intermediate VLM layers to trigger early termination, and proposes Inter-Layer Truncated Flow Matching that warm-starts denoising across layers, enabling accurate actions with substantially fewer effective denoising iterations.

Across simulation benchmarks (LIBERO, VLABench) and real robots (Franka, AgiBot), A1 achieves state-of-the-art success rates while significantly reducing inference cost (e.g., up to 72% lower per-episode latency for flow-matching inference and up to 76.6% backbone computation reduction with minor performance degradation).

## Transparency and Open Source

The team releases the full training stack (training code, data/data-processing pipeline, intermediate checkpoints, and evaluation scripts) to enable end-to-end reproducibility. As a completely transparent system with no dependencies on closed-source components, it achieves an average success rate of 29.00% on RoboChallenge, ranking sixth overall.

## Research Affiliation

The research was submitted on April 7, 2026 by Rongtao Xu, and is associated with institutions including Sun Yat-sen University and MBZUAI according to the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fc35fd5-f152-4a32-b53c-6314b7ee5b75",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "76e391bc-de23-4ed9-840e-01fce6876894",
  "sourceToolAssistantUUID": "8fc35fd5-f152-4a32-b53c-6314b7ee5b75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-14T05:38:08.588Z_

<details><summary>↩ Tool result · `toolu_01BVf6JZ1ua3ub3RSHKaA5Vu`</summary>

```text
Web search results for query: ""Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" 2025"

Links: [{"title":"Enhancing Generalization in Vision-Language-Action Models","url":"https://gen-vla.github.io/"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/abs/2509.11417"},{"title":"Enhancing Generalization in Vision-Language-Action ...","url":"https://arxiv.org/pdf/2509.11417"},{"title":"[PDF] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Enhancing-Generalization-in-Vision-Language-Action-Grover-Gopalkrishnan/272525654b60ab7f4366e58244feadcfd2675aaf"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/html/2510.25616v1"},{"title":"[2511.19878] MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization","url":"https://arxiv.org/abs/2511.19878"},{"title":"10 Open Challenges Steering the Future of Vision-Language-Action Models","url":"https://arxiv.org/html/2511.05936v1"},{"title":"VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models","url":"https://arxiv.org/html/2601.03309v1"}]

I found research on "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" from 2025. Here's a summary:

## Overview

The paper presents a framework that enhances the generalization of Vision-Language-Action models by preserving pretrained representations. While Vision-language-action (VLA) models finetuned from powerful pretrained vision-language models (VLMs) promise to create generalist robots, the finetuning process often degrades the very representations that make them powerful, limiting generalization.

## Key Methodology

The method introduces a dual-encoder design to retain features, a string-based action tokenizer to align actions with language, and a co-training strategy to balance robot and vision-language data.

More specifically, the approach has three main components:

1. **Dual-encoder design**: Two encoders are used—one frozen to preserve robust, pretrained VLM features and one trainable to adapt to the specific robot task.

2. **String-based action tokenizer**: The tokenizer casts continuous actions into character sequences aligned with the model's pretraining domain.

3. **Co-training strategy**: The approach combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances.

## Results

The evaluations show significant improvements in robustness, generalization, and overall task success. Additionally, evaluations in simulation and on real robots show that the method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.

**Citation**: Grover et al., "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations," arXiv preprint arXiv:2509.11417, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95ae9385-6d87-431c-b8ee-9a3b50953f59",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "b4d3f068-48fd-4330-8d19-8c4bec47932d",
  "sourceToolAssistantUUID": "95ae9385-6d87-431c-b8ee-9a3b50953f59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T05:38:08.863Z_

<details><summary>↩ Tool result · `toolu_01T4RcdtRwMqax93XoMMZyHV`</summary>

```text
Web search results for query: "pi0 pi0.5 robustness perturbation Physical Intelligence 2025 2026"

Links: [{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054"},{"title":"π 0 : Our First Generalist Policy","url":"https://www.pi.website/blog/pi0"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://www.pi.website/download/pi0.pdf"},{"title":"[Paper Review] Pi0, Pi0.5, Pi0-FAST - Tracing the Path of Physical Intelligence (PI)","url":"https://bequiet-log.vercel.app/pi-review"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"π0 robot policy model. π0[1] is a generalist robot policy… | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/%CF%800-robot-policy-model-50d50b739a40"},{"title":"Physical Intelligence (π)","url":"https://www.pi.website/"},{"title":"π0 and π0-FAST: Vision-Language-Action Models for General Robot Control","url":"https://huggingface.co/blog/pi0"}]

Based on the search results, I found relevant information about pi0, pi0.5, and Physical Intelligence's work on robustness and perturbation. Here's what I found:

## Overview

π0 (pi-zero) is a general-purpose robot foundation model developed by Physical Intelligence over the past eight months. π₀.₅ is a new model based on π₀ that uses co-training on heterogeneous tasks to enable broad generalization, using data from multiple robots, high-level semantic prediction, web data, and other sources.

## Robustness and Perturbations

The frontiers of robot foundation model research include long-horizon reasoning and planning, autonomous self-improvement, robustness, and safety. The models aim to solve diverse tasks situated in varied physical environments, while responding intelligently to environmental constraints, language commands, and unexpected perturbations.

## Robustness Improvements

An interesting finding from real-world evaluations: Physical Intelligence suggested allowing a bit of randomness—called "sampling with temperature"—where letting π₀ occasionally pick the second-most likely action may help it recover from mistakes.

Additionally, training on lower quality data provides the model robustness in terms of recovering from mistakes while training on high-quality data provides examples on how to efficiently achieve goals, and combining these types of datasets can help train models that are efficient as well as robust.

## Timeline

π₀.₅ was published in April 2025, representing improvements over the original π₀ model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4415534f-6d5b-442e-b25f-5587dd4fd256",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "47eb2d4d-c2e5-489f-942a-106c91c8e06b",
  "sourceToolAssistantUUID": "4415534f-6d5b-442e-b25f-5587dd4fd256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T05:38:13.070Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016dvsuDGgB4szyiQtrXB4hD`</summary>

```json
{
  "query": "Gemini Robotics robustness generalization DeepMind VLA 2025 perturbation method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47eb2d4d-c2e5-489f-942a-106c91c8e06b",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vRX1ccTgcFcVb7BKDe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b7bf35d-09e3-4db0-9d1e-4aa5ce08ac7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWLgmfPRgagGhdEc8m7rwG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 3044,
      "cache_read_input_tokens": 34866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3044,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 64 · 2026-05-14T05:38:13.861Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qckd8hT8Pk2qwf9oRv73kF`</summary>

```json
{
  "query": "\"IBTM\" \"information bottleneck\" \"token merging\" transformer block CompTrack AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b7bf35d-09e3-4db0-9d1e-4aa5ce08ac7c",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vRX1ccTgcFcVb7BKDe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c47aa1d-f689-4826-ba93-884d41ba19ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWLgmfPRgagGhdEc8m7rwG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 3044,
      "cache_read_input_tokens": 34866,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3044
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1000,
          "output_tokens": 139,
          "cache_read_input_tokens": 34866,
          "cache_creation_input_tokens": 3044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3044,
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

_source line 65 · 2026-05-14T05:38:20.153Z_

<details><summary>↩ Tool result · `toolu_016dvsuDGgB4szyiQtrXB4hD`</summary>

```text
Web search results for query: "Gemini Robotics robustness generalization DeepMind VLA 2025 perturbation method"

Links: [{"title":"Gemini Robotics On-Device brings AI to local robotic devices — Google DeepMind","url":"https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/"},{"title":"Gemini Robotics — Google DeepMind","url":"https://deepmind.google/models/gemini-robotics/"},{"title":"Gemini Robotics 1.5 brings AI agents into the physical world — Google DeepMind","url":"https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/"},{"title":"[2503.20020] Gemini Robotics: Bringing AI into the Physical World","url":"https://arxiv.org/abs/2503.20020"},{"title":"Gemini Robotics 1.5: Pushing the Frontier of Generalist ...","url":"https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-1-5-Tech-Report.pdf"},{"title":"Gemini Robotics: Bringing AI into the Physical World","url":"https://arxiv.org/html/2503.20020v1"},{"title":"Introducing Gemini Robotics and Gemini Robotics-ER, AI models designed for robots to understand, act and react to the physical world. — Google DeepMind","url":"https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/"},{"title":"Gemini Robotics On-Device — Google DeepMind","url":"https://deepmind.google/models/gemini-robotics/gemini-robotics-on-device/"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"Google DeepMind introduces on-device Gemini AI model for robots - The Robot Report","url":"https://www.therobotreport.com/google-deepmind-introduces-on-device-gemini-ai-model-robots/"}]

I've found comprehensive information about DeepMind's Gemini Robotics models. Here's what the search results reveal:

## Overview

Gemini Robotics is an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots. Gemini Robotics executes smooth and reactive movements to tackle a wide range of complex manipulation tasks while also being robust to variations in object types and positions, handling unseen environments as well as following diverse, open vocabulary instructions.

## Robustness and Generalization

The models evaluate generalization ability across three axes: Visual Generalization (invariance to visual changes like lighting and distractor objects), Instruction Generalization (understanding paraphrasing and different languages), and behavioral robustness. On average, Gemini Robotics more than doubles performance on a comprehensive generalization benchmark compared to other state-of-the-art vision-language-action models.

## Key Advances

Gemini Robotics 1.5 shows a remarkable ability to learn across different embodiments and can transfer motions learned from one robot to another, without needing to specialize the model to each new embodiment. The model quickly adapts to new tasks, with as few as 50 to 100 demonstrations.

## Recent Releases

Gemini Robotics On-Device is the most powerful VLA model optimized to run locally on robotic devices. The search results do not contain specific details about a perturbation method mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b7bf35d-09e3-4db0-9d1e-4aa5ce08ac7c",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "52f5336f-6155-4cdb-bdfc-7b45a6504d92",
  "sourceToolAssistantUUID": "7b7bf35d-09e3-4db0-9d1e-4aa5ce08ac7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T05:38:20.556Z_

<details><summary>↩ Tool result · `toolu_01Qckd8hT8Pk2qwf9oRv73kF`</summary>

```text
Web search results for query: ""IBTM" "information bottleneck" "token merging" transformer block CompTrack AAAI 2026"

Links: [{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219v1"},{"title":"EFFICIENT VISION TRANSFORMER BY INFORMATION ...","url":"https://openreview.net/pdf?id=Jwgw3znxT3"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950v1"},{"title":"1 Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/pdf/2407.15219"},{"title":"CompTrack: Information Bottleneck‑Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking","url":"https://arxiv.org/html/2511.15580"},{"title":"Adaptive Token Merging for Efficient Transformer Semantic Communication at the Edge","url":"https://arxiv.org/html/2509.09955"},{"title":"DTMFormer: Dynamic Token Merging for Boosting Transformer-Based Medical","url":"https://ojs.aaai.org/index.php/AAAI/article/view/28394/28770"},{"title":"Efficient Transformer Adaptation with Soft Token Merging | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/10678039"}]

Based on the web search results, I found relevant information about both IBTM and CompTrack:

## IBTM (Information Bottleneck inspired Token Merging)

IBTM is a novel compact transformer block that performs token merging in a learnable scheme inspired by the information bottleneck principle. IBTM is compatible with many popular and compact transformer networks, such as MobileViT and EfficientViT, and it reduces the FLOPs and the inference time of the vision transformers while maintaining or even improving the prediction accuracy.

The IBTM is motivated by the reduction of the Information Bottleneck (IB), and a novel and separable variational upper bound for the IB loss is derived. In experiments, all the transformer blocks in popular vision transformers, including MobileViT, EfficientViT, ViT, and Swin, are replaced with IBTM blocks.

## CompTrack (AAAI 2026)

CompTrack is a framework designed to eliminate both spatial and information redundancy, employing a Spatial Foreground Predictor (SPF) to address spatial redundancy and an Information Bottleneck-guided Dynamic Token Compression (IB-DTC) module that resolves informational redundancy. This module adaptively compresses the redundant foreground into a compact and highly informative set of proxy tokens for precise and efficient tracking. CompTrack achieves top-performing tracking performance with superior efficiency, running at a real-time 90 FPS on a single RTX 3090 GPU.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c47aa1d-f689-4826-ba93-884d41ba19ba",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8b4d08ae6a7b69fc",
  "type": "user",
  "uuid": "227bd1d2-7d88-4dc6-9fd6-cab215d4f7dc",
  "sourceToolAssistantUUID": "4c47aa1d-f689-4826-ba93-884d41ba19ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-14T05:40:05.236Z_

Based on my extensive research, here is a comprehensive report of competing and related work that the paper generator may have missed:

---

## Comprehensive Competitor Landscape for VLA Robustness Paper

### CATEGORY 1: Direct VLA Robustness Methods (Highest Novelty Threat)

**1. RobustVLA (ICLR 2026 submission)**
- *Title*: "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models"
- *Venue*: OpenReview/arXiv (2511.01331)
- *Method*: Lightweight online RL post-training with two key regularizations -- Jacobian regularization (mitigates sensitivity to observation noise) and smoothness regularization (stabilizes policies under action perturbations). Formulates robustness as a multi-armed bandit problem with UCB to identify the most harmful noise automatically.
- *Results*: +12.6% absolute on pi0 backbone, +10.4% on OpenVLA across 17 perturbations; 50.6x faster than visual-robust BYOVLA.
- **NOVELTY THREAT: HIGH** -- If the proposed paper also uses regularization or RL-based post-training for robustness, this is a direct competitor.

**2. "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations" (ICLR 2026, published)**
- *Venue*: ICLR 2026 (conference paper)
- *arXiv*: 2510.00037
- *Method*: Offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. Proposes multi-modal perturbation framework covering 17 uncertainties in 4 modalities.
- *Key finding*: Action is the most fragile modality; existing visual-robust VLAs do not transfer to other modalities; pi0 demonstrates inherently superior robustness.
- **NOVELTY THREAT: HIGH** -- Establishes the benchmark and baseline for VLA multi-modal robustness. Any new paper must compare against this.

**3. Corruption Restoration Transformer (CRT) (Feb 2026)**
- *Title*: "Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs"
- *arXiv*: 2602.01158
- *Method*: Plug-and-play, model-agnostic vision transformer placed upstream of the VLA. Uses adversarial training to restore clean observations from corrupted inputs. No fine-tuning of the underlying VLA needed.
- *Key insight*: VLAs drop from 90% to 2% success under common sensor artifacts; CRT restores performance with negligible overhead.
- **NOVELTY THREAT: MEDIUM-HIGH** -- If the proposed paper also uses a modular approach to improve robustness without retraining, CRT is a direct competitor.

**4. "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" (2025)**
- *arXiv*: 2509.11417
- *Method*: Dual-encoder design (one frozen, one trainable), string-based action tokenizer, co-training strategy with robot + VL data. Prevents representation degradation during finetuning.
- **NOVELTY THREAT: MEDIUM** -- Addresses robustness through representation preservation rather than token selection, but related if the proposed paper argues about maintaining informative representations.

---

### CATEGORY 2: Token Selection/Pruning for VLAs (High Relevance to Token-Based Approaches)

**5. VLA-IAP (March 2026)**
- *Title*: "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models"
- *arXiv*: 2603.22991
- *Method*: Shifts from Perception-First to Interaction-First pruning paradigm. Introduces geometric prior mechanism and dynamic scheduling (conservative-to-aggressive transition). Preserves structurally critical regions for manipulation.
- *Results*: 97.8% success rate with 1.54x speedup.
- **NOVELTY THREAT: HIGH** -- If the proposed paper uses task-aware token selection for robustness, VLA-IAP already does this for efficiency AND maintains/improves success rates. The "interaction alignment" framing is conceptually close to "action-relevant token selection."

**6. VLA-Pruner (Nov 2025)**
- *Title*: "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference"
- *arXiv*: 2511.16449
- *Method*: Dual-level importance criterion -- vision-language prefill attention for semantic relevance AND action decode attention (estimated via temporal smoothing) for action-level importance.
- **NOVELTY THREAT: HIGH** -- Explicitly addresses the dual-system nature (understanding + action) and selects tokens relevant to both. If the proposed paper argues that action-aware token selection improves robustness, VLA-Pruner already provides the selection mechanism.

**7. SpecPrune-VLA (Sep 2025, updated Feb 2026)**
- *Title*: "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning"
- *arXiv*: 2509.05614
- *Method*: Action-level static pruning + layer-level dynamic pruning + lightweight action-aware controller that classifies actions as coarse/fine-grained and adjusts pruning aggressiveness.
- *Results*: 1.57x speedup in LIBERO, 1.70x real-world with negligible degradation.
- **NOVELTY THREAT: MEDIUM-HIGH** -- The "action-aware" adaptive pruning is conceptually similar to adaptive token selection for robustness.

**8. Compressor-VLA (Nov 2025)**
- *Title*: "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation"
- *arXiv*: 2511.18950
- *Method*: Hybrid instruction-conditioned compression with Semantic Task Compressor (STC) + Spatial Refinement Compressor (SRC). Dynamically modulated by language instruction.
- *Results*: 59% FLOPs reduction, 3x token reduction on LIBERO.
- **NOVELTY THREAT: MEDIUM** -- Instruction-guided compression is related if the proposed paper uses task context to guide token selection for robustness.

**9. ETA-VLA (March 2026)**
- *Title*: "ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models"
- *arXiv*: 2603.25766
- *Method*: Temporal Fusion Module (TFM) + Intra-LLM Sparse Aggregator (ILSA) with text-guided scoring + diversity-preserving sparsification.
- *Results*: 85% token pruning, 61% FLOPs reduction, retains 94% accuracy.
- **NOVELTY THREAT: MEDIUM** -- Text-guided scoring for token selection is relevant if proposed paper uses similar mechanisms.

**10. VLA-Cache (Feb 2025)**
- *Title*: "VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation"
- *arXiv*: 2502.02175
- *Method*: Dynamic token selection that identifies task-relevant tokens, fraction of reused tokens dynamically adjusted at each layer based on attention distribution.
- **NOVELTY THREAT: MEDIUM** -- Adaptive per-layer token selection based on task relevance.

**11. Token Expand-Merge (TEAM-VLA) (Dec 2025)**
- *Title*: "Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models"
- *arXiv*: 2512.09927
- *Method*: Dual strategy of early context pruning + mid-layer merging with dynamic token expansion near attention-highlighted regions under action-aware guidance.
- **NOVELTY THREAT: MEDIUM** -- Action-aware merging guidance is related.

**12. A1: Truncated VLA (April 2026)**
- *Title*: "A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model"
- *arXiv*: 2604.05672
- *Method*: Monitors action consistency across intermediate VLM layers to trigger early termination. Inter-Layer Truncated Flow Matching that warm-starts denoising across layers.
- *Results*: Up to 76.6% backbone computation reduction with minor performance degradation.
- **NOVELTY THREAT: LOW-MEDIUM** -- Early termination based on consistency is a form of adaptive computation.

---

### CATEGORY 3: Information Bottleneck in Robot Learning (Critical Overlap)

**13. BC-IB (ICML 2025) -- MOST RELEVANT**
- *Title*: "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation"
- *Venue*: ICML 2025 (published)
- *arXiv*: 2502.02853
- *Method*: Incorporates the Information Bottleneck (IB) principle into behavior cloning. Uses mutual information to quantify and mitigate redundancy in latent representations. Reduces MI between input and latent space to compress task-irrelevant features.
- *Results*: Consistent improvements on CortexBench and LIBERO. Reduces MI to 1/4 original value, +7.7% success on LIBERO-Goal.
- **NOVELTY THREAT: VERY HIGH** -- If the proposed paper combines information bottleneck with token selection for VLA robustness, BC-IB already establishes the IB-for-robot-manipulation paradigm. The proposed work would need to clearly differentiate from this.

**14. Token Bottleneck (ToBo) (NeurIPS 2025)**
- *Title*: "Token Bottleneck: One Token to Remember Dynamics"
- *Venue*: NeurIPS 2025
- *arXiv*: 2507.06543
- *From*: NAVER AI Lab
- *Method*: Self-supervised pipeline that squeezes a scene into a single bottleneck token and predicts subsequent scene using minimal patches as hints. Evaluated on robot manipulation tasks.
- **NOVELTY THREAT: HIGH** -- Explicitly uses a token bottleneck concept for robot manipulation with demonstrated robustness on physical robots.

**15. OneWM-VLA (May 2026)**
- *Title*: "One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy"
- *arXiv*: 2605.07931
- *Method*: Adaptive Attention Pooling distills each view into a single semantic latent token per frame. Joint flow-matching objective generates future latent stream + action trajectory together.
- *Key finding*: Per-frame visual bandwidth can be reduced to a single token without compromising long-horizon performance.
- **NOVELTY THREAT: HIGH** -- Demonstrates that extreme information compression (bottleneck to 1 token) works for VLA without hurting performance, which directly relates to information bottleneck arguments.

---

### CATEGORY 4: Information Bottleneck + Token Pruning/Selection (Any Domain)

**16. IBTM - Information Bottleneck inspired Token Merging (2025-2026)**
- *Venue*: OpenReview (under review)
- *Method*: Novel transformer block (IBTM) that performs learnable token merging based on IB principle. Derives separable variational upper bound for IB loss. Compatible with MobileViT, EfficientViT, ViT, Swin.
- **NOVELTY THREAT: HIGH** -- This is EXACTLY the combination of information bottleneck + token merging in a general vision transformer setting. If the proposed paper claims novelty in combining IB with token selection, IBTM already does this.

**17. CompTrack (AAAI 2026)**
- *Title*: "CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking"
- *Venue*: AAAI 2026
- *Method*: Information Bottleneck-guided Dynamic Token Compression (IB-DTC) that adaptively compresses redundant foreground into compact proxy tokens. Spatial Foreground Predictor + IB-DTC.
- *Results*: Real-time 90 FPS on RTX 3090.
- **NOVELTY THREAT: MEDIUM-HIGH** -- Demonstrates IB-guided dynamic token compression in a different domain (tracking), showing the concept is not novel to any single domain.

---

### CATEGORY 5: Major Lab Efforts (Physical Intelligence, DeepMind, Berkeley)

**18. Physical Intelligence pi0 / pi0.5 (2024-2025)**
- pi0 uses pre-trained VLM connected to action expert with flow matching loss.
- pi0.5 adds co-training on heterogeneous tasks for open-world generalization.
- Robustness comes from training on diverse/lower quality data (recovery from mistakes).
- Already shown to have inherently superior robustness in ICLR 2026 benchmarks.
- **Status**: Not a paper on robustness methods per se, but the baseline that robustness papers compare against.

**19. Google DeepMind Gemini Robotics (March 2025)**
- *arXiv*: 2503.20020
- *Method*: Advanced VLA generalist model with demonstrated robustness to variations in object types, positions, unseen environments, and open vocabulary instructions. More than doubles performance on generalization benchmarks vs. other VLAs.
- Gemini Robotics 1.5 shows cross-embodiment transfer.
- **NOVELTY THREAT: MEDIUM** -- Demonstrates that scale + large-scale pretraining achieves robustness without specialized methods, potentially undermining the motivation for specialized robustness techniques.

**20. "Do World Action Models Generalize Better than VLAs?" (March 2026)**
- *arXiv*: 2603.22078
- *From*: Huawei/U of Toronto
- *Finding*: WAMs achieve strong robustness (LingBot-VA: 74.2%, Cosmos-Policy: 82.2%) but struggle with geometric perturbations and have 4.8x slower inference. pi0.5 achieves comparable robustness with extensive training.
- **NOVELTY THREAT: LOW-MEDIUM** -- Comparative benchmark, but relevant if it shows alternative paths to robustness.

---

### CATEGORY 6: Regarding Specific Papers Mentioned

**21. "RoboPro VLA"**
- I could NOT find a paper specifically titled "RoboPro VLA" in any search. This may be a misremembered name. The closest match is **RobustVLA** (described above in #1/#2). If you have additional details about this paper, I can search more specifically.

**22. "FastVLA token merging"**
- I could NOT find a paper specifically titled "FastVLA." The closest matches are:
  - **FAST** (Physical Intelligence): Frequency-space Action Sequence Tokenization for efficient action tokenization (not visual token merging).
  - **FASTer**: Learnable action tokenizer with block-wise decoding.
  - **TEAM-VLA** (Token Expand-Merge): Training-free visual token compression.
  - **TTF-VLA**: Temporal Token Fusion via Pixel-Attention Integration.
  
  The landscape of VLA token efficiency papers is extremely crowded (see Category 2 above), so "FastVLA" may refer to any of these or an unpublished/in-submission work.

---

## Summary: Key Novelty Threats

The strongest threats to a paper proposing "information bottleneck + token selection for VLA robustness" are:

| Paper | Why It's a Threat |
|-------|------------------|
| **BC-IB (ICML 2025)** | Already applies IB to robot manipulation, proves it removes task-irrelevant info |
| **IBTM (2025-2026)** | Combines IB principle with token merging in vision transformers directly |
| **VLA-IAP (March 2026)** | Interaction-aware token pruning that improves both efficiency AND task success |
| **VLA-Pruner (Nov 2025)** | Dual-level (semantic + action) token selection |
| **RobustVLA (ICLR 2026)** | RL-based robustness post-training with theoretical regularization |
| **Token Bottleneck/ToBo (NeurIPS 2025)** | Token bottleneck concept for robot manipulation |
| **OneWM-VLA (May 2026)** | Extreme bottleneck (1 token/frame) works without performance loss |
| **CRT (Feb 2026)** | Plug-and-play robustness restoration module |

The proposed paper would need to clearly differentiate by showing that (a) combining IB-guided token selection specifically improves robustness (not just efficiency), (b) the mechanism is fundamentally different from VLA-IAP's interaction alignment and VLA-Pruner's dual-level approach, and (c) it goes beyond what BC-IB achieves by operating at the token level rather than the latent representation level.

---

Sources:
- [RobustVLA](https://arxiv.org/abs/2511.01331)
- [On Robustness of VLA against Multi-Modal Perturbations (ICLR 2026)](https://arxiv.org/abs/2510.00037)
- [CRT - Improving Robustness by Restoring Corrupted Visual Inputs](https://arxiv.org/abs/2602.01158)
- [VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment](https://arxiv.org/abs/2603.22991)
- [VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning](https://arxiv.org/abs/2511.16449)
- [SpecPrune-VLA: Action-Aware Self-Speculative Pruning](https://arxiv.org/abs/2509.05614)
- [Compressor-VLA: Instruction-Guided Visual Token Compression](https://arxiv.org/abs/2511.18950)
- [ETA-VLA: Efficient Token Adaptation](https://arxiv.org/abs/2603.25766)
- [VLA-Cache: Adaptive Token Caching](https://arxiv.org/html/2502.02175v2)
- [Token Expand-Merge (TEAM-VLA)](https://arxiv.org/abs/2512.09927)
- [A1: Truncated VLA](https://arxiv.org/abs/2604.05672)
- [BC-IB: Information Bottleneck for Robot Manipulation (ICML 2025)](https://arxiv.org/abs/2502.02853)
- [Token Bottleneck (ToBo) - NeurIPS 2025](https://arxiv.org/abs/2507.06543)
- [OneWM-VLA: One Token Per Frame](https://arxiv.org/abs/2605.07931)
- [IBTM: Information Bottleneck Inspired Token Merging](https://openreview.net/forum?id=Jwgw3znxT3)
- [CompTrack: IB-Guided Dynamic Token Compression (AAAI 2026)](https://arxiv.org/html/2511.15580)
- [Enhancing Generalization by Preserving Pretrained Representations](https://arxiv.org/abs/2509.11417)
- [LIBERO-Plus: In-depth Robustness Analysis](https://arxiv.org/abs/2510.13626)
- [Do World Action Models Generalize Better than VLAs?](https://arxiv.org/abs/2603.22078)
- [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020)
- [Physical Intelligence pi0.5](https://arxiv.org/abs/2504.16054)
- [FAST: Efficient Action Tokenization](https://arxiv.org/html/2501.09747v1)
- [TTF-VLA: Temporal Token Fusion](https://arxiv.org/abs/2508.19257)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "227bd1d2-7d88-4dc6-9fd6-cab215d4f7dc",
  "isSidechain": true,
  "agentId": "a8b4d08ae6a7b69fc",
  "requestId": "req_011Cb1vSP7t8f6QFFQibJG93",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dca7b67-227f-4501-956f-3c59b178eba7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxaeHi7rtZA8YGWFv3btuU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2994,
      "cache_read_input_tokens": 37910,
      "output_tokens": 5076,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2994
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5076,
          "cache_read_input_tokens": 37910,
          "cache_creation_input_tokens": 2994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2994,
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
