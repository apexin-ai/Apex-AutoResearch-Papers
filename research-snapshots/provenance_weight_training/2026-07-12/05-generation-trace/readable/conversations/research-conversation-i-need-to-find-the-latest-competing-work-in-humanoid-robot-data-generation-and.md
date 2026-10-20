# Research conversation: I need to find the latest competing work in humanoid robot data generation and task composition from 2026. Please use We

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae310ba66c7250626.jsonl`
- **Structured JSON:** [`3886def2bb1fd70ff51d.json`](../../sessions/38/3886def2bb1fd70ff51d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-10T19:21:06.819Z_

I need to find the latest competing work in humanoid robot data generation and task composition from 2026. Please use WebSearch for:

1. "humanoid" "task generation" OR "environment generation" simulation 2026
2. site:arxiv.org humanoid whole-body loco-manipulation 2026
3. "GR00T-Dreams" NVIDIA humanoid synthetic data 2026
4. "DexMimicGen" humanoid 2026
5. "Cosmos" humanoid video generation training data 2026
6. "procedural generation" humanoid robot tasks 2026

Report all relevant papers you find, especially anything that generates diverse humanoid training tasks or environments automatically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "ae310ba66c7250626",
  "type": "user",
  "uuid": "f6118a55-c676-4472-8bf8-35662cfa1b81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T19:21:07.959Z_

I'll search for the latest work in humanoid robot data generation and task composition. Let me run these searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6118a55-c676-4472-8bf8-35662cfa1b81",
  "isSidechain": true,
  "agentId": "ae310ba66c7250626",
  "requestId": "req_011CauRwiYqgKwbRjZyGbXrp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cd9c86c5-6b5c-41aa-87c1-9a58d54ed2c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012KBwLvFVHRVp8u3Wa6BwcC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 579,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T19:21:08.209Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cd8wdwbMUDxX9o84C49RDc`</summary>

```json
{
  "query": "humanoid task generation OR environment generation simulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd9c86c5-6b5c-41aa-87c1-9a58d54ed2c9",
  "isSidechain": true,
  "agentId": "ae310ba66c7250626",
  "requestId": "req_011CauRwiYqgKwbRjZyGbXrp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a43ccac7-078c-4258-8b5d-02a91fc3525a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012KBwLvFVHRVp8u3Wa6BwcC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 579,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:21:08.241Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JYJ7pKuJD4WpRBdRDvnckE`</summary>

```json
{
  "query": "site:arxiv.org humanoid whole-body loco-manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a43ccac7-078c-4258-8b5d-02a91fc3525a",
  "isSidechain": true,
  "agentId": "ae310ba66c7250626",
  "requestId": "req_011CauRwiYqgKwbRjZyGbXrp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "44e63c2a-4e3b-4532-8fd4-67c4f9634ea7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012KBwLvFVHRVp8u3Wa6BwcC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 579,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:21:08.438Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KBK7aqdxKnfD4UN388cEmW`</summary>

```json
{
  "query": "GR00T-Dreams NVIDIA humanoid synthetic data 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44e63c2a-4e3b-4532-8fd4-67c4f9634ea7",
  "isSidechain": true,
  "agentId": "ae310ba66c7250626",
  "requestId": "req_011CauRwiYqgKwbRjZyGbXrp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6f67f634-6a41-4d7f-9607-e2ed1e405fcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012KBwLvFVHRVp8u3Wa6BwcC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 579,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T19:21:08.604Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016bbVwNUjRn9Asx4PrXL2DH`</summary>

```json
{
  "query": "DexMimicGen humanoid 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f67f634-6a41-4d7f-9607-e2ed1e405fcf",
  "isSidechain": true,
  "agentId": "ae310ba66c7250626",
  "requestId": "req_011CauRwiYqgKwbRjZyGbXrp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3b71be84-8594-436a-94ed-a0c79fa97869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012KBwLvFVHRVp8u3Wa6BwcC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 579,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T19:21:08.608Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F1La9cTKGn14f7Az5y32DG`</summary>

