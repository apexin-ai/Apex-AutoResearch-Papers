# research second vla survey

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/workers/worker_research_second_vla_survey_20260519T162116.log`
- **Structured JSON:** [`076ef3e0c1874c27bbf6.json`](../../sessions/07/076ef3e0c1874c27bbf6.json)

## Before a recorded user message

89 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
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
  "uuid": "377a77ee-b4e3-4339-81db-559fb11518c4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779225600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1cfc1040-2f08-4453-9bf3-d2ad0e552614",
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854"
}
```

---

### Assistant

_source line 4_

我来搜索 2024-2026 年公开可用的 decoder-only VLA 模型。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "d0343ef9-5058-4347-98a0-7e213a86170a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHwQJUAca9FuvR1JCFHKvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11847,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11847
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BZUcR3K5zXQ4Pj3ZZbAPEq`</summary>

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
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "a2401020-61e9-4a82-a4e9-f5c46ede0f80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHwQJUAca9FuvR1JCFHKvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11847,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11847
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-19T16:21:29.425Z_

<details><summary>↩ Tool result · `toolu_01BZUcR3K5zXQ4Pj3ZZbAPEq`</summary>

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
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "853a332f-eb82-40bf-84ec-bdd94491ecb0",
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
Let me search for decoder-only VLA models in parallel with multiple search queries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "98f40574-d6ab-4e74-835a-e2dd8a6346ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UcGMqLsMcYF5nNtQAj69W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
      },
      "output_tokens": 34,
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

_source line 8_

开始多路并行搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "a4ce6746-8625-4ddc-8e71-3689fdb8d21c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UcGMqLsMcYF5nNtQAj69W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
      },
      "output_tokens": 34,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JoNvhjAdW4U7jQYdSrK57Z`</summary>

```json
{
  "query": "vision language action model open source weights 2024 2025 decoder-only robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "983a347f-b4b4-480c-83a9-257ad63a0c71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UcGMqLsMcYF5nNtQAj69W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
      },
      "output_tokens": 34,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YawU7qK5WafEBCWYDbmP5G`</summary>

```json
{
  "query": "OpenVLA alternative VLA model open weights huggingface 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "63759cb1-c4cb-47aa-8fb8-10e91c2a1f27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UcGMqLsMcYF5nNtQAj69W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
      },
      "output_tokens": 34,
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015hphq5cL2SmNZGEW7YoRYU`</summary>

```json
{
  "query": "RT-2 open source implementation VLA decoder-only weights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "b09fe6c7-07b6-43ff-8db8-3b9a8a797460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UcGMqLsMcYF5nNtQAj69W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
      },
      "output_tokens": 34,
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FoTRRQ8psLB78guZRFc6oK`</summary>

```json
{
  "query": "pi-zero pi0 physical intelligence VLA architecture 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "89de7517-7de2-4610-8103-d38c263c8794",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UcGMqLsMcYF5nNtQAj69W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
      },
      "output_tokens": 34,
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LXbJXutLYpnF5Hq8cu2LNQ`</summary>

```json
{
  "query": "robot foundation model decoder-only transformer action prediction 2024 2025 open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "545015ef-4168-4d8c-bec9-281b70fdd5bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UcGMqLsMcYF5nNtQAj69W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
      },
      "output_tokens": 34,
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

_source line 14 · 2026-05-19T16:21:41.327Z_

<details><summary>↩ Tool result · `toolu_01YawU7qK5WafEBCWYDbmP5G`</summary>

```text
Web search results for query: "OpenVLA alternative VLA model open weights huggingface 2024 2025"

