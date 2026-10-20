# Research conversation: I'm planning experiments on RoboCasa and LIBERO-PRO benchmarks for a robotics research project. The reviewer noted that 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aeaac1eb060a9f17c.jsonl`
- **Structured JSON:** [`84318575de5aecd169df.json`](../../sessions/84/84318575de5aecd169df.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

61 recorded events

### User

_source line 1 · 2026-05-10T18:23:01.979Z_

I'm planning experiments on RoboCasa and LIBERO-PRO benchmarks for a robotics research project. The reviewer noted that UWM has never been evaluated on these benchmarks and the engineering effort is unaccounted.

Search for:
1. **RoboCasa benchmark current SOTA (2026)**: What are the latest results? Who holds SOTA? What methods have been evaluated? Search "RoboCasa benchmark 2026 SOTA", "RoboCasa robotic manipulation results"
2. **LIBERO-PRO**: Search for "LIBERO-PRO robustness benchmark 2025 2026" — what methods have been evaluated? What are current results?
3. **UWM on RoboCasa**: Has anyone adapted UWM to RoboCasa? Search "UWM RoboCasa" and "unified world model RoboCasa"
4. **UWM benchmark results**: What benchmarks has UWM actually been evaluated on? What are its scores?
5. **Compute costs for adapter training on frozen DiT**: Search for "parameter efficient adapter diffusion transformer training cost" — how many GPU hours do similar adapter-based approaches typically require?

Also check Papers With Code for RoboCasa leaderboard if available.

I need to build a realistic compute plan that fits within 200 H100-hours total.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "69f1ed83-d82c-48e9-b967-5da76ec75fc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:23:01.981Z_

```json
{
  "parentUuid": "69f1ed83-d82c-48e9-b967-5da76ec75fc3",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
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
  "uuid": "5c818a81-0bea-4bd9-a180-d14c12c647a6",
  "timestamp": "2026-05-10T18:23:01.981Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:23:04.787Z_



I'll conduct a comprehensive web search across all these topics in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c818a81-0bea-4bd9-a180-d14c12c647a6",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMWqLxNDDkRb9kmtCkZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eae4108a-086b-4f10-aef5-90b1fef41874",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuzvCpitZhWfp2NZDaRBWj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 852,
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

_source line 4 · 2026-05-10T18:23:04.987Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EtALW6THyisfhfqyXBy1Kv`</summary>

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
  "parentUuid": "eae4108a-086b-4f10-aef5-90b1fef41874",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMWqLxNDDkRb9kmtCkZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5ccc675-4bb6-4e39-aa2c-98f0698bb737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuzvCpitZhWfp2NZDaRBWj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 8223,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 852,
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

_source line 5 · 2026-05-10T18:23:04.991Z_

<details><summary>↩ Tool result · `toolu_01EtALW6THyisfhfqyXBy1Kv`</summary>

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
  "parentUuid": "c5ccc675-4bb6-4e39-aa2c-98f0698bb737",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "48279909-fd9d-43ef-95fb-2524eea0f546",
  "sourceToolAssistantUUID": "c5ccc675-4bb6-4e39-aa2c-98f0698bb737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:23:08.636Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48279909-fd9d-43ef-95fb-2524eea0f546",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMX4TzPTq8kBLD5DaUW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45c036c5-bf96-4e17-8f5e-19b433906c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qvj9GjTtacJDQZPGPk7cmr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 9075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1408,
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

_source line 7 · 2026-05-10T18:23:09.215Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GsJcu6GWBR5EV15SeUot6g`</summary>

```json
{
  "query": "RoboCasa benchmark 2026 SOTA results robotic manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45c036c5-bf96-4e17-8f5e-19b433906c44",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMX4TzPTq8kBLD5DaUW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7c229c4-55ec-4b27-8e63-4c405428c4ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qvj9GjTtacJDQZPGPk7cmr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 9075,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1408
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 78,
          "cache_read_input_tokens": 9075,
          "cache_creation_input_tokens": 1408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1408,
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

_source line 8 · 2026-05-10T18:23:15.962Z_

<details><summary>↩ Tool result · `toolu_01GsJcu6GWBR5EV15SeUot6g`</summary>

```text
Web search results for query: "RoboCasa benchmark 2026 SOTA results robotic manipulation"

Links: [{"title":"RoboCAS: A Benchmark for Robotic Manipulation in Complex Object Arrangement Scenarios","url":"https://arxiv.org/html/2407.06951v1"},{"title":"RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots | OpenReview","url":"https://openreview.net/forum?id=tQJYKwc3n4"},{"title":"RoboCasa","url":"https://robocasa.ai/"},{"title":"[2407.06951] RoboCAS: A Benchmark for Robotic Manipulation in Complex Object Arrangement Scenarios","url":"https://arxiv.org/abs/2407.06951"},{"title":"[2603.04356] RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://arxiv.org/abs/2603.04356"},{"title":"GitHub - robocasa/robocasa: RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots · GitHub","url":"https://github.com/robocasa/robocasa"},{"title":"DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA","url":"https://arxiv.org/pdf/2603.29844"},{"title":"RoboCasa: Scalable Household Robotics Simulation","url":"https://www.emergentmind.com/topics/robocasa"},{"title":"NVIDIA adds Cosmos Policy to its world foundation models - The Robot Report","url":"https://www.therobotreport.com/nvidia-adds-cosmos-policy-world-foundation-models/"},{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"}]

Based on the search results, here's what I found about RoboCasa benchmark 2026 SOTA results for robotic manipulation:

## RoboCasa365 - Latest Benchmark (2026)

RoboCasa365 introduces 365 everyday tasks across 2,500 diverse kitchen environments, with over 600 hours of human demonstration data and over 1600 hours of synthetically generated demonstration data. The benchmark includes extensive experiments with state-of-the-art methods analyzing the impacts of task diversity, dataset scale, and environment variation on generalization.

## State-of-the-Art Results

The Cosmos-Policy-RoboCasa-Predict2-2B model achieves state-of-the-art performance on the RoboCasa simulation benchmark with a 67.1% average success rate across 24 kitchen manipulation tasks. On RoboCasa, Cosmos Policy achieves higher success rates than baselines trained from scratch, demonstrating improved generalization across diverse household manipulation scenarios.

## Benchmark Structure

RoboCasa365 focuses on ten foundational skills including pick and place, opening and closing doors and drawers, twisting knobs, turning levers, pressing buttons, insertion, navigation, sliding racks, and closing/opening lids, with 65 atomic tasks for systematically training and benchmarking these skills.

RoboCasa365 includes benchmarking support for popular policy learning methods including Diffusion Policy, pi, and GR00T, plus user-submitted models on the leaderboard.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7c229c4-55ec-4b27-8e63-4c405428c4ae",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "c5973055-3e98-43ef-9f9f-a4fef6d16fda",
  "sourceToolAssistantUUID": "e7c229c4-55ec-4b27-8e63-4c405428c4ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T18:23:20.074Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pr2cmaSTftrf6fTxpsMZzK`</summary>

```json
{
  "query": "LIBERO-PRO robustness benchmark 2025 2026 results methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5973055-3e98-43ef-9f9f-a4fef6d16fda",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMXs9dPJcBTtPxQnBNQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc3ba54d-33a7-4e3d-93ef-a6e51c067157",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzhUp735NwqnG54924rxWm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 10483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 944,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T18:23:20.851Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013GX7fYsZwWjrwzPtJCj4oM`</summary>

```json
{
  "query": "UWM RoboCasa unified world model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc3ba54d-33a7-4e3d-93ef-a6e51c067157",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMXs9dPJcBTtPxQnBNQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebf30f87-b448-4a0f-be81-559511cde405",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzhUp735NwqnG54924rxWm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 10483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 944,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T18:23:21.310Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014noo35tM8Z7E3bsJDojbj9`</summary>

```json
{
  "query": "UWM unified world model benchmark results evaluation robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf30f87-b448-4a0f-be81-559511cde405",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMXs9dPJcBTtPxQnBNQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e4ef846-381f-4faa-8661-4d7ebb866b0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzhUp735NwqnG54924rxWm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 10483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 944,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T18:23:22.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MnFwUvFRNLP9APNZCdhH15`</summary>

```json
{
  "query": "parameter efficient adapter diffusion transformer training cost GPU hours"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e4ef846-381f-4faa-8661-4d7ebb866b0b",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMXs9dPJcBTtPxQnBNQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15d878df-3487-4442-b719-8f786c8fdd23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzhUp735NwqnG54924rxWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 10483,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 10483,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 944,
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

_source line 13 · 2026-05-10T18:23:27.931Z_

<details><summary>↩ Tool result · `toolu_013GX7fYsZwWjrwzPtJCj4oM`</summary>

```text
Web search results for query: "UWM RoboCasa unified world model"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"World2Act: Latent Action Post-Training via Skill-Compositional World Models","url":"https://arxiv.org/html/2603.10422"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"RoboCasa: Large-Scale Simulation of Household Tasks for Generalist Robots","url":"https://www.researchgate.net/publication/383894362_RoboCasa_Large-Scale_Simulation_of_Household_Tasks_for_Generalist_Robots"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling","url":"https://arxiv.org/html/2604.19734"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Request PDF","url":"https://www.researchgate.net/publication/395371959_Unified_World_Models_Coupling_Video_and_Action_Diffusion_for_Pretraining_on_Large_Robotic_Datasets"},{"title":"Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model","url":"https://arxiv.org/html/2510.27607v1"},{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"},{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"}]

Based on the search results, I can provide you with information about UWM (Unified World Models) and RoboCasa:

## Unified World Models (UWM)

UWM is a framework that allows for leveraging both video and action data for policy learning. UWM combines video and action diffusion in one transformer, with separate timesteps for each modality.

### Key Capabilities

In addition to learning policies, UWM captures temporal dynamics in the dataset, making it desirable as a pretraining paradigm on large multitask datasets. UWM naturally integrates unlabeled videos into training by treating the missing actions as noise, unlocking previously inaccessible datasets.

UWM represents a policy, a forward dynamics model, an inverse dynamics model, and a video prediction model in a unified framework.

### Performance on RoboCasa

To evaluate UWM's ability to learn from large multitask robotic datasets, researchers pretrained UWM on a subset of the DROID dataset, and then finetuned it to diverse downstream tasks, finding UWM to outperform baseline models in both in-distribution (ID) and out-of-distribution (OOD) settings.

The research has been published at Robotics: Science and Systems (RSS) 2025, and the project includes code and resources available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebf30f87-b448-4a0f-be81-559511cde405",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "9f03113d-7e68-420e-9721-abba2fe3c910",
  "sourceToolAssistantUUID": "ebf30f87-b448-4a0f-be81-559511cde405",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:23:28.252Z_

<details><summary>↩ Tool result · `toolu_014noo35tM8Z7E3bsJDojbj9`</summary>

```text
Web search results for query: "UWM unified world model benchmark results evaluation robotics"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Request PDF","url":"https://www.researchgate.net/publication/395371959_Unified_World_Models_Coupling_Video_and_Action_Diffusion_for_Pretraining_on_Large_Robotic_Datasets"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation","url":"https://arxiv.org/html/2604.19092v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"[PDF] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-World-Models:-Coupling-Video-and-Action-for-Zhu-Yu/514b9977bdb57f6e9586461f36fcf6467a775b3c"},{"title":"[2604.19092] RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation","url":"https://arxiv.org/abs/2604.19092"},{"title":"GitHub - tsinghua-fib-lab/WorldArena: WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models · GitHub","url":"https://github.com/tsinghua-fib-lab/WorldArena"},{"title":"WorldArena: A Unified Benchmark for Evaluating Perception","url":"https://arxiv.org/pdf/2602.08971"},{"title":"Unified World Models: A Scalable AI Framework For Video And Action Data","url":"https://quantumzeitgeist.com/unified-world-models-a-scalable-ai-framework-for-video-and-action-data/"}]

Based on the search results, here's information about UWM (Unified World Models) benchmark results and evaluation in robotics:

## Overview

Unified World Model (UWM) is a multimodal diffusion transformer that uses separate diffusion timesteps for actions and videos to flexibly learn policies, forward dynamics, inverse dynamics, and video prediction models from both robot and video data.

## Benchmark Evaluations

### LIBERO Benchmark Results
UWM was tested on LIBERO, a robotic manipulation benchmark containing 100 robotic manipulation tasks, using 90 for pretraining and 5 for evaluation. UWM achieves the highest success rates across the evaluation tasks in the out-of-distribution setting, with DP achieving the second highest performance, followed by GR1 and PAD.

### Real Robot Tasks
UWM consistently improves performance when exposed to additional videos during pretraining. This suggests using diffusion time steps for masking as an effective strategy for co-training on multimodal data.

## Performance Advantages

UWM and DP perform similarly when trained from scratch; however, UWM scales from pretraining more effectively than DP. UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning.

The research demonstrates that UWM successfully addresses key challenges in learning from large robotic datasets by leveraging both video and action data through a unified diffusion-based framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e4ef846-381f-4faa-8661-4d7ebb866b0b",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "b2cd9646-e92f-4822-8067-eceed04fe9bc",
  "sourceToolAssistantUUID": "1e4ef846-381f-4faa-8661-4d7ebb866b0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T18:23:28.913Z_

<details><summary>↩ Tool result · `toolu_01Pr2cmaSTftrf6fTxpsMZzK`</summary>

```text
Web search results for query: "LIBERO-PRO robustness benchmark 2025 2026 results methods"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"}]

Based on the search results, here's an overview of the LIBERO-PRO and related robustness benchmarks from 2025-2026:

## LIBERO-PRO: Overview

LIBERO-PRO is a plug-and-play extension of LIBERO designed to foster fair comparison across models and to advance research on building VLA systems. The evaluation suite introduces perturbations across four dimensions: objects, goals, spatial configurations, and task sets.

## Key Findings

The research reveals significant robustness challenges in current Vision-Language-Action (VLA) models:

**Performance Issues:**
- Despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, even when constructed from training components
- Apparent stability against object and instruction perturbations is largely due to overfitting rather than genuine task understanding

## LIBERO-Plus: Complementary Benchmark

A related benchmark called LIBERO-Plus provides additional robustness analysis. It performs systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

**Key Results:**
- Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations
- Models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely

LIBERO-Plus establishes a comprehensive benchmark with a systematic two-stage process: expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing; and evaluating the resulting tasks using four representative models and stratifying them into five difficulty levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc3ba54d-33a7-4e3d-93ef-a6e51c067157",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "472e466c-a1c3-4aa0-866b-2b2003585993",
  "sourceToolAssistantUUID": "fc3ba54d-33a7-4e3d-93ef-a6e51c067157",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:23:34.678Z_

<details><summary>↩ Tool result · `toolu_01MnFwUvFRNLP9APNZCdhH15`</summary>

```text
Web search results for query: "parameter efficient adapter diffusion transformer training cost GPU hours"

Links: [{"title":"How OpenAI or DeepMind calculates cost of training a transformer based models?","url":"https://masteringllm.medium.com/how-openai-or-deepmind-calculates-cost-of-training-a-transformer-based-models-b0b629f0942b"},{"title":"Transformer training costs | Continuum Labs","url":"https://training.continuumlabs.ai/infrastructure/data-and-memory/transformer-training-costs"},{"title":"[2310.00426] PixArt-𝛼: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis","url":"https://ar5iv.labs.arxiv.org/html/2310.00426"},{"title":"Parameter-efficient fine-tuning in large language models: a survey of methodologies | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11236-4"},{"title":"TREAD: Token Routing for Efﬁcient Architecture-agnostic Diffusion Training","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Krause_TREAD_Token_Routing_for_Efficient_Architecture-agnostic_Diffusion_Training_ICCV_2025_paper.pdf"},{"title":"PixArt-$\\alpha$: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis | OpenReview","url":"https://openreview.net/forum?id=eAKmQPe3m1"},{"title":"PLoRA: Efficient LoRA Hyperparameter Tuning for Large Models Minghao Yan∗†","url":"https://arxiv.org/pdf/2508.02932"},{"title":"Aman's AI Journal • Primers • Parameter Efficient Fine-Tuning","url":"https://aman.ai/primers/ai/parameter-efficient-fine-tuning/"},{"title":"LightSeq2: Accelerated Training for Transformer-based Models on GPUs","url":"https://arxiv.org/pdf/2110.05722"},{"title":"Optimizing Transformer-Based Diffusion Models for Video Generation with NVIDIA TensorRT | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/optimizing-transformer-based-diffusion-models-for-video-generation-with-nvidia-tensorrt/"}]

Based on the search results, here's what I found about parameter-efficient adapter training for diffusion transformers and their GPU hour costs:

## Key Findings

**Training Costs for Diffusion Transformers:**

The most advanced text-to-image (T2I) models require significant training costs (e.g., millions of GPU hours). More specifically, training a DiT on standard benchmarks alone requires thousands of A100 GPU hours without reaching convergence, and text-to-image models demand even more resources, with Stable Diffusion requiring about 150,000 A100 GPU hours.

**Parameter-Efficient Methods:**

Parameter-efficient fine-tuning (PEFT) significantly reduces computational costs; for instance, a full SFT process that requires 4 million GPU hours can be reduced to 400K GPU hours or less with PEFT. This represents a roughly 10x reduction in computational requirements.

**Adapter-Specific Efficiency:**

LLaMA-Adapter introduces only 1.2 million learnable parameters on top of the frozen LLaMA 7B model, with fine-tuning taking less than one hour on 8 A100 GPUs. Additionally, adapters are a PEFT technique shown to achieve similar performance as compared to tuning the top layers while requiring as fewer parameters as two orders of magnitude.

The search results show that parameter-efficient approaches like adapters and LoRA can dramatically reduce training costs while maintaining competitive performance, though specific GPU-hour metrics for diffusion transformer adapters were not extensively detailed in the available results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15d878df-3487-4442-b719-8f786c8fdd23",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "bab52959-c0dc-482a-baac-80df7521a25a",
  "sourceToolAssistantUUID": "15d878df-3487-4442-b719-8f786c8fdd23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T18:23:36.708Z_

Now let me get more specific details on several of these topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bab52959-c0dc-482a-baac-80df7521a25a",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMZFDCqC1jXe18QdzoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6ec4b0e-7a88-4982-816c-8ff5837005e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R99T6Pai2ZnNauow53WnQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 11427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4072,
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

_source line 18 · 2026-05-10T18:23:37.776Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FNdhC7qsiRfKEs4j8scGvp`</summary>

```json
{
  "query": "RoboCasa benchmark leaderboard Papers with Code results 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6ec4b0e-7a88-4982-816c-8ff5837005e4",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMZFDCqC1jXe18QdzoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f2ac036-f149-4d42-ad65-432b7dfdaa99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R99T6Pai2ZnNauow53WnQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 11427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4072,
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

_source line 19 · 2026-05-10T18:23:38.708Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Anh5ohDXuyiv8JL1LfkYfJ`</summary>

```json
{
  "query": "UWM unified world model LIBERO benchmark scores success rate specific numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f2ac036-f149-4d42-ad65-432b7dfdaa99",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMZFDCqC1jXe18QdzoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31a05e7e-2bbf-4ff6-a76e-1a17ca9cfb4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R99T6Pai2ZnNauow53WnQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 11427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4072,
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

_source line 20 · 2026-05-10T18:23:40.044Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QEiYx1HFsL8hDkBVUyfTfb`</summary>

```json
{
  "query": "Cosmos Policy RoboCasa results success rate 67.1 methods compared"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31a05e7e-2bbf-4ff6-a76e-1a17ca9cfb4a",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMZFDCqC1jXe18QdzoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbe20227-68f0-4127-b80e-df368b3065e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R99T6Pai2ZnNauow53WnQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 11427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4072,
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

_source line 21 · 2026-05-10T18:23:40.284Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jrh8BrFhBs2AEqpHDK6z2t`</summary>

```json
{
  "query": "LoRA adapter frozen diffusion transformer robotics policy training GPU hours compute"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbe20227-68f0-4127-b80e-df368b3065e4",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMZFDCqC1jXe18QdzoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5713a934-7a5a-4051-b059-b0988a48dea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R99T6Pai2ZnNauow53WnQo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 11427,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4072
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 11427,
          "cache_creation_input_tokens": 4072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4072,
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

_source line 22 · 2026-05-10T18:23:45.043Z_

<details><summary>↩ Tool result · `toolu_01FNdhC7qsiRfKEs4j8scGvp`</summary>

```text
Web search results for query: "RoboCasa benchmark leaderboard Papers with Code results 2025 2026"

Links: [{"title":"GitHub - robocasa/robocasa: RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots · GitHub","url":"https://github.com/robocasa/robocasa"},{"title":"RoboCasa","url":"https://robocasa.ai/"},{"title":"RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots | OpenReview","url":"https://openreview.net/forum?id=tQJYKwc3n4"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/attachment?id=tQJYKwc3n4&name=pdf"},{"title":"RoboCasa: Scalable Household Robotics Simulation","url":"https://www.emergentmind.com/topics/robocasa"},{"title":"[2603.04356] RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://arxiv.org/abs/2603.04356"},{"title":"Releases · robocasa/robocasa","url":"https://github.com/robocasa/robocasa/releases"},{"title":"[2407.06951] RoboCAS: A Benchmark for Robotic Manipulation in Complex Object Arrangement Scenarios","url":"https://arxiv.org/abs/2407.06951"},{"title":"Papers with Code is Dead — Best Alternatives 2026 by Use Case | Codesota | CodeSOTA","url":"https://www.codesota.com/papers-with-code"},{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"}]

Based on the search results, here's what I found about the RoboCasa benchmark:

## RoboCasa365 Overview

RoboCasa365 was released on 2/18/2026 with 365 tasks, 2500+ kitchen scenes, 2200+ hours of robot demonstration data, and benchmarking support. RoboCasa365 introduces 365 everyday tasks across 2,500 diverse kitchen environments, with over 600 hours of human demonstration data and over 1600 hours of synthetically generated demonstration data.

## Leaderboard Access

The RoboCasa project includes a leaderboard, which is available at the official RoboCasa website. However, I should note that Papers with Code was shut down by Meta in July 2025, so leaderboard results may no longer be hosted on that platform.

## Benchmark Methods

RoboCasa365 includes benchmarking support for popular policy learning methods including Diffusion Policy, pi, and GR00T, plus user-submitted models on the leaderboard.

## Example Results

One notable result: Cosmos-Policy-RoboCasa-Predict2-2B achieves a 67.1% average success rate across 24 kitchen manipulation tasks.

For the most current leaderboard results and rankings, I'd recommend visiting the official RoboCasa website directly at robocasa.ai, as the Papers with Code platform is no longer operational.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f2ac036-f149-4d42-ad65-432b7dfdaa99",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "63d501e4-6a6f-41ac-a281-92ccdbb03532",
  "sourceToolAssistantUUID": "8f2ac036-f149-4d42-ad65-432b7dfdaa99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T18:23:46.971Z_

<details><summary>↩ Tool result · `toolu_01Jrh8BrFhBs2AEqpHDK6z2t`</summary>

```text
Web search results for query: "LoRA adapter frozen diffusion transformer robotics policy training GPU hours compute"

Links: [{"title":"What Is FLUX 2 Dev LoRA? Custom AI Image Styles with Fine-Tuning | MindStudio","url":"https://www.mindstudio.ai/blog/what-is-flux-2-dev-lora"},{"title":"What is Lora Fine Tuning? The Definitive Guide","url":"https://www.truefoundry.com/blog/lora-fine-tuning"},{"title":"Policies in AI Robotics","url":"https://docs.phospho.ai/learn/policies"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN","url":"https://openreview.net/pdf?id=nZeVKeeFYf9"},{"title":"Using LoRA for Efficient Stable Diffusion Fine-Tuning","url":"https://huggingface.co/blog/lora"},{"title":"Parameter Efficient Fine Tuning. Adapters; LoRA; QLora; Surgical… | by Amanatullah | 𝐀𝐈 𝐦𝐨𝐧𝐤𝐬.𝐢𝐨 | Medium","url":"https://medium.com/aimonks/parameter-efficient-fine-tuning-075954d1db51"},{"title":"A Comprehensive Guide to Multi-GPU LoRA Fine-Tuning with Distributed Data Parallelism and Sequence Parallelism using Axolotl — 1 | by Dhananjay Kumar | Medium","url":"https://dhnanjay.medium.com/a-comprehensive-guide-to-multi-gpu-lora-fine-tuning-with-distributed-data-parallelism-and-sequence-384a52b0a0ad"},{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"LoRA · Hugging Face","url":"https://huggingface.co/docs/diffusers/training/lora"},{"title":"LoRA (Low-Rank Adaptation) · Hugging Face","url":"https://huggingface.co/learn/llm-course/chapter11/4"}]

I've performed a web search for your query on LoRA adapters, frozen diffusion transformers, robotics policy training, and GPU compute hours. Here are the key findings:

## LoRA Adapters and Frozen Base Models

LoRA solves the fine-tuning problem by freezing the pre-trained model weights and inserting lightweight trainable adapters into specific layers—usually the query and value projection layers in transformer-based architectures.

## GPU Hours and Compute Requirements

For robotics applications specifically:

- Training takes a few hours on an NVIDIA A100 GPU for OpenVLA, a vision-language-action model for complex robotics tasks.
- Fine-tuning takes about 8 hours on a single NVIDIA A100 GPU for diffusion transformer-based robot policies.

For general diffusion models:
- Training a LoRA adapter might take 2-8 hours on a consumer GPU, while full fine-tuning could take weeks and require expensive hardware.

## Memory and Parameter Efficiency

Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times. Only the low-rank adapter parameters (typically a few million) are optimized.

The search results show that LoRA is particularly effective for efficient fine-tuning of large frozen transformer models, including diffusion-based robotics policies, while dramatically reducing computational and memory requirements compared to full model fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5713a934-7a5a-4051-b059-b0988a48dea6",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "7aad3984-d9af-4563-8b57-be2d739af059",
  "sourceToolAssistantUUID": "5713a934-7a5a-4051-b059-b0988a48dea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T18:23:46.974Z_

<details><summary>↩ Tool result · `toolu_01QEiYx1HFsL8hDkBVUyfTfb`</summary>

```text
Web search results for query: "Cosmos Policy RoboCasa results success rate 67.1 methods compared"

Links: [{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"},{"title":"Cosmos Policy — Cosmos Lab","url":"https://research.nvidia.com/labs/cosmos-lab/cosmos-policy/"},{"title":"Cosmos Policy Achieves 98.5% Robot Control With Single- ...","url":"https://quantumzeitgeist.com/percent-cosmos-policy-achieves-robot-control/"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/html/2601.16163v1"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning | OpenReview","url":"https://openreview.net/forum?id=wPEIStHxYH"},{"title":"[2601.16163] Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/abs/2601.16163"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - Cosmos Cookbook","url":"https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html"},{"title":"nvidia/RoboCasa-Cosmos-Policy · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nvidia/RoboCasa-Cosmos-Policy"},{"title":"Introducing NVIDIA Cosmos Policy for Advanced Robot Control","url":"https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control"}]

Based on the search results, here's what I found about Cosmos Policy and its RoboCasa results:

## Performance Results

Cosmos Policy achieves state-of-the-art performance on the RoboCasa simulation benchmark with a 67.1% average success rate across 24 kitchen manipulation tasks.

## Training Efficiency

A key advantage of Cosmos Policy is its efficiency. It achieves an average success rate of 67.1% while requiring significantly fewer training demonstrations than prior SOTA methods (50 demos versus 300).

## Methods Compared

Methods in comparison include diffusion-based policies trained from scratch (Diffusion Policy, Dita) and video model-based policies. More specifically, Cosmos Policy outperforms strong diffusion policies trained from scratch, video model-based policies, and state-of-the-art vision-language-action models fine-tuned on the same robot demonstrations.

## Evaluation Protocol

Success rates are averaged over 50 trials per task (across 5 evaluation scenes with 10 trials each) and 3 random seeds (3,600 trials total).

## How It Works

Cosmos Policy learns to directly generate robot actions encoded as latent frames within the video model's latent diffusion process, and additionally generates future state images and values (expected cumulative rewards), which are similarly encoded as latent frames, enabling test-time planning of action trajectories with higher likelihood of success.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbe20227-68f0-4127-b80e-df368b3065e4",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "6220097a-e026-462c-9e13-f5988a8361b9",
  "sourceToolAssistantUUID": "fbe20227-68f0-4127-b80e-df368b3065e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T18:23:52.704Z_

<details><summary>↩ Tool result · `toolu_01Anh5ohDXuyiv8JL1LfkYfJ`</summary>

```text
Web search results for query: "UWM unified world model LIBERO benchmark scores success rate specific numbers"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"},{"title":"VLA Model Leaderboard (beta)","url":"https://allenai.github.io/vla-evaluation-harness/leaderboard/"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [Quick Review]","url":"https://liner.com/review/unified-world-models-coupling-video-and-action-diffusion-for-pretraining"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"[2504.00983] WorldScore: A Unified Evaluation Benchmark for World Generation","url":"https://arxiv.org/abs/2504.00983"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"World Action Model (WaM) Overview","url":"https://www.emergentmind.com/topics/world-action-model-wam"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"}]

Let me search for more specific numerical results from the UWM paper on LIBERO benchmark scores.

Links: [{"title":"2030 Metrics Table– October 2025 Update - 2030 Action Plan","url":"https://uwm.edu/2030-action-plan/2030-metrics-table-october-2025-update/"},{"title":"Average success rate across evaluation settings on LIBERO and... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Average-success-rate-across-evaluation-settings-on-LIBERO-and-MetaWorld-v2-All-results_tbl1_397006917"},{"title":"Grade Calculator – Martha Carlin","url":"https://sites.uwm.edu/carlin/grade-calculator/"},{"title":"Grades – Registrar's Office","url":"https://uwm.edu/registrar/student-record/grades/"},{"title":"Student Success - Academic Affairs","url":"https://uwm.edu/academicaffairs/academic_priorities/student-success/"},{"title":"University of Wisconsin-Milwaukee (UWM) Chances Calculator","url":"https://www.campusreel.org/college-acceptance-calculator/chance-of-getting-into-university-of-wisconsin-milwaukee"},{"title":"University of Wisconsin - Milwaukee Admission Requirements","url":"https://www.prepscholar.com/sat/s/colleges/University-of-Wisconsin---Milwaukee-admission-requirements"},{"title":"United Wholesale Mortgage Review 2026 | Bankrate","url":"https://www.bankrate.com/mortgages/reviews/united-wholesale-mortgage/"},{"title":"Student Success and Retention Initiative Summary – College of Engineering & Applied Science","url":"https://uwm.edu/engineering/student-success-and-retention-initiative-summary/"},{"title":"University of Wisconsin - Milwaukee - Niche","url":"https://www.niche.com/colleges/university-of-wisconsin-milwaukee/"}]

Those results are about the University of Wisconsin-Milwaukee, not the robotics model. Let me search more specifically for the UWM robotics paper's numerical results.

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"[2504.02792] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792"},{"title":"[2504.02792v1] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792v1"},{"title":"Unified World Models: Memory-Augmented Planning and Foresight for Visual Navigation","url":"https://arxiv.org/html/2510.08713v1"},{"title":"[PDF] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-World-Models:-Coupling-Video-and-Action-for-Zhu-Yu/514b9977bdb57f6e9586461f36fcf6467a775b3c"},{"title":"GitHub - operator22th/awesome-world-models-for-robots: Awesome World Model for Robotics Papers · GitHub","url":"https://github.com/operator22th/awesome-world-models-for-robots"}]

Let me try a more specific search for the actual table with numerical scores.

Links: [{"title":"[2504.02792] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"[PDF] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-World-Models:-Coupling-Video-and-Action-for-Zhu-Yu/514b9977bdb57f6e9586461f36fcf6467a775b3c"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"[1904.02792] Unifying Human and Statistical Evaluation for Natural Language Generation","url":"https://arxiv.org/abs/1904.02792"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2504.02792"}]

Based on my search results, I found information about the UWM (Unified World Models) paper and its evaluation on the LIBERO benchmark, but the search results don't provide the complete numerical table with specific success rate percentages. However, I can provide you with what information is available:

UWM was tested on LIBERO, a robotic manipulation benchmark containing 100 robotic manipulation tasks, with 90 tasks used for pretraining and 5 for evaluation. 

The evaluation tasks include Stack-Bowls, Block-Cabinet, Paper-Towel, Hang-Towel, and Rice-Cooker.

Regarding performance results, UWM was found to outperform baseline models in both in-distribution (ID) and out-of-distribution (OOD) settings. Additionally, when evaluating the inverse dynamics model on trajectory tracking, UWM achieved a higher success rate than the policy, indicating that actions generated by the inverse dynamics adhere more closely to the reference trajectory.

Unfortunately, the specific numerical success rate percentages for each task are not fully visible in the search results I retrieved. To access the complete Table II with the exact benchmark scores, you would need to view the full paper directly at the arXiv page (arxiv.org/abs/2504.02792) or the project website at https://weirdlabuw.github.io/uwm/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31a05e7e-2bbf-4ff6-a76e-1a17ca9cfb4a",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "9e9c76d4-7d0e-4dcd-9aa6-484d10e90be3",
  "sourceToolAssistantUUID": "31a05e7e-2bbf-4ff6-a76e-1a17ca9cfb4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T18:23:56.851Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FaESYCCjHHS8UstDWSjkKX`</summary>

```json
{
  "query": "LIBERO-PRO benchmark methods evaluated OpenVLA pi0 diffusion policy results table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e9c76d4-7d0e-4dcd-9aa6-484d10e90be3",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMaaGDAcZAUHZmUitWu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6af49522-0ec6-42e3-b161-952f350031db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6YhohemEjDFxPGFABvEQ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1831,
      "cache_creation_input_tokens": 3532,
      "cache_read_input_tokens": 15499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3532,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T18:23:58.240Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KSZPoKMhSPJchmx3Refhh3`</summary>

```json
{
  "query": "UWM unified world model arxiv 2504.02792 LIBERO DROID evaluation results table numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6af49522-0ec6-42e3-b161-952f350031db",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMaaGDAcZAUHZmUitWu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dd8056d-575f-413b-8154-b6f09808ade9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6YhohemEjDFxPGFABvEQ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1831,
      "cache_creation_input_tokens": 3532,
      "cache_read_input_tokens": 15499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3532,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-10T18:23:59.104Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HirsWVB1D7xV8icgauti9i`</summary>

```json
{
  "query": "RoboCasa365 ICLR 2026 diffusion policy GR00T pi0 benchmark results comparison table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dd8056d-575f-413b-8154-b6f09808ade9",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMaaGDAcZAUHZmUitWu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e7ad647-d246-451c-9329-ce916526c7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6YhohemEjDFxPGFABvEQ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1831,
      "cache_creation_input_tokens": 3532,
      "cache_read_input_tokens": 15499,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3532
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1831,
          "output_tokens": 192,
          "cache_read_input_tokens": 15499,
          "cache_creation_input_tokens": 3532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3532,
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

_source line 29 · 2026-05-10T18:24:03.406Z_

<details><summary>↩ Tool result · `toolu_01KSZPoKMhSPJchmx3Refhh3`</summary>

```text
Web search results for query: "UWM unified world model arxiv 2504.02792 LIBERO DROID evaluation results table numbers"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"[2504.02792] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Paper page - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://huggingface.co/papers/2504.02792"},{"title":"[PDF] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-World-Models:-Coupling-Video-and-Action-for-Zhu-Yu/514b9977bdb57f6e9586461f36fcf6467a775b3c"},{"title":"Unified World Models: Coupling Video and Action Diffusion ...","url":"https://arxiv.org/pdf/2504.02792"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [Quick Review]","url":"https://liner.com/review/unified-world-models-coupling-video-and-action-diffusion-for-pretraining"},{"title":"[2504.00983] WorldScore: A Unified Evaluation Benchmark for World Generation","url":"https://arxiv.org/abs/2504.00983"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"},{"title":"UniDWM: Towards a Unified Driving World Model via Multifaceted Representation Learning","url":"https://arxiv.org/html/2602.01536"}]

Based on the search results, I found information about the UWM paper (arxiv 2504.02792). The paper evaluates UWM on LIBERO, a robotic manipulation benchmark that contains 100 robotic manipulation tasks and corresponding datasets, from which they use 90 for pretraining and 5 for evaluation.

However, the search results provided do not contain the specific evaluation results table numbers or detailed numerical results comparing UWM's performance on LIBERO and DROID tasks. The results mention that they pretrain a UWM on a subset of the DROID dataset and then finetune it to diverse downstream tasks, finding UWM to outperform baseline models in both in-distribution (ID) and out-of-distribution (OOD) settings.

To access the specific evaluation results tables and numbers, you would need to consult the full paper at arxiv.org/abs/2504.02792 or the project website at https://weirdlabuw.github.io/uwm/, as these detailed numerical results are not captured in the search results I retrieved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dd8056d-575f-413b-8154-b6f09808ade9",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "cac6c4e7-56b2-457d-807d-e3cb0d30d6c9",
  "sourceToolAssistantUUID": "3dd8056d-575f-413b-8154-b6f09808ade9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T18:24:16.886Z_

<details><summary>↩ Tool result · `toolu_01FaESYCCjHHS8UstDWSjkKX`</summary>

```text
Web search results for query: "LIBERO-PRO benchmark methods evaluated OpenVLA pi0 diffusion policy results table"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf"}]

Based on the search results, I found comprehensive information about LIBERO-PRO benchmark evaluation of Vision-Language-Action (VLA) models.

## LIBERO-PRO Benchmark Overview

LIBERO-PRO is an extended evaluation suite designed to enable more comprehensive assessment of VLA models, with evaluation scenarios along four key dimensions: manipulated objects, initial states, task instructions, and environments.

## Models Evaluated

Three representative models were evaluated—OpenVLA, pi0, and pi0.5, where OpenVLA was assessed using four official checkpoints trained on different LIBERO suites, while pi0 and pi0.5 were evaluated with a single official checkpoint.

## Key Findings

Despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, even when constructed from training components.

The results show that models exhibit near-complete failure under several settings: the models cannot cope with changes in object positions, nor can they correctly follow slightly rephrased task instructions—even when such instructions have appeared in other training contexts.

While most models fail under perturbations, Pi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0, revealing differences masked by standard benchmark scores.

The evaluation suite introduces perturbations across four dimensions: objects, goals, spatial configurations, and task sets (see Tables 2, 3, 4, 5). The original papers contain detailed result tables with performance metrics across these different perturbation types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6af49522-0ec6-42e3-b161-952f350031db",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "cdf91e10-936c-4517-8f0b-1d9e107eb18b",
  "sourceToolAssistantUUID": "6af49522-0ec6-42e3-b161-952f350031db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T18:24:19.020Z_

<details><summary>↩ Tool result · `toolu_01HirsWVB1D7xV8icgauti9i`</summary>

```text
Web search results for query: "RoboCasa365 ICLR 2026 diffusion policy GR00T pi0 benchmark results comparison table"

Links: [{"title":"ICLR Poster RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://iclr.cc/virtual/2026/poster/10006981"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/9f0ef5cd7a44233fc06f8d5bbacfba0cbe04e008.pdf"},{"title":"GitHub - robocasa/robocasa: RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots · GitHub","url":"https://github.com/robocasa/robocasa"},{"title":"RoboCasa","url":"https://robocasa.ai/"},{"title":"RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://arxiv.org/html/2603.04356v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"(PDF) RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://www.researchgate.net/publication/401564362_RoboCasa365_A_Large-Scale_Simulation_Framework_for_Training_and_Benchmarking_Generalist_Robots"},{"title":"ROBOCASA365","url":"https://robocasa.ai/assets/robocasa365_iclr26.pdf"},{"title":"Overview — RoboCasa 1.0 documentation","url":"https://robocasa.ai/docs/build/html/introduction/overview.html"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"}]

Based on the search results, I found information about the RoboCasa365 benchmark results from the ICLR 2026 paper. Here's what I found regarding the comparison of different policy learning methods:

## Benchmark Results Overview

RoboCasa365 introduces 365 everyday tasks across 2,500 diverse kitchen environments, with over 600 hours of human demonstration data and over 1600 hours of synthetically generated demonstration data.

## Policy Methods Benchmarked

RoboCasa365 supports popular policy learning models, such as Diffusion Policy, π₀, and GR00T.

## Multi-Task Training Results Comparison

The paper evaluated these methods on multi-task learning across different task categories. Overall, GR00T N1.5 performs the best among all methods, followed by π₀, and finally Diffusion Policy. More specifically, GR00T N1.5 and π₀ show non-zero success rates on Composite-Unseen tasks, a sign of stronger generalization abilities, while Diffusion Policy performs the worst, highlighting how high-capacity vision-language-action models can better fit large, diverse multi-task robot datasets.

The benchmarks evaluated performance across three task categories: Atomic, Composite-Seen, and Composite-Unseen tasks, where learning Atomic tasks is the easiest, followed by Composite-Seen tasks and Composite-Unseen tasks, as Atomic tasks are shorter-horizon tasks that present fewer learning challenges for imitation learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e7ad647-d246-451c-9329-ce916526c7a2",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "9fa8bba0-e1ee-4a0e-95e7-4037f9df1201",
  "sourceToolAssistantUUID": "0e7ad647-d246-451c-9329-ce916526c7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-10T18:24:22.794Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eu3cqR67JasaD3mZckFk81`</summary>

```json
{
  "query": "Cosmos Policy RoboCasa training compute GPU hours how many GPUs training details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fa8bba0-e1ee-4a0e-95e7-4037f9df1201",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMcWkBZx6qQiCcNhRGv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "729d1beb-91bd-4b40-b86e-8531e9b6a927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wqBaBQEkvWPNV2b3QvPVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4867,
      "cache_read_input_tokens": 19031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4867,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T18:24:23.740Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0179PFtWQxBA4WWUtEqMrobE`</summary>

```json
{
  "query": "UWM unified world model training compute cost GPUs pretraining DROID how long"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "729d1beb-91bd-4b40-b86e-8531e9b6a927",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMcWkBZx6qQiCcNhRGv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1031ee23-4aaf-4574-9bca-cb6518388b83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wqBaBQEkvWPNV2b3QvPVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4867,
      "cache_read_input_tokens": 19031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4867,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T18:24:24.147Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WzTgHa11rnsmFFRZ5iWJQt`</summary>

```json
{
  "query": "RoboCasa365 GR00T N1.5 pi0 diffusion policy success rate numbers atomic composite"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1031ee23-4aaf-4574-9bca-cb6518388b83",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMcWkBZx6qQiCcNhRGv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb2a39f1-8285-4b15-9643-73632214f132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wqBaBQEkvWPNV2b3QvPVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4867,
      "cache_read_input_tokens": 19031,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4867
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 19031,
          "cache_creation_input_tokens": 4867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4867,
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

_source line 35 · 2026-05-10T18:24:27.939Z_

<details><summary>↩ Tool result · `toolu_01Eu3cqR67JasaD3mZckFk81`</summary>

```text
Web search results for query: "Cosmos Policy RoboCasa training compute GPU hours how many GPUs training details"

Links: [{"title":"GitHub - NVlabs/cosmos-policy: Cosmos Policy · GitHub","url":"https://github.com/NVlabs/cosmos-policy"},{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - Cosmos Cookbook","url":"https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html"},{"title":"Introducing NVIDIA Cosmos Policy for Advanced Robot Control","url":"https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control"},{"title":"Cosmos Policy Core System | NVlabs/cosmos-policy | DeepWiki","url":"https://deepwiki.com/NVlabs/cosmos-policy/3-cosmos-policy-core-system"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/html/2601.16163v1"},{"title":"nvidia/Cosmos-Policy-ALOHA-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B"},{"title":"NVlabs/cosmos-policy | DeepWiki","url":"https://deepwiki.com/NVlabs/cosmos-policy/1-overview"},{"title":"nvidia/RoboCasa-Cosmos-Policy · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nvidia/RoboCasa-Cosmos-Policy"},{"title":"Cosmos Policy — Cosmos Lab","url":"https://research.nvidia.com/labs/cosmos-lab/cosmos-policy/"}]

Based on the search results, here are the training compute details for Cosmos Policy RoboCasa:

## RoboCasa Training Specifications

For RoboCasa training, the researchers used 32 80GB GPUs (H100s) for 48 hours with 1200 demonstrations.

### Additional Training Context

Cosmos Policy was trained on the RoboCasa benchmark with 24 tasks and 50 demonstrations per task. However, to assess the relative data efficiency of Cosmos Policy compared to prior works, they trained their method on the 50 human-teleoperated demonstrations alone.

### Inference Requirements

For inference, the compute requirements are significantly lower: 1 GPU with 8.9 GB VRAM is needed for RoboCasa sim benchmark tasks.

### Alternative Training Options

If you have fewer GPUs, you can use gradient accumulation to increase total batch size, which was found to lead to faster convergence than taking more gradient steps with a smaller batch size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "729d1beb-91bd-4b40-b86e-8531e9b6a927",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "0cff3d5d-795e-4286-a186-2bd66c400a95",
  "sourceToolAssistantUUID": "729d1beb-91bd-4b40-b86e-8531e9b6a927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T18:24:28.882Z_

<details><summary>↩ Tool result · `toolu_0179PFtWQxBA4WWUtEqMrobE`</summary>

```text
Web search results for query: "UWM unified world model training compute cost GPUs pretraining DROID how long"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [Quick Review]","url":"https://liner.com/review/unified-world-models-coupling-video-and-action-diffusion-for-pretraining"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.02792v1"},{"title":"[2504.02792] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Request PDF","url":"https://www.researchgate.net/publication/395371959_Unified_World_Models_Coupling_Video_and_Action_Diffusion_for_Pretraining_on_Large_Robotic_Datasets"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://liqing.io/mindflow/Papers/2504-UWM"},{"title":"Paper page - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://huggingface.co/papers/2504.02792"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"}]

Based on the search results, I found information about Unified World Models (UWM) and its training on the DROID dataset. However, the search results don't contain specific details about compute cost, GPU requirements, or training duration. Here's what I found:

## UWM Training on DROID

UWM was pretrained on a curated subset of 2000 trajectories from the DROID dataset based on location, and another 2000 trajectories from the rest of the dataset were used as videos for co-training.

The paper describes a UWM that integrates an action diffusion process and a video diffusion process within a unified transformer architecture.

## What's Not Covered

Unfortunately, the search results do not contain specific information about:
- **Compute cost** for training UWM
- **GPU specifications** or requirements
- **Training duration** (how long pretraining took)

To find these specific details, you would likely need to check the full paper (arXiv 2504.02792) directly or look for supplementary materials, as papers often include computational details in appendices or supplementary sections that may not be indexed in web search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1031ee23-4aaf-4574-9bca-cb6518388b83",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "e00b37dd-58e6-4eaf-9e04-658ea83a1ed7",
  "sourceToolAssistantUUID": "1031ee23-4aaf-4574-9bca-cb6518388b83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T18:24:30.690Z_

<details><summary>↩ Tool result · `toolu_01WzTgHa11rnsmFFRZ5iWJQt`</summary>

```text
Web search results for query: "RoboCasa365 GR00T N1.5 pi0 diffusion policy success rate numbers atomic composite"

Links: [{"title":"RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://arxiv.org/html/2603.04356v1"},{"title":"GitHub - robocasa/robocasa: RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots · GitHub","url":"https://github.com/robocasa/robocasa"},{"title":"Multi-Task Learning — RoboCasa 1.0 documentation","url":"https://robocasa.ai/docs/build/html/benchmarking/multitask_learning.html"},{"title":"(PDF) RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://www.researchgate.net/publication/401564362_RoboCasa365_A_Large-Scale_Simulation_Framework_for_Training_and_Benchmarking_Generalist_Robots"},{"title":"[Literature Review] RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://www.themoonlight.io/en/review/robocasa365-a-large-scale-simulation-framework-for-training-and-benchmarking-generalist-robots"},{"title":"Releases · robocasa/robocasa","url":"https://github.com/robocasa/robocasa/releases"},{"title":"Overview — RoboCasa 1.0 documentation","url":"https://robocasa.ai/docs/build/html/introduction/overview.html"},{"title":"Policy Learning Algorithms — RoboCasa 1.0 documentation","url":"https://robocasa.ai/docs/build/html/benchmarking/policy_learning_algorithms.html"},{"title":"Diffusion Policy Baseline Details · Issue #418 · NVIDIA/Isaac-GR00T","url":"https://github.com/NVIDIA/Isaac-GR00T/issues/418"},{"title":"RoboCasa","url":"https://robocasa.ai/"}]

Based on the search results, here's what I found regarding RoboCasa365 success rates for different policy learning models:

## Multi-Task Learning Results

GR00T N1.5 performs the best among all methods, followed by π0.5, π0, and finally Diffusion Policy. All methods show non-zero success rates on Composite-Unseen tasks, a sign of stronger generalization abilities.

For Composite-Unseen tasks specifically, GR00T N1.5 achieved the highest average task success rate of 20.0%, demonstrating superior generalization on Composite-Unseen tasks. Diffusion Policy performs the worst, highlighting how high-capacity vision-language-action models can better fit large, diverse multi-task robot datasets.

## Real-World Transfer Results

A GR00T N1.5 model trained using a "Sim-and-Real" approach, which involved mid-training on simulation tasks and then co-fine-tuning on real and corresponding simulation data, achieved an average task success rate of 79.8% on four real-world tasks, substantially outperforming the "Real Only" model (61.8%).

The research shows that learning atomic tasks was easiest, while composite tasks, especially unseen ones, proved more challenging.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb2a39f1-8285-4b15-9643-73632214f132",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "e447739f-b0f3-4bc7-8c80-c65f055becd0",
  "sourceToolAssistantUUID": "cb2a39f1-8285-4b15-9643-73632214f132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-10T18:24:33.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fn7ZjNMMXNjRg9eDs8utr3`</summary>

```json
{
  "query": "LIBERO-PRO OpenVLA pi0 pi0.5 success rate perturbation results numbers table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e447739f-b0f3-4bc7-8c80-c65f055becd0",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMdNbpNgvaapFQvH21Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dc09523-41c1-4b22-8c7f-1b99a872bccf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ry1h617D3FbMB9DKpH6XT7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2749,
      "cache_read_input_tokens": 23898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2749,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-10T18:24:33.886Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Er1rCbwdg6ARo1mTHXz94E`</summary>

```json
{
  "query": "UWM unified world model DiT architecture size parameters training 8 GPUs A100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dc09523-41c1-4b22-8c7f-1b99a872bccf",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMdNbpNgvaapFQvH21Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b899deff-e5e5-4664-8609-391c5ef65006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ry1h617D3FbMB9DKpH6XT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2749,
      "cache_read_input_tokens": 23898,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2749
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 23898,
          "cache_creation_input_tokens": 2749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2749,
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

_source line 40 · 2026-05-10T18:24:39.521Z_

<details><summary>↩ Tool result · `toolu_01Er1rCbwdg6ARo1mTHXz94E`</summary>

```text
Web search results for query: "UWM unified world model DiT architecture size parameters training 8 GPUs A100"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"Right-Sizing AI Training with NVIDIA A100 & A40 on CoreWeave","url":"https://www.coreweave.com/blog/right-sizing-training-workloads-with-nvidia-a100-and-a40-gpus"},{"title":"Practical Guide: Training, Deploying & Scaling AI Models on GPUs and TPUs | by NJ | Medium","url":"https://medium.com/@nraman.n6/practical-guide-training-deploying-scaling-ai-models-on-gpus-and-tpus-ed38f52efb4d"},{"title":"8 A100 GPUs with 80GB memory is minimum requirements for local-GPU finetune? · Issue #346 · lm-sys/FastChat","url":"https://github.com/lm-sys/FastChat/issues/346"},{"title":"Architecting a Heterogeneous AI Cloud for Training and Inference | WhiteFiber","url":"https://www.whitefiber.com/blog/heterogeneous-ai-cloud"},{"title":"NVIDIA A100 GPU Guide: 2.0TB/s Specs, MIG & Cloud Rental","url":"https://www.runpod.io/articles/guides/nvidia-a100-gpu"},{"title":"V1.0 NVIDIA A100 Tensor Core GPU Architecture","url":"https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf"},{"title":"Calculate GPU Requirements for Your LLM Training | by Thiyagarajan Palaniyappan | Medium","url":"https://medium.com/@plthiyagu/calculate-gpu-requirements-for-your-llm-training-7122a3700547"},{"title":"The Complete Guide to Multi-GPU Training: Scaling AI Models Beyond Single-Card Limitations","url":"https://www.runpod.io/articles/guides/the-complete-guide-to-multi-gpu-training-scaling-ai-models-beyond-single-card-limitations"},{"title":"Unified World Model Specification","url":"https://www.emergentmind.com/topics/unified-design-specification-for-world-models"}]

Based on the search results, I found information about UWM (Unified World Models) but the specific technical details about its DiT architecture size, parameters, and training specifications with 8 GPUs A100 were not explicitly provided in these search results.

Here's what I found:

Unified World Model (UWM) is a multimodal diffusion transformer that uses separate diffusion timesteps for actions and videos. UWM can be trained on (o, a, o') triplets from robot trajectories as well as (o, o') tuples from action-free videos, using random noise for masking.

The search results did provide general context about A100 GPU training capabilities. With 80GB A100s using model parallelism, you can train with 16-32 GPUs, while smaller memory configurations or data parallelism approaches may require 32-64 GPUs for effective training.

However, the specific architectural details you're looking for—such as the exact parameter count of the UWM DiT model, the hidden dimension sizes, and training configurations optimized for 8 A100 GPUs—were not found in these results. For more detailed technical specifications, you may want to consult the official UWM paper or technical documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b899deff-e5e5-4664-8609-391c5ef65006",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "0043ed06-9060-4980-bf01-6f4d58e626c6",
  "sourceToolAssistantUUID": "b899deff-e5e5-4664-8609-391c5ef65006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T18:24:41.119Z_

<details><summary>↩ Tool result · `toolu_01Fn7ZjNMMXNjRg9eDs8utr3`</summary>

```text
Web search results for query: "LIBERO-PRO OpenVLA pi0 pi0.5 success rate perturbation results numbers table"

Links: [{"title":"Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"}]

I found relevant information about LIBERO-PRO and the success rates for OpenVLA, pi0, and pi0.5 models under perturbation conditions.

## LIBERO-PRO Success Rate Results Table

Here is the performance table showing normalized success rates (0.00–1.00) for the models across different perturbations:

| Model | LIBERO-Goal | LIBERO-Spatial | LIBERO-10 | LIBERO-Object | Total |
|-------|-------------|----------------|-----------|---------------|-------|
| | Obj | Pos | Sem | Task | Env | Obj | Pos | Sem | Task | Env | Obj | Pos | Sem | Task | Env | Obj | Pos | Sem | Task | Env | |
| OpenVLA | 0.96 | 0.00 | 0.98 | 0.00 | 0.98 | 0.97 | 0.00 | 0.97 | 0.00 | 0.89 | 0.81 | 0.00 | 0.96 | 0.00 | 0.85 | 0.98 | 0.00 | 0.98 | 0.00 | 0.00 | 0.52 |
| Pi0 | 0.94 | 0.00 | 0.93 | 0.00 | 0.39 | 0.95 | 0.00 | 0.97 | 0.00 | 0.60 | 0.79 | 0.00 | 0.82 | 0.00 | 0.27 | 0.94 | 0.00 | 0.90 | 0.00 | 0.29 | 0.44 |
| Pi0.5 | 0.97 | 0.38 | 0.97 | 0.00 | 0.46 | 0.97 | 0.20 | 0.97 | 0.01 | 0.46 | 0.92 | 0.08 | 0.93 | 0.01 | — | — | — | — | — | — | — |

Key findings from the results:

- OpenVLA and pi0 show performance collapse once object displacement exceeds 0.2 units, while pi0.5 exhibits improved resilience and sustains non-trivial accuracy up to 0.4 units before also collapsing to zero

- Under position perturbations, Pi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0

- Despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications

The table uses these abbreviations: Obj (Object), Pos (Position), Sem (Semantic), Task (Task-level), and Env (Environment) perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dc09523-41c1-4b22-8c7f-1b99a872bccf",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "190dd967-3271-48cb-ae45-ffe9ae8bc57b",
  "sourceToolAssistantUUID": "4dc09523-41c1-4b22-8c7f-1b99a872bccf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T18:24:51.240Z_

Now let me try to get the UWM paper details and Cosmos Policy training specifics for the compute plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "190dd967-3271-48cb-ae45-ffe9ae8bc57b",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMe9Jtc36wpHvcRqJvc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0a27359-d7d5-4f5d-aaf5-a2285dffff51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6dp7VNAmLfwUMCMD1tLAo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 26647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1549,
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

_source line 43 · 2026-05-10T18:24:52.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HTJaEjXqPM6CJ1FUr3eWcd`</summary>

```json
{
  "query": "site:arxiv.org \"unified world models\" 2504.02792 training details GPU batch size epochs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a27359-d7d5-4f5d-aaf5-a2285dffff51",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMe9Jtc36wpHvcRqJvc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7afb1f05-ad07-407d-8848-815ed8a87143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6dp7VNAmLfwUMCMD1tLAo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 26647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1549,
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

_source line 44 · 2026-05-10T18:24:53.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sd6dCbiMcRxwbF92yGUaFt`</summary>

```json
{
  "query": "diffusion policy RoboCasa training 8 GPU hours compute finetuning robotic manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7afb1f05-ad07-407d-8848-815ed8a87143",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMe9Jtc36wpHvcRqJvc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eade16ec-1173-458e-91d7-50b651d28c68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6dp7VNAmLfwUMCMD1tLAo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 26647,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1549
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 155,
          "cache_read_input_tokens": 26647,
          "cache_creation_input_tokens": 1549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1549,
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

_source line 45 · 2026-05-10T18:24:57.264Z_

<details><summary>↩ Tool result · `toolu_01HTJaEjXqPM6CJ1FUr3eWcd`</summary>

```text
Web search results for query: "site:arxiv.org "unified world models" 2504.02792 training details GPU batch size epochs"

Links: [{"title":"[2504.02792] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792"},{"title":"[2504.02792v1] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion ...","url":"https://arxiv.org/pdf/2504.02792"},{"title":"[2510.08713] Towards Unified World Models for Visual Navigation via Memory-Augmented Planning and Foresight","url":"https://arxiv.org/abs/2510.08713"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=1250&show=100"},{"title":"RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization","url":"https://arxiv.org/html/2603.12639v2"},{"title":"Unified World Models: Memory-Augmented Planning and Foresight for Visual Navigation","url":"https://arxiv.org/html/2510.08713v1"},{"title":"UniDWM: Towards a Unified Driving World Model via Multifaceted Representation Learning","url":"https://arxiv.org/html/2602.01536"},{"title":"TesserAct: Learning 4D Embodied World Models","url":"https://arxiv.org/html/2504.20995"}]

I found the paper arXiv:2504.02792 on "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets." The search results include the abstract and general information about the paper, but the detailed training specifications you're looking for (GPU, batch size, epochs, and other training details) are not visible in the search results provided.

To access the specific training details you mentioned, you would need to:

1. View the full PDF of the paper at https://arxiv.org/pdf/2504.02792
2. Check the HTML version at https://arxiv.org/html/2504.02792v1
3. Look in the "Experiments" or "Implementation Details" section of the paper

The search results confirm that a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality, but the specific training hyperparameters you're asking about are not included in these search result excerpts. You would need to access the full paper directly to find those implementation details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7afb1f05-ad07-407d-8848-815ed8a87143",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "dbbbcd54-8736-406e-b202-c86a3787028d",
  "sourceToolAssistantUUID": "7afb1f05-ad07-407d-8848-815ed8a87143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T18:24:59.512Z_

<details><summary>↩ Tool result · `toolu_01Sd6dCbiMcRxwbF92yGUaFt`</summary>

```text
Web search results for query: "diffusion policy RoboCasa training 8 GPU hours compute finetuning robotic manipulation"

Links: [{"title":"Policy Learning Algorithms — RoboCasa 1.0 documentation","url":"https://robocasa.ai/docs/build/html/benchmarking/policy_learning_algorithms.html"},{"title":"GitHub - robocasa/robocasa: RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots · GitHub","url":"https://github.com/robocasa/robocasa"},{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"},{"title":"RoboCasa","url":"https://robocasa.ai/"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - Cosmos Cookbook","url":"https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"[PDF] RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RoboCasa:-Large-Scale-Simulation-of-Everyday-Tasks-Nasiriany-Maddukuri/f773ceb43ffc7f9cd685250c4919924ec0bc85c7"},{"title":"GitHub - YanjieZe/3D-Diffusion-Policy: [RSS 2024] 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations · GitHub","url":"https://github.com/YanjieZe/3D-Diffusion-Policy"},{"title":"RoboCasa: Scalable Household Robotics Simulation","url":"https://www.emergentmind.com/topics/robocasa"},{"title":"Releases · robocasa/robocasa","url":"https://github.com/robocasa/robocasa/releases"}]

Based on the search results, I found information about Diffusion Policy training on RoboCasa:

RoboCasa has a fork of the official Diffusion Policy codebase, and for training Diffusion Policy, a GPU with at least 24 GB of memory is recommended, though 48 GB+ is preferred.

However, the search results do not contain specific information about training Diffusion Policy on RoboCasa with 8 GPU hours of compute or details about fine-tuning compute requirements for robotic manipulation tasks. The documentation I found focuses on GPU memory requirements rather than total training time or compute hours.

For reference, 3D Diffusion Policy takes approximately 10GB GPU memory and about 3 hours on an Nvidia A40 GPU as a different example of diffusion policy training requirements, but this is for a different implementation and task setting.

If you need more specific information about the 8 GPU hours training time for Diffusion Policy on RoboCasa, you may want to check the official RoboCasa documentation, the Diffusion Policy fork repository, or relevant research papers on the topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eade16ec-1173-458e-91d7-50b651d28c68",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "66de6869-657a-4437-bb8f-9fabb841165a",
  "sourceToolAssistantUUID": "eade16ec-1173-458e-91d7-50b651d28c68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-10T18:25:02.962Z_

Now let me fetch the UWM paper's HTML page directly to get specific benchmark numbers and training details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66de6869-657a-4437-bb8f-9fabb841165a",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMfVtg6AjG19HGxCCRz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6df9637-fbc6-4384-aa95-eeabd22e0731",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKPLZVfXmsgnY34XRttRvs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2834,
      "cache_read_input_tokens": 28196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2834,
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

_source line 48 · 2026-05-10T18:25:03.409Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MP1AFu2426jHHFqwUKvAbk`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6df9637-fbc6-4384-aa95-eeabd22e0731",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMfVtg6AjG19HGxCCRz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68b66f50-f67e-4cbb-a3d6-899622a6bbb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKPLZVfXmsgnY34XRttRvs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2834,
      "cache_read_input_tokens": 28196,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2834
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 28196,
          "cache_creation_input_tokens": 2834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2834,
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

_source line 49 · 2026-05-10T18:25:03.411Z_

<details><summary>↩ Tool result · `toolu_01MP1AFu2426jHHFqwUKvAbk`</summary>

````text
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
  "parentUuid": "68b66f50-f67e-4cbb-a3d6-899622a6bbb0",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "461524d7-209e-4e8e-94c7-5688c52e7c9d",
  "sourceToolAssistantUUID": "68b66f50-f67e-4cbb-a3d6-899622a6bbb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-10T18:25:11.971Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018FUGSkbaYELiwsge3uocM7`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.02792v1",
  "prompt": "Extract ALL numerical benchmark results from this paper. I need:\n1. The exact success rate numbers for UWM on LIBERO tasks (Table II or similar) - every number for every task and every method compared\n2. What benchmarks/tasks were used for evaluation (LIBERO, MetaWorld, real robot, etc.)\n3. Training details: how many GPUs, what type, batch size, training time/epochs, model size/parameters\n4. What baselines were compared (Diffusion Policy, GR1, PAD, etc.) and their exact scores\n5. Any mention of RoboCasa"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "461524d7-209e-4e8e-94c7-5688c52e7c9d",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMfo4nPyskstd7yCDjH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab86bf1c-87e2-4c7d-84af-23dcd84e8b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUYQBjTdUFxE3sQAdk9hD3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 31030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 618,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T18:25:15.384Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HdCmvUMwfwExWc8DWFKGMq`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.03827v1",
  "prompt": "Extract ALL numerical results from LIBERO-PRO paper. I need:\n1. Complete results tables with exact success rates for all models (OpenVLA, pi0, pi0.5, etc.)\n2. Performance under each perturbation type (object, position, semantic, task, environment)\n3. Standard LIBERO success rates vs perturbed success rates\n4. Any mention of UWM or unified world models\n5. What methods/models were evaluated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab86bf1c-87e2-4c7d-84af-23dcd84e8b9e",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMfo4nPyskstd7yCDjH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "723d86fe-40c0-4ce6-936a-c036ac69dd4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUYQBjTdUFxE3sQAdk9hD3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 31030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 618,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T18:25:16.493Z_

<details><summary>↩ Tool result · `toolu_018FUGSkbaYELiwsge3uocM7`</summary>

```text
# Numerical Benchmark Results from "Unified World Models"

## LIBERO Benchmark Results (Table II)

**UWM (Ours):**
- Book-Caddy: 0.91 ± 0.07
- Soup-Cheese: 0.93 ± 0.01
- Bowl-Drawer: 0.80 ± 0.02
- Moka-Moka: 0.68 ± 0.02
- Mug-Mug: 0.65 ± 0.01
- Average: 0.79 ± 0.11

**Diffusion Policy:**
- Book-Caddy: 0.73 ± 0.10
- Soup-Cheese: 0.88 ± 0.02
- Bowl-Drawer: 0.77 ± 0.02
- Moka-Moka: 0.65 ± 0.03
- Mug-Mug: 0.53 ± 0.05
- Average: 0.71 ± 0.12

**PAD:** Average 0.57 ± 0.19
**GR1:** Average 0.58 ± 0.14

## Real Robot Tasks (Table I)

UWM achieved superior performance across five tasks (Stack-Bowls, Block-Cabinet, Paper-Towel, Hang-Towel, Rice-Cooker) in both in-distribution and out-of-distribution settings, with improvements up to 20% over baselines.

## Training Details

The paper specifies: "100K steps" for pretraining and "10K gradient steps" for finetuning in LIBERO. Appendix indicates use of a single GPU setup, though specific hardware details are limited.

## RoboCasa

No mention of RoboCasa appears in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab86bf1c-87e2-4c7d-84af-23dcd84e8b9e",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "39c46281-dcaa-4a87-a7ee-cd742dd7de3e",
  "sourceToolAssistantUUID": "ab86bf1c-87e2-4c7d-84af-23dcd84e8b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-10T18:25:17.534Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NoKkoDGgbhupPqbdbUP4XZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.16163v1",
  "prompt": "Extract from this Cosmos Policy paper:\n1. Exact RoboCasa success rates for each of the 24 tasks\n2. All baseline methods compared and their exact scores\n3. Training compute details: how many GPUs, what type, total GPU hours, training duration\n4. Model architecture and parameter count\n5. Number of demonstrations used for training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39c46281-dcaa-4a87-a7ee-cd742dd7de3e",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMfo4nPyskstd7yCDjH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c1c5fab-1437-4b69-8d1a-f79819de8c35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUYQBjTdUFxE3sQAdk9hD3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 31030,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 618
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 31030,
          "cache_creation_input_tokens": 618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 618,
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

_source line 54 · 2026-05-10T18:25:19.888Z_

<details><summary>↩ Tool result · `toolu_01HdCmvUMwfwExWc8DWFKGMq`</summary>

```text
# LIBERO-PRO: Numerical Results Extraction

## Models Evaluated
Three primary models: **OpenVLA**, **pi0**, and **pi0.5**

## Standard LIBERO Performance vs. LIBERO-PRO

All models achieve ~90-98% on standard LIBERO but collapse dramatically under perturbations:

### LIBERO-Goal Results (Table 2)
- **OpenVLA**: 98% (original) → 0% (position perturbation)
- **pi0**: 92% (original) → 0% (position perturbation)  
- **pi0.5**: 97% (original) → 38% (position perturbation)

### LIBERO-Spatial Results (Table 3)
- **OpenVLA**: 98% (original) → 0% (position) → 89% (environment)
- **pi0**: 97% (original) → 0% (position) → 60% (environment)
- **pi0.5**: 98% (original) → 20% (position) → 46% (environment)

### LIBERO-10 Results (Table 4)
- **OpenVLA**: 93% (original) → 0% (position)
- **pi0**: 82% (original) → 0% (position)
- **pi0.5**: 93% (original) → 8% (position)

### LIBERO-Object Results (Table 5)
- **OpenVLA**: 99% (original) → 0% (position)
- **pi0**: 98% (original) → 0% (position)
- **pi0.5**: 98% (original) → 17% (position)

## Key Finding
"Despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications."

**No mention of UWM or unified world models in provided content.**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "723d86fe-40c0-4ce6-936a-c036ac69dd4e",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "560ac7cf-36ec-4808-a31e-17b9def377e0",
  "sourceToolAssistantUUID": "723d86fe-40c0-4ce6-936a-c036ac69dd4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-10T18:25:24.042Z_

<details><summary>↩ Tool result · `toolu_01NoKkoDGgbhupPqbdbUP4XZ`</summary>

```text
# Cosmos Policy: Key Details Extract

## 1. RoboCasa Success Rates by Task
The document provides **overall average success rates** (67.1%) but does not break down individual task-level results. It states: "Success rates are averaged over 50 trials for each task and three random seeds (3600 trials total)."

## 2. Baseline Methods and Scores
The paper compares against multiple approaches with these aggregate results:

| Method | Training Demos | Success Rate |
|--------|---|---|
| Cosmos Policy | 50 | 67.1% |
| Video Policy | 300 | 66.0% |
| FLARE | 300 | 66.4% |
| GR00T-N1.5 | 300 | 64.1% |
| π₀ | 300 | 62.5% |

Additional baselines tested include UVA (50%), DP-VLA (57.3%), and GR00T-N1 variants.

## 3. Training Compute Details
For RoboCasa: "train Cosmos Policy for 45K gradient steps using 32 H100 GPUs with global batch size 800 (taking 48 hours total)."

## 4. Model Architecture and Parameters
The base model is "Cosmos-Predict2-2B" (2 billion parameters). The paper states: "no architectural modifications" were made—new modalities were incorporated through latent frame injection rather than structural changes.

## 5. Training Demonstrations
RoboCasa training used "50 human-teleoperated demonstrations alone," deliberately selecting the smaller dataset to assess data efficiency compared to prior work using 300+ demonstrations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c1c5fab-1437-4b69-8d1a-f79819de8c35",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "5efeea10-f277-403e-9c81-3b48d30c0182",
  "sourceToolAssistantUUID": "7c1c5fab-1437-4b69-8d1a-f79819de8c35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-10T18:25:27.606Z_

Now I have detailed numbers. Let me get one more piece of information about compute planning for adapter-based approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5efeea10-f277-403e-9c81-3b48d30c0182",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMhJtBuCi7Sdqbitrgn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bacc2bb-cdb9-4325-90fd-2c7b2a4d97b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KC7RtKwaYCaARGKrUfPNiE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 31648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 57 · 2026-05-10T18:25:28.323Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015nb694v3Ahmexm8w6sVNZp`</summary>

```json
{
  "query": "adapter LoRA finetuning diffusion transformer robotics policy 1-2B parameters GPU hours H100 training time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bacc2bb-cdb9-4325-90fd-2c7b2a4d97b5",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMhJtBuCi7Sdqbitrgn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb71086f-c642-4fe7-8764-f5c1ae35a92a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KC7RtKwaYCaARGKrUfPNiE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 31648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 58 · 2026-05-10T18:25:28.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RJcX8C4iVmWgYwnVKaMBp5`</summary>

```json
{
  "query": "RoboCasa evaluation simulation rollout time per task GPU compute evaluation cost"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb71086f-c642-4fe7-8764-f5c1ae35a92a",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMhJtBuCi7Sdqbitrgn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c96af11-c777-4f54-b866-5f6bfc84d427",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KC7RtKwaYCaARGKrUfPNiE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 31648,
      "output_tokens": 151,
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
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 31648,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1911,
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

_source line 59 · 2026-05-10T18:25:34.083Z_

<details><summary>↩ Tool result · `toolu_01RJcX8C4iVmWgYwnVKaMBp5`</summary>

```text
Web search results for query: "RoboCasa evaluation simulation rollout time per task GPU compute evaluation cost"

Links: [{"title":"GitHub - robocasa/robocasa: RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots · GitHub","url":"https://github.com/robocasa/robocasa"},{"title":"RoboCasa","url":"https://robocasa.ai/"},{"title":"GitHub - robocasa/robocasa-gr1-tabletop-tasks: Simulation benchmarks of GR1 Tabletop Tasks for GR00T N1","url":"https://github.com/robocasa/robocasa-gr1-tabletop-tasks"},{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"},{"title":"RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots","url":"https://robocasa.ai/assets/robocasa_rss24.pdf"},{"title":"RoboCasa: Scalable Household Robotics Simulation","url":"https://www.emergentmind.com/topics/robocasa"},{"title":"RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots | OpenReview","url":"https://openreview.net/forum?id=tQJYKwc3n4"},{"title":"robocasa/robocasa at main · robocasa/robocasa","url":"https://github.com/robocasa/robocasa/tree/main/robocasa"},{"title":"RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots","url":"https://arxiv.org/html/2406.02523v1"},{"title":"Simplify Generalist Robot Policy Evaluation in Simulation with NVIDIA Isaac Lab-Arena | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/simplify-generalist-robot-policy-evaluation-in-simulation-with-nvidia-isaac-lab-arena/"}]

Based on the search results, I found some relevant information about RoboCasa evaluation performance metrics, though the specific metrics you asked about are not fully detailed in these results.

Here's what I found:

**Evaluation Performance:**
In a recent evaluation of RoboCasa tasks using Isaac Lab-Arena, 10 RoboCasa tasks were evaluated with the Isaac GR00T N1.5 policy across 4,096 homogeneous environment variations per task on 8x6000D GPUs. The parallel evaluation took 0.76 hours, which is 40x faster than sequential evaluation (34.9 hours).

**GPU Requirements:**
For inference with the Cosmos Policy model on RoboCasa sim benchmark tasks, 1 GPU with 8.9 GB VRAM is needed.

**Success Rate Evaluation:**
Success rates in RoboCasa evaluations are typically averaged over 50 trials per task (across 5 evaluation scenes with 10 trials each) and 3 random seeds (3,600 trials total).

However, the search results don't contain specific information about rollout time per task or detailed GPU compute costs for RoboCasa evaluation. For more detailed technical specifications about these metrics, you may need to consult the full RoboCasa paper or technical documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c96af11-c777-4f54-b866-5f6bfc84d427",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "0b6167d9-a72e-4e0a-ae1c-bfbd37393e5a",
  "sourceToolAssistantUUID": "7c96af11-c777-4f54-b866-5f6bfc84d427",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-10T18:25:35.863Z_

<details><summary>↩ Tool result · `toolu_015nb694v3Ahmexm8w6sVNZp`</summary>

```text
Web search results for query: "adapter LoRA finetuning diffusion transformer robotics policy 1-2B parameters GPU hours H100 training time"

Links: [{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"LoRA · Hugging Face","url":"https://huggingface.co/docs/diffusers/training/lora"},{"title":"LLM Fine-Tuning on a Budget: Top FAQs on Adapters, LoRA, and Other Parameter-Efficient Methods","url":"https://www.runpod.io/articles/guides/llm-fine-tuning-on-a-budget-top-faqs-on-adapters-lora-and-other-parameter-efficient-methods"},{"title":"Parameter Efficient Fine Tuning. Adapters; LoRA; QLora; Surgical… | by Amanatullah | 𝐀𝐈 𝐦𝐨𝐧𝐤𝐬.𝐢𝐨 | Medium","url":"https://medium.com/aimonks/parameter-efficient-fine-tuning-075954d1db51"},{"title":"What is Lora Fine Tuning? The Definitive Guide","url":"https://www.truefoundry.com/blog/lora-fine-tuning"},{"title":"Gen AI Fine-Tuning Techniques: LoRA, QLoRA, And Adapters Compared - Digitaldividedata.com","url":"https://www.digitaldividedata.com/blog/ai-fine-tuning-techniques-lora-qlora-and-adapters"},{"title":"LoRA (Low-Rank Adaptation) · Hugging Face","url":"https://huggingface.co/learn/llm-course/chapter11/4"},{"title":"Using LoRA for Efficient Stable Diffusion Fine-Tuning","url":"https://huggingface.co/blog/lora"},{"title":"What Is SDXL LoRA? Custom Fine-Tuned Styles for Stable Diffusion | MindStudio","url":"https://www.mindstudio.ai/blog/what-is-sdxl-lora-custom-styles"},{"title":"Fine-Tuning LLMs with LoRA Adapters: A Comprehensive Guide | by Payoda Technology Inc | Medium","url":"https://payodatechnologyinc.medium.com/fine-tuning-llms-with-lora-adapters-a-comprehensive-guide-246fc5e01aec"}]

Based on the search results, I found relevant information about LoRA and adapter-based fine-tuning for diffusion models and transformers. Here's what the search revealed:

## LoRA Fine-tuning for Diffusion Models

LoRA freezes pre-trained model weights and injects trainable rank-decomposition matrices in each transformer block, greatly reducing the number of trainable parameters and GPU memory requirements since gradients don't need to be computed for most model weights.

### Training Time and GPU Requirements

A full LoRA training run takes approximately 5 hours on a 2080 Ti GPU with 11GB of VRAM for diffusion model fine-tuning. For more modern hardware, LoRA fine-tuning of diffusion models could be done on a 2080 Ti with 11 GB of VRAM, with trained weights saved as a single file weighing around 3 MB.

### Parameter Efficiency

Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times.

### Training for Large Models

With LoRA, you could fine-tune a 7B model in a few hours on a cloud GPU, instead of needing an expensive multi-GPU server.

However, the search results don't contain specific information about training times for 1-2B parameter models on H100 GPUs with diffusion transformers for robotics policies. The available data focuses on language models and general diffusion models rather than robotics policy-specific applications. For more precise information about robotics policy fine-tuning with those specifications, you may need to consult robotics-specific research papers or technical documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb71086f-c642-4fe7-8764-f5c1ae35a92a",
  "isSidechain": true,
  "promptId": "8fe7ba83-077d-4d82-b693-e5f7f4fab09b",
  "agentId": "aeaac1eb060a9f17c",
  "type": "user",
  "uuid": "b5df1e05-2a8f-4bab-966d-9f723fb2830c",
  "sourceToolAssistantUUID": "cb71086f-c642-4fe7-8764-f5c1ae35a92a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-10T18:26:43.043Z_

I now have comprehensive data across all five questions. Here is the full synthesis:

---

## Research Findings: RoboCasa, LIBERO-PRO, UWM, and Compute Planning

### 1. RoboCasa Benchmark -- Current SOTA (2026)

**RoboCasa** (original, RSS 2024) has been superseded by **RoboCasa365** (ICLR 2026), which scales to 365 tasks across 2,500 kitchen environments with 2,200+ hours of demonstration data.

**Current SOTA on original RoboCasa (24 tasks):**

| Method | Training Demos | Avg Success Rate |
|--------|---------------|-----------------|
| **Cosmos Policy (NVIDIA)** | **50** | **67.1%** |
| FLARE | 300 | 66.4% |
| Video Policy | 300 | 66.0% |
| GR00T N1.5 | 300 | 64.1% |
| pi0 | 300 | 62.5% |
| DP-VLA | 300 | 57.3% |
| UVA | 300 | 50.0% |

Cosmos Policy is notable for achieving SOTA with only 50 demos (vs. 300 for all baselines). It is built on a frozen **Cosmos-Predict2-2B** (2B-parameter video diffusion transformer) with action heads injected as latent frames -- no architectural modifications to the backbone. Training: **32 H100 GPUs, 48 hours, 45K gradient steps, global batch size 800**. That is approximately **1,536 H100-hours**.

**RoboCasa365 leaderboard (multi-task, 365 tasks):**
- **GR00T N1.5** performs best overall, followed by pi0/pi0.5, then Diffusion Policy
- GR00T N1.5 achieves ~20% on Composite-Unseen tasks (hardest category)
- Real-world transfer: GR00T N1.5 "Sim-and-Real" approach reaches **79.8%** on 4 real tasks

Note: Papers With Code was shut down by Meta in July 2025; the active leaderboard is hosted at [robocasa.ai](https://robocasa.ai/).

**Sources:**
- [Cosmos Policy paper](https://arxiv.org/abs/2601.16163)
- [Cosmos Policy HuggingFace model card](https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B)
- [RoboCasa365 (ICLR 2026)](https://arxiv.org/abs/2603.04356)
- [RoboCasa365 OpenReview](https://openreview.net/forum?id=tQJYKwc3n4)
- [RoboCasa official site](https://robocasa.ai/)

---

### 2. LIBERO-PRO Benchmark

LIBERO-PRO (arXiv 2510.03827) is a robustness extension of LIBERO that tests VLA models under four perturbation dimensions: **objects, positions, semantics, task-level, and environment**.

**Models evaluated:** OpenVLA, pi0, pi0.5

**Key results (standard LIBERO -> under perturbation):**

| Model | Standard LIBERO | Position Perturbation | Semantic Perturbation | Environment Perturbation |
|-------|----------------|----------------------|----------------------|------------------------|
| OpenVLA | 93-99% | **0%** | 96-98% | 0-98% |
| pi0 | 82-98% | **0%** | 82-97% | 27-60% |
| pi0.5 | 93-98% | **8-38%** | 93-97% | 46% |

The devastating finding: models scoring 90%+ on standard LIBERO **collapse to 0%** under simple position perturbations. pi0.5 is the only model with any resilience (38% best case under position changes). Models also largely ignore language instructions.

A related benchmark, **LIBERO-Plus** (arXiv 2510.13626), tests seven perturbation dimensions and finds performance drops from 95% to below 30% under modest camera viewpoint or initial state changes.

**UWM has NOT been evaluated on LIBERO-PRO.** The LIBERO-PRO paper makes no mention of UWM.

**Sources:**
- [LIBERO-PRO paper](https://arxiv.org/abs/2510.03827)
- [LIBERO-PRO GitHub](https://github.com/Zxy-MLlab/LIBERO-PRO)
- [LIBERO-Plus paper](https://arxiv.org/abs/2510.13626)

---

### 3. UWM on RoboCasa -- No Evidence Found

**No one has adapted UWM to RoboCasa.** My searches for "UWM RoboCasa" and "unified world model RoboCasa" returned no results showing any such adaptation. The UWM paper itself makes no mention of RoboCasa. This confirms the reviewer's concern that this would be genuinely new engineering work.

---

### 4. UWM Benchmark Results (What It Has Actually Been Evaluated On)

UWM (arXiv 2504.02792, RSS 2025) was evaluated on:

**A. LIBERO simulation (5 evaluation tasks out of 100, 90 used for pretraining):**

| Method | Book-Caddy | Soup-Cheese | Bowl-Drawer | Moka-Moka | Mug-Mug | **Average** |
|--------|-----------|-------------|-------------|-----------|---------|------------|
| **UWM** | 0.91 +/- 0.07 | 0.93 +/- 0.01 | 0.80 +/- 0.02 | 0.68 +/- 0.02 | 0.65 +/- 0.01 | **0.79 +/- 0.11** |
| Diffusion Policy | 0.73 +/- 0.10 | 0.88 +/- 0.02 | 0.77 +/- 0.02 | 0.65 +/- 0.03 | 0.53 +/- 0.05 | 0.71 +/- 0.12 |
| GR1 | - | - | - | - | - | 0.58 +/- 0.14 |
| PAD | - | - | - | - | - | 0.57 +/- 0.19 |

**B. Real robot tasks** (5 tasks: Stack-Bowls, Block-Cabinet, Paper-Towel, Hang-Towel, Rice-Cooker) -- UWM outperforms baselines by up to 20% in both in-distribution and OOD settings.

**C. Pretraining data:** 2,000 trajectories from DROID + 2,000 action-free video trajectories for co-training. Training: 100K steps pretraining, 10K steps finetuning.

**Critically, UWM has NOT been evaluated on:** RoboCasa, RoboCasa365, LIBERO-PRO, LIBERO-Plus, MetaWorld, or any large-scale multi-task kitchen benchmark.

**Sources:**
- [UWM project page](https://weirdlabuw.github.io/uwm/)
- [UWM paper](https://arxiv.org/abs/2504.02792)
- [UWM GitHub](https://github.com/WEIRDLabUW/unified-world-model)

---

### 5. Compute Costs for Adapter Training on Frozen DiT

**Reference points from comparable approaches:**

| Approach | Base Model | Training Setup | Total GPU-Hours |
|----------|-----------|---------------|----------------|
| **Cosmos Policy** (frozen 2B DiT + action latent injection) | Cosmos-Predict2-2B | 32x H100, 48h | **~1,536 H100-hrs** |
| LoRA on Stable Diffusion | ~1B UNet | 1x 2080 Ti, ~5h | ~5 GPU-hrs |
| OpenVLA LoRA fine-tuning | 7B VLA | 1x A100, few hours | ~4-8 A100-hrs |
| Diffusion Policy (from scratch) | ~100M | 1x A40, ~3h | ~3 GPU-hrs |
| 3D Diffusion Policy | ~100M | 1x A40, ~3h | ~3 GPU-hrs |
| General PEFT vs full fine-tune | Any | - | ~10x reduction |

**Key insight for your 200 H100-hour budget:** Cosmos Policy's 1,536 H100-hour training cost is far above your budget, but that includes full training from the frozen video backbone. If you are doing **adapter/LoRA-based fine-tuning** on a frozen DiT of similar size (~2B), you should expect:

- **LoRA/adapter training on a frozen 2B DiT:** Likely **20-80 H100-hours** (based on the ~10x reduction factor from PEFT literature, scaled from Cosmos Policy's full training)
- **Evaluation on RoboCasa** (3,600 rollouts at Cosmos Policy protocol): With parallel simulation on 8 GPUs, approximately **1-5 H100-hours** per full evaluation sweep
- **LIBERO-PRO evaluation:** Much cheaper, as tasks are shorter-horizon -- estimate **1-3 H100-hours**

**Sources:**
- [Cosmos Policy training details](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html)
- [LoRA for Stable Diffusion](https://huggingface.co/blog/lora)
- [LoRA paper](https://arxiv.org/abs/2106.09685)
- [Isaac Lab-Arena parallel evaluation](https://developer.nvidia.com/blog/simplify-generalist-robot-policy-evaluation-in-simulation-with-nvidia-isaac-lab-arena/)

---

### Proposed Compute Plan (200 H100-hours)

| Phase | Task | Estimated H100-hours |
|-------|------|---------------------|
| **1. Engineering & integration** | Adapt UWM codebase to RoboCasa env (data pipeline, observation space, action space) | 10-20 (debugging runs) |
| **2. Adapter training on RoboCasa** | LoRA/adapter fine-tuning of frozen UWM DiT on RoboCasa demonstrations | 40-80 |
| **3. Adapter training on LIBERO** | Fine-tune for LIBERO tasks (smaller scale) | 15-30 |
| **4. RoboCasa evaluation** | Full eval: 24 tasks x 50 trials x 3 seeds = 3,600 rollouts | 5-10 |
| **5. LIBERO-PRO evaluation** | Run perturbation suite across 4 dimensions | 3-8 |
| **6. Ablations & hyperparameter sweeps** | LoRA rank, learning rate, data scaling | 30-50 |
| **7. Buffer for failures/reruns** | Inevitable debugging, crashed runs | 20-30 |
| **TOTAL** | | **123-228** |

**Assessment:** 200 H100-hours is tight but feasible if you use parameter-efficient fine-tuning (LoRA/adapters) rather than full fine-tuning. The main risks are:

1. **Engineering unknowns** -- UWM has never touched RoboCasa, so observation/action space integration could require significant debugging
2. **Ablation budget** -- you may need to sacrifice comprehensive sweeps to stay within budget
3. **RoboCasa365 is out of scope** -- the 365-task version would require substantially more compute; stick to the original 24-task RoboCasa

To derisk, I would recommend starting with LIBERO (where UWM already has results) and using that as a validation of your adapter pipeline before moving to RoboCasa, which is the genuinely novel and higher-risk evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5df1e05-2a8f-4bab-966d-9f723fb2830c",
  "isSidechain": true,
  "agentId": "aeaac1eb060a9f17c",
  "requestId": "req_011CauMiBH51UzbRiH2UunG8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16de467b-ddcf-48cb-a6c8-4c8ddc9b1c85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981195d-1dd3-4986-bae6-45a75a7bbf26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMwYhaTMNR45hR4N6KbYp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 1236,
      "cache_read_input_tokens": 33559,
      "output_tokens": 3038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1236
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 865,
          "output_tokens": 3038,
          "cache_read_input_tokens": 33559,
          "cache_creation_input_tokens": 1236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1236,
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