```json
{
  "query": "Cosmos humanoid video generation training data 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b71be84-8594-436a-94ed-a0c79fa97869",
  "isSidechain": true,
  "agentId": "ae310ba66c7250626",
  "requestId": "req_011CauRwiYqgKwbRjZyGbXrp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0314c93f-295b-4dbc-b550-74846a72283e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012KBwLvFVHRVp8u3Wa6BwcC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 579,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T19:21:08.786Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GgjPae1Xjcgu7DqLySQ3gi`</summary>

```json
{
  "query": "procedural generation humanoid robot tasks 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0314c93f-295b-4dbc-b550-74846a72283e",
  "isSidechain": true,
  "agentId": "ae310ba66c7250626",
  "requestId": "req_011CauRwiYqgKwbRjZyGbXrp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2670a70-e1c5-46b1-870e-8657307a62ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012KBwLvFVHRVp8u3Wa6BwcC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 579
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 323,
          "cache_read_input_tokens": 13649,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 579,
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

_source line 9 · 2026-05-10T19:21:14.974Z_

<details><summary>↩ Tool result · `toolu_01F1La9cTKGn14f7Az5y32DG`</summary>

```text
Web search results for query: "Cosmos humanoid video generation training data 2026"

Links: [{"title":"NVIDIA Announces Major Release of Cosmos World Foundation Models and Physical AI Data Tools | NVIDIA Newsroom","url":"https://nvidianews.nvidia.com/news/nvidia-announces-major-release-of-cosmos-world-foundation-models-and-physical-ai-data-tools"},{"title":"Scale Synthetic Data and Physical AI Reasoning with NVIDIA Cosmos World Foundation Models | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/"},{"title":"NVIDIA Cosmos: World Foundation Models Powering Physical AI","url":"https://www.nvidia.com/en-us/ai/cosmos/"},{"title":"Generative AI in Industrial Robotics: 2026 Layers Guide","url":"https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"},{"title":"Cosmos World Foundation Model Platform for Physical AI","url":"https://arxiv.org/html/2501.03575v1"},{"title":"NVIDIA Cosmos · GitHub","url":"https://github.com/nvidia-cosmos"},{"title":"NVIDIA Makes Cosmos World Foundation Models Openly Available to Physical AI Developer Community","url":"https://blogs.nvidia.com/blog/cosmos-world-foundation-models/"},{"title":"Nvidia’s Cosmos Offers Synthetic Training Data; Following Tesla’s Lead","url":"https://www.notateslaapp.com/news/2484/nvidias-cosmos-offers-synthetic-training-data-following-teslas-lead"},{"title":"Cosmos Cookbook","url":"https://nvidia-cosmos.github.io/cosmos-cookbook/index.html"},{"title":"Advancing Physical AI with NVIDIA Cosmos World Foundation Model Platform | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/advancing-physical-ai-with-nvidia-cosmos-world-foundation-model-platform/"}]

Based on the search results, here's what I found about Cosmos humanoid video generation training data in 2026:

## Training Data Overview

The Cosmos world foundation models have been trained on 9,000 trillion tokens from 20 million hours of real-world human interactions, environment, industrial, robotics and driving data.

## Humanoid Robot Applications

1X is using Cosmos Predict and Cosmos Transfer to train its new humanoid robot NEO Gamma. Additionally, robot brain developer Skild AI is tapping into Cosmos Transfer to augment synthetic datasets for its robots.

## Data Generation for Humanoid Training

The combination of Cosmos for photorealistic synthetic video generation plus Isaac Sim for parallel physics-based trajectory collection constitutes NVIDIA's integrated answer to the training data problem for humanoid and industrial robot foundation models.

## Model Capabilities and Updates

Cosmos Transfer 2.5 provides faster and more scalable data augmentation from simulation and 3D spatial inputs, enabling greater diversity across environments, lighting conditions, and scene variations. Cosmos world foundation models have shown strong adherence to physical laws in evaluations, with metrics such as 3D consistency and physics alignment, and can be fine-tuned for specific applications like autonomous driving or humanoid robotics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0314c93f-295b-4dbc-b550-74846a72283e",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "ae310ba66c7250626",
  "type": "user",
  "uuid": "2a5180c8-dbda-4aee-bf39-17c215a0fc1f",
  "sourceToolAssistantUUID": "0314c93f-295b-4dbc-b550-74846a72283e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:21:14.993Z_

