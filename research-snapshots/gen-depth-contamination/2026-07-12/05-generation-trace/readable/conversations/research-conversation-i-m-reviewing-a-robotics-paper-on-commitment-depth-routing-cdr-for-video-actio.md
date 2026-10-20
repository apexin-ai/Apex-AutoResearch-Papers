# Research conversation: I'm reviewing a robotics paper on "Commitment Depth Routing" (CDR) for Video-Action Models (WAMs). CDR proposes selectiv

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a1b7541f794021425.jsonl`
- **Structured JSON:** [`894e6bec775c8c716006.json`](../../sessions/89/894e6bec775c8c716006.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-10T09:02:07.691Z_

I'm reviewing a robotics paper on "Commitment Depth Routing" (CDR) for Video-Action Models (WAMs). CDR proposes selectively activating video denoising per-observation based on how much video quality helps action prediction. I need to find any papers that might overlap significantly with CDR's contributions that the authors may have missed.

Please search for:

1. Papers on adaptive/selective video denoising for robot policies (2025-2026): 
   - Search: "adaptive video denoising robot manipulation policy 2026 arxiv"
   - Search: "selective video activation robot control diffusion 2026"

2. Papers on per-observation routing or early exit for diffusion-based robot policies (2025-2026):
   - Search: "per-observation routing diffusion policy robot 2026"
   - Search: "adaptive denoising steps robot manipulation arxiv 2026"

3. Papers specifically on noise level scheduling for video diffusion as robot policy:
   - Search: "noise scheduling video diffusion robot policy 2026"
   - Search: "video diffusion timestep routing robot manipulation 2026 arxiv"

4. Papers on "VADF" vision-adaptive diffusion policy (arXiv:2604.15938):
   - Search: "vision adaptive diffusion policy framework VADF arxiv 2604.15938"

5. Any papers specifically about "D3P" adaptive denoising steps RL:
   - Search: "D3P dynamic denoising diffusion policy reinforcement learning arxiv 2508"

For each search, please check 2-3 top results carefully. If you find papers that match CDR's core contribution (learning to predict per-observation video denoising depth for WAMs), report them in detail with arxiv IDs and what they cover. Search breadth: thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "99f25f76-8815-4663-bc75-9507243c6af7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T09:02:08.979Z_

I'll conduct a comprehensive search for papers that might overlap with the CDR (Commitment Depth Routing) contribution. Let me search systematically across all the areas you've identified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99f25f76-8815-4663-bc75-9507243c6af7",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catck2qcv6KZMtLKMJpfX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2c2b99ff-4320-4f66-b820-1ff9dcc901b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0178V93atbF6xLRJ5Zu2b9Vz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 3 · 2026-05-10T09:02:09.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xca7LAFbTZBH6aEhmTv6Kq`</summary>

```json
{
  "query": "adaptive video denoising robot manipulation policy 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c2b99ff-4320-4f66-b820-1ff9dcc901b3",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catck2qcv6KZMtLKMJpfX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "455717ac-2fc7-4bd6-850e-33624f9b399d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0178V93atbF6xLRJ5Zu2b9Vz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 4 · 2026-05-10T09:02:09.337Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015p5iJNUPf7cXCF25egGcZt`</summary>

```json
{
  "query": "selective video activation robot control diffusion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "455717ac-2fc7-4bd6-850e-33624f9b399d",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catck2qcv6KZMtLKMJpfX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "781ef824-80d0-4257-9cd5-cb5d7bc32779",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0178V93atbF6xLRJ5Zu2b9Vz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 5 · 2026-05-10T09:02:09.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WdYyR4kdSAr9NBN59PJLof`</summary>

```json
{
  "query": "per-observation routing diffusion policy robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "781ef824-80d0-4257-9cd5-cb5d7bc32779",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catck2qcv6KZMtLKMJpfX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "03c922ef-0bd4-4d33-84a1-5268d390be74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0178V93atbF6xLRJ5Zu2b9Vz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 6 · 2026-05-10T09:02:09.556Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KWfmTgV8PfiC1Li2ujFb7E`</summary>

```json
{
  "query": "adaptive denoising steps robot manipulation arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03c922ef-0bd4-4d33-84a1-5268d390be74",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catck2qcv6KZMtLKMJpfX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "068bc2c3-5c6d-447f-b8c4-e83f41722110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0178V93atbF6xLRJ5Zu2b9Vz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 7 · 2026-05-10T09:02:09.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0157Ca54DdDMGaKmZdnz4ggq`</summary>

```json
{
  "query": "noise scheduling video diffusion robot policy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "068bc2c3-5c6d-447f-b8c4-e83f41722110",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catck2qcv6KZMtLKMJpfX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fa20c13e-6af0-4e37-843e-93b39f0a4534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0178V93atbF6xLRJ5Zu2b9Vz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 8 · 2026-05-10T09:02:09.825Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U2A6J7huvAtNC8gBSvHM7Z`</summary>

```json
{
  "query": "video diffusion timestep routing robot manipulation 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa20c13e-6af0-4e37-843e-93b39f0a4534",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catck2qcv6KZMtLKMJpfX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6bfee55b-6927-4b25-8835-65d869d2c0c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0178V93atbF6xLRJ5Zu2b9Vz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

### Tool result

_source line 9 · 2026-05-10T09:02:15.125Z_

<details><summary>↩ Tool result · `toolu_01WdYyR4kdSAr9NBN59PJLof`</summary>

```text
Web search results for query: "per-observation routing diffusion policy robot 2026"

