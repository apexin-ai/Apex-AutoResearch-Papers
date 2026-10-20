# Research conversation: You are helping me verify an ML research proposal about compositional humanoid trajectory generation using body-part inp

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 94
- **Recorded user turns:** 1
- **Tool calls:** 40
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7ec97cca13734ab9.jsonl`
- **Structured JSON:** [`fdd82811661ce0186316.json`](../../sessions/fd/fdd82811661ce0186316.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

94 recorded events

### User

_source line 1 · 2026-05-10T20:24:47.100Z_

You are helping me verify an ML research proposal about compositional humanoid trajectory generation using body-part inpainting on diffusion models. I need to find ANY competing or closely related work the proposal may have missed. Search thoroughly for:

1. **Compositional body-part motion generation 2025-2026**: Search for recent papers that decompose motion generation by body parts using diffusion models. Try multiple queries:
   - "body part compositional motion diffusion 2026"
   - "spatial composition motion generation diffusion"
   - "body part inpainting motion diffusion"
   - "humanoid compositional trajectory generation"

2. **Iterative conditional generation in diffusion**: Search for papers that use sequential conditional diffusion processes (generate one part, then condition the next generation on it), as opposed to score composition. Try:
   - "iterative conditional diffusion generation"
   - "sequential conditional diffusion composition"
   - "autoregressive diffusion spatial composition"

3. **Robot motion diffusion with inpainting/masking 2025-2026**: Search for papers that apply inpainting or masking to robot-specific (not human) motion diffusion models:
   - "robot motion diffusion inpainting"
   - "masked robot trajectory diffusion"
   - "constraint conditioning diffusion robot"

4. **Kimodo extensions or follow-up work**: Search for any papers building on Kimodo (NVIDIA, March 2026):
   - "Kimodo motion generation"
   - "BONES-SEED diffusion"
   - "G1 humanoid diffusion"

5. **Any concurrent work on humanoid data generation via diffusion**: 
   - "humanoid data generation diffusion 2026"
   - "synthetic humanoid training data diffusion"

Use WebSearch for each query. Report ALL papers found with titles, venues, dates, and brief descriptions. I need to know if there's anything the proposal missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "bdc0caca-afde-4cb8-9967-3e8c89f6ce75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:24:47.103Z_

```json
{
  "parentUuid": "bdc0caca-afde-4cb8-9967-3e8c89f6ce75",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
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
  "uuid": "c1e6892b-674d-4af8-98e7-fc415db2b77a",
  "timestamp": "2026-05-10T20:24:47.103Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T20:24:54.701Z_



I'll conduct a thorough search across all these areas. Let me start by loading the WebSearch tool, then run searches in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1e6892b-674d-4af8-98e7-fc415db2b77a",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWoKx9Vd3QGqALVyuwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "713519b9-4399-4b7c-a656-5e7e75632d47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2XVcyXF4A9cmtneeTknrS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 8083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 979,
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

_source line 4 · 2026-05-10T20:24:54.998Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013PqbQtfqfaP1fyphqdiKpg`</summary>

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
  "parentUuid": "713519b9-4399-4b7c-a656-5e7e75632d47",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWoKx9Vd3QGqALVyuwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7df12a75-99e7-4447-bdf0-20916be8fad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2XVcyXF4A9cmtneeTknrS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 8083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 979,
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

### Tool result

_source line 5 · 2026-05-10T20:24:55.001Z_

<details><summary>↩ Tool result · `toolu_013PqbQtfqfaP1fyphqdiKpg`</summary>

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
  "parentUuid": "7df12a75-99e7-4447-bdf0-20916be8fad0",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "aaec2358-7bea-40da-aa3f-30eada7552d2",
  "sourceToolAssistantUUID": "7df12a75-99e7-4447-bdf0-20916be8fad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T20:24:59.166Z_



Now let me run the first batch of searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaec2358-7bea-40da-aa3f-30eada7552d2",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWow7VduuZzXLc6kbsi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5a4d6d1-34f9-43bb-a921-6d80336b09f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G64wpz7TFw6kTGhFwvGjh4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 9062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1424,
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

_source line 7 · 2026-05-10T20:24:59.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BimT7CdoXQnxiTM32Hxwm7`</summary>

```json
{
  "query": "body part compositional motion diffusion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5a4d6d1-34f9-43bb-a921-6d80336b09f9",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWow7VduuZzXLc6kbsi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24feb4a1-0a81-4b13-88fd-9b72946c527d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G64wpz7TFw6kTGhFwvGjh4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 9062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1424,
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

_source line 8 · 2026-05-10T20:25:00.214Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015SbacRNYRgxbw9cDM3RmhE`</summary>

```json
{
  "query": "spatial composition motion generation diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24feb4a1-0a81-4b13-88fd-9b72946c527d",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWow7VduuZzXLc6kbsi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4c14527-b46a-4881-bc07-675103f39a9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G64wpz7TFw6kTGhFwvGjh4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 9062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1424,
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

_source line 9 · 2026-05-10T20:25:00.588Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017yrwPdnYSpakPBSiC3H4Wy`</summary>

```json
{
  "query": "body part inpainting motion diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4c14527-b46a-4881-bc07-675103f39a9d",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWow7VduuZzXLc6kbsi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f0bea6d-5a7e-4b6a-80a0-165bf75cdcdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G64wpz7TFw6kTGhFwvGjh4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 9062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1424,
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

_source line 10 · 2026-05-10T20:25:00.872Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FbyqsBRwZ2bcSnJ5ZwrPyq`</summary>

```json
{
  "query": "humanoid compositional trajectory generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f0bea6d-5a7e-4b6a-80a0-165bf75cdcdb",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWow7VduuZzXLc6kbsi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09b29de4-a6da-4201-8827-20b4e46e3468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G64wpz7TFw6kTGhFwvGjh4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 9062,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1424
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 9062,
          "cache_creation_input_tokens": 1424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1424,
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

_source line 11 · 2026-05-10T20:25:07.438Z_

<details><summary>↩ Tool result · `toolu_015SbacRNYRgxbw9cDM3RmhE`</summary>

```text
Web search results for query: "spatial composition motion generation diffusion"

Links: [{"title":"Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models","url":"https://arxiv.org/html/2409.11920v1"},{"title":"[2409.11920] Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models","url":"https://arxiv.org/abs/2409.11920"},{"title":"[2409.11920v1] Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models","url":"https://arxiv.org/abs/2409.11920v1"},{"title":"EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space","url":"https://arxiv.org/html/2412.14706v1"},{"title":"FineMoGen: Fine-Grained Spatio-Temporal Motion Generation and Editing","url":"https://arxiv.org/html/2312.15004"},{"title":"ST-GDance++: A Scalable Spatial–Temporal Diffusion for Long-Duration Group Choreography","url":"https://arxiv.org/html/2603.22316"},{"title":"FineMoGen: Fine-Grained Spatio-Temporal Motion ...","url":"https://mingyuan-zhang.github.io/projects/FineMoGen.html"},{"title":"Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions","url":"https://arxiv.org/html/2604.16135v1"},{"title":"CustomCrafter: Customized Video Generation with Preserving Motion and Concept Composition Abilities","url":"https://arxiv.org/html/2408.13239"},{"title":"EnergyMoGen: Compositional Human Motion Generation with ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_EnergyMoGen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_CVPR_2025_paper.pdf"}]

Based on the web search results, I found several research papers related to spatial composition and motion generation using diffusion models. Here are the key findings:

## Main Research Areas

The research addresses the challenge of generating realistic 3D human motions for action classes that were never seen during the training phase by decomposing complex actions into simpler movements using GPT models.

## Key Approaches

1. **Temporal and Spatial Composition**: Methods offer solutions to both temporal and spatial decomposition during the inference phase, which can be integrated with any pre-trained motion diffusion model to synthesize motions that fall outside the distribution of the training set.

2. **Energy-Based Models**: EnergyMoGen is a compositional motion generation framework that incorporates cross-attention within the denoising autoencoder and enables motion composition by implicitly combining energy terms of multiple diffusion models.

3. **Fine-Grained Spatio-Temporal Motion**: FineMoGen is a diffusion-based motion generation framework with spatial-temporal composition that builds upon diffusion models with a Spatio-Temporal Mixture Attention (SAMI) architecture, which optimizes generation by explicitly modeling constraints of spatio-temporal composition.

4. **Compound Action Generation**: Motion-Adapter integrates cross-attention with convolutional layers to compute decoupled cross-attention maps, which serve as structural masks applied to noisy motions at each denoising step to guide generation toward semantically precise actions.

These approaches enable generating complex, compositional human motions by decomposing them into simpler, known components that can be recombined spatially and temporally.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4c14527-b46a-4881-bc07-675103f39a9d",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "44cdd940-bcff-46f5-bb4f-0cc6db2713fc",
  "sourceToolAssistantUUID": "e4c14527-b46a-4881-bc07-675103f39a9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T20:25:07.630Z_

<details><summary>↩ Tool result · `toolu_017yrwPdnYSpakPBSiC3H4Wy`</summary>

```text
Web search results for query: "body part inpainting motion diffusion"

Links: [{"title":"MDM: Human Motion Diffusion Model","url":"https://guytevet.github.io/mdm-page/"},{"title":"COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation","url":"https://arxiv.org/html/2408.16426"},{"title":"Stable Diffusion inpaint top body experiments | by Sarit Ritwirune | Medium","url":"https://sarit-r.medium.com/stable-diffusion-inpaint-top-body-experiments-42d5b7603756"},{"title":"COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation","url":"https://nvlabs.github.io/COIN/"},{"title":"COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-72640-8_24"},{"title":"From Rigging to Waving: 3D-Guided Diffusion for Natural Animation of Hand-Drawn Characters","url":"https://arxiv.org/html/2509.06573"},{"title":"How to remove extra limbs with Stable Diffusion inpainting - Stable Diffusion Art","url":"https://stable-diffusion-art.com/inpainting-remove-extra-limbs/"},{"title":"Human Motion Prediction via Spatio-Temporal Inpainting","url":"https://www.researchgate.net/publication/339562094_Human_Motion_Prediction_via_Spatio-Temporal_Inpainting"},{"title":"COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation | Request PDF","url":"https://www.researchgate.net/publication/383530125_COIN_Control-Inpainting_Diffusion_Prior_for_Human_and_Camera_Motion_Estimation"},{"title":"RePaint: Inpainting using Denoising Diffusion Probabilistic Models | Request PDF","url":"https://www.researchgate.net/publication/363908996_RePaint_Inpainting_using_Denoising_Diffusion_Probabilistic_Models"}]

Based on the search results, here are the key findings about body part inpainting and motion diffusion:

## Motion Diffusion Models with Inpainting

Diffusion-based motion models can adapt image inpainting techniques by setting motion prefixes and suffixes, then using the model to fill in the gap, with textual conditions guiding the model to fill the gap with specific motion while maintaining semantic consistency.

## COIN: Control-Inpainting Diffusion Prior

A notable recent approach is COIN, which uses a control-inpainting motion diffusion prior to handle challenging cases involving entangled human and camera motion. The method includes a soft inpainting strategy that automatically identifies high-confidence regions of predicted global motion and uses them as soft constraints, while less confident regions are sampled from scratch using the motion model and confident regions are only slightly refined.

## Applications in Character Animation

In animation contexts, inpainting can be formulated as an enhancement task where a domain-adapted diffusion model refines masked regions requiring improvement, particularly those involving secondary dynamics.

## Fine-Grained Body Part Control

Some motion diffusion models respond to fine-grained instructions on body parts, enabling multi-level manipulation with arbitrary-length motion synthesis.

These approaches combine diffusion models' generative capabilities with inpainting techniques to enable precise control over human motion generation at both global and local body part levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f0bea6d-5a7e-4b6a-80a0-165bf75cdcdb",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "5c8870c0-1194-4d76-aff8-0daf259aa19e",
  "sourceToolAssistantUUID": "5f0bea6d-5a7e-4b6a-80a0-165bf75cdcdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T20:25:08.584Z_

<details><summary>↩ Tool result · `toolu_01BimT7CdoXQnxiTM32Hxwm7`</summary>

```text
Web search results for query: "body part compositional motion diffusion 2026"

Links: [{"title":"GitHub - kkadry/CardioComposer: [ICLR 2026] CardioComposer: Leveraging Differentiable Geometry for Compositional Control of Anatomical Diffusion Models · GitHub","url":"https://github.com/kkadry/CardioComposer"},{"title":"FrankenMotion: Part-level Human Motion Generation and Composition Chuqiao Li1","url":"https://coral79.github.io/frankenmotion/Files/FrankenMotion.pdf"},{"title":"Human Motion Diffusion Model | OpenReview","url":"https://openreview.net/forum?id=SJ1kSyO2jwu"},{"title":"Wandering and feeling the Scenes: Body-Aware Diffusion for 3D Human Motion Generation | Proceedings of the 7th ACM International Conference on Multimedia in Asia","url":"https://dl.acm.org/doi/10.1145/3743093.3770934"},{"title":"2026-3-16 Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/assets/kimodo_tech_report.pdf"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/"},{"title":"GitHub - GuyTevet/motion-diffusion-model: The official PyTorch implementation of the paper \"Human Motion Diffusion Model\" · GitHub","url":"https://github.com/GuyTevet/motion-diffusion-model"},{"title":"SMooGPT: Stylized Motion Generation using Large Language Models","url":"https://arxiv.org/pdf/2509.04058"},{"title":"GitHub - Zilize/awesome-text-to-motion: Text-driven human motion generation surveys, datasets and models. · GitHub","url":"https://github.com/Zilize/awesome-text-to-motion"},{"title":"MDM: Human Motion Diffusion Model","url":"https://guytevet.github.io/mdm-page/"}]

Based on the search results, here are the key findings related to "body part compositional motion diffusion 2026":

## Recent Research (2026)

Kimodo is an expressive and controllable kinematic motion diffusion model trained on 700 hours of optical motion capture data. The model generates high-quality motions while being easily controlled through text and a comprehensive suite of kinematic constraints including full-body keyframes, sparse joint positions/rotations, 2D waypoints, and dense 2D paths, enabled through a carefully designed motion representation and two-stage denoiser architecture that decomposes root and body prediction.

## Body-Part Compositional Control

Several approaches focus on compositional body-part control for motion generation:

BA-IDM is a body-aware diffusion framework that enables controllable 3D human motion generation within complex scenes. The body-aware subsystem divides the human body into five parts (head, left arm, right arm, spine, and legs), and plays a crucial role in fine-grained control within the whole framework by accurately mapping complex text instructions to specific body parts.

FrankenMotion is a transformer-based diffusion model that can be input conditioned on sequence level prompts, action-level prompts, and part-level prompts.

## Key Developments

The field has seen significant progress in compositional motion generation, with models now supporting:
- Part-level control and decomposition
- Temporal action composition
- Multi-stage diffusion architectures for improved motion quality
- Integration of geometric constraints and spatial reasoning

These advances enable more flexible and precise control over human motion generation compared to earlier approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24feb4a1-0a81-4b13-88fd-9b72946c527d",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "a5274f82-95f2-4bf2-90bb-6ea8adc724f2",
  "sourceToolAssistantUUID": "24feb4a1-0a81-4b13-88fd-9b72946c527d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T20:25:08.845Z_

<details><summary>↩ Tool result · `toolu_01FbyqsBRwZ2bcSnJ5ZwrPyq`</summary>

```text
Web search results for query: "humanoid compositional trajectory generation"

Links: [{"title":"Generative Trajectory Stitching through Diffusion Composition","url":"https://comp-diffuser.github.io/"},{"title":"Generative Trajectory Stitching through Diffusion Composition","url":"https://arxiv.org/html/2503.05153v1"},{"title":"Generative Trajectory Stitching through Diffusion Composition Yunhao Luo1","url":"https://arxiv.org/pdf/2503.05153"},{"title":"Online Free Walking Trajectory Generation for Biped Humanoid Robot KHR-3 (HUBO) - Robotics Institute Carnegie Mellon University","url":"https://publications.ri.cmu.edu/online-free-walking-trajectory-generation-for-biped-humanoid-robot-khr-3-hubo"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"Hierarchical Visuomotor Control in Humanoids","url":"https://www.emergentmind.com/topics/hierarchical-visuomotor-control-of-humanoids"},{"title":"dblp: Analytical Center of Mass Trajectory Generation for Humanoid Walking and Running with Continuous Gait Transitions.","url":"https://dblp.org/rec/conf/humanoids/EgleEO22.html"},{"title":"Real-Time Trajectory Generation for Both Arms of a Humanoid Robot | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-642-37374-9_37"},{"title":"Estimating and Generating Human Motions from Interactions Jinkun Cao","url":"https://www.ri.cmu.edu/app/uploads/2025/09/jinkunc_phd_ri_2025.pdf"},{"title":"Trajectory tracking of single and multiple humanoid robots in cluttered environment - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S2214785321083243"}]

Based on the search results, here's what I found about humanoid compositional trajectory generation:

## CompDiffuser: Generative Trajectory Stitching through Diffusion Composition

CompDiffuser is a generative trajectory stitching method that leverages the compositionality of diffusion models. The method introduces a noise-conditioned score function formulation that helps in performing autoregressive sampling of multiple short-horizon trajectory diffusion models and eventually stitching them to form a longer-horizon goal-conditioned trajectory.

### Key Innovation

CompDiffuser is a novel generative approach that can solve new tasks by learning to compositionally stitch together shorter trajectory chunks from previously seen tasks. The key insight is modeling the trajectory distribution by subdividing it into overlapping chunks and learning their conditional relationships through a single bidirectional diffusion model, which allows information to propagate between segments during generation, ensuring physically consistent connections.

### Application to Humanoids

The method has been tested across benchmark tasks with varying difficulty levels, including different agent state dimensions from 2D point agents to 50D humanoid robots. The evaluation includes various trajectory stitching tasks involving higher-dimensional state spaces such as HumanoidMaze, where maze navigation experiments are conducted using ant and humanoid agents with pre-collected datasets.

### Performance Benefits

CompDiffuser generates long-horizon plans by compositionally sampling a sequence of coherent short trajectory segments while only being trained on short-horizon data, making it efficient for learning complex robot behaviors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09b29de4-a6da-4201-8827-20b4e46e3468",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "dcd6bcf2-f057-485e-9ed8-d533d2f92b40",
  "sourceToolAssistantUUID": "09b29de4-a6da-4201-8827-20b4e46e3468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T20:25:12.902Z_

Good results so far. Let me continue with the next batch of searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd6bcf2-f057-485e-9ed8-d533d2f92b40",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWpvpQtKHspscyyxQmJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6290318-4fb3-4c01-8ad9-c94decc36279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XCJE72AgXKXCeui8Dxzqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3869,
      "cache_read_input_tokens": 10486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3869,
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

_source line 16 · 2026-05-10T20:25:13.848Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PNcrUn1DEYfXGQYUMhomoV`</summary>

```json
{
  "query": "iterative conditional diffusion generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6290318-4fb3-4c01-8ad9-c94decc36279",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWpvpQtKHspscyyxQmJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5837a6a3-3ca4-44a1-a7c6-63e88e7c1082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XCJE72AgXKXCeui8Dxzqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3869,
      "cache_read_input_tokens": 10486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3869,
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

_source line 17 · 2026-05-10T20:25:14.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019az7zGNkhbGhBa27hnzZNK`</summary>

```json
{
  "query": "sequential conditional diffusion composition body parts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5837a6a3-3ca4-44a1-a7c6-63e88e7c1082",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWpvpQtKHspscyyxQmJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c095761-4f40-4e4a-b673-f25f11af413c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XCJE72AgXKXCeui8Dxzqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3869,
      "cache_read_input_tokens": 10486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3869,
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

_source line 18 · 2026-05-10T20:25:14.363Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TPFFeQK4B7NSKZgs8yR6C3`</summary>

```json
{
  "query": "autoregressive diffusion spatial composition motion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c095761-4f40-4e4a-b673-f25f11af413c",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWpvpQtKHspscyyxQmJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4166553f-236f-4a40-8e78-e3e0a8046541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XCJE72AgXKXCeui8Dxzqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3869,
      "cache_read_input_tokens": 10486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3869,
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

_source line 19 · 2026-05-10T20:25:14.898Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012q5fXab5RuJeKh11pd6NfD`</summary>

```json
{
  "query": "robot motion diffusion inpainting 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4166553f-236f-4a40-8e78-e3e0a8046541",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWpvpQtKHspscyyxQmJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "430dd8f6-d384-4a6c-a68f-012c1c16ea39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XCJE72AgXKXCeui8Dxzqt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3869,
      "cache_read_input_tokens": 10486,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3869
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 10486,
          "cache_creation_input_tokens": 3869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3869,
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

_source line 20 · 2026-05-10T20:25:20.740Z_

<details><summary>↩ Tool result · `toolu_01PNcrUn1DEYfXGQYUMhomoV`</summary>

```text
Web search results for query: "iterative conditional diffusion generation 2025 2026"

Links: [{"title":"From Clues to Generation: Language-Guided Conditional Diffusion for Cross-Domain Recommendation","url":"https://arxiv.org/html/2604.05365"},{"title":"Graph Diffusion Evolution Model for Multi-Conditional Molecular Generation | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/10.1145/3774904.3792118"},{"title":"DiffMC‐Gen: A Dual Denoising Diffusion Model for Multi‐Conditional Molecular Generation - Yang - 2025 - Advanced Science - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202417726"},{"title":"Diffusion models for conditional generation of hypothetical new families of superconductors | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-61040-3"},{"title":"Conditional Image Synthesis with Diffusion Models: A Survey","url":"https://arxiv.org/html/2409.19365v3"},{"title":"Implementation of a Conditional Latent Diffusion-Based Generative Model to Synthetically Create Unlabeled Histopathological Images - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12292637/"},{"title":"ADDING CONDITIONAL CONTROL TO DIFFUSION MOD","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8bead340bb510de5c8356f60ca039efc-Paper-Conference.pdf"},{"title":"Target-aware 3D molecular generation based on guided equivariant diffusion | Nature Communications","url":"https://www.nature.com/articles/s41467-025-63245-0"},{"title":"GitHub - moatifbutt/awesome-diffusion-iclr-2025: List of diffusion related active submissions on OpenReview for ICLR 2025. · GitHub","url":"https://github.com/moatifbutt/awesome-diffusion-iclr-2025"},{"title":"Opportunities and challenges of diffusion models for generative AI | National Science Review | Oxford Academic","url":"https://academic.oup.com/nsr/article/11/12/nwae348/7810289"}]

Based on the web search results for "iterative conditional diffusion generation 2025 2026," here are the key findings:

## Recent Research in Conditional Diffusion Generation

GDEM (Graph Diffusion Evolution Model) was proposed for multi-conditional molecule generation, decomposing the process of molecular generation into a chain-like Markov evolution process that continuously adjusts the molecular structure and gradually approaches the true multi-conditional joint distribution.

Diffusion models define a process that gradually introduces noise into the data and then trains neural networks to reverse this degradation through iterative denoising. Denoising diffusion models have demonstrated significant potential in the emergence of various deep learning-based de novo molecular generation algorithms.

## Applications and Methodologies

In the context of conditional generation, images are generally synthesized from Gaussian noise through iterative denoising steps guided by the predictions of a denoising network. DiffGui is a target-conditioned E(3)-equivariant diffusion model that integrates bond diffusion and property guidance.

Guidance allows for the creation of diverse and relevant content across a wide range of applications, and diffusion models with guidance are called conditional diffusion models.

## Challenges and Future Directions

There is a gap between theory and practice for conditional diffusion models, and a theoretical foundation to support principled methodologies for guidance design and adapting diffusion models to task-specific needs is still lacking.

The research in 2025-2026 shows active development in applying iterative conditional diffusion methods across multiple domains including molecular generation, image synthesis, and materials discovery.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5837a6a3-3ca4-44a1-a7c6-63e88e7c1082",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "cdc208b1-cffb-4c2b-aecc-ba6b75e3072b",
  "sourceToolAssistantUUID": "5837a6a3-3ca4-44a1-a7c6-63e88e7c1082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T20:25:21.318Z_

<details><summary>↩ Tool result · `toolu_01TPFFeQK4B7NSKZgs8yR6C3`</summary>

```text
Web search results for query: "autoregressive diffusion spatial composition motion"

Links: [{"title":"MotionStreamer: Streaming Motion Generation via Diffusion-based","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Xiao_MotionStreamer_Streaming_Motion_Generation_via_Diffusion-based_Autoregressive_Model_in_Causal_ICCV_2025_paper.pdf"},{"title":"Diffusion is spectral autoregression – Sander Dieleman","url":"https://sander.ai/2024/09/02/spectral-autoregression.html"},{"title":"sive motion model for real-time text-driven","url":"https://openreview.net/pdf/35852357896bdb17098c35bd7244a9e062f6ce23.pdf"},{"title":"DartControl: A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control","url":"https://zkf1997.github.io/DART/"},{"title":"Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models","url":"https://arxiv.org/html/2409.11920v1"},{"title":"MotionStreamer: Streaming Motion Generation via Diffusion-based Autoregressive Model in Causal Latent Space","url":"https://zju3dv.github.io/MotionStreamer/"},{"title":"AMD: Autoregressive Motion Diffusion","url":"https://www.researchgate.net/publication/379278441_AMD_Autoregressive_Motion_Diffusion"},{"title":"FrankenMotion: Part-level Human Motion Generation and Composition Chuqiao Li1","url":"https://coral79.github.io/frankenmotion/Files/FrankenMotion.pdf"},{"title":"AMD: Autoregressive Motion Diffusion","url":"https://arxiv.org/pdf/2305.09381"},{"title":"[2503.15451] MotionStreamer: Streaming Motion Generation via Diffusion-based Autoregressive Model in Causal Latent Space","url":"https://arxiv.org/abs/2503.15451"}]

Based on the search results, I found several relevant research papers and projects combining autoregressive diffusion models with spatial composition for motion generation:

## Key Research Areas

The literature distinguishes between two types of compositions of human motions: Temporal (two movements executed one after the other) and Spatial (two movements occurring simultaneously).

### Notable Methods

**Motion Composition Diffusion (MCD):** MCD takes a textual annotation describing the movement and decomposes it through GPT into known sub-movements, and during inference processes each sub-movement individually and then combines them based on their respective start and end times.

**DartControl (DART):** DART uses an architecture of autoregressive latent diffusion to learn a motion primitive space jointly conditioned on text prompts and motion history. It enables various motion generation applications with spatial constraints and goals, including motion in-between, waypoint goal reaching, and human-scene interaction generation.

**MotionStreamer:** MotionStreamer incorporates a continuous causal latent space into a probabilistic autoregressive model, where continuous latents mitigate information loss and reduce error accumulation during long-term autoregressive generation. The method supports multi-round generation, long-term generation, and dynamic motion composition.

**Theoretical Perspective:** Diffusion models of images perform approximate autoregression in the frequency domain, suggesting a fundamental connection between these two generative modeling approaches.

These approaches combine the strengths of autoregressive generation (handling variable-length sequences) with diffusion models (high-quality generation) while addressing spatial composition challenges in human motion synthesis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4166553f-236f-4a40-8e78-e3e0a8046541",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "13e20643-d36f-45eb-9846-eeb35d5e9c32",
  "sourceToolAssistantUUID": "4166553f-236f-4a40-8e78-e3e0a8046541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T20:25:22.688Z_

<details><summary>↩ Tool result · `toolu_019az7zGNkhbGhBa27hnzZNK`</summary>

```text
Web search results for query: "sequential conditional diffusion composition body parts"

Links: [{"title":"Reshaping the Human Body With CGI and Stable Diffusion - Metaphysic.ai","url":"https://blog.metaphysic.ai/reshaping-the-human-body-with-cgi-and-stable-diffusion/"},{"title":"Using prompts to modify face and body in Stable Diffusion XL","url":"https://dav.one/using-prompts-to-modify-face-and-body-in-stable-diffusion-xl/"},{"title":"Compositional Visual Generation with Composable Diffusion Models","url":"https://energy-based-model.github.io/Compositional-Visual-Generation-with-Composable-Diffusion-Models/"},{"title":"Dual Conditional Diffusion Models for Sequential Recommendation","url":"https://arxiv.org/html/2410.21967"},{"title":"Using prompts to modify face and body in Stable Diffusion 1.5","url":"https://dav.one/using-prompts-to-modify-face-and-body-in-stable-diffusion-15/"},{"title":"GitHub - energy-based-model/Compositional-Visual-Generation-with-Composable-Diffusion-Models-PyTorch: [ECCV 2022] Compositional Generation using Diffusion Models · GitHub","url":"https://github.com/energy-based-model/Compositional-Visual-Generation-with-Composable-Diffusion-Models-PyTorch"},{"title":"Different ways to condition the diffusion model (conditional diffusion model) | by Jonghwa Yim | Medium","url":"https://jonhwayim.medium.com/different-ways-to-condition-the-diffusion-model-d2e41eaa01c2"},{"title":"Attention Interpolation for Text-to-Image Diffusion Qiyuan He1 Jinghao Wang2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/b12a1d1014e952e676f5d6931d03241a-Paper-Conference.pdf"},{"title":"Conditional Denoising Diffusion for Sequential Recommendation | Advances in Knowledge Discovery and Data Mining","url":"https://dl.acm.org/doi/10.1007/978-981-97-2262-4_13"},{"title":"Conditional diffusion model for inverse prediction of process parameters and dendritic microstructures from mechanical properties | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-22942-y"}]

Based on the search results, I found several relevant topics related to your query about sequential conditional diffusion and composition of body parts:

## Compositional Visual Generation with Diffusion Models

Compositional diffusion models can be trained to generate images conditioned on a single human facial attribute, and during inference, can recursively compose multiple facial attributes using compositional operators. The model generates individual images conditioned on single descriptions, and then composes them together to create combined results.

## Body Part Specification in Diffusion Models

Stable Diffusion understands the body types and body parts. Users can specify individual body parts precisely, such as wide hips, narrow waist, large breasts, and other features.

## Conditional Mechanisms in Diffusion Models

Latent Diffusion Models introduced sophisticated cross-attention mechanisms that allow the model to selectively focus on relevant parts of the conditional input, enabling capture of more nuanced relationships between the input and generated output.

## Sequential Application

Image-to-image translation can be used to modify fine details of initial coarse images produced earlier in the workflow, inspired by the Stochastic Differential Editing (SDEdit) framework. Separate refinement modules can be applied to address shortcomings in rendering of the entire body and improve depiction of the face.

These techniques enable sequential and compositional approaches to generating complex images with specific body part attributes through conditional diffusion models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c095761-4f40-4e4a-b673-f25f11af413c",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "5f765688-e3b2-48d3-a295-353dde22a82c",
  "sourceToolAssistantUUID": "3c095761-4f40-4e4a-b673-f25f11af413c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T20:25:25.334Z_

<details><summary>↩ Tool result · `toolu_012q5fXab5RuJeKh11pd6NfD`</summary>

```text
Web search results for query: "robot motion diffusion inpainting 2025 2026"

Links: [{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"Diffusion Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2504.08438v3"},{"title":"GitHub - mbreuss/diffusion-literature-for-robotics: Summary of key papers and blogs about diffusion models to learn about the topic. Detailed list of all published diffusion robotics papers. · GitHub","url":"https://github.com/mbreuss/diffusion-literature-for-robotics"},{"title":"MDM: Human Motion Diffusion Model","url":"https://guytevet.github.io/mdm-page/"},{"title":"GitHub - moatifbutt/awesome-diffusion-iclr-2025: List of diffusion related active submissions on OpenReview for ICLR 2025. · GitHub","url":"https://github.com/moatifbutt/awesome-diffusion-iclr-2025"},{"title":"GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub","url":"https://github.com/YanjieZe/Paper-List"},{"title":"OmniPainter: Global-Local Temporally Consistent Video Inpainting Diffusion Model | OpenReview","url":"https://openreview.net/forum?id=NMKVz3hQfz"},{"title":"[2509.13214] End4: End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection","url":"https://arxiv.org/abs/2509.13214"}]

I've found recent research on robot motion, diffusion models, and inpainting. Here are the key findings:

## Diffusion Models for Robot Motion

Diffusion models have recently emerged as a promising approach in robotics, especially in robot manipulations. Diffusion models leverage a probabilistic framework, and they stand out with their ability to model multi-modal distributions and their robustness to high-dimensional input and output spaces.

## Inpainting Conditioning

Janner et al. (2022) formulates conditioning as inpainting, where during inferences at each denoising step, specific states from the currently being generated sample are replaced with states from the condition. This approach has become an important technique in robot motion planning.

## Recent Applications and Advances (2025-2026)

The research shows several recent developments:

- Many methods adopt using RGB inputs, also developing more intricate encoding schemes (Qi et al., 2025).

- Another example of an additional input modality could be natural language (Ke et al., 2024; Du et al., 2023; Li et al., 2025), which also enables the integration of foundation models, like large language models, into the workflow.

- A comprehensive survey on "Diffusion models for robotic manipulation" was published in 2025, covering grasp learning, trajectory planning, and data augmentation applications.

These developments highlight the growing importance of diffusion-based approaches for generating robot motions while maintaining temporal consistency through techniques like inpainting-based conditioning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "430dd8f6-d384-4a6c-a68f-012c1c16ea39",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "3b378745-5bf6-403f-b2a1-3193850ed4e2",
  "sourceToolAssistantUUID": "430dd8f6-d384-4a6c-a68f-012c1c16ea39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T20:25:26.945Z_

Now let me search for the remaining topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b378745-5bf6-403f-b2a1-3193850ed4e2",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWr9PEx1gMUr7QttkMz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5942061-70a2-412d-8aaf-eed1ff2fea96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsUW4j6iXCRVC47xmDLmgT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4054,
      "cache_read_input_tokens": 14355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4054,
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

_source line 25 · 2026-05-10T20:25:27.428Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MyFqkqPMZFME6o7QyTjKPg`</summary>

```json
{
  "query": "masked robot trajectory diffusion planning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5942061-70a2-412d-8aaf-eed1ff2fea96",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWr9PEx1gMUr7QttkMz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39a385e2-6dd1-45be-9202-8e11f7a2347c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsUW4j6iXCRVC47xmDLmgT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4054,
      "cache_read_input_tokens": 14355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4054,
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

_source line 26 · 2026-05-10T20:25:27.902Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SfCRagjy1uH2U1gkrdrX4Q`</summary>

```json
{
  "query": "constraint conditioning diffusion robot locomotion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39a385e2-6dd1-45be-9202-8e11f7a2347c",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWr9PEx1gMUr7QttkMz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a759a60-1f53-4e20-819d-60ca9dabb344",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsUW4j6iXCRVC47xmDLmgT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4054,
      "cache_read_input_tokens": 14355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4054,
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

_source line 27 · 2026-05-10T20:25:28.939Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BwwUMSzFzD7UdsyrEHTkbQ`</summary>

```json
{
  "query": "Kimodo NVIDIA motion generation March 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a759a60-1f53-4e20-819d-60ca9dabb344",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWr9PEx1gMUr7QttkMz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "354589e3-effd-475f-a1d6-3a8b6aeda658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsUW4j6iXCRVC47xmDLmgT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4054,
      "cache_read_input_tokens": 14355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4054,
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

_source line 28 · 2026-05-10T20:25:29.113Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DqS4Lj54dMFGzdmGNJQyUa`</summary>

```json
{
  "query": "BONES-SEED diffusion motion generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "354589e3-effd-475f-a1d6-3a8b6aeda658",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWr9PEx1gMUr7QttkMz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a228f53d-1bcc-432c-8d3d-c56e9f82eaf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsUW4j6iXCRVC47xmDLmgT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4054,
      "cache_read_input_tokens": 14355,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4054
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 14355,
          "cache_creation_input_tokens": 4054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4054,
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

_source line 29 · 2026-05-10T20:25:33.497Z_

<details><summary>↩ Tool result · `toolu_01MyFqkqPMZFME6o7QyTjKPg`</summary>

```text
Web search results for query: "masked robot trajectory diffusion planning"

Links: [{"title":"GitHub - mbreuss/diffusion-literature-for-robotics: Summary of key papers and blogs about diffusion models to learn about the topic. Detailed list of all published diffusion robotics papers. · GitHub","url":"https://github.com/mbreuss/diffusion-literature-for-robotics"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"Diffusion Trajectory-guided Policy for Long-horizon Robot Manipulation","url":"https://arxiv.org/html/2502.10040v1"},{"title":"[2308.01557] Motion Planning Diffusion: Learning and Planning of Robot Motions with Diffusion Models","url":"https://arxiv.org/abs/2308.01557"},{"title":"Diffusion Trajectory-guided Policy for Long-horizon Robot Manipulation","url":"https://diffusion-trajectory-guided-policy.github.io/"},{"title":"Learning and Planning of Robot Motions with Diffusion ...","url":"https://sites.google.com/view/mp-diffusion"},{"title":"Motion Planning Diffusion: Learning and Planning of Robot Motions with Diffusion Models","url":"https://arxiv.org/html/2308.01557v2"},{"title":"Multi-Robot Motion Planning with Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=AUCYptvAf3"},{"title":"Any-point Trajectory Modeling for Policy Learning","url":"https://www.roboticsproceedings.org/rss20/p092.pdf"},{"title":"Diffusion Trajectory-guided Policy: A Novel Framework for Long-Horizon Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=VaoeAi5CW8"}]

Based on the web search results, here's an overview of research in masked robot trajectory diffusion planning:

## Key Research Areas

Notable papers include "NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration", which represents one approach to masked diffusion-based planning.

## Main Approaches

**Diffusion Trajectory-guided Policy (DTP)**: The DTP framework generates 2D trajectories through a diffusion model to guide policy learning for long-horizon tasks, providing trajectory-level guidance to reduce error accumulation through a two-stage approach that first trains a generative vision-language model to create diffusion-based trajectories, then refines the imitation policy using them.

**Motion Planning Diffusion**: Learning priors on trajectory distributions can help accelerate robot motion planning optimization, and diffusion has been shown to effectively encode data multimodality in high-dimensional settings, which is particularly well-suited for large trajectory datasets.

## Applications

Methods exist for generating collision-free multi-robot trajectories that conform to underlying data distributions, combining learned diffusion models with classical search-based techniques to generate data-driven motions under collision constraints.

The field encompasses trajectory generation for robot manipulation, navigation, motion planning, and multi-robot coordination using diffusion-based generative models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39a385e2-6dd1-45be-9202-8e11f7a2347c",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "3f52b9c7-2f26-462a-a363-3623db5f1e35",
  "sourceToolAssistantUUID": "39a385e2-6dd1-45be-9202-8e11f7a2347c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T20:25:35.978Z_

<details><summary>↩ Tool result · `toolu_01BwwUMSzFzD7UdsyrEHTkbQ`</summary>

```text
Web search results for query: "Kimodo NVIDIA motion generation March 2026"

Links: [{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/"},{"title":"GitHub - nv-tlabs/kimodo: Official implementation of Kimodo, a kinematic motion diffusion model for high-quality human(oid) motion generation. · GitHub","url":"https://github.com/nv-tlabs/kimodo"},{"title":"Kimodo: Scaling Controllable Human Motion Generation | DAIR @ NVIDIA Research","url":"https://research.nvidia.com/labs/dair/publication/kimodo2026/"},{"title":"2026-3-16 Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/assets/kimodo_tech_report.pdf"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://arxiv.org/html/2603.15546v1"},{"title":"NVIDIA Kimodo Text-to-Motion: Open Code, Closed Data — What It Means for Robotics | Pebblous","url":"https://blog.pebblous.ai/blog/kimodo-text-to-motion/en/"},{"title":"nvidia/Kimodo-SOMA-RP-v1 · Hugging Face","url":"https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1"},{"title":"Kimodo: Scaling Controllable Human Motion Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260315546R/abstract"},{"title":"Quick Start — Kimodo","url":"https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html"},{"title":"NVIDIA’s Kimodo generates studio-quality 3D motion from text, and it’s free - Efficienist","url":"https://efficienist.com/nvidias-kimodo-generates-studio-quality-3d-motion-from-text-and-its-free/"}]

Based on the search results, here's what I found about Kimodo NVIDIA motion generation from March 2026:

## Overview

Kimodo is an expressive and controllable kinematic motion diffusion model trained on 700 hours of optical motion capture data. The initial open-source release of Kimodo occurred on March 16, 2026, with five model variants (SOMA, G1, SMPL-X), CLI, interactive demo, and timeline annotations for BONES-SEED.

## Key Features

Kimodo is controlled through text and constraints to generate high-quality 3D human and robot motions. Kimodo supports flexible and intuitive control for motion generation through text prompting combined with an extensive suite of kinematic constraints, and by training on 700 hours of optical mocap data, the model achieves precise control accuracy for a large variety of behaviors.

## Technical Capabilities

On an NVIDIA RTX 3090, generating a motion from a single prompt takes anywhere from 2 to 5 seconds, depending on the specified duration. The Bones Rigplay dataset is a large studio mocap dataset containing over 700 hours of production-quality human motion with corresponding text descriptions.

## Model Variants

Multiple model variants were released including Kimodo-SOMA-RP-v1, Kimodo-G1-RP-v1, Kimodo-SOMA-SEED-v1, Kimodo-G1-SEED-v1, and Kimodo-SMPLX-RP-v1, all released on March 16, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "354589e3-effd-475f-a1d6-3a8b6aeda658",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "6843c6b6-3cf0-40b2-969e-4fafaae0cdfd",
  "sourceToolAssistantUUID": "354589e3-effd-475f-a1d6-3a8b6aeda658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T20:25:36.451Z_

<details><summary>↩ Tool result · `toolu_01DqS4Lj54dMFGzdmGNJQyUa`</summary>

```text
Web search results for query: "BONES-SEED diffusion motion generation"

Links: [{"title":"GitHub - nv-tlabs/kimodo: Official implementation of Kimodo, a kinematic motion diffusion model for high-quality human(oid) motion generation. · GitHub","url":"https://github.com/nv-tlabs/kimodo"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/"},{"title":"bones-studio/seed · Datasets at Hugging Face","url":"https://huggingface.co/datasets/bones-studio/seed"},{"title":"DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning","url":"https://arxiv.org/html/2410.16727v1"},{"title":"DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning","url":"https://diffusion-seeder.github.io/"},{"title":"Morphological Computation in Plant Seeds for a New Generation of Self-Burial and Flying Soft Robots - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/34901173/"},{"title":"Bones Studio to Release BONES-SEED - the First Multimodal Motion Dataset Purpose-Built for Humanoid Robotics","url":"https://www.prweb.com/releases/bones-studio-to-release-bones-seed---the-first-multimodal-motion-dataset-purpose-built-for-humanoid-robotics-302714306.html"},{"title":"Bones Studio to Release BONES-SEED - the First Multimodal Motion Dataset Purpose-Built for Humanoid Robotics | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/03/17/bones-studio-to-release-bones-seed-the-first-multimodal-motion-dataset-purpose-built-for-humanoid-robotics/26276/"},{"title":"Bones Studio unveils BONES-SEED humanoid motion dataset | NVDA Stock News","url":"https://www.stocktitan.net/news/NVDA/bones-studio-to-release-bones-seed-the-first-multimodal-motion-fklduqdwfkkn.html"},{"title":"AI Datasets - Bones Seed | Bones Studio","url":"https://bones.studio/datasets/seed"}]

Based on the search results, here's what I found about BONES-SEED and diffusion motion generation:

## BONES-SEED Dataset

BONES-SEED (Skeletal Everyday Embodiment Dataset) is an open dataset of 142,220 annotated human motion animations for humanoid robotics. It provides motion capture data in SOMA and Unitree G1 formats, with natural language descriptions, temporal segmentation, and detailed skeletal metadata.

Each motion in BONES-SEED comes with rich multimodal annotations designed for language-conditioned policy learning, motion retrieval, and motion generation. The dataset spans locomotion and everyday activities to object interactions and complex whole-body behaviors, all curated specifically for humanoid robotics applications.

## Diffusion-Based Motion Generation with BONES-SEED

The BONES-SEED dataset is used to train motion diffusion models, most notably **Kimodo**. Kimodo is a kinematic motion diffusion model trained on large-scale optical mocap data. It is controlled through text and constraints to generate high-quality 3D human and robot motions.

Kimodo is an expressive and controllable kinematic motion diffusion model trained on 700 hours of optical motion capture data. The model generates high-quality motions while being easily controlled through text and a comprehensive suite of kinematic constraints including full-body keyframes, sparse joint positions/rotations, 2D waypoints, and dense 2D paths.

Models trained on BONES-SEED use 288 hours of publicly available mocap data so are less capable, but are useful for comparing to other models trained on BONES-SEED.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a228f53d-1bcc-432c-8d3d-c56e9f82eaf0",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "5f73b5fe-4ef3-4c25-8f93-5c9150842c87",
  "sourceToolAssistantUUID": "a228f53d-1bcc-432c-8d3d-c56e9f82eaf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T20:25:38.709Z_

<details><summary>↩ Tool result · `toolu_01SfCRagjy1uH2U1gkrdrX4Q`</summary>

```text
Web search results for query: "constraint conditioning diffusion robot locomotion"

Links: [{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion Predictive Control with Constraints","url":"https://arxiv.org/html/2412.09342"},{"title":"Constraint-Aware Diffusion Guidance for Robotics: Real-Time Obstacle Avoidance for Autonomous Racing","url":"https://arxiv.org/html/2505.13131"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"[2505.13131] Constraint-Aware Diffusion Guidance for Robotics: Real-Time Obstacle Avoidance for Autonomous Racing","url":"https://arxiv.org/abs/2505.13131"},{"title":"Constraint-Aware Diffusion Guidance for Robotics: Real-Time Obstacle Avoidance for Autonomous Racing | Request PDF","url":"https://www.researchgate.net/publication/391911828_Constraint-Aware_Diffusion_Guidance_for_Robotics_Real-Time_Obstacle_Avoidance_for_Autonomous_Racing"},{"title":"Learning Diverse Robot Striking Motions with Diffusion Models and Kinematically Constrained Gradient Guidance","url":"https://arxiv.org/html/2409.15528v1"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"3D Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss20/p067.pdf"},{"title":"(PDF) Constrained Skill Discovery: Quadruped Locomotion with Unsupervised Reinforcement Learning","url":"https://www.researchgate.net/publication/384811811_Constrained_Skill_Discovery_Quadruped_Locomotion_with_Unsupervised_Reinforcement_Learning"}]

Based on the search results, here's what I found about constraint conditioning in diffusion models for robotics:

## Key Research Areas

**Constraint-Aware Diffusion Guidance (CoDiG):** CoDiG is a data-efficient and general-purpose framework that integrates barrier functions into the denoising process, guiding diffusion sampling toward constraint-satisfying outputs. This framework has been evaluated in miniature autonomous racing where real-time obstacle avoidance is essential, with real-world experiments showing that CoDiG generates safe outputs efficiently under dynamic conditions.

**Diffusion Predictive Control with Constraints:** Incorporating model-based projections into the trajectory denoising process allows sampling future trajectories that are constraint-satisfying, dynamically feasible, and suitable for solving learned tasks.

**General Constraint Handling in Robotics:** Classifier-free guidance has been introduced where a conditional and an unconditional diffusion model per constraint are trained in parallel, allowing for arbitrary combinations of constraints not seen together during training, though it does not generalize to entirely new constraints.

**Kinematically Constrained Approaches:** Research has formulated methods for guiding diffusion samples towards kinematics constraints using techniques inspired by inverse problems, which enables constraints to be better incorporated into the resulting diffusion samples.

**Quadrupedal Locomotion:** Recent work presents a diffusion-based approach to quadrupedal locomotion that simultaneously addresses the limitations of learning and interpolating between multiple skills and of offline adapting to new locomotion behaviors after training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a759a60-1f53-4e20-819d-60ca9dabb344",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "4c0b456f-d8be-4b41-871c-db5d5a5d3b50",
  "sourceToolAssistantUUID": "6a759a60-1f53-4e20-819d-60ca9dabb344",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T20:25:40.830Z_

Good. Now let me search for the remaining topics and some more specific queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c0b456f-d8be-4b41-871c-db5d5a5d3b50",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWs8WSEddXg2Rye8M5Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed7bed2a-eb59-49d0-80e3-9f1903b275af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtBYUWMsargtiHjmquM8de",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1937,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 18409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1991,
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

_source line 34 · 2026-05-10T20:25:41.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BrkFUF1zaBQohg6pXcVpL`</summary>

```json
{
  "query": "G1 humanoid diffusion motion policy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed7bed2a-eb59-49d0-80e3-9f1903b275af",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWs8WSEddXg2Rye8M5Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68cb4657-2901-4dd4-8131-980cfea6dddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtBYUWMsargtiHjmquM8de",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1937,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 18409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1991,
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

_source line 35 · 2026-05-10T20:25:41.841Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SkgFhiSLySL9ZjJuz2bS1R`</summary>

```json
{
  "query": "humanoid data generation diffusion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68cb4657-2901-4dd4-8131-980cfea6dddb",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWs8WSEddXg2Rye8M5Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b49e6f6e-0dbc-47ad-8f44-539d3b66c4e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtBYUWMsargtiHjmquM8de",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1937,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 18409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1991,
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

_source line 36 · 2026-05-10T20:25:42.367Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GNCHScuwF9gS22kpHtmL83`</summary>

```json
{
  "query": "synthetic humanoid training data diffusion motion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b49e6f6e-0dbc-47ad-8f44-539d3b66c4e1",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWs8WSEddXg2Rye8M5Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8946e7c-cf85-498b-9ca5-749bd8f13f6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtBYUWMsargtiHjmquM8de",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1937,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 18409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1991,
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

_source line 37 · 2026-05-10T20:25:42.973Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VFZuddjTd4hsGPyHvXf44D`</summary>

```json
{
  "query": "FrankenMotion part-level human motion generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8946e7c-cf85-498b-9ca5-749bd8f13f6e",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWs8WSEddXg2Rye8M5Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c7a0424-f51b-4753-8bc0-728740225f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtBYUWMsargtiHjmquM8de",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1937,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 18409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1991,
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

_source line 38 · 2026-05-10T20:25:49.057Z_

<details><summary>↩ Tool result · `toolu_016BrkFUF1zaBQohg6pXcVpL`</summary>

```text
Web search results for query: "G1 humanoid diffusion motion policy 2026"

Links: [{"title":"GitHub - nv-tlabs/kimodo: Official implementation of Kimodo, a kinematic motion diffusion model for high-quality human(oid) motion generation. · GitHub","url":"https://github.com/nv-tlabs/kimodo"},{"title":"From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance | OpenReview","url":"https://openreview.net/forum?id=k3Cyx3Uets"},{"title":"Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"},{"title":"BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion","url":"https://arxiv.org/html/2508.08241v1"},{"title":"Humanoid Robot Comparison 2026: OpenArm vs Mobile ALOHA vs Unitree G1 | SVRC","url":"https://www.roboticscenter.ai/blog/humanoid-robot-comparison-2026"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"Generalizable Humanoid Manipulation with 3D Diffusion Policies | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11246340/"},{"title":"RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting","url":"https://arxiv.org/html/2604.21355"},{"title":"PHUMA: PHYSICALLY-GROUNDED HUMANOID ...","url":"https://openreview.net/pdf/a36747cac87a488230dfe8cb6d5c0aa5a6db82d7.pdf"},{"title":"The Code Is Open. The Data Isn't. — NVIDIA Kimodo and the Humanoid Motion Data Race","url":"https://blog.pebblous.ai/blog/kimodo-text-to-motion/en/"}]

Based on the search results, here's what I found about G1 humanoid diffusion motion policy research and developments in 2026:

## Key Projects and Research

**Kimodo - NVIDIA's Text-to-Motion System:**
An open-source release of Kimodo occurred on March 16, 2026, with five model variants including G1, CLI, interactive demo, and timeline annotations. Kimodo is a kinematic motion diffusion model for high-quality human(oid) motion generation. Kimodo generates full-body Unitree G1 motion from plain English in 2–5 seconds, with the model being open-source while the 700 hours of motion capture data that power it are not.

**Motion Tracking and Control Frameworks:**
BeyondMimic is the first real-world framework to learn from human motions for versatile and naturalistic humanoid control via guided diffusion, providing a motion tracking pipeline capable of challenging skills such as jumping spins, sprinting, and cartwheels.

**Terrain-Aware Locomotion:**
A whole-body humanoid locomotion framework combines skills learned from reference motions with terrain-aware adaptation, training a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions and a whole-body reference tracker with RL.

**Multi-Skill Integration:**
RPG (Robust Policy Gating) is a hybrid expert policy framework for smooth and stable humanoid multi-skills transition that incorporates motion transition randomization and temporal randomization to train a unified policy.

These projects demonstrate significant progress in using diffusion models for motion generation and control on the Unitree G1 humanoid robot platform in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68cb4657-2901-4dd4-8131-980cfea6dddb",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "0aac7fa9-b68d-4c47-a87d-a8b7c3259d98",
  "sourceToolAssistantUUID": "68cb4657-2901-4dd4-8131-980cfea6dddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T20:25:49.215Z_

<details><summary>↩ Tool result · `toolu_01SkgFhiSLySL9ZjJuz2bS1R`</summary>

```text
Web search results for query: "humanoid data generation diffusion 2026"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"What Is Stable Diffusion? The 2026 Complete Guide","url":"https://www.articsledge.com/post/stable-diffusion"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=Mk9ykil8eP"},{"title":"FlowAct-R1: Towards Interactive Humanoid Video Generation","url":"https://arxiv.org/html/2601.10103v1"},{"title":"Humanoid data: 10 Things That Matter in AI Right Now | MIT Technology Review","url":"https://www.technologyreview.com/2026/04/21/1135656/humanoid-data-robot-training-ai-artificial-intelligence/"},{"title":"Humanoid robots 2026: The convergence moment | Roland Berger","url":"https://www.rolandberger.com/en/Insights/Publications/Humanoid-robots-why-the-convergence-moment-is-now.html"},{"title":"[2604.17335] Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/abs/2604.17335"},{"title":"Generalizable Humanoid Manipulation with 3D Diffusion Policies Yanjie Ze1","url":"https://humanoid-manipulation.github.io/assets/paper.pdf"},{"title":"Humanoid data: 10 Things That Matter in AI Right Now","url":"https://www.technologyreview.com/2026/04/21/1135656/humanoid-data-robot-training-ai-artificial-intelligence/amp/"}]

Based on the search results, here are the key findings related to humanoid data generation and diffusion models in 2026:

## Data Generation Approaches

HumanoidGen is an automated task creation and demonstration collection framework that leverages atomic dexterous skills and LLM reasoning to generate relational constraints. The results show that the performance of 2D and 3D diffusion policies can scale with the generated dataset.

## Motion Generation with Diffusion

Researchers are combining diffusion-based motion generation with RL-based motion tracking to repurpose coordinated human whole-body skills learned from motion data for perceptive humanoid locomotion. One approach trains a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions, while concurrently training a whole-body reference tracker with RL using this motion data.

## Interactive Video Generation

Interactive humanoid video generation aims to synthesize lifelike visual agents that can engage with humans through continuous and responsive video, with frameworks like FlowAct-R1 designed specifically for real-time interactive humanoid video generation.

## Data Collection Challenges

The bottleneck in humanoid robotics is training data. As venture capital money poured into robotics—$6.1 billion in 2025 for humanoids alone—there are now training centers in China where people wear exoskeletons and virtual-reality hardware while doing repetitive tasks hundreds of times per day, and gig workers in Nigeria, Argentina, and India are filming themselves doing chores at home.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b49e6f6e-0dbc-47ad-8f44-539d3b66c4e1",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "2dd58773-779d-4e81-9656-66145df692df",
  "sourceToolAssistantUUID": "b49e6f6e-0dbc-47ad-8f44-539d3b66c4e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T20:25:50.514Z_

<details><summary>↩ Tool result · `toolu_01VFZuddjTd4hsGPyHvXf44D`</summary>

```text
Web search results for query: "FrankenMotion part-level human motion generation"

Links: [{"title":"FrankenMotion","url":"https://coral79.github.io/frankenmotion/"},{"title":"[2601.10909] FrankenMotion: Part-level Human Motion Generation and Composition","url":"https://arxiv.org/abs/2601.10909"},{"title":"FrankenMotion: Part-level Human Motion Generation and Composition Chuqiao Li1","url":"https://coral79.github.io/frankenmotion/Files/FrankenMotion.pdf"},{"title":"FrankenMotion: Part-level Human Motion Generation and Composition","url":"https://arxiv.org/html/2601.10909v1"},{"title":"GitHub - Coral79/FrankenMotion-Code: [arXiv 2026] FrankenMotion: Part-level Human Motion Generation and Composition","url":"https://github.com/Coral79/FrankenMotion-Code"},{"title":"Human Motion Generation: A Survey | Request PDF","url":"https://www.researchgate.net/publication/375493854_Human_Motion_Generation_A_Survey"},{"title":"MotionLLM: Understanding Human Behaviors from Human Motions and Videos | Request PDF","url":"https://www.researchgate.net/publication/397120370_MotionLLM_Understanding_Human_Behaviors_from_Human_Motions_and_Videos"},{"title":"Part-level Human Motion Generation and Composition","url":"https://www.researchgate.net/publication/399876146_FrankenMotion_Part-level_Human_Motion_Generation_and_Composition"},{"title":"video-generation-survey/virtual_human.md at main · yzhang2016/video-generation-survey","url":"https://github.com/yzhang2016/video-generation-survey/blob/main/virtual_human.md"},{"title":"FrankenMotion - Part-Level Human Motion Generation and ...","url":"https://www.scribd.com/document/998929005/FrankenMotion-Part-level-Human-Motion-Generation-and-Composition"}]

Based on the search results, here's an overview of FrankenMotion:

## Overview

FrankenMotion is a diffusion-based part-aware motion generation framework where each body part is guided by its own temporally-structured textual prompt.

## Key Problem It Addresses

Existing methods primarily rely on either sequence-level or action-level descriptions due to the absence of fine-grained, part-level motion annotations, which limits their controllability over individual body parts.

## Approach

The work constructs a high-quality motion dataset with atomic, temporally-aware part-level text annotations, leveraging large language models (LLMs), with a dataset that captures asynchronous and semantically distinct part movements at fine temporal resolution.

The model is a transformer-based diffusion model that can be input conditioned on sequence level prompt, action-level prompt and part-level prompt.

## Key Capabilities

This is the first work to provide atomic, temporally-aware part-level motion annotations and have a model that allows motion generation with both spatial (body part) and temporal (atomic action) control.

Experiments demonstrate that FrankenMotion outperforms all previous baseline models adapted and retrained for the setting, and the model can compose motions unseen during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c7a0424-f51b-4753-8bc0-728740225f48",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "3ea540a0-b7a1-4cbd-83bc-96ca314a2215",
  "sourceToolAssistantUUID": "4c7a0424-f51b-4753-8bc0-728740225f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T20:25:50.600Z_

<details><summary>↩ Tool result · `toolu_01GNCHScuwF9gS22kpHtmL83`</summary>

```text
Web search results for query: "synthetic humanoid training data diffusion motion"

Links: [{"title":"Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"},{"title":"2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf"},{"title":"GitHub - nv-tlabs/kimodo: Official implementation of Kimodo, a kinematic motion diffusion model for high-quality human(oid) motion generation. · GitHub","url":"https://github.com/nv-tlabs/kimodo"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/"},{"title":"The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control | OpenReview","url":"https://openreview.net/forum?id=ahx1zNx3GE"},{"title":"The Role of Domain Randomization in Training Diffusion ...","url":"https://arxiv.org/pdf/2411.01349"},{"title":"The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control","url":"https://arxiv.org/html/2411.01349"},{"title":"GitHub - YanjieZe/3D-Diffusion-Policy: [RSS 2024] 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations · GitHub","url":"https://github.com/YanjieZe/3D-Diffusion-Policy"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"Shape‐Conditioned Human Motion Diffusion Model with Mesh Representation - Xue - 2025 - Computer Graphics Forum - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/cgf.70065?af=R"}]

Based on the search results, here's what I found about synthetic humanoid training data diffusion motion:

## Overview

The search results reveal several key developments in using diffusion models for synthetic humanoid motion generation and training:

### Synthetic Motion Generation Pipelines

NVIDIA's approach uses spatial computing devices to record motion demonstrations by teleoperating simulated robots, then uses these recordings to generate larger sets of physically accurate synthetic motion trajectories and produces exponentially large, photorealistic, and diverse sets of training data. NVIDIA was able to generate 780K synthetic trajectories in 11 hours, equivalent to 6.5K hours of human demonstration data, and improved GR00T N1 performance by 40% when combined with real data.

### GR00T N1 Foundation Model

GR00T N1 is a Vision-Language-Action (VLA) model with a dual-system architecture where a diffusion transformer module (System 1) generates fluid motor actions in real time. The model is trained with a heterogeneous mixture of real-robot trajectories, human videos, and synthetically generated datasets.

### Kimodo Motion Diffusion Model

Kimodo is a kinematic motion diffusion model trained on a large-scale (700 hours) commercially-friendly optical motion capture dataset that generates high-quality 3D human and robot motions, controlled through text prompts and constraints such as full-body pose keyframes, end-effector positions/rotations, 2D paths, and 2D waypoints.

### Diffusion Policies for Humanoid Control

Synthetic demonstrations can be generated by training Adversarial Motion Prior (AMP) agents under various Domain Randomization conditions, and successful training of locomotion policies requires significantly larger and more diverse datasets compared to manipulation tasks.

These developments represent a growing field combining diffusion models with synthetic data generation to train more capable humanoid robots.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8946e7c-cf85-498b-9ca5-749bd8f13f6e",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "6604e4f6-b1f5-4102-a9a2-13ed9b827498",
  "sourceToolAssistantUUID": "d8946e7c-cf85-498b-9ca5-749bd8f13f6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T20:25:53.851Z_

Excellent finds. Let me continue with more targeted searches for closely related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6604e4f6-b1f5-4102-a9a2-13ed9b827498",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWt1Qa1smi7Dm3TXH2p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c732374-e4d7-40e0-be11-4d52c6e9250e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWP6QWwRtERQXJ14NoXyCX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 5107,
      "cache_read_input_tokens": 20400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5107,
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

_source line 43 · 2026-05-10T20:25:54.869Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PiqU47vPX41euXPUtE5ALc`</summary>

```json
{
  "query": "EnergyMoGen compositional motion generation energy diffusion CVPR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c732374-e4d7-40e0-be11-4d52c6e9250e",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWt1Qa1smi7Dm3TXH2p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75d866cc-19d4-42a8-b356-560dadc41fbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWP6QWwRtERQXJ14NoXyCX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 5107,
      "cache_read_input_tokens": 20400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5107,
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

_source line 44 · 2026-05-10T20:25:55.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bme5PpkoRQxuNrk1oFpvRY`</summary>

```json
{
  "query": "BeyondMimic humanoid guided diffusion 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75d866cc-19d4-42a8-b356-560dadc41fbb",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWt1Qa1smi7Dm3TXH2p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a3f32a5-4adc-4a08-99cc-b2cb3d85c523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWP6QWwRtERQXJ14NoXyCX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 5107,
      "cache_read_input_tokens": 20400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5107,
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

_source line 45 · 2026-05-10T20:25:56.308Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ucZrpjxRg1NwHuHRopiU7`</summary>

```json
{
  "query": "motion diffusion inpainting body joint masking conditioning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a3f32a5-4adc-4a08-99cc-b2cb3d85c523",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWt1Qa1smi7Dm3TXH2p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e033e9c-fee0-4546-a484-321ecd78bd3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWP6QWwRtERQXJ14NoXyCX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 5107,
      "cache_read_input_tokens": 20400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5107,
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

_source line 46 · 2026-05-10T20:25:56.696Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AnM433GsCWsb8VBnLtzy9H`</summary>

```json
{
  "query": "DiffusionSeeder robot motion planning diffusion 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e033e9c-fee0-4546-a484-321ecd78bd3b",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWt1Qa1smi7Dm3TXH2p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "390a9aff-80ea-4d05-babf-c1222ee9d2ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWP6QWwRtERQXJ14NoXyCX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 5107,
      "cache_read_input_tokens": 20400,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5107
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 851,
          "output_tokens": 228,
          "cache_read_input_tokens": 20400,
          "cache_creation_input_tokens": 5107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5107,
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

_source line 47 · 2026-05-10T20:26:01.988Z_

<details><summary>↩ Tool result · `toolu_01PiqU47vPX41euXPUtE5ALc`</summary>

```text
Web search results for query: "EnergyMoGen compositional motion generation energy diffusion CVPR 2025"

Links: [{"title":"EnergyMoGen: Compositional Human Motion Generation with ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_EnergyMoGen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_CVPR_2025_paper.pdf"},{"title":"CVPR Poster EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space","url":"https://cvpr.thecvf.com/virtual/2025/poster/34658"},{"title":"[2412.14706] EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space","url":"https://arxiv.org/abs/2412.14706"},{"title":"dblp: EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space.","url":"https://dblp.org/rec/conf/cvpr/ZhangF025.html"},{"title":"EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space","url":"https://arxiv.org/html/2412.14706v1"},{"title":"EnergyMoGen","url":"https://jiro-zhang.github.io/EnergyMoGen/"},{"title":"EnergyMogen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space | Request PDF","url":"https://www.researchgate.net/publication/394606916_EnergyMogen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_Latent_Space"},{"title":"EnergyMogen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11093839/"},{"title":"GitHub - Zilize/awesome-text-to-motion: Text-driven human motion generation surveys, datasets and models. · GitHub","url":"https://github.com/Zilize/awesome-text-to-motion"},{"title":"DeMoGen: Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models","url":"https://arxiv.org/html/2512.22324"}]

I found comprehensive information about EnergyMoGen. Here's a summary of the research:

## Overview

EnergyMoGen addresses the challenge that latent diffusion models struggle to effectively compose multiple semantic concepts into a single, coherent motion sequence, proposing two spectrums of Energy-Based Models: a latent-aware energy-based model and a semantic-aware energy model based on cross-attention.

## Key Components

The approach uses a Motion Variational Autoencoder (VAE) to map 3D human motion into latent vectors, and cross-attention-based transformers as the denoising network in a Latent Diffusion Model (LDM).

To overcome the challenges of semantic inconsistency and motion distortion across the two energy-based model spectrums, the paper introduces Synergistic Energy Fusion, which allows the motion latent diffusion model to synthesize high-quality, complex motions by combining multiple energy terms corresponding to textual descriptions.

## Results

The approach outperforms existing state-of-the-art models on various motion generation tasks, including text-to-motion generation, compositional motion generation, and multi-concept motion generation.

The method is able to compose complex motions from simple concepts in settings of concept conjunction, concept negation, compositional motion generation with conjunction and negation, and multi-concept motion generation.

The paper was published at CVPR 2025 by Jianrong Zhang, Hehe Fan, and Yi Yang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75d866cc-19d4-42a8-b356-560dadc41fbb",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "389e54cc-9057-4416-b209-d7fa0bc6a35c",
  "sourceToolAssistantUUID": "75d866cc-19d4-42a8-b356-560dadc41fbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T20:26:02.848Z_

<details><summary>↩ Tool result · `toolu_01AnM433GsCWsb8VBnLtzy9H`</summary>

```text
Web search results for query: "DiffusionSeeder robot motion planning diffusion 2025"

Links: [{"title":"DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning","url":"https://proceedings.mlr.press/v270/huang25f.html"},{"title":"DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning","url":"https://diffusion-seeder.github.io/"},{"title":"DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning","url":"https://arxiv.org/html/2410.16727v1"},{"title":"[2410.16727] DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning","url":"https://arxiv.org/abs/2410.16727"},{"title":"DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning | OpenReview","url":"https://openreview.net/forum?id=B7Lf6xEv7l"},{"title":"PRESTO: Fast Motion Planning Using Diffusion Models Based on Key-Configuration Environment Representation – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/2025/05/19/seo-icra25-presto/"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"[2412.19948] Motion Planning Diffusion: Learning and Adapting Robot Motion Planning with Diffusion Models","url":"https://arxiv.org/abs/2412.19948"},{"title":"Multi-Robot Motion Planning with Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=AUCYptvAf3"},{"title":"DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/diffusionseeder-seeding-motion-optimization-diffusion-rapid-motion"}]

Based on the search results, here's what I found about DiffusionSeeder:

## Overview

DiffusionSeeder is a diffusion-based approach that generates trajectories to seed motion optimization for rapid robot motion planning.

## How It Works

DiffusionSeeder takes the initial depth image observation of the scene and generates high quality, multi-modal trajectories that are then fine-tuned with few iterations of motion optimization. The system consists of a ViT observation encoder and a conditional diffusion model.

## Performance Results

When integrated with cuRobo (a GPU-accelerated motion optimization method), DiffusionSeeder results in 12x speed up on average, and 36x speed up for more complicated problems, while achieving 10% higher success rate in partially observed simulation environments.

Physical experiments on a Franka robot demonstrate the sim2real transfer of DiffusionSeeder to the real robot, with an average success rate of 86% and planning time of 26ms, increasing on cuRobo by 51% higher success rate and 2.5x speed up.

## Publication

DiffusionSeeder was published in the Proceedings of The 8th Conference on Robot Learning in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "390a9aff-80ea-4d05-babf-c1222ee9d2ca",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "d50421a7-2646-4537-bac7-6a53ccefff4f",
  "sourceToolAssistantUUID": "390a9aff-80ea-4d05-babf-c1222ee9d2ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T20:26:03.096Z_

<details><summary>↩ Tool result · `toolu_01Bme5PpkoRQxuNrk1oFpvRY`</summary>

```text
Web search results for query: "BeyondMimic humanoid guided diffusion 2025"

Links: [{"title":"BeyondMimic","url":"https://beyondmimic.github.io/"},{"title":"[2508.08241] BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion","url":"https://arxiv.org/abs/2508.08241"},{"title":"BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion","url":"https://arxiv.org/html/2508.08241v1"},{"title":"BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250808241L/abstract"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2508.08241"},{"title":"Dataset - BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion","url":"https://zenodo.org/records/17529720"},{"title":"[2508.08241v3] BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion","url":"https://arxiv.org/abs/2508.08241v3"},{"title":"BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion | alphaXiv","url":"https://www.alphaxiv.org/resources/2508.08241v3"},{"title":"BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion","url":"https://www.researchgate.net/publication/394438302_BeyondMimic_From_Motion_Tracking_to_Versatile_Humanoid_Control_via_Guided_Diffusion"}]

Based on the search results, here's what I found about BeyondMimic:

## Overview

BeyondMimic is a real-world framework to learn from human motions for versatile and naturalistic humanoid control via guided diffusion. The paper was submitted on August 11, 2025.

## Key Features

The framework provides a motion tracking pipeline, capable of challenging skills such as jumping spins, sprinting, and cartwheel with state-of-the-art motion quality. It enables mastering a wide range of radically agile behaviors, including aerial cartwheels, spin-kicks, flip-kicks, and sprinting, with a single setup and shared hyperparameters.

## Core Innovation

Beyond mimicking, the framework introduces a unified diffusion policy that enables zero-shot task-specific control at test time using simple cost functions. The model leverages classifier guidance, a diffusion-specific technique for test-time optimization toward novel objectives, extending its capability to solve downstream tasks never encountered during training, including motion inpainting, joystick teleoperation, and obstacle avoidance.

## Real-World Deployment

Deployed on hardware, BeyondMimic performs diverse tasks at test time, including waypoint navigation, joystick teleoperation, and obstacle avoidance, bridging sim-to-real motion tracking and flexible synthesis of human motion primitives for whole-body control.

You can find more details on the official project page at https://beyondmimic.github.io/ and the academic paper on arXiv (2508.08241).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a3f32a5-4adc-4a08-99cc-b2cb3d85c523",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "4c29cfcf-a78b-44a8-bd4d-a1cd3dc0a1d9",
  "sourceToolAssistantUUID": "4a3f32a5-4adc-4a08-99cc-b2cb3d85c523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T20:26:04.756Z_

<details><summary>↩ Tool result · `toolu_015ucZrpjxRg1NwHuHRopiU7`</summary>

```text
Web search results for query: "motion diffusion inpainting body joint masking conditioning"

Links: [{"title":"MDM: Human Motion Diffusion Model","url":"https://guytevet.github.io/mdm-page/"},{"title":"Published as a conference paper at ICLR 2023 HUMAN MOTION DIFFUSION MODEL","url":"https://openreview.net/pdf?id=SJ1kSyO2jwu"},{"title":"MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting","url":"https://arxiv.org/html/2409.14393v1"},{"title":"Flexible Motion In-betweening with Diffusion Models","url":"https://arxiv.org/html/2405.11126v1"},{"title":"Dexterous World Models Byungjun Kim1* Taeksoo Kim1* Junyoung Lee1","url":"https://snuvclab.github.io/dwm/static/pdf/dwm_arxiv_reduced.pdf"},{"title":"A Unified Masked Autoencoder with Patchified Skeletons for Motion Synthesis","url":"https://arxiv.org/html/2308.07301v2"},{"title":"COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation","url":"https://arxiv.org/html/2408.16426v1"},{"title":"Shape Conditioned Human Motion Generation with Diffusion Model","url":"https://arxiv.org/html/2405.06778"},{"title":"Towards Natural Prosthetic Hand Gestures: A Common-Rig and Diffusion Inpainting Pipeline","url":"https://kaseungyup.github.io/natural-prosthetic-hand-gestures/"},{"title":"Mask-Conditioned Voxel Diffusion for Joint Geometry and Color Inpainting","url":"https://arxiv.org/html/2601.00368"}]

I found several relevant research papers and projects related to your search query. Here are the key findings:

## Motion Diffusion Inpainting

The Motion Diffusion Model (MDM) is a carefully adapted classifier-free diffusion-based generative model for the human motion domain. By adapting diffusion image-inpainting, researchers can set a motion prefix and suffix and use the model to fill in the gap, with textual conditions guiding MDM to fill the gap with specific motion that maintains the semantics of the original input.

## Body Joint Masking and Conditioning

Inpainting can be performed in the joints space rather than temporally to demonstrate semantic editing of specific body parts. The UNIMASK-M model decomposes a human pose into body parts to leverage spatio-temporal relationships in human motion, reformulating various pose-conditioned motion synthesis tasks as a reconstruction problem with different masking patterns, and by explicitly informing the model about masked joints, it becomes more robust to occlusions.

## Related Approaches

MaskedMimic is a unified physics-based character control framework that produces full-body motions by inpainting from partial motion descriptions, which can include target keyframes, target joint positions/rotations, text instructions, object interactions, or combinations thereof.

Conditional Motion Diffusion In-betweening (CondMDI) is a unified and flexible method for motion in-betweening based on a masked conditional diffusion model that trains on randomly sampled keyframes with randomly sampled joints, together with a mask that indicates the observed keyframes and features.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e033e9c-fee0-4546-a484-321ecd78bd3b",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "a9c2ae7f-80f3-460a-aeaf-05b588256914",
  "sourceToolAssistantUUID": "7e033e9c-fee0-4546-a484-321ecd78bd3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-10T20:26:07.148Z_

Let me search for more specific related work that might be directly competing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9c2ae7f-80f3-460a-aeaf-05b588256914",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWu3sw2FDFmLGdETLMk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "995fc02d-4368-4006-a9e0-d3db23c15379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQSWEcYBfiMBd4LS4q9QHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 878,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 25507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3895,
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

_source line 52 · 2026-05-10T20:26:07.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LpazERVK7iwKTP3YFmstX1`</summary>

```json
{
  "query": "MaskedMimic physics character control masked motion inpainting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "995fc02d-4368-4006-a9e0-d3db23c15379",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWu3sw2FDFmLGdETLMk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9a7262a-ecc7-44f7-a435-cc9837d05d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQSWEcYBfiMBd4LS4q9QHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 878,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 25507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3895,
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

_source line 53 · 2026-05-10T20:26:08.685Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HtdbhFr3pa3BqcissfpyWB`</summary>

```json
{
  "query": "DeMoGen decompositional motion generation energy diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9a7262a-ecc7-44f7-a435-cc9837d05d00",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWu3sw2FDFmLGdETLMk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7a2ccd4-816a-49a2-88a7-c89c8e0af241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQSWEcYBfiMBd4LS4q9QHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 878,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 25507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3895,
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

_source line 54 · 2026-05-10T20:26:09.154Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VnMmu75MLayAQCXHtiDMZ5`</summary>

```json
{
  "query": "\"Motion Composition Diffusion\" MCD body part spatial"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7a2ccd4-816a-49a2-88a7-c89c8e0af241",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWu3sw2FDFmLGdETLMk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71ffd4e3-6eb0-40f3-9cc8-e902636a30be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQSWEcYBfiMBd4LS4q9QHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 878,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 25507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3895,
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

_source line 55 · 2026-05-10T20:26:09.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NK6KKDHzMwfSEM8AF4kcpD`</summary>

```json
{
  "query": "CondMDI conditional motion diffusion in-betweening masked joints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71ffd4e3-6eb0-40f3-9cc8-e902636a30be",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWu3sw2FDFmLGdETLMk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4322ad52-4325-4697-a724-1de51341de0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQSWEcYBfiMBd4LS4q9QHQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 878,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 25507,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3895
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 878,
          "output_tokens": 224,
          "cache_read_input_tokens": 25507,
          "cache_creation_input_tokens": 3895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3895,
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

_source line 56 · 2026-05-10T20:26:13.231Z_

<details><summary>↩ Tool result · `toolu_01LpazERVK7iwKTP3YFmstX1`</summary>

```text
Web search results for query: "MaskedMimic physics character control masked motion inpainting"

Links: [{"title":"MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting","url":"https://research.nvidia.com/labs/par/maskedmimic/"},{"title":"Paper page - MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting","url":"https://huggingface.co/papers/2409.14393"},{"title":"[2409.14393] MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting","url":"https://arxiv.org/abs/2409.14393"},{"title":"MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting","url":"https://arxiv.org/html/2409.14393v1"},{"title":"MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting | NVIDIA Research Tel-Aviv Lab","url":"https://research.nvidia.com/labs/par/project/maskedmimic.html"},{"title":"MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting | ACM Transactions on Graphics","url":"https://dl.acm.org/doi/10.1145/3687951"},{"title":"MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240914393T/abstract"},{"title":"MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting | Research","url":"https://research.nvidia.com/publication/2024-12_maskedmimic-unified-physics-based-character-control-through-masked-motion"},{"title":"GitHub - DanielTruong99/MaskedMimic: Masked Mimic 🥷: Unified Physics-Based Character Control Through Masked Motion Inpainting","url":"https://github.com/DanielTruong99/MaskedMimic"},{"title":"MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting - Bar-Ilan University","url":"https://cris.biu.ac.il/en/publications/maskedmimic-unified-physics-based-character-control-through-maske/"}]

Based on the search results, here's what I found about MaskedMimic:

## Overview

MaskedMimic is a novel approach that formulates physics-based character control as a general motion inpainting problem. It is a single, unified controller for physics-based humanoid characters, capable of generating a wide range of motions over diverse terrains from intuitive user intents.

## Key Innovation

The key insight is to train a single unified model to synthesize motions from partial (masked) motion descriptions, such as masked keyframes, objects, text descriptions, or any combination thereof. This is achieved by leveraging motion tracking data and designing a scalable training method that can effectively utilize diverse motion descriptions to produce coherent animations.

## Capabilities and Applications

The system is capable of generating full-body motion from partial joint target positions, responding to joystick steering, engaging in object interactions, following paths, interpreting text commands, and even combining these modalities, such as executing text-stylized path following.

## Advantages

The approach learns a physics-based controller that provides an intuitive control interface without requiring tedious reward engineering for all behaviors of interest, and the resulting controller supports a wide range of control modalities and enables seamless transitions between disparate tasks.

The work was published by researchers at NVIDIA and collaborators, and appears in ACM Transactions on Graphics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9a7262a-ecc7-44f7-a435-cc9837d05d00",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "c34327b7-8e4f-4e87-91a5-a008c135475e",
  "sourceToolAssistantUUID": "f9a7262a-ecc7-44f7-a435-cc9837d05d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-10T20:26:15.253Z_

<details><summary>↩ Tool result · `toolu_01HtdbhFr3pa3BqcissfpyWB`</summary>

```text
Web search results for query: "DeMoGen decompositional motion generation energy diffusion"

Links: [{"title":"[2512.22324] DeMoGen: Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models","url":"https://arxiv.org/abs/2512.22324"},{"title":"DeMoGen: Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models","url":"https://arxiv.org/html/2512.22324"},{"title":"DeMoGen","url":"https://jiro-zhang.github.io/DeMoGen/"},{"title":"[2412.14706] EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space","url":"https://arxiv.org/abs/2412.14706"},{"title":"EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space","url":"https://arxiv.org/html/2412.14706v1"},{"title":"EnergyMoGen: Compositional Human Motion Generation with ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_EnergyMoGen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_CVPR_2025_paper.pdf"},{"title":"EnergyMogen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space | Request PDF","url":"https://www.researchgate.net/publication/394606916_EnergyMogen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_Latent_Space"},{"title":"DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning","url":"https://arxiv.org/html/2502.16932v1"},{"title":"DemoGen | Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning","url":"https://demo-generation.github.io/"},{"title":"EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/energymogen-compositional-human-motion-generation-energy-based"}]

Based on the search results, here's what I found about DeMoGen:

## DeMoGen Overview

DeMoGen is a compositional training paradigm for decompositional learning that employs an energy-based diffusion model. The approach considers the inverse perspective of decomposing a holistic motion into semantically meaningful sub-components.

## Key Innovation

The energy formulation directly captures the composed distribution of multiple motion concepts, enabling the model to discover them without relying on ground-truth motions for individual concepts.

## Training Variants

Within this paradigm, there are three training variants to encourage a decompositional understanding of motion: DeMoGen-Exp explicitly trains on decomposed text prompts; DeMoGen-OSS performs orthogonal self-supervised decomposition; DeMoGen-SC enforces semantic consistency between original and decomposed text embeddings.

## Capabilities

These variants enable the approach to disentangle reusable motion primitives from complex motion sequences, and the decomposed motion concepts can be flexibly recombined to generate diverse and novel motions, generalizing beyond the training distribution.

The paper was recently published on arXiv (December 26, 2025) and represents a significant advancement in human motion generation by treating motion composition from a decompositional perspective using energy-based diffusion models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7a2ccd4-816a-49a2-88a7-c89c8e0af241",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "0ebe4512-ca05-4557-a12a-5f78b7638738",
  "sourceToolAssistantUUID": "d7a2ccd4-816a-49a2-88a7-c89c8e0af241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T20:26:17.532Z_

<details><summary>↩ Tool result · `toolu_01NK6KKDHzMwfSEM8AF4kcpD`</summary>

```text
Web search results for query: "CondMDI conditional motion diffusion in-betweening masked joints"

Links: [{"title":"Flexible Motion In-betweening with Diffusion Models","url":"https://arxiv.org/html/2405.11126v1"},{"title":"Flexible Motion In-betweening with Diffusion Models","url":"https://setarehc.github.io/CondMDI/"},{"title":"Flexible Motion In-betweening with Diffusion Models Setareh Cohan","url":"https://xbpeng.github.io/projects/CondMDI/CondMDI_2024.pdf"},{"title":"[Literature Review] Flexible Motion In-betweening with Diffusion Models","url":"https://www.themoonlight.io/en/review/flexible-motion-in-betweening-with-diffusion-models"},{"title":"Flexible Motion In-betweening with Diffusion Models","url":"https://xbpeng.github.io/projects/CondMDI/index.html"},{"title":"GitHub - setarehc/diffusion-motion-inbetweening: The official implementation of Flexible Motion In-betweening with Diffusion Models, SIGGRAPH 2024","url":"https://github.com/setarehc/diffusion-motion-inbetweening"},{"title":"[2405.11126] Flexible Motion In-betweening with Diffusion Models","url":"https://arxiv.org/abs/2405.11126"},{"title":"Flexible Motion In-betweening with Diffusion Models | Research","url":"https://research.nvidia.com/index.php/publication/2024-05_flexible-motion-betweening-diffusion-models"},{"title":"Flexible Motion In-betweening with Diffusion Models | ACM SIGGRAPH 2024 Conference Papers","url":"https://dl.acm.org/doi/10.1145/3641519.3657414"},{"title":"MMM: Generative Masked Motion Model","url":"https://arxiv.org/html/2312.03596v2"}]

Based on the search results, here's comprehensive information about CondMDI:

## Overview

CondMDI (Conditional Motion Diffusion In-betweening) is a unified and flexible method for motion in-betweening based on a masked conditional diffusion model. Motion in-betweening is a fundamental task in character animation that consists of generating motion sequences that plausibly interpolate user-provided keyframe constraints, and has long been recognized as a labor-intensive and challenging process.

## Key Features

The method trains on randomly sampled keyframes with randomly sampled joints, together with a mask that indicates the observed keyframes and features, offering significant flexibility in terms of number of keyframes and their placement in time, as well as partial keyframes (providing information for a subset of the joints).

CondMDI allows for arbitrary dense-or-sparse keyframe placement and partial keyframe constraints while generating high-quality motions that are diverse and coherent with the given keyframes.

## Technical Approach

To condition the model on keyframes, the method uses a simple and effective approach: replacing the noisy input motion with the given keyframes over the provided frames, and concatenating the observation mask to further inform the model of the keyframe locations.

CondMDI allows for text prompts to be used as an additional condition to control the generated motions.

## Performance

CondMDI exhibits the best performance compared to inference-conditioning methods, and does better on partial keyframe in-betweening tasks, as the model is trained with partial keyframes.

The work was published at SIGGRAPH 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4322ad52-4325-4697-a724-1de51341de0b",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "37271c15-2886-4571-9c71-25328369a63e",
  "sourceToolAssistantUUID": "4322ad52-4325-4697-a724-1de51341de0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-10T20:26:20.029Z_

<details><summary>↩ Tool result · `toolu_01VnMmu75MLayAQCXHtiDMZ5`</summary>

```text
Web search results for query: ""Motion Composition Diffusion" MCD body part spatial"

Links: [{"title":"Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models","url":"https://arxiv.org/html/2409.11920v1"},{"title":"Published as a conference paper at ICLR 2023 HUMAN MOTION DIFFUSION MODEL","url":"https://openreview.net/pdf?id=SJ1kSyO2jwu"},{"title":"SinMDM: Single Motion Diffusion","url":"https://sinmdm.github.io/SinMDM-page/"},{"title":"Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation","url":"https://arxiv.org/html/2401.08559v2"},{"title":"FrankenMotion: Part-level Human Motion Generation and Composition Chuqiao Li1","url":"https://coral79.github.io/frankenmotion/Files/FrankenMotion.pdf"},{"title":"FrankenMotion","url":"https://coral79.github.io/frankenmotion/"},{"title":"MDM: Human Motion Diffusion Model","url":"https://guytevet.github.io/mdm-page/"},{"title":"[PDF] SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SINC:-Spatial-Composition-of-3D-Human-Motions-for-Athanasiou-Petrovich/ff969f811673061e50ba2c384e3034ce30c1d561"},{"title":"Shape‐Conditioned Human Motion Diffusion Model with Mesh Representation - Xue - 2025 - Computer Graphics Forum - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/cgf.70065?af=R"},{"title":"[2409.11920] Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models","url":"https://arxiv.org/abs/2409.11920"}]

Based on the search results, here's what I found about Motion Composition Diffusion (MCD):

## Overview

Motion Composition Diffusion (MCD) is a method for generating actions unseen during the training phase. MCD takes a textual annotation describing the movement to be generated and its duration and decomposes it through GPT into one or more known sub-movements present in the training set, each characterized by a start and an end time.

## How It Works

The textual description of an unknown input movement is decomposed using GPT into multiple known basic actions, each with associated time intervals. At each step of the denoising diffusion process, each sub-movement motion is generated, then all are combined into a single movement.

## Spatial and Temporal Composition

The method handles two key types of composition:

- Temporal composition involves two movements executed one after the other, such as "bend knees" and then "jump".
- Spatial composition involves two movements occurring simultaneously, such as "jump" while "throwing an object".

The sum operation for annotations belonging in the same time interval corresponds to an AND condition, which means that it simultaneously satisfies two textual conditions, allowing for spatial composition. By summing the sub-movements generated within their respective time intervals, the method can specify when and for how long the actions occur, thus enabling temporal composition. In this way, both spatial and temporal compositions are achieved using a single equation.

## Key Advantage

Unlike previous approaches, MCD is agnostic to spatial overlap and does not require that each sub-movement specifies the primary body part involved, such as "legs", "left arm", "right arm", etc.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71ffd4e3-6eb0-40f3-9cc8-e902636a30be",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "eddbfefc-1557-42d7-89ea-846b234e2bb6",
  "sourceToolAssistantUUID": "71ffd4e3-6eb0-40f3-9cc8-e902636a30be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-10T20:26:22.218Z_

Let me do a few more targeted searches to catch any remaining relevant work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eddbfefc-1557-42d7-89ea-846b234e2bb6",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWvBDjSthbe9wUGz5Xo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e7e5cee-ae46-48b1-9740-4de119c5f7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPWeDzgnJRwWdmy2PXvFcB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 913,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 29402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3892,
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

_source line 61 · 2026-05-10T20:26:23.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012ArCFdbfHi117LpEaqyibb`</summary>

```json
{
  "query": "SINC spatial composition 3D human motions simultaneous action generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e7e5cee-ae46-48b1-9740-4de119c5f7a8",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWvBDjSthbe9wUGz5Xo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f75365f7-9f1d-4374-82d4-1519f21636d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPWeDzgnJRwWdmy2PXvFcB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 913,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 29402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3892,
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

_source line 62 · 2026-05-10T20:26:23.609Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011QpCT8yeGXeEwntJbmtYRK`</summary>

```json
{
  "query": "Motion-Adapter diffusion compound actions text-to-motion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f75365f7-9f1d-4374-82d4-1519f21636d1",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWvBDjSthbe9wUGz5Xo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d017665e-936c-48d4-b37c-4bd83253c342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPWeDzgnJRwWdmy2PXvFcB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 913,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 29402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3892,
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

_source line 63 · 2026-05-10T20:26:24.542Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0189FfzupTkUmMJe2s9QjPXQ`</summary>

```json
{
  "query": "PHUMA physically grounded humanoid manipulation diffusion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d017665e-936c-48d4-b37c-4bd83253c342",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWvBDjSthbe9wUGz5Xo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "580cf8ca-1f8b-4665-8851-4039094a8199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPWeDzgnJRwWdmy2PXvFcB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 913,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 29402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3892,
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

_source line 64 · 2026-05-10T20:26:25.061Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015HuQ8t4SVz89PkCTsJtV3B`</summary>

```json
{
  "query": "multi-track timeline control motion generation diffusion body parts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "580cf8ca-1f8b-4665-8851-4039094a8199",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWvBDjSthbe9wUGz5Xo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34ebd0c1-1c5c-47be-a506-9fb66f3a684c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPWeDzgnJRwWdmy2PXvFcB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 913,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 29402,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3892
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 913,
          "output_tokens": 225,
          "cache_read_input_tokens": 29402,
          "cache_creation_input_tokens": 3892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3892,
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

_source line 65 · 2026-05-10T20:26:29.820Z_

<details><summary>↩ Tool result · `toolu_012ArCFdbfHi117LpEaqyibb`</summary>

```text
Web search results for query: "SINC spatial composition 3D human motions simultaneous action generation"

Links: [{"title":"[2304.10417] SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation","url":"https://arxiv.org/abs/2304.10417"},{"title":"SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation","url":"https://arxiv.org/html/2304.10417v3"},{"title":"SINC","url":"https://sinc.is.tue.mpg.de/"},{"title":"SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10378366/"},{"title":"GitHub - atnikos/sinc: Official PyTorch implementation of the paper \"SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation\" [ICCV 2023] · GitHub","url":"https://github.com/atnikos/sinc"},{"title":"SINC: Spatial Composition of 3D Human Motions for ...","url":"https://openaccess.thecvf.com/content/ICCV2023/papers/Athanasiou_SINC_Spatial_Composition_of_3D_Human_Motions_for_Simultaneous_Action_ICCV_2023_paper.pdf"},{"title":"[PDF] SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SINC:-Spatial-Composition-of-3D-Human-Motions-for-Athanasiou-Petrovich/ff969f811673061e50ba2c384e3034ce30c1d561"},{"title":"SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation - Algorithms, architectures, image analysis and computer graphics","url":"https://sciencespo.hal.science/LIGM_A3SI/hal-04258194v1"},{"title":"SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation | Perceiving Systems – MPI-IS","url":"https://is.mpg.de/ps/publications/sinc-iccv-2023-96f4db44-d7e5-4adc-a93f-4fb8987ec6da"},{"title":"Mathis Petrovich","url":"https://mathis.petrovich.fr/"}]

I found comprehensive information about SINC. Here's what the search revealed:

## SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation

SINC aims to synthesize 3D human motions given textual inputs describing simultaneous actions, for example 'waving hand' while 'walking' at the same time.

### Key Concept

The paper refers to generating such simultaneous movements as performing 'spatial compositions'. In contrast to temporal compositions that seek to transition from one action to another, spatial compositing requires understanding which body parts are involved in which action, to be able to move them simultaneously.

### Methodology

Motivated by the observation that the correspondence between actions and body parts is encoded in powerful language models, the researchers extract this knowledge by prompting GPT-3 with text such as "what are the body parts involved in the action?", while also providing the parts list and few-shot examples. Given this action-part mapping, they combine body parts from two motions together and establish the first automated method to spatially compose two actions.

### Training Approach

Since training data with compositional actions is always limited by the combinatorics, the researchers further create synthetic data with this approach, and use it to train a new state-of-the-art text-to-motion generation model, called SINC.

### Publication

SINC was presented at ICCV 2023, with an official PyTorch implementation available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f75365f7-9f1d-4374-82d4-1519f21636d1",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "cf5518ea-98b5-4a24-b94b-d5a1ffbf70b2",
  "sourceToolAssistantUUID": "f75365f7-9f1d-4374-82d4-1519f21636d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-10T20:26:30.241Z_

<details><summary>↩ Tool result · `toolu_011QpCT8yeGXeEwntJbmtYRK`</summary>

```text
Web search results for query: "Motion-Adapter diffusion compound actions text-to-motion 2026"

Links: [{"title":"Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions","url":"https://arxiv.org/html/2604.16135v1"},{"title":"Pose-guided Motion Diffusion Model for Text-to-motion Generation | OpenReview","url":"https://openreview.net/forum?id=if8iIYcmVC"},{"title":"Local Action-Guided Motion Diffusion Model for Text-to-Motion Generation","url":"https://jpthu17.github.io/GuidedMotion-project/"},{"title":"MDM: Human Motion Diffusion Model","url":"https://guytevet.github.io/mdm-page/"},{"title":"MotionDiffuse: Text-Driven Human Motion Generation ...","url":"https://mingyuan-zhang.github.io/projects/MotionDiffuse.html"},{"title":"[2208.15001] MotionDiffuse: Text-Driven Human Motion Generation with Diffusion Model","url":"https://arxiv.org/abs/2208.15001"},{"title":"ACMo: Attribute Controllable Motion Generation","url":"https://arxiv.org/html/2503.11038"},{"title":"GitHub - GuyTevet/motion-diffusion-model: The official PyTorch implementation of the paper \"Human Motion Diffusion Model\" · GitHub","url":"https://github.com/GuyTevet/motion-diffusion-model"},{"title":"GitHub - mingyuan-zhang/MotionDiffuse: MotionDiffuse: Text-Driven Human Motion Generation with Diffusion Model","url":"https://github.com/mingyuan-zhang/MotionDiffuse"},{"title":"Local Action-Guided Motion Diffusion Model for Text-to-Motion Generation","url":"https://arxiv.org/html/2407.10528"}]

Based on the search results, here's what I found about Motion-Adapter:

## Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation

Motion-Adapter addresses two key limitations in current text-to-motion diffusion models: catastrophic neglect, where earlier actions are overwritten by later ones due to improper handling of temporal information, and attention collapse from excessive feature fusion in cross-attention mechanisms.

### How It Works

Motion-Adapter is a plug-and-play module that guides text-to-motion diffusion models in generating compound actions by computing decoupled cross-attention maps, which serve as structural masks during denoising steps. Motion-Adapter is trained solely on single-action motions and requires no modification or additional tuning of the diffusion backbone, enabling efficient and consistent motion synthesis.

### Key Features and Performance

Extensive experiments show that the approach outperforms existing methods in generating compound actions and long-term motions, and substantially improves the fidelity and diversity of the generated motions. The framework has been integrated with two diffusion backbones—MDM and MotionDiffuse—and compared against seven state-of-the-art methods under textual prompts of varying complexity.

The research addresses the practical problem of generating natural compound actions like "greeting while walking" from simple text descriptions, without requiring detailed body-part specifications or large language models for interpretation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d017665e-936c-48d4-b37c-4bd83253c342",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "6f145dbc-a055-4899-a9a3-71ecb3c0f812",
  "sourceToolAssistantUUID": "d017665e-936c-48d4-b37c-4bd83253c342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-10T20:26:31.975Z_

<details><summary>↩ Tool result · `toolu_015HuQ8t4SVz89PkCTsJtV3B`</summary>

```text
Web search results for query: "multi-track timeline control motion generation diffusion body parts"

Links: [{"title":"[2401.08559] Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation","url":"https://arxiv.org/abs/2401.08559"},{"title":"Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation","url":"https://arxiv.org/html/2401.08559v2"},{"title":"Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation | OpenReview","url":"https://openreview.net/forum?id=vR0GJh2ph2"},{"title":"GitHub - nv-tlabs/stmc: Implementation of \"Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation\" from CVPR Workshop on Human Motion Generation 2024. · GitHub","url":"https://github.com/nv-tlabs/stmc"},{"title":"[PDF] Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/d135b38816993a9110f6d2aadd65ca371489ed03"},{"title":"Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/10677511/10677844/10678064.pdf"},{"title":"Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation | Request PDF","url":"https://www.researchgate.net/publication/384414467_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation"},{"title":"MotionFix: Text-Driven 3D Human Motion Editing","url":"https://arxiv.org/html/2408.00712v3"},{"title":"STMC - Mathis Petrovich","url":"https://mathis.petrovich.fr/stmc/"},{"title":"Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation | Perceiving Systems – Max Planck Institute for Intelligent Systems","url":"https://is.mpg.de/ps/publications/stmc"}]

Based on the search results, the query returns information about **"Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation"** (STMC), a research paper and method developed for controlled motion generation.

## Overview

Instead of a single prompt, users can specify a multi-track timeline of multiple prompts organized in temporal intervals that may overlap, enabling specifying the exact timings of each action and composing multiple actions in sequence or at overlapping intervals.

## Technical Approach

To generate composite animations from a multi-track timeline, the method proposes a new test-time denoising method that can be integrated with any pre-trained motion diffusion model to synthesize realistic motions that accurately reflect the timeline.

At every step of denoising, the method processes each timeline interval (text prompt) individually, subsequently aggregating the predictions with consideration for the specific body parts engaged in each action.

## Key Innovation

Using a single text prompt as input lacks the fine-grained control needed by animators, such as composing multiple actions and defining precise durations for parts of the motion. To address this, the method introduces the new problem of timeline control for text-driven motion synthesis, which provides an intuitive, yet fine-grained, input interface for users.

The method was presented at the CVPR Workshop on Human Motion Generation 2024, and implementation code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34ebd0c1-1c5c-47be-a506-9fb66f3a684c",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "fba19479-cbb2-4d07-95c7-2f0b8b03fad4",
  "sourceToolAssistantUUID": "34ebd0c1-1c5c-47be-a506-9fb66f3a684c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-10T20:26:34.473Z_

<details><summary>↩ Tool result · `toolu_0189FfzupTkUmMJe2s9QjPXQ`</summary>

```text
Web search results for query: "PHUMA physically grounded humanoid manipulation diffusion 2026"

Links: [{"title":"PHUMA: Physically-Grounded Humanoid Locomotion Dataset | OpenReview","url":"https://openreview.net/forum?id=DDogB73gS4"},{"title":"Paper page - PHUMA: Physically-Grounded Humanoid Locomotion Dataset","url":"https://huggingface.co/papers/2510.26236"},{"title":"[2510.26236] PHUMA: Physically-Grounded Humanoid Locomotion Dataset","url":"https://arxiv.org/abs/2510.26236"},{"title":"PHUMA: PHYSICALLY-GROUNDED HUMANOID ...","url":"https://openreview.net/pdf/a36747cac87a488230dfe8cb6d5c0aa5a6db82d7.pdf"},{"title":"GitHub - DAVIAN-Robotics/PHUMA: Code for \"PHUMA: Physically-Grounded Humanoid Locomotion Dataset\" · GitHub","url":"https://github.com/DAVIAN-Robotics/PHUMA"},{"title":"(PDF) PHUMA: Physically-Grounded Humanoid Locomotion Dataset","url":"https://www.researchgate.net/publication/397088902_PHUMA_Physically-Grounded_Humanoid_Locomotion_Dataset"},{"title":"DAVIAN-Robotics · GitHub","url":"https://github.com/DAVIAN-Robotics"},{"title":"DAVIAN-Robotics/PHUMA · Datasets at Hugging Face","url":"https://huggingface.co/datasets/DAVIAN-Robotics/PHUMA"},{"title":"PHUMA: PHYSICALLY-GROUNDED HUMANOID LOCOMOTION DATASET","url":"https://arxiv.org/pdf/2510.26236"},{"title":"[Quick Review] PHUMA: Physically-Grounded Humanoid Locomotion Dataset","url":"https://liner.com/review/phuma-physicallygrounded-humanoid-locomotion-dataset"}]

Based on the search results, I found information about PHUMA, though it's focused on locomotion rather than manipulation with diffusion models. Here's what I found:

PHUMA is a Physically-grounded HUMAnoid locomotion dataset that leverages human video at scale, while addressing physical artifacts through careful data curation and physics-constrained retargeting.

PHUMA enforces joint limits, ensures ground contact, and eliminates foot skating, producing motions that are both large-scale and physically reliable.

To address artifacts introduced during the retargeting process, PhySINK is employed as a physics-constrained retargeting method that adapts curated human motion to humanoid robots while enforcing physical plausibility.

PHUMA-trained policies outperform Humanoid-X and AMASS, achieving significant gains in imitating diverse motions.

The research was submitted to ICLR 2026, with the paper initially appearing on arXiv in October 2025. However, my search results don't contain information specifically about PHUMA being used with diffusion models for manipulation tasks—the results focus primarily on the locomotion dataset and its application to humanoid movement imitation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "580cf8ca-1f8b-4665-8851-4039094a8199",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "f94b70d5-f803-4159-9572-a219e3e2084b",
  "sourceToolAssistantUUID": "580cf8ca-1f8b-4665-8851-4039094a8199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-10T20:26:38.366Z_

Let me search for a few more specific areas that could be directly relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f94b70d5-f803-4159-9572-a219e3e2084b",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWwEyV2fFbtqnjC3KDd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a43396d-6123-4644-9c25-8b7b46130f19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAW7SCLVdV3Bg8ZYgezMeP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 890,
      "cache_creation_input_tokens": 3813,
      "cache_read_input_tokens": 33294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3813,
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

_source line 70 · 2026-05-10T20:26:39.362Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BFHDfP4WRmKExBNxNuDSbj`</summary>

```json
{
  "query": "humanoid robot retargeting diffusion motion generation whole-body 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a43396d-6123-4644-9c25-8b7b46130f19",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWwEyV2fFbtqnjC3KDd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b362897f-40fd-4a22-a423-a2764256f139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAW7SCLVdV3Bg8ZYgezMeP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 890,
      "cache_creation_input_tokens": 3813,
      "cache_read_input_tokens": 33294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3813,
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

_source line 71 · 2026-05-10T20:26:39.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ArxhNsF5xixNja7LZxDa1e`</summary>

```json
{
  "query": "diffusion model compositionality score composition vs inpainting motion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b362897f-40fd-4a22-a423-a2764256f139",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWwEyV2fFbtqnjC3KDd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a31c0513-ad41-420b-84e9-84dd0ad43c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAW7SCLVdV3Bg8ZYgezMeP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 890,
      "cache_creation_input_tokens": 3813,
      "cache_read_input_tokens": 33294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3813,
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

_source line 72 · 2026-05-10T20:26:40.366Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CsenrgPTv48B89gzdDwAcP`</summary>

```json
{
  "query": "BA-IDM body-aware diffusion motion generation body parts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a31c0513-ad41-420b-84e9-84dd0ad43c56",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWwEyV2fFbtqnjC3KDd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3450a0c9-520f-45d5-b34e-d97c5e2b0f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAW7SCLVdV3Bg8ZYgezMeP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 890,
      "cache_creation_input_tokens": 3813,
      "cache_read_input_tokens": 33294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3813,
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

_source line 73 · 2026-05-10T20:26:41.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0179VvGY3naKfPgTQjp8tqvp`</summary>

```json
{
  "query": "Kimodo follow-up extending building on 2026 humanoid"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3450a0c9-520f-45d5-b34e-d97c5e2b0f0a",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWwEyV2fFbtqnjC3KDd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd43c413-5d30-455e-ad0d-06c33dafe42c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAW7SCLVdV3Bg8ZYgezMeP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 890,
      "cache_creation_input_tokens": 3813,
      "cache_read_input_tokens": 33294,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3813
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 890,
          "output_tokens": 229,
          "cache_read_input_tokens": 33294,
          "cache_creation_input_tokens": 3813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3813,
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

_source line 74 · 2026-05-10T20:26:46.377Z_

<details><summary>↩ Tool result · `toolu_01ArxhNsF5xixNja7LZxDa1e`</summary>

```text
Web search results for query: "diffusion model compositionality score composition vs inpainting motion"

Links: [{"title":"Compositional Visual Generation with Composable Diffusion Models","url":"https://energy-based-model.github.io/Compositional-Visual-Generation-with-Composable-Diffusion-Models/"},{"title":"Diffusion model - Wikipedia","url":"https://en.wikipedia.org/wiki/Diffusion_model"},{"title":"State of the Art on Diffusion Models for Visual Computing","url":"https://web.stanford.edu/~gordonwz/DiffusionSTAR.pdf"},{"title":"Diffuse to Choose: Enriching Image Conditioned Inpainting in Latent Diffusion Models for Virtual Try-All","url":"https://arxiv.org/html/2401.13795v1"},{"title":"Diffusion Classifiers Understand Compositionality, but Conditions Apply","url":"https://arxiv.org/html/2505.17955v1"},{"title":"Compositional Generation with Energy-Based Diffusion ...","url":"https://proceedings.mlr.press/v202/du23a/du23a.pdf"},{"title":"GitHub - YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy: Diffusion model papers, survey, and taxonomy · GitHub","url":"https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy"},{"title":"Compositional Abilities Emerge Multiplicatively: Exploring Diffusion Models on a Synthetic Task | OpenReview","url":"https://openreview.net/forum?id=frVo9MzRuU"},{"title":"Diffusion Classifiers Understand Compositionality, but Conditions Apply | OpenReview","url":"https://openreview.net/forum?id=c2F2dUx01R"},{"title":"COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation","url":"https://arxiv.org/html/2408.16426"}]

Based on the search results, I found several relevant papers and resources about diffusion model compositionality, composition techniques, inpainting, and motion handling:

## Compositionality in Diffusion Models

Research on compositional diffusion models sends images and individual concepts to the diffusion model to generate scores, then composes different concepts using compositional operators to denoise the generated images. Methods can compose multiple diffusion models during inference and generate images containing all the concepts described in the inputs without further training.

While discriminative models often struggle with compositional understanding, recent generative text-to-image diffusion models excel at synthesizing complex scenes, suggesting inherent compositional capabilities.

## Composition vs. Inpainting

Diffusion models offer a unique platform for fine-grained image editing by facilitating adjustments to various network phases and components to manipulate both spatial layout and visual aesthetics. The search results show that both compositional generation and inpainting are distinct applications of diffusion models within image editing tasks.

## Motion Handling

Recent work proposes control-inpainting motion diffusion priors that enable fine-grained control, introducing a novel control-inpainting score distillation sampling method to ensure well-aligned, consistent, and high-quality motion from the diffusion prior.

The results indicate that diffusion model compositionality is an active research area with applications across composition tasks, inpainting, and motion estimation, though each involves different technical approaches and challenges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a31c0513-ad41-420b-84e9-84dd0ad43c56",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "d3b9d248-4e35-4845-8d26-284527e25116",
  "sourceToolAssistantUUID": "a31c0513-ad41-420b-84e9-84dd0ad43c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-10T20:26:46.944Z_

<details><summary>↩ Tool result · `toolu_01CsenrgPTv48B89gzdDwAcP`</summary>

```text
Web search results for query: "BA-IDM body-aware diffusion motion generation body parts"

Links: [{"title":"Wandering and feeling the Scenes: Body-Aware Diffusion for 3D Human Motion Generation | Proceedings of the 7th ACM International Conference on Multimedia in Asia","url":"https://dl.acm.org/doi/10.1145/3743093.3770934"},{"title":"Wandering and feeling the Scenes: Body-Aware Diffusion for 3D Human Motion Generation - East China Normal University","url":"https://pure.ecnu.edu.cn/en/publications/wandering-and-feeling-the-scenes-body-aware-diffusion-for-3d-huma/"},{"title":"FrankenMotion: Part-level Human Motion Generation and Composition Chuqiao Li1","url":"https://coral79.github.io/frankenmotion/Files/FrankenMotion.pdf"},{"title":"Published as a conference paper at ICLR 2023 HUMAN MOTION DIFFUSION MODEL","url":"https://openreview.net/pdf?id=SJ1kSyO2jwu"},{"title":"MDM: Human Motion Diffusion Model","url":"https://guytevet.github.io/mdm-page/"},{"title":"BioMoDiffuse: Physics-Guided Biomechanical Diffusion for Controllable and Authentic Human Motion Synthesis","url":"https://arxiv.org/html/2503.06151v1"},{"title":"HMD2: Environment-aware Motion Generation from Single Egocentric Head-Mounted Device","url":"https://arxiv.org/html/2409.13426v1"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/"},{"title":"Shape‐Conditioned Human Motion Diffusion Model with Mesh Representation - Xue - 2025 - Computer Graphics Forum - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/cgf.70065?af=R"},{"title":"Holistic-Motion2D: Scalable Whole-body Human Motion Generation in 2D Space","url":"https://arxiv.org/html/2406.11253v1"}]

Based on the search results, I found detailed information about BA-IDM:

## BA-IDM: Body-Aware Diffusion Motion Generation

BA-IDM is a body-aware diffusion framework that enables controllable 3D human motion generation within complex scenes.

### Key Components:

**Body-Aware Subsystem:**
The Body-Aware subsystem divides text into atomic motions and predicts target body parts. The body-aware subsystem plays a crucial role in fine-grained control within the whole framework by accurately mapping complex text instructions to specific body parts, allowing BA-IDM to generate vivid and complex motions.

**Core Features:**
The key contributions are: (1) a body-aware subsystem enabling fine-grained control by mapping text instructions to body parts and refining motion rhythms; (2) a diffusion framework that enhances motion-text alignment; and (3) auxiliary modules that integrate reinforcement learning and conditional guidance for stable, extendable motion generation.

**Motion Control:**
The framework further adjusts the overall motion rhythm based on text instructions that control leg movements.

### Publication:
The research was presented at the 7th ACM International Conference on Multimedia in Asia (MMAsia 2025).

The BA-IDM framework addresses limitations in existing scene-aware motion generation methods by providing fine-grained, body-part-specific control over human motion synthesis in complex environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3450a0c9-520f-45d5-b34e-d97c5e2b0f0a",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "fc298e2f-10c5-4554-b072-cc92c375e56a",
  "sourceToolAssistantUUID": "3450a0c9-520f-45d5-b34e-d97c5e2b0f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-10T20:26:47.127Z_

<details><summary>↩ Tool result · `toolu_01BFHDfP4WRmKExBNxNuDSbj`</summary>

```text
Web search results for query: "humanoid robot retargeting diffusion motion generation whole-body 2025 2026"

Links: [{"title":"GitHub - YanjieZe/GMR: [ICRA 2026] GMR: General Motion Retargeting. Retarget human motions into diverse humanoid robots in real time on CPU. Retargeter for TWIST. · GitHub","url":"https://github.com/YanjieZe/GMR"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Natural Humanoid Robot Locomotion with Generative Motion Prior","url":"https://arxiv.org/html/2503.09015v1"},{"title":"Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking","url":"https://arxiv.org/html/2510.02252v1"},{"title":"From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance","url":"https://arxiv.org/html/2510.14952"},{"title":"Robot Motion Diffusion Model: Motion Generation for Robotic Characters | SIGGRAPH Asia 2024 Conference Papers","url":"https://dl.acm.org/doi/10.1145/3680528.3687626"},{"title":"Multi-Humanoid Robot Arm Motion Imitation and Collaboration Based on Improved Retargeting","url":"https://www.mdpi.com/2313-7673/10/3/190"},{"title":"Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control","url":"https://arxiv.org/html/2603.22201v3"},{"title":"Conditional Adversarial Motion Priors by a Novel Retargeting Method for Versatile Humanoid Robot Control - Zhang - 2025 - International Journal of Adaptive Control and Signal Processing - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/acs.3915"},{"title":"Harmon: Whole-Body Motion Generation of Humanoid ...","url":"https://ut-austin-rpl.github.io/Harmon/"}]

Here are the search results for humanoid robot retargeting, diffusion-based motion generation, and whole-body control from 2025-2026:

## Key Research Areas Found

**Motion Retargeting Methods:**
GMR (General Motion Retargeting) is a project that retargets human motions into diverse humanoid robots in real time, with research published at ICRA 2026. Recent updates include support for multiple humanoid robot platforms such as Booster T1, Berkeley Humanoid Lite, and Unitree H1.

NMR (Neural Motion Retargeting) reformulates the retargeting problem as learning data distribution rather than optimizing optimal solutions, proposing a dynamics-aware learned process.

**Diffusion-Based Motion Generation:**
Recent work performs whole-body motion retargeting to transform human natural motion data to humanoid robots, then trains a motion generation network based on a Conditional Variational Auto-encoder (CVAE) capable of predicting future natural robot motions in an auto-regressive manner.

Some approaches employ a hybrid causal transformer–diffusion architecture where the transformer backbone captures long-horizon dependencies and ensures global consistency.

**Whole-Body Control Systems:**
Deploying text-to-motion models on real robots typically requires a hierarchical pipeline: decoding human motion from language, retargeting it to robot morphology, and tracking the trajectory with a physics-based controller.

**Related Research:**
Recent papers from 2025-2026 include work on humanoid dexterous manipulation, dynamics-aware motion generation for high-DoF robots, and generalizable learning approaches for humanoid robot manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b362897f-40fd-4a22-a423-a2764256f139",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "b5195929-1dc8-450a-ab72-ec0844ec06f1",
  "sourceToolAssistantUUID": "b362897f-40fd-4a22-a423-a2764256f139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-10T20:26:48.922Z_

<details><summary>↩ Tool result · `toolu_0179VvGY3naKfPgTQjp8tqvp`</summary>

```text
Web search results for query: "Kimodo follow-up extending building on 2026 humanoid"

Links: [{"title":"GitHub - nv-tlabs/kimodo: Official implementation of Kimodo, a kinematic motion diffusion model for high-quality human(oid) motion generation. · GitHub","url":"https://github.com/nv-tlabs/kimodo"},{"title":"The Code Is Open. The Data Isn't. — NVIDIA Kimodo and the Humanoid Motion Data Race","url":"https://blog.pebblous.ai/blog/kimodo-text-to-motion/en/"},{"title":"2026-3-16 Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/assets/kimodo_tech_report.pdf"},{"title":"GitHub - NVlabs/GR00T-WholeBodyControl: Welcome to GR00T Whole-Body Control (WBC)! This is a unified platform for developing and deploying advanced humanoid controllers. This includes: Decoupled WBC models used in NVIDIA Isaac-Gr00t, Gr00t N1.5 and N1.6 and GEAR-SONIC · GitHub","url":"https://github.com/NVlabs/GR00T-WholeBodyControl"},{"title":"2026-3-16 Kimodo: Scaling Controllable Human Motion Generation Davis Rempe*, Mathis Petrovich*, Ye Y - YouTube","url":"https://www.youtube.com/watch?v=4mCXgZVu8E4"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://arxiv.org/html/2603.15546v1"},{"title":"kimodo-motion-diffusion by aradotso/trending-skills | explainx.ai","url":"https://explainx.ai/skills/aradotso/trending-skills/kimodo-motion-diffusion"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/"},{"title":"Kimodo: Scaling Controllable Human Motion Generation | DAIR @ NVIDIA Research","url":"https://research.nvidia.com/labs/dair/publication/kimodo2026/"},{"title":"Latest Breakthroughs of Humanoid Robots in 2026 - Philip Metzger","url":"https://philipmetzger.com/latest-breakthroughs-of-humanoid-robots-in-2026/"}]

Based on the search results, I can provide you with information about Kimodo and its developments in 2026:

## Kimodo: Scaling Controllable Human Motion Generation

Kimodo had its initial open-source release in March 2026 with five model variants (SOMA, G1, SMPL-X), CLI, interactive demo, and timeline annotations for BONES-SEED.

### Key Follow-up Developments

On April 10, 2026, the Kimodo Motion Generation Benchmark was released alongside new v1.1 Kimodo-SOMA models. Additionally, on April 24, 2026, improvements were made to multi-prompt generation and better support for small VRAM GPUs via TEXT_ENCODER_DEVICE=cpu environment variable.

### Building on Humanoid Technology

Kimodo is used to generate demonstration data directly on the G1 robot, which is then tracked by a physics-based humanoid policy trained with ProtoMotions and deployed to a real-world robot. The architecture separates semantic generation from robot-specific retargeting, meaning the motion understanding layer doesn't need to be retrained for each new robot platform, and the text-to-motion core stays stable while only the retargeting head changes - an abstraction designed for a multi-platform future.

The live SONIC web demo features Kimodo text-to-motion generation. Kimodo has also been incorporated into the interactive GEAR-SONIC demo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd43c413-5d30-455e-ad0d-06c33dafe42c",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "664a1527-ebb5-4012-a942-06fa95364c52",
  "sourceToolAssistantUUID": "dd43c413-5d30-455e-ad0d-06c33dafe42c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-10T20:26:51.028Z_

Let me do one final batch of searches for any remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "664a1527-ebb5-4012-a942-06fa95364c52",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWxJijNAUqgDJyKXHRH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44c0b280-48bd-42a9-ad86-1e2e3fd0b142",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwSkvJVN3agindnwSpYYuV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 37107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4854,
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

_source line 79 · 2026-05-10T20:26:52.028Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LmGRm1AbDXicNiWU4hiimV`</summary>

```json
{
  "query": "Robot Motion Diffusion Model SIGGRAPH Asia 2024 non-human morphology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44c0b280-48bd-42a9-ad86-1e2e3fd0b142",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWxJijNAUqgDJyKXHRH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "622d33db-85c7-4ea5-b75b-d1d1b7169b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwSkvJVN3agindnwSpYYuV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 37107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4854,
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

_source line 80 · 2026-05-10T20:26:52.497Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012vZVWzVtdwBQAohfq2a6td`</summary>

```json
{
  "query": "Harmon whole-body motion generation humanoid robot diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "622d33db-85c7-4ea5-b75b-d1d1b7169b1d",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWxJijNAUqgDJyKXHRH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52896861-3340-484f-b33e-8a3a62f20f4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwSkvJVN3agindnwSpYYuV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 37107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4854,
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

_source line 81 · 2026-05-10T20:26:53.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KYWqmAZMV2iGV1mqATLWkK`</summary>

```json
{
  "query": "diffusion policy humanoid whole-body inpainting masking joint constraint 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52896861-3340-484f-b33e-8a3a62f20f4a",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWxJijNAUqgDJyKXHRH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "148efaf7-c368-4d29-856d-eba92baba607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwSkvJVN3agindnwSpYYuV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 37107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4854,
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

_source line 82 · 2026-05-10T20:26:54.132Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018v6FjSyNw71xbmmKTzFn3L`</summary>

```json
{
  "query": "Dexterous World Models diffusion inpainting robot hand"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "148efaf7-c368-4d29-856d-eba92baba607",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWxJijNAUqgDJyKXHRH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ffd9a24-b4f6-4954-81b1-e9c07a9cdc6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwSkvJVN3agindnwSpYYuV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 37107,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4854
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 234,
          "cache_read_input_tokens": 37107,
          "cache_creation_input_tokens": 4854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4854,
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

_source line 83 · 2026-05-10T20:26:58.709Z_

<details><summary>↩ Tool result · `toolu_012vZVWzVtdwBQAohfq2a6td`</summary>

```text
Web search results for query: "Harmon whole-body motion generation humanoid robot diffusion"

Links: [{"title":"Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions","url":"https://arxiv.org/html/2410.12773v1"},{"title":"[2410.12773] Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions","url":"https://arxiv.org/abs/2410.12773"},{"title":"Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions","url":"https://proceedings.mlr.press/v270/jiang25b.html"},{"title":"Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions | OpenReview","url":"https://openreview.net/forum?id=UUZ4Yw3lt0&noteId=UUZ4Yw3lt0"},{"title":"Harmon: Whole-Body Motion Generation of Humanoid ...","url":"https://ut-austin-rpl.github.io/Harmon/"},{"title":"[2410.12773v1] Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions","url":"https://arxiv.org/abs/2410.12773v1"},{"title":"Harmon: Language-Driven Motion Generation for Robots","url":"https://www.emergentmind.com/papers/2410.12773"},{"title":"Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions | NVIDIA Learning and Perception Research","url":"https://research.nvidia.com/labs/lpr/publication/harmon2024/"},{"title":"[Literature Review] Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions","url":"https://www.themoonlight.io/en/review/harmon-whole-body-motion-generation-of-humanoid-robots-from-language-descriptions"},{"title":"Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions - Paper Detail","url":"https://deeplearn.org/arxiv/537519/harmon:-whole-body-motion-generation-of-humanoid-robots-from-language-descriptions"}]

Based on the search results, here's what I found about Harmon:

## Overview

Harmon (Humanoid Robot Motion Generation) generates whole-body humanoid motions from free-form language descriptions by incorporating human motion priors.

## Technical Approach

The system uses a multi-stage pipeline:

1. **Human Motion Generation**: PhysDiff, a diffusion-based generative model trained on large-scale human motion datasets generates human motions from language descriptions and incorporates physics constraints during the diffusion process to generate physically plausible human motions.

2. **Motion Retargeting**: The human motion is then retargeted to a simulated humanoid robot using inverse kinematics.

3. **Motion Refinement**: Vision Language Models (VLMs) are leveraged to edit the humanoid motion. A VLM is employed to generate finger and head motions and iteratively adjust the body motion.

## Results

Harmon demonstrates natural and text-aligned humanoid motions and is favored by human evaluators on 86.7% of test cases. The system was tested on a Fourier GR1 humanoid robot, with the generated motions executed on the physical robot to illustrate diverse and expressive humanoid motions in the real world.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52896861-3340-484f-b33e-8a3a62f20f4a",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "c93e42ef-7d02-4383-b214-16403e28fd3d",
  "sourceToolAssistantUUID": "52896861-3340-484f-b33e-8a3a62f20f4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-10T20:26:59.470Z_

<details><summary>↩ Tool result · `toolu_01LmGRm1AbDXicNiWU4hiimV`</summary>

```text
Web search results for query: "Robot Motion Diffusion Model SIGGRAPH Asia 2024 non-human morphology"

Links: [{"title":"Robot Motion Diffusion Model: Motion Generation for Robotic Characters | SIGGRAPH Asia 2024 Conference Papers","url":"https://dl.acm.org/doi/10.1145/3680528.3687626"},{"title":"Contributors - SIGGRAPH Asia 2024","url":"https://asia.siggraph.org/2024/contributors/"},{"title":"SIGGRAPH Asia 2024 Conference Papers - ACM Digital Library","url":"https://dl.acm.org/doi/proceedings/10.1145/3680528?tocHeading=heading15"},{"title":"Robot Motion Diffusion Model: Motion Generation for Robotic Characters - Disney Research","url":"https://la.disneyresearch.com/publication/robot-motion-diffusion-model-motion-generation-for-robotic-characters/"},{"title":"Robot Motion Diffusion Model: Motion Generation for Robotic Characters","url":"https://la.disneyresearch.com/wp-content/uploads/RobotMDM_2.pdf"},{"title":"SA Real-Time Live! '24: SIGGRAPH Asia 2024 Real-Time Live!","url":"https://www.siggraph.org/wp-content/uploads/2025/03/SIGGRAPH-Asia-2024-Real-Time-Live.html"},{"title":"Robot Motion Diffusion Model: Motion Generation for Robotic Characters | Request PDF","url":"https://www.researchgate.net/publication/386409165_Robot_Motion_Diffusion_Model_Motion_Generation_for_Robotic_Characters"},{"title":"Diffuse-CLoC: Guided Diffusion for Physics-based Character Look-ahead Control","url":"https://arxiv.org/html/2503.11801v1"},{"title":"PDP: Physics-Based Character Animation via Diffusion Policy | SIGGRAPH Asia 2024 Conference Papers","url":"https://dl.acm.org/doi/10.1145/3680528.3687683"},{"title":"Biomechanical analysis of cinematic motion: AI-driven generation and evaluation in film and animation - Zhaoqi Li, 2025","url":"https://journals.sagepub.com/doi/10.1177/14727978251348639"}]

I found relevant information about the Robot Motion Diffusion Model paper from SIGGRAPH Asia 2024. Here are the key findings:

## Robot Motion Diffusion Model: Motion Generation for Robotic Characters

The paper was presented at ACM SIGGRAPH Asia 2024 by researchers from Disney Research and ETH Zurich, including Agon Serifi, Ruben Grandia, Espen Knoop, and Markus Gross.

### Key Focus and Contribution

The method addresses the issue that kinematic generative motion models often produce motions that fail to adhere to physical constraints, and introduces a novel approach that integrates kinematic generative models with physics-based character control.

### Technical Approach

RobotMDM (Robot Motion Diffusion Model) leverages a pre-trained imitation policy (Actor) and a pre-trained Motion Diffusion Model in a two-stage process, where a Critic is trained to evaluate the Actor's performance, creating a differentiable surrogate for expected future rewards conditioned on motion input.

### Handling Non-Human Morphologies

Notably, the framework generalizes across human, non-human, and synthetic morphologies, where distinct energy-efficient strategies naturally appear—for example, quadrupedal gaits in Chimanoid versus bipedal gaits in Humanoid.

### Evaluation

The method was evaluated on a bipedal robot with 20 degrees of freedom, standing 0.84 m tall with a mass of 16.2 kg.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "622d33db-85c7-4ea5-b75b-d1d1b7169b1d",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "058a3675-985a-4b27-aeaf-66cde5def89b",
  "sourceToolAssistantUUID": "622d33db-85c7-4ea5-b75b-d1d1b7169b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-10T20:27:00.546Z_

<details><summary>↩ Tool result · `toolu_01KYWqmAZMV2iGV1mqATLWkK`</summary>

```text
Web search results for query: "diffusion policy humanoid whole-body inpainting masking joint constraint 2025 2026"

Links: [{"title":"COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-72640-8_24"},{"title":"NeurIPS Inpainting-Guided Policy Optimization for Diffusion Large Language Models","url":"https://neurips.cc/virtual/2025/126612"},{"title":"Stable Diffusion-Based Approach for Human De-Occlusion","url":"https://arxiv.org/html/2508.12663v1"},{"title":"Mask-Conditioned Inpainting","url":"https://www.emergentmind.com/topics/mask-conditioned-inpainting"},{"title":"[2410.10803] Generalizable Humanoid Manipulation with 3D Diffusion Policies","url":"https://arxiv.org/abs/2410.10803"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Stable Diffusion Inpainting","url":"https://www.emergentmind.com/topics/stable-diffusion-inpainting"},{"title":"Single-Image 3D Human Reconstruction with 3D-Aware Diffusion Priors and Facial Enhancement | Proceedings of the SIGGRAPH Asia 2025 Conference Papers","url":"https://dl.acm.org/doi/10.1145/3757377.3763839"},{"title":"Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies","url":"https://arxiv.org/html/2410.10803v1"},{"title":"[2601.02098] InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting","url":"https://arxiv.org/abs/2601.02098"}]

I found several relevant research papers and resources related to diffusion policies for humanoid robots and inpainting techniques. Here's a summary of the search results:

## Key Findings:

**Humanoid Diffusion Policies:**
A system integrating a whole-upper-body robotic teleoperation system, a 25-DoF humanoid robot platform with a height-adjustable cart and 3D LiDAR sensor, and an improved 3D Diffusion Policy learning algorithm for humanoid robots to learn from noisy human data was developed to enable full-sized humanoid robots to perform complex manipulation tasks using only data collected in one single scene and with only onboard computing.

**Improved 3D Diffusion Policies:**
The Improved 3D Diffusion Policy (iDP3) is a novel 3D visuomotor policy that eliminates constraints by leveraging egocentric 3D visual representations, addressing challenges with camera calibration and point-cloud segmentation on mobile robots.

**Diffusion Models in Robotics:**
Diffusion models enable the incorporation of constraints embedded with an MLP, and formulate conditioning as inpainting, where during inference at each denoising step, specific states from the currently being generated sample are replaced with states from the condition.

**Human Reconstruction with Inpainting:**
An identity-preserving diffusion inpainting module integrates textual inversion with semantic-conditioned guidance for subject-specific, temporally coherent completion to reconstruct occluded humans with high fidelity.

These papers demonstrate the integration of diffusion policies with humanoid robotics and advanced inpainting techniques for handling constraints and occlusions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "148efaf7-c368-4d29-856d-eba92baba607",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "e0bef283-8876-426b-96a1-ce251805dc21",
  "sourceToolAssistantUUID": "148efaf7-c368-4d29-856d-eba92baba607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-10T20:27:02.305Z_

<details><summary>↩ Tool result · `toolu_018v6FjSyNw71xbmmKTzFn3L`</summary>

```text
Web search results for query: "Dexterous World Models diffusion inpainting robot hand"

Links: [{"title":"Dexterous World Models Byungjun Kim1* Taeksoo Kim1* Junyoung Lee1","url":"https://snuvclab.github.io/dwm/static/pdf/dwm_arxiv_reduced.pdf"},{"title":"Dexterous World Models","url":"https://arxiv.org/html/2512.17907v1"},{"title":"Dexterous World Models (DWM)","url":"https://snuvclab.github.io/dwm/"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"World Models Can Leverage Human Videos for Dexterous Manipulation","url":"https://arxiv.org/html/2512.13644v1"},{"title":"[2512.13644] World Models for Learning Dexterous Hand-Object Interactions from Human Videos","url":"https://arxiv.org/abs/2512.13644"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Interaction-aware Diffusion Planning for Adaptive Dexterous ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Liang_DexHandDiff_Interaction-aware_Diffusion_Planning_for_Adaptive_Dexterous_Manipulation_CVPR_2025_paper.pdf"},{"title":"World Models for Learning Dexterous Hand-Object Interactions from Human Videos","url":"https://arxiv.org/html/2512.13644"},{"title":"DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation","url":"https://arxiv.org/html/2505.21864v1"}]

Based on the search results, here's what I found about Dexterous World Models with diffusion inpainting for robot hands:

## Dexterous World Models (DWM)

Dexterous World Model (DWM) is a scene-action-conditioned video diffusion framework that models how dexterous human actions induce dynamic changes in static 3D scenes.

### How It Works

Given a static 3D scene rendering and an egocentric hand motion sequence, DWM generates temporally coherent videos depicting plausible human–scene interactions. The approach leverages diffusion inpainting through two key conditioning inputs: static scene renderings following a specified camera trajectory to ensure spatial consistency, and egocentric hand mesh renderings that encode both geometry and motion cues in the egocentric view to model action-conditioned dynamics directly.

### Inpainting Strategy

A core idea behind the formulation is to model only the residual dynamics caused by human actions while preserving all unaltered regions, and the model is initialized from a pretrained video inpainting diffusion model. The model takes a text prompt as an additional conditioning signal.

### Capabilities

The model synthesizes physically plausible interactions in which hand actions induce consistent scene changes, such as object displacement or articulation. Notably, DWM-generated human-scene interaction videos can be converted to robot-scene interaction videos.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ffd9a24-b4f6-4954-81b1-e9c07a9cdc6a",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "a8a15a61-9e84-4e23-86a8-f5b808d4852a",
  "sourceToolAssistantUUID": "8ffd9a24-b4f6-4954-81b1-e9c07a9cdc6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-10T20:27:05.751Z_

Now let me do a final round of very targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8a15a61-9e84-4e23-86a8-f5b808d4852a",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWyHv9LcdfStCFcXN4F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e64b6cc-840e-43db-b1bc-1c751ea88b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BKs4UuTTadH6ZcZWCtAid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 41961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3867,
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

_source line 88 · 2026-05-10T20:27:06.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EWwrcLYtyyJCE91at4MUmV`</summary>

```json
{
  "query": "\"learning whole-body humanoid locomotion\" motion generation tracking diffusion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e64b6cc-840e-43db-b1bc-1c751ea88b2e",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWyHv9LcdfStCFcXN4F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58c5195c-27c3-4f2d-bd42-e135f3e802e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BKs4UuTTadH6ZcZWCtAid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 41961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3867,
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

_source line 89 · 2026-05-10T20:27:07.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017mnNvKCr6MFtCHAse9KeSo`</summary>

```json
{
  "query": "compositional diffusion robotics body part decomposition trajectory 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58c5195c-27c3-4f2d-bd42-e135f3e802e4",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWyHv9LcdfStCFcXN4F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ded0622-66f0-419f-9cfa-ef227aeef50c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BKs4UuTTadH6ZcZWCtAid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 41961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3867,
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

_source line 90 · 2026-05-10T20:27:07.689Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QhgnEUDfEDJsDr6eG5JNN9`</summary>

```json
{
  "query": "prosthetic hand natural gesture diffusion inpainting body part"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ded0622-66f0-419f-9cfa-ef227aeef50c",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWyHv9LcdfStCFcXN4F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f431466e-6c89-4cf7-9f25-74aa8fe1fe18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BKs4UuTTadH6ZcZWCtAid",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 41961,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3867
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 41961,
          "cache_creation_input_tokens": 3867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3867,
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

_source line 91 · 2026-05-10T20:27:14.271Z_

<details><summary>↩ Tool result · `toolu_017mnNvKCr6MFtCHAse9KeSo`</summary>

```text
Web search results for query: "compositional diffusion robotics body part decomposition trajectory 2025 2026"

Links: [{"title":"Boosting Offline MARL under Imbalanced Datasets via ...","url":"https://www.lamda.nju.edu.cn/lilh/file/codi.pdf"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Generative Trajectory Stitching through Diffusion Composition","url":"https://comp-diffuser.github.io/"},{"title":"Generative Trajectory Stitching through Diffusion Composition","url":"https://arxiv.org/html/2503.05153v1"},{"title":"GitHub - mbreuss/diffusion-literature-for-robotics: Summary of key papers and blogs about diffusion models to learn about the topic. Detailed list of all published diffusion robotics papers. · GitHub","url":"https://github.com/mbreuss/diffusion-literature-for-robotics"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"MULTI-ROBOT MOTION PLANNING WITH DIFFUSION ...","url":"http://irl.cs.brown.edu/pubs/mrmp_diffusion.pdf"},{"title":"compositional world models empowering robot imitation ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0d446441a938d9de420a8ab8d7fd36-Paper-Conference.pdf"},{"title":"Compositional Diffusion Models for Powered Descent Trajectory Generation with Flexible Constraints - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004261B/abstract"}]

I've completed the web search for your query about compositional diffusion robotics, body part decomposition, and trajectory generation in 2025-2026. Here are the key findings:

## Recent Research (2025-2026)

CompDiffuser is a novel generative approach that can solve new tasks by learning to compositionally stitch together shorter trajectory chunks from previously seen tasks. It models the trajectory distribution by subdividing it into overlapping chunks and learning their conditional relationships through a single bidirectional diffusion model, allowing information to propagate between segments during generation and ensuring physically consistent connections.

Surveys on diffusion models in robotic manipulation cover grasp learning, trajectory planning, and data augmentation. Skill-composition is a common method to handle long-horizon tasks.

## Related Compositional World Models

Researchers leverage foundational models to automatically create a compositional world model and show the effectiveness of using transformed demonstrations for task learning without requiring extensive interaction with the world model.

## Multi-Agent Approaches

Compositional diffusion training enables more targeted approaches to quality improvement by preserving high-quality behaviors from other agents and their sub-trajectories.

The research shows active development in compositional diffusion approaches for robotics, with emphasis on trajectory generation, skill composition, and body/agent-level decomposition methods for improved task generalization and long-horizon planning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ded0622-66f0-419f-9cfa-ef227aeef50c",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "c697b1c5-5822-4361-9d9e-c58be5698bfd",
  "sourceToolAssistantUUID": "9ded0622-66f0-419f-9cfa-ef227aeef50c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-10T20:27:14.507Z_

<details><summary>↩ Tool result · `toolu_01EWwrcLYtyyJCE91at4MUmV`</summary>

```text
Web search results for query: ""learning whole-body humanoid locomotion" motion generation tracking diffusion 2026"

Links: [{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"[2604.17335] Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/abs/2604.17335"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning","url":"https://arxiv.org/html/2504.14305v2"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning","url":"https://arxiv.org/html/2510.05070v1"},{"title":"Scalable and General Whole-Body Control for Cross-Humanoid Locomotion","url":"https://arxiv.org/html/2602.05791v2"},{"title":"Natural Humanoid Robot Locomotion with Generative Motion Prior","url":"https://arxiv.org/html/2503.09015v1"},{"title":"Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning | OpenReview","url":"https://openreview.net/forum?id=hVoIz6xD9Q"},{"title":"BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion","url":"https://arxiv.org/html/2508.08241v3"}]

The search results show recent research on humanoid robot control combining motion generation and tracking with diffusion models. Here are the key findings:

## Main Research Approach

A recent framework trains a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions, and concurrently trains a whole-body reference tracker with reinforcement learning using this motion data.

## Key Challenge and Solution

Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need for real-time adaptation to various terrains, with reinforcement learning directly often leading to lower-body-dominated behaviors. The proposed system adapts a motion generation and motion tracking framework to real-time robot control, combining diffusion-based motion generation with RL-based motion tracking and repurposing coordinated human whole-body skills for perceptive humanoid locomotion.

## Real-World Deployment

The system supports directional goal-reaching control with terrain-aware whole-body adaptation and can be deployed on a Unitree G1 humanoid robot with onboard perception and computation, demonstrating successful traversal over boxes, hurdles, stairs, and mixed terrain combinations.

The research demonstrates that combining diffusion-based motion generation with reinforcement learning-based tracking provides an effective approach for achieving natural, adaptive whole-body humanoid locomotion across diverse terrain conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58c5195c-27c3-4f2d-bd42-e135f3e802e4",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "259d2054-18b7-4b07-87c9-46c5cb1bc751",
  "sourceToolAssistantUUID": "58c5195c-27c3-4f2d-bd42-e135f3e802e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-10T20:27:15.514Z_

<details><summary>↩ Tool result · `toolu_01QhgnEUDfEDJsDr6eG5JNN9`</summary>

```text
Web search results for query: "prosthetic hand natural gesture diffusion inpainting body part"

Links: [{"title":"Towards Natural Prosthetic Hand Gestures: A Common-Rig and Diffusion Inpainting Pipeline","url":"https://kaseungyup.github.io/natural-prosthetic-hand-gestures/"},{"title":"Towards Natural Prosthetic Hand Gestures: A Common-Rig and Diffusion Inpainting Pipeline | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10782646"},{"title":"Towards Natural Prosthetic Hand Gestures: A Common-Rig and Diffusion Inpainting Pipeline","url":"https://www.researchgate.net/publication/387152739_Towards_Natural_Prosthetic_Hand_Gestures_A_Common-Rig_and_Diffusion_Inpainting_Pipeline"},{"title":"HandRefiner: Refining Malformed Hands in Generated Images by Diffusion-based Conditional Inpainting","url":"https://arxiv.org/html/2311.17957v2"},{"title":"Stable Diffusion Fix Hands With ControlNet and Inpainting (Easy Method) - YouTube","url":"https://www.youtube.com/watch?v=ikicWPlb1CI"},{"title":"Stable Diffusion Tutorial: Fixing hands and details with Inpainting - YouTube","url":"https://www.youtube.com/watch?v=gu9z_42B934"},{"title":"HandCraft: Anatomically Correct Restoration of Malformed Hands in Diffusion Generated Images","url":"https://arxiv.org/html/2411.04332v1"},{"title":"A Comprehensive Guide to Inpainting: Part 2, Advanced Concepts and Hands | Civitai","url":"https://civitai.com/articles/2294/a-comprehensive-guide-to-inpainting-part-2-advanced-concepts-and-hands"},{"title":"Stable Diffusion Fix Hands Without ControlNet and Inpainting (Easy) | SDXL FREE! (Automatic1111)","url":"https://stablediffusion3.net/blog-Stable-Diffusion-Fix-Hands-Without-ControlNet-and-Inpainting-Easy-SDXL-FREE-Automatic1111-39374"},{"title":"How to remove extra limbs with Stable Diffusion inpainting - Stable Diffusion Art","url":"https://stable-diffusion-art.com/inpainting-remove-extra-limbs/"}]

I found search results related to your query. Here's what the research shows:

## Primary Research Topic

The most directly relevant result is "Towards Natural Prosthetic Hand Gestures," which proposes a pipeline for generating hand motion from body motion via using the Common-Rig, a kinematic rig representation, and a diffusion-based inpainting method. 

## Key Methodology

Common rigging is applied to a motion capture dataset with both body and hands information, and hand motions are generated while conditioned on the body motions of a hand-zeroed test set. More specifically, a diffusion-based inpainting method is utilized to generate the missing hand motions from body-only motion.

## Results and Application

Achieving specific hand movements, such as pointing the index finger, are desired but research on generating the hand movement itself has yet to be widely explored. The research addresses this gap, with the generated hand motions being validated on a real robotic system consisting of a dual-arm system with prosthetic hands.

## Related Research

The search also returned results on hand inpainting in image generation, including methods like HandRefiner and HandCraft that use diffusion-based approaches to correct and generate realistic hands in AI-generated images, though these focus on visual generation rather than motion generation for prosthetics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f431466e-6c89-4cf7-9f25-74aa8fe1fe18",
  "isSidechain": true,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "agentId": "a7ec97cca13734ab9",
  "type": "user",
  "uuid": "c8fe1ef3-67c1-4b4f-afe7-a2a3d2534753",
  "sourceToolAssistantUUID": "f431466e-6c89-4cf7-9f25-74aa8fe1fe18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 94 · 2026-05-10T20:28:53.032Z_

I now have comprehensive results. Here is my full report of all relevant and competing work found:

---

## Comprehensive Literature Search Results

### Category 1: Compositional Body-Part Motion Generation (2024-2026)

**FrankenMotion: Part-level Human Motion Generation and Composition** (arXiv, January 2026)
- A transformer-based diffusion model that accepts sequence-level, action-level, AND part-level text prompts. It constructs a dataset with atomic, temporally-aware part-level annotations using LLMs. This is the MOST DIRECTLY competing work -- it explicitly decomposes motion by body parts and generates part-conditioned motion using diffusion. First to provide atomic, temporally-aware part-level motion annotations.
- [Paper](https://arxiv.org/abs/2601.10909) | [Project](https://coral79.github.io/frankenmotion/)

**EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space** (CVPR 2025)
- Uses energy-based composition of multiple diffusion models in latent space for compositional motion. Introduces "Synergistic Energy Fusion" to combine multiple energy terms corresponding to text descriptions. Achieves concept conjunction, negation, and multi-concept composition.
- [Paper](https://arxiv.org/abs/2412.14706) | [Project](https://jiro-zhang.github.io/EnergyMoGen/)

**DeMoGen: Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models** (arXiv, December 2025)
- Inverse of composition: decomposes holistic motion into semantically meaningful sub-components using an energy-based diffusion model. Three training variants (explicit decomposition, orthogonal self-supervised, semantic consistency). Enables disentangling reusable motion primitives from complex sequences.
- [Paper](https://arxiv.org/abs/2512.22324) | [Project](https://jiro-zhang.github.io/DeMoGen/)

**SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation** (ICCV 2023)
- Uses GPT-3 to map actions to body parts, then combines body parts from two motions. Creates synthetic compositional training data. Earlier foundational work on spatial composition of body parts.
- [Paper](https://arxiv.org/abs/2304.10417)

**Motion Composition Diffusion (MCD): Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models** (arXiv, September 2024)
- Decomposes complex actions into sub-movements via GPT, processes each individually during denoising, then combines. Handles both temporal and spatial composition. Agnostic to spatial overlap, no need for body-part specification.
- [Paper](https://arxiv.org/abs/2409.11920)

**STMC: Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation** (CVPR Workshop 2024)
- Multi-track timeline with overlapping text prompts. At each denoising step, processes each timeline interval individually, then aggregates predictions with consideration for specific body parts engaged. Test-time method compatible with any pre-trained motion diffusion model.
- [Paper](https://arxiv.org/abs/2401.08559) | [GitHub](https://github.com/nv-tlabs/stmc)

**BA-IDM: Body-Aware Diffusion for 3D Human Motion Generation** (MMAsia 2025)
- Divides body into five parts (head, left arm, right arm, spine, legs). Maps complex text instructions to specific body parts. Includes RL and conditional guidance for stable generation in complex scenes.
- [Paper](https://dl.acm.org/doi/10.1145/3743093.3770934)

**Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions** (arXiv, April 2026)
- Plug-and-play adapter that computes decoupled cross-attention maps serving as structural masks during denoising. Trained on single-action motions only. Addresses catastrophic neglect and attention collapse. Very recent.
- [Paper](https://arxiv.org/html/2604.16135v1)

**FineMoGen: Fine-Grained Spatio-Temporal Motion Generation and Editing** (NeurIPS area)
- Builds a Spatio-Temporal Mixture Attention (SAMI) architecture for explicit spatial-temporal composition constraints.
- [Paper](https://arxiv.org/abs/2312.15004)

---

### Category 2: Iterative/Sequential Conditional Generation in Diffusion

**CompDiffuser: Generative Trajectory Stitching through Diffusion Composition** (arXiv, March 2025)
- Autoregressive sampling of multiple short-horizon diffusion models, stitching them into longer trajectories. Uses noise-conditioned score function formulation. Models overlapping chunks with conditional relationships via a single bidirectional diffusion model. Tested on 50D humanoid (HumanoidMaze).
- [Paper](https://arxiv.org/abs/2503.05153) | [Project](https://comp-diffuser.github.io/)

**DartControl (DART): A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control** (2024)
- Autoregressive latent diffusion for motion primitive generation, jointly conditioned on text prompts and motion history. Supports spatial constraints, waypoint goal reaching, and in-betweening.
- [Paper](https://zkf1997.github.io/DART/)

**MotionStreamer: Streaming Motion Generation via Diffusion-based Autoregressive Model in Causal Latent Space** (ICCV 2025)
- Continuous causal latent space with probabilistic autoregressive model. Supports multi-round generation, long-term generation, and dynamic motion composition.
- [Paper](https://arxiv.org/abs/2503.15451)

---

### Category 3: Inpainting/Masking in Motion Diffusion

**MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting** (NVIDIA, ACM TOG 2024)
- HIGHLY RELEVANT. Formulates physics-based character control as motion inpainting. Single unified model synthesizes motions from partial (masked) motion descriptions -- masked keyframes, objects, text, or combinations. Supports partial joint targets, joystick control, text commands, and multi-modal composition.
- [Paper](https://arxiv.org/abs/2409.14393) | [Project](https://research.nvidia.com/labs/par/maskedmimic/)

**CondMDI: Flexible Motion In-betweening with Diffusion Models** (SIGGRAPH 2024)
- Trains on randomly sampled keyframes with randomly sampled joints and a mask indicating observations. Supports partial keyframe constraints (subset of joints). Replaces noisy input with given keyframes and concatenates observation mask.
- [Paper](https://arxiv.org/abs/2405.11126)

**COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation** (ECCV 2024)
- Soft inpainting strategy that identifies high-confidence regions and uses them as soft constraints while re-sampling low-confidence regions from scratch.
- [Paper](https://arxiv.org/html/2408.16426)

**MDM: Human Motion Diffusion Model** (ICLR 2023)
- Original work demonstrating inpainting in joint space for semantic editing of specific body parts.
- [Paper](https://guytevet.github.io/mdm-page/)

**Towards Natural Prosthetic Hand Gestures: A Common-Rig and Diffusion Inpainting Pipeline** (IEEE, 2024)
- Directly relevant: generates hand motion from body motion via diffusion-based inpainting on a common kinematic rig. Conditions hand generation on body-only motion. Validated on a real robotic system.
- [Paper](https://kaseungyup.github.io/natural-prosthetic-hand-gestures/)

---

### Category 4: Robot-Specific Motion Diffusion

**RobotMDM: Robot Motion Diffusion Model** (SIGGRAPH Asia 2024, Disney Research)
- Integrates kinematic generative motion models with physics-based character control. Generalizes across human, non-human, and synthetic morphologies. Tested on a bipedal robot (20 DoF).
- [Paper](https://dl.acm.org/doi/10.1145/3680528.3687626)

**DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning** (CoRL 2025)
- Uses diffusion to generate trajectory seeds for motion optimization. 12x speed-up on average. Sim2real on Franka robot.
- [Paper](https://arxiv.org/abs/2410.16727)

**CoDiG: Constraint-Aware Diffusion Guidance for Robotics** (arXiv, May 2025)
- Integrates barrier functions into denoising to guide toward constraint-satisfying outputs. Real-world racing experiments.
- [Paper](https://arxiv.org/abs/2505.13131)

**Diffusion Predictive Control with Constraints** (arXiv, December 2024)
- Model-based projections in trajectory denoising for constraint-satisfying, dynamically feasible trajectories.
- [Paper](https://arxiv.org/html/2412.09342)

---

### Category 5: Kimodo Ecosystem and Extensions

**Kimodo: Scaling Controllable Human Motion Generation** (NVIDIA, March 16, 2026)
- Kinematic motion diffusion model trained on 700 hours of mocap (BONES-RigPlay). Five model variants (SOMA, G1, SMPL-X). Supports text + full-body keyframes, sparse joint positions/rotations, 2D waypoints, dense 2D paths. Two-stage denoiser separating root and body prediction. Open-source code, closed data.
- Updates: v1.1 models + benchmark (April 10, 2026); multi-prompt improvements (April 24, 2026).
- Integrated into GEAR-SONIC interactive demo.
- [Project](https://research.nvidia.com/labs/sil/projects/kimodo/) | [GitHub](https://github.com/nv-tlabs/kimodo)

**BONES-SEED (Skeletal Everyday Embodiment Dataset)** (Bones Studio, March 2026)
- 142,220 annotated motion animations for humanoid robotics. SOMA and Unitree G1 formats. 288 hours publicly available.
- [Dataset](https://huggingface.co/datasets/bones-studio/seed)

**GR00T Whole-Body Control** (NVIDIA, 2025-2026)
- Unified platform for humanoid controllers, connected to Kimodo for motion generation.
- [GitHub](https://github.com/NVlabs/GR00T-WholeBodyControl)

---

### Category 6: Concurrent Humanoid Data Generation via Diffusion (2025-2026)

**NVIDIA Synthetic Motion Generation Pipeline** (2026)
- 780K synthetic trajectories in 11 hours from recorded demonstrations. Improved GR00T N1 performance by 40%. Combines real + synthetic data.
- [Blog](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/)

**HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning** (OpenReview, 2026)
- Automated task creation and demonstration collection using atomic dexterous skills + LLM reasoning. Shows scaling of 2D/3D diffusion policies with generated data.
- [Paper](https://openreview.net/forum?id=Mk9ykil8eP)

**Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions** (CoRL 2025)
- Multi-stage pipeline: PhysDiff (diffusion-based) generates human motion from text, then retargets to humanoid robot (Fourier GR1), then VLM edits finger/head motions. 86.7% human preference rate.
- [Paper](https://arxiv.org/abs/2410.12773) | [Project](https://ut-austin-rpl.github.io/Harmon/)

**BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion** (arXiv, August 2025)
- Unified diffusion policy for humanoid control. Uses classifier guidance for zero-shot task-specific control. Supports motion inpainting, joystick teleoperation, obstacle avoidance. Deployed on real hardware.
- [Paper](https://arxiv.org/abs/2508.08241)

**Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking** (arXiv, April 2026)
- Trains diffusion model on retargeted human motions for real-time terrain-aware reference motion prediction. Concurrent RL-based whole-body tracker. Deployed on Unitree G1.
- [Paper](https://arxiv.org/abs/2604.17335)

**PHUMA: Physically-Grounded Humanoid Locomotion Dataset** (ICLR 2026)
- Physics-constrained retargeting (PhySINK) from human video. Outperforms Humanoid-X and AMASS datasets.
- [Paper](https://arxiv.org/abs/2510.26236)

**Dexterous World Models (DWM)** (arXiv, December 2025)
- Video diffusion framework using inpainting to model how dexterous hand actions change 3D scenes. Initialized from pretrained video inpainting model. Converts human-scene interaction videos to robot-scene interaction.
- [Paper](https://arxiv.org/abs/2512.17907)

---

### Key Papers the Proposal Likely Needs to Address

The papers most likely to be missed and most directly relevant to a "compositional humanoid trajectory generation using body-part inpainting on diffusion models" proposal are:

1. **FrankenMotion** (Jan 2026) -- Part-level motion generation with diffusion, extremely close in concept
2. **MaskedMimic** (NVIDIA, 2024) -- Motion inpainting with partial/masked body joint specifications in a physics-based diffusion setting
3. **CondMDI** (SIGGRAPH 2024) -- Masked joint diffusion conditioning
4. **STMC** (CVPR Workshop 2024) -- Body-part-aware denoising aggregation at test time
5. **EnergyMoGen / DeMoGen** (CVPR 2025 / Dec 2025) -- Energy-based compositional/decompositional alternatives
6. **Motion-Adapter** (April 2026) -- Very recent structural masking approach for compound actions
7. **BeyondMimic** (Aug 2025) -- Diffusion-based humanoid control with motion inpainting capability
8. **Harmon** (CoRL 2025) -- Diffusion-based whole-body humanoid motion generation from language
9. **Prosthetic Hand Gestures pipeline** (2024) -- Body-part inpainting on kinematic rig for robot hands
10. **Kimodo v1.1** (April 2026) -- Benchmarks and multi-prompt support may overlap with compositional approach

Sources:
- [FrankenMotion](https://arxiv.org/abs/2601.10909)
- [EnergyMoGen](https://arxiv.org/abs/2412.14706)
- [DeMoGen](https://arxiv.org/abs/2512.22324)
- [SINC](https://arxiv.org/abs/2304.10417)
- [MCD](https://arxiv.org/abs/2409.11920)
- [STMC](https://arxiv.org/abs/2401.08559)
- [BA-IDM](https://dl.acm.org/doi/10.1145/3743093.3770934)
- [Motion-Adapter](https://arxiv.org/html/2604.16135v1)
- [FineMoGen](https://arxiv.org/abs/2312.15004)
- [CompDiffuser](https://arxiv.org/abs/2503.05153)
- [DartControl](https://zkf1997.github.io/DART/)
- [MotionStreamer](https://arxiv.org/abs/2503.15451)
- [MaskedMimic](https://arxiv.org/abs/2409.14393)
- [CondMDI](https://arxiv.org/abs/2405.11126)
- [COIN](https://arxiv.org/html/2408.16426)
- [MDM](https://guytevet.github.io/mdm-page/)
- [Prosthetic Hand Gestures](https://kaseungyup.github.io/natural-prosthetic-hand-gestures/)
- [RobotMDM](https://dl.acm.org/doi/10.1145/3680528.3687626)
- [DiffusionSeeder](https://arxiv.org/abs/2410.16727)
- [CoDiG](https://arxiv.org/abs/2505.13131)
- [Diffusion Predictive Control](https://arxiv.org/html/2412.09342)
- [Kimodo](https://research.nvidia.com/labs/sil/projects/kimodo/)
- [BONES-SEED](https://huggingface.co/datasets/bones-studio/seed)
- [GR00T WBC](https://github.com/NVlabs/GR00T-WholeBodyControl)
- [NVIDIA Synthetic Pipeline](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/)
- [HumanoidGen](https://openreview.net/forum?id=Mk9ykil8eP)
- [Harmon](https://arxiv.org/abs/2410.12773)
- [BeyondMimic](https://arxiv.org/abs/2508.08241)
- [Whole-Body Humanoid Locomotion](https://arxiv.org/abs/2604.17335)
- [PHUMA](https://arxiv.org/abs/2510.26236)
- [Dexterous World Models](https://arxiv.org/abs/2512.17907)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8fe1ef3-67c1-4b4f-afe7-a2a3d2534753",
  "isSidechain": true,
  "agentId": "a7ec97cca13734ab9",
  "requestId": "req_011CauWzGQPSYwWytmhdrNDf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6462f63-b389-4310-8e15-6ca90c65737d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmZeX7TvKyWFSpfV5W1Ymx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 45828,
      "output_tokens": 4607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2908
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4607,
          "cache_read_input_tokens": 45828,
          "cache_creation_input_tokens": 2908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2908,
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