<details><summary>↩ Tool result · `toolu_01KBK7aqdxKnfD4UN388cEmW`</summary>

```text
Web search results for query: "GR00T-Dreams NVIDIA humanoid synthetic data 2026"

Links: [{"title":"Enhance Robot Learning with Synthetic Trajectory Data Generated by World Foundation Models | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/"},{"title":"Isaac GR00T - Generalist Robot 00 Technology | NVIDIA Developer","url":"https://developer.nvidia.com/isaac/gr00t"},{"title":"Use Case: NVIDIA Computing Platforms for Humanoid Robots","url":"https://www.nvidia.com/en-us/use-cases/humanoid-robots/"},{"title":"Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"},{"title":"NVIDIA Powers Humanoid Robot Industry With Cloud-to-Robot Computing Platforms for Physical AI | NVIDIA Newsroom","url":"https://nvidianews.nvidia.com/news/nvidia-powers-humanoid-robot-industry-with-cloud-to-robot-computing-platforms-for-physical-ai"},{"title":"NVIDIA Announces Isaac GR00T Blueprint to Accelerate Humanoid Robotics Development | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/isaac-gr00t-blueprint-humanoid-robotics/"},{"title":"NVIDIA's Robots Dream of Trajectories, Not Electric Sheep, with GR00T-Dreams - Hackster.io","url":"https://www.hackster.io/news/nvidia-s-robots-dream-of-trajectories-not-electric-sheep-with-gr00t-dreams-1f12db16c80f"},{"title":"NVIDIA Announces Isaac GR00T N1 — the World’s First Open Humanoid Robot Foundation Model — and Simulation Frameworks to Speed Robot Development | NVIDIA Newsroom","url":"https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks"},{"title":"Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"},{"title":"NVIDIA releases cloud-to-robot computing platforms for physical AI, humanoid development - The Robot Report","url":"https://www.therobotreport.com/nvidia-cloud-robot-computing-platforms-physical-ai-humanoid-development/"}]

Based on the search results, here's information about GR00T-Dreams, NVIDIA's humanoid synthetic data technology:

## Overview

The Isaac GR00T-Dreams blueprint is a reference workflow for generating vast amounts of synthetic trajectory data used for teaching humanoid robots to perform new actions in novel environments.

## How It Works

The NVIDIA Isaac GR00T-Dreams blueprint generates vast amounts of synthetic trajectory data using NVIDIA Cosmos world foundation models, prompted by a single image and language instructions. Using the Cosmos Predict-2 physical AI model combined with the Cosmos-Reason1 multimodal model, the blueprint is capable of turning real robot data into synthetic trajectories.

## Key Benefits

NVIDIA Research developed GR00T N1.5, an update to the world's first open foundation model for generalized humanoid robot reasoning and skills, in just 36 hours, a task that would have taken nearly three months with manual data collection. The GR00T-Dreams blueprint enables robots to generalize across behaviors, adapt to new environments, and learn novel actions from language instructions, even with training data from only a single task.

## Applications

GR00T models are trained on an expansive humanoid dataset consisting of real captured data, synthetic data generated using the components of the Isaac GR00T-Mimic blueprint, Isaac GR00T-Dreams blueprint, and internet-scale video data. Multiple robotics companies are adopting these technologies for applications in industrial automation and household systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f67f634-6a41-4d7f-9607-e2ed1e405fcf",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "ae310ba66c7250626",
  "type": "user",
  "uuid": "cefd2c26-4624-4d71-a0c7-7e14d7517ad2",
  "sourceToolAssistantUUID": "6f67f634-6a41-4d7f-9607-e2ed1e405fcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T19:21:16.338Z_

<details><summary>↩ Tool result · `toolu_016bbVwNUjRn9Asx4PrXL2DH`</summary>

```text
Web search results for query: "DexMimicGen humanoid 2026"

