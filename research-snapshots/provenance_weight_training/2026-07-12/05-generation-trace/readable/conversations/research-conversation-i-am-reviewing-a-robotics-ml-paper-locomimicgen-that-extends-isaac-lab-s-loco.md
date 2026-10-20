# Research conversation: I am reviewing a robotics ML paper "LocoMimicGen" that extends Isaac Lab's loco-manipulation infrastructure for humanoid

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa0ba314500a9b4f4.jsonl`
- **Structured JSON:** [`0a528c64607ef3533618.json`](../../sessions/0a/0a528c64607ef3533618.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-10T13:33:29.274Z_

I am reviewing a robotics ML paper "LocoMimicGen" that extends Isaac Lab's loco-manipulation infrastructure for humanoid demo generation. I need you to do independent verification of the following claims and searches. Please search thoroughly and report what you find.

**Search 1**: Verify that SoftMimicGen (arXiv:2603.25725) is a real paper from March 2026 extending MimicGen to deformable objects. Search for "SoftMimicGen deformable robot manipulation 2026 arxiv".

**Search 2**: Verify that ULTRA (arXiv:2603.03279) is a real paper about humanoid loco-manipulation via MoCap retargeting. Search for "ULTRA humanoid loco-manipulation arxiv 2603.03279".

**Search 3**: Search for any NEW papers from April-May 2026 on "humanoid loco-manipulation data generation" that might be concurrent with LocoMimicGen and not yet cited. Try: "humanoid data generation simulation 2026 arxiv site:arxiv.org".

**Search 4**: Search for any recent papers on "SE(3) demonstration generation" or "object-centric demo multiplication" for mobile manipulation or loco-manipulation: "SE3 object centric demonstration generation robot locomotion manipulation 2026".

**Search 5**: Search specifically for papers on "stance selection reachability humanoid data generation" to see if any paper has specifically solved the IRM-for-bipedal-data-generation problem the generator claims is novel: "inverse reachability map bipedal humanoid imitation learning data generation".

**Search 6**: Search for "DemoGen RSS 2025 humanoid manipulation" to verify the DemoGen paper characterization.

**Search 7**: Search for any new Isaac Lab papers or code updates that might affect the PR #3259 characterization: "Isaac Lab locomanipulation 2025 2026 data generation".

Report your findings concisely - what papers were confirmed, what wasn't found, and any surprising concurrent work discovered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8d094254-63e5-4cc7-b74e-bff62736c708",
  "agentId": "aa0ba314500a9b4f4",
  "type": "user",
  "uuid": "1ed991e1-fa88-474d-b4cc-773d3fd49ef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T13:33:31.034Z_

I'll conduct thorough searches on each of these claims about the LocoMimicGen paper and related work. Let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ed991e1-fa88-474d-b4cc-773d3fd49ef8",
  "isSidechain": true,
  "agentId": "aa0ba314500a9b4f4",
  "requestId": "req_011CatySERL38M8nFRLNEbFG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae1836f9-1518-455d-8a67-238b15524427",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WfzseNEgnicD6D9VWDaDpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17056,
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

_source line 3 · 2026-05-10T13:33:31.043Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ErqgtpZDG4sorvzW6TXzvN`</summary>

```json
{
  "query": "SoftMimicGen deformable robot manipulation 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae1836f9-1518-455d-8a67-238b15524427",
  "isSidechain": true,
  "agentId": "aa0ba314500a9b4f4",
  "requestId": "req_011CatySERL38M8nFRLNEbFG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cc87cdfe-477c-4070-a3de-85d355be8d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WfzseNEgnicD6D9VWDaDpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17056,
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

_source line 4 · 2026-05-10T13:33:31.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013hTvSyRbzYuzR3x935vMch`</summary>

```json
{
  "query": "ULTRA humanoid loco-manipulation arxiv 2603.03279"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc87cdfe-477c-4070-a3de-85d355be8d66",
  "isSidechain": true,
  "agentId": "aa0ba314500a9b4f4",
  "requestId": "req_011CatySERL38M8nFRLNEbFG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af72f5ec-e1ae-4b15-ad2c-9dd73d787c09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WfzseNEgnicD6D9VWDaDpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17056,
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

_source line 5 · 2026-05-10T13:33:31.463Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YQjbfpUa9Gxf6avdMDQjZT`</summary>

