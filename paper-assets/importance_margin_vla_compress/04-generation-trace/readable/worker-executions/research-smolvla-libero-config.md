# research smolvla libero config

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_research_smolvla_libero_config_20260516T233302.log`
- **Structured JSON:** [`f86377c1e0f8cd4beee3.json`](../../sessions/f8/f86377c1e0f8cd4beee3.json)

## Before a recorded user message

28 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "05c87335-4160-4c33-8bbc-ff9af5e1b4f4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778976600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6a55790c-e0ab-4b7e-94c5-942230c9b277",
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for SmolVLA's official LIBERO training configuration and evaluation protocol to understand why their Full FT 100K achieves ~49% SR on libero_object while SmolVLA reports 87.3%. Let me search for this information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "46c8d7e9-f88f-45c2-bc77-25ed1db6a8bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WphG2RYrbRSQNh8gG9eA9B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12579,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12579
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nzk3717NXCj3JZ2SH2c5Hd`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "96117533-4f35-42c6-9159-f6871dcce5cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WphG2RYrbRSQNh8gG9eA9B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12579,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12579
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T23:33:13.408Z_

<details><summary>↩ Tool result · `toolu_01Nzk3717NXCj3JZ2SH2c5Hd`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "509884be-09a0-4c14-abe2-8e5981a7a961",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me search for SmolVLA paper and its LIBERO training details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "ed395717-5fa8-4988-8447-6c9fa88bc812",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhZ6wUKwhTYwTMV6ETvFW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Le83ZFJcu6xEyDX7ZfxEu8`</summary>

```json
{
  "query": "SmolVLA paper arxiv LIBERO training configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "ba4397f6-f84f-457f-8bc1-da33fac42ae9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhZ6wUKwhTYwTMV6ETvFW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QTuwHB7sX9AiGBpRQnkrwE`</summary>

```json
{
  "query": "lerobot LIBERO fine-tuning config SmolVLA steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "d52fd110-aae4-452d-93a2-327901843769",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhZ6wUKwhTYwTMV6ETvFW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TjierYkx9joUoE7nR9y51z`</summary>

```json
{
  "query": "SmolVLA 87.3 LIBERO success rate evaluation protocol"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "6ddd8d50-4870-4142-83ae-0686f9e2032f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhZ6wUKwhTYwTMV6ETvFW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T23:33:26.985Z_

<details><summary>↩ Tool result · `toolu_01Le83ZFJcu6xEyDX7ZfxEu8`</summary>

```text
Web search results for query: "SmolVLA paper arxiv LIBERO training configuration"

Links: [{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"bicmol/smolvla-libero · Hugging Face","url":"https://huggingface.co/bicmol/smolvla-libero"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors","url":"https://arxiv.org/html/2604.21241"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"}]

I found relevant information about the SmolVLA paper and its LIBERO training configuration. Here are the key findings:

## SmolVLA Paper Overview

SmolVLA is a small, efficient, and community-driven vision-language-action model that drastically reduces both training and inference costs, while retaining competitive performance, designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.

## LIBERO Training Configuration

All ablations are conducted on the LIBERO benchmark. Unless otherwise noted, models are trained from scratch without any pretraining on robotics data. The VLM backbone is frozen, and only the action expert is trained from scratch.

SmolVLA is always trained in a multi-task setting.

## Dataset Details

Each LIBERO dataset contains demonstrations relative to one task, with 10 trajectories for each of 5 distinct starting positions, resulting in a total of 50 demonstrations per dataset.

## Attention Mechanisms

Interleaved cross and self-attention yield the best results, and preventing future action leakage improves performance.

The arXiv paper is available at **arXiv:2506.01844** and was published on June 2, 2025. The paper demonstrates that SmolVLA achieves competitive performance on the LIBERO benchmark despite its smaller size compared to other VLAs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "08069b18-102d-42a9-8b0d-425c291fd3f4",
  "tool_use_result": {
    "query": "SmolVLA paper arxiv LIBERO training configuration",
    "results": [
      {
        "tool_use_id": "srvtoolu_015o82Uxi8Y39rvTpg33E8mL",
        "content": [
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://arxiv.org/abs/2506.01844"
          },
          {
            "title": "Leave No Observation Behind: Real-time Correction for VLA Action Chunks",
            "url": "https://arxiv.org/html/2509.23224v1"
          },
          {
            "title": "lerobot/smolvla_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/smolvla_base"
          },
          {
            "title": "bicmol/smolvla-libero · Hugging Face",
            "url": "https://huggingface.co/bicmol/smolvla-libero"
          },
          {
            "title": "arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model",
            "url": "https://arxiv.org/pdf/2506.01844"
          },
          {
            "title": "VLA-0-Smol",
            "url": "https://robot-learning-collective.github.io/vla-0-smol"
          },
          {
            "title": "CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors",
            "url": "https://arxiv.org/html/2604.21241"
          },
          {
            "title": "Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero"
          }
        ]
      },
      "I found relevant information about the SmolVLA paper and its LIBERO training configuration. Here are the key findings:\n\n## SmolVLA Paper Overview\n\nSmolVLA is a small, efficient, and community-driven vision-language-action model that drastically reduces both training and inference costs, while retaining competitive performance, designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.\n\n## LIBERO Training Configuration\n\nAll ablations are conducted on the LIBERO benchmark. Unless otherwise noted, models are trained from scratch without any pretraining on robotics data. The VLM backbone is frozen, and only the action expert is trained from scratch.\n\nSmolVLA is always trained in a multi-task setting.\n\n## Dataset Details\n\nEach LIBERO dataset contains demonstrations relative to one task, with 10 trajectories for each of 5 distinct starting positions, resulting in a total of 50 demonstrations per dataset.\n\n## Attention Mechanisms\n\nInterleaved cross and self-attention yield the best results, and preventing future action leakage improves performance.\n\nThe arXiv paper is available at **arXiv:2506.01844** and was published on June 2, 2025. The paper demonstrates that SmolVLA achieves competitive performance on the LIBERO benchmark despite its smaller size compared to other VLAs."
    ],
    "durationSeconds": 5.980949492
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T23:33:28.169Z_

<details><summary>↩ Tool result · `toolu_01QTuwHB7sX9AiGBpRQnkrwE`</summary>

```text
Web search results for query: "lerobot LIBERO fine-tuning config SmolVLA steps"

Links: [{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"}]

Based on the search results, here's information about fine-tuning SmolVLA on LIBERO using LeRobot:

## Fine-tuning Configuration

The basic fine-tuning command for SmolVLA on LIBERO uses parameters like `--policy.path=lerobot/smolvla_base`, `--dataset.repo_id=HuggingFaceVLA/libero`, `--env.type=libero`, `--env.task=libero_spatial`, `--steps=100000`, `--batch_size=32`, and `--peft.method_type=LORA` with `--peft.r=64`.

## Training Steps

Training the model for 20k steps will roughly take ~4 hrs on a single A100 GPU, and you should tune the number of steps based on performance and your use-case. However, the configuration example shows `--steps=100000` for more comprehensive fine-tuning.

## PEFT Fine-tuning Details

LoRA (Low-Rank Adapter) is a popular fine-tuning method that only fine-tunes a matrix with comparably low rank instead of the full weight matrix. By default, PEFT will target the q_proj and v_proj layers of the LM expert in SmolVLA and will also target the state and action projection matrices as they are most likely task-dependent.

## Alternative Approaches

For reproducing Physical Intelligence results on LIBERO, one approach involves taking a base model and finetuning for an additional 6k steps in bfloat16 with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "a35956bd-8e2e-46fb-96bc-90650435e029",
  "tool_use_result": {
    "query": "lerobot LIBERO fine-tuning config SmolVLA steps",
    "results": [
      {
        "tool_use_id": "srvtoolu_016keSFufjmBoQasngs1n5wM",
        "content": [
          {
            "title": "Train SmolVLA",
            "url": "https://docs.phospho.ai/learn/train-smolvla"
          },
          {
            "title": "[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1316"
          },
          {
            "title": "lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"
          },
          {
            "title": "SmolVLA · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/en/smolvla"
          },
          {
            "title": "lerobot/smolvla_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/smolvla_base"
          },
          {
            "title": "Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"
          },
          {
            "title": "Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2259"
          },
          {
            "title": "LIBERO · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/libero"
          },
          {
            "title": "SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics",
            "url": "https://smolvla.net/index_en"
          },
          {
            "title": "SmolVLA: Efficient Vision Language Action Model - LeRobot",
            "url": "https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"
          }
        ]
      },
      "Based on the search results, here's information about fine-tuning SmolVLA on LIBERO using LeRobot:\n\n## Fine-tuning Configuration\n\nThe basic fine-tuning command for SmolVLA on LIBERO uses parameters like `--policy.path=lerobot/smolvla_base`, `--dataset.repo_id=HuggingFaceVLA/libero`, `--env.type=libero`, `--env.task=libero_spatial`, `--steps=100000`, `--batch_size=32`, and `--peft.method_type=LORA` with `--peft.r=64`.\n\n## Training Steps\n\nTraining the model for 20k steps will roughly take ~4 hrs on a single A100 GPU, and you should tune the number of steps based on performance and your use-case. However, the configuration example shows `--steps=100000` for more comprehensive fine-tuning.\n\n## PEFT Fine-tuning Details\n\nLoRA (Low-Rank Adapter) is a popular fine-tuning method that only fine-tunes a matrix with comparably low rank instead of the full weight matrix. By default, PEFT will target the q_proj and v_proj layers of the LM expert in SmolVLA and will also target the state and action projection matrices as they are most likely task-dependent.\n\n## Alternative Approaches\n\nFor reproducing Physical Intelligence results on LIBERO, one approach involves taking a base model and finetuning for an additional 6k steps in bfloat16 with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset."
    ],
    "durationSeconds": 6.987741503000001
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T23:33:28.180Z_

<details><summary>↩ Tool result · `toolu_01TjierYkx9joUoE7nR9y51z`</summary>

```text
Web search results for query: "SmolVLA 87.3 LIBERO success rate evaluation protocol"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]","url":"https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"},{"title":"Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2107"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"DEEPTHINKVLA: ENHANCING REASONING CAPA- BILITY OF VISION-LANGUAGE-ACTION MODELS","url":"https://arxiv.org/pdf/2511.15669"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"}]

Based on the search results, I found information about SmolVLA's 87.3% LIBERO success rate and the LIBERO evaluation protocol:

## SmolVLA's 87.3% Success Rate on LIBERO

The 0.45B parameter SmolVLA achieves an average success rate of 87.3% on LIBERO, outperforming Octo (0.09B, 75.1%), OpenVLA (7B, 76.5%), and even the robotics-pretrained π0 (3.3B, 86.0%).

## LIBERO Evaluation Protocol

The LIBERO evaluation uses a dataset containing 1,693 episodes covering all tasks, and evaluates with 10 trials per task, reporting average success rates based on binary completion criteria. 

The LIBERO benchmark provides four suites (Object, Spatial, Goal, and Long) of language-conditioned robotic manipulation tasks. Each suite contains 10 tasks. Evaluation is conducted under 50 randomized initial conditions for each task and performance is measured by the average Success Rate (SR) under the standard evaluation protocol, with task success rate evaluated under 50 randomized initial conditions per task, averaged within each suite and across all suites.

It's worth noting that researchers have raised concerns about the standard LIBERO evaluation protocol. LIBERO has emerged as the dominant benchmark and is now the most widely adopted protocol for evaluating VLA models. Its standardized task suite and unified reporting metrics have made it the de facto standard for performance comparison.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "cd6f7456-2093-41dd-87dd-3414e1d0e905",
  "tool_use_result": {
    "query": "SmolVLA 87.3 LIBERO success rate evaluation protocol",
    "results": [
      {
        "tool_use_id": "srvtoolu_016q7Sa7WeED8gc73ZznJm5y",
        "content": [
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "VLA-0-Smol",
            "url": "https://robot-learning-collective.github.io/vla-0-smol"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]",
            "url": "https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"
          },
          {
            "title": "Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2107"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"
          },
          {
            "title": "Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"
          },
          {
            "title": "DEEPTHINKVLA: ENHANCING REASONING CAPA- BILITY OF VISION-LANGUAGE-ACTION MODELS",
            "url": "https://arxiv.org/pdf/2511.15669"
          },
          {
            "title": "SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics",
            "url": "https://smolvla.net/index_en"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          }
        ]
      },
      "Based on the search results, I found information about SmolVLA's 87.3% LIBERO success rate and the LIBERO evaluation protocol:\n\n## SmolVLA's 87.3% Success Rate on LIBERO\n\nThe 0.45B parameter SmolVLA achieves an average success rate of 87.3% on LIBERO, outperforming Octo (0.09B, 75.1%), OpenVLA (7B, 76.5%), and even the robotics-pretrained π0 (3.3B, 86.0%).\n\n## LIBERO Evaluation Protocol\n\nThe LIBERO evaluation uses a dataset containing 1,693 episodes covering all tasks, and evaluates with 10 trials per task, reporting average success rates based on binary completion criteria. \n\nThe LIBERO benchmark provides four suites (Object, Spatial, Goal, and Long) of language-conditioned robotic manipulation tasks. Each suite contains 10 tasks. Evaluation is conducted under 50 randomized initial conditions for each task and performance is measured by the average Success Rate (SR) under the standard evaluation protocol, with task success rate evaluated under 50 randomized initial conditions per task, averaged within each suite and across all suites.\n\nIt's worth noting that researchers have raised concerns about the standard LIBERO evaluation protocol. LIBERO has emerged as the dominant benchmark and is now the most widely adopted protocol for evaluating VLA models. Its standardized task suite and unified reporting metrics have made it the de facto standard for performance comparison."
    ],
    "durationSeconds": 6.891461452
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V92r6ENbJL1M4dBRec1ghj`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.01844v1",
  "prompt": "Extract all training details for LIBERO experiments: number of training steps, batch size, learning rate, optimizer, which parts of the model are frozen vs trained, evaluation protocol (episodes per task, max steps per episode), data augmentation, and the exact success rates reported for each LIBERO suite (object, spatial, goal, long). Also extract the model architecture details - total parameters and expert parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "a6465563-663e-4fc5-be88-08a4278bd7c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHyWPubhGzH8mAMmoeLcqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2948,
      "cache_read_input_tokens": 25595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2948
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FiRFbXC67Sn66RZx8eTAxk`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/2107",
  "prompt": "Extract the discussion about low success rate when training SmolVLA on LIBERO. What training configuration do they use? What success rates do they report? What solutions or explanations are offered for the gap between reported and actual performance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "b31c5430-2ad1-42bb-9c8e-9675eb040393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHyWPubhGzH8mAMmoeLcqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2948,
      "cache_read_input_tokens": 25595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2948
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T23:33:40.271Z_

<details><summary>↩ Tool result · `toolu_01V92r6ENbJL1M4dBRec1ghj`</summary>

```text
# SmolVLA LIBERO Training & Architecture Details

## Training Configuration

**Pretraining Phase:**
- Steps: 200,000
- Batch size: 256 (global)
- Learning rate: "1e-4" with cosine decay to "2.5e-6"
- Optimizer: "AdamW optimizer with β1=0.9,β2=0.95"
- Frozen components: VLM backbone (only action expert trained)
- Image resolution: 512×512

**Fine-tuning Phase (LIBERO):**
- Steps: 100,000
- Batch size: 64
- Frozen components: VLM backbone remains frozen
- Training precision: "bfloat16 precision and torch.compile()"

## Evaluation Protocol

- Tasks per category: 10 (Spatial, Object, Goal, Long)
- Trials per task: 10
- Success metric: Binary (1 if fully completed, 0 otherwise)
- Dataset size: "1,693 episodes covering all tasks"

## Model Architecture

**Overall Parameters:**
- Main model: "450 million parameters"
- Action expert: "approximately 100 million" parameters
- VLM layers utilized: First 16 layers (L−N where N=L/2)

**Expert Specifications:**
- Hidden size: 0.75× VLM dimension
- Action chunk size: n=50
- Flow matching inference steps: 10

## LIBERO Success Rates

| Category | SmolVLA (0.45B) |
|----------|-----------------|
| Spatial  | 90%             |
| Object   | 96%             |
| Goal     | 92%             |
| Long     | 71%             |
| **Avg.** | **87.3%**       |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "73e2fa4e-995d-42d6-a542-ab64be032cf5",
  "tool_use_result": {
    "bytes": 522052,
    "code": 200,
    "codeText": "OK",
    "result": "# SmolVLA LIBERO Training & Architecture Details\n\n## Training Configuration\n\n**Pretraining Phase:**\n- Steps: 200,000\n- Batch size: 256 (global)\n- Learning rate: \"1e-4\" with cosine decay to \"2.5e-6\"\n- Optimizer: \"AdamW optimizer with β1=0.9,β2=0.95\"\n- Frozen components: VLM backbone (only action expert trained)\n- Image resolution: 512×512\n\n**Fine-tuning Phase (LIBERO):**\n- Steps: 100,000\n- Batch size: 64\n- Frozen components: VLM backbone remains frozen\n- Training precision: \"bfloat16 precision and torch.compile()\"\n\n## Evaluation Protocol\n\n- Tasks per category: 10 (Spatial, Object, Goal, Long)\n- Trials per task: 10\n- Success metric: Binary (1 if fully completed, 0 otherwise)\n- Dataset size: \"1,693 episodes covering all tasks\"\n\n## Model Architecture\n\n**Overall Parameters:**\n- Main model: \"450 million parameters\"\n- Action expert: \"approximately 100 million\" parameters\n- VLM layers utilized: First 16 layers (L−N where N=L/2)\n\n**Expert Specifications:**\n- Hidden size: 0.75× VLM dimension\n- Action chunk size: n=50\n- Flow matching inference steps: 10\n\n## LIBERO Success Rates\n\n| Category | SmolVLA (0.45B) |\n|----------|-----------------|\n| Spatial  | 90%             |\n| Object   | 96%             |\n| Goal     | 92%             |\n| Long     | 71%             |\n| **Avg.** | **87.3%**       |",
    "durationMs": 6077,
    "url": "https://arxiv.org/html/2506.01844v1"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T23:33:41.879Z_

<details><summary>↩ Tool result · `toolu_01FiRFbXC67Sn66RZx8eTAxk`</summary>

```text
# SmolVLA-0.24B Training on LIBERO: Issue Summary

## Training Configuration
The user employed this command:
`lerobot-train --policy.type=smolvla --policy.load_vlm_weights=true --dataset.repo_id=HuggingFaceVLA/libero --env.type=libero --env.task=libero_10 --output_dir=./outputs/ --steps=100000 --batch_size=64 --eval.batch_size=1 --eval.n_episodes=1 --eval_freq=1000 --wandb.enable=true`

Key specifications included a single RTX4090 GPU and the "HuggingFaceTB/SmolVLM2-256M-Video-Instruct" base model.

## Performance Results
The developer reported disappointing outcomes: "the success rate on the eval set is quite low. The success rate was only 7.5%." They included training plots visualizing this subpar performance.

## Proposed Solutions
The page content itself does not contain responses, explanations, or proposed solutions addressing the performance gap. The issue appears to be an open question awaiting community feedback or maintainer guidance rather than a resolved discussion with documented remedies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "adb34eab-8cb0-49a3-8682-1c3e724646c0",
  "tool_use_result": {
    "bytes": 278744,
    "code": 200,
    "codeText": "OK",
    "result": "# SmolVLA-0.24B Training on LIBERO: Issue Summary\n\n## Training Configuration\nThe user employed this command:\n`lerobot-train --policy.type=smolvla --policy.load_vlm_weights=true --dataset.repo_id=HuggingFaceVLA/libero --env.type=libero --env.task=libero_10 --output_dir=./outputs/ --steps=100000 --batch_size=64 --eval.batch_size=1 --eval.n_episodes=1 --eval_freq=1000 --wandb.enable=true`\n\nKey specifications included a single RTX4090 GPU and the \"HuggingFaceTB/SmolVLM2-256M-Video-Instruct\" base model.\n\n## Performance Results\nThe developer reported disappointing outcomes: \"the success rate on the eval set is quite low. The success rate was only 7.5%.\" They included training plots visualizing this subpar performance.\n\n## Proposed Solutions\nThe page content itself does not contain responses, explanations, or proposed solutions addressing the performance gap. The issue appears to be an open question awaiting community feedback or maintainer guidance rather than a resolved discussion with documented remedies.",
    "durationMs": 6173,
    "url": "https://github.com/huggingface/lerobot/issues/2107"
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011AUPfthVGgCmkyU39Y2ZAq`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/smolvla",
  "prompt": "Extract the official fine-tuning configuration for SmolVLA on LIBERO: training steps, batch size, learning rate, which parts are frozen, evaluation settings. Also look for any mention of pretraining on robotics data before LIBERO fine-tuning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "9b67a514-e08a-4d94-ba6c-3a58911421a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACFQvucRLQRZw9ED3pN9qm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1055,
      "cache_read_input_tokens": 28543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1055
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T23:33:46.654Z_

<details><summary>↩ Tool result · `toolu_011AUPfthVGgCmkyU39Y2ZAq`</summary>

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

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "54a59332-ac49-4211-b165-9656a9a6fca1",
  "tool_use_result": {
    "bytes": 4919,
    "code": 200,
    "codeText": "OK",
    "result": "# SmolVLA\n\nSmolVLA is Hugging Face’s lightweight foundation model for robotics. Designed for easy fine-tuning on LeRobot datasets, it helps accelerate your development!\n\n  \n  \n  \n    Figure 1. SmolVLA takes as input (i) multiple cameras views, (ii) the\n    robot’s current sensorimotor state, and (iii) a natural language\n    instruction, encoded into contextual features used to condition the action\n    expert when generating an action chunk.\n  \n\n## Set Up Your Environment\n\n1. Install LeRobot by following our [Installation Guide](./installation).\n2. Install SmolVLA dependencies by running:\n\n   ```bash\n   pip install -e \".[smolvla]\"\n   ```\n\n## Collect a dataset\n\nSmolVLA is a base model, so fine-tuning on your own data is required for optimal performance in your setup.\nWe recommend recording ~50 episodes of your task as a starting point. Follow our guide to get started: [Recording a Dataset](./il_robots)\n\nIn your dataset, make sure to have enough demonstrations per each variation (e.g. the cube position on the table if it is cube pick-place task) you are introducing.\n\nWe recommend checking out the dataset linked below for reference that was used in the [SmolVLA paper](https://huggingface.co/papers/2506.01844):\n\n🔗 [SVLA SO100 PickPlace](https://huggingface.co/spaces/lerobot/visualize_dataset?path=%2Flerobot%2Fsvla_so100_pickplace%2Fepisode_0)\n\nIn this dataset, we recorded 50 episodes across 5 distinct cube positions. For each position, we collected 10 episodes of pick-and-place interactions. This structure, repeating each variation several times, helped the model generalize better. We tried similar dataset with 25 episodes, and it was not enough leading to a bad performance. So, the data quality and quantity is definitely a key.\nAfter you have your dataset available on the Hub, you are good to go to use our finetuning script to adapt SmolVLA to your application.\n\n## Finetune SmolVLA on your data\n\nUse [`smolvla_base`](https://hf.co/lerobot/smolvla_base), our pretrained 450M model, and fine-tune it on your data.\nTraining the model for 20k steps will roughly take ~4 hrs on a single A100 GPU. You should tune the number of steps based on performance and your use-case.\n\nIf you don't have a gpu device, you can train using our notebook on [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb)\n\nPass your dataset to the training script using `--dataset.repo_id`. If you want to test your installation, run the following command where we use one of the datasets we collected for the [SmolVLA Paper](https://huggingface.co/papers/2506.01844).\n\n```bash\ncd lerobot && lerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=${HF_USER}/mydataset \\\n  --batch_size=64 \\\n  --steps=20000 \\\n  --output_dir=outputs/train/my_smolvla \\\n  --job_name=my_smolvla_training \\\n  --policy.device=cuda \\\n  --wandb.enable=true\n```\n\n  You can start with a small batch size and increase it incrementally, if the\n  GPU allows it, as long as loading times remain short.\n\nFine-tuning is an art. For a complete overview of the options for finetuning, run\n\n```bash\nlerobot-train --help\n```\n\n  \n  \n  \n    Figure 2: Comparison of SmolVLA across task variations. From left to right:\n    (1) pick-place cube counting, (2) pick-place cube counting, (3) pick-place\n    cube counting under perturbations, and (4) generalization on pick-and-place\n    of the lego block with real-world SO101.\n  \n\n## Evaluate the finetuned model and run it in real-time\n\nSimilarly for when recording an episode, it is recommended that you are logged in to the HuggingFace Hub. You can follow the corresponding steps: [Record a dataset](./il_robots).\nOnce you are logged in, you can run inference in your setup by doing:\n\n```bash\nlerobot-record \\\n  --robot.type=so101_follower \\\n  --robot.port=/dev/ttyACM0 \\ # <- Use your port\n  --robot.id=my_blue_follower_arm \\ # <- Use your robot id\n  --robot.cameras=\"{ front: {type: opencv, index_or_path: 8, width: 640, height: 480, fps: 30}}\" \\ # <- Use your cameras\n  --dataset.single_task=\"Grasp a lego block and put it in the bin.\" \\ # <- Use the same task description you used in your dataset recording\n  --dataset.repo_id=${HF_USER}/eval_DATASET_NAME_test \\  # <- This will be the dataset name on HF Hub\n  --dataset.episode_time_s=50 \\\n  --dataset.num_episodes=10 \\\n  --dataset.streaming_encoding=true \\\n  --dataset.encoder_threads=2 \\\n  # --dataset.vcodec=auto \\\n  # <- Teleop optional if you want to teleoperate in between episodes \\\n  # --teleop.type=so100_leader \\\n  # --teleop.port=/dev/ttyACM0 \\\n  # --teleop.id=my_red_leader_arm \\\n  --policy.path=HF_USER/FINETUNE_MODEL_NAME # <- Use your fine-tuned model\n```\n\nDepending on your evaluation setup, you can configure the duration and the number of episodes to record for your evaluation suite.\n\n",
    "durationMs": 428,
    "url": "https://huggingface.co/docs/lerobot/en/smolvla"
  }
}
````

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BregvVkHYSAXPRWgB3US6m`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/1316",
  "prompt": "Extract the discussion about SmolVLA LIBERO evaluation protocol. What are the specific evaluation settings? How many episodes per task? What is the max steps per episode? Any information about the gap between reported and reproduced results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "e4990901-09be-4c73-9d8a-99c41135e358",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACFQvucRLQRZw9ED3pN9qm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1055,
      "cache_read_input_tokens": 28543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1055
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T23:33:51.220Z_

<details><summary>↩ Tool result · `toolu_01BregvVkHYSAXPRWgB3US6m`</summary>

```text
# SmolVLA LIBERO Evaluation Discussion

Based on the GitHub issue content provided, there is **no discussion of specific evaluation settings, episode counts, or maximum steps per episode**. 

The issue simply contains a user's question requesting clarification about the fine-tuning process used in the SmolVLA paper's simulation evaluation. The user asks: "Could you elaborate on the details of the fine-tuning process? (which parameters were trained/frozen, optimizer, gradient steps, etc..) I am planning to reproduce the results."

**Key points:**
- The issue is labeled as a "question" seeking "clarification or additional information"
- No evaluation protocol details are provided in the visible content
- No information about gaps between reported and reproduced results appears in this discussion
- The issue remains open without visible responses containing the requested technical specifications

To find the actual evaluation protocol details, you would need to consult the SmolVLA paper itself or check for responses in the full issue thread beyond what's shown here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "9070f8cb-d245-46c7-b396-74a1310b41c0",
  "tool_use_result": {
    "bytes": 504937,
    "code": 200,
    "codeText": "OK",
    "result": "# SmolVLA LIBERO Evaluation Discussion\n\nBased on the GitHub issue content provided, there is **no discussion of specific evaluation settings, episode counts, or maximum steps per episode**. \n\nThe issue simply contains a user's question requesting clarification about the fine-tuning process used in the SmolVLA paper's simulation evaluation. The user asks: \"Could you elaborate on the details of the fine-tuning process? (which parameters were trained/frozen, optimizer, gradient steps, etc..) I am planning to reproduce the results.\"\n\n**Key points:**\n- The issue is labeled as a \"question\" seeking \"clarification or additional information\"\n- No evaluation protocol details are provided in the visible content\n- No information about gaps between reported and reproduced results appears in this discussion\n- The issue remains open without visible responses containing the requested technical specifications\n\nTo find the actual evaluation protocol details, you would need to consult the SmolVLA paper itself or check for responses in the full issue thread beyond what's shown here.",
    "durationMs": 4023,
    "url": "https://github.com/huggingface/lerobot/issues/1316"
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015EMG44bQLbXv9mZiUmYRig`</summary>

```json
{
  "query": "SmolVLA LIBERO pretraining \"robotics data\" before fine-tuning Open X-Embodiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "e8db9ab1-dffb-44ab-aa41-e7fa526e1ada",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDLHrPCkTf7EQZ6vdobK5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 29598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2014
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BkBNnwzCQWnnuUA6ws2V7c`</summary>

```json
{
  "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero",
  "prompt": "Extract the model card details: what base model was used, how was it trained on LIBERO, training steps, batch size, what was frozen, any pretraining information, evaluation results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "30307be3-7a87-43d7-97db-90381af865a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDLHrPCkTf7EQZ6vdobK5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 29598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2014
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T23:34:01.208Z_

<details><summary>↩ Tool result · `toolu_01BkBNnwzCQWnnuUA6ws2V7c`</summary>

````text
# SmolVLA LIBERO Model Card Details

Based on the provided content, here's what can be extracted:

## Base Model
- **Base Model:** `lerobot/smolvla_base`
- **Model Type:** SmolVLA (Vision-Language-Action model)
- **License:** Apache-2.0

## Training Information

### Training Approach
The model was trained using **LeRobot** framework with the following configuration shown in the example:

```bash
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

### Training Parameters (Example):
- **Batch Size:** 64
- **Steps:** 20,000
- **Device:** CUDA

## Notable Details

⚠️ **Limited Information:** The provided content does **not** include:
- What layers were frozen during fine-tuning
- Specific pretraining details
- Evaluation/benchmark results on LIBERO
- Learning rate or optimizer information
- Actual training configuration used for this specific model

## Related Resources
- **Paper:** [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://huggingface.co/papers/2506.01844) (arxiv: 2506.01844)
- **Framework:** [LeRobot Documentation](https://huggingface.co/docs/lerobot/index)
- **Downloads:** 25,225 (last month)

**Note:** For complete training specifications and evaluation results, refer to the full paper and LeRobot documentation.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "2d647b54-a38b-4fd8-8954-8277c7c4ec34",
  "tool_use_result": {
    "bytes": 133137,
    "code": 200,
    "codeText": "OK",
    "result": "# SmolVLA LIBERO Model Card Details\n\nBased on the provided content, here's what can be extracted:\n\n## Base Model\n- **Base Model:** `lerobot/smolvla_base`\n- **Model Type:** SmolVLA (Vision-Language-Action model)\n- **License:** Apache-2.0\n\n## Training Information\n\n### Training Approach\nThe model was trained using **LeRobot** framework with the following configuration shown in the example:\n\n```bash\npython lerobot/scripts/train.py \\\n  --policy.path=HuggingFaceVLA/smolvla_libero \\\n  --dataset.repo_id=lerobot/svla_so101_pickplace \\\n  --batch_size=64 \\\n  --steps=20000 \\\n  --output_dir=outputs/train/my_smolvla \\\n  --job_name=my_smolvla_training \\\n  --policy.device=cuda \\\n  --wandb.enable=true\n```\n\n### Training Parameters (Example):\n- **Batch Size:** 64\n- **Steps:** 20,000\n- **Device:** CUDA\n\n## Notable Details\n\n⚠️ **Limited Information:** The provided content does **not** include:\n- What layers were frozen during fine-tuning\n- Specific pretraining details\n- Evaluation/benchmark results on LIBERO\n- Learning rate or optimizer information\n- Actual training configuration used for this specific model\n\n## Related Resources\n- **Paper:** [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://huggingface.co/papers/2506.01844) (arxiv: 2506.01844)\n- **Framework:** [LeRobot Documentation](https://huggingface.co/docs/lerobot/index)\n- **Downloads:** 25,225 (last month)\n\n**Note:** For complete training specifications and evaluation results, refer to the full paper and LeRobot documentation.",
    "durationMs": 4382,
    "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero"
  }
}
````

</details>

---

### Tool result

_source line 25 · 2026-05-16T23:34:02.247Z_

<details><summary>↩ Tool result · `toolu_015EMG44bQLbXv9mZiUmYRig`</summary>

```text
Web search results for query: "SmolVLA LIBERO pretraining "robotics data" before fine-tuning Open X-Embodiment"

Links: [{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"SmolVLA - ArXivIQ","url":"https://arxiviq.substack.com/p/smolvla"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"}]

Based on the search results, I found information about SmolVLA's pretraining approach:

## SmolVLA Pretraining Strategy

For real-world evaluation, SmolVLA is pretrained on community-collected datasets. More specifically, for its pretraining, SmolVLA leveraged a curated set of 481 datasets, primarily for the SO-100 robotic arm, encompassing approximately 23,000 episodes (10.6 million frames).

SmolVLA is trained on the open community LeRobot dataset and fully trained on publicly available LeRobot community datasets on Hugging Face and released as open source.

Notably, SmolVLA is only initialized from the VLM (vision-language model), rather than being pre-trained on large-scale robotics data like some competing approaches. This contrasts with larger models like OpenVLA, which curates a dataset of 970k robot manipulation trajectories from the Open X-Embodiment (OpenX) dataset that spans a wide range of tasks, scenes and robot embodiments.

## LIBERO Benchmarking

After its initialization and community-driven pretraining approach, SmolVLA is evaluated on two major simulation benchmarks–LIBERO and Meta-World–using a multi-task training setup, and outperforms other VLA-based approaches such as Octo and OpenVLA, as well as the diffusion policy baseline across both LIBERO and Meta-World.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "b383bbb9-72c5-4403-844f-0fe2bb22e09b",
  "tool_use_result": {
    "query": "SmolVLA LIBERO pretraining \"robotics data\" before fine-tuning Open X-Embodiment",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PyPMCh3tNFk6C8Q9To3j31",
        "content": [
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model",
            "url": "https://arxiv.org/pdf/2506.01844"
          },
          {
            "title": "Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics",
            "url": "https://smolvla.net/index_en"
          },
          {
            "title": "SmolVLA: Efficient Vision Language Action Model - LeRobot",
            "url": "https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "SmolVLA - ArXivIQ",
            "url": "https://arxiviq.substack.com/p/smolvla"
          },
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://arxiv.org/abs/2506.01844"
          }
        ]
      },
      "Based on the search results, I found information about SmolVLA's pretraining approach:\n\n## SmolVLA Pretraining Strategy\n\nFor real-world evaluation, SmolVLA is pretrained on community-collected datasets. More specifically, for its pretraining, SmolVLA leveraged a curated set of 481 datasets, primarily for the SO-100 robotic arm, encompassing approximately 23,000 episodes (10.6 million frames).\n\nSmolVLA is trained on the open community LeRobot dataset and fully trained on publicly available LeRobot community datasets on Hugging Face and released as open source.\n\nNotably, SmolVLA is only initialized from the VLM (vision-language model), rather than being pre-trained on large-scale robotics data like some competing approaches. This contrasts with larger models like OpenVLA, which curates a dataset of 970k robot manipulation trajectories from the Open X-Embodiment (OpenX) dataset that spans a wide range of tasks, scenes and robot embodiments.\n\n## LIBERO Benchmarking\n\nAfter its initialization and community-driven pretraining approach, SmolVLA is evaluated on two major simulation benchmarks–LIBERO and Meta-World–using a multi-task training setup, and outperforms other VLA-based approaches such as Octo and OpenVLA, as well as the diffusion policy baseline across both LIBERO and Meta-World."
    ],
    "durationSeconds": 6.9463300650000015
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me compile the findings:

1. **SmolVLA 87.3% uses how many steps?**
   - Fine-tuning on LIBERO: 100K steps, batch size 64
   - BUT: SmolVLA was PRETRAINED for 200K steps on robotics data (481 community datasets, ~23K episodes, 10.6M frames) before the LIBERO fine-tuning
   - The VLM backbone is frozen; only the action expert (~100M params) is trained
   
2. **What gets trained during fine-tuning?**
   - The VLM backbone stays frozen while only the action expert (~100M of 450M total params) gets trained
   - There's some ambiguity in the paper—the ablations are trained from scratch, but the final 87.3% result likely leverages the pretrained model

3. **Evaluation setup:**
   - 10 trials per task across 10 tasks per suite, 4 suites total, with binary success metrics

4. **The 38 percentage point gap likely comes down to:**
   - SmolVLA's 87.3% uses a model pretrained on 481 robotics datasets first (200K steps), then fine-tuned on LIBERO, whereas the baseline trains from scratch without that robotics pretraining
   - SmolVLA also takes a different architectural approach by freezing the VLM and training only the action expert, rather than doing full fine-tuning
   - I need to clarify whether the 87.3% actually includes pretraining or if it's purely the LIBERO results trained from scratch

Looking at the paper more carefully, the ablations test different architecture choices from scratch on LIBERO, but the main comparison table results (where SmolVLA shows 87.3% average across Object, Spatial, Goal, and Long horizon tasks) likely represent the full pretrained model fine-tuned on LIBERO. The distinction matters because the user's "Full FT 100K" approach is probably training from scratch without the robotics pretraining that gives SmolVLA its foundation.

The 38 percentage point gap likely stems from three factors: SmolVLA's 200K steps of diverse robotics pretraining before LIBERO fine-tuning, the difference in training scope where SmolVLA only trains the expert module while the user is doing full model fine-tuning (which can be harder to optimize), and SmolVLA's specific expert architecture with interleaved cross and self attention plus causal masking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "0bda5051-4e73-4904-9762-f5d2dad555af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPM4jH9nfe9hpd9fJuYmYM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 496,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 31612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1190
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 27_

## 结果

### SmolVLA LIBERO 训练配置 (arXiv:2506.01844)

| 项目 | 值 |
|------|------|
| 总参数 | 450M (VLM) + ~100M (action expert) |
| LIBERO FT 步数 | **100K steps** |
| Batch size | 64 |
| LR | 1e-4, cosine decay → 2.5e-6 |
| Optimizer | AdamW (β1=0.9, β2=0.95) |
| 冻结部分 | **VLM backbone 全冻**，只训 action expert (~100M) |
| 精度 | bfloat16 + torch.compile |
| 评估 | 10 trials/task, 10 tasks/suite, binary success |

### 关键发现：Robotics Pretraining

SmolVLA 在 LIBERO fine-tune 之前有 **200K steps 的 robotics pretraining**（481 个社区数据集，~23K episodes，10.6M frames，batch 256）。87.3% 的结果来自 pretrained base → LIBERO FT，不是 from scratch。

### 38pp Gap 分析

| 问题 | 回答 |
|------|------|
| 步数不够？ | 步数相同（都是100K），不是主因 |
| Scope不同？ | **是主因之一**：SmolVLA 冻VLM只训expert(100M)，你做Full FT可能过拟合或优化困难 |
| 预训练差异？ | **最大主因**：SmolVLA有200K步robotics预训练，你的模型没有 |
| 数据增强？ | 论文未提特殊augmentation |
| 评估协议？ | 10 episodes/task，与你的设置需对齐确认 |

### 结论

**38pp gap 最可能原因**：SmolVLA 的 87.3% 建立在 robotics pretraining 之上（相当于额外 200K steps on diverse data）。你的 Full FT 100K 是 from VLM scratch，等价于少了整个预训练阶段。次要原因是 Full FT vs Expert-only 的优化难度差异。

**建议方向**：用 `lerobot/smolvla_base`（已含 robotics pretrain）作为起点做 LIBERO FT，或只训 action expert 而非 full model。

Sources:
- [SmolVLA Paper (HTML)](https://arxiv.org/html/2506.01844v1)
- [SmolVLA HF Docs](https://huggingface.co/docs/lerobot/en/smolvla)
- [Low SR Issue #2107](https://github.com/huggingface/lerobot/issues/2107)
- [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "uuid": "91d2a7f5-4604-48de-b283-dd17d116dec2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPM4jH9nfe9hpd9fJuYmYM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 496,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 31612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1190
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 28_

## 结果

### SmolVLA LIBERO 训练配置 (arXiv:2506.01844)

| 项目 | 值 |
|------|------|
| 总参数 | 450M (VLM) + ~100M (action expert) |
| LIBERO FT 步数 | **100K steps** |
| Batch size | 64 |
| LR | 1e-4, cosine decay → 2.5e-6 |
| Optimizer | AdamW (β1=0.9, β2=0.95) |
| 冻结部分 | **VLM backbone 全冻**，只训 action expert (~100M) |
| 精度 | bfloat16 + torch.compile |
| 评估 | 10 trials/task, 10 tasks/suite, binary success |

### 关键发现：Robotics Pretraining

SmolVLA 在 LIBERO fine-tune 之前有 **200K steps 的 robotics pretraining**（481 个社区数据集，~23K episodes，10.6M frames，batch 256）。87.3% 的结果来自 pretrained base → LIBERO FT，不是 from scratch。

### 38pp Gap 分析

| 问题 | 回答 |
|------|------|
| 步数不够？ | 步数相同（都是100K），不是主因 |
| Scope不同？ | **是主因之一**：SmolVLA 冻VLM只训expert(100M)，你做Full FT可能过拟合或优化困难 |
| 预训练差异？ | **最大主因**：SmolVLA有200K步robotics预训练，你的模型没有 |
| 数据增强？ | 论文未提特殊augmentation |
| 评估协议？ | 10 episodes/task，与你的设置需对齐确认 |

### 结论

**38pp gap 最可能原因**：SmolVLA 的 87.3% 建立在 robotics pretraining 之上（相当于额外 200K steps on diverse data）。你的 Full FT 100K 是 from VLM scratch，等价于少了整个预训练阶段。次要原因是 Full FT vs Expert-only 的优化难度差异。

**建议方向**：用 `lerobot/smolvla_base`（已含 robotics pretrain）作为起点做 LIBERO FT，或只训 action expert 而非 full model。

Sources:
- [SmolVLA Paper (HTML)](https://arxiv.org/html/2506.01844v1)
- [SmolVLA HF Docs](https://huggingface.co/docs/lerobot/en/smolvla)
- [Low SR Issue #2107](https://github.com/huggingface/lerobot/issues/2107)
- [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 90466,
  "duration_api_ms": 113313,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "047a7f9a-c478-4a63-920b-838bf0c3d599",
  "total_cost_usd": 0.4538067499999999,
  "usage": {
    "input_tokens": 505,
    "cache_creation_input_tokens": 20961,
    "cache_read_input_tokens": 151609,
    "output_tokens": 2792,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 20961,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 496,
        "output_tokens": 1705,
        "cache_read_input_tokens": 31612,
        "cache_creation_input_tokens": 1190,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1190
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 117826,
      "outputTokens": 3369,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 4,
      "costUSD": 0.174671,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 505,
      "outputTokens": 2792,
      "cacheReadInputTokens": 151609,
      "cacheCreationInputTokens": 20961,
      "webSearchRequests": 0,
      "costUSD": 0.27913575,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b136f954-7f85-47fc-b7ea-2ce85f4c7f6c"
}
```

</details>

---
