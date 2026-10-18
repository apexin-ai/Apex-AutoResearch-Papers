# paper research lit vla models

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_research_lit_vla_models_20260517T120905.log`
- **Structured JSON:** [`27ee4822d07e61457099.json`](../../sessions/27/27ee4822d07e61457099.json)

## Before a recorded user message

19 recorded events

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
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "5a8256fa-f4b6-4f98-897c-9943b7c3b754",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779030600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "947ff0a2-e31c-4716-bbf8-fcb1cf1bd5f2",
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d"
}
```

---

### Assistant

_source line 4_

I'll search for VLA model papers and build the literature map. Let me start by searching for the must-cite papers and additional VLA papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "c98c3f2b-2edf-4f2d-bbb2-da7876583b8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnQArTymw58PTCCwXJhYEL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13194,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13194
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01F773NfY9toC28DXNj7uDy8`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "dabad91a-9cce-46e7-8132-d07e41210373",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnQArTymw58PTCCwXJhYEL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13194,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13194
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-17T12:09:16.384Z_

<details><summary>↩ Tool result · `toolu_01F773NfY9toC28DXNj7uDy8`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "f2ad690b-7329-4603-a4ee-22a40097e5a9",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 50
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the VLA papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "17ffe1ee-5f95-4c96-b1e1-9face9fa8bc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhzwZDiMsH8EWd1M5oWUY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 25035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011xCvJVRUDw47V6v6X9q3f7`</summary>

```json
{
  "query": "SmolVLA Rouatbi 2025 arXiv vision language action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "b9e07c8b-ed99-432b-98a9-e3c5985a7a05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhzwZDiMsH8EWd1M5oWUY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 25035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HgC1BnEKCAbSNJMVYHpUve`</summary>

```json
{
  "query": "OpenVLA Kim 2024 arXiv vision language action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "96e8e615-3d49-45f1-9fc7-ca1ecbd808e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhzwZDiMsH8EWd1M5oWUY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 25035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NGJuZRDL5uo88HJgyJfNhn`</summary>

```json
{
  "query": "RT-2 Brohan 2023 vision language action model robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "1768f9c5-37bc-4186-ac47-653d5006defc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhzwZDiMsH8EWd1M5oWUY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 25035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_016RGLEdjkdkMvRJcNtPus6C`</summary>

```json
{
  "query": "Octo Team 2024 robot policy arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "fcfddfc7-a5a5-4dc7-b2ac-3b8157dc7a68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhzwZDiMsH8EWd1M5oWUY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 25035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AJjgPN7HQrEeatBWMcWupE`</summary>

```json
{
  "query": "pi0 Physical Intelligence 2024 vision language action robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "15c1c2a0-76cf-4a26-9777-ec789e243c17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhzwZDiMsH8EWd1M5oWUY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 25035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X4YdjQQHzwH5mS7ZbPGAjr`</summary>

```json
{
  "query": "vision language action model robot 2024 2025 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "fca0a7f5-6fdc-497f-ad83-7ce7333d530c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhzwZDiMsH8EWd1M5oWUY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 25035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
      },
      "output_tokens": 19,
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

_source line 14 · 2026-05-17T12:09:25.028Z_

<details><summary>↩ Tool result · `toolu_011xCvJVRUDw47V6v6X9q3f7`</summary>

```text
Web search results for query: "SmolVLA Rouatbi 2025 arXiv vision language action model"