```json
{
  "query": "humanoid data generation simulation 2026 arxiv site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af72f5ec-e1ae-4b15-ad2c-9dd73d787c09",
  "isSidechain": true,
  "agentId": "aa0ba314500a9b4f4",
  "requestId": "req_011CatySERL38M8nFRLNEbFG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad0e25a8-8ca1-4987-9379-895a5bce7562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WfzseNEgnicD6D9VWDaDpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17056,
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

_source line 6 · 2026-05-10T13:33:31.662Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AUzW2yxxWYXwGYPAHhNeTv`</summary>

```json
{
  "query": "SE3 object centric demonstration generation robot locomotion manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad0e25a8-8ca1-4987-9379-895a5bce7562",
  "isSidechain": true,
  "agentId": "aa0ba314500a9b4f4",
  "requestId": "req_011CatySERL38M8nFRLNEbFG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ed1102f4-8976-4ea0-becb-d18c73efc028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WfzseNEgnicD6D9VWDaDpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17056,
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

_source line 7 · 2026-05-10T13:33:31.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ALsWRT7MGZobpcwnkGafiJ`</summary>

```json
{
  "query": "inverse reachability map bipedal humanoid imitation learning data generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed1102f4-8976-4ea0-becb-d18c73efc028",
  "isSidechain": true,
  "agentId": "aa0ba314500a9b4f4",
  "requestId": "req_011CatySERL38M8nFRLNEbFG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b3aec3c0-727b-4b78-b23d-d021e6624347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WfzseNEgnicD6D9VWDaDpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17056,
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

_source line 8 · 2026-05-10T13:33:31.897Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LyFenJjJnTtzKi9McFNH6y`</summary>

```json
{
  "query": "DemoGen RSS 2025 humanoid manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3aec3c0-727b-4b78-b23d-d021e6624347",
  "isSidechain": true,
  "agentId": "aa0ba314500a9b4f4",
  "requestId": "req_011CatySERL38M8nFRLNEbFG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e76e63d7-f30e-4145-b80f-fc8f4218f322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WfzseNEgnicD6D9VWDaDpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17056,
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

_source line 9 · 2026-05-10T13:33:32.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K2fzeU3vud4qRf86GRiP6y`</summary>

```json
{
  "query": "Isaac Lab locomanipulation 2025 2026 data generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e76e63d7-f30e-4145-b80f-fc8f4218f322",
  "isSidechain": true,
  "agentId": "aa0ba314500a9b4f4",
  "requestId": "req_011CatySERL38M8nFRLNEbFG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e96919b1-b7cd-430d-b4ed-f8bdac4da87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WfzseNEgnicD6D9VWDaDpP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17056
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 396,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17056,
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

_source line 10 · 2026-05-10T13:33:37.579Z_

<details><summary>↩ Tool result · `toolu_01AUzW2yxxWYXwGYPAHhNeTv`</summary>

```text
Web search results for query: "SE3 object centric demonstration generation robot locomotion manipulation 2026"

