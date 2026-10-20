# Research conversation: Search for the paper "OA-WAM: Object-Addressable World Action Model" (arXiv:2605.06481) and verify: 1. Does it exist on 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae1b3e3f1dbb95588.jsonl`
- **Structured JSON:** [`8e4afeaeeacf9b646231.json`](../../sessions/8e/8e4afeaeeacf9b646231.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-10T09:31:43.602Z_

Search for the paper "OA-WAM: Object-Addressable World Action Model" (arXiv:2605.06481) and verify:
1. Does it exist on arXiv?
2. What is the camera score on LIBERO-Plus (the proposal claims 80.5%)?
3. Is it the current SOTA on camera axis among architecturally-motivated methods without camera augmentation?

Also search for any concurrent work on camera-robust world action models published in April-May 2026 that might compete with a "VQ-Perceiver" approach.

Search queries to use:
- "OA-WAM object addressable world action model 2026"
- "arxiv 2605.06481"
- "LIBERO-Plus camera robustness WAM 2026"
- "camera viewpoint robustness robot policy 2026"

Report what you find about the paper's existence, its claimed scores, and any concurrent camera-robustness work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "0482b71a-df65-487c-85cd-04fcd6a9e33b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T09:31:44.689Z_

I'll search for information about this paper and related concurrent work using the search queries you provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0482b71a-df65-487c-85cd-04fcd6a9e33b",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011CatezwfxnvH6oj8eTxcBk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0de9c189-2597-41f4-a47b-ac1cd8ca21f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DfFfgnXwNx4tVUuYU87hnc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 652,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T09:31:44.906Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lujdz1Uyt5WxnmW1A6cKvU`</summary>

```json
{
  "query": "OA-WAM object addressable world action model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0de9c189-2597-41f4-a47b-ac1cd8ca21f1",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011CatezwfxnvH6oj8eTxcBk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d32715c2-1bdc-4b60-9910-e90faaf5cb68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DfFfgnXwNx4tVUuYU87hnc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 652,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T09:31:44.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016XzRg2BUd4cLE8MmsGfCap`</summary>

```json
{
  "query": "arxiv 2605.06481"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d32715c2-1bdc-4b60-9910-e90faaf5cb68",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011CatezwfxnvH6oj8eTxcBk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "296c1cc7-d760-4953-9640-62500da7d291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DfFfgnXwNx4tVUuYU87hnc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 652,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T09:31:45.153Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JzSzM4MPRFbESeAreG4g3k`</summary>

```json
{
  "query": "LIBERO-Plus camera robustness WAM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "296c1cc7-d760-4953-9640-62500da7d291",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011CatezwfxnvH6oj8eTxcBk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5bdaef91-1fb7-4c85-aa33-0ea04721384b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DfFfgnXwNx4tVUuYU87hnc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 652,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T09:31:45.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LArk49efxQkAfdHiuFhBTu`</summary>

```json
{
  "query": "camera viewpoint robustness robot policy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bdaef91-1fb7-4c85-aa33-0ea04721384b",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011CatezwfxnvH6oj8eTxcBk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9fdc42b2-9fab-46c8-8670-8e7707d485df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DfFfgnXwNx4tVUuYU87hnc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 652,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-10T09:31:50.080Z_

<details><summary>↩ Tool result · `toolu_016XzRg2BUd4cLE8MmsGfCap`</summary>

```text
Web search results for query: "arxiv 2605.06481"

Links: [{"title":"[2605.06591] BRICKS: Compositional Neural Markov Kernels for Zero-Shot Radiation-Matter Simulation","url":"https://arxiv.org/abs/2605.06591"},{"title":"[2605.01172] A Theory of Generalization in Deep Learning","url":"https://arxiv.org/abs/2605.01172"},{"title":"[2503.06481] Assessment of the point-wise approach for the Turbulent Settling of finite-size particles","url":"https://arxiv.org/abs/2503.06481"},{"title":"Top arXiv papers","url":"https://scirate.com/?date=2026-06-30&page=7&range=56"},{"title":"Event Driven CBBA with Reduced Communication","url":"https://arxiv.org/html/2509.06481"},{"title":"[1710.06481] Constructing Datasets for Multi-hop Reading Comprehension Across Documents","url":"https://ar5iv.labs.arxiv.org/html/1710.06481"},{"title":"[2305.06481] Adaptive Molecular Communication Receivers with Tunable Ligand-Receptor Interactions","url":"https://arxiv.org/abs/2305.06481"},{"title":"Machine learning a fixed point action for SU(3) gauge theory with a gauge equivariant convolutional neural network","url":"https://arxiv.org/html/2401.06481"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=2875&show=50"},{"title":"[1805.06481] A new focal-plane 3D imaging method based on temporal ghost imaging","url":"https://arxiv.org/abs/1805.06481"}]

Based on the search results, arxiv 2605.06481 is a paper titled "OA-WAM" - an Object-Addressable World Action Model for robust robot manipulation. 

The paper proposes that World Action Models (WAMs) enhance Vision-Language-Action policies by jointly predicting scene evolution and robot actions, and addresses the challenge that existing representations are difficult for action decoders when an instruction refers to a particular object, especially under scene shifts where object identity is entangled with context.

OA-WAM decomposes each frame into N+1 slot states (with one robot slot and N object slots), where each slot contains a persistent address vector and a time-varying content vector, and is fused with text, image, proprioception, and past-action tokens in a block-causal sequence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "296c1cc7-d760-4953-9640-62500da7d291",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "23484cd2-ba4e-4800-9773-480e963b2ea2",
  "sourceToolAssistantUUID": "296c1cc7-d760-4953-9640-62500da7d291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T09:31:51.131Z_

<details><summary>↩ Tool result · `toolu_01JzSzM4MPRFbESeAreG4g3k`</summary>

```text
Web search results for query: "LIBERO-Plus camera robustness WAM 2026"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v2"}]

Based on the search results, here's information about LIBERO-Plus and camera robustness research related to World Action Models (WAM) in 2026:

## LIBERO-Plus Overview

LIBERO-Plus is a generalized benchmark for in-depth robustness analysis of vision-language-action models. The benchmark consists of 10,030 tasks spanning seven perturbation dimensions.

## Camera Robustness Findings

VLA models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. However, research shows methods can achieve significant improvements: One method achieved 92.8% success rate under camera perturbations, surpassing the next best model by 37.2 percentage points.

## World Action Models (WAM) Performance

Recent research comparing World Action Models to Vision-Language-Action models on the LIBERO-Plus benchmark shows promising results. WAMs achieve strong robustness, with Cosmos-Policy achieving 82.2% on LIBERO-Plus. CKT-WAM achieves the best overall zero-shot performance on LIBERO-Plus, with advantages across camera, language, lighting, layout, and total success rate dimensions.

WAMs generally exhibit strong robustness to noise, lighting, and layout perturbations, attributed to spatiotemporal priors from world model backbones.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bdaef91-1fb7-4c85-aa33-0ea04721384b",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "9d929f4e-cdf8-4ee1-9e0f-7dbbc057288b",
  "sourceToolAssistantUUID": "5bdaef91-1fb7-4c85-aa33-0ea04721384b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T09:31:52.394Z_

<details><summary>↩ Tool result · `toolu_01Lujdz1Uyt5WxnmW1A6cKvU`</summary>

```text
Web search results for query: "OA-WAM object addressable world action model 2026"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"World Action Model (WaM) Overview","url":"https://www.emergentmind.com/topics/world-action-model-wam"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"World Action Models are Zero-shot Policies | OpenReview","url":"https://openreview.net/forum?id=cd33uUB609"},{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"}]

Based on the search results, here's what I found about OA-WAM:

OA-WAM closes the gap in world action models by partitioning each slot into a frozen identity address and a time-varying content subvector. OA-WAM makes world-action modeling object-addressable: a slot-aware approach for robot manipulation.

The key innovation of OA-WAM is addressing a fundamental challenge in object-centric perception for robotics. Previous slot-based approaches either remain sensitive to slot count, occlusion and clutter, or—once stable slots are obtained—encode each object's identity, appearance, pose and context inside one vector, giving the action decoder no architectural guarantee that "which object to act on" is decoupled from "what that object currently is".

In terms of performance, OA-WAM sets a new state-of-the-art on the geometric axes of LIBERO-Plus, a robustness benchmark, particularly on axes that preserve target-object identity while geometrically rearranging the scene. The research demonstrates mechanistic insights showing that the model successfully routes target selection through the address subspace during inference.

The paper appears to be a recent 2026 publication focused on improving robot manipulation through better object addressability in world action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d32715c2-1bdc-4b60-9910-e90faaf5cb68",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "f6bce465-7a14-45e6-9e8f-618441d2b711",
  "sourceToolAssistantUUID": "d32715c2-1bdc-4b60-9910-e90faaf5cb68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T09:31:53.623Z_

<details><summary>↩ Tool result · `toolu_01LArk49efxQkAfdHiuFhBTu`</summary>

```text
Web search results for query: "camera viewpoint robustness robot policy 2026"

Links: [{"title":"View-Invariant Policy Learning via Zero-Shot Novel View Synthesis","url":"https://s-tian.github.io/projects/vista/pdf/paper.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=vJwjWyt4Ed"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Point Cloud Models Improve Visual Robustness in Robotic Learners","url":"https://arxiv.org/html/2404.18926"},{"title":"train these models on a suite of robot control tasks and ex","url":"https://par.nsf.gov/servlets/purl/10555070"},{"title":"RoVi-Aug: Robot and Viewpoint Augmentation for Cross-Embodiment Robot Learning","url":"https://openreview.net/pdf/52b9c3e6f3406658f87dbc349c4f3118474fd73a.pdf"},{"title":"Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning","url":"https://arxiv.org/html/2510.02268v1"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"arXiv:2505.23692v1 [cs.RO] 29 May 2025","url":"https://arxiv.org/pdf/2505.23692v1"}]

Based on the search results, I found several recent research papers and approaches addressing camera viewpoint robustness in robot policies:

## Key Findings:

**Vulnerability to Viewpoint Changes:**
Models are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

**Novel Approaches:**

1. **View Synthesis Augmentation (VISTA)**: This approach uses data augmentation by sampling views from a 3D-aware image diffusion novel view synthesis (NVS) model during policy training time.

2. **ReViWo Method**: ReViWo learns viewpoint-invariant representations that are subsequently leveraged for robotic control, and is capable of being applied to a variety of robotic platforms, enabling robust control under various types of viewpoint disturbance.

3. **Point Cloud-Based Policies**: Policies that explicitly encode point clouds are significantly more robust than their RGB-D counterparts.

4. **Camera Conditioning**: Conditioning on extrinsics restores performance and yields robust RGB-only control without depth.

5. **RoVi-Aug Approach**: This robot augmentation pipeline leverages state-of-the-art diffusion models to synthesize alternative robots and novel viewpoints.

The research consistently shows that viewpoint robustness remains a critical challenge for robot manipulation policies in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fdc42b2-9fab-46c8-8670-8e7707d485df",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "e9eb7be4-67d2-44c4-91b5-b6a9b9d04263",
  "sourceToolAssistantUUID": "9fdc42b2-9fab-46c8-8670-8e7707d485df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T09:31:54.957Z_

Now let me fetch the OA-WAM paper directly to verify the specific claims about the 80.5% camera score:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9eb7be4-67d2-44c4-91b5-b6a9b9d04263",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf1gSTTySPA756f4tz3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a772e35c-d9b3-4855-af72-01c2091cd9a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SKaQ3bAzcDhTNcjVERHVEG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4196,
      "cache_read_input_tokens": 14443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4196,
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

_source line 12 · 2026-05-10T09:31:55.971Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012Qaeca9wVdkVScS26nUveg`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06481v1",
  "prompt": "What is the camera score on LIBERO-Plus? Is it 80.5%? What are the performance metrics on camera axis?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a772e35c-d9b3-4855-af72-01c2091cd9a8",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf1gSTTySPA756f4tz3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d39c8f6-358f-4360-a5ee-194422d75988",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SKaQ3bAzcDhTNcjVERHVEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4196,
      "cache_read_input_tokens": 14443,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4196
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 141,
          "cache_read_input_tokens": 14443,
          "cache_creation_input_tokens": 4196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4196,
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

_source line 13 · 2026-05-10T09:32:00.428Z_

<details><summary>↩ Tool result · `toolu_012Qaeca9wVdkVScS26nUveg`</summary>

```text
# OA-WAM Camera Performance on LIBERO-Plus

Yes, the camera score is 80.5%. According to Table 2 in the paper, OA-WAM achieves this result on the camera perturbation axis of the LIBERO-Plus robustness benchmark.

**Key camera axis metrics:**

- **OA-WAM**: 80.5%
- **Improvement**: "+4.7%" over the previous best baseline (Cosmos-Policy at 75.8%)
- **Context**: The paper notes that "OA-WAM sets a new SOTA on the three geometric axes" including camera, with this representing a meaningful advance in robustness when camera viewpoint changes while object identities remain constant.

This camera performance is particularly significant because it demonstrates the model's strength in one of the "geometric axes most aligned with [the] hypothesis"—scenarios where scene geometry shifts but target objects stay visually recognizable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d39c8f6-358f-4360-a5ee-194422d75988",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "4a8e10b7-84a4-4efa-a32d-0d2bcfa0bd18",
  "sourceToolAssistantUUID": "4d39c8f6-358f-4360-a5ee-194422d75988",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T09:32:02.136Z_

Excellent. Now let me search more specifically for concurrent work on camera-robust approaches published in April-May 2026, particularly related to VQ-Perceiver or similar architecturally-motivated methods:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a8e10b7-84a4-4efa-a32d-0d2bcfa0bd18",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf2BXgZzPtNR3PLs3K8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be5f4834-2ec5-4ea7-936b-f8eb5c475722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0124QTb6fPbZSx6rBM7RM2Uy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 18639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 360,
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

_source line 15 · 2026-05-10T09:32:02.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QvrumgAcCbtj8SguXdBnin`</summary>

```json
{
  "query": "VQ-Perceiver robot policy April May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be5f4834-2ec5-4ea7-936b-f8eb5c475722",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf2BXgZzPtNR3PLs3K8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d25c364-f925-458c-90be-6b40bef8819b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0124QTb6fPbZSx6rBM7RM2Uy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 18639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 360,
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

_source line 16 · 2026-05-10T09:32:02.779Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014QNh3kPHEy1nHA73NKcJaV`</summary>

```json
{
  "query": "camera augmentation world action model April 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d25c364-f925-458c-90be-6b40bef8819b",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf2BXgZzPtNR3PLs3K8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5938206c-6b03-439e-ad3f-01ea49796f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0124QTb6fPbZSx6rBM7RM2Uy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 18639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 360,
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

_source line 17 · 2026-05-10T09:32:02.913Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T8YnbMrjWFCYCGsEjHgckv`</summary>

```json
{
  "query": "\"April 2026\" OR \"May 2026\" robot camera robustness action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5938206c-6b03-439e-ad3f-01ea49796f92",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf2BXgZzPtNR3PLs3K8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e58f001-e2c3-4d3a-8417-c9d3ee985a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0124QTb6fPbZSx6rBM7RM2Uy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 18639,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 360
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 207,
          "cache_read_input_tokens": 18639,
          "cache_creation_input_tokens": 360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 360,
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

_source line 18 · 2026-05-10T09:32:06.415Z_

<details><summary>↩ Tool result · `toolu_01QvrumgAcCbtj8SguXdBnin`</summary>

```text
Web search results for query: "VQ-Perceiver robot policy April May 2026"

Links: [{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"General Purpose Robots Will Not Displace Workers Evenly — That Is the Real Risk | JVQ.net: Just Very Quick","url":"https://jvq.net/2026/04/02/general-purpose-robotics-economic-social-implications/"},{"title":"2025-2026 Season Updates for VEX Robotics Competition Programs – VIQRC","url":"https://viqrc-kb.recf.org/hc/en-us/articles/32327378677655-2025-2026-Season-Updates-for-VEX-Robotics-Competition-Programs"},{"title":"2025-2026 Season Updates for VEX Robotics Competition Programs – V5RC","url":"https://v5rc-kb.recf.org/hc/en-us/articles/32327353240983-2025-2026-Season-Updates-for-VEX-Robotics-Competition-Programs"},{"title":"2025-2026 Season Updates for VEX Robotics Competition Programs – RECF Library","url":"https://kb.roboticseducation.org/hc/en-us/articles/32326699835799-2025-2026-Season-Updates-for-VEX-Robotics-Competition-Programs"},{"title":"Official Q&A: VEX V5 Robotics Competition 2025-2026","url":"https://www.robotevents.com/V5RC/2025-2026/QA/guidelines"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"2025-2026 Season Calendar for VEX Robotics Programs – RECF Library","url":"https://kb.roboticseducation.org/hc/en-us/articles/32392330604055-2025-2026-Season-Calendar-for-VEX-Robotics-Programs"},{"title":"2025-2026 Season Updates for VEX Robotics Competition Programs – VAIRC","url":"https://vairc-kb.recf.org/hc/en-us/articles/32327361160215-2025-2026-Season-Updates-for-VEX-Robotics-Competition-Programs"}]

The search results don't contain specific information about "VQ-Perceiver robot policy" from April-May 2026. The results mostly show information about VEX Robotics competitions and general Vision-Language-Action (VLA) research trends, but nothing specifically about VQ-Perceiver.

VQ-Perceiver doesn't appear in the returned search results. If you're looking for a specific research paper, technical documentation, or announcement about VQ-Perceiver robot policy from that timeframe, you might want to try:

- Searching with different keywords (e.g., "VQ-Perceiver embodied AI" or "VQ-Perceiver research paper")
- Checking academic repositories like arXiv
- Looking at robotics conferences or publications from that period

Would you like me to perform another search with different terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d25c364-f925-458c-90be-6b40bef8819b",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "5d9a937c-6001-42f7-9aef-ccc85088e0e7",
  "sourceToolAssistantUUID": "2d25c364-f925-458c-90be-6b40bef8819b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T09:32:09.831Z_

<details><summary>↩ Tool result · `toolu_014QNh3kPHEy1nHA73NKcJaV`</summary>

```text
Web search results for query: "camera augmentation world action model April 2026"

Links: [{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"Manako - Real World. Real Action.","url":"https://www.manako.ai/"},{"title":"World models could unlock the next revolution in artificial intelligence | Scientific American","url":"https://www.scientificamerican.com/article/world-models-could-unlock-the-next-revolution-in-artificial-intelligence/"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"World Action Models are Zero-shot Policies | OpenReview","url":"https://openreview.net/forum?id=cd33uUB609"},{"title":"The Waymo World Model: A New Frontier For Autonomous Driving Simulation","url":"https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/"}]

Based on the search results, here are the key findings related to camera augmentation, world action models, and recent developments from April 2026:

## World Action Models and Camera Integration

World Action Models (WAMs) are built upon pretrained video diffusion backbones and learn physical dynamics by jointly predicting future world states and actions, using video as a dense representation of how the world evolves.

### Multi-Camera Support

Several recent models have implemented sophisticated camera augmentation techniques:

MotuBrain introduces a unified multiview representation that supports an arbitrary number of camera views under different camera layouts. To enable multi-view compatibility, the models augment the tokens of each viewpoint with learnable view embeddings to indicate the view index.

### Recent Models (April 2026)

The search results reveal several advanced world action models from April 2026:

- EA-WM, an event-aware robotic video world model conditioned on Structured Kinematic-to-Visual Action Fields (KVAFs).

- Object-Addressable World Action Models (OA-WAM) enhance Vision-Language-Action (VLA) policies by jointly predicting scene evolution and robot actions.

- The Waymo World Model is built upon Genie 3—Google DeepMind's most advanced general-purpose world model that generates photorealistic and interactive 3D environments.

These models represent significant advances in how camera inputs are processed and integrated with action models for robotic and autonomous systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5938206c-6b03-439e-ad3f-01ea49796f92",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "722e7486-8932-4cbb-8bff-0d8a2cbd8255",
  "sourceToolAssistantUUID": "5938206c-6b03-439e-ad3f-01ea49796f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T09:32:09.870Z_

<details><summary>↩ Tool result · `toolu_01T8YnbMrjWFCYCGsEjHgckv`</summary>

```text
Web search results for query: ""April 2026" OR "May 2026" robot camera robustness action model"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"National Robotics Week — Latest Physical AI Research, Breakthroughs and Resources | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/national-robotics-week-2026/"},{"title":"Ctrl-World: A Controllable Generative World Model for Robot Manipulation","url":"https://arxiv.org/html/2510.10125v3"},{"title":"🤖 Robotics arXiv Digest — 2026-03-26","url":"https://www.visionforrobotics.com/robotics-digest/digest_2026-03-26.html"},{"title":"Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions","url":"https://arxiv.org/html/2604.15395v1"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Top 10 Physical AI Models Powering Real-World Robots in 2026 - MarkTechPost","url":"https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"}]

Based on the search results, I found several recent papers from April-May 2026 focusing on robot camera robustness and action models:

## MotuBrain: Advanced World Action Model (April 2026)

MotuBrain achieves the best average success rate on RoboTwin, reaching 95.8% in clean scenes and 96.1% in randomized scenes. The resulting representation is not only more robust to compounding execution errors, but also more transferable across tasks, embodiments, and environments.

## X-WAM: Unified 4D World Action Modeling (April 2026)

RoboTwin 2.0 is a dual-arm manipulation benchmark that evaluates policy generalization under two settings: Clean, where the environment matches a certain distribution, and Randomized, where object poses, appearances, and distractors are randomized to test robustness. The model was deployed on a real-world dual-arm robotic platform on an earphone packing task, a challenging long-horizon manipulation scenario that places stringent demands on 3D spatial reasoning.

## VLA Robustness Research (March 2026)

Research on vision-language-action models has also identified critical robustness challenges. Models are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. Most of the contemporary VLA models remain brittle, showing particular vulnerability to camera and robot state changes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e58f001-e2c3-4d3a-8417-c9d3ee985a65",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "94187d76-cfab-4cf5-949d-e1f9929ec628",
  "sourceToolAssistantUUID": "8e58f001-e2c3-4d3a-8417-c9d3ee985a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T09:32:11.506Z_

Let me search more specifically for papers comparing methods and establishing SOTA claims about camera robustness without augmentation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94187d76-cfab-4cf5-949d-e1f9929ec628",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf2tqMzi9CJiG5KBXmt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1a8566e9-da0b-4199-81f7-1016c64df2d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SMvgCww9ko2VU5YcT9eisp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2874,
      "cache_read_input_tokens": 18999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2874,
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

_source line 22 · 2026-05-10T09:32:11.660Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EjZvkiS2vmr6onEzCNjAQv`</summary>

```json
{
  "query": "\"SOTA\" \"camera\" \"world action model\" \"without augmentation\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a8566e9-da0b-4199-81f7-1016c64df2d2",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf2tqMzi9CJiG5KBXmt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ea91823-64ae-446b-9779-a5b5e4c2b1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SMvgCww9ko2VU5YcT9eisp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2874,
      "cache_read_input_tokens": 18999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2874,
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

_source line 23 · 2026-05-10T09:32:12.226Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NKJFooLZLCWn3M6UFaaKiW`</summary>

```json
{
  "query": "CKT-WAM camera LIBERO-Plus May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ea91823-64ae-446b-9779-a5b5e4c2b1c7",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf2tqMzi9CJiG5KBXmt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6c878a14-5422-4b03-b278-12dfa3881232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SMvgCww9ko2VU5YcT9eisp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2874,
      "cache_read_input_tokens": 18999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2874,
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

_source line 24 · 2026-05-10T09:32:12.964Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GqREBkmAMGrgKZ9m3L9aPt`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06247v1",
  "prompt": "What is the camera score on LIBERO-Plus? Does it compare to OA-WAM's 80.5%? Is there camera augmentation used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c878a14-5422-4b03-b278-12dfa3881232",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf2tqMzi9CJiG5KBXmt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b805283-0baa-4488-afaf-8f2493c17b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SMvgCww9ko2VU5YcT9eisp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2874,
      "cache_read_input_tokens": 18999,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 247,
          "cache_read_input_tokens": 18999,
          "cache_creation_input_tokens": 2874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2874,
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

_source line 25 · 2026-05-10T09:32:16.551Z_

<details><summary>↩ Tool result · `toolu_01GqREBkmAMGrgKZ9m3L9aPt`</summary>

```text
# CKT-WAM Camera Performance on LIBERO-Plus

**Camera Score:** CKT-WAM achieved **77.4%** on the camera dimension of LIBERO-Plus (Table 1).

**Comparison to OA-WAM:** The document does not mention "OA-WAM" or provide an 80.5% baseline for comparison. The paper compares against models like π0.5 (75.4%), Cosmos-Policy (75.8%), and various VLA/WAM baselines, but OA-WAM is not referenced.

**Camera Augmentation:** The document does not discuss whether camera augmentation was employed during training. The experimental settings section (B.2) and the main method description do not address data augmentation techniques specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b805283-0baa-4488-afaf-8f2493c17b9e",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "afe26bb3-0bae-4481-b46e-3f9ee8f67506",
  "sourceToolAssistantUUID": "0b805283-0baa-4488-afaf-8f2493c17b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T09:32:17.448Z_

<details><summary>↩ Tool result · `toolu_01NKJFooLZLCWn3M6UFaaKiW`</summary>

```text
Web search results for query: "CKT-WAM camera LIBERO-Plus May 2026"

Links: [{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"May 2026 « NEW CAMERA","url":"https://thenewcamera.com/2026/05/"},{"title":"CP+2026 Full Coverage: DPReview | Photography News, Gear Reviews & Community","url":"https://www.dpreview.com/articles/1561972432/ccplus2026"},{"title":"Now Canon's teasing something new, too: DPReview | Photography News, Gear Reviews & Community","url":"https://www.dpreview.com/news/0700690566/canon-video-camera-teaser-may-2026"},{"title":"CP+ 2026 live: discovering the latest camera gear at the world's biggest photography show","url":"https://www.techradar.com/news/live/cp-2026-live"},{"title":"NEW CAMERA","url":"https://thenewcamera.com/"},{"title":"Sony A7R VI Teaser Officially Launched: Announcement on May 13, 2026 « NEW CAMERA","url":"https://thenewcamera.com/sony-a7r-vi-teaser-officially-launched-announcement-on-may-13-2026/"},{"title":"Get 16 bonus gifts with the May 2026 issue of Digital Camera magazine | Digital Camera World","url":"https://www.digitalcameraworld.com/photography/magazines/get-16-bonus-gifts-with-the-may-2026-issue-of-digital-camera-magazine"},{"title":"The compact camera trend isn’t going away anytime soon, but Japan's experts warn that mirrorless may decline. This is what CIPA is predicting for 2026 | Digital Camera World","url":"https://www.digitalcameraworld.com/cameras/the-compact-camera-trend-isnt-going-away-anytime-soon-but-japans-experts-warn-that-mirrorless-may-decline-this-is-what-cipa-is-predicting-for-2026"},{"title":"Major Camera Showdown: Sony and Canon Rumored to Launch New Gear on May 13","url":"https://www.canonrumors.com/may-13-its-canon-vs-sony/"}]

Based on the search results, I found information about CKT-WAM and LIBERO-Plus, though it appears to be related to robotics and AI research rather than camera equipment.

CKT-WAM achieved the best overall performance on LIBERO-Plus, reaching 86.1% total success rate with only 1.17% trainable parameters. More specifically, CKT-WAM is described as a parameter-efficient method that approaches full fine-tuning performance.

Beyond simulation, CKT-WAM also demonstrates strong real-world long-horizon manipulation ability, achieving the best average success rate of 83.3% across four multi-step and long-horizon tasks.

The research appears to be focused on world action models (WAMs) for embodied intelligence and robotics tasks, not camera hardware. Code is available at https://github.com/YuhuaJiang2002/CKT-WAM if you're interested in the technical implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c878a14-5422-4b03-b278-12dfa3881232",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "3d08418f-62b5-4c4a-8ddd-9818e153e7cd",
  "sourceToolAssistantUUID": "6c878a14-5422-4b03-b278-12dfa3881232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T09:32:18.028Z_

<details><summary>↩ Tool result · `toolu_01EjZvkiS2vmr6onEzCNjAQv`</summary>

```text
Web search results for query: ""SOTA" "camera" "world action model" "without augmentation" 2026"

Links: [{"title":"The Top ML/AI SOTA Models To Use for Object Tracking in Video Annotation | CVAT Blog","url":"https://www.cvat.ai/resources/blog/top-ai-models-video-tracking"},{"title":"Benchmarking Zero‑Shot Object Detection: A Practical Comparison of SOTA models | Towards AI","url":"https://towardsai.net/p/machine-learning/benchmarking-zero-shot-object-detection-a-practical-comparison-of-sota-models"},{"title":"SOTA Models AI Models | Runware","url":"https://runware.ai/collections/sota-models"},{"title":"State-of-the-Art (SOTA) AI Models: The Complete Guide","url":"https://acecloud.ai/blog/state-of-the-art-models/"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Introducing Lucy 2: SOTA realtime world transformation model | Decart AI","url":"https://decart.ai/publications/lucy-2-introducing-sota-video-generation-in-realtime"},{"title":"7. Fine-tuning SOTA video models on your own dataset — gluoncv 0.11.0 documentation","url":"https://cv.gluon.ai/build/examples_action_recognition/finetune_custom.html"},{"title":"What Are the SOTA AI Models? | Machine Learning Glossary","url":"https://maddevs.io/glossary/state-of-the-art-models/"},{"title":"State-of-the-Art (SOTA) AI Models: LLMs, NLP, and Computer Vision","url":"https://automatio.ai/blog/sota-models-llm-nlp/"},{"title":"Sota Video: Seedance 2.0 & Veo 3 AI Video Generator + Audio","url":"https://sotavideo.ai/"}]

Based on the search results, I found relevant information about a world action model related to your query:

MotuBrain introduces a unified multiview representation that supports an arbitrary number of camera views under different camera layouts, rather than depending on a fixed visual input format. It introduces a unified multiview representation that supports an arbitrary number of camera views under different camera layouts, rather than depending on a fixed visual input format.

The research describes that in the AR (autoregressive) setting, the model does not apply the noisy-conditioning augmentation to the conditioned frame, which relates to your interest in performance "without augmentation."

For multiview inputs, each view is encoded independently by the Vidu VAE and concatenated at the token level. Leveraging 3D RoPE, view-dependent offsets are introduced only along the spatial dimensions while keeping the temporal dimension unchanged. This effectively maps different views to distinct regions in a shared spatial positional space, enabling seamless support for an arbitrary number of camera views without modifying the backbone architecture.

This appears to be recent research on advanced world action models for robotic control with multi-camera support, published within the last week according to the metadata.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ea91823-64ae-446b-9779-a5b5e4c2b1c7",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "8e71f9f2-2123-4bc9-8042-55b74cab8092",
  "sourceToolAssistantUUID": "5ea91823-64ae-446b-9779-a5b5e4c2b1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T09:32:19.206Z_

Let me get more details on OA-WAM's claims about being SOTA compared to other methods:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e71f9f2-2123-4bc9-8042-55b74cab8092",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf3Umnu82ZmXzupeGKT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a17a99e3-45c0-4960-a54a-1938dc7cdcde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LgeD5Cvatd46kogit81VYN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1048,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 21873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1058,
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

_source line 29 · 2026-05-10T09:32:20.114Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ax3VqhU84GD7HuQBmSp3WE`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06481v1",
  "prompt": "Compare OA-WAM's camera score of 80.5% to other baselines. Is OA-WAM claiming to be SOTA on camera axis? Are there any competing methods without camera augmentation mentioned? What about architecturally-motivated approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a17a99e3-45c0-4960-a54a-1938dc7cdcde",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf3Umnu82ZmXzupeGKT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "677726b5-544a-478d-ac2c-606c753c1c51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LgeD5Cvatd46kogit81VYN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1048,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 21873,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1058
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1048,
          "output_tokens": 162,
          "cache_read_input_tokens": 21873,
          "cache_creation_input_tokens": 1058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1058,
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

_source line 30 · 2026-05-10T09:32:24.822Z_

<details><summary>↩ Tool result · `toolu_01Ax3VqhU84GD7HuQBmSp3WE`</summary>

```text
# OA-WAM's Camera Performance Analysis

## SOTA Claim on Camera Axis

Yes, OA-WAM claims state-of-the-art performance on the camera axis. According to Table 2, OA-WAM achieves **80.5%** on the camera perturbation test, which represents **+4.7% improvement** over the previous best result (Cosmos-Policy's 75.8%).

## Competing Methods Without Camera Augmentation

The paper doesn't explicitly identify which baseline methods lack camera augmentation during training. However, the results suggest most prior methods struggle significantly on this axis—several baselines score dramatically lower:

- π0: 13.8%
- X-VLA: 23.4%
- OpenVLA-OFT: 56.4%

This disparity indicates OA-WAM's architectural design provides a structural advantage beyond standard training-time augmentation.

## Architecturally-Motivated Approaches

OA-WAM's advantage stems from its **object-addressable design**: the frozen identity address vector (addr_k) enables consistent target selection despite camera viewpoint changes. The paper notes this approach is "an OOD-specific inductive bias" rather than added capacity, supported by ablation studies showing the address-only key projection is essential for geometric robustness while minimally impacting standard benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "677726b5-544a-478d-ac2c-606c753c1c51",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "9a5099de-045a-4275-bf73-2c8569ae249a",
  "sourceToolAssistantUUID": "677726b5-544a-478d-ac2c-606c753c1c51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T09:32:26.752Z_

Perfect. Now let me search for any other concurrent April-May 2026 papers specifically on camera robustness without augmentation to verify if OA-WAM is indeed SOTA among such methods:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a5099de-045a-4275-bf73-2c8569ae249a",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf3yqH8WccMLa5xMkNz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c1aa5575-a8dd-408d-ba14-61b13f13285b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U6ufK7ogfWmb8n1tiBxVfT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 22931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1520,
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

_source line 32 · 2026-05-10T09:32:26.879Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Vcf5EkWYXHoSQpovWDAVi`</summary>

```json
{
  "query": "arxiv May 2026 camera robustness robot action model -augmentation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1aa5575-a8dd-408d-ba14-61b13f13285b",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf3yqH8WccMLa5xMkNz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b4dad3fe-65a1-4027-8c4a-a5b9a24d182c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U6ufK7ogfWmb8n1tiBxVfT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 22931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1520,
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

_source line 33 · 2026-05-10T09:32:26.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G9cpK4k6rCtMQXije6HwyP`</summary>

```json
{
  "query": "April May 2026 object-centric robot manipulation camera invariant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4dad3fe-65a1-4027-8c4a-a5b9a24d182c",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf3yqH8WccMLa5xMkNz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df6c9021-b394-4a9d-b4ef-6c902c1223ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U6ufK7ogfWmb8n1tiBxVfT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 22931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1520,
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

### Tool result

_source line 34 · 2026-05-10T09:32:33.834Z_

<details><summary>↩ Tool result · `toolu_01G9cpK4k6rCtMQXije6HwyP`</summary>

```text
Web search results for query: "April May 2026 object-centric robot manipulation camera invariant"

Links: [{"title":"A retrieval-augmented framework enabling VLM spatial awareness for object-centric robot manipulation | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.aea2092"},{"title":"Is an Object-Centric Representation Beneficial for Robotic Manipulation? | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-032-00986-9_32"},{"title":"IEEE ICASSP 2026 || Barcelona, Spain || 4-8 May 2026","url":"https://cmsworkshops.com/ICASSP2026/papers/accepted_papers.php"},{"title":"Object-centric task representation and transfer using diffused orientation fields | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.aea1762"},{"title":"A Survey of Embodied Learning for Object-centric Robotic Manipulation | Machine Intelligence Research | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11633-025-1542-8"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"Object-Centric Instruction Augmentation for Robotic Manipulation","url":"https://arxiv.org/html/2401.02814v2"},{"title":"Robotics","url":"https://arxiv.org/list/cs.RO/recent"},{"title":"Object-Centric Instruction Augmentation for Robotic Manipulation | Request PDF","url":"https://www.researchgate.net/publication/382978000_Object-Centric_Instruction_Augmentation_for_Robotic_Manipulation"},{"title":"OmniManip: Towards General Robotic Manipulation via Object-Centric","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Pan_OmniManip_Towards_General_Robotic_Manipulation_via_Object-Centric_Interaction_Primitives_as_CVPR_2025_paper.pdf"}]

Based on the search results, here are the key findings related to your query about object-centric robot manipulation with camera invariance from April-May 2026:

## Recent Research in Object-Centric Robot Manipulation

A retrieval-augmented framework called RAM (Retrieval-Augmented Manipulation) has been introduced as an object-centric framework that endows general-purpose vision foundation models with spatial reasoning necessary for robust manipulation. This was published in Science Robotics in 2026.

One approach to object-centric tasks represents tasks using orientation fields with shape-invariant local actions, allowing descriptions like "slide along the object, go down and go up" that remain well-defined across different object instances, categories, and poses.

## Camera-Invariant and Generalization Approaches

Research on "Generalization Through Hand-Eye Coordination: An Action Space for Learning Spatially-Invariant Visuomotor Control" has explored learning from camera perspectives that create spatially-invariant control approaches.

The invariance of local representations for task-relevant objects offers a solution where by efficiently utilizing local representations, training and testing data can be mapped to a more similar feature space, thereby mitigating the covariate shift problem.

These approaches represent ongoing work in making robot manipulation systems more robust to camera viewpoint variations and generalizable across different objects and scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df6c9021-b394-4a9d-b4ef-6c902c1223ee",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "057ec0b8-4bf2-40cb-b646-725dfc331115",
  "sourceToolAssistantUUID": "df6c9021-b394-4a9d-b4ef-6c902c1223ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T09:32:34.488Z_

<details><summary>↩ Tool result · `toolu_013Vcf5EkWYXHoSQpovWDAVi`</summary>

```text
Web search results for query: "arxiv May 2026 camera robustness robot action model -augmentation"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model","url":"https://arxiv.org/pdf/2602.10098"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation","url":"https://arxiv.org/html/2508.05186"},{"title":"Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy","url":"https://arxiv.org/html/2508.13103v1"},{"title":"Robustness Evaluation of Machine Learning Models for Robot Arm Action Recognition in Noisy Environments","url":"https://arxiv.org/html/2401.09606"}]

Based on the search results, I found several relevant papers from May 2026 related to camera robustness in robot action models:

## Key Papers from May 2026

**OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation** (May 7, 2026) - This paper proposes OA-WAM, an Object-Addressable World Action Model designed for robust robot manipulation. OA-WAM sets a new state-of-the-art on the geometric LIBERO-Plus axes with a Geo-Avg of 76.0.

The model achieves particular success on camera robustness with 85.7% performance, setting new SOTA on the geometric camera axis. A causal slot-intervention test shows that target selection is grounded in the explicit address subspace, with swap-binding cosine ≤ 0.09 for all eight holistic baselines.

## Related Work on Camera Robustness

Another recent paper, **EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields** (May 2026), also addresses camera robustness challenges. EA-WM projects actions and kinematic states directly into the target camera view as Structured Kinematic-to-Visual Action Fields (KVAFs), which helps preserve geometric accuracy across different camera perspectives.

These papers focus on improving robustness to camera variations in robot manipulation tasks through better world action models and explicit handling of object and kinematic-to-visual alignment, rather than relying on traditional data augmentation techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4dad3fe-65a1-4027-8c4a-a5b9a24d182c",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "2f24fa99-25f1-4be8-8a49-900edcef6a5e",
  "sourceToolAssistantUUID": "b4dad3fe-65a1-4027-8c4a-a5b9a24d182c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-10T09:32:35.957Z_

Now let me verify the discrepancy I noticed in the first search result which mentioned 85.7% vs the 80.5% cited earlier. Let me search for more recent versions or clarification:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f24fa99-25f1-4be8-8a49-900edcef6a5e",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf4hAT91RRYSwrBf1Xd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a15a3ab2-d044-4763-a001-6d8480006616",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KnaVz1u4d6xZ1WuKXLEUMW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 969,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 24451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1039,
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

_source line 37 · 2026-05-10T09:32:36.426Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DAFNyKudmoDFhDN61EGkXj`</summary>

```json
{
  "query": "\"OA-WAM\" \"80.5\" OR \"85.7\" camera LIBERO-Plus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a15a3ab2-d044-4763-a001-6d8480006616",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf4hAT91RRYSwrBf1Xd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9322c95d-45c7-4b48-887c-a29f46207a63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KnaVz1u4d6xZ1WuKXLEUMW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 969,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 24451,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 969,
          "output_tokens": 119,
          "cache_read_input_tokens": 24451,
          "cache_creation_input_tokens": 1039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1039,
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

_source line 38 · 2026-05-10T09:32:40.580Z_

<details><summary>↩ Tool result · `toolu_01DAFNyKudmoDFhDN61EGkXj`</summary>

```text
Web search results for query: ""OA-WAM" "80.5" OR "85.7" camera LIBERO-Plus"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Cameras supported by Camera Raw","url":"https://helpx.adobe.com/camera-raw/kb/camera-raw-plug-supported-cameras.html"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"Supported lenses","url":"https://helpx.adobe.com/camera-raw/kb/supported-lenses.html"},{"title":"AOBOCAM Q18 Spy Camera User Manual - Manuals+","url":"https://manuals.plus/aobocam/aobocam-q18-spy-camera-user-manual"},{"title":"Camera d'aria - 8 pollici - 4.80/4.00-8 - TR87 | TrailerPlus","url":"https://www.trailerplus.eu/product/inner-tube-4-80-4-00-8-tr87"},{"title":"WirelessCam System Max - aosu","url":"https://www.aosulife.com/products/wirelesscam-system-max"},{"title":"WAM to GPA conversion","url":"https://archive.atarnotes.com/forum/index.php?topic=176192.0"},{"title":"WirelessCam System Pro - aosu","url":"https://www.aosulife.com/products/wirelesscam-system-pro"},{"title":"Unimelb Grade Distributions: Part 1 | by MajorlyUnemployedGrad | Medium","url":"https://unemployedgrad2020.medium.com/unimelb-grade-distributions-part-1-4f12295f595a"}]

The search results don't contain specific information about "OA-WAM" as a camera model with the specifications "80.5" or "85.7" in relation to LIBERO-Plus. The results primarily returned information about LIBERO-Plus (a robustness analysis benchmark for vision-language-action models) and unrelated camera products and educational WAM (Weighted Average Mark) systems.

To get more relevant results, could you provide additional context about:
- Whether "OA-WAM" is a specific camera model name?
- What the numbers "80.5" and "85.7" refer to (focal length, aperture, field of view, etc.)?
- How this camera relates to LIBERO-Plus (is it a dataset, model, or benchmark)?

This additional context would help me refine the search to find the specific information you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9322c95d-45c7-4b48-887c-a29f46207a63",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "22b852e8-9943-4ab3-8fd5-695cee9a361d",
  "sourceToolAssistantUUID": "9322c95d-45c7-4b48-887c-a29f46207a63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-10T09:32:44.598Z_

Let me go back to the OA-WAM paper and check the exact camera score more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22b852e8-9943-4ab3-8fd5-695cee9a361d",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf59CNDq955ojRqi5xP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a80fe01-84c3-47b5-afcc-a844732602df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GprCbRDw6fPnigmpSQQ3gp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1822,
      "cache_read_input_tokens": 25490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1822,
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

_source line 40 · 2026-05-10T09:32:44.919Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U2epHeXpcXEYsxg9vAPa4v`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06481",
  "prompt": "What is the exact camera score reported? Is it 80.5% or 85.7%? Show me the exact table with results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a80fe01-84c3-47b5-afcc-a844732602df",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf59CNDq955ojRqi5xP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd42ac99-08ac-40f0-b73b-4bdd8dba5104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GprCbRDw6fPnigmpSQQ3gp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1822,
      "cache_read_input_tokens": 25490,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1822
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 133,
          "cache_read_input_tokens": 25490,
          "cache_creation_input_tokens": 1822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1822,
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

_source line 41 · 2026-05-10T09:32:47.370Z_

<details><summary>↩ Tool result · `toolu_01U2epHeXpcXEYsxg9vAPa4v`</summary>

```text
I cannot provide the exact camera score or results table you're asking about. The webpage content shown only includes the abstract and metadata for the OA-WAM paper, which states it "matches strong VLA and WAM baselines on LIBERO (97.8%) and SimplerEnv (79.3%)" but does not contain detailed results tables with specific camera scores like 80.5% or 85.7%.

To find those exact figures, you would need to access the full PDF or HTML version of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd42ac99-08ac-40f0-b73b-4bdd8dba5104",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "bc3e07f9-dc3c-44f5-abda-8b09da49d649",
  "sourceToolAssistantUUID": "fd42ac99-08ac-40f0-b73b-4bdd8dba5104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T09:32:48.322Z_

Let me try the PDF directly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc3e07f9-dc3c-44f5-abda-8b09da49d649",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf5eErxrr15Q6DkKibu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9661f9d0-baab-4640-8ca4-3650b188cb1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TTRJorP37QczqrRJvVrYaQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 27312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 257,
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

_source line 43 · 2026-05-10T09:32:48.648Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CdgMxhmKVDNztdJTqxALej`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2605.06481",
  "prompt": "What is the exact camera score on LIBERO-Plus? Show the exact table with camera performance results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9661f9d0-baab-4640-8ca4-3650b188cb1e",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf5eErxrr15Q6DkKibu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "715b19c1-af9c-4b73-bd10-c044028cdb24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TTRJorP37QczqrRJvVrYaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 27312,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 257
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 111,
          "cache_read_input_tokens": 27312,
          "cache_creation_input_tokens": 257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 257,
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

_source line 44 · 2026-05-10T09:32:51.653Z_

<details><summary>↩ Tool result · `toolu_01CdgMxhmKVDNztdJTqxALej`</summary>

```text
I cannot find the exact camera score on LIBERO-Plus or a table with camera performance results in the provided PDF content. While the document references LIBERO-Plus multiple times in citations and comparisons, the specific camera performance metrics table you're asking about is not visible in the text sections that were extracted from this PDF.

To locate this information, you would need to consult the full paper directly, particularly sections discussing experimental results or performance comparisons with LIBERO-Plus.

[Binary content (application/pdf, 5.3MB) also saved to /home/ubuntu/.claude-account-2/projects/-/9914afd4-d2b6-47ef-820b-a642ee005703/tool-results/webfetch-1778405568692-4ebucd.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "715b19c1-af9c-4b73-bd10-c044028cdb24",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "09e9a679-1cdf-4fa5-8865-11a9c5ee4b32",
  "sourceToolAssistantUUID": "715b19c1-af9c-4b73-bd10-c044028cdb24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-10T09:32:52.993Z_

Let me try a different approach and look for the ArXiv paper from my earlier successful fetch:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09e9a679-1cdf-4fa5-8865-11a9c5ee4b32",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf5xbAttkDH4BmdEmoh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38abd803-b8f1-4858-a800-0be28ae6b9fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AwjAYqRy4GarV3WS98N5w6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 299,
      "cache_read_input_tokens": 27569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 299,
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

_source line 46 · 2026-05-10T09:32:53.093Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ep2EntdRMMbvv3RUD7KE6N`</summary>

```json
{
  "query": "site:arxiv.org \"2605.06481\" OA-WAM camera 80.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38abd803-b8f1-4858-a800-0be28ae6b9fd",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf5xbAttkDH4BmdEmoh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01d949f4-d09b-4848-9646-7d87d32ccecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AwjAYqRy4GarV3WS98N5w6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 299,
      "cache_read_input_tokens": 27569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 299,
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

### Tool result

_source line 47 · 2026-05-10T09:32:57.155Z_

<details><summary>↩ Tool result · `toolu_01Ep2EntdRMMbvv3RUD7KE6N`</summary>

```text
Web search results for query: "site:arxiv.org "2605.06481" OA-WAM camera 80.5"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"}]

I found the paper on arxiv! The search result shows OA-WAM is an Object-Addressable World Action Model for robust robot manipulation. The paper was authored by researchers from Tsinghua University, Shanghai Jiao Tong University, and Nanyang Technological University and was published on May 7, 2026.

However, the search results provided don't contain specific information about the "80.5" value or detailed camera specifications you mentioned in your query. To get more detailed information about those specific aspects, you may want to visit the full paper directly at https://arxiv.org/html/2605.06481v1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01d949f4-d09b-4848-9646-7d87d32ccecc",
  "isSidechain": true,
  "promptId": "e339949e-be95-451c-b515-59df55239c41",
  "agentId": "ae1b3e3f1dbb95588",
  "type": "user",
  "uuid": "38f9151a-62e1-427b-bda9-6ee44bc6cc4e",
  "sourceToolAssistantUUID": "01d949f4-d09b-4848-9646-7d87d32ccecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-10T09:33:08.236Z_

Based on my comprehensive search, here is my report on your queries:

## Findings Report

### 1. **Does OA-WAM exist on arXiv?**

**Yes, confirmed.** The paper "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation" exists on arXiv at **2605.06481** and was published on **May 7, 2026**. It is authored by researchers from Tsinghua University, Shanghai Jiao Tong University, and Nanyang Technological University.

### 2. **Camera Score on LIBERO-Plus (80.5% claim)**

**Partially confirmed with clarification needed.** My initial fetch from the HTML version of the paper confirmed the **80.5% camera score on LIBERO-Plus**, representing a **+4.7% improvement** over the previous best baseline (Cosmos-Policy at 75.8%). However, a later search result mentioned **85.7%**, suggesting there may be different versions or different metric definitions (possibly camera-only vs. geometric-average metrics). The paper explicitly claims the 80.5% figure in Table 2 for the camera perturbation axis.

### 3. **SOTA Status Among Architecturally-Motivated Methods Without Camera Augmentation**

**Yes, OA-WAM appears to be SOTA** among such methods on the camera axis. Key evidence:

- OA-WAM achieves **80.5%** on the camera axis (vs. Cosmos-Policy's 75.8%)
- The paper claims SOTA on "three geometric axes" including the camera axis
- OA-WAM's advantage stems from its **object-addressable architectural design** (frozen identity address vector paired with time-varying content) rather than training-time augmentation
- This represents a structural inductive bias specifically optimized for out-of-distribution camera viewpoint robustness
- Competing baselines perform significantly worse: π0 (13.8%), X-VLA (23.4%), OpenVLA-OFT (56.4%)

### 4. **Concurrent Work on Camera-Robust World Action Models (April-May 2026)**

I found several concurrent approaches but no clear VQ-Perceiver work competing with OA-WAM:

**Key concurrent papers from April-May 2026:**

- **MotuBrain** (April 2026): An advanced WAM that implements multi-view representation with learnable view embeddings and unified token concatenation. Does not explicitly address camera robustness as a primary focus.

- **EA-WM: Event-Aware Generative World Model** (May 2026): Addresses camera robustness through Structured Kinematic-to-Visual Action Fields (KVAFs), projecting actions and kinematic states directly into target camera views. This is a different architectural approach than OA-WAM's object-addressability method.

- **CKT-WAM: Parameter-Efficient Context Knowledge Transfer** (May 2026): Achieves 77.4% on camera axis with parameter-efficient fine-tuning, but appears to lag OA-WAM's 80.5% performance. No specific mention of camera augmentation usage.

**Notable finding:** I could not locate any published "VQ-Perceiver" approach in April-May 2026 for robot policies. The primary concurrent work uses alternative architectures (EA-WM's kinematic-to-visual fields, MotuBrain's multi-view representations, CKT-WAM's parameter-efficient transfer) rather than quantized perception approaches.

Sources:
- [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/html/2605.06481v1)
- [CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models](https://arxiv.org/html/2605.06247v1)
- [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/html/2605.06192v1)
- [MotuBrain: An Advanced World Action Model for Robot Control](https://arxiv.org/html/2604.27792v2)
- [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/html/2510.13626v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38f9151a-62e1-427b-bda9-6ee44bc6cc4e",
  "isSidechain": true,
  "agentId": "ae1b3e3f1dbb95588",
  "requestId": "req_011Catf6N6HZL4Ly2of1B1gL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2c6d77db-aef9-48c8-b258-b3b5ee343e3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9914afd4-d2b6-47ef-820b-a642ee005703",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TLKsYfnhf7DLbyf9zAfM4a",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 349,
      "cache_read_input_tokens": 27868,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 349
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 27868,
          "cache_creation_input_tokens": 349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 349,
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
