# Research conversation: You are helping with an ML paper review. I need to find any recent work (2025-2026) that proposes adaptive or self-corre

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a731ae481ce349556.jsonl`
- **Structured JSON:** [`90dfe5cce9a8d4b38f58.json`](../../sessions/90/90dfe5cce9a8d4b38f58.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-10T18:36:34.911Z_

You are helping with an ML paper review. I need to find any recent work (2025-2026) that proposes adaptive or self-correcting inference for diffusion models in robotics/world models, especially:

1. Any work that does CROSS-MODAL verification within denoising (checking video prediction against action prediction for quality)
2. Any work on adaptive step allocation for multi-modal diffusion models
3. Any work on quality-floor guarantees for diffusion inference
4. Any work on self-correcting diffusion inference (extending steps when quality is low)

Search for:
- "adaptive inference diffusion robotics 2026"
- "cross-modal verification denoising world model"
- "quality guarantee diffusion policy"
- "self-correcting diffusion inference"
- "adaptive denoising steps robot manipulation 2026"
- "per-sample adaptive diffusion steps"
- "diffusion early stopping quality guarantee"

Also search for:
- "MotuBrain world action model" to verify its caching mechanism
- "FFDC-WAM" or "when to trust imagination world action model" 
- "SpectralCache CVPR 2026" 
- "AdaCorrection adaptive cache correction"

For each search, report what you found. I need to know if anyone has already proposed the idea of cross-modal disagreement detection within denoising as a quality oracle for WAMs. Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "a7b5b2ad-1bb3-4c71-9ebd-5d52e5bb3ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:36:34.917Z_

```json
{
  "parentUuid": "a7b5b2ad-1bb3-4c71-9ebd-5d52e5bb3ead",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
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
  "uuid": "289116c8-16aa-4bfc-b80a-5d6c6e7f379f",
  "timestamp": "2026-05-10T18:36:34.917Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:36:43.685Z_



I'll conduct a comprehensive search across all these queries. Let me start by loading the WebSearch tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "289116c8-16aa-4bfc-b80a-5d6c6e7f379f",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNYm8cxuDnRb55yBQoj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ccb57dca-777f-446f-957a-dbbf2f0b4502",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Epgjeo4Kp4epTEbkxWtY72",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
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

_source line 4 · 2026-05-10T18:36:43.977Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CnE7SmTQ8usTg6jvXKhjpi`</summary>

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
  "parentUuid": "ccb57dca-777f-446f-957a-dbbf2f0b4502",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNYm8cxuDnRb55yBQoj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5660d1e1-2c66-46b5-8b59-4ec046be3cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Epgjeo4Kp4epTEbkxWtY72",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 8223,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 873,
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

_source line 5 · 2026-05-10T18:36:43.981Z_

<details><summary>↩ Tool result · `toolu_01CnE7SmTQ8usTg6jvXKhjpi`</summary>

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
  "parentUuid": "5660d1e1-2c66-46b5-8b59-4ec046be3cb0",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "d6a5db8a-5e7a-45aa-8547-2f752f47951c",
  "sourceToolAssistantUUID": "5660d1e1-2c66-46b5-8b59-4ec046be3cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:36:57.192Z_



Now let me run all the searches in parallel batches. Starting with the first batch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6a5db8a-5e7a-45aa-8547-2f752f47951c",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNZRzTsYhFQorbWEyBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a69fc638-15d7-4849-bfbb-dcda0294277f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoxE1d6b5LQsthaALnumx2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 7 · 2026-05-10T18:36:58.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NWdNB8MDyXTZ6tycLnWY7V`</summary>

```json
{
  "query": "adaptive inference diffusion robotics 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a69fc638-15d7-4849-bfbb-dcda0294277f",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNZRzTsYhFQorbWEyBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d88b4c1-20ab-4cdc-825a-fa6cec7d6774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoxE1d6b5LQsthaALnumx2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 8 · 2026-05-10T18:36:58.807Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Lb6PSV39mqeVeHVugV3QS`</summary>

```json
{
  "query": "cross-modal verification denoising world model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d88b4c1-20ab-4cdc-825a-fa6cec7d6774",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNZRzTsYhFQorbWEyBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dec3220b-d745-4c36-aa2a-1694086205e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoxE1d6b5LQsthaALnumx2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 9 · 2026-05-10T18:36:59.156Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DExo2eMXfLdw5bQGbJo7vb`</summary>

```json
{
  "query": "quality guarantee diffusion policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dec3220b-d745-4c36-aa2a-1694086205e8",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNZRzTsYhFQorbWEyBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4e087cd-d1a7-42ae-bd06-dd41cc31e2ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoxE1d6b5LQsthaALnumx2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9096,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 9096,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1415,
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

### Tool call

_source line 10 · 2026-05-10T18:36:59.193Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E7PcPRX4iK7BqZBp2FqHuZ`</summary>

```json
{
  "query": "self-correcting diffusion inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4e087cd-d1a7-42ae-bd06-dd41cc31e2ca",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNZRzTsYhFQorbWEyBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a88116f-2792-4887-8289-7a7261d93f18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoxE1d6b5LQsthaALnumx2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9096,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 9096,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1415,
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

_source line 11 · 2026-05-10T18:37:05.652Z_

<details><summary>↩ Tool result · `toolu_019Lb6PSV39mqeVeHVugV3QS`</summary>

```text
Web search results for query: "cross-modal verification denoising world model"

Links: [{"title":"Multi-model cooperative denoising for robust cross-modal retrieval with noisy labels | Multimedia Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00530-025-02121-9"},{"title":"Denoising and Verification Cross-Layer Ensemble Against Black-box Adversarial Attacks | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9006090/"},{"title":"Adaptive Latent Interaction Reasoning for Multimodal ...","url":"https://www.preprints.org/frontend/manuscript/d48afc20056b3399d571ec0d7f238a9f/download_pub"},{"title":"DMformer: a transformer with denoising and multi-modal data fusion for enhancing BEV perception | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-01984-9"},{"title":"Multimodal Fake News Detection: MFND Dataset and Shallow-Deep Multitask","url":"https://www.ijcai.org/proceedings/2025/0891.pdf"},{"title":"Diffusion-Based Cross-Modal Denoising and Reliability-Aware Deep Matching for Robust Radar Odometry | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-5567-3_35"},{"title":"A Survey of Multimodal Controllable Diffusion Models","url":"https://jcst.ict.ac.cn/fileup/1000-9000/PDF/JCST-2024-3-2-3814-509.pdf"},{"title":"Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks","url":"https://arxiv.org/html/2603.04364v1"},{"title":"Evolving from Single-modal to Multi-modal Facial Deepfake Detection: A Survey","url":"https://arxiv.org/html/2406.06965v1"},{"title":"Source-free cross-modality medical image synthesis with diffusion priors | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00200-5"}]

Based on the search results, here's what I found about cross-modal verification denoising world models:

The search returned several relevant papers on cross-modal denoising and verification techniques:

## Key Research Areas

**Cross-Modal Denoising Applications:**
One approach leverages a decoupled conditional diffusion model to process radar point clouds, generating LiDAR-like point clouds for effective cross-modal denoising. This is applied to radar odometry applications.

**Multi-Modal Fusion and Denoising:**
DMFormer is an innovative multi-modal BEV perception framework that employs Transformer architecture and a diffusion denoising model to tackle key challenges, including sensor noise, efficient fusion of multi-modal data, and modeling dynamic scenes. This system is designed for autonomous driving applications.

**Cross-Modal Verification Techniques:**
MODEF intelligently combines unsupervised model denoising ensemble with supervised model verification ensemble by quantifying model diversity, aiming to boost the robustness of the target model against adversarial examples.

**Multimodal Learning with Noise Handling:**
A Multi-Model Cooperative Denoising (MMCD) approach adaptively clarifies data labels and filters out noisy labels for robust cross-modal retrieval with noisy labels.

These approaches demonstrate how cross-modal verification and denoising techniques are being applied across various domains including autonomous driving perception, medical imaging, radar processing, and retrieval tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dec3220b-d745-4c36-aa2a-1694086205e8",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "8c084fa9-f6cd-4ed2-8cad-30ef588155a1",
  "sourceToolAssistantUUID": "dec3220b-d745-4c36-aa2a-1694086205e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:37:05.779Z_

<details><summary>↩ Tool result · `toolu_01NWdNB8MDyXTZ6tycLnWY7V`</summary>

```text
Web search results for query: "adaptive inference diffusion robotics 2026"

Links: [{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"D3P: Dynamic Denoising Diffusion Policy via ...","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"How Active Inference Could Help Revolutionise Robotics","url":"https://www.mdpi.com/1099-4300/24/3/361"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.21251"},{"title":"How Active Inference Could Help Revolutionise Robotics - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8946999/"},{"title":"Diffusion Model in Robotics: A Comprehensive Review by Linxin Bai, Chenkang Du, Liangjing Shao, Xiaobo Yang, Xinrong Chen :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/df28019c-c464-43dc-984d-21d6d8716696-MECA.pdf?abstractid=5237963&mirid=1"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising","url":"https://arxiv.org/pdf/2510.21991"},{"title":"DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11093775/;jsessionid=6E0FE0B577259E9262C880455054586A"}]

Based on the search results, here are some key findings about adaptive inference, diffusion models, and robotics in 2026:

## Adaptive Inference in Diffusion-Based Robotics

Recent work proposes Dynamic Denoising Diffusion Policy (D3P), a diffusion-based policy that adaptively allocates denoising steps across actions at test time. D3P uses a lightweight, state-aware adaptor to allocate the optimal number of denoising steps for each action, with the adaptor and base diffusion policy jointly optimized via reinforcement learning to balance task performance and inference efficiency. On simulated tasks, D3P achieves an averaged 2.2x inference speed-up over baselines without degrading success.

## Mixture-of-Experts Approaches

A diffusion-based mixture-of-experts policy called Skill Mixture-of-Experts Policy (SMP) performs skill abstraction in a locally whitened action space. The method includes an adaptive expert activation strategy that dynamically selects a compact subset of experts at inference time, reducing computational cost while maintaining action sampling accuracy.

## Recent Advances in Diffusion-Based Robotics

Since 2022, there has been a noticeable increase in the implementation of diffusion probabilistic models within robotic manipulation, applied across various tasks including trajectory planning and grasp prediction. Several recent methods address sampling speed specifically for applications in robotic manipulation.

## Adaptive Dexterous Manipulation

DexHand-Diff is an interaction-aware diffusion planning framework for adaptive dexterous manipulation that models joint state-action dynamics through a dual-phase diffusion process consisting of pre-interaction contact alignment and post-contact goal-directed control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d88b4c1-20ab-4cdc-825a-fa6cec7d6774",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "fbb6f460-e189-4814-872b-6c6d74b0f19f",
  "sourceToolAssistantUUID": "8d88b4c1-20ab-4cdc-825a-fa6cec7d6774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:37:05.904Z_

<details><summary>↩ Tool result · `toolu_01DExo2eMXfLdw5bQGbJo7vb`</summary>

```text
Web search results for query: "quality guarantee diffusion policy"

Links: [{"title":"How Well do Diffusion Policies Learn Kinematic Constraint Manifolds?","url":"https://arxiv.org/html/2510.01404"},{"title":"Diffusion Policy Explained. This is a detailed breakdown of the… | by Fotios (Fotis) Lygerakis | Medium","url":"https://medium.com/@ligerfotis/diffusion-policy-explained-14a3075ba26c"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"3D Diffusion Policy","url":"https://3d-diffusion-policy.github.io/"},{"title":"GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub","url":"https://github.com/real-stanford/diffusion_policy"},{"title":"Quality Guarantees That Sell: Write & Promote Yours Right","url":"https://deliberatedirections.com/quality-guarantee-that-sells/"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Paper Review: Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | by Yutong Zhang | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/diffusion-policy-applying-diffusion-model-to-policy-learning-8ee16fc056bb"},{"title":"Quality Guarantee - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/engineering/quality-guarantee"},{"title":"Policy-Guided Diffusion","url":"https://arxiv.org/html/2404.06356v1"}]

Based on the web search results, I found information related to diffusion policies in robotics research. Here's what the search revealed:

## Diffusion Policy Overview

Diffusion policy is based on diffusion models, which are generative models that can learn the distribution of a dataset and create new data points from this distribution.

## Quality and Constraint Satisfaction

Regarding quality in diffusion policies, the search results highlight important considerations:

There is value in quantifying the extent to which diffusion policies adhere to the constraint manifold in robot data, as well as carefully studying the factors that affect the quality of this adherence.

Research on diffusion policies examines how three factors affect trained policies: dataset size, dataset quality, and manifold curvature, with experiments showing diffusion policies learn a coarse approximation of the constraint manifold with learning affected negatively by decreases in both dataset size and quality.

## Performance and Advantages

Diffusion Policy consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%. The diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability.

The search results primarily focus on diffusion policies in the context of robotics and machine learning rather than quality guarantee policies in a traditional business sense.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4e087cd-d1a7-42ae-bd06-dd41cc31e2ca",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "078d8003-92ed-41d1-86cf-c48f98ff2042",
  "sourceToolAssistantUUID": "d4e087cd-d1a7-42ae-bd06-dd41cc31e2ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:37:06.293Z_

<details><summary>↩ Tool result · `toolu_01E7PcPRX4iK7BqZBp2FqHuZ`</summary>

```text
Web search results for query: "self-correcting diffusion inference"

Links: [{"title":"[2603.02230] Generalized Discrete Diffusion with Self-Correction","url":"https://arxiv.org/abs/2603.02230"},{"title":"Generalized Discrete Diffusion with Self-Correction","url":"https://arxiv.org/html/2603.02230"},{"title":"Learn from Your Mistakes: Self-Correcting Masked Diffusion Models","url":"https://arxiv.org/html/2602.11590"},{"title":"[2602.11590] Learn from Your Mistakes: Self-Correcting Masked Diffusion Models","url":"https://arxiv.org/abs/2602.11590"},{"title":"BackPlay: Plug-in Look-Back Self-Correction for Diffusion ...","url":"https://www.arxiv.org/pdf/2601.06428"},{"title":"[2311.16090] Self-correcting LLM-controlled Diffusion ... - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2311.16090"},{"title":"Self-correcting LLM-controlled Diffusion Models","url":"https://arxiv.org/html/2311.16090"},{"title":"Self-correcting LLM-controlled Diffusion Models Tsung-Han Wu* Long Lian*","url":"https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_Self-correcting_LLM-controlled_Diffusion_Models_CVPR_2024_paper.pdf"},{"title":"Self-Correcting LLM-Controlled Diffusion Models | Request PDF","url":"https://www.researchgate.net/publication/384235785_Self-Correcting_LLM-Controlled_Diffusion_Models"},{"title":"Self-Correcting LLM-Controlled Diffusion (SLD)","url":"https://www.emergentmind.com/topics/self-correcting-llm-controlled-diffusion-sld-framework"}]

Based on the search results, here's what I found about self-correcting diffusion inference:

## Overview

Self-correction is an effective technique for maintaining parallel sampling in discrete diffusion models with minimal performance degradation.

## Key Approaches

There are several notable methods in this area:

**1. Progressive Self-Correction (ProSeCo):** Masked diffusion models (MDMs) have emerged as a promising alternative to autoregressive models, enabling parallel token generation while achieving competitive performance. Despite these advantages, MDMs face a fundamental limitation: once tokens are unmasked, they remain fixed, leading to error accumulation and ultimately degrading sample quality. ProSeCo addresses this by applying additional corrective refinement steps between unmasking ones in order to change decoded tokens and improve outputs.

**2. Self-Correcting Discrete Diffusion (SCDD):** SCDD model reformulates pretrained self-correction with explicit state transitions and learn directly in discrete time.

**3. LLM-Controlled Diffusion (SLD):** SLD is a framework that integrates LLM-driven feedback with diffusion models, enabling iterative correction of latent outputs based on complex prompt requirements.

## Performance Improvements

ProSeCo yields better quality-efficiency trade-offs (up to ~2-3x faster sampling) and enables inference-time compute scaling to further increase sample quality beyond standard MDMs (up to ~1.3x improvement on benchmarks).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a88116f-2792-4887-8289-7a7261d93f18",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "a2919194-7e79-4cd7-a8c8-a85e3bb00f71",
  "sourceToolAssistantUUID": "3a88116f-2792-4887-8289-7a7261d93f18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T18:37:08.874Z_

Good results so far. Let me continue with the next batch of searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2919194-7e79-4cd7-a8c8-a85e3bb00f71",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNb59ebv9nD8qJwBHHZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88744bf3-23b2-4707-91b1-bdb91fa158cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9iwjysrnHUi6ycA1mf4e2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3881,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3881,
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

_source line 16 · 2026-05-10T18:37:09.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QjtEFzDgxichj9V5ezefHQ`</summary>

```json
{
  "query": "adaptive denoising steps robot manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88744bf3-23b2-4707-91b1-bdb91fa158cd",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNb59ebv9nD8qJwBHHZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd39bd13-8f6e-4f8f-94a3-5e62874b5b6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9iwjysrnHUi6ycA1mf4e2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3881,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3881,
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

_source line 17 · 2026-05-10T18:37:09.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01USZbpm4dtUeW5NC25aNN5U`</summary>

```json
{
  "query": "per-sample adaptive diffusion steps inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd39bd13-8f6e-4f8f-94a3-5e62874b5b6b",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNb59ebv9nD8qJwBHHZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d56a9f6e-5791-4f8b-a18d-726c9776a824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9iwjysrnHUi6ycA1mf4e2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3881,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3881,
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

_source line 18 · 2026-05-10T18:37:10.352Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019tz2eDEevE5TJGYHT1wWVY`</summary>

```json
{
  "query": "diffusion early stopping quality guarantee inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d56a9f6e-5791-4f8b-a18d-726c9776a824",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNb59ebv9nD8qJwBHHZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fe92ada-c1a3-4a24-9fd8-5eb699a7e4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9iwjysrnHUi6ycA1mf4e2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3881,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3881,
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

_source line 19 · 2026-05-10T18:37:10.986Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qdwm5gzMprTwzzMBLTfSKQ`</summary>

```json
{
  "query": "MotuBrain world action model caching"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fe92ada-c1a3-4a24-9fd8-5eb699a7e4fe",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNb59ebv9nD8qJwBHHZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a91ed802-9a5e-4c27-879a-ce1b98ecb352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9iwjysrnHUi6ycA1mf4e2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3881,
      "cache_read_input_tokens": 10511,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3881
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 10511,
          "cache_creation_input_tokens": 3881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3881,
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

_source line 20 · 2026-05-10T18:37:16.531Z_

<details><summary>↩ Tool result · `toolu_01USZbpm4dtUeW5NC25aNN5U`</summary>

```text
Web search results for query: "per-sample adaptive diffusion steps inference"

Links: [{"title":"Adapt and Diffuse: Sample-Adaptive Reconstruction Via Latent Diffusion Models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11421836/"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://ojs.aaai.org/index.php/AAAI/article/download/33075/35230"},{"title":"Predict-then-Diffuse: Adaptive Response Length for Compute-Budgeted Inference in Diffusion LLMs","url":"https://arxiv.org/html/2605.04215"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://arxiv.org/html/2311.14768v2"},{"title":"Adapt and Diffuse: Sample-adaptive Reconstruction via Latent Diffusion Models","url":"https://arxiv.org/html/2309.06642"},{"title":"[2311.14768] AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://arxiv.org/abs/2311.14768"},{"title":"AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10120.pdf"},{"title":"Diffusion-Based Sampling Methods","url":"https://www.emergentmind.com/topics/diffusion-based-sampling"},{"title":"Stable Diffusion Samplers: A Comprehensive Guide - Stable Diffusion Art","url":"https://stable-diffusion-art.com/samplers/"},{"title":"Common Diffusion Noise Schedules and Sample Steps are Flawed Shanchuan Lin","url":"https://openaccess.thecvf.com/content/WACV2024/papers/Lin_Common_Diffusion_Noise_Schedules_and_Sample_Steps_Are_Flawed_WACV_2024_paper.pdf"}]

Based on the search results, here's what I found about per-sample adaptive diffusion steps inference:

## Overview

Per-sample adaptive diffusion steps inference refers to methods that dynamically adjust the number of denoising steps required for each individual sample during diffusion model inference, rather than using a fixed number of steps for all samples.

## Key Approaches

**AdaDiff**: Denoising steps should be sample-specific conditioned on the richness of input texts, and AdaDiff is a lightweight framework designed to learn instance-specific step usage policies. AdaDiff aims to dynamically decide the optimal step that achieves a balance between visual quality and inference time on a per-input basis.

**Flash-Diffusion**: This technique solves general noisy inverse problems based on latent diffusion models that leverages predicted degradation severities to fine-tune the reverse diffusion sampling trajectory and achieve sample-adaptive inference times. Flash-Diffusion achieves 8× to 10× acceleration in average number of reverse diffusion steps across the test dataset compared to the non-adaptive baseline, without any drop in reconstruction quality.

## Performance Benefits

AdaDiff achieves similar visual quality compared to a fixed 50 denoising steps baseline while reducing inference time by at least 33%, going as high as 40%. AdaDiff allocates more steps to more informative prompts and fewer steps to simpler prompts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d56a9f6e-5791-4f8b-a18d-726c9776a824",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "496aaaee-fb33-4946-a588-1d59f1f812d9",
  "sourceToolAssistantUUID": "d56a9f6e-5791-4f8b-a18d-726c9776a824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T18:37:17.350Z_

<details><summary>↩ Tool result · `toolu_01QjtEFzDgxichj9V5ezefHQ`</summary>

```text
Web search results for query: "adaptive denoising steps robot manipulation 2026"

Links: [{"title":"ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/html/2508.06266"},{"title":"D3P: Dynamic Denoising Difusion Policy via Reinforcement Learning Shu’ang Yu","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising | OpenReview","url":"https://openreview.net/forum?id=YY1MPKBHp7"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising","url":"https://arxiv.org/pdf/2510.21991"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Abstracting Robot Manipulation Skills via Mixture-of- ...","url":"https://arxiv.org/pdf/2601.21251"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"[2508.06266] ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/abs/2508.06266"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"}]

I found several relevant papers and research on adaptive denoising steps in robot manipulation from 2026. Here are the key findings:

## Dynamic Denoising Diffusion Policy (D3P)

D3P is a diffusion-based policy that adaptively allocates denoising steps across actions at test time. Research shows that robotic tasks often contain a mix of crucial and routine actions, which differ in their impact on task success. D3P uses a lightweight, state-aware adaptor to allocate the optimal number of denoising steps for each action. Using the same amount of training data, D3P achieves an average 2.2× inference speed-up over baseline methods while maintaining comparable performance.

## Adaptive Diffusion Policy (ADP)

ADP introduces structure into the denoising process through complementary mechanisms including a manifold constraint guided by the relative pose between end-effector and target object, and refinement of reverse diffusion dynamics using a Gaussian spherical prior that constrains denoising steps to lie on a hypersphere.

## Two-Steps Diffusion Policy via Genetic Denoising

Research shows that diffusion policies can operate effectively with as few as 5 neural function evaluations (NFE) by tailoring the denoising process to the specific characteristics of embodied AI tasks. This method consistently outperforms standard diffusion-based policies, achieving up to 20% performance gains with significantly fewer inference steps.

These recent 2026 approaches demonstrate significant progress in making robot manipulation more efficient by dynamically adapting the denoising process rather than using a fixed number of steps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd39bd13-8f6e-4f8f-94a3-5e62874b5b6b",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "c6ed8bc4-2a0a-469e-bb20-f9cdd996b5ef",
  "sourceToolAssistantUUID": "bd39bd13-8f6e-4f8f-94a3-5e62874b5b6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T18:37:18.117Z_

<details><summary>↩ Tool result · `toolu_01Qdwm5gzMprTwzzMBLTfSKQ`</summary>

```text
Web search results for query: "MotuBrain world action model caching"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/26497/"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html"},{"title":"ShengShu Technology Unveils Motubrain: A Unified \"World Action Model\" to Solve the Robotics Scaling Problem | Humanoids Daily","url":"https://www.humanoidsdaily.com/news/shengshu-technology-unveils-motubrain-a-unified-world-action-model-to-solve-the-robotics-scaling-problem"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/awesome-world-models"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://aithority.com/robots/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | The Manila Times","url":"https://www.manilatimes.net/2026/04/29/tmt-newswire/pr-newswire/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/2331652"},{"title":"GitHub - Robbyant/lingbot-va: Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/Robbyant/lingbot-va"},{"title":"[2512.13030] Motus: A Unified Latent Action World Model","url":"https://arxiv.org/abs/2512.13030"},{"title":"ChinaPulse.com - ShengShu Technology Unveils World Action Model “Motubrain”: One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.chinapulse.com/data-news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"}]

Based on the search results, here's what I found about MotuBrain's world action model caching:

## Key Caching Mechanism

MotuBrain's video latent is frozen, and the video-text branch is executed once to build per-layer cached keys and values for the fixed visual-language context.

## How Caching Improves Inference

Subsequent denoising steps update only the action tokens: action queries attend to the cached video/text keys and values together with their own action keys and values. This removes the repeated video-stream computation from the latter part of sampling while preserving the same attention semantics as the V2A-style model.

## Performance Impact

Combined with the other inference optimizations above, this design enables ours to reach a 11 Hz inference frequency, exceeding typical human reaction speed. More broadly, MotuBrain's systems-oriented inference stack including denoising-step reduction, compilation with CUDA-graph-friendly execution, FP8 quantization, and DiT caching together delivers more than 50x end-to-end speedup over the naive baseline.

The caching strategy is particularly effective because it avoids redundant computation of the visual-language context across multiple diffusion steps while still allowing the action generation process to attend to this cached information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a91ed802-9a5e-4c27-879a-ce1b98ecb352",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "2f2c087b-b265-4287-8f5e-73d0eae4d953",
  "sourceToolAssistantUUID": "a91ed802-9a5e-4c27-879a-ce1b98ecb352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T18:37:19.376Z_

<details><summary>↩ Tool result · `toolu_019tz2eDEevE5TJGYHT1wWVY`</summary>

```text
Web search results for query: "diffusion early stopping quality guarantee inference"

Links: [{"title":"[2205.12524] Accelerating Diffusion Models via Early Stop of the Diffusion Process","url":"https://arxiv.org/abs/2205.12524"},{"title":"(PDF) Accelerating Diffusion Models via Early Stop of the Diffusion Process","url":"https://www.researchgate.net/publication/360859429_Accelerating_Diffusion_Models_via_Early_Stop_of_the_Diffusion_Process"},{"title":"Consistency diffusion language models: Up to 14x faster inference without sacrificing quality","url":"https://www.together.ai/blog/consistency-diffusion-language-models"},{"title":"EDIT: Early Diffusion Inference Termination for dLLMs Based on Dynamics of Training Gradients","url":"https://arxiv.org/html/2512.00670v1"},{"title":"Under review. OPTIMAL STOPPING IN LATENT DIFFUSION MODELS Yu-Han Wu∗","url":"https://arxiv.org/pdf/2510.08409"},{"title":"AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10120.pdf"},{"title":"Optimizing Resource Consumption in Diffusion Models through Hallucination Early Detection","url":"https://arxiv.org/html/2409.10597v1"},{"title":"Diffusion Language Models Know the Answer Before Decoding","url":"https://arxiv.org/pdf/2508.19982"},{"title":"Optimal Stopping in Latent Diffusion Models","url":"https://arxiv.org/html/2510.08409v1"},{"title":"FAST-DECODING DIFFUSION LANGUAGE MODELS VIA PROGRESS-AWARE CONFIDENCE SCHEDULES","url":"https://arxiv.org/pdf/2512.02892"}]

I found several relevant research papers and articles about diffusion early stopping with quality guarantees. Here's a summary of the key findings:

## Key Research Areas

**Early Stopping Strategies for Diffusion Models:**

ES-DDPM (Early-Stopped DDPM) is a principled acceleration strategy that stops the diffusion process early where only the few initial diffusing steps are considered and the reverse denoising process starts from a non-Gaussian distribution. This approach improves sample quality substantially, outperforming both the vanilla DDPM and adopted pre-trained generative models.

**Quality Guarantees Through Optimal Stopping:**

Stopping at a specific time is an optimal strategy to improve generation quality by minimizing the distance between generated and true data distributions, and this strategy is not only computationally more efficient but also enhances generation quality by avoiding noise introduced by superfluous dimensions. Under a Gaussian framework with linear autoencoders, lower-dimensional representations benefit from earlier termination, whereas higher-dimensional latent spaces require later stopping time.

**Recent Advances in Diffusion Language Models:**

EDIT (Early Diffusion Inference Termination) preserves training metadata and uses it to guide early inference termination in diffusion language models by capturing optimization dynamics during fine-tuning to detect when reasoning is complete, reducing inference cost without architectural changes. It achieves 11.8–68.3% fewer diffusion steps while maintaining or improving accuracy.

**Uncertainty-Based Early Stopping:**

AdaDiff presents a timestep-aware uncertainty estimation module (UEM) that is integrated at each intermediate layer to evaluate predictive uncertainty, which serves as an indicator for determining whether to terminate the inference process.

These approaches provide both theoretical justifications and practical methods for implementing early stopping while maintaining or even improving output quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fe92ada-c1a3-4a24-9fd8-5eb699a7e4fe",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "8e339555-1932-4d52-b97e-f505fbce6cf3",
  "sourceToolAssistantUUID": "5fe92ada-c1a3-4a24-9fd8-5eb699a7e4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T18:37:21.893Z_

Excellent findings. Now let me search for the remaining queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e339555-1932-4d52-b97e-f505fbce6cf3",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNc36Pzvjxved58XwuP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df383409-4406-47d3-b92b-426b29448cae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwoUTTJ8gMABzv7RKARogV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1150,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 14392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2936,
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

_source line 25 · 2026-05-10T18:37:22.908Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DArsfr81Tg2ow2NVtGBJtb`</summary>

```json
{
  "query": "FFDC-WAM \"when to trust imagination\" world action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df383409-4406-47d3-b92b-426b29448cae",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNc36Pzvjxved58XwuP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "219c8198-bc03-4fb3-8234-e9559436679d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwoUTTJ8gMABzv7RKARogV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1150,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 14392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2936,
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

_source line 26 · 2026-05-10T18:37:23.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0121w4BnPaAPEof7JDSomDe9`</summary>

```json
{
  "query": "SpectralCache CVPR 2026 diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "219c8198-bc03-4fb3-8234-e9559436679d",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNc36Pzvjxved58XwuP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf3c6956-102e-4da0-85f8-c28f4dd4b750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwoUTTJ8gMABzv7RKARogV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1150,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 14392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2936,
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

_source line 27 · 2026-05-10T18:37:23.850Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WcoMHGoyn9xFPUmZb68V3n`</summary>

```json
{
  "query": "AdaCorrection adaptive cache correction diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf3c6956-102e-4da0-85f8-c28f4dd4b750",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNc36Pzvjxved58XwuP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcdc05d2-237b-46a6-9bef-b0001a7e0cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwoUTTJ8gMABzv7RKARogV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1150,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 14392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2936,
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

_source line 28 · 2026-05-10T18:37:24.312Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TmVHD6aid71SXtJhCsQiRC`</summary>

```json
{
  "query": "cross-modal disagreement detection diffusion denoising quality oracle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcdc05d2-237b-46a6-9bef-b0001a7e0cfe",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNc36Pzvjxved58XwuP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f54c4b6-8622-42db-a87b-75c3bc6b9faf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwoUTTJ8gMABzv7RKARogV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1150,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 14392,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1150,
          "output_tokens": 217,
          "cache_read_input_tokens": 14392,
          "cache_creation_input_tokens": 2936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2936,
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

_source line 29 · 2026-05-10T18:37:26.512Z_

<details><summary>↩ Tool result · `toolu_01DArsfr81Tg2ow2NVtGBJtb`</summary>

```text
Web search results for query: "FFDC-WAM "when to trust imagination" world action model"

Links: [{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"[2605.06222] When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/abs/2605.06222"}]

I found the research paper you're searching for! 

World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation by jointly predicting future visual observations and future actions. However, current WAMs typically execute a fixed number of predicted actions after each model inference, leaving the robot blind to whether the imagined future remains consistent with the actual physical rollout.

The paper proposes Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that jointly reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions to estimate whether the remaining action rollout can still be trusted.

FFDC enables adaptive action chunk sizes as an emergent consequence of prediction-observation consistency, preserving the efficiency of long-horizon execution while restoring responsiveness in contact-rich or difficult phases.

Experiments on the RoboTwin benchmark and in the real world demonstrate that the method reduces WAM forward passes by 69.10% and execution time by 34.02%, while improving success rate by 2.54% over the short-chunk baseline; in real-world experiments, it improves success rate by 35%.

The paper was recently published on arXiv (May 7, 2026) and is authored by Rui Wang and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "219c8198-bc03-4fb3-8234-e9559436679d",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "fd4955c8-a3a9-43af-aa02-3d4fd6c38338",
  "sourceToolAssistantUUID": "219c8198-bc03-4fb3-8234-e9559436679d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T18:37:29.822Z_

<details><summary>↩ Tool result · `toolu_0121w4BnPaAPEof7JDSomDe9`</summary>

```text
Web search results for query: "SpectralCache CVPR 2026 diffusion"

Links: [{"title":"GitHub - jiwoogit/SeaCache: [CVPR 2026] SeaCache: Spectral-Evolution-Aware Cache for Accelerating Diffusion Models · GitHub","url":"https://github.com/jiwoogit/SeaCache"},{"title":"GitHub - hanjq17/Spectrum: [CVPR 2026] Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration · GitHub","url":"https://github.com/hanjq17/Spectrum"},{"title":"CVPR Poster SpeeDiff: Scalable Pixel-Anchored End-to-End Latent Diffusion Model","url":"https://cvpr.thecvf.com/virtual/2026/poster/40237"},{"title":"CVPR Poster WeatherDiffusion: Controllable Weather Editing in Intrinsic Space","url":"https://cvpr.thecvf.com/virtual/2026/poster/37773"},{"title":"CVPR Poster Masked-Diffusion Autoencoders for 3D Medical Vision Representation Learning","url":"https://cvpr.thecvf.com/virtual/2026/poster/39592"},{"title":"CVPR Poster ARCache: Mitigating Error Accumulation for Caching-based Acceleration in Autoregressive Video Diffusion Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38193"},{"title":"Envisioning the Future, One Step at a Time","url":"https://compvis.github.io/myriad/"},{"title":"GitHub - Paper2Chinese/CVPR-2026-reading-papers-with-code · GitHub","url":"https://github.com/Paper2Chinese/CVPR-2026-reading-papers-with-code"},{"title":"Publications | Yulun Zhang","url":"https://yulunzhang.com/publications/"},{"title":"CVPR 2026 Accepted Papers: Trends, Big Tech Bets & Top Highlights","url":"https://www.bohrium.com/en/blog/research-notes/cvpr-2026-accepted-papers-highlights/"}]

Based on the search results, I found information about spectral-based diffusion acceleration methods accepted at CVPR 2026, though the results show two related papers rather than one specifically titled "SpectralCache":

1. **SeaCache**: SeaCache is a training-free diffusion cache schedule that bases reuse decisions on spectrally aligned representations. By modeling spectral evolution along the denoising trajectory, it derives a Spectral-Evolution-Aware (SEA) filter that preserves content-relevant components while suppressing noise components. The paper, code, and project page were released on February 21, 2026.

2. **Spectrum**: Spectrum is a training-free spectral diffusion feature forecaster that enables global, long-range feature reuse with tightly controlled error. It views the latent features of the denoiser as functions over time and approximates them with Chebyshev polynomials. Specifically, it fits the coefficient for each basis via ridge regression, which is then leveraged to forecast features at multiple future diffusion steps.

Both papers focus on accelerating diffusion models through spectral analysis and represent the growing trend of diffusion-based optimization research at CVPR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf3c6956-102e-4da0-85f8-c28f4dd4b750",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "e2b48355-fadf-4847-b999-c3357d7a276c",
  "sourceToolAssistantUUID": "bf3c6956-102e-4da0-85f8-c28f4dd4b750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T18:37:30.150Z_

<details><summary>↩ Tool result · `toolu_01TmVHD6aid71SXtJhCsQiRC`</summary>

```text
Web search results for query: "cross-modal disagreement detection diffusion denoising quality oracle"

Links: [{"title":"Consistent and Invariant Generalization Learning for Short-video","url":"https://arxiv.org/pdf/2507.04061"},{"title":"Adaptive Latent Interaction Reasoning for Multimodal ...","url":"https://www.preprints.org/frontend/manuscript/d48afc20056b3399d571ec0d7f238a9f/download_pub"},{"title":"Learning Multi-Modal Diffusion Models for Joint Audio and ...","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Ruan_MM-Diffusion_Learning_Multi-Modal_Diffusion_Models_for_Joint_Audio_and_Video_CVPR_2023_paper.pdf"},{"title":"Clash: A Benchmark for Cross-Modal Contradiction Detection","url":"https://arxiv.org/html/2511.19199v1"},{"title":"DDFD: Diffusion-Based Denoising Fusion for Object Detection in Infrared-Visible Images | Proceedings of the 33rd ACM International Conference on Multimedia","url":"https://dl.acm.org/doi/10.1145/3746027.3755183"},{"title":"A Survey of Multimodal Controllable Diffusion Models","url":"https://jcst.ict.ac.cn/fileup/1000-9000/PDF/JCST-2024-3-2-3814-509.pdf"},{"title":"DiffDis: Empowering Generative Diffusion Model with Cross-Modal","url":"https://openaccess.thecvf.com/content/ICCV2023/papers/Huang_DiffDis_Empowering_Generative_Diffusion_Model_with_Cross-Modal_Discrimination_Capability_ICCV_2023_paper.pdf"},{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf"},{"title":"[2511.19199] CLASH: A Benchmark for Cross-Modal Contradiction Detection","url":"https://arxiv.org/abs/2511.19199"},{"title":"GitHub - 52CV/CVPR-2024-Papers · GitHub","url":"https://github.com/52CV/CVPR-2024-Papers"}]

Based on the web search results, here are the relevant findings related to your search query:

## Cross-Modal Detection and Diffusion Models

The search results reveal several related research areas:

### Cross-Modal Contradiction Detection

Contradictory multimodal inputs are common in real-world settings, and the CLASH benchmark addresses cross-modal contradiction detection with COCO images paired with contradictory captions containing controlled object-level or attribute-level contradictions. Analysis of state-of-the-art models reveals substantial limitations in recognizing cross-modal conflicts, exposing systematic modality biases and category-specific weaknesses.

### Diffusion-Based Denoising for Multi-Modal Fusion

DDFD (diffusion-based denoising fusion for object detection) treats image fusion as a diffusion-based denoising process to generate fused images that are informative yet non-redundant.

### Cross-Modal Discrimination in Diffusion Models

DiffDis joints discriminative and generative tasks under the diffusion processing framework for cross-modal understanding, combining both image-text generation and alignment learning.

The search results indicate that current research in this area focuses on detecting disagreements/contradictions between modalities, using denoising diffusion models for fusion, and improving cross-modal interaction. However, I did not find a specific paper matching all elements of your search query phrase exactly as stated, so you may want to refine your search for more targeted results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f54c4b6-8622-42db-a87b-75c3bc6b9faf",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "6faac39f-40c5-4c0e-bde6-af60a3a4c626",
  "sourceToolAssistantUUID": "1f54c4b6-8622-42db-a87b-75c3bc6b9faf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T18:37:43.043Z_

<details><summary>↩ Tool result · `toolu_01WcoMHGoyn9xFPUmZb68V3n`</summary>

```text
Web search results for query: "AdaCorrection adaptive cache correction diffusion"

Links: [{"title":"AdaCorrection: Adaptive Offset Cache Correction for Accurate Diffusion Transformers","url":"https://arxiv.org/html/2602.13357"},{"title":"[2602.13357] AdaCorrection: Adaptive Offset Cache Correction for Accurate Diffusion Transformers","url":"https://arxiv.org/abs/2602.13357"},{"title":"Learning-to-Cache: Accelerating Diffusion Transformer via Layer Caching | Request PDF","url":"https://www.researchgate.net/publication/397212934_Learning-to-Cache_Accelerating_Diffusion_Transformer_via_Layer_Caching"},{"title":"Adaptive Caching for Faster Video Generation with Diffusion Transformers","url":"https://adacache-dit.github.io/"},{"title":"Paper page - SeaCache: Spectral-Evolution-Aware Cache for Accelerating Diffusion Models","url":"https://huggingface.co/papers/2602.18993"},{"title":"Paper page - DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers","url":"https://huggingface.co/papers/2602.16968"},{"title":"Adaptive Caching for Faster Video Generation with Diffusion Transformers","url":"https://arxiv.org/html/2411.02397v1"},{"title":"Adaptive Caching for Faster Video Generation with Diffusion Transformers | OpenReview","url":"https://openreview.net/forum?id=DyyLUUVXJ5"},{"title":"[2411.02397] Adaptive Caching for Faster Video Generation with Diffusion Transformers","url":"https://arxiv.org/abs/2411.02397"},{"title":"Adaptive Caching for Faster Video Generation with Diffusion Transformers · HF Daily Paper Reviews by AI","url":"https://deep-diver.github.io/ai-paper-reviewer/paper-reviews/2411.02397/"}]

Based on the search results, here's what I found about AdaCorrection:

## AdaCorrection Overview

AdaCorrection is an adaptive offset cache correction framework that maintains high generation fidelity while enabling efficient cache reuse across Transformer layers during diffusion inference.

## Problem It Addresses

Prior methods accelerate sampling by caching intermediate features, but they rely on static reuse schedules or coarse-grained heuristics, which often lead to temporal drift and cache misalignment that significantly degrade generation quality.

## How It Works

AdaCorrection is a lightweight and training-free module that introduces adaptive offset correction for cached activations in Diffusion Transformers. Unlike static reuse strategies, AdaCorrection evaluates cache validity per layer using spatio-temporal misalignment signals and adaptively blends cached and fresh activations to restore alignment.

The Offset Estimation Module (OEM) quantifies misalignment via spatio–temporal deviation statistics, producing an offset score per layer and step. The Adaptive Correction Module (ACM) maps the score to a correction weight that governs interpolation between cached and fresh computations.

## Key Benefits

The design integrates seamlessly with existing diffusion pipelines and does not require model retraining or architecture modification. The approach achieves strong generation quality with minimal computational overhead, maintaining near-original FID while providing moderate acceleration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcdc05d2-237b-46a6-9bef-b0001a7e0cfe",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "6545a19c-b050-4940-9498-a2cf40c870c7",
  "sourceToolAssistantUUID": "fcdc05d2-237b-46a6-9bef-b0001a7e0cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T18:37:46.485Z_

Let me do a few more targeted searches to fill in remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6545a19c-b050-4940-9498-a2cf40c870c7",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNdnHU5CAcNUMfFLYTY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fb5ba14-e6f5-484e-86d5-6d3e095f1834",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tj6dcoVT6WpyLqDFL7VhLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1017,
      "cache_creation_input_tokens": 3505,
      "cache_read_input_tokens": 17328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3505,
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

_source line 34 · 2026-05-10T18:37:47.441Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FNLNYcvjDEaKmHe7psXDC4`</summary>

```json
{
  "query": "FFDC-WAM arxiv 2605.06222 cross-modal verification action video prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fb5ba14-e6f5-484e-86d5-6d3e095f1834",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNdnHU5CAcNUMfFLYTY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f10949bb-1a5a-47e7-b99e-ef6ff845ed9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tj6dcoVT6WpyLqDFL7VhLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1017,
      "cache_creation_input_tokens": 3505,
      "cache_read_input_tokens": 17328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3505,
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

_source line 35 · 2026-05-10T18:37:48.433Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012dGyRfsBAVvat897wRGHb4`</summary>

```json
{
  "query": "\"world action model\" adaptive inference quality self-correcting denoising 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f10949bb-1a5a-47e7-b99e-ef6ff845ed9d",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNdnHU5CAcNUMfFLYTY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c39da74-6759-411a-b903-7f8f537efd0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tj6dcoVT6WpyLqDFL7VhLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1017,
      "cache_creation_input_tokens": 3505,
      "cache_read_input_tokens": 17328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3505,
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

_source line 36 · 2026-05-10T18:37:49.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YMyWxcEV7CKpay6hZABdQ7`</summary>

```json
{
  "query": "D3P dynamic denoising diffusion policy adaptive steps reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c39da74-6759-411a-b903-7f8f537efd0f",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNdnHU5CAcNUMfFLYTY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ea8eb21-e5fa-463c-b200-639747c26b24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tj6dcoVT6WpyLqDFL7VhLJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1017,
      "cache_creation_input_tokens": 3505,
      "cache_read_input_tokens": 17328,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3505
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1017,
          "output_tokens": 192,
          "cache_read_input_tokens": 17328,
          "cache_creation_input_tokens": 3505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3505,
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

_source line 37 · 2026-05-10T18:37:57.416Z_

<details><summary>↩ Tool result · `toolu_012dGyRfsBAVvat897wRGHb4`</summary>

```text
Web search results for query: ""world action model" adaptive inference quality self-correcting denoising 2025 2026"

Links: [{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"𝐴₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/html/2604.05672"},{"title":"AdaWorld: Learning Adaptable World Models with Latent Actions","url":"https://arxiv.org/html/2503.18938v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"A Comprehensive Survey on World Models for Embodied AI","url":"https://arxiv.org/html/2510.16732v1"},{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"}]

I found several highly relevant research papers on world action models from 2025-2026. Here are the key findings:

## Recent World Action Model Research

**X-WAM (Unified 4D World Model)**

X-WAM is a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis (video + 3D reconstruction) in a single framework, addressing limitations of prior models that fail to balance action efficiency and world modeling quality. The model proposes Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency, which applies a specialized asynchronous denoising schedule during inference.

**DreamZero: World Action Models as Zero-shot Policies**

During inference, DreamZero jointly denoises video and action chunks, leveraging KV caching for efficiency. The model implements a caching mechanism that exploits temporal redundancy by tracking cosine similarity between successive velocity predictions, bypassing forward passes when similarity exceeds a threshold, reducing average DiT steps from 16 to 4 with minimal degradation to video and action fidelity.

**MotuBrain: Advanced World Action Model**

MotuBrain develops a systems-oriented inference stack including denoising-step reduction, compilation with CUDA-graph-friendly execution, FP8 quantization, and DiT caching, which together deliver more than 50× end-to-end speedup.

**A₁: Adaptive Inference Model**

A₁ is equipped with a budget-aware adaptive inference mechanism that computes actions at intermediate VLM layers and performs an action-consistency test to decide early termination, achieving substantial end-to-end latency reduction through Inter-Layer Truncated Flow Matching with warm-start denoising.

These papers represent the latest advances in adaptive inference, quality optimization, and self-correcting denoising for world action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c39da74-6759-411a-b903-7f8f537efd0f",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "d2e3e7c0-8ac3-47fc-9ae4-4c20788db2f9",
  "sourceToolAssistantUUID": "0c39da74-6759-411a-b903-7f8f537efd0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T18:37:57.949Z_

<details><summary>↩ Tool result · `toolu_01YMyWxcEV7CKpay6hZABdQ7`</summary>

```text
Web search results for query: "D3P dynamic denoising diffusion policy adaptive steps reinforcement learning"

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"[2508.06804] D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/abs/2508.06804"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2508.06804v1"},{"title":"D3P: Dynamic Denoising Difusion Policy via Reinforcement Learning Shu’ang Yu","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"(PDF) D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://www.researchgate.net/publication/394438722_D3P_Dynamic_Denoising_Diffusion_Policy_via_Reinforcement_Learning"},{"title":"Denoising Diffusion Policy Optimization","url":"https://www.emergentmind.com/topics/denoising-diffusion-policy-optimization-ddpo"},{"title":"Diffusion Policy Framework","url":"https://www.emergentmind.com/topics/diffusion-policy-dp"},{"title":"TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration","url":"https://arxiv.org/html/2512.15773"},{"title":"[2305.13301] Training Diffusion Models with Reinforcement Learning","url":"https://arxiv.org/abs/2305.13301"},{"title":"3D Diffusion Policy (DP3)","url":"https://www.emergentmind.com/topics/3d-diffusion-policy-dp3"}]

I found comprehensive information about D3P (Dynamic Denoising Diffusion Policy). Here's a summary of the research:

## Overview

D3P is a diffusion-based policy that adaptively allocates denoising steps across actions at test time. Diffusion policies excel at learning complex action distributions for robotic visuomotor tasks, yet their iterative denoising process poses a major bottleneck for real-time deployment. Existing acceleration methods apply a fixed number of denoising steps per action, implicitly treating all actions as equally important. However, experiments reveal that robotic tasks often contain a mix of crucial and routine actions, which differ in their impact on task success.

## Architecture and Method

D3P uses a lightweight, state-aware adaptor to allocate the optimal number of denoising steps for each action. The method is mathematically formulated as a two-layer partially observable Markov decision process (POMDP), then reinforcement learning is used to jointly train both the base diffusion policy and the adaptor. The lightweight adaptor is trained from scratch with PPO, where its reward function incentivizes minimizing denoising steps without compromising performance.

## Key Insight

Task executions typically consist of pivotal crucial actions that largely determine success, and more forgiving routine actions with only a marginal impact. For instance, in a Transport task, the precise moment of object handover is crucial, whereas the arm movements before and after have less impact on task success. This motivates allocating denoising steps adaptively: spend more computation on crucial actions, and less on routine ones—to balance precision and efficiency.

## Performance Results

D3P dynamically adapts its denoising effort, using more denoising steps only when necessary. This allows D3P to match or even exceed the peak performance of the 10-step DPPO policy while achieving an average inference speed-up of 2.2 times. On a physical robot, D3P achieves a 1.9× acceleration over the baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ea8eb21-e5fa-463c-b200-639747c26b24",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "0345dbe9-f2a4-4589-bc3e-b347e0b3203c",
  "sourceToolAssistantUUID": "9ea8eb21-e5fa-463c-b200-639747c26b24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T18:38:01.152Z_

<details><summary>↩ Tool result · `toolu_01FNLNYcvjDEaKmHe7psXDC4`</summary>

```text
Web search results for query: "FFDC-WAM arxiv 2605.06222 cross-modal verification action video prediction"

Links: [{"title":"[2605.06222] When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/abs/2605.06222"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"Evolving from Single-modal to Multi-modal Facial Deepfake Detection: A Survey","url":"https://arxiv.org/html/2406.06965v1"},{"title":"[2605.05511] Non-Myopic Active Feature Acquisition via Pathwise Policy Gradients","url":"https://arxiv.org/abs/2605.05511"},{"title":"A Survey of Unified Multimodal Understanding and Generation","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/290060/preprint_pdf/6da27c93134f892297c4365ec17ce686.pdf"},{"title":"GitHub - 52CV/CVPR-2024-Papers · GitHub","url":"https://github.com/52CV/CVPR-2024-Papers"},{"title":"GitHub - 52CV/CVPR-2023-Papers · GitHub","url":"https://github.com/52CV/CVPR-2023-Papers"},{"title":"Multimodal Learning on Low-Quality Data with Conformal Predictive Self-Calibration","url":"https://arxiv.org/html/2605.03820"}]

Based on the search results, I found the paper you're looking for:

The arxiv paper 2605.06222 is titled "When to Trust Imagination: Adaptive Action Execution for World Action Models".

Here's what the paper is about:

World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation by jointly predicting future visual observations and future actions. The paper formulates adaptive WAM execution as a future-reality verification problem, proposing Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that jointly reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions to estimate whether the remaining action rollout can still be trusted.

FFDC enables adaptive action chunk sizes as an emergent consequence of prediction-observation consistency, and the work introduces Mixture-of-Horizon Training to improve long-horizon trajectory coverage for adaptive execution.

Experiments on the RoboTwin benchmark and in the real world demonstrate that the method reduces WAM forward passes by 69.10% and execution time by 34.02%, while improving success rate by 2.54% over the short-chunk baseline; in real-world experiments, it improves success rate by 35%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f10949bb-1a5a-47e7-b99e-ef6ff845ed9d",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "6bcc4630-0450-43e7-9f77-b6a0925cd71d",
  "sourceToolAssistantUUID": "f10949bb-1a5a-47e7-b99e-ef6ff845ed9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-10T18:38:04.107Z_

Let me do a final batch of searches to be thorough on the specific cross-modal verification within denoising angle.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bcc4630-0450-43e7-9f77-b6a0925cd71d",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNf7h4A1XGh28daLWyU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb224856-e5a5-40fa-885a-db799428ecd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qmpPpHznPA94WdeJFfyu3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1931,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 20833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2012,
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

_source line 41 · 2026-05-10T18:38:04.984Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dek53fnKsUBzMCVT2H2ZQf`</summary>

```json
{
  "query": "FFDC \"future forward dynamics causal attention\" verifier WAM prediction observation consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb224856-e5a5-40fa-885a-db799428ecd9",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNf7h4A1XGh28daLWyU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a1db3b8-6bcf-47fd-aec4-ab5502ec8d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qmpPpHznPA94WdeJFfyu3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1931,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 20833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2012,
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

_source line 42 · 2026-05-10T18:38:05.984Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ub2GZvNEX4Z7b9GKUNtP95`</summary>

```json
{
  "query": "Fast-WAM \"test-time future imagination\" world action model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a1db3b8-6bcf-47fd-aec4-ab5502ec8d6f",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNf7h4A1XGh28daLWyU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2378d22-b9ad-4ffc-b876-c844b3c830e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qmpPpHznPA94WdeJFfyu3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1931,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 20833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2012,
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

_source line 43 · 2026-05-10T18:38:07.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VyC9jxBp9tnb1sVMddo1et`</summary>

```json
{
  "query": "A1 model \"action-consistency test\" early termination truncated flow matching adaptive inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2378d22-b9ad-4ffc-b876-c844b3c830e5",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNf7h4A1XGh28daLWyU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f0d494a-6400-4604-bfb5-cba78d060c80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qmpPpHznPA94WdeJFfyu3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1931,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 20833,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2012
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1931,
          "output_tokens": 199,
          "cache_read_input_tokens": 20833,
          "cache_creation_input_tokens": 2012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2012,
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

_source line 44 · 2026-05-10T18:38:11.135Z_

<details><summary>↩ Tool result · `toolu_01Dek53fnKsUBzMCVT2H2ZQf`</summary>

```text
Web search results for query: "FFDC "future forward dynamics causal attention" verifier WAM prediction observation consistency"

Links: [{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"GitHub - colorfulfuture/Awesome-Trajectory-Motion-Prediction-Papers · GitHub","url":"https://github.com/colorfulfuture/Awesome-Trajectory-Motion-Prediction-Papers"},{"title":"Silent Expectations: Dynamic Causal Modeling of Cortical Prediction and Attention to Sounds That Weren't - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/27511005/"},{"title":"FFN-Attention Co-optimized Transformer Architecture with ...","url":"https://dl.acm.org/doi/pdf/10.1145/3579371.3589057"},{"title":"WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference","url":"https://wedlm.github.io/"},{"title":"Analyzing Feed-Forward Blocks in Transformers through the Lens of Attention Maps","url":"https://arxiv.org/html/2302.00456"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Frequency-Dynamic Attention Modulation for Dense Prediction Linwei Chen1","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Frequency-Dynamic_Attention_Modulation_For_Dense_Prediction_ICCV_2025_paper.pdf"},{"title":"FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision","url":"https://tridao.me/publications/flash3/flash3.pdf"},{"title":"Frequency-Dynamic Attention Modulation for Dense Prediction","url":"https://arxiv.org/html/2507.12006v1"}]

Based on the search results, I found highly relevant information about FFDC and its relationship to WAM prediction and observation consistency.

FFDC (Future Forward Dynamics Causal Attention) is a lightweight verifier that jointly reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions to estimate whether the remaining action rollout can still be trusted.

The framework formulates adaptive WAM (World Action Model) execution as a future–reality verification problem, where the WAM's predicted visual future is used to assess whether its remaining action rollout can still be trusted, with the robot comparing WAM-predicted visual dynamics with real observations during execution to decide whether the remaining action sequence can still be trusted.

The effective action chunk size expands when prediction and reality remain consistent and shrinks when they diverge.

In difficult phases, FFDC detects when the imagined future becomes unreliable and triggers replanning, improving robustness. The lightweight verifier performs high-frequency verification through a causal attention mechanism over visual and action modalities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a1db3b8-6bcf-47fd-aec4-ab5502ec8d6f",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "f2d90fb1-e36d-458f-880c-90831d3bcc1e",
  "sourceToolAssistantUUID": "8a1db3b8-6bcf-47fd-aec4-ab5502ec8d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T18:38:14.969Z_

<details><summary>↩ Tool result · `toolu_01Ub2GZvNEX4Z7b9GKUNtP95`</summary>

```text
Web search results for query: "Fast-WAM "test-time future imagination" world action model 2026"

Links: [{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination? | alphaXiv","url":"https://www.alphaxiv.org/resources/2603.16666v1"},{"title":"Fast-WAM: Rethinking Test-Time Imagination","url":"https://www.emergentmind.com/papers/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination? (Mar 2026) - YouTube","url":"https://www.youtube.com/watch?v=Andhx2GX5eA"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"}]

I found comprehensive information about Fast-WAM. Here's what the research shows:

## Overview

World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action. Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising, yet it remains unclear whether explicit future imagination is actually necessary for strong action performance.

## Fast-WAM Architecture

Fast-WAM is a WAM architecture that retains video co-training during training but skips future prediction at test time. Fast-WAM keeps video co-training during training but removes explicit future generation at inference time, enabling direct action generation from latent world representations in a single forward pass.

## Key Findings

Fast-WAM remains competitive with imagine-then-execute variants, while removing video co-training causes a much larger performance drop. The main value of video prediction in WAMs may lie in improving world representations during training rather than generating future observations at test time.

## Performance

Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin) and real-world tasks, without embodied pretraining. It runs in real time with 190ms latency, over 4× faster than existing imagine-then-execute WAMs.

The paper was published in March 2026 by authors Tianyuan Yuan, Zibin Dong, Yicheng Liu, and Hang Zhao.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2378d22-b9ad-4ffc-b876-c844b3c830e5",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "b09c89a7-4f7a-4548-84e5-77c98e7ea3e3",
  "sourceToolAssistantUUID": "e2378d22-b9ad-4ffc-b876-c844b3c830e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T18:38:15.686Z_

<details><summary>↩ Tool result · `toolu_01VyC9jxBp9tnb1sVMddo1et`</summary>

```text
Web search results for query: "A1 model "action-consistency test" early termination truncated flow matching adaptive inference"

Links: [{"title":"𝐴₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/html/2604.05672"},{"title":"Knowledge Insulating Vision-Language-Action Models","url":"https://www.pi.website/download/pi05_KI.pdf"},{"title":"Ambiguity-aware Truncated Flow Matching for Ambiguous Medical Image Segmentation","url":"https://arxiv.org/html/2511.06857"},{"title":"Adaptive Time Step Flow Matching for Autonomous Driving Motion Planning","url":"https://arxiv.org/html/2602.10285"},{"title":"FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation","url":"https://arxiv.org/html/2412.04987v2"},{"title":"F1: A Vision-Language-Action Model Bridging ...","url":"https://arxiv.org/pdf/2509.06951"},{"title":"Consistency Flow Matching: Defining Straight Flows with Velocity Consistency","url":"https://arxiv.org/html/2407.02398v1"},{"title":"On the Closed-Form of Flow Matching: Generalization","url":"https://openreview.net/pdf/891239399aeb4629291513a63696bb354288ee3c.pdf"},{"title":"Published as a conference paper at ICLR 2025 CONSISTENCY MODELS MADE EASY","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/bb166dd4de5dba363bf1023eb956a826-Paper-Conference.pdf"},{"title":"An introduction to Flow Matching · Cambridge MLG Blog","url":"https://mlg.eng.cam.ac.uk/blog/2024/01/20/flow-matching.html"}]

Based on the search results, here's what I found about the A1 model and the techniques you mentioned:

## A1 Model Overview

The A1 model targets the full inference pipeline by introducing a budget-aware adaptive inference scheme that jointly accelerates the backbone and the action head.

## Action-Consistency Test & Early Termination

The A1 model monitors action consistency across intermediate VLM layers to trigger early termination, and proposes Inter-Layer Truncated Flow Matching that warm-starts denoising across layers, enabling accurate actions with substantially fewer effective denoising iterations.

## Key Performance Results

Across simulation benchmarks (LIBERO, VLABench) and real robots (Franka, AgiBot), A1 achieves state-of-the-art success rates while significantly reducing inference cost (e.g., up to 72% lower per-episode latency for flow-matching inference and up to 76.6% backbone computation reduction with minor performance degradation).

## Adaptive Inference Implementation

The A1-MLP model achieves best performance with an average success rate of 96.6%, while reducing layer computation by 15.6% compared to full inference. As the exit criterion decreases to 0.7, 0.4, and 0.1, the computational reduction increases to 39.1%, 58.5%, and 76.6%, respectively, while the success rate drops by only 0.3%, 2.3% and 1.7%. Even when reducing 76.6% of the computation cost, the model still achieves a 92.3% success rate.

The research demonstrates an innovative approach to efficient robotic control by combining action consistency monitoring with truncated flow matching techniques for adaptive inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f0d494a-6400-4604-bfb5-cba78d060c80",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a731ae481ce349556",
  "type": "user",
  "uuid": "0579cced-96cc-474f-9e9c-c522a9330f7c",
  "sourceToolAssistantUUID": "1f0d494a-6400-4604-bfb5-cba78d060c80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-10T18:39:27.001Z_

Now I have comprehensive findings across all queries. Here is the consolidated report:

---

## Comprehensive Search Results

### 1. CROSS-MODAL VERIFICATION WITHIN DENOISING

**The most directly relevant paper found is FFDC-WAM (arxiv 2605.06222, May 7, 2026):**
- **"When to Trust Imagination: Adaptive Action Execution for World Action Models"** by Rui Wang et al.
- This paper proposes **Future Forward Dynamics Causal Attention (FFDC)**, a lightweight verifier that jointly reasons over *predicted future actions*, *predicted visual dynamics*, *real observations*, and *language instructions* to estimate whether the remaining action rollout can still be trusted.
- It formulates adaptive WAM execution as a **future-reality verification problem** -- the robot compares WAM-predicted visual dynamics with real observations during execution to decide whether the remaining action sequence is trustworthy.
- **However**, this operates at the *execution* level (post-denoising), not *within* the denoising loop itself. FFDC checks prediction-observation consistency after actions are generated, not during intermediate denoising steps. The cross-modal check is between the WAM's predicted video and the real observed frames, not between video and action branches mid-denoising.
- Results: Reduces WAM forward passes by 69.10%, execution time by 34.02%, improves success rate by 2.54% (simulation) and 35% (real-world).

**No paper was found that proposes cross-modal disagreement detection *within* the denoising process itself** (i.e., checking video-branch vs. action-branch intermediate latents at each denoising step as an internal quality oracle). This appears to be a gap.

### 2. ADAPTIVE STEP ALLOCATION FOR MULTI-MODAL DIFFUSION MODELS

Several relevant works exist:

- **D3P (Dynamic Denoising Diffusion Policy)** (arxiv 2508.06804): Uses a lightweight state-aware adaptor trained via RL (PPO) to allocate per-action denoising steps. Achieves 2.2x inference speedup. This is for single-modal (action-only) diffusion policies, not joint video-action models.

- **ADPro** (arxiv 2508.06266): Test-time adaptive diffusion policy using manifold-constrained denoising and task-aware initialization.

- **AdaDiff** (arxiv 2311.14768, AAAI): Per-sample adaptive step selection for image diffusion models. Learns instance-specific step policies. Achieves 33-40% inference time reduction.

- **A1 Model** (arxiv 2604.05672): Uses **action-consistency tests across intermediate VLM layers** to trigger early termination, combined with Inter-Layer Truncated Flow Matching that warm-starts denoising across layers. Achieves up to 72% lower per-episode latency for flow-matching inference. This is the closest to adaptive step allocation in a multi-modal setting, though it operates at the VLM backbone level rather than within a joint video-action diffusion process.

- **X-WAM** (arxiv 2604.26694): Proposes **Asynchronous Noise Sampling (ANS)** to jointly optimize generation quality and action decoding efficiency in a unified 4D world model with asynchronous denoising schedules for different modalities.

### 3. QUALITY-FLOOR GUARANTEES FOR DIFFUSION INFERENCE

- **Optimal Stopping in Latent Diffusion Models** (arxiv 2510.08409): Provides theoretical framework for optimal stopping time that minimizes distance between generated and true data distributions. Lower-dimensional representations benefit from earlier termination; higher-dimensional latent spaces require later stopping.

- **EDIT** (arxiv 2512.00670): Early Diffusion Inference Termination for diffusion LLMs based on dynamics of training gradients. Achieves 11.8-68.3% fewer steps while maintaining/improving accuracy.

- **AdaDiff's UEM** (ECCV 2024): Timestep-aware uncertainty estimation module integrated at each intermediate layer to evaluate predictive uncertainty as an indicator for early termination.

No paper was found that provides formal *quality-floor guarantees* (e.g., "output quality will not drop below threshold X") for diffusion inference in the robotics/WAM setting specifically.

### 4. SELF-CORRECTING DIFFUSION INFERENCE

- **ProSeCo (Progressive Self-Correction)** (arxiv 2602.11590): For masked diffusion models -- applies corrective refinement steps between unmasking steps to change decoded tokens and improve outputs. Achieves 2-3x faster sampling and ~1.3x quality improvement.

- **SCDD (Self-Correcting Discrete Diffusion)** (arxiv 2603.02230): Reformulates pretrained self-correction with explicit state transitions in discrete time.

- **SLD (Self-correcting LLM-controlled Diffusion)** (CVPR 2024): LLM-driven feedback loop that iteratively corrects diffusion latent outputs based on prompt requirements. Operates post-generation, not within denoising.

- **BackPlay** (arxiv 2601.06428): Plug-in look-back self-correction for diffusion models.

All of these operate on text-to-image or discrete token domains. **None proposes self-correction within a joint video-action diffusion denoising process for WAMs.**

### 5. MOTUBRAIN CACHING MECHANISM (VERIFIED)

- **MotuBrain** (arxiv 2604.27792) by ShengShu Technology: Caches video-text branch keys/values after one forward pass; subsequent denoising steps update only action tokens, attending to cached video/text KV. Combined with denoising-step reduction, CUDA graph compilation, FP8 quantization, this delivers **50x+ end-to-end speedup** and **11 Hz inference frequency**.

### 6. SPECTRALCACHE / SPECTRAL DIFFUSION CACHING (CVPR 2026)

No paper specifically named "SpectralCache" was found. However, two closely related CVPR 2026 papers exist:

- **SeaCache (Spectral-Evolution-Aware Cache)** -- training-free cache schedule using spectrally aligned representations. Models spectral evolution along the denoising trajectory with a SEA filter. Released Feb 21, 2026.

- **Spectrum** -- training-free spectral diffusion feature forecaster using Chebyshev polynomial approximation for long-range feature reuse.

- **ARCache** (CVPR 2026 poster): Mitigates error accumulation for caching-based acceleration in autoregressive video diffusion models.

### 7. ADACORRECTION (VERIFIED)

- **AdaCorrection** (arxiv 2602.13357): Adaptive Offset Cache Correction for Diffusion Transformers. Training-free module that evaluates cache validity per layer using spatio-temporal misalignment signals and adaptively blends cached and fresh activations. Includes an Offset Estimation Module (OEM) and Adaptive Correction Module (ACM).

### 8. FAST-WAM

- **Fast-WAM** (arxiv 2603.16666, March 2026): Argues that the main value of video prediction in WAMs lies in improving world representations during *training*, not at test time. Skips future video generation at inference, achieving 190ms latency (4x+ faster) while remaining competitive.

### 9. DREAMZERO CACHING

- **DreamZero**: Implements a similarity-based caching mechanism that tracks cosine similarity between successive velocity predictions, bypassing forward passes when similarity exceeds a threshold. Reduces average DiT steps from 16 to 4.

---

## Key Finding: Gap Analysis

**The specific idea of using cross-modal disagreement *within the denoising loop* (i.e., monitoring video-branch vs. action-branch intermediate representations at each denoising step as an internal quality oracle for WAMs) does not appear to have been proposed.** Here is what exists nearby:

| Concept | Closest Work | Key Difference |
|---|---|---|
| Cross-modal verification for WAMs | FFDC-WAM (May 2026) | Operates post-denoising at execution time, not within the denoising loop |
| Adaptive denoising steps | D3P, A1 | Single-modal or VLM-level, not joint video-action diffusion |
| Self-correcting diffusion | ProSeCo, SCDD | For discrete/masked diffusion in NLP, not multi-modal WAMs |
| Quality oracle within denoising | AdaDiff UEM, AdaCorrection | Per-layer uncertainty or cache validity, not cross-modal consistency |
| Asynchronous multi-modal denoising | X-WAM ANS | Separate schedules per modality, but no cross-modal quality check |

The idea of using video-action branch disagreement *mid-denoising* as a quality oracle that triggers extended steps or rollback appears to be novel. FFDC-WAM is the closest conceptually (cross-modal verification for WAMs) but operates at a fundamentally different level (execution-time, post-inference, comparing predictions vs. reality rather than comparing two model branches mid-generation).

Sources:
- [FFDC-WAM: When to Trust Imagination](https://arxiv.org/abs/2605.06222)
- [D3P: Dynamic Denoising Diffusion Policy](https://arxiv.org/abs/2508.06804)
- [ADPro: Test-time Adaptive Diffusion Policy](https://arxiv.org/abs/2508.06266)
- [AdaDiff: Adaptive Step Selection](https://arxiv.org/abs/2311.14768)
- [MotuBrain: Advanced World Action Model](https://arxiv.org/html/2604.27792v2)
- [SeaCache: Spectral-Evolution-Aware Cache (CVPR 2026)](https://github.com/jiwoogit/SeaCache)
- [Spectrum: Adaptive Spectral Feature Forecasting (CVPR 2026)](https://github.com/hanjq17/Spectrum)
- [ARCache (CVPR 2026)](https://cvpr.thecvf.com/virtual/2026/poster/38193)
- [AdaCorrection](https://arxiv.org/abs/2602.13357)
- [Fast-WAM](https://arxiv.org/abs/2603.16666)
- [X-WAM: Unified 4D World Action Modeling](https://arxiv.org/html/2604.26694v2)
- [A1 Model: Adaptive Truncated VLA](https://arxiv.org/html/2604.05672)
- [ProSeCo: Self-Correcting Masked Diffusion](https://arxiv.org/abs/2602.11590)
- [SCDD: Generalized Discrete Diffusion with Self-Correction](https://arxiv.org/abs/2603.02230)
- [SLD: Self-correcting LLM-controlled Diffusion (CVPR 2024)](https://arxiv.org/abs/2311.16090)
- [Optimal Stopping in Latent Diffusion Models](https://arxiv.org/abs/2510.08409)
- [EDIT: Early Diffusion Inference Termination](https://arxiv.org/html/2512.00670v1)
- [DreamZero: World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922)
- [Diffusion Policy (RSS 2023)](https://diffusion-policy.cs.columbia.edu/)
- [Two-Steps Diffusion Policy via Genetic Denoising](https://arxiv.org/pdf/2510.21991)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0579cced-96cc-474f-9e9c-c522a9330f7c",
  "isSidechain": true,
  "agentId": "a731ae481ce349556",
  "requestId": "req_011CauNgBqsB7bS9sGcAfd1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0742c4b-04bf-431f-bf3a-f2039ddda578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkVMWDQX8UfAUUzzvVqEGz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4831,
      "cache_read_input_tokens": 22845,
      "output_tokens": 2851,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4831
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2851,
          "cache_read_input_tokens": 22845,
          "cache_creation_input_tokens": 4831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4831,
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
