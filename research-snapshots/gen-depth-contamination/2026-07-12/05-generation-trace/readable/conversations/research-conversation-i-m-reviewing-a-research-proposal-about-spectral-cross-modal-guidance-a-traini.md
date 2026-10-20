# Research conversation: I'm reviewing a research proposal about "Spectral Cross-Modal Guidance" — a training-free method that uses SVD-based spe

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac57742c17df894bb.jsonl`
- **Structured JSON:** [`7a2ee74b74481175a8fb.json`](../../sessions/7a/7a2ee74b74481175a8fb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-10T19:46:23.708Z_

I'm reviewing a research proposal about "Spectral Cross-Modal Guidance" — a training-free method that uses SVD-based spectral filtering on video→action guidance signals in World-Action Models (WAMs) to improve robustness under geometric perturbations. I need to find competing work the proposal may have missed.

Search for:

1. "test-time adaptation diffusion policy robustness" 2025 2026 — any inference-time methods for improving robot policy robustness
2. "spectral filtering diffusion guidance robot" 2025 2026 — any spectral/SVD methods applied to robot action diffusion
3. "cross-modal guidance robot manipulation" 2025 2026 — any cross-modal guidance methods for robot control
4. "world model robustness geometric perturbation robot" 2026 — any other methods addressing WAM geometric robustness
5. "inference-time guidance robot policy" 2025 2026 — training-free methods for improving robot policies
6. "SVD diffusion model guidance" 2025 2026 — SVD-based methods in diffusion model guidance beyond DiffStateGrad
7. "ADPro adaptive diffusion policy test-time" — verify this paper exists and check its relevance
8. "TTPL test-time perturbation learning VLA" 2026 — verify this exists

Report all findings with paper titles, venues, and brief descriptions. Under 500 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "7474d2c7-5309-4e7b-8c81-4b750c1bd428",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:46:23.727Z_

```json
{
  "parentUuid": "7474d2c7-5309-4e7b-8c81-4b750c1bd428",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
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
  "uuid": "15d0315f-91da-40d7-83ab-9c80dcbe9c5d",
  "timestamp": "2026-05-10T19:46:23.727Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:46:26.212Z_



I'll search for all these topics in parallel using web search.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15d0315f-91da-40d7-83ab-9c80dcbe9c5d",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTsY5vDmujBfXvCvE76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f93f77d-6ead-4ce1-b06a-cf223658fdab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te6mR42u3UyghsQGrdsAQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 879,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:46:26.381Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014dGSgjdZz9coTsJLxYmfo7`</summary>

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
  "parentUuid": "7f93f77d-6ead-4ce1-b06a-cf223658fdab",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTsY5vDmujBfXvCvE76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b691702-3a28-4d55-bb00-f24a85e02c60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te6mR42u3UyghsQGrdsAQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 8223,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 879
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 90,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 879,
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

_source line 5 · 2026-05-10T19:46:26.383Z_

<details><summary>↩ Tool result · `toolu_014dGSgjdZz9coTsJLxYmfo7`</summary>

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
  "parentUuid": "9b691702-3a28-4d55-bb00-f24a85e02c60",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "72f845af-5c04-4f37-b66d-1fa8d25c3ee5",
  "sourceToolAssistantUUID": "9b691702-3a28-4d55-bb00-f24a85e02c60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:46:29.244Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72f845af-5c04-4f37-b66d-1fa8d25c3ee5",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTsjaUD46frc4yxQWEm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "201173c4-6ca9-4923-b21b-1045ae85c8fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8fpXfZF63bNyhcCVCJMzo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1407,
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

_source line 7 · 2026-05-10T19:46:30.024Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GuzfBKQeshEbW5DiRND69A`</summary>

```json
{
  "query": "test-time adaptation diffusion policy robustness robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "201173c4-6ca9-4923-b21b-1045ae85c8fb",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTsjaUD46frc4yxQWEm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51c2e49d-3c55-4876-9b32-a57ddc0c4e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8fpXfZF63bNyhcCVCJMzo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9102,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1407
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 82,
          "cache_read_input_tokens": 9102,
          "cache_creation_input_tokens": 1407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1407,
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

_source line 8 · 2026-05-10T19:46:40.729Z_

<details><summary>↩ Tool result · `toolu_01GuzfBKQeshEbW5DiRND69A`</summary>

```text
Web search results for query: "test-time adaptation diffusion policy robustness robot 2025 2026"

Links: [{"title":"Everything to the Synthetic: Diffusion-driven Test-time Adaptation via","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Guo_Everything_to_the_Synthetic_Diffusion-driven_Test-time_Adaptation_via_Synthetic-Domain_Alignment_CVPR_2025_paper.pdf"},{"title":"Flexible Locomotion Learning with Diffusion Model Predictive Control","url":"https://arxiv.org/pdf/2510.04234"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"[2510.01068] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/abs/2510.01068"},{"title":"Frontiers | Research on the robustness of the open-world test-time training model","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1621025/full"},{"title":"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/html/2510.01068v1"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising","url":"https://arxiv.org/pdf/2510.21991"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"}]

I've completed the web search for your query on test-time adaptation, diffusion policies, robustness, and robots in 2025-2026. Here are the key findings:

## Recent Research on Diffusion-Based Robot Policies with Test-Time Adaptation

**Test-Time Adaptation and Composition:**
Recent work has introduced "Compose Your Policies," a training-free method called General Policy Composition (GPC) that enhances performance by combining the distributional scores of multiple pre-trained policies via a convex combination and test-time search. Experiments on Robomimic, PushT, and RoboTwin benchmarks alongside real-world robotic evaluations confirm that GPC consistently improves performance and adaptability across a diverse set of tasks.

**Flexible Test-Time Adaptation in Locomotion:**
Diffusion-MPC leverages a learned generative diffusion model as an approximate dynamics prior for planning, enabling flexible test-time adaptation through reward and constraint based optimization. This approach can adapt its behavior at test time to new joint constraints, heights, and terrains.

**Robustness of Diffusion Policies:**
Diffusion Policy's robustness against visual and physical perturbations has been demonstrated: when the front camera was blocked, the policy remained on-course; when the T block was shifted, the diffusion policy immediately re-planned; and when the T block was moved, the policy immediately changed course to adjust the target.

**Broader Applications:**
Diffusion models leverage a probabilistic framework and stand out with their ability to model multi-modal distributions and their robustness to high-dimensional input and output spaces.

These recent developments highlight significant progress in making diffusion-based robot policies more adaptive and robust to real-world perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51c2e49d-3c55-4876-9b32-a57ddc0c4e4e",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "48271fbe-c61d-4316-a7a0-988317bfc9bb",
  "sourceToolAssistantUUID": "51c2e49d-3c55-4876-9b32-a57ddc0c4e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T19:46:44.244Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013c4ioyKsADokeGC7ZjLVE1`</summary>

```json
{
  "query": "spectral filtering SVD diffusion guidance robot manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48271fbe-c61d-4316-a7a0-988317bfc9bb",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTtneYP1ztJxNonzwcR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e32364a3-92c8-4c37-839c-c7fe9cd4e4ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Gv1VXPU3GdBtk8x2AdkUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 10509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1160,
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

_source line 10 · 2026-05-10T19:46:44.724Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F38ga4kFDjXxKiZqLAW9v1`</summary>

```json
{
  "query": "cross-modal guidance robot manipulation diffusion 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e32364a3-92c8-4c37-839c-c7fe9cd4e4ac",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTtneYP1ztJxNonzwcR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "681c3bad-efa5-4ed8-a127-f32ce70f38b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Gv1VXPU3GdBtk8x2AdkUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 10509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1160,
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

_source line 11 · 2026-05-10T19:46:45.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VYJZVcYVSdBPgw1H6NmqnT`</summary>

```json
{
  "query": "world model robustness geometric perturbation robot policy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "681c3bad-efa5-4ed8-a127-f32ce70f38b5",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTtneYP1ztJxNonzwcR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af0efd88-b934-4f14-9076-6f48362414fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Gv1VXPU3GdBtk8x2AdkUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 10509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1160,
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

_source line 12 · 2026-05-10T19:46:46.134Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014sT6ivjHoyJuVGsaQLkZaa`</summary>

```json
{
  "query": "inference-time guidance robot policy training-free 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af0efd88-b934-4f14-9076-6f48362414fa",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTtneYP1ztJxNonzwcR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f76b5cd-9897-4b06-bc3a-f5bd8a0cebb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Gv1VXPU3GdBtk8x2AdkUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 10509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1160,
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

_source line 13 · 2026-05-10T19:46:47.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cg8EFhDkaHVQgWK64gCdbi`</summary>

```json
{
  "query": "SVD diffusion model guidance spectral 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f76b5cd-9897-4b06-bc3a-f5bd8a0cebb8",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTtneYP1ztJxNonzwcR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ea2fd91-9552-4cde-abca-3edc4fba8141",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Gv1VXPU3GdBtk8x2AdkUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 10509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1160,
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

_source line 14 · 2026-05-10T19:46:47.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BTXrHRsvKindeGSWy4sagL`</summary>

```json
{
  "query": "ADPro adaptive diffusion policy test-time robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ea2fd91-9552-4cde-abca-3edc4fba8141",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTtneYP1ztJxNonzwcR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "225f3674-e024-42a2-b8d1-9c2b45fc8aec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Gv1VXPU3GdBtk8x2AdkUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 10509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1160,
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

_source line 15 · 2026-05-10T19:46:48.066Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QHMvYT1Y8cHfmLmQpREgdu`</summary>

```json
{
  "query": "TTPL test-time perturbation learning VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "225f3674-e024-42a2-b8d1-9c2b45fc8aec",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTtneYP1ztJxNonzwcR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b27be47-5413-4f0c-b690-0a509126383b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Gv1VXPU3GdBtk8x2AdkUQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 10509,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1160
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 10509,
          "cache_creation_input_tokens": 1160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1160,
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

_source line 16 · 2026-05-10T19:46:51.259Z_

<details><summary>↩ Tool result · `toolu_013c4ioyKsADokeGC7ZjLVE1`</summary>

```text
Web search results for query: "spectral filtering SVD diffusion guidance robot manipulation 2025 2026"

Links: [{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"SODA: Spectral Orthogonal Decomposition Adaptation for Diffusion Models","url":"https://openaccess.thecvf.com/content/WACV2025/papers/Zhang_SODA_Spectral_Orthogonal_Decomposition_Adaptation_for_Diffusion_Models_WACV_2025_paper.pdf"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"GitHub - mbreuss/diffusion-literature-for-robotics: Summary of key papers and blogs about diffusion models to learn about the topic. Detailed list of all published diffusion robotics papers. · GitHub","url":"https://github.com/mbreuss/diffusion-literature-for-robotics"},{"title":"Diffusion Trajectory-guided Policy for Long-horizon Robot Manipulation","url":"https://arxiv.org/html/2502.10040v1"},{"title":"Video Generators are Robot Policies - Columbia University","url":"https://videopolicy.cs.columbia.edu/assets/video_policy.pdf"},{"title":"[2504.08438] Diffusion Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/abs/2504.08438"},{"title":"Diffusion Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2504.08438v1"}]

Based on the search results, I found relevant research on diffusion models in robot manipulation from 2025-2026. Here are the key findings:

## Recent Research on Diffusion Models for Robot Manipulation

A comprehensive survey from 2025 provides a review of state-of-the-art diffusion models in robotic manipulation, including grasp learning, trajectory planning, and data augmentation.

### Diffusion Guidance Applications

Diffusion models have recently emerged as a promising approach in robotics, especially in robot manipulations, leveraging a probabilistic framework with ability to model multi-modal distributions and robustness to high-dimensional input and output spaces.

One recent approach uses trajectory-guided diffusion policy that leverages task-relevant trajectories to provide trajectory-level guidance, reducing error accumulation through a two-stage method that trains a generative vision-language model to create diffusion-based trajectories, then refines the imitation policy.

### SVD and Model Compression

In robot manipulation work from 2025, Singular Value Decomposition (SVD) is used to estimate layer importance as a common technique in model compression, with SVD providing singular values that capture significant components of weight matrices.

### Spectral Filtering in Diffusion Models

Research on SODA demonstrates that incorporating spectral tuning can further enhance performance in diffusion model adaptation.

The search results show active research in applying diffusion models to robotic manipulation tasks in 2025-2026, with particular focus on guidance mechanisms, model efficiency through decomposition techniques, and spectral optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e32364a3-92c8-4c37-839c-c7fe9cd4e4ac",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "4f02db77-bb6d-44a3-9f73-0da9fa53037b",
  "sourceToolAssistantUUID": "e32364a3-92c8-4c37-839c-c7fe9cd4e4ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T19:46:53.056Z_

<details><summary>↩ Tool result · `toolu_01F38ga4kFDjXxKiZqLAW9v1`</summary>

```text
Web search results for query: "cross-modal guidance robot manipulation diffusion 2025 2026"

Links: [{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"A framework for robotic manipulation tasks based on multiple zero shot models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-17015-z"},{"title":"Diffusion models for robotic manipulation: a survey - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40995149/"},{"title":"Diffusion Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2504.08438v1"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Multimodal Fusion and Vision-Language Models: A Survey for Robot Vision","url":"https://arxiv.org/pdf/2504.02477"}]

I found several relevant research results on cross-modal guidance, robot manipulation, and diffusion models from 2025-2026. Here's what the search revealed:

## Key Findings

### Diffusion Models for Robot Manipulation

Diffusion models leverage a probabilistic framework and stand out with their ability to model multi-modal distributions and their robustness to high-dimensional input and output spaces. Recent research from 2025 indicates that research efforts focus on various components of the diffusion process adapted to different tasks in the domain of robotic manipulation, with developed architectures integrating different or even multiple input modalities.

### Cross-Modal Integration Approaches

Natural language represents an additional input modality, which also enables the integration of foundation models, like large language models, into the workflow. Additionally, 3D diffuser actor integrates multi-modal representations to generate end-effector trajectories, combining with recent progress in multiview transformers that leverage foundation model features.

### Multimodal Fusion with Vision-Language-Action Models

A December 2025 survey on multimodal fusion found that hierarchical and late fusion architectures achieve the highest manipulation success and generalization, confirming the benefit of multi-level cross-modal integration, with diffusion-based decoders demonstrating superior cross-domain transfer and robustness compared to autoregressive heads.

### Recent 2025-2026 Work

TinyVLA incorporates a diffusion-based head module on top of a pretrained VLA to directly generate robotic actions. Furthermore, PointWorld is scaling 3D world models for in-the-wild robotic manipulation, representing cutting-edge research from 2026.

The search results indicate active and growing research in combining cross-modal guidance techniques with diffusion models for robot manipulation during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "681c3bad-efa5-4ed8-a127-f32ce70f38b5",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "ebe79f8d-d0d3-4107-b5cd-60d0825f005d",
  "sourceToolAssistantUUID": "681c3bad-efa5-4ed8-a127-f32ce70f38b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T19:46:53.462Z_

<details><summary>↩ Tool result · `toolu_01VYJZVcYVSdBPgw1H6NmqnT`</summary>

```text
Web search results for query: "world model robustness geometric perturbation robot policy 2026"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Mask World Model: Predicting What Matters for Robust Robot Policy Learning","url":"https://arxiv.org/html/2604.19683"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"WARPD – World-model Assisted Reactive Policy Diffusion | OpenReview","url":"https://openreview.net/forum?id=OS9eo7NQeO"},{"title":"Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics","url":"https://arxiv.org/html/2501.10100v1"},{"title":"[2501.10100] Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics","url":"https://arxiv.org/abs/2501.10100"},{"title":"Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness","url":"https://arxiv.org/html/2603.21017v1"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"GitHub - leggedrobotics/robotic_world_model: Repository for our papers: Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics and Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots · GitHub","url":"https://github.com/leggedrobotics/robotic_world_model"},{"title":"Strengthening Generative Robot Policies through Predictive World Modeling","url":"https://arxiv.org/html/2502.00622v1"}]

I've completed the web search for your query on "world model robustness geometric perturbation robot policy 2026". Here are the key findings:

## Recent Research on World Model Robustness and Robot Policy

The search retrieved several highly relevant 2026 papers addressing world model robustness under geometric perturbations:

### OA-WAM: Object-Addressable World Action Model
Explicitly organizing a world model as addressable object states is an effective path toward more robust robot manipulation under scene perturbations. OA-WAM specifically degrades geometric axes while leaving LIBERO essentially unchanged—offering a verifiable design path toward world-action models that stay stable when scenes are geometrically rearranged while target identity is preserved.

### Mask World Model (MWM)
The Mask World Model leverages video diffusion architectures to predict the evolution of semantic masks instead of pixels, imposing a geometric information bottleneck that forces the model to capture essential physical dynamics and contact relations while filtering out visual noise.

### WAM vs VLA Robustness Comparison
World Action Models (WAMs) generally demonstrate strong robustness to noise, lighting and layout perturbations in both single-arm and bimanual settings, with this robustness believed to be at least partially attributable to the spatiotemporal priors inherited from their world model backbones.

### Additional Approaches
Shared representations between policy and world model capture robust geometric priors, empowering the world model to actively assist when physical observations become unreliable.

These papers represent cutting-edge work from March-May 2026 on improving world model robustness specifically under geometric perturbations for robotic manipulation and control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af0efd88-b934-4f14-9076-6f48362414fa",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "62aaabcd-4b62-4788-be23-7402f7f2325f",
  "sourceToolAssistantUUID": "af0efd88-b934-4f14-9076-6f48362414fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T19:46:54.589Z_

<details><summary>↩ Tool result · `toolu_01Cg8EFhDkaHVQgWK64gCdbi`</summary>

```text
Web search results for query: "SVD diffusion model guidance spectral 2025 2026"

Links: [{"title":"Stable Video Diffusion XT | Open Laboratory","url":"https://openlaboratory.com/models/svd-xt/"},{"title":"Spectral Analysis of Diffusion Models with Application to Schedule Design | OpenReview","url":"https://openreview.net/forum?id=ymmY3rrD1t"},{"title":"A diffusion model for hyperspectral and multispectral fusion guided by prior knowledge - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1569843225005709"},{"title":"Conditional guided diffusion model in latent space for social recommendation | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-026-07094-4"},{"title":"GitHub - hanjq17/Spectrum: [CVPR 2026] Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration · GitHub","url":"https://github.com/hanjq17/Spectrum"},{"title":"NeurIPS Poster Spectral Analysis of Diffusion Models with Application to Schedule Design","url":"https://neurips.cc/virtual/2025/poster/115111"},{"title":"Full article: S2TDM: Spatial-spectral transformer-based diffusion model for hyperspectral image denoising","url":"https://www.tandfonline.com/doi/full/10.1080/10095020.2025.2591277"},{"title":"Spectral Regularization for Diffusion Models","url":"https://arxiv.org/html/2603.02447v1"},{"title":"A Spectral Variability and Class-Constrained Diffusion Model for Unsupervised Hyperspectral Unmixing","url":"https://www.mdpi.com/2072-4292/18/10/1483"},{"title":"Stable Video Diffusion (SVD)","url":"https://www.emergentmind.com/topics/stable-video-diffusion-svd"}]

Based on the search results, I found several relevant papers and research from 2025-2026 related to spectral analysis and diffusion models:

## Spectral Analysis of Diffusion Models

A paper published in September 2025 offers a novel analysis of diffusion model inference with a frequency response perspective, presenting the inference process as a closed-form spectral transfer function that captures how the generated signal evolves in response to initial noise. The spectral analysis can be leveraged to design a noise schedule that aligns effectively with data characteristics.

## Spectral Regularization for Diffusion Models

Recent work on spectral regularization notes that while diffusion models are typically trained using pointwise reconstruction losses in the signal domain, these objectives are agnostic to the spectral and multi-scale structure characterizing many natural signals. One approach retains standard pixel- or waveform-space diffusion and applies wavelet regularization purely at the loss level.

## Spectral Feature Forecasting (CVPR 2026)

Spectrum is a training-free spectral diffusion feature forecaster that enables global, long-range feature reuse by viewing latent features of the denoiser as functions over time and approximating them with Chebyshev polynomials. Extensive experiments on various state-of-the-art image and video diffusion models verify the approach's superiority, achieving up to 4.67× speedup while maintaining higher sample quality.

## SVD and Guidance

For SVD-XT's image-to-video pathway, a variant of classifier-free guidance is incorporated where the guidance scale increases across generated frames, effectively reducing artifacts such as color oversaturation or temporal inconsistencies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ea2fd91-9552-4cde-abca-3edc4fba8141",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "d09e4fce-c75b-4e88-bbff-083474520b5d",
  "sourceToolAssistantUUID": "6ea2fd91-9552-4cde-abca-3edc4fba8141",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T19:46:54.798Z_

<details><summary>↩ Tool result · `toolu_014sT6ivjHoyJuVGsaQLkZaa`</summary>

```text
Web search results for query: "inference-time guidance robot policy training-free 2025 2026"

Links: [{"title":"[2502.00622] Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling","url":"https://arxiv.org/abs/2502.00622"},{"title":"Inference-Time Policy Steering through Human Interactions","url":"https://yanweiw.github.io/itps/"},{"title":"Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling","url":"https://arxiv.org/html/2502.00622v3"},{"title":"GEN-1: Scaling Embodied Foundation Models to Mastery - Generalist AI","url":"https://generalistai.com/blog/apr-02-2026-GEN-1"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"[2506.14287] Steering Robots with Inference-Time Interactions","url":"https://arxiv.org/abs/2506.14287"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Proceedings of Machine Learning Research vol 283:1–14, 2025","url":"https://arxiv.org/pdf/2412.09342"},{"title":"Steering Robots with Inference-Time Interactions","url":"https://arxiv.org/pdf/2506.14287"},{"title":"arXiv:2506.21427v1 [cs.LG] 26 Jun 2025","url":"https://dr.lib.iastate.edu/server/api/core/bitstreams/7700bc60-e412-4db4-9ed3-e170be9828a8/content"}]

Based on the search results, here are the key findings related to inference-time guidance for robot policy training-free approaches in 2025-2026:

## Key Research Areas

**Inference-Time Enhancement & Guidance:**

GPC (Generative Predictive Control) is an inference-time method for improving pretrained behavior-cloning policies without retraining, while it augments a frozen diffusion policy at deployment by coupling it with a predictive world model.

The Inference-Time Policy Steering (ITPS) framework uses human interactions to bias the generative sampling process instead of fine-tuning the policy on interaction data. ITPS evaluates six sampling strategies including Random Sampling, Output Perturbation, Post-Hoc Ranking, Biased Initialization, Guided Diffusion, and Guided Stochastic Sampling.

**Training-Free Policy Control:**

Research proposes inference-time steering, which leverages user interactions to switch between discrete skills, and task and motion imitation, which enables user interactions to edit continuous motions while satisfying task constraints.

**Foundation Model Advances:**

GEN-1 comprises innovations across pre-training advances, post-training techniques, learning from experience (RL), multimodal human guidance, as well as new inference-time techniques.

These approaches represent significant progress in enabling robot policies to be improved and guided at inference time without requiring additional training or retraining cycles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f76b5cd-9897-4b06-bc3a-f5bd8a0cebb8",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "40eaa177-a46b-40a7-845a-946edd4822d7",
  "sourceToolAssistantUUID": "2f76b5cd-9897-4b06-bc3a-f5bd8a0cebb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T19:46:54.891Z_

<details><summary>↩ Tool result · `toolu_01BTXrHRsvKindeGSWy4sagL`</summary>

```text
Web search results for query: "ADPro adaptive diffusion policy test-time robustness"

Links: [{"title":"ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/html/2508.06266"},{"title":"ADPro: a Test-time Adaptive Diffusion Policy for Robot Manipulation via Manifold and Initial Noise Constraints","url":"https://arxiv.org/html/2508.06266v1"},{"title":"[2508.06266] ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/abs/2508.06266"},{"title":"ADPro: a Test-time Adaptive Diffusion Policy for Robot ...","url":"https://www.alphaxiv.org/overview/2508.06266v1"},{"title":"Adaptive Diffusion Denoised Smoothing : Certified Robustness via Randomized Smoothing with Differentially Private Guided Denoising Diffusion","url":"https://arxiv.org/html/2507.08163v1"},{"title":"On Pitfalls of Test-Time Adaptation","url":"https://proceedings.mlr.press/v202/zhao23d/zhao23d.pdf"},{"title":"In Search of Lost Online Test-Time Adaptation: A Survey | International Journal of Computer Vision | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11263-024-02213-5"},{"title":"awesome-test-time-adaptation/TTA-TTBA.md at main · tim-learn/awesome-test-time-adaptation","url":"https://github.com/tim-learn/awesome-test-time-adaptation/blob/main/TTA-TTBA.md"},{"title":"A Comprehensive Survey on Test-Time Adaptation under ...","url":"https://arxiv.org/pdf/2303.15361"},{"title":"Evaluating the Adversarial Robustness of Adaptive Test-time Defenses","url":"https://proceedings.mlr.press/v162/croce22a/croce22a.pdf"}]

Based on the search results, here's information about ADPro:

## ADPro: Adaptive Diffusion Policy for Robotic Manipulation

ADPro proposes incorporating task-specific constraints and a priori knowledge at test time, enabling a learned diffusion policy to dynamically adapt to task structure without retraining.

### Key Components

The method introduces two main inductive biases:

1. **Manifold-constrained Denoising**: Guiding the denoising process along known geometric or control-relevant manifolds (e.g., object-relative poses, contact trajectories) helps the model avoid implausible regions of the action space, resulting in more efficient inference and improved success rates.

2. **Task-aware Initialization**: To reduce unnecessary exploration and accelerate convergence, an analytically guided initialization is proposed: rather than sampling from an uninformative prior, a rough registration between the gripper and target scenes is computed to propose a structured initial noisy action.

### Test-Time Robustness and Adaptation

Test-time adaptation transforms a general-purpose policy into a task-specialized one on-the-fly, improving both robustness and sample efficiency. ADP is compatible with pre-trained diffusion policies and requires no retraining, enabling test-time adaptation that tailors the policy to specific tasks, thereby enhancing generalization across novel tasks and environments.

### Performance Results

Experiments on RLBench, CALVIN, and real-world datasets show that ADPro improves success rates, generalization, and sampling efficiency, achieving up to 25% faster execution and 9% points over strong diffusion baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "225f3674-e024-42a2-b8d1-9c2b45fc8aec",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "e980475c-5247-4e98-b267-b53105916dff",
  "sourceToolAssistantUUID": "225f3674-e024-42a2-b8d1-9c2b45fc8aec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:46:55.606Z_

<details><summary>↩ Tool result · `toolu_01QHMvYT1Y8cHfmLmQpREgdu`</summary>

```text
Web search results for query: "TTPL test-time perturbation learning VLA 2026"

Links: [{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for","url":"https://arxiv.org/pdf/2604.18107"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.18107"},{"title":"Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of...","url":"https://openreview.net/forum?id=p1UF73ZvE0"},{"title":"Test-Time RL for VLAs","url":"https://www.emergentmind.com/topics/test-time-reinforcement-learning-for-vlas-tt-vla"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"[2602.15873] Test-Time Adaptation for Tactile-Vision-Language Models","url":"https://arxiv.org/abs/2602.15873"},{"title":"[2504.16084] TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2504.16084"},{"title":"TTRL: Test-Time Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=VuVhgEiu20"}]

I found relevant information about TTPL test-time perturbation learning for VLAs. Here are the key findings:

## PDF: Perturbation Learning with Delayed Feedback

The primary research on this topic is Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model.

### The Problem It Addresses

Vision-Language-Action models (VLAs) achieve remarkable performance in sequential decision-making but remain fragile to subtle environmental shifts, such as small changes in object pose, with this brittleness attributed to trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns.

### Key Components

PDF mitigates the spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. Additionally, PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issue.

### Performance Results

Experiments on LIBERO (+7.4% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success over vanilla VLA and VLA with test-time adaptation.

This research was published recently (April 2026) and represents a practical approach to improving VLA robustness through test-time perturbation learning without requiring model retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b27be47-5413-4f0c-b690-0a509126383b",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "79721690-b755-480b-8692-83003ac5f1a4",
  "sourceToolAssistantUUID": "2b27be47-5413-4f0c-b690-0a509126383b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T19:46:58.412Z_

Let me do a few more targeted searches to get precise details on the most relevant competing papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79721690-b755-480b-8692-83003ac5f1a4",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTutEviszhHpa6Er7fh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03defc9b-174b-46e5-b597-5381c879681f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA9NwuLga2mCJC7wH4XKDz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6999,
      "cache_read_input_tokens": 11669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6999,
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

_source line 24 · 2026-05-10T19:46:59.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AVkMs6jzMRZmN4PK7rZtHB`</summary>

```json
{
  "query": "DiffStateGrad diffusion state gradient guidance robot 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03defc9b-174b-46e5-b597-5381c879681f",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTutEviszhHpa6Er7fh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4114034-c4a7-4603-b83e-3a81b351908a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA9NwuLga2mCJC7wH4XKDz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6999,
      "cache_read_input_tokens": 11669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6999,
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

_source line 25 · 2026-05-10T19:47:00.451Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KimmoCAeKo4uPgdimDTaW4`</summary>

```json
{
  "query": "\"Dreaming the Unseen\" world model diffusion policy robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4114034-c4a7-4603-b83e-3a81b351908a",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTutEviszhHpa6Er7fh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4df9358b-d656-4fec-ba02-33a26449fc3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA9NwuLga2mCJC7wH4XKDz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6999,
      "cache_read_input_tokens": 11669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6999,
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

_source line 26 · 2026-05-10T19:47:01.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TKB8mQ7r5MbwuXf44GAiJ2`</summary>

```json
{
  "query": "WARPD world-model assisted reactive policy diffusion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4df9358b-d656-4fec-ba02-33a26449fc3a",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTutEviszhHpa6Er7fh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b093cdb-3ed3-4def-9006-8f95753508f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA9NwuLga2mCJC7wH4XKDz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6999,
      "cache_read_input_tokens": 11669,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6999
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 11669,
          "cache_creation_input_tokens": 6999,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6999,
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

_source line 27 · 2026-05-10T19:47:05.914Z_

<details><summary>↩ Tool result · `toolu_01AVkMs6jzMRZmN4PK7rZtHB`</summary>

```text
Web search results for query: "DiffStateGrad diffusion state gradient guidance robot 2025"

Links: [{"title":"GitHub - Anima-Lab/DiffStateGrad: DiffStateGrad [ICLR 2025]","url":"https://github.com/Anima-Lab/DiffStateGrad"},{"title":"Diffusion State-Guided Projected Gradient for Inverse Problems","url":"https://diffstategrad.github.io/"},{"title":"DIFFUSION STATE-GUIDED PROJECTED GRADIENT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5b7f7a0603b75e39ffebbf95e3b7ee-Paper-Conference.pdf"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"[2410.03463] Diffusion State-Guided Projected Gradient for Inverse Problems","url":"https://arxiv.org/abs/2410.03463"},{"title":"Diffusion State-Guided Projected Gradient for Inverse Problems","url":"https://arxiv.org/html/2410.03463"},{"title":"Diffusion State-Guided Projected Gradient for Inverse Problems | OpenReview","url":"https://openreview.net/forum?id=kRBQwlkFSP"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"Gradient Diffusion Strategy","url":"https://www.emergentmind.com/topics/gradient-diffusion-strategy"}]

Based on the search results, here's what I found about DiffStateGrad:

## Overview

DiffStateGrad is a paper accepted to ICLR 2025 by authors Rayhan Zirvi, Bahareh Tolooshams, and Anima Anandkumar. The work focuses on enhancing diffusion models for solving inverse problems, not specifically for robotics applications.

## Core Concept

DiffStateGrad is a novel approach that enhances diffusion-based inverse problem solvers by projecting measurement guidance gradients onto a data-driven low-rank subspace defined by intermediate diffusion states. The projection is achieved by performing singular value decomposition (SVD) on the diffusion state of an image to which guidance is applied and using the highest contributing singular vectors as the projection matrix.

## Key Benefits

DiffStateGrad projects the measurement gradient onto a subspace that captures statistics of the diffusion state, which helps the process stay closer to the data manifold during the diffusion process, resulting in better posterior sampling. DiffStateGrad improves the robustness of diffusion models in terms of the choice of measurement guidance step size and noise, and demonstrates improved performance on linear and nonlinear image restoration inverse problems.

## Note on Robotics

While the search results include information about diffusion models in robotics more broadly, DiffStateGrad itself is specifically designed for image restoration and inverse problems, not for robot control or manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4114034-c4a7-4603-b83e-3a81b351908a",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "fb12a652-f3cf-4943-8f0d-7fe1904a4970",
  "sourceToolAssistantUUID": "a4114034-c4a7-4603-b83e-3a81b351908a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T19:47:07.279Z_

<details><summary>↩ Tool result · `toolu_01KimmoCAeKo4uPgdimDTaW4`</summary>

```text
Web search results for query: ""Dreaming the Unseen" world model diffusion policy robustness 2026"

Links: [{"title":"Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness","url":"https://arxiv.org/html/2603.21017v1"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion","url":"https://www.researchgate.net/publication/384857010_Diffusion_policy_Visuomotor_policy_learning_via_action_diffusion"},{"title":"Alois Knoll's research works | Technical University of Munich and other places","url":"https://www.researchgate.net/scientific-contributions/60613465_Alois_Knoll"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/Awesome-World-Models"},{"title":"One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion","url":"https://arxiv.org/html/2505.18780v1"},{"title":"Multimodal Dreaming: A Global Workspace Approach to World Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2502.21142v2"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"World Models via Policy-Guided Trajectory Diffusion | OpenReview","url":"https://openreview.net/forum?id=9CcgO0LhKG"},{"title":"Probabilistic Dreaming for World Models","url":"https://arxiv.org/html/2603.04715v1"}]

Based on the search results, I found relevant information about "Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness."

## Summary

Diffusion policies excel at visuomotor control but often fail catastrophically under severe out-of-distribution (OOD) disturbances, such as unexpected object displacements or visual corruptions. To address this vulnerability, the researchers introduce the Dream Diffusion Policy (DDP), a framework that deeply integrates a diffusion world model into the policy's training objective via a shared 3D visual encoder.

When encountering sudden OOD anomalies during inference, DDP detects the real-imagination discrepancy and actively abandons the corrupted visual stream. Instead, it relies on its internal "imagination"—autoregressively forecasted latent dynamics—to safely bypass the disruption, generating imagined trajectories before smoothly realigning with physical reality.

DDP tightly couples a diffusion policy with a predictive world model via a shared 3D visual encoder. As the policy learns standard behavior cloning, the world model simultaneously predicts future observation latents. This shared representation captures robust geometric priors, empowering the world model to actively assist when physical observations become unreliable.

The models were trained for 500 epochs with 3 seeds using a fixed dataset of 50 demonstrations per task. Extensive evaluations demonstrate DDP's exceptional resilience.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4df9358b-d656-4fec-ba02-33a26449fc3a",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "09bd271b-6e6f-4020-b8a8-77d2bb0cced4",
  "sourceToolAssistantUUID": "4df9358b-d656-4fec-ba02-33a26449fc3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T19:47:08.416Z_

<details><summary>↩ Tool result · `toolu_01TKB8mQ7r5MbwuXf44GAiJ2`</summary>

```text
Web search results for query: "WARPD world-model assisted reactive policy diffusion 2026"

Links: [{"title":"WARPD – World-model Assisted Reactive Policy Diffusion | OpenReview","url":"https://openreview.net/forum?id=OS9eo7NQeO"},{"title":"WARPD: World model Assisted Reactive Policy Diffusion - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241014040H/abstract"},{"title":"WARPD: World model Assisted Reactive Policy Diffusion","url":"https://arxiv.org/html/2410.14040"},{"title":"[2410.14040] WARPD: World model Assisted Reactive Policy Diffusion","url":"https://arxiv.org/abs/2410.14040"},{"title":"WARPD: WORLD MODEL ASSISTED REACTIVE POLICY ...","url":"https://openreview.net/pdf/4e71c7593b59c0f34cd92f689ff5e4cd854fc331.pdf"},{"title":"World Models via Policy-Guided Trajectory Diffusion | OpenReview","url":"https://openreview.net/forum?id=9CcgO0LhKG"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"WMPO: World Model-based Policy Optimization for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=qE2FyvRvuF"},{"title":"[2509.19080] World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation","url":"https://arxiv.org/abs/2509.19080"},{"title":"World Models via Policy-Guided Trajectory Diffusion","url":"https://arxiv.org/html/2312.08533v4"}]

Based on the search results, here's what I found about WARPD:

## Overview

WARPD (World model Assisted Reactive Policy Diffusion) is a method that generates closed-loop policies (weights for neural policies) directly, instead of open-loop trajectories.

## Key Advantages

By learning behavioral distributions in parameter space rather than trajectory space, WARPD offers two major advantages: extended action horizons with robustness to perturbations while maintaining high task performance, and significantly reduced inference costs.

By generating closed-loop policies under learned dynamics, WARPD mitigates trajectory tracking errors, enabling policies to operate over extended time horizons with fewer diffusion queries. Additionally, closed-loop policies are reactive to environmental changes, ensuring WARPD-generated policies remain robust under stochastic disturbances.

## Performance Results

WARPD outperforms Diffusion Policy in long-horizon and perturbed environments, and achieves multitask performance on par with Diffusion Policy while requiring only approximately 1/45th of the inference-time FLOPs per step.

## Technical Approach

WARPD first encodes demonstration trajectories into a latent space, then learns their distribution using a diffusion model, and finally decodes them into policy weights via a hypernetwork. The generated policy is also optimized with model-based imitation learning using a co-trained world (dynamics) model.

The paper was submitted for review at ICLR 2026 and appears to have been recently accepted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b093cdb-3ed3-4def-9006-8f95753508f1",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "ac57742c17df894bb",
  "type": "user",
  "uuid": "a7dd802e-af98-45ca-b206-e6025ec65989",
  "sourceToolAssistantUUID": "9b093cdb-3ed3-4def-9006-8f95753508f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-10T19:47:45.117Z_

Here are the findings from all eight searches:

---

## Competing Work Report

### 1. Test-Time Adaptive Diffusion Policies

- **ADPro** (arXiv 2508.06266) -- Confirmed to exist. A test-time adaptive diffusion policy using manifold-constrained denoising and task-aware initialization. Training-free; improves success rates by up to 9 percentage points over diffusion baselines on RLBench, CALVIN, and real-world tasks. **Directly competing**: it is a training-free, inference-time method for improving diffusion policy robustness.

- **Compose Your Policies (GPC)** (arXiv 2510.01068) -- A training-free method that composes multiple pre-trained diffusion/flow policies at test time via distributional score combination and test-time search. Validated on Robomimic, PushT, RoboTwin, and real robots.

### 2. TTPL / PDF for VLAs

- **PDF: Perturbation Learning with Delayed Feedback** (arXiv 2604.18107, April 2026) -- Confirmed to exist (the paper the proposal likely refers to as "TTPL"). A verifier-free test-time adaptation framework for VLAs that uses uncertainty-based data augmentation, action voting, and a lightweight perturbation module. Achieves +7.4% success on LIBERO. **Directly relevant** as a competing test-time robustness method for embodied policies.

### 3. World Model Robustness Under Geometric Perturbations

- **OA-WAM: Object-Addressable World Action Model** (arXiv 2605.06481, May 2026) -- Organizes WAMs as addressable object states to improve robustness under geometric scene rearrangements. **Highly relevant**: directly targets WAM geometric robustness.

- **Mask World Model (MWM)** (arXiv 2604.19683, April 2026) -- Predicts semantic mask evolution instead of pixels via video diffusion, imposing a geometric information bottleneck. Filters visual noise while preserving physical dynamics.

- **"Do WAMs Generalize Better than VLAs?"** (arXiv 2603.22078, March 2026) -- A robustness study showing WAMs inherit spatiotemporal priors from world model backbones, giving them strong robustness to noise, lighting, and layout perturbations. **Must-cite** for any WAM robustness proposal.

- **Dream Diffusion Policy (DDP) / "Dreaming the Unseen"** (arXiv 2603.21017, March 2026) -- Integrates a diffusion world model into the policy via a shared 3D encoder. When OOD perturbations occur, the policy detects discrepancies and falls back to imagined latent dynamics. Addresses geometric robustness but requires training.

### 4. Inference-Time World-Model Guidance

- **Inference-Time Enhancement via Predictive World Modeling** (arXiv 2502.00622) -- Augments a frozen diffusion policy at deployment with a predictive world model, providing inference-time guidance without retraining. **Directly competing** with the "Spectral Cross-Modal Guidance" concept.

- **WARPD** (arXiv 2410.14040, ICLR 2026) -- Generates closed-loop policy weights via diffusion in parameter space, using a co-trained world model. Achieves robustness under perturbations with 1/45th inference FLOPs.

### 5. SVD/Spectral Methods in Diffusion Guidance

- **DiffStateGrad** (ICLR 2025) -- Uses SVD on intermediate diffusion states to project measurement gradients onto a low-rank subspace. Designed for image inverse problems, not robotics, but the core SVD-on-diffusion-state technique is closely related. The proposal should clarify differentiation.

- **Spectral Regularization for Diffusion Models** (arXiv 2603.02447, March 2026) -- Applies wavelet-domain spectral regularization to diffusion training losses. Not robotics-specific but relevant to the spectral filtering methodology.

### 6. No Direct Match Found

No paper combining SVD-based spectral filtering specifically with video-to-action cross-modal guidance in WAMs was found, suggesting the proposal's core contribution may be novel. However, the papers above collectively cover each component (SVD in diffusion guidance, inference-time WAM robustness, geometric perturbation handling), so the proposal should cite and differentiate from all of them.

**Key gaps in the proposal**: The WAM robustness study (arXiv 2603.22078), OA-WAM, DDP, and the inference-time world-model enhancement paper (arXiv 2502.00622) are the most critical potential omissions.

Sources:
- [ADPro](https://arxiv.org/abs/2508.06266)
- [Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068)
- [PDF: Perturbation Learning with Delayed Feedback](https://arxiv.org/abs/2604.18107)
- [OA-WAM](https://arxiv.org/html/2605.06481v1)
- [Mask World Model](https://arxiv.org/html/2604.19683)
- [Do WAMs Generalize Better than VLAs?](https://arxiv.org/html/2603.22078v1)
- [Dream Diffusion Policy (DDP)](https://arxiv.org/html/2603.21017v1)
- [Inference-Time Enhancement via Predictive World Modeling](https://arxiv.org/abs/2502.00622)
- [WARPD](https://arxiv.org/abs/2410.14040)
- [DiffStateGrad](https://arxiv.org/abs/2410.03463)
- [Spectral Regularization for Diffusion Models](https://arxiv.org/html/2603.02447v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7dd802e-af98-45ca-b206-e6025ec65989",
  "isSidechain": true,
  "agentId": "ac57742c17df894bb",
  "requestId": "req_011CauTvq4TbwDvL9yfSKMCv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a527d36-47b2-417d-a5a8-82eb058bff89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4qZoRNoVMnQGwQqyioVYJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2837,
      "cache_read_input_tokens": 18668,
      "output_tokens": 1465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2837
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1465,
          "cache_read_input_tokens": 18668,
          "cache_creation_input_tokens": 2837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2837,
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