Links: [{"title":"Open-Weight Foundation Models for Robotics (2025 Guide) | RoboCloud Hub","url":"https://robocloud-dashboard.vercel.app/learn/blog/open-weight-robot-models"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"phospho starter pack documentation","url":"https://docs.phospho.ai/learn/policies"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"openvla/openvla-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"Economies of Open Intelligence: Tracing Power & Participation in the Model Ecosystem","url":"https://arxiv.org/pdf/2512.03073"}]

Based on the search results, here are alternative VLA (Vision-Language-Action) models to OpenVLA with open weights available on Hugging Face:

## Key OpenVLA Alternatives

**SmolVLA**: An open-source compact VLA with 450 million parameters released by Hugging Face. It was trained entirely on LeRobot, an open-source dataset collected and curated by the community. Despite its compact size, SmolVLA achieved comparable performances with much larger VLAs such as Octo, OpenVLA and π0.

**Octo**: A lightweight open-source generalist robot policy from UC Berkeley. Originally trained on Open X-Embodiment, it was released in smaller configurations (27M and 93M parameters).

**GR00T-N1**: NVIDIA's foundation model for robots released in March 2025. The model weights are available on Hugging Face. GR00T-N1 combines both VLA for language understanding and Diffusion transformers for fine grained controls.

**RDT-1b**: A diffusion transformer called RDT-1b (May 2024) is currently the #1 model in robotics on Hugging Face.

## About OpenVLA

For context, OpenVLA is a 7B parameter open-source vision-language-action model pretrained on 970k robot episodes from the Open X-Embodiment dataset. The OpenVLA checkpoints and PyTorch training pipeline are fully open-source and models can be downloaded and fine-tuned from HuggingFace.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "8dadbe1a-b73d-497b-a236-3210ce842353",
  "tool_use_result": {
    "query": "OpenVLA alternative VLA model open weights huggingface 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X31kf47H9piDxfRojRkTXY",
        "content": [
          {
            "title": "Open-Weight Foundation Models for Robotics (2025 Guide) | RoboCloud Hub",
            "url": "https://robocloud-dashboard.vercel.app/learn/blog/open-weight-robot-models"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "phospho starter pack documentation",
            "url": "https://docs.phospho.ai/learn/policies"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "openvla/openvla-7b · Hugging Face",
            "url": "https://huggingface.co/openvla/openvla-7b"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/pdf/2406.09246"
          },
          {
            "title": "Economies of Open Intelligence: Tracing Power & Participation in the Model Ecosystem",
            "url": "https://arxiv.org/pdf/2512.03073"
          }
        ]
      },
      "Based on the search results, here are alternative VLA (Vision-Language-Action) models to OpenVLA with open weights available on Hugging Face:\n\n## Key OpenVLA Alternatives\n\n**SmolVLA**: An open-source compact VLA with 450 million parameters released by Hugging Face. It was trained entirely on LeRobot, an open-source dataset collected and curated by the community. Despite its compact size, SmolVLA achieved comparable performances with much larger VLAs such as Octo, OpenVLA and π0.\n\n**Octo**: A lightweight open-source generalist robot policy from UC Berkeley. Originally trained on Open X-Embodiment, it was released in smaller configurations (27M and 93M parameters).\n\n**GR00T-N1**: NVIDIA's foundation model for robots released in March 2025. The model weights are available on Hugging Face. GR00T-N1 combines both VLA for language understanding and Diffusion transformers for fine grained controls.\n\n**RDT-1b**: A diffusion transformer called RDT-1b (May 2024) is currently the #1 model in robotics on Hugging Face.\n\n## About OpenVLA\n\nFor context, OpenVLA is a 7B parameter open-source vision-language-action model pretrained on 970k robot episodes from the Open X-Embodiment dataset. The OpenVLA checkpoints and PyTorch training pipeline are fully open-source and models can be downloaded and fine-tuned from HuggingFace."
    ],
    "durationSeconds": 7.093492521
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T16:21:41.518Z_

<details><summary>↩ Tool result · `toolu_01FoTRRQ8psLB78guZRFc6oK`</summary>

```text
Web search results for query: "pi-zero pi0 physical intelligence VLA architecture 2024"

Links: [{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub","url":"https://github.com/allenzren/open-pi-zero"},{"title":"π0 and π0-FAST: Vision-Language-Action Models for General Robot Control","url":"https://huggingface.co/blog/pi0"},{"title":"Physical Intelligence π0 vs OpenVLA: Best VLA Model for Robot Learning 2026 | SVRC","url":"https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla"},{"title":"Physical Intelligence Unveils Robotics Foundation Model Pi-Zero - InfoQ","url":"https://www.infoq.com/news/2024/12/pi-zero-robot/"},{"title":"π 0 : Our First Generalist Policy","url":"https://www.pi.website/blog/pi0"},{"title":"DM0: An Embodied-Native Vision-Language-Action Model towards Physical AI","url":"https://arxiv.org/pdf/2602.14974"},{"title":"Our First Generalist Policy","url":"https://physicalintelligence.company/blog/pi0"}]

Based on the search results, here's what I found about π0 (pi-zero), Physical Intelligence's VLA architecture from 2024:

## Overview

π0 (Pi-Zero) is a Vision-Language-Action (VLA) model developed by the Physical Intelligence team designed for generalist robot control. Physical Intelligence recently announced π0 as a general-purpose AI foundation model for robots that is based on a pre-trained vision-language model (VLM) and outperforms other baseline models in evaluations on five robot tasks.

## Architecture

π0 combines large-scale multi-task and multi-robot data collection with a new network architecture to enable the most capable and dexterous generalist robot policy to date. The architecture incorporates mixture of experts (MoE) and block-attention components, and the PiZero class follows the original Pi0 architecture, while the underlying JointModel and Mixture classes form a general instantiation of the MoE + block-attention architecture.

## Performance

π0 is by far the best-performing model across all tested tasks, with more than a 2x improvement in performance from using the full-size architecture with VLM pre-training compared to the smaller π0-small version.

## Access

π0 from Physical Intelligence delivers state-of-the-art dexterity performance but requires partnership access and cannot be self-hosted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "0daa504e-8986-44ee-b494-241cc3da510e",
  "tool_use_result": {
    "query": "pi-zero pi0 physical intelligence VLA architecture 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A1MsRXsrpSBaXrFYYzTfRu",
        "content": [
          {
            "title": "GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub",
            "url": "https://github.com/lucidrains/pi-zero-pytorch"
          },
          {
            "title": "GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub",
            "url": "https://github.com/allenzren/open-pi-zero"
          },
          {
            "title": "π0 and π0-FAST: Vision-Language-Action Models for General Robot Control",
            "url": "https://huggingface.co/blog/pi0"
          },
          {
            "title": "Physical Intelligence π0 vs OpenVLA: Best VLA Model for Robot Learning 2026 | SVRC",
            "url": "https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla"
          },
          {
            "title": "Physical Intelligence Unveils Robotics Foundation Model Pi-Zero - InfoQ",
            "url": "https://www.infoq.com/news/2024/12/pi-zero-robot/"
          },
          {
            "title": "π 0 : Our First Generalist Policy",
            "url": "https://www.pi.website/blog/pi0"
          },
          {
            "title": "DM0: An Embodied-Native Vision-Language-Action Model towards Physical AI",
            "url": "https://arxiv.org/pdf/2602.14974"
          },
          {
            "title": "Our First Generalist Policy",
            "url": "https://physicalintelligence.company/blog/pi0"
          }
        ]
      },
      "Based on the search results, here's what I found about π0 (pi-zero), Physical Intelligence's VLA architecture from 2024:\n\n## Overview\n\nπ0 (Pi-Zero) is a Vision-Language-Action (VLA) model developed by the Physical Intelligence team designed for generalist robot control. Physical Intelligence recently announced π0 as a general-purpose AI foundation model for robots that is based on a pre-trained vision-language model (VLM) and outperforms other baseline models in evaluations on five robot tasks.\n\n## Architecture\n\nπ0 combines large-scale multi-task and multi-robot data collection with a new network architecture to enable the most capable and dexterous generalist robot policy to date. The architecture incorporates mixture of experts (MoE) and block-attention components, and the PiZero class follows the original Pi0 architecture, while the underlying JointModel and Mixture classes form a general instantiation of the MoE + block-attention architecture.\n\n## Performance\n\nπ0 is by far the best-performing model across all tested tasks, with more than a 2x improvement in performance from using the full-size architecture with VLM pre-training compared to the smaller π0-small version.\n\n## Access\n\nπ0 from Physical Intelligence delivers state-of-the-art dexterity performance but requires partnership access and cannot be self-hosted."
    ],
    "durationSeconds": 6.273554522999999
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T16:21:42.189Z_

<details><summary>↩ Tool result · `toolu_01JoNvhjAdW4U7jQYdSrK57Z`</summary>

```text
Web search results for query: "vision language action model open source weights 2024 2025 decoder-only robot"

Links: [{"title":"Open-Weight Foundation Models for Robotics (2025 Guide) | RoboCloud Hub","url":"https://robocloud-dashboard.vercel.app/learn/blog/open-weight-robot-models"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://proceedings.mlr.press/v270/kim25c.html"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"}]

Based on the search results, here are the key open-source vision-language-action (VLA) models with publicly available weights released in 2024-2025:

## OpenVLA

OpenVLA was released in January 2025 by UC Berkeley and is the first commercially-usable, open-weight Vision-Language-Action model. It is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.

## Octo

Octo (Stanford, December 2024) takes a different approach than OpenVLA, using a diffusion policy to generate smooth, continuous trajectories instead of outputting discrete action tokens. It combines a transformer encoder (for visual reasoning) with a diffusion decoder (for smooth action generation), offering both semantic understanding and natural motion.

## Other Notable Models

π0 (pi-zero) is a large-scale generalist VLA announced in late 2024 by the startup Physical Intelligence, incorporating Paligemma as a pre-trained VLM backbone with an action expert trained on robot trajectories from Open X-Embodiment.

The search results indicate these are leading decoder-based or diffusion-based approaches designed for robotic manipulation tasks with publicly available weights.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "f403cbee-e574-4dad-945b-32ac4fa59668",
  "tool_use_result": {
    "query": "vision language action model open source weights 2024 2025 decoder-only robot",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Tdu8HAiXGkiNhxpWXvrGoi",
        "content": [
          {
            "title": "Open-Weight Foundation Models for Robotics (2025 Guide) | RoboCloud Hub",
            "url": "https://robocloud-dashboard.vercel.app/learn/blog/open-weight-robot-models"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://proceedings.mlr.press/v270/kim25c.html"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model",
            "url": "https://arxiv.org/pdf/2604.05672"
          }
        ]
      },
      "Based on the search results, here are the key open-source vision-language-action (VLA) models with publicly available weights released in 2024-2025:\n\n## OpenVLA\n\nOpenVLA was released in January 2025 by UC Berkeley and is the first commercially-usable, open-weight Vision-Language-Action model. It is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.\n\n## Octo\n\nOcto (Stanford, December 2024) takes a different approach than OpenVLA, using a diffusion policy to generate smooth, continuous trajectories instead of outputting discrete action tokens. It combines a transformer encoder (for visual reasoning) with a diffusion decoder (for smooth action generation), offering both semantic understanding and natural motion.\n\n## Other Notable Models\n\nπ0 (pi-zero) is a large-scale generalist VLA announced in late 2024 by the startup Physical Intelligence, incorporating Paligemma as a pre-trained VLM backbone with an action expert trained on robot trajectories from Open X-Embodiment.\n\nThe search results indicate these are leading decoder-based or diffusion-based approaches designed for robotic manipulation tasks with publicly available weights."
    ],
    "durationSeconds": 8.929871631000001
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T16:21:43.320Z_

<details><summary>↩ Tool result · `toolu_015hphq5cL2SmNZGEW7YoRYU`</summary>

```text
Web search results for query: "RT-2 open source implementation VLA decoder-only weights"

Links: [{"title":"RT-2, Robotic Transformer 2 Review | gracefullight.dev","url":"https://gracefullight.dev/en/2025/08/24/rt-2-review/"},{"title":"[Robotics] RT-2: Vision-Language-Action Models | by Ming-Hao Hsu | Medium","url":"https://medium.com/@amiable_cardinal_crocodile_398/robotics-rt-2-vision-language-action-models-8db0c197d02"},{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"OpenVLA to RT-2-X is what Llama-3 is to GPT-4 - TechTalks","url":"https://bdtechtalks.substack.com/p/openvla-to-rt-2-x-is-what-llama-3"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic   Control","url":"https://arxiv.org/pdf/2307.15818"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"},{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/learn/vla-models-comparison"}]

Based on the search results, here's what I found regarding RT-2 open source implementation and VLA decoder-only weights:

## RT-2 Availability

Google has not released weights or training code for RT-2. The state-of-the-art VLA models, such as RT-2 and RT-2-X, are not open and their data and training code are not available for others to build on.

## Open Source Alternative: OpenVLA

While RT-2 itself is closed source, OpenVLA is an open-source generalist robotics model that addresses these shortcomings. The foundation for OpenVLA is Prismatic-7B, a VLM that uses a two-part visual encoder for extracting features from input images and a Llama-2 7B model to process language instructions. The researchers have open-sourced all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale.

## VLA Architecture Details

Regarding the decoder-only architecture for VLAs: The simplest implementations of VLAs discretize actions so the model can predict them as tokens in its vocabulary. The actions are trained and decoded autoregressively, with discretized tokens added to the model's vocabulary.

If you're looking for an open source VLA implementation with available weights, OpenVLA would be the recommended alternative to RT-2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "b79faf67-1023-40c8-ae28-d3e18df4e4e2",
  "tool_use_result": {
    "query": "RT-2 open source implementation VLA decoder-only weights",
    "results": [
      {
        "tool_use_id": "srvtoolu_012JZkKQbUQxDSai2ApEL4KF",
        "content": [
          {
            "title": "RT-2, Robotic Transformer 2 Review | gracefullight.dev",
            "url": "https://gracefullight.dev/en/2025/08/24/rt-2-review/"
          },
          {
            "title": "[Robotics] RT-2: Vision-Language-Action Models | by Ming-Hao Hsu | Medium",
            "url": "https://medium.com/@amiable_cardinal_crocodile_398/robotics-rt-2-vision-language-action-models-8db0c197d02"
          },
          {
            "title": "RT-2: Vision-Language-Action Models",
            "url": "https://robotics-transformer2.github.io/"
          },
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "OpenVLA to RT-2-X is what Llama-3 is to GPT-4 - TechTalks",
            "url": "https://bdtechtalks.substack.com/p/openvla-to-rt-2-x-is-what-llama-3"
          },
          {
            "title": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic   Control",
            "url": "https://arxiv.org/pdf/2307.15818"
          },
          {
            "title": "Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
            "url": "https://huggingface.co/papers/2307.15818"
          },
          {
            "title": "VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC",
            "url": "https://www.roboticscenter.ai/learn/vla-models-comparison"
          }
        ]
      },
      "Based on the search results, here's what I found regarding RT-2 open source implementation and VLA decoder-only weights:\n\n## RT-2 Availability\n\nGoogle has not released weights or training code for RT-2. The state-of-the-art VLA models, such as RT-2 and RT-2-X, are not open and their data and training code are not available for others to build on.\n\n## Open Source Alternative: OpenVLA\n\nWhile RT-2 itself is closed source, OpenVLA is an open-source generalist robotics model that addresses these shortcomings. The foundation for OpenVLA is Prismatic-7B, a VLM that uses a two-part visual encoder for extracting features from input images and a Llama-2 7B model to process language instructions. The researchers have open-sourced all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale.\n\n## VLA Architecture Details\n\nRegarding the decoder-only architecture for VLAs: The simplest implementations of VLAs discretize actions so the model can predict them as tokens in its vocabulary. The actions are trained and decoded autoregressively, with discretized tokens added to the model's vocabulary.\n\nIf you're looking for an open source VLA implementation with available weights, OpenVLA would be the recommended alternative to RT-2."
    ],
    "durationSeconds": 8.935942245000001
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T16:21:44.366Z_

<details><summary>↩ Tool result · `toolu_01LXbJXutLYpnF5Hq8cu2LNQ`</summary>

```text
Web search results for query: "robot foundation model decoder-only transformer action prediction 2024 2025 open source"

Links: [{"title":"Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions","url":"https://arxiv.org/html/2604.15395v1"},{"title":"Foundation Models for Robot Manipulation: RT-2, OpenVLA, Octo, and π0 | SVRC","url":"https://www.roboticscenter.ai/research/foundation-models-robot-manipulation-2025"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - Argo-Robot/foundation_models: Overview about state-of-art imitation learning techniques for robotic manipulation, enabling generalization across diverse tasks and environments. · GitHub","url":"https://github.com/Argo-Robot/foundation_models"},{"title":"Research on Robotics Diffusion Transformer in Robot Foundation Models Based on Diffusion Model | Proceedings of the 2025 4th International Conference on Intelligent Systems, Communications and Computer Networks","url":"https://dl.acm.org/doi/10.1145/3732945.3733004"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control","url":"https://arxiv.org/pdf/2603.10448"}]

Based on the web search results, here are the key findings regarding robot foundation models with decoder-only transformers and action prediction in 2024-2025:

## Open-Source Models

OpenVLA (Stanford + UC Berkeley, 2024) is the leading open-weight robot foundation model as of 2025, based on a 7B parameter LLaMA-2 language model with a DINOv2 + SigLIP vision encoder. Model weights are published on HuggingFace (openvla/openvla-7b).

Octo (Berkeley, 2024) takes a different architectural approach with a smaller transformer model with a diffusion policy action head, trained entirely on robot data. Its architecture includes a transformer observation encoder (images + proprioception + language) + diffusion action head with ~93M parameters. Octo is fully open-source.

## Decoder-Only Transformers

Decoder-only models (such as PaLM and GPT-4) benefit from scale, improving robotic reasoning and planning performance in robotics applications.

## Action Prediction Approaches

The simplest implementations of VLAs discretize actions so the model can predict them as tokens in its vocabulary. OpenVLA uses action output via tokenized discretization (256 bins).

π0 (pi-zero) introduced a flow-matching model to generate high-frequency continuous actions, up to 50 Hz, while the action head takes advantage of a diffusion policy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "fb2d92e1-6307-438a-97b2-a75cd1195ef9",
  "tool_use_result": {
    "query": "robot foundation model decoder-only transformer action prediction 2024 2025 open source",
    "results": [
      {
        "tool_use_id": "srvtoolu_016EqzrpSPnETRVFPeC7MPsa",
        "content": [
          {
            "title": "Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions",
            "url": "https://arxiv.org/html/2604.15395v1"
          },
          {
            "title": "Foundation Models for Robot Manipulation: RT-2, OpenVLA, Octo, and π0 | SVRC",
            "url": "https://www.roboticscenter.ai/research/foundation-models-robot-manipulation-2025"
          },
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "GitHub - Argo-Robot/foundation_models: Overview about state-of-art imitation learning techniques for robotic manipulation, enabling generalization across diverse tasks and environments. · GitHub",
            "url": "https://github.com/Argo-Robot/foundation_models"
          },
          {
            "title": "Research on Robotics Diffusion Transformer in Robot Foundation Models Based on Diffusion Model | Proceedings of the 2025 4th International Conference on Intelligent Systems, Communications and Computer Networks",
            "url": "https://dl.acm.org/doi/10.1145/3732945.3733004"
          },
          {
            "title": "Physical Intelligence open-sources Pi0 robotics foundation model",
            "url": "https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"
          },
          {
            "title": "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/pdf/2503.14734"
          },
          {
            "title": "DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control",
            "url": "https://arxiv.org/pdf/2603.10448"
          }
        ]
      },
      "Based on the web search results, here are the key findings regarding robot foundation models with decoder-only transformers and action prediction in 2024-2025:\n\n## Open-Source Models\n\nOpenVLA (Stanford + UC Berkeley, 2024) is the leading open-weight robot foundation model as of 2025, based on a 7B parameter LLaMA-2 language model with a DINOv2 + SigLIP vision encoder. Model weights are published on HuggingFace (openvla/openvla-7b).\n\nOcto (Berkeley, 2024) takes a different architectural approach with a smaller transformer model with a diffusion policy action head, trained entirely on robot data. Its architecture includes a transformer observation encoder (images + proprioception + language) + diffusion action head with ~93M parameters. Octo is fully open-source.\n\n## Decoder-Only Transformers\n\nDecoder-only models (such as PaLM and GPT-4) benefit from scale, improving robotic reasoning and planning performance in robotics applications.\n\n## Action Prediction Approaches\n\nThe simplest implementations of VLAs discretize actions so the model can predict them as tokens in its vocabulary. OpenVLA uses action output via tokenized discretization (256 bins).\n\nπ0 (pi-zero) introduced a flow-matching model to generate high-frequency continuous actions, up to 50 Hz, while the action head takes advantage of a diffusion policy."
    ],
    "durationSeconds": 8.722813529000002
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Good, I have initial results. Let me now do more targeted searches for specific candidates that look promising:

1. **SmolVLA** - 450M params, by HuggingFace - need to check architecture
2. **π0 open source** - there are open-source re-implementations
3. **OpenVLA-OFT or OpenVLA v2** - any variants?
4. **GR00T-N1** - NVIDIA's model
5. **RDT-1b** - diffusion transformer
6. **A1** - mentioned in first search result
7. **DeeR-VLA** or other decoder-only VLAs


Now I'm diving deeper into the details on each of these candidates to see which ones actually fit the criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "6b9a664e-99e6-4c5d-92d4-663412ceceef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLw5jstkdA1YC4UEvTig5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4103,
      "cache_read_input_tokens": 24818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4103
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

_source line 20_

找到初步候选列表，继续深入搜索具体架构信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "9e1c88bf-8df8-4541-a714-650c2fd82d61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLw5jstkdA1YC4UEvTig5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4103,
      "cache_read_input_tokens": 24818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4103
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

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QSinN7UdA7cYon1dJ3dYaf`</summary>

```json
{
  "query": "SmolVLA architecture decoder-only huggingface 2025 backbone model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "ccd86396-9469-4a18-a22c-45aba9ead208",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLw5jstkdA1YC4UEvTig5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4103,
      "cache_read_input_tokens": 24818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4103
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

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DkZr9TtV21wc4GxbXkN8fW`</summary>

```json
{
  "query": "pi0 open source weights huggingface \"open-pi-zero\" architecture decoder-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "07b34a9d-f18d-4af2-a9d5-bc387a2f07e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLw5jstkdA1YC4UEvTig5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4103,
      "cache_read_input_tokens": 24818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4103
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

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018CwCFDL6j7fkYoMQi85GXz`</summary>

```json
{
  "query": "OpenVLA-v2 OpenVLA-OFT \"OpenVLA 2\" variant different backbone 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "78a27cc0-a97b-4ec1-8d45-08e42c4137ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLw5jstkdA1YC4UEvTig5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4103,
      "cache_read_input_tokens": 24818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4103
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

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019RKT87dCLdNHPNhYRF24ce`</summary>

```json
{
  "query": "GR00T-N1 NVIDIA architecture decoder-only VLA open weights huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "cbf0f3c6-83c6-4896-a8b8-af762a449f47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLw5jstkdA1YC4UEvTig5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4103,
      "cache_read_input_tokens": 24818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4103
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

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xb6DX3yqY6NsrFScGTVyu3`</summary>

```json
{
  "query": "\"A1\" VLA model \"truncated\" vision language action 2025 architecture open weights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "6f318f2b-2385-48e4-ae2f-18ab07bd2a59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLw5jstkdA1YC4UEvTig5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4103,
      "cache_read_input_tokens": 24818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4103
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

### Tool result

_source line 26 · 2026-05-19T16:22:00.280Z_

<details><summary>↩ Tool result · `toolu_01DkZr9TtV21wc4GxbXkN8fW`</summary>

```text
Web search results for query: "pi0 open source weights huggingface "open-pi-zero" architecture decoder-only"

Links: [{"title":"Open Sourcing π0","url":"https://www.pi.website/blog/openpi"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"},{"title":"memevis/PI0 · Hugging Face","url":"https://huggingface.co/memevis/PI0"},{"title":"π0 and π0-FAST: Vision-Language-Action Models for General Robot Control","url":"https://huggingface.co/blog/pi0"},{"title":"allenzren/open-pi-zero · Hugging Face","url":"https://huggingface.co/allenzren/open-pi-zero"},{"title":"GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub","url":"https://github.com/allenzren/open-pi-zero"},{"title":"π₀ (Pi0) · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi0"},{"title":"lerobot/pi0_base · Hugging Face","url":"https://huggingface.co/lerobot/pi0_base"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"README.md · lerobot/pi0_base at main","url":"https://huggingface.co/lerobot/pi0_base/blob/main/README.md"}]

Based on the search results, here's what I found about π0 (Pi-Zero) and the related open-source resources:

## π0 Overview

π0 (Pi-Zero) is a Vision-Language-Action (VLA) model developed by the Physical Intelligence team designed for generalist robot control.

## Open Source Release

Physical Intelligence has released the code and weights for Pi0 as part of its experimental openpi repository on GitHub, providing checkpoints for simple tasks on available platforms such as ALOHA and DROID, along with example code and fine-tuning code.

HuggingFace has also prepared a PyTorch port of openpi for developers who prefer PyTorch over JAX.

## Model Variants

Pi0 base is the standard pre-trained model trained on OXE and 7 of Physical Intelligence's robot platforms, designed for fine-tuning though it can be used in zero shot for tasks present in the pre-training data.

Pi0-FAST uses the FAST tokenizer to enable control via autoregressive discretization and provides somewhat better language following performance, but has higher inference cost (about 4-5x higher).

## "open-pi-zero" Repository

The allenzren/open-pi-zero repository is a re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence. The model adopts a MoE-like architecture using a pre-trained 3B PaliGemma VLM and a new set of action expert parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "4915dfea-21d0-4103-b5cf-15a27600cf73",
  "tool_use_result": {
    "query": "pi0 open source weights huggingface \"open-pi-zero\" architecture decoder-only",
    "results": [
      {
        "tool_use_id": "srvtoolu_012gJemnd3cbLwhDYcTRXmWo",
        "content": [
          {
            "title": "Open Sourcing π0",
            "url": "https://www.pi.website/blog/openpi"
          },
          {
            "title": "Physical Intelligence open-sources Pi0 robotics foundation model",
            "url": "https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"
          },
          {
            "title": "memevis/PI0 · Hugging Face",
            "url": "https://huggingface.co/memevis/PI0"
          },
          {
            "title": "π0 and π0-FAST: Vision-Language-Action Models for General Robot Control",
            "url": "https://huggingface.co/blog/pi0"
          },
          {
            "title": "allenzren/open-pi-zero · Hugging Face",
            "url": "https://huggingface.co/allenzren/open-pi-zero"
          },
          {
            "title": "GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub",
            "url": "https://github.com/allenzren/open-pi-zero"
          },
          {
            "title": "π₀ (Pi0) · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/pi0"
          },
          {
            "title": "lerobot/pi0_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi0_base"
          },
          {
            "title": "GitHub - Physical-Intelligence/openpi · GitHub",
            "url": "https://github.com/Physical-Intelligence/openpi"
          },
          {
            "title": "README.md · lerobot/pi0_base at main",
            "url": "https://huggingface.co/lerobot/pi0_base/blob/main/README.md"
          }
        ]
      },
      "Based on the search results, here's what I found about π0 (Pi-Zero) and the related open-source resources:\n\n## π0 Overview\n\nπ0 (Pi-Zero) is a Vision-Language-Action (VLA) model developed by the Physical Intelligence team designed for generalist robot control.\n\n## Open Source Release\n\nPhysical Intelligence has released the code and weights for Pi0 as part of its experimental openpi repository on GitHub, providing checkpoints for simple tasks on available platforms such as ALOHA and DROID, along with example code and fine-tuning code.\n\nHuggingFace has also prepared a PyTorch port of openpi for developers who prefer PyTorch over JAX.\n\n## Model Variants\n\nPi0 base is the standard pre-trained model trained on OXE and 7 of Physical Intelligence's robot platforms, designed for fine-tuning though it can be used in zero shot for tasks present in the pre-training data.\n\nPi0-FAST uses the FAST tokenizer to enable control via autoregressive discretization and provides somewhat better language following performance, but has higher inference cost (about 4-5x higher).\n\n## \"open-pi-zero\" Repository\n\nThe allenzren/open-pi-zero repository is a re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence. The model adopts a MoE-like architecture using a pre-trained 3B PaliGemma VLM and a new set of action expert parameters."
    ],
    "durationSeconds": 7.9103773770000005
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T16:22:00.799Z_

<details><summary>↩ Tool result · `toolu_019RKT87dCLdNHPNhYRF24ce`</summary>

```text
Web search results for query: "GR00T-N1 NVIDIA architecture decoder-only VLA open weights huggingface"

Links: [{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v1"},{"title":"nvidia/GR00T-N1.6-3B · Hugging Face","url":"https://huggingface.co/nvidia/GR00T-N1.6-3B"},{"title":"NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots","url":"https://huggingface.co/blog/nvidia/gr00t-n1-7"},{"title":"README.md · nvidia/GR00T-N1.6-3B at main","url":"https://huggingface.co/nvidia/GR00T-N1.6-3B/blob/main/README.md"},{"title":"nvidia/GR00T-N1-2B · Hugging Face","url":"https://huggingface.co/nvidia/GR00T-N1-2B"},{"title":"Accelerate Generalist Humanoid Robot Development with NVIDIA Isaac GR00T N1 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/"},{"title":"GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub","url":"https://github.com/NVIDIA/Isaac-GR00T"},{"title":"GitHub - NVIDIA-Medtech/GR00T-H: Gr00t-H · GitHub","url":"https://github.com/NVIDIA-Medtech/GR00T-H"}]

Based on the search results, here's what I found about GR00T-N1:

GR00T N1 is an open foundation model for generalist humanoid robots that is a Vision-Language-Action (VLA) model, which generates actions from image and language instruction input.

**Architecture Details:**

The neural network architecture of GR00T N1.6 is a combination of vision-language foundation model and diffusion transformer head that denoises continuous actions. More specifically, it uses vision and text transformers to encode the robot's image observations and text instructions.

The model uses a pre-trained vision transformer (SigLip2) for processing RGB camera frames and a pre-trained transformer (T5) for encoding text.

**Open Weights & HuggingFace:**

The GR00T-N1-2B model checkpoint, training data, and simulation benchmarks are publicly available on GitHub and HuggingFace Datasets. The models are available on HuggingFace under the NVIDIA organization, with versions like GR00T-N1-2B and GR00T-N1.6-3B available.

**Note:** The search results indicate that GR00T-N1 uses a **diffusion transformer** architecture rather than a pure decoder-only transformer. The model processes visual and language information through separate encoders and then uses a flow-matching diffusion transformer for action generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "b1f4f182-e26a-4a55-a10f-6f67532653fd",
  "tool_use_result": {
    "query": "GR00T-N1 NVIDIA architecture decoder-only VLA open weights huggingface",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y3vu9xA1f8ivwCxQfW39y5",
        "content": [
          {
            "title": "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/html/2503.14734v1"
          },
          {
            "title": "nvidia/GR00T-N1.6-3B · Hugging Face",
            "url": "https://huggingface.co/nvidia/GR00T-N1.6-3B"
          },
          {
            "title": "NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots",
            "url": "https://huggingface.co/blog/nvidia/gr00t-n1-7"
          },
          {
            "title": "README.md · nvidia/GR00T-N1.6-3B at main",
            "url": "https://huggingface.co/nvidia/GR00T-N1.6-3B/blob/main/README.md"
          },
          {
            "title": "nvidia/GR00T-N1-2B · Hugging Face",
            "url": "https://huggingface.co/nvidia/GR00T-N1-2B"
          },
          {
            "title": "Accelerate Generalist Humanoid Robot Development with NVIDIA Isaac GR00T N1 | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/"
          },
          {
            "title": "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub",
            "url": "https://github.com/NVIDIA/Isaac-GR00T"
          },
          {
            "title": "GitHub - NVIDIA-Medtech/GR00T-H: Gr00t-H · GitHub",
            "url": "https://github.com/NVIDIA-Medtech/GR00T-H"
          }
        ]
      },
      "Based on the search results, here's what I found about GR00T-N1:\n\nGR00T N1 is an open foundation model for generalist humanoid robots that is a Vision-Language-Action (VLA) model, which generates actions from image and language instruction input.\n\n**Architecture Details:**\n\nThe neural network architecture of GR00T N1.6 is a combination of vision-language foundation model and diffusion transformer head that denoises continuous actions. More specifically, it uses vision and text transformers to encode the robot's image observations and text instructions.\n\nThe model uses a pre-trained vision transformer (SigLip2) for processing RGB camera frames and a pre-trained transformer (T5) for encoding text.\n\n**Open Weights & HuggingFace:**\n\nThe GR00T-N1-2B model checkpoint, training data, and simulation benchmarks are publicly available on GitHub and HuggingFace Datasets. The models are available on HuggingFace under the NVIDIA organization, with versions like GR00T-N1-2B and GR00T-N1.6-3B available.\n\n**Note:** The search results indicate that GR00T-N1 uses a **diffusion transformer** architecture rather than a pure decoder-only transformer. The model processes visual and language information through separate encoders and then uses a flow-matching diffusion transformer for action generation."
    ],
    "durationSeconds": 6.914791909
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T16:22:01.016Z_

<details><summary>↩ Tool result · `toolu_018CwCFDL6j7fkYoMQi85GXz`</summary>

```text
Web search results for query: "OpenVLA-v2 OpenVLA-OFT "OpenVLA 2" variant different backbone 2025"

Links: [{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"A Comprehensive Overview of Vision-Language-Action Models | DigitalOcean","url":"https://www.digitalocean.com/community/conceptual-articles/vision-language-action-models"}]

Based on the search results, here's what I found about OpenVLA variants and backbones:

## OpenVLA Backbone Architecture

OpenVLA's model consists of a fused visual encoder with SigLIP and DinoV2 backbones, a projector that maps visual encoder outputs to a language model's input space, and a Llama 2 7B language model backbone.

## OpenVLA-OFT (2025)

In March 2025, the OpenVLA team recommended trying the new OFT recipe for fine-tuning OpenVLA to produce faster and more successful policies. Through parallel decoding and action chunking, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model.

The search results mention "OpenVLA-OFT+" as a variant tested alongside other models like RDT-1B and π0, but they don't indicate that OpenVLA-OFT uses a fundamentally different language backbone compared to the original 7B model. The OFT variant appears to be a fine-tuning recipe and inference optimization rather than a variant with a different backbone architecture.

The search results do not contain specific information about an "OpenVLA-v2" release or details about variants with different language backbones released in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "c3d86094-3f3d-4e06-8c72-0df5620149a7",
  "tool_use_result": {
    "query": "OpenVLA-v2 OpenVLA-OFT \"OpenVLA 2\" variant different backbone 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Cih1wz6ggXsbHxEfcjkq2y",
        "content": [
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "Understanding OpenVLA: A Simple Guide - Hankyu Kim",
            "url": "https://hankyukim.com/openvla/"
          },
          {
            "title": "OpenVLA-OFT",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "A Comprehensive Overview of Vision-Language-Action Models | DigitalOcean",
            "url": "https://www.digitalocean.com/community/conceptual-articles/vision-language-action-models"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA variants and backbones:\n\n## OpenVLA Backbone Architecture\n\nOpenVLA's model consists of a fused visual encoder with SigLIP and DinoV2 backbones, a projector that maps visual encoder outputs to a language model's input space, and a Llama 2 7B language model backbone.\n\n## OpenVLA-OFT (2025)\n\nIn March 2025, the OpenVLA team recommended trying the new OFT recipe for fine-tuning OpenVLA to produce faster and more successful policies. Through parallel decoding and action chunking, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model.\n\nThe search results mention \"OpenVLA-OFT+\" as a variant tested alongside other models like RDT-1B and π0, but they don't indicate that OpenVLA-OFT uses a fundamentally different language backbone compared to the original 7B model. The OFT variant appears to be a fine-tuning recipe and inference optimization rather than a variant with a different backbone architecture.\n\nThe search results do not contain specific information about an \"OpenVLA-v2\" release or details about variants with different language backbones released in 2025."
    ],
    "durationSeconds": 7.7035243300000005
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T16:22:01.803Z_

<details><summary>↩ Tool result · `toolu_01QSinN7UdA7cYon1dJ3dYaf`</summary>

```text
Web search results for query: "SmolVLA architecture decoder-only huggingface 2025 backbone model"

Links: [{"title":"blog/smolvla.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/smolvla.md"},{"title":"SmolVLM · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/smolvlm"},{"title":"Hugging Face Releases SmolVLA, a Compact Open-Source Robotics Model -- Pure AI","url":"https://pureai.com/articles/2025/06/10/hugging-face-releases-smolvla.aspx"},{"title":"AI and Robotics: With SmolVLA, Hugging Face Opens Vision-Language-Action Models to the Community","url":"https://www.actuia.com/en/news/ai-and-robotics-with-smolvla-hugging-face-opens-vision-language-action-models-to-the-community/"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Select the VLM backbone for SmolVLA · Issue #2104 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2104"}]

Based on the search results, here's what I found about SmolVLA's architecture:

## SmolVLA Architecture Overview

SmolVLA consists of two core components: a Vision-Language Model (VLM) that processes multimodal inputs and an action expert that outputs robot control commands.

## Backbone Model

SmolVLA uses SmolVLM2 as its VLM backbone, which is optimized for multi-image inputs and consists of a SigLIP vision encoder and a SmolLM2 language decoder.

## Decoder Architecture

Regarding the decoder-only aspect: The SmolLM2 language decoder works with the SigLIP visual encoder, allowing the system to decipher the robot's visual environment and generate understanding in natural language. The decoder layers process concatenated image, language, and state tokens.

## Action Expert Component

The Action Expert is a 100 million parameter transformer that predicts the actions the robot should take, based on information provided by the VLM. SmolVLA employs an interleaved approach in the action expert, where each block contains either a cross-attention or self-attention layer.

## Model Size

SmolVLA has less than 0.5 billion parameters, allowing for fast inference on consumer-grade hardware.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "1bd14c8a-1451-4702-9f2a-cbc18f4d72df",
  "tool_use_result": {
    "query": "SmolVLA architecture decoder-only huggingface 2025 backbone model",
    "results": [
      {
        "tool_use_id": "srvtoolu_017XadRGr46fF1SwvcCwRmCu",
        "content": [
          {
            "title": "blog/smolvla.md at main · huggingface/blog",
            "url": "https://github.com/huggingface/blog/blob/main/smolvla.md"
          },
          {
            "title": "SmolVLM · Hugging Face",
            "url": "https://huggingface.co/docs/transformers/model_doc/smolvlm"
          },
          {
            "title": "Hugging Face Releases SmolVLA, a Compact Open-Source Robotics Model -- Pure AI",
            "url": "https://pureai.com/articles/2025/06/10/hugging-face-releases-smolvla.aspx"
          },
          {
            "title": "AI and Robotics: With SmolVLA, Hugging Face Opens Vision-Language-Action Models to the Community",
            "url": "https://www.actuia.com/en/news/ai-and-robotics-with-smolvla-hugging-face-opens-vision-language-action-models-to-the-community/"
          },
          {
            "title": "Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "Select the VLM backbone for SmolVLA · Issue #2104 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2104"
          }
        ]
      },
      "Based on the search results, here's what I found about SmolVLA's architecture:\n\n## SmolVLA Architecture Overview\n\nSmolVLA consists of two core components: a Vision-Language Model (VLM) that processes multimodal inputs and an action expert that outputs robot control commands.\n\n## Backbone Model\n\nSmolVLA uses SmolVLM2 as its VLM backbone, which is optimized for multi-image inputs and consists of a SigLIP vision encoder and a SmolLM2 language decoder.\n\n## Decoder Architecture\n\nRegarding the decoder-only aspect: The SmolLM2 language decoder works with the SigLIP visual encoder, allowing the system to decipher the robot's visual environment and generate understanding in natural language. The decoder layers process concatenated image, language, and state tokens.\n\n## Action Expert Component\n\nThe Action Expert is a 100 million parameter transformer that predicts the actions the robot should take, based on information provided by the VLM. SmolVLA employs an interleaved approach in the action expert, where each block contains either a cross-attention or self-attention layer.\n\n## Model Size\n\nSmolVLA has less than 0.5 billion parameters, allowing for fast inference on consumer-grade hardware."
    ],
    "durationSeconds": 10.382650021999998
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T16:22:02.263Z_

<details><summary>↩ Tool result · `toolu_01Xb6DX3yqY6NsrFScGTVyu3`</summary>

```text
Web search results for query: ""A1" VLA model "truncated" vision language action 2025 architecture open weights"

Links: [{"title":"𝐴₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/html/2604.05672"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment","url":"https://arxiv.org/pdf/2511.04555"}]

Based on the search results, here's what I found about the A1 VLA model:

## Overview

A₁ is a fully open-source and transparent Vision-Language-Action (VLA) framework designed for low-cost, high-throughput inference without sacrificing manipulation success, leveraging pretrained VLMs that provide implicit affordance priors for action generation.

## Key Architecture Features

The model uses Inter-Layer Truncated Flow Matching that warm-starts denoising across intermediate layers. A₁ targets the full inference pipeline by introducing a budget-aware adaptive inference scheme that jointly accelerates the backbone and the action head.

## Open-Source Commitment

The project releases the full training stack including training code, data/data-processing pipeline, intermediate checkpoints, and evaluation scripts to enable end-to-end reproducibility.

## Training Data

A₁ is trained using open-source robotic datasets including DROID, AgiBot, RoboCOIN, RoboMind, GM-100, and RoboChallenge.

## Performance

The joint design accelerates both components of the VLA pipeline, yielding substantial wall-clock savings (e.g., 37.8s to 10.5s per episode on LIBERO for flow-matching inference) while maintaining success rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "84abd0da-5a03-46cb-bafb-1f6a0681cae8",
  "tool_use_result": {
    "query": "\"A1\" VLA model \"truncated\" vision language action 2025 architecture open weights",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EuNLrpjBkd5YMu4NryUDJJ",
        "content": [
          {
            "title": "𝐴₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2604.05672"
          },
          {
            "title": "A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model",
            "url": "https://arxiv.org/pdf/2604.05672"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment",
            "url": "https://arxiv.org/pdf/2511.04555"
          }
        ]
      },
      "Based on the search results, here's what I found about the A1 VLA model:\n\n## Overview\n\nA₁ is a fully open-source and transparent Vision-Language-Action (VLA) framework designed for low-cost, high-throughput inference without sacrificing manipulation success, leveraging pretrained VLMs that provide implicit affordance priors for action generation.\n\n## Key Architecture Features\n\nThe model uses Inter-Layer Truncated Flow Matching that warm-starts denoising across intermediate layers. A₁ targets the full inference pipeline by introducing a budget-aware adaptive inference scheme that jointly accelerates the backbone and the action head.\n\n## Open-Source Commitment\n\nThe project releases the full training stack including training code, data/data-processing pipeline, intermediate checkpoints, and evaluation scripts to enable end-to-end reproducibility.\n\n## Training Data\n\nA₁ is trained using open-source robotic datasets including DROID, AgiBot, RoboCOIN, RoboMind, GM-100, and RoboChallenge.\n\n## Performance\n\nThe joint design accelerates both components of the VLA pipeline, yielding substantial wall-clock savings (e.g., 37.8s to 10.5s per episode on LIBERO for flow-matching inference) while maintaining success rate."
    ],
    "durationSeconds": 7.8873958239999995
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Good progress. Let me now get more specific details about the most promising candidates:

1. **π0 / openpi** - officially open-sourced, uses PaliGemma (3B) as VLM backbone with action expert. Architecture uses cross-attention between VLM and action expert (MoE-like), NOT purely decoder-only. But π0-FAST uses autoregressive discretization...
2. **SmolVLA** - uses SmolLM2 as backbone, action expert with cross-attention. Not purely decoder-only.


3. **GR00T-N1** - encoder-decoder with SigLip2, T5, and diffusion transformer, so that's not decoder-only either.
4. **A1** - still need to dig into its architecture details.
5. **OpenVLA-OFT** - same Llama-2 backbone as OpenVLA, just a different fine-tuning approach.

Now I'm looking for candidates that are actually decoder-only architectures. Let me check CogACT, DeeR-VLA, 3D-VLA, HPT, RoboVLM, TraceVLA, SpatialVLA, and any Qwen-based models to see which ones fit that constraint.

Actually, I need to be more precise about what decoder-only means here. The architecture needs a causal LLM backbone where vision and action tokens all flow through the same decoder with causal masking—like OpenVLA does, where images get encoded and projected into the LLM's input space, then processed end-to-end by Llama-2. Models like π0 use separate action experts with cross-attention, which breaks that pure decoder-only pattern. Let me search more systematically for VLAs that actually follow this decoder-only design.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "9b36a943-a7bd-4b57-a9ab-4ffa5783d223",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1UhLyYRXtqr2HksN5Lhwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 28921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4242
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

_source line 32_

需要更精确地搜索 decoder-only 架构的候选。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "665d219a-4b4a-41d6-83ee-4c40486cd5f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1UhLyYRXtqr2HksN5Lhwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 28921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4242
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

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Azi4VA9wcjZvruruRHmZUK`</summary>

```json
{
  "query": "CogACT VLA decoder-only action tokenization 2024 open source weights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "8b9a4ada-aabc-4615-9b20-a08f48dbf5b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1UhLyYRXtqr2HksN5Lhwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 28921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4242
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

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sy4s986GnkJkkdwjX75pPH`</summary>

```json
{
  "query": "SpatialVLA TraceVLA RoboVLM decoder-only VLA 2024 2025 open weights huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "d30c4a6a-40fb-4936-85f2-7d5e8bb1fca5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1UhLyYRXtqr2HksN5Lhwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 28921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4242
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

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LueMi8AKFBHU5QR2Px47n8`</summary>

```json
{
  "query": "DeeR-VLA 3D-VLA decoder-only architecture open source weights 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "1515b52d-201c-4400-b381-38694a8af4c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1UhLyYRXtqr2HksN5Lhwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 28921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4242
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

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KTTmUtiZCX7HQDadbE6fiZ`</summary>

```json
{
  "query": "\"Qwen\" OR \"Phi\" OR \"Llama-3\" VLA robot action model decoder-only 2024 2025 open weights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "a0a840fd-ac6b-4b4b-9ec4-eb04bea8e2ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1UhLyYRXtqr2HksN5Lhwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 28921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4242
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

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C9gt62KuZWYBv7tWH3dCi6`</summary>

```json
{
  "query": "HPT \"heterogeneous pretrained transformers\" robot action open source 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "5aeee8e3-88f1-412c-b77a-bd045f9b0dbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1UhLyYRXtqr2HksN5Lhwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 28921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4242
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

### Tool result

_source line 38 · 2026-05-19T16:22:23.186Z_

<details><summary>↩ Tool result · `toolu_01Sy4s986GnkJkkdwjX75pPH`</summary>

```text
Web search results for query: "SpatialVLA TraceVLA RoboVLM decoder-only VLA 2024 2025 open weights huggingface"

Links: [{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/395370588_SpatialVLA_Exploring_Spatial_Representations_for_Visual-Language-Action_Models"},{"title":"SpatialVLA (SpatialVLA) · GitHub","url":"https://github.com/SpatialVLA"},{"title":"GitHub - SpatialVLA/SpatialVLA: 🔥 SpatialVLA: a spatial-enhanced vision-language-action model that is trained on 1.1 Million real robot episodes. Accepted at RSS 2025.","url":"https://github.com/SpatialVLA/SpatialVLA"},{"title":"furonghuang-lab/tracevla_phi3v · Hugging Face","url":"https://huggingface.co/furonghuang-lab/tracevla_phi3v"},{"title":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4...","url":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt/raw/main/README.md"},{"title":"README.md · IPEC-COMMUNITY/spatialvla-4b-224-pt at 01f5ea2199f921c2d6cef03eba4fd5ed4a8c4662","url":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt/blob/01f5ea2199f921c2d6cef03eba4fd5ed4a8c4662/README.md"},{"title":"IPEC-COMMUNITY/spatialvla-4b-224-pt · Hugging Face","url":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt"},{"title":"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies","url":"https://arxiv.org/pdf/2412.10345"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://arxiv.org/pdf/2501.15830"}]

Based on the search results, here's information about these Vision-Language-Action (VLA) models:

## SpatialVLA

SpatialVLA is a spatial-enhanced vision-language-action model trained on 1.1 Million real robot episodes, purely huggingface-based with concise code and efficient performance. The VLM backbone of SpatialVLA is PaLiGemma2, which requires transformers >= 4.47.0. All SpatialVLA checkpoints and training codebase are released under an MIT License. SpatialVLA 1.0 was released on 2025/01/29 and achieves state-of-the-art performance across diverse evaluations with significantly faster inference speed and fewer tokens per action.

## TraceVLA

TraceVLA was developed by finetuning OpenVLA on 150K robot manipulation trajectories using visual trace prompting, demonstrating state-of-the-art performance that outperforms OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks. A compact 4B Phi-3-Vision variant was also created, pretrained on the Open-X-Embodiment dataset and finetuned on the TraceVLA dataset, rivaling the 7B OpenVLA baseline while improving inference efficiency. TraceVLA models are available on Hugging Face.

## RoboVLM

RoboVLM appears in performance comparisons with other VLA models, showing competitive results across different benchmarks.

All three models have open-weight versions available and support HuggingFace-based deployment with standard transformer libraries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "67dc68f9-9bae-4072-9eb0-5beb4f39efcf",
  "tool_use_result": {
    "query": "SpatialVLA TraceVLA RoboVLM decoder-only VLA 2024 2025 open weights huggingface",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G2rxwQB9jZciVPG182JWDq",
        "content": [
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | Request PDF",
            "url": "https://www.researchgate.net/publication/395370588_SpatialVLA_Exploring_Spatial_Representations_for_Visual-Language-Action_Models"
          },
          {
            "title": "SpatialVLA (SpatialVLA) · GitHub",
            "url": "https://github.com/SpatialVLA"
          },
          {
            "title": "GitHub - SpatialVLA/SpatialVLA: 🔥 SpatialVLA: a spatial-enhanced vision-language-action model that is trained on 1.1 Million real robot episodes. Accepted at RSS 2025.",
            "url": "https://github.com/SpatialVLA/SpatialVLA"
          },
          {
            "title": "furonghuang-lab/tracevla_phi3v · Hugging Face",
            "url": "https://huggingface.co/furonghuang-lab/tracevla_phi3v"
          },
          {
            "title": "https://huggingface.co/IPEC-COMMUNITY/spatialvla-4...",
            "url": "https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt/raw/main/README.md"
          },
          {
            "title": "README.md · IPEC-COMMUNITY/spatialvla-4b-224-pt at 01f5ea2199f921c2d6cef03eba4fd5ed4a8c4662",
            "url": "https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt/blob/01f5ea2199f921c2d6cef03eba4fd5ed4a8c4662/README.md"
          },
          {
            "title": "IPEC-COMMUNITY/spatialvla-4b-224-pt · Hugging Face",
            "url": "https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt"
          },
          {
            "title": "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies",
            "url": "https://arxiv.org/pdf/2412.10345"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model",
            "url": "https://arxiv.org/pdf/2501.15830"
          }
        ]
      },
      "Based on the search results, here's information about these Vision-Language-Action (VLA) models:\n\n## SpatialVLA\n\nSpatialVLA is a spatial-enhanced vision-language-action model trained on 1.1 Million real robot episodes, purely huggingface-based with concise code and efficient performance. The VLM backbone of SpatialVLA is PaLiGemma2, which requires transformers >= 4.47.0. All SpatialVLA checkpoints and training codebase are released under an MIT License. SpatialVLA 1.0 was released on 2025/01/29 and achieves state-of-the-art performance across diverse evaluations with significantly faster inference speed and fewer tokens per action.\n\n## TraceVLA\n\nTraceVLA was developed by finetuning OpenVLA on 150K robot manipulation trajectories using visual trace prompting, demonstrating state-of-the-art performance that outperforms OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks. A compact 4B Phi-3-Vision variant was also created, pretrained on the Open-X-Embodiment dataset and finetuned on the TraceVLA dataset, rivaling the 7B OpenVLA baseline while improving inference efficiency. TraceVLA models are available on Hugging Face.\n\n## RoboVLM\n\nRoboVLM appears in performance comparisons with other VLA models, showing competitive results across different benchmarks.\n\nAll three models have open-weight versions available and support HuggingFace-based deployment with standard transformer libraries."
    ],
    "durationSeconds": 7.120423182999999
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T16:22:24.295Z_

<details><summary>↩ Tool result · `toolu_01Azi4VA9wcjZvruruRHmZUK`</summary>

```text
Web search results for query: "CogACT VLA decoder-only action tokenization 2024 open source weights"

Links: [{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://cogact.github.io/"},{"title":"GitHub - Psi-Robot/Awesome-VLA-Papers: Paper list in the survey: A Survey on Vision-Language-Action Models: An Action Tokenization Perspective · GitHub","url":"https://github.com/Psi-Robot/Awesome-VLA-Papers"},{"title":"CogACT/CogACT-Base · Hugging Face","url":"https://huggingface.co/CogACT/CogACT-Base"},{"title":"CogACT/CogACT-Small · Hugging Face","url":"https://huggingface.co/CogACT/CogACT-Small"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation ...","url":"https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Dexbotic: Open-Source Vision-Language-Action Toolbox","url":"https://arxiv.org/html/2510.23511v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing   Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/pdf/2411.19650"}]

Based on the search results, here's what I found about CogACT VLA:

## Overview

CogACT is a Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation, released in 2024.11. CogACT-VLA has three componentized modules: a Vision Module that processes raw image input into perceptual tokens, a Language Module that integrates visual information and language instructions for cognitive reasoning, and an Action Module that receives cognition features as input to generate actions.

## Architecture and Action Handling

Rather than using decoder-only action tokenization, CogACT predicts actions using a diffusion modeling process and applies a Diffusion Transformer (DiT) as a powerful backbone for the action decoding process. CogACT is based on OpenVLA and extracts the cognition token, which together with noises is input to the Diffusion Transformer for diffusion modeling.

## Performance and Training Data

CogACT-VLA exceeds the average success rates of OpenVLA (which has a similar 7B model size) by over 35% in simulated evaluation and 55% in real robot experiments. The model is pretrained on 0.4M trajectories from the Open X-Embodiment dataset.

## Open Source Availability

Open source weights for CogACT-Base and CogACT-Small are available on Hugging Face, and the code is also publicly available via their official repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "14f9dcb8-9bf5-4c98-941c-ae8e9d50922e",
  "tool_use_result": {
    "query": "CogACT VLA decoder-only action tokenization 2024 open source weights",
    "results": [
      {
        "tool_use_id": "srvtoolu_016uevC1peQ5MNyyx8CioYeR",
        "content": [
          {
            "title": "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation",
            "url": "https://cogact.github.io/"
          },
          {
            "title": "GitHub - Psi-Robot/Awesome-VLA-Papers: Paper list in the survey: A Survey on Vision-Language-Action Models: An Action Tokenization Perspective · GitHub",
            "url": "https://github.com/Psi-Robot/Awesome-VLA-Papers"
          },
          {
            "title": "CogACT/CogACT-Base · Hugging Face",
            "url": "https://huggingface.co/CogACT/CogACT-Base"
          },
          {
            "title": "CogACT/CogACT-Small · Hugging Face",
            "url": "https://huggingface.co/CogACT/CogACT-Small"
          },
          {
            "title": "VLA-Cache: Efficient Vision-Language-Action Manipulation ...",
            "url": "https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "Dexbotic: Open-Source Vision-Language-Action Toolbox",
            "url": "https://arxiv.org/html/2510.23511v1"
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
            "title": "CogACT: A Foundational Vision-Language-Action Model for Synergizing   Cognition and Action in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2411.19650"
          }
        ]
      },
      "Based on the search results, here's what I found about CogACT VLA:\n\n## Overview\n\nCogACT is a Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation, released in 2024.11. CogACT-VLA has three componentized modules: a Vision Module that processes raw image input into perceptual tokens, a Language Module that integrates visual information and language instructions for cognitive reasoning, and an Action Module that receives cognition features as input to generate actions.\n\n## Architecture and Action Handling\n\nRather than using decoder-only action tokenization, CogACT predicts actions using a diffusion modeling process and applies a Diffusion Transformer (DiT) as a powerful backbone for the action decoding process. CogACT is based on OpenVLA and extracts the cognition token, which together with noises is input to the Diffusion Transformer for diffusion modeling.\n\n## Performance and Training Data\n\nCogACT-VLA exceeds the average success rates of OpenVLA (which has a similar 7B model size) by over 35% in simulated evaluation and 55% in real robot experiments. The model is pretrained on 0.4M trajectories from the Open X-Embodiment dataset.\n\n## Open Source Availability\n\nOpen source weights for CogACT-Base and CogACT-Small are available on Hugging Face, and the code is also publicly available via their official repository."
    ],
    "durationSeconds": 8.277745870999999
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T16:22:25.276Z_

<details><summary>↩ Tool result · `toolu_01KTTmUtiZCX7HQDadbE6fiZ`</summary>

```text
Web search results for query: ""Qwen" OR "Phi" OR "Llama-3" VLA robot action model decoder-only 2024 2025 open weights"

Links: [{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/pdf/2503.02310"},{"title":"DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.15669"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks","url":"https://arxiv.org/pdf/2504.19854"},{"title":"VITA-VLA: Efficiently Teaching Vision-Language Models to Act via Action Expert Distillation","url":"https://arxiv.org/pdf/2510.09607"}]

Based on the search results, I found relevant information about Vision Language Action (VLA) models and their architectures in 2024-2025:

## Key Findings

**VLA Architectures and Models:**

As of April 2025, state-of-the-art Vision Language Action Models employ either dual-level expert systems combining a VLM and diffusion decoders (notably Nvidia GR00T and Figure AI's Helix) or foundational generalist policies like π0 by Physical Intelligence.

**Decoder-Only VLMs in VLA Systems:**

The system uses decoder-only VLMs like Qwen3-VL as a dedicated bottleneck interface between the vision language model and the continuous action head (a Diffusion Transformer). By leveraging the causal masking inherent in decoder-only VLMs, systems can precisely control the information encoded in the queries by changing the position in the input sequence.

**Recent Models Using Qwen:**

NORA is a 3B-parameter model designed to reduce computational overhead while maintaining strong task performance, adopting the Qwen-2.5-VL-3B multimodal model as its backbone.

**VLA Architecture Categories:**

The first category adopts a discretization-based approach by transforming continuous actions into discrete tokens through partitioning the action space into fixed intervals, with visual and language features mapped to these action tokens via an LLM. The second category, represented by GR00T and π0, follows a diffusion-based design.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "c848632e-290b-46a7-827a-9833578fb81d",
  "tool_use_result": {
    "query": "\"Qwen\" OR \"Phi\" OR \"Llama-3\" VLA robot action model decoder-only 2024 2025 open weights",
    "results": [
      {
        "tool_use_id": "srvtoolu_013qbvFeUpsFQRCxazGFwXPv",
        "content": [
          {
            "title": "LangForce: Bayesian Decomposition of Vision Language ...",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding",
            "url": "https://arxiv.org/pdf/2503.02310"
          },
          {
            "title": "DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2511.15669"
          },
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks",
            "url": "https://arxiv.org/pdf/2504.19854"
          },
          {
            "title": "VITA-VLA: Efficiently Teaching Vision-Language Models to Act via Action Expert Distillation",
            "url": "https://arxiv.org/pdf/2510.09607"
          }
        ]
      },
      "Based on the search results, I found relevant information about Vision Language Action (VLA) models and their architectures in 2024-2025:\n\n## Key Findings\n\n**VLA Architectures and Models:**\n\nAs of April 2025, state-of-the-art Vision Language Action Models employ either dual-level expert systems combining a VLM and diffusion decoders (notably Nvidia GR00T and Figure AI's Helix) or foundational generalist policies like π0 by Physical Intelligence.\n\n**Decoder-Only VLMs in VLA Systems:**\n\nThe system uses decoder-only VLMs like Qwen3-VL as a dedicated bottleneck interface between the vision language model and the continuous action head (a Diffusion Transformer). By leveraging the causal masking inherent in decoder-only VLMs, systems can precisely control the information encoded in the queries by changing the position in the input sequence.\n\n**Recent Models Using Qwen:**\n\nNORA is a 3B-parameter model designed to reduce computational overhead while maintaining strong task performance, adopting the Qwen-2.5-VL-3B multimodal model as its backbone.\n\n**VLA Architecture Categories:**\n\nThe first category adopts a discretization-based approach by transforming continuous actions into discrete tokens through partitioning the action space into fixed intervals, with visual and language features mapped to these action tokens via an LLM. The second category, represented by GR00T and π0, follows a diffusion-based design."
    ],
    "durationSeconds": 7.20546142
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T16:22:25.346Z_

<details><summary>↩ Tool result · `toolu_01C9gt62KuZWYBv7tWH3dCi6`</summary>

```text
Web search results for query: "HPT "heterogeneous pretrained transformers" robot action open source 2024"

Links: [{"title":"Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers | OpenReview","url":"https://openreview.net/forum?id=Pf7kdIjHRf"},{"title":"Heterogeneous Pre-trained Transformers","url":"https://liruiw.github.io/hpt/"},{"title":"Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers","url":"https://arxiv.org/html/2409.20537v1"},{"title":"[2409.20537] Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers","url":"https://arxiv.org/abs/2409.20537"},{"title":"Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained   Transformers","url":"https://arxiv.org/pdf/2409.20537"},{"title":"GitHub - liruiw/HPT: Heterogeneous Pre-trained Transformer (HPT) as Scalable Policy Learner. · GitHub","url":"https://github.com/liruiw/HPT"},{"title":"NeurIPS Poster Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers","url":"https://neurips.cc/virtual/2024/poster/95294"},{"title":"MIT Researchers Developed Heterogeneous Pre-trained Transformers (HPTs): A Scalable AI Approach for Robotic Learning from Heterogeneous Data - MarkTechPost","url":"https://www.marktechpost.com/2024/11/07/mit-researchers-developed-heterogeneous-pre-trained-transformers-hpts-a-scalable-ai-approach-for-robotic-learning-from-heterogeneous-data/"},{"title":"liruiw/hpt - Heterogenous Pre-trained Transformers","url":"https://huggingface.co/liruiw/hpt"}]

I found comprehensive information about HPT (Heterogeneous Pre-trained Transformers) from 2024. Here's what the search revealed:

## Overview

HPT proposes pre-training a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared representation. This work studies the problem of learning policy representations through heterogeneous pre-training on robot data across different embodiments and tasks at scale.

## Key Features

The general architecture aligns the specific proprioception and vision inputs from distinct embodiments to a short sequence of tokens and then processes such tokens to map to control robots for different tasks.

The training mixtures contains over 50 datasets and 200k trajectories from real robot teleops, human videos, simulation, and deployed robots. HPTs outperform several baselines and enhance the fine-tuned policy performance by over 20% on unseen tasks in multiple simulator benchmarks and real-world settings.

## Open Source Status

The code and weights are open-sourced. This is a pytorch implementation for pre-training Heterogenous Pre-trained Transformers (HPTs). The code is available on GitHub at https://github.com/liruiw/HPT, with implementations also available on Hugging Face.

## Publication

The work was published as a NeurIPS 2024 spotlight presentation on September 25, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "919fc698-e5ec-493e-b5a9-facf671961e3",
  "tool_use_result": {
    "query": "HPT \"heterogeneous pretrained transformers\" robot action open source 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BaT5tuCwEMowF68E2qyZdz",
        "content": [
          {
            "title": "Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers | OpenReview",
            "url": "https://openreview.net/forum?id=Pf7kdIjHRf"
          },
          {
            "title": "Heterogeneous Pre-trained Transformers",
            "url": "https://liruiw.github.io/hpt/"
          },
          {
            "title": "Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers",
            "url": "https://arxiv.org/html/2409.20537v1"
          },
          {
            "title": "[2409.20537] Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers",
            "url": "https://arxiv.org/abs/2409.20537"
          },
          {
            "title": "Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained   Transformers",
            "url": "https://arxiv.org/pdf/2409.20537"
          },
          {
            "title": "GitHub - liruiw/HPT: Heterogeneous Pre-trained Transformer (HPT) as Scalable Policy Learner. · GitHub",
            "url": "https://github.com/liruiw/HPT"
          },
          {
            "title": "NeurIPS Poster Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers",
            "url": "https://neurips.cc/virtual/2024/poster/95294"
          },
          {
            "title": "MIT Researchers Developed Heterogeneous Pre-trained Transformers (HPTs): A Scalable AI Approach for Robotic Learning from Heterogeneous Data - MarkTechPost",
            "url": "https://www.marktechpost.com/2024/11/07/mit-researchers-developed-heterogeneous-pre-trained-transformers-hpts-a-scalable-ai-approach-for-robotic-learning-from-heterogeneous-data/"
          },
          {
            "title": "liruiw/hpt - Heterogenous Pre-trained Transformers",
            "url": "https://huggingface.co/liruiw/hpt"
          }
        ]
      },
      "I found comprehensive information about HPT (Heterogeneous Pre-trained Transformers) from 2024. Here's what the search revealed:\n\n## Overview\n\nHPT proposes pre-training a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared representation. This work studies the problem of learning policy representations through heterogeneous pre-training on robot data across different embodiments and tasks at scale.\n\n## Key Features\n\nThe general architecture aligns the specific proprioception and vision inputs from distinct embodiments to a short sequence of tokens and then processes such tokens to map to control robots for different tasks.\n\nThe training mixtures contains over 50 datasets and 200k trajectories from real robot teleops, human videos, simulation, and deployed robots. HPTs outperform several baselines and enhance the fine-tuned policy performance by over 20% on unseen tasks in multiple simulator benchmarks and real-world settings.\n\n## Open Source Status\n\nThe code and weights are open-sourced. This is a pytorch implementation for pre-training Heterogenous Pre-trained Transformers (HPTs). The code is available on GitHub at https://github.com/liruiw/HPT, with implementations also available on Hugging Face.\n\n## Publication\n\nThe work was published as a NeurIPS 2024 spotlight presentation on September 25, 2024."
    ],
    "durationSeconds": 7.090808033000001
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T16:22:25.833Z_

<details><summary>↩ Tool result · `toolu_01LueMi8AKFBHU5QR2Px47n8`</summary>

```text
Web search results for query: "DeeR-VLA 3D-VLA decoder-only architecture open source weights 2024"

Links: [{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large ...","url":"https://openreview.net/pdf?id=QKp3nhPU41"},{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution","url":"https://arxiv.org/html/2411.02359"},{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution | OpenReview","url":"https://openreview.net/forum?id=QKp3nhPU41"},{"title":"GitHub - UMass-Embodied-AGI/3D-VLA: [ICML 2024] 3D-VLA: A 3D Vision-Language-Action Generative World Model · GitHub","url":"https://github.com/UMass-Embodied-AGI/3D-VLA"},{"title":"GitHub - yueyang130/DeeR-VLA: Official code of paper \"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution\"","url":"https://github.com/yueyang130/DeeR-VLA"},{"title":"JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse","url":"https://arxiv.org/html/2503.16365v2"},{"title":"Yang130/DeeR-VLA · Hugging Face","url":"https://huggingface.co/Yang130/DeeR-VLA"}]

Based on the search results, here's information about the DeeR-VLA and 3D-VLA projects:

## DeeR-VLA

DeeR-VLA is a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation.

On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance.

The official code and open-source weights for DeeR-VLA are available on GitHub at [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) and on Hugging Face at [Yang130/DeeR-VLA](https://huggingface.co/Yang130/DeeR-VLA). The paper was presented at The Thirty-eighth Annual Conference on Neural Information Processing Systems in 2024.

## 3D-VLA

3D-VLA is a framework that connects vision-language-action (VLA) models to the 3D physical world. Unlike traditional 2D models, 3D-VLA integrates 3D perception, reasoning, and action through a generative world model, similar to human cognitive processes. 3D-VLA pretraining code and goal image generation LDM checkpoint were released in July 2024. The code is available on GitHub at [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "c1f96645-32a1-4c9e-b1c6-8ac8e77ed0b6",
  "tool_use_result": {
    "query": "DeeR-VLA 3D-VLA decoder-only architecture open source weights 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EPk43k7TZDFqzTavWBMq2r",
        "content": [
          {
            "title": "DeeR-VLA: Dynamic Inference of Multimodal Large ...",
            "url": "https://openreview.net/pdf?id=QKp3nhPU41"
          },
          {
            "title": "DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution",
            "url": "https://arxiv.org/html/2411.02359"
          },
          {
            "title": "DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution | OpenReview",
            "url": "https://openreview.net/forum?id=QKp3nhPU41"
          },
          {
            "title": "GitHub - UMass-Embodied-AGI/3D-VLA: [ICML 2024] 3D-VLA: A 3D Vision-Language-Action Generative World Model · GitHub",
            "url": "https://github.com/UMass-Embodied-AGI/3D-VLA"
          },
          {
            "title": "GitHub - yueyang130/DeeR-VLA: Official code of paper \"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution\"",
            "url": "https://github.com/yueyang130/DeeR-VLA"
          },
          {
            "title": "JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse",
            "url": "https://arxiv.org/html/2503.16365v2"
          },
          {
            "title": "Yang130/DeeR-VLA · Hugging Face",
            "url": "https://huggingface.co/Yang130/DeeR-VLA"
          }
        ]
      },
      "Based on the search results, here's information about the DeeR-VLA and 3D-VLA projects:\n\n## DeeR-VLA\n\nDeeR-VLA is a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation.\n\nOn the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance.\n\nThe official code and open-source weights for DeeR-VLA are available on GitHub at [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) and on Hugging Face at [Yang130/DeeR-VLA](https://huggingface.co/Yang130/DeeR-VLA). The paper was presented at The Thirty-eighth Annual Conference on Neural Information Processing Systems in 2024.\n\n## 3D-VLA\n\n3D-VLA is a framework that connects vision-language-action (VLA) models to the 3D physical world. Unlike traditional 2D models, 3D-VLA integrates 3D perception, reasoning, and action through a generative world model, similar to human cognitive processes. 3D-VLA pretraining code and goal image generation LDM checkpoint were released in July 2024. The code is available on GitHub at [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA)."
    ],
    "durationSeconds": 8.746187158000001
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Let me now get more details on the most promising decoder-only candidates. Key findings so far:

**Truly decoder-only (like OpenVLA):**
1. **TraceVLA** - Built on top of OpenVLA (Llama-2 backbone), also has a Phi-3-Vision 4B variant. The Phi-3 variant uses a different backbone! This is promising.
2. **SpatialVLA** - Uses PaLiGemma2 as backbone. Need to check if PaLiGemma2 is decoder-only or encoder-decoder. 

PaLiGemma is based on Gemma (decoder-only) + SigLIP, processing vision tokens through the decoder, so this could work! 3. **NORA** - 3B model based on Qwen-2.5-VL-3B. Decoder-only! Need to check if weights are available.
4. **DeeR-VLA** - Based on multi-exit MLLM. What backbone does it use?

**NOT decoder-only (use cross-attention/diffusion action heads):**
- π0: VLM + separate action expert with cross-attention (MoE)
- SmolVLA: VLM + action expert with cross-attention
- GR00T-N1

: encoder-decoder + diffusion transformer
- CogACT: OpenVLA backbone + separate Diffusion Transformer action head
- HPT: Separate trunk, not a standard LLM backbone

Now I'm looking into more details on the most promising candidates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "e19f4dc2-304f-4193-b400-c1b30e27030b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FECgXcKGRGzeC4cDYbNBfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1558,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 33163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3588
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

_source line 44_

几个关键候选浮出水面，深入查其架构细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "2264e5ac-1b3d-4eaa-be8f-954c37541227",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FECgXcKGRGzeC4cDYbNBfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1558,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 33163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3588
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

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BVhb6tGR95DQWqXVTFPufw`</summary>

```json
{
  "query": "SpatialVLA architecture PaLiGemma2 decoder-only action tokenization discrete tokens 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "61a3a3eb-f2d8-4d7a-9b03-d3cc527bde23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FECgXcKGRGzeC4cDYbNBfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1558,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 33163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3588
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

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HZbyPUx2kadekE3ePJVx3m`</summary>

```json
{
  "query": "TraceVLA Phi-3-Vision architecture decoder-only action tokens huggingface weights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "a3e5696e-668e-446a-8dd3-4bafbbea7f07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FECgXcKGRGzeC4cDYbNBfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1558,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 33163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3588
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

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VqDfVt2S4zTubMPDxHLB2c`</summary>

```json
{
  "query": "NORA VLA Qwen-2.5-VL 3B open source weights decoder-only action tokens 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "3817e931-a1ad-468b-805b-199d27983712",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FECgXcKGRGzeC4cDYbNBfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1558,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 33163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3588
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

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015mtVtR8J2etQv9pmbKrMdm`</summary>

```json
{
  "query": "DeeR-VLA backbone architecture Qwen LLaVA decoder-only CALVIN benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "1686e7d4-67ea-4f90-acd8-3c6b8d82862a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FECgXcKGRGzeC4cDYbNBfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1558,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 33163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3588
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

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QafucPeDP94sWAwefDDMR1`</summary>

```json
{
  "query": "RoboVLM architecture decoder-only open weights huggingface 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "3b96a759-b81e-4c68-87d0-72b788968b93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FECgXcKGRGzeC4cDYbNBfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1558,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 33163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3588
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

### Tool result

_source line 50 · 2026-05-19T16:22:44.578Z_

<details><summary>↩ Tool result · `toolu_01HZbyPUx2kadekE3ePJVx3m`</summary>

```text
Web search results for query: "TraceVLA Phi-3-Vision architecture decoder-only action tokens huggingface weights"

Links: [{"title":"furonghuang-lab/tracevla_phi3v · Hugging Face","url":"https://huggingface.co/furonghuang-lab/tracevla_phi3v"},{"title":"Phi-3 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/phi3"},{"title":"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies","url":"https://arxiv.org/html/2412.10345v2"},{"title":"microsoft/Phi-3-vision-128k-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-3-vision-128k-instruct"},{"title":"Kukedlc/Phi-3-Vision-Win-snap · Hugging Face","url":"https://huggingface.co/Kukedlc/Phi-3-Vision-Win-snap"},{"title":"microsoft/Phi-3.5-vision-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-3.5-vision-instruct"},{"title":"Phi-3 Tutorial: Hands-On With Microsoft's Smallest AI Model","url":"https://www.datacamp.com/tutorial/phi-3-tutorial"},{"title":"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies","url":"https://arxiv.org/pdf/2412.10345"}]

Based on the search results, here's what I found about TraceVLA and its architecture:

TraceVLA-Phi3 is a VLA model fine-tuned using the 4B-parameter Phi-3-Vision as a backbone on the Open X-Embodiments dataset, which comprises 970K trajectories across diverse robot embodiments, tasks, and scenes. TraceVLA-Phi3 offers improved inference efficiency and reduced computational requirements while maintaining robust performance.

Regarding the architecture and action tokens: Vision-language-action models comprise a visual encoder that converts input images into patch embeddings, a projector that maps these embeddings to the language model's input space, and a large language model backbone. A separator token is inserted between the visual tokens of images with overlaid visual traces, then concatenated with text tokens and fed into the underlying vision language model backbone to output action tokens.

Phi-3 employs a dense decoder-only Transformer architecture.

The model weights are available on Hugging Face at the repository: **furonghuang-lab/tracevla_phi3v**


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "3b6ceff1-5e10-47e5-a5e9-e991fc969cc1",
  "tool_use_result": {
    "query": "TraceVLA Phi-3-Vision architecture decoder-only action tokens huggingface weights",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UxFX4obJjpX2wdbHfAAk3M",
        "content": [
          {
            "title": "furonghuang-lab/tracevla_phi3v · Hugging Face",
            "url": "https://huggingface.co/furonghuang-lab/tracevla_phi3v"
          },
          {
            "title": "Phi-3 · Hugging Face",
            "url": "https://huggingface.co/docs/transformers/en/model_doc/phi3"
          },
          {
            "title": "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies",
            "url": "https://arxiv.org/html/2412.10345v2"
          },
          {
            "title": "microsoft/Phi-3-vision-128k-instruct · Hugging Face",
            "url": "https://huggingface.co/microsoft/Phi-3-vision-128k-instruct"
          },
          {
            "title": "Kukedlc/Phi-3-Vision-Win-snap · Hugging Face",
            "url": "https://huggingface.co/Kukedlc/Phi-3-Vision-Win-snap"
          },
          {
            "title": "microsoft/Phi-3.5-vision-instruct · Hugging Face",
            "url": "https://huggingface.co/microsoft/Phi-3.5-vision-instruct"
          },
          {
            "title": "Phi-3 Tutorial: Hands-On With Microsoft's Smallest AI Model",
            "url": "https://www.datacamp.com/tutorial/phi-3-tutorial"
          },
          {
            "title": "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies",
            "url": "https://arxiv.org/pdf/2412.10345"
          }
        ]
      },
      "Based on the search results, here's what I found about TraceVLA and its architecture:\n\nTraceVLA-Phi3 is a VLA model fine-tuned using the 4B-parameter Phi-3-Vision as a backbone on the Open X-Embodiments dataset, which comprises 970K trajectories across diverse robot embodiments, tasks, and scenes. TraceVLA-Phi3 offers improved inference efficiency and reduced computational requirements while maintaining robust performance.\n\nRegarding the architecture and action tokens: Vision-language-action models comprise a visual encoder that converts input images into patch embeddings, a projector that maps these embeddings to the language model's input space, and a large language model backbone. A separator token is inserted between the visual tokens of images with overlaid visual traces, then concatenated with text tokens and fed into the underlying vision language model backbone to output action tokens.\n\nPhi-3 employs a dense decoder-only Transformer architecture.\n\nThe model weights are available on Hugging Face at the repository: **furonghuang-lab/tracevla_phi3v**"
    ],
    "durationSeconds": 6.002164499000006
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T16:22:44.623Z_

<details><summary>↩ Tool result · `toolu_01BVhb6tGR95DQWqXVTFPufw`</summary>

```text
Web search results for query: "SpatialVLA architecture PaLiGemma2 decoder-only action tokenization discrete tokens 2025"

Links: [{"title":"DTP:A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models","url":"https://arxiv.org/html/2601.16065"},{"title":"Discrete Robot Action Tokens","url":"https://www.emergentmind.com/topics/discrete-robot-action-tokens"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v3"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://arxiv.org/pdf/2501.15830"},{"title":"Ordered Action Tokenization","url":"https://ordered-action-tokenization.github.io/"},{"title":"Gemma explained: PaliGemma architecture - Google Developers Blog","url":"https://developers.googleblog.com/gemma-explained-paligemma-architecture/"},{"title":"The Compression Gap: Why Discrete Tokenization Limits Vision-Language-Action Model Scaling","url":"https://arxiv.org/pdf/2604.03191"}]

Based on the search results, here's what I found about SpatialVLA and related architecture details:

## SpatialVLA Architecture

SpatialVLA is a 3B model based on Paligemma 2 with integrated 3D position encoding. SpatialVLA incorporates the depth information for the objects in the input image, boosting spatial perception ability and yielding the increase in task success rate.

## Action Tokenization and Discrete Tokens

RT-2 fine-tuned the VLM PaLI-X on both large-scale vision-language data and robot demonstration data via autoregressive next token prediction, where robot actions are discretized into 256 bins and represented as separate tokens analogous to text tokens. This foundational approach influenced subsequent VLA models.

The core VLA pipeline includes a visual encoder, a language model, and discrete action token generation.

## Related Recent Work

FAST applies the Discrete Cosine Transform (DCT) to action chunks, quantizing the coefficients, then uses BPE for further compression, yielding variable-length high-entropy integer tokens. SpatialVLA is listed among AR-style or BERT-style generation of discrete action tokens with a unified VLM backbone.

The search results indicate that SpatialVLA represents a recent advancement in vision-language-action models that combines strong spatial understanding with discrete action tokenization approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "7ec96916-3eaf-491b-91c8-7b9adcfd2cb2",
  "tool_use_result": {
    "query": "SpatialVLA architecture PaLiGemma2 decoder-only action tokenization discrete tokens 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015xw1M5pEArwLBmuNzkNppf",
        "content": [
          {
            "title": "DTP:A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models",
            "url": "https://arxiv.org/html/2601.16065"
          },
          {
            "title": "Discrete Robot Action Tokens",
            "url": "https://www.emergentmind.com/topics/discrete-robot-action-tokens"
          },
          {
            "title": "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies",
            "url": "https://arxiv.org/html/2508.20072v3"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model",
            "url": "https://arxiv.org/pdf/2501.15830"
          },
          {
            "title": "Ordered Action Tokenization",
            "url": "https://ordered-action-tokenization.github.io/"
          },
          {
            "title": "Gemma explained: PaliGemma architecture - Google Developers Blog",
            "url": "https://developers.googleblog.com/gemma-explained-paligemma-architecture/"
          },
          {
            "title": "The Compression Gap: Why Discrete Tokenization Limits Vision-Language-Action Model Scaling",
            "url": "https://arxiv.org/pdf/2604.03191"
          }
        ]
      },
      "Based on the search results, here's what I found about SpatialVLA and related architecture details:\n\n## SpatialVLA Architecture\n\nSpatialVLA is a 3B model based on Paligemma 2 with integrated 3D position encoding. SpatialVLA incorporates the depth information for the objects in the input image, boosting spatial perception ability and yielding the increase in task success rate.\n\n## Action Tokenization and Discrete Tokens\n\nRT-2 fine-tuned the VLM PaLI-X on both large-scale vision-language data and robot demonstration data via autoregressive next token prediction, where robot actions are discretized into 256 bins and represented as separate tokens analogous to text tokens. This foundational approach influenced subsequent VLA models.\n\nThe core VLA pipeline includes a visual encoder, a language model, and discrete action token generation.\n\n## Related Recent Work\n\nFAST applies the Discrete Cosine Transform (DCT) to action chunks, quantizing the coefficients, then uses BPE for further compression, yielding variable-length high-entropy integer tokens. SpatialVLA is listed among AR-style or BERT-style generation of discrete action tokens with a unified VLM backbone.\n\nThe search results indicate that SpatialVLA represents a recent advancement in vision-language-action models that combines strong spatial understanding with discrete action tokenization approaches."
    ],
    "durationSeconds": 6.9836633560000045
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T16:22:46.686Z_

<details><summary>↩ Tool result · `toolu_01VqDfVt2S4zTubMPDxHLB2c`</summary>

```text
Web search results for query: "NORA VLA Qwen-2.5-VL 3B open source weights decoder-only action tokens 2025"

Links: [{"title":"Paper page - NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://huggingface.co/papers/2504.19854"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/html/2504.19854v1"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks","url":"https://arxiv.org/pdf/2504.19854"},{"title":"[2504.19854] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/abs/2504.19854"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://declare-lab.github.io/nora"},{"title":"Qwen2.5-VL · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/qwen2_5_vl"},{"title":"GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3-VL"}]

Based on the search results, here's what I found about NORA, the VLA model using Qwen-2.5-VL 3B:

## NORA Overview

NORA is a 3B-parameter Vision-Language-Action (VLA) model trained on the Open X-Embodiment dataset. NORA adopts the Qwen-2.5-VL-3B multimodal model as its backbone, leveraging its superior visual-semantic understanding to enhance visual reasoning and action grounding.

## Key Features

- **Training Data**: NORA is trained on 970k real-world robot demonstrations and equipped with the FAST+ tokenizer for efficient action sequence generation.

- **Action Tokenization**: The vocabulary of the VLM tokenizer was augmented by 2048 additional tokens introduced by the FAST+ tokenizer. NORA employs the FAST+ tokenizer to discretize continuous action tokens, optimizing action sequence generation for a wide range of robotic tasks.

- **Model Type**: NORA adopts the state-of-the-art open-source multi-modal model Qwen-2.5-VL-3B as the VLM backbone due to its excellent balance between performance and efficiency at this scale.

## Performance

Experimental results demonstrate that NORA outperforms existing large-scale VLA models, achieving better task performance with significantly reduced computational overhead, making it a more practical solution for real-time robotic autonomy.

The paper was published on April 28, 2025, and represents an effort to create a more efficient alternative to larger VLA models while maintaining strong task execution capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "a2b27c01-d033-4a30-b1e5-66ed494a8748",
  "tool_use_result": {
    "query": "NORA VLA Qwen-2.5-VL 3B open source weights decoder-only action tokens 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TRZjaiqAgSgwBRtRziqfPb",
        "content": [
          {
            "title": "Paper page - NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://huggingface.co/papers/2504.19854"
          },
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://arxiv.org/html/2504.19854v1"
          },
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks",
            "url": "https://arxiv.org/pdf/2504.19854"
          },
          {
            "title": "[2504.19854] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://arxiv.org/abs/2504.19854"
          },
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://declare-lab.github.io/nora"
          },
          {
            "title": "Qwen2.5-VL · Hugging Face",
            "url": "https://huggingface.co/docs/transformers/model_doc/qwen2_5_vl"
          },
          {
            "title": "GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub",
            "url": "https://github.com/QwenLM/Qwen3-VL"
          }
        ]
      },
      "Based on the search results, here's what I found about NORA, the VLA model using Qwen-2.5-VL 3B:\n\n## NORA Overview\n\nNORA is a 3B-parameter Vision-Language-Action (VLA) model trained on the Open X-Embodiment dataset. NORA adopts the Qwen-2.5-VL-3B multimodal model as its backbone, leveraging its superior visual-semantic understanding to enhance visual reasoning and action grounding.\n\n## Key Features\n\n- **Training Data**: NORA is trained on 970k real-world robot demonstrations and equipped with the FAST+ tokenizer for efficient action sequence generation.\n\n- **Action Tokenization**: The vocabulary of the VLM tokenizer was augmented by 2048 additional tokens introduced by the FAST+ tokenizer. NORA employs the FAST+ tokenizer to discretize continuous action tokens, optimizing action sequence generation for a wide range of robotic tasks.\n\n- **Model Type**: NORA adopts the state-of-the-art open-source multi-modal model Qwen-2.5-VL-3B as the VLM backbone due to its excellent balance between performance and efficiency at this scale.\n\n## Performance\n\nExperimental results demonstrate that NORA outperforms existing large-scale VLA models, achieving better task performance with significantly reduced computational overhead, making it a more practical solution for real-time robotic autonomy.\n\nThe paper was published on April 28, 2025, and represents an effort to create a more efficient alternative to larger VLA models while maintaining strong task execution capabilities."
    ],
    "durationSeconds": 7.575953442000013
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T16:22:47.224Z_

<details><summary>↩ Tool result · `toolu_01QafucPeDP94sWAwefDDMR1`</summary>

```text
Web search results for query: "RoboVLM architecture decoder-only open weights huggingface 2024 2025"

Links: [{"title":"blog/vlms-2025.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/vlms-2025.md"},{"title":"Open-Weight Foundation Models for Robotics (2025 Guide) | RoboCloud Hub","url":"https://robocloud-dashboard.vercel.app/learn/blog/open-weight-robot-models"},{"title":"robovlms/RoboVLMs · Hugging Face","url":"https://huggingface.co/robovlms/RoboVLMs"},{"title":"GitHub - Robot-VLAs/RoboVLMs","url":"https://github.com/Robot-VLAs/RoboVLMs"},{"title":"RoBERTa · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/roberta"},{"title":"NVLM: Open Frontier-Class Multimodal LLMs","url":"https://arxiv.org/pdf/2409.11402"}]

Based on the search results, here's what I found about RoboVLM:

RoboVLMs is a unified framework for easily building VLAs (Vision Language Actions) from VLMs (Vision Language Models). The RoboVLMs codebase was released to help the community, and it allows integrating most VLMs within 30 lines of code.

Regarding the architecture, RoboVLMs supports several VLA structures, multi-view input and various backbones. Three pre-trained model checkpoints are available: RoboKosMos trained on the CALVIN dataset (splits ABCD and ABC) and on the OXE-magic-soup dataset.

Notably, decoder-only architecture is one of the common architectures used to build multimodal LLMs, though the search results don't specifically confirm that RoboVLMs uses a decoder-only architecture. The model can be used to predict action based on vision and language input, and RoboVLMs includes the strongest VLA model driven by KosMos VLM backbone.

The models are available on Hugging Face as open weights, as indicated by the GitHub and Hugging Face repository links in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "4976bcc0-22cb-4f0d-8548-1fde152fd7a1",
  "tool_use_result": {
    "query": "RoboVLM architecture decoder-only open weights huggingface 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D81F3WUrEmwb2hGb1YBbz1",
        "content": [
          {
            "title": "blog/vlms-2025.md at main · huggingface/blog",
            "url": "https://github.com/huggingface/blog/blob/main/vlms-2025.md"
          },
          {
            "title": "Open-Weight Foundation Models for Robotics (2025 Guide) | RoboCloud Hub",
            "url": "https://robocloud-dashboard.vercel.app/learn/blog/open-weight-robot-models"
          },
          {
            "title": "robovlms/RoboVLMs · Hugging Face",
            "url": "https://huggingface.co/robovlms/RoboVLMs"
          },
          {
            "title": "GitHub - Robot-VLAs/RoboVLMs",
            "url": "https://github.com/Robot-VLAs/RoboVLMs"
          },
          {
            "title": "RoBERTa · Hugging Face",
            "url": "https://huggingface.co/docs/transformers/en/model_doc/roberta"
          },
          {
            "title": "NVLM: Open Frontier-Class Multimodal LLMs",
            "url": "https://arxiv.org/pdf/2409.11402"
          }
        ]
      },
      "Based on the search results, here's what I found about RoboVLM:\n\nRoboVLMs is a unified framework for easily building VLAs (Vision Language Actions) from VLMs (Vision Language Models). The RoboVLMs codebase was released to help the community, and it allows integrating most VLMs within 30 lines of code.\n\nRegarding the architecture, RoboVLMs supports several VLA structures, multi-view input and various backbones. Three pre-trained model checkpoints are available: RoboKosMos trained on the CALVIN dataset (splits ABCD and ABC) and on the OXE-magic-soup dataset.\n\nNotably, decoder-only architecture is one of the common architectures used to build multimodal LLMs, though the search results don't specifically confirm that RoboVLMs uses a decoder-only architecture. The model can be used to predict action based on vision and language input, and RoboVLMs includes the strongest VLA model driven by KosMos VLM backbone.\n\nThe models are available on Hugging Face as open weights, as indicated by the GitHub and Hugging Face repository links in the search results."
    ],
    "durationSeconds": 6.854065797999996
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T16:22:48.844Z_

<details><summary>↩ Tool result · `toolu_015mtVtR8J2etQv9pmbKrMdm`</summary>

```text
Web search results for query: "DeeR-VLA backbone architecture Qwen LLaVA decoder-only CALVIN benchmark"

Links: [{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution","url":"https://arxiv.org/html/2411.02359v1/"},{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large ...","url":"https://openreview.net/pdf?id=QKp3nhPU41"},{"title":"GitHub - yueyang130/DeeR-VLA: Official code of paper \"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution\"","url":"https://github.com/yueyang130/DeeR-VLA"},{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution | OpenReview","url":"https://openreview.net/forum?id=QKp3nhPU41"},{"title":"DeeR-VLA | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3739719"},{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution","url":"https://proceedings.neurips.cc//paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html"},{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for   Efficient Robot Execution","url":"https://arxiv.org/pdf/2411.02359"},{"title":"VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models","url":"https://arxiv.org/html/2601.03309v1"}]

Based on the search results, here's what I found about DeeR-VLA:

## Overview
DeeR is a Dynamic Early-Exit for Robotic MLLM framework that automatically configures the size of MLLMs conditioned on each situation confronted by an embodied agent.

## Architecture
The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Exit points were configured after every two self-attention layers in all MLLM models.

## Backbone Model
A subset of the OpenFlamingo model was employed as the backbone, specifically using only the first 12 layers from OpenFlamingo3B (which has 24 LLM layers) and OpenFlamingo9B (which has 32 LLM layers), resulting in 6 exit points.

## Early-Termination Algorithms
Novel algorithms establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (power consumption), as well as peak computational consumption (latency) and GPU memory usage.

## CALVIN Benchmark Results
On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. The CALVIN Long-Horizon Multi-Task Language Control benchmark is used as the testbed to test the learned multi-task, language-conditioned policy, where the objective is for the agent to successfully complete task sequences, each with five subtasks described in natural language.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "ee8498d4-295d-4376-990a-e745ff84a820",
  "tool_use_result": {
    "query": "DeeR-VLA backbone architecture Qwen LLaVA decoder-only CALVIN benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_019fgstQzpAayKs2U6oMbfWx",
        "content": [
          {
            "title": "DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution",
            "url": "https://arxiv.org/html/2411.02359v1/"
          },
          {
            "title": "DeeR-VLA: Dynamic Inference of Multimodal Large ...",
            "url": "https://openreview.net/pdf?id=QKp3nhPU41"
          },
          {
            "title": "GitHub - yueyang130/DeeR-VLA: Official code of paper \"DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution\"",
            "url": "https://github.com/yueyang130/DeeR-VLA"
          },
          {
            "title": "DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution | OpenReview",
            "url": "https://openreview.net/forum?id=QKp3nhPU41"
          },
          {
            "title": "DeeR-VLA | Proceedings of the 38th International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3737916.3739719"
          },
          {
            "title": "DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution",
            "url": "https://proceedings.neurips.cc//paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html"
          },
          {
            "title": "DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for   Efficient Robot Execution",
            "url": "https://arxiv.org/pdf/2411.02359"
          },
          {
            "title": "VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2601.03309v1"
          }
        ]
      },
      "Based on the search results, here's what I found about DeeR-VLA:\n\n## Overview\nDeeR is a Dynamic Early-Exit for Robotic MLLM framework that automatically configures the size of MLLMs conditioned on each situation confronted by an embodied agent.\n\n## Architecture\nThe approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Exit points were configured after every two self-attention layers in all MLLM models.\n\n## Backbone Model\nA subset of the OpenFlamingo model was employed as the backbone, specifically using only the first 12 layers from OpenFlamingo3B (which has 24 LLM layers) and OpenFlamingo9B (which has 32 LLM layers), resulting in 6 exit points.\n\n## Early-Termination Algorithms\nNovel algorithms establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (power consumption), as well as peak computational consumption (latency) and GPU memory usage.\n\n## CALVIN Benchmark Results\nOn the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. The CALVIN Long-Horizon Multi-Task Language Control benchmark is used as the testbed to test the learned multi-task, language-conditioned policy, where the objective is for the agent to successfully complete task sequences, each with five subtasks described in natural language."
    ],
    "durationSeconds": 8.779706877999997
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clearer picture. Let me now get the key details I need for the most promising decoder-only candidates:

1. **SpatialVLA** - 4B model based on PaLiGemma2. PaLiGemma2 uses Gemma 2 (decoder-only) as the LLM backbone + SigLIP vision encoder. This is **decoder-only** with discrete action tokenization. Different backbone from OpenVLA (Gemma 2 vs Llama 2). Open weights available. This is a TOP candidate.


2. **TraceVLA-Phi3** - 4B decoder-only model using Phi-3-Vision with open weights on HuggingFace, offering a different backbone alternative to OpenVLA.
3. **NORA** - 3B decoder-only model based on Qwen-2.5-VL with FAST+ tokenization, though I need to verify if the weights have been released.
4. **DeeR-VLA** - Built on OpenFlamingo's cross-attention architecture, which actually deviates from the decoder-only pattern since it adds cross-attention layers to a base decoder-only LLM.
5. **CogACT** - Uses OpenVLA's Llama-2 backbone for the cognition component but switches to a separate Diffusion Transformer for action generation, so it's not purely decoder-only for action prediction.
6. **π0** - A cross-attention MoE architecture that doesn't follow the decoder-only approach.

I should verify whether NORA's weights are publicly available and look into SpatialVLA's architecture details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "2334debd-ef5d-452a-97c7-767264c93751",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHNtu3vWYkb2DKBTE7fQ63",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 36751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
      },
      "output_tokens": 9,
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

_source line 56_

找到三个最有前景的 decoder-only 候选。确认权重和具体细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "8249e57b-049f-4328-91ca-740ad024d088",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHNtu3vWYkb2DKBTE7fQ63",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 36751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
      },
      "output_tokens": 9,
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

_source line 57_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FTjVUXRzauTUqhbSdSaQRk`</summary>

```json
{
  "query": "NORA VLA declare-lab github open source weights released download 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "1c8c67ae-b0d7-4282-9524-aee661144e0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHNtu3vWYkb2DKBTE7fQ63",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 36751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
      },
      "output_tokens": 9,
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

_source line 58_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016S4i5QnuoWoHwDKNJHVB6m`</summary>

```json
{
  "query": "SpatialVLA huggingface IPEC-COMMUNITY spatialvla-4b model size parameters action tokens discrete"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "dc09f8d5-6c18-4f1c-a72d-8099197ea938",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHNtu3vWYkb2DKBTE7fQ63",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 36751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
      },
      "output_tokens": 9,
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

_source line 59_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DJJBm4BPfCvrEjv8Se6go8`</summary>

```json
{
  "query": "TraceVLA tracevla_phi3v model parameters size LIBERO evaluation 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "338115e2-85e3-4037-9a40-d0f2b1795a73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHNtu3vWYkb2DKBTE7fQ63",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 36751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
      },
      "output_tokens": 9,
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

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018mv4zRsatAyRCaVUgHC9Sj`</summary>

```json
{
  "query": "ECoT embodied chain thought VLA Llama backbone decoder-only open weights 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "7f6c2bc9-5f34-4404-97ff-588ee801b007",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHNtu3vWYkb2DKBTE7fQ63",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 36751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
      },
      "output_tokens": 9,
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

_source line 61_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F8fL1LjQHYopENo9LbAA3a`</summary>

```json
{
  "query": "TinyVLA Phi-2 VLA decoder-only open source weights huggingface 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "03b98317-221f-4709-a812-75d01c63c651",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHNtu3vWYkb2DKBTE7fQ63",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 36751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
      },
      "output_tokens": 9,
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

_source line 62 · 2026-05-19T16:23:07.653Z_

<details><summary>↩ Tool result · `toolu_01FTjVUXRzauTUqhbSdSaQRk`</summary>

```text
Web search results for query: "NORA VLA declare-lab github open source weights released download 2025"

Links: [{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/html/2504.19854v1"},{"title":"GitHub - declare-lab/nora: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub","url":"https://github.com/declare-lab/nora"},{"title":"GitHub - declare-lab/nora-1.5: NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards · GitHub","url":"https://github.com/declare-lab/nora-1.5"},{"title":"GitHub - ehaller00/NORA-VLA: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub","url":"https://github.com/ehaller00/NORA-VLA"},{"title":"declare-lab/nora-1.5 · Hugging Face","url":"https://huggingface.co/declare-lab/nora-1.5"},{"title":"declare-lab/nora · Hugging Face","url":"https://huggingface.co/declare-lab/nora"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks","url":"https://arxiv.org/pdf/2504.19854"},{"title":"nora huggingface.co api & declare-lab nora github AI Model - Toolify","url":"https://www.toolify.ai/ai-model/declare-lab-nora"}]

Based on the search results, here's what I found about NORA VLA from declare-lab:

## NORA Overview

NORA is a 3B-parameter model designed to reduce computational overhead while maintaining strong task performance. NORA adopts the Qwen-2.5-VL-3B multimodal model as its backbone, leveraging its superior visual-semantic understanding to enhance visual reasoning and action grounding.

## Open Source Release

Codes & Checkpoints are available at https://declare-lab.github.io/nora, and the official GitHub repository is at https://github.com/declare-lab/nora.

All the eval scripts and model checkpoints have been released. The model weights are available on Hugging Face at https://huggingface.co/declare-lab/nora.

## NORA-1.5 Update

NORA-1.5 is the new VLA model from the NORA family, achieving SOTA (state-of-the-art) performance on several benchmarks. NORA-1.5 improves generalization and real-world decision making through post-training with world-model-based and action-based preference rewards. The NORA-1.5 repository is available at https://github.com/declare-lab/nora-1.5.

## Getting Started

They provide a lightweight interface with minimal dependencies to get started with loading and running NORA for inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "91cff26d-cd3d-412a-96a2-d8bba6145a31",
  "tool_use_result": {
    "query": "NORA VLA declare-lab github open source weights released download 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XBEyujm5QpPSfViiehV7cA",
        "content": [
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://arxiv.org/html/2504.19854v1"
          },
          {
            "title": "GitHub - declare-lab/nora: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub",
            "url": "https://github.com/declare-lab/nora"
          },
          {
            "title": "GitHub - declare-lab/nora-1.5: NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards · GitHub",
            "url": "https://github.com/declare-lab/nora-1.5"
          },
          {
            "title": "GitHub - ehaller00/NORA-VLA: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub",
            "url": "https://github.com/ehaller00/NORA-VLA"
          },
          {
            "title": "declare-lab/nora-1.5 · Hugging Face",
            "url": "https://huggingface.co/declare-lab/nora-1.5"
          },
          {
            "title": "declare-lab/nora · Hugging Face",
            "url": "https://huggingface.co/declare-lab/nora"
          },
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks",
            "url": "https://arxiv.org/pdf/2504.19854"
          },
          {
            "title": "nora huggingface.co api & declare-lab nora github AI Model - Toolify",
            "url": "https://www.toolify.ai/ai-model/declare-lab-nora"
          }
        ]
      },
      "Based on the search results, here's what I found about NORA VLA from declare-lab:\n\n## NORA Overview\n\nNORA is a 3B-parameter model designed to reduce computational overhead while maintaining strong task performance. NORA adopts the Qwen-2.5-VL-3B multimodal model as its backbone, leveraging its superior visual-semantic understanding to enhance visual reasoning and action grounding.\n\n## Open Source Release\n\nCodes & Checkpoints are available at https://declare-lab.github.io/nora, and the official GitHub repository is at https://github.com/declare-lab/nora.\n\nAll the eval scripts and model checkpoints have been released. The model weights are available on Hugging Face at https://huggingface.co/declare-lab/nora.\n\n## NORA-1.5 Update\n\nNORA-1.5 is the new VLA model from the NORA family, achieving SOTA (state-of-the-art) performance on several benchmarks. NORA-1.5 improves generalization and real-world decision making through post-training with world-model-based and action-based preference rewards. The NORA-1.5 repository is available at https://github.com/declare-lab/nora-1.5.\n\n## Getting Started\n\nThey provide a lightweight interface with minimal dependencies to get started with loading and running NORA for inference."
    ],
    "durationSeconds": 6.153162748000002
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-19T16:23:08.847Z_

<details><summary>↩ Tool result · `toolu_016S4i5QnuoWoHwDKNJHVB6m`</summary>

```text
Web search results for query: "SpatialVLA huggingface IPEC-COMMUNITY spatialvla-4b model size parameters action tokens discrete"

Links: [{"title":"SpatialVLA (SpatialVLA) · GitHub","url":"https://github.com/SpatialVLA"},{"title":"GitHub - SpatialVLA/SpatialVLA: 🔥 SpatialVLA: a spatial-enhanced vision-language-action model that is trained on 1.1 Million real robot episodes. Accepted at RSS 2025.","url":"https://github.com/SpatialVLA/SpatialVLA"},{"title":"IPEC-COMMUNITY/spatialvla-4b-mix-224-pt · Hugging Face","url":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-mix-224-pt"},{"title":"IPEC-COMMUNITY/spatialvla-4b-224-pt · Hugging Face","url":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt"},{"title":"README.md · IPEC-COMMUNITY/spatialvla-4b-224-pt at 01f5ea2199f921c2d6cef03eba4fd5ed4a8c4662","url":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt/blob/01f5ea2199f921c2d6cef03eba4fd5ed4a8c4662/README.md"},{"title":"IPEC-COMMUNITY/spatialvla-4b-224-sft-bridge · Hugging Face","url":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-sft-bridge"}]

Based on the search results, here's what I found about SpatialVLA:

**Model Overview:**
SpatialVLA is a spatial-enhanced vision-language-action model trained on 1.1 Million real robot episodes.

**Model Size and Parameters:**
The search results indicate that the model comes in a 4B variant (as shown in the model name "spatialvla-4b"), where the "4b" refers to approximately 4 billion parameters. The model requires 8.5GB of GPU memory for inference.

**Training Details:**
SpatialVLA is pre-trained with 1.1 Million real-robot demonstrations from the OXE and RH20T dataset on a cluster of 64 A100 GPUs for about 10 days, using a batch size of 2048.

**Model Type and Function:**
SpatialVLA is a Vision-language-action model that takes language and image inputs to produce robot actions.

**Action Output:**
The model includes functionality to predict and decode actions - the model uses a `predict_action` method that outputs generation results, which are then decoded using a `decode_actions` processor function.

The search results don't contain specific details about discrete action tokens or the exact parameter count beyond the "4b" designation. If you need more technical details about the action token representation, you may want to check the model's paper or detailed technical documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "9815c5f2-bef3-4901-94f7-ba4b5bd9a6be",
  "tool_use_result": {
    "query": "SpatialVLA huggingface IPEC-COMMUNITY spatialvla-4b model size parameters action tokens discrete",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MLkxQPWf4BXRtUuuhXKxrR",
        "content": [
          {
            "title": "SpatialVLA (SpatialVLA) · GitHub",
            "url": "https://github.com/SpatialVLA"
          },
          {
            "title": "GitHub - SpatialVLA/SpatialVLA: 🔥 SpatialVLA: a spatial-enhanced vision-language-action model that is trained on 1.1 Million real robot episodes. Accepted at RSS 2025.",
            "url": "https://github.com/SpatialVLA/SpatialVLA"
          },
          {
            "title": "IPEC-COMMUNITY/spatialvla-4b-mix-224-pt · Hugging Face",
            "url": "https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-mix-224-pt"
          },
          {
            "title": "IPEC-COMMUNITY/spatialvla-4b-224-pt · Hugging Face",
            "url": "https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt"
          },
          {
            "title": "README.md · IPEC-COMMUNITY/spatialvla-4b-224-pt at 01f5ea2199f921c2d6cef03eba4fd5ed4a8c4662",
            "url": "https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt/blob/01f5ea2199f921c2d6cef03eba4fd5ed4a8c4662/README.md"
          },
          {
            "title": "IPEC-COMMUNITY/spatialvla-4b-224-sft-bridge · Hugging Face",
            "url": "https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-sft-bridge"
          }
        ]
      },
      "Based on the search results, here's what I found about SpatialVLA:\n\n**Model Overview:**\nSpatialVLA is a spatial-enhanced vision-language-action model trained on 1.1 Million real robot episodes.\n\n**Model Size and Parameters:**\nThe search results indicate that the model comes in a 4B variant (as shown in the model name \"spatialvla-4b\"), where the \"4b\" refers to approximately 4 billion parameters. The model requires 8.5GB of GPU memory for inference.\n\n**Training Details:**\nSpatialVLA is pre-trained with 1.1 Million real-robot demonstrations from the OXE and RH20T dataset on a cluster of 64 A100 GPUs for about 10 days, using a batch size of 2048.\n\n**Model Type and Function:**\nSpatialVLA is a Vision-language-action model that takes language and image inputs to produce robot actions.\n\n**Action Output:**\nThe model includes functionality to predict and decode actions - the model uses a `predict_action` method that outputs generation results, which are then decoded using a `decode_actions` processor function.\n\nThe search results don't contain specific details about discrete action tokens or the exact parameter count beyond the \"4b\" designation. If you need more technical details about the action token representation, you may want to check the model's paper or detailed technical documentation."
    ],
    "durationSeconds": 6.336308798000013
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T16:23:09.322Z_

<details><summary>↩ Tool result · `toolu_01DJJBm4BPfCvrEjv8Se6go8`</summary>

```text
Web search results for query: "TraceVLA tracevla_phi3v model parameters size LIBERO evaluation 2024"

Links: [{"title":"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies","url":"https://arxiv.org/html/2412.10345v2"},{"title":"tracevla: visual trace prompting enhances spatial-temporal ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf"},{"title":"TraceVLA: Enhancing Robotic Spatial-Temporal Skills","url":"https://www.emergentmind.com/topics/tracevla"},{"title":"furonghuang-lab/tracevla_phi3v · Hugging Face","url":"https://huggingface.co/furonghuang-lab/tracevla_phi3v"},{"title":"Paper page - TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies","url":"https://huggingface.co/papers/2412.10345"},{"title":"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies","url":"https://tracevla.github.io/"},{"title":"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies","url":"https://arxiv.org/pdf/2412.10345"}]

Based on the search results, here's what I found about TraceVLA and the tracevla_phi3v model:

## Model Parameters and Size

TraceVLA is a 7B-parameter VLA model, while TraceVLA-Phi3 uses a 4B-parameter Phi-3-Vision backbone. The 4B Phi3-Vision VLA model was pretrained on the Open X-Embodiment dataset using a batch size of 4096 for 30 epochs with 32 H100 GPUs.

## Model Development

TraceVLA was developed by finetuning OpenVLA on a dataset of 150K robot manipulation trajectories using visual trace prompting. TraceVLA-Phi3 was finetuned on the Open X-Embodiments dataset, which comprises 970K trajectories across diverse robot embodiments, tasks, and scenes.

## Evaluation Results

While the search results don't specifically mention "LIBERO evaluation," they do provide evaluation details: TraceVLA was evaluated across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot, demonstrating state-of-the-art performance and outperforming OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks. Both the full-scale 7B models (TraceVLA vs OpenVLA) and their 4B versions (TraceVLA-Phi3 vs OpenVLA-Phi3) showed improvements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "e601ff15-34a2-4b13-bf44-c79fe4e7ebee",
  "tool_use_result": {
    "query": "TraceVLA tracevla_phi3v model parameters size LIBERO evaluation 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_011svJCXU2SVrbPSyhvDTUcE",
        "content": [
          {
            "title": "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies",
            "url": "https://arxiv.org/html/2412.10345v2"
          },
          {
            "title": "tracevla: visual trace prompting enhances spatial-temporal ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf"
          },
          {
            "title": "TraceVLA: Enhancing Robotic Spatial-Temporal Skills",
            "url": "https://www.emergentmind.com/topics/tracevla"
          },
          {
            "title": "furonghuang-lab/tracevla_phi3v · Hugging Face",
            "url": "https://huggingface.co/furonghuang-lab/tracevla_phi3v"
          },
          {
            "title": "Paper page - TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies",
            "url": "https://huggingface.co/papers/2412.10345"
          },
          {
            "title": "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies",
            "url": "https://tracevla.github.io/"
          },
          {
            "title": "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies",
            "url": "https://arxiv.org/pdf/2412.10345"
          }
        ]
      },
      "Based on the search results, here's what I found about TraceVLA and the tracevla_phi3v model:\n\n## Model Parameters and Size\n\nTraceVLA is a 7B-parameter VLA model, while TraceVLA-Phi3 uses a 4B-parameter Phi-3-Vision backbone. The 4B Phi3-Vision VLA model was pretrained on the Open X-Embodiment dataset using a batch size of 4096 for 30 epochs with 32 H100 GPUs.\n\n## Model Development\n\nTraceVLA was developed by finetuning OpenVLA on a dataset of 150K robot manipulation trajectories using visual trace prompting. TraceVLA-Phi3 was finetuned on the Open X-Embodiments dataset, which comprises 970K trajectories across diverse robot embodiments, tasks, and scenes.\n\n## Evaluation Results\n\nWhile the search results don't specifically mention \"LIBERO evaluation,\" they do provide evaluation details: TraceVLA was evaluated across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot, demonstrating state-of-the-art performance and outperforming OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks. Both the full-scale 7B models (TraceVLA vs OpenVLA) and their 4B versions (TraceVLA-Phi3 vs OpenVLA-Phi3) showed improvements."
    ],
    "durationSeconds": 5.874291628999999
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-19T16:23:11.110Z_

<details><summary>↩ Tool result · `toolu_01F8fL1LjQHYopENo9LbAA3a`</summary>

```text
Web search results for query: "TinyVLA Phi-2 VLA decoder-only open source weights huggingface 2024"

Links: [{"title":"bczhou/TinyLLaVA-1.5B · Hugging Face","url":"https://huggingface.co/bczhou/TinyLLaVA-1.5B"},{"title":"GitHub - TinyLLaVA/TinyLLaVA_Factory: A Framework of Small-scale Large Multimodal Models · GitHub","url":"https://github.com/TinyLLaVA/TinyLLaVA_Factory"},{"title":"bczhou/tiny-llava-v1-hf · Hugging Face","url":"https://huggingface.co/bczhou/tiny-llava-v1-hf"},{"title":"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2409.12514v1"},{"title":"hz1919810/TinyVLA-droid_diffusion_metaworld · Hugging Face","url":"https://huggingface.co/hz1919810/TinyVLA-droid_diffusion_metaworld"},{"title":"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/pdf/2409.12514"},{"title":"Paper page - TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://huggingface.co/papers/2409.12514"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

Based on the search results, I found relevant information about TinyVLA:

TinyVLA is a new family of compact vision-language-action models that offers two key advantages over existing VLA models: faster inference speeds and improved data efficiency, eliminating the need for pre-training stage.

The TinyVLA framework incorporates two essential components: initializing the policy backbone with robust, high-speed multimodal models, and integrating a diffusion policy decoder during fine-tuning to enable precise robot actions.

Extensive evaluations of TinyVLA in both simulation and on real robots demonstrated that the approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance.

Notably, there is a TinyLLaVA-Phi-2-SigLIP-3.1B model that achieves better overall performance against existing 7B models such as LLaVA-1.5 and Qwen-VL, which combines the Phi-2 language model with the TinyLLaVA framework. The weights and evaluation code for these models were made available on HuggingFace in February 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "a1d7dc85-03f2-4d30-8f7c-7b737f7e9d06",
  "tool_use_result": {
    "query": "TinyVLA Phi-2 VLA decoder-only open source weights huggingface 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_013GhqQ7MumNiLsbUy6rJycj",
        "content": [
          {
            "title": "bczhou/TinyLLaVA-1.5B · Hugging Face",
            "url": "https://huggingface.co/bczhou/TinyLLaVA-1.5B"
          },
          {
            "title": "GitHub - TinyLLaVA/TinyLLaVA_Factory: A Framework of Small-scale Large Multimodal Models · GitHub",
            "url": "https://github.com/TinyLLaVA/TinyLLaVA_Factory"
          },
          {
            "title": "bczhou/tiny-llava-v1-hf · Hugging Face",
            "url": "https://huggingface.co/bczhou/tiny-llava-v1-hf"
          },
          {
            "title": "TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2409.12514v1"
          },
          {
            "title": "hz1919810/TinyVLA-droid_diffusion_metaworld · Hugging Face",
            "url": "https://huggingface.co/hz1919810/TinyVLA-droid_diffusion_metaworld"
          },
          {
            "title": "TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2409.12514"
          },
          {
            "title": "Paper page - TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation",
            "url": "https://huggingface.co/papers/2409.12514"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          }
        ]
      },
      "Based on the search results, I found relevant information about TinyVLA:\n\nTinyVLA is a new family of compact vision-language-action models that offers two key advantages over existing VLA models: faster inference speeds and improved data efficiency, eliminating the need for pre-training stage.\n\nThe TinyVLA framework incorporates two essential components: initializing the policy backbone with robust, high-speed multimodal models, and integrating a diffusion policy decoder during fine-tuning to enable precise robot actions.\n\nExtensive evaluations of TinyVLA in both simulation and on real robots demonstrated that the approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance.\n\nNotably, there is a TinyLLaVA-Phi-2-SigLIP-3.1B model that achieves better overall performance against existing 7B models such as LLaVA-1.5 and Qwen-VL, which combines the Phi-2 language model with the TinyLLaVA framework. The weights and evaluation code for these models were made available on HuggingFace in February 2024."
    ],
    "durationSeconds": 6.118054533000002
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T16:23:12.240Z_

<details><summary>↩ Tool result · `toolu_018mv4zRsatAyRCaVUgHC9Sj`</summary>

```text
Web search results for query: "ECoT embodied chain thought VLA Llama backbone decoder-only open weights 2024"

Links: [{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://embodied-cot.github.io/"},{"title":"[2407.08693] Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2407.08693"},{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://openreview.net/pdf?id=S70MgnIA0v"},{"title":"GitHub - MichalZawalski/embodied-CoT: Embodied Chain of Thought: A robotic policy that reason to solve the task. · GitHub","url":"https://github.com/MichalZawalski/embodied-CoT"},{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2407.08693v1"},{"title":"GitHub - Everloom-129/ECoT: Research on the Embodied Chain of Thought: A robotic policy that reason to solve the task.","url":"https://github.com/Everloom-129/ECoT"},{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2407.08693"},{"title":"Fast ECoT: Efficient Embodied Chain-of-Thought via Thoughts Reuse","url":"https://arxiv.org/html/2506.07639v1"},{"title":"[2506.07639] Fast ECoT: Efficient Embodied Chain-of-Thought via Thoughts Reuse","url":"https://arxiv.org/abs/2506.07639"},{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning | OpenReview","url":"https://openreview.net/forum?id=S70MgnIA0v"}]

Based on the search results, here's what I found about ECoT:

ECoT (Embodied Chain-of-Thought Reasoning) is an approach for VLAs (Vision-Language-Action models) where VLAs are trained to perform multiple steps of reasoning about plans, sub-tasks, motions, and visually grounded features like object bounding boxes and end effector positions, before predicting the robot action.

**Key Technical Details:**

The approach uses the Llama 2 text tokenizer to translate reasoning elements into reasoning tokens. The codebase is built on top of OpenVLA.

**Performance:**

ECoT increases the absolute success rate of OpenVLA, the current strongest open-source VLA policy, by 28% across challenging generalization tasks, without any additional robot training data.

**Released Models:**

Two ECoT models were released: ecot-openvla-7b-bridge (trained on the Bridge dataset annotated with reasoning for 80k steps) and ecot-openvla-7b-oxe (initially trained on the Open-X-Embodiment dataset, fine-tuned on a mixture of OXE action-only data and Bridge reasonings for 20k steps). The code is released under an MIT License, though the pretrained models may inherit restrictions from underlying base models.

The paper was published in 2024 and presented at CoRL 2024 (Conference on Robot Learning).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "a6c86de9-6b0a-4657-b268-4e45d232cf8a",
  "tool_use_result": {
    "query": "ECoT embodied chain thought VLA Llama backbone decoder-only open weights 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LnfoZUdRtVhcCF6vH4nDTz",
        "content": [
          {
            "title": "Robotic Control via Embodied Chain-of-Thought Reasoning",
            "url": "https://embodied-cot.github.io/"
          },
          {
            "title": "[2407.08693] Robotic Control via Embodied Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/abs/2407.08693"
          },
          {
            "title": "Robotic Control via Embodied Chain-of-Thought Reasoning",
            "url": "https://openreview.net/pdf?id=S70MgnIA0v"
          },
          {
            "title": "GitHub - MichalZawalski/embodied-CoT: Embodied Chain of Thought: A robotic policy that reason to solve the task. · GitHub",
            "url": "https://github.com/MichalZawalski/embodied-CoT"
          },
          {
            "title": "Robotic Control via Embodied Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2407.08693v1"
          },
          {
            "title": "GitHub - Everloom-129/ECoT: Research on the Embodied Chain of Thought: A robotic policy that reason to solve the task.",
            "url": "https://github.com/Everloom-129/ECoT"
          },
          {
            "title": "Robotic Control via Embodied Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2407.08693"
          },
          {
            "title": "Fast ECoT: Efficient Embodied Chain-of-Thought via Thoughts Reuse",
            "url": "https://arxiv.org/html/2506.07639v1"
          },
          {
            "title": "[2506.07639] Fast ECoT: Efficient Embodied Chain-of-Thought via Thoughts Reuse",
            "url": "https://arxiv.org/abs/2506.07639"
          },
          {
            "title": "Robotic Control via Embodied Chain-of-Thought Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=S70MgnIA0v"
          }
        ]
      },
      "Based on the search results, here's what I found about ECoT:\n\nECoT (Embodied Chain-of-Thought Reasoning) is an approach for VLAs (Vision-Language-Action models) where VLAs are trained to perform multiple steps of reasoning about plans, sub-tasks, motions, and visually grounded features like object bounding boxes and end effector positions, before predicting the robot action.\n\n**Key Technical Details:**\n\nThe approach uses the Llama 2 text tokenizer to translate reasoning elements into reasoning tokens. The codebase is built on top of OpenVLA.\n\n**Performance:**\n\nECoT increases the absolute success rate of OpenVLA, the current strongest open-source VLA policy, by 28% across challenging generalization tasks, without any additional robot training data.\n\n**Released Models:**\n\nTwo ECoT models were released: ecot-openvla-7b-bridge (trained on the Bridge dataset annotated with reasoning for 80k steps) and ecot-openvla-7b-oxe (initially trained on the Open-X-Embodiment dataset, fine-tuned on a mixture of OXE action-only data and Bridge reasonings for 20k steps). The code is released under an MIT License, though the pretrained models may inherit restrictions from underlying base models.\n\nThe paper was published in 2024 and presented at CoRL 2024 (Conference on Robot Learning)."
    ],
    "durationSeconds": 7.750909503000003
  }
}
```

</details>

---

### Assistant

_source line 67_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check on a few more details:

1. **SpatialVLA** uses PaLiGemma2 (Gemma 2 backbone, decoder-only), 4B params, discrete action tokens, open weights. **STRONG CANDIDATE.**

2. **TraceVLA-Phi3** uses Phi-3-Vision (decoder-only), 4B params, discrete action tokens (same as OpenVLA), open weights. **STRONG CANDIDATE.**


3. **NORA** uses Qwen-2.5-VL-3B (decoder-only), 3B params, FAST+ tokenizer for action tokens, open weights. **STRONG CANDIDATE.**

4. **ECoT** is built on OpenVLA with the same Llama-2 backbone, so it's less ideal since I'm looking for different architectures.

5. **TinyVLA** combines Phi-2 with a diffusion policy decoder, which doesn't fit the purely decoder-only requirement for actions.

I should verify whether there's an OpenVLA variant using Phi-3 instead of Llama-2.

Actually, TraceVLA mentions "OpenVLA-Phi3" as a baseline, so that variant does exist. But I need to reconsider what "decoder-only" really means here. π0-FAST uses autoregressive discretization with the FAST tokenizer, but the underlying π0 architecture still relies on cross-attention between the PaliGemma VLM and the action expert—it's not purely causal attention. For my analysis to work, I need models where the LLM backbone processes vision, language, and action tokens through the same causal attention mechanism so I can extract meaningful attention patterns from those layers.

Looking at which models actually fit this criterion: OpenVLA with Llama-2, SpatialVLA with Gemma 2, TraceVLA-Phi3, and NORA with Qwen-2.5 all route everything through their decoder backbone, though NORA's FAST+ tokenizer does change how actions are represented. Models like π0, SmolVLA, and GR00 don't work because they use separate action experts with cross-attention instead.

I also need to account for encoder-decoder architectures with diffusion heads like CogACT and TinyVLA, which take a different approach entirely. For the analysis framework itself, I need to extract attention matrices from the LLM backbone and track which tokens are instructions, vision, or actions flowing through the same causal attention mechanism. I should verify whether SpatialVLA uses the same discrete action tokens as OpenVLA, and I need to be careful with NORA since its FAST+ tokenizer compresses actions into variable-length tokens rather than using simple discrete tokens like OpenVLA does.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "8e818e3e-4795-4de2-960b-de50d4d332d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wWmTFnRqfo4vhq4UNTos9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 4644,
      "cache_read_input_tokens": 42200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4644
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

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q5wTiuivridhj4uFNMhs28`</summary>

```json
{
  "query": "SpatialVLA action prediction discrete tokens autoregressive next-token-prediction Gemma architecture details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "20d10bb7-c47c-4b9c-99e7-b41a617f5978",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wWmTFnRqfo4vhq4UNTos9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 4644,
      "cache_read_input_tokens": 42200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4644
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

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NPhkKvm34VeiiGE7c5BWvr`</summary>

```json
{
  "query": "NORA VLA Qwen-2.5-VL FAST+ tokenizer action prediction autoregressive causal attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "b8cf1847-247c-49e6-b162-a558bada29e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wWmTFnRqfo4vhq4UNTos9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 4644,
      "cache_read_input_tokens": 42200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4644
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

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Wc2hdzwP3tdwvY266BSPJ`</summary>

```json
{
  "query": "\"OpenVLA\" \"Phi-3\" variant openvla-phi3 backbone huggingface 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "5711a4ec-04d7-4301-8100-03cb20149a41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wWmTFnRqfo4vhq4UNTos9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 4644,
      "cache_read_input_tokens": 42200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4644
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

### Tool result

_source line 71 · 2026-05-19T16:23:43.165Z_

<details><summary>↩ Tool result · `toolu_015Wc2hdzwP3tdwvY266BSPJ`</summary>

```text
Web search results for query: ""OpenVLA" "Phi-3" variant openvla-phi3 backbone huggingface 2024 2025"

Links: [{"title":"furonghuang-lab/openvla_phi3v · Hugging Face","url":"https://huggingface.co/furonghuang-lab/openvla_phi3v"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.","url":"https://github.com/openvla/openvla?tab=readme-ov-file"},{"title":"SpatialVLA (SpatialVLA) · GitHub","url":"https://github.com/SpatialVLA"},{"title":"MBZUAI/LLaVA-Phi-3-mini-4k-instruct · Hugging Face","url":"https://huggingface.co/MBZUAI/LLaVA-Phi-3-mini-4k-instruct"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"openvla/openvla-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b"}]

Based on the search results, here's what I found about the OpenVLA Phi-3 variant:

## OpenVLA-Phi3V Model

OpenVLA-Phi3V is a vision-language-action model obtained by finetuning the base Phi3V Model on the same Open X-Embodiment robot mixture dataset as the original OpenVLA model. The model is available on Hugging Face through the furonghuang-lab organization.

The model was updated on January 7, 2025, and is associated with research on "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies," which was published in 2024.

The OpenVLA-Phi3V variant extends the OpenVLA framework to use Phi-3V as the backbone instead of the original architecture used in the base OpenVLA-7B model, which was trained on 970K robot manipulation episodes from the Open X-Embodiment dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "3e809fcf-4d60-4306-ae84-7969bac46b00",
  "tool_use_result": {
    "query": "\"OpenVLA\" \"Phi-3\" variant openvla-phi3 backbone huggingface 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BYAUTEYwdCEH1h7jTzZ56F",
        "content": [
          {
            "title": "furonghuang-lab/openvla_phi3v · Hugging Face",
            "url": "https://huggingface.co/furonghuang-lab/openvla_phi3v"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.",
            "url": "https://github.com/openvla/openvla?tab=readme-ov-file"
          },
          {
            "title": "SpatialVLA (SpatialVLA) · GitHub",
            "url": "https://github.com/SpatialVLA"
          },
          {
            "title": "MBZUAI/LLaVA-Phi-3-mini-4k-instruct · Hugging Face",
            "url": "https://huggingface.co/MBZUAI/LLaVA-Phi-3-mini-4k-instruct"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/CHELabUB/openvla"
          },
          {
            "title": "openvla/openvla-7b · Hugging Face",
            "url": "https://huggingface.co/openvla/openvla-7b"
          }
        ]
      },
      "Based on the search results, here's what I found about the OpenVLA Phi-3 variant:\n\n## OpenVLA-Phi3V Model\n\nOpenVLA-Phi3V is a vision-language-action model obtained by finetuning the base Phi3V Model on the same Open X-Embodiment robot mixture dataset as the original OpenVLA model. The model is available on Hugging Face through the furonghuang-lab organization.\n\nThe model was updated on January 7, 2025, and is associated with research on \"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies,\" which was published in 2024.\n\nThe OpenVLA-Phi3V variant extends the OpenVLA framework to use Phi-3V as the backbone instead of the original architecture used in the base OpenVLA-7B model, which was trained on 970K robot manipulation episodes from the Open X-Embodiment dataset."
    ],
    "durationSeconds": 5.783968949999981
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T16:23:43.329Z_

<details><summary>↩ Tool result · `toolu_01Q5wTiuivridhj4uFNMhs28`</summary>

```text
Web search results for query: "SpatialVLA action prediction discrete tokens autoregressive next-token-prediction Gemma architecture details"

Links: [{"title":"[Literature Review] SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://www.themoonlight.io/en/review/spatialvla-exploring-spatial-representations-for-visual-language-action-model"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/395370588_SpatialVLA_Exploring_Spatial_Representations_for_Visual-Language-Action_Models"},{"title":"10 Open Challenges Steering the Future of Vision-Language-Action Models","url":"https://arxiv.org/html/2511.05936v1"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models","url":"https://spatialvla.github.io/"},{"title":"arXiv:2503.10631v3 [cs.CV] 23 Jun 2025","url":"https://arxiv.org/pdf/2503.10631"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.pi.website/download/fast.pdf"},{"title":"E0: Enhancing Generalization and Fine-Grained Control in VLA Models via Tweedie Discrete Diffusion","url":"https://arxiv.org/pdf/2511.21542"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://arxiv.org/pdf/2501.15830"}]

Based on the search results, here's information about SpatialVLA and its architecture:

## SpatialVLA Overview

SpatialVLA is a novel framework for enhancing robot manipulation through improved spatial understanding using a Visual-Language-Action (VLA) model that utilizes a combination of ego-centric spatial representations, adaptive action grids, and a comprehensive pre-training strategy.

## Architecture

SpatialVLA is built upon a vision-language model, specifically using the Paligemma2 backbone.

## Action Prediction Approach

Given an image observation and a natural language task instruction, the model processes the image observation with Ego3D Position Encoding and auto-regressively predict spatial action tokens that are de-tokenized to continuous actions for robot control.

The model consists of three key components: (1) the model first extracts 2D semantic features with SigLIP vision encoder and injects 3D spatial context with Ego3D Position Encoding; (2) the spatial action movements are discretized by a unified adaptive action grids and represented with separate spatial action tokens for prediction; (3) the action grids and spatial action tokens are able to adjust and update for effective adaption to new robot setups.

## Training Objective

During training, the model learns generalized representations using an autoregressive next-token prediction objective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "5864e724-597c-4a4c-a12b-f5350b65b154",
  "tool_use_result": {
    "query": "SpatialVLA action prediction discrete tokens autoregressive next-token-prediction Gemma architecture details",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TvRTYxtt527ipENXk7upGW",
        "content": [
          {
            "title": "[Literature Review] SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model",
            "url": "https://www.themoonlight.io/en/review/spatialvla-exploring-spatial-representations-for-visual-language-action-model"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | Request PDF",
            "url": "https://www.researchgate.net/publication/395370588_SpatialVLA_Exploring_Spatial_Representations_for_Visual-Language-Action_Models"
          },
          {
            "title": "10 Open Challenges Steering the Future of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.05936v1"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models",
            "url": "https://spatialvla.github.io/"
          },
          {
            "title": "arXiv:2503.10631v3 [cs.CV] 23 Jun 2025",
            "url": "https://arxiv.org/pdf/2503.10631"
          },
          {
            "title": "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies",
            "url": "https://arxiv.org/html/2508.20072v1"
          },
          {
            "title": "FAST: Efficient Action Tokenization for Vision-Language-Action Models",
            "url": "https://www.pi.website/download/fast.pdf"
          },
          {
            "title": "E0: Enhancing Generalization and Fine-Grained Control in VLA Models via Tweedie Discrete Diffusion",
            "url": "https://arxiv.org/pdf/2511.21542"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model",
            "url": "https://arxiv.org/pdf/2501.15830"
          }
        ]
      },
      "Based on the search results, here's information about SpatialVLA and its architecture:\n\n## SpatialVLA Overview\n\nSpatialVLA is a novel framework for enhancing robot manipulation through improved spatial understanding using a Visual-Language-Action (VLA) model that utilizes a combination of ego-centric spatial representations, adaptive action grids, and a comprehensive pre-training strategy.\n\n## Architecture\n\nSpatialVLA is built upon a vision-language model, specifically using the Paligemma2 backbone.\n\n## Action Prediction Approach\n\nGiven an image observation and a natural language task instruction, the model processes the image observation with Ego3D Position Encoding and auto-regressively predict spatial action tokens that are de-tokenized to continuous actions for robot control.\n\nThe model consists of three key components: (1) the model first extracts 2D semantic features with SigLIP vision encoder and injects 3D spatial context with Ego3D Position Encoding; (2) the spatial action movements are discretized by a unified adaptive action grids and represented with separate spatial action tokens for prediction; (3) the action grids and spatial action tokens are able to adjust and update for effective adaption to new robot setups.\n\n## Training Objective\n\nDuring training, the model learns generalized representations using an autoregressive next-token prediction objective."
    ],
    "durationSeconds": 7.059952392000007
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-19T16:23:45.158Z_

<details><summary>↩ Tool result · `toolu_01NPhkKvm34VeiiGE7c5BWvr`</summary>

```text
Web search results for query: "NORA VLA Qwen-2.5-VL FAST+ tokenizer action prediction autoregressive causal attention"

Links: [{"title":"NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards","url":"https://arxiv.org/html/2511.14659v1"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks","url":"https://arxiv.org/pdf/2504.19854"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/html/2504.19854v1"},{"title":"[Literature Review] NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards","url":"https://www.themoonlight.io/en/review/nora-15-a-vision-language-action-model-trained-using-world-model-and-action-based-preference-rewards"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://declare-lab.github.io/nora"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=FAST++tokenizer"},{"title":"Paper page - NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://huggingface.co/papers/2504.19854"},{"title":"NORA-1.5: A Vision-Language-Action Model Trained using World Model-","url":"https://arxiv.org/pdf/2511.14659"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2501.09747"}]

Based on the search results, here's what I found about NORA, VLA, Qwen-2.5-VL, FAST+ tokenizer, and action prediction:

## NORA Model Architecture

NORA is a 3B-parameter auto-regressive Vision-Language-Action (VLA) model obtained by fine-tuning Qwen-2.5-VL-3B on the Open X-Embodiment dataset to predict action tokens. NORA is trained on 970k real-world robot demonstrations and equipped with the FAST+ tokenizer for efficient action sequence generation.

## Qwen-2.5-VL Backbone

Qwen-2.5-VL-3B is used as the VLM backbone for NORA due to its excellent balance between performance and efficiency at this scale. NORA leverages its strong general world knowledge, multi-modal reasoning, representation learning, and instruction-following capabilities.

## FAST+ Tokenizer

The FAST+ tokenizer is used to discretize the continuous action tokens, given its proven efficacy across a wide range of action sequences, including single-arm, bi-manual, and mobile robot tasks, making it a strong choice for training autoregressive VLA models. FAST+ is a universal robot action tokenizer, trained on 1M real robot action trajectories that cover a large diversity of robot embodiments, action spaces and control frequencies.

## Action Prediction

FAST enables autoregressive VLA policies via simple next token prediction for highly dexterous and high-frequency tasks. The model uses causal attention as part of its autoregressive architecture for generating action sequences sequentially.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "25a6b587-34b1-43ee-a5aa-74b36d2edd0d",
  "tool_use_result": {
    "query": "NORA VLA Qwen-2.5-VL FAST+ tokenizer action prediction autoregressive causal attention",
    "results": [
      {
        "tool_use_id": "srvtoolu_016ZWrs8H3hf9C7kBZNmaJ9r",
        "content": [
          {
            "title": "NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards",
            "url": "https://arxiv.org/html/2511.14659v1"
          },
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks",
            "url": "https://arxiv.org/pdf/2504.19854"
          },
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://arxiv.org/html/2504.19854v1"
          },
          {
            "title": "[Literature Review] NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards",
            "url": "https://www.themoonlight.io/en/review/nora-15-a-vision-language-action-model-trained-using-world-model-and-action-based-preference-rewards"
          },
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://declare-lab.github.io/nora"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=FAST++tokenizer"
          },
          {
            "title": "Paper page - NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://huggingface.co/papers/2504.19854"
          },
          {
            "title": "NORA-1.5: A Vision-Language-Action Model Trained using World Model-",
            "url": "https://arxiv.org/pdf/2511.14659"
          },
          {
            "title": "FAST: Efficient Action Tokenization for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2501.09747"
          }
        ]
      },
      "Based on the search results, here's what I found about NORA, VLA, Qwen-2.5-VL, FAST+ tokenizer, and action prediction:\n\n## NORA Model Architecture\n\nNORA is a 3B-parameter auto-regressive Vision-Language-Action (VLA) model obtained by fine-tuning Qwen-2.5-VL-3B on the Open X-Embodiment dataset to predict action tokens. NORA is trained on 970k real-world robot demonstrations and equipped with the FAST+ tokenizer for efficient action sequence generation.\n\n## Qwen-2.5-VL Backbone\n\nQwen-2.5-VL-3B is used as the VLM backbone for NORA due to its excellent balance between performance and efficiency at this scale. NORA leverages its strong general world knowledge, multi-modal reasoning, representation learning, and instruction-following capabilities.\n\n## FAST+ Tokenizer\n\nThe FAST+ tokenizer is used to discretize the continuous action tokens, given its proven efficacy across a wide range of action sequences, including single-arm, bi-manual, and mobile robot tasks, making it a strong choice for training autoregressive VLA models. FAST+ is a universal robot action tokenizer, trained on 1M real robot action trajectories that cover a large diversity of robot embodiments, action spaces and control frequencies.\n\n## Action Prediction\n\nFAST enables autoregressive VLA policies via simple next token prediction for highly dexterous and high-frequency tasks. The model uses causal attention as part of its autoregressive architecture for generating action sequences sequentially."
    ],
    "durationSeconds": 8.069127387999993
  }
}
```

</details>

---

### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have a very complete picture. Let me also fetch the details about the A1 model to check its architecture.

Let me summarize what I've found:

## Decoder-only VLA candidates (ranked by suitability):

### 1. SpatialVLA (4B, PaLiGemma2 / Gemma 2 backbone)
- **Architecture**: Decoder-only (Gemma 2 LLM + SigLIP vision encoder)
- **Backbone**: Gemma 2 (DIFFERENT from OpenVLA's Llama-2) ✓


- **Action prediction**: Autoregressive discrete tokens (spatial action tokens) ✓
- **Weights**: Open (IPEC-COMMUNITY/spatialvla-4b-224-pt on HuggingFace) ✓
- **Size**: ~4B params, fits on 2×96GB easily ✓
- **Training data**: 1.1M real robot episodes (OXE + RH20T)
- **Framework**: PyTorch (HuggingFace Transformers) ✓
- **Adaptation**: Standard HuggingFace VLM, attention extraction straightforward
- **Pros**: Different backbone with autoregressive discrete tokens following the same paradigm as OpenVLA, well-documented with an active community
- **Cons**: Uses adaptive action grids instead of OpenVLA's 256-bin tokens, so I'll need to understand their tokenization scheme

Now looking at NORA, which runs on a 3B Qwen-2.5-VL backbone instead of Llama-2. It's also decoder-only with autoregressive action prediction via FAST+ tokenizer, has open weights on HuggingFace, and was trained on 970K episodes from OXE.

The main trade-off with NORA is that FAST+ produces variable-length action tokens rather than fixed 256-bin tokens, which could complicate attention analysis since action boundaries aren't as clear. Plus Qwen-2.5-VL uses dynamic resolution, so the number of vision tokens varies.

TraceVLA-Phi3 is another option with a 4B Phi-3-Vision backbone—it's decoder-only and crucially uses the same discrete 256-bin action tokens as OpenVLA, which would make direct comparison much cleaner.

Actually, OpenVLA-Phi3V stands out as the ideal choice because it's the exact same training recipe and data as the original OpenVLA, just with a different backbone, making it the most directly comparable architecture for isolating how backbone changes affect attention patterns.

For negative controls, I should look at architectures that diverge more fundamentally—π0 uses cross-attention MoE, SmolVLA has a separate action expert, and GR00T-N1 is encoder-decoder with diffusion, so none of these would show the same L1 routing pattern if it's specific to decoder-only designs.

I'm also noting that ECoT and CogACT both build on OpenVLA in ways that muddy the comparison, so they're less useful as independent validation points.

Now I'm checking whether PaLiGemma2, which powers SpatialVLA, truly processes actions through a decoder-only pathway—and it does: the vision encoder feeds into a linear projection, then everything flows through Gemma 2's causal decoder, so action tokens get the same treatment as text tokens. That's another solid decoder-only candidate to include.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "9242a651-53df-4885-bc4d-0379c3871792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjPo56NT7kaBGddRDwiGNm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 708,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 46844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3615
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

_source line 75_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NAZNp5vbEHVCwVpCQxWns8`</summary>

```json
{
  "query": "A1 VLA model architecture backbone Qwen InternVL decoder-only flow matching 2025 open weights github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "d23abdbc-de64-4fc6-a8cb-2f258ef24753",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjPo56NT7kaBGddRDwiGNm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 708,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 46844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3615
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

_source line 76_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019SbJ2N2brpNgfPASi72YZZ`</summary>

```json
{
  "url": "https://huggingface.co/furonghuang-lab/openvla_phi3v",
  "prompt": "What is this model? What backbone does it use? What is the model size? What action tokenization does it use (discrete bins or other)? Is it decoder-only? What dataset was it trained on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "c29029d9-558e-426a-b472-1cdb5cad0114",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjPo56NT7kaBGddRDwiGNm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 708,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 46844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3615
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

_source line 77 · 2026-05-19T16:24:21.317Z_

<details><summary>↩ Tool result · `toolu_019SbJ2N2brpNgfPASi72YZZ`</summary>

````text
# OpenVLA-Phi3V Model Summary

## What is this model?
OpenVLA-Phi3V is a **vision-language-action (VLA) model** designed for robotic control. It was created by fine-tuning the base Phi3V model on the Open X-Embodiment robot mixture dataset, the same dataset used for the original OpenVLA-7B model.

## Backbone
**Phi3V** - a vision-language model that serves as the foundation for this VLA variant.

## Model Size
Not explicitly specified in the provided content.

## Action Tokenization
The model uses **continuous action outputs** (not discrete bins). This is evident from the inference code, which loads dataset statistics for action normalization:

```python
action_norm_stats = json.load(file)[dataset_name]['action']
model.prepare_action_inference(action_norm_stats, processor.tokenizer.vocab_size)
```

The model predicts continuous action values that are normalized/denormalized using dataset statistics.

## Architecture
**Decoder-only** - It uses `AutoModelForCausalLM`, indicating a causal language model architecture.

## Training Dataset
**Open X-Embodiment robot mixture dataset** - the same multi-robot demonstration dataset used for training the original OpenVLA model. The model is fine-tuned on robot manipulation tasks.

## Performance
The model shows competitive results on SimplerEnv benchmarks (Fractal and Bridge environments) for robotic manipulation tasks like picking, moving, opening drawers, and stacking blocks.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "3ca4bfb5-3792-436c-af5d-d40bc3b15326",
  "tool_use_result": {
    "bytes": 127775,
    "code": 200,
    "codeText": "OK",
    "result": "# OpenVLA-Phi3V Model Summary\n\n## What is this model?\nOpenVLA-Phi3V is a **vision-language-action (VLA) model** designed for robotic control. It was created by fine-tuning the base Phi3V model on the Open X-Embodiment robot mixture dataset, the same dataset used for the original OpenVLA-7B model.\n\n## Backbone\n**Phi3V** - a vision-language model that serves as the foundation for this VLA variant.\n\n## Model Size\nNot explicitly specified in the provided content.\n\n## Action Tokenization\nThe model uses **continuous action outputs** (not discrete bins). This is evident from the inference code, which loads dataset statistics for action normalization:\n\n```python\naction_norm_stats = json.load(file)[dataset_name]['action']\nmodel.prepare_action_inference(action_norm_stats, processor.tokenizer.vocab_size)\n```\n\nThe model predicts continuous action values that are normalized/denormalized using dataset statistics.\n\n## Architecture\n**Decoder-only** - It uses `AutoModelForCausalLM`, indicating a causal language model architecture.\n\n## Training Dataset\n**Open X-Embodiment robot mixture dataset** - the same multi-robot demonstration dataset used for training the original OpenVLA model. The model is fine-tuned on robot manipulation tasks.\n\n## Performance\nThe model shows competitive results on SimplerEnv benchmarks (Fractal and Bridge environments) for robotic manipulation tasks like picking, moving, opening drawers, and stacking blocks.",
    "durationMs": 5760,
    "url": "https://huggingface.co/furonghuang-lab/openvla_phi3v"
  }
}
````

</details>

---

### Tool result

_source line 78 · 2026-05-19T16:24:31.772Z_

<details><summary>↩ Tool result · `toolu_01NAZNp5vbEHVCwVpCQxWns8`</summary>

```text
Web search results for query: "A1 VLA model architecture backbone Qwen InternVL decoder-only flow matching 2025 open weights github"

Links: [{"title":"Qwen-VL: A Frontier Large Vision-Language Model with Versatile Abilities | Request PDF","url":"https://www.researchgate.net/publication/373363993_Qwen-VL_A_Frontier_Large_Vision-Language_Model_with_Versatile_Abilities"},{"title":"One of the best VLA models — Qwen 3VL 😁","url":"https://medium.com/@zlodeibaal/one-of-the-best-vla-models-qwen-3vl-d-551cf9bf2e60"},{"title":"Qwen Models: Evolution of Multimodal LLMs","url":"https://www.emergentmind.com/topics/qwen-models"},{"title":"Qwen3-VL: Scalable Cloud & Mobile LVLMs","url":"https://www.emergentmind.com/topics/qwen3-vl-model-series"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models","url":"https://arxiv.org/pdf/2509.04063"},{"title":"NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards","url":"https://arxiv.org/pdf/2511.14659"},{"title":"StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation","url":"https://arxiv.org/pdf/2603.28565"}]

Let me search more specifically for the A1 VLA model with InternVL architecture:

Links: [{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"GitHub - OpenGVLab/InternVL: [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-4o. 近GPT-4o表现的开源多模态对话模型 · GitHub","url":"https://github.com/opengvlab/internvl"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal   Models with Open-Source Suites","url":"https://arxiv.org/pdf/2404.16821"},{"title":"GitHub - zli12321/Vision-Language-Models-Overview: A most Frontend Collection and survey of vision-language model papers, and models GitHub repository. Continuous updates. · GitHub","url":"https://github.com/zli12321/Vision-Language-Models-Overview"},{"title":"StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing","url":"https://arxiv.org/pdf/2604.05014"},{"title":"Scalable, Training-Free Visual Language Robotics: A Modular Multi-Model   Framework for Consumer-Grade GPUs","url":"https://arxiv.org/pdf/2502.01071"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

Perfect! I found the A1 model. Let me search for more specific information about InternVLA-A1:

Links: [{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"GitHub - InternRobotics/InternVLA-A1: InternVLA-A1: Unifying Understanding, Generation, and Action for Robotic Manipulation​","url":"https://github.com/InternRobotics/InternVLA-A1"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"GitHub - InternRobotics/InternVLA-M1: InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy · GitHub","url":"https://github.com/InternRobotics/InternVLA-M1"},{"title":"GitHub - OpenGVLab/InternVL: [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-4o. 接近GPT-4o表现的开源多模态对话模型 · GitHub","url":"https://github.com/OpenGVLab/InternVL"},{"title":"GitHub - InternRobotics/InternManip: An All-in-one robot manipulation learning suite for policy models training and evaluation on various datasets and benchmarks.","url":"https://github.com/InternRobotics/InternManip"},{"title":"Decentralized Autoregressive Generation","url":"https://arxiv.org/pdf/2601.03184"},{"title":"GitHub - InternRobotics/InternVLA-M1: InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy","url":"https://github.com/InternRobotics/InternVLA-M1/tree/InternVLA-M1"}]

Based on my web search results, I can provide you with comprehensive information about the A1 VLA model architecture:

## A1 Model Overview

A1 is a Vision-Language-Action (VLA) model that uses a large-scale Vision-Language Model (VLM) to compress multimodal observations into a latent representation, with an action head that is flow-matching-based to map this latent into continuous motor commands. This design inherits strong semantics from pretrained VLMs and expressive generative decoders.

## Architecture Details

The model monitors action consistency across intermediate VLM layers to trigger early termination, and proposes Inter-Layer Truncated Flow Matching that warm-starts denoising across layers, enabling accurate actions with substantially fewer effective denoising iterations.

## Backbone and Performance

Across simulation benchmarks (LIBERO, VLABench) and real robots (Franka, AgiBot), A1 achieves state-of-the-art success rates while significantly reducing inference cost (e.g., up to 72% lower per-episode latency for flow-matching inference and up to 76.6% backbone computation reduction with minor performance degradation).

## Open Source Availability

The code is available at https://github.com/ATeam-Research/A1 with a project page at http://www.ateam.xin/#/research/A1, with the paper dated April 9, 2026.

Additionally, InternVLA-A1 is listed as "Unifying Understanding, Generation and Action for Robotic Manipulation" with available paper, project, and code resources for 2025. The InternVLA-A1 model is available on GitHub with code to replace default implementations of model modules (e.g., π0, InternVLA_A1_3B, InternVLA_A1_2B) to support custom architectures for robot learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "bc31d694-2379-4365-8a64-3814c436b848",
  "tool_use_result": {
    "query": "A1 VLA model architecture backbone Qwen InternVL decoder-only flow matching 2025 open weights github",
    "results": [
      {
        "tool_use_id": "srvtoolu_014X9BMC1zKXR3Zxv9JKAJcE",
        "content": [
          {
            "title": "Qwen-VL: A Frontier Large Vision-Language Model with Versatile Abilities | Request PDF",
            "url": "https://www.researchgate.net/publication/373363993_Qwen-VL_A_Frontier_Large_Vision-Language_Model_with_Versatile_Abilities"
          },
          {
            "title": "One of the best VLA models — Qwen 3VL 😁",
            "url": "https://medium.com/@zlodeibaal/one-of-the-best-vla-models-qwen-3vl-d-551cf9bf2e60"
          },
          {
            "title": "Qwen Models: Evolution of Multimodal LLMs",
            "url": "https://www.emergentmind.com/topics/qwen-models"
          },
          {
            "title": "Qwen3-VL: Scalable Cloud & Mobile LVLMs",
            "url": "https://www.emergentmind.com/topics/qwen3-vl-model-series"
          },
          {
            "title": "LangForce: Bayesian Decomposition of Vision Language ...",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models",
            "url": "https://arxiv.org/pdf/2509.04063"
          },
          {
            "title": "NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards",
            "url": "https://arxiv.org/pdf/2511.14659"
          },
          {
            "title": "StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation",
            "url": "https://arxiv.org/pdf/2603.28565"
          }
        ]
      },
      "Let me search more specifically for the A1 VLA model with InternVL architecture:",
      {
        "tool_use_id": "srvtoolu_01JPD2iVLicWrfdJYsk4R9hm",
        "content": [
          {
            "title": "A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model",
            "url": "https://arxiv.org/pdf/2604.05672"
          },
          {
            "title": "GitHub - OpenGVLab/InternVL: [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-4o. 近GPT-4o表现的开源多模态对话模型 · GitHub",
            "url": "https://github.com/opengvlab/internvl"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal   Models with Open-Source Suites",
            "url": "https://arxiv.org/pdf/2404.16821"
          },
          {
            "title": "GitHub - zli12321/Vision-Language-Models-Overview: A most Frontend Collection and survey of vision-language model papers, and models GitHub repository. Continuous updates. · GitHub",
            "url": "https://github.com/zli12321/Vision-Language-Models-Overview"
          },
          {
            "title": "StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing",
            "url": "https://arxiv.org/pdf/2604.05014"
          },
          {
            "title": "Scalable, Training-Free Visual Language Robotics: A Modular Multi-Model   Framework for Consumer-Grade GPUs",
            "url": "https://arxiv.org/pdf/2502.01071"
          },
          {
            "title": "SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data",
            "url": "https://huggingface.co/blog/smolvla"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          }
        ]
      },
      "Perfect! I found the A1 model. Let me search for more specific information about InternVLA-A1:",
      {
        "tool_use_id": "srvtoolu_01SLVgs7PiHibT29mHtHQhQm",
        "content": [
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "GitHub - InternRobotics/InternVLA-A1: InternVLA-A1: Unifying Understanding, Generation, and Action for Robotic Manipulation​",
            "url": "https://github.com/InternRobotics/InternVLA-A1"
          },
          {
            "title": "A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model",
            "url": "https://arxiv.org/pdf/2604.05672"
          },
          {
            "title": "GitHub - InternRobotics/InternVLA-M1: InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy · GitHub",
            "url": "https://github.com/InternRobotics/InternVLA-M1"
          },
          {
            "title": "GitHub - OpenGVLab/InternVL: [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-4o. 接近GPT-4o表现的开源多模态对话模型 · GitHub",
            "url": "https://github.com/OpenGVLab/InternVL"
          },
          {
            "title": "GitHub - InternRobotics/InternManip: An All-in-one robot manipulation learning suite for policy models training and evaluation on various datasets and benchmarks.",
            "url": "https://github.com/InternRobotics/InternManip"
          },
          {
            "title": "Decentralized Autoregressive Generation",
            "url": "https://arxiv.org/pdf/2601.03184"
          },
          {
            "title": "GitHub - InternRobotics/InternVLA-M1: InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy",
            "url": "https://github.com/InternRobotics/InternVLA-M1/tree/InternVLA-M1"
          }
        ]
      },
      "Based on my web search results, I can provide you with comprehensive information about the A1 VLA model architecture:\n\n## A1 Model Overview\n\nA1 is a Vision-Language-Action (VLA) model that uses a large-scale Vision-Language Model (VLM) to compress multimodal observations into a latent representation, with an action head that is flow-matching-based to map this latent into continuous motor commands. This design inherits strong semantics from pretrained VLMs and expressive generative decoders.\n\n## Architecture Details\n\nThe model monitors action consistency across intermediate VLM layers to trigger early termination, and proposes Inter-Layer Truncated Flow Matching that warm-starts denoising across layers, enabling accurate actions with substantially fewer effective denoising iterations.\n\n## Backbone and Performance\n\nAcross simulation benchmarks (LIBERO, VLABench) and real robots (Franka, AgiBot), A1 achieves state-of-the-art success rates while significantly reducing inference cost (e.g., up to 72% lower per-episode latency for flow-matching inference and up to 76.6% backbone computation reduction with minor performance degradation).\n\n## Open Source Availability\n\nThe code is available at https://github.com/ATeam-Research/A1 with a project page at http://www.ateam.xin/#/research/A1, with the paper dated April 9, 2026.\n\nAdditionally, InternVLA-A1 is listed as \"Unifying Understanding, Generation and Action for Robotic Manipulation\" with available paper, project, and code resources for 2025. The InternVLA-A1 model is available on GitHub with code to replace default implementations of model modules (e.g., π0, InternVLA_A1_3B, InternVLA_A1_2B) to support custom architectures for robot learning."
    ],
    "durationSeconds": 17.349711095999986
  }
}
```

</details>

---

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
Interesting - the WebFetch says OpenVLA-Phi3V uses continuous action outputs, not discrete bins. Let me re-check this. Actually, looking at the code snippet, it mentions `action_norm_stats` for normalization - this is actually similar to OpenVLA's approach where the model outputs discrete tokens that are then denormalized. Let me check the OpenVLA code - OpenVLA uses 256 discrete bins, and then denormalizes them using action statistics. The fact that it loads `action_norm_stats` suggests it uses the same discretization approach.


There's a discrepancy between the documentation saying "continuous" and the code loading normalization statistics, which points toward discrete tokens being denormalized to continuous values like OpenVLA does. The `prepare_action_inference` call with vocab_size confirms it's likely using discrete bins. Now I need to compile everything into the report, though I should double-check if there's another model I'm missing.

I'm also thinking through what makes the best fit for our specific needs: a decoder-only LLM backbone that handles vision, language, and action tokens with causal attention, uses a different backbone than Llama-2, has open weights on HuggingFace, employs discrete action tokenization for comparability with OpenVLA, runs on PyTorch, fits within our GPU constraints, and doesn't require extensive adaptation work. Based on these criteria, OpenVLA-Phi3V stands out as the top candidate since it uses the same training approach as the original OpenVLA.

but swaps in Phi-3 as the backbone, making it the most controlled comparison possible. SpatialVLA comes in second with its Gemma 2 backbone and well-documented autoregressive discrete tokens, offering a different architecture while maintaining the same action tokenization approach.

For the third option, NORA uses Qwen-2.5-VL with a FAST+ tokenizer that produces variable-length tokens instead of the fixed 256-bin discretization, which could complicate analyzing attention patterns and make the comparison less clean.

As a negative control, π0 uses a cross-attention MoE architecture rather than decoder-only, so it shouldn't exhibit the L1 instruction routing pattern I'm looking for.

I need to reconsider OpenVLA-Phi3V though—the code shows it's using discrete tokenization with denormalization at inference time, which is actually the same approach as the original OpenVLA, just with continuous outputs applied afterward. So this is still a valid discrete action tokenization scheme.

Now I can write up the full report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "d4f508eb-4ee4-422a-b449-07f726f5c04c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5dANhNkpiFS2v8Ltc6h6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 384,
      "cache_creation_input_tokens": 4485,
      "cache_read_input_tokens": 50459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4485
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 80_

信息收集完毕。现在写调研报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "3efbcc02-33ac-4ae2-be3e-429a7c1d4c2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5dANhNkpiFS2v8Ltc6h6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 384,
      "cache_creation_input_tokens": 4485,
      "cache_read_input_tokens": 50459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4485
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TnXJeKrCYCrEsVREA5D1tJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "a4cbcad6-531f-42f2-bd9e-132d9f66c626",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5dANhNkpiFS2v8Ltc6h6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 384,
      "cache_creation_input_tokens": 4485,
      "cache_read_input_tokens": 50459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4485
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-19T16:24:58.256Z_

<details><summary>↩ Tool result · `toolu_01TnXJeKrCYCrEsVREA5D1tJ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "59d262e9-bd8d-40b0-a886-21999a4a9435",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 83_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool has a whitelist and the report should go to the artifacts directory. Let me use the Write tool instead to write to the artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "5a15a327-e842-49e8-9db3-d8fa75b6133b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuxvCfyV6UVQR2j2XQi4fK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2031,
      "cache_read_input_tokens": 54944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2031
      },
      "output_tokens": 24,
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

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_018hnh2G1fbFofepjughjyQi`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "39ad2971-84e6-48b5-9fd1-cbbdbed4d94f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuxvCfyV6UVQR2j2XQi4fK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2031,
      "cache_read_input_tokens": 54944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2031
      },
      "output_tokens": 24,
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

_source line 85 · 2026-05-19T16:25:03.912Z_

<details><summary>↩ Tool result · `toolu_018hnh2G1fbFofepjughjyQi`</summary>

```text
_project
ablation_narrative_playbook.md
action_metrics_extended
action_probe_design.md
analyze_ablation_50demos.py
attention
attention_decomposition
attention_decomposition_and_r2.py
attention_normalization_entropy
attention_normalization_entropy.py
behavioral_pilot_w4_diagnosis.md
bootstrap_task_ratio.json
branch_split_rsa_results.md
citation_verification_2026.md
controlb_analysis
counterfactual_instruction.py
counterfactual_token_overlap
cross_inst_extract_phase2
cross_instruction
definitive_rsa_results.md
demo_sensitivity.py
demo_standardized_rsa.md
dinov2_baseline
dream_reports
extract_fused_backbone.py
fig2_cross_instruction_heatmap.pdf
fig_ood_diagnostics.png
fig_rsa_perlayer_curve.pdf
fig_rsa_perlayer_curve.png
figures
fulllayer_action_probe.py
groundtruth_action_error
l1_ablation_action_probe_50demos.py
layer_stability_analysis.md
libero_finetuned_attention
libero_finetuned_probe_profile.json
libero_goal_feasibility.md
literature_map.yaml
literature_map_probing.md
literature_survey_instruction_probing.md
llama2base_action_probe.py
manifest.yaml
matched_ablation_controls.py
matched_ablation_controls_diagnosis.md
mvp_controlb_trained
mvp_probe_trained
openvla_libero_goal_compat.md
paper_consistency_report.md
patch_probes.py
pca_linear_probe_gc.py
pca_linear_probe_perlayer.py
permutation_test_I2.py
pipeline_audit_libero_goal.md
plan_010_libero_spatial
plan_011_fulllayer_r2
plan_012_clip_vit_control
plot_dose_response.py
probe_design_plan.md
qa_probe_classification.py
random_subset_ablation.py
rebuttal_drafts.md
redream_evidence_v2.md
review_issues.yaml
review_reports
rsa_analysis.py
rsa_branch_split.py
rsa_definitive.py
rsa_method_audit_report.md
rsa_unified_vla.py
task_complexity_routing
task_routing_loo_sensitivity
unified_action_probe.py
unified_rsa_summary.md
untrained_last_preaction_probe.json
vla-ssd_final_2026-05-19.pdf
vla-ssd_round12_2026-05-19.pdf
vla_rsa_method_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "9a631c71-fb3b-49b9-b5ce-81e6bba799e9",
  "tool_use_result": {
    "stdout": "_project\nablation_narrative_playbook.md\naction_metrics_extended\naction_probe_design.md\nanalyze_ablation_50demos.py\nattention\nattention_decomposition\nattention_decomposition_and_r2.py\nattention_normalization_entropy\nattention_normalization_entropy.py\nbehavioral_pilot_w4_diagnosis.md\nbootstrap_task_ratio.json\nbranch_split_rsa_results.md\ncitation_verification_2026.md\ncontrolb_analysis\ncounterfactual_instruction.py\ncounterfactual_token_overlap\ncross_inst_extract_phase2\ncross_instruction\ndefinitive_rsa_results.md\ndemo_sensitivity.py\ndemo_standardized_rsa.md\ndinov2_baseline\ndream_reports\nextract_fused_backbone.py\nfig2_cross_instruction_heatmap.pdf\nfig_ood_diagnostics.png\nfig_rsa_perlayer_curve.pdf\nfig_rsa_perlayer_curve.png\nfigures\nfulllayer_action_probe.py\ngroundtruth_action_error\nl1_ablation_action_probe_50demos.py\nlayer_stability_analysis.md\nlibero_finetuned_attention\nlibero_finetuned_probe_profile.json\nlibero_goal_feasibility.md\nliterature_map.yaml\nliterature_map_probing.md\nliterature_survey_instruction_probing.md\nllama2base_action_probe.py\nmanifest.yaml\nmatched_ablation_controls.py\nmatched_ablation_controls_diagnosis.md\nmvp_controlb_trained\nmvp_probe_trained\nopenvla_libero_goal_compat.md\npaper_consistency_report.md\npatch_probes.py\npca_linear_probe_gc.py\npca_linear_probe_perlayer.py\npermutation_test_I2.py\npipeline_audit_libero_goal.md\nplan_010_libero_spatial\nplan_011_fulllayer_r2\nplan_012_clip_vit_control\nplot_dose_response.py\nprobe_design_plan.md\nqa_probe_classification.py\nrandom_subset_ablation.py\nrebuttal_drafts.md\nredream_evidence_v2.md\nreview_issues.yaml\nreview_reports\nrsa_analysis.py\nrsa_branch_split.py\nrsa_definitive.py\nrsa_method_audit_report.md\nrsa_unified_vla.py\ntask_complexity_routing\ntask_routing_loo_sensitivity\nunified_action_probe.py\nunified_rsa_summary.md\nuntrained_last_preaction_probe.json\nvla-ssd_final_2026-05-19.pdf\nvla-ssd_round12_2026-05-19.pdf\nvla_rsa_method_audit.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Write · `toolu_018XUk2oAjwm44aXgHU8rnKV`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/second_vla_survey.md",
  "content": "# 第二 VLA 模型调研报告\n\n**目的**: 寻找第二个 decoder-only VLA 模型，验证 L1 instruction routing 是否为 decoder-only VLA 的通用现象。\n\n**核心约束**: 必须是 decoder-only 架构（causal mask），必须有公开权重，backbone 最好与 OpenVLA (Llama-2-7B) 不同，排除 JAX 框架。\n\n---\n\n## 1. 候选列表总表\n\n| 模型 | 架构类型 | Backbone | 参数量 | 公开权重 | 训练数据 | 框架 | Action 编码方式 | 适配难度 |\n|------|---------|----------|--------|---------|---------|------|----------------|---------|\n| **OpenVLA-Phi3V** | decoder-only ✅ | Phi-3-Vision (4B) | ~4B | [HF](https://huggingface.co/furonghuang-lab/openvla_phi3v) | OXE 970K | PyTorch | 256-bin discrete (同 OpenVLA) | ⭐ 极低 |\n| **SpatialVLA** | decoder-only ✅ | PaLiGemma2 / Gemma 2 | ~4B | [HF](https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt) | OXE + RH20T 1.1M | PyTorch | Adaptive spatial action tokens | ⭐⭐ 低-中 |\n| **NORA** | decoder-only ✅ | Qwen-2.5-VL-3B | ~3B | [HF](https://huggingface.co/declare-lab/nora) | OXE 970K | PyTorch | FAST+ tokenizer (变长) | ⭐⭐⭐ 中 |\n| **TraceVLA-Phi3** | decoder-only ✅ | Phi-3-Vision (4B) | ~4B | [HF](https://huggingface.co/furonghuang-lab/tracevla_phi3v) | OXE 970K + trace | PyTorch | 256-bin discrete (同 OpenVLA) | ⭐ 极低 |\n| **NORA-1.5** | decoder-only ✅ | Qwen-2.5-VL-3B | ~3B | [HF](https://huggingface.co/declare-lab/nora-1.5) | OXE 970K + pref. | PyTorch | FAST+ tokenizer (变长) | ⭐⭐⭐ 中 |\n| **π₀ (openpi)** | cross-attn MoE ❌ | PaliGemma 3B + action expert | ~3B+ | [GitHub](https://github.com/Physical-Intelligence/openpi) | OXE + PI data | JAX→PyTorch | Flow matching (连续) | N/A (负对照) |\n| **SmolVLA** | VLM + cross-attn action expert ❌ | SmolLM2 + SigLIP | ~450M | [HF/LeRobot](https://huggingface.co/blog/smolvla) | LeRobot community | PyTorch | Cross-attn action expert | N/A (负对照) |\n| **GR00T-N1** | encoder-decoder + diffusion ❌ | SigLip2 + T5 + DiT | 2-3B | [HF](https://huggingface.co/nvidia/GR00T-N1-2B) | NVIDIA data | PyTorch | Diffusion transformer | N/A (架构不同) |\n| **CogACT** | decoder-only backbone + DiT action head | Llama-2-7B + DiT | ~7B+ | [HF](https://huggingface.co/CogACT/CogACT-Base) | OXE 400K | PyTorch | Diffusion (DiT action head) | 不适用 |\n| **DeeR-VLA** | cross-attn (OpenFlamingo) ❌ | OpenFlamingo 3B/9B | 3-9B | [HF](https://huggingface.co/Yang130/DeeR-VLA) | CALVIN | PyTorch | 连续 | 不适用 |\n| **Octo** | encoder + diffusion head ❌ | Transformer encoder | 93M | 开源 | OXE | JAX ❌ | Diffusion | 已排除 (JAX) |\n| **RT-2-X** | decoder-only | PaLM-E 55B | 55B | **无公开权重** ❌ | Google 内部 | JAX | 256-bin discrete | 不可用 |\n| **A1** | VLM + flow matching head | 未明确 (可能 InternVL) | 未知 | 代码开源，权重待确认 | DROID+AgiBot+OXE | PyTorch | Flow matching | 待确认 |\n\n---\n\n## 2. 排除理由汇总\n\n| 排除模型 | 排除原因 |\n|----------|---------|\n| **Octo** | JAX 框架 |\n| **RT-2-X** | 无公开权重，模型 55B 太大，JAX |\n| **GR00T-N1** | 非 decoder-only (encoder-decoder + diffusion)，action 不通过 LLM backbone |\n| **π₀** | 非 decoder-only (cross-attention MoE)，action expert 独立于 VLM backbone |\n| **SmolVLA** | 非 decoder-only (独立 action expert + cross-attention) |\n| **CogACT** | action 由独立 DiT 生成，不经过 LLM backbone；且 backbone 与 OpenVLA 相同 (Llama-2) |\n| **DeeR-VLA** | 基于 OpenFlamingo (cross-attention 架构)，非纯 decoder-only |\n| **ECoT** | 基于 OpenVLA (Llama-2 backbone)，backbone 与 OpenVLA 相同 |\n\n---\n\n## 3. Top-3 推荐（排序 + 理由）\n\n### 🥇 推荐 1: OpenVLA-Phi3V\n\n**理由**: 这是最理想的对比实验候选。与 OpenVLA-7B 使用完全相同的训练配方（相同数据 OXE 970K、相同 action tokenization 256-bin discrete、相同架构范式），唯一区别是 LLM backbone 从 Llama-2-7B 换成了 Phi-3-Vision (~4B)。这使得对比实验的变量控制最干净——如果 L1 instruction routing 同样出现在 Phi-3 backbone 中，可以强有力地论证这是 decoder-only VLA 的通用属性而非 Llama-2 的特异行为。\n\n| 属性 | 详情 |\n|------|------|\n| HuggingFace | `furonghuang-lab/openvla_phi3v` |\n| Backbone | Phi-3-Vision (decoder-only, ~4B params) |\n| Action tokens | 256-bin discrete（与 OpenVLA 完全相同） |\n| 训练数据 | OXE 970K（与 OpenVLA 相同） |\n| GPU 需求 | ~10GB (FP16)，单卡即可 |\n| 适配工作量 | **极低** — 与 OpenVLA 使用相同 codebase，attention extraction 代码可直接复用，仅需调整模型加载路径 |\n\n**下载命令**:\n```bash\n# 下载模型\npip install huggingface_hub\nhuggingface-cli download furonghuang-lab/openvla_phi3v --local-dir /root/autodl-tmp/models/openvla-phi3v\n\n# 或在代码中\nfrom transformers import AutoModelForCausalLM, AutoProcessor\nmodel = AutoModelForCausalLM.from_pretrained(\"furonghuang-lab/openvla_phi3v\", torch_dtype=torch.bfloat16)\n```\n\n**预计适配步骤**:\n1. 下载模型权重 (~8GB)\n2. 修改现有 attention extraction 代码，适配 Phi-3 的 attention 层命名 (Phi-3 用 `model.layers[i].self_attn` 而非 Llama 的命名)\n3. 确认 vision/language/action token 边界在 Phi-3 中的定位方式\n4. 运行 attention extraction + probe 分析\n5. **预计时间: 2-3 天**\n\n**风险**: \n- Phi-3-Vision 的注意力头数/层数与 Llama-2 不同，需确认 L1 定义（Layer 1 of decoder）在 Phi-3 中的对应位置\n- OpenVLA-Phi3V 由 TraceVLA 团队（非 OpenVLA 官方）训练，训练超参可能有微小差异\n\n---\n\n### 🥈 推荐 2: SpatialVLA\n\n**理由**: 完全独立的团队和框架，backbone 是 Gemma 2（通过 PaLiGemma2），与 Llama-2 差异更大。使用 autoregressive next-token prediction 训练，action tokens 通过 Gemma 2 decoder 的 causal attention 处理。如果 L1 routing 同样出现在 Gemma 2 backbone 中，说明这个现象跨越了 Llama 和 Gemma 两个完全不同的 LLM 家族。\n\n| 属性 | 详情 |\n|------|------|\n| HuggingFace | `IPEC-COMMUNITY/spatialvla-4b-224-pt` |\n| Backbone | PaLiGemma2 = SigLIP (vision) + Gemma 2 (decoder-only LLM, ~2B decoder params) |\n| Action tokens | Adaptive spatial action tokens (离散，autoregressive 预测) |\n| 训练数据 | OXE + RH20T, 1.1M episodes |\n| GPU 需求 | ~8.5GB (inference) |\n| 适配工作量 | **低-中** — 需要理解 spatial action token 的 tokenization 方案，attention extraction 需要适配 PaLiGemma2 的架构 |\n\n**下载命令**:\n```bash\nhuggingface-cli download IPEC-COMMUNITY/spatialvla-4b-224-pt --local-dir /root/autodl-tmp/models/spatialvla-4b\n\n# 代码示例\ngit clone https://github.com/SpatialVLA/SpatialVLA.git\n```\n\n**预计适配步骤**:\n1. 下载模型 + clone SpatialVLA repo\n2. 研究 PaLiGemma2 的 attention 层结构（Gemma 2 decoder layers）\n3. 确定 vision tokens / language tokens / action tokens 在 input sequence 中的边界\n4. 理解 adaptive action grid tokenization（与 OpenVLA 的 256-bin 不同）\n5. 适配 attention extraction 代码\n6. 运行分析\n7. **预计时间: 4-5 天**\n\n**风险**:\n- Action tokenization 方案不同于 OpenVLA（spatial action tokens vs 256-bin），attention pattern 的对比需要 normalize\n- PaLiGemma2 的 vision token 处理方式不同（SigLIP tokens 直接投射到 Gemma 2 input space）\n- 相对 OpenVLA-Phi3V，变量控制更松（同时改变了 backbone 和 action tokenization）\n\n---\n\n### 🥉 推荐 3: NORA\n\n**理由**: backbone 是 Qwen-2.5-VL (又一个不同的 LLM 家族)，模型最小 (3B)，实验速度最快。Qwen-2.5-VL 与 Llama-2 和 Gemma 2 都不同，增加 generalizability 覆盖面。\n\n| 属性 | 详情 |\n|------|------|\n| HuggingFace | `declare-lab/nora` |\n| Backbone | Qwen-2.5-VL-3B (decoder-only) |\n| Action tokens | FAST+ tokenizer（变长离散 token，基于 DCT + BPE） |\n| 训练数据 | OXE 970K |\n| GPU 需求 | ~7GB (inference) |\n| 适配工作量 | **中** — FAST+ tokenizer 产生变长 token，action token 边界识别复杂；Qwen-2.5-VL 使用动态分辨率（vision token 数量可变） |\n\n**下载命令**:\n```bash\nhuggingface-cli download declare-lab/nora --local-dir /root/autodl-tmp/models/nora\n\ngit clone https://github.com/declare-lab/nora.git\n```\n\n**预计适配步骤**:\n1. 下载模型 + clone nora repo\n2. 研究 Qwen-2.5-VL 的 attention 层结构\n3. 理解 FAST+ tokenizer 的 action token 编码方式（变长 token）\n4. 处理 Qwen-2.5-VL 的动态分辨率 vision token 问题\n5. 适配 attention extraction + probe 代码\n6. 运行分析\n7. **预计时间: 5-7 天**\n\n**风险**:\n- FAST+ tokenizer 产生变长 action tokens，与 OpenVLA 的固定 7-dim 256-bin tokens 差异大，attention pattern 对比困难\n- Qwen-2.5-VL 使用 dynamic resolution (vision token 数不固定)，token position 分析复杂\n- 模型较新 (2025-04)，社区使用经验少\n\n---\n\n## 4. 推荐策略\n\n### 首选方案：OpenVLA-Phi3V（快速出结果）\n- **优势**: 最小适配工作量，变量控制最干净，2-3 天可出结果\n- **论文叙事**: \"We replicate our analysis on OpenVLA-Phi3V, which uses an identical training recipe but replaces Llama-2 with Phi-3-Vision as the LLM backbone. The L1 instruction routing pattern persists across different LLM architectures.\"\n- **潜在 reviewer 反驳**: \"Phi-3 和 Llama-2 都是同类 decoder-only LLM，能否证明在更不同的架构上也成立？\"\n\n### 加强方案：OpenVLA-Phi3V + SpatialVLA（双重验证）\n- **优势**: 覆盖 Llama-2 + Phi-3 + Gemma 2 三个 LLM 家族，一个同配方不同 backbone，一个完全独立的模型\n- **论文叙事**: \"The L1 routing phenomenon generalizes across three distinct LLM backbones (Llama-2, Phi-3, Gemma-2) and two independent VLA training frameworks (OpenVLA, SpatialVLA).\"\n\n### 负对照（可选）：π₀\n- 用 openpi (PyTorch port via LeRobot) 做负对照\n- 预测：cross-attention MoE 架构不应出现 L1 instruction routing pattern\n- 若负对照成立，进一步证明 L1 routing 是 decoder-only 架构的特异性质\n\n---\n\n## 5. 详细架构对比\n\n```\nOpenVLA-7B:           [SigLIP+DINOv2] → Projector → [Llama-2-7B Decoder] → action tokens (256-bin)\n                                                      ↑ causal attention over all tokens\n\nOpenVLA-Phi3V:        [Phi-3-Vision Encoder] → Projector → [Phi-3 Decoder ~4B] → action tokens (256-bin)\n                                                             ↑ causal attention over all tokens\n\nSpatialVLA:           [SigLIP + Ego3D PE] → Projector → [Gemma-2 Decoder ~2B] → spatial action tokens\n                                                          ↑ causal attention over all tokens\n\nNORA:                 [Qwen-2.5-VL Vision] → Projector → [Qwen-2.5 Decoder ~3B] → FAST+ action tokens\n                                                           ↑ causal attention over all tokens\n\nπ₀ (负对照):          [PaliGemma VLM 3B] ──cross-attn──→ [Action Expert] → flow matching actions\n                       ↑ VLM 和 action expert 是分离的，不共享 causal attention\n```\n\n关键共性：前四个模型都将 vision + language + action tokens 送入同一个 decoder-only LLM，用 causal attention 处理。π₀ 的 action expert 是独立的，通过 cross-attention 与 VLM 交互。\n\n---\n\n## 6. 风险总评\n\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| OpenVLA-Phi3V 非官方训练，可能有 subtle 差异 | 低 | 先验证其在 SimplerEnv 上的 baseline 性能是否合理 |\n| SpatialVLA action tokenization 与 OpenVLA 不同 | 中 | 分析时关注 instruction→vision attention 而非 instruction→action，减少 tokenization 差异影响 |\n| NORA FAST+ 变长 token 难以定位 action boundary | 中-高 | 先尝试 OpenVLA-Phi3V 和 SpatialVLA，NORA 作为备选 |\n| 所有候选训练数据高度重叠 (OXE) | 低 | 这实际上是优势——控制了训练数据变量 |\n| Phi-3 层数/头数不同，L1 对应关系需要重新定义 | 低 | 定义为 \"第一个 decoder layer\" 而非绝对层号 |\n\n---\n\n*调研日期: 2026-05-19*\n*搜索覆盖: arXiv 2024-2026, HuggingFace, GitHub, 主要 VLA 综述*\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "b1c7af6e-a671-44ca-91f1-c07be67e88ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQgGJ63TnUaXLBnqbs8Bfy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 56975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 878
      },
      "output_tokens": 63,
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

_source line 87 · 2026-05-19T16:26:32.053Z_

<details><summary>↩ Tool result · `toolu_018XUk2oAjwm44aXgHU8rnKV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/second_vla_survey.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "5558578a-d98e-4025-9bbe-acb73ebd96f6",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/second_vla_survey.md",
    "content": "# 第二 VLA 模型调研报告\n\n**目的**: 寻找第二个 decoder-only VLA 模型，验证 L1 instruction routing 是否为 decoder-only VLA 的通用现象。\n\n**核心约束**: 必须是 decoder-only 架构（causal mask），必须有公开权重，backbone 最好与 OpenVLA (Llama-2-7B) 不同，排除 JAX 框架。\n\n---\n\n## 1. 候选列表总表\n\n| 模型 | 架构类型 | Backbone | 参数量 | 公开权重 | 训练数据 | 框架 | Action 编码方式 | 适配难度 |\n|------|---------|----------|--------|---------|---------|------|----------------|---------|\n| **OpenVLA-Phi3V** | decoder-only ✅ | Phi-3-Vision (4B) | ~4B | [HF](https://huggingface.co/furonghuang-lab/openvla_phi3v) | OXE 970K | PyTorch | 256-bin discrete (同 OpenVLA) | ⭐ 极低 |\n| **SpatialVLA** | decoder-only ✅ | PaLiGemma2 / Gemma 2 | ~4B | [HF](https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt) | OXE + RH20T 1.1M | PyTorch | Adaptive spatial action tokens | ⭐⭐ 低-中 |\n| **NORA** | decoder-only ✅ | Qwen-2.5-VL-3B | ~3B | [HF](https://huggingface.co/declare-lab/nora) | OXE 970K | PyTorch | FAST+ tokenizer (变长) | ⭐⭐⭐ 中 |\n| **TraceVLA-Phi3** | decoder-only ✅ | Phi-3-Vision (4B) | ~4B | [HF](https://huggingface.co/furonghuang-lab/tracevla_phi3v) | OXE 970K + trace | PyTorch | 256-bin discrete (同 OpenVLA) | ⭐ 极低 |\n| **NORA-1.5** | decoder-only ✅ | Qwen-2.5-VL-3B | ~3B | [HF](https://huggingface.co/declare-lab/nora-1.5) | OXE 970K + pref. | PyTorch | FAST+ tokenizer (变长) | ⭐⭐⭐ 中 |\n| **π₀ (openpi)** | cross-attn MoE ❌ | PaliGemma 3B + action expert | ~3B+ | [GitHub](https://github.com/Physical-Intelligence/openpi) | OXE + PI data | JAX→PyTorch | Flow matching (连续) | N/A (负对照) |\n| **SmolVLA** | VLM + cross-attn action expert ❌ | SmolLM2 + SigLIP | ~450M | [HF/LeRobot](https://huggingface.co/blog/smolvla) | LeRobot community | PyTorch | Cross-attn action expert | N/A (负对照) |\n| **GR00T-N1** | encoder-decoder + diffusion ❌ | SigLip2 + T5 + DiT | 2-3B | [HF](https://huggingface.co/nvidia/GR00T-N1-2B) | NVIDIA data | PyTorch | Diffusion transformer | N/A (架构不同) |\n| **CogACT** | decoder-only backbone + DiT action head | Llama-2-7B + DiT | ~7B+ | [HF](https://huggingface.co/CogACT/CogACT-Base) | OXE 400K | PyTorch | Diffusion (DiT action head) | 不适用 |\n| **DeeR-VLA** | cross-attn (OpenFlamingo) ❌ | OpenFlamingo 3B/9B | 3-9B | [HF](https://huggingface.co/Yang130/DeeR-VLA) | CALVIN | PyTorch | 连续 | 不适用 |\n| **Octo** | encoder + diffusion head ❌ | Transformer encoder | 93M | 开源 | OXE | JAX ❌ | Diffusion | 已排除 (JAX) |\n| **RT-2-X** | decoder-only | PaLM-E 55B | 55B | **无公开权重** ❌ | Google 内部 | JAX | 256-bin discrete | 不可用 |\n| **A1** | VLM + flow matching head | 未明确 (可能 InternVL) | 未知 | 代码开源，权重待确认 | DROID+AgiBot+OXE | PyTorch | Flow matching | 待确认 |\n\n---\n\n## 2. 排除理由汇总\n\n| 排除模型 | 排除原因 |\n|----------|---------|\n| **Octo** | JAX 框架 |\n| **RT-2-X** | 无公开权重，模型 55B 太大，JAX |\n| **GR00T-N1** | 非 decoder-only (encoder-decoder + diffusion)，action 不通过 LLM backbone |\n| **π₀** | 非 decoder-only (cross-attention MoE)，action expert 独立于 VLM backbone |\n| **SmolVLA** | 非 decoder-only (独立 action expert + cross-attention) |\n| **CogACT** | action 由独立 DiT 生成，不经过 LLM backbone；且 backbone 与 OpenVLA 相同 (Llama-2) |\n| **DeeR-VLA** | 基于 OpenFlamingo (cross-attention 架构)，非纯 decoder-only |\n| **ECoT** | 基于 OpenVLA (Llama-2 backbone)，backbone 与 OpenVLA 相同 |\n\n---\n\n## 3. Top-3 推荐（排序 + 理由）\n\n### 🥇 推荐 1: OpenVLA-Phi3V\n\n**理由**: 这是最理想的对比实验候选。与 OpenVLA-7B 使用完全相同的训练配方（相同数据 OXE 970K、相同 action tokenization 256-bin discrete、相同架构范式），唯一区别是 LLM backbone 从 Llama-2-7B 换成了 Phi-3-Vision (~4B)。这使得对比实验的变量控制最干净——如果 L1 instruction routing 同样出现在 Phi-3 backbone 中，可以强有力地论证这是 decoder-only VLA 的通用属性而非 Llama-2 的特异行为。\n\n| 属性 | 详情 |\n|------|------|\n| HuggingFace | `furonghuang-lab/openvla_phi3v` |\n| Backbone | Phi-3-Vision (decoder-only, ~4B params) |\n| Action tokens | 256-bin discrete（与 OpenVLA 完全相同） |\n| 训练数据 | OXE 970K（与 OpenVLA 相同） |\n| GPU 需求 | ~10GB (FP16)，单卡即可 |\n| 适配工作量 | **极低** — 与 OpenVLA 使用相同 codebase，attention extraction 代码可直接复用，仅需调整模型加载路径 |\n\n**下载命令**:\n```bash\n# 下载模型\npip install huggingface_hub\nhuggingface-cli download furonghuang-lab/openvla_phi3v --local-dir /root/autodl-tmp/models/openvla-phi3v\n\n# 或在代码中\nfrom transformers import AutoModelForCausalLM, AutoProcessor\nmodel = AutoModelForCausalLM.from_pretrained(\"furonghuang-lab/openvla_phi3v\", torch_dtype=torch.bfloat16)\n```\n\n**预计适配步骤**:\n1. 下载模型权重 (~8GB)\n2. 修改现有 attention extraction 代码，适配 Phi-3 的 attention 层命名 (Phi-3 用 `model.layers[i].self_attn` 而非 Llama 的命名)\n3. 确认 vision/language/action token 边界在 Phi-3 中的定位方式\n4. 运行 attention extraction + probe 分析\n5. **预计时间: 2-3 天**\n\n**风险**: \n- Phi-3-Vision 的注意力头数/层数与 Llama-2 不同，需确认 L1 定义（Layer 1 of decoder）在 Phi-3 中的对应位置\n- OpenVLA-Phi3V 由 TraceVLA 团队（非 OpenVLA 官方）训练，训练超参可能有微小差异\n\n---\n\n### 🥈 推荐 2: SpatialVLA\n\n**理由**: 完全独立的团队和框架，backbone 是 Gemma 2（通过 PaLiGemma2），与 Llama-2 差异更大。使用 autoregressive next-token prediction 训练，action tokens 通过 Gemma 2 decoder 的 causal attention 处理。如果 L1 routing 同样出现在 Gemma 2 backbone 中，说明这个现象跨越了 Llama 和 Gemma 两个完全不同的 LLM 家族。\n\n| 属性 | 详情 |\n|------|------|\n| HuggingFace | `IPEC-COMMUNITY/spatialvla-4b-224-pt` |\n| Backbone | PaLiGemma2 = SigLIP (vision) + Gemma 2 (decoder-only LLM, ~2B decoder params) |\n| Action tokens | Adaptive spatial action tokens (离散，autoregressive 预测) |\n| 训练数据 | OXE + RH20T, 1.1M episodes |\n| GPU 需求 | ~8.5GB (inference) |\n| 适配工作量 | **低-中** — 需要理解 spatial action token 的 tokenization 方案，attention extraction 需要适配 PaLiGemma2 的架构 |\n\n**下载命令**:\n```bash\nhuggingface-cli download IPEC-COMMUNITY/spatialvla-4b-224-pt --local-dir /root/autodl-tmp/models/spatialvla-4b\n\n# 代码示例\ngit clone https://github.com/SpatialVLA/SpatialVLA.git\n```\n\n**预计适配步骤**:\n1. 下载模型 + clone SpatialVLA repo\n2. 研究 PaLiGemma2 的 attention 层结构（Gemma 2 decoder layers）\n3. 确定 vision tokens / language tokens / action tokens 在 input sequence 中的边界\n4. 理解 adaptive action grid tokenization（与 OpenVLA 的 256-bin 不同）\n5. 适配 attention extraction 代码\n6. 运行分析\n7. **预计时间: 4-5 天**\n\n**风险**:\n- Action tokenization 方案不同于 OpenVLA（spatial action tokens vs 256-bin），attention pattern 的对比需要 normalize\n- PaLiGemma2 的 vision token 处理方式不同（SigLIP tokens 直接投射到 Gemma 2 input space）\n- 相对 OpenVLA-Phi3V，变量控制更松（同时改变了 backbone 和 action tokenization）\n\n---\n\n### 🥉 推荐 3: NORA\n\n**理由**: backbone 是 Qwen-2.5-VL (又一个不同的 LLM 家族)，模型最小 (3B)，实验速度最快。Qwen-2.5-VL 与 Llama-2 和 Gemma 2 都不同，增加 generalizability 覆盖面。\n\n| 属性 | 详情 |\n|------|------|\n| HuggingFace | `declare-lab/nora` |\n| Backbone | Qwen-2.5-VL-3B (decoder-only) |\n| Action tokens | FAST+ tokenizer（变长离散 token，基于 DCT + BPE） |\n| 训练数据 | OXE 970K |\n| GPU 需求 | ~7GB (inference) |\n| 适配工作量 | **中** — FAST+ tokenizer 产生变长 token，action token 边界识别复杂；Qwen-2.5-VL 使用动态分辨率（vision token 数量可变） |\n\n**下载命令**:\n```bash\nhuggingface-cli download declare-lab/nora --local-dir /root/autodl-tmp/models/nora\n\ngit clone https://github.com/declare-lab/nora.git\n```\n\n**预计适配步骤**:\n1. 下载模型 + clone nora repo\n2. 研究 Qwen-2.5-VL 的 attention 层结构\n3. 理解 FAST+ tokenizer 的 action token 编码方式（变长 token）\n4. 处理 Qwen-2.5-VL 的动态分辨率 vision token 问题\n5. 适配 attention extraction + probe 代码\n6. 运行分析\n7. **预计时间: 5-7 天**\n\n**风险**:\n- FAST+ tokenizer 产生变长 action tokens，与 OpenVLA 的固定 7-dim 256-bin tokens 差异大，attention pattern 对比困难\n- Qwen-2.5-VL 使用 dynamic resolution (vision token 数不固定)，token position 分析复杂\n- 模型较新 (2025-04)，社区使用经验少\n\n---\n\n## 4. 推荐策略\n\n### 首选方案：OpenVLA-Phi3V（快速出结果）\n- **优势**: 最小适配工作量，变量控制最干净，2-3 天可出结果\n- **论文叙事**: \"We replicate our analysis on OpenVLA-Phi3V, which uses an identical training recipe but replaces Llama-2 with Phi-3-Vision as the LLM backbone. The L1 instruction routing pattern persists across different LLM architectures.\"\n- **潜在 reviewer 反驳**: \"Phi-3 和 Llama-2 都是同类 decoder-only LLM，能否证明在更不同的架构上也成立？\"\n\n### 加强方案：OpenVLA-Phi3V + SpatialVLA（双重验证）\n- **优势**: 覆盖 Llama-2 + Phi-3 + Gemma 2 三个 LLM 家族，一个同配方不同 backbone，一个完全独立的模型\n- **论文叙事**: \"The L1 routing phenomenon generalizes across three distinct LLM backbones (Llama-2, Phi-3, Gemma-2) and two independent VLA training frameworks (OpenVLA, SpatialVLA).\"\n\n### 负对照（可选）：π₀\n- 用 openpi (PyTorch port via LeRobot) 做负对照\n- 预测：cross-attention MoE 架构不应出现 L1 instruction routing pattern\n- 若负对照成立，进一步证明 L1 routing 是 decoder-only 架构的特异性质\n\n---\n\n## 5. 详细架构对比\n\n```\nOpenVLA-7B:           [SigLIP+DINOv2] → Projector → [Llama-2-7B Decoder] → action tokens (256-bin)\n                                                      ↑ causal attention over all tokens\n\nOpenVLA-Phi3V:        [Phi-3-Vision Encoder] → Projector → [Phi-3 Decoder ~4B] → action tokens (256-bin)\n                                                             ↑ causal attention over all tokens\n\nSpatialVLA:           [SigLIP + Ego3D PE] → Projector → [Gemma-2 Decoder ~2B] → spatial action tokens\n                                                          ↑ causal attention over all tokens\n\nNORA:                 [Qwen-2.5-VL Vision] → Projector → [Qwen-2.5 Decoder ~3B] → FAST+ action tokens\n                                                           ↑ causal attention over all tokens\n\nπ₀ (负对照):          [PaliGemma VLM 3B] ──cross-attn──→ [Action Expert] → flow matching actions\n                       ↑ VLM 和 action expert 是分离的，不共享 causal attention\n```\n\n关键共性：前四个模型都将 vision + language + action tokens 送入同一个 decoder-only LLM，用 causal attention 处理。π₀ 的 action expert 是独立的，通过 cross-attention 与 VLM 交互。\n\n---\n\n## 6. 风险总评\n\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| OpenVLA-Phi3V 非官方训练，可能有 subtle 差异 | 低 | 先验证其在 SimplerEnv 上的 baseline 性能是否合理 |\n| SpatialVLA action tokenization 与 OpenVLA 不同 | 中 | 分析时关注 instruction→vision attention 而非 instruction→action，减少 tokenization 差异影响 |\n| NORA FAST+ 变长 token 难以定位 action boundary | 中-高 | 先尝试 OpenVLA-Phi3V 和 SpatialVLA，NORA 作为备选 |\n| 所有候选训练数据高度重叠 (OXE) | 低 | 这实际上是优势——控制了训练数据变量 |\n| Phi-3 层数/头数不同，L1 对应关系需要重新定义 | 低 | 定义为 \"第一个 decoder layer\" 而非绝对层号 |\n\n---\n\n*调研日期: 2026-05-19*\n*搜索覆盖: arXiv 2024-2026, HuggingFace, GitHub, 主要 VLA 综述*\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 88_

调研报告已写入 `artifacts/second_vla_survey.md`。

**核心结论**:

**Top-1: OpenVLA-Phi3V** (`furonghuang-lab/openvla_phi3v`) — Phi-3-Vision backbone, 与 OpenVLA 使用完全相同的训练配方和 256-bin action tokenization，唯一变量是 backbone 从 Llama-2 换成 Phi-3。适配工作量极低（~2-3 天），变量控制最干净。

**Top-2: SpatialVLA** (`IPEC-COMMUNITY/spatialvla-4b-224-pt`) — PaLiGemma2/Gemma-2 backbone，完全独立的团队和框架，autoregressive discrete action tokens。覆盖第三个 LLM 家族。适配 ~4-5 天。

**Top-3: NORA** (`declare-lab/nora`) — Qwen-2.5-VL-3B backbone，3B 最小最快，但 FAST+ 变长 tokenizer 增加分析难度。

**推荐策略**: 先做 OpenVLA-Phi3V（快速出结果，控制变量最干净），若 reviewer 仍嫌不够，再加 SpatialVLA（覆盖 Llama-2 / Phi-3 / Gemma-2 三个 LLM 家族）。可选用 π₀ 做负对照（cross-attention 架构，预测不会出现 L1 routing）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "uuid": "5ee8eddf-8e0a-4d39-8b65-65446114df44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WL63qV6goEsEfPidpbQCQD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5221,
      "cache_read_input_tokens": 57853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5221
      },
      "output_tokens": 1,
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

_source line 89_

调研报告已写入 `artifacts/second_vla_survey.md`。

**核心结论**:

**Top-1: OpenVLA-Phi3V** (`furonghuang-lab/openvla_phi3v`) — Phi-3-Vision backbone, 与 OpenVLA 使用完全相同的训练配方和 256-bin action tokenization，唯一变量是 backbone 从 Llama-2 换成 Phi-3。适配工作量极低（~2-3 天），变量控制最干净。

**Top-2: SpatialVLA** (`IPEC-COMMUNITY/spatialvla-4b-224-pt`) — PaLiGemma2/Gemma-2 backbone，完全独立的团队和框架，autoregressive discrete action tokens。覆盖第三个 LLM 家族。适配 ~4-5 天。

**Top-3: NORA** (`declare-lab/nora`) — Qwen-2.5-VL-3B backbone，3B 最小最快，但 FAST+ 变长 tokenizer 增加分析难度。

**推荐策略**: 先做 OpenVLA-Phi3V（快速出结果，控制变量最干净），若 reviewer 仍嫌不够，再加 SpatialVLA（覆盖 Llama-2 / Phi-3 / Gemma-2 三个 LLM 家族）。可选用 π₀ 做负对照（cross-attention 架构，预测不会出现 L1 routing）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 315157,
  "duration_api_ms": 483535,
  "num_turns": 35,
  "stop_reason": "end_turn",
  "session_id": "b517f969-aea8-416a-a27b-0f89ebf07854",
  "total_cost_usd": 1.6251137499999997,
  "usage": {
    "input_tokens": 4063,
    "cache_creation_input_tokens": 51233,
    "cache_read_input_tokens": 468457,
    "output_tokens": 13055,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 51233,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 426,
        "cache_read_input_tokens": 57853,
        "cache_creation_input_tokens": 5221,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5221
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 341034,
      "outputTokens": 14591,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 31,
      "costUSD": 0.723989,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4063,
      "outputTokens": 13055,
      "cacheReadInputTokens": 468457,
      "cacheCreationInputTokens": 51233,
      "webSearchRequests": 0,
      "costUSD": 0.9011247499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "34b9cf14-bb10-44ad-915c-ea2e9911f40a"
}
```

</details>

---