Links: [{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":"NanoVLA: Routing Decoupled Vision-Language Understanding for Nano-sized Generalist Robotic Policies","url":"https://arxiv.org/html/2510.25122v1"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250601844S/abstract"}]

Based on the search results, here's information about SmolVLA:

## Overview

SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. The paper was published on arXiv on June 2, 2025 (arXiv:2506.01844).

## Key Features

SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. SmolVLA has less than 0.5 billion parameters, allowing for fast inference on consumer-grade hardware.

Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger.

## Architecture

SmolVLA is composed of two main components: (i) a pretrained VLM tasked with perception and (ii) an action expert, trained to act. SmolVLA uses SmolVLM-2, an efficient model optimized for multi-image and video inputs.

## Technical Innovation

To further improve responsiveness, SmolVLA introduces an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation.

## Evaluation and Release

The authors evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "88086830-4668-4228-9b96-d6c3ed9b17f9",
  "tool_use_result": {
    "query": "SmolVLA Rouatbi 2025 arXiv vision language action model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RosU7qLVb3r5hs3mDh8XAn",
        "content": [
          {
            "title": "arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model",
            "url": "https://arxiv.org/pdf/2506.01844"
          },
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://arxiv.org/abs/2506.01844"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "http://export.arxiv.org/abs/2506.01844"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.06951v1"
          },
          {
            "title": "NanoVLA: Routing Decoupled Vision-Language Understanding for Nano-sized Generalist Robotic Policies",
            "url": "https://arxiv.org/html/2510.25122v1"
          },
          {
            "title": "[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"
          },
          {
            "title": "Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://huggingface.co/papers/2506.01844"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250601844S/abstract"
          }
        ]
      },
      "Based on the search results, here's information about SmolVLA:\n\n## Overview\n\nSmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. The paper was published on arXiv on June 2, 2025 (arXiv:2506.01844).\n\n## Key Features\n\nSmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. SmolVLA has less than 0.5 billion parameters, allowing for fast inference on consumer-grade hardware.\n\nDespite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger.\n\n## Architecture\n\nSmolVLA is composed of two main components: (i) a pretrained VLM tasked with perception and (ii) an action expert, trained to act. SmolVLA uses SmolVLM-2, an efficient model optimized for multi-image and video inputs.\n\n## Technical Innovation\n\nTo further improve responsiveness, SmolVLA introduces an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation.\n\n## Evaluation and Release\n\nThe authors evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data."
    ],
    "durationSeconds": 5.249293532000001
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T12:09:26.270Z_

<details><summary>↩ Tool result · `toolu_01NGJuZRDL5uo88HJgyJfNhn`</summary>

