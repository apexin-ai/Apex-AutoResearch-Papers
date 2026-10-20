# Research conversation: You are helping me review an ML research idea about "token masking as regularization during VLA (Vision-Language-Action)

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 94
- **Recorded user turns:** 1
- **Tool calls:** 41
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6466d84670312cd2.jsonl`
- **Structured JSON:** [`ca96183a68bc0b7fe34b.json`](../../sessions/ca/ca96183a68bc0b7fe34b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

94 recorded events

### User

_source line 1 · 2026-05-13T04:42:32.382Z_

You are helping me review an ML research idea about "token masking as regularization during VLA (Vision-Language-Action) finetuning." I need you to search for competitive and concurrent work that the idea may have missed. Use WebSearch extensively.

Search for the following:

1. **Token masking/dropout in VLAs**: Search "token masking VLA 2025 2026", "visual token dropout robot learning", "token pruning VLA generalization"

2. **VLA robustness/generalization recent work**: Search "VLA generalization out-of-distribution 2026", "vision language action robust finetuning 2026"

3. **Information bottleneck in robotics/VLA**: Search "information bottleneck robot learning", "information bottleneck VLA", "IB regularization vision language action"

4. **VLA-Pruner**: Search for "VLA-Pruner temporal visual token pruning" — the idea mentions this but doesn't detail it. Check if it's a close competitor.

5. **LIBERO-Plus benchmark**: Search "LIBERO-Plus robustness benchmark VLA" to verify this exists.

6. **SimplerEnv visual variants**: Search "SimplerEnv visual variant aggregation VLA evaluation" to verify this benchmark exists and is standard.

7. **CRL-VLA (arXiv 2602.03445)**: Search for this continual learning VLA paper.

8. **VLM2VLA / Actions as Language (ICLR 2026)**: Verify this exists.

9. **Gen-VLA (arXiv 2509.11417)**: Verify this exists.

10. **Recent arXiv (Feb-May 2026) on VLA regularization**: Search "VLA regularization arXiv 2026", "vision language action model finetuning 2026" to find any very recent concurrent work.

For each search, report what you found, whether the papers exist, and whether any of them are close competitors to the proposed "Counterfactual Token Masking" idea. Use WebSearch and WebFetch on the most important results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "1fd21dba-08c9-4721-aca2-1f10a428508b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T04:42:32.384Z_

```json
{
  "parentUuid": "1fd21dba-08c9-4721-aca2-1f10a428508b",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
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
  "uuid": "7b873929-1de0-4bc9-be1e-86268b9d58a3",
  "timestamp": "2026-05-13T04:42:32.384Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T04:42:36.051Z_



I'll conduct a comprehensive search for competitive and concurrent work related to "Counterfactual Token Masking" for VLA finetuning. Let me start by loading the WebSearch and WebFetch tools, then systematically search across all 10 areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b873929-1de0-4bc9-be1e-86268b9d58a3",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxNezydjLi2mtCAbffE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a9b9f6b-03d6-4724-a6f7-bf5a7b7ae770",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NanLvTUpQ6dybUMj7buPKH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1037,
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

_source line 4 · 2026-05-13T04:42:36.289Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HQzEAtmotMnwHxH4rxw2zh`</summary>

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
  "parentUuid": "0a9b9f6b-03d6-4724-a6f7-bf5a7b7ae770",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxNezydjLi2mtCAbffE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "127ef9dc-648c-4bb1-a71b-3010337644de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NanLvTUpQ6dybUMj7buPKH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 8223,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 138,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 1037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1037,
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

_source line 5 · 2026-05-13T04:42:36.296Z_

<details><summary>↩ Tool result · `toolu_01HQzEAtmotMnwHxH4rxw2zh`</summary>

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
  "parentUuid": "127ef9dc-648c-4bb1-a71b-3010337644de",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "9cdcfe78-77f9-4da2-b72c-1e0bbebffd93",
  "sourceToolAssistantUUID": "127ef9dc-648c-4bb1-a71b-3010337644de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T04:42:39.222Z_



Now let me launch all the searches in parallel across the 10 areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cdcfe78-77f9-4da2-b72c-1e0bbebffd93",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxNx1AtHQjxSAmj1UHR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00dc6f7a-ebe2-4b80-a44b-4dba969a396d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT1P81Rh5oEFGqRP9ZxCWU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1947,
      "cache_read_input_tokens": 9260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1947,
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

_source line 7 · 2026-05-13T04:42:39.853Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VzSq8eQM7ozyTohCxod1NE`</summary>

```json
{
  "query": "token masking VLA vision language action 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00dc6f7a-ebe2-4b80-a44b-4dba969a396d",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxNx1AtHQjxSAmj1UHR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "860b30ca-cfc1-4aa0-9e1a-4e94d5eaedf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT1P81Rh5oEFGqRP9ZxCWU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1947,
      "cache_read_input_tokens": 9260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1947,
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

_source line 8 · 2026-05-13T04:42:39.856Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0168x24f3yBDCxpZef6j6BJ2`</summary>

```json
{
  "query": "visual token dropout robot learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "860b30ca-cfc1-4aa0-9e1a-4e94d5eaedf7",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxNx1AtHQjxSAmj1UHR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10b8d595-ee6f-4ce3-846a-2ff288af2a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT1P81Rh5oEFGqRP9ZxCWU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1947,
      "cache_read_input_tokens": 9260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1947,
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

_source line 9 · 2026-05-13T04:42:40.173Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TeGV2Vs6TZmUQF56syUzFD`</summary>

```json
{
  "query": "token pruning VLA generalization robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10b8d595-ee6f-4ce3-846a-2ff288af2a6f",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxNx1AtHQjxSAmj1UHR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13eba76d-89ef-4d8e-9034-353553dc96f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT1P81Rh5oEFGqRP9ZxCWU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1947,
      "cache_read_input_tokens": 9260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1947,
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

_source line 10 · 2026-05-13T04:42:40.648Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LuqmirbuHpMHzm7XnMP2Ue`</summary>

```json
{
  "query": "VLA generalization out-of-distribution 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13eba76d-89ef-4d8e-9034-353553dc96f4",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxNx1AtHQjxSAmj1UHR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd21ad15-0afb-44cd-bb26-68802c585ba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT1P81Rh5oEFGqRP9ZxCWU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1947,
      "cache_read_input_tokens": 9260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1947,
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

_source line 11 · 2026-05-13T04:42:40.821Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WaNHsT4TTcjsfS8nque2by`</summary>

```json
{
  "query": "vision language action robust finetuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd21ad15-0afb-44cd-bb26-68802c585ba0",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxNx1AtHQjxSAmj1UHR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb4bc20e-cb44-4565-b952-829b4d2512e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT1P81Rh5oEFGqRP9ZxCWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1947,
      "cache_read_input_tokens": 9260,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1947
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 9260,
          "cache_creation_input_tokens": 1947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1947,
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

_source line 12 · 2026-05-13T04:42:47.066Z_

<details><summary>↩ Tool result · `toolu_0168x24f3yBDCxpZef6j6BJ2`</summary>

```text
Web search results for query: "visual token dropout robot learning 2025 2026"

Links: [{"title":"From Vision-Language Models to Robot Control — Without Forgetting – Princeton Laboratory for Artificial Intelligence Research Blog","url":"https://blog.ai.princeton.edu/2026/04/23/from-vision-language-models-to-robot-control-without-forgetting/"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Multimodal learning with next-token prediction for large multimodal models | Nature","url":"https://www.nature.com/articles/s41586-025-10041-x"},{"title":"HERO: Rethinking Visual Token Early Dropping in High-Resolution Large Vision-Language Models","url":"https://arxiv.org/html/2509.13067v1"},{"title":"GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub","url":"https://github.com/YanjieZe/Paper-List"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Rethinking Visual Token Reduction in LVLMs under Cross-modal Misalignment","url":"https://arxiv.org/html/2506.22283v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"}]

I found several relevant results on visual token dropout and robot learning in 2025-2026. Here's what the search revealed:

## Visual Token Dropout and Reduction in VLMs

HERO is an inference-time visual token pruning strategy that effectively improves the computational efficiency of high-resolution Large Vision-Language Models with minimal performance degradation. This approach addresses the challenge that dense patch-level tokenization encodes visual inputs as long sequences of tokens to capture rich fine-grained semantics, but this dense representation comes at a significant computational cost.

Recent studies have explored reducing the number of visual tokens either before or within the layers of large language models, with approaches like Yang et al. (2025), Zhang et al. (2025c), Chen et al. (2024b), and Xing et al. (2025).

## Vision-Language-Action Models in Robot Learning

The field of robot learning is increasingly incorporating visual token techniques. UniVLA (Wang et al., 2025) incorporates world modeling during post-training over a native multimodal tokenization framework, allowing the model to absorb causal dynamics from large-scale video data without introducing a separate external world model.

Additionally, Emu3 demonstrates interleaved vision–language generation and vision–language–action modelling for robotic manipulation.

A comprehensive analysis of 164 Vision-Language-Action model submissions at ICLR 2026 discovered trends in discrete diffusion VLAs, reasoning models, and benchmarks including LIBERO, CALVIN, and SIMPLER.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10b8d595-ee6f-4ce3-846a-2ff288af2a6f",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "cad0864a-0d06-427d-8944-cbe551b9e275",
  "sourceToolAssistantUUID": "10b8d595-ee6f-4ce3-846a-2ff288af2a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T04:42:48.134Z_

<details><summary>↩ Tool result · `toolu_01VzSq8eQM7ozyTohCxod1NE`</summary>

```text
Web search results for query: "token masking VLA vision language action 2025 2026"

Links: [{"title":"Unified Vision-Language-Action Tokenization","url":"https://www.emergentmind.com/topics/unified-vision-language-action-vla-tokenization"},{"title":"VLA (Vision Language Action) · GitHub","url":"https://gist.github.com/sikang99/78a2c2ff736e7ce681d9d800e06dabd5"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.pi.website/download/fast.pdf"},{"title":"Unified Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=PklMD8PwUy"},{"title":"CVPR 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html"},{"title":"[2501.09747] FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2501.09747"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175v2"},{"title":"FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding | OpenReview","url":"https://openreview.net/forum?id=k6nTUFoqeT"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"}]

Based on the search results, I found several important developments in token masking and Vision-Language-Action (VLA) models for 2025-2026:

## Key Developments in Token Masking for VLAs

**Masked-Diffusion Decoding and Adaptive Token Management:**

At each step, the transformer predicts distributions over all masked positions, adaptively commits high-confidence tokens, and remasks uncertain slots, which removes left-to-right bottlenecks and permits error correction across inference rounds.

**VLA-Cache: Efficient Token Caching:**

Partial token caching or masking schemes (VLA-Cache) reduce inference cost by up to 27%, supporting real-time control. More specifically, VLA-Cache is a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames, exploiting temporal continuity in robotic manipulation, while selectively re-computing task-relevant tokens that are environmentally sensitive.

**Hierarchical Token Planning:**

In LoHoVLA, token decoding is organized into alternating planning and control loops where a sequence of sub-task tokens is generated and re-used for several control steps unless failures occur, boosting task robustness and sample efficiency.

**Broader VLA Tokenization Framework:**

Unified vocabularies improve cross-modal alignment and reduce the cost of transferring or scaling models across tasks and domains. Additionally, a comprehensive survey details eight major classes of action tokens, which can co-exist within unified token streams.

These advances represent significant progress in making VLA systems more efficient and capable through sophisticated token masking, caching, and management strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "860b30ca-cfc1-4aa0-9e1a-4e94d5eaedf7",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "553952e0-8172-4e8f-877a-e2fb10f465d8",
  "sourceToolAssistantUUID": "860b30ca-cfc1-4aa0-9e1a-4e94d5eaedf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T04:42:48.490Z_

<details><summary>↩ Tool result · `toolu_01WaNHsT4TTcjsfS8nque2by`</summary>

```text
Web search results for query: "vision language action robust finetuning 2026"

Links: [{"title":"[2512.08333] Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging","url":"https://arxiv.org/abs/2512.08333"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/17/"},{"title":"Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging","url":"https://arxiv.org/html/2512.08333"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v2"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"A comprehensive survey of Vision–Language Models: Pretrained models, fine-tuning, prompt engineering, adapters, and benchmark datasets - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1566253525006955"},{"title":"Prompt-Robust Vision-Language Models via Meta-Finetuning | OpenReview","url":"https://openreview.net/forum?id=3wZ6IIwPJq"}]

Based on the search results, here are the key findings on vision-language-action (VLA) robust finetuning research from 2026:

## Recent VLA Finetuning Research

**Robust Parameter Merging Approach**

A notable recent paper submitted in December 2025 and revised in February 2026 addresses robust finetuning of vision-language-action robot policies via parameter merging. The core problem is that when generalist policies are finetuned on limited demonstrations of a new task, they often overfit to the specific demonstrations—losing their prior abilities to solve a wide variety of generalist tasks. The proposed solution involves merging the pretrained and finetuned policy checkpoints in weight space to achieve significantly improved generalization on target tasks at no additional training or inference cost.

**Reinforcement Fine-Tuning (RFT)**

Another approach called VLA-RFT leverages a data-driven world model as a controllable simulator that predicts future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards. This method exhibits strong robustness under perturbed conditions and surpasses strong supervised baselines with fewer than 400 fine-tuning steps.

**Parameter-Efficient Fine-Tuning**

Recent VLA works explore LoRA (Low-Rank Adaptation) for fine-tuning, with OpenVLA being among the earliest to adopt LoRA for lower training memory consumption, and evidence showing that LoRA better preserves pre-trained VLM knowledge during VLA adaptation.

These approaches represent the current frontier of making VLA models more robust and efficient during the fine-tuning process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb4bc20e-cb44-4565-b952-829b4d2512e7",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "0b5bc8c6-a25e-4245-81e7-8f24315bbdcf",
  "sourceToolAssistantUUID": "cb4bc20e-cb44-4565-b952-829b4d2512e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T04:42:48.706Z_

<details><summary>↩ Tool result · `toolu_01TeGV2Vs6TZmUQF56syUzFD`</summary>

```text
Web search results for query: "token pruning VLA generalization robotics"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"(PDF) VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://www.researchgate.net/publication/388685612_VLA-Cache_Towards_Efficient_Vision-Language-Action_Model_via_Adaptive_Token_Caching_in_Robotic_Manipulation/fulltext/67a2d84c8311ce680c52f13c/VLA-Cache-Towards-Efficient-Vision-Language-Action-Model-via-Adaptive-Token-Caching-in-Robotic-Manipulation.pdf?origin=scientificContributions"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"GitHub - KwanWaiPang/Awesome-VLA: Paper Survey for Visual Language Action · GitHub","url":"https://github.com/KwanWaiPang/Awesome-VLA"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"}]

I found several recent research papers on token pruning for Vision-Language-Action (VLA) models in robotics. Here's a summary of the key findings:

## Overview

Vision-Language-Action (VLA) models are a family of large vision-language models which directly translate visual information and language instructions into executable action policies, and they have shown remarkable promise in robotics manipulation, yet their high computational cost hinders real-time deployment.

## Key Research Directions

**Interaction-Aligned Pruning**: Existing visual token pruning methods mainly rely on semantic saliency or simple temporal cues, overlooking the continuous physical interaction, a fundamental property of VLA tasks, often pruning visually sparse yet structurally critical regions that support manipulation. VLA-IAP achieves a 97.8% success rate with a 1.25× speedup on the LIBERO benchmark, and up to 1.54× speedup while maintaining performance comparable to the unpruned backbone, demonstrating superior and consistent performance across multiple model architectures and simulation environments, as well as a real robot platform.

**Adaptive Token Pruning**: LightVLA is the first work to apply adaptive visual token pruning to VLA tasks with the collateral goals of efficiency and performance.

**Geometry-Aware Resampling**: Breaking the compression trade-off requires rethinking compression as a geometry-aware, continuous token resampling in the vision encoder, with the Differentiable Grid Sampler (GridS) performing task-aware, continuous resampling of visual tokens in VLA by adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation.

**Joint Scheduling and Pruning**: Model scheduling and spatio-semantic dual-aware token pruning work jointly to guide the VLA in focusing on critical actions and salient visual information, achieving up to 1.5× acceleration with less than 3% drop in accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13eba76d-89ef-4d8e-9034-353553dc96f4",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "2aee40b6-b7f0-4ac4-b5d0-0e0b0fe7e937",
  "sourceToolAssistantUUID": "13eba76d-89ef-4d8e-9034-353553dc96f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T04:42:50.051Z_

<details><summary>↩ Tool result · `toolu_01LuqmirbuHpMHzm7XnMP2Ue`</summary>

```text
Web search results for query: "VLA generalization out-of-distribution 2026"

Links: [{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://rlvla.github.io/"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"},{"title":"HALO: A Unified Vision-Language-Action Model for ...","url":"https://arxiv.org/pdf/2602.21157"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"[2505.19789] What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/abs/2505.19789"},{"title":"VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251014902Z/abstract"}]

Based on the search results, here's what I found about VLA generalization and out-of-distribution research in 2026:

## Key Research Findings

Several recent studies focus on improving Vision-Language-Action (VLA) model generalization to out-of-distribution scenarios:

### Reinforcement Learning for VLA Generalization
In out-of-distribution tests, RL enhances VLA generalization substantially in Execution, improves moderately in Semantics, and performs on par with SFT for Vision. RL fine-tuning, particularly with PPO, significantly enhances generalization in semantic understanding and execution robustness over SFT, while maintaining comparable visual robustness.

### Preserving Pretrained Representations
Approaches that preserve pretrained representations yield stronger generalization to out-of-distribution visuals, such as backgrounds, table textures, and distractor objects, as well as to varied language commands, leading to higher task success rates.

### Multimodal Reasoning Approaches
The HALO model validates effectiveness in challenging out-of-distribution and real-world settings, highlighting it as a scalable and generalizable human-like VLA reasoning paradigm.

### World Model-Based Reinforcement Fine-Tuning
World-model-based RFT is established as a practical post-training paradigm to enhance the generalization and robustness of VLA models.

### Out-of-Distribution Object Handling
VLA models' success rate drops significantly when faced with object concepts outside the training data, but an agentic framework approach mitigates generalization failure when handling out-of-distribution objects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd21ad15-0afb-44cd-bb26-68802c585ba0",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "89f49a9d-a562-421c-bf15-9ae53b163d01",
  "sourceToolAssistantUUID": "cd21ad15-0afb-44cd-bb26-68802c585ba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-13T04:42:52.486Z_

Good, I'm getting rich results. Let me continue with the remaining searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89f49a9d-a562-421c-bf15-9ae53b163d01",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxPxaRUjX2c92NP6ar7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e642ba5d-3af1-4dd6-bd39-8e43dbc787fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A2CAqaQxW65XVWZTz8WP5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 11207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4248,
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

_source line 18 · 2026-05-13T04:42:52.999Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q9HEJwRuXkhRpJW59NQCyi`</summary>

```json
{
  "query": "information bottleneck robot learning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e642ba5d-3af1-4dd6-bd39-8e43dbc787fe",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxPxaRUjX2c92NP6ar7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "576aeef6-9ed9-4f19-bc57-95d1e77c76c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A2CAqaQxW65XVWZTz8WP5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 11207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4248,
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

_source line 19 · 2026-05-13T04:42:54.010Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XrqVbVrXkB3fbfdQ3z2Ysi`</summary>

```json
{
  "query": "IB regularization vision language action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "576aeef6-9ed9-4f19-bc57-95d1e77c76c9",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxPxaRUjX2c92NP6ar7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b07a8596-ec7f-45ba-85f2-bd4fd20256d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A2CAqaQxW65XVWZTz8WP5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 11207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4248,
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

_source line 20 · 2026-05-13T04:42:54.480Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xov2Guxjok7aPFT1hYwQce`</summary>

```json
{
  "query": "VLA-Pruner temporal visual token pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b07a8596-ec7f-45ba-85f2-bd4fd20256d3",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxPxaRUjX2c92NP6ar7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad484d26-d2f2-4e4f-864c-38212233c743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A2CAqaQxW65XVWZTz8WP5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 11207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4248,
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

_source line 21 · 2026-05-13T04:42:54.966Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CHaDsuJrwYtCbfPV6zKNAQ`</summary>

```json
{
  "query": "LIBERO-Plus robustness benchmark VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad484d26-d2f2-4e4f-864c-38212233c743",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxPxaRUjX2c92NP6ar7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a097a790-c51c-43da-b373-1ae1d4ea62cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A2CAqaQxW65XVWZTz8WP5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 11207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4248,
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

_source line 22 · 2026-05-13T04:42:55.441Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P9YPyzg1Mon9KJ3xt6fn2q`</summary>

```json
{
  "query": "SimplerEnv visual variant aggregation VLA evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a097a790-c51c-43da-b373-1ae1d4ea62cd",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxPxaRUjX2c92NP6ar7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "529c38eb-836d-49e6-b707-6402de35b0b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A2CAqaQxW65XVWZTz8WP5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 11207,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4248
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 954,
          "output_tokens": 253,
          "cache_read_input_tokens": 11207,
          "cache_creation_input_tokens": 4248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4248,
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

_source line 23 · 2026-05-13T04:42:59.866Z_

<details><summary>↩ Tool result · `toolu_01Q9HEJwRuXkhRpJW59NQCyi`</summary>

```text
Web search results for query: "information bottleneck robot learning VLA"

Links: [{"title":"CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning","url":"https://arxiv.org/html/2602.12532"},{"title":"Precise Manipulation with Efficient Online RL","url":"https://www.pi.website/research/rlt"},{"title":"Variational Information Bottleneck Regularized Deep Reinforcement Learning for Efficient Robotic Skill Adaptation","url":"https://www.mdpi.com/1424-8220/23/2/762"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"VLAs as Model Organisms for AI Safety","url":"https://www.lesswrong.com/posts/4p2HBMxCkh7pZ3xCa/vlas-as-model-organisms-for-ai-safety"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Vision-Language-Action (VLA) Models for Robotics","url":"https://blog.roboflow.com/vision-language-action-models/"},{"title":"A Pragmatic VLA Foundation Model","url":"https://arxiv.org/html/2601.18692"},{"title":"Variational Information Bottleneck Regularized Deep Reinforcement Learning for Efficient Robotic Skill Adaptation - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9864208/"}]

Based on the web search results, I found several relevant applications of information bottleneck principles in robot learning and VLA (Vision-Language-Action) models:

## Information Bottleneck in VLA and Robot Learning

**CRAFT Framework for Contact-Rich Manipulation:**
The CRAFT framework adapts VLA models to contact-rich manipulation using a variational information bottleneck to balance the influence of vision, language, and force modalities. More specifically, CRAFT inserts a variational information bottleneck after vision and language embeddings to regulate their information entropy, enforcing a curriculum that encourages the model to prioritize the force modality during early training stages, then gradually restores the contribution of visual and language signals.

**RL Tokens (RLT) for Efficient Online RL:**
The RL token must retain enough information for a decoder to reconstruct the original VLA embeddings, forcing it to act as an information bottleneck. RLT adapts the VLA by adding an encoder-decoder transformer trained to predict the model's internal embeddings through a bottleneck, leading to a compressed representation called the RL token.

**Variational Information Bottleneck for Meta-RL:**
A meta-reinforcement learning algorithm based on variational information bottleneck has been developed for efficient robotic skill transfer, where the information bottleneck is applied to infer basic tasks during meta-training, then maximum entropy regularized reinforcement learning learns skills consistent with those tasks. This approach can improve sample efficiency by 200–5000 times on new tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "576aeef6-9ed9-4f19-bc57-95d1e77c76c9",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "94b30754-7e4f-49e2-8bc9-074ba42ab7e6",
  "sourceToolAssistantUUID": "576aeef6-9ed9-4f19-bc57-95d1e77c76c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T04:43:00.231Z_

<details><summary>↩ Tool result · `toolu_01XrqVbVrXkB3fbfdQ3z2Ysi`</summary>

```text
Web search results for query: "IB regularization vision language action model"

Links: [{"title":"Contrastive Representation Regularization for Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01711v1"},{"title":"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.23202v1"},{"title":"Contrastive Representation Regularization for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=hm2EcwFm2Q"},{"title":"A Survey on Vision-Language-Action Models for Embodied ...","url":"https://arxiv.org/html/2405.14093v5"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"[2405.14093] A Survey on Vision-Language-Action Models for Embodied AI","url":"https://arxiv.org/abs/2405.14093"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"[2510.24795] A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.24795"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"}]

Based on the web search results, here's what I found about IB regularization in vision-language-action models:

## Key Findings

The search results reveal recent research on regularization techniques for Vision-Language-Action (VLA) models. The most relevant work appears to be **Contrastive Representation Regularization for Vision-Language-Action Models**.

Vision-Language-Action (VLA) models have shown capabilities in robot manipulation by leveraging rich representations from pre-trained Vision-Language Models (VLMs), but their representations arguably remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive states.

### Robot State-aware Contrastive Loss (RS-CL)

A recent approach introduces Robot State-aware Contrastive Loss (RS-CL), a representation regularization for VLA models designed to bridge the gap between VLM representations and robotic signals by aligning the representations more closely with the robot's proprioceptive states, using relative distances between the states as soft supervision. This approach effectively enhances control-relevant representation learning while being lightweight and fully compatible with standard VLA training pipelines.

### Gaze Regularization

Additionally, the search reveals research that hypothesizes aligning a VLA's internal attention with human gaze distribution can improve both learning efficiency and downstream task performance, using human gaze priors to regularize spatial attention.

These regularization techniques represent efforts to improve the quality of learned representations in VLA models for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b07a8596-ec7f-45ba-85f2-bd4fd20256d3",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "59cda2e6-a54a-4024-92fb-eba86231eec6",
  "sourceToolAssistantUUID": "b07a8596-ec7f-45ba-85f2-bd4fd20256d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-13T04:43:01.432Z_

<details><summary>↩ Tool result · `toolu_01Xov2Guxjok7aPFT1hYwQce`</summary>

```text
Web search results for query: "VLA-Pruner temporal visual token pruning"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/html/2603.06480"},{"title":"[2603.06480] History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/abs/2603.06480"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"}]

Based on the search results, here's what I found about VLA-Pruner:

## VLA-Pruner Overview

VLA-Pruner addresses the heavy computational cost of processing continuous visual streams in Vision-Language-Action (VLA) models, which limits their real-time deployment.

## Key Features

VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance.

It selects tokens using last-layer prefill attention and temporal smoothing of action-to-vision attention averaged over the latter half layers.

## Problem It Solves

Traditional VLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution. Consequently, these methods bias token retention toward semantic cues, discard critical information for action generation, and significantly degrade VLA performance.

## Design Approach

VLA-Pruner proposes a novel dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens for both semantic understanding and action execution under given compute budget.

## Performance

VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks. The paper was updated as recently as February 10, 2026, according to the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad484d26-d2f2-4e4f-864c-38212233c743",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "be1b80f3-1587-4169-a004-5a1ab48be41e",
  "sourceToolAssistantUUID": "ad484d26-d2f2-4e4f-864c-38212233c743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T04:43:01.897Z_

<details><summary>↩ Tool result · `toolu_01CHaDsuJrwYtCbfPV6zKNAQ`</summary>

```text
Web search results for query: "LIBERO-Plus robustness benchmark VLA"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

I found comprehensive information about LIBERO-Plus. Here's what the search revealed:

## Overview

LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions of Vision-Language-Action (VLA) models.

## Benchmark Scope

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise. The benchmark contains 10,030 tasks spanning seven perturbation dimensions, with evaluation across seven robustness dimensions and 21 sub-dimensions.

## Key Findings

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Additionally, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

## Benchmark Structure

The benchmark construction follows a systematic two-stage process: expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing; and evaluating resulting tasks using four representative models and stratifying them into five difficulty levels (Level-1 to Level-5).

The benchmark is available on GitHub at the official repository and represents a significant effort to expose the brittleness of current VLA models beneath their apparently high benchmark scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a097a790-c51c-43da-b373-1ae1d4ea62cd",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "9962ac0f-01fc-416d-8e81-bc3c35c72d63",
  "sourceToolAssistantUUID": "a097a790-c51c-43da-b373-1ae1d4ea62cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-13T04:43:02.352Z_

<details><summary>↩ Tool result · `toolu_01P9YPyzg1Mon9KJ3xt6fn2q`</summary>

```text
Web search results for query: "SimplerEnv visual variant aggregation VLA evaluation"

Links: [{"title":"GitHub - DelinQu/SimplerEnv-OpenVLA: Evaluating and reproducing real-world robot manipulation policies (e.g., RT-1, RT-1-X, Octo, and OpenVLA) in simulation under common setups (e.g., Google Robot, WidowX+Bridge) · GitHub","url":"https://github.com/DelinQu/SimplerEnv-OpenVLA"},{"title":"Enhancing Generalization in Vision-Language-Action Models","url":"https://gen-vla.github.io/"},{"title":"SimplerEnv-OpenVLA/README.md at main · DelinQu/SimplerEnv-OpenVLA","url":"https://github.com/DelinQu/SimplerEnv-OpenVLA/blob/main/README.md"},{"title":"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies","url":"https://tracevla.github.io/"},{"title":"SimplerEnv-OpenVLA/README.md at main · TeleHuman/SimplerEnv-OpenVLA","url":"https://github.com/TeleHuman/SimplerEnv-OpenVLA/blob/main/README.md"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting","url":"https://arxiv.org/html/2507.05116"},{"title":"tracevla: visual trace prompting enhances spatial-temporal ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf"},{"title":"StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing","url":"https://arxiv.org/html/2604.05014v1"},{"title":"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies","url":"https://arxiv.org/html/2412.10345v1"}]

Based on the search results, I can provide you with information about SimplerEnv's Visual Variant Aggregation (VLA) evaluation:

## SimplerEnv Visual Variant Aggregation Evaluation

Variant Aggregation evaluation involves creating different sim environment variants (e.g., different backgrounds, lightings, distractors, table textures, etc) and averaging their results.

The Visual Variant Aggregation setup introduces backgrounds, lightings, table textures, distractor objects, and camera poses out of the distribution of the robot data (OOD), serving as a generalization test.

### Purpose and Context

SimplerEnv provides two complementary evaluation settings for Vision-Language-Action (VLA) models:

1. The Visual Matching setup contains visuals closely matching the VLA training data, serving as an in-distribution evaluation.

2. The variant aggregation setting covers a wide range of environmental variations including backgrounds from different rooms, lighter and darker lighting conditions, varying numbers of distractors, solid color and complex table textures, and different robot camera poses, allowing assessment of robustness and adaptability in diverse manipulation scenarios.

### Usage in Research

This evaluation methodology has been widely adopted in recent VLA research to assess model generalization and robustness across different environmental conditions, particularly for robot manipulation tasks evaluated on platforms like the Google Robot and WidowX.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "529c38eb-836d-49e6-b707-6402de35b0b1",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "ec194359-e787-47cc-bbbe-705f83fdccf7",
  "sourceToolAssistantUUID": "529c38eb-836d-49e6-b707-6402de35b0b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-13T04:43:05.508Z_

Excellent progress. Now let me search for the remaining specific papers and recent concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec194359-e787-47cc-bbbe-705f83fdccf7",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxQsydW6fpphR7hyPkD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3645d6a0-bb85-4f64-a74b-4ce395d25006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4VRKuccwRuzwZJcZejcAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5682,
      "cache_read_input_tokens": 15455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5682,
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

_source line 29 · 2026-05-13T04:43:06.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KY6QhYbcRTh3CCXikrkPqj`</summary>

```json
{
  "query": "CRL-VLA arXiv 2602.03445 continual learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3645d6a0-bb85-4f64-a74b-4ce395d25006",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxQsydW6fpphR7hyPkD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47caa460-833b-4b8f-bd2e-bdc897e4d009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4VRKuccwRuzwZJcZejcAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5682,
      "cache_read_input_tokens": 15455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5682,
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

_source line 30 · 2026-05-13T04:43:06.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KRT1QQ58feyJxWHcsPpGFC`</summary>

```json
{
  "query": "VLM2VLA \"Actions as Language\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47caa460-833b-4b8f-bd2e-bdc897e4d009",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxQsydW6fpphR7hyPkD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc60c0d4-f25a-4e73-9d9f-d0acd43d66ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4VRKuccwRuzwZJcZejcAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5682,
      "cache_read_input_tokens": 15455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5682,
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

_source line 31 · 2026-05-13T04:43:07.403Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BaRMeti2M1wGTEeyu5CmZV`</summary>

```json
{
  "query": "Gen-VLA arXiv 2509.11417 preserving pretrained representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc60c0d4-f25a-4e73-9d9f-d0acd43d66ea",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxQsydW6fpphR7hyPkD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59cc2e37-6162-411d-9c35-6ff05372cdca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4VRKuccwRuzwZJcZejcAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5682,
      "cache_read_input_tokens": 15455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5682,
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

_source line 32 · 2026-05-13T04:43:07.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DgKgfsQ6uh7UH4zfjigYns`</summary>

```json
{
  "query": "VLA regularization arXiv 2026 token masking finetuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59cc2e37-6162-411d-9c35-6ff05372cdca",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxQsydW6fpphR7hyPkD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9b3f64f-2856-450c-9fe3-3dae23edb69a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4VRKuccwRuzwZJcZejcAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5682,
      "cache_read_input_tokens": 15455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5682,
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

_source line 33 · 2026-05-13T04:43:08.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014U9omn99jqn35RkeGaSdcY`</summary>

```json
{
  "query": "vision language action model finetuning regularization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9b3f64f-2856-450c-9fe3-3dae23edb69a",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxQsydW6fpphR7hyPkD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4927596b-2a18-4501-a01d-5fd71d2cb14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4VRKuccwRuzwZJcZejcAZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5682,
      "cache_read_input_tokens": 15455,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5682
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 15455,
          "cache_creation_input_tokens": 5682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5682,
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

_source line 34 · 2026-05-13T04:43:13.065Z_

<details><summary>↩ Tool result · `toolu_01KRT1QQ58feyJxWHcsPpGFC`</summary>

```text
Web search results for query: "VLM2VLA "Actions as Language" ICLR 2026"

Links: [{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://vlm2vla.github.io/"},{"title":"From Vision-Language Models to Robot Control — Without Forgetting – Princeton Laboratory for Artificial Intelligence Research Blog","url":"https://blog.ai.princeton.edu/2026/04/23/from-vision-language-models-to-robot-control-without-forgetting/"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | OpenReview","url":"https://openreview.net/forum?id=sFO9d6XSlf"},{"title":"[2509.22195] Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/abs/2509.22195"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.22195v1"}]

Based on the search results, I found comprehensive information about VLM2VLA "Actions as Language":

## Overview

VLM2VLA is a VLA model training paradigm that represents low-level robot actions in natural language to better align the robot fine-tuning data with the base VLM's representation space.

## Key Innovation

The research argues that catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data, and introduces VLM2VLA which resolves this mismatch at the data level by representing low-level actions with natural language.

## Technical Approach

The alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting.

## Performance Results

Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following. Additionally, across twelve multimodal understanding benchmarks, VLM2VLA retains over 85% of the base model's performance.

## ICLR 2026 Acceptance

The paper "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting" is included in the ICLR 2026 program.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc60c0d4-f25a-4e73-9d9f-d0acd43d66ea",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "d891ba5e-3ce2-4222-bdbf-4ca2999e92c1",
  "sourceToolAssistantUUID": "cc60c0d4-f25a-4e73-9d9f-d0acd43d66ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-13T04:43:13.974Z_

<details><summary>↩ Tool result · `toolu_01KY6QhYbcRTh3CCXikrkPqj`</summary>

```text
Web search results for query: "CRL-VLA arXiv 2602.03445 continual learning"

Links: [{"title":"[2602.03445] CRL-VLA: Continual Vision-Language-Action Learning","url":"https://arxiv.org/abs/2602.03445"},{"title":"CRL-VLA: Continual Vision–Language–Action Learning","url":"https://arxiv.org/pdf/2602.03445"},{"title":"[PDF] CRL-VLA: Continual Vision-Language-Action Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CRL-VLA:-Continual-Vision-Language-Action-Learning-Zeng-Zhang/a4dc1fff332dd25b873a508273728e16085238d5"},{"title":"(PDF) CRL-VLA: Continual Vision-Language-Action Learning","url":"https://www.researchgate.net/publication/400415793_CRL-VLA_Continual_Vision-Language-Action_Learning"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/pastweek?skip=798&show=2000"},{"title":"CRL-VLA: Continual Vision-Language-Action Learning","url":"https://ribbitribbit.co/paper/arxiv.2602.03445-CRL-VLA-Continual-Vision-Language-Action-Learning"},{"title":"[2603.11653] Simple Recipe Works: Vision-Language-Action Models are Natural Continual Learners with Reinforcement Learning","url":"https://arxiv.org/abs/2603.11653"},{"title":"Simple Recipe Works: Vision-Language-Action Models are Natural Continual Learners with Reinforcement Learning","url":"https://arxiv.org/html/2603.11653"},{"title":"[2506.21872] A Survey of Continual Reinforcement Learning","url":"https://arxiv.org/abs/2506.21872"},{"title":"[2601.09512] CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion","url":"https://arxiv.org/abs/2601.09512"}]

Based on the search results, here's what I found about CRL-VLA (arXiv:2602.03445):

## Overview

CRL-VLA is a framework for continual post-training of VLA models with rigorous theoretical bounds. Lifelong learning is critical for embodied agents in open-world environments, where reinforcement learning fine-tuning has emerged as an important paradigm to enable Vision-Language-Action (VLA) models to master dexterous manipulation through environmental interaction. Continual Reinforcement Learning (CRL) is a promising pathway for deploying VLA models in lifelong robotic scenarios, yet balancing stability (retaining old skills) and plasticity (learning new ones) remains a formidable challenge for existing methods.

## Key Contributions

The framework derives a unified performance bound linking the stability-plasticity trade-off to goal-conditioned advantage magnitude, scaled by policy divergence. CRL-VLA resolves this dilemma via asymmetric regulation: constraining advantage magnitudes on prior tasks while enabling controlled growth on new tasks.

## Technical Approach

CRL-VLA is a continual learning framework that disentangles stable value semantics from adaptive policy learning via a novel Goal-Conditioned Value Formulation (GCVF). The method employs a dual-critic architecture in which a frozen critic anchors long-horizon, language-conditioned value semantics, while a trainable critic estimator drives adaptation.

## Authors

The paper was submitted on February 3, 2026, with authors Qixin Zeng, Shuo Zhang, Hongyin Zhang, Renjie Wang, Han Zhao, Libang Zhao, Runze Li, Donglin Wang, and Chao Huang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47caa460-833b-4b8f-bd2e-bdc897e4d009",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "421b8c86-6928-45fc-a7d3-74a35ac5a20f",
  "sourceToolAssistantUUID": "47caa460-833b-4b8f-bd2e-bdc897e4d009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T04:43:15.028Z_

<details><summary>↩ Tool result · `toolu_01BaRMeti2M1wGTEeyu5CmZV`</summary>

```text
Web search results for query: "Gen-VLA arXiv 2509.11417 preserving pretrained representations"

Links: [{"title":"[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/abs/2509.11417"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417"},{"title":"Enhancing Generalization in Vision–Language–Action Models by","url":"https://arxiv.org/pdf/2509.11417"},{"title":"Enhancing Generalization in Vision-Language-Action Models","url":"https://gen-vla.github.io/"},{"title":"[PDF] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Enhancing-Generalization-in-Vision-Language-Action-Grover-Gopalkrishnan/272525654b60ab7f4366e58244feadcfd2675aaf"},{"title":"Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/html/2510.25616v1"},{"title":": A Vision-Language-Action Model Bridging Understanding and Generation to Actions","url":"https://arxiv.org/html/2509.06951"},{"title":"[2509.10468] Learning Decomposed Contextual Token Representations from Pretrained and Collaborative Signals for Generative Recommendation","url":"https://arxiv.org/abs/2509.10468"},{"title":"Knowledge Insulating Vision-Language-Action Models","url":"https://www.pi.website/download/pi05_KI.pdf"},{"title":"JEPA-VLA: Video Predictive Embedding is Needed for VLA Models","url":"https://arxiv.org/html/2602.11832v1"}]

Based on the search results, here's information about the Gen-VLA paper (arXiv 2509.11417):

## Overview

This paper addresses Vision-Language-Action (VLA) models finetuned from vision-language models (VLMs), which hold promise for building generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization.

## Key Framework Components

The method introduces a dual-encoder design to retain features, a string-based action tokenizer to align actions with language, and a co-training strategy to balance robot and vision-language data.

The three main design choices are:

1. **Partially-Frozen Visual Encoders**: The approach uses two encoders—one frozen to preserve robust, pretrained VLM features and one trainable to adapt to the specific robot task.

2. **String-Based Action Tokenizer**: Robotic actions are expressed as digit-based strings to maximally reuse pretrained language representations and to unify prediction targets across non-robotic and robotic task domains for co-training.

3. **Co-Training Strategy**: Jointly training on robotic and vision-language datasets that emphasize spatial affordance and reasoning helps preserve pretrained representations for generalization.

## Results

The evaluations show significant improvements in robustness, generalization, and overall task success. The approach yields stronger generalization to out-of-distribution visuals, such as backgrounds, table textures, and distractor objects, as well as to varied language commands, leading to higher task success rates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59cc2e37-6162-411d-9c35-6ff05372cdca",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "1f68c0a9-bee9-4947-bb09-eed793a1ed73",
  "sourceToolAssistantUUID": "59cc2e37-6162-411d-9c35-6ff05372cdca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-13T04:43:15.244Z_

<details><summary>↩ Tool result · `toolu_01DgKgfsQ6uh7UH4zfjigYns`</summary>

```text
Web search results for query: "VLA regularization arXiv 2026 token masking finetuning"

Links: [{"title":"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.23202v1"},{"title":"VLA-0: Building State-of-the-Art VLAs with Zero Modification","url":"https://arxiv.org/pdf/2510.13054"},{"title":"Contrastive Representation Regularization for Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01711v1"},{"title":"VGAS: Value-Guided Action-Chunk Selection for Few-Shot Vision-Language-Action Adaptation","url":"https://arxiv.org/html/2602.07399"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"When LLaVA Meets Objects: Token Composition for Vision-Language-Models","url":"https://arxiv.org/html/2602.04864v1"},{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning","url":"https://arxiv.org/html/2602.12532"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"}]

Based on the search results, I found several recent papers on arXiv from 2026 related to VLA (Vision-Language-Action) models, regularization, token masking, and fine-tuning:

## Key Findings:

**Token Masking and Fine-tuning:**
One approach involves randomly masking out characters in target action strings during training to force the VLM to reason about actions based on visual observations and instructions rather than auto-completing sequences.

**VLA Regularization Methods:**

1. **Gaze-Regularized VLA**: A gaze-regularized training framework aligns VLA models' internal attention with human visual patterns by transforming gaze heatmaps into patch-level distributions and regularizing the transformer's attention through KL divergence.

2. **Robot State-Aware Contrastive Loss**: A self-supervised regularization objective for VLA models uses Robot State-aware Contrastive Loss (RS-CL) that explicitly shapes VLM representations toward capturing robotic signals and uses proprioceptive state distances as soft supervision.

3. **Force-Aware Curriculum Fine-tuning**: CRAFT introduces a variational information bottleneck (VIB) after the vision-language encoder with KL regularization that initially suppresses high-entropy visual and language signals.

**Parameter-Efficient Fine-tuning:**
VLA-GSE is proposed as a parameter-efficient VLA fine-tuning framework designed to strengthen adaptation without sacrificing knowledge retention.

These papers demonstrate various approaches to improving VLA models through regularization techniques and efficient fine-tuning strategies involving token-level operations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9b3f64f-2856-450c-9fe3-3dae23edb69a",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "568039fb-8ba4-4648-825f-bdc713285f55",
  "sourceToolAssistantUUID": "c9b3f64f-2856-450c-9fe3-3dae23edb69a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T04:43:20.778Z_

<details><summary>↩ Tool result · `toolu_014U9omn99jqn35RkeGaSdcY`</summary>

```text
Web search results for query: "vision language action model finetuning regularization 2026"

Links: [{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.23202v1"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/html/2603.03818"},{"title":"Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior","url":"https://arxiv.org/html/2604.01570v1"},{"title":"RL4VLM","url":"https://rl4vlm.github.io/"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly","url":"https://arxiv.org/pdf/2603.03818"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/17/"}]

I found several recent papers and resources on vision-language-action models with a focus on finetuning and regularization techniques from 2026. Here are the key findings:

## Recent VLA Finetuning Research (2026)

**Gaze-Regularized VLA Models:** A gaze-regularized training framework aligns VLA models' internal attention with human visual patterns without architectural modifications or inference-time overhead, transforming temporally aggregated gaze heatmaps into patch-level distributions and regularizing the transformer's attention through KL divergence. This approach yields 4-12% improvements across manipulation benchmarks.

**Feasible Action Neighborhood (FAN) Regularization:** A FAN-guided regularizer shapes the model's output distribution to align with the geometry of feasible action neighborhoods, introducing a Gaussian prior that promotes locally smooth and unimodal predictions around the preferred direction and magnitude. This method achieves significant improvements in sample efficiency and success rate in both in-distribution and out-of-distribution scenarios.

**Continual Learning in Pretrained VLAs:** Large-scale pretraining enables simple experience replay to achieve near-zero forgetting with surprisingly small buffers, fundamentally changing how regularization and continual finetuning work compared to smaller models.

**General VLA Finetuning:** Recent vision-language-action models build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization.

These papers demonstrate that regularization techniques in VLA finetuning are increasingly tailored to the unique properties of robotic action spaces and the benefits of large-scale pretraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4927596b-2a18-4501-a01d-5fd71d2cb14a",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "13a5be48-fe90-4ed5-b5a4-2c1392414ffa",
  "sourceToolAssistantUUID": "4927596b-2a18-4501-a01d-5fd71d2cb14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-13T04:43:23.661Z_

Now let me fetch detailed information on the most important/closest competitor papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13a5be48-fe90-4ed5-b5a4-2c1392414ffa",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxSDtUvmuFp18kEpYYU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3711b75e-4dc9-4755-82a4-9338883d1fbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPDuy4K1V1DPEuDmyCTSfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 21137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4650,
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

_source line 40 · 2026-05-13T04:43:25.610Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QVi1ea2i4595JvHmHE43sU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.08333",
  "prompt": "What is the full title, authors, and method of this paper? How does it improve robustness during VLA finetuning? Does it use any form of token masking or dropout? What benchmarks does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3711b75e-4dc9-4755-82a4-9338883d1fbb",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxSDtUvmuFp18kEpYYU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfb4aaba-e6dd-417b-9475-4c98c4047fab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPDuy4K1V1DPEuDmyCTSfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 21137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4650,
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

_source line 41 · 2026-05-13T04:43:27.111Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CHW7Kmr2mCCreUxv4ZP2hd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.16449",
  "prompt": "What is the full title, authors, and method of VLA-Pruner? Is this about efficiency (inference speed) or about generalization/regularization? Does it mask tokens during training or only during inference? What benchmarks does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfb4aaba-e6dd-417b-9475-4c98c4047fab",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxSDtUvmuFp18kEpYYU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84f0fc3b-c637-4b2c-8bda-65cac0d51572",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPDuy4K1V1DPEuDmyCTSfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 21137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4650,
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

_source line 42 · 2026-05-13T04:43:28.946Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EsuWWsjWCmU8g9HehHfXGZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.01711v1",
  "prompt": "What is the full title and method of this paper on contrastive representation regularization for VLA models? Does it use token masking? What is the regularization approach? How does it improve generalization? What benchmarks does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84f0fc3b-c637-4b2c-8bda-65cac0d51572",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxSDtUvmuFp18kEpYYU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd7b0c1e-36d2-4f7c-aa04-63fc533f51fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPDuy4K1V1DPEuDmyCTSfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 21137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4650,
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

_source line 43 · 2026-05-13T04:43:29.814Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Tck2NcSyXuVgfXdx15Bcwr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.11417",
  "prompt": "What is the full title, authors, and method of Gen-VLA? Does it use any form of token masking? What is its approach to preserving representations? What benchmarks does it evaluate on (SimplerEnv, LIBERO)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd7b0c1e-36d2-4f7c-aa04-63fc533f51fe",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxSDtUvmuFp18kEpYYU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a62823a1-2718-416d-b22d-fc184d4ae7b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPDuy4K1V1DPEuDmyCTSfg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 21137,
      "output_tokens": 497,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4650
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 497,
          "cache_read_input_tokens": 21137,
          "cache_creation_input_tokens": 4650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4650,
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

_source line 44 · 2026-05-13T04:43:29.933Z_

<details><summary>↩ Tool result · `toolu_01QVi1ea2i4595JvHmHE43sU`</summary>

```text
# Paper Summary

**Title:** "Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging"

**Authors:** Yajat Yadav, Zhiyuan Zhou, Andrew Wagenmaker, Karl Pertsch, and Sergey Levine

**Core Method:** The paper proposes a straightforward approach—"interpolating the weights of a finetuned model with that of the pretrained model." This parameter merging technique addresses the overfitting problem that occurs when adapting generalist policies to new tasks with limited data.

**Robustness Improvement:** The method preserves generalization by blending the finetuned weights with the pretrained weights. This allows the resulting model to "inherit the generalist abilities of the base model and learn to solve the new task robustly," particularly excelling on out-of-distribution task variations.

**Token Masking or Dropout:** The webpage content provided does not contain information about whether token masking or dropout techniques are employed.

**Benchmarks:** The abstract mentions testing across "extensive simulated and real-world experiments" but does not specify particular benchmark names in the available content.

**Additional Finding:** The research demonstrates that performance scales with pretraining data volume and supports continual skill acquisition in lifelong learning scenarios without degrading previously learned competencies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfb4aaba-e6dd-417b-9475-4c98c4047fab",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "9f4273a0-c50a-4041-8741-3918550df054",
  "sourceToolAssistantUUID": "bfb4aaba-e6dd-417b-9475-4c98c4047fab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-13T04:43:31.411Z_

<details><summary>↩ Tool result · `toolu_01CHW7Kmr2mCCreUxv4ZP2hd`</summary>

```text
# VLA-Pruner Summary

**Full Title:** "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference"

**Authors:** Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, and Bo Zhao

**Method:** The approach uses a dual-level importance criterion combining two attention metrics: vision-language prefill attention for semantic relevance and action decode attention (estimated through temporal smoothing) for action-level importance.

**Focus:** This work targets **inference efficiency**. The paper states the goal is addressing "heavy computational cost of processing continuous visual streams" to enable "real-time deployment."

**Training vs. Inference:** The abstract describes it as "a versatile plug-and-play VLA-specific token prune method," suggesting token selection occurs during inference rather than training modifications.

**Benchmarks:** The page provides no specific benchmark details. It only notes that "experiments show that VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks," without naming particular datasets or evaluation metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84f0fc3b-c637-4b2c-8bda-65cac0d51572",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "f7898a88-d036-4e75-ab0e-10224f5a75ba",
  "sourceToolAssistantUUID": "84f0fc3b-c637-4b2c-8bda-65cac0d51572",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T04:43:34.111Z_

<details><summary>↩ Tool result · `toolu_01Tck2NcSyXuVgfXdx15Bcwr`</summary>

```text
# Gen-VLA Summary

**Full Title:** "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations"

**Authors:** Shresth Grover, Akshay Gopalkrishnan, Bo Ai, Henrik I. Christensen, Hao Su, and Xuanlin Li

**Core Method:** The framework employs three key components: "(i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances."

**Token Masking:** The provided content does not mention token masking techniques.

**Representation Preservation Approach:** The method maintains pretrained features through a dual-encoder architecture where one vision encoder remains frozen while a separate trainable encoder handles task-specific adaptation. Additionally, the string-based action tokenizer aligns actions with the model's original pretraining domain.

**Benchmarks:** The abstract does not specify evaluation on SimplerEnv or LIBERO. It only mentions "evaluations in simulation and on real robots."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a62823a1-2718-416d-b22d-fc184d4ae7b4",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "92ead76e-e5ce-4876-9685-5d7fd3f78981",
  "sourceToolAssistantUUID": "a62823a1-2718-416d-b22d-fc184d4ae7b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-13T04:43:34.970Z_

<details><summary>↩ Tool result · `toolu_01EsuWWsjWCmU8g9HehHfXGZ`</summary>

```text
# Contrastive Representation Regularization for Vision-Language-Action Models

## Title and Method
The paper introduces **Robot State-aware Contrastive Loss (RS-CL)**, a representation regularization technique designed to align Vision-Language Model (VLM) embeddings with robotic proprioceptive signals in VLA models.

## Masking Approach
The method does **not** use token masking. Instead, it employs "view cutoff," which is described as "a simple representation-level augmentation" that randomly masks feature slices corresponding to observation views rather than individual tokens.

## Regularization Strategy
RS-CL uses weighted contrastive learning where weights are computed from distances between proprioceptive states. The approach assigns "pairwise weights based on the distances between robot proprioceptive states, guiding the representations to better reflect robot control-relevant structure." This complements the standard action prediction loss during training.

## Generalization Improvements
The method demonstrates generalization across visual shifts, physical variations, and language grounding tasks. The authors note that RS-CL "maintains strong generalization performance of VLAs" while improving robustness to partial occlusion through view-invariant representations.

## Benchmarks Evaluated
- **RoboCasa-Kitchen**: Improves from 30.8% to 41.5% on pick-and-place tasks
- **LIBERO**: Multi-task benchmark with four suites (spatial, object, goal, long)
- **Real-world experiments**: 7-DoF Franka manipulator with pick-and-place and close-lid tasks
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd7b0c1e-36d2-4f7c-aa04-63fc533f51fe",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "270f631d-c235-4a12-bad2-90f58b1e6f7a",
  "sourceToolAssistantUUID": "cd7b0c1e-36d2-4f7c-aa04-63fc533f51fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-13T04:43:37.942Z_

Let me now dig deeper into the closest potential competitors and the most relevant recent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "270f631d-c235-4a12-bad2-90f58b1e6f7a",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxTGdTRvFeUde5fS1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c06d5ba-446a-492d-a636-1fb859658c53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVm3yRKc7b1fizQV1QJTaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 318,
      "cache_creation_input_tokens": 1600,
      "cache_read_input_tokens": 25787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1600,
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

_source line 49 · 2026-05-13T04:43:39.476Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BdverCRDzLAEjzLrtMebbc`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.23202v1",
  "prompt": "What is the full title, authors, and method of this gaze-regularized VLA paper? Does it use any form of token masking or information bottleneck? How does the KL divergence regularization work? What benchmarks does it use? When was it published?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c06d5ba-446a-492d-a636-1fb859658c53",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxTGdTRvFeUde5fS1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca66e9fa-d534-40b9-84a5-225241aaf677",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVm3yRKc7b1fizQV1QJTaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 318,
      "cache_creation_input_tokens": 1600,
      "cache_read_input_tokens": 25787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1600,
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

_source line 50 · 2026-05-13T04:43:40.935Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pc65pEVUEAUW714jeui2Jn`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.01570v1",
  "prompt": "What is the full title, authors, and method of this paper on Feasible Action Neighborhood prior? Does it use any form of token masking or information bottleneck? How does its regularization approach work? When was it submitted? What benchmarks does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca66e9fa-d534-40b9-84a5-225241aaf677",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxTGdTRvFeUde5fS1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8952f89-3fba-40bc-aac3-3d77255e5784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVm3yRKc7b1fizQV1QJTaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 318,
      "cache_creation_input_tokens": 1600,
      "cache_read_input_tokens": 25787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1600,
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

_source line 51 · 2026-05-13T04:43:43.336Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013X8ghbmpCBEGooRVT3y4nN`</summary>

```json
{
  "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html",
  "prompt": "List all VLA papers mentioned from ICLR 2026. Are there any that use token masking as regularization, counterfactual reasoning, or information bottleneck methods for VLA finetuning? List any papers about VLA robustness, generalization, or regularization techniques."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8952f89-3fba-40bc-aac3-3d77255e5784",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxTGdTRvFeUde5fS1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4431ba6-61a7-49d1-a105-7c191b6573ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVm3yRKc7b1fizQV1QJTaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 318,
      "cache_creation_input_tokens": 1600,
      "cache_read_input_tokens": 25787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1600,
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

_source line 52 · 2026-05-13T04:43:43.801Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XGijsFULbk3p1aMGLYdCyr`</summary>

```json
{
  "query": "\"counterfactual\" VLA robot learning masking 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4431ba6-61a7-49d1-a105-7c191b6573ea",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxTGdTRvFeUde5fS1Qg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "159b19ac-08cb-4f2b-a21f-2b2e6d7716cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVm3yRKc7b1fizQV1QJTaT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 318,
      "cache_creation_input_tokens": 1600,
      "cache_read_input_tokens": 25787,
      "output_tokens": 476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1600
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 318,
          "output_tokens": 476,
          "cache_read_input_tokens": 25787,
          "cache_creation_input_tokens": 1600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1600,
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

_source line 53 · 2026-05-13T04:43:46.373Z_

<details><summary>↩ Tool result · `toolu_01BdverCRDzLAEjzLrtMebbc`</summary>

```text
# Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation

**Full Title:** "Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation"

**Authors:** Anupam Pani and Yanchao Yang (Institute of Data Science, University of Hong Kong)

**Publication Date:** March 24, 2026 (arXiv:2603.23202v1)

## Method Overview

The approach uses human gaze patterns as a training-time supervisory signal to align transformer attention mechanisms with task-relevant regions, without requiring architectural modifications or inference-time gaze input.

**Key Components:**
- Synthetic gaze generation via pretrained Global-Local Correlation (GLC) network
- Conversion of gaze heatmaps into patch-level probability distributions matching visual token granularity
- Temporal aggregation of gaze across frames to capture anticipatory fixations

## KL Divergence Regularization

The method employs KL divergence to align model attention with gaze distributions:

> "ℒgaze=λ∗DKL​(Gti∥Sti)"

This soft constraint encourages the language query's attention over visual patches to mirror human fixation patterns while preserving task-specific learning flexibility.

## Information Bottleneck

Yes—the architecture uses causal attention masking where visual tokens attend only to vision-language features, while action tokens attend to all preceding tokens. This maintains a semantic bottleneck while allowing gaze-guided attention modulation.

## Benchmarks

- LIBERO suite (Spatial, Object, Goal, LIBERO-10)
- ALOHA-Sim
- Real-world robot tasks
- OpenVLA architecture validation

**Key Results:** 4-12% improvements across benchmarks with 6-8% gains appearing within 20,000 training steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca66e9fa-d534-40b9-84a5-225241aaf677",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "4534df52-0e83-4fde-826c-4b3f97991435",
  "sourceToolAssistantUUID": "ca66e9fa-d534-40b9-84a5-225241aaf677",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-13T04:43:48.518Z_

<details><summary>↩ Tool result · `toolu_01Pc65pEVUEAUW714jeui2Jn`</summary>

```text
# Paper Summary: Feasible Action Neighborhood Prior for VLA Finetuning

## Title and Authors
**Full Title:** "Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior"

**Authors:** Haochen Niu, Kanyu Zhang, Shuyu Yin, Qinghai Guo, Peilin Liu, and Fei Wen from Shanghai Jiao Tong University and Huawei Technologies

## Submission Date
The paper was submitted to arXiv on April 2, 2026 (arXiv:2604.01570v1).

## Core Method
The approach introduces a "FAN-guided regularizer" that shapes policy output distributions using KL divergence with a target Gaussian distribution. Rather than employing token masking or information bottlenecks, the method models the feasible action neighborhood as a locally unimodal region through a regularization term: `ℒ_FAN = 𝔼_s[D_KL(π(·|s) ∥ 𝒩(·|μ(s),Σ(s)))]`

The regularization adapts differently for supervised versus reinforced finetuning, using dynamic covariance in SFT and fixed covariance in RFT.

## Benchmarks
The evaluation covers:
- **ManiSkill:** PutOnPlateInScene25Main-v3 with 15 OOD perturbation types
- **LIBERO:** LIBERO-Spatial suite with spatial perturbation tests
- **Real-world:** 7-DoF JAKA manipulator experiments
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8952f89-3fba-40bc-aac3-3d77255e5784",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "7ac6546e-82be-4b62-916e-222f3546beb1",
  "sourceToolAssistantUUID": "b8952f89-3fba-40bc-aac3-3d77255e5784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-13T04:43:51.252Z_

<details><summary>↩ Tool result · `toolu_01XGijsFULbk3p1aMGLYdCyr`</summary>

```text
Web search results for query: ""counterfactual" VLA robot learning masking 2025 2026"

Links: [{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"Generative Models for Robot Learning","url":"https://iclr.cc/virtual/2025/workshop/23977"}]

Based on the search results, I found relevant information about counterfactual reasoning, VLA models, and masking techniques in robot learning from 2025-2026:

## Key Findings

**Counterfactual Learning in VLAs:**
In 2025, research was published on "Learning counterfactually decoupled attention for open-world model attribution", indicating active development of counterfactual approaches in AI systems relevant to robot learning.

**Masking Techniques in VLA Training:**
One significant study examined the role of language masking in VLA performance. Researchers trained VLA models by masking the language instruction while feeding only the visual observation, effectively testing vision-only performance, and found that vision-only models achieved a 44.6% success rate compared to a language-conditioned baseline of 47.8%. This small gap revealed that models can succeed without relying on language instructions when training and evaluation scenes and tasks are highly similar.

**VLA Research Landscape (2025-2026):**
Recent VLA models have converged toward three major architectural paradigms that balance efficiency, modularity, and robustness: early fusion models, dual-system architectures, and self-correcting frameworks, each addressing specific challenges in grounding, generalization, and action reliability.

The search results show active research at ICLR 2026 and other top venues focused on improving VLA generalization, robustness, and the role of multimodal components in robot learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "159b19ac-08cb-4f2b-a21f-2b2e6d7716cd",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "68fc5d83-1a89-49ea-a95e-8c00f801378c",
  "sourceToolAssistantUUID": "159b19ac-08cb-4f2b-a21f-2b2e6d7716cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-13T04:43:54.623Z_

<details><summary>↩ Tool result · `toolu_013X8ghbmpCBEGooRVT3y4nN`</summary>

```text
# VLA Papers from ICLR 2026

## Complete List of Mentioned Papers

**Discrete Diffusion VLAs:**
1. DISCRETE DIFFUSION VLA: BRINGING DISCRETE DIFFUSION TO ACTION DECODING IN VISION-LANGUAGE-ACTION POLICIES
2. dVLA: DIFFUSION VISION-LANGUAGE-ACTION MODEL WITH MULTIMODAL CHAIN-OF-THOUGHT
3. DIVA: DISCRETE DIFFUSION VISION-LANGUAGE-ACTION MODELS FOR PARALLELIZED ACTION GENERATION
4. UNIFIED DIFFUSION VLA: VISION-LANGUAGE-ACTION MODEL VIA JOINT DISCRETE DENOISING DIFFUSION PROCESS

**Reasoning VLAs & ECoT:**
5. ACTIONS AS LANGUAGE: FINE-TUNING VLMS INTO VLAS WITHOUT CATASTROPHIC FORGETTING
6. VISION-LANGUAGE-ACTION INSTRUCTION TUNING: FROM UNDERSTANDING TO MANIPULATION
7. EMBODIED-R1: REINFORCED EMBODIED REASONING FOR GENERAL ROBOTIC MANIPULATION
8. HYBRID TRAINING FOR VISION-LANGUAGE-ACTION MODELS

**Tokenizers:**
9. FASTER: TOWARD POWERFUL AND EFFICIENT AUTOREGRESSIVE VISION–LANGUAGE–ACTION MODELS
10. OMNISAT: COMPACT ACTION TOKEN, FASTER AUTOREGRESSION FOR VISION-LANGUAGE-ACTION MODELS

**Efficient VLAs:**
11. HYPERVLA: EFFICIENT INFERENCE IN VISION-LANGUAGE-ACTION MODELS VIA HYPERNETWORKS
12. AUTOQVLA: NOT ALL CHANNELS ARE EQUAL IN VISION-LANGUAGE-ACTION MODEL'S QUANTIZATION

**RL for VLAs:**
13. SELF-IMPROVING VISION-LANGUAGE-ACTION MODELS WITH DATA GENERATION VIA RESIDUAL RL
14. PROGRESSIVE STAGE-AWARE REINFORCEMENT FOR FINE-TUNING VISION-LANGUAGE-ACTION MODELS

**Video Prediction:**
15. DISENTANGLED ROBOT LEARNING VIA SEPARATE FORWARD AND INVERSE DYNAMICS PRETRAINING
16. UNIFIED VISION–LANGUAGE–ACTION MODEL
17. COSMOS POLICY: FINE-TUNING VIDEO MODELS FOR VISUOMOTOR CONTROL AND PLANNING

**Evaluation & Benchmarking:**
18. ROBOTARENA ∞: UNLIMITED ROBOT BENCHMARKING VIA REAL-TO-SIM TRANSLATION
19. ROBOCASA365: A LARGE-SCALE SIMULATION FRAMEWORK FOR TRAINING AND BENCHMARKING GENERALIST ROBOTS
20. WORLDGYM: WORLD MODEL AS AN ENVIRONMENT FOR POLICY EVALUATION

**Cross-Action-Space:**
21. X-VLA: SOFT-PROMPTED TRANSFORMER AS SCALABLE CROSS-EMBODIMENT VISION-LANGUAGE-ACTION MODEL
22. XR-1: TOWARDS VERSATILE VISION-LANGUAGE-ACTION MODELS VIA LEARNING UNIFIED VISION-MOTION REPRESENTATIONS
23. HIMOE-VLA: HIERARCHICAL MIXTURE-OF-EXPERTS FOR GENERALIST VISION–LANGUAGE–ACTION POLICIES

**Other:**
24. HAMLET: SWITCH YOUR VISION-LANGUAGE-ACTION MODEL INTO A HISTORY-AWARE POLICY
25. COMPOSE YOUR POLICIES! IMPROVING DIFFUSION-BASED OR FLOW-BASED ROBOT POLICIES VIA TEST-TIME DISTRIBUTION-LEVEL COMPOSITION
26. VLM4VLA: REVISITING VISION-LANGUAGE-MODELS IN VISION-LANGUAGE-ACTION MODELS

## Papers on Robustness, Generalization, and Regularization

The document does not identify any papers explicitly using token masking, counterfactual reasoning, or information bottleneck methods as regularization techniques.

However, several papers address generalization and robustness indirectly:

- **X-VLA** employs "soft-prompted transformer" architecture to manage heterogeneous action spaces
- **ACTIONS AS LANGUAGE** addresses catastrophic forgetting through relabeling strategies
- **HAMLET** introduces memory mechanisms to improve temporal robustness
- Papers on cross-action-space learning implicitly tackle generalization challenges

The author notes that "in-context learning" remains underexplored in current VLA research despite its potential for improving zero-shot generalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4431ba6-61a7-49d1-a105-7c191b6573ea",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "6e642f89-8c0c-44db-98a9-5b2a5ee60fdc",
  "sourceToolAssistantUUID": "c4431ba6-61a7-49d1-a105-7c191b6573ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-13T04:43:57.978Z_

Let me fetch more details on the most critical competitor papers and search for a few more specific topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e642f89-8c0c-44db-98a9-5b2a5ee60fdc",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxUipqFTnnsAvmkZ7cy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32dd6992-a9ee-4f7f-b432-158091973b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyTAcWhCYgLHNxQd8tPTa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 2685,
      "cache_read_input_tokens": 27387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2685,
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

_source line 58 · 2026-05-13T04:43:59.683Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CbRuuRiFCNgv7owHfEXKcv`</summary>

```json
{
  "url": "https://icml.cc/virtual/2026/poster/65010",
  "prompt": "What is the full title, authors, and method of this ICML 2026 paper about differentiable grid sample pruning for VLA generalization? Does it use token masking for regularization/generalization rather than just efficiency? What benchmarks does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32dd6992-a9ee-4f7f-b432-158091973b47",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxUipqFTnnsAvmkZ7cy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4aa2449-1819-46a9-8623-11efc1d7139d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyTAcWhCYgLHNxQd8tPTa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 2685,
      "cache_read_input_tokens": 27387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2685,
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

_source line 59 · 2026-05-13T04:44:00.384Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0183JF3nuDWx3upGXkB88c7w`</summary>

```json
{
  "query": "\"See What Matters\" differentiable grid sample pruning VLA generalization ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4aa2449-1819-46a9-8623-11efc1d7139d",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxUipqFTnnsAvmkZ7cy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31e819a8-aa88-41de-995b-67ffacce8353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyTAcWhCYgLHNxQd8tPTa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 2685,
      "cache_read_input_tokens": 27387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2685,
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

_source line 60 · 2026-05-13T04:44:01.224Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HJVSQJxYF97E8HdEgQ5Tif`</summary>

```json
{
  "query": "LightVLA adaptive visual token pruning VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31e819a8-aa88-41de-995b-67ffacce8353",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxUipqFTnnsAvmkZ7cy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a8c7d94-45e4-4bda-8348-a513133cf32f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyTAcWhCYgLHNxQd8tPTa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 2685,
      "cache_read_input_tokens": 27387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2685,
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

_source line 61 · 2026-05-13T04:44:01.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011qRjeCKt3WGjVNkXGtbEeb`</summary>

```json
{
  "query": "\"Don't Blind Your VLA\" visual representations OOD generalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a8c7d94-45e4-4bda-8348-a513133cf32f",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxUipqFTnnsAvmkZ7cy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2323a87-acbf-4ff8-88ec-fe7ef8b2bdb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyTAcWhCYgLHNxQd8tPTa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 2685,
      "cache_read_input_tokens": 27387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2685,
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

_source line 62 · 2026-05-13T04:44:03.064Z_

<details><summary>↩ Tool result · `toolu_01CbRuuRiFCNgv7owHfEXKcv`</summary>

```text
# ICML 2026 Paper Summary

**Full Title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

**Method:** The paper introduces GridS (Differentiable Grid Sampler), described as a "plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA." The approach uses "differentiable interpolation" to extract features while maintaining spatial information, achieving significant compression with under 10% of original visual tokens.

**Token Masking for Generalization:** The provided content does not discuss token masking for regularization or generalization purposes. The focus is purely on computational efficiency and compression.

**Benchmarks:** The paper evaluates performance on:
- LIBERO benchmark
- Real robotic platform

**Results:** GridS achieves "76% reduction in FLOPs with no degradation in the success rate," representing what the authors claim as "the lowest feasible visual token count reported to date."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4aa2449-1819-46a9-8623-11efc1d7139d",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "991863ae-410f-497b-b7fb-ee367a597b1c",
  "sourceToolAssistantUUID": "c4aa2449-1819-46a9-8623-11efc1d7139d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-13T04:44:03.677Z_

<details><summary>↩ Tool result · `toolu_0183JF3nuDWx3upGXkB88c7w`</summary>

```text
Web search results for query: ""See What Matters" differentiable grid sample pruning VLA generalization ICML 2026"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"}]

I found results for your search! Here's what I found:

"See What Matters" presents the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA by adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation.

Vision-Language-Action (VLA) models have shown promise in robotics manipulation, but existing token pruning methods face a trade-off where aggressive compression discards critical geometric details like contact points, leading to performance degradation. GridS preserves essential spatial information while achieving drastic compression with fewer than 10% tokens.

This work appears as an ICML 2026 poster presentation and addresses the challenge of deploying VLA models efficiently for real-time robotics applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31e819a8-aa88-41de-995b-67ffacce8353",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "ae9b465b-1264-437d-9754-ae720a179732",
  "sourceToolAssistantUUID": "31e819a8-aa88-41de-995b-67ffacce8353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-13T04:44:08.917Z_

<details><summary>↩ Tool result · `toolu_01HJVSQJxYF97E8HdEgQ5Tif`</summary>

```text
Web search results for query: "LightVLA adaptive visual token pruning VLA 2025 2026"

Links: [{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"AI Bites | YouTube Channel on X: \"LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by https://t.co/bE0Zv0mb0c\" / X","url":"https://x.com/ai_bites/status/1970481721163313156"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"}]

Based on the search results, here's what I found about LightVLA and adaptive visual token pruning for VLA models:

## Overview

LightVLA is a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by the heavy attention-based computation over large sets of visual tokens.

## Core Mechanism

LightVLA addresses this challenge through adaptive, performance-driven pruning of visual tokens: It generates dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously.

## Key Advantages

Notably, LightVLA requires no heuristic "magic numbers" and introduces no additional trainable parameters, making it compatible with modern inference frameworks.

## Performance Results

LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate. Experimental results demonstrate that LightVLA outperforms different VLA models and existing token pruning methods across diverse tasks on the LIBERO benchmark, achieving higher success rates with substantially reduced computational overhead.

## Significance

LightVLA is the first work to apply adaptive visual token pruning to VLA tasks with the collateral goals of efficiency and performance, marking a significant step toward more efficient, powerful and practical real-time robotic systems.

The paper was published in September 2025 and is scheduled for presentation at ICRA 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a8c7d94-45e4-4bda-8348-a513133cf32f",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "ec81ff72-91ed-4e17-a02c-1169d245566f",
  "sourceToolAssistantUUID": "3a8c7d94-45e4-4bda-8348-a513133cf32f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-13T04:44:09.653Z_

<details><summary>↩ Tool result · `toolu_011qRjeCKt3WGjVNkXGtbEeb`</summary>

```text
Web search results for query: ""Don't Blind Your VLA" visual representations OOD generalization"

Links: [{"title":"Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://blind-vla-paper.github.io/"},{"title":"[2510.25616] Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/abs/2510.25616"},{"title":"[2510.25616v1] Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/abs/2510.25616v1"},{"title":"GitHub - CognitiveAISystems/BlindVLA: Official implementation of Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization. https://blind-vla-paper.github.io","url":"https://github.com/CognitiveAISystems/BlindVLA"},{"title":"Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.25616v1"},{"title":"Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/pdf/2510.25616"},{"title":"Paper page - Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://huggingface.co/papers/2510.25616"},{"title":"[Literature Review] Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://www.themoonlight.io/en/review/dont-blind-your-vla-aligning-visual-representations-for-ood-generalization"},{"title":"Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization [Quick Review]","url":"https://liner.com/review/dont-blind-your-vla-aligning-visual-representations-for-ood-generalization"},{"title":"Enhancing Generalization in Vision-Language-Action Models","url":"https://gen-vla.github.io/"}]

Here are the search results for "Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization":

## Overview

The paper addresses Vision-Language-Action (VLA) models and how, when pretrained Vision-Language Models (VLMs) are adapted to the action modality, their original VL representations and knowledge may not be preserved, with naive action fine-tuning leading to degradation of visual representations.

## Key Findings

The researchers identified three major problems after probing VLA representations: (1) attention sink where attention maps become diffuse and noisy, (2) representation collapse where patch embeddings lose separability, and (3) domain forgetting where VL understanding in symbolic/abstract categories degrade after naive supervised fine-tuning.

## Proposed Solution

To address the degradation of visual-language (VL) representations during VLA supervised fine-tuning (SFT), the paper introduces Visual Representation Alignment. During SFT, the method pulls a VLA's visual tokens toward a frozen teacher's features via a lightweight frozen projector using cosine similarity.

## Evaluation

The approach was evaluated in Simpler-based environments using the VL-Think Task Suite and a benchmark measuring VLA generalization across Vision (textures, noise), Semantics (unseen objects, paraphrases, distractors), and Execution (randomized poses, object changes), with OOD evaluation holding out one variation per axis, including 9 new objects and 16 unseen receptacles.

The paper's code and resources are publicly available on GitHub and at blind-vla-paper.github.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2323a87-acbf-4ff8-88ec-fe7ef8b2bdb5",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "fcd0cc46-5ea9-4a5d-bbe7-a9d2b320f25f",
  "sourceToolAssistantUUID": "a2323a87-acbf-4ff8-88ec-fe7ef8b2bdb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-13T04:44:14.272Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013hTNgfXrvERbtxfBHud1dc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.25616",
  "prompt": "What is the full method of \"Don't Blind Your VLA\"? Does it use any token masking? How does the visual representation alignment work in detail? What benchmarks (SimplerEnv, LIBERO-Plus) does it evaluate on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcd0cc46-5ea9-4a5d-bbe7-a9d2b320f25f",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxVptz3D6a3e6JTDhKF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7642c29-0da6-4add-b4a4-8c833770549e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jo6zajydFFmXsxWJwgCrQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4010,
      "cache_read_input_tokens": 30072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4010,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 67 · 2026-05-13T04:44:14.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X7UN1RwuTVbjy884z4wxGr`</summary>

```json
{
  "query": "Knowledge Insulating Vision-Language-Action Models pi VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7642c29-0da6-4add-b4a4-8c833770549e",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxVptz3D6a3e6JTDhKF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b536635-a0a0-4d6f-9887-1859855c4ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jo6zajydFFmXsxWJwgCrQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4010,
      "cache_read_input_tokens": 30072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4010,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 68 · 2026-05-13T04:44:15.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AGJfQyEYfgN4V7YNLp3x39`</summary>

```json
{
  "query": "\"dropout\" \"masking\" VLA training regularization generalization robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b536635-a0a0-4d6f-9887-1859855c4ad9",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxVptz3D6a3e6JTDhKF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0828a76e-2882-4e9a-973c-4986658cceae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jo6zajydFFmXsxWJwgCrQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4010,
      "cache_read_input_tokens": 30072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4010,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 69 · 2026-05-13T04:44:16.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019ruLEj23T9uc77VRf9S3Xj`</summary>

```json
{
  "query": "ETA-VLA efficient token adaptation temporal fusion sparsification VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0828a76e-2882-4e9a-973c-4986658cceae",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxVptz3D6a3e6JTDhKF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53d3466b-9a7e-4d0b-a892-61e131594af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jo6zajydFFmXsxWJwgCrQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4010,
      "cache_read_input_tokens": 30072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4010,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 70 · 2026-05-13T04:44:16.844Z_

<details><summary>↩ Tool result · `toolu_013hTNgfXrvERbtxfBHud1dc`</summary>

```text
Based on the provided content, I cannot give you the detailed information you're requesting. 

The arXiv abstract page only states that the authors "introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios," but it does not describe the actual method specifics, token masking approaches, or technical details of visual representation alignment.

Similarly, the page does not mention SimplerEnv, LIBERO-Plus, or other specific benchmarks used in evaluation. To obtain these details about the methodology, alignment mechanisms, and experimental benchmarks, you would need to access the full paper PDF or HTML version linked on this page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7642c29-0da6-4add-b4a4-8c833770549e",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "1d270df0-ca54-4474-b4f4-cf30dc301068",
  "sourceToolAssistantUUID": "f7642c29-0da6-4add-b4a4-8c833770549e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-13T04:44:22.896Z_

<details><summary>↩ Tool result · `toolu_01X7UN1RwuTVbjy884z4wxGr`</summary>

```text
Web search results for query: "Knowledge Insulating Vision-Language-Action Models pi VLA 2026"

Links: [{"title":"Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better | OpenReview","url":"https://openreview.net/forum?id=cb0xbZ3APM"},{"title":"Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://arxiv.org/html/2505.23705v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2505.23705] Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://arxiv.org/abs/2505.23705"},{"title":"Knowledge Insulating Vision-Language-Action Models","url":"https://www.pi.website/download/pi05_KI.pdf"},{"title":"[Literature Review] Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://www.themoonlight.io/en/review/knowledge-insulating-vision-language-action-models-train-fast-run-fast-generalize-better"},{"title":"VLAs that Train Fast, Run Fast, and Generalize Better","url":"https://www.pi.website/research/knowledge_insulation"},{"title":"NeurIPS Poster Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://neurips.cc/virtual/2025/poster/117079"},{"title":"[PDF] Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f8a3331421b98c7d4065ecf55c4013e6306359f2"},{"title":"Porting and Optimizing Advanced Vision-Language-Action Models for Embedded Autonomous Systems - 2026 Embedded Vision Summit","url":"https://embeddedvisionsummit.com/2026/session/porting-and-optimizing-advanced-vision-language-action-models-for-embedded-autonomous-systems"}]

Based on the search results, here's what I found about "Knowledge Insulating Vision-Language-Action Models":

## Overview

This research studies Vision-Language-Action models that include continuous diffusion or flow matching action experts, showing that naively including such experts significantly harms both training speed and knowledge transfer, and proposes a technique for insulating the VLM backbone during VLA training to address this issue.

## The Core Problem

The constraints of real-time control are often at odds with the design of VLMs: the most powerful VLMs have tens or hundreds of billions of parameters, presenting an obstacle to real-time inference, and operate on discrete tokens rather than the continuous-valued outputs required for controlling robots. Adding new motor control weights to the model during VLA finetuning can damage the VLM's internal representations, causing "forgetfulness," slowing down training significantly and harming the model's ability to interpret language.

## The Solution: Knowledge Insulation

The key idea behind knowledge insulation is to fine-tune the VLM backbone with discretized actions while simultaneously adapting an action expert to produce continuous actions (e.g., via flow matching or diffusion) without propagating its gradients back into the VLM backbone. The method fine-tunes the VLM backbone with FAST-tokenized discretized actions for learning high-quality representations quickly, while simultaneously adapting the action expert to produce continuous actions without propagating its gradients back into the VLM backbone, and after training, the action expert can produce fluent continuous actions via flow matching while the discretized actions are discarded.

## Research Details

The paper was published in May 2025 by researchers including Danny Driess and colleagues from Physical Intelligence. Videos and open-source model weights are available at their research website and GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b536635-a0a0-4d6f-9887-1859855c4ad9",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "f3ded621-ad8d-4883-a106-93730b30415c",
  "sourceToolAssistantUUID": "9b536635-a0a0-4d6f-9887-1859855c4ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-13T04:44:23.477Z_

<details><summary>↩ Tool result · `toolu_01AGJfQyEYfgN4V7YNLp3x39`</summary>

```text
Web search results for query: ""dropout" "masking" VLA training regularization generalization robot 2026"

Links: [{"title":"Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization","url":"https://arxiv.org/html/2602.09722"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.23202v1"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://rlvla.github.io/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"Domain-generalized person re-identification via refined neuron dropout and reciprocal-expansion re-ranking | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-30664-4"},{"title":"Contrastive Representation Regularization for Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01711v1"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"}]

I found relevant research on dropout, masking, VLA training, regularization, and robot generalization from 2026. Here's what the search results show:

## Key Findings on Sensory Dropout and Training Regularization

A systematic study on scaling Vision-Language-Action (VLA) models evaluates the scalability of training modifications, such as sensory dropout and curriculum learning, to determine if these approaches provide tangible benefits in a large-scale pretraining regime.

The results are striking: Complex training techniques like sensory dropout do not consistently bring improvements, suggesting that simple training recipes are often sufficient. This is further confirmed across multiple analyses, where intuitive strategies, such as sensory dropout and multi-stage fine-tuning, do not consistently improve performance at scale.

## Related Regularization Approaches

The research also explores alternative regularization techniques for VLAs. For instance, gaze-regularized training strategy utilizes human gaze as a training-time supervisory prior to direct the model's internal attention to actionable regions in the scene, without changing the underlying architecture or requiring gaze at inference.

## Broader Context on VLA Generalization

A systematic study on scaling Vision-Language-Action (VLA) models with heterogeneous robot data introduces a Grouped Blind Ensemble protocol that minimizes human bias in real-world experiments, providing more reliable evaluations of generalization capabilities.

The research suggests that while regularization techniques like dropout have intuitive appeal, simply increasing data scale does not automatically lead to better performance, indicating that the relationship between regularization, data scaling, and generalization in robotics is more nuanced than traditional machine learning assumptions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0828a76e-2882-4e9a-973c-4986658cceae",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "6860f027-761a-4404-a337-07fa3efcc845",
  "sourceToolAssistantUUID": "0828a76e-2882-4e9a-973c-4986658cceae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-13T04:44:25.596Z_

<details><summary>↩ Tool result · `toolu_019ruLEj23T9uc77VRf9S3Xj`</summary>

```text
Web search results for query: "ETA-VLA efficient token adaptation temporal fusion sparsification VLA"

Links: [{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766v1"},{"title":"[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.25766"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for","url":"https://arxiv.org/pdf/2508.19257"},{"title":"[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.19257"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.10518"},{"title":"HiST-VLA: A Hierarchical Spatio-Temporal Vision-Language-Action Model for End-to-End Autonomous Driving","url":"https://arxiv.org/html/2602.13329"},{"title":"[PDF] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TTF-VLA:-Temporal-Token-Fusion-via-Pixel-Attention-Liu-Zhang/02462f0f53d1b48867e35eae8901d75996e5a662"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/395033880_TTF-VLA_Temporal_Token_Fusion_via_Pixel-Attention_Integration_for_Vision-Language-Action_Models"}]

Based on the search results, here's information about ETA-VLA:

## ETA-VLA Overview

ETA-VLA is an Efficient Temporal Aggregation framework for VLA models. It addresses the integration of Vision-Language-Action (VLA) models into autonomous driving systems, offering a unified framework for interpreting complex scenes and executing control commands.

## Key Components

ETA-VLA introduces two complementary components: a Temporal Fusion Module (TFM) and an Intra-LLM Sparse Aggregator (ILSA).

**Temporal Fusion Module:** The TFM mitigates the linear growth of token count with time by operating on visual encoder features before the LLM, and adaptively fuses multi-frame historical features into a concise representation via transformer and learnable weights.

**Intra-LLM Sparse Aggregator:** ILSA dynamically identifies and prunes redundant visual tokens guided by textual queries and temporal consistency, utilizing a text-guided scoring mechanism alongside a diversity-preserving sparsification strategy.

## Performance and Efficiency

ETA-VLA (with 35% token pruning) establishes a new state-of-the-art with an EPDMS score of 85.0 on the NAVSIM v2 Navtest benchmark. The method achieves driving performance comparable to state-of-the-art baselines while reducing computational FLOPs by approximately 32%. The method prunes 85% of visual tokens and reduces inference FLOPs by 61%, but still retains 94% of the original accuracy on the NAVSIM v2 benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53d3466b-9a7e-4d0b-a892-61e131594af5",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "c549f271-550c-475b-8cbf-58a62c0094a7",
  "sourceToolAssistantUUID": "53d3466b-9a7e-4d0b-a892-61e131594af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-13T04:44:29.660Z_

This is extremely important -- let me fetch the paper that explicitly studies sensory dropout in VLA scaling, as it may be a direct competitor or challenge to the token masking idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c549f271-550c-475b-8cbf-58a62c0094a7",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxX12Tp3k5sSWqcg6We",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44931ec5-0826-493a-9afa-fe704bb31e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQniUJoaSQA2mPK5jTh2Gr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3411,
      "cache_read_input_tokens": 34082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3411,
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

_source line 75 · 2026-05-13T04:44:31.566Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JzX9jKbiVAREaxdX4ekyy9`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.09722",
  "prompt": "What is the full title, authors, and main findings of this paper? What exactly is \"sensory dropout\" in the context of this paper? How was it tested? Did they test masking/dropping visual tokens as regularization? What were the results -- did sensory dropout help or hurt? What scale of training was involved? What benchmarks did they use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44931ec5-0826-493a-9afa-fe704bb31e54",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxX12Tp3k5sSWqcg6We",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0f5814f-46e2-4548-9018-cf28f857169a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQniUJoaSQA2mPK5jTh2Gr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3411,
      "cache_read_input_tokens": 34082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3411,
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

_source line 76 · 2026-05-13T04:44:33.440Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014HxswnaDa4MAKEgEmgC28J`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.22195",
  "prompt": "What is the full title, authors, and method of VLM2VLA (Actions as Language)? Does it use any form of token masking? How does it prevent catastrophic forgetting? What conference was it accepted to?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0f5814f-46e2-4548-9018-cf28f857169a",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxX12Tp3k5sSWqcg6We",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35a9e88d-deca-488e-aed5-9bbe7739cb9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQniUJoaSQA2mPK5jTh2Gr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3411,
      "cache_read_input_tokens": 34082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3411,
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

_source line 77 · 2026-05-13T04:44:34.151Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015oMJdXoa6Mk8v6RGqWkNNg`</summary>

```json
{
  "query": "\"random token masking\" \"visual token\" regularization finetuning generalization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35a9e88d-deca-488e-aed5-9bbe7739cb9e",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxX12Tp3k5sSWqcg6We",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c06ba932-07fd-4450-aea2-fea3df4f6bc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQniUJoaSQA2mPK5jTh2Gr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3411,
      "cache_read_input_tokens": 34082,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 34082,
          "cache_creation_input_tokens": 3411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3411,
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

_source line 78 · 2026-05-13T04:44:38.054Z_

<details><summary>↩ Tool result · `toolu_01JzX9jKbiVAREaxdX4ekyy9`</summary>

```text
# Paper Summary

**Title & Authors:**
"Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization" by Wang et al. from Renmin University of China, BeingBeyond, and Peking University.

**Main Findings:**
The research challenges common assumptions about scaling robotic models across diverse embodiments. Key discoveries include: end-effector-relative action representations outperform alternatives, naive data pooling across robots causes performance degradation rather than gains, and standard regularization techniques provide minimal benefits at scale.

**Sensory Dropout Definition & Testing:**
Sensory dropout involves stochastically masking inputs during training. Specifically, they tested "masking proprioception by zeroing the input proprioceptive vector with probability p=0.2" and "independent dropping of each camera view with p=0.2" while ensuring at least one visual view remained.

**Results on Sensory Dropout:**
Counterintuitively, sensory dropout *hurt* performance. Disabling visual dropout increased success rates to 85.6% versus the baseline of 84.5%, while heavy proprioceptive masking reduced performance further. The authors suggest "the natural diversity of the pre-training corpus already serves as an effective regularizer."

**Training Scale:**
Pre-training used "a global batch size of 256 on 8 NVIDIA A800 GPUs" across approximately 182 million balanced frame transitions.

**Benchmarks:**
Evaluation included LIBERO 5-shot tasks, RoboCasa (24 kitchen tasks), and four real-robot tasks on a Franka Panda arm.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0f5814f-46e2-4548-9018-cf28f857169a",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "5267321d-ad87-4cd6-854d-9c0402ef6aa0",
  "sourceToolAssistantUUID": "f0f5814f-46e2-4548-9018-cf28f857169a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-13T04:44:38.069Z_

<details><summary>↩ Tool result · `toolu_014HxswnaDa4MAKEgEmgC28J`</summary>

```text
# VLM2VLA: Actions as Language - Summary

**Full Title:** "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting"

**Authors:** Asher J. Hancock, Xindi Wu, Lihan Zha, Olga Russakovsky, and Anirudha Majumdar

**Method:** The approach represents low-level robot actions as natural language text to align with the VLM's pretraining distribution, then applies "Low-Rank Adaptation (LoRA)" for minimal backbone modification during fine-tuning.

**Token Masking:** The provided content does not mention token masking techniques.

**Catastrophic Forgetting Prevention:** The paper addresses this by identifying "a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data." By representing actions linguistically and using LoRA, the model "minimally modifying the VLM backbone and averting catastrophic forgetting."

**Conference Acceptance:** The document does not indicate acceptance to any conference. It shows submission to arXiv on September 26, 2025 (preprint server), with no conference venue mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35a9e88d-deca-488e-aed5-9bbe7739cb9e",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "801d830d-71fb-401a-b651-14218710c5bb",
  "sourceToolAssistantUUID": "35a9e88d-deca-488e-aed5-9bbe7739cb9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-13T04:44:41.340Z_

<details><summary>↩ Tool result · `toolu_015oMJdXoa6Mk8v6RGqWkNNg`</summary>

```text
Web search results for query: ""random token masking" "visual token" regularization finetuning generalization 2025 2026"

Links: [{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"arXiv:2505.10518v1 [cs.CL] 15 May 2025 Multi-Token Prediction Needs Registers","url":"https://arxiv.org/pdf/2505.10518"},{"title":"Learning to Mask and Permute Visual Tokens for Vision Transformer Pre-Training","url":"https://arxiv.org/html/2306.07346"},{"title":"Masked Token Prediction (MTP)","url":"https://www.emergentmind.com/topics/masked-token-prediction-mtp"},{"title":"[2306.07346] Learning to Mask and Permute Visual Tokens for Vision Transformer Pre-Training","url":"https://arxiv.org/abs/2306.07346"},{"title":"DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Alvar_DivPrune_Diversity-based_Visual_Token_Pruning_for_Large_Multimodal_Models_CVPR_2025_paper.pdf"},{"title":"Masked-Input Multi-Token Prediction","url":"https://www.emergentmind.com/topics/masked-input-multi-token-prediction"},{"title":"Rethinking Token Reduction with Parameter-Efficient Fine-Tuning in ViT for","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Lei_Rethinking_Token_Reduction_with_Parameter-Efficient_Fine-Tuning_in_ViT_for_Pixel-Level_CVPR_2025_paper.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf"},{"title":"[2505.08561] Reinforcement Learning meets Masked Video Modeling : Trajectory-Guided Adaptive Token Selection","url":"https://arxiv.org/abs/2505.08561"}]

I've completed a web search for your query about random token masking, visual tokens, regularization, fine-tuning, and generalization in 2025-2026. Here are the relevant findings:

## Key Research Areas

**Masked Token Prediction and Regularization:**
Random token masking provides implicit gradient averaging and acts as an input-level regularizer, with masked-input multi-token prediction achieving measurable improvements across tasks and benchmarks.

**Visual Token Masking Strategies:**
Recent approaches have employed the Masked Image Modeling paradigm, which pre-trains a backbone by reconstructing visual tokens associated with randomly masked image patches, though this masking approach introduces noise into the input data during pre-training, leading to discrepancies that can impair performance during the fine-tuning phase.

MaPeT (Masked and Permuted Vision Transformer) employs autoregressive and permuted predictions to capture intra-patch dependencies, addressing generalization issues.

**Video and Spatial Token Masking:**
Masked video modeling has emerged as a highly effective pre-training strategy for visual foundation models, whereby the model reconstructs masked spatiotemporal tokens, however, a key challenge in such approaches lies in selecting an appropriate masking strategy.

**Fine-tuning and Transfer Learning:**
Enhanced supervised fine-tuning and parameter-efficient training for domains such as math, summarization, and code benefit from masked-input multi-token prediction approaches.

The search results show active research in 2025 on how random token masking and regularization techniques improve model generalization during fine-tuning across vision and multimodal models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c06ba932-07fd-4450-aea2-fea3df4f6bc7",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "14ad3853-f9e0-41fa-9b8c-3a055929c419",
  "sourceToolAssistantUUID": "c06ba932-07fd-4450-aea2-fea3df4f6bc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-13T04:44:44.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019UW57E8SKxJeFGroyahJ7i`</summary>

```json
{
  "query": "SimplerEnv benchmark VLA evaluation visual matching variant aggregation Google Robot WidowX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14ad3853-f9e0-41fa-9b8c-3a055929c419",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxYANpAK4ceKGkP6viA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db57acbf-da64-4f63-8bc7-ba27517c86df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzjqpGA7JBFXxcndosEh7Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 37493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 82 · 2026-05-13T04:44:45.468Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BpNvetJD7ny77q8S6nnze`</summary>

```json
{
  "query": "\"information bottleneck\" \"token masking\" regularization vision language model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db57acbf-da64-4f63-8bc7-ba27517c86df",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxYANpAK4ceKGkP6viA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cce2621f-6aa5-4c8b-94c7-2dbd17a960d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzjqpGA7JBFXxcndosEh7Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 37493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 83 · 2026-05-13T04:44:46.677Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019svJ6Wd7psghMbWcxmR7JH`</summary>

```json
{
  "url": "https://gen-vla.github.io/",
  "prompt": "What benchmarks does Gen-VLA evaluate on? Does it use SimplerEnv or LIBERO? What are the visual matching and variant aggregation results? What is the full author list?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce2621f-6aa5-4c8b-94c7-2dbd17a960d6",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxYANpAK4ceKGkP6viA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "097f33d5-d0b3-43ac-ab4f-227abecbc144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzjqpGA7JBFXxcndosEh7Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 37493,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 37493,
          "cache_creation_input_tokens": 2074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2074,
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

_source line 84 · 2026-05-13T04:44:50.601Z_

<details><summary>↩ Tool result · `toolu_019svJ6Wd7psghMbWcxmR7JH`</summary>

```text
Based on the webpage content provided:

**Benchmarks and Datasets:**
The paper evaluates on SimplerEnv, as evidenced by the section headers "SimplerEnv Visual Matching" and "SimplerEnv Variant Aggregation (OOD)." The document does not mention LIBERO as an evaluation benchmark.

**Visual Matching and Variant Aggregation Results:**
The webpage includes bar charts for both metrics but does not provide specific numerical values in the text. It only states that the approach "demonstrates substantially stronger generalization" and shows "significant improvements" compared to baselines.

**Full Author List:**
The research team includes: Shresth Grover, Akshay Gopalkrishnan, Bo Ai, Henrik I. Christensen, Hao Su, and Xuanlin Li, with affiliations at UC San Diego and Hillbot.

**Note:** The paper is titled "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" rather than "Gen-VLA." The code is noted as "Coming Soon" on the GitHub repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "097f33d5-d0b3-43ac-ab4f-227abecbc144",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "b9074756-26c6-4c3b-8428-9d9c00fa6dbb",
  "sourceToolAssistantUUID": "097f33d5-d0b3-43ac-ab4f-227abecbc144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-13T04:44:50.618Z_

<details><summary>↩ Tool result · `toolu_019UW57E8SKxJeFGroyahJ7i`</summary>

```text
Web search results for query: "SimplerEnv benchmark VLA evaluation visual matching variant aggregation Google Robot WidowX"

Links: [{"title":"GitHub - simpler-env/SimplerEnv: Evaluating and reproducing real-world robot manipulation policies (e.g., RT-1, RT-1-X, Octo) in simulation under common setups (e.g., Google Robot, WidowX+Bridge) (CoRL 2024) · GitHub","url":"https://github.com/simpler-env/SimplerEnv"},{"title":"GitHub - DelinQu/SimplerEnv-OpenVLA: Evaluating and reproducing real-world robot manipulation policies (e.g., RT-1, RT-1-X, Octo, and OpenVLA) in simulation under common setups (e.g., Google Robot, WidowX+Bridge) · GitHub","url":"https://github.com/DelinQu/SimplerEnv-OpenVLA"},{"title":"GitHub - allenzren/SimplerEnv: Evaluating and reproducing real-world robot manipulation policies (e.g., RT-1, RT-1-X, Octo) in simulation under common setups (e.g., Google Robot, WidowX+Bridge) (CoRL 2024)","url":"https://github.com/allenzren/SimplerEnv"},{"title":"GitHub - LiHaoHN/SimX-OR: SimX-OR: Extending Any Simulation Benchmark to Evaluate the Observational Robustness of VLA Models","url":"https://github.com/LiHaoHN/SimX-OR"},{"title":"tracevla: visual trace prompting enhances spatial-temporal ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf"},{"title":"Isaac-GR00T/examples/SimplerEnv/README.md at main · NVIDIA/Isaac-GR00T","url":"https://github.com/NVIDIA/Isaac-GR00T/blob/main/examples/SimplerEnv/README.md"},{"title":"InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy","url":"https://arxiv.org/html/2510.13778v1"},{"title":"GitHub - Ratstar216/SimplerEnv-HSR: Evaluating and reproducing real-world robot manipulation policies (e.g., RT-1, RT-1-X, Octo, and OpenVLA) in simulation under common setups (e.g., Google Robot, WidowX+Bridge) · GitHub","url":"https://github.com/Ratstar216/SimplerEnv-HSR"},{"title":"VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting","url":"https://arxiv.org/html/2507.05116v3"},{"title":"SimplerEnv-OpenVLA/README.md at main · DelinQu/SimplerEnv-OpenVLA","url":"https://github.com/DelinQu/SimplerEnv-OpenVLA/blob/main/README.md"}]

Based on the search results, here's what I found about SimplerEnv benchmark VLA evaluation with visual matching and variant aggregation:

## SimplerEnv Overview

SimplerEnv provides policy inference scripts to reproduce Google Robot and WidowX real-to-sim evaluation results with sweeps over object/robot poses and advanced loggings.

## Two Main Evaluation Setups

SimplerEnv encompasses two distinct real-to-sim evaluation approaches:

1. **Visual Matching Evaluation**: This approach matches real and simulated visual appearances for policy evaluation by overlaying real-world images onto simulation backgrounds and adjusting foreground object and robot textures in simulation.

2. **Variant Aggregation Evaluation**: This creates different simulated environment variants (e.g., different backgrounds, lightings, distractors, table textures, etc) and averages their results.

## VLA Model Evaluation

The benchmark supports policy inference with both visual matching and variant aggregation evaluation setups along with RT-1, RT-1-X, and Octo policies. Additional implementations also support OpenVLA models.

## Technical Foundation

The repository's code is based in the SAPIEN simulator and the CPU based ManiSkill2 benchmark. There is also an integration with the Bridge dataset environments into ManiSkill3, which offers GPU parallelization and can run 10-15x faster than the ManiSkill2 version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db57acbf-da64-4f63-8bc7-ba27517c86df",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "a4a3d1f0-c51b-49b6-9884-53d64f452383",
  "sourceToolAssistantUUID": "db57acbf-da64-4f63-8bc7-ba27517c86df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-13T04:44:53.320Z_

<details><summary>↩ Tool result · `toolu_011BpNvetJD7ny77q8S6nnze`</summary>

```text
Web search results for query: ""information bottleneck" "token masking" regularization vision language model 2025 2026"

Links: [{"title":"HybridToken-VLM: Hybrid Token Compression for Vision-Language Models","url":"https://arxiv.org/html/2512.08240"},{"title":"The Describe-Then-Generate Bottleneck: How VLM Descriptions Alter Image Generation Outcomes Sports Vision Research","url":"https://arxiv.org/html/2509.18179v1"},{"title":"Visual-Language Models Overview","url":"https://www.emergentmind.com/topics/visual-language-model-vlm-7a269805-2dcd-4718-9ddd-caa784f88849"},{"title":"masked-vision-and-language-modeling-for-multi-modal- ...","url":"https://assets.amazon.science/da/b0/6023fe3b4c69989e069a0c0abddd/masked-vision-and-language-modeling-for-multi-modal-representation-learning.pdf"},{"title":"GitHub - VILA-Lab/Awesome-DLMs: The official GitHub repo for the survey paper \"A Survey on Diffusion Language Models\". · GitHub","url":"https://github.com/VILA-Lab/Awesome-DLMs"},{"title":"Token Bottleneck: One Token to Remember Dynamics","url":"https://arxiv.org/html/2507.06543v1"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"TokenCom: Vision-Language Model for Multimodal and Multitask Token Communications","url":"https://arxiv.org/html/2603.00482v1"},{"title":"Vision-centric Token Compression in Large Language Model","url":"https://arxiv.org/pdf/2502.00791"},{"title":"ExLM: Rethinking the Impact of [MASK] Tokens in Masked Language Models","url":"https://arxiv.org/html/2501.13397v1"}]

I've completed the web search for your query on information bottleneck, token masking, and regularization in vision-language models. Here's a summary of the relevant findings from 2025-2026:

## Key Research Findings:

**Vision-Language Model Compression and Bottlenecks:**

Recent work grounds architectural design in the Information Bottleneck principle and variational inference. HTC-VLM introduces a hybrid framework that disentangles semantics and appearance through dual channels using a continuous pathway for fine-grained details and discrete pathway for symbolic anchors, which are fused through a disentanglement attention mask and bottleneck.

**Token Masking as Regularization:**

Masked image modeling (MIM) and masked language modeling (MLM) serve as auxiliary regularization techniques in vision-language models. Frequency-based masking strategies improve the information density of text token embeddings, and this role is critical for guiding visual encoders to capture semantically meaningful features.

**Information-Theoretic Approaches:**

The Information Bottleneck Principle establishes fundamental limits on information transmission through intermediate representations, with Optimal Multimodal Information Bottleneck frameworks addressing imbalanced task-relevant information across modalities through theoretically-derived regularization bounds.

**Token Merging Methods:**

Recent IBTM (Information Bottleneck inspired Token Merging) is motivated by reducing the Information Bottleneck, with a novel variational upper bound for the IB loss, where the mask module generates token merging masks designed to reduce this bound.

The search results show significant research activity in 2025-2026 on applying information-theoretic principles to improve vision-language model efficiency through token masking and bottleneck-based regularization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce2621f-6aa5-4c8b-94c7-2dbd17a960d6",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "f09d3963-0ea4-42bf-8374-59bba9a20d52",
  "sourceToolAssistantUUID": "cce2621f-6aa5-4c8b-94c7-2dbd17a960d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-13T04:44:56.041Z_

Let me do one final round of searches to catch any closely-related work I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f09d3963-0ea4-42bf-8374-59bba9a20d52",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxZ3bJXk9xeT48p6y3A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a96bd3e6-9742-4d4b-afad-77e6d0a81fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPxK7qXdsiccDEEKvrRMJy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 280,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 39567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2417,
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

_source line 88 · 2026-05-13T04:44:56.678Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016gWtABi5FzqpJ3UxYECQrz`</summary>

```json
{
  "query": "\"visual token masking\" \"as regularization\" robot policy training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a96bd3e6-9742-4d4b-afad-77e6d0a81fc9",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxZ3bJXk9xeT48p6y3A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b805f80-7a8e-4c93-a88d-815a3c4602b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPxK7qXdsiccDEEKvrRMJy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 280,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 39567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2417,
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

_source line 89 · 2026-05-13T04:44:57.719Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DuFujTg8uGTEcNbtYZ9vvY`</summary>

```json
{
  "query": "CRAFT VLA variational information bottleneck force-aware curriculum finetuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b805f80-7a8e-4c93-a88d-815a3c4602b3",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxZ3bJXk9xeT48p6y3A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0c77888-2d84-4602-96e1-7244174cdbef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPxK7qXdsiccDEEKvrRMJy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 280,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 39567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2417,
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

_source line 90 · 2026-05-13T04:44:58.443Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HFAmXeNM7jdvRW2uvXUQzS`</summary>

```json
{
  "query": "\"RL token\" RLT VLA information bottleneck encoder decoder 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0c77888-2d84-4602-96e1-7244174cdbef",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011CayxZ3bJXk9xeT48p6y3A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "766ec4c9-9aeb-440b-901f-a2ea09d6e65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPxK7qXdsiccDEEKvrRMJy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 280,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 39567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2417,
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

_source line 91 · 2026-05-13T04:45:03.526Z_

<details><summary>↩ Tool result · `toolu_01DuFujTg8uGTEcNbtYZ9vvY`</summary>

```text
Web search results for query: "CRAFT VLA variational information bottleneck force-aware curriculum finetuning 2026"

Links: [{"title":"CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning","url":"https://arxiv.org/html/2602.12532v1"},{"title":"[2602.12532] CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning","url":"https://arxiv.org/abs/2602.12532"},{"title":"Revisiting the Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=w10KdRwcMk"},{"title":"Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning","url":"https://arxiv.org/html/2602.08167v1"},{"title":"Deep Variational Multivariate Information Bottleneck","url":"https://www.jmlr.org/papers/volume26/24-0204/24-0204.pdf"},{"title":"[1612.00410] Deep Variational Information Bottleneck","url":"https://arxiv.org/abs/1612.00410"},{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"Deep Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=HyxQzBceg"},{"title":"GitHub - 52CV/CVPR-2025-Papers · GitHub","url":"https://github.com/52CV/CVPR-2025-Papers"},{"title":"Variational Autoencoders (VAEs): The Latent Intelligence (AI 2026)","url":"https://blog.weskill.org/2026/04/variational-autoencoders-vaes-latent.html"}]

I found relevant information about CRAFT! Here are the key details:

## CRAFT: Force-Aware Curriculum Fine-Tuning for VLA Models

CRAFT is a lightweight and model-agnostic framework for adapting pretrained VLA models to contact-rich manipulation.

### Core Methodology

CRAFT introduces a variational information bottleneck (VIB) after the vision–language encoder to temporarily restrict the information flow from visual and language embeddings. Within a curriculum fine-tuning scheme, the VIB initially imposes a strong Kullback–Leibler (KL) penalty that suppresses high-entropy visual and language signals, compelling the policy to focus on low-entropy force inputs and thereby acquire stable, contact-aware behaviors.

As training progresses, the weight of the VIB regularization is gradually annealed, releasing the bottleneck and allowing the model to reincorporate rich perceptual information while retaining the previously learned force-sensitive representations.

### Results

Extensive real-world experiments demonstrate that CRAFT enhances task success, improves generalization to unseen objects and novel tasks, and is broadly applicable across different VLA-based approaches.

The research was published in February 2026 on arXiv (paper ID: 2602.12532).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0c77888-2d84-4602-96e1-7244174cdbef",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "e0789e77-1aa2-4524-ac9c-16af5a653a1c",
  "sourceToolAssistantUUID": "c0c77888-2d84-4602-96e1-7244174cdbef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-13T04:45:03.948Z_

<details><summary>↩ Tool result · `toolu_016gWtABi5FzqpJ3UxYECQrz`</summary>

```text
Web search results for query: ""visual token masking" "as regularization" robot policy training 2025 2026"

Links: [{"title":"From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.04678v1"},{"title":"ICLR 2025 Schedule","url":"https://iclr.cc/virtual/2025/calendar"},{"title":"Language-Guided Token Compression with Reinforcement Learning in Large Vision-Language Models","url":"https://arxiv.org/html/2603.13394v1"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Real-World Robot Learning with Masked Visual Pre-training","url":"https://tetexiao.com/projects/real-mvp"},{"title":"(PDF) Masked Visual-Tactile Pre-training for Robot Manipulation","url":"https://www.researchgate.net/publication/378067504_Masked_Visual-Tactile_Pre-training_for_Robot_Manipulation"},{"title":"GitHub - ir413/mvp: Masked Visual Pre-training for Robotics · GitHub","url":"https://github.com/ir413/mvp"},{"title":"Robot Learning with Sensorimotor Pre-training","url":"https://robotic-pretrained-transformer.github.io/"},{"title":"4D Visual Pre-training for Robot Learning - CVF Open Access","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_4D_Visual_Pre-training_for_Robot_Learning_ICCV_2025_paper.pdf"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"}]

Based on the search results, I found relevant research on visual token masking and related techniques in robot policy training from 2025-2026:

## Key Findings

**Vision-Language-Action (VLA) Models and Regularization:**
Vision-Language-Action (VLA) models have emerged as a paradigm for learning generalist robotic policies, with these methods achieving robust performance across diverse tasks and environments by training on large-scale datasets. Recent approaches explicitly regularize VLMs via discrete latent action supervision.

**Masked Prediction for Robot Learning:**
Research on sensorimotor pre-training encodes interleaved sequences of camera images, proprioceptive robot states, and past actions into tokens, masks out random subsets, and trains models to predict the masked-out content from the rest. This involves random masking across all modalities and time using high masking ratios to encourage the model to learn cross-modal, spatio-temporal representations.

**Masked Visual Pre-training Applications:**
Pretraining models predict future actions as well as object pose and size using masked multimodal inputs, facilitating cross-modal regularization.

**Token Efficiency in Vision Models:**
More recent work has also explored token reduction techniques. Self-attention modules enable tokens to interact with the entire visual field to generate adaptive pruning masks, which is essential for accurately distinguishing between task-critical information and disposable visual noise.

The search results show that visual token masking is being actively used as both a regularization technique and a pre-training approach in robot policy training, with recent papers from 2025-2026 demonstrating its effectiveness in various robotic learning scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b805f80-7a8e-4c93-a88d-815a3c4602b3",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "553f6279-b68c-4a79-9129-65ef2de2f117",
  "sourceToolAssistantUUID": "3b805f80-7a8e-4c93-a88d-815a3c4602b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-13T04:45:07.023Z_

<details><summary>↩ Tool result · `toolu_01HFAmXeNM7jdvRW2uvXUQzS`</summary>

```text
Web search results for query: ""RL token" RLT VLA information bottleneck encoder decoder 2026"

Links: [{"title":"Precise Manipulation with Efficient Online RL","url":"https://www.pi.website/research/rlt"},{"title":"RL Token: Online RL with VLAs | Mochan.org | Mochan Shrestha","url":"https://mochan.org/posts/rlt/"},{"title":"The Last Millimeter: Physical Intelligence Unveils RL Tokens for Hyper-Fast Precision | Humanoids Daily","url":"https://www.humanoidsdaily.com/news/the-last-millimeter-physical-intelligence-unveils-rl-tokens-for-hyper-fast-precision"},{"title":"RL Token: Bootstrapping Online RL with Vision-Language-Action Models","url":"https://www.pi.website/download/rlt.pdf"},{"title":"RL Token: Bootstrapping Online RL with Vision-Language-Action Models","url":"https://arxiv.org/html/2604.23073v1"},{"title":"[2604.23073] RL Token: Bootstrapping Online RL with Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.23073"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Is Zuckerberg's Bold Bet Paying Off? Meta Speeds Up Long-Context Processing in LLMs by 30 Times","url":"https://eu.36kr.com/en/p/3457775156336003"},{"title":"Fwd2Bot: LVLM Visual Token Compression with Double Forward Bottleneck","url":"https://arxiv.org/html/2503.21757v1"}]

Based on the search results, here's what I found about RL Token (RLT), VLA, and the information bottleneck encoder-decoder architecture:

## RL Token Overview

An RL token summarizes the information that the RL actor and critic need about the current observation, making it possible for even a very small actor and critic to learn to improve the model based on its own rich internal representations.

## How It Works with VLAs

The RL Token is extracted from VLA models to enable fast online RL and improve throughput on precise tasks with few hours of data. RLT adds a special output token that provides a compact interface between the VLA and a lightweight RL policy, allowing the robot to adapt its behavior in just a few hours without fine-tuning the full model.

## Information Bottleneck Architecture

By forcing the decoder to rebuild the full context from just this one vector, the system creates an information bottleneck that mathematically guarantees the RL Token captures and retains all the crucial, task-relevant visual and contextual information from the scene.

RLT adds an encoder-decoder transformer to a pretrained VLA. The augmented sequence is then processed through a small, additional encoder transformer, and the output at the special token's position becomes the RL token.

## Performance Results

Across four challenging manipulation tasks, RLT speeds up the most precise stages of each task by up to 3×, and can surpass the speed of human teleoperation. RLT was evaluated on four challenging manipulation tasks that require high precision at critical moments: using an electric screwdriver to drive a tiny M3 screw into a robot arm, zip tie fastening, ethernet cable insertion and power-cord insertion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "766ec4c9-9aeb-440b-901f-a2ea09d6e65f",
  "isSidechain": true,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "agentId": "a6466d84670312cd2",
  "type": "user",
  "uuid": "68217126-269a-4470-b9d7-ff197c9050ff",
  "sourceToolAssistantUUID": "766ec4c9-9aeb-440b-901f-a2ea09d6e65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 94 · 2026-05-13T04:46:37.240Z_

Now I have comprehensive data. Let me compile the final analysis.

---

Here is my comprehensive review of competitive and concurrent work for the "Counterfactual Token Masking" (CTM) idea for VLA finetuning, organized by search area.

---

## 1. Token Masking / Dropout in VLAs

**This is the most crowded competitive space.** There is a large and rapidly growing body of work on visual token pruning/masking in VLAs, though most focus on **inference efficiency** rather than **regularization for generalization**:

- **VLA-Pruner** (arXiv:2511.16449, Nov 2025, updated Feb 2026): Temporal-aware dual-level visual token pruning. Uses prefill attention + temporal smoothing of action-decode attention as a plug-and-play **inference-time** method. Focus is efficiency, not regularization. **Not a direct competitor** to CTM's training-time regularization framing.

- **LightVLA** (arXiv:2509.12594, ICRA 2026): Differentiable token pruning using Gumbel softmax for adaptive token selection during **training**. Reduces FLOPs by 59% with 2.9% improvement in success rate. This is closer to CTM since it modifies training, though framed as efficiency rather than regularization.

- **VLA-IAP** (arXiv:2603.22991, Mar 2026): Training-free visual token pruning via interaction alignment. Inference-time only. Not a competitor.

- **"See What Matters" / GridS** (ICML 2026): Differentiable grid sample pruning for "generalizable" VLA. This paper explicitly connects token pruning to **generalization**, not just efficiency. Uses continuous resampling of visual tokens. Published at a top venue. **Potentially a close competitor** if CTM's story is that token reduction improves generalization.

- **ETA-VLA** (arXiv:2603.25766): Temporal fusion + intra-LLM sparsification. Focused on autonomous driving VLAs. Efficiency-focused.

- **SP-VLA** (arXiv:2506.12723): Joint model scheduling and token pruning. Efficiency-focused.

- **SpecPrune-VLA** (OpenReview): Action-aware self-speculative pruning. Efficiency-focused.

**Key gap CTM could exploit:** Most of these papers frame token reduction as an **efficiency** problem. CTM's framing of token masking as an explicit **regularization** strategy grounded in the information bottleneck principle is relatively novel in the VLA space.

---

## 2. VLA Robustness / Generalization Recent Work

**CRITICAL FINDING -- "Rethinking VLA Model Scaling" (arXiv:2602.09722, Feb 2026):** This paper by Wang et al. **directly tested sensory dropout** (stochastically masking visual inputs and proprioception during training with p=0.2) as a regularization technique for VLA scaling. Their finding: **sensory dropout HURT performance**. Disabling visual dropout increased success rates from 84.5% to 85.6%. They conclude "the natural diversity of the pre-training corpus already serves as an effective regularizer." **This is a direct challenge to the CTM premise** and must be addressed in the paper. The CTM paper needs to explain why its approach differs (e.g., counterfactual design, targeted rather than random masking, different training regime, finetuning vs. pretraining context).

Other relevant generalization work:
- **"What Can RL Bring to VLA Generalization?"** (arXiv:2505.19789): RL finetuning (PPO) enhances VLA generalization, especially in execution and semantics.
- **VLA-RFT** (ICLR 2026): Reinforcement finetuning with world model simulators.
- **"Robust Finetuning via Parameter Merging"** (arXiv:2512.08333, Yadav et al., Berkeley): Weight interpolation between pretrained and finetuned checkpoints. No token masking -- purely weight-space. Uses LIBERO and real-world. **Close competitor** in the "robust finetuning" framing.
- **"Boosting VLA Finetuning with Feasible Action Neighborhood Prior"** (arXiv:2604.01570, Apr 2026): KL-divergence regularizer on action distributions using Gaussian priors. Tested on LIBERO and ManiSkill. **Close competitor** in the "regularization during finetuning" framing.

---

## 3. Information Bottleneck in Robotics / VLA

- **CRAFT** (arXiv:2602.12532, Feb 2026): This paper uses a **variational information bottleneck (VIB)** after the vision-language encoder in a VLA, with KL regularization that initially suppresses vision/language signals to force reliance on force modality, then gradually anneals the bottleneck. **This is the closest IB-based competitor** -- it literally applies an information bottleneck to VLA finetuning, though for a different purpose (contact-rich manipulation, not generalization per se).

- **RL Token (RLT)** (arXiv:2604.23073, Physical Intelligence, Apr 2026): Creates an explicit information bottleneck by compressing VLA embeddings into a single "RL token" via an encoder-decoder transformer. The bottleneck forces the token to retain all task-relevant information. Different goal (enabling efficient online RL) but uses the same theoretical motivation.

- **Variational IB for Meta-RL** (Sensors 2023): Older work applying IB to meta-reinforcement learning for robot skill transfer. Improves sample efficiency 200-5000x.

- **IBTM** (OpenReview): Information Bottleneck inspired Token Merging for vision transformers. Not VLA-specific but theoretically adjacent.

**Assessment:** CRAFT is the paper CTM needs to cite and differentiate from most carefully in the IB space. CRAFT uses IB to modulate modality influence; CTM (presumably) uses masking to create an IB that improves visual generalization.

---

## 4. VLA-Pruner (Detailed)

Confirmed: VLA-Pruner (arXiv:2511.16449) is a **plug-and-play inference-time** token pruning method. It does NOT modify training. Its dual-level criterion (semantic + action importance) is designed for computational efficiency during deployment. **It is NOT a close competitor** to CTM's training-time regularization approach, though CTM should cite it in the related work section on token reduction in VLAs.

---

## 5. LIBERO-Plus Benchmark

**Confirmed to exist.** LIBERO-Plus (arXiv:2510.13626) is a robustness benchmark with 10,030 tasks spanning 7 perturbation dimensions (object layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise) with 5 difficulty levels. It appeared as a **CVPR 2026 poster**. GitHub: `github.com/sylvestf/LIBERO-plus`. It is integrated into HuggingFace LeRobot. This is a legitimate and increasingly standard benchmark for VLA robustness evaluation.

---

## 6. SimplerEnv Visual Variants

**Confirmed to exist and is standard.** SimplerEnv (CoRL 2024) provides two evaluation setups:
- **Visual Matching**: sim visuals closely match real training data (in-distribution)
- **Variant Aggregation**: averages across OOD backgrounds, lightings, distractors, table textures, camera poses (out-of-distribution generalization test)

It evaluates on Google Robot and WidowX+Bridge setups. This is widely used in VLA papers (Gen-VLA, TraceVLA, OpenVLA, etc.) and is considered a standard benchmark.

---

## 7. CRL-VLA (arXiv:2602.03445)

**Confirmed to exist.** CRL-VLA: "Continual Vision-Language-Action Learning" by Zeng et al., submitted Feb 3, 2026. It addresses the stability-plasticity tradeoff in continual RL finetuning of VLAs using Goal-Conditioned Value Formulation with a dual-critic architecture. This is about continual learning, not regularization per se, so it is tangentially related but not a direct competitor.

---

## 8. VLM2VLA / Actions as Language

**Confirmed to exist at ICLR 2026.** "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting" by Hancock, Wu, Zha, Russakovsky, and Majumdar (Princeton). The method represents robot actions as natural language strings and uses LoRA to minimize backbone modification. It preserves VLM capabilities (85%+ retention on 12 multimodal benchmarks) and enables zero-shot generalization. Available on OpenReview (`openreview.net/forum?id=sFO9d6XSlf`).

---

## 9. Gen-VLA (arXiv:2509.11417)

**Confirmed to exist.** "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" by Grover, Gopalkrishnan, Ai, Christensen, Su, and Li (UC San Diego / Hillbot). Uses: (1) dual-encoder with one frozen encoder, (2) string-based action tokenizer, (3) co-training with VL datasets. Evaluates on **SimplerEnv** (both Visual Matching and Variant Aggregation). Does NOT use token masking. **Close competitor** in the generalization-through-representation-preservation space.

---

## 10. Recent Concurrent Work (Feb-May 2026)

Several important papers the CTM idea should be aware of:

- **Gaze-Regularized VLA** (arXiv:2603.23202, Mar 2026): Uses KL divergence to align transformer attention with human gaze distributions. 4-12% improvements on LIBERO. A different regularization approach but in the same "regularize VLA attention" space.

- **RS-CL / Contrastive Representation Regularization** (arXiv:2510.01711): Robot State-aware Contrastive Loss that aligns VLM representations with proprioceptive states. Uses "view cutoff" (randomly masking feature slices for observation views) -- this is somewhat related to token masking. Evaluated on LIBERO and RoboCasa.

- **"Don't Blind Your VLA"** (arXiv:2510.25616): Identifies attention sink, representation collapse, and domain forgetting during VLA SFT. Proposes Visual Representation Alignment using a frozen teacher with cosine similarity. Evaluated on SimplerEnv. Diagnoses the same problem (VLA representations degrade during finetuning) but proposes a different solution.

- **Knowledge Insulation** (arXiv:2505.23705, Physical Intelligence, NeurIPS 2025): Insulates VLM backbone by not propagating action expert gradients. Trains with discrete FAST tokens for representation quality while using flow matching for continuous actions. Addresses the same root problem of representation degradation during finetuning.

- **VLA-GSE** (arXiv:2605.06175, May 2026): Parameter-efficient finetuning with generalized and specialized expert modules. Very recent.

---

## Summary of Competitive Threats

**Highest threat (must address explicitly):**

1. **"Rethinking VLA Model Scaling" (arXiv:2602.09722)** -- Directly tested sensory dropout in VLA training and found it **hurts performance**. The CTM paper must explain why its approach is different (counterfactual design, finetuning vs. pretraining, targeted vs. random, etc.).

2. **CRAFT (arXiv:2602.12532)** -- Already uses a variational information bottleneck in VLA finetuning. Different application (force-modality focus) but same theoretical framework.

3. **"See What Matters" / GridS (ICML 2026)** -- Connects token pruning to VLA generalization, not just efficiency.

**Medium threat (should cite and differentiate):**

4. **LightVLA** -- Differentiable token pruning during training.
5. **Gen-VLA** -- Preservation-based generalization approach.
6. **"Don't Blind Your VLA"** -- Same problem diagnosis (representation degradation during SFT).
7. **Parameter Merging (arXiv:2512.08333)** -- Competing robust finetuning approach.
8. **FAN Prior (arXiv:2604.01570)** -- Competing regularization-during-finetuning approach.
9. **RS-CL (arXiv:2510.01711)** -- View masking + contrastive regularization.
10. **Knowledge Insulation (NeurIPS 2025)** -- Competing approach to preventing representation degradation.

**Lower threat (cite in related work):**
- VLA-Pruner, VLA-IAP, ETA-VLA, SP-VLA (all inference-time efficiency)
- VLM2VLA, CRL-VLA (different problems: forgetting, continual learning)
- Gaze-Regularized VLA (different regularization signal)

Sources:
- [VLA-Pruner](https://arxiv.org/abs/2511.16449)
- [LightVLA](https://arxiv.org/abs/2509.12594)
- [VLA-IAP](https://arxiv.org/abs/2603.22991)
- [See What Matters / GridS (ICML 2026)](https://icml.cc/virtual/2026/poster/65010)
- [Rethinking VLA Model Scaling](https://arxiv.org/html/2602.09722)
- [Robust Finetuning via Parameter Merging](https://arxiv.org/abs/2512.08333)
- [FAN Prior for VLA Finetuning](https://arxiv.org/html/2604.01570v1)
- [CRAFT: Force-Aware Curriculum Fine-tuning](https://arxiv.org/abs/2602.12532)
- [RL Token](https://arxiv.org/abs/2604.23073)
- [LIBERO-Plus](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus CVPR 2026](https://cvpr.thecvf.com/virtual/2026/poster/38735)
- [SimplerEnv GitHub](https://github.com/simpler-env/SimplerEnv)
- [CRL-VLA](https://arxiv.org/abs/2602.03445)
- [VLM2VLA / Actions as Language](https://arxiv.org/abs/2509.22195)
- [VLM2VLA OpenReview (ICLR 2026)](https://openreview.net/forum?id=sFO9d6XSlf)
- [Gen-VLA](https://arxiv.org/abs/2509.11417)
- [Gen-VLA Project Page](https://gen-vla.github.io/)
- [Gaze-Regularized VLA](https://arxiv.org/html/2603.23202v1)
- [RS-CL / Contrastive Representation Regularization](https://arxiv.org/html/2510.01711v1)
- [Don't Blind Your VLA](https://arxiv.org/abs/2510.25616)
- [Knowledge Insulation (Physical Intelligence)](https://arxiv.org/abs/2505.23705)
- [VLA-GSE](https://arxiv.org/html/2605.06175v1)
- [ETA-VLA](https://arxiv.org/abs/2603.25766)
- [What Can RL Bring to VLA Generalization](https://arxiv.org/abs/2505.19789)
- [VLA-RFT (ICLR 2026)](https://openreview.net/forum?id=Jaut99EHeu)
- [ICLR 2026 VLA Survey Blog](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
- [VLA-Cache](https://arxiv.org/html/2502.02175v2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68217126-269a-4470-b9d7-ff197c9050ff",
  "isSidechain": true,
  "agentId": "a6466d84670312cd2",
  "requestId": "req_011Cayxa4Gm5D7Umketfh1yf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9668e236-89a3-489f-94a2-ac46fcd04f3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tn6mgK5RUtkW2ChYkeXDRL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3148,
      "cache_read_input_tokens": 41984,
      "output_tokens": 4032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3148
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4032,
          "cache_read_input_tokens": 41984,
          "cache_creation_input_tokens": 3148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3148,
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
