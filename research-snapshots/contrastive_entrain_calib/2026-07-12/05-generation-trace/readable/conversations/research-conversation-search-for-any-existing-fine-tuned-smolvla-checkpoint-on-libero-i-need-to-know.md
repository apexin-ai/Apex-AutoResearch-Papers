# Research conversation: Search for any existing fine-tuned SmolVLA checkpoint on LIBERO. I need to know: 1. Does a model like `lerobot/smolvla_l

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a075377ac0fc8921a.jsonl`
- **Structured JSON:** [`28fb7cde195ec9919613.json`](../../sessions/28/28fb7cde195ec9919613.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-15T14:54:15.859Z_

Search for any existing fine-tuned SmolVLA checkpoint on LIBERO. I need to know:

1. Does a model like `lerobot/smolvla_libero` or similar exist on HuggingFace?
2. What LIBERO-related datasets exist under the `lerobot` org on HuggingFace?
3. What is the standard LeRobot training command (`lerobot-train`) for SmolVLA?

Search these locations:
- WebSearch: "smolvla libero huggingface"
- WebSearch: "lerobot-train smolvla" 
- WebSearch: "lerobot libero fine-tune"
- Check if there's a LeRobot config for LIBERO training

Report what you find, including exact HF model IDs if any exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "63ab922e-8443-4e5d-8177-dfa5a9d4b25b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-15T14:54:17.312Z_

I'll search for information about SmolVLA on LIBERO and LeRobot fine-tuning. Let me conduct these searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63ab922e-8443-4e5d-8177-dfa5a9d4b25b",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4Ye4Xiu4kpgTyhmWjAi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6b0953df-f6be-41e5-8424-51538c1241f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q5CWtudKJD4Tu1x5hhUCWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32224,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32224,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T14:54:17.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V4KLnCEQWFYBuaoAb3CJuY`</summary>

```json
{
  "query": "smolvla libero huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b0953df-f6be-41e5-8424-51538c1241f9",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4Ye4Xiu4kpgTyhmWjAi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a65c19ca-32b5-413c-8634-110dcf89e1de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q5CWtudKJD4Tu1x5hhUCWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32224,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32224,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T14:54:17.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MAH9CGVRufPgPmPWoAA5Ba`</summary>

```json
{
  "query": "lerobot-train smolvla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a65c19ca-32b5-413c-8634-110dcf89e1de",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4Ye4Xiu4kpgTyhmWjAi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5c1e3a7c-77ce-4234-8689-ef5e33e098c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q5CWtudKJD4Tu1x5hhUCWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32224,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32224,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T14:54:17.742Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHwLWwFMLNJe83TBi3YhKF`</summary>

```json
{
  "query": "lerobot libero fine-tune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c1e3a7c-77ce-4234-8689-ef5e33e098c1",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4Ye4Xiu4kpgTyhmWjAi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fbca18ac-756e-4d50-8772-c77baa599b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q5CWtudKJD4Tu1x5hhUCWa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32224,
      "cache_read_input_tokens": 0,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 223,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 32224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32224,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T14:54:17.770Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0113EuoBWeYLBKTDBptbhwDx`</summary>

```json
{
  "query": "LeRobot SmolVLA LIBERO benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbca18ac-756e-4d50-8772-c77baa599b45",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4Ye4Xiu4kpgTyhmWjAi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "586b12fe-8395-4c40-aa8a-9be6562b2fa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q5CWtudKJD4Tu1x5hhUCWa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32224,
      "cache_read_input_tokens": 0,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 223,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 32224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32224,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T14:54:23.542Z_

<details><summary>↩ Tool result · `toolu_01V4KLnCEQWFYBuaoAb3CJuY`</summary>

```text
Web search results for query: "smolvla libero huggingface"

Links: [{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"irisWU23/smolVLA_libero · Hugging Face","url":"https://huggingface.co/irisWU23/smolVLA_libero"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"The performance of SmolVLA on LIBERO cannot be replicated · Issue #1369 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1369"},{"title":"bicmol/smolvla-libero · Hugging Face","url":"https://huggingface.co/bicmol/smolvla-libero"},{"title":"Hugging Face Releases SmolVLA, a Compact Open-Source Robotics Model -- Pure AI","url":"https://pureai.com/articles/2025/06/10/hugging-face-releases-smolvla.aspx"}]

Based on the search results, here's what I found about SmolVLA Libero on Hugging Face:

## Overview

SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. SmolVLA is Hugging Face's lightweight foundation model for robotics, designed for easy fine-tuning on LeRobot datasets.