```text
Web search results for query: "RT-2 Brohan 2023 vision language action model robotics"

Links: [{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"RT-2: New model translates vision and language into action — Google DeepMind","url":"https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | by Faryal Saud | Medium","url":"https://medium.com/@faryal.saud/rt-2-vision-language-action-models-transfer-web-knowledge-to-robotic-control-8cffbd038781"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"},{"title":"Vision-Language-Action Models Transfer Web Knowledge ...","url":"https://robotics-transformer2.github.io/assets/rt2.pdf"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"}]

I found comprehensive search results about RT-2, the vision-language-action model. Here's what I found:

## Overview

RT-2 is a novel vision-language-action (VLA) model that learns from both web and robotics data, and translates this knowledge into generalised instructions for robotic control.

## Core Innovation

To make RT-2 easily compatible with large, pre-trained vision-language models, robot actions are represented as another language, which can be cast into text tokens and trained together with Internet-scale vision-language datasets. The approach proposes to co-fine-tune state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering.

## Key Capabilities

RT-2 demonstrates significantly improved generalization to novel objects, the ability to interpret commands not present in the robot training data (such as placing an object onto a particular number or icon), and the ability to perform rudimentary reasoning in response to user commands (such as picking up the smallest or largest object, or the one closest to another object). 

Incorporating chain of thought reasoning allows RT-2 to perform multi-stage semantic reasoning, for example figuring out which object to pick up for use as an improvised hammer (a rock), or which type of drink is best suited for someone who is too sleepy.

## Authors and Publication

The work was authored by Anthony Brohan and 53 other co-authors from DeepMind. The paper was published in the Proceedings of The 7th Conference on Robot Learning (2023).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "298510d9-f0be-40cf-845a-e7c8fdb5898a",
  "tool_use_result": {
    "query": "RT-2 Brohan 2023 vision language action model robotics",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DEU31k8v2obV5uinKskzqd",
        "content": [
          {
            "title": "RT-2: Vision-Language-Action Models",
            "url": "https://robotics-transformer2.github.io/"
          },
          {
            "title": "[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
            "url": "https://arxiv.org/abs/2307.15818"
          },
          {
            "title": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
            "url": "https://proceedings.mlr.press/v229/zitkovich23a.html"
          },
          {
            "title": "RT-2: New model translates vision and language into action — Google DeepMind",
            "url": "https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/"
          },
          {
            "title": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | by Faryal Saud | Medium",
            "url": "https://medium.com/@faryal.saud/rt-2-vision-language-action-models-transfer-web-knowledge-to-robotic-control-8cffbd038781"
          },
          {
            "title": "(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
            "url": "https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"
          },
          {
            "title": "RT-2: Vision-Language-Action Models Transfer Web ...",
            "url": "https://arxiv.org/pdf/2307.15818"
          },
          {
            "title": "Vision-Language-Action Models Transfer Web Knowledge ...",
            "url": "https://robotics-transformer2.github.io/assets/rt2.pdf"
          },
          {
            "title": "[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"
          },
          {
            "title": "Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
            "url": "https://huggingface.co/papers/2307.15818"
          }
        ]
      },
      "I found comprehensive search results about RT-2, the vision-language-action model. Here's what I found:\n\n## Overview\n\nRT-2 is a novel vision-language-action (VLA) model that learns from both web and robotics data, and translates this knowledge into generalised instructions for robotic control.\n\n## Core Innovation\n\nTo make RT-2 easily compatible with large, pre-trained vision-language models, robot actions are represented as another language, which can be cast into text tokens and trained together with Internet-scale vision-language datasets. The approach proposes to co-fine-tune state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering.\n\n## Key Capabilities\n\nRT-2 demonstrates significantly improved generalization to novel objects, the ability to interpret commands not present in the robot training data (such as placing an object onto a particular number or icon), and the ability to perform rudimentary reasoning in response to user commands (such as picking up the smallest or largest object, or the one closest to another object). \n\nIncorporating chain of thought reasoning allows RT-2 to perform multi-stage semantic reasoning, for example figuring out which object to pick up for use as an improvised hammer (a rock), or which type of drink is best suited for someone who is too sleepy.\n\n## Authors and Publication\n\nThe work was authored by Anthony Brohan and 53 other co-authors from DeepMind. The paper was published in the Proceedings of The 7th Conference on Robot Learning (2023)."
    ],
    "durationSeconds": 5.396320583999999
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T12:09:27.509Z_

<details><summary>↩ Tool result · `toolu_01HgC1BnEKCAbSNJMVYHpUve`</summary>

```text
Web search results for query: "OpenVLA Kim 2024 arXiv vision language action model"

