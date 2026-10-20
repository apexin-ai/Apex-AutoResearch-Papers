# Research conversation: I need to do a very targeted search for any work that proposes using cross-modal disagreement or per-modality convergenc

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afc022510ad977c81.jsonl`
- **Structured JSON:** [`dba3258292d98c4bd154.json`](../../sessions/db/dba3258292d98c4bd154.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-10T20:03:00.717Z_

I need to do a very targeted search for any work that proposes using cross-modal disagreement or per-modality convergence monitoring WITHIN diffusion denoising as a quality signal. This is the core novelty claim of a proposal I'm reviewing.

Search for:
1. "per-modality convergence" diffusion denoising 2025 2026
2. "cross-modal disagreement" diffusion inference quality
3. "modality-specific convergence" diffusion adaptive steps
4. "extension mechanism" denoising diffusion steps quality guarantee
5. "self-correction" continuous diffusion multi-modal
6. "quality floor" diffusion inference robotics
7. site:arxiv.org "per-modality" "denoising" "adaptive" 2026
8. "A1 adaptive vision language action" early exit 2026

For result #8 (A1), please use WebFetch to read https://arxiv.org/abs/2604.05672 - I need to understand if A1's "action-consistency test for early termination" is similar to cross-modal disagreement-based extension.

Also search for:
9. "CycleVLA self-correcting" 2026 - to understand if CycleVLA's self-correction is related
10. "TS-DP reinforcement speculative decoding diffusion policy" - verify this paper exists

Report everything you find, especially anything that could be a direct competitor to "using cross-modal convergence disagreement within denoising to trigger extension of computation."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "a346955d-5be1-4cd0-abb8-1fa18b7b5015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T20:03:02.693Z_

I'll conduct a comprehensive search for these specific topics. Let me start with multiple parallel searches to cover all the queries efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a346955d-5be1-4cd0-abb8-1fa18b7b5015",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauV92WVFrtckHzf4gini",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea3b4f6c-b31d-4ed3-82a9-2e7c5fda7833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4ef8teFMs1PVQPEGytsH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 776,
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

_source line 3 · 2026-05-10T20:03:03.012Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015P8aZ6HU2XFAdDnYTqd1mA`</summary>

```json
{
  "query": "per-modality convergence diffusion denoising 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea3b4f6c-b31d-4ed3-82a9-2e7c5fda7833",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauV92WVFrtckHzf4gini",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6adcc7b-1a92-4da6-bf98-8d3ac62122d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4ef8teFMs1PVQPEGytsH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 776,
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

_source line 4 · 2026-05-10T20:03:03.107Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013GWwpn839McqkK6uoYSe1W`</summary>

```json
{
  "query": "cross-modal disagreement diffusion inference quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6adcc7b-1a92-4da6-bf98-8d3ac62122d3",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauV92WVFrtckHzf4gini",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3838b1b9-ae8e-442b-86b7-26b2196dcbb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4ef8teFMs1PVQPEGytsH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 776,
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

_source line 5 · 2026-05-10T20:03:03.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F1YwntZHnfm3DAupMsH59p`</summary>

```json
{
  "query": "modality-specific convergence diffusion adaptive steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3838b1b9-ae8e-442b-86b7-26b2196dcbb7",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauV92WVFrtckHzf4gini",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ec651baa-8837-4c22-bc1f-b3a2bcd9a2aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4ef8teFMs1PVQPEGytsH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 776,
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

_source line 6 · 2026-05-10T20:03:03.392Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YD3mCobKDNP2ansioGL9kC`</summary>

```json
{
  "query": "extension mechanism denoising diffusion steps quality guarantee"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec651baa-8837-4c22-bc1f-b3a2bcd9a2aa",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauV92WVFrtckHzf4gini",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a2564102-36be-4255-aca7-7160108c80bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4ef8teFMs1PVQPEGytsH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 776,
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

_source line 7 · 2026-05-10T20:03:03.571Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXojwfARigsbxTyYPn5Mct`</summary>

```json
{
  "query": "self-correction continuous diffusion multi-modal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2564102-36be-4255-aca7-7160108c80bf",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauV92WVFrtckHzf4gini",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b68a17e7-e84f-41f9-a699-d2f122488ca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4ef8teFMs1PVQPEGytsH9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 16153,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 776,
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

_source line 8 · 2026-05-10T20:03:03.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AzDeRxgNsa1ZUoQCENX56i`</summary>

```json
{
  "query": "quality floor diffusion inference robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b68a17e7-e84f-41f9-a699-d2f122488ca3",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauV92WVFrtckHzf4gini",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "44ae0d5b-7034-4d9b-8c34-96fb8b6a4a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4ef8teFMs1PVQPEGytsH9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 16153,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 776,
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

_source line 9 · 2026-05-10T20:03:10.171Z_

<details><summary>↩ Tool result · `toolu_013GWwpn839McqkK6uoYSe1W`</summary>

```text
Web search results for query: "cross-modal disagreement diffusion inference quality"

Links: [{"title":"DiffDis: Empowering Generative Diffusion Model with Cross-Modal","url":"https://openaccess.thecvf.com/content/ICCV2023/papers/Huang_DiffDis_Empowering_Generative_Diffusion_Model_with_Cross-Modal_Discrimination_Capability_ICCV_2023_paper.pdf"},{"title":"Diffexplainer: Towards Cross-modal Global Explanations with Diffusion Models","url":"https://arxiv.org/html/2404.02618v1"},{"title":"Contrastive Diffusion for Cross-Modal and Conditional Generation","url":"https://l-yezhu.github.io/CDCD/"},{"title":"Theoretical Framework, Technical Evolution, and Future Prospects of Cross-Modal Mapping and Controllable Image Generation Under Multi-Source Heterogeneous Collaboration","url":"https://www.mdpi.com/1424-8220/26/10/2972"},{"title":"Cross-Attention Makes Inference Cumbersome in Text-to-Image Diffusion Models","url":"https://arxiv.org/html/2404.02747v1"},{"title":"Towards Safe Concept Transfer of Multi-Modal Diffusion via ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/1741917e3df34daa1a4c564e2980bb59-Paper-Conference.pdf"},{"title":"Discrete Contrastive Diffusion for Cross-Modal and Conditional Generation | DeepAI","url":"https://deepai.org/publication/discrete-contrastive-diffusion-for-cross-modal-and-conditional-generation"},{"title":"Graph-Oriented Cross-Modality Diffusion for Multimedia Recommendation | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-981-95-3453-1_17"},{"title":"Unified Multimodal Understanding and Generation Models","url":"https://arxiv.org/pdf/2505.02567"},{"title":"DiffExplainer: Towards cross-modal global explanations with diffusion models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1077314225002826"}]

Based on the search results, here are several research works related to cross-modal diffusion and inference quality:

## Key Research Areas

**1. Cross-Modal Discrimination and Generation**

DiffDis is a framework that joints discriminative and generative tasks under the diffusion processing, combining both image generation and image-text discrimination capabilities. DiffDis outperforms CLIP-ViT-L/14 in R@1 of image-to-text retrieval and text-to-image retrieval by 11.6% and 8.2%, respectively, on the MSCOCO dataset.

**2. Cross-Modal Explainability**

DiffExplainer is a novel framework that leverages language-vision models to enable multimodal global explainability by employing diffusion models conditioned on optimized text prompts, synthesizing images that maximize class outputs and hidden features of a classifier.

**3. Contrastive Diffusion for Cross-Modal Synthesis**

The Conditional Discrete Contrastive Diffusion (CDCD) loss uses two contrastive diffusion mechanisms to effectively incorporate contrastive learning into the denoising process. This approach improves the convergence of diffusion models, reducing the number of required diffusion steps by more than 35% inference speed.

**4. Cross-Attention and Inference Efficiency**

Cross-attention outputs converge to a fixed point after few inference steps, with the convergence point dividing the inference process into two stages: an initial semantics-planning stage and a subsequent fidelity-improving stage.

These research directions address various aspects of improving inference quality, efficiency, and cross-modal alignment in diffusion models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3838b1b9-ae8e-442b-86b7-26b2196dcbb7",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "b57a25d6-0b83-4bae-b113-e87da10320d7",
  "sourceToolAssistantUUID": "3838b1b9-ae8e-442b-86b7-26b2196dcbb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T20:03:10.309Z_

<details><summary>↩ Tool result · `toolu_01AzDeRxgNsa1ZUoQCENX56i`</summary>

```text
Web search results for query: "quality floor diffusion inference robotics"

Links: [{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"Diffusion Transformer (DiT) — Architecture for Video & Robot Control | Claru","url":"https://claru.ai/glossary/diffusion-transformer"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"GitHub - mbreuss/diffusion-literature-for-robotics: Summary of key papers and blogs about diffusion models to learn about the topic. Detailed list of all published diffusion robotics papers. · GitHub","url":"https://github.com/mbreuss/diffusion-literature-for-robotics"},{"title":"FRMD: Fast Robot Motion Diffusion with Consistency-Distilled","url":"https://arxiv.org/pdf/2503.02048"},{"title":"FloorDiffusion: Diffusion model-based conditional floorplan image generation method using parameter-efficient fine-tuning and image inpainting - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S2352710224018886"},{"title":"Diffusion Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2504.08438v3"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"}]

I've performed the web search for "quality floor diffusion inference robotics". Here are the key findings:

## Main Results

The search results reveal several important topics related to diffusion models in robotics:

### **Diffusion Policy for Robot Learning**
Diffusion Policy is a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. It benchmarks across 12 different tasks from 4 different robot manipulation benchmarks and consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%.

### **Quality Floor in Training Data**
Interestingly, one result discusses the concept of a "quality floor" in robot learning. Demonstrations with task failures, dropped objects, or operator confusion should be filtered out. This highlights that while diffusion models can handle noisy data, there is still a minimum quality threshold required for training data.

### **Inference Speed and Quality Trade-offs**
It is imperative to consider an appropriate trade-off between sample quality and inference time, tailored to the specific task requirements. Common choices of noise levels are 50–100 during training, but only a subset of five to ten steps during inference.

### **Floor Plan Generation with Diffusion**
The search also returned results on "FloorDiffusion," a specialized application: FloorDiffusion is a diffusion model-based conditional floorplan generation method where only a few key parameters of the pre-trained diffusion model are fine-tuned for the floorplan domain, and the fine-tuned diffusion model performs conditional floorplan generation by inpainting unfinished regions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44ae0d5b-7034-4d9b-8c34-96fb8b6a4a12",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "a25edf48-d650-4a82-86bd-2825e1a93d84",
  "sourceToolAssistantUUID": "44ae0d5b-7034-4d9b-8c34-96fb8b6a4a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T20:03:10.750Z_

<details><summary>↩ Tool result · `toolu_015P8aZ6HU2XFAdDnYTqd1mA`</summary>

```text
Web search results for query: "per-modality convergence diffusion denoising 2025 2026"

