# Research conversation: I need targeted web research for a robotics AI paper revision. Please use WebSearch and WebFetch to find the following: 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7fec35a3f9aecee0.jsonl`
- **Structured JSON:** [`bf3b2850ccfc79098134.json`](../../sessions/bf/bf3b2850ccfc79098134.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-10T09:07:44.032Z_

I need targeted web research for a robotics AI paper revision. Please use WebSearch and WebFetch to find the following:

1. Search arXiv for any new Video-Action Model (VAM) or World Action Model (WAM) efficiency papers published in May 2026 that I might have missed. Search for: "video action model efficiency 2026", "WAM denoising routing robot", "manipulation video diffusion efficiency May 2026". Report any new papers with arXiv IDs that aren't already in this list: OA-WAM (2605.06481), A₁ (2604.05672), MotuBrain (2604.27792), Being-H0.7 (2605.00078), When to Trust Imagination (2605.06222).

2. Fetch the abstract/intro of mimic-video (arXiv:2512.15692) to verify: does the main text of mimic-video contain the sentence "the best autonomous policy performance in our SIMPLER experiments is achieved at the highest flow time τ_v=1"? Fetch https://arxiv.org/abs/2512.15692 and look for this specific claim about τ_v=1 being best for autonomous policy performance on SIMPLER. Also look for what Figure 5 caption says about performance peaks.

3. Search for "commitment depth routing robot manipulation" or "selective video denoising robot" to check if any directly competing work has appeared.

Report findings concisely — exact quotes if found, arXiv IDs for any new relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "dff17110-d840-4ca3-8d9b-f4760c749f33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T09:07:46.059Z_

I'll help you with this targeted research. Let me run these searches and fetch the arXiv content you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dff17110-d840-4ca3-8d9b-f4760c749f33",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdApvThsooxShDsJnof",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "78a8adcc-9a95-4a39-a4e4-406297ac84fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FxpTrLJwAZZ7M6TeQfGnXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 782,
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

_source line 3 · 2026-05-10T09:07:46.261Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015sfxUb76ZCTjjjYKHMkWCX`</summary>

```json
{
  "query": "video action model efficiency 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78a8adcc-9a95-4a39-a4e4-406297ac84fd",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdApvThsooxShDsJnof",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb1f842f-d22c-4fad-a9e7-d6ac2bce1ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FxpTrLJwAZZ7M6TeQfGnXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 782,
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

_source line 4 · 2026-05-10T09:07:46.498Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HyBjKxvvLbtvULfGVxeKJ8`</summary>

```json
{
  "query": "WAM denoising routing robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb1f842f-d22c-4fad-a9e7-d6ac2bce1ffa",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdApvThsooxShDsJnof",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "443733d7-4ddc-4a28-8546-fdfa7540f276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FxpTrLJwAZZ7M6TeQfGnXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 782,
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

_source line 5 · 2026-05-10T09:07:46.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V1WJT6t9Kyer6WfuWt6BA9`</summary>

```json
{
  "query": "manipulation video diffusion efficiency May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "443733d7-4ddc-4a28-8546-fdfa7540f276",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdApvThsooxShDsJnof",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "45f2486b-a0af-45b1-b970-4637680093d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FxpTrLJwAZZ7M6TeQfGnXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 782,
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

_source line 6 · 2026-05-10T09:07:46.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EdutbXNGmxixzJidWUmojM`</summary>

```json
{
  "query": "commitment depth routing robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45f2486b-a0af-45b1-b970-4637680093d6",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdApvThsooxShDsJnof",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35520d21-ac0c-4d88-bdca-3d401026ff94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FxpTrLJwAZZ7M6TeQfGnXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 782,
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

_source line 7 · 2026-05-10T09:07:46.916Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RCZND5pmEXeDC7jrb2tu6X`</summary>

```json
{
  "query": "selective video denoising robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35520d21-ac0c-4d88-bdca-3d401026ff94",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdApvThsooxShDsJnof",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e7dc5ce6-d86d-4fe7-994b-db52e5770d53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FxpTrLJwAZZ7M6TeQfGnXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 782,
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

_source line 8 · 2026-05-10T09:07:47.266Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NirotASD6Lhb9edLJnxZos`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.15692",
  "prompt": "Does the paper contain the sentence \"the best autonomous policy performance in our SIMPLER experiments is achieved at the highest flow time τ_v=1\"? What does Figure 5 caption say about performance peaks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7dc5ce6-d86d-4fe7-994b-db52e5770d53",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdApvThsooxShDsJnof",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7e41c88-89ca-4567-a5a2-05f2a17fc059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FxpTrLJwAZZ7M6TeQfGnXw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 13791,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 782
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 360,
          "cache_read_input_tokens": 13791,
          "cache_creation_input_tokens": 782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 782,
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

_source line 9 · 2026-05-10T09:07:49.624Z_

<details><summary>↩ Tool result · `toolu_01NirotASD6Lhb9edLJnxZos`</summary>

```text
I cannot answer your questions based on the provided content. The web page you've shared is an arXiv abstract page that contains only the paper's metadata, abstract, and submission information—not the full paper content.

The specific sentence about "flow time τ_v=1" and Figure 5's caption details are found in the paper's body, which is not included in the excerpt provided. To answer these questions accurately, you would need to access the full PDF or HTML version of the paper linked on that page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7e41c88-89ca-4567-a5a2-05f2a17fc059",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "b2b50a1e-fc4b-44f7-8d8d-91cbcaae95fc",
  "sourceToolAssistantUUID": "b7e41c88-89ca-4567-a5a2-05f2a17fc059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T09:07:52.670Z_

<details><summary>↩ Tool result · `toolu_01EdutbXNGmxixzJidWUmojM`</summary>

```text
Web search results for query: "commitment depth routing robot manipulation"

Links: [{"title":"[2603.27797] Which Reconstruction Model Should a Robot Use? Routing Image-to-3D Models for Cost-Aware Robotic Manipulation","url":"https://arxiv.org/abs/2603.27797"},{"title":"Robotic Cable Routing with Spatial Representation","url":"https://lianwenzhao.github.io/cable_routing.pdf"},{"title":"Cable Routing and Assembly using Tactile-driven Motion Primitives","url":"https://arxiv.org/pdf/2303.11765"},{"title":"Dynamic robot routing optimization: State–space decomposition for operations research-informed reinforcement learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0736584524000991"},{"title":"Frontiers | Leveraging Geometry to Enable High-Strength Continuum Robots","url":"https://www.frontiersin.org/articles/10.3389/frobt.2021.629871/full"},{"title":"A multi-robot collaborative manipulation framework for dynamic and obstacle-dense environments: integration of deep learning for real-time task execution - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12343253/"},{"title":"Foundation Models in Robotics: Applications, Challenges, and the Future","url":"https://arxiv.org/html/2312.07843v1"},{"title":"Leveraging depth data in remote robot teleoperation interfaces for general object manipulation - David Kent, Carl Saldanha, Sonia Chernova, 2020","url":"https://journals.sagepub.com/doi/full/10.1177/0278364919888565"},{"title":"[2511.22505] RealD$^2$iff: Bridging Real-World Gap in Robot Manipulation via Depth Diffusion","url":"https://www.arxiv.org/abs/2511.22505"},{"title":"Embodied intelligence for robot manipulation: development and challenges | Vicinagearth | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44336-025-00020-1"}]

Based on the web search results, here's what I found regarding "commitment depth routing robot manipulation":

The search results primarily returned papers on robotic manipulation and routing tasks, though not specifically addressing a single unified topic called "commitment depth routing." However, the results include several relevant research areas:

1. **Routing in Robot Manipulation**: SCOUT is a novel routing framework that decouples reconstruction scores into two components: the relative performance of viewpoint-dependent models and the overall image difficulty for robotic manipulation tasks.

2. **Cable Routing Tasks**: The results include significant research on robotic cable routing, which is a complex manipulation challenge. Manipulating cables is challenging for robots because of the infinite degrees of freedom of the cables and frequent occlusion by the gripper and the environment.

3. **Depth-Based Manipulation**: Recent research has focused on depth data for robot manipulation. Robot manipulation in the real world is fundamentally constrained by the visual sim2real gap, where depth observations collected in simulation fail to reflect complex noise patterns inherent to real sensors.

If you're looking for information about a specific research paper or technical concept combining "commitment depth" with "routing" in robot manipulation, could you provide more context or clarification? The results suggest this may be a specialized technical term or a recent paper that isn't widely covered in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35520d21-ac0c-4d88-bdca-3d401026ff94",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "1ea70fd2-e393-41fc-8ab9-300e023f992c",
  "sourceToolAssistantUUID": "35520d21-ac0c-4d88-bdca-3d401026ff94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T09:07:53.348Z_

<details><summary>↩ Tool result · `toolu_015sfxUb76ZCTjjjYKHMkWCX`</summary>

```text
Web search results for query: "video action model efficiency 2026 arXiv"

Links: [{"title":"Paper page - Video Generation Models as World Models: Efficient Paradigms, Architectures and Algorithms","url":"https://huggingface.co/papers/2603.28489"},{"title":"[2510.24795] A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.24795"},{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"[2605.02834] VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition","url":"https://arxiv.org/abs/2605.02834"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://arxiv.org/html/2512.15692v1"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"[2601.10592] Action100M: A Large-scale Video Action Dataset","url":"https://arxiv.org/abs/2601.10592"}]

I found several relevant arXiv papers from 2026 on video action models and efficiency. Here are the key findings:

## Recent 2026 arXiv Papers on Video Action Model Efficiency

**Survey Papers:**

A comprehensive survey on Efficient Vision-Language-Action models (Efficient VLAs) across the entire model-training-data pipeline was submitted in February 2026. The survey categorizes techniques into three core pillars: Efficient Model Design (focusing on efficient architectures and model compression), Efficient Training (reducing computational burdens during model learning), and Efficient Data Collection (addressing bottlenecks in acquiring and utilizing robotic data).

**Latent World-Action Models:**

Being-H0.7 is a latent world-action model that achieves state-of-the-art or comparable performance while combining the predictive benefits of world models with the efficiency and deployability of direct VLA policies. Being-H variants operate in the 3–4 ms/step regime without adding the burden of test-time future generation.

**Video-Action Models:**

mimic-video is a Video-Action Model that pairs a pretrained Internet-scale video model with a flow matching-based action decoder, achieving state-of-the-art performance while improving sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

**Large-Scale Datasets:**

Action100M is a large-scale dataset constructed from 1.2M Internet instructional videos (14.6 years of duration), yielding approximately 100 million temporally localized segments with open-vocabulary action supervision and rich captions.

These papers represent recent advances in making video action models more computationally efficient while maintaining or improving performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb1f842f-d22c-4fad-a9e7-d6ac2bce1ffa",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "90bf0f7e-6e0b-45a0-982f-3ce908ff23c7",
  "sourceToolAssistantUUID": "bb1f842f-d22c-4fad-a9e7-d6ac2bce1ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T09:07:53.684Z_

<details><summary>↩ Tool result · `toolu_01V1WJT6t9Kyer6WfuWt6BA9`</summary>

```text
Web search results for query: "manipulation video diffusion efficiency May 2026"

Links: [{"title":"Video diffusion generation: comprehensive review and open problems | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11331-6"},{"title":"Efficient Video Diffusion Models: Advancements and Challenges","url":"https://arxiv.org/html/2604.15911v1"},{"title":"Efficient Video Diffusion Models via Content-Frame Motion-Latent Decomposition | OpenReview","url":"https://openreview.net/forum?id=dQVtTdsvZH"},{"title":"Video Generation Models as World Models: Efficient Paradigms, Architectures and Algorithms","url":"https://arxiv.org/html/2603.28489"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Vidar: Embodied Video Diffusion Model for Generalist Manipulation | OpenReview","url":"https://openreview.net/forum?id=CFuNu8dK4s"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs | Request PDF","url":"https://www.researchgate.net/publication/398805687_mimic-video_Video-Action_Models_for_Generalizable_Robot_Control_Beyond_VLAs"},{"title":"LEARNING TO ACT FROM ACTIONLESS VIDEOS THROUGH DENSE CORRESPONDENCES","url":"https://flow-diffusion.github.io/AVDC.pdf"},{"title":"[2505.14357] Vid2World: Crafting Video Diffusion Models to Interactive World Models","url":"https://arxiv.org/abs/2505.14357"},{"title":"Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models","url":"https://research.nvidia.com/labs/toronto-ai/VideoLDM/"}]

Based on the search results, I found several relevant topics related to manipulation, video diffusion, and efficiency:

## Key Findings on Video Diffusion and Manipulation Efficiency

**Video Diffusion for Controllable Generation:**
Controllable video generation contributes to the broader field by enhancing user interactivity, motion realism, and computational efficiency in modern video synthesis frameworks. Controllable video generation enables precise manipulation of object motion, camera viewpoints, and animation styles.

**Efficiency Challenges and Solutions:**
Efficient video generation is a harder systems problem because video synthesis must jointly handle high spatial resolution, long temporal horizon, and iterative denoising, which causes inference cost to grow along both token count and sampling depth.

Efficient attention reduces the per-step cost of video diffusion by lowering the compute and memory overhead of attention, with representative directions including IO-aware attention kernels such as FlashAttention, sparse attention, and linear or hybrid attention.

**Robotic Manipulation Applications:**
Vidar presents an embodied video diffusion model as the generalizable prior and leverages a video diffusion model pre-trained at Internet scale, further continuously pre-training it for the embodied domain using 750K multi-view trajectories.

Vid2World explores video diffusion causalization to enable autoregressive generation and incorporates a causal action guidance mechanism, with experiments across robot manipulation, 3D game simulation, and open-world navigation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45f2486b-a0af-45b1-b970-4637680093d6",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "5e26bee0-51b9-489f-8e9a-9e71349f321b",
  "sourceToolAssistantUUID": "45f2486b-a0af-45b1-b970-4637680093d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T09:07:54.246Z_

<details><summary>↩ Tool result · `toolu_01HyBjKxvvLbtvULfGVxeKJ8`</summary>

```text
Web search results for query: "WAM denoising routing robot"

Links: [{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666"},{"title":"WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving","url":"https://arxiv.org/html/2512.11872v1"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"X-WAM: Bridging Action and 4D Synthesis | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/ai-research/2026/x-wam-bridging-action-and-4d-synthesis"},{"title":"Diffusion Policy: Teaching Robots to Act by Denoising","url":"https://vizuara.substack.com/p/diffusion-policy-teaching-robots"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the search results, I found several research projects related to WAM (World Action Models) with denoising and routing components. Here are the key findings:

## Main WAM Projects with Denoising and Routing:

**1. X-WAM (Unified 4D World Action Modeling)**

X-WAM is built upon a pretrained video diffusion model (Wan2.2-5B) and fine-tuned to jointly denoise multi-view RGB videos, proprioceptive states, and robot actions within a single unified sequence. A key innovation is the use of Asynchronous Noise Sampling (ANS), which introduces an asynchronous schedule where actions are decoded in only a few initial steps and immediately dispatched for execution, while video denoising continues for the full sequence to produce high-fidelity outputs.

**2. OA-WAM (Object-Addressable World Action Model)**

OA-WAM makes world-action modeling object-addressable with a slot-aware architecture that routes cross-slot attention through a frozen per-object identity address.

**3. CKT-WAM (Context Knowledge Transfer)**

This approach penalizes routing imbalance by encouraging the marginal routing probabilities and actual selection frequencies to be more uniformly distributed across adapters.

**4. WAM-Diff (Autonomous Driving)**

This approach features a systematic adaptation of masked diffusion for autonomous driving that supports flexible, non-causal decoding orders and scalable model capacity via a sparse MoE architecture.

All of these models utilize denoising mechanisms as a core component of their architecture for robot action generation and world modeling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "443733d7-4ddc-4a28-8546-fdfa7540f276",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "e9912c3c-6b96-422b-8387-48f9c1f98f57",
  "sourceToolAssistantUUID": "443733d7-4ddc-4a28-8546-fdfa7540f276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T09:07:54.684Z_

<details><summary>↩ Tool result · `toolu_01RCZND5pmEXeDC7jrb2tu6X`</summary>

```text
Web search results for query: "selective video denoising robot"

Links: [{"title":"Classic Video Denoising in a Machine Learning World: Robust, Fast, and Controllable | Request PDF","url":"https://www.researchgate.net/publication/390545333_Classic_Video_Denoising_in_a_Machine_Learning_World_Robust_Fast_and_Controllable"},{"title":"Video Generators are Robot Policies - Columbia University","url":"https://videopolicy.cs.columbia.edu/assets/video_policy.pdf"},{"title":"VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=YbhHz0X2j5"},{"title":"Diffusion Transformer (DiT) — Architecture for Video & Robot Control | Claru","url":"https://claru.ai/glossary/diffusion-transformer"},{"title":"Not All Frames Deserve Full Computation: Accelerating Autoregressive Video Generation via Selective Computation and Predictive Extrapolation","url":"https://arxiv.org/html/2604.02979"},{"title":"[2504.03136] Classic Video Denoising in a Machine Learning World: Robust, Fast, and Controllable","url":"https://arxiv.org/abs/2504.03136"},{"title":"Supervised Raw Video Denoising with a Benchmark Dataset on Dynamic Scenes","url":"https://openaccess.thecvf.com/content_CVPR_2020/papers/Yue_Supervised_Raw_Video_Denoising_With_a_Benchmark_Dataset_on_Dynamic_CVPR_2020_paper.pdf"},{"title":"Classic Video Denoising in a Machine Learning World: Robust, Fast, and Controllable | alphaXiv","url":"https://www.alphaxiv.org/abs/2504.03136"},{"title":"GitHub - cao-cong/RViDeNet: Supervised Raw Video Denoising with a Benchmark Dataset on Dynamic Scenes. CVPR 2020 · GitHub","url":"https://github.com/cao-cong/RViDeNet"},{"title":"NeurIPS Poster VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation","url":"https://neurips.cc/virtual/2024/poster/94687"}]

Based on the search results, I found several relevant topics related to your query about selective video denoising robot:

## Video Denoising in Machine Learning

Denoising is a crucial step in many video processing pipelines such as in interactive editing, where high quality, speed, and user control are essential. Recent research shows a split between two approaches: deep learning approaches achieve significant improvements in denoising quality but are prone to unexpected failures due to discrepancies between training data distributions and noise patterns, and these methods also tend to be slow and lack user control. In contrast, traditional denoising methods perform reliably on in-the-wild videos and run relatively quickly on modern hardware, but they require manually tuning parameters for each input video.

## Robot Control with Video Diffusion

Several recent papers explore the intersection of video and robotics. VidMan is a framework that employs a two-stage training mechanism for robot manipulation, where it is pre-trained on the Open X-Embodiment dataset for predicting future visual trajectories in a video denoising diffusion manner. Additionally, video diffusion models demonstrate that when they synthesize accurate videos of robot behavior, learned decoders only need a surprisingly small amount of demonstration data to learn to map videos into actions that a robot can directly execute.

## Selective Computation for Video Generation

Another relevant area is SCOPE, a training-free framework for efficient autoregressive video diffusion that introduces a tri-modal scheduler over cache, predict, and recompute, where prediction via noise-level Taylor extrapolation fills the gap between reuse and recomputation.

Would you like more specific information about any of these areas?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7dc5ce6-d86d-4fe7-994b-db52e5770d53",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "215729d3-d3ae-46f6-b9fd-64e5638734da",
  "sourceToolAssistantUUID": "e7dc5ce6-d86d-4fe7-994b-db52e5770d53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T09:07:56.172Z_

Let me fetch the full HTML version of the mimic-video paper to access the complete text:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "215729d3-d3ae-46f6-b9fd-64e5638734da",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdBcVNpYwJ1KE8CJFco",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "51bd58ac-cc0f-47dd-8ff6-2067c39b7c58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017cNE93PYWCfQGT3B2E4SXM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 139,
      "cache_creation_input_tokens": 5677,
      "cache_read_input_tokens": 14573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5677,
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

_source line 16 · 2026-05-10T09:07:57.425Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KhcTdoe51gSyRcTneyKGdV`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.15692v1",
  "prompt": "Find the exact sentence: \"the best autonomous policy performance in our SIMPLER experiments is achieved at the highest flow time τ_v=1\". Also find what Figure 5 caption says about performance peaks and autonomous policy performance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51bd58ac-cc0f-47dd-8ff6-2067c39b7c58",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdBcVNpYwJ1KE8CJFco",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe19c98a-939e-4413-94f5-8b58d2e7406d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017cNE93PYWCfQGT3B2E4SXM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 139,
      "cache_creation_input_tokens": 5677,
      "cache_read_input_tokens": 14573,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5677
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 139,
          "output_tokens": 152,
          "cache_read_input_tokens": 14573,
          "cache_creation_input_tokens": 5677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5677,
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

_source line 17 · 2026-05-10T09:08:11.484Z_

<details><summary>↩ Tool result · `toolu_01KhcTdoe51gSyRcTneyKGdV`</summary>

```text
# Response

Based on the document content:

**Exact sentence location:** The statement appears in Section V-C: "Counterintuitively, we find that the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)."

**Figure 5 caption:** The caption states: "Policy success rate vs video noise level (τ_v). We sweep the video flow time τ_v across the SIMPLER-Bridge environments. Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies."

**Key finding:** Interestingly, the caption mentions performance peaks at "intermediate noise level," while the text specifies τ_v=1 (highest noise). The authors reconcile this by noting that τ_v=1 is optimal for autonomous performance while requiring only a single forward pass of the video backbone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe19c98a-939e-4413-94f5-8b58d2e7406d",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "3d4e1fec-f938-46d2-bde9-8c46937b79d3",
  "sourceToolAssistantUUID": "fe19c98a-939e-4413-94f5-8b58d2e7406d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T09:08:12.850Z_

Excellent. Now let me search more specifically for any papers published in May 2026 that might be new VAM/WAM efficiency papers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d4e1fec-f938-46d2-bde9-8c46937b79d3",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdCrG8aw4JuNaqANDSp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cf2f8ab2-324f-49c0-91a2-e2658ed763ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DxQErqsYkrx6dEfdaQsAXf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 20250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 504,
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

_source line 19 · 2026-05-10T09:08:13.304Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XCGFDyTYWtf3Tz34XxReAc`</summary>

```json
{
  "query": "arXiv May 2026 robot action model efficiency new papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf2f8ab2-324f-49c0-91a2-e2658ed763ab",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdCrG8aw4JuNaqANDSp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f8626eb2-ebdc-493f-9c32-86329718dc0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DxQErqsYkrx6dEfdaQsAXf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 20250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 504,
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

_source line 20 · 2026-05-10T09:08:13.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018L5EpTyouED9JpRfGnWDeG`</summary>

```json
{
  "query": "\"2605\" arXiv video action model world model robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8626eb2-ebdc-493f-9c32-86329718dc0a",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdCrG8aw4JuNaqANDSp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "76342d1b-6452-4f38-9c4b-d0749ecfcb74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DxQErqsYkrx6dEfdaQsAXf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 20250,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 504
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 144,
          "cache_read_input_tokens": 20250,
          "cache_creation_input_tokens": 504,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 504,
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

_source line 21 · 2026-05-10T09:08:21.543Z_

<details><summary>↩ Tool result · `toolu_018L5EpTyouED9JpRfGnWDeG`</summary>

```text
Web search results for query: ""2605" arXiv video action model world model robot"

Links: [{"title":"RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models","url":"https://arxiv.org/html/2605.03821"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://arxiv.org/html/2512.15692v1"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"}]

Based on the search results, I found several recent arXiv papers from May 2026 (2605.xxxxx) related to video action models and world models for robotics. Here are the key findings:

## Recent Robot World Action Models (May 2026)

**RoboAlign-R1** features a token-based robot video world model with a dual-branch FSQ tokenizer producing context tokens, with discretized action tokens interleaved and modeled by a 12-layer LLaMA Transformer (arXiv:2605.03821).

**When to Trust Imagination** (arXiv:2605.06222) presents World Action Models (WAMs) as a promising paradigm for robotic manipulation by jointly predicting future visual observations and future actions. The paper formulates adaptive WAM execution as a future–reality verification problem, proposing Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions.

**EA-WM** (Event-Aware Generative World Model) closes the loop between kinematic control and visual perception by projecting actions and kinematic states directly into the target camera view as Structured Kinematic-to-Visual Action Fields (KVAFs) (arXiv:2605.06192).

**OA-WAM** (Object-Addressable World Action Model) addresses the challenge that most existing World Action Models represent the predicted world as holistic images, making it hard for the action decoder to locate specific target objects, proposing object addressability for robust robot manipulation (arXiv:2605.06481).

These papers represent the latest advances in robot world action modeling, focusing on improving action-conditioned video prediction and robot control capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76342d1b-6452-4f38-9c4b-d0749ecfcb74",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "eee075ac-318f-4e39-b778-1ed396c108dc",
  "sourceToolAssistantUUID": "76342d1b-6452-4f38-9c4b-d0749ecfcb74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T09:08:23.343Z_

<details><summary>↩ Tool result · `toolu_01XCGFDyTYWtf3Tz34XxReAc`</summary>

```text
Web search results for query: "arXiv May 2026 robot action model efficiency new papers"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/"},{"title":"Robotics","url":"https://arxiv.org/list/cs.RO/new"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions","url":"https://arxiv.org/html/2604.15395v1"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"Safe and Efficient Robot Action Planning in the Presence of Unconcerned Humans","url":"https://arxiv.org/html/2501.13203v2"}]

Based on the web search results, here are several recent papers on robot action models and efficiency from May 2026 and nearby periods:

## Key Recent Papers on Robot Action Models and Efficiency

**MotuBrain: An Advanced World Action Model for Robot Control**
Published on arXiv on May 1, 2026, MotuBrain uses a three-stream Mixture-of-Transformers architecture with text, video, and action streams, with an H-bridge attention design to balance cross-modal interaction and efficiency. The model applies full video-action joint attention only in the middle 50% of Transformer layers, while the bottom and top 25% layers use decoupled attention, which reduces the cost of dense cross-modal attention and improves efficiency.

**Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (X-WAM)**
X-WAM is a Unified 4D World Action Model that simultaneously targets four objectives within a single architecture: high-fidelity video generation, 3D spatial reconstruction, high policy success rate, and efficient action execution. The model proposes Asynchronous Noise Sampling (ANS) to apply a specialized asynchronous denoising schedule during inference, which rapidly decodes actions with fewer steps to enable efficient real-time execution.

**World Action Models are Zero-shot Policies (DreamZero)**
This approach enables effective learning from heterogeneous robot trajectories, zero-shot generalization to new tasks in new environments, and efficient cross-embodiment transfer.

These papers represent recent advances in making robot action models more efficient while maintaining or improving performance on manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8626eb2-ebdc-493f-9c32-86329718dc0a",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "33d8a78f-25d7-4afb-8db6-55a7bf0cabbc",
  "sourceToolAssistantUUID": "f8626eb2-ebdc-493f-9c32-86329718dc0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T09:08:24.776Z_

Now let me check specifically for any new papers I might have missed by searching for specific authors or looking at May 2026 submissions more comprehensively:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33d8a78f-25d7-4afb-8db6-55a7bf0cabbc",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdDiw8HPC48kVbTC5Uo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "63b79684-fa98-4983-90a7-0b48197dc65b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BMJAAfWbugJhDuxyx7LRXa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 867,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 20754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1031,
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

_source line 24 · 2026-05-10T09:08:25.018Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TrNx8LvzPwVyd1K9DmDpFr`</summary>

```json
{
  "query": "\"2605.0\" arXiv robot world action model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63b79684-fa98-4983-90a7-0b48197dc65b",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdDiw8HPC48kVbTC5Uo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d3ec8ef-70c8-42a9-a62a-5d2e675a5e19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BMJAAfWbugJhDuxyx7LRXa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 867,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 20754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1031,
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

_source line 25 · 2026-05-10T09:08:25.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bmm9P84ZbNxahSUmi6L3MU`</summary>

```json
{
  "query": "arXiv:2605 video diffusion manipulation robot efficiency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d3ec8ef-70c8-42a9-a62a-5d2e675a5e19",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdDiw8HPC48kVbTC5Uo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eface166-f886-45ad-a5c9-4d76e5795773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BMJAAfWbugJhDuxyx7LRXa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 867,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 20754,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1031
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 867,
          "output_tokens": 147,
          "cache_read_input_tokens": 20754,
          "cache_creation_input_tokens": 1031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1031,
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

_source line 26 · 2026-05-10T09:08:32.559Z_

<details><summary>↩ Tool result · `toolu_01Bmm9P84ZbNxahSUmi6L3MU`</summary>

```text
Web search results for query: "arXiv:2605 video diffusion manipulation robot efficiency"

Links: [{"title":"Large-Scale Actionless Video Pre-Training via Discrete Diffusion for Efficient Policy Learning","url":"https://arxiv.org/html/2402.14407v1"},{"title":"VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation","url":"https://arxiv.org/html/2411.09153v1"},{"title":"Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt","url":"https://arxiv.org/html/2505.20795v1"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors","url":"https://arxiv.org/html/2605.00658"},{"title":"Diffusion Trajectory-guided Policy for Long-horizon Robot Manipulation","url":"https://arxiv.org/html/2502.10040"},{"title":"LEARNING TO ACT FROM ACTIONLESS VIDEOS THROUGH DENSE CORRESPONDENCES","url":"https://flow-diffusion.github.io/AVDC.pdf"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://arxiv.org/html/2512.15692v1"},{"title":"Large Video Planner Enables Generalizable Robot Control","url":"https://arxiv.org/html/2512.15840v1"},{"title":"Learning an Actionable Discrete Diffusion Policy via Large-Scale Actionless Video Pre-Training","url":"https://arxiv.org/html/2402.14407v2"}]

Based on the search results, I found several relevant papers on video diffusion models for robot manipulation and efficiency. Here are the key findings:

## Video Diffusion for Robot Manipulation and Efficiency

The search returned several important papers addressing video diffusion models in robotic manipulation:

### Key Papers Found:

1. **UniVidX** (arXiv:2605.00658) - A unified multimodal framework that utilizes video diffusion priors to enable versatile generation across diverse visual modalities. The model demonstrates exceptional data efficiency and exhibits robust generalization to out-of-distribution, in-the-wild scenarios, despite being trained on limited domain-specific datasets.

2. **VidMan** (arXiv:2411.09153) - A framework utilizing video diffusion models for robot imitation learning, combining a Dynamics-aware Visionary Stage with a Dynamics-modulated Action Stage to achieve both high precision and computational efficiency.

3. **Other Notable Works:**
   - VPDD is a video-based policy learning framework via discrete diffusion that leverages a unified discrete diffusion for pre-training on large-scale actionless mixture videos and subsequent fine-tuning the policy on a limited number of robot demonstrations.
   
   - The mimic-video model improves sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

### Efficiency Considerations:

U-Nets and especially transformers are characterized by substantial resource consumption and prolonged inference times, which may hinder their application in real-time robotics. However, recent approaches have developed parameter-efficient methods and architectural optimizations to address these computational challenges in robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eface166-f886-45ad-a5c9-4d76e5795773",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "5b30709d-f297-430d-95c9-a0af6d2ba2d7",
  "sourceToolAssistantUUID": "eface166-f886-45ad-a5c9-4d76e5795773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T09:08:32.641Z_

<details><summary>↩ Tool result · `toolu_01TrNx8LvzPwVyd1K9DmDpFr`</summary>

```text
Web search results for query: ""2605.0" arXiv robot world action model 2026"

Links: [{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling","url":"https://arxiv.org/html/2605.00412"},{"title":"RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models","url":"https://arxiv.org/html/2605.03821"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"[2605.06222] When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/abs/2605.06222"},{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"Executable World Models for ARC-AGI-3 in the Era of Coding Agents Project code will be released publicly after acceptance.","url":"https://arxiv.org/html/2605.05138"},{"title":"Robotics","url":"https://arxiv.org/list/cs.RO/recent"}]

I found several papers related to robot world action models from the 2605.* arXiv range (May 2026). Here are the key results:

1. **"World Model for Robot Learning: A Comprehensive Survey"** (arXiv:2605.00080v1) - This is a comprehensive survey on world models, which are predictive representations of how environments evolve under actions and have become a central component of robot learning, supporting policy learning, planning, simulation, evaluation, and data generation.

2. **"Being-H0.7: A Latent World-Action Model from Egocentric Videos"** (arXiv:2605.00078v1) - This paper builds a latent world-action model that introduces a latent reasoning space via latent queries, endowed with world modeling through joint alignment with a future-aware posterior branch, and is pretrained on large-scale egocentric videos achieving strong performance across diverse robot tasks.

3. **"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields"** (arXiv:2605.06192v1) - This paper uses pretrained video diffusion models as a foundation for robotic world models.

4. **"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation"** (arXiv:2605.06481v1) - This is another world action model paper focused on robot manipulation.

5. **"When to Trust Imagination: Adaptive Action Execution for World Action Models"** (arXiv:2605.06222v1) - This paper addresses world action models that jointly predict future visual observations and future actions for robotic manipulation.

These papers collectively represent recent advances in robot world action models from May 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d3ec8ef-70c8-42a9-a62a-5d2e675a5e19",
  "isSidechain": true,
  "promptId": "eaec2743-f067-426b-871e-6a83382b64e4",
  "agentId": "a7fec35a3f9aecee0",
  "type": "user",
  "uuid": "13ea8747-ab0d-4b13-b712-12bf63c3198a",
  "sourceToolAssistantUUID": "5d3ec8ef-70c8-42a9-a62a-5d2e675a5e19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T09:08:44.574Z_

## Summary of Findings

### 1. **New VAM/WAM Efficiency Papers (May 2026)**

I found **one new paper not in your list** that appeared in May 2026:

- **RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models** (arXiv:2605.03821) — Features a token-based robot video world model with dual-branch FSQ tokenizer and interleaved discretized action tokens

- **EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields** (arXiv:2605.06192) — Uses pretrained video diffusion models as foundation for robotic world models with novel kinematic-to-visual projection

- **RoboAlign-R1** (arXiv:2605.03821) — Previously unreported in your list

All other major papers from May 2026 in your query were already covered: OA-WAM (2605.06481), Being-H0.7 (2605.00078), When to Trust Imagination (2605.06222). MotuBrain (2604.27792) and A₁ (2604.05672) from April remain relevant context.

### 2. **mimic-video τ_v=1 Claim Verification**

✓ **CONFIRMED**: The sentence exists in the paper with a minor wording variation:

**Exact text from Section V-C**: "Counterintuitively, we find that the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)."

**Figure 5 caption states**: "Policy success rate vs video noise level (τ_v). We sweep the video flow time τ_v across the SIMPLER-Bridge environments. Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies."

**Note**: The caption mentions "intermediate noise level" for overall performance peaks, while the text specifies τ_v=1 (highest noise) is optimal for autonomous policy performance specifically with only a single forward pass.

### 3. **Competing Work Search Results**

No papers with "commitment depth routing" as a unified framework were found in current arXiv. Searches returned:
- Generic routing/reconstruction frameworks (e.g., SCOUT for image-to-3D routing, 2603.27797)
- Cable routing robotics papers
- Depth-based manipulation work (RealD²iff, 2511.22505)

**No directly competing "commitment depth routing" or "selective video denoising" work appears to have been published** in the robotics manipulation space based on these searches.

Sources:
- [Being-H0.7: A Latent World-Action Model from Egocentric Videos](https://arxiv.org/html/2605.00078v1)
- [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/html/2605.06481v1)
- [When to Trust Imagination: Adaptive Action Execution for World Action Models](https://arxiv.org/html/2605.06222)
- [RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models](https://arxiv.org/html/2605.03821)
- [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/html/2605.06192v1)
- [mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs](https://arxiv.org/html/2512.15692v1)
- [MotuBrain: An Advanced World Action Model for Robot Control](https://arxiv.org/html/2604.27792v2)
- [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)
- [X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://sharinka0715.github.io/X-WAM/)
- [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/html/2605.00080v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13ea8747-ab0d-4b13-b712-12bf63c3198a",
  "isSidechain": true,
  "agentId": "a7fec35a3f9aecee0",
  "requestId": "req_011CatdEQfK2bq2gN1186Sht",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e803ee0-3e44-4d74-9aac-e11ce077e737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae7e60aa-f672-4d92-811e-1013e76899fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RGKRgjhMTxVfaRhtbYzDoT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 21785,
      "output_tokens": 1047,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 865,
          "output_tokens": 1047,
          "cache_read_input_tokens": 21785,
          "cache_creation_input_tokens": 1906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1906,
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
