# Research conversation: Search the web to verify two papers: 1. "DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control" - claimed to be

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a514fa3ddfc20f678.jsonl`
- **Structured JSON:** [`75ad0c7a1411deff9b6f.json`](../../sessions/75/75ad0c7a1411deff9b6f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-14T03:07:50.995Z_

Search the web to verify two papers:

1. "DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control" - claimed to be NeurIPS 2024. Verify it exists, is at NeurIPS 2024, and that it demonstrates latent-space forward dynamics with pretrained encoders on LIBERO and real-robot tasks.

2. "DeFI: Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining" - claimed to be ICLR 2026. Verify it exists and shows that forward dynamics pretraining in DINO feature space transfers effectively to manipulation.

Use searches like:
- "DynaMo dynamics pretraining visuo-motor NeurIPS 2024 site:arxiv.org"
- "DeFI disentangled forward inverse dynamics pretraining ICLR 2026"
- "site:arxiv.org DynaMo in-domain dynamics pretraining"

Try to WebFetch the arxiv pages if found. Report specific findings about venue, methodology, and whether they support the claims made about them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "cc1e094b-7dcd-4fd1-8012-9c488382874f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T03:07:50.997Z_

```json
{
  "parentUuid": "cc1e094b-7dcd-4fd1-8012-9c488382874f",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
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
  "uuid": "4af73abf-de03-4732-8976-6ef35c1d8bae",
  "timestamp": "2026-05-14T03:07:50.997Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-14T03:07:53.778Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TGdWZtjhmUXZ3vepsWe83R`</summary>

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
  "parentUuid": "4af73abf-de03-4732-8976-6ef35c1d8bae",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1ixmkrAkjmuk2smvx95",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "686a12d8-1a1c-4f9c-bda3-de0183251650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNUfyUWPjU8snyXAMbDR78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 8223,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 803,
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

_source line 4 · 2026-05-14T03:07:53.781Z_

<details><summary>↩ Tool result · `toolu_01TGdWZtjhmUXZ3vepsWe83R`</summary>

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
  "parentUuid": "686a12d8-1a1c-4f9c-bda3-de0183251650",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "77a26596-b2f5-45a1-b313-28b402ecf7c5",
  "sourceToolAssistantUUID": "686a12d8-1a1c-4f9c-bda3-de0183251650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-14T03:07:56.749Z_



I'll search for both papers in parallel to verify the claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77a26596-b2f5-45a1-b313-28b402ecf7c5",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1ixyubEXtcehsBrpQQy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2160a376-d10b-4776-9d11-ea897b03b035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtwbTnQHnAAa8tK3thWg8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 6 · 2026-05-14T03:07:57.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pm8AKhN4oSatEtdx1P6qaQ`</summary>

```json
{
  "query": "DynaMo dynamics pretraining visuo-motor NeurIPS 2024 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2160a376-d10b-4776-9d11-ea897b03b035",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1ixyubEXtcehsBrpQQy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baaf3069-3fc0-4708-8ba5-50a30d276568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtwbTnQHnAAa8tK3thWg8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 7 · 2026-05-14T03:07:57.686Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RGa8epJ7bh1AGkpFYZBV5D`</summary>

```json
{
  "query": "site:arxiv.org DynaMo in-domain dynamics pretraining"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baaf3069-3fc0-4708-8ba5-50a30d276568",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1ixyubEXtcehsBrpQQy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9870c1a-92ee-4b3f-9e5a-415112cf7e40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtwbTnQHnAAa8tK3thWg8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 8 · 2026-05-14T03:07:58.156Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013d64jTFmaNtJ9ssJFjLaMf`</summary>

```json
{
  "query": "DeFI disentangled forward inverse dynamics pretraining ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9870c1a-92ee-4b3f-9e5a-415112cf7e40",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1ixyubEXtcehsBrpQQy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee74cf8a-f0b7-463a-88c4-75d37a01a195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtwbTnQHnAAa8tK3thWg8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 9 · 2026-05-14T03:07:58.602Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F5MnKnLUn74RBwFd7TshQx`</summary>

```json
{
  "query": "\"DeFI\" \"disentangled\" \"forward and inverse dynamics\" pretraining robot site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee74cf8a-f0b7-463a-88c4-75d37a01a195",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1ixyubEXtcehsBrpQQy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74c29036-a3ff-471d-8c68-cfe882bc05d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtwbTnQHnAAa8tK3thWg8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9026,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 258,
          "cache_read_input_tokens": 9026,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

_source line 10 · 2026-05-14T03:08:03.318Z_

<details><summary>↩ Tool result · `toolu_01Pm8AKhN4oSatEtdx1P6qaQ`</summary>

```text
Web search results for query: "DynaMo dynamics pretraining visuo-motor NeurIPS 2024 site:arxiv.org"

Links: [{"title":"[2409.12192] DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://arxiv.org/abs/2409.12192"},{"title":"DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://arxiv.org/html/2409.12192v1"},{"title":"[2409.12192v1] DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://arxiv.org/abs/2409.12192v1"},{"title":"villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models","url":"https://arxiv.org/html/2507.23682"},{"title":"Computer Science Sep 2024","url":"http://arxiv.org/list/cs/2024-09?skip=5210&show=10"},{"title":"Computer Vision and Pattern Recognition Sep 2024","url":"https://www.arxiv.org/list/cs.CV/2024-09?skip=2250&show=10"},{"title":"Boosting Action-Information via a Variational Bottleneck on Unlabelled Robot Videos","url":"https://arxiv.org/html/2508.08743v1"},{"title":"Midway Network: Learning Representations for Recognition and Motion from Latent Dynamics","url":"https://arxiv.org/html/2510.05558v1"},{"title":"Latent Diffusion Planning for Imitation Learning","url":"https://arxiv.org/html/2504.16925v1"},{"title":"3D-CAVLA: Leveraging Depth and 3D Context to Generalize Vision–Language Action Models for Unseen Tasks","url":"https://arxiv.org/html/2505.05800v1"}]

I found the paper! Here's what I found about DynaMo:

## DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control

DynaMo is a new in-domain, self-supervised method for learning visual representations. Given a set of expert demonstrations, it jointly learns a latent inverse dynamics model and a forward dynamics model over a sequence of image embeddings, predicting the next frame in latent space, without augmentations, contrastive sampling, or access to ground truth actions.

Imitation learning has proven to be a powerful tool for training complex visuomotor policies. However, current methods often require hundreds to thousands of expert demonstrations to handle high-dimensional visual observations. Importantly, DynaMo does not require any out-of-domain data such as Internet datasets or cross-embodied datasets.

According to the search results, DynaMo was presented at the Advances in Neural Information Processing Systems 38 (NeurIPS 2024) conference held in Vancouver, BC, Canada, December 10-15, 2024.

The paper is available on arXiv as paper 2409.12192, authored by Zichen Jeff Cui, Hengkai Pan, Aadhithya Iyer, Siddhant Haldar, and Lerrel Pinto.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baaf3069-3fc0-4708-8ba5-50a30d276568",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "8384a8cd-17c1-43f4-b8bb-e5bb9074e34e",
  "sourceToolAssistantUUID": "baaf3069-3fc0-4708-8ba5-50a30d276568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T03:08:04.304Z_

<details><summary>↩ Tool result · `toolu_01F5MnKnLUn74RBwFd7TshQx`</summary>

```text
Web search results for query: ""DeFI" "disentangled" "forward and inverse dynamics" pretraining robot site:arxiv.org"

Links: [{"title":"Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://arxiv.org/html/2604.16391v1"},{"title":"[2604.16391] Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://arxiv.org/abs/2604.16391"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"LA-Pose: Latent Action Pretraining Meets Pose Estimation","url":"https://arxiv.org/html/2604.27448"},{"title":"Train Robots in a JIF: Joint Inverse and Forward Dynamics with Human and Robot Demonstrations","url":"https://arxiv.org/html/2503.12297"},{"title":"Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation","url":"https://arxiv.org/html/2412.15109v1"},{"title":"Train Robots in a JIF: Joint Inverse and Forward Dynamics ...","url":"https://arxiv.org/pdf/2503.12297"},{"title":"[2503.12297] Train Robots in a JIF: Joint Inverse and Forward Dynamics with Human and Robot Demonstrations","url":"https://arxiv.org/abs/2503.12297"},{"title":"DEAR: Disentangled Environment and Agent Representations for Reinforcement Learning without Reconstruction","url":"https://arxiv.org/html/2407.00633v2"},{"title":"Inverse Dynamics Pretraining Learns Good","url":"https://arxiv.org/pdf/2305.16985"}]

I found the paper you were searching for! Here are the key results:

## Main Paper Found

**DeFI** is a novel framework that decouples visual forward and inverse dynamics pretraining to exploit respective data sources, wherein video generation and action prediction are disentangled.

### Key Components

The framework introduces the General Forward Dynamics Model (GFDM), pretrained on diverse human and robot videos for future prediction, and the General Inverse Dynamics Model (GIDM), trained via self-supervised learning to infer latent actions from unlabeled video transitions.

### Performance

DeFI achieves state-of-the-art performance, with an average task length of 4.51 for CALVIN, 51.2% success rate on SimplerEnv-Fractal benchmark and 81.3% success rate in real-world deployment.

### Publication Details

The paper is titled "Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining" and was published as a conference paper at ICLR 2026 (arXiv:2604.16391, dated March 27, 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74c29036-a3ff-471d-8c68-cfe882bc05d5",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "5d0555b0-a6c9-4d70-a2f0-930848afb82f",
  "sourceToolAssistantUUID": "74c29036-a3ff-471d-8c68-cfe882bc05d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T03:08:04.370Z_

<details><summary>↩ Tool result · `toolu_01RGa8epJ7bh1AGkpFYZBV5D`</summary>

```text
Web search results for query: "site:arxiv.org DynaMo in-domain dynamics pretraining"

Links: [{"title":"[2409.12192] DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://arxiv.org/abs/2409.12192"},{"title":"DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://arxiv.org/html/2409.12192v1"},{"title":"[2409.12192v1] DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://arxiv.org/abs/2409.12192v1"},{"title":"OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation","url":"https://arxiv.org/html/2505.20425v1"},{"title":"Boosting Action-Information via a Variational Bottleneck on Unlabelled Robot Videos","url":"https://arxiv.org/html/2508.08743v1"},{"title":"3D-CAVLA: Leveraging Depth and 3D Context to Generalize Vision–Language Action Models for Unseen Tasks","url":"https://arxiv.org/html/2505.05800v1"},{"title":"CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://arxiv.org/html/2508.01600v1"},{"title":"Computer Science Sep 2024","url":"https://arxiv.org/list/cs/2024-09?skip=5210&show=500"},{"title":"Computer Vision and Pattern Recognition Sep 2024","url":"https://www.arxiv.org/list/cs.CV/2024-09?skip=2250&show=10"},{"title":"villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models","url":"https://arxiv.org/html/2507.23682"}]

Based on the search results, here's what I found:

## DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control

DynaMo is a new in-domain, self-supervised method for learning visual representations. The paper was published on arXiv as paper 2409.12192 by Zichen Jeff Cui and colleagues.

### Key Features:

Given a set of expert demonstrations, the method jointly learns a latent inverse dynamics model and a forward dynamics model over a sequence of image embeddings, predicting the next frame in latent space, without augmentations, contrastive sampling, or access to ground truth actions.

Importantly, DynaMo does not require any out-of-domain data such as Internet datasets or cross-embodied datasets.

### Motivation:

Current imitation learning methods often require hundreds to thousands of expert demonstrations to handle high-dimensional visual observations, because visual representations are predominantly either pretrained on out-of-domain data or trained directly through a behavior cloning objective.

### Performance:

On a suite of six simulated and real environments, representations learned with DynaMo significantly improve downstream imitation learning performance over prior self-supervised learning objectives and pretrained representations. Gains from using DynaMo hold across policy classes such as Behavior Transformer, Diffusion Policy, MLP, and nearest neighbors.

The paper was updated on October 30, 2024, and is categorized under Robotics, Artificial Intelligence, Computer Vision and Pattern Recognition, and Machine Learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9870c1a-92ee-4b3f-9e5a-415112cf7e40",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "34f209a3-ec48-4936-aa2a-0bf217ee229d",
  "sourceToolAssistantUUID": "a9870c1a-92ee-4b3f-9e5a-415112cf7e40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T03:08:05.081Z_

<details><summary>↩ Tool result · `toolu_013d64jTFmaNtJ9ssJFjLaMf`</summary>

```text
Web search results for query: "DeFI disentangled forward inverse dynamics pretraining ICLR 2026"

Links: [{"title":"GitHub - LogosRoboticsGroup/DeFi: [ICLR 2026] Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining · GitHub","url":"https://github.com/LogosRoboticsGroup/DeFi"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining | OpenReview","url":"https://openreview.net/forum?id=DdrsHWobR1"},{"title":"ICLR Poster Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://iclr.cc/virtual/2026/poster/10010761"},{"title":"DISENTANGLED ROBOT LEARNING VIA SEPARATE FOR","url":"https://openreview.net/pdf/6c80995dd180bf48c385ce8de5f092461642f12b.pdf"},{"title":"[2604.16391] Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://arxiv.org/abs/2604.16391"},{"title":"Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://arxiv.org/html/2604.16391"},{"title":"Paper page - Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://huggingface.co/papers/2604.16391"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"Disentangled World Models: Learning to Transfer Semantic ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Disentangled_World_Models_Learning_to_Transfer_Semantic_Knowledge_from_Distracting_ICCV_2025_paper.pdf"}]

Based on the search results, here's what I found about DeFI:

## DeFI: Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining

DeFI is an ICLR 2026 paper on disentangled robot learning via separate forward and inverse dynamics pretraining.

### Framework Overview

DeFI is a novel framework that decouples visual forward and inverse dynamics pretraining to exploit respective data sources, wherein video generation and action prediction are disentangled.

### Key Components

The framework introduces the Foundation Forward Dynamics Model (FFDM), pretrained on diverse human and robot videos for future prediction, and the Foundation Inverse Dynamics Model (FIDM), trained via self-supervised learning to infer latent actions from unlabeled video transitions. These models are then integrated into a unified architecture for end-to-end finetuning on downstream tasks.

### Problem It Addresses

Vision-language-action (VLA) models face a dilemma regarding misalignment of 2D image forecasting and 3D action prediction, and such vision-action entangled training manner limits model learning from large-scale, action-free web video data.

### Performance Results

DeFI achieves an average task length of 4.51 for CALVIN, 51.2% success rate on SimplerEnv-Fractal benchmark and 81.3% success rate in real-world deployment, significantly outperforming prior methods.

The code and resources are available on GitHub at the LogosRoboticsGroup/DeFi repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee74cf8a-f0b7-463a-88c4-75d37a01a195",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "9fbb415d-f909-4d55-a248-80dbe8b5e6a5",
  "sourceToolAssistantUUID": "ee74cf8a-f0b7-463a-88c4-75d37a01a195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-14T03:08:08.579Z_

Now let me fetch the arxiv pages for both papers to get more detailed information about methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fbb415d-f909-4d55-a248-80dbe8b5e6a5",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1iyp52rmKqjM8y8q1it",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57bdb1bb-f1b4-49af-a477-278c8acd7744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Mn6AohMSu2bET1osG2H4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 761,
      "cache_creation_input_tokens": 2941,
      "cache_read_input_tokens": 10914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2941,
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

_source line 15 · 2026-05-14T03:08:11.076Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LTAVd2zNnDmFdmoNaxD7Dz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2409.12192",
  "prompt": "Extract the full abstract, authors, venue/conference information, and any details about the methodology (latent-space forward dynamics, pretrained encoders, LIBERO benchmark, real-robot tasks). Also note whether it mentions NeurIPS 2024."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57bdb1bb-f1b4-49af-a477-278c8acd7744",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1iyp52rmKqjM8y8q1it",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96f7a4f5-9f6e-46fb-936c-330095e676d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Mn6AohMSu2bET1osG2H4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 761,
      "cache_creation_input_tokens": 2941,
      "cache_read_input_tokens": 10914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2941,
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

_source line 16 · 2026-05-14T03:08:12.542Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RCSTW2xH7SAoLkyd8jimux`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.16391",
  "prompt": "Extract the full abstract, authors, venue/conference information, and any details about the methodology. Specifically, does it mention forward dynamics pretraining in DINO feature space? Does it mention transfer to manipulation tasks? Does it confirm ICLR 2026?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96f7a4f5-9f6e-46fb-936c-330095e676d7",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1iyp52rmKqjM8y8q1it",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04609944-50b0-4a8f-b3f6-9a4551e626cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Mn6AohMSu2bET1osG2H4s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 761,
      "cache_creation_input_tokens": 2941,
      "cache_read_input_tokens": 10914,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2941
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 761,
          "output_tokens": 276,
          "cache_read_input_tokens": 10914,
          "cache_creation_input_tokens": 2941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2941,
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

_source line 17 · 2026-05-14T03:08:17.824Z_

<details><summary>↩ Tool result · `toolu_01RCSTW2xH7SAoLkyd8jimux`</summary>

```text
# Research Paper Summary

**Title:** Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining

**Authors:** Wenyao Zhang, Bozhou Zhang, Zekun Qi, Wenjun Zeng, Xin Jin, Li Zhang

**Venue:** ICLR 2026 (confirmed)

## Abstract
The paper addresses misalignment between 2D image forecasting and 3D action prediction in Vision-Language-Action models. It proposes "DeFI," which "Decouples visual Forward and Inverse dynamics pretraining to exploit respective data sources."

## Methodology Details
The framework introduces two main components:
- **GFDM (General Forward Dynamics Model):** "pretrained on diverse human and robot videos for future prediction"
- **GIDM (General Inverse Dynamics Model):** "trained via self-supervised learning to infer latent actions from unlabeled video transitions"

## Key Findings
Performance results include 4.51 average task length on CALVIN ABC-D, 51.2% success rate on SimplerEnv-Fractal, and 81.3% success in real-world deployment.

## Notes on Your Specific Questions
- **DINO feature space:** Not mentioned in this abstract
- **Transfer to manipulation tasks:** The paper evaluates on CALVIN and SimplerEnv benchmarks but doesn't explicitly detail manipulation-specific transfer methodology in the excerpt provided
- **ICLR 2026:** Confirmed as listed under "Comments"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04609944-50b0-4a8f-b3f6-9a4551e626cf",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "7e35b32e-a923-462c-aabc-c873d33fc2f3",
  "sourceToolAssistantUUID": "04609944-50b0-4a8f-b3f6-9a4551e626cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T03:08:18.415Z_

<details><summary>↩ Tool result · `toolu_01LTAVd2zNnDmFdmoNaxD7Dz`</summary>

```text
# DynaMo Paper Analysis

## Full Abstract
"Imitation learning has proven to be a powerful tool for training complex visuomotor policies. However, current methods often require hundreds to thousands of expert demonstrations to handle high-dimensional visual observations. A key reason for this poor data efficiency is that visual representations are predominantly either pretrained on out-of-domain data or trained directly through a behavior cloning objective. In this work, we present DynaMo, a new in-domain, self-supervised method for learning visual representations. Given a set of expert demonstrations, we jointly learn a latent inverse dynamics model and a forward dynamics model over a sequence of image embeddings, predicting the next frame in latent space, without augmentations, contrastive sampling, or access to ground truth actions. Importantly, DynaMo does not require any out-of-domain data such as Internet datasets or cross-embodied datasets. On a suite of six simulated and real environments, we show that representations learned with DynaMo significantly improve downstream imitation learning performance over prior self-supervised learning objectives, and pretrained representations. Gains from using DynaMo hold across policy classes such as Behavior Transformer, Diffusion Policy, MLP, and nearest neighbors. Finally, we ablate over key components of DynaMo and measure its impact on downstream policy performance."

## Authors
Zichen Jeff Cui, Hengkai Pan, Aadhithya Iyer, Siddhant Haldar, Lerrel Pinto

## Venue/Conference Information
- **Preprint status**: arXiv:2409.12192 (submitted September 18, 2024; revised October 30, 2024)
- **Subject categories**: Robotics (cs.RO), Artificial Intelligence (cs.AI), Computer Vision (cs.CV), Machine Learning (cs.LG)
- **No mention of NeurIPS 2024** in the provided content

## Key Methodology Details
- **Latent-space dynamics**: The method learns both inverse and forward dynamics models operating on image embeddings in latent space
- **Self-supervised approach**: Predicts next frames without requiring augmentations, contrastive sampling, or ground truth actions
- **In-domain training**: Operates exclusively on expert demonstration data; no external datasets needed

## Environment Testing
The paper evaluates performance across "six simulated and real environments" but does not specifically mention the LIBERO benchmark or name particular real-robot tasks in the provided abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96f7a4f5-9f6e-46fb-936c-330095e676d7",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "cf8ddf49-8f0b-4482-b3f8-adc0a2c9f4a4",
  "sourceToolAssistantUUID": "96f7a4f5-9f6e-46fb-936c-330095e676d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T03:08:21.140Z_

Let me search for more specific details about DynaMo's use of LIBERO and about DeFI's use of DINO features.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf8ddf49-8f0b-4482-b3f8-adc0a2c9f4a4",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1iznypnJkJvpjwrn7n6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb22aba2-6e3e-4d1f-9de8-e4b0223b9f51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcLpJjJ1fD6GY9NmFtzQRZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 380,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 13855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1621,
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

_source line 20 · 2026-05-14T03:08:21.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AMzgW3HVSBrfQfPo3CQLoK`</summary>

```json
{
  "query": "DynaMo NeurIPS 2024 LIBERO benchmark Zichen Cui"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb22aba2-6e3e-4d1f-9de8-e4b0223b9f51",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1iznypnJkJvpjwrn7n6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c407e81-07b1-4b5a-9063-d2bc77d418ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcLpJjJ1fD6GY9NmFtzQRZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 380,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 13855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1621,
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

_source line 21 · 2026-05-14T03:08:22.360Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UkXRQjhsyGVCHCYNh4e4KJ`</summary>

```json
{
  "query": "DeFI DINO feature space forward dynamics pretraining \"2604.16391\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c407e81-07b1-4b5a-9063-d2bc77d418ab",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1iznypnJkJvpjwrn7n6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e229c9b4-ef88-4edc-aea6-bb14ddae3a74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcLpJjJ1fD6GY9NmFtzQRZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 380,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 13855,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1621
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 380,
          "output_tokens": 158,
          "cache_read_input_tokens": 13855,
          "cache_creation_input_tokens": 1621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1621,
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

_source line 22 · 2026-05-14T03:08:28.275Z_

<details><summary>↩ Tool result · `toolu_01AMzgW3HVSBrfQfPo3CQLoK`</summary>

```text
Web search results for query: "DynaMo NeurIPS 2024 LIBERO benchmark Zichen Cui"

Links: [{"title":"NeurIPS Poster DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://neurips.cc/virtual/2024/poster/93200"},{"title":"[Quick Review] DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://liner.com/review/dynamo-indomain-dynamics-pretraining-for-visuomotor-control"},{"title":"DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/3b8db54b629e00537b59cbc6612026d7-Abstract-Conference.html"},{"title":"NeurIPS Poster LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://neurips.cc/virtual/2023/poster/73415"},{"title":"DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control | Request PDF","url":"https://www.researchgate.net/publication/397200025_DynaMo_In-Domain_Dynamics_Pretraining_for_Visuo-Motor_Control"},{"title":"NeurIPS 2024 Datasets and Benchmarks Track | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2024%2FDatasets_and_Benchmarks_Track"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html"},{"title":"(PDF) DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control","url":"https://www.researchgate.net/publication/384116458_DynaMo_In-Domain_Dynamics_Pretraining_for_Visuo-Motor_Control"},{"title":"[PDF] DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DynaMo:-In-Domain-Dynamics-Pretraining-for-Control-Cui-Pan/cf3b71fe73e7b61ab807a92be7156c3075b2482f"},{"title":"NeurIPS 2024 Accepted Paper List: Datasets & Benchmarks Track - Paper Copilot","url":"https://papercopilot.com/paper-list/neurips-paper-list/neurips-2024-paper-list-datasets-benchmarks-track/"}]

Based on the search results, here's what I found:

## DynaMo at NeurIPS 2024

DynaMo is a paper by Zichen Cui, Hengkai Pan, Aadhithya Iyer, Siddhant Haldar, and Lerrel Pinto, presented as a 2024 Poster at NeurIPS.

### Overview

DynaMo is a new in-domain, self-supervised method for learning visual representations. It jointly learns a latent inverse dynamics model and a forward dynamics model over a sequence of image embeddings, predicting the next frame in latent space, without augmentations, contrastive sampling, or access to ground truth actions.

### Performance on LIBERO Benchmark

On the LIBERO benchmark, DynaMo achieves a score of 0.93, matching the best prior methods on LIBERO Goal. The method demonstrates strong performance across multiple simulated environments, with notable improvements on other benchmarks like Block Pushing and Push-T.

### Key Features

DynaMo does not require any out-of-domain data such as Internet datasets or cross-embodied datasets. Representations learned with DynaMo significantly improve downstream imitation learning performance over prior self-supervised learning objectives, and pretrained representations, with gains holding across policy classes such as Behavior Transformer, Diffusion Policy, MLP, and nearest neighbors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c407e81-07b1-4b5a-9063-d2bc77d418ab",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "292289fc-56c4-4f3d-9a09-a59b49412a7d",
  "sourceToolAssistantUUID": "3c407e81-07b1-4b5a-9063-d2bc77d418ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T03:08:30.136Z_

<details><summary>↩ Tool result · `toolu_01UkXRQjhsyGVCHCYNh4e4KJ`</summary>

```text
Web search results for query: "DeFI DINO feature space forward dynamics pretraining "2604.16391""

Links: [{"title":"Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://arxiv.org/html/2604.16391"},{"title":"[2604.16391] Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://arxiv.org/abs/2604.16391"},{"title":"GitHub - LogosRoboticsGroup/DeFi: [ICLR 2026] Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining · GitHub","url":"https://github.com/LogosRoboticsGroup/DeFi"},{"title":"Paper page - Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://huggingface.co/papers/2604.16391"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion","url":"https://arxiv.org/html/2604.01761"},{"title":"Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining | OpenReview","url":"https://openreview.net/forum?id=DdrsHWobR1"},{"title":"GitHub - IDEA-Research/GroundingDINO: [ECCV 2024] Official implementation of the paper \"Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection\" · GitHub","url":"https://github.com/IDEA-Research/GroundingDINO"},{"title":"DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning | OpenReview","url":"https://openreview.net/forum?id=GARbxyCV13"},{"title":"DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning","url":"https://dino-wm.github.io/"}]

Based on the search results, I found information about the paper you're looking for:

## DeFI: Disentangled Robot Learning

DeFI is a novel framework that Decouples visual Forward and Inverse dynamics pretraining to exploit respective data sources, wherein video generation and action prediction are disentangled.

### Key Components

The framework introduces the General Forward Dynamics Model (GFDM), pretrained on diverse human and robot videos for future prediction, and the General Inverse Dynamics Model (GIDM), trained via self-supervised learning to infer latent actions from unlabeled video transitions.

### Feature Space and Training

The framework adopts a Transformer architecture as the general inverse dynamics model and trains it in the DINO feature space to obtain semantically rich representations.

### Motivation and Results

Vision-language-action (VLA) models have shown great potential in building generalist robots, but still face a dilemma of misalignment of 2D image forecasting and 3D action prediction, and such a vision-action entangled training manner limits model learning from large-scale, action-free web video data.

Extensive experiments on CALVIN ABC-D and SimplerEnv demonstrate state-of-the-art performance, with DeFI achieving an average task length of 4.51 for CALVIN, 51.2% success rate on SimplerEnv-Fractal benchmark and 81.3% success rate in real-world deployment.

The paper (arXiv:2604.16391) was published at ICLR 2026 in March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e229c9b4-ef88-4edc-aea6-bb14ddae3a74",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "9636376a-c186-4f05-a6ca-d49ab29d8900",
  "sourceToolAssistantUUID": "e229c9b4-ef88-4edc-aea6-bb14ddae3a74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T03:08:33.840Z_

Now let me fetch the DynaMo NeurIPS proceedings page and the DeFI HTML page for more details about DINO usage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9636376a-c186-4f05-a6ca-d49ab29d8900",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1j1f6qVP8i8fSYCByDJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "196ff693-47ed-42f7-955f-478d8b47cb66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZfL1Tps8X23ioNL1ebYnu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 15476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 25 · 2026-05-14T03:08:35.320Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NiXPnRG34q2NPNH1gmekML`</summary>

```json
{
  "url": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/3b8db54b629e00537b59cbc6612026d7-Abstract-Conference.html",
  "prompt": "Confirm this is DynaMo at NeurIPS 2024, extract any details about LIBERO, real-robot tasks, pretrained encoders, and forward dynamics in latent space."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "196ff693-47ed-42f7-955f-478d8b47cb66",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1j1f6qVP8i8fSYCByDJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0bce589-fc76-489c-9dab-cb94bea2978b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZfL1Tps8X23ioNL1ebYnu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 15476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 26 · 2026-05-14T03:08:37.103Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CNuaxBQgSoHBGaCc9em8wP`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.16391",
  "prompt": "Look for mentions of DINO feature space in the forward dynamics pretraining. Does the paper explicitly state that forward dynamics pretraining happens in DINO feature space? Also look for details about transfer to manipulation tasks and the methodology of disentangling forward and inverse dynamics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0bce589-fc76-489c-9dab-cb94bea2978b",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1j1f6qVP8i8fSYCByDJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a753d18d-80b3-44dd-9b73-bcdf4cdb8d18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZfL1Tps8X23ioNL1ebYnu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 15476,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2559
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 15476,
          "cache_creation_input_tokens": 2559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2559,
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

_source line 27 · 2026-05-14T03:08:38.655Z_

<details><summary>↩ Tool result · `toolu_01NiXPnRG34q2NPNH1gmekML`</summary>

```text
# DynaMo at NeurIPS 2024 - Confirmed

Yes, this is indeed DynaMo presented at NeurIPS 2024 in the Main Conference Track.

## Key Details Found:

**Forward Dynamics in Latent Space:**
The method involves "jointly learn[ing] a latent inverse dynamics model and a forward dynamics model over a sequence of image embeddings, predicting the next frame in latent space, without augmentations, contrastive sampling, or access to ground truth actions."

**Real-Robot Tasks:**
The abstract confirms evaluation "on a suite of six simulated and real environments" with robot videos available at the project website.

**Pretrained Encoders:**
The approach contrasts with existing methods where "visual representations are predominantly either pretrained on out-of-domain data or trained directly through a behavior cloning objective." DynaMo requires "no out-of-domain data such as Internet datasets or cross-embodied datasets."

**LIBERO:**
No mention of LIBERO appears in the provided webpage content.

The work demonstrates improvements across multiple policy classes including Behavior Transformer, Diffusion Policy, MLP, and nearest neighbors approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0bce589-fc76-489c-9dab-cb94bea2978b",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "53f77224-0632-4d91-9970-e80fefad4209",
  "sourceToolAssistantUUID": "e0bce589-fc76-489c-9dab-cb94bea2978b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T03:08:42.394Z_

<details><summary>↩ Tool result · `toolu_01CNuaxBQgSoHBGaCc9em8wP`</summary>

```text
# Analysis of DeFI's Forward Dynamics Pretraining

## DINO Feature Space in Forward Dynamics

The paper does **not** explicitly state that forward dynamics pretraining occurs in DINO feature space. Instead, the General Forward Dynamics Model (GFDM) operates differently:

The GFDM uses "Stable Video Diffusion (SVD)" and works in latent video space through a video VAE, predicting future video frames directly. As stated, the model predicts "future video clips conditioned on the current observation and instruction."

## Inverse Dynamics in DINO Space

By contrast, the General Inverse Dynamics Model (GIDM) explicitly operates in DINO feature space: "we start with a pair of consecutive video frames...then extract a pair of latent states using the DINOv2 visual encoder."

## Disentanglement Strategy

The core disentanglement works as follows:

- **GFDM** learns motion regularities through video generation objectives on mixed human/robot data
- **GIDM** learns action inference through self-supervised reconstruction, also on mixed data but focusing on latent action representations

During fine-tuning, "the GFDM ℱθ is kept frozen" while "the GIDM ℐϕ is optimized to interpret these aligned latents and infer latent actions."

This separation allows each module to "specialize while still benefiting from heterogeneous data."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a753d18d-80b3-44dd-9b73-bcdf4cdb8d18",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "fc2c2f3b-49fa-4aea-9858-bad6c9726d7f",
  "sourceToolAssistantUUID": "a753d18d-80b3-44dd-9b73-bcdf4cdb8d18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T03:08:47.660Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xeu52W8yH5473HPUdsqQQH`</summary>

```json
{
  "url": "https://arxiv.org/html/2409.12192v1",
  "prompt": "Look for mentions of LIBERO benchmark/tasks, real-robot experiments, and whether pretrained visual encoders (like ResNet, ViT, DINO, etc.) are used as the backbone. What specific environments are tested? Does it use pretrained encoders that are then refined with forward dynamics?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc2c2f3b-49fa-4aea-9858-bad6c9726d7f",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1j2ZYVdXFmb8gW2hCeY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61db6003-260a-4b9c-99fb-f2f60c9111f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3aCHoqFzvh6ctgeYrVAnA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 963,
      "cache_read_input_tokens": 18035,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 963
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 18035,
          "cache_creation_input_tokens": 963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 963,
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

_source line 30 · 2026-05-14T03:08:53.969Z_

<details><summary>↩ Tool result · `toolu_01Xeu52W8yH5473HPUdsqQQH`</summary>

```text
# DynaMo: Key Experimental Details

## LIBERO Benchmark
DynaMo evaluates on **LIBERO Goal**, which consists of "10 manipulation tasks with a 7-dimensional action space simulated Franka arm and gripper" with 500 total demonstrations (50 per task). The method reports a 0.93 success rate, matching the best pretrained baseline.

## Real-Robot Experiments
The paper includes extensive real-world testing:
- **Allegro Manipulation**: Three contact-rich dexterous tasks (sponge picking, teabag picking, microwave opening) with 6-7 demonstrations each
- **xArm Kitchen**: Multi-task environment with five tasks across 65 total demonstrations

DynaMo achieves 43% improvement over baselines on Allegro and 20% on xArm Kitchen.

## Backbone Architecture
The method uses **ResNet18 as the primary backbone**, not pretrained vision models. Notably, "MAE-style baselines (VC-1, MVP, MAE) use a ViT-B backbone. All other baselines and DynaMo use a ResNet18 backbone."

## Pretraining Strategy
DynaMo trains the encoder **from random initialization** with inverse and forward dynamics models, without requiring pretrained weights. However, the paper shows DynaMo can also fine-tune ImageNet-pretrained ResNet18, achieving improvements in some tasks (Table 5).

The method explicitly does **not** rely on out-of-domain pretrained encoders, distinguishing it from approaches requiring Internet-scale datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61db6003-260a-4b9c-99fb-f2f60c9111f9",
  "isSidechain": true,
  "promptId": "31ff1a08-d809-4d14-ab4e-0388adfed88a",
  "agentId": "a514fa3ddfc20f678",
  "type": "user",
  "uuid": "5c04b55a-986d-4038-a247-3efea6e2e344",
  "sourceToolAssistantUUID": "61db6003-260a-4b9c-99fb-f2f60c9111f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T03:09:22.838Z_

I now have comprehensive information to provide a detailed verification report.

---

## Verification Report

### Paper 1: "DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control"

**Existence and Venue: CONFIRMED at NeurIPS 2024**

- The paper exists on arXiv as [2409.12192](https://arxiv.org/abs/2409.12192) and is officially published in the NeurIPS 2024 Main Conference proceedings at [proceedings.neurips.cc](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3b8db54b629e00537b59cbc6612026d7-Abstract-Conference.html).
- It was presented as a poster at NeurIPS 2024 in Vancouver (confirmed via [neurips.cc/virtual/2024/poster/93200](https://neurips.cc/virtual/2024/poster/93200)).
- Authors: Zichen Jeff Cui, Hengkai Pan, Aadhithya Iyer, Siddhant Haldar, Lerrel Pinto.

**Methodology Claims: PARTIALLY SUPPORTED**

- **Latent-space forward dynamics**: CONFIRMED. The paper jointly learns "a latent inverse dynamics model and a forward dynamics model over a sequence of image embeddings, predicting the next frame in latent space."
- **Pretrained encoders**: NUANCED. DynaMo's primary contribution is training representations from scratch (random initialization with ResNet18 backbone) using in-domain data only. It does NOT rely on pretrained encoders as its core method. However, the paper shows DynaMo can optionally fine-tune an ImageNet-pretrained ResNet18 (Table 5). The claim that it "demonstrates latent-space forward dynamics with pretrained encoders" is slightly misleading -- the default setup trains from scratch; pretrained initialization is an ablation variant.
- **LIBERO tasks**: CONFIRMED. The paper evaluates on LIBERO Goal (10 manipulation tasks, 7-DOF Franka arm, 500 demonstrations), achieving 0.93 success rate.
- **Real-robot tasks**: CONFIRMED. The paper includes real-world experiments on Allegro dexterous manipulation (3 tasks) and xArm Kitchen (5 tasks), with 43% and 20% improvement over baselines respectively.

---

### Paper 2: "DeFI: Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining"

**Existence and Venue: CONFIRMED at ICLR 2026**

- The paper exists on arXiv as [2604.16391](https://arxiv.org/abs/2604.16391) and is published as a conference paper at ICLR 2026 (confirmed on [OpenReview](https://openreview.net/forum?id=DdrsHWobR1) and via the [ICLR 2026 virtual poster](https://iclr.cc/virtual/2026/poster/10010761)).
- Authors: Wenyao Zhang, Bozhou Zhang, Zekun Qi, Wenjun Zeng, Xin Jin, Li Zhang.
- Code available at [GitHub: LogosRoboticsGroup/DeFi](https://github.com/LogosRoboticsGroup/DeFi).

**Methodology Claims: PARTIALLY SUPPORTED with important nuance**

- **Forward dynamics pretraining in DINO feature space**: NOT ACCURATE as stated. The paper's architecture is:
  - The **General Forward Dynamics Model (GFDM)** uses Stable Video Diffusion (SVD) and operates in a video VAE latent space, predicting future video frames -- it does NOT operate in DINO feature space.
  - The **General Inverse Dynamics Model (GIDM)** operates in DINO feature space -- it uses DINOv2 visual encoder to extract latent states from consecutive frames and infers latent actions.
  - So it is the **inverse** dynamics, not forward dynamics, that works in DINO feature space.
- **Transfer to manipulation**: CONFIRMED. DeFI demonstrates strong transfer to manipulation tasks, achieving 4.51 average task length on CALVIN ABC-D, 51.2% on SimplerEnv-Fractal, and 81.3% success in real-world deployment.
- **Disentanglement approach**: CONFIRMED. The core contribution is decoupling forward dynamics (video prediction) from inverse dynamics (action inference) so each can be pretrained on its optimal data source.

---

### Summary of Claim Accuracy

| Claim | Verdict |
|-------|---------|
| DynaMo exists and is at NeurIPS 2024 | CONFIRMED |
| DynaMo demonstrates latent-space forward dynamics | CONFIRMED |
| DynaMo uses "pretrained encoders" | MISLEADING -- default is from-scratch; pretrained is an ablation |
| DynaMo evaluates on LIBERO | CONFIRMED (LIBERO Goal) |
| DynaMo evaluates on real-robot tasks | CONFIRMED (Allegro + xArm Kitchen) |
| DeFI exists and is at ICLR 2026 | CONFIRMED |
| DeFI shows forward dynamics pretraining in DINO feature space | INCORRECT -- it is the *inverse* dynamics model that uses DINO; the forward dynamics model uses video diffusion in VAE latent space |
| DeFI transfers effectively to manipulation | CONFIRMED |

Sources:
- [DynaMo on arXiv](https://arxiv.org/abs/2409.12192)
- [DynaMo NeurIPS 2024 Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3b8db54b629e00537b59cbc6612026d7-Abstract-Conference.html)
- [DynaMo NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/93200)
- [DeFI on arXiv](https://arxiv.org/abs/2604.16391)
- [DeFI on OpenReview (ICLR 2026)](https://openreview.net/forum?id=DdrsHWobR1)
- [DeFI GitHub Repository](https://github.com/LogosRoboticsGroup/DeFi)
- [DeFI ICLR 2026 Virtual Poster](https://iclr.cc/virtual/2026/poster/10010761)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c04b55a-986d-4038-a247-3efea6e2e344",
  "isSidechain": true,
  "agentId": "a514fa3ddfc20f678",
  "requestId": "req_011Cb1j3R33xgUQnM2sdsUAh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e978992-da63-493b-807c-26e72717caec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49957197-7e23-47ce-8e44-1930fa9eddb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aq79MzKijqU4NUAC3aTgbZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 18998,
      "output_tokens": 1569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 522
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1569,
          "cache_read_input_tokens": 18998,
          "cache_creation_input_tokens": 522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 522,
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
