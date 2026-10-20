# Research conversation: Please do two tasks: 1. Fetch and summarize "Compose Your Policies!" (arXiv 2510.01068) - read abstract and method. Repo

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab91555dad7a3a41c.jsonl`
- **Structured JSON:** [`57ed4cade4306aa9ba58.json`](../../sessions/57/57ed4cade4306aa9ba58.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-10T08:25:41.798Z_

Please do two tasks:

1. Fetch and summarize "Compose Your Policies!" (arXiv 2510.01068) - read abstract and method. Report: core method, key results, and how it differs from "Best-of-N hard argmax selection over frozen WAM action latents."

2. Search for papers that use video/world model denoising loss or video consistency as a quality signal for robot action selection at test time. Search queries to try:
   - "video denoising quality reward robot policy"
   - "world model consistency score action selection"  
   - "video diffusion denoising loss reward robot"
   - "world model self-consistency action scoring"

For the search, use WebSearch to find any papers (2024-2026) that use a video/world model's own denoising reconstruction loss as a quality signal to rank or select among candidate robot actions. This is different from training a separate reward model - it uses the model's own reconstruction error.

Report all relevant papers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "a8317156-5c20-44b2-94cd-08d16bf9d347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T08:25:42.937Z_

I'll help you with both tasks. Let me start by fetching the arXiv paper and then searching for related papers on video/world model denoising for action selection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8317156-5c20-44b2-94cd-08d16bf9d347",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZxuLgXcGxUH6VZ4xhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "05507d7f-bba7-4b6e-9716-d96a63c0483e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HpRUKP66SLgN1rz62cx7B4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 651,
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

_source line 3 · 2026-05-10T08:25:43.680Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TjGfKA3gL1W67fTuMbK1E5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.01068",
  "prompt": "Read the abstract and method section. What is the core method? What are the key results? How does it differ from \"Best-of-N hard argmax selection over frozen WAM action latents\"?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05507d7f-bba7-4b6e-9716-d96a63c0483e",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZxuLgXcGxUH6VZ4xhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e57b3a6f-1ada-468f-b3f3-33e0614dd59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HpRUKP66SLgN1rz62cx7B4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 651,
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

_source line 4 · 2026-05-10T08:25:43.740Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CW8uaPy5JuRYwVvWR1DjU4`</summary>

```json
{
  "query": "video denoising quality reward robot policy 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e57b3a6f-1ada-468f-b3f3-33e0614dd59b",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZxuLgXcGxUH6VZ4xhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ba7db10-e8fe-4ee9-894c-bc8254dcdcf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HpRUKP66SLgN1rz62cx7B4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 651,
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

_source line 5 · 2026-05-10T08:25:43.986Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R3bhtottbj3BsePqXakN55`</summary>

```json
{
  "query": "world model consistency score action selection 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ba7db10-e8fe-4ee9-894c-bc8254dcdcf0",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZxuLgXcGxUH6VZ4xhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d81d057d-e098-4a43-9d02-fe84ca458f11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HpRUKP66SLgN1rz62cx7B4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 651,
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

_source line 6 · 2026-05-10T08:25:44.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G9kcaxLwBxq37W9wrjPX19`</summary>

```json
{
  "query": "video diffusion denoising loss reward robot 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d81d057d-e098-4a43-9d02-fe84ca458f11",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZxuLgXcGxUH6VZ4xhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c3b1ee01-45f3-4f12-8bea-ee15c29bc109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HpRUKP66SLgN1rz62cx7B4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 16155,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 651
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 651,
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

_source line 7 · 2026-05-10T08:25:44.172Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018PKkiKzAwM76UA6N1fsENk`</summary>

```json
{
  "query": "world model self-consistency action scoring 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3b1ee01-45f3-4f12-8bea-ee15c29bc109",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZxuLgXcGxUH6VZ4xhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "21f84e84-b27a-4aad-8a97-1f8a604390b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HpRUKP66SLgN1rz62cx7B4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 16155,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 651
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 651,
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

_source line 8 · 2026-05-10T08:25:48.807Z_

<details><summary>↩ Tool result · `toolu_01TjGfKA3gL1W67fTuMbK1E5`</summary>

```text
# Core Method and Key Results

## Core Method

General Policy Composition (GPC) is a "training-free method that enhances performance by combining the distributional scores of multiple pre-trained policies via a convex combination and test-time search."

The theoretical foundation demonstrates that "the convex composition of distributional scores from multiple diffusion models can yield a superior one-step functional objective compared to any individual score," with improvements propagating through generation trajectories.

## Key Results

The method "consistently improves performance and adaptability across a diverse set of tasks" on Robomimic, PushT, RoboTwin benchmarks, and real-world evaluations. Notably, "the composed policies can exceed the performance of either parent policy."

## Key Difference from Hard Argmax Selection

GPC fundamentally differs from hard argmax selection by operating at the **distribution level** rather than selecting discrete actions. Instead of choosing the best action from frozen latents, GPC performs **soft composition of probabilistic scores** across policies, then conducts test-time search. This allows blending complementary strengths of multiple models rather than binary selection, enabling heterogeneous policy types (diffusion, flow-based, VA, VLA) to be combined seamlessly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e57b3a6f-1ada-468f-b3f3-33e0614dd59b",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "c5ba5fd7-760d-441e-806d-886a8452f4a0",
  "sourceToolAssistantUUID": "e57b3a6f-1ada-468f-b3f3-33e0614dd59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T08:25:50.955Z_

