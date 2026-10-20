# Research conversation: I'm reviewing a research proposal about adaptive inference for World-Action Models (WAMs) that claims to be novel in pro

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-adcca2df099752510.jsonl`
- **Structured JSON:** [`27cf035ab00c5e84b4ae.json`](../../sessions/27/27cf035ab00c5e84b4ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

56 recorded events

### User

_source line 1 · 2026-05-10T19:37:04.571Z_

I'm reviewing a research proposal about adaptive inference for World-Action Models (WAMs) that claims to be novel in providing "cross-modal self-correction" during denoising. I need to find any competing or concurrent work the proposal may have missed.

Use WebSearch to search for:

1. "adaptive denoising steps world model robot" 2025-2026
2. "cross-modal convergence diffusion" 2025-2026
3. "quality guarantee diffusion policy inference" 2025-2026
4. "self-correcting diffusion inference" 2025-2026
5. "adaptive inference world action model" 2026
6. site:arxiv.org "world action model" acceleration 2026
7. site:arxiv.org "diffusion policy" adaptive steps 2026
8. "convergence caching" diffusion 2026

Report any papers that seem to do something similar to: monitoring per-modality convergence signals during joint video+action denoising to adaptively allocate or extend denoising steps, especially with quality floor guarantees. Also report any papers about adaptive step allocation for multi-modal diffusion models in general.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "87339f30-ac2f-4d42-a1ee-34197c543430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:37:04.574Z_

```json
{
  "parentUuid": "87339f30-ac2f-4d42-a1ee-34197c543430",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
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
  "uuid": "65f0e691-5da1-4726-92f6-2f42a92eaa03",
  "timestamp": "2026-05-10T19:37:04.574Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:37:08.456Z_



I'll search for competing and concurrent work across all these queries. Let me start by loading the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65f0e691-5da1-4726-92f6-2f42a92eaa03",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTAKKa3zBzRRvKiJJoS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00329bc2-f7a1-4bad-8194-6766e089aebd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSpYxUUJTLskHugjcq76QU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
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

_source line 4 · 2026-05-10T19:37:10.575Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HWYb5DZLZickxxVLdQXLot`</summary>

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
  "parentUuid": "00329bc2-f7a1-4bad-8194-6766e089aebd",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTAKKa3zBzRRvKiJJoS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "696157db-a600-431e-9c2e-acbea7add8fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSpYxUUJTLskHugjcq76QU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
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

_source line 5 · 2026-05-10T19:37:10.578Z_

<details><summary>↩ Tool result · `toolu_01HWYb5DZLZickxxVLdQXLot`</summary>

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
  "parentUuid": "696157db-a600-431e-9c2e-acbea7add8fd",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "6e455930-e1b3-47a5-9a84-a58d56a193b4",
  "sourceToolAssistantUUID": "696157db-a600-431e-9c2e-acbea7add8fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:37:13.665Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e455930-e1b3-47a5-9a84-a58d56a193b4",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTAmWAbSGyrnsXwt1bP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0776d20-8962-47b0-b45c-3ce83dc8b2c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkgoiRgaT7pBenCMRFUcf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 7 · 2026-05-10T19:37:14.628Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011ZpkJmkbmfW5DX7AzymRBY`</summary>

```json
{
  "query": "\"adaptive denoising steps world model robot\" 2025-2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0776d20-8962-47b0-b45c-3ce83dc8b2c2",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTAmWAbSGyrnsXwt1bP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5893c7e5-5eaa-4d24-bac6-c749dc6187fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkgoiRgaT7pBenCMRFUcf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 8 · 2026-05-10T19:37:15.096Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U1Uo3DirKH9pyFuiJ4rzF6`</summary>

```json
{
  "query": "\"cross-modal convergence diffusion\" 2025-2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5893c7e5-5eaa-4d24-bac6-c749dc6187fe",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTAmWAbSGyrnsXwt1bP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d4ec83e-600e-430e-87ac-f4cc00fc8374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkgoiRgaT7pBenCMRFUcf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 9 · 2026-05-10T19:37:15.563Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JLSTqVrs9YpvNiQTFmmMzd`</summary>

```json
{
  "query": "\"quality guarantee diffusion policy inference\" 2025-2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d4ec83e-600e-430e-87ac-f4cc00fc8374",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTAmWAbSGyrnsXwt1bP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eaa72316-64bb-420a-8e4f-995fe59386fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkgoiRgaT7pBenCMRFUcf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 10 · 2026-05-10T19:37:15.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FUCwN4AHfefAj4bLnxZPz4`</summary>

```json
{
  "query": "\"self-correcting diffusion inference\" 2025-2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaa72316-64bb-420a-8e4f-995fe59386fd",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTAmWAbSGyrnsXwt1bP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42549efe-3c41-4a6d-a315-5a92d27855e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkgoiRgaT7pBenCMRFUcf2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9032,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1418
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 227,
          "cache_read_input_tokens": 9032,
          "cache_creation_input_tokens": 1418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1418,
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

_source line 11 · 2026-05-10T19:37:22.451Z_

<details><summary>↩ Tool result · `toolu_011ZpkJmkbmfW5DX7AzymRBY`</summary>

```text
Web search results for query: ""adaptive denoising steps world model robot" 2025-2026"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://arxiv.org/html/2511.02097v1"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"D3P: Dynamic Denoising Difusion Policy via Reinforcement Learning Shu’ang Yu","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"Ctrl-World: A Controllable Generative World Model for Robot Manipulation","url":"https://arxiv.org/html/2510.10125v1"},{"title":"Interactive World Simulator for Robot Policy Training and Evaluation","url":"https://www.yixuanwang.me/interactive_world_sim/texts/main.pdf"},{"title":"Boosting Offline MARL under Imbalanced Datasets via ...","url":"https://www.lamda.nju.edu.cn/lilh/file/codi.pdf"}]

The search results reveal several recent developments in adaptive denoising steps for world models and robot control. Here are the key findings:

## MotuBrain: Advanced World Action Model

One approach adopts a DreamZero-style DiT caching strategy to exploit temporal redundancy across denoising steps. The system implements denoising-step reduction along with compilation, quantization, and DiT caching techniques, delivering more than 50× end-to-end speedup over the naive baseline and making large world action models practical for real-time robotic deployment.

## X-WAM: Asynchronous Denoising Approach

X-WAM proposes Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency by applying a specialized asynchronous denoising schedule during inference, which rapidly decodes actions with fewer steps.

## D3P: Dynamic Denoising Diffusion Policy

Another approach addresses the number of denoising steps for each action, jointly optimizing an adaptor and base diffusion policy via reinforcement learning to balance task performance and inference efficiency.

## Broader Context

Diffusion-based models generate samples through an iterative denoising process, enabling them to model complex, multi-modal distributions and produce globally coherent sequences, with iterative refinement making them more robust to individual prediction errors. However, diffusion models are computationally intensive and slower during inference.

These recent developments (2025-2026) show significant progress in making adaptive denoising steps more efficient for real-time robot control applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5893c7e5-5eaa-4d24-bac6-c749dc6187fe",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "4b617326-080d-4e13-8a98-da7b0c20ab7d",
  "sourceToolAssistantUUID": "5893c7e5-5eaa-4d24-bac6-c749dc6187fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:37:22.459Z_

<details><summary>↩ Tool result · `toolu_01U1Uo3DirKH9pyFuiJ4rzF6`</summary>

```text
Web search results for query: ""cross-modal convergence diffusion" 2025-2026"

Links: [{"title":"[2604.21836] Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion","url":"https://arxiv.org/abs/2604.21836"},{"title":"A multi-modal diffusion model with dual-cross-attention for multi-omics data generation and translation | Nature Communications","url":"https://www.nature.com/articles/s41467-026-71744-x"},{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf"},{"title":"CMADiff: Cross-Modal Aligned Diffusion for Controllable Protein Generation","url":"https://arxiv.org/html/2503.21450v2"},{"title":"Theoretical Framework, Technical Evolution, and Future Prospects of Cross-Modal Mapping and Controllable Image Generation Under Multi-Source Heterogeneous Collaboration","url":"https://www.mdpi.com/1424-8220/26/10/2972"},{"title":"Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion","url":"https://arxiv.org/html/2604.21836"},{"title":"A Survey on Large Multimodal Models for 3D Vision and Scene ...","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176784330.01281926/v1"},{"title":"Graph-Oriented Cross-Modality Diffusion for Multimedia Recommendation | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-981-95-3453-1_17"},{"title":"Downloads 2025","url":"https://iclr.cc/Downloads/2025"},{"title":"GitHub - donghao51/Awesome-Multimodal-Adaptation: [TPAMI 2026] Advances in Multimodal Adaptation and Generalization: From Traditional Approaches to Foundation Models · GitHub","url":"https://github.com/donghao51/Awesome-Multimodal-Adaptation"}]

I've found several recent research papers on cross-modal convergence and diffusion models from 2025-2026:

## Key Findings:

**Cross-Modal Convergence Studies:**
Research shows that intra-modal dispersion strongly modulates alignment between vision and language models (cross-modal convergence). Specifically, stimuli with low intra-modal dispersion (high agreement among vision models) elicited significantly higher cross-modal alignment than those with high dispersion, by up to a factor of two.

**Multimodal Diffusion Models:**
Researchers developed scDiffusion-X, a multimodal generative diffusion model that generates realistic single-cell multi-omics data, enables cross-modality prediction, and reveals gene regulatory relationships.

**Cross-Modal Aligned Diffusion:**
CMADiff is a novel cross-modal aligned diffusion framework that bridges the gap between protein physicochemical properties and natural language descriptions. By integrating a CVAE-based latent space with the BioAligner module, CMADiff enables intuitive and controllable protein sequence generation.

**Cross-Modal Mapping and Controllable Generation:**
The rapid evolution of diffusion models has shifted visual synthesis from text-only inputs to precisely controlled generation driven by multi-source heterogeneous sensor signals (e.g., audio, 3D, and physiological data).

**Multimodal Diffusion Transformers:**
TACA is a parameter-efficient method that dynamically rebalances cross-modal attention in multimodal diffusion, presented at ICCV 2025.

These recent papers demonstrate active research in combining cross-modal learning with diffusion models for applications ranging from biology to multimedia generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d4ec83e-600e-430e-87ac-f4cc00fc8374",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "e969ccb1-aa0e-4475-a9ea-d615f719184c",
  "sourceToolAssistantUUID": "9d4ec83e-600e-430e-87ac-f4cc00fc8374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:37:22.906Z_

<details><summary>↩ Tool result · `toolu_01JLSTqVrs9YpvNiQTFmmMzd`</summary>

```text
Web search results for query: ""quality guarantee diffusion policy inference" 2025-2026"

Links: [{"title":"Diffusion Models: Mechanism, Benefits, and Types (2026)|ArchiVinci | ArchiVinci","url":"https://www.archivinci.com/blogs/diffusion-models-guide"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"Why Diffusion Models Could Change Developer Workflows in 2026 | The JetBrains AI Blog","url":"https://blog.jetbrains.com/ai/2025/11/why-diffusion-models-could-change-developer-workflows-in-2026/"},{"title":"Diffusion Policy Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=mEpqHvbD2h"},{"title":"Measuring policy diffusion intensity: A text-driven analysis of government documents - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325003243"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://arxiv.org/pdf/2303.04137"},{"title":"Frontiers | Quantitative analysis of the diffusion characteristics of China's long-term care insurance policy based on the PMC index model","url":"https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1467062/full"},{"title":"News - NESA - Network System Security & Privacy Lab","url":"https://nesa.zju.edu.cn/webpage/news.html"},{"title":"Downloads 2025","url":"https://iclr.cc/Downloads/2025"}]

Based on the search results, I found relevant information about diffusion policy and inference from 2025-2026. Here's what the research shows:

## Diffusion Policy and Quality in 2025-2026

Diffusion Policy is a new way of generating robot behavior that consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9% across 15 different tasks from 4 different robot manipulation benchmarks.

### Inference Quality and Speed

Traditional DDPMs can require over a thousand steps making inference slow, while DDIMs and newer approaches cut this to a few dozen without major quality loss. Recent acceleration methods achieve near-real-time generation in as few as four steps, balancing speed with precision depending on the target use case.

### Policy Optimization Advances (2025)

Diffusion Policy Policy Optimization (DPPO) is an algorithmic framework including best practices for fine-tuning diffusion-based policies in continuous control and robot learning tasks using policy gradient methods from reinforcement learning. DPPO achieves the strongest overall performance and efficiency for fine-tuning in common benchmarks compared to other RL methods for diffusion-based policies.

### Key Advantages

The diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaa72316-64bb-420a-8e4f-995fe59386fd",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "5a81bddd-887c-4da6-a2ba-661e2d6629ac",
  "sourceToolAssistantUUID": "eaa72316-64bb-420a-8e4f-995fe59386fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:37:24.830Z_

<details><summary>↩ Tool result · `toolu_01FUCwN4AHfefAj4bLnxZPz4`</summary>

```text
Web search results for query: ""self-correcting diffusion inference" 2025-2026"

Links: [{"title":"Generalized Discrete Diffusion with Self-Correction","url":"https://arxiv.org/html/2603.02230"},{"title":"Improving faithfulness of text-to-image diffusion models through inference intervention - Amazon Science","url":"https://www.amazon.science/publications/improving-faithfulness-of-text-to-image-diffusion-models-through-inference-intervention"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"[2603.02230] Generalized Discrete Diffusion with Self-Correction","url":"https://arxiv.org/abs/2603.02230"},{"title":"Why Diffusion Models Could Change Developer Workflows in 2026 | The JetBrains AI Blog","url":"https://blog.jetbrains.com/ai/2025/11/why-diffusion-models-could-change-developer-workflows-in-2026/"},{"title":"GitHub - moatifbutt/awesome-diffusion-iclr-2025: List of diffusion related active submissions on OpenReview for ICLR 2025. · GitHub","url":"https://github.com/moatifbutt/awesome-diffusion-iclr-2025"},{"title":"Inference-stage Adaptation-projection Strategy Adapts Diffusion Policy to Cross-manipulators Scenarios","url":"https://arxiv.org/html/2509.11621v1"},{"title":"Comprehensive exploration of diffusion models in image generation: a survey | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11110-3"},{"title":"GitHub - 52CV/CVPR-2025-Papers · GitHub","url":"https://github.com/52CV/CVPR-2025-Papers"},{"title":"Mode-seeking for inverse problems with diffusion models | OpenReview","url":"https://openreview.net/forum?id=lRQCpF1paA"}]

I found several results related to self-correcting diffusion inference from 2025-2026. Here's what the search revealed:

## Recent Research on Self-Correcting Diffusion Inference

**Generalized Discrete Diffusion with Self-Correction (SCDD)**

A Self-Correcting Discrete Diffusion (SCDD) model has been proposed to reformulate pretrained self-correction with explicit state transitions and learn directly in discrete time. Self-correction is an effective technique for maintaining parallel sampling in discrete diffusion models with minimal performance degradation.

This recent work (submitted February 13, 2026) addresses limitations in earlier approaches. Prior work has explored self-correction at inference time or during post-training; however, such approaches often suffer from limited generalization and may impair reasoning performance.

**Key Features of SCDD:**

During inference, SCDD requires no post-hoc heuristic samplers and no hyperparameter-tuning, with all token generation and correction performed solely by running the backward process derived from Bayes' rule. Experiments at the GPT-2 scale indicate that the model consistently surpasses existing benchmarks over standard datasets, achieving lower generative perplexity without sacrificing sample diversity in parallel generation settings.

**Other Applications of Inference-Time Diffusion Correction**

Beyond language models, researchers have proposed an intervention-based mechanism to enhance the faithfulness of diffusion models by controlling the denoising process, detecting incorrectly-generated/missing objects during denoising steps, constructing a layout from the erroneous objects, returning to an earlier denoising step, and feeding the new layout to obtain its latent representation, with correction applied by composing the new latents with the original ones to drive the generation away from erroneous directions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42549efe-3c41-4a6d-a315-5a92d27855e6",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "87af9a05-1ab3-4b0a-af43-eb121f1e8cfc",
  "sourceToolAssistantUUID": "42549efe-3c41-4a6d-a315-5a92d27855e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T19:37:28.332Z_

Good, I'm getting highly relevant results. Let me run the remaining 4 searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87af9a05-1ab3-4b0a-af43-eb121f1e8cfc",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTBow3WN66zvsVmn1b7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72ec4613-c5f5-4472-aead-6b0783d79133",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CDX6PtBcyCxiP9ehknBFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4041,
      "cache_read_input_tokens": 10450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4041,
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

_source line 16 · 2026-05-10T19:37:29.342Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EwVjK5ftL9TBB4C3EqsSJP`</summary>

```json
{
  "query": "\"adaptive inference world action model\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72ec4613-c5f5-4472-aead-6b0783d79133",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTBow3WN66zvsVmn1b7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efaa64ea-341e-4d6e-aeff-c81287341d74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CDX6PtBcyCxiP9ehknBFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4041,
      "cache_read_input_tokens": 10450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4041,
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

_source line 17 · 2026-05-10T19:37:29.816Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N73kdJSNiizJCL4cez8RcQ`</summary>

```json
{
  "query": "site:arxiv.org \"world action model\" acceleration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efaa64ea-341e-4d6e-aeff-c81287341d74",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTBow3WN66zvsVmn1b7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50e52564-28c1-4e42-b575-7fe85ac0c93b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CDX6PtBcyCxiP9ehknBFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4041,
      "cache_read_input_tokens": 10450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4041,
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

_source line 18 · 2026-05-10T19:37:30.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GeKKnHg5otZCkcGyF9KLFj`</summary>

```json
{
  "query": "site:arxiv.org \"diffusion policy\" adaptive steps 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50e52564-28c1-4e42-b575-7fe85ac0c93b",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTBow3WN66zvsVmn1b7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f4fc26d-6b42-4589-a507-9e246faa7281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CDX6PtBcyCxiP9ehknBFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4041,
      "cache_read_input_tokens": 10450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4041,
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

_source line 19 · 2026-05-10T19:37:30.647Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018g1PriYJjJp3kiBfRH71rY`</summary>

```json
{
  "query": "\"convergence caching\" diffusion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f4fc26d-6b42-4589-a507-9e246faa7281",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTBow3WN66zvsVmn1b7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7054e426-2913-4f7a-8fc3-0f39bd0ab8e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CDX6PtBcyCxiP9ehknBFm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4041,
      "cache_read_input_tokens": 10450,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4041
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 225,
          "cache_read_input_tokens": 10450,
          "cache_creation_input_tokens": 4041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4041,
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

_source line 20 · 2026-05-10T19:37:36.732Z_

<details><summary>↩ Tool result · `toolu_01EwVjK5ftL9TBB4C3EqsSJP`</summary>

```text
Web search results for query: ""adaptive inference world action model" 2026"

Links: [{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"Flying by Inference: Active Inference World Models for Adaptive UAV Swarms","url":"https://arxiv.org/html/2604.27935"},{"title":"[2605.06222] When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/abs/2605.06222"},{"title":"[2604.14732] World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems","url":"https://arxiv.org/abs/2604.14732"},{"title":"𝐴₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/html/2604.05672"},{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"World Guidance: World Modeling in Condition Space for Action Generation","url":"https://arxiv.org/html/2602.22010v1"},{"title":"A Comprehensive Survey on World Models for Embodied AI","url":"https://arxiv.org/html/2510.16732v1"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"}]

Based on the search results, here are the recent developments in adaptive inference with world action models from 2026:

## Key Research Areas

**Adaptive Action Execution for World Action Models**

World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation by jointly predicting future visual observations and future actions. However, current WAMs typically execute a fixed number of predicted actions after each model inference, leaving the robot blind to whether the imagined future remains consistent with the actual physical rollout.

Recent work formulates adaptive WAM execution as a future–reality verification problem: the robot should execute longer when the WAM-predicted future remains reliable, and replan earlier when reality deviates from imagination. To this end, researchers propose Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that jointly reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions to estimate whether the remaining action rollout can still be trusted.

**Performance Improvements**

On the RoboTwin benchmark, FFDC reduces WAM forward passes by 69.10% and execution time by 34.02%, while improving success rate by 2.54% over the short-chunk baseline; in real-world experiments, it improves success rate by 35%.

**Related Approaches**

The 2026 research landscape also includes other adaptive mechanisms. With the rapid scaling of Vision-Language-Action (VLA) models, efficiency has become a central challenge for real-world deployment, and adaptive inference has been introduced as a strategy during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efaa64ea-341e-4d6e-aeff-c81287341d74",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "f1ba1d8c-24ce-41b0-ad31-deb654c75e3a",
  "sourceToolAssistantUUID": "efaa64ea-341e-4d6e-aeff-c81287341d74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T19:37:36.805Z_

<details><summary>↩ Tool result · `toolu_01N73kdJSNiizJCL4cez8RcQ`</summary>

```text
Web search results for query: "site:arxiv.org "world action model" acceleration 2026"

Links: [{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"[2603.24581] Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving","url":"https://arxiv.org/abs/2603.24581"}]

I found several recent research papers on arXiv about World Action Models (WAMs) from 2026. Here are the key findings:

## Papers on World Action Models and Acceleration

**Fast-WAM** (March 2026): A paper questioning whether World Action Models need test-time future imagination. Most existing WAMs follow an imagine-then-execute paradigm with substantial test-time latency from iterative video denoising.

**DreamZero** (February 2026): Researchers introduced DreamZero, a World Action Model built upon a pretrained video diffusion backbone as a zero-shot policy approach.

**MotuBrain** (April 2026): An advanced World Action Model featuring inference-time acceleration strategies. The paper addresses inference latency as a practical concern, noting that jointly denoising video and action latents couples two of the slowest computations in modern generative modeling, and enables substantial inference acceleration without degrading task success rate.

**Generalization Study** (March-April 2026): A robustness comparison of World Action Models and VLAs, where world action models are built upon world models trained on large corpora of video data to predict future states.

**Latent-WAM** (March 2026): An efficient end-to-end autonomous driving framework using latent world action modeling for trajectory planning.

The search results show significant activity in 2026 on addressing WAM efficiency and acceleration challenges, particularly focusing on reducing inference latency for real-world robotic control applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50e52564-28c1-4e42-b575-7fe85ac0c93b",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "9f8c8e82-85b6-431a-9891-760b39879bcc",
  "sourceToolAssistantUUID": "50e52564-28c1-4e42-b575-7fe85ac0c93b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:37:37.458Z_

<details><summary>↩ Tool result · `toolu_018g1PriYJjJp3kiBfRH71rY`</summary>

```text
Web search results for query: ""convergence caching" diffusion 2026"

Links: [{"title":"ICLR Poster Evolutionary Caching to Accelerate Your Off-the-Shelf Diffusion Model","url":"https://iclr.cc/virtual/2026/poster/10006485"},{"title":"Beyond the next token: Why diffusion LLMs are changing the game | Red Hat Developer","url":"https://developers.redhat.com/articles/2026/04/28/beyond-next-token-why-diffusion-llms-are-changing-game"},{"title":"Towards Stabilized and Efﬁcient Diffusion Transformers through","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Towards_Stabilized_and_Efficient_Diffusion_Transformers_through_Long-Skip-Connections_with_Spectral_ICCV_2025_paper.pdf"},{"title":"A Convergence Theory for Diffusion Language Models","url":"https://arxiv.org/abs/2505.21400"},{"title":"Learning-to-Cache: Accelerating Diffusion Transformer via Layer Caching | OpenReview","url":"https://openreview.net/forum?id=ZupoMzMNrO"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.03674"},{"title":"Improved Convergence Rate for Diffusion Probabilistic Models | OpenReview","url":"https://openreview.net/forum?id=SOd07Qxkw4"},{"title":"15 Best Stable Diffusion Models in 2026: The Ultimate Guide - AI Photo Generator","url":"https://www.aiphotogenerator.net/blog/2026/02/best-stable-diffusion-models-2026"},{"title":"GitHub - macovaseas/ProCache: [AAAI 2026] Official implementation for \"ProCache: Constraint-Aware Feature Caching with Selective Computation for Diffusion Transformer Acceleration\" · GitHub","url":"https://github.com/macovaseas/ProCache"},{"title":"AB-Cache: Training-Free Acceleration of Diffusion Models ...","url":"https://dl.acm.org/doi/pdf/10.1145/3746027.3755650"}]

I found several relevant results about convergence caching and diffusion models in 2026. Here's what the search revealed:

## Key Findings

**Convergence Theory for Diffusion Models:**
Researchers have developed convergence guarantees for diffusion language models from an information-theoretic perspective, with analysis showing that sampling error measured by KL divergence decays inversely with the number of iterations and scales linearly with mutual information between tokens in target text sequences.

**Caching Acceleration Methods:**
Several caching-based approaches have emerged in 2026 to accelerate diffusion transformers:

1. **ProCache**: ProCache speeds up Diffusion Transformers with constraint-aware feature caching and selective computation, trading redundant work for quality-preserving inference.

2. **AB-Cache**: Caching-based methods have emerged as a promising direction that exploit the high similarity between adjacent denoising steps and the structure of U-Net/DiT networks, introducing caching mechanisms to reuse computations and boost efficiency.

3. **Learning-to-Cache (L2C)**: Learning-to-Cache learns to conduct caching in a dynamic manner for diffusion transformers by leveraging the identical structure of layers in transformers and the sequential nature of diffusion to explore redundant computations between timesteps.

4. **Evolutionary Caching (ECAD)**: ECAD uses a genetic algorithm that learns efficient, per-model, caching schedules forming a Pareto frontier, using only a small set of calibration prompts.

These approaches represent a significant research focus on improving the efficiency of diffusion model inference through intelligent caching strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7054e426-2913-4f7a-8fc3-0f39bd0ab8e7",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "75267b3c-77ff-4267-9c70-e730764bc2cf",
  "sourceToolAssistantUUID": "7054e426-2913-4f7a-8fc3-0f39bd0ab8e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T19:37:44.003Z_

<details><summary>↩ Tool result · `toolu_01GeKKnHg5otZCkcGyF9KLFj`</summary>

```text
Web search results for query: "site:arxiv.org "diffusion policy" adaptive steps 2026"

Links: [{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2604.15938"},{"title":"[2602.04037] DADP: Domain Adaptive Diffusion Policy","url":"https://arxiv.org/abs/2602.04037"},{"title":"DADP: Domain Adaptive Diffusion Policy","url":"https://arxiv.org/html/2602.04037"},{"title":"ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/html/2508.06266"},{"title":"[2602.21622] ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation","url":"https://arxiv.org/abs/2602.21622"},{"title":"[2602.20057] AdaWorldPolicy: World-Model-Driven Diffusion Policy with Online Adaptive Learning for Robotic Manipulation","url":"https://arxiv.org/abs/2602.20057"},{"title":"TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration","url":"https://arxiv.org/html/2512.15773"},{"title":"AdaWorldPolicy: World-Model-Driven Diffusion Policy with Online Adaptive Learning for Robotic Manipulation","url":"https://arxiv.org/html/2602.20057"},{"title":"ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation","url":"https://arxiv.org/html/2602.21622"},{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"}]

I found several recent papers from arXiv.org about diffusion policies with adaptive mechanisms. Here are the key results:

## Recent Diffusion Policy Papers with Adaptive Steps (2026)

1. **VADF: Vision-Adaptive Diffusion Policy Framework** A vision-driven dual-adaptive framework that significantly reduces convergence steps and achieves early success in inference, with model-agnostic design. It adaptively segments action sequences into simple and complex subtasks by assigning shorter noise schedules with longer direct execution sequences to simple actions, and longer noise steps with shorter execution sequences to complex ones.

2. **DADP: Domain Adaptive Diffusion Policy** A method that achieves robust adaptation through unsupervised disentanglement and domain-aware diffusion injection, using Lagged Context Dynamical Prediction to condition future state estimation on historical offset context, and integrating learned domain representations directly into the generative process.

3. **ADM-DP: Adaptive Dynamic Modality Diffusion Policy** A framework that integrates vision, tactile, and graph-based (multi-agent pose) modalities for coordinated control.

4. **AdaWorldPolicy** A framework to enhance robotic manipulation under dynamic conditions, with the core insight that world models provide strong supervision signals, enabling online adaptive learning in dynamic environments.

5. **TS-DP: Temporal-aware Reinforcement-based Speculative Diffusion Policy** The first framework that enables speculative decoding for DP with temporal adaptivity, training a PPO-based scheduler that formulates DP execution as a Markov process and adaptively tunes speculative parameters over time.

These papers represent recent advances in making diffusion policies more adaptive and efficient through dynamic step allocation and other optimization strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f4fc26d-6b42-4589-a507-9e246faa7281",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "43049e47-ce1a-4b61-9f6b-c057cf2a075c",
  "sourceToolAssistantUUID": "1f4fc26d-6b42-4589-a507-9e246faa7281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T19:37:48.318Z_

Excellent results. Let me now do several follow-up searches to dig deeper into the most relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43049e47-ce1a-4b61-9f6b-c057cf2a075c",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTDDvhnVER9Eay3bZkf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4302dacc-28ba-4f35-aa2b-a015bfb50a83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQr5GA4JrdvxmTo49Buzkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 14491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2923,
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

_source line 25 · 2026-05-10T19:37:49.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Kt4Wsq1s1sEWiCTyFJ4CV`</summary>

```json
{
  "query": "X-WAM asynchronous denoising \"asynchronous noise sampling\" video action 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4302dacc-28ba-4f35-aa2b-a015bfb50a83",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTDDvhnVER9Eay3bZkf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97d78e46-0b13-4141-b0b6-305f878613b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQr5GA4JrdvxmTo49Buzkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 14491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2923,
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

_source line 26 · 2026-05-10T19:37:50.298Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LwGBU1w1zETeeQ6sPbWUnv`</summary>

```json
{
  "query": "D3P \"dynamic denoising diffusion policy\" adaptive steps reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97d78e46-0b13-4141-b0b6-305f878613b6",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTDDvhnVER9Eay3bZkf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64ec3a08-f346-4825-98ea-6ba3e48ac3c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQr5GA4JrdvxmTo49Buzkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 14491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2923,
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

_source line 27 · 2026-05-10T19:37:51.338Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JM2qYLsoj5EsEtdS1XMeqU`</summary>

```json
{
  "query": "MotuBrain \"DiT caching\" denoising acceleration world action model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64ec3a08-f346-4825-98ea-6ba3e48ac3c7",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTDDvhnVER9Eay3bZkf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "978c188c-1aea-4c1a-931b-f18f95792f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQr5GA4JrdvxmTo49Buzkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 14491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2923,
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

_source line 28 · 2026-05-10T19:37:51.946Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KQiYhrFrw33iFumnGyY4zq`</summary>

```json
{
  "query": "VADF \"vision-adaptive diffusion policy\" convergence steps early stopping 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "978c188c-1aea-4c1a-931b-f18f95792f97",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTDDvhnVER9Eay3bZkf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66226012-13e6-4c33-84c4-1d823d6a89dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQr5GA4JrdvxmTo49Buzkg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 14491,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2923
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 992,
          "output_tokens": 258,
          "cache_read_input_tokens": 14491,
          "cache_creation_input_tokens": 2923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2923,
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

_source line 29 · 2026-05-10T19:37:57.947Z_

<details><summary>↩ Tool result · `toolu_01LwGBU1w1zETeeQ6sPbWUnv`</summary>

```text
Web search results for query: "D3P "dynamic denoising diffusion policy" adaptive steps reinforcement learning 2025"

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"[2508.06804] D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/abs/2508.06804"},{"title":"D3P: Dynamic Denoising Difusion Policy via Reinforcement Learning Shu’ang Yu","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2508.06804v1"},{"title":"(PDF) D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://www.researchgate.net/publication/394438722_D3P_Dynamic_Denoising_Diffusion_Policy_via_Reinforcement_Learning"},{"title":"Denoising Diffusion Policy Optimization","url":"https://www.emergentmind.com/topics/denoising-diffusion-policy-optimization-ddpo"},{"title":"Diffusion Steering via Reinforcement Learning","url":"https://www.emergentmind.com/topics/diffusion-steering-via-reinforcement-learning-dsrl"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration","url":"https://arxiv.org/html/2512.15773"},{"title":"Entropy-Adaptive Diffusion Policy Optimization with Dynamic Step Alignment","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_Entropy-Adaptive_Diffusion_Policy_Optimization_with_Dynamic_Step_Alignment_ICCV_2025_paper.pdf"}]

I found relevant information about D3P. Here's what the search revealed:

## D3P: Dynamic Denoising Diffusion Policy

D3P (Dynamic Denoising Diffusion Policy) is a diffusion policy that capitalizes on the varying action criticalities in robotic tasks. It employs a lightweight adaptor to dynamically adjust denoising steps, assigning more steps to crucial actions and fewer to routine ones. The method uses RL to jointly optimize the base policy and the adaptor with a carefully-designed reward and a three-stage training strategy.

### Key Innovation

Diffusion policies excel at learning complex action distributions for robotic visuomotor tasks, yet their iterative denoising process poses a major bottleneck for real-time deployment. Existing acceleration methods apply a fixed number of denoising steps per action, implicitly treating all actions as equally important. However, experiments reveal that robotic tasks often contain a mix of crucial and routine actions, which differ in their impact on task success. D3P was motivated by this finding to adaptively allocate denoising steps across actions at test time.

### Technical Approach

D3P uses a lightweight, state-aware adaptor to allocate the optimal number of denoising steps for each action. The adaptor and base diffusion policy are jointly optimized via reinforcement learning to balance task performance and inference efficiency.

### Performance Results

On simulated tasks, D3P achieves an averaged 2.2× inference speed-up over baselines without degrading success. Furthermore, D3P's effectiveness was demonstrated on a physical robot, achieving a 1.9× acceleration over the baseline.

The paper was published in August 2025 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64ec3a08-f346-4825-98ea-6ba3e48ac3c7",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "63aaca95-c153-47b5-83b8-5acffad81fd7",
  "sourceToolAssistantUUID": "64ec3a08-f346-4825-98ea-6ba3e48ac3c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T19:37:59.124Z_

<details><summary>↩ Tool result · `toolu_01JM2qYLsoj5EsEtdS1XMeqU`</summary>

```text
Web search results for query: "MotuBrain "DiT caching" denoising acceleration world action model 2026"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Less is Enough: Training-Free Video Diffusion Acceleration via Runtime-Adaptive Caching","url":"https://arxiv.org/html/2507.02860v1"},{"title":"MotuBrain World Model Tops Two Global Benchmarks — A Breakthrough in Robot Intelligence - DeepInsightAI","url":"https://deepinsightai.io/motubrain-world-model/"},{"title":"WorldCache: Content-Aware Caching for Accelerated Video World Models","url":"https://arxiv.org/html/2603.22286"},{"title":"A Survey on Cache Methods in Diffusion Models","url":"https://arxiv.org/pdf/2510.19755"},{"title":"WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching","url":"https://arxiv.org/html/2603.06331"},{"title":"Upsample What Matters: Region-Adaptive Latent Sampling for Accelerated Diffusion Transformers","url":"https://arxiv.org/html/2507.08422v2"},{"title":"FASTERCACHE: TRAINING-FREE VIDEO DIFFUSION ...","url":"https://i.cs.hku.hk/~kykwong/publications/zlv_iclr2025.pdf"},{"title":"ScalingCache: Extreme Acceleration of DiTs through Difference Scaling and Dynamic Interval Caching | OpenReview","url":"https://openreview.net/forum?id=uXmbrTlko7"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html"}]

Based on the search results, here's what I found about MotuBrain and DiT caching denoising acceleration:

## MotuBrain Overview

MotuBrain is a World Action Model announced by ShengShu Technology that replaces multiple task-specific systems with a single, unified model that functions as a robotic brain for the physical world. It ranks highly on both WorldArena and RoboTwin 2.0, two of the field's most rigorous benchmarks in embodied world models.

## DiT Caching and Denoising Acceleration

MotuBrain employs several techniques to accelerate inference, specifically including DiT caching. The model develops a systems-oriented inference stack including denoising-step reduction, compilation with CUDA-graph-friendly execution, FP8 quantization, and DiT caching.

The specific DiT caching strategy works as follows: The video latent is frozen, and the video-text branch is executed once to build per-layer cached keys and values for the fixed visual-language context. Subsequent denoising steps update only the action tokens: action queries attend to the cached video/text keys and values together with their own action keys and values. This removes the repeated video-stream computation from the latter part of sampling while preserving the same attention semantics as the V2A-style model.

## Inference Performance

Combined with the other inference optimizations, this design enables MotuBrain to reach an 11 Hz inference frequency, exceeding typical human reaction speed. This asymmetric dependency makes it possible to use an action-only suffix during inference, and in practice it enables substantial inference acceleration without degrading task success rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "978c188c-1aea-4c1a-931b-f18f95792f97",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "3aa4f1af-dcd0-433a-b7d0-ac49e7b80d9b",
  "sourceToolAssistantUUID": "978c188c-1aea-4c1a-931b-f18f95792f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T19:38:00.535Z_

<details><summary>↩ Tool result · `toolu_01KQiYhrFrw33iFumnGyY4zq`</summary>

```text
Web search results for query: "VADF "vision-adaptive diffusion policy" convergence steps early stopping 2026"

Links: [{"title":"[2604.15938] VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2604.15938"},{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2604.15938"},{"title":"(PDF) VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://www.researchgate.net/publication/403976521_VADF_Vision-Adaptive_Diffusion_Policy_Framework_for_Efficient_Robotic_Manipulation"},{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2604.15938"},{"title":"VADF: Vision-Adaptive Diffusion Framework. VADF introduces a... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/ADF-Vision-Adaptive-Diffusion-Framework-VADF-introduces-a-dualadaptive-mechanism-for_fig1_403976521"},{"title":"Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/336869092_Relay_Policy_Learning_Solving_Long-Horizon_Tasks_via_Imitation_and_Reinforcement_Learning"},{"title":"[2604.20360] On the convergence of an adaptive denoiser driven iterative regularization with early stopping","url":"https://arxiv.org/abs/2604.20360"},{"title":"GitHub - wangkai930418/awesome-diffusion-categorized: collection of diffusion model papers categorized by their subareas · GitHub","url":"https://github.com/wangkai930418/awesome-diffusion-categorized"},{"title":"GitHub - 52CV/CVPR-2025-Papers · GitHub","url":"https://github.com/52CV/CVPR-2025-Papers"},{"title":"Diffusion Policy Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=mEpqHvbD2h"}]

Based on the search results, I found detailed information about VADF (Vision-Adaptive Diffusion Policy Framework) from a 2026 research paper:

## Overview

VADF is a vision-driven dual-adaptive framework that significantly reduces convergence steps and achieves early success in inference, with model-agnostic design enabling seamless integration.

## Convergence and Training

Diffusion policies suffer from hard negative class imbalance due to uniform sampling and lack of sample difficulty awareness, leading to slow training convergence and frequent inference timeout failures. 

The ALN module significantly accelerates convergence, reaching peak success rates with substantially fewer gradient steps than vanilla DP while reducing variance. Models are trained for 600 to 3,500 epochs (approximately 20k–120k gradient steps) to ensure full convergence across tasks of varying complexity.

## Key Components

During training, an Adaptive Loss Network (ALN) is introduced as a lightweight MLP-based loss predictor that quantifies per-step sample difficulty in real time and performs weighted sampling to prioritize high-loss regions, enabling adaptive weight updates and faster convergence.

In inference, the Hierarchical Vision Task Segmenter (HVTS) decomposes high-level task instructions into multi-stage low-level sub-instructions based on visual input and adaptively segments action sequences by assigning shorter noise schedules with longer direct execution sequences to simple actions, and longer noise steps with shorter execution sequences to complex ones.

## Performance Results

VADF consistently matches or improves task success rates while substantially boosting early success rate—from 85.4% to 91.3% for the MLP variant and from 80.1% to 86.8% for the Transformer variant.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66226012-13e6-4c33-84c4-1d823d6a89dc",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "020ce0f5-ed3a-4ee5-8e06-dd10f329b08a",
  "sourceToolAssistantUUID": "66226012-13e6-4c33-84c4-1d823d6a89dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T19:38:00.981Z_

<details><summary>↩ Tool result · `toolu_019Kt4Wsq1s1sEWiCTyFJ4CV`</summary>

```text
Web search results for query: "X-WAM asynchronous denoising "asynchronous noise sampling" video action 2026"

Links: [{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"X-WAM: Bridging Action and 4D Synthesis | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/ai-research/2026/x-wam-bridging-action-and-4d-synthesis"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Request PDF","url":"https://www.researchgate.net/publication/395371959_Unified_World_Models_Coupling_Video_and_Action_Diffusion_for_Pretraining_on_Large_Robotic_Datasets"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"GitHub - DravenALG/awesome-vla-wam: A Curated List of Vision-Language-Action (VLA) and World Action Models (WAM) Research and Beyond · GitHub","url":"https://github.com/DravenALG/awesome-vla-wam"}]

Based on the web search results, here's what I found about X-WAM and its asynchronous denoising approach:

## Overview

X-WAM is a unified 4D World Action Model that simultaneously targets high-fidelity video generation, 3D spatial reconstruction, and real-time policy execution.

## Asynchronous Noise Sampling (ANS)

X-WAM proposes Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency, which applies a specialized asynchronous denoising schedule during inference that rapidly decodes actions with fewer steps to enable efficient real-time execution, while dedicating the full sequence of steps to generate high-fidelity video.

### How ANS Works

ANS introduces a specialized asynchronous denoising schedule for inference: it rapidly decodes precise actions using only a fraction of the initial steps to allow them to be immediately executed by the policy, and subsequently completes the remaining steps to render high-fidelity future videos.

ANS systematically samples from a joint distribution of video and actions that strictly matches the test-time distribution, which elegantly eliminates the inefficiencies of decoupled sampling, maximizing both action inference speed and visual generation quality.

## Performance Results

X-WAM achieves impressive average success rates of 79.2% on the RoboCasa benchmark and 90.7% on RoboTwin 2.0. X-WAM was deployed on physical robots to validate real-world performance, with the model executing various manipulation tasks on real hardware and demonstrating its generalization from simulation to the real world.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97d78e46-0b13-4141-b0b6-305f878613b6",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "940b9f2c-02b8-404a-a687-2b67463eed75",
  "sourceToolAssistantUUID": "97d78e46-0b13-4141-b0b6-305f878613b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T19:38:04.154Z_

Now let me search for a few more specific angles -- per-modality convergence monitoring, Fast-WAM, TS-DP, and entropy-adaptive diffusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "940b9f2c-02b8-404a-a687-2b67463eed75",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTEUV686vXkJ8anfTv5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af6599c0-f4f1-42c8-9bd3-8dd7e27f4fdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tzor1iyMok7hPqq5y4oZxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2988,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 17414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2204,
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

_source line 34 · 2026-05-10T19:38:05.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TK66v2jnoWR7aqasuKyQKY`</summary>

```json
{
  "query": "Fast-WAM \"test-time\" imagination denoising steps video action model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af6599c0-f4f1-42c8-9bd3-8dd7e27f4fdb",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTEUV686vXkJ8anfTv5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53edef1f-f6f0-47c5-9815-5237fa09ccec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tzor1iyMok7hPqq5y4oZxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2988,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 17414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2204,
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

_source line 35 · 2026-05-10T19:38:05.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HHEqw7sKDu8Eaphv6SuKkN`</summary>

```json
{
  "query": "TS-DP \"speculative decoding\" diffusion policy adaptive temporal 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53edef1f-f6f0-47c5-9815-5237fa09ccec",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTEUV686vXkJ8anfTv5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2d4ff93-7602-4d67-a02b-e4836ef35992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tzor1iyMok7hPqq5y4oZxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2988,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 17414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2204,
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

_source line 36 · 2026-05-10T19:38:06.594Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D7UCqE9tDN8beaxMBsj2Tk`</summary>

```json
{
  "query": "\"entropy-adaptive diffusion\" \"dynamic step alignment\" ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2d4ff93-7602-4d67-a02b-e4836ef35992",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTEUV686vXkJ8anfTv5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b29f7b4-25fb-47fe-bce6-299002a5c8d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tzor1iyMok7hPqq5y4oZxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2988,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 17414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2204,
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

_source line 37 · 2026-05-10T19:38:07.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MTk8Hqdtf21VPgzF3LBfqL`</summary>

```json
{
  "query": "\"per-modality\" OR \"modality-specific\" convergence denoising diffusion adaptive steps 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b29f7b4-25fb-47fe-bce6-299002a5c8d2",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTEUV686vXkJ8anfTv5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78bdb4f3-a5d4-4b04-a4ba-2572f8be8ebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tzor1iyMok7hPqq5y4oZxV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2988,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 17414,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2204
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2988,
          "output_tokens": 280,
          "cache_read_input_tokens": 17414,
          "cache_creation_input_tokens": 2204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2204,
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

_source line 38 · 2026-05-10T19:38:10.934Z_

<details><summary>↩ Tool result · `toolu_01TK66v2jnoWR7aqasuKyQKY`</summary>

```text
Web search results for query: "Fast-WAM "test-time" imagination denoising steps video action model 2026"

Links: [{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"Fast-WAM: Rethinking Test-Time Imagination","url":"https://www.emergentmind.com/papers/2603.16666"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"},{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination? - PULRC Portal","url":"https://lrc.perdanauniversity.edu.my/sdi/fast-wam-do-world-action-models-need-test-time-future-imagination/"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"}]

Based on the search results, here's what I found about Fast-WAM:

## Fast-WAM: Do World Action Models Need Test-time Future Imagination?

Fast-WAM is a World Action Model (WAM) architecture that retains video co-training during training but skips future prediction at test time.

### Key Concept

Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising. Fast-WAM addresses this by decoupling the role of video modeling from explicit future generation. At inference time, Fast-WAM keeps only the clean latent tokens of the current observation, processes them with the video backbone once, and directly generates actions without explicit future video denoising.

### Performance Findings

Fast-WAM remains competitive with imagine-then-execute variants, while removing video co-training causes a much larger performance drop. Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin) and real-world tasks, without embodied pretraining. It runs in real time with 190ms latency, over 4× faster than existing imagine-then-execute WAMs.

### Main Insight

These results suggest that the main value of video prediction in WAMs may lie in improving world representations during training rather than generating future observations at test time.

The paper was published in March 2026 on arXiv (2603.16666) by authors including Tianyuan Yuan, Zibin Dong, Yicheng Liu, and Hang Zhao.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53edef1f-f6f0-47c5-9815-5237fa09ccec",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "fb3b0a1d-6079-4804-94e4-d1eb1fe4cf1f",
  "sourceToolAssistantUUID": "53edef1f-f6f0-47c5-9815-5237fa09ccec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T19:38:14.207Z_

<details><summary>↩ Tool result · `toolu_01HHEqw7sKDu8Eaphv6SuKkN`</summary>

```text
Web search results for query: "TS-DP "speculative decoding" diffusion policy adaptive temporal 2025 2026"

Links: [{"title":"[2512.15773] TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration","url":"https://arxiv.org/abs/2512.15773"},{"title":"TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration","url":"https://arxiv.org/html/2512.15773"},{"title":"Artificial Intelligence Dec 2025","url":"https://arxiv.org/list/cs.AI/2025-12?skip=2525&show=250"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=speculative+decoding"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Self Speculative Decoding for Diffusion Large Language Model | OpenReview","url":"https://openreview.net/forum?id=rKJ7A30lQQ"},{"title":"[2510.02358] DiffuSpec: Unlocking Diffusion Language Models for Speculative Decoding","url":"https://arxiv.org/abs/2510.02358"},{"title":"[2408.05636] Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion","url":"https://arxiv.org/abs/2408.05636"},{"title":"SELF SPECULATIVE DECODING FOR DIFFUSION ...","url":"https://openreview.net/pdf?id=rKJ7A30lQQ"},{"title":"GitHub - VILA-Lab/Awesome-DLMs: The official GitHub repo for the survey paper \"A Survey on Diffusion Language Models\". · GitHub","url":"https://github.com/VILA-Lab/Awesome-DLMs"}]

I found research on TS-DP. Here are the key findings:

## TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration

TS-DP (Temporal-aware Reinforcement-based Speculative Diffusion Policy) is the first framework that enables speculative decoding for Diffusion Policy with temporal adaptivity.

### Problem Being Addressed

Diffusion Policy excels in embodied control but suffers from high inference latency and computational cost due to multiple iterative denoising steps. Speculative decoding offers a lossless and adaptive alternative for DP, yet remains underexplored in this domain.

### Key Components

The framework has two main components:

1. **Drafter Model**: A Transformer-based drafter is distilled to imitate the base model and replace its costly denoising calls.

2. **Adaptive Scheduler**: An RL-based scheduler adapts to time-varying task difficulty by adjusting speculative parameters to maintain accuracy while improving efficiency.

### Performance Results

TS-DP achieves up to 4.17 times faster inference with over 94% accepted drafts, reaching an inference frequency of 25 Hz and enabling real-time diffusion-based control without performance degradation.

The paper was published on arXiv on December 13, 2025, authored by Ye Li and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2d4ff93-7602-4d67-a02b-e4836ef35992",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "bcffcec9-6472-4def-ac30-849080cfbab5",
  "sourceToolAssistantUUID": "f2d4ff93-7602-4d67-a02b-e4836ef35992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T19:38:15.181Z_

<details><summary>↩ Tool result · `toolu_01D7UCqE9tDN8beaxMBsj2Tk`</summary>

```text
Web search results for query: ""entropy-adaptive diffusion" "dynamic step alignment" ICCV 2025"

Links: [{"title":"Entropy-Adaptive Diffusion Policy Optimization with Dynamic Step Alignment","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_Entropy-Adaptive_Diffusion_Policy_Optimization_with_Dynamic_Step_Alignment_ICCV_2025_paper.pdf"},{"title":"Entropy-Adaptive Diffusion Policy Optimization with Dynamic ...","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Yan_Entropy-Adaptive_Diffusion_Policy_Optimization_with_Dynamic_Step_Alignment_ICCV_2025_paper.html"},{"title":"ICCV 2025 Schedule","url":"https://iccv.thecvf.com/virtual/2025/calendar"},{"title":"GitHub - xie-lab-ml/awesome-alignment-of-diffusion-models: [ACM Computing Surveys] The collection of awesome papers on alignment of diffusion models. · GitHub","url":"https://github.com/xie-lab-ml/awesome-alignment-of-diffusion-models"},{"title":"ICCV 2025 Papers","url":"https://iccv.thecvf.com/virtual/2025/papers.html"},{"title":"Track: Poster Session 1 & Exhibit Hall","url":"https://iccv.thecvf.com/virtual/2025/session/2873"},{"title":"Diffusion Model Alignment via Shortcut-based Fine-Tuning","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_ShortFT_Diffusion_Model_Alignment_via_Shortcut-based_Fine-Tuning_ICCV_2025_paper.pdf"},{"title":"Robust Concept Erasure in Diffusion Models","url":"https://arxiv.org/pdf/2509.12024"},{"title":"Multi-modal LLMs, Diffusions, and the Unification","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Multi-modal%20Generative%20AI%20Multi-modal%20LLMs%20Diffusions%20and%20the%20Unification.pdf"},{"title":"GitHub - 52CV/CVPR-2025-Papers · GitHub","url":"https://github.com/52CV/CVPR-2025-Papers"}]

I found the paper! Here are the search results for "entropy-adaptive diffusion" "dynamic step alignment" ICCV 2025:

## Paper Details

The paper is titled "Entropy-Adaptive Diffusion Policy Optimization with Dynamic Step Alignment" and was authored by Renye Yan, Jikang Cheng, Yaozhong Gan, Shikun Sun, You Wu, Yunfan Yang, Ling Liang, Jinlong Lin, Yeshuang Zhu, Jie Zhou, Jinchao Zhang, Junliang Xing, Yimao Cai, and Ru Huang from Peking University, Tencent Inc, Tsinghua University, and Nanjing University.

## Main Contributions

While fine-tuning diffusion models with reinforcement learning has demonstrated effectiveness in optimizing downstream objectives, existing RL frameworks are prone to overfitting rewards. The paper addresses this by introducing entropy as a quantitative measure to enhance the exploratory capacity of diffusion models' denoising policies.

The paper proposes an adaptive mechanism that dynamically adjusts the application and magnitude of entropy and regularization, guided by real-time quality estimation of intermediate noised states.

## Publication Details

The paper appears in the Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pages 1924-1934.

The paper is available as an open access PDF through the Computer Vision Foundation's website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b29f7b4-25fb-47fe-bce6-299002a5c8d2",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "814bcb0d-435e-4319-88f7-f19538ea9353",
  "sourceToolAssistantUUID": "3b29f7b4-25fb-47fe-bce6-299002a5c8d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T19:38:15.306Z_

<details><summary>↩ Tool result · `toolu_01MTk8Hqdtf21VPgzF3LBfqL`</summary>

```text
Web search results for query: ""per-modality" OR "modality-specific" convergence denoising diffusion adaptive steps 2025 2026"

Links: [{"title":"Adaptive Clinical-Aware Latent Diffusion for Multimodal Brain Image Generation and Missing Modality Imputation","url":"https://arxiv.org/html/2603.09931"},{"title":"Denoising diffusion probabilistic models are optimally adaptive to unknown low dimensionality","url":"https://arxiv.org/html/2410.18784v3"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf"},{"title":"Source-free cross-modality medical image synthesis with diffusion priors | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00200-5"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new?skip=275&show=2000"},{"title":"Curriculum Conditioned Diffusion for Multimodal Recommendation","url":"https://www.atailab.cn/seminar2025Spring/pdf/2025_AAAI_Curriculum%20Conditioned%20Diffusion%20for%20Multimodal%20Recommendation.pdf"},{"title":"Multi-modal LLMs, Diffusions, and the Unification","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Multi-modal%20Generative%20AI%20Multi-modal%20LLMs%20Diffusions%20and%20the%20Unification.pdf"},{"title":"DiffMC‐Gen: A Dual Denoising Diffusion Model for Multi‐Conditional Molecular Generation - Yang - 2025 - Advanced Science - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202417726"},{"title":"What are Diffusion Models? | Lil'Log","url":"https://lilianweng.github.io/posts/2021-07-11-diffusion-models/"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=550&show=2000"}]

I found several relevant search results related to your query about per-modality/modality-specific convergence, denoising, diffusion, and adaptive steps from 2025-2026. Here are the key findings:

## Recent Research on Adaptive Diffusion and Modality-Specific Approaches

**Adaptive Clinical-Aware Diffusion (ACADiff)** - ACADiff is a framework that synthesizes missing brain imaging modalities through adaptive clinical-aware diffusion, learning mappings between incomplete multimodal observations and target modalities by progressively denoising latent representations while attending to available imaging data and clinical metadata. The timestep controls denoising dynamics across all layers, enabling the model to adaptively adjust its denoising strength at each diffusion step.

**Convergence Analysis of DDPM** - Research develops a sharp convergence theory for the DDPM in the face of unknown low dimensionality, with convergence guarantees for reaching an ε²-accurate distribution measured by the KL divergence.

**Dynamic Gradient Weighting for Diffusion** - Dynamic Gradient Weighting (DyWeight) is a lightweight, learning-based multi-step solver that learns unconstrained time-varying parameters that adaptively aggregate historical gradients while intrinsically scaling the effective step size.

**Multimodal Generation Models** - A unified paradigm uses discrete tokens for text modeled autoregressively and continuous image pixels modeled using denoising diffusion, though integrating these two distinct techniques into one single network is non-trivial due to significant differences between discrete text tokens and continuous image/video representations.

These recent papers (2025-2026) demonstrate active research in adaptive, modality-aware diffusion approaches with convergence improvements and specialized handling of different data modalities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78bdb4f3-a5d4-4b04-a4ba-2572f8be8ebf",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "eb11ad0e-400c-4443-8920-fdb294407674",
  "sourceToolAssistantUUID": "78bdb4f3-a5d4-4b04-a4ba-2572f8be8ebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T19:38:19.488Z_

Let me do a final round of targeted searches on the most directly overlapping concepts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb11ad0e-400c-4443-8920-fdb294407674",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTFXq2o9x61NuVuSWE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e222b48b-6f00-4f01-b0b0-22c32a7f203f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BZyDuY17cdx2GTgynZ4bt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7272,
      "cache_read_input_tokens": 19618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7272,
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

_source line 43 · 2026-05-10T19:38:20.591Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B7nzYKjiSCwCbQAHd4gCVz`</summary>

```json
{
  "query": "ADPro \"test-time adaptive diffusion policy\" manifold denoising robotic 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e222b48b-6f00-4f01-b0b0-22c32a7f203f",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTFXq2o9x61NuVuSWE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44bb7bac-152e-4a69-ba21-af2522c1a881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BZyDuY17cdx2GTgynZ4bt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7272,
      "cache_read_input_tokens": 19618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7272,
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

_source line 44 · 2026-05-10T19:38:21.390Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HA88f9EqZYtf3M9UYHv6PJ`</summary>

```json
{
  "query": "\"quality floor\" OR \"quality guarantee\" diffusion denoising steps adaptive allocation robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44bb7bac-152e-4a69-ba21-af2522c1a881",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTFXq2o9x61NuVuSWE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f237d0e3-fecd-420e-ac57-a5cccf05d406",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BZyDuY17cdx2GTgynZ4bt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7272,
      "cache_read_input_tokens": 19618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7272,
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

_source line 45 · 2026-05-10T19:38:22.317Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KSQpqcv8VZoei8P5Vy6Nie`</summary>

```json
{
  "query": "WorldCache \"token caching\" video world model acceleration denoising 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f237d0e3-fecd-420e-ac57-a5cccf05d406",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTFXq2o9x61NuVuSWE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56903b0f-9ec9-4863-8ff0-9f4225eda158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BZyDuY17cdx2GTgynZ4bt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7272,
      "cache_read_input_tokens": 19618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7272,
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

_source line 46 · 2026-05-10T19:38:22.892Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018yCLpZsGGiLuEE3zz4qY5e`</summary>

```json
{
  "query": "\"multi-modal diffusion\" \"adaptive steps\" OR \"dynamic steps\" OR \"variable steps\" joint denoising 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56903b0f-9ec9-4863-8ff0-9f4225eda158",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTFXq2o9x61NuVuSWE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87dd7083-b11e-4234-8f9f-ea72219b910c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BZyDuY17cdx2GTgynZ4bt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7272,
      "cache_read_input_tokens": 19618,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7272
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 19618,
          "cache_creation_input_tokens": 7272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7272,
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

_source line 47 · 2026-05-10T19:38:27.606Z_

<details><summary>↩ Tool result · `toolu_01B7nzYKjiSCwCbQAHd4gCVz`</summary>

```text
Web search results for query: "ADPro "test-time adaptive diffusion policy" manifold denoising robotic 2025"

Links: [{"title":"[2508.06266] ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/abs/2508.06266"},{"title":"ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/html/2508.06266"},{"title":"ADPro: a Test-time Adaptive Diffusion Policy for Robot Manipulation via Manifold and Initial Noise Constraints","url":"https://arxiv.org/html/2508.06266v1"},{"title":"ADPro: a Test-time Adaptive Diffusion Policy for Robot ...","url":"https://www.alphaxiv.org/overview/2508.06266v1"},{"title":"6-DOF Grasping for Target-driven Object Manipulation in Clutter | Request PDF","url":"https://www.researchgate.net/publication/344983529_6-DOF_Grasping_for_Target-driven_Object_Manipulation_in_Clutter"},{"title":"Adaptive Diffusion Policy Optimization for Robotic Manipulation","url":"https://arxiv.org/html/2505.08376v1"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"Discriminative Active Learning for Robotic Grasping in Cluttered Scene | Request PDF","url":"https://www.researchgate.net/publication/368404027_Discriminative_Active_Learning_for_Robotic_Grasping_in_Cluttered_Scene"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"}]

Based on the search results, here's information about ADPro and the related research:

## ADPro: Test-time Adaptive Diffusion Policy

ADPro is a test-time adaptive diffusion policy via manifold-constrained denoising and task-aware initialization for robotic manipulation.

### Key Components

The Adaptive Diffusion Policy (ADP) is a test-time adaptation method that introduces two key inductive biases into the diffusion. First, it embeds a geometric manifold constraint that aligns denoising updates with task-relevant subspaces, leveraging the fact that the relative pose between the end-effector and target scene provides a natural gradient direction, and guiding denoising along the geodesic path of the manipulation manifold.

Second, to reduce unnecessary exploration and accelerate convergence, it proposes an analytically guided initialization: rather than sampling from an uninformative prior, a rough registration is computed between the gripper and target scenes to propose a structured initial noisy action.

### Key Advantages

ADP is compatible with pre-trained diffusion policies and requires no retraining, enabling test-time adaptation that tailors the policy to specific tasks, thereby enhancing generalization across novel tasks and environments.

### Performance Results

Experiments on RLBench, CALVIN, and real-world datasets show that ADPro, an implementation of ADP, improves success rates, generalization, and sampling efficiency, achieving up to 25% improvements (the text appears to be cut off in the source, but indicates significant performance gains).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44bb7bac-152e-4a69-ba21-af2522c1a881",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "40712f4f-d3eb-4115-af95-ee8e0d3e333e",
  "sourceToolAssistantUUID": "44bb7bac-152e-4a69-ba21-af2522c1a881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T19:38:28.793Z_

<details><summary>↩ Tool result · `toolu_01HA88f9EqZYtf3M9UYHv6PJ`</summary>

```text
Web search results for query: ""quality floor" OR "quality guarantee" diffusion denoising steps adaptive allocation robot 2025 2026"

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/html/2508.06266"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://ojs.aaai.org/index.php/AAAI/article/download/33075/35230"},{"title":"D3P: Dynamic Denoising Diffusion Policy via ...","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising | OpenReview","url":"https://openreview.net/forum?id=YY1MPKBHp7"},{"title":"Denoising Diffusion Policy Optimization","url":"https://www.emergentmind.com/topics/denoising-diffusion-policy-optimization"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://arxiv.org/html/2311.14768"},{"title":"AdaptDiffuser: Diffusion Models as Adaptive Self-evolving Planners","url":"https://proceedings.mlr.press/v202/liang23e/liang23e.pdf"},{"title":"Steering Diffusion Policies with Value-Guided Denoising | OpenReview","url":"https://openreview.net/forum?id=dtMBW9W5jo"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"}]

I found several highly relevant research papers on adaptive allocation of denoising steps in diffusion-based robot policies from 2025-2026. Here are the key findings:

## Dynamic Denoising Diffusion Policy (D3P)

D3P proposes a diffusion-based policy that adaptively allocates denoising steps across actions at test time. D3P uses a lightweight, state-aware adaptor to allocate the optimal number of denoising steps for each action. 

The research identifies an important insight: task executions typically consist of pivotal crucial actions that largely determine success, and more forgiving routine actions with only a marginal impact. The design principle is to allocate denoising steps adaptively: spend more computation on crucial actions, and less on routine ones—to balance precision and efficiency.

D3P achieves an average 2.2× inference speed-up over baseline methods while maintaining comparable performance. It allocates more steps for crucial actions, such as grasping and aligning, and fewer for routine movements.

## Adaptive Diffusion Policy (ADPro)

ADPro is a test-time adaptation method that introduces a geometric manifold constraint that aligns denoising updates with task-relevant subspaces. Task-aware initialization drives the diffusion process towards a more accurate direction instead of random noise, effectively reducing the number of denoising steps required.

## Additional Approaches

Diffusion policies can operate effectively with as few as 5 neural function evaluations (NFE) by tailoring the denoising process to the specific characteristics of embodied AI tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f237d0e3-fecd-420e-ac57-a5cccf05d406",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "a6cdc647-a1cb-4406-b48d-c245366cd648",
  "sourceToolAssistantUUID": "f237d0e3-fecd-420e-ac57-a5cccf05d406",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T19:38:31.180Z_

<details><summary>↩ Tool result · `toolu_018yCLpZsGGiLuEE3zz4qY5e`</summary>

```text
Web search results for query: ""multi-modal diffusion" "adaptive steps" OR "dynamic steps" OR "variable steps" joint denoising 2025 2026"

Links: [{"title":"Dual Trainable Diffusion Models(DTDM) for Adaptive Denoising in Telecom operators Recommendation Systems | Proceedings of the 2025 11th International Conference on Communication and Information Processing","url":"https://dl.acm.org/doi/full/10.1145/3784833.3784860"},{"title":"Seminars · FIB-LAB","url":"https://fi.ee.tsinghua.edu.cn/seminar/15/"},{"title":"ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation","url":"https://arxiv.org/html/2602.21622"},{"title":"D3P: Dynamic Denoising Diffusion Policy via ...","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"Denoising Diffusion Model-Driven Adaptive Estimation of Distribution Algorithm Integrating Multi-Modal Data","url":"https://www.mdpi.com/2227-7390/13/23/3777"},{"title":"Multi-modal LLMs, Diffusions, and the Unification","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Multi-modal%20Generative%20AI%20Multi-modal%20LLMs%20Diffusions%20and%20the%20Unification.pdf"},{"title":"Multi-scale adversarial diffusion network for image super-resolution | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-96185-2"},{"title":"MODIFy : A multi-modal anomaly diagnosis framework with diffusion-enhanced adaptive fusion in microservices - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0164121226000786"},{"title":"AdaDiff: Accelerating Diffusion Models Through Step-Wise Adaptive Computation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-72986-7_5"},{"title":"MIDAS: Multimodal Interactive Digital-humAn Synthesis via ...","url":"https://arxiv.org/pdf/2508.19320"}]

Based on the web search results, I found several relevant papers and works on multi-modal diffusion with adaptive or dynamic denoising approaches from 2025-2026:

## Key Findings:

### 1. **AdaDiff: Accelerating Diffusion Models Through Step-Wise Adaptive Computation**
AdaDiff addresses accelerating diffusion models through step-wise adaptive computation, published in ECCV 2024 (2025).

### 2. **Dual Trainable Diffusion Models (DTDM)**
DTDM is a framework unifying multi-model denoising for adaptive denoising policy selection. The architecture pre-trains specialized denoisers for distinct noise profiles like sparsity and temporal drift, and employs a Deep Q-Network (DQN) to dynamically select denoising weights.

### 3. **ADM-DP: Adaptive Dynamic Modality Diffusion Policy**
For efficient inference, ADM-DP adopts DDIM sampling to accelerate inference, requiring only 20 denoising steps to generate actions. This work focuses on multi-agent manipulation with vision-tactile-graph fusion.

### 4. **MODIFy: Multi-modal Anomaly Diagnosis with Diffusion-Enhanced Adaptive Fusion**
Single-modal features are integrated through a multi-scale channel-adaptive convolutional gated fusion module, which models multimodal features at different resolutions through multi-scale convolutions while adaptively weighting features across modalities.

### 5. **Denoising Diffusion Model-Driven Adaptive Estimation**
A user interest preference model based on a denoising diffusion model is established by learning the fusion representation of multi-modal data.

These papers represent the cutting edge of research combining multi-modal diffusion models with adaptive or dynamic denoising strategies from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87dd7083-b11e-4234-8f9f-ea72219b910c",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "ca864717-58ef-406a-a751-04ede372e767",
  "sourceToolAssistantUUID": "87dd7083-b11e-4234-8f9f-ea72219b910c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T19:38:32.830Z_

<details><summary>↩ Tool result · `toolu_01KSQpqcv8VZoei8P5Vy6Nie`</summary>

```text
Web search results for query: "WorldCache "token caching" video world model acceleration denoising 2026"

Links: [{"title":"Paper page - WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching","url":"https://huggingface.co/papers/2603.06331"},{"title":"WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching","url":"https://arxiv.org/html/2603.06331"},{"title":"[2603.06331] WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching","url":"https://arxiv.org/abs/2603.06331"},{"title":"WorldCache: Content-Aware Caching for Accelerated Video World Models [Quick Review]","url":"https://liner.com/review/worldcache-contentaware-caching-for-accelerated-video-world-models"},{"title":"WorldCache: Content-Aware Caching for Accelerated Video World Models","url":"https://arxiv.org/pdf/2603.22286"},{"title":"(PDF) WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching","url":"https://www.researchgate.net/publication/401692389_WorldCache_Accelerating_World_Models_for_Free_via_Heterogeneous_Token_Caching"},{"title":"GitHub - umair1221/WorldCache: WorldCache: Content-Aware Caching for Accelerated Video World Models · GitHub","url":"https://github.com/umair1221/WorldCache"},{"title":"X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference","url":"https://arxiv.org/html/2604.20289v2"},{"title":"[2603.22286] WorldCache: Content-Aware Caching for Accelerated Video World Models","url":"https://arxiv.org/abs/2603.22286"},{"title":"WorldCache — Content-Aware Caching for Accelerated Video World Models","url":"https://umair1221.github.io/World-Cache/"}]

Based on the search results, I found information about WorldCache, which appears to refer to two related research papers on token caching for accelerating world models:

## WorldCache: Heterogeneous Token Caching (Paper 1)

WorldCache is a caching framework tailored to diffusion world models. It introduces Curvature-guided Heterogeneous Token Prediction, which uses a physics-grounded curvature score to estimate token predictability and applies a Hermite-guided damped predictor for chaotic tokens with abrupt direction changes.

WorldCache alternates between FULL and CACHE steps during denoising. In FULL, it evaluates the backbone to refresh cached outputs, estimate token curvature, and update token groups. In CACHE, it predicts the surrogate output via heterogeneous token prediction (reuse / linear / damped) and updates the curvature-normalized drift accumulator.

WorldCache delivers up to 3.7× end-to-end speedups while maintaining 98% rollout quality.

## WorldCache: Content-Aware Caching (Paper 2)

Diffusion Transformers (DiTs) power high-fidelity video world models but remain computationally expensive due to sequential denoising and costly spatio-temporal attention. Training-free feature caching accelerates inference by reusing intermediate activations across denoising steps; however, existing methods largely rely on a Zero-Order Hold assumption.

WorldCache is a Perception-Constrained Dynamical Caching framework that improves both when and how to reuse features. It introduces motion-adaptive thresholds, saliency-weighted drift estimation, optimal approximation via blending and warping, and phase-aware threshold scheduling across diffusion steps.

On Cosmos-Predict2.5-2B evaluated on PAI-Bench, WorldCache achieves 2.3× inference speedup while preserving 99.4% of baseline quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56903b0f-9ec9-4863-8ff0-9f4225eda158",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "67d3b2d4-27a1-4991-936f-f8360d3d523c",
  "sourceToolAssistantUUID": "56903b0f-9ec9-4863-8ff0-9f4225eda158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-10T19:38:35.542Z_

Let me do one more targeted search for the most specific overlap -- monitoring convergence signals during joint video+action denoising.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67d3b2d4-27a1-4991-936f-f8360d3d523c",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTGq5Pv5PW23svQA9LT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00c8df5e-2899-479b-a73a-ab2f9e36cfce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJqgyXGkVWbLh2FidisWwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1106,
      "cache_creation_input_tokens": 3194,
      "cache_read_input_tokens": 26890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3194,
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

_source line 52 · 2026-05-10T19:38:36.706Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DRoLk5dYrnpAwLeRWbtQ7s`</summary>

```json
{
  "query": "AdaDiff \"adaptive step selection\" diffusion convergence signal early exit 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00c8df5e-2899-479b-a73a-ab2f9e36cfce",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTGq5Pv5PW23svQA9LT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfb2004d-d37e-46f6-ab12-7367116ccc9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJqgyXGkVWbLh2FidisWwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1106,
      "cache_creation_input_tokens": 3194,
      "cache_read_input_tokens": 26890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3194,
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

_source line 53 · 2026-05-10T19:38:37.489Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WewvJrSDsSCYmqt3JndpxN`</summary>

```json
{
  "query": "\"TACA\" \"cross-modal attention\" multimodal diffusion transformer rebalancing 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfb2004d-d37e-46f6-ab12-7367116ccc9b",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTGq5Pv5PW23svQA9LT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7381bda-f8ce-426a-ab64-94bab3d6943f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJqgyXGkVWbLh2FidisWwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1106,
      "cache_creation_input_tokens": 3194,
      "cache_read_input_tokens": 26890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3194,
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

_source line 54 · 2026-05-10T19:38:44.407Z_

<details><summary>↩ Tool result · `toolu_01DRoLk5dYrnpAwLeRWbtQ7s`</summary>

```text
Web search results for query: "AdaDiff "adaptive step selection" diffusion convergence signal early exit 2024 2025"

Links: [{"title":"[2311.14768] AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://arxiv.org/abs/2311.14768"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/33075"},{"title":"AdaDiff: Accelerating Diffusion Models Through Step-Wise Adaptive Computation | Computer Vision – ECCV 2024","url":"https://dl.acm.org/doi/10.1007/978-3-031-72986-7_5"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://ojs.aaai.org/index.php/AAAI/article/download/33075/35230"},{"title":"AdaDiff: Accelerating Diffusion Models Through Step-Wise Adaptive Computation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-72986-7_5"},{"title":"ECCV Poster AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation","url":"https://eccv.ecva.net/virtual/2024/poster/2161"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://arxiv.org/html/2311.14768v2"},{"title":"GitHub - Tangshengku/AdaDiff: Official Pytorch Implementation of Paper \"AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation\" · GitHub","url":"https://github.com/Tangshengku/AdaDiff"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion","url":"https://www.emergentmind.com/papers/2311.14768"},{"title":"AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10120.pdf"}]

Based on the search results, I found information about two related approaches using the AdaDiff name:

## AdaDiff: Adaptive Step Selection for Fast Diffusion Models

AdaDiff is a lightweight framework designed to learn instance-specific step usage policies, which are then used by the diffusion model for generation. AdaDiff is optimized using a policy gradient method to maximize a carefully designed reward function, balancing inference time and generation quality. 

AdaDiff allocates more steps to more informative prompts and fewer steps to simpler prompts. The results show that the approach achieves similar visual quality compared to the baseline using a fixed 50 denoising steps while reducing inference time by at least 33%, going as high as 40%.

## AdaDiff: Accelerating Diffusion Models Through Step-Wise Adaptive Computation

A separate but related approach with the same name was presented at ECCV 2024. An Uncertainty Estimation Module (UEM) integrated at each intermediate layer evaluates the predictive uncertainty, which serves as an indicator for determining whether to terminate the inference process. Comprehensive experiments demonstrate superior performance and efficiency of AdaDiff relative to current early exiting techniques in diffusion models, with an acceleration ratio reduction of around 45%. AdaDiff achieves more than 40% speedup with minimal performance drop on CIFAR-10, CelebA, COCO and ImageNet.

Both approaches address the computational expense of diffusion model inference through adaptive mechanisms, though they use different technical strategies—one based on policy gradient optimization for step selection, and the other using uncertainty estimation for early exiting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfb2004d-d37e-46f6-ab12-7367116ccc9b",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "6c20be4b-8ffc-4bc9-a31b-20c25158dde8",
  "sourceToolAssistantUUID": "cfb2004d-d37e-46f6-ab12-7367116ccc9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-10T19:38:44.937Z_

<details><summary>↩ Tool result · `toolu_01WewvJrSDsSCYmqt3JndpxN`</summary>

```text
Web search results for query: ""TACA" "cross-modal attention" multimodal diffusion transformer rebalancing 2025"

Links: [{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf"},{"title":"TACA: Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://arxiv.org/html/2506.07986v1"},{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://arxiv.org/html/2506.07986"},{"title":"Paper page - Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://huggingface.co/papers/2506.07986"},{"title":"[2506.07986] Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://arxiv.org/abs/2506.07986"},{"title":"[Literature Review] Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://www.themoonlight.io/en/review/rethinking-cross-modal-interaction-in-multimodal-diffusion-transformers"},{"title":"GitHub - Vchitect/TACA: TACA: Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://github.com/Vchitect/TACA"},{"title":"MMDit: Multimodal Diffusion Transformers","url":"https://www.emergentmind.com/topics/multimodal-diffusion-transformers-mmdit"},{"title":"Multimodal Diffusion Transformer","url":"https://www.emergentmind.com/topics/multimodal-diffusion-transformer"},{"title":"Multimodal Diffusion Transformers (MMDiT)","url":"https://www.emergentmind.com/topics/multimodal-diffusion-transformers-mmdit-2005a3fb-41c7-4015-a0ed-4829abfb52bf"}]

Based on the search results, I found comprehensive information about TACA and its application to multimodal diffusion transformers:

## TACA: Temperature-Adjusted Cross-Modal Attention

TACA (Temperature-Adjusted Cross-modal Attention) is a simple yet effective modification to the attention mechanism of Multimodal Diffusion Transformers (MM-DiT). It is a parameter-efficient method that dynamically rebalances cross-modal attention in multimodal diffusion.

### Key Technical Innovations

The approach introduces two key innovations: modality-specific temperature scaling and timestep-dependent adjustment of cross-modal interactions.

**Modality-Specific Temperature Scaling:** To mitigate the suppression of cross-attention caused by the dominance of visual tokens, the method amplifies the logits of visual-text interactions through a temperature coefficient, effectively rebalancing the competition in softmax by increasing the relative weight of cross-modal interactions.

**Timestep-Dependent Adjustment:** The temperature coefficient is made dependent on the denoising timestep to reflect the changing importance of textual guidance, using higher values in early steps for layout formation. Early steps are crucial for global composition and require strong textual guidance, while later steps focus on fine details and self-attention becomes more important.

### Performance and Applications

Combined with LoRA fine-tuning to reduce artifacts, TACA significantly improved text-image alignment on the T2I-CompBench benchmark. TACA has been tested on state-of-the-art models like FLUX and SD3.5, demonstrating its ability to improve image-text alignment in terms of object appearance, attribute binding, and spatial relationships.

The code is publicly available on GitHub at the Vchitect/TACA repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7381bda-f8ce-426a-ab64-94bab3d6943f",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "adcca2df099752510",
  "type": "user",
  "uuid": "3f9cb3eb-a6b4-4551-b6e3-13c7fe1de9fa",
  "sourceToolAssistantUUID": "f7381bda-f8ce-426a-ab64-94bab3d6943f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-10T19:39:44.119Z_

I now have comprehensive results. Here is my report.

---

## Literature Review: Competing and Concurrent Work on Adaptive Inference for World-Action Models

I searched extensively across 16 queries covering adaptive denoising, cross-modal convergence, quality guarantees, self-correcting diffusion, WAM acceleration, and convergence caching. Below are the papers most relevant to a proposal about monitoring per-modality convergence signals during joint video+action denoising to adaptively allocate or extend denoising steps with quality floor guarantees.

---

### TIER 1: Directly Competing / Highly Overlapping

These papers address adaptive denoising step allocation in the same WAM or diffusion-policy domain and must be cited/differentiated.

**1. X-WAM: Unified 4D World Action Modeling with Asynchronous Denoising (April 2026)**
- [arXiv 2604.26694](https://arxiv.org/html/2604.26694v2)
- Proposes **Asynchronous Noise Sampling (ANS)**: during joint video+action denoising, actions are decoded with fewer initial steps and dispatched early, while video completes the full schedule. This is a form of per-modality adaptive step allocation during joint denoising -- arguably the closest existing work. The key difference from "cross-modal self-correction" would be that ANS uses a fixed asymmetric schedule rather than dynamically monitoring convergence, but the overlap is substantial.

**2. D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning (August 2025)**
- [arXiv 2508.06804](https://arxiv.org/abs/2508.06804)
- Uses an RL-trained lightweight adaptor to dynamically choose how many denoising steps each action gets at test time, allocating more steps to crucial actions and fewer to routine ones. Achieves 2.2x speedup. This is single-modality (action only) but is the closest precedent for adaptive step allocation in diffusion policies.

**3. VADF: Vision-Adaptive Diffusion Policy Framework (April 2026)**
- [arXiv 2604.15938](https://arxiv.org/abs/2604.15938)
- A dual-adaptive framework that (a) accelerates training convergence via an Adaptive Loss Network, and (b) at inference, uses a vision-based task segmenter to assign shorter noise schedules to simple sub-tasks and longer schedules to complex ones. Achieves faster convergence and early success. Relevant because it adaptively varies denoising steps based on task complexity signals.

**4. TS-DP: Temporal-Aware Reinforcement Speculative Decoding for Diffusion Policy (December 2025)**
- [arXiv 2512.15773](https://arxiv.org/abs/2512.15773)
- Applies speculative decoding to diffusion policies with an RL-based scheduler that adapts speculative parameters over time based on task difficulty. Achieves 4.17x speedup at 25 Hz. The adaptive scheduling mechanism is conceptually related.

**5. Fast-WAM: Do World Action Models Need Test-time Future Imagination? (March 2026)**
- [arXiv 2603.16666](https://arxiv.org/abs/2603.16666)
- Takes the radical position that video denoising at test time is unnecessary -- you can skip it entirely and just use action denoising with a video-trained backbone. 4x faster at 190ms latency. This is relevant as a competing philosophy: rather than adaptively monitoring video convergence, just skip video generation at inference entirely.

**6. When to Trust Imagination: Adaptive Action Execution for WAMs (May 2026)**
- [arXiv 2605.06222](https://arxiv.org/abs/2605.06222)
- Proposes FFDC (Future Forward Dynamics Causal Attention), which monitors whether the WAM's predicted future remains consistent with reality and adaptively extends or truncates action execution. Reduces WAM forward passes by 69%. While this operates at the action-execution level rather than the denoising-step level, it is conceptually close to "monitoring convergence and adapting accordingly."

---

### TIER 2: Strongly Related Methods and Frameworks

**7. MotuBrain: Advanced World Action Model (April 2026)**
- [arXiv 2604.27792](https://arxiv.org/html/2604.27792v2)
- Achieves 50x+ speedup through DiT caching: after initial computation, the video latent is frozen and only action tokens are updated in subsequent denoising steps, reusing cached video keys/values. Runs at 11 Hz. This is a form of modality-asymmetric denoising (video converges first, then is cached), though it is a fixed schedule rather than adaptive.

**8. ADPro: Test-time Adaptive Diffusion Policy (August 2025)**
- [arXiv 2508.06266](https://arxiv.org/abs/2508.06266)
- Introduces manifold-constrained denoising and task-aware initialization to reduce the number of denoising steps needed. Achieves up to 25% improvement in success rates. Relevant for its convergence-acceleration approach at test time.

**9. TACA: Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers (ICCV 2025)**
- [arXiv 2506.07986](https://arxiv.org/abs/2506.07986)
- Introduces modality-specific temperature scaling and timestep-dependent adjustment of cross-modal attention in MM-DiT. Higher cross-modal attention weights in early denoising steps, lower in later steps. Directly relevant to the concept of modality-aware denoising dynamics.

**10. Entropy-Adaptive Diffusion Policy Optimization with Dynamic Step Alignment (ICCV 2025)**
- [ICCV 2025 paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_Entropy-Adaptive_Diffusion_Policy_Optimization_with_Dynamic_Step_Alignment_ICCV_2025_paper.pdf)
- Uses entropy as a convergence signal and dynamically adjusts regularization guided by real-time quality estimation of intermediate noised states. Relevant to the idea of monitoring signals during denoising to adapt behavior.

---

### TIER 3: Related Infrastructure / Acceleration

**11. AdaDiff: Adaptive Step Selection for Fast Diffusion Models (AAAI 2025)**
- [arXiv 2311.14768](https://arxiv.org/abs/2311.14768)
- Learns instance-specific step usage policies via policy gradient, allocating more steps to complex prompts, fewer to simple ones. 33-40% speedup. General-purpose (image generation), but establishes the idea of learned adaptive step allocation.

**12. Self-Correcting Discrete Diffusion (SCDD) (February 2026)**
- [arXiv 2603.02230](https://arxiv.org/abs/2603.02230)
- Self-correction during denoising for discrete diffusion (language), where the model corrects its own errors during the backward process. Conceptually related to "self-correction during denoising" but in the language domain.

**13. WorldCache: Heterogeneous Token Caching for World Models (March 2026)**
- [arXiv 2603.06331](https://arxiv.org/abs/2603.06331) and [arXiv 2603.22286](https://arxiv.org/abs/2603.22286)
- Uses curvature-guided token prediction to decide which tokens to cache vs. recompute during denoising. Up to 3.7x speedup. Relevant as infrastructure that could complement adaptive step allocation.

---

### Key Gaps and Assessment

**What appears genuinely novel in "cross-modal self-correction":**
No paper I found explicitly proposes monitoring per-modality convergence signals (e.g., video convergence rate vs. action convergence rate) during joint denoising and using those signals to dynamically extend or reallocate steps with quality floor guarantees. The closest work is:

- **X-WAM's ANS** uses a fixed asymmetric schedule (actions finish early, video runs full), not a dynamic/adaptive one based on convergence monitoring.
- **D3P** adapts steps but only for actions (single modality), not cross-modal.
- **MotuBrain** freezes one modality (video) after initial steps, but this is a fixed caching strategy, not convergence-driven.
- **VADF** adapts based on task complexity, not per-modality convergence signals.

**What the proposal must address:**
The proposal should explicitly differentiate from X-WAM (asynchronous but fixed schedule), D3P (adaptive but single-modality), Fast-WAM (skip video entirely), MotuBrain (asymmetric caching), VADF (task-complexity-driven adaptation), and the "When to Trust Imagination" paper (adaptive execution length, not denoising steps). The concept of quality floor guarantees also needs to be contrasted with D3P's RL reward design and VADF's early success metrics.

Sources:
- [X-WAM: Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)
- [D3P: Dynamic Denoising Diffusion Policy](https://arxiv.org/abs/2508.06804)
- [VADF: Vision-Adaptive Diffusion Policy](https://arxiv.org/abs/2604.15938)
- [TS-DP: Speculative Decoding for Diffusion Policy](https://arxiv.org/abs/2512.15773)
- [Fast-WAM](https://arxiv.org/abs/2603.16666)
- [When to Trust Imagination](https://arxiv.org/abs/2605.06222)
- [MotuBrain](https://arxiv.org/html/2604.27792v2)
- [ADPro: Test-time Adaptive Diffusion Policy](https://arxiv.org/abs/2508.06266)
- [TACA: Cross-Modal Attention in MM-DiT](https://arxiv.org/abs/2506.07986)
- [Entropy-Adaptive Diffusion Policy (ICCV 2025)](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_Entropy-Adaptive_Diffusion_Policy_Optimization_with_Dynamic_Step_Alignment_ICCV_2025_paper.pdf)
- [AdaDiff: Adaptive Step Selection (AAAI)](https://arxiv.org/abs/2311.14768)
- [SCDD: Self-Correcting Discrete Diffusion](https://arxiv.org/abs/2603.02230)
- [WorldCache: Heterogeneous Token Caching](https://arxiv.org/abs/2603.06331)
- [WorldCache: Content-Aware Caching](https://arxiv.org/abs/2603.22286)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f9cb3eb-a6b4-4551-b6e3-13c7fe1de9fa",
  "isSidechain": true,
  "agentId": "adcca2df099752510",
  "requestId": "req_011CauTHiUYmRJZF4euJTQwJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65fe56e0-d530-4aa5-883f-4298e52b6e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbiSVVUxovWcnRzvYD5LnK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3250,
      "cache_read_input_tokens": 30084,
      "output_tokens": 2699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3250
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2699,
          "cache_read_input_tokens": 30084,
          "cache_creation_input_tokens": 3250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3250,
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