## Performance on LIBERO

SmolVLA-450M outperforms much larger VLAs and strong baselines such as ACT on simulation (LIBERO, Meta-World) and real-world tasks (SO100, SO101). Despite its relatively small size and modest training data — fewer than 30,000 episodes — SmolVLA matches or outperforms larger models like ACT on both simulated (LIBERO, Meta-World) and real-world (SO100, SO101) benchmarks.

## LIBERO Dataset

Smol-LIBERO is a compact version of the LIBERO benchmark, built to make experimentation fast and accessible, containing just 1.79 GB (compared to ~34 GB for the full LIBERO), with fewer trajectories and cameras while keeping the same multimodal structure.

## Technical Details

The policy has been trained and pushed to the Hub using LeRobot. You can access the SmolVLA Libero model directly on Hugging Face at the HuggingFaceVLA/smolvla_libero repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a65c19ca-32b5-413c-8634-110dcf89e1de",
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "4eff9562-151d-4b03-a89f-90cf83e6dfda",
  "sourceToolAssistantUUID": "a65c19ca-32b5-413c-8634-110dcf89e1de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T14:54:24.090Z_

<details><summary>↩ Tool result · `toolu_01MAH9CGVRufPgPmPWoAA5Ba`</summary>

```text
Web search results for query: "lerobot-train smolvla"

Links: [{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"Training SmolVLA with LeRobot Notebook - Colab - Google","url":"https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"LeRobot datasets and training | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"GitHub - huggingface/VLAb · GitHub","url":"https://github.com/huggingface/VLAb"}]

Based on the search results, here's what I found about `lerobot-train` and SmolVLA:

## Overview

LeRobot is a platform designed to make real-world robotics more accessible for everyone, providing pre-trained models, datasets, and tools in PyTorch, and focusing on state-of-the-art approaches in imitation learning and reinforcement learning.

## SmolVLA

SmolVLA is a 450M parameter, open-source Vision-Language-Action (VLA) model from Hugging Face's LeRobot team. It's designed to run efficiently on consumer hardware by using several clever tricks, such as skipping layers in its Vision-Language Model (VLM) backbone and using asynchronous inference to compute the next action while the current one is still executing.

## Training with lerobot-train

The `lerobot-train` command is used to train SmolVLA models. An example training command includes specifying the policy path, dataset repository ID, batch size, number of steps, output directory, job name, device, and whether to enable WandB logging.

A typical training command fine-tunes the base SmolVLA model on a "pick and place" dataset with parameters like batch_size=256, steps=30000, and save_freq=5000.

All training data used in SmolVLA comes from LeRobot Community Datasets, robotics datasets shared on the Hugging Face Hub under the lerobot tag, collected in diverse settings from labs to living rooms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c1e3a7c-77ce-4234-8689-ef5e33e098c1",
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "c3365331-669d-46cc-a6cb-e13becc38313",
  "sourceToolAssistantUUID": "5c1e3a7c-77ce-4234-8689-ef5e33e098c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T14:54:25.250Z_

<details><summary>↩ Tool result · `toolu_01LHwLWwFMLNJe83TBi3YhKF`</summary>

```text
Web search results for query: "lerobot libero fine-tune"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"},{"title":"lerobot/pi05_libero_finetuned_v044 · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned_v044"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task","url":"https://huggingface.co/docs/lerobot/en/xvla"},{"title":"lerobot/docs/source/libero.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"},{"title":"lerobot/pi05_libero_finetuned_quantiles_v044 · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned_quantiles_v044"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"fine tune SmolVLA in libero with tensor shape mismatch · Issue #2418 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2418"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"}]

Based on the search results, here's what I found about LeRobot LIBERO fine-tuning:

## Overview

LeRobot reproduces the results of π₀.₅ on the LIBERO benchmark. The Physical Intelligence LIBERO base model (pi05_libero) is finetuned for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset.

## Available Fine-tuned Models

The finetuned model can be found as: π₀.₅ LIBERO: lerobot/pi05_libero_finetuned. There are also variants with different normalization approaches.

## Fine-tuning Process

LeRobot defines how to process raw LIBERO data from the LeRobot dataset for training, with TrainConfig defining fine-tuning hyperparameters, data config, and weight loader. Before running training, normalization statistics for the training data need to be computed.

## Training Command

For custom fine-tuning, users can run commands like:
lerobot-train with parameters including --dataset.repo_id, --output_dir, --policy.path, --policy.dtype=bfloat16, --steps, and --batch_size

The framework also supports fine-tuning other models on LIBERO tasks, such as SmolVLA, with similar training pipelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbca18ac-756e-4d50-8772-c77baa599b45",
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "0784fcf7-be2d-4f9a-add3-c1dd25dac0ae",
  "sourceToolAssistantUUID": "fbca18ac-756e-4d50-8772-c77baa599b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T14:54:25.923Z_

<details><summary>↩ Tool result · `toolu_0113EuoBWeYLBKTDBptbhwDx`</summary>

```text
Web search results for query: "LeRobot SmolVLA LIBERO benchmark"

Links: [{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"The performance of SmolVLA on LIBERO cannot be replicated · Issue #1369 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1369"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"}]

Based on the search results, here's what I found about LeRobot SmolVLA and the LIBERO benchmark:

## SmolVLA Overview

SmolVLA is a lightweight Vision-Language-Action model that was evaluated using the LIBERO benchmark through the LeRobot framework. At only 450 million parameters, it's an order of magnitude smaller than frontier robotics models (which can exceed 5–7 billion parameters), meaning it can run on consumer hardware without needing to rent expensive GPU clusters.

## LIBERO Benchmark

The LIBERO benchmark covers 130 tasks, ranging from simple object manipulations to complex multi-step scenarios, and is meant to grow over time to serve as a shared benchmark where the community can test and improve lifelong learning algorithms.

LIBERO assesses diverse visuomotor skills across four categories–Spatial, Object, Goal, and Long–with 10 tasks per category (40 total).

## SmolVLA Performance

The 0.45B model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3%. SmolVLA outperforms other VLA-based approaches such as Octo and OpenVLA, as well as the diffusion policy baseline across both LIBERO and Meta-World.

## Integration with LeRobot

LIBERO is now part of LeRobot's multi-eval supported simulation, meaning you can benchmark your policies either on a single suite of tasks or across multiple suites at once with just a flag.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "586b12fe-8395-4c40-aa8a-9be6562b2fa7",
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "0a35af1b-994b-43f4-a8c1-b5942f24979d",
  "sourceToolAssistantUUID": "586b12fe-8395-4c40-aa8a-9be6562b2fa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T14:54:27.456Z_

Excellent! I found comprehensive information. Let me get more specific details on the exact model IDs and training configs by checking the documentation links.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a35af1b-994b-43f4-a8c1-b5942f24979d",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4YeoUPGxL18p49Npm4s",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b9db265-1b52-4bb4-91ed-a96f9d2ad110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012UxMLLY6m8Uw8ZfRVC3TbL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4636,
      "cache_read_input_tokens": 32224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4636,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T14:54:28.101Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013VWMwUHE2fXMCTcvQU7u8R`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/smolvla",
  "prompt": "What is the exact lerobot-train command for SmolVLA? What are the standard training hyperparameters?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b9db265-1b52-4bb4-91ed-a96f9d2ad110",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4YeoUPGxL18p49Npm4s",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6d71a179-2cbe-4803-9818-514f43ab2c25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012UxMLLY6m8Uw8ZfRVC3TbL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4636,
      "cache_read_input_tokens": 32224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4636,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T14:54:28.598Z_

<details><summary>↩ Tool result · `toolu_013VWMwUHE2fXMCTcvQU7u8R`</summary>

````text
# SmolVLA

SmolVLA is Hugging Face’s lightweight foundation model for robotics. Designed for easy fine-tuning on LeRobot datasets, it helps accelerate your development!

  
  
  
    Figure 1. SmolVLA takes as input (i) multiple cameras views, (ii) the
    robot’s current sensorimotor state, and (iii) a natural language
    instruction, encoded into contextual features used to condition the action
    expert when generating an action chunk.
  

## Set Up Your Environment

1. Install LeRobot by following our [Installation Guide](./installation).
2. Install SmolVLA dependencies by running:

   ```bash
   pip install -e ".[smolvla]"
   ```

## Collect a dataset

SmolVLA is a base model, so fine-tuning on your own data is required for optimal performance in your setup.
We recommend recording ~50 episodes of your task as a starting point. Follow our guide to get started: [Recording a Dataset](./il_robots)

In your dataset, make sure to have enough demonstrations per each variation (e.g. the cube position on the table if it is cube pick-place task) you are introducing.

We recommend checking out the dataset linked below for reference that was used in the [SmolVLA paper](https://huggingface.co/papers/2506.01844):

🔗 [SVLA SO100 PickPlace](https://huggingface.co/spaces/lerobot/visualize_dataset?path=%2Flerobot%2Fsvla_so100_pickplace%2Fepisode_0)

In this dataset, we recorded 50 episodes across 5 distinct cube positions. For each position, we collected 10 episodes of pick-and-place interactions. This structure, repeating each variation several times, helped the model generalize better. We tried similar dataset with 25 episodes, and it was not enough leading to a bad performance. So, the data quality and quantity is definitely a key.
After you have your dataset available on the Hub, you are good to go to use our finetuning script to adapt SmolVLA to your application.

## Finetune SmolVLA on your data

Use [`smolvla_base`](https://hf.co/lerobot/smolvla_base), our pretrained 450M model, and fine-tune it on your data.
Training the model for 20k steps will roughly take ~4 hrs on a single A100 GPU. You should tune the number of steps based on performance and your use-case.

If you don't have a gpu device, you can train using our notebook on [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb)

Pass your dataset to the training script using `--dataset.repo_id`. If you want to test your installation, run the following command where we use one of the datasets we collected for the [SmolVLA Paper](https://huggingface.co/papers/2506.01844).

```bash
cd lerobot && lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --job_name=my_smolvla_training \
  --policy.device=cuda \
  --wandb.enable=true
```

  You can start with a small batch size and increase it incrementally, if the
  GPU allows it, as long as loading times remain short.

Fine-tuning is an art. For a complete overview of the options for finetuning, run

```bash
lerobot-train --help
```

  
  
  
    Figure 2: Comparison of SmolVLA across task variations. From left to right:
    (1) pick-place cube counting, (2) pick-place cube counting, (3) pick-place
    cube counting under perturbations, and (4) generalization on pick-and-place
    of the lego block with real-world SO101.
  

## Evaluate the finetuned model and run it in real-time

Similarly for when recording an episode, it is recommended that you are logged in to the HuggingFace Hub. You can follow the corresponding steps: [Record a dataset](./il_robots).
Once you are logged in, you can run inference in your setup by doing:

```bash
lerobot-record \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM0 \ # <- Use your port
  --robot.id=my_blue_follower_arm \ # <- Use your robot id
  --robot.cameras="{ front: {type: opencv, index_or_path: 8, width: 640, height: 480, fps: 30}}" \ # <- Use your cameras
  --dataset.single_task="Grasp a lego block and put it in the bin." \ # <- Use the same task description you used in your dataset recording
  --dataset.repo_id=${HF_USER}/eval_DATASET_NAME_test \  # <- This will be the dataset name on HF Hub
  --dataset.episode_time_s=50 \
  --dataset.num_episodes=10 \
  --dataset.streaming_encoding=true \
  --dataset.encoder_threads=2 \
  # --dataset.vcodec=auto \
  # <- Teleop optional if you want to teleoperate in between episodes \
  # --teleop.type=so100_leader \
  # --teleop.port=/dev/ttyACM0 \
  # --teleop.id=my_red_leader_arm \
  --policy.path=HF_USER/FINETUNE_MODEL_NAME # <- Use your fine-tuned model
```

Depending on your evaluation setup, you can configure the duration and the number of episodes to record for your evaluation suite.


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d71a179-2cbe-4803-9818-514f43ab2c25",
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "c64f173d-6bf1-40bd-8113-2f52422a9cd0",
  "sourceToolAssistantUUID": "6d71a179-2cbe-4803-9818-514f43ab2c25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T14:54:28.711Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XJ4oTpgkFp4AcgfeRrytnH`</summary>

```json
{
  "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero",
  "prompt": "What is the exact model ID and what configuration was used to train this SmolVLA on LIBERO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c64f173d-6bf1-40bd-8113-2f52422a9cd0",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4YeoUPGxL18p49Npm4s",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b5a01e11-ea7a-451d-911b-b39f36d155c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012UxMLLY6m8Uw8ZfRVC3TbL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4636,
      "cache_read_input_tokens": 32224,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4636
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 242,
          "cache_read_input_tokens": 32224,
          "cache_creation_input_tokens": 4636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4636,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T14:54:32.555Z_

<details><summary>↩ Tool result · `toolu_01XJ4oTpgkFp4AcgfeRrytnH`</summary>

````text
# SmolVLA LIBERO Model Information

## Model ID
**HuggingFaceVLA/smolvla_libero**

## Base Model
This model is a fine-tuned version of: **lerobot/smolvla_base**

## Training Configuration

Based on the documentation provided, here's the training setup used:

```python
python lerobot/scripts/train.py \
  --policy.path=HuggingFaceVLA/smolvla_libero \
  --dataset.repo_id=lerobot/svla_so101_pickplace \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --job_name=my_smolvla_training \
  --policy.device=cuda \
  --wandb.enable=true
```

## Key Details
- **Framework**: LeRobot
- **License**: Apache 2.0
- **Training Dataset**: LIBERO dataset (specifically referenced as `svla_so101_pickplace`)
- **Batch Size**: 64
- **Training Steps**: 20,000
- **Device**: CUDA

## Model Type
- **Architecture**: Vision-Language-Action (VLA) model
- **Focus**: Compact and efficient robotics model deployable on consumer-grade hardware
- **Paper**: arXiv 2506.01844 (SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics)

The model was trained and pushed to the Hugging Face Hub using the LeRobot framework, as noted in the model card.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5a01e11-ea7a-451d-911b-b39f36d155c5",
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "f305bee2-6e52-4f56-bb8a-76c3b1d0ed5b",
  "sourceToolAssistantUUID": "b5a01e11-ea7a-451d-911b-b39f36d155c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-15T14:54:34.876Z_

Perfect! Now let me check for the LIBERO datasets available under the lerobot org.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f305bee2-6e52-4f56-bb8a-76c3b1d0ed5b",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4YfHrScUbeHuXcU7Zb1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99d000c7-3a33-487e-89c7-023c40823532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RKVCQAZQ43V7gNHcpaiv1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2163,
      "cache_read_input_tokens": 36860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2163,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T14:54:35.148Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2sJMWXwcL3pQPWw7S8sWy`</summary>

```json
{
  "query": "site:huggingface.co/datasets/lerobot libero"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99d000c7-3a33-487e-89c7-023c40823532",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4YfHrScUbeHuXcU7Zb1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c6eab29e-0dbb-4a32-934a-e68c7aaebfe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RKVCQAZQ43V7gNHcpaiv1t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2163,
      "cache_read_input_tokens": 36860,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2163
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 88,
          "cache_read_input_tokens": 36860,
          "cache_creation_input_tokens": 2163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2163,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T14:54:38.895Z_

<details><summary>↩ Tool result · `toolu_01R2sJMWXwcL3pQPWw7S8sWy`</summary>

```text
Web search results for query: "site:huggingface.co/datasets/lerobot libero"

Links: [{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/libero_spatial_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_spatial_image"},{"title":"Commits · lerobot/libero_goal_image","url":"https://huggingface.co/datasets/lerobot/libero_goal_image/commits/main"},{"title":"lerobot/svla_so100_pickplace · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/svla_so100_pickplace"},{"title":"lerobot/xarm_lift_medium at main","url":"https://huggingface.co/datasets/lerobot/xarm_lift_medium/tree/main"},{"title":"lerobot/aloha_sim_insertion_scripted at main","url":"https://huggingface.co/datasets/lerobot/aloha_sim_insertion_scripted/tree/main"},{"title":"lerobot/config_examples · add_configs","url":"https://huggingface.co/datasets/lerobot/config_examples/discussions/1/files"},{"title":"lerobot/svla_so101_pickplace · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/svla_so101_pickplace"}]

I found several results related to your search. The primary result is the main LIBERO dataset repository at Hugging Face. Here are the search results:

**Main Results:**

1. **lerobot/libero** - https://huggingface.co/datasets/lerobot/libero

2. **Related LIBERO variants:**
   - lerobot/libero_object_image - https://huggingface.co/datasets/lerobot/libero_object_image
   - lerobot/libero_10_image - https://huggingface.co/datasets/lerobot/libero_10_image
   - lerobot/libero_spatial_image - https://huggingface.co/datasets/lerobot/libero_spatial_image
   - lerobot/libero_goal_image - https://huggingface.co/datasets/lerobot/libero_goal_image

The search results indicate these are datasets hosted on Hugging Face under the LeRobot organization. The main dataset page and its variants appear to be available, though the page content in the search results only shows the general Hugging Face mission statement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6eab29e-0dbb-4a32-934a-e68c7aaebfe7",
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "3a2fde11-473c-45ed-a840-de43d1923ee5",
  "sourceToolAssistantUUID": "c6eab29e-0dbb-4a32-934a-e68c7aaebfe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T14:54:40.496Z_

Excellent! Let me fetch more details on the LIBERO dataset configurations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a2fde11-473c-45ed-a840-de43d1923ee5",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4YfkrtzRiczG8eH3NtM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "711f9cb7-2957-4cd9-a1bf-6150fec8859f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KQambVKw9TAHms6m5jcDJC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 39023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 881,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T14:54:40.921Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D7bGSN2grZS57a7JdqoSGP`</summary>

```json
{
  "url": "https://huggingface.co/datasets/lerobot/libero",
  "prompt": "What are the dataset details, size, and how is it structured?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "711f9cb7-2957-4cd9-a1bf-6150fec8859f",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4YfkrtzRiczG8eH3NtM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ebacef43-ab83-4c6a-aadd-1e537237a793",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KQambVKw9TAHms6m5jcDJC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 39023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 881,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T14:54:41.578Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019RFVEvSEbtKErBBuYps3k5`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/libero",
  "prompt": "What is the standard lerobot-train command for LIBERO? What hyperparameters are recommended?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebacef43-ab83-4c6a-aadd-1e537237a793",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4YfkrtzRiczG8eH3NtM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7b4d646-e86e-407f-8f94-e815f17a7f01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KQambVKw9TAHms6m5jcDJC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 39023,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 881
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 207,
          "cache_read_input_tokens": 39023,
          "cache_creation_input_tokens": 881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 881,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T14:54:41.982Z_

<details><summary>↩ Tool result · `toolu_019RFVEvSEbtKErBBuYps3k5`</summary>

````text
# LIBERO

LIBERO is a benchmark designed to study **lifelong robot learning** — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on **knowledge transfer**: how well a robot can apply what it has already learned to new situations. By evaluating on LIBERO, different algorithms can be compared fairly and researchers can build on each other's work.

- Paper: [Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)
- GitHub: [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
- Project website: [libero-project.github.io](https://libero-project.github.io)

![An overview of the LIBERO benchmark](https://libero-project.github.io/assets/img/libero/fig1.png)

## Available tasks

LIBERO includes **five task suites** covering **130 tasks**, ranging from simple object manipulations to complex multi-step scenarios:

| Suite          | CLI name         | Tasks | Description                                        |
| -------------- | ---------------- | ----- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | Long-horizon tasks from the LIBERO-100 collection  |

## Installation

After following the LeRobot installation instructions:

```bash
pip install -e ".[libero]"
```

LIBERO requires Linux (`sys_platform == 'linux'`). LeRobot uses MuJoCo for simulation — set the rendering backend before training or evaluation:

```bash
export MUJOCO_GL=egl  # for headless servers (HPC, cloud)
```

## Evaluation

### Default evaluation (recommended)

Evaluate across the four standard suites (10 episodes per task):

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

### Single-suite evaluation

Evaluate on one LIBERO suite:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_object \
  --eval.batch_size=2 \
  --eval.n_episodes=3
```

- `--env.task` picks the suite (`libero_object`, `libero_spatial`, etc.).
- `--env.task_ids` restricts to specific task indices (`[0]`, `[1,2,3]`, etc.). Omit to run all tasks in the suite.
- `--eval.batch_size` controls how many environments run in parallel.
- `--eval.n_episodes` sets how many episodes to run per task.

### Multi-suite evaluation

Benchmark a policy across multiple suites at once by passing a comma-separated list:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_object,libero_spatial \
  --eval.batch_size=1 \
  --eval.n_episodes=2
```

### Control mode

LIBERO supports two control modes — `relative` (default) and `absolute`. Different VLA checkpoints are trained with different action parameterizations, so make sure the mode matches your policy:

```bash
--env.control_mode=relative   # or "absolute"
```

### Policy inputs and outputs

**Observations:**

- `observation.state` — 8-dim proprioceptive features (eef position, axis-angle orientation, gripper qpos)
- `observation.images.image` — main camera view (`agentview_image`), HWC uint8
- `observation.images.image2` — wrist camera view (`robot0_eye_in_hand_image`), HWC uint8

  LeRobot enforces the `.images.*` prefix for visual features. Ensure your
  policy config `input_features` use the same naming keys, and that your dataset
  metadata keys follow this convention. If your data contains different keys,
  you must rename the observations to match what the policy expects, since
  naming keys are encoded inside the normalization statistics layer.

**Actions:**

- Continuous control in `Box(-1, 1, shape=(7,))` — 6D end-effector delta + 1D gripper

### Recommended evaluation episodes

For reproducible benchmarking, use **10 episodes per task** across all four standard suites (Spatial, Object, Goal, Long). This gives 400 total episodes and matches the protocol used for published results.

## Training

### Dataset

We provide a preprocessed LIBERO dataset fully compatible with LeRobot:

- [HuggingFaceVLA/libero](https://huggingface.co/datasets/HuggingFaceVLA/libero)

For reference, the original dataset published by Physical Intelligence:

- [physical-intelligence/libero](https://huggingface.co/datasets/physical-intelligence/libero)

### Example training command

```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/libero-test \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --output_dir=./outputs/ \
  --steps=100000 \
  --batch_size=4 \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --eval_freq=1000
```

## Reproducing published results

We reproduce the results of Pi0.5 on the LIBERO benchmark. We take the Physical Intelligence LIBERO base model (`pi05_libero`) and finetune for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the [HuggingFace LIBERO dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero).

The finetuned model: [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned)

### Evaluation command

```bash
lerobot-eval \
  --output_dir=./eval_logs/ \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --policy.path=pi05_libero_finetuned \
  --policy.n_action_steps=10 \
  --env.max_parallel_tasks=1
```

We set `n_action_steps=10`, matching the original OpenPI implementation.

### Results

| Model               | LIBERO Spatial | LIBERO Object | LIBERO Goal | LIBERO 10 | Average  |
| ------------------- | -------------- | ------------- | ----------- | --------- | -------- |
| **Pi0.5 (LeRobot)** | 97.0           | 99.0          | 98.0        | 96.0      | **97.5** |

These results are consistent with the [original results](https://github.com/Physical-Intelligence/openpi/tree/main/examples/libero#results) reported by Physical Intelligence:

| Model              | LIBERO Spatial | LIBERO Object | LIBERO Goal | LIBERO 10 | Average   |
| ------------------ | -------------- | ------------- | ----------- | --------- | --------- |
| **Pi0.5 (OpenPI)** | 98.8           | 98.2          | 98.0        | 92.4      | **96.85** |


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7b4d646-e86e-407f-8f94-e815f17a7f01",
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "8269c10c-40d7-4a9e-8c11-8ca8007c70af",
  "sourceToolAssistantUUID": "c7b4d646-e86e-407f-8f94-e815f17a7f01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T14:54:46.965Z_

<details><summary>↩ Tool result · `toolu_01D7bGSN2grZS57a7JdqoSGP`</summary>

````text
# LeRobot LIBERO Dataset Details

## Overview
The **lerobot/libero** dataset is a robotics dataset containing demonstrations for the LIBERO (Learning from Interleaved Behavior via Engagement in Realistic Observation) benchmark.

## Dataset Size & Scale
- **Total Rows**: 273,465 frames
- **Total Episodes**: 1,693
- **Total Tasks**: 40
- **Total Size**: 1.94 GB
- **Data Files Size**: ~100 MB
- **Video Files Size**: ~500 MB
- **FPS**: 10.0 frames per second

## Structure

### Dataset Format
- **Format**: Parquet (auto-converted)
- **Split**: Single training split covering all 1,693 episodes
- **Robot Type**: Panda
- **Chunks**: Data organized into chunks of 1,000 frames

### Feature Schema

```json
{
  "observation.images.image": {
    "dtype": "video",
    "shape": [256, 256, 3],
    "codec": "av1"
  },
  "observation.images.image2": {
    "dtype": "video",
    "shape": [256, 256, 3],
    "codec": "av1"
  },
  "observation.state": {
    "dtype": "float32",
    "shape": [8]
  },
  "action": {
    "dtype": "float32",
    "shape": [7]
  },
  "timestamp": "float32",
  "frame_index": "int64",
  "episode_index": "int64",
  "index": "int64",
  "task_index": "int64"
}
```

## Data Characteristics
- **Modalities**: Video, Tabular, Time-series
- **Task Category**: Robotics
- **License**: Apache 2.0
- **Libraries**: Datasets, Dask, Polars

The dataset includes state vectors (8-dimensional), 7-dimensional action vectors, and dual RGB camera streams (256×256) recorded at 10 FPS.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebacef43-ab83-4c6a-aadd-1e537237a793",
  "isSidechain": true,
  "promptId": "b1b80eba-cf26-46a4-aa50-d2368788499c",
  "agentId": "a075377ac0fc8921a",
  "type": "user",
  "uuid": "a4084fff-b2e2-44a0-8c60-4fca67eb25bd",
  "sourceToolAssistantUUID": "ebacef43-ab83-4c6a-aadd-1e537237a793",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-15T14:54:57.966Z_

Perfect! Now I have comprehensive information. Let me compile the final report.

## Summary of Findings

Based on my search, here's what exists for SmolVLA on LIBERO:

### 1. **SmolVLA Fine-tuned on LIBERO - Model IDs**

Yes, fine-tuned SmolVLA checkpoints exist:

- **Primary Model**: `HuggingFaceVLA/smolvla_libero` - [https://huggingface.co/HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)
- **Base Model**: `lerobot/smolvla_base` (450M parameters) - [https://huggingface.co/lerobot/smolvla_base](https://huggingface.co/lerobot/smolvla_base)
- **Alternative**: `irisWU23/smolVLA_libero` - [https://huggingface.co/irisWU23/smolVLA_libero](https://huggingface.co/irisWU23/smolVLA_libero)
- **Another variant**: `bicmol/smolvla-libero` - [https://huggingface.co/bicmol/smolvla-libero](https://huggingface.co/bicmol/smolvla-libero)

### 2. **LIBERO-Related Datasets under `lerobot` Organization**

The following LIBERO datasets exist on HuggingFace under the LeRobot org:

- **Main dataset**: `lerobot/libero` (1.94 GB, 1,693 episodes, 40 tasks, 273,465 frames) - [https://huggingface.co/datasets/lerobot/libero](https://huggingface.co/datasets/lerobot/libero)
- **Variant datasets**:
  - `lerobot/libero_object_image` - [https://huggingface.co/datasets/lerobot/libero_object_image](https://huggingface.co/datasets/lerobot/libero_object_image)
  - `lerobot/libero_10_image` - [https://huggingface.co/datasets/lerobot/libero_10_image](https://huggingface.co/datasets/lerobot/libero_10_image)
  - `lerobot/libero_spatial_image` - [https://huggingface.co/datasets/lerobot/libero_spatial_image](https://huggingface.co/datasets/lerobot/libero_spatial_image)
  - `lerobot/libero_goal_image` - [https://huggingface.co/datasets/lerobot/libero_goal_image](https://huggingface.co/datasets/lerobot/libero_goal_image)

**Compact Version**: `HuggingFaceVLA/smol-libero` (1.79 GB, compact for fast experimentation) - [https://huggingface.co/datasets/HuggingFaceVLA/smol-libero](https://huggingface.co/datasets/HuggingFaceVLA/smol-libero)

### 3. **Standard LeRobot Training Commands**

**For SmolVLA fine-tuning** (general):
```bash
cd lerobot && lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=YOUR_DATASET_ID \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --job_name=my_smolvla_training \
  --policy.device=cuda \
  --wandb.enable=true
```

**For SmolVLA on LIBERO** (specific):
```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/libero-test \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --output_dir=./outputs/ \
  --steps=100000 \
  --batch_size=4 \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --eval_freq=1000
```

**Recommended Evaluation Command**:
```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

### Key Details:
- SmolVLA achieves ~87% average success on LIBERO (90% Spatial, 96% Object, 92% Goal, 71% Long)
- Training 20k steps on single A100: ~4 hours
- Base model: 450M parameters (lightweight, runs on consumer hardware)
- SmolVLA outperforms larger models like ACT on both LIBERO and MetaWorld
- Official documentation: [https://huggingface.co/docs/lerobot/en/smolvla](https://huggingface.co/docs/lerobot/en/smolvla)
- LIBERO documentation: [https://huggingface.co/docs/lerobot/libero](https://huggingface.co/docs/lerobot/libero)

Sources:
- [SmolVLA on HuggingFace](https://huggingface.co/HuggingFaceVLA/smolvla_libero)
- [SmolVLA Documentation](https://huggingface.co/docs/lerobot/en/smolvla)
- [LIBERO Benchmark Documentation](https://huggingface.co/docs/lerobot/libero)
- [SmolVLA Blog Post](https://huggingface.co/blog/smolvla)
- [LeRobot GitHub Repository](https://github.com/huggingface/lerobot)
- [LIBERO Dataset](https://huggingface.co/datasets/lerobot/libero)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4084fff-b2e2-44a0-8c60-4fca67eb25bd",
  "isSidechain": true,
  "agentId": "a075377ac0fc8921a",
  "requestId": "req_011Cb4YgMXEAuVhidVqZo2kU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "610d3662-e05c-43ed-bc93-de5d7ffde198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/.claude/sessions/agent_e863954b",
  "sessionId": "181ac6cc-f175-4937-a744-2351866a0034",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-crunching-wozniak",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01STNQ4NEHGNrazDgrgRA8SD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2169,
      "cache_creation_input_tokens": 743,
      "cache_read_input_tokens": 39904,
      "output_tokens": 1613,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 743
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2169,
          "output_tokens": 1613,
          "cache_read_input_tokens": 39904,
          "cache_creation_input_tokens": 743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 743,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