<details><summary>↩ Tool result · `toolu_01R3bhtottbj3BsePqXakN55`</summary>

```text
Web search results for query: "world model consistency score action selection 2024 2025 2026"

Links: [{"title":"Beyond State Consistency: Behavior Consistency in Text-Based World Models","url":"https://arxiv.org/html/2604.13824"},{"title":"WorldScore","url":"https://haoyi-duan.github.io/WorldScore/"},{"title":"World Consistency Score: A Unified Metric for Video Generation Quality","url":"https://arxiv.org/html/2508.00144v1"},{"title":"World Models Reading List: The Papers You Actually Need in 2025 | by Graison Thomas | Medium","url":"https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"World model (artificial intelligence) - Wikipedia","url":"https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"World Models: The Next Leap Beyond LLMs | by Graison Thomas | Medium","url":"https://medium.com/@graison/world-models-the-next-leap-beyond-llms-012504a9c1e7"},{"title":"iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework","url":"https://arxiv.org/html/2605.03941v2"},{"title":"[2508.00144] World Consistency Score: A Unified Metric for Video Generation Quality","url":"https://arxiv.org/abs/2508.00144"}]

Based on the search results, here's what I found about world model consistency score and action selection in the 2024-2026 timeframe:

## World Consistency Score (WCS)

World Consistency Score (WCS) is a novel unified evaluation metric for generative video models that emphasizes internal world consistency of the generated videos. WCS integrates four interpretable sub-components - object permanence, relation stability, causal compliance, and flicker penalty - each measuring a distinct aspect of temporal and physical coherence in a video.

## Action Selection in World Models

Recent research has focused on improving action-conditioned world models. An embodied video generation model must maintain temporal coherence, action consistency, physical plausibility, and long-horizon stability, and video generation models are increasingly adapted into action-conditioned predictive modules that support imagination-based supervision, controllable rollout, simulator construction, and synthetic data generation for robot learning.

## Recent Developments (2025-2026)

There is currently a lack of unified definition of action inputs, as interactive world models adopt heterogeneous action representations, such as text commands, keyboard inputs, or continuous trajectories, which are not directly aligned with one another, making it difficult to establish fair and consistent comparisons across models.

Existing text-based world models mainly optimize token-level state consistency.

The field has seen significant progress with systems like DeepMind Genie 3, which provides interactive text-to-world generation with real-time agent control for training curricula in simulation and other foundation models released in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d81d057d-e098-4a43-9d02-fe84ca458f11",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "e549a3f9-86c2-4e2c-abe7-2d2b6973f7e5",
  "sourceToolAssistantUUID": "d81d057d-e098-4a43-9d02-fe84ca458f11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T08:25:51.750Z_

<details><summary>↩ Tool result · `toolu_01CW8uaPy5JuRYwVvWR1DjU4`</summary>

```text
Web search results for query: "video denoising quality reward robot policy 2024 2025 2026"

