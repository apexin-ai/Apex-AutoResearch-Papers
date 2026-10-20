# Research conversation: I'm writing a research proposal that fine-tunes Qwen3-VL-8B-Instruct with LoRA (rank=64) on 50K synthetic coordinate-pre

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab102fc4e0ed9c1b2.jsonl`
- **Structured JSON:** [`e4a87a4f5470ced31f47.json`](../../sessions/e4/e4a87a4f5470ced31f47.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-10T07:20:10.418Z_

I'm writing a research proposal that fine-tunes Qwen3-VL-8B-Instruct with LoRA (rank=64) on 50K synthetic coordinate-prediction tasks in normalized [0,1] space (Stage 1 SFT), then applies GRPO on ChartQA (~28K examples) in Stage 2. The reviewer flagged catastrophic forgetting risk from Stage 1.

Please search for:
1. "LoRA catastrophic forgetting VLM" or "LoRA continual learning multimodal" - are there papers showing how severe forgetting is with typical LoRA ranks (64, 128) in vision-language models?
2. What is the standard practice for detecting/mitigating forgetting in two-stage VLM fine-tuning?
3. Is there precedent for Stage 2 GRPO recovering from Stage 1 distribution shift?

Use WebSearch to find relevant papers or blog posts. I need a brief summary of what the literature says about LoRA forgetting severity and how to detect it. Keep it concise - just key facts and citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0e7d6d04-6c83-41f1-ac2d-beed114dd3f9",
  "agentId": "ab102fc4e0ed9c1b2",
  "type": "user",
  "uuid": "9830d379-6f80-4786-881c-08df74eba444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T07:20:11.901Z_

I'll search for information on LoRA catastrophic forgetting in vision-language models and two-stage fine-tuning practices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9830d379-6f80-4786-881c-08df74eba444",
  "isSidechain": true,
  "agentId": "ab102fc4e0ed9c1b2",
  "requestId": "req_011CatUy6s92BjWxtEQ8rXMh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1aaf5cf0-d70e-49e9-a645-33a484ab8e0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018cq62U4BUiqRNGmiS3CDy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
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

_source line 3 · 2026-05-10T07:20:11.960Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AHqJisSMvzP78LYroktAFg`</summary>

```json
{
  "query": "LoRA catastrophic forgetting vision language models VLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aaf5cf0-d70e-49e9-a645-33a484ab8e0b",
  "isSidechain": true,
  "agentId": "ab102fc4e0ed9c1b2",
  "requestId": "req_011CatUy6s92BjWxtEQ8rXMh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e638c5a7-0689-4e5e-9153-00ddac2496ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018cq62U4BUiqRNGmiS3CDy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
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

_source line 4 · 2026-05-10T07:20:11.967Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017gJxtdmtQ636AcCWfS8666`</summary>

```json
{
  "query": "LoRA rank 64 128 continual learning multimodal forgetting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e638c5a7-0689-4e5e-9153-00ddac2496ef",
  "isSidechain": true,
  "agentId": "ab102fc4e0ed9c1b2",
  "requestId": "req_011CatUy6s92BjWxtEQ8rXMh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c563cd5-6ec8-46af-9564-1394aa4f841d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018cq62U4BUiqRNGmiS3CDy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
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

_source line 5 · 2026-05-10T07:20:12.185Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BurJTeEiAkZcFkserRiVwK`</summary>

```json
{
  "query": "two-stage fine-tuning VLM distribution shift SFT reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c563cd5-6ec8-46af-9564-1394aa4f841d",
  "isSidechain": true,
  "agentId": "ab102fc4e0ed9c1b2",
  "requestId": "req_011CatUy6s92BjWxtEQ8rXMh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b25d22f2-29a5-4da7-9471-a2574c591b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018cq62U4BUiqRNGmiS3CDy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
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

_source line 6 · 2026-05-10T07:20:12.459Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016HdbosHn7LDiyFrqJDtfi6`</summary>