Links: [{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://proceedings.mlr.press/v270/kim25c.html"},{"title":"Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions","url":"https://arxiv.org/html/2505.11214v1"},{"title":"VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models","url":"https://arxiv.org/html/2601.03309v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"openvla/openvla-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"}]

Based on the search results, here's what I found about OpenVLA:

## Overview

OpenVLA is a vision-language-action (VLA) model that represents large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations. It is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations.

## Authors and Affiliation

The model was created by researchers from Stanford University, UC Berkeley, Toyota Research Institute, Google DeepMind, Physical Intelligence, and MIT, including Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, and others.

## Paper Details

The paper was submitted on June 13, 2024, with the arXiv identifier 2406.09246.

## Architecture

The model consists of three key elements: (1) a fused visual encoder with SigLIP and DinoV2 backbones that maps images to patch embeddings, (2) a projector that maps visual encoder outputs into a language model's input space, and (3) a Llama 2 7B language model backbone.

## Key Capabilities

OpenVLA 7B takes language instructions and camera images as input and generates robot actions. The model shows strong generalization results in multi-task environments involving multiple objects and strong language grounding abilities, outperforming Diffusion Policy by 20.4%.

## Accessibility

OpenVLA can be fine-tuned on consumer GPUs via low-rank adaptation methods and served efficiently via quantization, with model checkpoints, fine-tuning notebooks, and PyTorch codebase released for training VLAs at scale.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "34c4d920-adab-48ef-ab2a-f76b7b60f637",
  "tool_use_result": {
    "query": "OpenVLA Kim 2024 arXiv vision language action model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YUKiuEzsdbU9KjG599pkjN",
        "content": [
          {
            "title": "[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/abs/2406.09246"
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
            "title": "[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://proceedings.mlr.press/v270/kim25c.html"
          },
          {
            "title": "Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions",
            "url": "https://arxiv.org/html/2505.11214v1"
          },
          {
            "title": "VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2601.03309v1"
          },
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/html/2508.10333v1"
          },
          {
            "title": "openvla/openvla-7b · Hugging Face",
            "url": "https://huggingface.co/openvla/openvla-7b"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v2"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA:\n\n## Overview\n\nOpenVLA is a vision-language-action (VLA) model that represents large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations. It is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations.\n\n## Authors and Affiliation\n\nThe model was created by researchers from Stanford University, UC Berkeley, Toyota Research Institute, Google DeepMind, Physical Intelligence, and MIT, including Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, and others.\n\n## Paper Details\n\nThe paper was submitted on June 13, 2024, with the arXiv identifier 2406.09246.\n\n## Architecture\n\nThe model consists of three key elements: (1) a fused visual encoder with SigLIP and DinoV2 backbones that maps images to patch embeddings, (2) a projector that maps visual encoder outputs into a language model's input space, and (3) a Llama 2 7B language model backbone.\n\n## Key Capabilities\n\nOpenVLA 7B takes language instructions and camera images as input and generates robot actions. The model shows strong generalization results in multi-task environments involving multiple objects and strong language grounding abilities, outperforming Diffusion Policy by 20.4%.\n\n## Accessibility\n\nOpenVLA can be fine-tuned on consumer GPUs via low-rank adaptation methods and served efficiently via quantization, with model checkpoints, fine-tuning notebooks, and PyTorch codebase released for training VLAs at scale."
    ],
    "durationSeconds": 7.573056169999998
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T12:09:30.084Z_

<details><summary>↩ Tool result · `toolu_016RGLEdjkdkMvRJcNtPus6C`</summary>

```text
Web search results for query: "Octo Team 2024 robot policy arXiv"

Links: [{"title":"[2405.12213] Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/abs/2405.12213"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/html/2405.12213v1"},{"title":"Octo: An Open-Source Generalist Robot Policy - Paper Detail","url":"https://deeplearn.org/arxiv/487297/octo:-an-open-source-generalist-robot-policy"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/"},{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://arxiv.org/pdf/2405.12213"},{"title":"[PDF] Octo: An Open-Source Generalist Robot Policy | Semantic Scholar","url":"https://www.semanticscholar.org/paper/1d2753d74025e7a71594506623be81f18b073adb"},{"title":"[2405.12213v2] Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/abs/2405.12213v2"},{"title":"dblp: Octo: An Open-Source Generalist Robot Policy.","url":"https://dblp.org/rec/journals/corr/abs-2405-12213.html"},{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://openreview.net/pdf/e2dabc0a3fd32239dcab07d7bcfa1fae085f49b0.pdf"},{"title":"Octo: An Open-Source Generalist Robot Policy | Request PDF","url":"https://www.researchgate.net/publication/383897130_Octo_An_Open-Source_Generalist_Robot_Policy"}]

I found the arXiv paper you're looking for! Here's what I discovered:

## Octo: An Open-Source Generalist Robot Policy

Octo is a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date.

**Key Features:**
- It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action space
- Two initial versions are available: Octo-Small (27M parameters) and Octo-Base (93M parameters)

**Performance & Evaluation:**
- In experiments across 9 robotic platforms, Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces
- Out-of-the-box, when using natural language to specify tasks, it outperforms RT-1-X, and performs similarly to RT-2-X, a 55-billion parameter model

**Paper Details:**
- **arXiv ID:** 2405.12213
- **Submitted:** May 20, 2024
- **Last revised:** May 26, 2024
- **Authors:** Octo Model Team (including researchers from UC Berkeley, Stanford, Carnegie Mellon University, and Google DeepMind)
- **Published in:** Proceedings of Robotics: Science and Systems (2024)

The paper and code are publicly available at the official website: https://octo-models.github.io/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "e14284d4-5663-41ef-99ab-2a5d0e0cf8af",
  "tool_use_result": {
    "query": "Octo Team 2024 robot policy arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F3yoL6HPRTbPuVUfsfVCJj",
        "content": [
          {
            "title": "[2405.12213] Octo: An Open-Source Generalist Robot Policy",
            "url": "https://arxiv.org/abs/2405.12213"
          },
          {
            "title": "Octo: An Open-Source Generalist Robot Policy",
            "url": "https://arxiv.org/html/2405.12213v1"
          },
          {
            "title": "Octo: An Open-Source Generalist Robot Policy - Paper Detail",
            "url": "https://deeplearn.org/arxiv/487297/octo:-an-open-source-generalist-robot-policy"
          },
          {
            "title": "Octo: An Open-Source Generalist Robot Policy",
            "url": "https://octo-models.github.io/"
          },
          {
            "title": "Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1",
            "url": "https://arxiv.org/pdf/2405.12213"
          },
          {
            "title": "[PDF] Octo: An Open-Source Generalist Robot Policy | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/1d2753d74025e7a71594506623be81f18b073adb"
          },
          {
            "title": "[2405.12213v2] Octo: An Open-Source Generalist Robot Policy",
            "url": "https://arxiv.org/abs/2405.12213v2"
          },
          {
            "title": "dblp: Octo: An Open-Source Generalist Robot Policy.",
            "url": "https://dblp.org/rec/journals/corr/abs-2405-12213.html"
          },
          {
            "title": "Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1",
            "url": "https://openreview.net/pdf/e2dabc0a3fd32239dcab07d7bcfa1fae085f49b0.pdf"
          },
          {
            "title": "Octo: An Open-Source Generalist Robot Policy | Request PDF",
            "url": "https://www.researchgate.net/publication/383897130_Octo_An_Open-Source_Generalist_Robot_Policy"
          }
        ]
      },
      "I found the arXiv paper you're looking for! Here's what I discovered:\n\n## Octo: An Open-Source Generalist Robot Policy\n\nOcto is a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date.\n\n**Key Features:**\n- It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action space\n- Two initial versions are available: Octo-Small (27M parameters) and Octo-Base (93M parameters)\n\n**Performance & Evaluation:**\n- In experiments across 9 robotic platforms, Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces\n- Out-of-the-box, when using natural language to specify tasks, it outperforms RT-1-X, and performs similarly to RT-2-X, a 55-billion parameter model\n\n**Paper Details:**\n- **arXiv ID:** 2405.12213\n- **Submitted:** May 20, 2024\n- **Last revised:** May 26, 2024\n- **Authors:** Octo Model Team (including researchers from UC Berkeley, Stanford, Carnegie Mellon University, and Google DeepMind)\n- **Published in:** Proceedings of Robotics: Science and Systems (2024)\n\nThe paper and code are publicly available at the official website: https://octo-models.github.io/"
    ],
    "durationSeconds": 8.740267953
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T12:09:30.110Z_

<details><summary>↩ Tool result · `toolu_01X4YdjQQHzwH5mS7ZbPGAjr`</summary>

```text
Web search results for query: "vision language action model robot 2024 2025 survey"

Links: [{"title":"Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://vla-survey.github.io/"},{"title":"[2510.07077] Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://arxiv.org/abs/2510.07077"},{"title":"A Survey on Vision-Language-Action Models for Embodied ...","url":"https://arxiv.org/html/2405.14093v8"},{"title":"[2405.14093] A Survey on Vision-Language-Action Models for Embodied AI","url":"https://arxiv.org/abs/2405.14093"},{"title":"[2507.01925] A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/abs/2507.01925"},{"title":"GitHub - Psi-Robot/Awesome-VLA-Papers: Paper list in the survey: A Survey on Vision-Language-Action Models: An Action Tokenization Perspective · GitHub","url":"https://github.com/Psi-Robot/Awesome-VLA-Papers"},{"title":"[Literature Review] Survey of Vision-Language-Action Models for Embodied Manipulation","url":"https://www.themoonlight.io/en/review/survey-of-vision-language-action-models-for-embodied-manipulation"},{"title":"[2510.24795] A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.24795"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"}]

Based on the search results, I found several comprehensive surveys on Vision-Language-Action (VLA) models for robotics from 2024-2025:

## Major Surveys on VLAs

**1. Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications**

This 2025 survey by Kawaharazuka et al. was published in IEEE Access. Unlike previous surveys that focus narrowly on action representations or high-level model architectures, this work offers a comprehensive, full-stack review, integrating both software and hardware components of VLA systems. The paper provides a systematic review of VLAs covering their strategy and architectural transition, architectures and building blocks, modality-specific processing techniques, learning paradigms, commonly used robot platforms, data collection strategies, publicly available datasets, data augmentation methods, and evaluation benchmarks.

**2. A Survey on Vision-Language-Action Models for Embodied AI**

This survey by Ma et al. was first submitted in May 2024 with the most recent version from February 2026. Building on the success of large language models and vision-language models, a new category of multimodal models—referred to as vision-language-action models (VLAs)—has emerged to address language-conditioned robotic tasks in embodied AI.

**3. A Survey on Vision-Language-Action Models: An Action Tokenization Perspective**

This survey by Zhong et al. was submitted in July 2025 and focuses specifically on action tokenization approaches in VLAs.

**4. A Survey on Efficient Vision-Language-Action Models**

This survey presents the first comprehensive review of Efficient Vision-Language-Action models across the entire model-training-data pipeline, categorizing techniques into three core pillars: (1) Efficient Model Design, (2) Efficient Training, and (3) Efficient Data Collection. The timeline reveals a distinct acceleration in the emergence of efficient VLAs, particularly from late 2024 onwards.

## Current Trends (2024-2025)

The trend in 2024-2025 focuses on integrating LLM/VLM reasoning, enhancing efficiency, and exploring hierarchical (System 1/2/3) architectures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "d1b7313e-44a7-4bf2-b723-c987a094447b",
  "tool_use_result": {
    "query": "vision language action model robot 2024 2025 survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L9eUvanPqU6Q6jUgYWB41o",
        "content": [
          {
            "title": "Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications",
            "url": "https://vla-survey.github.io/"
          },
          {
            "title": "[2510.07077] Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications",
            "url": "https://arxiv.org/abs/2510.07077"
          },
          {
            "title": "A Survey on Vision-Language-Action Models for Embodied ...",
            "url": "https://arxiv.org/html/2405.14093v8"
          },
          {
            "title": "[2405.14093] A Survey on Vision-Language-Action Models for Embodied AI",
            "url": "https://arxiv.org/abs/2405.14093"
          },
          {
            "title": "[2507.01925] A Survey on Vision-Language-Action Models: An Action Tokenization Perspective",
            "url": "https://arxiv.org/abs/2507.01925"
          },
          {
            "title": "GitHub - Psi-Robot/Awesome-VLA-Papers: Paper list in the survey: A Survey on Vision-Language-Action Models: An Action Tokenization Perspective · GitHub",
            "url": "https://github.com/Psi-Robot/Awesome-VLA-Papers"
          },
          {
            "title": "[Literature Review] Survey of Vision-Language-Action Models for Embodied Manipulation",
            "url": "https://www.themoonlight.io/en/review/survey-of-vision-language-action-models-for-embodied-manipulation"
          },
          {
            "title": "[2510.24795] A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.24795"
          },
          {
            "title": "1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey",
            "url": "https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v1"
          }
        ]
      },
      "Based on the search results, I found several comprehensive surveys on Vision-Language-Action (VLA) models for robotics from 2024-2025:\n\n## Major Surveys on VLAs\n\n**1. Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications**\n\nThis 2025 survey by Kawaharazuka et al. was published in IEEE Access. Unlike previous surveys that focus narrowly on action representations or high-level model architectures, this work offers a comprehensive, full-stack review, integrating both software and hardware components of VLA systems. The paper provides a systematic review of VLAs covering their strategy and architectural transition, architectures and building blocks, modality-specific processing techniques, learning paradigms, commonly used robot platforms, data collection strategies, publicly available datasets, data augmentation methods, and evaluation benchmarks.\n\n**2. A Survey on Vision-Language-Action Models for Embodied AI**\n\nThis survey by Ma et al. was first submitted in May 2024 with the most recent version from February 2026. Building on the success of large language models and vision-language models, a new category of multimodal models—referred to as vision-language-action models (VLAs)—has emerged to address language-conditioned robotic tasks in embodied AI.\n\n**3. A Survey on Vision-Language-Action Models: An Action Tokenization Perspective**\n\nThis survey by Zhong et al. was submitted in July 2025 and focuses specifically on action tokenization approaches in VLAs.\n\n**4. A Survey on Efficient Vision-Language-Action Models**\n\nThis survey presents the first comprehensive review of Efficient Vision-Language-Action models across the entire model-training-data pipeline, categorizing techniques into three core pillars: (1) Efficient Model Design, (2) Efficient Training, and (3) Efficient Data Collection. The timeline reveals a distinct acceleration in the emergence of efficient VLAs, particularly from late 2024 onwards.\n\n## Current Trends (2024-2025)\n\nThe trend in 2024-2025 focuses on integrating LLM/VLM reasoning, enhancing efficiency, and exploring hierarchical (System 1/2/3) architectures."
    ],
    "durationSeconds": 7.952115684999999
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T12:09:31.195Z_

<details><summary>↩ Tool result · `toolu_01AJjgPN7HQrEeatBWMcWupE`</summary>

```text
Web search results for query: "pi0 Physical Intelligence 2024 vision language action robot"

Links: [{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"π0 and π0-FAST: Vision-Language-Action Models for General Robot Control","url":"https://huggingface.co/blog/pi0"},{"title":"[2410.24164] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164"},{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"Physical Intelligence Unveils Robotics Foundation Model Pi-Zero - InfoQ","url":"https://www.infoq.com/news/2024/12/pi-zero-robot/"},{"title":"Notes on: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" | cloderic.com","url":"https://www.cloderic.com/content/2025-02-27-notes-on-pi0"},{"title":"[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://www.pi.website/download/pi0.pdf"},{"title":"π 0 : Our First Generalist Policy","url":"https://www.pi.website/blog/pi0"},{"title":"Physical Intelligence (π)","url":"https://www.pi.website/"}]

Based on the search results, here's comprehensive information about π0 (Pi-Zero):

## Overview

π0 (Pi-Zero) is a Vision-Language-Action (VLA) model, developed by the Physical Intelligence team designed for generalist robot control. Physical Intelligence (Pi, or π) is a robotics startup co-founded in early 2024 by Sergey Levine and others from academia and industry. The company raised a $70M seed round, followed by $400M more in late 2024, reaching a $2B valuation.

## Architecture and Capabilities

It builds upon large-scale pretraining and flow matching-based action generation, enabling robots to perform dexterous manipulation tasks across different embodiments. The model uses a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge.

The model's input is a combination of vision images, the robot's joint angles, and a language command; the output is a sequence of robot action tokens.

## Training Data and Performance

π0 is trained on data from 7 robotic platforms and 68 unique tasks, demonstrating strong zero-shot and fine-tuned performance on complex, real-world tasks such as laundry folding, table bussing, grocery bagging, box assembly, and object retrieval. Pi-zero is based on the PaliGemma VLM, which was then further trained on a custom dataset collected from 7 different robots performing 68 tasks as well as the Open X-Embodiment dataset.

## Technical Advantages

Unlike standard robotic policies, π0 employs flow matching to produce smooth, real-time action trajectories at 50Hz, making it highly efficient, precise, and adaptable for real-world deployment.

## Recent Developments

A new model based on π0 called π0.5 uses co-training on heterogeneous tasks to enable broad generalization. π0.5 uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89d913d1-15c6-43cb-aa2e-ed734c313a6d",
  "uuid": "e2351be8-d931-4c78-9e55-13f2fc8fd27a",
  "tool_use_result": {
    "query": "pi0 Physical Intelligence 2024 vision language action robot",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BYGG2QpYKbZKeNw6kApbos",
        "content": [
          {
            "title": "𝜋₀: A Vision-Language-Action Flow Model for General Robot Control",
            "url": "https://arxiv.org/html/2410.24164v1"
          },
          {
            "title": "π0 and π0-FAST: Vision-Language-Action Models for General Robot Control",
            "url": "https://huggingface.co/blog/pi0"
          },
          {
            "title": "[2410.24164] $π_0$: A Vision-Language-Action Flow Model for General Robot Control",
            "url": "https://arxiv.org/abs/2410.24164"
          },
          {
            "title": "GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub",
            "url": "https://github.com/lucidrains/pi-zero-pytorch"
          },
          {
            "title": "Physical Intelligence Unveils Robotics Foundation Model Pi-Zero - InfoQ",
            "url": "https://www.infoq.com/news/2024/12/pi-zero-robot/"
          },
          {
            "title": "Notes on: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" | cloderic.com",
            "url": "https://www.cloderic.com/content/2025-02-27-notes-on-pi0"
          },
          {
            "title": "[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization",
            "url": "https://arxiv.org/abs/2504.16054"
          },
          {
            "title": "π0: A Vision-Language-Action Flow Model for General Robot Control",
            "url": "https://www.pi.website/download/pi0.pdf"
          },
          {
            "title": "π 0 : Our First Generalist Policy",
            "url": "https://www.pi.website/blog/pi0"
          },
          {
            "title": "Physical Intelligence (π)",
            "url": "https://www.pi.website/"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about π0 (Pi-Zero):\n\n## Overview\n\nπ0 (Pi-Zero) is a Vision-Language-Action (VLA) model, developed by the Physical Intelligence team designed for generalist robot control. Physical Intelligence (Pi, or π) is a robotics startup co-founded in early 2024 by Sergey Levine and others from academia and industry. The company raised a $70M seed round, followed by $400M more in late 2024, reaching a $2B valuation.\n\n## Architecture and Capabilities\n\nIt builds upon large-scale pretraining and flow matching-based action generation, enabling robots to perform dexterous manipulation tasks across different embodiments. The model uses a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge.\n\nThe model's input is a combination of vision images, the robot's joint angles, and a language command; the output is a sequence of robot action tokens.\n\n## Training Data and Performance\n\nπ0 is trained on data from 7 robotic platforms and 68 unique tasks, demonstrating strong zero-shot and fine-tuned performance on complex, real-world tasks such as laundry folding, table bussing, grocery bagging, box assembly, and object retrieval. Pi-zero is based on the PaliGemma VLM, which was then further trained on a custom dataset collected from 7 different robots performing 68 tasks as well as the Open X-Embodiment dataset.\n\n## Technical Advantages\n\nUnlike standard robotic policies, π0 employs flow matching to produce smooth, real-time action trajectories at 50Hz, making it highly efficient, precise, and adaptable for real-world deployment.\n\n## Recent Developments\n\nA new model based on π0 called π0.5 uses co-training on heterogeneous tasks to enable broad generalization. π0.5 uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation."
    ],
    "durationSeconds": 9.379816994999999
  }
}
```

</details>

---