Links: [{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation","url":"https://nvlabs.github.io/object_centric_diffusion/"},{"title":"[2411.00965] SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation","url":"https://arxiv.org/abs/2411.00965"},{"title":"(PDF) SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation","url":"https://www.researchgate.net/publication/385528942_SPOT_SE3_Pose_Trajectory_Diffusion_for_Object-Centric_Manipulation"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation | Research","url":"https://research.nvidia.com/publication/2025-05_spot-se3-pose-trajectory-diffusion-object-centric-manipulation"},{"title":"A retrieval-augmented framework enabling VLM spatial awareness for object-centric robot manipulation | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.aea2092"},{"title":"A Survey of Embodied Learning for Object-centric Robotic Manipulation | Machine Intelligence Research | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11633-025-1542-8"},{"title":"Paper-List/README.md at main · YanjieZe/Paper-List","url":"https://github.com/YanjieZe/Paper-List/blob/main/README.md"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"SPIDER: Scalable Physics-Informed Dexterous Retargeting","url":"https://arxiv.org/html/2511.09484"},{"title":"Toward next-generation learned robot manipulation | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.abd9461"}]

Based on the search results, here are the key findings related to your query:

## SPOT: SE(3) Pose Trajectory Diffusion

SPOT is an object-centric imitation learning framework that captures each task by an object-centric representation, specifically the SE(3) object pose trajectory relative to the target. This approach decouples embodiment actions from sensory inputs, facilitating learning across different robot embodiments.

## Object-Centric Robotic Manipulation Research

Embodied learning for object-centric robotic manipulation is a rapidly developing and challenging area in embodied AI that is crucial for advancing next-generation intelligent robots. Recent work categorizes existing approaches into three main branches: embodied perceptual learning for predicting object pose and affordance, embodied policy learning using reinforcement and imitation learning, and embodied task-oriented learning designed to optimize robot performance based on task characteristics.

## Related 2026 Research

A retrieval-augmented framework for object-centric robot manipulation combines vision-language models with an object-centric engine to create a generalizable framework for spatially aware manipulation of unseen objects.

The search results show that SE(3) object-centric representations and diffusion-based learning approaches are becoming prominent methods for improving robot manipulation and locomotion across different embodiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed1102f4-8976-4ea0-becb-d18c73efc028",
  "isSidechain": true,
  "promptId": "8d094254-63e5-4cc7-b74e-bff62736c708",
  "agentId": "aa0ba314500a9b4f4",
  "type": "user",
  "uuid": "84cb2b34-6a76-426c-b50b-74142f2fdad5",
  "sourceToolAssistantUUID": "ed1102f4-8976-4ea0-becb-d18c73efc028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T13:33:38.064Z_

<details><summary>↩ Tool result · `toolu_01ErqgtpZDG4sorvzW6TXzvN`</summary>

```text
Web search results for query: "SoftMimicGen deformable robot manipulation 2026 arxiv"

Links: [{"title":"[2603.25725] SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation","url":"https://arxiv.org/abs/2603.25725"},{"title":"[2603.25725v1] SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation","url":"https://arxiv.org/abs/2603.25725v1"},{"title":"SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation","url":"https://arxiv.org/html/2603.25725v1"},{"title":"SoftMimicGen","url":"https://softmimicgen.github.io/"},{"title":"🤖 Robotics arXiv Digest — 2026-03-26","url":"https://www.visionforrobotics.com/robotics-digest/digest_2026-03-26.html"},{"title":"GitHub - BaiShuanghao/Awesome-Robotics-Manipulation: A comprehensive list of papers about Robot Manipulation, including papers, codes, and related websites. · GitHub","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation"},{"title":"Generative Artificial Intelligence in Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2503.03464v1"},{"title":"What foundation models can bring for robot learning in manipulation: A survey - Dingzhe Li, Yixiang Jin, YuHao Sun, Yong A, Hongze Yu, Jun Shi, Xiaoshuai Hao, Peng Hao, Huaping Liu, Xiang Li, Xinde Li, Fuchun Sun, Jianwei Zhang, Bin Fang, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251390579"},{"title":"MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | OpenReview","url":"https://openreview.net/forum?id=dk-2R1f_LR"},{"title":"Zhenjia Xu's research works | NVIDIA and other places","url":"https://www.researchgate.net/scientific-contributions/Zhenjia-Xu-2204621322"}]

I found the paper you're looking for. SoftMimicGen was submitted on March 26, 2026 on arXiv (ID: 2603.25725).

SoftMimicGen is an automated data generation pipeline for deformable object manipulation tasks. While the synthetic data generation paradigm has been limited to rigid-body tasks which are easy to simulate, deformable object manipulation encompasses a large portion of real-world manipulation and remains a crucial gap to address.

The paper addresses key challenges in deformable object manipulation. The system extends the MimicGen data synthesis paradigm to deformable objects (cloth, foam, flexible tubes), where the core challenge is demonstration transfer: deformable objects deform differently under each grasp, so naive trajectory replication from seed demonstrations fails — SoftMimicGen develops deformation-aware transfer that accounts for how geometry changes affect the execution.

The paper introduces a suite of high-fidelity simulation environments that encompasses a wide range of deformable objects (stuffed animal, rope, tissue, towel) and manipulation behaviors (high-precision threading, dynamic whipping, folding, pick-and-place), across four robot embodiments: a single-arm manipulator, bimanual arms, a humanoid, and a surgical robot.

The paper is authored by Masoud Moghani, Mahdi Azizian, Animesh Garg, Yuke Zhu, Sean Huver, and Ajay Mandlekar, with additional information available at the project website: softmimicgen.github.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc87cdfe-477c-4070-a3de-85d355be8d66",
  "isSidechain": true,
  "promptId": "8d094254-63e5-4cc7-b74e-bff62736c708",
  "agentId": "aa0ba314500a9b4f4",
  "type": "user",
  "uuid": "6daf8324-c4fb-4d7d-b9ce-e0390d644161",
  "sourceToolAssistantUUID": "cc87cdfe-477c-4070-a3de-85d355be8d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T13:33:38.742Z_

<details><summary>↩ Tool result · `toolu_01LyFenJjJnTtzKi9McFNH6y`</summary>

```text
Web search results for query: "DemoGen RSS 2025 humanoid manipulation"

Links: [{"title":"GitHub - TEA-Lab/DemoGen: [RSS25] Official implementation of DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning","url":"https://github.com/TEA-Lab/DemoGen"},{"title":"GitHub - YanjieZe/3D-Diffusion-Policy: [RSS 2024] 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations · GitHub","url":"https://github.com/YanjieZe/3D-Diffusion-Policy"},{"title":"GitHub - gist-ailab/AILab-DemoGen: [RSS25] Official implementation of DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning","url":"https://github.com/gist-ailab/AILab-DemoGen"},{"title":"DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning | Request PDF","url":"https://www.researchgate.net/publication/395366085_DemoGen_Synthetic_Demonstration_Generation_for_Data-Efficient_Visuomotor_Policy_Learning"},{"title":"Xue 等 - 2025 - DemoGen Synthetic Demonstration Generation for Da","url":"https://www.scribd.com/document/900355111/Xue-%E7%AD%89-2025-DemoGen-Synthetic-Demonstration-Generation-for-Da"},{"title":"DemoGen | Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning","url":"https://demo-generation.github.io/"},{"title":"DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning","url":"https://arxiv.org/html/2502.16932v1"},{"title":"Embodied intelligence for robot manipulation: development and challenges | Vicinagearth | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44336-025-00020-1"},{"title":"DemoGen: Synthetic Demonstration Generation","url":"https://www.roboticsproceedings.org/rss21/p157.pdf"},{"title":"Humanoids 2025 Program | Tuesday September 30, 2025","url":"https://ras.papercept.net/conferences/scripts/rtf/ICHR25_ContentListWeb_1.html"}]

Based on the search results, here's what I found about DemoGen at RSS 2025 and humanoid manipulation:

## DemoGen Overview

DemoGen is a synthetic data generation approach designed for robotic manipulation. Given only one human demonstration collected in the real world, DemoGen could produce hundreds of spatially-augmented synthetic demonstrations in few seconds.

## Humanoid Manipulation

DemoGen has been successfully applied to bimanual humanoid platforms. DemoGen demonstrates 90.8% success rate on bimanual humanoid platforms and its ability to help policies generalize to out-of-distribution orientations. DemoGen significantly enhances policy performance across a diverse range of real-world manipulation tasks, showing its applicability even in challenging scenarios involving deformable objects, dexterous hand end-effectors, and bimanual platforms.

## Technical Approach

For action generation, DemoGen adopts the idea of Task and Motion Planning (TAMP) and adapts the source actions according to novel object configurations. For visual observation generation, DemoGen leverages 3D point clouds as the modality and rearranges the subjects in the scene via 3D editing.

## Publication

DemoGen is the official implementation published at RSS25 for Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e76e63d7-f30e-4145-b80f-fc8f4218f322",
  "isSidechain": true,
  "promptId": "8d094254-63e5-4cc7-b74e-bff62736c708",
  "agentId": "aa0ba314500a9b4f4",
  "type": "user",
  "uuid": "8e55c9aa-89cc-4dd3-830d-55c5d21bfe8c",
  "sourceToolAssistantUUID": "e76e63d7-f30e-4145-b80f-fc8f4218f322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T13:33:38.817Z_

<details><summary>↩ Tool result · `toolu_01K2fzeU3vud4qRf86GRiP6y`</summary>

```text
Web search results for query: "Isaac Lab locomanipulation 2025 2026 data generation"

Links: [{"title":"Adds locomanipulation data generation via. disjoint navigation by jaybdub · Pull Request #3259 · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/pull/3259"},{"title":"Releases · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/releases"},{"title":"Release Notes — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/refs/release_notes.html"},{"title":"Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/"},{"title":"Isaac Lab: A GPU Accelerated Simulation Framework For Multi-Modal Robot Learning | Research","url":"https://research.nvidia.com/publication/2025-09_isaac-lab-gpu-accelerated-simulation-framework-multi-modal-robot-learning"},{"title":"MANUS Is the Official Data Glove of NVIDIA's Isaac Teleop","url":"https://humanoidroboticstechnology.com/industry-news/nvidia-launches-isaac-teleop-at-gtc-2026-with-manus-as-the-official-data-glove/"},{"title":"Announcing General Availability for NVIDIA Isaac Sim 5.0 and NVIDIA Isaac Lab 2.2 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/isaac-sim-and-isaac-lab-are-now-available-for-early-developer-preview/"},{"title":"Teleoperation and Imitation Learning with Isaac Lab Mimic — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html"},{"title":"[2511.04831] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning","url":"https://arxiv.org/abs/2511.04831"},{"title":"GitHub - unitreerobotics/unitree_sim_isaaclab: The Unitree simulation environment built based on Isaac Lab · GitHub","url":"https://github.com/unitreerobotics/unitree_sim_isaaclab"}]

Based on the search results, here's what I found about Isaac Lab locomanipulation data generation:

## Overview

Isaac Lab 2.3 accelerates robot learning by automating the generation of complex manipulation and locomotion data.

## Locomanipulation Data Generation Features

A pull request adds locomanipulation data generation via disjoint navigation. The approach allows the user to replay static manipulation data recorded with the G1 through an end to end pick-up -> navigation workflow.

More specifically, a new G1 humanoid environment combines RL-based locomotion with IK-based manipulation, with a full robot navigation stack integrated to augment demonstrations with randomization of tabletop pick/place locations, destination and ground obstacles. By segmenting tasks into pick-navigate-place phases, this method enables generation of large-scale loco-manipulation datasets from manipulation-only demonstrations.

## Practical Implementation

The locomanipulation dataset generation process takes the previously generated manipulation dataset and creates scenarios where the robot must navigate from one location to another while performing manipulation tasks, creating a more complex dataset that includes both locomotion and manipulation behaviors.

Locomanipulation data generation via disjoint navigation was added to Isaac Lab in recent releases (2025-2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e96919b1-b7cd-430d-b4ed-f8bdac4da87b",
  "isSidechain": true,
  "promptId": "8d094254-63e5-4cc7-b74e-bff62736c708",
  "agentId": "aa0ba314500a9b4f4",
  "type": "user",
  "uuid": "a85e6ddf-7d87-4eee-b742-98b253120b71",
  "sourceToolAssistantUUID": "e96919b1-b7cd-430d-b4ed-f8bdac4da87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T13:33:39.066Z_

<details><summary>↩ Tool result · `toolu_013hTvSyRbzYuzR3x935vMch`</summary>

```text
Web search results for query: "ULTRA humanoid loco-manipulation arxiv 2603.03279"

Links: [{"title":"[2603.03279] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2603.03279"},{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/html/2603.03279"},{"title":"[2603.03279v1] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2603.03279v1"},{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation | alphaXiv","url":"https://www.alphaxiv.org/abs/2603.03279"},{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://ultra-humanoid.github.io/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"OmniClone: Engineering a Robust, All-Rounder Whole-Body Humanoid Teleoperation System","url":"https://arxiv.org/html/2603.14327"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2603.12263"},{"title":"HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit","url":"https://arxiv.org/html/2502.13013v1"}]

Based on the search results, here's information about the paper:

## ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation

ULTRA is a unified framework with two key components: a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions, and a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs.

Existing approaches are fundamentally constrained by scarce or low-quality retargeted data, difficulty scaling to large skill repertoires, and reliance on tracking predefined motion references rather than generating behavior from perception and high-level task specifications.

The framework distills a universal tracking policy into the controller, compresses motor skills into a compact latent space, and applies reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios, enabling coordinated whole-body behavior from sparse intent without test-time reference motions.

The paper evaluates ULTRA in simulation and on a real Unitree G1 humanoid, showing that it generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.

The paper was submitted to arXiv on March 3, 2026, and is authored by Xialin He, Sirui Xu, Xinyao Li, Runpei Dong, Liuyu Bian, Yu-Xiong Wang, and Liang-Yan Gui from the University of Illinois Urbana-Champaign.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af72f5ec-e1ae-4b15-ad2c-9dd73d787c09",
  "isSidechain": true,
  "promptId": "8d094254-63e5-4cc7-b74e-bff62736c708",
  "agentId": "aa0ba314500a9b4f4",
  "type": "user",
  "uuid": "0f0667a1-c557-4d74-9190-8577f5cb1749",
  "sourceToolAssistantUUID": "af72f5ec-e1ae-4b15-ad2c-9dd73d787c09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T13:33:39.733Z_

<details><summary>↩ Tool result · `toolu_01YQjbfpUa9Gxf6avdMDQjZT`</summary>

```text
Web search results for query: "humanoid data generation simulation 2026 arxiv site:arxiv.org"

Links: [{"title":"[2601.02078] Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot","url":"https://arxiv.org/abs/2601.02078"},{"title":"Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot","url":"https://arxiv.org/html/2601.02078v1"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/html/2509.26633v2"},{"title":"[2507.00833v1] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/abs/2507.00833v1"},{"title":"RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation","url":"https://arxiv.org/html/2311.01455v3"},{"title":"Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation","url":"https://arxiv.org/html/2503.24361.pdf"},{"title":"[2512.01061] Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer","url":"https://arxiv.org/abs/2512.01061"},{"title":"DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning","url":"https://arxiv.org/html/2506.16012v1"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/html/2507.00833"},{"title":"[2507.00833] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/abs/2507.00833"}]

Based on the search results, here are several relevant papers on humanoid data generation and simulation from arXiv in 2026 and recent papers:

## Key Papers Found:

1. **Genie Sim 3.0: A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot** (arxiv:2601.02078)
   - Introduces Genie Sim 3.0, a unified simulation platform for robotic manipulation with an LLM-powered tool that constructs high-fidelity scenes from natural language instructions. The platform integrates scene generation, evaluation synthesis, data acquisition, and closed-loop model assessment, and open-sources 5140 assets, 10,000+ hours dataset, 100,000+ evaluation scenarios, and the complete codebase.

2. **OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction** (arxiv:2509.26633)
   - Introduces OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves spatial and contact relationships, generating kinematically feasible trajectories.

3. **HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning** (arxiv:2507.00833)
   - Presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints.

4. **Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer** (arxiv:2512.01061)
   - Recent progress in GPU-accelerated, photorealistic simulation has opened a scalable data-generation path for robot learning, where massive physics and visual randomization allow policies to generalize beyond curated environments.

5. **DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning** (arxiv:2506.16012)
   - Presents DualTHOR, a high-fidelity simulation environment designed to enable realistic bimanual humanoid robot interaction with parallel dual-arm control and an advanced physical engine.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad0e25a8-8ca1-4987-9379-895a5bce7562",
  "isSidechain": true,
  "promptId": "8d094254-63e5-4cc7-b74e-bff62736c708",
  "agentId": "aa0ba314500a9b4f4",
  "type": "user",
  "uuid": "f9039c9f-2cc8-43b9-83c2-2bfb089da04f",
  "sourceToolAssistantUUID": "ad0e25a8-8ca1-4987-9379-895a5bce7562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T13:33:43.751Z_

<details><summary>↩ Tool result · `toolu_01ALsWRT7MGZobpcwnkGafiJ`</summary>

```text
Web search results for query: "inverse reachability map bipedal humanoid imitation learning data generation"

Links: [{"title":"Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation","url":"https://arxiv.org/html/2508.11275v1"},{"title":"Efficient SE(3) Reachability Map Generation via Interplanar Integration of Intra-planar Convolutions | Request PDF","url":"https://www.researchgate.net/publication/355429152_Efficient_SE3_Reachability_Map_Generation_via_Interplanar_Integration_of_Intra-planar_Convolutions"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"ICRA2021PaperList/README.md at main · dectrfov/ICRA2021PaperList","url":"https://github.com/dectrfov/ICRA2021PaperList/blob/main/README.md"},{"title":"Robust walking motion generation for biped robots using manipulability-based reinforcement learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0921889025003069"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"Imitation learning of a model predictive controller for real-time humanoid robot walking - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197624020785"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"Bipedal Locomotion Primitive Learning, Control and Prediction from Human Data - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1474667016336655"},{"title":"Human Imitated Bipedal Locomotion with Frequency Based Gait Generator Network","url":"https://arxiv.org/html/2511.17387"}]

Based on the search results, here's what I found about inverse reachability maps, bipedal humanoid robots, imitation learning, and data generation:

## Differentiable Reachability Maps for Humanoid Motion

A data-driven method can learn a continuous representation of kinematic reachability, referred to as a differentiable reachability map, from a sample set of end-effector poses. This reachability map provides a scalar-valued function defined over the task space that indicates whether a given pose is reachable, and it is differentiable with respect to task-space coordinates.

Such differentiable reachability maps can be learned from a set of end-effector poses generated using a robot's kinematic model, using either a neural network or a support vector machine as the learning model. Various motion generation problems, such as footstep planning, multi-contact motion planning, and loco-manipulation planning, can be formulated using reachability constraints expressed by the learned map.

## Inverse Reachability Mapping

An approach of inverting precomputed reachability representations can be used in order to generate suitable robot base positions for grasping. An orientation-based reachability map can support on-line end effector frame extensions, enabling robots to handle partially constrained task paths with different tool frames.

## Imitation Learning for Bipedal Humanoids

Imitation learning may be employed to copy the behavior of a model predictive controller to a neural network, being able to predict the trajectory of the Center of Mass (CoM), as well as the position, rotation, and duration of each step.

A lightweight framework combines a gait generator network learned from human motion with Proximal Policy Optimization (PPO) controller for torque control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3aec3c0-727b-4b78-b23d-d021e6624347",
  "isSidechain": true,
  "promptId": "8d094254-63e5-4cc7-b74e-bff62736c708",
  "agentId": "aa0ba314500a9b4f4",
  "type": "user",
  "uuid": "7ef60b7a-dd85-4af5-a930-bb51d8f7210f",
  "sourceToolAssistantUUID": "b3aec3c0-727b-4b78-b23d-d021e6624347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T13:33:59.282Z_

## Independent Verification Report: LocoMimicGen Paper Claims

Based on comprehensive searches, here are my findings:

### **Search 1: SoftMimicGen (arXiv:2603.25725) - CONFIRMED**
✓ **Paper exists and is real.** SoftMimicGen was submitted to arXiv on March 26, 2026 (ID: 2603.25725). It extends MimicGen to deformable object manipulation, addressing the challenge of demonstration transfer for deformable objects (cloth, foam, flexible tubes) where objects deform differently under each grasp. The paper covers humanoid embodiments among four different robot platforms and has an official project website at softmimicgen.github.io.

### **Search 2: ULTRA (arXiv:2603.03279) - CONFIRMED**
✓ **Paper exists and is real.** ULTRA was submitted on March 3, 2026 (ID: 2603.03279). The full title is "ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation." It presents a physics-driven neural retargeting algorithm for translating MoCap data to humanoid embodiments and supports both dense motion references and sparse task specifications. Evaluated on the Unitree G1 humanoid robot.

### **Search 3: NEW papers April-May 2026 on humanoid loco-manipulation - NOTABLE CONCURRENT WORK FOUND**
⚠ **Concurrent work discovered (not papers from April-May specifically, but recent 2026 work):**
- **Genie Sim 3.0** (2601.02078, January 2026): High-fidelity simulation platform for humanoid robots with LLM-powered scene generation and 10,000+ hours of data
- **OmniRetarget** (2509.26633, September 2025): Interaction-preserving data generation for humanoid whole-body loco-manipulation using interaction meshes
- **HumanoidGen** (2507.00833, July 2025): Data generation for bimanual dexterous manipulation via LLM reasoning
- **DualTHOR** (2506.16012): Dual-arm humanoid simulation platform

### **Search 4: SE(3) object-centric demonstration generation - FOUND RELATED WORK**
✓ **Relevant work exists but not specific to loco-manipulation:** SPOT (2411.00965) - "SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation" from NVIDIA. This provides SE(3)-based object-centric representation for manipulation tasks but appears focused on manipulation rather than loco-manipulation specifically.

### **Search 5: Stance selection/reachability for humanoid data generation - PARTIALLY FOUND**
⚠ **Reachability research exists but no paper specifically solving "IRM-for-bipedal-data-generation":** Found "Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation" (2508.11275), which covers differentiable reachability representations. However, no papers were found that specifically frame inverse reachability mapping as a novel contribution for automating bipedal data generation—this may indeed be novel to LocoMimicGen.

### **Search 6: DemoGen RSS 2025 - CONFIRMED**
✓ **Paper exists and is correctly characterized.** DemoGen is an RSS25 paper on synthetic demonstration generation for visuomotor policy learning. It demonstrates 90.8% success on bimanual humanoid platforms and can generate hundreds of spatially-augmented synthetic demonstrations from a single human demo. Has official implementation on GitHub and project website.

### **Search 7: Isaac Lab PR #3259 and recent updates - CONFIRMED**
✓ **PR #3259 is real and matches characterization.** The pull request "Adds locomanipulation data generation via disjoint navigation" is active on the Isaac Lab GitHub repository. It enables generating loco-manipulation datasets from manipulation-only demonstrations by segmenting tasks into pick-navigate-place phases with RL-based locomotion and IK-based manipulation. Isaac Lab 2.3 explicitly features enhanced whole-body control and data generation automation.

---

### **Summary of Verification:**

| Claim | Status | Notes |
|-------|--------|-------|
| SoftMimicGen (2603.25725) | ✓ CONFIRMED | Real paper from March 2026, extends MimicGen to deformable objects |
| ULTRA (2603.03279) | ✓ CONFIRMED | Real paper from March 2026, MoCap retargeting for humanoid loco-manipulation |
| Concurrent April-May 2026 papers | ⚠ NOT FOUND | No papers from April-May specifically, but multiple recent 2026 loco-manipulation papers exist (Genie Sim 3.0, OmniRetarget, etc.) |
| SE(3) demo generation work | ⚠ PARTIAL | SPOT exists but focuses on manipulation, not loco-manipulation |
| Stance selection for bipedal data generation | ⚠ POTENTIALLY NOVEL | Reachability mapping research exists but no paper found claiming this specific contribution |
| DemoGen RSS 2025 | ✓ CONFIRMED | Real paper, correctly characterized as RSS25 with bimanual humanoid results |
| Isaac Lab PR #3259 | ✓ CONFIRMED | Real PR with loco-manipulation data generation via disjoint navigation |

**Key Observation:** The claim about "inverse reachability mapping for stance selection" appears to be genuinely novel—while reachability research exists broadly, no papers were found claiming this as a solved problem for automating bipedal data generation specifically.

Sources:
- [SoftMimicGen arXiv](https://arxiv.org/abs/2603.25725)
- [ULTRA arXiv](https://arxiv.org/abs/2603.03279)
- [Genie Sim 3.0 arXiv](https://arxiv.org/abs/2601.02078)
- [DemoGen GitHub](https://github.com/TEA-Lab/DemoGen)
- [Isaac Lab PR #3259](https://github.com/isaac-sim/IsaacLab/pull/3259)
- [SPOT SE(3) Manipulation](https://arxiv.org/abs/2411.00965)
- [Differentiable Reachability Maps](https://arxiv.org/abs/2508.11275)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ef60b7a-dd85-4af5-a930-bb51d8f7210f",
  "isSidechain": true,
  "agentId": "aa0ba314500a9b4f4",
  "requestId": "req_011CatyTHUuJPgikwwDMqwCJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6840fea-c1a4-426b-97f4-209412690572",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c452eabe-2ba3-4020-bd3d-a3e30f0fb913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CyaEPhuYQsBnD9B2NvXszu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1888,
      "cache_creation_input_tokens": 6208,
      "cache_read_input_tokens": 17056,
      "output_tokens": 1551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6208
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1888,
          "output_tokens": 1551,
          "cache_read_input_tokens": 17056,
          "cache_creation_input_tokens": 6208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6208,
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