Links: [{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance","url":"https://arxiv.org/html/2505.08712v2"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"NVIDIA Cosmos Policy: Advanced Robot Control Guide","url":"https://www.huuphan.com/2026/02/nvidia-cosmos-policy-advanced-robot.html"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub","url":"https://github.com/real-stanford/diffusion_policy"},{"title":"Diffusion Policy Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=mEpqHvbD2h"},{"title":"Diffusion Policy in Robotics: The Generative Revolution in Robot Control | by Arjun R | Medium","url":"https://medium.com/@itsrarjun/diffusion-policy-in-robotics-the-generative-revolution-in-robot-control-4e9379f7ba81"}]

Based on the search results, I found information about diffusion policies for robotics. However, the search results don't contain specific information about "per-observation routing diffusion policy" as a distinct or named method.

The search results show that Diffusion Policy is a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. This represents a general framework for robot learning using diffusion models.

The results also indicate that the diffusion process is conditioned on a history of observations using feature-wise linear modification (FiLM). This conditioning on observations is central to how diffusion policies work in robotics.

While the search results don't explicitly discuss "per-observation routing" as a specific technique, they show the broader landscape of diffusion-based policies in robotics as of 2025-2026. If you're looking for information about a specific research paper or technique with "per-observation routing" in its name, that particular method doesn't appear in the top search results. You may want to try searching for it more directly or provide additional context about the research or authors involved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03c922ef-0bd4-4d33-84a1-5268d390be74",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "477f6f41-3f57-4696-a7e6-edbf37a553e7",
  "sourceToolAssistantUUID": "03c922ef-0bd4-4d33-84a1-5268d390be74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T09:02:16.510Z_

<details><summary>↩ Tool result · `toolu_0157Ca54DdDMGaKmZdnz4ggq`</summary>

```text
Web search results for query: "noise scheduling video diffusion robot policy 2026"

Links: [{"title":"Diffusion Policy: Teaching Robots to Act by Denoising","url":"https://vizuara.substack.com/p/diffusion-policy-teaching-robots"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"D3P: Dynamic Denoising Diffusion Policy via ...","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations | OpenReview","url":"https://openreview.net/forum?id=c0dhw1du33"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"Large Video Planner Enables Generalizable Robot Control","url":"https://arxiv.org/html/2512.15840v1"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Fast Policy Synthesis with Variable Noise Diffusion Models","url":"https://arxiv.org/pdf/2406.04806"},{"title":"Video Generators are Robot Policies - Columbia University","url":"https://videopolicy.cs.columbia.edu/assets/video_policy.pdf"}]

Here are the web search results for "noise scheduling video diffusion robot policy 2026":

## Key Findings

**Noise Scheduling in Robot Policies:**

The noise schedule, defined by functions of the iteration step and additive Gaussian noise, controls the extent to which diffusion policy captures high- and low-frequency characteristics of action signals. For robot control tasks, the Square Cosine Schedule proposed in iDDPM has been found to work best.

**Video Diffusion for Robot Policy:**

Recent developments in 2025-2026 show growing interest in video diffusion models for robotics:

- Video diffusion models (VDMs) demonstrate the ability to predict future frames and showcase a strong understanding of the physical world, with representations that encompass both current static information and predicted future dynamics for robot action learning.

- Large Video Planner (LVP) is a large-scale video foundation model designed for robotic manipulation with an associated framework for deploying it as a zero-shot policy on real robots.

- Video diffusion models can synthesize accurate videos of robot behavior, and small decoders only need minimal demonstration data to learn to map videos into executable robot actions, with the video generative model serving as the policy itself.

**Recent 2026 Developments:**

Dynamic Denoising Diffusion Policy (D3P) is a diffusion-based policy that adaptively allocates denoising steps across actions at test time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa20c13e-6af0-4e37-843e-93b39f0a4534",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "1c332cd3-c9cb-45b5-bd9b-6200e2650265",
  "sourceToolAssistantUUID": "fa20c13e-6af0-4e37-843e-93b39f0a4534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T09:02:17.332Z_

<details><summary>↩ Tool result · `toolu_01Xca7LAFbTZBH6aEhmTv6Kq`</summary>

```text
Web search results for query: "adaptive video denoising robot manipulation policy 2026 arxiv"

Links: [{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2604.15938"},{"title":"Large-Scale Actionless Video Pre-Training via Discrete Diffusion for Efficient Policy Learning","url":"https://arxiv.org/html/2402.14407v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"ForeDiffusion: Foresight-Conditioned Diffusion Policy via Future View Construction for Robot Manipulation","url":"https://arxiv.org/html/2601.12925"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://arxiv.org/html/2508.00697"},{"title":"Adaptive Diffusion Policy Optimization for Robotic Manipulation","url":"https://arxiv.org/html/2505.08376v1"},{"title":"From Human Hands to Robot Arms: Manipulation Skills Transfer via Trajectory Alignment","url":"https://arxiv.org/html/2510.00491v1"}]

I found several relevant papers from arXiv related to adaptive video denoising and robot manipulation policies in 2026. Here are the key results:

## Main Findings:

**1. VADF: Vision-Adaptive Diffusion Policy Framework**
VADF is a unified framework that introduces vision-driven adaptive computation into diffusion policies, addressing sample and stage heterogeneity for the first time. Simple stages receive shorter denoising budgets for speed, while complex stages obtain more steps for higher precision, substantially reducing average cost while increasing success rates.

**2. X-WAM: Unified 4D World Action Model**
X-WAM is a unified 4D World Action Model that jointly predicts future multi-view RGB-D videos and robot actions from video priors, featuring a lightweight depth adaptation module for spatial reconstruction and Asynchronous Noise Sampling (ANS) for efficient action decoding.

**3. D3P: Dynamic Denoising Diffusion Policy**
D3P is a diffusion-based policy that adaptively allocates denoising steps across actions at test time, using a lightweight, state-aware adaptor to allocate the optimal number of denoising steps for each action. D3P achieves an average 2.2× inference speed-up over baseline methods while maintaining comparable performance.

**4. ForeDiffusion**
ForeDiffusion significantly improves the success rate by 23% in complex manipulation tasks, where other models perform poorly.

**5. World Action Models as Zero-shot Policies**
DreamZero is a 14B autoregressive diffusion transformer trained with a teacher-forcing chunk-wise video denoising objective.

These papers represent recent advances in combining adaptive denoising strategies with robot manipulation policies to improve both efficiency and performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "455717ac-2fc7-4bd6-850e-33624f9b399d",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "49e81f45-856e-4e5b-af4c-7d54312c59cd",
  "sourceToolAssistantUUID": "455717ac-2fc7-4bd6-850e-33624f9b399d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T09:02:17.336Z_

<details><summary>↩ Tool result · `toolu_015p5iJNUPf7cXCF25egGcZt`</summary>

```text
Web search results for query: "selective video activation robot control diffusion 2026"

Links: [{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control | OpenReview","url":"https://openreview.net/forum?id=OeDwYtp8n1"},{"title":"Video Generators are Robot Policies - Columbia University","url":"https://videopolicy.cs.columbia.edu/assets/video_policy.pdf"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"GitHub - mbreuss/diffusion-literature-for-robotics: Summary of key papers and blogs about diffusion models to learn about the topic. Detailed list of all published diffusion robotics papers. · GitHub","url":"https://github.com/mbreuss/diffusion-literature-for-robotics"},{"title":"Real-Time Motion-Controllable Autoregressive Video Diffusion | OpenReview","url":"https://openreview.net/forum?id=4Q55RwYte9"},{"title":"Exploring Conditions for Diffusion models in Robotic Control | OpenReview","url":"https://openreview.net/forum?id=9h5MCXYu3y"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the web search results, I found several relevant research papers and resources related to video diffusion models for robot control from 2025-2026. Here are the key findings:

## Recent Research on Video Diffusion and Robot Control

Recent breakthroughs in generative modeling, such as diffusion and flow-matching, have enabled high-fidelity controllable video synthesis conditioned on user inputs such as text prompts, robot actions, and video frames.

### Unified World Models (UWM)

A UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies.

### RoboMaster Framework

RoboMaster learns an interactive world simulator for robotic manipulation, based on a video diffusion model conditioned on a collaborative trajectory, which controls the motions of both the robotic arm and the manipulated object.

### MotuBrain: World Action Model

Separate SNR-based timestep sampling is used for the two modalities during training. This approach addresses the challenge of inference latency in world-action models for robot control.

### Vision-Language-Action Research

There is comprehensive analysis of 164 Vision-Language-Action (VLA) model submissions at ICLR 2026, discovering trends in discrete diffusion VLAs, reasoning models, benchmarks (LIBERO, CALVIN, SIMPLER), and the gap between frontier and academic research.

The search results indicate this is a very active research area with significant developments in 2025-2026, particularly around selective control of diffusion timesteps for video generation in robotic applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "781ef824-80d0-4257-9cd5-cb5d7bc32779",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "653ccf00-ecb4-4652-a3c0-4d867afa0ac5",
  "sourceToolAssistantUUID": "781ef824-80d0-4257-9cd5-cb5d7bc32779",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T09:02:18.555Z_

<details><summary>↩ Tool result · `toolu_01U2A6J7huvAtNC8gBSvHM7Z`</summary>

```text
Web search results for query: "video diffusion timestep routing robot manipulation 2026 arxiv"

Links: [{"title":"VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation","url":"https://arxiv.org/html/2411.09153v1"},{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2604.15938"},{"title":"RoboTransfer: Controllable Geometry-Consistent Video Diffusion for Manipulation Policy Transfer","url":"https://arxiv.org/html/2505.23171"},{"title":"Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?","url":"https://arxiv.org/html/2604.04502"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Abstracting Robot Manipulation Skills via Mixture-of- ...","url":"https://arxiv.org/pdf/2601.21251"},{"title":"RoboTransfer: Geometry-Consistent Video Diffusion for Robotic Visual Policy Transfer","url":"https://arxiv.org/html/2505.23171v1"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Large Video Planner Enables Generalizable Robot Control","url":"https://arxiv.org/html/2512.15840v1"}]

I found several relevant papers on arXiv related to video diffusion, timestep routing, and robot manipulation. Here are the key results:

## Most Relevant Papers:

**1. VADF: Vision-Adaptive Diffusion Policy Framework** (2026, April)
VADF is a fully adaptive diffusion policy framework that dynamically optimizes during training via a learnable timestep sampler and online sample re-weighting. During inference, it achieves zero-shot task decomposition and stage-wise dynamic scheduling using a vision-language model (VLM), jointly controlling denoising steps. This addresses the limitation where early denoising steps and contact-rich trajectories exert a disproportionate influence on policy robustness but often receive insufficient optimization focus under a uniform regime.

**2. RoboTransfer: Controllable Geometry-Consistent Video Diffusion** (2026, January)
RoboTransfer is a diffusion-based video generation framework for synthesizing robotic data that leverages cross-view feature interactions and globally consistent 3D geometry, ensuring multi-view geometric consistency while enabling fine-grained control over scene elements.

**3. Unified World Models: Coupling Video and Action Diffusion** (2025, April)
UWM is a framework that leverages both video and action data for policy learning by integrating an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality.

**4. Large Video Planner Enables Generalizable Robot Control** (2025, December)
Large Video Planner (LVP) is a large-scale video foundation model designed for robotic manipulation with an associated framework for deploying it as a zero-shot policy on real robots.

These papers represent recent work on timestep routing and adaptive diffusion processes for robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bfee55b-6927-4b25-8835-65d869d2c0c8",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "26c3a339-0737-4dac-b091-addae1a4f437",
  "sourceToolAssistantUUID": "6bfee55b-6927-4b25-8835-65d869d2c0c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T09:02:19.910Z_

<details><summary>↩ Tool result · `toolu_01KWfmTgV8PfiC1Li2ujFb7E`</summary>

```text
Web search results for query: "adaptive denoising steps robot manipulation arxiv 2026"

Links: [{"title":"ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/html/2508.06266"},{"title":"Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation","url":"https://arxiv.org/html/2604.01414"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"Abstracting Robot Manipulation Skills via Mixture-of- ...","url":"https://arxiv.org/pdf/2601.21251"},{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2604.15938"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"D3P: Dynamic Denoising Difusion Policy via Reinforcement Learning Shu’ang Yu","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation","url":"https://arxiv.org/html/2510.21744"},{"title":"[2508.06266] ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/abs/2508.06266"}]

I found several relevant papers on arXiv related to adaptive denoising steps for robot manipulation. Here are the key results:

## Primary Results:

1. **D3P: Dynamic Denoising Diffusion Policy (2025)** - This paper proposes Dynamic Denoising Diffusion Policy (D3P), a diffusion-based policy that adaptively allocates denoising steps across actions at test time. D3P uses a lightweight, state-aware adaptor to allocate the optimal number of denoising steps for each action. The method achieves an average 2.2× inference speed-up over baseline methods while maintaining comparable performance.

2. **ADPro: Adaptive Diffusion Policy (2025)** - This work introduces ADP, a test-time adaptive diffusion policy that injects structure into the denoising process through three complementary mechanisms, including embedding a manifold constraint guided by the relative pose between end-effector and target object, and refining the reverse diffusion dynamics using a Gaussian spherical prior, constraining the denoising steps to lie on a hypersphere.

3. **VADF: Vision-Adaptive Diffusion Policy Framework (2026)** - VADF is a fully adaptive diffusion policy framework that during training dynamically optimizes via a learnable timestep sampler and online sample re-weighting, and during inference achieves zero-shot task decomposition and stage-wise dynamic scheduling using a vision-language model.

4. **FORGE-Tree (2025)** - This method aligns denoising to stage structure and casts inference as a budgeted search over denoising meta-actions, which segment to edit next and how aggressively to denoise it, so compute is adaptively focused where it matters.

These papers represent recent advances in adaptive denoising techniques for robot manipulation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "068bc2c3-5c6d-447f-b8c4-e83f41722110",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "b90ebcff-8ba0-4102-a1b7-c95c0239dd1a",
  "sourceToolAssistantUUID": "068bc2c3-5c6d-447f-b8c4-e83f41722110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T09:02:21.092Z_

Now let me search for the specific papers you mentioned (VADF and D3P) with their exact identifiers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b90ebcff-8ba0-4102-a1b7-c95c0239dd1a",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catckw4srkkJvyEcfcacf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6ce3bde-81f0-4614-a685-5d2e4cd91573",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GRPyXz4e5U5RkXa4vXGJD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1838,
      "cache_creation_input_tokens": 4850,
      "cache_read_input_tokens": 14638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4850,
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

_source line 16 · 2026-05-10T09:02:21.342Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0121eqrRmsJvhJJJm9iqg6F5`</summary>

```json
{
  "query": "vision adaptive diffusion policy framework VADF arxiv 2604.15938"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6ce3bde-81f0-4614-a685-5d2e4cd91573",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catckw4srkkJvyEcfcacf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8175bd2c-c3a4-410a-8844-e54ac9415867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GRPyXz4e5U5RkXa4vXGJD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1838,
      "cache_creation_input_tokens": 4850,
      "cache_read_input_tokens": 14638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4850,
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

_source line 17 · 2026-05-10T09:02:21.571Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018jvrzgzpZ2rEKx7apJV99e`</summary>

```json
{
  "query": "D3P dynamic denoising diffusion policy reinforcement learning arxiv 2508.06804"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8175bd2c-c3a4-410a-8844-e54ac9415867",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011Catckw4srkkJvyEcfcacf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1be5969f-60a9-4fc4-a2c5-25ef48753c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GRPyXz4e5U5RkXa4vXGJD7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1838,
      "cache_creation_input_tokens": 4850,
      "cache_read_input_tokens": 14638,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1838,
          "output_tokens": 149,
          "cache_read_input_tokens": 14638,
          "cache_creation_input_tokens": 4850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4850,
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

_source line 18 · 2026-05-10T09:02:28.866Z_

<details><summary>↩ Tool result · `toolu_0121eqrRmsJvhJJJm9iqg6F5`</summary>

```text
Web search results for query: "vision adaptive diffusion policy framework VADF arxiv 2604.15938"

Links: [{"title":"[2604.15938] VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2604.15938"},{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2604.15938"},{"title":"(PDF) VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://www.researchgate.net/publication/403976521_VADF_Vision-Adaptive_Diffusion_Policy_Framework_for_Efficient_Robotic_Manipulation"},{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2604.15938"},{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for ...","url":"https://arxiv.org/pdf/2604.15938"},{"title":"VADF: Vision-Adaptive Diffusion Framework. VADF introduces a... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/ADF-Vision-Adaptive-Diffusion-Framework-VADF-introduces-a-dualadaptive-mechanism-for_fig1_403976521"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"AdaVFM: Adaptive Vision Foundation Models for Edge Intelligence via LLM-Guided Execution","url":"https://arxiv.org/html/2604.15622"},{"title":"[2508.20072] Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/abs/2508.20072"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/diffusion_policy_2023.pdf"}]

I found detailed information about the paper. Here's what I found about VADF:

## VADF: Vision-Adaptive Diffusion Policy Framework

VADF (Vision-Adaptive Diffusion Policy Framework) is a vision-driven dual-adaptive framework that significantly reduces convergence steps and achieves early success in inference, with model-agnostic design enabling seamless integration into any diffusion policy architecture.

### Problem Being Addressed

Diffusion policies are becoming mainstream in robotic manipulation but suffer from hard negative class imbalance due to uniform sampling and lack of sample difficulty awareness, leading to slow training convergence and frequent inference timeout failures.

### Key Components

The framework has two main components:

1. **Adaptive Loss Network (ALN) for Training**: During training, the framework introduces Adaptive Loss Network (ALN), a lightweight MLP-based loss predictor that quantifies per-step sample difficulty in real time. Guided by hard negative mining, it performs weighted sampling to prioritize high-loss regions, enabling adaptive weight updates and faster convergence.

2. **Hierarchical Vision Task Segmenter (HVTS) for Inference**: HVTS leverages zero-shot task decomposition to dynamically schedule denoising budgets based on stage complexity, ensuring high precision with reduced latency.

### Evaluation

Extensive evaluations across multiple benchmarks (e.g., Push-T, Kitchen, Adroit) demonstrate consistent gains in training speed, inference efficiency, and task performance.

The paper was submitted on April 17, 2026, and represents work by researchers including Xinglei Yu from Fudan University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8175bd2c-c3a4-410a-8844-e54ac9415867",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "50be6d8a-bfea-4ffe-b3fa-636b62d69df3",
  "sourceToolAssistantUUID": "8175bd2c-c3a4-410a-8844-e54ac9415867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T09:02:30.067Z_

<details><summary>↩ Tool result · `toolu_018jvrzgzpZ2rEKx7apJV99e`</summary>

```text
Web search results for query: "D3P dynamic denoising diffusion policy reinforcement learning arxiv 2508.06804"

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"[2508.06804] D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/abs/2508.06804"},{"title":"D3P: Dynamic Denoising Difusion Policy via Reinforcement Learning Shu’ang Yu","url":"https://arxiv.org/pdf/2508.06804"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2508.06804v1"},{"title":"(PDF) D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://www.researchgate.net/publication/394438722_D3P_Dynamic_Denoising_Diffusion_Policy_via_Reinforcement_Learning"},{"title":"Structured Denoising Diffusion Models in Discrete State-Spaces","url":"https://arxiv.org/pdf/2107.03006"},{"title":"[2107.03006] Structured Denoising Diffusion Models in Discrete State-Spaces","url":"https://arxiv.org/abs/2107.03006"},{"title":"[2305.13301] Training Diffusion Models with Reinforcement Learning","url":"https://arxiv.org/abs/2305.13301"},{"title":"One-Step Flow Q-Learning: Addressing the Diffusion Policy Bottleneck in Offline Reinforcement Learning","url":"https://arxiv.org/html/2508.13904"},{"title":"GitHub - Abdennacer-Badaoui/D3PMs: A small project that uses Discrete Denoising Diffusion Probabilistic Models (D3PMs), a generative model for discrete data that builds upon the success of Denoising Diffusion Probabilistic Models (DDPMs) in continuous spaces. · GitHub","url":"https://github.com/Abdennacer-Badaoui/D3PMs"}]

Based on the search results, here's what I found about the D3P paper (arxiv 2508.06804):

## Overview

D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning addresses the fact that diffusion policies excel at learning complex action distributions for robotic visuomotor tasks, yet their iterative denoising process poses a major bottleneck for real-time deployment.

## Key Problem and Solution

Existing acceleration methods apply a fixed number of denoising steps per action, implicitly treating all actions as equally important. However, experiments reveal that robotic tasks often contain a mix of crucial and routine actions, which differ in their impact on task success.

D3P is a diffusion-based policy that adaptively allocates denoising steps across actions at test time, using a lightweight, state-aware adaptor to allocate the optimal number of denoising steps for each action.

## Architecture and Training

The D3P architecture consists of a standard noise predicting network as the base diffusion policy and a lightweight adaptor designed to predict the noise-level strides based on the current observation. The adaptor and base diffusion policy are jointly optimized via reinforcement learning to balance task performance and inference efficiency.

## Results

On simulated tasks, D3P achieves an averaged 2.2× inference speed-up over baselines without degrading success. Furthermore, D3P demonstrates effectiveness on a physical robot, achieving a 1.9× acceleration over the baseline.

The paper was submitted to arXiv on August 9, 2025, with authors including Shu-Ang Yu, Feng Gao, Yi Wu, Chao Yu, and Yu Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1be5969f-60a9-4fc4-a2c5-25ef48753c7f",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "9c8201d7-71b0-41eb-ac63-e3b924b5db41",
  "sourceToolAssistantUUID": "1be5969f-60a9-4fc4-a2c5-25ef48753c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T09:02:31.227Z_

Let me do a few additional targeted searches to ensure comprehensive coverage:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c8201d7-71b0-41eb-ac63-e3b924b5db41",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011CatcmgWoXaVj3AtwbwbCv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b333fe19-35da-472f-b74c-21c4b08b806f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNTWj1Xr7munYNQpYZLd4F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3931,
      "cache_read_input_tokens": 19488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3931,
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

_source line 21 · 2026-05-10T09:02:31.474Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wqsng3P3wKkiH8D1jurjor`</summary>

```json
{
  "query": "\"video action model\" \"denoising depth\" robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b333fe19-35da-472f-b74c-21c4b08b806f",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011CatcmgWoXaVj3AtwbwbCv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c4751a5-d1a7-4a85-ba81-9b2ce2eb7b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNTWj1Xr7munYNQpYZLd4F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3931,
      "cache_read_input_tokens": 19488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3931,
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

_source line 22 · 2026-05-10T09:02:31.921Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018P76FPcLrsKfdRadE4xHm2`</summary>

```json
{
  "query": "early exit diffusion policy robot observation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c4751a5-d1a7-4a85-ba81-9b2ce2eb7b84",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011CatcmgWoXaVj3AtwbwbCv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04e316eb-10dc-4c70-bb4c-f8c30aa3f158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNTWj1Xr7munYNQpYZLd4F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3931,
      "cache_read_input_tokens": 19488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3931,
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

_source line 23 · 2026-05-10T09:02:32.113Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CxeBLAGakEz3kuM2mj9YYa`</summary>

```json
{
  "query": "WAM \"world action model\" video quality denoising 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04e316eb-10dc-4c70-bb4c-f8c30aa3f158",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011CatcmgWoXaVj3AtwbwbCv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aad2de95-0303-4929-aca3-c56ec18dbfbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNTWj1Xr7munYNQpYZLd4F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3931,
      "cache_read_input_tokens": 19488,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3931
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 176,
          "cache_read_input_tokens": 19488,
          "cache_creation_input_tokens": 3931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3931,
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

_source line 24 · 2026-05-10T09:02:38.546Z_

<details><summary>↩ Tool result · `toolu_018P76FPcLrsKfdRadE4xHm2`</summary>

```text
Web search results for query: "early exit diffusion policy robot observation 2025 2026"

Links: [{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"Diffusion Trajectory-guided Policy: A Novel Framework for Long-Horizon Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=VaoeAi5CW8"},{"title":"A Survey on Diffusion Policy for Robotic Manipulation: Taxonomy, Analysis, and Future Directions | TechRxiv","url":"https://www.techrxiv.org/doi/full/10.36227/techrxiv.174378343.39356214/v1"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"Diffusion Policy in Robotics: The Generative Revolution in Robot Control | by Arjun R | Medium","url":"https://medium.com/@itsrarjun/diffusion-policy-in-robotics-the-generative-revolution-in-robot-control-4e9379f7ba81"},{"title":"Diffusion Trajectory-Guided Policy for Long-Horizon Robot Manipulation | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/7083369/11215960/11197656.pdf"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"}]

Based on the search results, I found relevant information about diffusion policies for robot control with visual observations. Here are the key findings:

## Diffusion Policy Overview

Diffusion Policy is a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. The diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability.

## Visual Observations and Conditioning

Robot actions are usually dependent on simulated or real-world observations with multi-modal sensory data and the robot's proprioception, thus the network used in the denoising process has to be conditioned on these observations. Most methods directly condition on visual observations, such as images, point clouds, or feature encodings and embeddings.

## Recent Developments (2025-2026)

Recent research has focused on efficiency improvements. Since the diffusion transformer requires multiple denoising steps to generate action prediction, which leads to high latency, researchers propose to accelerate the model by pruning and distillation.

Additionally, the Diffusion Trajectory-guided Policy (DTP) framework generates task-relevant trajectories through a diffusion model to guide policy learning for long-horizon tasks.

The search results reveal that diffusion policies have become a prominent approach in robotic manipulation research, with ongoing work on improving efficiency and handling complex, long-horizon tasks with visual observations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04e316eb-10dc-4c70-bb4c-f8c30aa3f158",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "655dc7d8-c8bf-4c46-8028-2b2bf05e6940",
  "sourceToolAssistantUUID": "04e316eb-10dc-4c70-bb4c-f8c30aa3f158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T09:02:39.533Z_

<details><summary>↩ Tool result · `toolu_01CxeBLAGakEz3kuM2mj9YYa`</summary>

```text
Web search results for query: "WAM "world action model" video quality denoising 2026"

Links: [{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"X-WAM: Bridging Action and 4D Synthesis | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/ai-research/2026/x-wam-bridging-action-and-4d-synthesis"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"}]

Based on the search results, I found several recent papers and projects related to World Action Models (WAM) and video quality in 2026:

## X-WAM: Unified 4D World Action Model

X-WAM is a unified 4D World Action Model that simultaneously targets high-fidelity video generation, 3D spatial reconstruction, and real-time policy execution. Regarding video quality and denoising:

X-WAM proposes Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency, which applies a specialized asynchronous denoising schedule during inference that rapidly decodes actions with fewer steps to enable efficient real-time execution, while dedicating the full sequence of steps to generate high-fidelity video.

X-WAM is built upon a pretrained video diffusion model (Wan2.2-5B) and fine-tuned to jointly denoise multi-view RGB videos, proprioceptive states, and robot actions within a single unified sequence.

## Fast-WAM: Alternative Approach to Future Imagination

Another notable 2026 development is Fast-WAM, where World Action Models have emerged as a promising alternative to Vision-Language-Action models for embodied control because they explicitly model how visual observations may evolve under action, though most existing WAMs follow an imagine-then-execute paradigm that incurs substantial test-time latency from iterative video denoising. Fast-WAM keeps only the clean latent tokens of the current observation, processes them with the video backbone once, and directly generates actions without explicit future video denoising, removing the main runtime bottleneck of imagine-then-execute WAMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aad2de95-0303-4929-aca3-c56ec18dbfbc",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "a0fb081c-b94f-49b0-8288-f731a743901d",
  "sourceToolAssistantUUID": "aad2de95-0303-4929-aca3-c56ec18dbfbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T09:02:41.185Z_

<details><summary>↩ Tool result · `toolu_01Wqsng3P3wKkiH8D1jurjor`</summary>

```text
Web search results for query: ""video action model" "denoising depth" robot 2026"

Links: [{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Request PDF","url":"https://www.researchgate.net/publication/395371959_Unified_World_Models_Coupling_Video_and_Action_Diffusion_for_Pretraining_on_Large_Robotic_Datasets"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"Video-Action Models: Are video model backbones the future of VLAs? | Elvis Nava","url":"https://www.elvisnava.com/posts/2026_01_06_video_backbones/"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"},{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Video Generators are Robot Policies - Columbia University","url":"https://videopolicy.cs.columbia.edu/assets/video_policy.pdf"}]

I found several recent research papers on video action models with denoising depth for robotics from 2026. Here are the key findings:

## X-WAM: Unified 4D World Action Modeling

X-WAM is a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis (video + 3D reconstruction) in a single framework. The model addresses a key challenge in robot learning by handling both video generation and action control simultaneously.

### Key Technical Innovations:

**Depth Integration:** To leverage the strong visual priors of pretrained video diffusion models, X-WAM imagines the future world by predicting multi-view RGB-D videos, and obtains spatial information efficiently through a lightweight structural adaptation: replicating the final few blocks of the pretrained Diffusion Transformer into a dedicated depth prediction branch for the reconstruction of future spatial information.

**Asynchronous Denoising:** While synthesizing high-fidelity video necessitates numerous denoising steps, low-dimensional actions require far fewer steps, and can be accurately recovered even from highly noisy video latents. Motivated by this insight, we propose Asynchronous Noise Sampling (ANS).

### Performance:

X-WAM consistently outperforms all baselines on RoboCasa and RoboTwin 2.0 benchmarks and real-world earphone packing experiments, while producing superior 4D reconstruction and generation across both visual and geometric metrics.

## Related Approaches

Other concurrent research includes EA-WM, which renders depth-aware arm structures, joint landmarks, gripper geometry, end-effector heatmaps, and pose cues as temporally aligned visual fields, and various video-action models that employ partial denoising strategies to improve efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c4751a5-d1a7-4a85-ba81-9b2ce2eb7b84",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "3121cf91-aa37-416a-8a14-43678d9b2089",
  "sourceToolAssistantUUID": "4c4751a5-d1a7-4a85-ba81-9b2ce2eb7b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T09:02:43.400Z_

Excellent! Let me do one final search to check for any other high-overlap papers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3121cf91-aa37-416a-8a14-43678d9b2089",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011CatcnW621YsUQzVMcRjEH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad8ef2de-c9db-47d5-8c1f-cdcd1cfe278b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ga3CS6tN4tTsdsfqqJtFQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1951,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 23419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 28 · 2026-05-10T09:02:43.824Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01URGfs978uy7g7mbDu9X4xY`</summary>

```json
{
  "query": "\"adaptive diffusion\" \"per-step\" OR \"per-action\" robot 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad8ef2de-c9db-47d5-8c1f-cdcd1cfe278b",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011CatcnW621YsUQzVMcRjEH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "96b53901-bf9f-4531-91f9-1a6d5f4941e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ga3CS6tN4tTsdsfqqJtFQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1951,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 23419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 29 · 2026-05-10T09:02:43.964Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PH2eDxeJLEkj1cpPzVVQXT`</summary>

```json
{
  "query": "video denoising steps prediction robot manipulation learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96b53901-bf9f-4531-91f9-1a6d5f4941e3",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011CatcnW621YsUQzVMcRjEH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04213e2b-d0d1-4df3-b331-bd6b2f3c9fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ga3CS6tN4tTsdsfqqJtFQT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1951,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 23419,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1951,
          "output_tokens": 143,
          "cache_read_input_tokens": 23419,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1129,
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

_source line 30 · 2026-05-10T09:02:51.064Z_

<details><summary>↩ Tool result · `toolu_01URGfs978uy7g7mbDu9X4xY`</summary>

```text
Web search results for query: ""adaptive diffusion" "per-step" OR "per-action" robot 2025 2026 arxiv"

Links: [{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"Abstracting Robot Manipulation Skills via Mixture-of- ...","url":"https://arxiv.org/pdf/2601.21251"},{"title":"[2510.01068v1] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/abs/2510.01068v1"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://arxiv.org/pdf/2303.04137"}]

I've performed a web search for your query about adaptive diffusion with per-step or per-action approaches in robotics from 2025-2026 on arXiv. Here are the key findings:

The search results show several relevant recent papers on diffusion models for robot manipulation:

1. **Survey on Diffusion Models for Robotic Manipulation (2025)**: A comprehensive review of state-of-the-art diffusion models in robotic manipulation, including grasp learning, trajectory planning, and data augmentation.

2. **Recent Composition and Adaptation Methods**: General Policy Composition (GPC) is a training-free method that enhances performance by combining the distributional scores of multiple pre-trained policies via a convex combination and test-time search, allowing for the plug-and-play composition of heterogeneous policies, including VA and VLA models, as well as those based on diffusion or flow-matching.

3. **MotuBrain World Action Model**: A recent paper describes an advanced system with post-training pipeline, including sparse adaptation and step distillation, which relates to per-step optimization approaches.

4. **Mixture-of-Experts Diffusion Policy**: An adaptive expert activation strategy that dynamically selects a compact subset of experts at inference time, reducing computational cost while maintaining action sampling accuracy.

The search results don't show a specific paper with the exact phrase "adaptive diffusion per-step" or "per-action" in the title, but these recent papers from 2025-2026 demonstrate active research in adaptive and efficient diffusion-based approaches for robot control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96b53901-bf9f-4531-91f9-1a6d5f4941e3",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "8ff1b9a6-c75e-4485-9ec2-09f898a7d9c5",
  "sourceToolAssistantUUID": "96b53901-bf9f-4531-91f9-1a6d5f4941e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T09:02:51.858Z_

<details><summary>↩ Tool result · `toolu_01PH2eDxeJLEkj1cpPzVVQXT`</summary>

```text
Web search results for query: "video denoising steps prediction robot manipulation learning 2026"

Links: [{"title":"Diffusion Policy: Teaching Robots to Act by Denoising","url":"https://vizuara.substack.com/p/diffusion-policy-teaching-robots"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Large-Scale Actionless Video Pre-Training via Discrete Diffusion for Efficient Policy Learning","url":"https://arxiv.org/html/2402.14407v1"},{"title":"Video Generators are Robot Policies - Columbia University","url":"https://videopolicy.cs.columbia.edu/assets/video_policy.pdf"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"},{"title":"VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation","url":"https://arxiv.org/html/2411.09153v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Request PDF","url":"https://www.researchgate.net/publication/395371959_Unified_World_Models_Coupling_Video_and_Action_Diffusion_for_Pretraining_on_Large_Robotic_Datasets"},{"title":"Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations","url":"https://arxiv.org/html/2412.14803v1"},{"title":"Combining next-token prediction and video diffusion in computer vision and robotics | MIT CSAIL","url":"https://www.csail.mit.edu/news/combining-next-token-prediction-and-video-diffusion-computer-vision-and-robotics"}]

I've searched for information on video denoising steps, prediction, robot manipulation learning, and recent 2026 research. Here are the key findings:

## Video Denoising in Robot Learning

Robot policies are now represented as conditional denoising diffusion processes that sample from the full action distribution by iteratively denoising random noise, conditioned on observations. The diffusion model predicts future action steps all at once across a prediction horizon.

## Denoising Architecture and Process

Instead of estimating the score function directly, a noise prediction network conditioned on the noise scale is trained, with new points generated by sampling Gaussian noise and iteratively denoising the samples using the learned network. MLPs are employed as denoising networks that take concatenated input features, such as observations, actions, and denoising time steps, to predict the noise.

## Recent 2026 Advances

Recent unified frameworks like VAG use flow-matching-based dual-stream approaches that jointly generate video and action under visual and language conditioning, synchronizing denoising in both branches. Recent research has shown that features of a generative model after a single denoising step already contain sufficient motion features to guide the action head's planning.

## Video Prediction for Manipulation

Both video prediction and action learning are formulated as denoising problems within a unified discrete diffusion process. Video diffusion models demonstrate the capability to accurately predict future image sequences and possess visual representations that reflect the evolution of the physical world.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04213e2b-d0d1-4df3-b331-bd6b2f3c9fe4",
  "isSidechain": true,
  "promptId": "8113a2cb-b2d2-40e7-83cb-9f599c120205",
  "agentId": "a1b7541f794021425",
  "type": "user",
  "uuid": "e5c0a4cb-739d-4a78-99d6-d9d96d489fa4",
  "sourceToolAssistantUUID": "04213e2b-d0d1-4df3-b331-bd6b2f3c9fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-10T09:03:04.335Z_

Based on my comprehensive search across multiple queries, I've identified several papers that have significant overlap with the Commitment Depth Routing (CDR) contribution. Here are the key findings:

## Papers with Significant Overlap to CDR

### 1. **D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning**
- **arXiv ID**: 2508.06804 (submitted August 9, 2025)
- **Core Contribution**: Adaptively allocates denoising steps across different actions at test time using a lightweight, state-aware adaptor that predicts the optimal number of denoising steps per action
- **Key Overlap with CDR**: This is the closest match - it learns per-action denoising depth based on observation/state, achieving 2.2× inference speed-up
- **URL**: https://arxiv.org/abs/2508.06804

### 2. **VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation**
- **arXiv ID**: 2604.15938 (submitted April 17, 2026)
- **Core Contribution**: A dual-adaptive framework with Adaptive Loss Network (ALN) for training and Hierarchical Vision Task Segmenter (HVTS) for inference. During inference, dynamically schedules denoising budgets per stage based on visual complexity using a vision-language model
- **Key Overlap with CDR**: Uses vision-adaptive stage-wise dynamic scheduling of denoising steps, though focuses on task decomposition stages rather than per-observation routing
- **URL**: https://arxiv.org/abs/2604.15938

### 3. **X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising**
- **arXiv ID**: 2604.26694 (April 2026)
- **Core Contribution**: Proposes Asynchronous Noise Sampling (ANS) which applies differential denoising schedules - actions are decoded with fewer steps from noisy latents while full denoising is reserved for high-fidelity video generation
- **Key Overlap with CDR**: Uses selective/asynchronous denoising based on task requirements (action vs video), addressing the insight that actions don't require full video denoising quality
- **URL**: https://arxiv.org/html/2604.26694v2

### 4. **Fast-WAM: Do World Action Models Need Test-time Future Imagination?**
- **arXiv ID**: 2603.16666 (March 2026)
- **Core Contribution**: Removes explicit video denoising at test-time entirely, directly generating actions without iterative video denoising while keeping clean latent tokens
- **Key Overlap with CDR**: Addresses the same core insight that not all observations need full video denoising for effective action prediction; extreme case of selective activation
- **URL**: https://arxiv.org/abs/2603.16666

### 5. **ADPro: Test-time Adaptive Diffusion Policy**
- **arXiv ID**: 2508.06266 (August 2025)
- **Core Contribution**: Test-time adaptive diffusion policy via manifold-constrained denoising and task-aware initialization
- **Key Overlap with CDR**: Related approach to adaptive denoising but focuses on constraint injection rather than depth routing
- **URL**: https://arxiv.org/abs/2508.06266

### 6. **Unified World Models: Coupling Video and Action Diffusion for Pretraining**
- **arXiv ID**: 2504.02792 (April 2025)
- **Core Contribution**: Uses independent diffusion timesteps for each modality (video and action), implicitly allowing different denoising depths
- **Key Overlap with CDR**: Related concept of modality-specific denoising control though not observation-dependent
- **URL**: https://arxiv.org/html/2504.02792v1

## Summary

The **most directly overlapping works** are:
1. **D3P** (2508.06804) - Nearly identical core contribution (per-action adaptive denoising)
2. **VADF** (2604.15938) - Stage-wise adaptive scheduling with vision-driven depth control
3. **X-WAM** (2604.26694) - Asynchronous denoising based on task requirements (actions vs video)
4. **Fast-WAM** (2603.16666) - Extreme case eliminating video denoising for action prediction

These papers collectively demonstrate that the concept of adapting denoising depth based on observation/task context is an active research direction in 2025-2026, with D3P and VADF being particularly close precedents to CDR's contribution.

Sources:
- [D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning](https://arxiv.org/abs/2508.06804)
- [VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation](https://arxiv.org/abs/2604.15938)
- [X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694)
- [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666)
- [ADPro: Test-time Adaptive Diffusion Policy](https://arxiv.org/abs/2508.06266)
- [Unified World Models: Coupling Video and Action Diffusion](https://arxiv.org/abs/2504.02792)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5c0a4cb-739d-4a78-99d6-d9d96d489fa4",
  "isSidechain": true,
  "agentId": "a1b7541f794021425",
  "requestId": "req_011CatcoHevyLnJYRt9WXj5v",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b27fc5ca-e8a0-44f3-8d20-2573763e40ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7c1f2b8c-c5eb-4c63-a9ff-39ff4e3aed0b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019LjDfGAVo7yHyzCa6c53gs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 24548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3920,
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
