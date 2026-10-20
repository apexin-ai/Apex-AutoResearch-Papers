# Research conversation: Use WebSearch and WebFetch to verify details about "Robometer" — claimed to be a dense frame-level reward model for robo

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab187563801a41da1.jsonl`
- **Structured JSON:** [`1a20cda94c90857c32ee.json`](../../sessions/1a/1a20cda94c90857c32ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-14T03:08:41.211Z_

Use WebSearch and WebFetch to verify details about "Robometer" — claimed to be a dense frame-level reward model for robotics (RSS 2026). I need to verify:

1. Does Robometer actually exist? Search for "Robometer reward model robot" and "Robometer RSS 2026"
2. Does it really provide dense FRAME-LEVEL rewards (not just trajectory-level)?
3. Is there a LIBERO checkpoint publicly available?
4. Is it trained on "RBM-1M" dataset with 1M+ trajectories?
5. Can it generalize to RoboMimic tasks, or is it LIBERO-specific?

Also search for other dense reward models for robotics: "RoboReward", "dense reward model robot manipulation 2025 2026". 

If Robometer doesn't exist or doesn't provide frame-level dense rewards, this is a critical issue for the paper idea that depends on it. Report concisely (under 400 words).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "aa4cd2e2-cc9d-4c10-a05d-d49453405c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T03:08:41.218Z_

```json
{
  "parentUuid": "aa4cd2e2-cc9d-4c10-a05d-d49453405c66",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7132cc73-caf2-4e8d-a0be-f82e3980c190",
  "timestamp": "2026-05-14T03:08:41.218Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T03:08:44.007Z_



I'll search for information about "Robometer" and related dense reward models for robotics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7132cc73-caf2-4e8d-a0be-f82e3980c190",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j2UX8LwYXBq9HydFgL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71a47756-d235-4a09-ab66-47d812cffbb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXyhQn7kueiEgc7XLM9hFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 749,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 4 · 2026-05-14T03:08:44.451Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012PrtnSjLWZ4muR21bdBRus`</summary>

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
  "parentUuid": "71a47756-d235-4a09-ab66-47d812cffbb3",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j2UX8LwYXBq9HydFgL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16bcef70-21ce-4dcc-b7bf-61e7c710af9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXyhQn7kueiEgc7XLM9hFW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 7304,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 749
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 749,
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

_source line 5 · 2026-05-14T03:08:44.453Z_

<details><summary>↩ Tool result · `toolu_012PrtnSjLWZ4muR21bdBRus`</summary>

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
  "parentUuid": "16bcef70-21ce-4dcc-b7bf-61e7c710af9e",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "ec7bff70-4bd5-4b2e-a4c7-4cfbba482d4d",
  "sourceToolAssistantUUID": "16bcef70-21ce-4dcc-b7bf-61e7c710af9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T03:08:46.962Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec7bff70-4bd5-4b2e-a4c7-4cfbba482d4d",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j2iYEZRqLY9tVuDLp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "971bb29a-19d0-40b9-8d06-07f6140dac58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T92N7juayqdW2fWZcKmX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-14T03:08:47.976Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pg3x1o9VUNVoGTD4GDxkmu`</summary>

```json
{
  "query": "Robometer reward model robot RSS 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "971bb29a-19d0-40b9-8d06-07f6140dac58",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j2iYEZRqLY9tVuDLp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5f31a96-6e86-445c-8fc4-c1ea2be47901",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T92N7juayqdW2fWZcKmX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-14T03:08:48.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HpuWwP5yjvCv3wto5T27iV`</summary>

```json
{
  "query": "Robometer dense frame-level reward model robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5f31a96-6e86-445c-8fc4-c1ea2be47901",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j2iYEZRqLY9tVuDLp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72091315-f625-43db-b0c7-56aa2a6c730a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T92N7juayqdW2fWZcKmX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-14T03:08:48.926Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CYRs8J8pCBvrd7EfXsGrRk`</summary>

```json
{
  "query": "Robometer RBM-1M dataset robot trajectories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72091315-f625-43db-b0c7-56aa2a6c730a",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j2iYEZRqLY9tVuDLp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c683e25a-4c64-461c-8686-0b22e5ccbd32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T92N7juayqdW2fWZcKmX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 10 · 2026-05-14T03:08:49.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QJVtH4fKTxTf2WUdZLrLVn`</summary>

```json
{
  "query": "RoboReward dense reward model robot manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c683e25a-4c64-461c-8686-0b22e5ccbd32",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j2iYEZRqLY9tVuDLp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f98d449-b3b3-4e7f-9a91-059d246da7b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T92N7juayqdW2fWZcKmX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 11 · 2026-05-14T03:08:50.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CGBMyMxCfbtv3Bcns5LBHg`</summary>

```json
{
  "query": "Robometer LIBERO checkpoint generalization RoboMimic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f98d449-b3b3-4e7f-9a91-059d246da7b3",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j2iYEZRqLY9tVuDLp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a57d003-37fa-4a03-a931-0ebe6f76ee0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T92N7juayqdW2fWZcKmX3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8053,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 264,
          "cache_read_input_tokens": 8053,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 12 · 2026-05-14T03:08:55.606Z_

<details><summary>↩ Tool result · `toolu_01CYRs8J8pCBvrd7EfXsGrRk`</summary>

```text
Web search results for query: "Robometer RBM-1M dataset robot trajectories"

Links: [{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"ROBOMETER: Scaling General-Purpose Robotic","url":"https://robometer.github.io/assets/robometer.pdf"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115v1"},{"title":"GitHub - robometer/robometer: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons · GitHub","url":"https://github.com/robometer/robometer"},{"title":"[2603.02115] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115"},{"title":"[2603.02115v1] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115v1"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | alphaXiv","url":"https://www.alphaxiv.org/resources/2603.02115v1"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models","url":"https://robotics-transformer-x.github.io/"},{"title":"aliangdw/Robometer-4B-LIBERO · Hugging Face","url":"https://huggingface.co/aliangdw/Robometer-4B-LIBERO"},{"title":"GitHub - mint-lab/awesome-robotics-datasets: A collection of useful datasets for robotics and computer vision · GitHub","url":"https://github.com/mint-lab/awesome-robotics-datasets"}]

Based on the search results, here's what I found about the Robometer RBM-1M dataset:

## Overview

RBM-1M is a large-scale reward-learning dataset comprising over one million trajectories spanning diverse robot embodiments and tasks, including substantial suboptimal and failure data.

## Dataset Composition

The dataset spans 21 robot embodiments, containing both reward-labeled/expert trajectories and reward-unlabeled, failed trajectories. Suboptimal and failure data constitute a substantial fraction, enabling the preference-based learning component of Robometer.

## Purpose and Applications

The model is supervised with a dual objective: predicting frame-level task progress (reward) and learning trajectory-level preferences from pairwise comparisons. The training recipe enables scalable reward learning and supports diverse downstream applications such as offline & online RL, imitation learning data filtering and retrieval, and automated failure detection.

## Related Model

The RBM-1M dataset was created to train Robometer, a general-purpose robotic reward model trained on trajectory comparisons from the RBM-1M dataset that provides dense, video-language-conditioned rewards for robot learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c683e25a-4c64-461c-8686-0b22e5ccbd32",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "c7b01eaf-cd49-4f77-a167-e400d1e1f3e2",
  "sourceToolAssistantUUID": "c683e25a-4c64-461c-8686-0b22e5ccbd32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T03:08:55.846Z_

<details><summary>↩ Tool result · `toolu_01HpuWwP5yjvCv3wto5T27iV`</summary>

```text
Web search results for query: "Robometer dense frame-level reward model robotics"

Links: [{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115v1"},{"title":"[2603.02115] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115"},{"title":"Scaling General-Purpose Robotic Reward Models via ...","url":"https://robometer.github.io/assets/robometer.pdf"},{"title":"GitHub - robometer/robometer: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons · GitHub","url":"https://github.com/robometer/robometer"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | alphaXiv","url":"https://www.alphaxiv.org/abs/2603.02115"},{"title":"[2603.02115v1] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115v1"},{"title":"Jiahui Zhang's research works | University of Southern California and other places","url":"https://www.researchgate.net/scientific-contributions/Jiahui-Zhang-2254368611"},{"title":"Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models","url":"https://arxiv.org/html/2603.16065"},{"title":"aliangdw/Robometer-4B-LIBERO · Hugging Face","url":"https://huggingface.co/aliangdw/Robometer-4B-LIBERO"}]

## Results

I found comprehensive information about Robometer. Here's an overview:

### What is Robometer?

Robometer is a general-purpose, video-language-input, dense reward model trained with a dual reward-prediction objective: a frame-level progress loss on expert data and a preference-prediction loss over trajectory comparisons.

### The Problem It Addresses

General-purpose robot reward models are typically trained to predict absolute task progress from expert demonstrations, providing only local, frame-level supervision. While effective for expert demonstrations, this paradigm scales poorly to large-scale robotics datasets where failed and suboptimal trajectories are abundant and assigning dense progress labels is ambiguous.

### Key Innovation

Robometer combines intra-trajectory progress supervision with inter-trajectory preference supervision. It is trained with a dual objective: a frame-level progress loss that anchors reward magnitude on expert data, and a trajectory-comparison preference loss that imposes global ordering constraints across trajectories of the same task, enabling effective learning from both real and augmented failed trajectories.

### Supporting Dataset

To support this formulation at scale, they curate RBM-1M, a reward-learning dataset comprising over one million trajectories spanning diverse robot embodiments and tasks, including substantial suboptimal and failure data.

### Performance

Across benchmarks and real-world evaluations, Robometer learns more generalizable reward functions than prior methods and improves robot learning performance across a diverse set of downstream applications.

The project includes open-source code and model weights available on GitHub and Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72091315-f625-43db-b0c7-56aa2a6c730a",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "02016f17-b567-43cb-9c36-bd1b2e6b6277",
  "sourceToolAssistantUUID": "72091315-f625-43db-b0c7-56aa2a6c730a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T03:08:56.304Z_

<details><summary>↩ Tool result · `toolu_01Pg3x1o9VUNVoGTD4GDxkmu`</summary>

```text
Web search results for query: "Robometer reward model robot RSS 2026"

Links: [{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"[2603.02115v1] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115v1"},{"title":"[2603.02115] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115"},{"title":"GitHub - robometer/robometer: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons · GitHub","url":"https://github.com/robometer/robometer"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115"},{"title":"Scaling General-Purpose Robotic Reward Models via ...","url":"https://robometer.github.io/assets/robometer.pdf"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.02115"},{"title":"New RoboReward dataset and models automate robotic training and evaluation","url":"https://techxplore.com/news/2026-01-roboreward-dataset-automate-robotic.html"},{"title":"RSS: Robotics: Science and Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2506&f=Robotics"},{"title":"aliangdw/Robometer-4B-LIBERO · Hugging Face","url":"https://huggingface.co/aliangdw/Robometer-4B-LIBERO"}]

Based on the search results, here's what I found about Robometer:

## Robometer: Scaling General-Purpose Robotic Reward Models

Robometer is a scalable reward modeling framework that combines intra-trajectory progress supervision with inter-trajectory preference supervision. Robometer is trained with a dual objective: a frame-level progress loss that anchors reward magnitude on expert data, and a trajectory-comparison preference loss that imposes global ordering constraints across trajectories of the same task, enabling effective learning from both real and augmented failed trajectories.

### Key Features

It provides dense, video-language-conditioned rewards for robot learning. The model combines frame-level progress supervision on expert data and trajectory-comparison preference supervision, so it can learn from both successful and failed rollouts and generalize across diverse robot embodiments and tasks.

### The RBM-1M Dataset

To support this formulation at scale, the research curates RBM-1M, a reward-learning dataset comprising over one million trajectories spanning diverse robot embodiments and tasks, including substantial suboptimal and failure data.

### Publication and Results

The work was accepted to Robotics: Science and Systems 2026 (RSS 2026). Across benchmarks and real-world evaluations, Robometer learns more generalizable reward functions than prior methods and improves robot learning performance across a diverse set of downstream applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5f31a96-6e86-445c-8fc4-c1ea2be47901",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "9e2b8962-bff3-4ae7-ba0c-cb075cb39580",
  "sourceToolAssistantUUID": "f5f31a96-6e86-445c-8fc4-c1ea2be47901",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T03:08:57.107Z_

<details><summary>↩ Tool result · `toolu_01QJVtH4fKTxTf2WUdZLrLVn`</summary>

```text
Web search results for query: "RoboReward dense reward model robot manipulation 2025 2026"

Links: [{"title":"RoboReward","url":"https://openreview.net/pdf/0f7c964ef51527714b3964df61f35567d94b0e7b.pdf"},{"title":"[2601.00675] RoboReward: General-Purpose Vision-Language Reward Models for Robotics","url":"https://arxiv.org/abs/2601.00675"},{"title":"Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models","url":"https://arxiv.org/html/2603.16065"},{"title":"Rewarding DINO: Predicting Dense Rewards with Vision Foundation Models","url":"https://arxiv.org/html/2603.16978"},{"title":"New RoboReward dataset and models automate robotic training and evaluation","url":"https://techxplore.com/news/2026-01-roboreward-dataset-automate-robotic.html"},{"title":"RoboReward: A Dataset and Benchmark for Vision-Language Reward Models in Robotics | OpenReview","url":"https://openreview.net/forum?id=iDmt7Tzmke"},{"title":"Multi-Stage Manipulation with Demonstration-Augmented Reward, Policy, and World Model Learning","url":"https://arxiv.org/html/2503.01837v1"},{"title":"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://arxiv.org/html/2602.19313v1"},{"title":"[2604.00055] Generalizable Dense Reward for Long-Horizon Robotic Tasks","url":"https://arxiv.org/abs/2604.00055"},{"title":"RoboReward: General-Purpose Vision-Language Reward Models for Robotics | ArXiv Intelligence","url":"https://arxivai.iip.com.ua/paper/Um9ib1Jld2FyZCUzQSUy"}]

Based on the search results, here's what I found about RoboReward and dense reward models for robot manipulation:

## RoboReward Overview

RoboReward is a new open-source dataset and benchmark designed to automate the training and evaluation of vision-language reward models (VLMs) for robotics. Researchers at Stanford University and UC Berkeley introduced RoboReward, presenting RoboReward 4B and 8B, two new VLMs that outperform other models introduced in the past.

## Purpose and Problem It Solves

A well-designed reward is critical for effective reinforcement learning-based policy improvement, and in real-world robotics, obtaining such rewards typically requires either labor-intensive human labeling or brittle, handcrafted objectives. The RoboReward dataset can significantly improve accuracy, taking us one step closer to fully autonomous improvement of real-world robot policies.

## Key Features

RoboReward-3B/7B are two general-purpose robot reward models, and the team open-sourced all models, training data, and evaluation benchmark to advance the development of general-purpose reward models for robotics. The researchers proposed counterfactual relabeling that turns successful episodes into calibrated negative and near-miss examples for the same video.

## Performance Results

RoboReward achieved a success rate 40% higher than baseline CLIP-Reward methods on a suite of complex manipulation tasks in Meta-World. The 3B and 7B vision-language reward models trained on this dataset outperform much larger VLMs, including state-of-the-art proprietary VLMs, and show promising results when used as a reward for real robot reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f98d449-b3b3-4e7f-9a91-059d246da7b3",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "d924713a-8f69-4eca-a14d-f94410cd6bf7",
  "sourceToolAssistantUUID": "2f98d449-b3b3-4e7f-9a91-059d246da7b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T03:08:58.028Z_

<details><summary>↩ Tool result · `toolu_01CGBMyMxCfbtv3Bcns5LBHg`</summary>

```text
Web search results for query: "Robometer LIBERO checkpoint generalization RoboMimic"

Links: [{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"aliangdw/Robometer-4B-LIBERO · Hugging Face","url":"https://huggingface.co/aliangdw/Robometer-4B-LIBERO"},{"title":"GitHub - robometer/robometer: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons · GitHub","url":"https://github.com/robometer/robometer"},{"title":"robomimic","url":"https://robomimic.github.io/"},{"title":"RoboMM: All-in-One Multimodal Large Model for Robotic Manipulation","url":"https://arxiv.org/html/2412.07215v1"},{"title":"GitHub - ARISE-Initiative/robomimic: robomimic: A Modular Framework for Robot Learning from Demonstration · GitHub","url":"https://github.com/ARISE-Initiative/robomimic"},{"title":"robomimic v0.1 (CoRL 2021) — robomimic 0.5 documentation","url":"https://robomimic.github.io/docs/datasets/robomimic_v0.1.html"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115v1"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"Real-World Data for LIBERO Lifelong Robot Learning | Claru","url":"https://claru.ai/benchmarks/libero"}]

Based on the web search results, here's what I found about the query terms:

## Robometer

Robometer is a scalable reward modeling framework that combines intra-trajectory progress supervision with inter-trajectory preference supervision, trained with a dual objective: a frame-level progress loss that anchors reward magnitude on expert data, and a trajectory-comparison preference loss that imposes global ordering constraints across trajectories of the same task. The model combines frame-level progress supervision on expert data and trajectory-comparison preference supervision, so it can learn from both successful and failed rollouts and generalize across diverse robot embodiments and tasks.

## LIBERO

LIBERO (LIfelong BEnchmark for RObot learning) evaluates lifelong and continual learning for robot manipulation, with 130 language-annotated manipulation tasks organized into 5 evaluation suites built on the robosuite/MuJoCo framework. LIBERO-Spatial tests whether a policy can adapt when objects move to new locations, LIBERO-Object tests generalization when new object categories appear, and LIBERO-Goal tests understanding of novel task specifications with familiar objects.

## Integration and Generalization

Robometer has been evaluated on LIBERO-90 tasks, with controlled settings using data from the LIBERO robot manipulation simulated benchmark, training models with successful demos from LIBERO subsets and evaluating performance on unseen tasks. Robometer outperforms reward baselines in both generalization and distinguishing successful / failed trajectories, and serves as a strong initialization for further fine-tuning.

## RoboMimic

RoboMimic is a framework for robot learning from demonstration that offers a broad set of demonstration datasets collected on robot manipulation domains, and learning algorithms to learn from these datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a57d003-37fa-4a03-a931-0ebe6f76ee0b",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "7e159333-afa8-45a8-9c6a-aa08249f3c89",
  "sourceToolAssistantUUID": "2a57d003-37fa-4a03-a931-0ebe6f76ee0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-14T03:09:03.408Z_

Let me get more details from the project page and the Hugging Face checkpoint to confirm specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e159333-afa8-45a8-9c6a-aa08249f3c89",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j3iN6YuXGYySLedh7E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed52ceb9-4d06-4ab6-ba3c-32728e6d1ab5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6MSjKK9Kk6MwgcHJR2k2D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 9963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4601,
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

_source line 18 · 2026-05-14T03:09:05.915Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W2vj8da4oAHVkzbqQh6gmX`</summary>

```json
{
  "url": "https://huggingface.co/aliangdw/Robometer-4B-LIBERO",
  "prompt": "What model is this? What is it trained on? Is it a dense frame-level reward model? What tasks/benchmarks does it support? Is there any mention of RoboMimic generalization?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed52ceb9-4d06-4ab6-ba3c-32728e6d1ab5",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j3iN6YuXGYySLedh7E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff001244-c7a1-4e3c-8fa9-21ce1b1d820d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6MSjKK9Kk6MwgcHJR2k2D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 9963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4601,
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

_source line 19 · 2026-05-14T03:09:07.488Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016F2dGg4P4w7Q3AcFgF3L6t`</summary>

```json
{
  "url": "https://robometer.github.io/",
  "prompt": "Does Robometer provide dense frame-level rewards or only trajectory-level rewards? Does it generalize to RoboMimic tasks? What benchmarks is it evaluated on? What is the RBM-1M dataset size? Is there a LIBERO checkpoint?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff001244-c7a1-4e3c-8fa9-21ce1b1d820d",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j3iN6YuXGYySLedh7E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab532306-d923-45b1-b137-0bec38c77eb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6MSjKK9Kk6MwgcHJR2k2D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 9963,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4601
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 9963,
          "cache_creation_input_tokens": 4601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4601,
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

_source line 20 · 2026-05-14T03:09:11.401Z_

<details><summary>↩ Tool result · `toolu_01W2vj8da4oAHVkzbqQh6gmX`</summary>

````text
# Robometer-4B-LIBERO Overview

## What Model Is This?

**Robometer** is a general-purpose **vision-language reward model for robotics** built on **Qwen3-VL-4B**. It's a 5B parameter model designed to evaluate robot trajectories and provide reward signals.

## Training Data

Trained on **RBM-1M** dataset with supervision on:
- Frame-level progress (continuous 0-1 values or binned)
- Frame-level success (per-timestep success probability)
- Trajectory preferences (ranking which trajectory is better)

The model is specifically trained on **LIBERO-10/Spatial/Object/Goal** tasks.

## Architecture: Dense Frame-Level Reward Model

Yes, it is a **dense frame-level reward model**. Given a task instruction and rollout video, it predicts:

1. **Per-frame progress** — continuous progress values over time
2. **Per-frame success** — success probability at each timestep
3. **Trajectory preferences** — ranking between two trajectories

## Tasks/Benchmarks Supported

The page explicitly mentions training on:
- **LIBERO-10**
- **LIBERO-Spatial**
- **LIBERO-Object**
- **LIBERO-Goal**

## RoboMimic Generalization

**No mention of RoboMimic generalization** is provided in the available content. The page references generalization across "diverse robot embodiments and tasks" but does not specifically discuss RoboMimic benchmarks.

## Usage Example

```python
from transformers import AutoProcessor, RFM

processor = AutoProcessor.from_pretrained("aliangdw/Robometer-4B-LIBERO")
model = RFM.from_pretrained("aliangdw/Robometer-4B-LIBERO")
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff001244-c7a1-4e3c-8fa9-21ce1b1d820d",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "19e2bf0c-9159-431a-808d-bb534454e047",
  "sourceToolAssistantUUID": "ff001244-c7a1-4e3c-8fa9-21ce1b1d820d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T03:09:13.595Z_

<details><summary>↩ Tool result · `toolu_016F2dGg4P4w7Q3AcFgF3L6t`</summary>

```text
# Robometer Q&A

**Dense vs. Trajectory-Level Rewards:**
Robometer provides dense, frame-level rewards. The method includes "Frame-Level Progress and Success Prediction" that anchors reward magnitude through "per-frame progress and success values on expert demonstration data."

**RoboMimic Generalization:**
The page does not mention RoboMimic tasks or whether Robometer generalizes to them.

**Evaluation Benchmarks:**
Robometer is evaluated on multiple benchmarks including "RBM-EVAL" (in-distribution and out-of-distribution), "RoboRewardBench," and various datasets like RACER, OXE variants, Metaworld, and Libero.

**RBM-1M Dataset Size:**
The dataset comprises "over one million trajectories spanning diverse robot embodiments and tasks" across "21 Robot Embodiments" with "140,000+ Trajs. from Mixed Expertise Datasets."

**LIBERO Checkpoint:**
The page does not specify whether a LIBERO-specific checkpoint exists. It shows results on "Libero (90)" as part of evaluation metrics but doesn't detail checkpoint availability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab532306-d923-45b1-b137-0bec38c77eb9",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "d01cc6ed-b61a-4bd5-859f-7f01a33b2dac",
  "sourceToolAssistantUUID": "ab532306-d923-45b1-b137-0bec38c77eb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-14T03:09:16.329Z_

Now let me check the GitHub repo and the arxiv paper for details on RoboMimic generalization specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d01cc6ed-b61a-4bd5-859f-7f01a33b2dac",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j4rzXv77sKkZE6g8o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64e51d18-b9d7-42aa-bc8e-4ed2e60b06ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAwr3iR1LXpq2iZKjVysFT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 14564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
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

_source line 23 · 2026-05-14T03:09:18.698Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EbfnRANekLW5wKz4iXdqYj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.02115",
  "prompt": "Does the paper mention RoboMimic tasks or generalization to RoboMimic? What benchmarks does it evaluate on beyond LIBERO? Does it claim to be general-purpose across embodiments? Is the reward truly per-frame (dense) or per-trajectory?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64e51d18-b9d7-42aa-bc8e-4ed2e60b06ef",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j4rzXv77sKkZE6g8o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee92d884-0b6c-496e-a353-474aed90c9e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAwr3iR1LXpq2iZKjVysFT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 14564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
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

_source line 24 · 2026-05-14T03:09:19.489Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GXq8z9GS8uHmqKpBLQnfx3`</summary>

```json
{
  "url": "https://github.com/robometer/robometer",
  "prompt": "What checkpoints are available? Is there a LIBERO checkpoint? Does it mention RoboMimic support? What benchmarks are supported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee92d884-0b6c-496e-a353-474aed90c9e8",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j4rzXv77sKkZE6g8o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3e7dc01-50c7-46d8-b922-94a4bac71112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAwr3iR1LXpq2iZKjVysFT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 14564,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1041
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 262,
          "cache_read_input_tokens": 14564,
          "cache_creation_input_tokens": 1041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1041,
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

_source line 25 · 2026-05-14T03:09:23.024Z_

<details><summary>↩ Tool result · `toolu_01EbfnRANekLW5wKz4iXdqYj`</summary>

```text
Based on the provided arXiv page content, I can address your questions:

**RoboMimic tasks/generalization:** The abstract does not mention RoboMimic or evaluation on RoboMimic benchmarks.

**Benchmarks beyond LIBERO:** The page does not specify which benchmarks are evaluated. It states results across "benchmarks and real-world evaluations" but doesn't name them beyond referencing the dataset.

**General-purpose across embodiments:** Yes, the paper explicitly addresses this. The abstract states the dataset includes "diverse robot embodiments and tasks," and the title references "General-Purpose Robotic Reward Models."

**Reward density:** The rewards appear to be dual-level rather than purely per-frame. The abstract indicates a "frame-level progress loss" combined with "trajectory-comparison preference loss," suggesting both frame-level and trajectory-level supervision rather than strictly dense, per-frame rewards.

The page notes the work curated "RBM-1M, a reward-learning dataset comprising over one million trajectories" and indicates code/models are available at robometer.github.io, but specific benchmark names aren't listed on this abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee92d884-0b6c-496e-a353-474aed90c9e8",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "6570d66a-235d-4e81-b76b-cb8b23f4789c",
  "sourceToolAssistantUUID": "ee92d884-0b6c-496e-a353-474aed90c9e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T03:09:24.688Z_

<details><summary>↩ Tool result · `toolu_01GXq8z9GS8uHmqKpBLQnfx3`</summary>

```text
# Robometer Checkpoints and Support

## Available Checkpoints

Two primary checkpoints are mentioned:

1. **Robometer-4B** — the general-purpose model trained on RBM-1M dataset
2. **Robometer-LIBERO** — a fine-tuned version optimized for LIBERO tasks, available as "robometer-4b-fft-libero"

The documentation notes that the LIBERO checkpoint is recommended "if you need to do LIBERO-90 RL or if the default Robometer checkpoint doesn't perform as well."

## LIBERO Support

Yes, LIBERO is well-supported. The repository includes training instructions for LIBERO datasets (10, Object, Spatial, and Goal variants), with evaluation against the LIBERO-90 benchmark.

## RoboMimic Support

The provided content does not mention RoboMimic or any related support for that dataset.

## Supported Benchmarks

The framework evaluates models using three primary metrics:
- **Reward alignment** — measuring progress prediction accuracy
- **Policy ranking** — assessing trajectory quality discrimination
- **Confusion matrix** — comparing performance across different robot embodiments and tasks
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3e7dc01-50c7-46d8-b922-94a4bac71112",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "ab187563801a41da1",
  "type": "user",
  "uuid": "74a41c60-026b-4675-9e6f-1f56863626df",
  "sourceToolAssistantUUID": "f3e7dc01-50c7-46d8-b922-94a4bac71112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-14T03:09:45.634Z_

Here is my report:

---

**Robometer Verification -- All 5 Claims**

**1. Does Robometer exist?** Yes. It is a real, published project (arXiv [2603.02115](https://arxiv.org/abs/2603.02115)), accepted at RSS 2026. It has a [project page](https://robometer.github.io/), [GitHub repo](https://github.com/robometer/robometer), and [Hugging Face checkpoints](https://huggingface.co/aliangdw/Robometer-4B-LIBERO). It is built on Qwen3-VL-4B (~5B params).

**2. Does it provide dense frame-level rewards?** Yes, confirmed. It predicts per-frame progress (continuous 0-1) and per-frame success probability. It is trained with a dual objective: a **frame-level progress loss** on expert data plus a **trajectory-comparison preference loss** for global ordering. So it genuinely provides dense, per-timestep reward signals -- not just a single trajectory-level score.

**3. Is there a LIBERO checkpoint publicly available?** Yes. A dedicated LIBERO checkpoint (`Robometer-4B-LIBERO` / `robometer-4b-fft-libero`) is available on Hugging Face. It is fine-tuned on LIBERO-10/Spatial/Object/Goal and recommended for LIBERO-90 RL.

**4. Is it trained on RBM-1M with 1M+ trajectories?** Yes. RBM-1M contains "over one million trajectories" across 21 robot embodiments, including both expert and failed/suboptimal data.

**5. Can it generalize to RoboMimic tasks?** **Not confirmed.** Neither the paper, project page, GitHub, nor HuggingFace model card mention RoboMimic. The general-purpose checkpoint is evaluated on RBM-EVAL (in/out-of-distribution), RoboRewardBench, RACER, OXE variants, MetaWorld, and LIBERO-90 -- but RoboMimic is absent. The model claims cross-embodiment generalization, so it *might* transfer, but this is unverified.

**Other dense reward models found:**
- **RoboReward** ([arXiv 2601.00675](https://arxiv.org/abs/2601.00675)) -- Stanford/Berkeley. 3B/7B vision-language reward models with open-sourced data and benchmark. 40% higher success rate than CLIP-Reward on MetaWorld.
- **Large Reward Models** ([arXiv 2603.16065](https://arxiv.org/html/2603.16065)) -- online reward generation with VLMs.
- **Rewarding DINO** ([arXiv 2603.16978](https://arxiv.org/html/2603.16978)) -- dense rewards via vision foundation models.
- **Generalizable Dense Reward for Long-Horizon Tasks** ([arXiv 2604.00055](https://arxiv.org/abs/2604.00055)).

**Bottom line for your paper:** Robometer is real, does provide frame-level dense rewards, has a public LIBERO checkpoint, and is trained on RBM-1M. The one risk is the assumption of RoboMimic generalization -- this is unverified and not claimed by the authors. If your paper depends on applying Robometer to RoboMimic, you would need to validate that yourself or use the general checkpoint and test transfer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74a41c60-026b-4675-9e6f-1f56863626df",
  "isSidechain": true,
  "agentId": "ab187563801a41da1",
  "requestId": "req_011Cb1j5gKcjecSTy52qbrd5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65da34bb-acfa-4810-addd-77682656dec6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1GLs4GynG2wf3zzP48vD1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 15605,
      "output_tokens": 854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 854
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 854,
          "cache_read_input_tokens": 15605,
          "cache_creation_input_tokens": 854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 854,
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