Links: [{"title":"Cross-modality 3D MRI synthesis via cycle-guided denoising diffusion probability model - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/41292517/"},{"title":"A Note on the Convergence of Denoising Diffusion Probabilistic Models | OpenReview","url":"https://openreview.net/forum?id=wLe1bG93yc"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf"},{"title":"Denoising diffusion probabilistic models are optimally adaptive to unknown low dimensionality","url":"https://arxiv.org/html/2410.18784v3"},{"title":"Denoising diffusion probabilistic models | Proceedings of the 34th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/abs/10.5555/3495724.3496298"},{"title":"GitHub - ChunmingHe/awesome-diffusion-models-in-low-level-vision: A Repository for Diffusion-Model-related Papers in Low-level Vision · GitHub","url":"https://github.com/ChunmingHe/awesome-diffusion-models-in-low-level-vision"},{"title":"Comprehensive exploration of diffusion models in image generation: a survey | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11110-3"},{"title":"GitHub - 52CV/WACV-2025-Papers · GitHub","url":"https://github.com/52CV/WACV-2025-Papers"},{"title":"[2406.01320] Structural and Convergence Analysis of Discrete-Time Denoising Diffusion Probabilistic Models","url":"https://arxiv.org/abs/2406.01320"},{"title":"Denoising Diffusion Probabilistic Models | Request PDF","url":"https://www.researchgate.net/publication/342352924_Denoising_Diffusion_Probabilistic_Models"}]

I've performed the web search for "per-modality convergence diffusion denoising 2025 2026". Here are the key findings:

## Recent Research on Diffusion Models and Denoising

The search results reveal several relevant research developments:

### Convergence Analysis of Diffusion Models

Denoising diffusion probabilistic models (DDPM) have emerged as a mainstream generative model in generative AI. While sharp convergence guarantees have been established for the DDPM, recent work investigates how the DDPM can achieve sampling speed-ups through automatic exploitation of intrinsic low dimensionality of data, demonstrating optimal adaptivity to unknown low dimensionality.

### Multimodal and Per-Modality Applications

A new paradigm proposes that text is represented as discrete tokens and modeled autoregressively, while continuous image pixels are modeled using denoising diffusion, though it is non-trivial to integrate these two distinct techniques into one single network due to significant differences between discrete text tokens and continuous image/video representations.

### Cross-Modality MRI Synthesis

Recent work proposes a cycle-guided denoising diffusion probability model (CG-DDPM) framework for cross-modality magnetic resonance imaging (MRI) synthesis, aiming to generate high-quality MRIs of a target modality from an existing modality.

### Theoretical Advances

Recent theoretical work shows that the time-dependent score function associated with the forward diffusion process admits a characterization as the backward component of a forward-backward stochastic differential equation, providing a structural description of the score function and clarifying how score estimation errors propagate along the reverse-time dynamics.

These developments reflect active research into convergence properties and per-modality handling in diffusion models throughout 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6adcc7b-1a92-4da6-bf98-8d3ac62122d3",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "2d018f8d-f7a6-4b82-903a-f1bae314cfee",
  "sourceToolAssistantUUID": "a6adcc7b-1a92-4da6-bf98-8d3ac62122d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T20:03:11.264Z_

<details><summary>↩ Tool result · `toolu_01F1YwntZHnfm3DAupMsH59p`</summary>

```text
Web search results for query: "modality-specific convergence diffusion adaptive steps"

Links: [{"title":"Adapt and Diffuse: Sample-Adaptive Reconstruction Via Latent Diffusion Models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11421836/"},{"title":"AMM-Diff: Adaptive Multi-Modality Diffusion Network for Missing Modality Imputation","url":"https://arxiv.org/html/2501.12840v1"},{"title":"Improved Noise Schedule for Diffusion Training","url":"https://arxiv.org/html/2407.03297"},{"title":"Convergence in Diffusion Models","url":"https://haroldbenoit.com/notes/ml/diffusion-models/training/convergence-in-diffusion-models"},{"title":"What are Diffusion Models? | Lil'Log","url":"https://lilianweng.github.io/posts/2021-07-11-diffusion-models/"},{"title":"1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29","url":"https://www.techrxiv.org/users/956810/articles/1325916/master/file/data/A%20Survey%20on%20Vision-Language%20Models%20for%20Multimodal%20Federated%20Learning%20Tasks/A%20Survey%20on%20Vision-Language%20Models%20for%20Multimodal%20Federated%20Learning%20Tasks.pdf?inline=true"},{"title":"Lumina-T2X: Transforming Text into Any Modality, Resolution, and Duration via Flow-based Large Diffusion Transformers","url":"https://arxiv.org/html/2405.05945v1"},{"title":"Diffusion model - Wikipedia","url":"https://en.wikipedia.org/wiki/Diffusion_model"},{"title":"ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation","url":"https://arxiv.org/html/2602.21622"},{"title":"Adaptive Clinical-Aware Latent Diffusion for Multimodal Brain Image Generation and Missing Modality Imputation","url":"https://arxiv.org/html/2603.09931"}]

Based on the web search results, here's what I found related to your query about "modality-specific convergence diffusion adaptive steps":

## Key Findings

The search results reveal several relevant research areas:

### 1. **Adaptive Diffusion Models with Sample-Based Convergence**

Methods can adapt their compute at test time by scaling the number of iterations to convergence, though it is unclear how the optimal number of iterations correlates with degradation severity. This relates to adaptive stepping strategies in diffusion-based image restoration.

### 2. **Multimodal Diffusion with Adaptive Fusion**

Recent research has developed adaptive approaches for handling multiple modalities:

- An Adaptive Multi-Modality Diffusion Network (AMM-Diff) is a diffusion-based generative model capable of handling any number of input modalities and generating the missing ones.

- ACADiff is a framework that synthesizes missing brain imaging modalities through adaptive clinical-aware diffusion by progressively denoising latent representations while attending to available imaging data, and employs adaptive fusion that dynamically reconfigures based on input availability.

### 3. **Dynamic Modality Weighting in Diffusion Policies**

Rather than using fixed fusion weights, adaptive approaches allocate attention based on task context, with systems automatically shifting from vision-dominant weights to balanced multi-modal attention during different task phases.

### 4. **Convergence Through Adaptive Sampling**

The learning of score function in diffusion models is more challenging in the middle of the schedule, and log-normal sampling places greater emphasis on central time steps, thereby accelerating convergence.

These approaches collectively address how diffusion models can adapt their steps and fusion strategies based on specific modalities and convergence requirements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec651baa-8837-4c22-bc1f-b3a2bcd9a2aa",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "dcd34305-bea4-4ebc-91a2-66d255df0b86",
  "sourceToolAssistantUUID": "ec651baa-8837-4c22-bc1f-b3a2bcd9a2aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T20:03:11.600Z_

<details><summary>↩ Tool result · `toolu_01YD3mCobKDNP2ansioGL9kC`</summary>

```text
Web search results for query: "extension mechanism denoising diffusion steps quality guarantee"

Links: [{"title":"StepSaver: Predicting Minimum Denoising Steps for Diffusion Model Image Generation","url":"https://arxiv.org/html/2408.02054v1"},{"title":"Enhancing Diffusion Model Guidance through Calibration and Regularization","url":"https://arxiv.org/html/2511.05844"},{"title":"Denoising Diffusion Step-aware Models","url":"https://arxiv.org/html/2310.03337v3"},{"title":"Optimizing Decoding Paths in Masked Diffusion Models by Quantifying Uncertainty","url":"https://arxiv.org/html/2512.21336v1"},{"title":"Aman's AI Journal • Primers • Diffusion Models","url":"https://aman.ai/primers/ai/diffusion-models/"},{"title":"Improved Denoising Diffusion Probabilistic Models","url":"https://proceedings.mlr.press/v139/nichol21a/nichol21a.pdf"},{"title":"Optimal Stepsize for Diffusion Sampling","url":"https://arxiv.org/html/2503.21774v1"},{"title":"Denoising Diffusion Step-aware Models | OpenReview","url":"https://openreview.net/forum?id=c43FGk8Pcg"},{"title":"Watch Your Step: Information Injection in Diffusion Models via Shadow Timestep Embedding","url":"https://arxiv.org/html/2605.00935"},{"title":"Structured Denoising Diffusion Models in Discrete State-Spaces","url":"https://arxiv.org/pdf/2107.03006"}]

Based on the search results, I found several relevant papers on denoising diffusion steps and quality guarantees. Here's what the research reveals:

## Key Findings

**Denoising Steps and Quality Relationship:**
A higher number of denoising steps generally leads to finer details and better image quality, but requires more computational resources and time. However, increasing the number of steps does not necessarily guarantee improved quality in the generated images.

**Extension Mechanisms for Quality Guarantees:**

Several approaches address quality optimization through different extension mechanisms:

1. **Optimal Stepsize Scheduling:** Optimal Stepsize Distillation proposes a dynamic programming framework that extracts theoretically optimal schedules by distilling knowledge from reference trajectories, reformulating stepsize optimization as recursive error minimization to guarantee global discretization bounds. This enables 10× accelerated text-to-image generation while preserving 99.4% performance.

2. **Step-aware Model Architecture:** DDSM employs a spectrum of neural networks whose sizes are adapted according to the importance of each generative step through evolutionary search, circumventing redundant computational efforts in less critical steps. This achieves computational savings of 49-76% across different datasets without compromising generation quality.

3. **Adaptive Step Prediction:** An innovative NLP model can be fine-tuned to determine the minimal number of denoising steps required for any given text prompt, serving as a real-time tool that recommends the ideal denoise steps for generating high-quality images efficiently.

These mechanisms provide theoretical guarantees or empirical robustness for maintaining quality while optimizing the denoising process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2564102-36be-4255-aca7-7160108c80bf",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "12bb71e3-0fbd-4de1-9a8a-6c2e78946fdd",
  "sourceToolAssistantUUID": "a2564102-36be-4255-aca7-7160108c80bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T20:03:17.010Z_

<details><summary>↩ Tool result · `toolu_01VXojwfARigsbxTyYPn5Mct`</summary>

```text
Web search results for query: "self-correction continuous diffusion multi-modal"

Links: [{"title":"Training-Free Self-Correction for Multimodal Masked Diffusion Models","url":"https://arxiv.org/html/2602.02927"},{"title":"Self-Correcting LLM-Controlled Diffusion (SLD)","url":"https://www.emergentmind.com/topics/self-correcting-llm-controlled-diffusion-sld-framework"},{"title":"Counterfactual condition diffusion with continuous prior adaptive correction for anomaly detection in multimodal brain MRI - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417424011618"},{"title":"Generalized Discrete Diffusion with Self-Correction","url":"https://arxiv.org/html/2603.02230"},{"title":"[2603.02230] Generalized Discrete Diffusion with Self-Correction","url":"https://arxiv.org/abs/2603.02230"},{"title":"GitHub - tsunghan-wu/SLD: 🔥 [CVPR2024] Official implementation of \"Self-correcting LLM-controlled Diffusion Models (SLD)","url":"https://github.com/tsunghan-wu/SLD"},{"title":"[2311.16090] Self-correcting LLM-controlled Diffusion ... - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2311.16090"},{"title":"Multi-Modal Latent Diffusion - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11049248/"},{"title":"[2311.16090] Self-correcting LLM-controlled Diffusion Models","url":"https://arxiv.org/abs/2311.16090"},{"title":"[2602.02927] Training-Free Self-Correction for Multimodal Masked Diffusion Models","url":"https://arxiv.org/abs/2602.02927"}]

Based on the web search results, here are the key findings related to self-correction, continuous diffusion, and multi-modal approaches:

## Training-Free Self-Correction for Multimodal Masked Diffusion Models

Masked diffusion models have emerged as a powerful framework for text and multimodal generation, though their sampling procedure updates multiple tokens simultaneously and treats generated tokens as immutable, which may lead to error accumulation when early mistakes cannot be revised.

A recent approach achieves training-free self-correction for multimodal MDMs by exploiting the inductive bias already present in pre-trained masked diffusion backbones, without modifying model parameters or introducing external evaluators. Extensive experiments on text-to-image generation and multimodal understanding benchmarks demonstrate that this approach consistently improves generation quality, while also enabling faster sampling without sacrificing output quality.

## Self-Correcting Discrete Diffusion (SCDD)

A Self-Correcting Discrete Diffusion (SCDD) model reformulates pretrained self-correction with explicit state transitions and learns directly in discrete time. Experiments conducted at the GPT-2 scale indicate that this model consistently surpasses existing benchmarks over a few standard datasets, achieving lower generative perplexity without sacrificing sample diversity in parallel generation settings.

## Self-Correcting LLM-Controlled Diffusion (SLD)

SLD is a framework that generates an image from the input prompt, assesses its alignment with the prompt, and performs self-corrections on the inaccuracies in the generated image, steered by an LLM controller that turns text-to-image generation into an iterative closed-loop process.

These approaches represent recent advances in combining self-correction mechanisms with diffusion models for improved multimodal generation and understanding tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b68a17e7-e84f-41f9-a699-d2f122488ca3",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "d354b679-8607-47f5-b678-74374c39d87a",
  "sourceToolAssistantUUID": "b68a17e7-e84f-41f9-a699-d2f122488ca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T20:03:19.271Z_

Let me continue with the remaining searches, including the arxiv.org specific search and the papers you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d354b679-8607-47f5-b678-74374c39d87a",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVAEDDuQEWVxyAU3rGg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ba8afe9-95f7-49d4-a55c-e63aafe011e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014TVczvzgKMpGBJCC2ULkyA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1004,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 16929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5910,
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

_source line 16 · 2026-05-10T20:03:19.507Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PMNDTPLGv1ESWWVkHPBcKN`</summary>

```json
{
  "query": "site:arxiv.org per-modality denoising adaptive 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ba8afe9-95f7-49d4-a55c-e63aafe011e2",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVAEDDuQEWVxyAU3rGg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f1ec47d8-975a-4d78-99cc-5b6cb64aae0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014TVczvzgKMpGBJCC2ULkyA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1004,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 16929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5910,
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

_source line 17 · 2026-05-10T20:03:19.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016S3vsxPWAVbT1Zv4BU4nL7`</summary>

```json
{
  "query": "A1 adaptive vision language action early exit 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1ec47d8-975a-4d78-99cc-5b6cb64aae0a",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVAEDDuQEWVxyAU3rGg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8eab8b00-b416-4f8e-b148-8bedd0e2695d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014TVczvzgKMpGBJCC2ULkyA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1004,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 16929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5910,
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

_source line 18 · 2026-05-10T20:03:20.144Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012AzQMAxxXmM89WYe8WAA3k`</summary>

```json
{
  "query": "CycleVLA self-correcting 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8eab8b00-b416-4f8e-b148-8bedd0e2695d",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVAEDDuQEWVxyAU3rGg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1849a92e-19b8-44fb-bcd1-08e5d4c8a6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014TVczvzgKMpGBJCC2ULkyA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1004,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 16929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5910,
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

_source line 19 · 2026-05-10T20:03:20.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tr9pmYHTNnTVr9NWFfJ5SG`</summary>

```json
{
  "query": "TS-DP reinforcement speculative decoding diffusion policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1849a92e-19b8-44fb-bcd1-08e5d4c8a6ad",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVAEDDuQEWVxyAU3rGg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "081b1623-cbf5-4b02-82d5-01bcac5feeac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014TVczvzgKMpGBJCC2ULkyA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1004,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 16929,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1004,
          "output_tokens": 231,
          "cache_read_input_tokens": 16929,
          "cache_creation_input_tokens": 5910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5910,
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

_source line 20 · 2026-05-10T20:03:26.838Z_

<details><summary>↩ Tool result · `toolu_012AzQMAxxXmM89WYe8WAA3k`</summary>

```text
Web search results for query: "CycleVLA self-correcting 2026"

Links: [{"title":"[2601.02295] CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding","url":"https://arxiv.org/abs/2601.02295"},{"title":"CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding","url":"https://arxiv.org/html/2601.02295v1"},{"title":"CycleVLA: Proactive VLA for Self-Correcting Robots","url":"https://www.emergentmind.com/topics/cyclevla"},{"title":"(PDF) CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding","url":"https://www.researchgate.net/publication/399477602_CycleVLA_Proactive_Self-Correcting_Vision-Language-Action_Models_via_Subtask_Backtracking_and_Minimum_Bayes_Risk_Decoding"},{"title":"[Literature Review] CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding","url":"https://www.themoonlight.io/en/review/cyclevla-proactive-self-correcting-vision-language-action-models-via-subtask-backtracking-and-minimum-bayes-risk-decoding"},{"title":"Robotics Papers on X: \"CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding Chenyang Ma, Guangyu Yang, Kai Lu, Shitong Xu, Bill Byrne, Niki Trigoni, Andrew Markham https://t.co/0U6xlqksof [𝚌𝚜.𝚁𝙾] https://t.co/nUs8dQi8JP\" / X","url":"https://x.com/OWW/status/2008788223112229129"},{"title":"Tactical Rewind: Self-Correction via Backtracking in Vision-And-Language Navigation | Request PDF","url":"https://www.researchgate.net/publication/338513475_Tactical_Rewind_Self-Correction_via_Backtracking_in_Vision-And-Language_Navigation"},{"title":"An Iterative Self-Correcting Agentic RAG System | The International FLAIRS Conference Proceedings","url":"https://journals.flvc.org/FLAIRS/article/view/141838"},{"title":"What We’ll Be Talking About in Cycling in 2026 - Škoda We Love Cycling","url":"https://www.welovecycling.com/wide/2025/12/29/what-well-be-talking-about-in-cycling-in-2026/"},{"title":"How to Self Pollinate Cucumbers | Step by Step Guide (2026)","url":"https://thegardenfixes.com/how-to-self-pollinate-cucumbers/"}]

Based on the search results, here's what I found about CycleVLA:

## CycleVLA: Proactive Self-Correcting Vision-Language-Action Models

CycleVLA is a system that equips Vision-Language-Action models (VLAs) with proactive self-correction, the capability to anticipate incipient failures and recover before they fully manifest during execution.

### Key Components

CycleVLA achieves this by integrating a progress-aware VLA that flags critical subtask transition points where failures most frequently occur, a VLM-based failure predictor and planner that triggers subtask backtracking upon predicted failure, and a test-time scaling strategy based on Minimum Bayes Risk (MBR) decoding to improve retry success after backtracking.

### How It Works

The system builds on the observation that task failures often occur at subtask transitions, where progress near completion provides strong cues for anticipating failure. It integrates a progress-aware VLA that flags critical subtask transition points, a VLM-based failure predictor and planner that triggers subtask backtracking upon predicted failure, and a test-time scaling strategy based on Minimum Bayes Risk (MBR) decoding to improve retry success after backtracking.

### Performance Results

Extensive experiments show that CycleVLA improves performance for both well-trained and under-trained VLAs, and that MBR serves as an effective zero-shot test-time scaling strategy for VLAs.

The paper was published on January 5-6, 2026, and represents a significant advance in making robotic systems more reliable through proactive failure anticipation rather than reactive correction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1849a92e-19b8-44fb-bcd1-08e5d4c8a6ad",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "6695cccb-d937-459d-94be-d60349cf317d",
  "sourceToolAssistantUUID": "1849a92e-19b8-44fb-bcd1-08e5d4c8a6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T20:03:27.347Z_

<details><summary>↩ Tool result · `toolu_016S3vsxPWAVbT1Zv4BU4nL7`</summary>

```text
Web search results for query: "A1 adaptive vision language action early exit 2026"

Links: [{"title":"DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving","url":"https://arxiv.org/html/2511.20720v1"},{"title":"Adaptive Vision-Language Model Routing for Computer Use Agents","url":"https://arxiv.org/html/2603.12823v1"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"[2603.07404] Adaptive Capacity Allocation for Vision Language Action Fine-tuning","url":"https://arxiv.org/abs/2603.07404"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future","url":"https://arxiv.org/html/2512.16760v1"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"}]

Based on the search results, I found relevant information about adaptive vision-language-action models with early exit mechanisms. Here are the key findings:

## Key Research on Adaptive Vision-Language-Action Models with Early Exit

DeeAD is a lightweight, plug-and-play early-exit framework tailored for VLA models, based on the core idea that the model should dynamically terminate inference once the predicted trajectory already falls within an acceptable deviation from a navigation reference.

The framework equips the decoder with an Early Exit Action Head capable of extracting partial trajectories from any layer without retraining. It introduces a lightweight Dissimilarity Estimation component that evaluates the spatial deviation between predicted and reference trajectories, using metrics such as L2 displacement to quantify whether an intermediate plan already satisfies physical driving constraints.

The framework includes a Multi-Hop Exit Controller that adaptively selects which layers to evaluate based on dissimilarity trends, making large jumps when predictions are far from threshold and fine-grained checks when nearing convergence.

When integrated into the ORION VLA framework and evaluated on Bench2Drive, DeeAD achieves up to 28% transformer-layer sparsity and 29% latency reduction.

Additionally, there are other adaptive routing approaches: Adaptive Vision-Language Model Routing (AVR) integrates safety guardrails and routes actions to small or large models based on difficulty and safety classifications, optimizing simultaneously for cost, accuracy, and safety.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8eab8b00-b416-4f8e-b148-8bedd0e2695d",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "909b350d-49fa-4b81-85c2-5cb51c63f8c5",
  "sourceToolAssistantUUID": "8eab8b00-b416-4f8e-b148-8bedd0e2695d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T20:03:27.683Z_

<details><summary>↩ Tool result · `toolu_01PMNDTPLGv1ESWWVkHPBcKN`</summary>

```text
Web search results for query: "site:arxiv.org per-modality denoising adaptive 2026"

Links: [{"title":"Adaptive Clinical-Aware Latent Diffusion for Multimodal Brain Image Generation and Missing Modality Imputation","url":"https://arxiv.org/html/2603.09931"},{"title":"Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation","url":"https://arxiv.org/html/2604.01414"},{"title":"dLLM-ASR: A Faster Diffusion LLM-based Framework for Speech Recognition","url":"https://arxiv.org/pdf/2601.17902"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=550&show=2000"},{"title":"Towards Dexterous Embodied Manipulation via Deep Multi-Sensory Fusion and Sparse Expert Scaling","url":"https://arxiv.org/html/2602.19764"},{"title":"[2604.19141] Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation","url":"https://arxiv.org/abs/2604.19141"},{"title":"Taming the Long Tail: Denoising Collaborative Information for Robust Semantic ID Generation","url":"https://arxiv.org/html/2510.25622"},{"title":"Teach Me How to Denoise: A Universal Framework for Denoising Multi-modal Recommender Systems via Guided Calibration","url":"https://arxiv.org/html/2504.14214"},{"title":"Relational graph-driven differential denoising and diffusion attention fusion for multimodal conversation emotion recognition","url":"https://arxiv.org/html/2603.25752"},{"title":"[2605.02973] Structured Diffusion Bridges: Inductive Bias for Denoising Diffusion Bridges","url":"https://arxiv.org/abs/2605.02973"}]

I've successfully performed the web search for your query: `site:arxiv.org per-modality denoising adaptive 2026`. Here are the results:

The search returned several relevant papers from arXiv from 2026 that involve per-modality (or modality-specific) denoising and adaptive mechanisms:

1. **ACADiff** - A framework that synthesizes missing brain imaging modalities through adaptive clinical-aware diffusion by learning mappings between incomplete multimodal observations and target modalities while progressively denoising latent representations. The framework employs adaptive fusion that dynamically reconfigures based on input availability.

2. **Vision-Torque Fusion** - Two independent UNets are trained in parallel and their noise predictions are blended at each denoising step via a learned routing network. A scale predictor determines the relative influence of torque information when combining the noise predictions from the two modality-specific noise predictors in the diffusion process.

3. **dLLM-ASR** - A diffusion LLM-based framework that transforms the recognition process to a prior-guided and adaptive denoising process.

4. **DeMUSE** - Uses an Adaptive Modality-specific Normalization (AdaMN) mechanism and a Sparse Mixture-of-Experts (MoE) architecture with residual shared experts for multi-sensory fusion.

5. **Patch Forcing** - Augments the model with a lightweight per-patch difficulty head to enable adaptive samplers that allocate compute dynamically, advancing easier regions earlier so they can provide context for harder ones.

These papers showcase various approaches to adaptive and per-modality denoising in 2026 research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1ec47d8-975a-4d78-99cc-5b6cb64aae0a",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "79a7cc2c-0c04-493a-b2e1-92b288eb3664",
  "sourceToolAssistantUUID": "f1ec47d8-975a-4d78-99cc-5b6cb64aae0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T20:03:29.579Z_

<details><summary>↩ Tool result · `toolu_01Tr9pmYHTNnTVr9NWFfJ5SG`</summary>

```text
Web search results for query: "TS-DP reinforcement speculative decoding diffusion policy"

Links: [{"title":"[2512.15773] TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration","url":"https://arxiv.org/abs/2512.15773"},{"title":"TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration","url":"https://arxiv.org/html/2512.15773v1"},{"title":"Artificial Intelligence Dec 2025","url":"https://arxiv.org/list/cs.AI/2025-12?skip=2525&show=250"},{"title":"GitHub - VILA-Lab/Awesome-DLMs: The official GitHub repo for the survey paper \"A Survey on Diffusion Language Models\". · GitHub","url":"https://github.com/VILA-Lab/Awesome-DLMs"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=speculative+decoding"},{"title":"Week 12: Speculative Decoding & Diffusion Models","url":"https://diophontine.github.io/csc412/slides/w12/sld12.pdf"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Self Speculative Decoding for Diffusion Large Language Model | OpenReview","url":"https://openreview.net/forum?id=rKJ7A30lQQ"},{"title":"[2408.05636] Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion","url":"https://arxiv.org/abs/2408.05636"},{"title":"Accelerated Diffusion Models via Speculative Sampling | OpenReview","url":"https://openreview.net/forum?id=BTJSkPpH1t&noteId=v8FBbQXd6b"}]

Based on the search results, I found detailed information about TS-DP:

## TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration

TS-DP (Temporal-aware Reinforcement-based Speculative Diffusion Policy) is the first framework that enables speculative decoding for Diffusion Policy with temporal adaptivity.

### Problem and Motivation

Diffusion Policy excels in embodied control but suffers from high inference latency and computational cost due to multiple iterative denoising steps. The temporal complexity of embodied tasks demands a dynamic and adaptable computation mode. Static and lossy acceleration methods, such as quantization, fail to handle such dynamic embodied tasks, while speculative decoding offers a lossless and adaptive yet underexplored alternative for DP.

### Technical Approach

To handle dynamic environments where task difficulty varies over time, TS-DP distills a Transformer-based drafter to imitate the base model and replace its costly denoising calls. Second, an RL-based scheduler further adapts to time-varying task difficulty by adjusting speculative parameters to maintain accuracy while improving efficiency.

### Key Components

The framework includes a PPO-based scheduler that evaluates time-varying task difficulty using past observations and actions, and produces adaptive speculative parameters.

### Results

Extensive experiments across diverse embodied environments demonstrate that TS-DP achieves up to 4.17 times faster inference with over 94% accepted drafts, reaching an inference frequency of 25 Hz and enabling real-time diffusion-based control without performance degradation.

The paper was published on December 13, 2025, on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "081b1623-cbf5-4b02-82d5-01bcac5feeac",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "e7080623-8c4a-47b0-a4c0-76ad44a871e8",
  "sourceToolAssistantUUID": "081b1623-cbf5-4b02-82d5-01bcac5feeac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T20:03:31.380Z_

Excellent! Now let me fetch the A1 paper you specifically mentioned to understand the action-consistency test mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7080623-8c4a-47b0-a4c0-76ad44a871e8",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVB9wGgCM584xRKUspV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c8e9eb97-3f34-423f-b0a5-07d9fd3d9346",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SW2vH9KFgrBaFSXHsNhL6q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5240,
      "cache_read_input_tokens": 22839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5240,
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

_source line 25 · 2026-05-10T20:03:31.901Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HnpssRmKyVcVauR2Byb9Lw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.05672",
  "prompt": "action-consistency test for early termination, cross-modal disagreement, quality signal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8e9eb97-3f34-423f-b0a5-07d9fd3d9346",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVB9wGgCM584xRKUspV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9ebe1d8e-d530-466f-be90-fd089e8b597b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SW2vH9KFgrBaFSXHsNhL6q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5240,
      "cache_read_input_tokens": 22839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5240,
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

### Tool result

_source line 26 · 2026-05-10T20:03:36.421Z_

<details><summary>↩ Tool result · `toolu_01HnpssRmKyVcVauR2Byb9Lw`</summary>

```text
# A1: Vision-Language-Action Model for Efficient Robot Control

## Key Innovation

The A1 framework introduces an adaptive inference approach that monitors "action consistency across intermediate VLM layers to trigger early termination." This allows the system to exit computations prematurely when confidence thresholds are met, rather than processing all layers.

## Performance Gains

According to the abstract, A1 achieves substantial efficiency improvements:
- Up to 72% reduction in per-episode latency for flow-matching inference
- Up to 76.6% backbone computation reduction with minimal performance loss
- Superior success rates on RoboChallenge (29.00%) versus comparable baselines

## Technical Approach

The framework combines two efficiency strategies: accelerating the vision-language backbone through early termination, and introducing "Inter-Layer Truncated Flow Matching" to warm-start denoising across different VLM layers, enabling fewer denoising iterations while maintaining accuracy.

## Open-Source Commitment

The researchers release the complete training infrastructure, including code, data pipelines, checkpoints, and evaluation scripts to support reproducibility across simulation benchmarks (LIBERO, VLABench) and real robotic platforms (Franka, AgiBot).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ebe1d8e-d530-466f-be90-fd089e8b597b",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "1f9cce1c-3be3-4a21-b2ac-6670f51d5968",
  "sourceToolAssistantUUID": "9ebe1d8e-d530-466f-be90-fd089e8b597b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T20:03:37.811Z_

Perfect! Now let me search for more specific information about whether there are other papers using disagreement monitoring or convergence-based extension mechanisms in diffusion models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f9cce1c-3be3-4a21-b2ac-6670f51d5968",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVBfAgDd1NryahryVmw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "50dce730-f278-4b8e-a731-b636d8ccd95a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E2Bc8RJA7HiAmbnkaKCMFb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 28079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 408,
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

_source line 28 · 2026-05-10T20:03:38.135Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SgRSGhDRA3QZXSRWTDGcvC`</summary>

```json
{
  "query": "\"disagreement\" \"diffusion\" \"convergence\" early stopping 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50dce730-f278-4b8e-a731-b636d8ccd95a",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVBfAgDd1NryahryVmw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "10d33466-90f5-4074-abc4-bc6f5a4a0d06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E2Bc8RJA7HiAmbnkaKCMFb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 28079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 408,
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

_source line 29 · 2026-05-10T20:03:38.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Hh8LJEyaTv1v5a7mRm1Up`</summary>

```json
{
  "query": "\"ensemble\" \"diffusion\" \"monitoring disagreement\" quality inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d33466-90f5-4074-abc4-bc6f5a4a0d06",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVBfAgDd1NryahryVmw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f22a955f-d7ea-4a33-86c6-6192dc666be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E2Bc8RJA7HiAmbnkaKCMFb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 28079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 408,
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

_source line 30 · 2026-05-10T20:03:38.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UMtFthWN1P1K8SHUhqDc2T`</summary>

```json
{
  "query": "\"divergence monitoring\" \"diffusion steps\" adaptive inference robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f22a955f-d7ea-4a33-86c6-6192dc666be7",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVBfAgDd1NryahryVmw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1132fd48-5a3e-4bfa-a655-6d8e87343ab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E2Bc8RJA7HiAmbnkaKCMFb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 28079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 408,
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

_source line 31 · 2026-05-10T20:03:44.434Z_

<details><summary>↩ Tool result · `toolu_01SgRSGhDRA3QZXSRWTDGcvC`</summary>

```text
Web search results for query: ""disagreement" "diffusion" "convergence" early stopping 2025 2026"

Links: [{"title":"Convergence of Score-Based Discrete Diffusion Models: A Discrete-Time Analysis | OpenReview","url":"https://openreview.net/forum?id=pq1WUegkza"},{"title":"[NeurIPS 2025] Why Diffusion Models Don’t Memorize: The Role of Implicit Dynamical Regularization in Training","url":"https://arxiviq.substack.com/p/neurips-2025-why-diffusion-models"},{"title":"[2410.02321] Convergence of Score-Based Discrete Diffusion Models: A Discrete-Time Analysis","url":"https://arxiv.org/abs/2410.02321"},{"title":"Why Diffusion Models Don’t Memorize: The Role of Implicit Dynamical Regularization in Training | OpenReview","url":"https://openreview.net/forum?id=BSZqpqgqM0"},{"title":"Why Diffusion Models Don't Memorize: The Role of Implicit ...","url":"https://openreview.net/pdf?id=BSZqpqgqM0"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=pq1WUegkza"},{"title":"Diffusion-based Large Language Models Survey","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/276128/preprint_pdf/e686b6b9b5d7b3a94626a1e185a486a1.pdf"},{"title":"Insights on Diffusion Models from Precise Learning Curves","url":"https://arxiv.org/pdf/2502.00336"},{"title":"2026 Stock Market Outlook: Cycle Convergence & What's Next","url":"https://io-fund.com/broad-market/2026-stock-market-outlook-cycle-convergence"},{"title":"Autonomous Agents on Blockchains: Standards, Execution ...","url":"https://arxiv.org/pdf/2601.04583"}]

I found several relevant research papers combining these topics. Here are the key results:

## Recent Research on Diffusion Models, Convergence, and Early Stopping (2025-2026)

### 1. **Convergence of Score-Based Discrete Diffusion Models** (ICLR 2025)

This work derives convergence bounds for the Kullback-Leibler (KL) divergence and total variation (TV) distance between the generated sample distribution and the data distribution, considering both scenarios with and without early stopping. The KL divergence bounds are nearly linear in the dimension d, aligning with state-of-the-art results for diffusion models.

### 2. **Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization** (NeurIPS 2025 Best Paper)

This paper addresses disagreement between generalization and memorization in diffusion models. The work identifies two distinct timescales: an early time τ_gen at which models begin to generate high-quality samples, and a later time τ_mem beyond which memorization emerges, with τ_mem increasing linearly with the training set size n while τ_gen remains constant, creating a growing window of training times where models generalize effectively.

The practical implication of this "Implicit Dynamical Regularization" is that early stopping is not merely a heuristic to prevent rising test error, but a structural necessity for score-based generative modeling.

Both papers directly address the intersection of diffusion models, convergence analysis, and early stopping strategies from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10d33466-90f5-4074-abc4-bc6f5a4a0d06",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "75fc6460-3669-4565-92a0-2b26b636b474",
  "sourceToolAssistantUUID": "10d33466-90f5-4074-abc4-bc6f5a4a0d06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T20:03:46.203Z_

<details><summary>↩ Tool result · `toolu_017Hh8LJEyaTv1v5a7mRm1Up`</summary>

```text
Web search results for query: ""ensemble" "diffusion" "monitoring disagreement" quality inference"

Links: [{"title":"Mitigating Biases with Diverse Ensembles and Diffusion Models","url":"https://arxiv.org/html/2311.16176v2"},{"title":"Mitigating Shortcut Learning with Diffusion Counterfactuals and Diverse Ensembles","url":"https://arxiv.org/html/2311.16176"},{"title":"When Are Two Scores Better Than One? Investigating Ensembles of Diffusion Models","url":"https://arxiv.org/html/2601.11444"},{"title":"Fast Ensembling with Diffusion Schrödinger Bridge","url":"https://arxiv.org/html/2404.15814v1"},{"title":"Improving Diffusion Models by Optimizing Noise at Inference Time | by Pietro Bolcato | Medium","url":"https://medium.com/@pietrobolcato/improving-diffusion-models-by-optimizing-noise-at-inference-time-0d8f5cfb13f6"},{"title":"Advances in diffusion models for image data augmentation: a review of methods, models, evaluation metrics and future research directions | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11116-x"},{"title":"How to Improve Performance of a Diffusion Model by an Ensemble of Expert Models | Towards Data Science","url":"https://towardsdatascience.com/how-to-improve-performance-of-a-diffusion-model-by-an-ensemble-of-expert-models-97e7cfd4c47f/"},{"title":"Ensemble Score Diffusion Model","url":"https://www.emergentmind.com/topics/ensemble-score-diffusion-model"},{"title":"Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=nAIhvNy15T"},{"title":"Learning Diffusions under Uncertainty","url":"https://ojs.aaai.org/index.php/AAAI/article/download/30026/31805"}]

Here are the search results for your query on ensemble diffusion models with monitoring disagreement for quality inference:

## Key Findings

**Ensemble Disagreement for Diversification:**
Ensemble disagreement on diffusion-generated counterfactuals can provide models with an opportunity to break spurious correlations encouraged during training. Synthetic counterfactuals are leveraged to increase model diversity via ensemble disagreement.

**Quality of Ensemble Disagreement:**
The extent and quality of diffusion-guided ensemble diversification is on par with existing methods that rely on additional data. Research shows that the quality of disagreement on ColorDSprites marginally benefits from additional disagreement samples, with approximately 7% more models averting their attention from the shortcut cue color compared to original experiments.

**Monitoring Ensemble Performance:**
Both validation ensemble accuracy and predictive diversity are monitored on a separate de-correlated set of validation data, with values selected at the intersection of accuracy and diversification trends for each model.

**Ensemble Inference Quality:**
Test-time inference requires combining the predictions of individual models into a single output, with the arithmetic mean being a common approach, particularly in regression and probabilistic settings.

**Advanced Ensemble Score Diffusion:**
The Ensemble Score Diffusion Model is a framework that combines score-based diffusion and ensemble-based inference to enable scalable, training-free data assimilation and sampling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f22a955f-d7ea-4a33-86c6-6192dc666be7",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "4856f3eb-33b7-4cfb-b959-e8bac44098ba",
  "sourceToolAssistantUUID": "f22a955f-d7ea-4a33-86c6-6192dc666be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T20:03:46.211Z_

<details><summary>↩ Tool result · `toolu_01UMtFthWN1P1K8SHUhqDc2T`</summary>

```text
Web search results for query: ""divergence monitoring" "diffusion steps" adaptive inference robotics"

Links: [{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://arxiv.org/pdf/2303.04137"},{"title":"RA-DP: Rapid Adaptive Diffusion Policy for Training-Free High-frequency Robotics Replanning","url":"https://arxiv.org/html/2503.04051"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising","url":"https://arxiv.org/pdf/2510.21991"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"One-Step Diffusion Policy: Fast Visuomotor Policies via Diffusion Distillation | OpenReview","url":"https://openreview.net/forum?id=Z85EoYQhCs"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"Diff-DAgger: Uncertainty Estimation with Diffusion Policy for Robotic Manipulation","url":"https://arxiv.org/html/2410.14868v1"},{"title":"Interaction-aware Diffusion Planning for Adaptive Dexterous ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Liang_DexHandDiff_Interaction-aware_Diffusion_Planning_for_Adaptive_Dexterous_Manipulation_CVPR_2025_paper.pdf"},{"title":"Robotics: Science and Systems 2023","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"}]

I found relevant research results on diffusion models in robotics. Here's what the search returned:

## Key Findings

The search results focus on diffusion-based policies for robotic manipulation, which is a rapidly growing area of research. Here are some relevant connections to your search terms:

**Diffusion Steps and Adaptive Inference:**
Single-step sampling processes can compromise accuracy compared to iterative approaches, and applying guidance directly to the data space either causes divergence or fails to influence the sampling process effectively. One approach integrates action queues with different noise levels for high-frequency replanning by denoising the action queue with monotonically increasing noise levels, enabling single-step action generation without compromising sample quality.

**Monitoring in Diffusion-Based Systems:**
Ensemble methods for robot-gated DAgger effectively distinguish in-distribution uni-modal from out-of-distribution data using action variance, but they fail at in-distribution multi-modal points due to policy disagreement. In deployment, the policy makes action inference by iteratively denoising a random noise conditioned on the current observation, and after action generation, the training loss function is used to compute the loss associated with the generated action.

**Robotics Applications:**
Since 2022, there has been a noticeable increase in the implementation of diffusion probabilistic models within robotic manipulation, applied across various tasks including trajectory planning and grasp prediction.

The search results suggest that divergence monitoring and adaptive control of diffusion steps are important considerations in real-time robotic applications where inference speed and reliability are critical.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1132fd48-5a3e-4bfa-a655-6d8e87343ab2",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "8acb84d7-f5f4-48dc-a38b-2eb5a45565bd",
  "sourceToolAssistantUUID": "1132fd48-5a3e-4bfa-a655-6d8e87343ab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-10T20:03:47.819Z_

Let me do a few more targeted searches to ensure comprehensive coverage of potential competitors to your core claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8acb84d7-f5f4-48dc-a38b-2eb5a45565bd",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVCP93cFEupeanPsnXq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b10e0c5a-f6fb-4e9e-96c2-4d69d8443937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0182FpWxoASQPjQs9KHmjrm8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 28487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
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

_source line 35 · 2026-05-10T20:03:48.351Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YAqNaxfYfkaXtbyjpxzsYb`</summary>

```json
{
  "query": "\"multi-head\" \"disagreement\" diffusion inference quality guarantee"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b10e0c5a-f6fb-4e9e-96c2-4d69d8443937",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVCP93cFEupeanPsnXq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d91b32a4-9683-4d36-9b12-e633878d554e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0182FpWxoASQPjQs9KHmjrm8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 28487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
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

_source line 36 · 2026-05-10T20:03:48.475Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KoeVwUvBdsBYJxEzEm4nyW`</summary>

```json
{
  "query": "\"oracle disagreement\" diffusion denoising extension steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d91b32a4-9683-4d36-9b12-e633878d554e",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVCP93cFEupeanPsnXq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ceb3fc2c-fc1d-4c4c-9b40-fe31f8da1060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0182FpWxoASQPjQs9KHmjrm8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 28487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
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

_source line 37 · 2026-05-10T20:03:48.877Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AbKGDnq5JMHJYrfycFvbhK`</summary>

```json
{
  "query": "\"confidence estimation\" diffusion inference adaptive steps robotics VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceb3fc2c-fc1d-4c4c-9b40-fe31f8da1060",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVCP93cFEupeanPsnXq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0c3406e1-3bf9-468b-a1a9-c7ea2b6220a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0182FpWxoASQPjQs9KHmjrm8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 28487,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2988
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 179,
          "cache_read_input_tokens": 28487,
          "cache_creation_input_tokens": 2988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2988,
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

_source line 38 · 2026-05-10T20:03:55.046Z_

<details><summary>↩ Tool result · `toolu_01KoeVwUvBdsBYJxEzEm4nyW`</summary>

```text
Web search results for query: ""oracle disagreement" diffusion denoising extension steps"

Links: [{"title":"Is Your Conditional Diffusion Model Actually Denoising?","url":"https://arxiv.org/html/2512.18736"},{"title":"StepSaver: Predicting Minimum Denoising Steps for Diffusion Model Image Generation","url":"https://arxiv.org/html/2408.02054v1"},{"title":"An In-Depth Guide to Denoising Diffusion Probabilistic Models DDPM – Theory to Implementation","url":"https://learnopencv.com/denoising-diffusion-probabilistic-models/"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"Denoising Diffusion Step-aware Models | OpenReview","url":"https://openreview.net/forum?id=c43FGk8Pcg"},{"title":"[2006.11239] Denoising Diffusion Probabilistic Models","url":"https://arxiv.org/abs/2006.11239"},{"title":"[2402.04384] Denoising Diffusion Probabilistic Models in Six Simple Steps","url":"https://arxiv.org/abs/2402.04384"},{"title":"Improved Denoising Diffusion Probabilistic Models","url":"https://proceedings.mlr.press/v139/nichol21a/nichol21a.pdf"},{"title":"Denoising Diffusion Probabilistic Models | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/denoising-diffusion-probabilistic-models-63b4fd3a3b67"},{"title":"Denoising Diffusion Probabilistic Models","url":"https://hojonathanho.github.io/diffusion/"}]

Based on the search results, I found highly relevant information about your query. The most directly relevant result is a recent research paper titled "Is Your Conditional Diffusion Model Actually Denoising?"

When conditional diffusion models are queried, their generations consistently deviate from the idealized "denoising" process, inducing disagreement between popular sampling algorithms (e.g. DDPM, DDIM).

The paper introduces Schedule Deviation, a rigorous measure which captures the rate of deviation from a standard denoising process. This appears to be related to what you're referring to as "oracle disagreement" in the context of extension steps.

The deviation from an idealized denoising process occurs due to the difficulty of bridging distinct denoising flows across different parts of the conditioning space.

The research shows that Schedule Deviation is strongly correlated with the difference between DDPM and DDIM samplers, as measured by the empirical 1-Wasserstein distance, with the structural similarity demonstrated across the conditioning space.

This research directly addresses the phenomenon of disagreement between denoising diffusion models and standard sampling algorithms when extending beyond the idealized denoising process, particularly in conditional diffusion models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceb3fc2c-fc1d-4c4c-9b40-fe31f8da1060",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "f4537b47-c77b-4271-bdfa-b148e845d8f7",
  "sourceToolAssistantUUID": "ceb3fc2c-fc1d-4c4c-9b40-fe31f8da1060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T20:03:56.110Z_

<details><summary>↩ Tool result · `toolu_01AbKGDnq5JMHJYrfycFvbhK`</summary>

```text
Web search results for query: ""confidence estimation" diffusion inference adaptive steps robotics VLA"

Links: [{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.14148v1"},{"title":"[2412.03293] Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning","url":"https://arxiv.org/abs/2412.03293"},{"title":"LLaDA-VLA: Diffusion Action Models in Robotics","url":"https://www.emergentmind.com/papers/2509.06932"},{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"(PDF) Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression","url":"https://www.researchgate.net/publication/386454973_Diffusion-VLA_Scaling_Robot_Foundation_Models_via_Unified_Diffusion_and_Autoregression"},{"title":"DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression | OpenReview","url":"https://openreview.net/forum?id=VdwdU81Uzy&noteId=KMyfyxiVhr"}]

I found several highly relevant papers on confidence estimation, diffusion inference, and adaptive steps in robotics Vision-Language-Action (VLA) models. Here are the key results:

## Key Findings

**AsyncVLA - Confidence-Aware Adaptive Inference:**
AsyncVLA proposes a confidence rater that estimates the relative confidence of each action token, enabling confidence-aware robot action generation with self-correction. Rather than using a fixed number of uniform denoising steps, AsyncVLA adaptively schedules the time steps in asynchronous flow matching, performing regeneration on action tokens with low confidence.

**Discrete Diffusion VLA - Adaptive Decoding:**
Discrete Diffusion VLA selects the inference order adaptively by confidence or confidence gap, enabling arbitrary-order decoding at test time. Its adaptive decoding mechanism keeps high-confidence tokens each round and anneals the keep ratio with a cosine schedule for easy-first parallel refinement.

**LLaDA-VLA - Hierarchical Confidence-Based Remasking:**
LLaDA-VLA introduces a two-level hierarchy where actions within a chunk are ranked by aggregated confidence scores with the most confident action selected for partial preservation, and within this action, tokens are further ranked by confidence with only high-confidence tokens retained.

**General VLA Survey:**
Recent VLA approaches are classified into 4 categories: autoregression-based, diffusion-based, reinforcement-based, hybrid, and specialized methods.

These papers demonstrate an active research area focusing on using confidence estimation to adaptively control inference steps in diffusion-based robotics VLA models, improving efficiency and robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c3406e1-3bf9-468b-a1a9-c7ea2b6220a4",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "92059c16-3a1b-4ff8-a380-037226d6d78c",
  "sourceToolAssistantUUID": "0c3406e1-3bf9-468b-a1a9-c7ea2b6220a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T20:03:57.672Z_

<details><summary>↩ Tool result · `toolu_01YAqNaxfYfkaXtbyjpxzsYb`</summary>

```text
Web search results for query: ""multi-head" "disagreement" diffusion inference quality guarantee"

Links: [{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"},{"title":"Diffusion Blend: Inference-Time Multi-Preference Alignment for Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=M2DXbwO8le"},{"title":"DiffThinker: Generative Multimodal Reasoning","url":"https://www.emergentmind.com/papers/2512.24165"},{"title":"IF-MDM: Implicit Face Motion Diffusion Model for High-Fidelity Realtime Talking Head Generation","url":"https://arxiv.org/html/2412.04000"},{"title":"Quantifying and Predicting Disagreement in Graded Human Ratings","url":"https://arxiv.org/html/2605.01168"},{"title":"[2505.18547] Diffusion Blend: Inference-Time Multi-Preference Alignment for Diffusion Models","url":"https://arxiv.org/abs/2505.18547"},{"title":"Towards Efficient Multi-LLM Inference: Characterization and Analysis of LLM Routing and Hierarchical Techniques","url":"https://arxiv.org/html/2506.06579v1"},{"title":"Consistency diffusion language models: Up to 14x faster inference without sacrificing quality","url":"https://www.together.ai/blog/consistency-diffusion-language-models"},{"title":"Untitled Document","url":"https://arxiv.org/html/2506.10978"},{"title":"Diffusion Models are Secretly Exchangeable:Parallelizing ...","url":"https://arxiv.org/pdf/2505.03983"}]

Based on the web search results, I found relevant research related to your query about multi-head disagreement, diffusion, inference, and quality guarantees. Here are the key findings:

## Multi-Head Perturbation in Diffusion Models

A recent work moves beyond heuristic layer selection in attention perturbation guidance by identifying attention heads as a more meaningful and fine-grained unit of intervention, presenting HeadHunter, an iterative framework for selecting semantically relevant attention heads aligned with arbitrary, user-defined objectives. Empirical results on state-of-the-art DiT-based models, including Stable Diffusion 3 and FLUX.1, show that head-level perturbation not only improves general image quality with a single search but also aesthetically enhances specific visual styles.

## Quality Guarantees in Diffusion Inference

Research on accelerating inference in DDPMs via parallelization shows it is possible to produce samples identically distributed as the sequential process, thereby ensuring zero quality loss, while also achieving a theoretically guaranteed speedup over sequential sampling.

## Multi-Preference Alignment

Diffusion Blend proposes a novel approach to solve inference-time multi-preference alignment by blending backward diffusion processes associated with fine-tuned models. Extensive experiments show that Diffusion Blend algorithms consistently outperform relevant baselines and closely match or exceed the performance of individually fine-tuned models, enabling efficient, user-driven alignment at inference-time.

These works address different aspects of controlling and improving diffusion model inference quality while managing multiple objectives and architectural components.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d91b32a4-9683-4d36-9b12-e633878d554e",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "f0ad18e4-3535-4e13-9293-531e0dd0af91",
  "sourceToolAssistantUUID": "d91b32a4-9683-4d36-9b12-e633878d554e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-10T20:03:59.863Z_

Excellent! Let me do one final round to search for any papers specifically about "soft stopping" or "quality threshold" in diffusion, and verify I have comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0ad18e4-3535-4e13-9293-531e0dd0af91",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVDE5cf8AjAcUbbeMGA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d546f190-beeb-441b-8a82-e6339419c1a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018CfYHuQUwLEhheXkqBr7g3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1773,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 31475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
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

_source line 42 · 2026-05-10T20:04:00.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NMDzs6Zm8bA6feK3M11y9J`</summary>

```json
{
  "query": "\"soft stopping\" diffusion inference variable steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d546f190-beeb-441b-8a82-e6339419c1a1",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVDE5cf8AjAcUbbeMGA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ab6c03e5-0544-42a6-8a36-dc427edbac71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018CfYHuQUwLEhheXkqBr7g3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1773,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 31475,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1123
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1773,
          "output_tokens": 143,
          "cache_read_input_tokens": 31475,
          "cache_creation_input_tokens": 1123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1123,
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

_source line 43 · 2026-05-10T20:04:00.496Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014PK7PKBfyteoNozxbE71gN`</summary>

```json
{
  "query": "\"quality threshold\" diffusion denoising early exit decision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab6c03e5-0544-42a6-8a36-dc427edbac71",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVDE5cf8AjAcUbbeMGA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d8419afd-1b0c-48c4-8037-e776dc84a172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018CfYHuQUwLEhheXkqBr7g3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1773,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 31475,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1123
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1773,
          "output_tokens": 143,
          "cache_read_input_tokens": 31475,
          "cache_creation_input_tokens": 1123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1123,
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

_source line 44 · 2026-05-10T20:04:07.480Z_

<details><summary>↩ Tool result · `toolu_014PK7PKBfyteoNozxbE71gN`</summary>

```text
Web search results for query: ""quality threshold" diffusion denoising early exit decision"

Links: [{"title":"Fast-Decoding Diffusion Language Models via Progress-Aware Confidence Schedules","url":"https://arxiv.org/html/2512.02892"},{"title":"DeeDiff: Dynamic Uncertainty-Aware Early Exiting for Accelerating Diffusion Model Generation","url":"https://arxiv.org/html/2309.17074v2"},{"title":"StepSaver: Predicting Minimum Denoising Steps for Diffusion Model Image Generation","url":"https://arxiv.org/html/2408.02054v1"},{"title":"Diffusion Language Models Know the Answer Before Decoding","url":"https://arxiv.org/pdf/2508.19982"},{"title":"A new hybrid image denoising algorithm using adaptive and modified decision-based filters for enhanced image quality | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92283-3"},{"title":"Breaking the Likelihood–Quality Trade-off in Diffusion Models by Merging Pretrained Experts","url":"https://arxiv.org/html/2511.19434"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"Boosting Offline MARL under Imbalanced Datasets via ...","url":"https://www.lamda.nju.edu.cn/lilh/file/codi.pdf"},{"title":"Optimizing Re-Masking Schedules for Reasoning in Discrete ...","url":"https://cs224r.stanford.edu/projects/pdfs/CS_224R_Final_Report__3_.pdf"},{"title":"[2006.11239] Denoising Diffusion Probabilistic Models","url":"https://arxiv.org/abs/2006.11239"}]

Based on the search results, I found several relevant papers discussing quality thresholds and early exit decisions in diffusion model denoising. Here are the key findings:

## Early Exit Mechanisms with Quality Thresholds

SchED is a training-free, architecture-agnostic early-exit mechanism for diffusion language models that compares a sequence-level confidence statistic to a smooth, progress-conditioned threshold. SchED compares a sequence-level logit-margin aggregate to a smooth, nonincreasing function of normalized diffusion progress, imposing a stringent requirement at early steps and gradually relaxing it thereafter.

## Dynamic Uncertainty-Based Thresholding

During inference, with the estimated uncertainty of the output prediction from each layer, the computation is able to make termination decisions once the uncertainty is lower than the predefined threshold. This approach is used in DeeDiff, which applies early exiting strategies across multiple inference steps in diffusion models.

## Progress-Aware Threshold Schedules

In early commit decoding, p = (Tmax − t)/Tmax is denoted as the decoding progress, where Tmax is the total number of decoding steps, and τ(p) is the threshold for early commit decoding. The method becomes more risk-tolerant, requiring a progressively smaller threshold to confirm convergence as the denoising progresses.

These approaches generally tie the stopping decision to model confidence or certainty stabilization, allowing diffusion models to achieve substantial speedups while maintaining generation quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8419afd-1b0c-48c4-8037-e776dc84a172",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "ecc7cc29-fc70-4551-88a7-d59718c81b09",
  "sourceToolAssistantUUID": "d8419afd-1b0c-48c4-8037-e776dc84a172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T20:04:07.595Z_

<details><summary>↩ Tool result · `toolu_01NMDzs6Zm8bA6feK3M11y9J`</summary>

```text
Web search results for query: ""soft stopping" diffusion inference variable steps"

Links: [{"title":"Basic performance · Hugging Face","url":"https://huggingface.co/docs/diffusers/stable_diffusion"},{"title":"Guide to Stable Diffusion Steps Parameter | getimg.ai","url":"https://getimg.ai/guides/interactive-guide-to-stable-diffusion-steps-parameter"},{"title":"Stable Diffusion with 🧨 Diffusers","url":"https://huggingface.co/blog/stable_diffusion"},{"title":"What are Diffusion Models? | Lil'Log","url":"https://lilianweng.github.io/posts/2021-07-11-diffusion-models/"},{"title":"What is Inference Steps? | Guide","url":"https://stablecog.com/guide/generation-settings/inference-steps"},{"title":"Stable Diffusion - Wikipedia","url":"https://en.wikipedia.org/wiki/Stable_Diffusion"},{"title":"StepSaver: Predicting Minimum Denoising Steps for Diffusion Model Image Generation","url":"https://arxiv.org/html/2408.02054v1"},{"title":"Hyperparameters are all you need: Using five-step inference for an original diffusion model to generate images comparable to the latest distillation model","url":"https://arxiv.org/html/2510.02390v1"},{"title":"SDXL inference in under 2 seconds: the ultimate guide to Stable Diffusion optimization","url":"https://www.baseten.co/blog/sdxl-inference-in-under-2-seconds-the-ultimate-guide-to-stable-diffusion-optimiza/"},{"title":"Stable Diffusion 3.5: Architecture and Inference","url":"https://learnopencv.com/stable-diffusion-3/"}]

Based on the search results, I found relevant information about diffusion inference optimization techniques, though the specific term "soft stopping" didn't appear in these results. However, I found closely related concepts:

## Variable Steps and Early Stopping in Diffusion Inference

A diffusion model starts with an image that's just noise and iterates toward the final output, with inference time scaling linearly with the number of iterations. However, the quality of the resulting image is not linear, as earlier steps have much more impact than later ones.

One optimization technique that's similar to what "soft stopping" might refer to is **partial guidance cessation**. You can stop using classifier-free guidance (CFG) partway through the invocation by setting it to zero, so the prompt still has extra influence on the essential first steps while the later steps where it is not as useful are faster. Turning CFG off after 40% of the steps was found to be the right tradeoff between marginal speed and marginal image quality.

Another approach involves finding optimal variable steps per prompt. 73.5% of prompts only need 30 or 20 steps to achieve the best image quality, suggesting that dynamically determining the number of steps needed for each prompt can improve efficiency.

The search results didn't contain a specific paper or technique explicitly called "soft stopping" for diffusion inference. If you're looking for information about a specific technique with that name, you might want to provide more context or search for it with additional terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab6c03e5-0544-42a6-8a36-dc427edbac71",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "afc022510ad977c81",
  "type": "user",
  "uuid": "5e27e83b-f84c-4401-ba38-e0229a38aabd",
  "sourceToolAssistantUUID": "ab6c03e5-0544-42a6-8a36-dc427edbac71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-10T20:04:39.980Z_

Perfect. Now I have comprehensive coverage. Let me compile my final report with all the findings.

## COMPREHENSIVE SEARCH REPORT: Cross-Modal Disagreement and Per-Modality Convergence in Diffusion Denoising

I've conducted an extensive search for work on cross-modal disagreement and per-modality convergence monitoring within diffusion denoising as a quality signal. Here are my findings:

### DIRECT COMPETITORS TO YOUR CORE CLAIM

**1. AsyncVLA: Confidence-Aware Adaptive Inference (2025)**
- [AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models](https://arxiv.org/html/2511.14148v1)
- **Key mechanism:** Estimates confidence of each action token and adaptively schedules denoising time steps, performing regeneration on low-confidence tokens. This is very similar to your proposal but operates at the token level rather than cross-modal disagreement level.

**2. A1: Action-Consistency Test for Early Termination (2026)**
- URL: https://arxiv.org/abs/2604.05672
- **Key mechanism:** Monitors "action consistency across intermediate VLM layers to trigger early termination." Introduces "Inter-Layer Truncated Flow Matching" to warm-start denoising across different VLM layers.
- **Similarity to your claim:** Uses consistency checking within the denoising process for early exit, but doesn't explicitly use cross-modal disagreement. Achieves up to 76.6% backbone computation reduction.
- **Critical difference:** Monitors action consistency within a single modality stream across layers, not cross-modal disagreement.

**3. Discrete Diffusion VLA: Confidence-Based Adaptive Ordering (2025)**
- [Discrete Diffusion VLA](https://arxiv.org/html/2508.20072v1)
- **Key mechanism:** Selects inference order adaptively by confidence or confidence gap, enabling arbitrary-order decoding. Keeps high-confidence tokens each round and anneals the keep ratio.

**4. DeeDiff: Dynamic Uncertainty-Based Early Exiting (2023-2024)**
- [DeeDiff: Dynamic Uncertainty-Aware Early Exiting for Accelerating Diffusion Model Generation](https://arxiv.org/html/2309.17074v2)
- **Key mechanism:** Uses estimated uncertainty from each layer to make termination decisions when uncertainty falls below a predefined threshold. This is a quality signal but based on single-model uncertainty, not disagreement.

**5. SchED: Progress-Aware Confidence Schedule (2025)**
- [Fast-Decoding Diffusion Language Models via Progress-Aware Confidence Schedules](https://arxiv.org/html/2512.02892)
- **Key mechanism:** Training-free early-exit comparing sequence-level confidence statistic to a smooth, progress-conditioned threshold. Not multimodal-specific.

**6. StepSaver: Predicting Minimum Denoising Steps (2024)**
- [StepSaver: Predicting Minimum Denoising Steps for Diffusion Model Image Generation](https://arxiv.org/html/2408.02054v1)
- **Key mechanism:** Uses NLP model to predict minimum denoising steps for given prompts. Single-model prediction, not disagreement-based.

---

### RELATED RESEARCH ON CONVERGENCE AND DISAGREEMENT MONITORING

**7. "Is Your Conditional Diffusion Model Actually Denoising?" (2024)**
- [Is Your Conditional Diffusion Model Actually Denoising?](https://arxiv.org/html/2512.18736)
- **Key finding:** Introduces "Schedule Deviation" metric capturing disagreement between popular sampling algorithms (DDPM vs DDIM). Shows disagreement between different denoising approaches—this is the closest thing to cross-modal disagreement in the literature.

**8. Ensemble Disagreement for Diversification (2023)**
- [Mitigating Shortcut Learning with Diffusion Counterfactuals and Diverse Ensembles](https://arxiv.org/html/2311.16176)
- **Key mechanism:** Uses ensemble disagreement on diffusion-generated samples to increase model diversity and break spurious correlations. Quality monitoring via disagreement but not applied to step extension in denoising.

**9. DiffDis: Cross-Modal Discrimination in Diffusion (2023)**
- [DiffDis: Empowering Generative Diffusion Model with Cross-Modal Discrimination Capability](https://openaccess.thecvf.com/content/ICCV2023/papers/Huang_DiffDis_Empowering_Generative_Diffusion_Model_with_Cross-Modal_Discrimination_Capability_ICCV_2023_paper.pdf)
- **Note:** Combines generative and discriminative tasks in diffusion but doesn't use disagreement for step extension.

**10. Why Diffusion Models Don't Memorize (NeurIPS 2025 Best Paper)**
- **Key insight:** Identifies two timescales in score-based models: τ_gen (sample quality generation) and τ_mem (memorization onset). Early stopping is structurally necessary for generalization. Convergence analysis but not disagreement-based.

---

### ADAPTIVE AND PER-MODALITY DIFFUSION APPROACHES

**11. Vision-Torque Fusion with Per-Modality Blending (2026)**
- [Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation](https://arxiv.org/html/2604.01414)
- **Key mechanism:** Trains two independent UNets in parallel (one per modality) and blends noise predictions at each denoising step via a learned routing network. Scale predictor determines influence balance. **This is per-modality convergence monitoring at the noise prediction level.**

**12. AMM-Diff: Adaptive Multi-Modality Diffusion (2025)**
- [AMM-Diff: Adaptive Multi-Modality Diffusion Network for Missing Modality Imputation](https://arxiv.org/html/2501.12840v1)
- **Key mechanism:** Handles any number of input modalities adaptively, dynamically reconfiguring based on input availability.

**13. ACADiff: Adaptive Clinical-Aware Diffusion (2026)**
- [Adaptive Clinical-Aware Latent Diffusion for Multimodal Brain Image Generation](https://arxiv.org/html/2603.09931)
- **Key mechanism:** Employs adaptive fusion that dynamically reconfigures based on modality availability.

**14. ADM-DP: Dynamic Modality Weighting (2026)**
- [ADM-DP: Adaptive Dynamic Modality Diffusion Policy via Vision-Tactile-Graph Fusion](https://arxiv.org/html/2602.21622)
- **Key mechanism:** Automatically shifts modality weights from vision-dominant to balanced multi-modal attention during different task phases.

**15. Contrastive Diffusion (CDCD): Convergence Acceleration (2023-2024)**
- [Contrastive Diffusion for Cross-Modal and Conditional Generation](https://l-yezhu.github.io/CDCD/)
- **Key finding:** Uses contrastive learning in denoising to improve convergence, reducing required steps by >35%. Not disagreement-based but shows convergence monitoring exists.

---

### REINFORCEMENT LEARNING APPROACHES TO ADAPTIVE DENOISING

**16. TS-DP: Reinforcement Speculative Decoding (December 2025)**
- [TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration](https://arxiv.org/abs/2512.15773)
- **Key mechanism:** PPO-based scheduler adapts speculative parameters to time-varying task difficulty. Achieves up to 4.17x faster inference while maintaining 94%+ draft acceptance.
- **Important:** Uses RL to adaptively control denoising iterations, but based on task difficulty not cross-modal disagreement.

**17. D3P: Dynamic Denoising Diffusion Policy via RL (2025)**
- [D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning](https://arxiv.org/html/2508.06804v1)
- **Key mechanism:** RL-based approach to dynamically control denoising steps in policy generation.

---

### SELF-CORRECTION IN MULTIMODAL SYSTEMS

**18. CycleVLA: Proactive Self-Correcting VLA (January 2026)**
- [CycleVLA: Proactive Self-Correcting Vision-Language-Action Models](https://arxiv.org/abs/2601.02295)
- **Key mechanism:** Proactively anticipates failures and triggers subtask backtracking using VLM-based failure predictor. Uses Minimum Bayes Risk decoding for test-time scaling.
- **Important difference:** Self-correction through backtracking, not through within-denoising disagreement monitoring.

**19. Training-Free Self-Correction for Multimodal Masked Diffusion (2026)**
- [Training-Free Self-Correction for Multimodal Masked Diffusion Models](https://arxiv.org/abs/2602.02927)
- **Key mechanism:** Exploits inductive bias in pre-trained masked diffusion models for self-correction without modifying parameters. Enables faster sampling without quality loss.

---

### EARLY EXIT MECHANISMS IN VLA

**20. DeeAD: Dynamic Early Exit for VLA (2025)**
- [DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving](https://arxiv.org/html/2511.20720v1)
- **Key mechanism:** Early Exit Action Head with Dissimilarity Estimation evaluating spatial deviation between predicted and reference trajectories. Multi-hop exit controller adaptively selects which layers to evaluate.
- **Important:** Uses trajectory dissimilarity not cross-modal disagreement.

---

### CONVERGENCE ANALYSIS IN DIFFUSION

**21. Convergence of Score-Based Discrete Diffusion Models (ICLR 2025)**
- [Convergence of Score-Based Discrete Diffusion Models: A Discrete-Time Analysis](https://arxiv.org/abs/2410.02321)
- **Key contribution:** Derives convergence bounds considering early stopping scenarios. Theoretical but not applied to disagreement-based extension.

---

### CRITICAL GAP ANALYSIS

**Your core novelty claim:** Using cross-modal disagreement or per-modality convergence monitoring **within diffusion denoising** as a quality signal to trigger extension of computation.

**What I found:**
1. **Per-modality noise prediction blending** (Vision-Torque Fusion) is very close but doesn't explicitly use disagreement to trigger extension
2. **Confidence-based adaptive steps** (AsyncVLA, Discrete Diffusion VLA) monitor single-modality confidence, not cross-modal disagreement
3. **Action consistency** (A1) monitors consistency within one modality stream, not across modalities
4. **Schedule Deviation** is the closest to cross-modal disagreement but measures disagreement between algorithms, not between modalities
5. **Ensemble disagreement** exists in diffusion but not applied to within-denoising extension
6. **No papers explicitly use cross-modal disagreement within denoising steps to trigger extension**

---

### PAPERS VERIFIED

- **TS-DP (2512.15773):** Confirmed - exists, published December 2025
- **A1 (2604.05672):** Confirmed - fetched and analyzed, published 2026
- **CycleVLA (2601.02295):** Confirmed - published January 2026

---

### SOURCES

- [A1: Vision-Language-Action Model for Efficient Robot Control](https://arxiv.org/abs/2604.05672)
- [AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models](https://arxiv.org/html/2511.14148v1)
- [TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration](https://arxiv.org/abs/2512.15773)
- [CycleVLA: Proactive Self-Correcting Vision-Language-Action Models](https://arxiv.org/abs/2601.02295)
- [DeeDiff: Dynamic Uncertainty-Aware Early Exiting for Accelerating Diffusion Model Generation](https://arxiv.org/html/2309.17074v2)
- [Is Your Conditional Diffusion Model Actually Denoising?](https://arxiv.org/html/2512.18736)
- [Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation](https://arxiv.org/html/2604.01414)
- [Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies](https://arxiv.org/html/2508.20072v1)
- [Training-Free Self-Correction for Multimodal Masked Diffusion Models](https://arxiv.org/abs/2602.02927)
- [AMM-Diff: Adaptive Multi-Modality Diffusion Network for Missing Modality Imputation](https://arxiv.org/html/2501.12840v1)
- [DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving](https://arxiv.org/html/2511.20720v1)
- [Fast-Decoding Diffusion Language Models via Progress-Aware Confidence Schedules](https://arxiv.org/html/2512.02892)
- [StepSaver: Predicting Minimum Denoising Steps for Diffusion Model Image Generation](https://arxiv.org/html/2408.02054v1)
- [Convergence of Score-Based Discrete Diffusion Models: A Discrete-Time Analysis](https://arxiv.org/abs/2410.02321)
- [Contrastive Diffusion for Cross-Modal and Conditional Generation](https://l-yezhu.github.io/CDCD/)

---

### CONCLUSION

**Your core claim appears to have substantial novelty.** While there is significant recent work on:
- Adaptive denoising steps via confidence/uncertainty
- Per-modality fusion in diffusion models
- Early exit mechanisms based on consistency/convergence
- Ensemble disagreement in diffusion models

I found **no papers that explicitly combine cross-modal disagreement monitoring within the denoising loop to trigger dynamic extension of computation steps.** The closest competitor is Vision-Torque Fusion's per-modality noise prediction blending, but this uses learned routing rather than disagreement-based decisions. AsyncVLA's confidence-aware adaptive scheduling is also close but monitors single-modality confidence, not cross-modal disagreement.

The proposal merges two mature concepts (multimodal fusion + adaptive step control) in a novel way within the denoising process itself, which appears to be genuinely unexplored territory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e27e83b-f84c-4401-ba38-e0229a38aabd",
  "isSidechain": true,
  "agentId": "afc022510ad977c81",
  "requestId": "req_011CauVDxXWd4daE5PwS7aF9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "15ae3320-8554-4efa-9db4-105136add0c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015LFj1NZYsBLLMtbEzcGFxL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 2738,
      "cache_read_input_tokens": 32598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2738,
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