```json
{
  "query": "GRPO training recovery from first stage fine-tuning drift"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b25d22f2-29a5-4da7-9471-a2574c591b49",
  "isSidechain": true,
  "agentId": "ab102fc4e0ed9c1b2",
  "requestId": "req_011CatUy6s92BjWxtEQ8rXMh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b1f353c2-102f-4f65-b0dc-f563e56b12f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018cq62U4BUiqRNGmiS3CDy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
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

_source line 7 · 2026-05-10T07:20:12.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0164ftidrsDUhV7cdo5zGKco`</summary>

```json
{
  "query": "detecting mitigating catastrophic forgetting fine-tuned language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1f353c2-102f-4f65-b0dc-f563e56b12f2",
  "isSidechain": true,
  "agentId": "ab102fc4e0ed9c1b2",
  "requestId": "req_011CatUy6s92BjWxtEQ8rXMh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6b2f8d1b-7b7c-4a45-963d-6bbb42339651",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018cq62U4BUiqRNGmiS3CDy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
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

### Tool result

_source line 8 · 2026-05-10T07:20:19.105Z_

<details><summary>↩ Tool result · `toolu_01AHqJisSMvzP78LYroktAFg`</summary>

```text
Web search results for query: "LoRA catastrophic forgetting vision language models VLM"