Links: [{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://arxiv.org/html/2410.24185v1"},{"title":"DexMimicGen: Automated Data Generation for Bimanual ...","url":"https://openreview.net/pdf/4189a2bc6c20d5c52d0e6542702e1be54de0fe82.pdf"},{"title":"DexMimicGen: Scalable Data for Bimanual Robotics","url":"https://www.emergentmind.com/topics/dexmimicgen"},{"title":"Researchers Reduce Human Effort in Robot Training | UT Austin Computer Science","url":"https://www.cs.utexas.edu/news/2025/researchers-reduce-human-effort-robot-training"},{"title":"[2410.24185] DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://arxiv.org/abs/2410.24185"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://dexmimicgen.github.io/"},{"title":"NVIDIA Research Breakthroughs Put Advanced Robots in Motion | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/nvidia-research-robotics-icra-2025/"},{"title":"Humanoids conquered CES 2026 - Humanoid.guide","url":"https://humanoid.guide/humanoids-ces-2026/"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://www.researchgate.net/publication/385443567_DexMimicGen_Automated_Data_Generation_for_Bimanual_Dexterous_Manipulation_via_Imitation_Learning"},{"title":"34 Best Humanoid Robots [2026 Ranked]","url":"https://blog.robozaps.com/b/best-humanoid-robots"}]

Based on the search results, here's what I found about DexMimicGen and humanoid robots:

## DexMimicGen Overview

DexMimicGen is a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands. The Robot Perception and Learning Lab launched DexMimicGen, a new data generation system to improve training for humanoid robots, building on the lab's earlier system, MimicGen, to predict humanoid autonomous robot movements from a small set of human demonstrations.

## How It Works

A human operator collects around five demonstrations of a task using a teleoperation device, and then DexMimicGen automatically generates a large set of demonstration trajectories in simulation. DexMimicGen was used to autonomously generate over 20,000 demonstrations for bimanual dexterous robots from just 60 source human demonstrations across 9 tasks, multiple simulators, and the real-world.

## Key Capabilities

While MimicGen only applies to robots with limited dexterity, DexMimicGen can handle bots with two arms and five-fingered hands—enabling more advanced tasks. The system includes tasks for GR-1 humanoid with dexterous hands like pouring, coffee (multi-phase), and can sorting (vision-based).

## Real-World Results

On the can sorting task, policies trained on 40 DexMimicGen-validated synthetic rollouts (from 4 real demos) achieved 90% real-world success, outperforming the 0% baseline of real-demos-only models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b71be84-8594-436a-94ed-a0c79fa97869",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "ae310ba66c7250626",
  "type": "user",
  "uuid": "135d79eb-9a2e-43cc-afc8-3a5ac52ed294",
  "sourceToolAssistantUUID": "3b71be84-8594-436a-94ed-a0c79fa97869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:21:16.414Z_

<details><summary>↩ Tool result · `toolu_01JYJ7pKuJD4WpRBdRDvnckE`</summary>

```text
Web search results for query: "site:arxiv.org humanoid whole-body loco-manipulation 2026"

Links: [{"title":"LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation in Diverse Messy Environments","url":"https://arxiv.org/html/2508.16943"},{"title":"[2604.08508] Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2604.08508"},{"title":"[2510.05070v1] ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning","url":"https://arxiv.org/abs/2510.05070v1"},{"title":"VisualMimic Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/html/2509.20322v1"},{"title":"Scalable and General Whole-Body Control for Cross-Humanoid Locomotion","url":"https://arxiv.org/html/2602.05791"},{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://arxiv.org/html/2506.09366v1"},{"title":"[2512.11047] WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control","url":"https://arxiv.org/abs/2512.11047"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"[2602.06643] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations","url":"https://arxiv.org/abs/2602.06643"},{"title":"TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality","url":"https://arxiv.org/html/2506.15146v1"}]

I found several recent papers on arxiv.org about humanoid whole-body loco-manipulation from 2026 and late 2025. Here are the results:

## Key Papers Found:

1. **LHM-Humanoid** (March 2026): A benchmark and learning framework for long-horizon whole-body humanoid loco-manipulation in diverse, cluttered scenes. The approach uses reinforcement learning to train teacher policies and distills them into a single end-to-end student policy, which is further distilled into a vision-language-action (VLA) model driven by egocentric RGB observations and natural language.

2. **Sumo** (April 2026): A sim-to-real approach that enables legged robots to dynamically manipulate large and heavy objects with whole-body dexterity, using test-time steering of a pre-trained whole-body control policy with a sample-based planner. The approach can be generalized to humanoid loco-manipulation tasks, such as opening a door and pushing a table, in simulation.

3. **WholeBodyVLA** (December 2025): A unified latent learning framework that enables Vision-Language-Action (VLA) systems to learn from low-cost action-free egocentric videos.

4. **ResMimic** (October 2025): A two-stage residual learning framework where a general motion tracking policy trained on large-scale human-only motion serves as a task-agnostic base, and an efficient but precise residual policy is then learned to refine outputs to improve locomotion and incorporate object interaction.

5. **SkillBlender** (June 2025): A hierarchical reinforcement learning framework that first pretrains goal-conditioned task-agnostic primitive skills, then dynamically blends these skills to accomplish complex loco-manipulation tasks with minimal task-specific reward engineering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44e63c2a-4e3b-4532-8fd4-67c4f9634ea7",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "ae310ba66c7250626",
  "type": "user",
  "uuid": "459423af-d769-4f78-ba58-8a89b495839f",
  "sourceToolAssistantUUID": "44e63c2a-4e3b-4532-8fd4-67c4f9634ea7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:21:16.693Z_

<details><summary>↩ Tool result · `toolu_01GgjPae1Xjcgu7DqLySQ3gi`</summary>

```text
Web search results for query: "procedural generation humanoid robot tasks 2026"

Links: [{"title":"Humanoid robots in 2026: Types, prices, and what’s next - Standard Bots","url":"https://standardbots.com/blog/humanoid-robot"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"},{"title":"AI Humanoid Robots 2026: Technology, Builders & Future","url":"https://www.articsledge.com/post/ai-humanoid-robots"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"Opportunities challenges and roadmap for humanoid robots in construction | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-30252-6"},{"title":"Humanoid Robots News | AI Breakthroughs, Robotics Trends & Synthetic Updates","url":"https://humanoid.press/"},{"title":"Will 2026 be the year of the Humanoid Robot?","url":"https://www.datapro.news/p/will-2026-be-the-year-of-the-humanoid-robot"},{"title":"2026 humanoid robot launches - Electronics360 - GlobalSpec","url":"https://electronics360.globalspec.com/article/23332/2026-humanoid-robot-launches"},{"title":"Which Humanoid Robots Launch in 2026? - Qviro Blog","url":"https://qviro.com/blog/humanoid-robots-launch-2026/"},{"title":"9 humanoid robots at CES 2026 that showed the future is already here","url":"https://interestingengineering.com/ai-robotics/9-humanoid-robots-at-ces-2026"}]

I've completed a web search for "procedural generation humanoid robot tasks 2026". Here are the key findings:

## Current State of Humanoid Robots in 2026

In 2026, humanoid robots operate in logistics, manufacturing, healthcare, and customer service. Most deployments remain in pilots, but adoption is accelerating.

## Advanced Task Training Methods

One particularly relevant development involves **procedural generation-like synthetic data creation**. The "GROOT-Dreams" blueprint uses a single image and language prompt to generate diverse 2D videos of future world states, which are then translated into 3D action data using an Inverse Dynamics Model, and this synthetic data is filtered by high-level reasoning models to ensure physical accuracy before being used to train the robot's policy. Policies trained on this mixture of real and synthetic data consistently outperform those trained on real data alone.

## Real-World Task Applications

In real deployments, 2025 humanoid robots in factories and warehouses mainly move totes, bins and parts, unload containers, and handle repetitive intralogistics tasks. Additional applications include warehouse order picking, manufacturing line inspection, household assistance, and customer service roles.

## Hardware Enablers

The NVIDIA Jetson Thor, released in late 2025, provides 2070 FP4 TFLOPS of AI compute, enabling real-time reasoning and bipedal control within a humanoid's power constraints.

The search results show that while procedural generation isn't explicitly the primary focus, synthetic data generation techniques that simulate future task states are increasingly important for training humanoid robots in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2670a70-e1c5-46b1-870e-8657307a62ae",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "ae310ba66c7250626",
  "type": "user",
  "uuid": "35f838b5-230e-4a80-80a7-57b4ff8d7d0b",
  "sourceToolAssistantUUID": "f2670a70-e1c5-46b1-870e-8657307a62ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:21:17.487Z_

<details><summary>↩ Tool result · `toolu_01Cd8wdwbMUDxX9o84C49RDc`</summary>

```text
Web search results for query: "humanoid task generation OR environment generation simulation 2026"

Links: [{"title":"Generative AI in Industrial Robotics: 2026 Layers Guide","url":"https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"},{"title":"Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot","url":"https://arxiv.org/html/2601.02078v1"},{"title":"Inside 1X’s Humanoid Robot Stack: Simulation, AI Training, and Onboard Compute with NVIDIA","url":"https://www.1x.tech/discover/nvidia-gtc-2026"},{"title":"2026 humanoid robot launches - Electronics360 - GlobalSpec","url":"https://electronics360.globalspec.com/article/23332/2026-humanoid-robot-launches"},{"title":"AGIBOT introduces Genie Sim 3.0 simulation platform for embodied AI - The Robot Report","url":"https://www.therobotreport.com/agibot-introduces-genie-sim-3-0-simulation-platform-embodied-ai/"},{"title":"January 2026 Humanoid Robot Launches - Qviro Blog","url":"https://qviro.com/blog/january-2026-humanoid-robot-launches/"},{"title":"Humanoids conquered CES 2026 - Humanoid.guide","url":"https://humanoid.guide/humanoids-ces-2026/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Humanoid robots in 2026: Types, prices, and what’s next - Standard Bots","url":"https://standardbots.com/blog/humanoid-robot"},{"title":"Use Case: NVIDIA Computing Platforms for Humanoid Robots","url":"https://www.nvidia.com/en-us/use-cases/humanoid-robots/"}]

I found comprehensive search results about humanoid task generation and environment generation simulation in 2026. Here are the key findings:

## Humanoid Simulation Platforms

Genie Sim 3.0 is a unified simulation platform for robotic manipulation that uses an LLM-powered tool to construct high-fidelity scenes from natural language instructions, with strength in rapid and multi-dimensional generalization for synthesizing diverse environments.

Genie Sim 3.0 integrates 3D reconstruction, visual generation, and physics engines to enable faster sim-to-real transfer, and enables scene generation in minutes, compared with hours in traditional pipelines.

1X uses NVIDIA Isaac Sim and NVIDIA Isaac Lab, open-source frameworks for robot simulation and learning, to generate photorealistic environments where robots can train and evaluate tasks.

## Task Generation and Environment Evaluation

Genie Sim 3.0 introduces the first benchmark that pioneers the application of LLM for automated evaluation, leveraging LLM to mass-generate evaluation scenarios and employing Vision-Language Model (VLM) to establish an automated assessment pipeline.

For five core capabilities of robot algorithms—instruction understanding, spatial reasoning, atomic skill operation, disturbance adaptation, and training-to-deployment generalization—AGIBOT designed five corresponding task suites.

## Synthetic Data Generation

NVIDIA Isaac GR00T-Dreams blueprint generates vast amounts of synthetic trajectory data using NVIDIA Cosmos world foundation models, prompted by a single image and language instructions, enabling robots to learn new tasks in unfamiliar environments without needing specific teleoperation data.

The 2026 landscape shows significant progress in automated environment and task generation for humanoid robots, with major emphasis on LLM-driven scene creation and synthetic data generation for training purposes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a43ccac7-078c-4258-8b5d-02a91fc3525a",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "ae310ba66c7250626",
  "type": "user",
  "uuid": "699b715c-b438-4840-8296-c771f386f801",
  "sourceToolAssistantUUID": "a43ccac7-078c-4258-8b5d-02a91fc3525a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T19:21:30.756Z_

## Summary of Latest Competing Work in Humanoid Robot Data Generation and Task Composition (2026)

Based on comprehensive web searches, I've identified the major research directions and systems in this space:

### **1. Simulation and Task Generation Platforms**

**Genie Sim 3.0** - A unified simulation platform for robotic manipulation that uses LLM-powered tools to construct high-fidelity scenes from natural language instructions. It enables scene generation in minutes (vs. hours in traditional pipelines) and introduces the first benchmark using LLMs for automated evaluation and mass-generation of evaluation scenarios, with five core task suites (instruction understanding, spatial reasoning, atomic skill operation, disturbance adaptation, and training-to-deployment generalization).

### **2. Synthetic Data Generation Systems**

**GR00T-Dreams (NVIDIA)** - A blueprint using NVIDIA Cosmos world foundation models to generate vast amounts of synthetic trajectory data from a single image and language instructions. Uses Cosmos Predict-2 physical AI models combined with Cosmos-Reason1 for converting real robot data into synthetic trajectories. GR00T N1.5 was developed in 36 hours (vs. 3 months manual collection).

**DexMimicGen** - An automated data generation system for bimanual dexterous manipulation that scales from ~5 human demonstrations to 20,000+ synthetic demonstrations across 9 tasks. Achieved 90% real-world success on can sorting with just 40 synthetic rollouts from 4 real demos.

### **3. Whole-Body Loco-Manipulation Learning (Recent arxiv papers)**

- **LHM-Humanoid** (March 2026) - Long-horizon humanoid whole-body loco-manipulation in diverse environments using RL with teacher-student policy distillation into VLA models
- **Sumo** (April 2026) - Sim-to-real whole-body dynamic manipulation using test-time steering of pre-trained policies
- **WholeBodyVLA** (December 2025) - Unified latent VLA framework for learning from action-free egocentric videos
- **ResMimic** (October 2025) - Two-stage residual learning framework combining general motion tracking with task-specific residual policies
- **SkillBlender** (June 2025) - Hierarchical RL framework with pretraining of goal-conditioned primitive skills

### **4. World Foundation Models for Physical AI**

**NVIDIA Cosmos** - Trained on 9,000 trillion tokens from 20 million hours of real-world data (human interactions, robotics, driving). Cosmos Transfer 2.5 enables photorealistic synthetic video generation with faster data augmentation. Used by 1X (NEO Gamma humanoid) and Skild AI.

### **Key Trend**

The convergence is clear: **synthetic data generation from foundation models + task composition from LLMs + simulation environments** enable rapid scaling without manual teleoperation or scene construction. All major systems emphasize sim-to-real transfer, procedural-like task generation from language prompts, and training on mixtures of real and synthetic data.

Sources:
- [Genie Sim 3.0 - AGIBOT](https://arxiv.org/html/2601.02078v1)
- [NVIDIA GR00T-Dreams Technical Blog](https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/)
- [DexMimicGen arxiv](https://arxiv.org/abs/2410.24185)
- [LHM-Humanoid arxiv](https://arxiv.org/html/2508.16943)
- [Sumo arxiv](https://arxiv.org/abs/2604.08508)
- [NVIDIA Cosmos World Foundation Models](https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/)
- [WholeBodyVLA arxiv](https://arxiv.org/abs/2512.11047)
- [ResMimic arxiv](https://arxiv.org/abs/2510.05070v1)
- [SkillBlender arxiv](https://arxiv.org/html/2506.09366v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "699b715c-b438-4840-8296-c771f386f801",
  "isSidechain": true,
  "agentId": "ae310ba66c7250626",
  "requestId": "req_011CauRxWDi3ovLDRLGEBZqM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "28a18287-1be8-4b6e-bd0c-7986a325b802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014Sfzwju1QTyMyqiPCWuVuu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4703,
      "cache_creation_input_tokens": 2077,
      "cache_read_input_tokens": 14228,
      "output_tokens": 1011,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2077
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4703,
          "output_tokens": 1011,
          "cache_read_input_tokens": 14228,
          "cache_creation_input_tokens": 2077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2077,
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