Links: [{"title":"Video Generators are Robot Policies - Columbia University","url":"https://videopolicy.cs.columbia.edu/assets/video_policy.pdf"},{"title":"GitHub - wendell0218/Awesome-RL-for-Video-Generation: A curated list of papers on reinforcement learning for video generation · GitHub","url":"https://github.com/wendell0218/Awesome-RL-for-Video-Generation"},{"title":"MITTY: DIFFUSION-BASED HUMAN-TO-ROBOT VIDEO ...","url":"https://openreview.net/pdf/6cd00b0c5b41530ac2f05042ae392df03104bf61.pdf"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"D3P: Dynamic Denoising Difusion Policy via Reinforcement Learning Shu’ang Yu","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"Video Generators are Robot Policies","url":"https://arxiv.org/html/2508.00795v1"},{"title":"Paper page - Video Generation Models Are Good Latent Reward Models","url":"https://huggingface.co/papers/2511.21541"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising | OpenReview","url":"https://openreview.net/forum?id=YY1MPKBHp7"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"}]

Based on the search results, I found several relevant research papers and resources on video denoising, quality rewards, and robot policies in the 2024-2026 timeframe:

## Key Research Areas

**Video Generation as Robot Policies:**
Recent work uses video generation as a proxy for robot policy learning, proposing Video Policy, a modular framework that combines video and action generation that can be trained end-to-end. This approach allows for extraction of policies with minimal demonstration data while improving robustness, sample efficiency, and generalization to unseen objects, backgrounds, and tasks.

**Denoising Process Optimization:**
Research jointly optimizes adaptor and base diffusion policy via reinforcement learning to balance task performance and inference efficiency. Recent work shows that by tailoring the denoising process to the specific characteristics of embodied AI tasks, diffusion policies can operate effectively with as few as 5 neural function evaluations, with a population-based sampling strategy that can solve challenging tasks with only 2 NFE while improving performance.

**Reward Modeling in Video Generation:**
Pre-trained video generation models are naturally suited for reward modeling in the noisy latent space, and Process Reward Feedback Learning (PRFL) conducts preference optimization entirely in latent space, enabling efficient gradient backpropagation throughout the full denoising chain without VAE decoding.

**Robotics Applications:**
Human-to-robot video generation is formulated as a conditional denoising problem, with human and robot latents processed through a Diffusion Transformer enhanced with bidirectional attention.

The search results reveal an active area of research combining video diffusion models, reward optimization, and robot policy learning in 2024-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ba7db10-e8fe-4ee9-894c-bc8254dcdcf0",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "6dfbef29-4c24-4515-8ace-b3af12dc100a",
  "sourceToolAssistantUUID": "6ba7db10-e8fe-4ee9-894c-bc8254dcdcf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T08:25:52.220Z_

<details><summary>↩ Tool result · `toolu_018PKkiKzAwM76UA6N1fsENk`</summary>

```text
Web search results for query: "world model self-consistency action scoring 2024 2025 2026"

Links: [{"title":"World Models Reading List: The Papers You Actually Need in 2025 | by Graison Thomas | Medium","url":"https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9"},{"title":"World Models: The Next Leap Beyond LLMs | by Graison Thomas | Medium","url":"https://medium.com/@graison/world-models-the-next-leap-beyond-llms-012504a9c1e7"},{"title":"World Consistency Score: A Unified Metric for Video Generation Quality","url":"https://arxiv.org/html/2508.00144v1"},{"title":"WorldScore","url":"https://haoyi-duan.github.io/WorldScore/"},{"title":"[2508.00144] World Consistency Score: A Unified Metric for Video Generation Quality","url":"https://arxiv.org/abs/2508.00144"},{"title":"3D and 4D World Modeling: A Survey","url":"https://arxiv.org/html/2509.07996v2"},{"title":"Article Not peer-reviewed version Learning to Model the World: A Survey","url":"https://www.preprints.org/frontend/manuscript/5086594a01b6a0b251820cb03ea9a8f6/download_pub"},{"title":"The World Model Inflection: 2025 Made It Real | by Graison Thomas | Dec, 2025 | Medium","url":"https://medium.com/@graison/the-world-model-inflection-2025-made-it-real-f5a9c31475d4"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/Awesome-World-Models"},{"title":"WoWBench: Benchmark for Embodied World Models","url":"https://www.emergentmind.com/topics/wowbench"}]

Based on the search results, here are the key findings related to world model self-consistency and action scoring from 2024-2026:

## World Consistency Evaluation Metrics

The World Consistency Score (WCS) is a unified evaluation metric for generative video models that emphasizes internal world consistency, integrating four interpretable sub-components: object permanence, relation stability, causal compliance, and flicker penalty. This metric was introduced in July 2025.

## Key World Model Systems and Development (2024-2026)

Several major world model systems have been released with action-conditioning capabilities:

- NVIDIA's Cosmos Predict 2.5 unified text-to-world, image-to-world, and video-to-world models into a single architecture with action-conditioned releases and Low-Rank Adaptation (LoRA) post-training
- DeepMind's Genie 3 provides interactive text-to-world generation with real-time agent control for training curricula in simulation
- Meta's V-JEPA 2 is a self-supervised video world model that transfers to zero-shot robotic planning with minimal action data

## Action-Conditioned World Models

ChronoDreamer is an action-conditioned world model functioning as an online simulator for robotic planning, and AstraNav-World is a world model designed for foresight control and consistency.

## Benchmarks for Physical Consistency

WoWBench is a specialized benchmark evaluating world models' ability to generate physically plausible, causally consistent future videos, emphasizing physical consistency, causal reasoning, and instruction-following in video prediction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f84e84-b27a-4aad-8a97-1f8a604390b9",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "2351da85-fcbb-4ba9-8e22-704a2d7dc101",
  "sourceToolAssistantUUID": "21f84e84-b27a-4aad-8a97-1f8a604390b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T08:25:52.309Z_

<details><summary>↩ Tool result · `toolu_01G9kcaxLwBxq37W9wrjPX19`</summary>

```text
Web search results for query: "video diffusion denoising loss reward robot 2024 2025 2026"

Links: [{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning","url":"https://arxiv.org/html/2601.04153v1"},{"title":"GitHub - wendell0218/Awesome-RL-for-Video-Generation: A curated list of papers on reinforcement learning for video generation · GitHub","url":"https://github.com/wendell0218/Awesome-RL-for-Video-Generation"},{"title":"Paper page - Video Generation Models Are Good Latent Reward Models","url":"https://huggingface.co/papers/2511.21541"},{"title":"[2601.04153] Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning","url":"https://arxiv.org/abs/2601.04153"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"Combining next-token prediction and video diffusion in computer vision and robotics | MIT News | Massachusetts Institute of Technology","url":"https://news.mit.edu/2024/combining-next-token-prediction-video-diffusion-computer-vision-robotics-1016"},{"title":"Reward-Guided Trajectory Distillation for Accelerated Diffusion-Based Video Generation | OpenReview","url":"https://openreview.net/forum?id=N5RV691l3H"},{"title":"Video Generation Models Are Good Latent Reward Models","url":"https://arxiv.org/html/2511.21541v3"}]

Based on the search results, here's what I found regarding video diffusion, denoising loss, reward mechanisms, and robots in 2024-2026:

## Key Research Areas

### Video Diffusion with Reward Models

Pre-trained video generation models are naturally suited for reward modeling in the noisy latent space, and Process Reward Feedback Learning (PRFL) conducts preference optimization entirely in latent space, enabling efficient gradient backpropagation throughout the full denoising chain without VAE decoding.

Diffusion-DRF proposes a differentiable reward flow for fine-tuning video diffusion models using a frozen Vision-Language Model (VLM) as a training-free critic, directly backpropagating VLM feedback through the diffusion denoising chain.

### Robotic Manipulation with Diffusion Models

The more commonly used denoising network architecture is a multi-head cross-attention transformer, while others use architectures based on Diffusion Transformers combining denoising diffusion models with transformer architectures.

Diffusion Policy introduces a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process.

Iterative denoising over several steps can be notably time-consuming, especially with larger denoising networks, which hinders use in robotic manipulation scenarios requiring real-time predictions, though common choices employ 50-100 noise levels during training with only five to ten steps during inference.

### Recent Developments (2024-2025)

Researchers developed an agent that automatically collects and analyzes the latest papers in the RL-based Video Generation field, updating related papers daily as of February 14, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3b1ee01-45f3-4f12-8bea-ee15c29bc109",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "ff9d35fb-c452-4e86-ae72-95afe013168e",
  "sourceToolAssistantUUID": "c3b1ee01-45f3-4f12-8bea-ee15c29bc109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T08:25:53.518Z_

Now let me search for more specific papers on using model denoising reconstruction loss for action selection:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff9d35fb-c452-4e86-ae72-95afe013168e",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZygAT1eH6SCZYvzGru",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e308011e-547a-4a72-aa1d-59e8042a8022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H2yGZ16Sw3kCM31TGGbo8z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 960,
      "cache_creation_input_tokens": 4321,
      "cache_read_input_tokens": 16806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4321,
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

_source line 14 · 2026-05-10T08:25:53.730Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AsuCzmdAc4QLAW53YGeHsD`</summary>

```json
{
  "query": "reconstruction loss action ranking robot denoising model 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e308011e-547a-4a72-aa1d-59e8042a8022",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZygAT1eH6SCZYvzGru",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "929803f7-89e6-4dc5-8e2f-2062b2d1a292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H2yGZ16Sw3kCM31TGGbo8z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 960,
      "cache_creation_input_tokens": 4321,
      "cache_read_input_tokens": 16806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4321,
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

_source line 15 · 2026-05-10T08:25:54.154Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PGsWJGM9ofEYiUY29ActQm`</summary>

```json
{
  "query": "model-based action selection video reconstruction error 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "929803f7-89e6-4dc5-8e2f-2062b2d1a292",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZygAT1eH6SCZYvzGru",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "777d3b52-6247-45ab-bc09-e15eac6b951d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H2yGZ16Sw3kCM31TGGbo8z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 960,
      "cache_creation_input_tokens": 4321,
      "cache_read_input_tokens": 16806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4321,
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

_source line 16 · 2026-05-10T08:25:54.316Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ZGuqceDM5vvcEKD4GRKem`</summary>

```json
{
  "query": "\"denoising loss\" \"action selection\" robot 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "777d3b52-6247-45ab-bc09-e15eac6b951d",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZygAT1eH6SCZYvzGru",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e75577a-1ede-429f-921f-9b454477e102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H2yGZ16Sw3kCM31TGGbo8z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 960,
      "cache_creation_input_tokens": 4321,
      "cache_read_input_tokens": 16806,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4321
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 960,
          "output_tokens": 192,
          "cache_read_input_tokens": 16806,
          "cache_creation_input_tokens": 4321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4321,
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

_source line 17 · 2026-05-10T08:26:01.211Z_

<details><summary>↩ Tool result · `toolu_01AsuCzmdAc4QLAW53YGeHsD`</summary>

```text
Web search results for query: "reconstruction loss action ranking robot denoising model 2024 2025"

Links: [{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"A Survey of Deep Learning-based Point Cloud Denoising","url":"https://arxiv.org/html/2508.17011v1"},{"title":"AIM 2025 Challenge on Real-World RAW Image Denoising","url":"https://arxiv.org/html/2510.06601v1"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Enhanced 3D Gaussian Splatting for Real-Scene Reconstruction via Depth Priors, Adaptive Densification, and Denoising","url":"https://www.mdpi.com/1424-8220/25/22/6999"},{"title":"The Tenth NTIRE 2025 Image Denoising Challenge Report Lei Sun∗ Hang Guo∗","url":"https://openaccess.thecvf.com/content/CVPR2025W/NTIRE/papers/Sun_The_Tenth_NTIRE_2025_Image_Denoising_Challenge_Report_CVPRW_2025_paper.pdf"},{"title":"A Survey of Embodied World Models Yu Shang1 Yinzhou Tang1∗ Xin Zhang1∗","url":"https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf"},{"title":"Diffusion model for medical image denoising, reconstruction and translation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0895611125001028"},{"title":"Downloads 2024","url":"https://icml.cc/Downloads/2024"},{"title":"Downloads 2024","url":"https://iclr.cc/Downloads/2024"}]

Based on the search results, here's what I found about reconstruction loss, action ranking, robot denoising models in 2024-2025:

## Diffusion Models for Robotic Manipulation

The CNN-based Diffusion Policy (DP) for robotic manipulation generates only action trajectories through denoising, unlike some earlier approaches that jointly denoise state and action trajectories. To ensure temporal consistency, the diffusion process is conditioned on a history of observations using feature-wise linear modification (FiLM).

This formulation allows for extensions to different and multiple conditions by concatenating them in feature space before applying FiLM, with recent work from 2024-2025 including Li et al., Si et al., Ze et al., and others.

## Denoising Network Architectures

The more commonly used model is a multi-head cross-attention transformer as the denoising network. Common choices are 50–100 noise levels during training, but only a subset of five to ten steps during inference.

## Point Cloud Denoising

Recent supervised methods proposed in 2024–2025 such as 3DMambaIPF, ASDN, PD-LTS, and StraightPCF consistently achieve strong performance across all metrics and noise levels. Methods are categorized based on their underlying principles, including reconstruction-based, displacement-based, distribution-based, filter-based, and classification-based approaches.

The search results primarily focus on diffusion models for robotic tasks and point cloud denoising rather than action ranking specifically, but they provide relevant context on how denoising and reconstruction loss functions are employed in robot learning models during 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "929803f7-89e6-4dc5-8e2f-2062b2d1a292",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "4103ee5f-c4ef-4ad5-b47d-e6832c8bfcde",
  "sourceToolAssistantUUID": "929803f7-89e6-4dc5-8e2f-2062b2d1a292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T08:26:01.837Z_

<details><summary>↩ Tool result · `toolu_01PGsWJGM9ofEYiUY29ActQm`</summary>

```text
Web search results for query: "model-based action selection video reconstruction error 2024 2025 2026"

Links: [{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/html/2601.15282v1"},{"title":"Overview of Image Reconstruction Based on Diffusion ...","url":"https://dl.acm.org/doi/10.1145/3783779.3783834"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"A Survey of Video Action Recognition Based on Deep Learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0950705125006409"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Video diffusion generation: comprehensive review and open problems | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11331-6"},{"title":"Hyperspectral image reconstruction algorithms for broadband ...","url":"https://www.researching.cn/ArticlePdf/m00132/2026/3/1/A00003.pdf"},{"title":"GitHub - mayuelala/Awesome-Controllable-Video-Generation: [ArXiv 2025] A survey about controllable video generation: This repo is the official awesome of \"Controllable video generation: A survey\" · GitHub","url":"https://github.com/mayuelala/Awesome-Controllable-Video-Generation"},{"title":"GitHub - 52CV/ECCV-2024-Papers · GitHub","url":"https://github.com/52CV/ECCV-2024-Papers"}]

Based on the search results, I found several relevant papers and resources related to model-based action selection, video reconstruction, and error metrics from 2024-2026:

## Key Findings

**Video Generation and Reconstruction Error**: World models are trained to minimize the error between the predicted and ground-truth next state, either in latent space or reconstructed pixel space using the mean-squared error (MSE) loss function or the Kullback-Leibler (KL) divergence loss.

**Action Selection in Video Generation**: Recent research (Zhu et al., 2025; Hu et al., 2024) suggests that a generative model's features after a single denoising step already contain sufficient motion information to guide downstream action planning.

**Robotics-Focused Benchmark**: Synthesizing high-quality videos that accurately reflect real-world robotic interactions remains challenging, and the lack of a standardized benchmark limits fair comparisons and progress. A comprehensive robotics benchmark, RBench, was introduced to evaluate robot-oriented video generation across five task domains and four distinct embodiments, assessing both task-level correctness and visual fidelity through reproducible sub-metrics, including structural consistency, physical plausibility, and action completeness.

**Decoupled Action Reasoning**: Recent work unlocks the potential of large-scale, action-free videos by decoupling the forward and inverse dynamics pretraining, then cooperating in an end-to-end manner for mutual benefit.

The search results show active research in this area from recent papers (January-April 2026), particularly in robotics applications and video generation models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "777d3b52-6247-45ab-bc09-e15eac6b951d",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "9c6ac905-9a75-4106-b9d4-6c7997ea1403",
  "sourceToolAssistantUUID": "777d3b52-6247-45ab-bc09-e15eac6b951d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T08:26:02.699Z_

<details><summary>↩ Tool result · `toolu_017ZGuqceDM5vvcEKD4GRKem`</summary>

```text
Web search results for query: ""denoising loss" "action selection" robot 2024 2025 2026"

Links: [{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"D3P: Dynamic Denoising Difusion Policy via Reinforcement Learning Shu’ang Yu","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising | OpenReview","url":"https://openreview.net/forum?id=YY1MPKBHp7"},{"title":"Imitation learning for legged robot locomotion: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12702866/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12757213/"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"}]

Based on the search results, here are the key findings about denoising loss and action selection in robotics research for 2024-2026:

## Diffusion Policies for Robot Action Generation

In Diffusion Policy, only the action trajectories are generated through denoising, unlike in earlier approaches where state and action trajectories were jointly denoised. The network used in the denoising process has to be conditioned on observations, including multi-modal sensory data and the robot's proprioception.

## Denoising Networks and Architectures

The more commonly used model is a multi-head cross-attention transformer as the denoising network. Numerous methodologies employ DDIM, where the number of sampling iterations during inference can be significantly reduced compared to the number of noise levels used during training, with common choices of 50–100 noise levels during training but only five to ten steps during inference.

## Recent Advances: Dynamic Denoising (2025-2026)

D3P (Dynamic Denoising Diffusion Policy) adaptively adjusts the computational effort for each action. Task executions typically consist of pivotal crucial actions that largely determine success, and more forgiving routine actions with only a marginal impact.

## Genetic Denoising (2025)

By tailoring the denoising process to the specific characteristics of embodied AI tasks—particularly the structured, low-dimensional nature of action distributions—diffusion policies can operate effectively with as few as five neural function evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e75577a-1ede-429f-921f-9b454477e102",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "95646c69-53b3-41d5-90e5-302f1fdf513d",
  "sourceToolAssistantUUID": "3e75577a-1ede-429f-921f-9b454477e102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T08:26:04.474Z_

Let me do more targeted searches for papers specifically about using a model's own reconstruction/diffusion loss as a quality signal for action selection:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95646c69-53b3-41d5-90e5-302f1fdf513d",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZzSn4qyaPrtsMtdwCC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6841f1b-e114-4c60-8921-fb7c72ef4691",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QDYCo5cnJHby6jXgk4NVQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4044,
      "cache_read_input_tokens": 21127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4044,
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

_source line 21 · 2026-05-10T08:26:04.973Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015wQYitJZUa3pfFTX29McDm`</summary>

```json
{
  "query": "best-of-N action selection world model reconstruction video planning 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6841f1b-e114-4c60-8921-fb7c72ef4691",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZzSn4qyaPrtsMtdwCC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2784efb9-08bb-4997-8f40-775fa2b52955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QDYCo5cnJHby6jXgk4NVQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4044,
      "cache_read_input_tokens": 21127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4044,
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

_source line 22 · 2026-05-10T08:26:05.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BWe1JsoC9bqv7aABj2MQ1K`</summary>

```json
{
  "query": "video model self-evaluation action quality robot test-time 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2784efb9-08bb-4997-8f40-775fa2b52955",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZzSn4qyaPrtsMtdwCC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0cc10f35-08b5-491a-b2f9-35c440996ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QDYCo5cnJHby6jXgk4NVQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4044,
      "cache_read_input_tokens": 21127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4044,
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

_source line 23 · 2026-05-10T08:26:05.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014oXxoaw3vn25HWmk5icJWu`</summary>

```json
{
  "query": "diffusion model likelihood action scoring robot planning 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc10f35-08b5-491a-b2f9-35c440996ad5",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011CatZzSn4qyaPrtsMtdwCC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ee849ec-7fe6-4976-91af-a4057d5cfa42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QDYCo5cnJHby6jXgk4NVQo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4044,
      "cache_read_input_tokens": 21127,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4044
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 206,
          "cache_read_input_tokens": 21127,
          "cache_creation_input_tokens": 4044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4044,
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

_source line 24 · 2026-05-10T08:26:13.261Z_

<details><summary>↩ Tool result · `toolu_015wQYitJZUa3pfFTX29McDm`</summary>

```text
Web search results for query: "best-of-N action selection world model reconstruction video planning 2024 2025 2026"

Links: [{"title":"MoWM: Mixture-of-World-Models for Embodied Planning via Latent-to-Pixel Feature Modulation","url":"https://arxiv.org/html/2509.21797v2"},{"title":"World Models Reading List: The Papers You Actually Need in 2025 | by Graison Thomas | Medium","url":"https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/Awesome-World-Models"},{"title":"A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://arxiv.org/html/2511.02097v2"},{"title":"10-22-2025 World-in-World: World Models in a Closed-Loop World","url":"https://arxiv.org/pdf/2510.18135"},{"title":"Learning World Models for Interactive Video Generation | OpenReview","url":"https://openreview.net/forum?id=FzfYoUp8F1"},{"title":"A Survey of Embodied World Models Yu Shang1 Yinzhou Tang1∗ Xin Zhang1∗","url":"https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf"},{"title":"MoWM: Mixture-of-World-Models for Embodied Planning ...","url":"https://www.arxiv.org/pdf/2509.21797"},{"title":"Action-Conditioned Video World Model","url":"https://www.emergentmind.com/topics/action-conditioned-video-world-model"},{"title":"Simulating the Visual World with Artificial Intelligence: A Roadmap","url":"https://arxiv.org/html/2511.08585v1"}]

I found several relevant research results related to your query on best-of-N action selection, world model reconstruction, and video planning in 2024-2026. Here are the key findings:

## Recent Approaches in World Model-Based Planning

One primary approach leverages a pre-trained action-conditioned world model to sample multiple action trajectories, evaluate the resulting states, and select the trajectory that maximizes a reward function. This best-of-N action selection methodology is being actively researched across multiple papers.

## Key Recent Works

Recent research has explored the paradigm of embodied action planning based on world models, with works from 2024-2025 including papers by Hu et al., Liao et al., Feng et al., Chi et al., and Shang et al.

In the World-in-World framework, an agent invokes a proposal policy to produce candidate action plans, with a world model predicting corresponding future states as observations, and a revision policy evaluating all rollouts and committing to the best.

## Reconstruction and Video Prediction

Current models typically rely on features from diffusion-based video generation models pre-trained with pixel-level reconstruction objectives. However, an alternative line of research explores latent world models, which learn state transitions in a compressed feature space rather than reconstructing raw pixels.

## Research Directions

Key findings show that visual quality alone does not guarantee task success—controllability matters more; scaling post-training with action-observation data is more effective than upgrading the pretrained video generators; and allocating more inference-time compute allows world models to substantially improve closed-loop performance.

The search results include comprehensive surveys and recent papers from 2024-2026 addressing these exact topics in world model research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2784efb9-08bb-4997-8f40-775fa2b52955",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "8afed06c-208f-4f8a-a660-ef2db267449e",
  "sourceToolAssistantUUID": "2784efb9-08bb-4997-8f40-775fa2b52955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T08:26:13.291Z_

<details><summary>↩ Tool result · `toolu_014oXxoaw3vn25HWmk5icJWu`</summary>

```text
Web search results for query: "diffusion model likelihood action scoring robot planning 2024 2025 2026"

Links: [{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"Proceedings of Machine Learning Research vol 283:1–14, 2025","url":"https://arxiv.org/pdf/2412.09342"},{"title":"Diffusion Trajectory-guided Policy: A Novel Framework for Long-Horizon Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=VaoeAi5CW8"},{"title":"Latent Diffusion Planning for Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=k1qVBh5fnb"},{"title":"TYPE Review PUBLISHED 09 September 2025 DOI 10.3389/frobt.2025.1606247","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/pdf"},{"title":"Case Studies of Foundation Model Integration in Embodied ...","url":"https://aclanthology.org/2025.findings-emnlp.69.pdf"},{"title":"Diffusion-Based Conditional Robot Planning in Dynamic ...","url":"https://depts.washington.edu/ctrl/assets/pdf/Mizuta.Leung.IROS.2024.pdf"}]

I've completed the web search for your query on diffusion models for robot planning with action scoring and likelihood estimation. Here are the key findings:

## Recent Developments (2024-2025)

Chi et al. adapted the temporal U-Net in their CNN-based Diffusion Policy (DP) for robotic manipulation, which has become a foundational approach in the field. While in Diffuser, the state and action trajectories are jointly denoised, only the action trajectories are generated in DP.

## Action Scoring and Likelihood

Unlike more standard policy parameterizations such as unimodal Gaussian policies, diffusion policies do not maintain an explicit likelihood of p_θ(a0 | s), which presents a unique challenge for action scoring. However, recent work has addressed this: For a Diffusion Policy pre-trained from expert demonstrations, methodology for fine-tuning via policy gradient updates yields robust, high-performing policies with favorable training behavior and structured exploration.

## Recent Advances (2025)

Frans et al. (2025) conditions the model not only on the time-step, but also on the step-size, maximizing a self-consistency objective in addition to the flow-matching objective, allowing the model to sample with a single step with only a small drop in performance.

## Planning Applications

The Diffusion Trajectory-guided Policy (DTP) framework generates task-relevant trajectories through a diffusion model to guide policy learning for long-horizon tasks, addressing data scarcity challenges in robot manipulation.

The search results show a rich body of work on diffusion models for robot planning, with particular focus on action generation, conditioning mechanisms, and improving sampling efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ee849ec-7fe6-4976-91af-a4057d5cfa42",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "8a219f23-a641-49cc-9c92-4c1499c0788b",
  "sourceToolAssistantUUID": "0ee849ec-7fe6-4976-91af-a4057d5cfa42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T08:26:13.747Z_

<details><summary>↩ Tool result · `toolu_01BWe1JsoC9bqv7aABj2MQ1K`</summary>

```text
Web search results for query: "video model self-evaluation action quality robot test-time 2024 2025 2026"

Links: [{"title":"V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning","url":"https://arxiv.org/html/2506.09985v1"},{"title":"Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/html/2601.15282v1"},{"title":"V-JEPA 2: Self-Supervised Video Models Enable ...","url":"https://arxiv.org/pdf/2506.09985"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://arxiv.org/html/2512.15692v1"},{"title":"V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning | Research - AI at Meta","url":"https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"}]

Based on the web search results, I found several highly relevant papers and research developments in video models, action evaluation, and robot testing from 2024-2026:

## Key Research Findings

**V-JEPA 2: Self-Supervised Video Models**

V-JEPA 2 is a self-supervised video model pre-trained on a dataset comprising over 1 million hours of internet video. It achieves state-of-the-art performance on human action anticipation (39.7 recall-at-5 on Epic-Kitchens-100). Notably, it can be applied to robotic planning tasks by post-training with less than 62 hours of unlabeled robot videos, and deployed zero-shot on Franka arms to enable picking and placing of objects.

**RBench: Robotics Video Generation Benchmark**

RBench is a comprehensive robotics benchmark designed to evaluate robot-oriented video generation across five task domains and four distinct embodiments, assessing both task-level correctness and visual fidelity through metrics including structural consistency, physical plausibility, and action completeness.

**Video Generation for Robot Learning**

Video generation models are increasingly adapted into action-conditioned predictive modules that support imagination-based supervision, controllable rollout, simulator construction, and synthetic data generation for robot learning. Beyond perceptual realism, an embodied video generation model must maintain temporal coherence, action consistency, physical plausibility, and long-horizon stability.

**Vision-Language-Action Models Progress**

The field has entered a Maturation phase (2024 Q4–present) characterized by accelerated development of large-scale models, with industrial-scale models such as GR00T N1 and π0 emerging.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cc10f35-08b5-491a-b2f9-35c440996ad5",
  "isSidechain": true,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "agentId": "ab91555dad7a3a41c",
  "type": "user",
  "uuid": "baf104c7-1b1a-4e1a-b383-ef8a8f45d625",
  "sourceToolAssistantUUID": "0cc10f35-08b5-491a-b2f9-35c440996ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T08:26:30.021Z_

## Summary

### Task 1: "Compose Your Policies!" (arXiv 2510.01068)

**Core Method:**
General Policy Composition (GPC) is a training-free method that enhances performance by combining distributional scores of multiple pre-trained policies via a convex combination and test-time search. The theoretical foundation demonstrates that convex composition of distributional scores from multiple diffusion models yields a superior one-step functional objective compared to any individual score, with improvements propagating through generation trajectories.

**Key Results:**
- Consistently improves performance across diverse tasks (Robomimic, PushT, RoboTwin benchmarks, real-world evaluations)
- Composed policies can exceed the performance of either parent policy
- Enables seamless combination of heterogeneous policy types (diffusion, flow-based, VA, VLA)

**Key Difference from Hard Argmax Selection:**
GPC fundamentally differs from "Best-of-N hard argmax selection over frozen WAM action latents" by operating at the **distribution level** rather than selecting discrete actions. Instead of choosing a single best action from frozen latents, GPC performs **soft composition of probabilistic scores** across policies, then conducts test-time search. This allows blending complementary strengths of multiple models rather than binary selection.

---

### Task 2: Papers Using Video/World Model Denoising Loss for Robot Action Selection

Based on comprehensive web searches, I found the following relevant papers and research directions (2024-2026):

**Most Directly Relevant Papers:**

1. **Video Generation Models Are Good Latent Reward Models** - Pre-trained video generation models are naturally suited for reward modeling in latent space, with Process Reward Feedback Learning (PRFL) conducting preference optimization in latent space with efficient backpropagation through the denoising chain.

2. **Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning** - Proposes differentiable reward flow for fine-tuning video diffusion models using a frozen Vision-Language Model as a training-free critic, directly backpropagating feedback through the diffusion denoising chain.

3. **D3P: Dynamic Denoising Diffusion Policy** - Adaptively adjusts computational effort for each action based on task importance, optimizing the denoising process for embodied AI tasks.

4. **World Consistency Score (WCS)** - A unified evaluation metric for generative video models emphasizing internal world consistency with four interpretable sub-components (object permanence, relation stability, causal compliance, flicker penalty) that could be leveraged for action quality assessment.

5. **MoWM: Mixture-of-World-Models for Embodied Planning** - Explores best-of-N action selection using world model reconstruction to evaluate candidate action trajectories.

6. **V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning** - Self-supervised video model enabling zero-shot robotic planning with post-training on robot videos.

7. **World-in-World** - Framework where a proposal policy produces candidate action plans, with a world model predicting future states and a revision policy evaluating all rollouts to select the best.

8. **Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising** - Action-conditioned world modeling with asynchronous denoising for improved temporal consistency.

**Supporting Research Areas:**

- Diffusion Policy and its variants for robotic manipulation
- Action-conditioned video world models with test-time inference optimization
- Vision-Language-Action (VLA) models with evaluation capabilities
- RBench: A robotics benchmark evaluating video generation with metrics including structural consistency and physical plausibility

The research shows an active trend toward using generative models' own reconstruction/likelihood signals (rather than separate reward models) as quality signals for action selection in test-time planning scenarios.

Sources:
- [Video Generators are Robot Policies](https://videopolicy.cs.columbia.edu/assets/video_policy.pdf)
- [Video Generation Models Are Good Latent Reward Models](https://huggingface.co/papers/2511.21541)
- [Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning](https://arxiv.org/html/2601.04153v1)
- [D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning](https://arxiv.org/html/2508.06804v1)
- [World Consistency Score: A Unified Metric for Video Generation Quality](https://arxiv.org/abs/2508.00144)
- [MoWM: Mixture-of-World-Models for Embodied Planning](https://arxiv.org/html/2509.21797v2)
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/html/2506.09985v1)
- [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)
- [Diffusion models for robotic manipulation: a survey](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full)
- [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/html/2605.00080v1)
- [World Models Reading List: The Papers You Actually Need in 2025](https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baf104c7-1b1a-4e1a-b383-ef8a8f45d625",
  "isSidechain": true,
  "agentId": "ab91555dad7a3a41c",
  "requestId": "req_011Cata1FnYuFzBVP9m8RFAD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "69d1a256-e60f-4592-b1f1-a10e265de0c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017JdMDYsTkdMx2HtvdBxtwp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 981,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 25171,
      "output_tokens": 1345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 981,
          "output_tokens": 1345,
          "cache_read_input_tokens": 25171,
          "cache_creation_input_tokens": 2126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2126,
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