Links: [{"title":"From Vision-Language Models to Robot Control — Without Forgetting – Princeton Laboratory for Artificial Intelligence Research Blog","url":"https://blog.ai.princeton.edu/2026/04/23/from-vision-language-models-to-robot-control-without-forgetting/"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://vlm2vla.github.io/"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/pdf/2509.22195"},{"title":"Complementary Subspace Low-Rank Adaptation of Vision-Language Models for","url":"https://arxiv.org/pdf/2501.15040"},{"title":"Complementary Subspace Low-Rank Adaptation of Vision-Language Models for Few-Shot Classification","url":"https://arxiv.org/html/2501.15040"},{"title":"Continual Learning in Vision-Language Models via ...","url":"https://arxiv.org/pdf/2506.03189"},{"title":"JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021 1","url":"https://www.isee-ai.cn/~wangruixuan/files/TMM2025Zhang.pdf"},{"title":"Boosting Continual Learning of Vision-Language Models via Mixture-of-Experts","url":"https://openaccess.thecvf.com/content/CVPR2024/papers/Yu_Boosting_Continual_Learning_of_Vision-Language_Models_via_Mixture-of-Experts_Adapters_CVPR_2024_paper.pdf"},{"title":"LoRA-Loop: Closing the Synthetic Replay Cycle for Continual VLM Learning","url":"https://arxiv.org/html/2507.13568"},{"title":"[2509.22195] Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/abs/2509.22195"}]

Based on the search results, here's what I found about LoRA and catastrophic forgetting in vision-language models:

## Overview

While parameter-efficient methods like Low-Rank Adaptation (LoRA) can avert catastrophic forgetting, their effectiveness relies on the fine-tuning data being sufficiently close to the model's pretrained representations.

## The Core Problem

The main obstacle to use LoRA for few shot fine-tuning is the catastrophic forgetting problem, because the visual language alignment knowledge is important for the generality in few shot learning, whereas low rank adaptation interferes with the most informative direction of the pretrained weight matrix.

## Key Research Solutions

**VLM2VLA Approach**: When actions are represented in natural language, fine-tuning can be done using LoRA, a parameter-efficient method that updates small low-rank weight matrices instead of modifying the full network. The model learns to act without overwriting what it already knows.

**Complementary Subspace LoRA (Comp-LoRA)**: The complementary subspace low rank adaptation (Comp-LoRA) method regularizes the catastrophic forgetting problem in few shot VLM finetuning by optimizing the low rank matrix in the complementary subspace, thus preserving the general vision language alignment ability of VLM when learning the novel few shot information.

**Continual Learning with Model Merging**: Merging demonstrates greater robustness to forgetting and task similarity compared to fine-tuning a single LoRA module, where performance fluctuates between steps.

The research shows that the key to mitigating catastrophic forgetting with LoRA is aligning the fine-tuning data distribution with the VLM's pretrained representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e638c5a7-0689-4e5e-9153-00ddac2496ef",
  "isSidechain": true,
  "promptId": "0e7d6d04-6c83-41f1-ac2d-beed114dd3f9",
  "agentId": "ab102fc4e0ed9c1b2",
  "type": "user",
  "uuid": "f0a43f6b-7aa9-4cc9-a04d-b97a43eca487",
  "sourceToolAssistantUUID": "e638c5a7-0689-4e5e-9153-00ddac2496ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T07:20:19.172Z_

<details><summary>↩ Tool result · `toolu_01BurJTeEiAkZcFkserRiVwK`</summary>

```text
Web search results for query: "two-stage fine-tuning VLM distribution shift SFT reinforcement learning"

Links: [{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/html/2508.16546v1"},{"title":"RL Fine-Tuning Heals OOD Forgetting in SFT","url":"https://arxiv.org/html/2509.12235v2"},{"title":"SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning","url":"https://arxiv.org/html/2506.19767v1"},{"title":"Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning","url":"https://arxiv.org/html/2505.03792"},{"title":"Reason-RFT: Reinforcement Fine-Tuning for Visual ...","url":"https://openreview.net/pdf/65dc0346cca4c6d3ceb0f9fcbf6938b5bb15a527.pdf"},{"title":"Reassessing the Role of Supervised Fine-Tuning: An Empirical Study in VLM Reasoning","url":"https://arxiv.org/html/2512.12690"},{"title":"Tuning Large Multimodal Models for Videos using Reinforcement Learning from AI Feedback","url":"https://arxiv.org/html/2402.03746v3"},{"title":"Fine-tuning LLMs with Reinforcement Learning | by Mehul Jain | Data Science + AI at Microsoft | Medium","url":"https://medium.com/data-science-at-microsoft/fine-tuning-llms-with-reinforcement-learning-ef84fe42d6a6"},{"title":"Improving Vision-Language-Action Model with Online Reinforcement Learning","url":"https://arxiv.org/html/2501.16664v1"},{"title":"Vision-SR1: Self-Rewarding Vision-Language Model via Reasoning Decomposition and Multi-Reward Policy Optimization","url":"https://arxiv.org/html/2508.19652v2"}]

Based on the web search results, I found several recent papers and research on two-stage fine-tuning approaches combining SFT (Supervised Fine-Tuning) and RL (Reinforcement Learning) for VLMs (Vision-Language Models) and LLMs, with focus on distribution shift and out-of-distribution (OOD) generalization:

## Key Findings:

**Two-Stage Fine-Tuning Framework:**

A two-stage offline-to-online fine-tuning process is used to train VLM agents, where before RL, the VLM agent is initialized using SFT on task-specific datasets.

**Distribution Shift and OOD Performance:**

In two-stage post-training, RL primarily serves as memory restoration rather than creation of OOD generalization capability, and RL does not endow fundamentally new capabilities; instead, it plays a restoration role that recovers general competencies compromised by aggressive SFT.

If SFT trains for too long, RL cannot recover the lost ability. This indicates there are critical boundaries to the recovery ability of RL following excessive SFT.

**Spectral Analysis Insights:**

OOD performance degradation and recovery correlate almost entirely with rotations of the singular vectors at the spectrum's extremes, while directional shifts in the extremal components, rather than magnitude shifts, govern model's performance.

**VLM-Specific Applications:**

Reason-RFT is the first two-stage reinforcement fine-tuning framework designed to enhance generalization in visual reasoning tasks, addressing domain shift robustness in VLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b25d22f2-29a5-4da7-9471-a2574c591b49",
  "isSidechain": true,
  "promptId": "0e7d6d04-6c83-41f1-ac2d-beed114dd3f9",
  "agentId": "ab102fc4e0ed9c1b2",
  "type": "user",
  "uuid": "cec252d1-180c-44d8-9ca0-b1dcff475c25",
  "sourceToolAssistantUUID": "b25d22f2-29a5-4da7-9471-a2574c591b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T07:20:19.413Z_

<details><summary>↩ Tool result · `toolu_017gJxtdmtQ636AcCWfS8666`</summary>

```text
Web search results for query: "LoRA rank 64 128 continual learning multimodal forgetting"

Links: [{"title":"GitHub - Christina200/Online-LoRA-official: [WACV 2025] Official implementation of \"Online-LoRA: Task-free Online Continual Learning via Low Rank Adaptation\" by Xiwen Wei, Guihong Li and Radu Marculescu · GitHub","url":"https://github.com/christina200/online-lora-official"},{"title":"GitHub - danbider/lora-tradeoffs: Information and artifacts for \"LoRA Learns Less and Forgets Less\" (TMLR, 2024) · GitHub","url":"https://github.com/danbider/lora-tradeoffs"},{"title":"LoRA Learns Less and Forgets Less","url":"https://arxiv.org/html/2405.09673v1"},{"title":"LoRA Learns Less and Forgets Less | OpenReview","url":"https://openreview.net/forum?id=aloEru2qCG"},{"title":"Adaptive Rank, Reduced Forgetting: Continual Learning with Dynamic Rank-Selective LoRA","url":"https://arxiv.org/html/2412.01004"},{"title":"Dual-LoRA and Quality-Enhanced Pseudo Replay for Multimodal Continual Food Learning","url":"https://arxiv.org/html/2511.13351"},{"title":"Continual Forgetting for Pre-trained Vision Models","url":"https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_Continual_Forgetting_for_Pre-trained_Vision_Models_CVPR_2024_paper.pdf"},{"title":"SMoLoRA: Exploring and Defying Dual Catastrophic Forgetting in Continual","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_SMoLoRA_Exploring_and_Defying_Dual_Catastrophic_Forgetting_in_Continual_Visual_ICCV_2025_paper.pdf"},{"title":"Examining Forgetting in Continual Pre-training of Aligned Large Language Models","url":"https://arxiv.org/html/2401.03129v1"},{"title":"(PDF) Adaptive Rank, Reduced Forgetting: Knowledge Retention in Continual Learning Vision-Language Models with Dynamic Rank-Selective LoRA","url":"https://www.researchgate.net/publication/386374822_Adaptive_Rank_Reduced_Forgetting_Knowledge_Retention_in_Continual_Learning_Vision-Language_Models_with_Dynamic_Rank-Selective_LoRA"}]

I found several relevant research papers and implementations related to LoRA rank settings (64, 128), continual learning, multimodal models, and catastrophic forgetting. Here's a summary of the key findings:

## Key Research Findings:

### LoRA Rank and Forgetting Trade-offs

Research on continual low-rank learning shows that higher-rank LoRA improves task learning (plasticity) but increases forgetting, while lower-rank LoRA reduces forgetting (stability).

### Learning vs. Forgetting Comparison

In standard low-rank settings, LoRA substantially underperforms full finetuning, but LoRA better maintains the base model's performance on tasks outside the target domain and mitigates forgetting more than common regularization techniques such as weight decay and dropout.

### Multimodal Continual Learning Approaches

Recent work on multimodal models includes:

- A Dual-LoRA framework integrated with Quality-Enhanced Pseudo Replay, introducing complementary low-rank adapters for each task: a specialized LoRA that learns task-specific knowledge with orthogonal constraints, and a cooperative LoRA that consolidates shared knowledge

- SMoLoRA for continual vision-instruction tuning, which uses a separable routing strategy to select the most suitable LoRA blocks for the current input, preventing interference between dissimilar tasks

### Continual Learning Implementations

Online-LoRA (WACV 2025) is a framework for task-free online continual learning that allows fine-tuning pre-trained Vision Transformer models in real-time, featuring a novel online weight regularization strategy to identify and consolidate important model parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c563cd5-6ec8-46af-9564-1394aa4f841d",
  "isSidechain": true,
  "promptId": "0e7d6d04-6c83-41f1-ac2d-beed114dd3f9",
  "agentId": "ab102fc4e0ed9c1b2",
  "type": "user",
  "uuid": "d2249291-17d7-4303-aab2-161d89387296",
  "sourceToolAssistantUUID": "7c563cd5-6ec8-46af-9564-1394aa4f841d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T07:20:19.839Z_

<details><summary>↩ Tool result · `toolu_016HdbosHn7LDiyFrqJDtfi6`</summary>

```text
Web search results for query: "GRPO training recovery from first stage fine-tuning drift"

Links: [{"title":"A Practical Guide to Fine-Tuning Language Models with GRPO","url":"https://community.cloudera.com/t5/Community-Articles/A-Practical-Guide-to-Fine-Tuning-Language-Models-with-GRPO/ta-p/411583"},{"title":"GRPO Fine-Tuning on GPU Cloud: Train Reasoning Models with Verifiable Rewards (2026 Guide) | Spheron Blog","url":"https://www.spheron.network/blog/grpo-fine-tuning-gpu-cloud/"},{"title":"Practical Exercise: Fine-tune a model with GRPO - Hugging Face LLM Course","url":"https://huggingface.co/learn/llm-course/en/chapter12/5"},{"title":"Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning","url":"https://arxiv.org/html/2510.04072"},{"title":"Reinforcement Fine-tuning (GRPO) | Predibase","url":"https://docs.predibase.com/user-guide/fine-tuning/grpo"},{"title":"GitHub - ksm26/Reinforcement-Fine-Tuning-LLMs-with-GRPO: The course teaches how to fine-tune LLMs using Group Relative Policy Optimization (GRPO)—a reinforcement learning method that improves model reasoning with minimal data. Learn RFT concepts, reward design, LLM-as-a-judge evaluation, and deploy jobs on the Predibase platform.","url":"https://github.com/ksm26/Reinforcement-Fine-Tuning-LLMs-with-GRPO"},{"title":"A Coding Guide on LLM Post Training with TRL from Supervised Fine Tuning to DPO and GRPO Reasoning - MarkTechPost","url":"https://www.marktechpost.com/2026/05/01/a-coding-guide-on-llm-post-training-with-trl-from-supervised-fine-tuning-to-dpo-and-grpo-reasoning/"},{"title":"Fine-tuning SmolLM with Group Relative Policy Optimization (GRPO) by following the Methodologies","url":"https://huggingface.co/blog/prithivMLmods/smollm-grpo-ft"},{"title":"Fine-Tuning LLMs: A Look at Group Relative Policy Optimization (GRPO) | by Anirudh Gokulaprasad | Medium","url":"https://medium.com/@g.anirudh15/fine-tuning-llms-a-look-at-group-relative-policy-optimization-grpo-8240cac48ebc"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"}]

Based on the search results, I found relevant information about GRPO training and recovery from training drift. Here are the key findings:

## Policy Drift in GRPO Training

Increasing beta (the KL penalty coefficient) from 0.04 to 0.08 counterintuitively increases the KL penalty and slows policy drift. This is a practical technique for controlling how far the model deviates from its reference policy during training.

## Addressing Early Training Instability

Research on improving GRPO reveals that GRPO inherits structural inefficiencies that make training fragile, particularly during early stages when rollouts are weak or uninformative, as stochastic rewards induce high-variance gradients that destabilize updates.

To address this, Slow-Fast Policy Optimization (SFPO) is an enhancement to GRPO that restructures each training step into three coordinated stages: fast—multiple inner updates on the same batch to stabilize the search direction; reposition—interpolation back toward the starting point to control off-policy drift; and slow—an extra gradient correction to align with local curvature.

## First-Stage Fine-Tuning

DeepSeek-R1 added a short cold-start SFT (supervised fine-tuning) phase first to stabilize early training, then applied GRPO on top. This approach demonstrates that starting with supervised fine-tuning can help stabilize subsequent GRPO training by providing a more informative initial policy.

These techniques collectively address the challenge of maintaining training stability and preventing excessive policy drift during GRPO-based fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1f353c2-102f-4f65-b0dc-f563e56b12f2",
  "isSidechain": true,
  "promptId": "0e7d6d04-6c83-41f1-ac2d-beed114dd3f9",
  "agentId": "ab102fc4e0ed9c1b2",
  "type": "user",
  "uuid": "d241530b-5b7b-4f53-85e1-0ef0e17a9e21",
  "sourceToolAssistantUUID": "b1f353c2-102f-4f65-b0dc-f563e56b12f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T07:20:20.800Z_

<details><summary>↩ Tool result · `toolu_0164ftidrsDUhV7cdo5zGKco`</summary>

```text
Web search results for query: "detecting mitigating catastrophic forgetting fine-tuned language models"

Links: [{"title":"Understanding Catastrophic Forgetting in Language Models via Implicit Inference | OpenReview","url":"https://openreview.net/forum?id=VrHiF2hsrm"},{"title":"[2308.08747] An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning","url":"https://arxiv.org/abs/2308.08747"},{"title":"Mechanistic Analysis of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning","url":"https://arxiv.org/html/2601.18699v1"},{"title":"How to Alleviate Catastrophic Forgetting in LLMs Finetuning? Hierarchical Layer-Wise and Element-Wise Regularization","url":"https://arxiv.org/html/2501.13669v2"},{"title":"Revisiting Catastrophic Forgetting in Large Language Model Tuning - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.249/"},{"title":"How to prevent catastrophic forgetting in fine tuned large language models? - Beginners - Hugging Face Forums","url":"https://discuss.huggingface.co/t/how-to-prevent-catastrophic-forgetting-in-fine-tuned-large-language-models/135153"},{"title":"Mitigating Catastrophic Forgetting in Large Language Models with Forgetting-aware Pruning | OpenReview","url":"https://openreview.net/forum?id=fHvh913U1H"},{"title":"Fine-Tuning LLMs: Overcoming Catastrophic Forgetting","url":"https://www.legionintel.com/blog/navigating-the-challenges-of-fine-tuning-and-catastrophic-forgetting"},{"title":"Mitigating Catastrophic Forgetting in Large Language Models with Forgetting-aware Pruning - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1108/"},{"title":"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning","url":"https://arxiv.org/html/2308.08747v4"}]

I've found comprehensive research on detecting and mitigating catastrophic forgetting in fine-tuned language models. Here are the key findings:

## Understanding Catastrophic Forgetting

Catastrophic Forgetting (CF) means models forgetting previously acquired knowledge when learning new data. Catastrophic forgetting is generally observed in LLMs ranging from 1b to 7b parameters.

## Detection Methods

Recent research has identified specific mechanistic signatures for detecting forgetting:

Landscape flattening preceded behavioral forgetting by 1 to 2 epochs. Curvature metrics began decreasing in the first epoch of fine-tuning, while accuracy remained stable, then accelerated in later epochs coinciding with performance degradation. This temporal offset suggests that landscape flattening represents an early mechanistic signature of forgetting processes, detectable before behavioral manifestations.

The degree to which task vectors (i.e., the subtraction of pre-trained weights from the weights fine-tuned on downstream tasks) overlap with pre-trained model parameters is a critical factor for CF. FAPM employs the ratio of the task vector to pre-trained model parameters as a metric to quantify CF.

## Mitigation Strategies

Several approaches have been proposed to mitigate catastrophic forgetting:

1. **Curvature Regularization**: Adding a curvature regularization term to the loss function during fine-tuning, penalizing reductions in Hessian eigenvalues along previous task-relevant directions, reduced forgetting by 34 percent with 12 percent slower convergence on new tasks.

2. **Loss Landscape Flattening**: The direct link between the flatness of the model loss landscape and the extent of CF in the field of LLMs has been revealed, and sharpness-aware minimization can mitigate CF by flattening the loss landscape.

3. **Parameter Importance-Based Approaches**: A novel approach computes the element-wise importance of model parameters crucial for preserving general knowledge during fine-tuning, using a dual-objective optimization strategy with regularization loss based on element-wise parameter importance.

4. **Pruning-Based Methods**: FAPM limits CF to just 0.25% while maintaining 99.67% accuracy on downstream tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b2f8d1b-7b7c-4a45-963d-6bbb42339651",
  "isSidechain": true,
  "promptId": "0e7d6d04-6c83-41f1-ac2d-beed114dd3f9",
  "agentId": "ab102fc4e0ed9c1b2",
  "type": "user",
  "uuid": "7636b2e8-5c8f-44aa-8caa-3350b33a8292",
  "sourceToolAssistantUUID": "6b2f8d1b-7b7c-4a45-963d-6bbb42339651",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T07:20:33.020Z_

Based on the literature search, here's a concise summary addressing the reviewer's catastrophic forgetting concern:

## Key Findings on LoRA Forgetting Severity

**Forgetting is real but controlled**: Research shows LoRA exhibits a learning-forgetting trade-off—higher ranks (like 64–128) improve task plasticity but increase forgetting compared to full fine-tuning. However, LoRA substantially *mitigates* forgetting compared to full fine-tuning on unrelated tasks, making it more stable for continual learning scenarios.

**VLM-specific solutions exist**: Recent work on vision-language models directly addresses your use case:
- **Comp-LoRA** (Complementary Subspace LoRA) reduces forgetting by optimizing in the complementary subspace to preserve vision-language alignment while learning novel tasks
- **SMoLoRA** uses separable routing to prevent task interference in continual VLM tuning
- **Model merging** shows greater robustness to forgetting than single LoRA modules

## Standard Forgetting Detection Practices

The literature identifies early mechanistic signatures before behavioral collapse:
- **Landscape flattening** precedes forgetting by 1–2 epochs; curvature metrics (Hessian eigenvalues) decrease first, then accuracy drops
- **Task vector overlap** with pre-trained parameters is a quantifiable CF metric
- These enable detection before catastrophic performance loss occurs

Mitigation approaches during training:
- Curvature regularization (34% forgetting reduction with ~12% slower convergence)
- Loss landscape flattening via sharpness-aware minimization
- Element-wise parameter importance regularization

## Stage 2 GRPO Recovery Capacity

**Critical finding**: Research on two-stage SFT→RL pipelines shows that RL functions as **memory restoration, not capability creation**. The recovery ability has hard limits:
- If Stage 1 SFT is excessive, Stage 2 RL cannot fully recover lost base model competencies
- OOD performance degradation/recovery correlates with singular vector rotations (extremal spectral components), not magnitude changes
- **DeepSeek-R1's approach**: Use brief SFT to stabilize, then apply GRPO—this is validated in practice

For your 50K→28K pipeline, the risk is real if Stage 1 is too aggressive, but GRPO can partially recover if the distribution shift isn't extreme. Detection via early curvature monitoring (before accuracy drops) is recommended.

---

**Sources:**
- [Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting](https://arxiv.org/pdf/2509.22195)
- [Complementary Subspace Low-Rank Adaptation of Vision-Language Models](https://arxiv.org/pdf/2501.15040)
- [LoRA Learns Less and Forgets Less](https://arxiv.org/html/2405.09673v1)
- [SMoLoRA: Exploring and Defying Dual Catastrophic Forgetting](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_SMoLoRA_Exploring_and_Defying_Dual_Catastrophic_Forgetting_in_Continual_Visual_ICCV_2025_paper.pdf)
- [RL Fine-Tuning Heals OOD Forgetting in SFT](https://arxiv.org/html/2509.12235v2)
- [Mechanistic Analysis of Catastrophic Forgetting in Large Language Models](https://arxiv.org/html/2601.18699v1)
- [Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning](https://arxiv.org/html/2510.04072)
- [An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning](https://arxiv.org/html/2308.08747v4)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7636b2e8-5c8f-44aa-8caa-3350b33a8292",
  "isSidechain": true,
  "agentId": "ab102fc4e0ed9c1b2",
  "requestId": "req_011CatUysbCsSabcUcVB633D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "afb360a8-e5ee-4f40-96bf-8187c8dbc341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f99a2d84-938f-4352-9c87-e776deebfbd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014yi2rwfqN7MvDcmFCbcHnN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6331,
      "cache_read_input_tokens": 16831,
      "output_tokens": 944,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6331
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 944,
          "cache_read_input_tokens": 16831,
          "cache_creation_input_tokens": 6331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6331,
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
