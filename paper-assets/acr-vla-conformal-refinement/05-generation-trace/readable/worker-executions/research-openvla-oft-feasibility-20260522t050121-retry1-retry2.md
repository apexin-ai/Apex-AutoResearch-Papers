# research openvla oft feasibility 20260522T050121 retry1 retry2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_research_openvla-oft-feasibility_20260522T050121_retry1_retry2.log`
- **Structured JSON:** [`54a568a80317e2005de7.json`](../../sessions/54/54a568a80317e2005de7.json)

## Before a recorded user message

50 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
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
    "Write"
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
  "uuid": "6a045535-1935-40c3-95ed-e5476ba1a3b6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 2_

我来搜索 OpenVLA-OFT 的相关信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "a6fcc3de-1e54-4327-92e4-d0660672012a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iewTZogbwPHmALZFB8jax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11921,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11921
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

_source line 3_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019RHSuNLQreduewHR22NYpW`</summary>

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
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "167cbd62-6e1e-404c-b5ba-06d23e788ae9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iewTZogbwPHmALZFB8jax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11921,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11921
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

_source line 4 · 2026-05-22T05:02:32.882Z_

<details><summary>↩ Tool result · `toolu_019RHSuNLQreduewHR22NYpW`</summary>

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
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "745aa453-0750-41e5-b1dc-1528f1656fbd",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  }
}
```

</details>

---

### Runtime record

_source line 5_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779667200,
    "rateLimitType": "seven_day",
    "utilization": 0.87,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "033209cb-c20c-48ee-bf6d-90ffffc7ca75",
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08"
}
```

---

### Assistant

_source line 6_

<details><summary>Logged reasoning block</summary>

```text
Let me search for OpenVLA-OFT information in parallel across multiple queries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "efaea2e6-e45b-4642-a153-78edce6b9795",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UExJVy2rkWQFpxDNVpedLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 23762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
      },
      "output_tokens": 25,
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

_source line 7_

并行搜索 OpenVLA-OFT 相关信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "9433b875-96a8-47b6-bde1-62bf6b434681",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UExJVy2rkWQFpxDNVpedLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 23762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kguakb39jaXKS6mppGSvUS`</summary>

```json
{
  "query": "OpenVLA-OFT paper flow matching fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "5eeae1e5-7f83-4b64-9893-e78f09be9bed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UExJVy2rkWQFpxDNVpedLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 23762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015tMQgkRagE3KSBSrP8Xn1j`</summary>

```json
{
  "query": "OpenVLA-OFT github repository code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "26eaa567-0fec-4870-a06f-6fd51925d122",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UExJVy2rkWQFpxDNVpedLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 23762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VC7M6tQAf4JinebVCuDtU4`</summary>

```json
{
  "query": "OpenVLA-OFT huggingface checkpoint weights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "9a1f8736-8870-4d3c-87ff-bc88fb1d45c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UExJVy2rkWQFpxDNVpedLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 23762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KVQeunPV7BXs3FnQhYWKPn`</summary>

```json
{
  "query": "OpenVLA-OFT LIBERO benchmark performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "6ad575e6-0287-45cb-be5f-4f1aae8cf1c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UExJVy2rkWQFpxDNVpedLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 23762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
      },
      "output_tokens": 25,
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

_source line 12 · 2026-05-22T05:02:46.947Z_

<details><summary>↩ Tool result · `toolu_015tMQgkRagE3KSBSrP8Xn1j`</summary>

```text
Web search results for query: "OpenVLA-OFT github repository code"

Links: [{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub","url":"https://github.com/siyuhsu/vla-cache"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"GitHub - shosae/openvla: OpenVLA","url":"https://github.com/shosae/openvla"},{"title":"GitHub - dusty-nv/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.","url":"https://github.com/dusty-nv/openvla"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"}]

Based on the search results, I found information about the OpenVLA-OFT GitHub repository:

## Main Repository

The primary OpenVLA-OFT repository is located at github.com/moojink/openvla-oft, which contains code for fine-tuning vision-language-action models.

## Key Features

OpenVLA-OFT (Optimized Fine-Tuning recipe for VLAs) enables 25-50x faster inference speed, higher task success rates, multiple input images, and high-frequency bimanual robot control compared to vanilla OpenVLA fine-tuning. Unlike FAST, OFT uses continuous actions for greater model quality.

## Code Examples

The repository includes Python scripts that allow users to download pretrained OpenVLA-OFT checkpoints and run inference to generate action chunks, with utilities like `get_vla()`, `get_processor()`, `get_action_head()`, and other helper functions for loading policies and processing inputs.

The repository also contains evaluation code and configuration classes for various robotic tasks, including LIBERO spatial tasks for evaluating model performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "97753d4f-8bb1-429c-beac-564a77a89aa3",
  "tool_use_result": {
    "query": "OpenVLA-OFT github repository code",
    "results": [
      {
        "tool_use_id": "srvtoolu_016KYNnQTrieWvPyEHPh6fTy",
        "content": [
          {
            "title": "GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub",
            "url": "https://github.com/moojink/openvla-oft"
          },
          {
            "title": "GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub",
            "url": "https://github.com/siyuhsu/vla-cache"
          },
          {
            "title": "GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/CHELabUB/openvla"
          },
          {
            "title": "GitHub - shosae/openvla: OpenVLA",
            "url": "https://github.com/shosae/openvla"
          },
          {
            "title": "GitHub - dusty-nv/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.",
            "url": "https://github.com/dusty-nv/openvla"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/reazon-research/openvla"
          }
        ]
      },
      "Based on the search results, I found information about the OpenVLA-OFT GitHub repository:\n\n## Main Repository\n\nThe primary OpenVLA-OFT repository is located at github.com/moojink/openvla-oft, which contains code for fine-tuning vision-language-action models.\n\n## Key Features\n\nOpenVLA-OFT (Optimized Fine-Tuning recipe for VLAs) enables 25-50x faster inference speed, higher task success rates, multiple input images, and high-frequency bimanual robot control compared to vanilla OpenVLA fine-tuning. Unlike FAST, OFT uses continuous actions for greater model quality.\n\n## Code Examples\n\nThe repository includes Python scripts that allow users to download pretrained OpenVLA-OFT checkpoints and run inference to generate action chunks, with utilities like `get_vla()`, `get_processor()`, `get_action_head()`, and other helper functions for loading policies and processing inputs.\n\nThe repository also contains evaluation code and configuration classes for various robotic tasks, including LIBERO spatial tasks for evaluating model performance."
    ],
    "durationSeconds": 6.0286153529999975
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T05:02:47.926Z_

<details><summary>↩ Tool result · `toolu_01KVQeunPV7BXs3FnQhYWKPn`</summary>

```text
Web search results for query: "OpenVLA-OFT LIBERO benchmark performance"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata · Hugging Face","url":"https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2511.11298v1"},{"title":"BitVLA: 1-bit Vision-Language-Action Models for Robotics ...","url":"https://arxiv.org/pdf/2506.07530"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

Based on the search results, here's what I found about OpenVLA-OFT's LIBERO benchmark performance:

## Standard LIBERO Benchmark

OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×. This 97.1% average success rate across 4 task suites outperforms π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy.

The improvements come from an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective.

## LIBERO-Plus (Robustness) Benchmark

When evaluated on the more challenging LIBERO-Plus benchmark with robustness perturbations, the method achieves the highest overall success rate of 79.6%, outperforming all baseline models across nearly all perturbation types. It exhibits a dramatic improvement in camera view robustness (92.8%), surpassing the next best model by 37.2 percentage points.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "e98d0b97-f99c-4fb6-9660-3e6e431fb98d",
  "tool_use_result": {
    "query": "OpenVLA-OFT LIBERO benchmark performance",
    "results": [
      {
        "tool_use_id": "srvtoolu_0173XVyK48K5Fc9s1kFZvpyR",
        "content": [
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/pdf/2502.19645"
          },
          {
            "title": "OpenVLA-OFT",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata · Hugging Face",
            "url": "https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.11298v1"
          },
          {
            "title": "BitVLA: 1-bit Vision-Language-Action Models for Robotics ...",
            "url": "https://arxiv.org/pdf/2506.07530"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA-OFT's LIBERO benchmark performance:\n\n## Standard LIBERO Benchmark\n\nOpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×. This 97.1% average success rate across 4 task suites outperforms π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy.\n\nThe improvements come from an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective.\n\n## LIBERO-Plus (Robustness) Benchmark\n\nWhen evaluated on the more challenging LIBERO-Plus benchmark with robustness perturbations, the method achieves the highest overall success rate of 79.6%, outperforming all baseline models across nearly all perturbation types. It exhibits a dramatic improvement in camera view robustness (92.8%), surpassing the next best model by 37.2 percentage points."
    ],
    "durationSeconds": 6.3314218009999985
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T05:02:47.955Z_

<details><summary>↩ Tool result · `toolu_01Kguakb39jaXKS6mppGSvUS`</summary>

```text
Web search results for query: "OpenVLA-OFT paper flow matching fine-tuning"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models","url":"https://arxiv.org/html/2510.09976v1"},{"title":"Chelsea Finn on X: \"We can now fine-tune the 7B OpenVLA model for 50 Hz control! 🤖 Paper: https://t.co/TxQJ42lYi8 Code: https://t.co/u5nzhytzRA\" / X","url":"https://x.com/chelseabfinn/status/1895538801742930041"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Online Reward-Weighted Fine-Tuning of Flow Matching with Wasserstein   Regularization","url":"https://arxiv.org/pdf/2502.06061"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"}]

I found research on the OpenVLA-OFT paper. Here's what the search revealed:

OpenVLA-OFT is an instantiation of an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding and action chunking, continuous action representations, and an L1 regression objective to enhance inference efficiency, task performance, and model input-output flexibility while maintaining algorithmic simplicity.

OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×.

In real-world evaluations, the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs (π₀ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate.

The paper titled "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" was published in February 2025, with code and pretrained checkpoints available at openvla-oft.github.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "21075112-e7fe-4f20-9ec9-192ecbcafb61",
  "tool_use_result": {
    "query": "OpenVLA-OFT paper flow matching fine-tuning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GjGNVY8naGs31JL8JkFj9t",
        "content": [
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v1"
          },
          {
            "title": "Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.09976v1"
          },
          {
            "title": "Chelsea Finn on X: \"We can now fine-tune the 7B OpenVLA model for 50 Hz control! 🤖 Paper: https://t.co/TxQJ42lYi8 Code: https://t.co/u5nzhytzRA\" / X",
            "url": "https://x.com/chelseabfinn/status/1895538801742930041"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/pdf/2502.19645"
          },
          {
            "title": "GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub",
            "url": "https://github.com/moojink/openvla-oft"
          },
          {
            "title": "Online Reward-Weighted Fine-Tuning of Flow Matching with Wasserstein   Regularization",
            "url": "https://arxiv.org/pdf/2502.06061"
          },
          {
            "title": "[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/abs/2502.19645"
          }
        ]
      },
      "I found research on the OpenVLA-OFT paper. Here's what the search revealed:\n\nOpenVLA-OFT is an instantiation of an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding and action chunking, continuous action representations, and an L1 regression objective to enhance inference efficiency, task performance, and model input-output flexibility while maintaining algorithmic simplicity.\n\nOpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×.\n\nIn real-world evaluations, the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs (π₀ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate.\n\nThe paper titled \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" was published in February 2025, with code and pretrained checkpoints available at openvla-oft.github.io."
    ],
    "durationSeconds": 7.042668736000001
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T05:02:48.806Z_

<details><summary>↩ Tool result · `toolu_01VC7M6tQAf4JinebVCuDtU4`</summary>

```text
Web search results for query: "OpenVLA-OFT huggingface checkpoint weights"

Links: [{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=OpenVLA-OFT"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"openvla/openvla-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"openvla/openvla-7b · An issue about full-fine tuning.","url":"https://huggingface.co/openvla/openvla-7b/discussions/3"}]

Based on the search results, here's what I found about OpenVLA-OFT huggingface checkpoint weights:

The code for OFT and pretrained model checkpoints are released at https://openvla-oft.github.io/.

Several fine-tuned OpenVLA-OFT checkpoint variants are available on Hugging Face:

- moojink/openvla-7b-oft-finetuned-libero-spatial - an OpenVLA-OFT checkpoint for LIBERO-Spatial
- moojink/openvla-7b-oft-finetuned-libero-10 - an OpenVLA-OFT checkpoint for LIBERO-Long
- moojink/openvla-7b-oft-finetuned-libero-goal - an OpenVLA-OFT checkpoint for LIBERO-Goal
- moojink/openvla-7b-oft-finetuned-libero-object - an OpenVLA-OFT checkpoint for LIBERO-Object

OpenVLA-OFT significantly improves upon the base OpenVLA model by incorporating optimized fine-tuning techniques. Additionally, the trained model checkpoints can be downloaded from HuggingFace, and all OpenVLA checkpoints are released under an MIT License.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "d61f0ae9-3c2e-42d5-856c-c6b48f3901f3",
  "tool_use_result": {
    "query": "OpenVLA-OFT huggingface checkpoint weights",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ARsvmTLwLBsMU5squd2mi5",
        "content": [
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=OpenVLA-OFT"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "openvla/openvla-7b · Hugging Face",
            "url": "https://huggingface.co/openvla/openvla-7b"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "openvla/openvla-7b · An issue about full-fine tuning.",
            "url": "https://huggingface.co/openvla/openvla-7b/discussions/3"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA-OFT huggingface checkpoint weights:\n\nThe code for OFT and pretrained model checkpoints are released at https://openvla-oft.github.io/.\n\nSeveral fine-tuned OpenVLA-OFT checkpoint variants are available on Hugging Face:\n\n- moojink/openvla-7b-oft-finetuned-libero-spatial - an OpenVLA-OFT checkpoint for LIBERO-Spatial\n- moojink/openvla-7b-oft-finetuned-libero-10 - an OpenVLA-OFT checkpoint for LIBERO-Long\n- moojink/openvla-7b-oft-finetuned-libero-goal - an OpenVLA-OFT checkpoint for LIBERO-Goal\n- moojink/openvla-7b-oft-finetuned-libero-object - an OpenVLA-OFT checkpoint for LIBERO-Object\n\nOpenVLA-OFT significantly improves upon the base OpenVLA model by incorporating optimized fine-tuning techniques. Additionally, the trained model checkpoints can be downloaded from HuggingFace, and all OpenVLA checkpoints are released under an MIT License."
    ],
    "durationSeconds": 7.435052993999999
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a lot of initial information. Now I need more details on:
1. Architecture specifics - is it flow matching or autoregressive? Action head details
2. Action space dimensions, chunk length, normalization
3. Observation features dimension
4. GPU memory requirements
5. Specific LIBERO per-suite scores (Object/Spatial/Long/Goal)
6. Sampling mechanism - temperature, stochasticity

Let me search for more specific details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "6049bfdf-da9f-455b-81e1-c397ef4f4b08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mQcUpBuV5syg8GhKkuLc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 24388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2533
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

_source line 17_

找到基础信息了，继续搜索架构细节和 LIBERO 分项成绩。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "cdf04ca5-79bf-4554-a860-3952cb317d26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mQcUpBuV5syg8GhKkuLc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 24388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2533
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

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PgWknJcdC7c3YyKiAN3XLV`</summary>

```json
{
  "query": "OpenVLA-OFT architecture action head MLP continuous action chunking parallel decoding details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "3e64df53-2275-4984-a90f-f9061bf541a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mQcUpBuV5syg8GhKkuLc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 24388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2533
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

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PrFcp3r2y4ijDwrpMxYJ4a`</summary>

```json
{
  "query": "OpenVLA-OFT LIBERO object spatial long goal success rate per suite"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "27e81df5-7af7-4047-9a16-aa53ea49f500",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mQcUpBuV5syg8GhKkuLc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 24388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2533
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

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BuQiKEqJqbwrxPZMZWvD44`</summary>

```json
{
  "query": "OpenVLA-OFT inference GPU memory requirements 7B parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "e1eb1e23-4673-4829-84df-38c926d63f89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mQcUpBuV5syg8GhKkuLc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 24388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2533
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

### Runtime record

_source line 21_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779667200,
    "rateLimitType": "seven_day",
    "utilization": 0.87,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "b8b80866-9c88-4aa6-ae8e-d8024ca69a72",
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779667200,
    "rateLimitType": "seven_day",
    "utilization": 0.87,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "15bdf567-2e23-4c69-9f6c-f3a02e1416e0",
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08"
}
```

---

### Tool result

_source line 23 · 2026-05-22T05:03:05.896Z_

<details><summary>↩ Tool result · `toolu_01BuQiKEqJqbwrxPZMZWvD44`</summary>

```text
Web search results for query: "OpenVLA-OFT inference GPU memory requirements 7B parameters"

Links: [{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"openvla-7b can’t run on multi-GPU rigs with ≤11 GB cards · Issue #311 · openvla/openvla","url":"https://github.com/openvla/openvla/issues/311"},{"title":"openvla-7b can't run on multi-GPU rigs with ≤11 GB cards","url":"https://ask-angle.netlify.app/?page=en-git-openvla-openvla-1761890550887"},{"title":"Deploy OpenVLA on GPU Cloud: Self-Host the Open Vision-Language-Action Robotics Foundation Model (2026 Setup Guide) | Spheron Blog","url":"https://www.spheron.network/blog/deploy-openvla-gpu-cloud/"},{"title":"Running Vision Models: VRAM Requirements and Optimization · Technical news about AI, coding and all","url":"https://dasroot.net/posts/2026/01/running-vision-models-vram-requirements/"},{"title":"GPU Memory Requirements for LLM Inference and Fine-Tuning - Platform for AI - Alibaba Cloud","url":"https://www.alibabacloud.com/help/en/pai/getting-started/estimation-of-the-required-video-memory-for-the-model"}]

Based on the search results, here's what I found about OpenVLA-OFT inference GPU memory requirements for the 7B parameter model:

## OpenVLA-OFT Inference GPU Memory Requirements

For OpenVLA-OFT inference with LIBERO (1 input image, 7 action dimensions, action chunk size 8) using the default bfloat16 data type, you need approximately 15.9 GB of GPU memory.

More broadly, OpenVLA's 7B parameters require ~16GB GPU memory for inference, fitting on a single A100, RTX 4090, or RTX 3090. Additionally, OpenVLA 7B in BF16 occupies approximately 14-15 GB of VRAM for weights.

The memory requirements can be reduced further through quantization techniques if needed, though the specific quantization requirements for OpenVLA-OFT weren't detailed in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "496770b1-dfa7-4808-88a4-b92565ec620f",
  "tool_use_result": {
    "query": "OpenVLA-OFT inference GPU memory requirements 7B parameters",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NfiH4XyHELUVoEDgjRg5mP",
        "content": [
          {
            "title": "Training Data for OpenVLA | Data Requirements & Formats | Claru",
            "url": "https://claru.ai/models/openvla"
          },
          {
            "title": "OpenVLA-OFT",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2406.09246v3"
          },
          {
            "title": "openvla-7b can’t run on multi-GPU rigs with ≤11 GB cards · Issue #311 · openvla/openvla",
            "url": "https://github.com/openvla/openvla/issues/311"
          },
          {
            "title": "openvla-7b can't run on multi-GPU rigs with ≤11 GB cards",
            "url": "https://ask-angle.netlify.app/?page=en-git-openvla-openvla-1761890550887"
          },
          {
            "title": "Deploy OpenVLA on GPU Cloud: Self-Host the Open Vision-Language-Action Robotics Foundation Model (2026 Setup Guide) | Spheron Blog",
            "url": "https://www.spheron.network/blog/deploy-openvla-gpu-cloud/"
          },
          {
            "title": "Running Vision Models: VRAM Requirements and Optimization · Technical news about AI, coding and all",
            "url": "https://dasroot.net/posts/2026/01/running-vision-models-vram-requirements/"
          },
          {
            "title": "GPU Memory Requirements for LLM Inference and Fine-Tuning - Platform for AI - Alibaba Cloud",
            "url": "https://www.alibabacloud.com/help/en/pai/getting-started/estimation-of-the-required-video-memory-for-the-model"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA-OFT inference GPU memory requirements for the 7B parameter model:\n\n## OpenVLA-OFT Inference GPU Memory Requirements\n\nFor OpenVLA-OFT inference with LIBERO (1 input image, 7 action dimensions, action chunk size 8) using the default bfloat16 data type, you need approximately 15.9 GB of GPU memory.\n\nMore broadly, OpenVLA's 7B parameters require ~16GB GPU memory for inference, fitting on a single A100, RTX 4090, or RTX 3090. Additionally, OpenVLA 7B in BF16 occupies approximately 14-15 GB of VRAM for weights.\n\nThe memory requirements can be reduced further through quantization techniques if needed, though the specific quantization requirements for OpenVLA-OFT weren't detailed in these results."
    ],
    "durationSeconds": 4.940904050999998
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T05:03:06.746Z_

<details><summary>↩ Tool result · `toolu_01PrFcp3r2y4ijDwrpMxYJ4a`</summary>

```text
Web search results for query: "OpenVLA-OFT LIBERO object spatial long goal success rate per suite"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/4ac089329d3a3ce0a6125ef6c36a66d6a4d91f63.pdf"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action Models","url":"https://arxiv.org/html/2509.23655v1"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"RL with LIBERO Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"}]

Based on the search results, here's what I found about OpenVLA-OFT performance on the LIBERO benchmark:

OpenVLA-OFT was evaluated on four LIBERO task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long, each providing 500 expert demonstrations across 10 tasks.

OpenVLA-OFT significantly boosted OpenVLA's average success rate across four task suites from 76.5% to 97.1%. However, the search results don't provide the specific per-suite breakdown of success rates for each individual LIBERO suite (Spatial, Object, Goal, and Long).

The results do indicate that even without any valid language input, the performance of OpenVLA-OFT on the object suite remained largely unchanged, with significant degradation observed only on the long suite, suggesting that the Long suite is more challenging than the Object suite.

For more detailed per-suite success rates, you may need to consult the full paper or supplementary materials linked in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "154b2bd8-f646-421d-b80a-d73022e25cf5",
  "tool_use_result": {
    "query": "OpenVLA-OFT LIBERO object spatial long goal success rate per suite",
    "results": [
      {
        "tool_use_id": "srvtoolu_015kaBton1B8bUuwimMwDMvF",
        "content": [
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v1"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2502.19645"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf/4ac089329d3a3ce0a6125ef6c36a66d6a4d91f63.pdf"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action Models",
            "url": "https://arxiv.org/html/2509.23655v1"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10 · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10"
          },
          {
            "title": "OpenVLA-OFT",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "RL with LIBERO Benchmark — RLinf documentation",
            "url": "https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/pdf/2502.19645"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA-OFT performance on the LIBERO benchmark:\n\nOpenVLA-OFT was evaluated on four LIBERO task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long, each providing 500 expert demonstrations across 10 tasks.\n\nOpenVLA-OFT significantly boosted OpenVLA's average success rate across four task suites from 76.5% to 97.1%. However, the search results don't provide the specific per-suite breakdown of success rates for each individual LIBERO suite (Spatial, Object, Goal, and Long).\n\nThe results do indicate that even without any valid language input, the performance of OpenVLA-OFT on the object suite remained largely unchanged, with significant degradation observed only on the long suite, suggesting that the Long suite is more challenging than the Object suite.\n\nFor more detailed per-suite success rates, you may need to consult the full paper or supplementary materials linked in the search results."
    ],
    "durationSeconds": 5.9832061130000005
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T05:03:07.860Z_

<details><summary>↩ Tool result · `toolu_01PgWknJcdC7c3YyKiAN3XLV`</summary>

```text
Web search results for query: "OpenVLA-OFT architecture action head MLP continuous action chunking parallel decoding details"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"OpenVLA-OFT+ on the bimanual ALOHA robot. Our Optimized Fine-Tuning... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/OpenVLA-OFT-on-the-bimanual-ALOHA-robot-Our-Optimized-Fine-Tuning-OFT-recipe-enhances_fig1_389399234"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"},{"title":"BitVLA: 1-bit Vision-Language-Action Models for Robotics ...","url":"https://arxiv.org/pdf/2506.07530"},{"title":"(PDF) Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.researchgate.net/publication/389399234_Fine-Tuning_Vision-Language-Action_Models_Optimizing_Speed_and_Success"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"[Literature Review] BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation","url":"https://www.themoonlight.io/en/review/bitvla-1-bit-vision-language-action-models-for-robotics-manipulation"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"}]

Based on the search results, here are the detailed architectural components of OpenVLA-OFT:

## Action Head Architecture

The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions. The MLP-based action head projects the latent representations of query tokens into continuous robotic action space.

## Continuous Action Representation

With continuous action representation, the VLA can directly model the action distribution without lossy discretization, as opposed to the baseline OpenVLA which uses discrete action tokens where each action dimension is normalized to [-1,+1] and uniformly discretized into 256 bins, with the discretization process sacrificing fine-grained action details.

## Parallel Decoding

The model architecture is modified to accept empty action embeddings as inputs, removing the necessity for a causal attention mask, and instead implementing bidirectional attention. Empty action embeddings differ only in their positional encoding values.

## Action Chunking

The model predicts sequences of K future actions rather than single timesteps, and for the ALOHA robot experiments, K=25 actions are predicted simultaneously, dramatically increasing throughput while maintaining low latency. Adding action chunking with K=8 increases latency by 17% due to longer attention sequences in the decoder, but when combined with parallel decoding, it dramatically improves throughput, achieving a 26x speedup over baseline OpenVLA.

## Overall Performance

Through parallel decoding and action chunking, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "02cecb5e-928b-4012-8ac2-08b4138529e4",
  "tool_use_result": {
    "query": "OpenVLA-OFT architecture action head MLP continuous action chunking parallel decoding details",
    "results": [
      {
        "tool_use_id": "srvtoolu_013JofqwPpt5VWE88acMVcKo",
        "content": [
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v1"
          },
          {
            "title": "OpenVLA-OFT+ on the bimanual ALOHA robot. Our Optimized Fine-Tuning... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/OpenVLA-OFT-on-the-bimanual-ALOHA-robot-Our-Optimized-Fine-Tuning-OFT-recipe-enhances_fig1_389399234"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2502.19645"
          },
          {
            "title": "[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"
          },
          {
            "title": "BitVLA: 1-bit Vision-Language-Action Models for Robotics ...",
            "url": "https://arxiv.org/pdf/2506.07530"
          },
          {
            "title": "(PDF) Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://www.researchgate.net/publication/389399234_Fine-Tuning_Vision-Language-Action_Models_Optimizing_Speed_and_Success"
          },
          {
            "title": "OpenVLA-OFT",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "[Literature Review] BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation",
            "url": "https://www.themoonlight.io/en/review/bitvla-1-bit-vision-language-action-models-for-robotics-manipulation"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/pdf/2502.19645"
          }
        ]
      },
      "Based on the search results, here are the detailed architectural components of OpenVLA-OFT:\n\n## Action Head Architecture\n\nThe MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions. The MLP-based action head projects the latent representations of query tokens into continuous robotic action space.\n\n## Continuous Action Representation\n\nWith continuous action representation, the VLA can directly model the action distribution without lossy discretization, as opposed to the baseline OpenVLA which uses discrete action tokens where each action dimension is normalized to [-1,+1] and uniformly discretized into 256 bins, with the discretization process sacrificing fine-grained action details.\n\n## Parallel Decoding\n\nThe model architecture is modified to accept empty action embeddings as inputs, removing the necessity for a causal attention mask, and instead implementing bidirectional attention. Empty action embeddings differ only in their positional encoding values.\n\n## Action Chunking\n\nThe model predicts sequences of K future actions rather than single timesteps, and for the ALOHA robot experiments, K=25 actions are predicted simultaneously, dramatically increasing throughput while maintaining low latency. Adding action chunking with K=8 increases latency by 17% due to longer attention sequences in the decoder, but when combined with parallel decoding, it dramatically improves throughput, achieving a 26x speedup over baseline OpenVLA.\n\n## Overall Performance\n\nThrough parallel decoding and action chunking, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model."
    ],
    "durationSeconds": 7.820714549000004
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Good, I'm getting a clearer picture. Let me now search for more specific details:
1. The observation features dimension from the Llama backbone
2. Per-suite LIBERO scores from the paper
3. Action space details (normalization, 7D action)
4. Temperature/sampling mechanism for continuous actions

Let me read the arxiv paper for more details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "d27a5a3a-bc1f-4d20-a88f-cadddafc1bc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011N2EAwrpKb1LHGrZ49A2RW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1461,
      "cache_creation_input_tokens": 2155,
      "cache_read_input_tokens": 26921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2155
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

需要更多细节，搜索论文中的具体数值和采样机制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "2f9cee62-a052-415d-a16a-56078d2bc47e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011N2EAwrpKb1LHGrZ49A2RW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1461,
      "cache_creation_input_tokens": 2155,
      "cache_read_input_tokens": 26921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2155
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NohLhBe6DGof3VG2iXhjDh`</summary>

```json
{
  "query": "OpenVLA-OFT arxiv 2502.19645 LIBERO-Spatial LIBERO-Object LIBERO-Goal LIBERO-Long success rate table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "6ce4a406-49a8-4027-823e-b8eba014d14b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011N2EAwrpKb1LHGrZ49A2RW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1461,
      "cache_creation_input_tokens": 2155,
      "cache_read_input_tokens": 26921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2155
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015BWZgLCRzuDs6QFZsckzs6`</summary>

```json
{
  "query": "OpenVLA hidden dimension Llama backbone 4096 observation features extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "def1e825-0a78-475f-b455-3625618b5adf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011N2EAwrpKb1LHGrZ49A2RW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1461,
      "cache_creation_input_tokens": 2155,
      "cache_read_input_tokens": 26921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2155
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

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LTnPdRaoVfrhSFDdKAi1zN`</summary>

```json
{
  "query": "OpenVLA-OFT action space normalization 7 dimensions continuous L1 regression sampling stochastic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "56137fd1-a5cb-4a9a-9781-4c6f3c667cb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011N2EAwrpKb1LHGrZ49A2RW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1461,
      "cache_creation_input_tokens": 2155,
      "cache_read_input_tokens": 26921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2155
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

_source line 31 · 2026-05-22T05:03:20.732Z_

<details><summary>↩ Tool result · `toolu_01NohLhBe6DGof3VG2iXhjDh`</summary>

```text
Web search results for query: "OpenVLA-OFT arxiv 2502.19645 LIBERO-Spatial LIBERO-Object LIBERO-Goal LIBERO-Long success rate table"

Links: [{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"[2502.19645v1] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Open-source OpenVLA-7B-OFT optimized visual-language-action model, specifically designed to improve the execution speed and success rate of robot tasks","url":"https://model.aibase.com/models/details/1935154868323094528"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"The OpenVLA-OFT Vision-Language-Action Model is open-sourced! Fine-tuning optimization enhances speed and success rate.","url":"https://model.aibase.com/models/details/1935154868167905280"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"}]

Based on the search results, I found information about OpenVLA-OFT from arxiv 2502.19645. However, the specific detailed success rate table you're looking for with individual results for LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long is not fully displayed in these search results.

From the available information:

OpenVLA-OFT boosted OpenVLA's average success rate across four task suites from 76.5% to 97.1%, and OpenVLA-OFT was evaluated in four LIBERO simulation benchmark task suites, measuring task success rates with and without additional inputs (wrist camera image and proprioceptive state).

To access the specific success rate table breaking down results for each of the four LIBERO task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long), you would need to consult the full paper directly at the arxiv link (https://arxiv.org/abs/2502.19645) or the project website at https://openvla-oft.github.io/, as these detailed tables are not reproduced in the search results I retrieved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "20a18cdd-94e4-4dd3-b8d3-a410515dfb30",
  "tool_use_result": {
    "query": "OpenVLA-OFT arxiv 2502.19645 LIBERO-Spatial LIBERO-Object LIBERO-Goal LIBERO-Long success rate table",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P8tFc9QC2jGGe1C6wtyjaZ",
        "content": [
          {
            "title": "[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/abs/2502.19645"
          },
          {
            "title": "[2502.19645v1] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/abs/2502.19645v1"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v1"
          },
          {
            "title": "Open-source OpenVLA-7B-OFT optimized visual-language-action model, specifically designed to improve the execution speed and success rate of robot tasks",
            "url": "https://model.aibase.com/models/details/1935154868323094528"
          },
          {
            "title": "OpenVLA-OFT",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"
          },
          {
            "title": "The OpenVLA-OFT Vision-Language-Action Model is open-sourced! Fine-tuning optimization enhances speed and success rate.",
            "url": "https://model.aibase.com/models/details/1935154868167905280"
          },
          {
            "title": "Training Data for OpenVLA | Data Requirements & Formats | Claru",
            "url": "https://claru.ai/models/openvla"
          },
          {
            "title": "GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub",
            "url": "https://github.com/moojink/openvla-oft"
          }
        ]
      },
      "Based on the search results, I found information about OpenVLA-OFT from arxiv 2502.19645. However, the specific detailed success rate table you're looking for with individual results for LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long is not fully displayed in these search results.\n\nFrom the available information:\n\nOpenVLA-OFT boosted OpenVLA's average success rate across four task suites from 76.5% to 97.1%, and OpenVLA-OFT was evaluated in four LIBERO simulation benchmark task suites, measuring task success rates with and without additional inputs (wrist camera image and proprioceptive state).\n\nTo access the specific success rate table breaking down results for each of the four LIBERO task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long), you would need to consult the full paper directly at the arxiv link (https://arxiv.org/abs/2502.19645) or the project website at https://openvla-oft.github.io/, as these detailed tables are not reproduced in the search results I retrieved."
    ],
    "durationSeconds": 5.582353372000005
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T05:03:21.632Z_

<details><summary>↩ Tool result · `toolu_015BWZgLCRzuDs6QFZsckzs6`</summary>

```text
Web search results for query: "OpenVLA hidden dimension Llama backbone 4096 observation features extraction"

Links: [{"title":"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture","url":"https://arxiv.org/html/2502.04558v1"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"},{"title":"OpenVLA-7B Vision-Language-Action Framework","url":"https://www.emergentmind.com/topics/openvla-7b-framework"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v2"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Probing a Vision-Language-Action Model for Symbolic States and   Integration into a Cognitive Architecture","url":"https://arxiv.org/pdf/2502.04558"},{"title":"Paper notes: OpenVLA. With the large-scale accessibility of… | by Jay Vakil | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/paper-notes-openvla-17540381187e"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"}]

Based on the search results, here's what I found about OpenVLA's hidden dimension and observation features extraction:

## Hidden Dimension

Each hidden-layer embedding in OpenVLA's Llama backbone is a 4096-dimensional vector. OpenVLA uses a Llama 2 7B backbone which consists of 32 transformer blocks plus an initial embedding layer, yielding 33 distinct hidden states when indexed from 0 to 32 at runtime, with each hidden state being a 4096-dimensional vector.

## Observation Features Extraction

OpenVLA's model consists of three key elements: (1) a fused visual encoder consisting of SigLIP and DinoV2 backbones that maps image inputs to image patch embeddings, (2) a projector that maps the visual encoder output embeddings into the input space of a large language model, and (3) a Llama 2 7B language model backbone that predicts tokenized output actions.

For image patches, each is embedded by both visual networks and concatenated, then a 2-layer MLP projects the concatenated vision features (approximately 4096 dimensions) to match the LLM's token embedding dimension.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "b93b1d4d-a7f4-4a71-b9ca-0504fc610f4b",
  "tool_use_result": {
    "query": "OpenVLA hidden dimension Llama backbone 4096 observation features extraction",
    "results": [
      {
        "tool_use_id": "srvtoolu_013jaUUPXkbGLTxB9L2npgx9",
        "content": [
          {
            "title": "Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture",
            "url": "https://arxiv.org/html/2502.04558v1"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "Understanding OpenVLA: A Simple Guide - Hankyu Kim",
            "url": "https://hankyukim.com/openvla/"
          },
          {
            "title": "OpenVLA-7B Vision-Language-Action Framework",
            "url": "https://www.emergentmind.com/topics/openvla-7b-framework"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2406.09246v2"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "Probing a Vision-Language-Action Model for Symbolic States and   Integration into a Cognitive Architecture",
            "url": "https://arxiv.org/pdf/2502.04558"
          },
          {
            "title": "Paper notes: OpenVLA. With the large-scale accessibility of… | by Jay Vakil | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/paper-notes-openvla-17540381187e"
          },
          {
            "title": "GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/reazon-research/openvla"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA's hidden dimension and observation features extraction:\n\n## Hidden Dimension\n\nEach hidden-layer embedding in OpenVLA's Llama backbone is a 4096-dimensional vector. OpenVLA uses a Llama 2 7B backbone which consists of 32 transformer blocks plus an initial embedding layer, yielding 33 distinct hidden states when indexed from 0 to 32 at runtime, with each hidden state being a 4096-dimensional vector.\n\n## Observation Features Extraction\n\nOpenVLA's model consists of three key elements: (1) a fused visual encoder consisting of SigLIP and DinoV2 backbones that maps image inputs to image patch embeddings, (2) a projector that maps the visual encoder output embeddings into the input space of a large language model, and (3) a Llama 2 7B language model backbone that predicts tokenized output actions.\n\nFor image patches, each is embedded by both visual networks and concatenated, then a 2-layer MLP projects the concatenated vision features (approximately 4096 dimensions) to match the LLM's token embedding dimension."
    ],
    "durationSeconds": 6.311371820000001
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T05:03:22.108Z_

<details><summary>↩ Tool result · `toolu_01LTnPdRaoVfrhSFDdKAi1zN`</summary>

```text
Web search results for query: "OpenVLA-OFT action space normalization 7 dimensions continuous L1 regression sampling stochastic"

Links: [{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"},{"title":"README.md · moojink/openvla-7b-oft-finetuned-libero-10 at main","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10/blob/main/README.md"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"}]

I found comprehensive information about OpenVLA-OFT's action space normalization and related technical details. Here's what the search results reveal:

## Action Space Normalization

OpenVLA delivers datasets with correctly normalized 7-DoF action vectors, and the original OpenVLA uses discrete action tokens where each action dimension is normalized to [-1, +1] and uniformly discretized into 256 bins.

## Continuous Action Representation with L1 Regression

OpenVLA-OFT implements L1 regression by replacing the decoder's output embedding layer with an MLP action head that directly maps final decoder layer hidden states to continuous action values, maintaining efficiency benefits of parallel decoding while potentially improving action precision.

For teams running OpenVLA-OFT's optimized fine-tuning recipe, continuous (un-discretized) action labels are delivered compatible with the L1 regression objective and parallel decoding setup.

## Training Convergence

Models are trained to minimize the mean L1 loss between predicted and ground-truth normalized actions (scaled between [-1, +1]) until it falls below 0.01.

## Overall OFT Recipe

The Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to improve inference efficiency, policy performance, and flexibility. OpenVLA-OFT achieves 97.1% average success rate on LIBERO while increasing action generation throughput by 26×.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "29c0eb02-e41c-4057-b83c-2590171eb297",
  "tool_use_result": {
    "query": "OpenVLA-OFT action space normalization 7 dimensions continuous L1 regression sampling stochastic",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VV4RjWEVEd9TEeVYxGzUGq",
        "content": [
          {
            "title": "Training Data for OpenVLA | Data Requirements & Formats | Claru",
            "url": "https://claru.ai/models/openvla"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v1"
          },
          {
            "title": "GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub",
            "url": "https://github.com/moojink/openvla-oft"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/pdf/2502.19645"
          },
          {
            "title": "[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"
          },
          {
            "title": "README.md · moojink/openvla-7b-oft-finetuned-libero-10 at main",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10/blob/main/README.md"
          },
          {
            "title": "OpenVLA-OFT",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/abs/2502.19645"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2502.19645"
          }
        ]
      },
      "I found comprehensive information about OpenVLA-OFT's action space normalization and related technical details. Here's what the search results reveal:\n\n## Action Space Normalization\n\nOpenVLA delivers datasets with correctly normalized 7-DoF action vectors, and the original OpenVLA uses discrete action tokens where each action dimension is normalized to [-1, +1] and uniformly discretized into 256 bins.\n\n## Continuous Action Representation with L1 Regression\n\nOpenVLA-OFT implements L1 regression by replacing the decoder's output embedding layer with an MLP action head that directly maps final decoder layer hidden states to continuous action values, maintaining efficiency benefits of parallel decoding while potentially improving action precision.\n\nFor teams running OpenVLA-OFT's optimized fine-tuning recipe, continuous (un-discretized) action labels are delivered compatible with the L1 regression objective and parallel decoding setup.\n\n## Training Convergence\n\nModels are trained to minimize the mean L1 loss between predicted and ground-truth normalized actions (scaled between [-1, +1]) until it falls below 0.01.\n\n## Overall OFT Recipe\n\nThe Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to improve inference efficiency, policy performance, and flexibility. OpenVLA-OFT achieves 97.1% average success rate on LIBERO while increasing action generation throughput by 26×."
    ],
    "durationSeconds": 6.645672596999997
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now I have a pretty complete picture. Let me also try to get the per-suite LIBERO scores by reading the paper HTML page, and clarify the sampling mechanism (since OFT uses L1 regression, it's deterministic - no built-in stochasticity unlike flow matching). Let me also check the GitHub repo for the code structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "ab12761e-e2a6-4371-a208-4b4d0d447a71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgW1aNz1LrBMdD3CVL2UU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4163,
      "cache_read_input_tokens": 29076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4163
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

_source line 35_

读取论文页面获取分项成绩，并搜索 GitHub 代码中的采样和 action head 细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "b7579025-9093-401b-957a-d89eb2eaf950",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgW1aNz1LrBMdD3CVL2UU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4163,
      "cache_read_input_tokens": 29076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4163
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QtmFoDHAz3uFxnvaEjFsYd`</summary>

```json
{
  "query": "select:WebFetch",
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
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "0650a472-e480-401f-8ccc-0759b7095757",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgW1aNz1LrBMdD3CVL2UU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4163,
      "cache_read_input_tokens": 29076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4163
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

_source line 37 · 2026-05-22T05:03:30.567Z_

<details><summary>↩ Tool result · `toolu_01QtmFoDHAz3uFxnvaEjFsYd`</summary>

````text
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
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "84159dde-971c-49ef-b483-ff3c8d9deeb3",
  "tool_use_result": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FE9P1d39AC6FS4ySpp3Hmz`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645v1",
  "prompt": "Extract the following specific information:\n1. LIBERO per-suite success rates: what are the exact success rates for LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long for OpenVLA-OFT?\n2. Action chunk size K used for LIBERO experiments\n3. Action dimensions (7D? what are they - delta xyz, delta rotation, gripper?)\n4. Is the model deterministic (L1 regression) or stochastic? Any mention of temperature sampling or adding noise for diversity?\n5. The MLP action head architecture details (input dimension, hidden dimension, output dimension, number of layers)\n6. Vision backbone output dimension / hidden state dimension from Llama decoder\n7. Any mention of how to extract intermediate features or hidden states"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "24a0f47c-42c9-4039-b831-7ead9e56b56f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPfzNBa6fu1hXAQdZixKoH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 33239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
      },
      "output_tokens": 45,
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

_source line 39_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013wW1hXpiSMRn4q79MPAgAM`</summary>

```json
{
  "url": "https://github.com/moojink/openvla-oft",
  "prompt": "Extract:\n1. Repository structure - what are the main directories and files?\n2. How is the action head defined? Look for MLP action head class definition details.\n3. How is inference done? Is there any temperature parameter or stochastic sampling?\n4. What is the action chunk size K for LIBERO?\n5. How are actions normalized?\n6. How to load the model for inference - what functions/classes are used?\n7. Any mention of extracting hidden states or intermediate features from the model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "9c597ca8-c80a-4ed8-ae7c-8db2790a37f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPfzNBa6fu1hXAQdZixKoH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 33239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
      },
      "output_tokens": 45,
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

_source line 40 · 2026-05-22T05:03:48.421Z_

<details><summary>↩ Tool result · `toolu_01FE9P1d39AC6FS4ySpp3Hmz`</summary>

```text
# OpenVLA-OFT Technical Specifications

## 1. LIBERO Success Rates (OpenVLA-OFT)

Per the paper's Table I, OpenVLA-OFT achieved these results:
- **LIBERO-Spatial**: 97.6%
- **LIBERO-Object**: 98.4%
- **LIBERO-Goal**: 97.9%
- **LIBERO-Long**: 94.5%
- **Average**: 97.1%

## 2. Action Chunk Size for LIBERO

The document states: "we set chunk size to K=8 to match the Diffusion Policy baseline" for LIBERO experiments.

## 3. Action Dimensions

The model predicts 7-dimensional actions representing "3 for position control, 3 for orientation control, and 1 for gripper control." These are delta end-effector pose actions in the original formulation.

## 4. Determinism and Sampling

The approach is **deterministic**. The paper describes using "L1 regression" which directly predicts continuous action values without stochastic sampling or temperature-based diversity mechanisms mentioned in the provided content.

## 5. MLP Action Head Architecture

For continuous actions: "the final hidden states are instead mapped directly to normalized continuous actions by a separate action head MLP." The appendix specifies a "4-layer MLP (ReLU activation)" for the action head, though exact dimensions aren't explicitly stated in the excerpt.

## 6. Vision and Language Dimensions

The document indicates "256 patch embeddings per view" from the dual vision encoders. The underlying model is Llama-2 7B, though specific hidden state dimensions aren't detailed in the provided sections.

## 7. Feature Extraction

No explicit mechanism for extracting intermediate hidden states is described in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "3781845e-eb0d-4bac-91a3-73690260304d",
  "tool_use_result": {
    "bytes": 338314,
    "code": 200,
    "codeText": "OK",
    "result": "# OpenVLA-OFT Technical Specifications\n\n## 1. LIBERO Success Rates (OpenVLA-OFT)\n\nPer the paper's Table I, OpenVLA-OFT achieved these results:\n- **LIBERO-Spatial**: 97.6%\n- **LIBERO-Object**: 98.4%\n- **LIBERO-Goal**: 97.9%\n- **LIBERO-Long**: 94.5%\n- **Average**: 97.1%\n\n## 2. Action Chunk Size for LIBERO\n\nThe document states: \"we set chunk size to K=8 to match the Diffusion Policy baseline\" for LIBERO experiments.\n\n## 3. Action Dimensions\n\nThe model predicts 7-dimensional actions representing \"3 for position control, 3 for orientation control, and 1 for gripper control.\" These are delta end-effector pose actions in the original formulation.\n\n## 4. Determinism and Sampling\n\nThe approach is **deterministic**. The paper describes using \"L1 regression\" which directly predicts continuous action values without stochastic sampling or temperature-based diversity mechanisms mentioned in the provided content.\n\n## 5. MLP Action Head Architecture\n\nFor continuous actions: \"the final hidden states are instead mapped directly to normalized continuous actions by a separate action head MLP.\" The appendix specifies a \"4-layer MLP (ReLU activation)\" for the action head, though exact dimensions aren't explicitly stated in the excerpt.\n\n## 6. Vision and Language Dimensions\n\nThe document indicates \"256 patch embeddings per view\" from the dual vision encoders. The underlying model is Llama-2 7B, though specific hidden state dimensions aren't detailed in the provided sections.\n\n## 7. Feature Extraction\n\nNo explicit mechanism for extracting intermediate hidden states is described in the provided content.",
    "durationMs": 6305,
    "url": "https://arxiv.org/html/2502.19645v1"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T05:03:48.791Z_

<details><summary>↩ Tool result · `toolu_013wW1hXpiSMRn4q79MPAgAM`</summary>

```text
# OpenVLA-OFT Repository Analysis

## 1. Repository Structure
The main directories include:
- `experiments/robot/` - contains evaluation scripts and configurations
- `prismatic/` - core VLA implementation
- `vla-scripts/` - utility scripts
- `scripts/extern/` - external dependencies

Key files: `LIBERO.md`, `ALOHA.md`, `SETUP.md`, and `pyproject.toml` for configuration.

## 2. Action Head Definition
The document references "MLP action head to generate continuous actions (via L1 regression)" but does not provide the class definition or implementation details. It's loaded via the `get_action_head()` function with parameters for `llm_dim`.

## 3. Inference Process
The quick start shows deterministic inference: "Generate robot action chunk (sequence of future actions)". No temperature parameter or stochastic sampling is mentioned in the provided content.

## 4. Action Chunk Size for LIBERO
The constant `NUM_ACTIONS_CHUNK` is referenced from `prismatic.vla.constants`, but its specific value is not disclosed in this excerpt.

## 5. Action Normalization
The configuration includes an `unnorm_key` parameter set to `"libero_spatial_no_noops"`, suggesting denormalization post-processing, but normalization methodology is not detailed.

## 6. Model Loading for Inference
Primary functions listed: `get_vla()`, `get_processor()`, `get_action_head()`, and `get_proprio_projector()`. These are imported from `experiments.robot.openvla_utils`.

## 7. Hidden States/Intermediate Features
No mention of extracting hidden states or intermediate features appears in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "9fa55ad7-cfdd-441a-9266-440dd4519926",
  "tool_use_result": {
    "bytes": 303686,
    "code": 200,
    "codeText": "OK",
    "result": "# OpenVLA-OFT Repository Analysis\n\n## 1. Repository Structure\nThe main directories include:\n- `experiments/robot/` - contains evaluation scripts and configurations\n- `prismatic/` - core VLA implementation\n- `vla-scripts/` - utility scripts\n- `scripts/extern/` - external dependencies\n\nKey files: `LIBERO.md`, `ALOHA.md`, `SETUP.md`, and `pyproject.toml` for configuration.\n\n## 2. Action Head Definition\nThe document references \"MLP action head to generate continuous actions (via L1 regression)\" but does not provide the class definition or implementation details. It's loaded via the `get_action_head()` function with parameters for `llm_dim`.\n\n## 3. Inference Process\nThe quick start shows deterministic inference: \"Generate robot action chunk (sequence of future actions)\". No temperature parameter or stochastic sampling is mentioned in the provided content.\n\n## 4. Action Chunk Size for LIBERO\nThe constant `NUM_ACTIONS_CHUNK` is referenced from `prismatic.vla.constants`, but its specific value is not disclosed in this excerpt.\n\n## 5. Action Normalization\nThe configuration includes an `unnorm_key` parameter set to `\"libero_spatial_no_noops\"`, suggesting denormalization post-processing, but normalization methodology is not detailed.\n\n## 6. Model Loading for Inference\nPrimary functions listed: `get_vla()`, `get_processor()`, `get_action_head()`, and `get_proprio_projector()`. These are imported from `experiments.robot.openvla_utils`.\n\n## 7. Hidden States/Intermediate Features\nNo mention of extracting hidden states or intermediate features appears in the provided content.",
    "durationMs": 6622,
    "url": "https://github.com/moojink/openvla-oft"
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check the GitHub repo for more details on the action head architecture, particularly the MLP dimensions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "da414d1d-998f-49fa-9f27-ed64a8ee2f7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YG8nmHTzavK1tAdMUCPb8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1327,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1327
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

_source line 43_

核心数据都有了。再补充确认 Llama-2 7B 的 hidden dimension 和 action head 细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "22f2ce9c-f148-4b11-8805-8e775b9a4dcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YG8nmHTzavK1tAdMUCPb8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1327,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1327
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

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013awfShFCpAVmWbDWhr3YX9`</summary>

```json
{
  "query": "Llama 2 7B hidden dimension 4096 model architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "0b60753e-50ca-43aa-8ef4-96f491184f43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YG8nmHTzavK1tAdMUCPb8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1327,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1327
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WpyNtJAsb7RjpGLMNcYVyM`</summary>

```json
{
  "query": "OpenVLA-OFT deterministic action prediction noise injection stochastic diversity candidates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "96b64220-c433-49ab-9177-97c3f5897362",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YG8nmHTzavK1tAdMUCPb8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1327,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1327
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

_source line 46 · 2026-05-22T05:03:58.816Z_

<details><summary>↩ Tool result · `toolu_01WpyNtJAsb7RjpGLMNcYVyM`</summary>

```text
Web search results for query: "OpenVLA-OFT deterministic action prediction noise injection stochastic diversity candidates"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges","url":"https://arxiv.org/html/2604.21391v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/pdf/2603.26666"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2602.20200"}]

Based on the search results, here's what I found about OpenVLA-OFT and related concepts:

## OpenVLA-OFT Overview

OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×.

The Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.

## Action Representation

OpenVLA originally uses discrete action tokens where each action dimension is normalized to [-1, +1] and uniformly discretized into 256 bins, though this approach can sacrifice fine-grained action details. OpenVLA-OFT uses continuous action representations instead to address this limitation.

## Related Concepts on Noise and Stochasticity

While the search results don't explicitly discuss "noise injection" and "stochastic diversity candidates" in OpenVLA-OFT specifically, I found relevant discussion in a related paper: Adaptive noise injection retains the model's exploratory power, preventing deterministic collapse and preserving generalization to novel tasks.

The search results focus primarily on OpenVLA-OFT's architectural improvements and performance gains rather than detailed mechanisms around noise injection for stochastic diversity in action prediction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "73bf051a-9470-4a6b-84a5-0cd07c0961d5",
  "tool_use_result": {
    "query": "OpenVLA-OFT deterministic action prediction noise injection stochastic diversity candidates",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HtAnnt1amdzXmwuEE9RWen",
        "content": [
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/pdf/2502.19645"
          },
          {
            "title": "From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges",
            "url": "https://arxiv.org/html/2604.21391v1"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2406.09246v3"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/pdf/2603.26666"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub",
            "url": "https://github.com/moojink/openvla-oft"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v1"
          },
          {
            "title": "[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/abs/2502.19645"
          },
          {
            "title": "Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2602.20200"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA-OFT and related concepts:\n\n## OpenVLA-OFT Overview\n\nOpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×.\n\nThe Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.\n\n## Action Representation\n\nOpenVLA originally uses discrete action tokens where each action dimension is normalized to [-1, +1] and uniformly discretized into 256 bins, though this approach can sacrifice fine-grained action details. OpenVLA-OFT uses continuous action representations instead to address this limitation.\n\n## Related Concepts on Noise and Stochasticity\n\nWhile the search results don't explicitly discuss \"noise injection\" and \"stochastic diversity candidates\" in OpenVLA-OFT specifically, I found relevant discussion in a related paper: Adaptive noise injection retains the model's exploratory power, preventing deterministic collapse and preserving generalization to novel tasks.\n\nThe search results focus primarily on OpenVLA-OFT's architectural improvements and performance gains rather than detailed mechanisms around noise injection for stochastic diversity in action prediction."
    ],
    "durationSeconds": 5.145594979000001
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-22T05:03:59.530Z_

<details><summary>↩ Tool result · `toolu_013awfShFCpAVmWbDWhr3YX9`</summary>

```text
Web search results for query: "Llama 2 7B hidden dimension 4096 model architecture"

Links: [{"title":"Llama 2 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/llama2"},{"title":"Llama · Hugging Face","url":"https://huggingface.co/docs/transformers/main/model_doc/llama"},{"title":"Llama2","url":"https://huggingface.co/docs/transformers/v4.31.0/en/model_doc/llama2"},{"title":"Introduction to Llama2 : Part-1 Architectural Analysis | by Utsavtiwari | Medium","url":"https://medium.com/@utsavtiwari9936/introduction-to-llama2-part-1-architectural-analysis-3e335e7b1104"},{"title":"Building and Quantizing Llama-2 from Scratch: Implementing a 7B Parameter Model with PyTorch | by Priyanthan Govindaraj | Medium","url":"https://medium.com/@govindarajpriyanthan/building-and-quantizing-llama-2-from-scratch-implementing-a-7b-parameter-model-with-pytorch-d9ce3f2c57ca"},{"title":"Gemma 2B vs Llama 3.2 vs Qwen 7B: Which Model Extracts Better?","url":"https://www.analyticsvidhya.com/blog/2025/01/gemma-2b-vs-llama-3-2-vs-qwen-7b/"},{"title":"LLaMA Architecture: Design Philosophy and Training Efficiency - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/llama-architecture-design-training-efficiency"},{"title":"Llama2-7B: Open-Source Transformer Insights","url":"https://www.emergentmind.com/topics/llama2-7b"},{"title":"Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers","url":"https://arxiv.org/html/2312.04333v4"},{"title":"Inference characteristics of Llama · Cursor","url":"https://cursor.com/blog/llama-inference"}]

Based on the search results, here's what I found about the Llama 2 7B model architecture with the 4096 hidden dimension:

## Key Architecture Parameters

The Llama 2 7B model consists of 32 transformer layers with a hidden embedding size of 4096. The intermediate size (MLP dimension) defaults to 11008.

Additional architectural details include:

- The model has 32 attention heads for each attention layer
- Vocabulary size of 32,000 tokens and a maximum position embeddings of 2048
- Each word-token is represented in a 4096-dimensional embedding vector, which is also called the hidden state size

## Core Components

The decoder blocks consist of RMSNorm, Multi-Head attention, and MLP layers, with the 7B model containing 32 decoder blocks. The Llama 2 architecture mostly keeps the same design as the original Llama, but it is pretrained on more tokens, doubles the context length, and uses grouped-query attention in the 70B model to improve inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "273af5e0-77d9-443e-aa99-8fee3c370b40",
  "tool_use_result": {
    "query": "Llama 2 7B hidden dimension 4096 model architecture",
    "results": [
      {
        "tool_use_id": "srvtoolu_013xV9bkESrowG6oLbJ4kFGA",
        "content": [
          {
            "title": "Llama 2 · Hugging Face",
            "url": "https://huggingface.co/docs/transformers/en/model_doc/llama2"
          },
          {
            "title": "Llama · Hugging Face",
            "url": "https://huggingface.co/docs/transformers/main/model_doc/llama"
          },
          {
            "title": "Llama2",
            "url": "https://huggingface.co/docs/transformers/v4.31.0/en/model_doc/llama2"
          },
          {
            "title": "Introduction to Llama2 : Part-1 Architectural Analysis | by Utsavtiwari | Medium",
            "url": "https://medium.com/@utsavtiwari9936/introduction-to-llama2-part-1-architectural-analysis-3e335e7b1104"
          },
          {
            "title": "Building and Quantizing Llama-2 from Scratch: Implementing a 7B Parameter Model with PyTorch | by Priyanthan Govindaraj | Medium",
            "url": "https://medium.com/@govindarajpriyanthan/building-and-quantizing-llama-2-from-scratch-implementing-a-7b-parameter-model-with-pytorch-d9ce3f2c57ca"
          },
          {
            "title": "Gemma 2B vs Llama 3.2 vs Qwen 7B: Which Model Extracts Better?",
            "url": "https://www.analyticsvidhya.com/blog/2025/01/gemma-2b-vs-llama-3-2-vs-qwen-7b/"
          },
          {
            "title": "LLaMA Architecture: Design Philosophy and Training Efficiency - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/llama-architecture-design-training-efficiency"
          },
          {
            "title": "Llama2-7B: Open-Source Transformer Insights",
            "url": "https://www.emergentmind.com/topics/llama2-7b"
          },
          {
            "title": "Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers",
            "url": "https://arxiv.org/html/2312.04333v4"
          },
          {
            "title": "Inference characteristics of Llama · Cursor",
            "url": "https://cursor.com/blog/llama-inference"
          }
        ]
      },
      "Based on the search results, here's what I found about the Llama 2 7B model architecture with the 4096 hidden dimension:\n\n## Key Architecture Parameters\n\nThe Llama 2 7B model consists of 32 transformer layers with a hidden embedding size of 4096. The intermediate size (MLP dimension) defaults to 11008.\n\nAdditional architectural details include:\n\n- The model has 32 attention heads for each attention layer\n- Vocabulary size of 32,000 tokens and a maximum position embeddings of 2048\n- Each word-token is represented in a 4096-dimensional embedding vector, which is also called the hidden state size\n\n## Core Components\n\nThe decoder blocks consist of RMSNorm, Multi-Head attention, and MLP layers, with the 7B model containing 32 decoder blocks. The Llama 2 architecture mostly keeps the same design as the original Llama, but it is pretrained on more tokens, doubles the context length, and uses grouped-query attention in the 70B model to improve inference."
    ],
    "durationSeconds": 6.310980316999994
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the report.

Key findings:
1. **OpenVLA-OFT** is NOT flow matching — it's L1 regression with continuous action outputs via an MLP action head. This is a critical difference from π0.5.
2. The model is **deterministic** — given the same input, it will produce the same action output. There's no built-in stochasticity (no temperature, no noise, no flow matching).
3. This is a major challenge for CRM pipeline because we need K diverse action candidates.


4. The architecture uses Llama-2 7B as the backbone with SigLIP and DinoV2 for vision encoding, feeding into a 4-layer MLP that outputs 7-dimensional normalized actions. The model runs on about 16GB of GPU memory in bf16 precision with a chunk size of 8 for LIBERO tasks.

5. LIBERO benchmarks show strong performance across all four suites—97.1% average with Spatial at 97.6%, Object at 98.4%, Goal at 97.9%, and Long-horizon at 94.5%—with fine-tuned checkpoints available on HuggingFace.

6. The main challenge for CRM adaptation is that the deterministic L1 regression approach doesn't naturally support sampling diverse action candidates like autoregressive or flow-based models do. I'm considering three approaches: injecting Gaussian noise into the MLP input, adding noise at intermediate feature layers, or training a separate flow/diffusion head on top of the frozen backbone, though the last option requires significant additional work.

7. I could also try MC Dropout at inference time for diversity, though it might not be sufficient, or fall back to the original discrete OpenVLA with temperature sampling—but that sacrifices the performance improvements from OFT.

8. The observation features are 4096-dimensional from the final Llama layer, which is substantially larger than SmolVLA's 960D or π0.5's 2048D, so the CRM input adapter would need to handle this higher dimensionality, potentially with a projection layer to compress it down.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "a9d01033-73e1-419a-a276-273693599d84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdPNeV4PA3JRLC3Rb2Laip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 835,
      "cache_creation_input_tokens": 1171,
      "cache_read_input_tokens": 35287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1171
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

_source line 49_

所有信息收集完毕，以下是调研报告。

---

## 1. 模型概况
- **论文**：*Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success* ([arXiv:2502.19645](https://arxiv.org/abs/2502.19645))
- **代码**：[github.com/moojink/openvla-oft](https://github.com/moojink/openvla-oft)
- **权重**：HuggingFace `moojink/openvla-7b-oft-finetuned-libero-{spatial,object,goal,10}`（每个 suite 一个 checkpoint）
- **架构**：**不是 flow matching**。基于 Llama-2 7B 骨干 + SigLIP/DinoV2 双视觉编码器，用 4 层 MLP action head 做 **L1 回归**，直接输出连续动作。核心改进是 parallel decoding + action chunking + 连续动作表示。
- **参数量**：~7B
- **显存需求**：推理 bf16 约 **15.9 GB**（单卡 A100/4090/3090 可跑）

## 2. Action Space
- **维度**：7D（3 position + 3 orientation + 1 gripper），delta end-effector pose
- **Chunk 长度**：LIBERO 实验 K=8
- **归一化**：每个维度归一化到 [-1, +1]，训练用 L1 loss（predicted vs ground-truth normalized actions，收敛到 loss < 0.01）
- **采样方式**：**完全确定性**。L1 回归直接输出均值预测，无 temperature、无随机噪声、无 flow steps。给定相同输入，输出完全相同。

## 3. LIBERO 性能
- **Fine-tuned checkpoint**：有，四个 suite 各一个
- **论文报告 SR**：
  - Spatial **97.6%**
  - Object **98.4%**
  - Goal **97.9%**
  - Long **94.5%**
  - Average **97.1%**（从原版 OpenVLA 76.5% 大幅提升）

## 4. CRM 适配评估

### Obs features 维度
- Llama-2 7B hidden dim = **4096D**（对比 SmolVLA 960D, π0.5 2048D）
- 提取位置：最后一层 Llama decoder 的 hidden states，输入 MLP action head 之前
- CRM 的 obs encoder 需新增 4096D → CRM latent 的适配层

### 核心困难：确定性模型无法采样多样 candidates

这是适配的**最大障碍**。CRM pipeline 需要 temperature > 0 采样 K 个 diverse action candidates，但 OpenVLA-OFT 是纯 L1 回归，**没有内置随机性机制**：

| VLA | 采样机制 | 多样性来源 |
|-----|----------|-----------|
| SmolVLA | autoregressive token decoding | temperature 控制 softmax |
| π0.5 | flow matching | 随机初始噪声 z₀ ~ N(0,I) |
| **OpenVLA-OFT** | L1 回归 MLP | **无** |

可能的 workaround（按可行性排序）：

1. **输入噪声注入**：在 MLP action head 的输入（4096D hidden state）上加高斯噪声 ε ~ N(0, σI)，σ 作为超参。简单但缺乏理论保障，噪声强度难调——太小无多样性，太大动作质量崩溃。
2. **MC Dropout**：推理时开启 Llama 层的 dropout，多次 forward 得到不同 hidden states。但 Llama-2 默认 dropout=0，需要 fine-tune 时加 dropout 或强行开启（效果不确定）。
3. **退回原版 OpenVLA（discrete tokens）**：原版 OpenVLA 用 256-bin 离散化 + autoregressive decoding，天然支持 temperature sampling。但性能只有 76.5% avg SR，且推理速度慢 26x。
4. **在 frozen backbone 上训练一个轻量 flow/diffusion head**：替换 MLP action head 为小型 flow matching head（类似 π0.5 的方式），既保留骨干特征又获得随机采样能力。工作量最大但最 principled。

### 其他适配工作项
- [ ] `get_vla()` / `get_action_head()` 接口适配，提取 hidden states 而非直接输出 action
- [ ] Action chunk 处理：CRM 需决定是对整个 8-step chunk 做 conformal prediction，还是只取第一步
- [ ] 归一化/反归一化对齐：确保 CRM correction delta 在 [-1,1] 归一化空间操作
- [ ] Obs feature 维度 4096D 比现有 VLA 大 2-4x，CRM 网络容量可能需调整

### 适配难度：**高**

核心原因是确定性 L1 回归与 CRM 需要的随机采样根本不兼容。SmolVLA 和 π0.5 都有天然随机性（token sampling / flow matching），适配只需调接口；OpenVLA-OFT 需要额外设计随机化方案，这本身就是一个研究问题。

### 预估工时
- 如果用 workaround 1（输入噪声注入）：**3-4 天**（接口适配 1 天 + 噪声方案调参 2-3 天）
- 如果用 workaround 4（训练 flow head）：**7-10 天**（设计+训练+调试）
- 建议：**暂缓适配**，优先完成 SmolVLA 和 π0.5 的 CRM 验证。如果确实需要第三个 VLA，噪声注入方案可作为 quick-and-dirty baseline 尝试。

---

Sources:
- [OpenVLA-OFT Paper (arXiv:2502.19645)](https://arxiv.org/abs/2502.19645)
- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)
- [OpenVLA-OFT Project Page](https://openvla-oft.github.io/)
- [HuggingFace: openvla-7b-oft-finetuned-libero-spatial](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial)
- [HuggingFace: openvla-7b-oft-finetuned-libero-object](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object)
- [HuggingFace: openvla-7b-oft-finetuned-libero-goal](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal)
- [HuggingFace: openvla-7b-oft-finetuned-libero-10](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "uuid": "2b770b3a-11e5-4c9e-ad7d-d5896393ea84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdPNeV4PA3JRLC3Rb2Laip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 835,
      "cache_creation_input_tokens": 1171,
      "cache_read_input_tokens": 35287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1171
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

_source line 50_

所有信息收集完毕，以下是调研报告。

---

## 1. 模型概况
- **论文**：*Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success* ([arXiv:2502.19645](https://arxiv.org/abs/2502.19645))
- **代码**：[github.com/moojink/openvla-oft](https://github.com/moojink/openvla-oft)
- **权重**：HuggingFace `moojink/openvla-7b-oft-finetuned-libero-{spatial,object,goal,10}`（每个 suite 一个 checkpoint）
- **架构**：**不是 flow matching**。基于 Llama-2 7B 骨干 + SigLIP/DinoV2 双视觉编码器，用 4 层 MLP action head 做 **L1 回归**，直接输出连续动作。核心改进是 parallel decoding + action chunking + 连续动作表示。
- **参数量**：~7B
- **显存需求**：推理 bf16 约 **15.9 GB**（单卡 A100/4090/3090 可跑）

## 2. Action Space
- **维度**：7D（3 position + 3 orientation + 1 gripper），delta end-effector pose
- **Chunk 长度**：LIBERO 实验 K=8
- **归一化**：每个维度归一化到 [-1, +1]，训练用 L1 loss（predicted vs ground-truth normalized actions，收敛到 loss < 0.01）
- **采样方式**：**完全确定性**。L1 回归直接输出均值预测，无 temperature、无随机噪声、无 flow steps。给定相同输入，输出完全相同。

## 3. LIBERO 性能
- **Fine-tuned checkpoint**：有，四个 suite 各一个
- **论文报告 SR**：
  - Spatial **97.6%**
  - Object **98.4%**
  - Goal **97.9%**
  - Long **94.5%**
  - Average **97.1%**（从原版 OpenVLA 76.5% 大幅提升）

## 4. CRM 适配评估

### Obs features 维度
- Llama-2 7B hidden dim = **4096D**（对比 SmolVLA 960D, π0.5 2048D）
- 提取位置：最后一层 Llama decoder 的 hidden states，输入 MLP action head 之前
- CRM 的 obs encoder 需新增 4096D → CRM latent 的适配层

### 核心困难：确定性模型无法采样多样 candidates

这是适配的**最大障碍**。CRM pipeline 需要 temperature > 0 采样 K 个 diverse action candidates，但 OpenVLA-OFT 是纯 L1 回归，**没有内置随机性机制**：

| VLA | 采样机制 | 多样性来源 |
|-----|----------|-----------|
| SmolVLA | autoregressive token decoding | temperature 控制 softmax |
| π0.5 | flow matching | 随机初始噪声 z₀ ~ N(0,I) |
| **OpenVLA-OFT** | L1 回归 MLP | **无** |

可能的 workaround（按可行性排序）：

1. **输入噪声注入**：在 MLP action head 的输入（4096D hidden state）上加高斯噪声 ε ~ N(0, σI)，σ 作为超参。简单但缺乏理论保障，噪声强度难调——太小无多样性，太大动作质量崩溃。
2. **MC Dropout**：推理时开启 Llama 层的 dropout，多次 forward 得到不同 hidden states。但 Llama-2 默认 dropout=0，需要 fine-tune 时加 dropout 或强行开启（效果不确定）。
3. **退回原版 OpenVLA（discrete tokens）**：原版 OpenVLA 用 256-bin 离散化 + autoregressive decoding，天然支持 temperature sampling。但性能只有 76.5% avg SR，且推理速度慢 26x。
4. **在 frozen backbone 上训练一个轻量 flow/diffusion head**：替换 MLP action head 为小型 flow matching head（类似 π0.5 的方式），既保留骨干特征又获得随机采样能力。工作量最大但最 principled。

### 其他适配工作项
- [ ] `get_vla()` / `get_action_head()` 接口适配，提取 hidden states 而非直接输出 action
- [ ] Action chunk 处理：CRM 需决定是对整个 8-step chunk 做 conformal prediction，还是只取第一步
- [ ] 归一化/反归一化对齐：确保 CRM correction delta 在 [-1,1] 归一化空间操作
- [ ] Obs feature 维度 4096D 比现有 VLA 大 2-4x，CRM 网络容量可能需调整

### 适配难度：**高**

核心原因是确定性 L1 回归与 CRM 需要的随机采样根本不兼容。SmolVLA 和 π0.5 都有天然随机性（token sampling / flow matching），适配只需调接口；OpenVLA-OFT 需要额外设计随机化方案，这本身就是一个研究问题。

### 预估工时
- 如果用 workaround 1（输入噪声注入）：**3-4 天**（接口适配 1 天 + 噪声方案调参 2-3 天）
- 如果用 workaround 4（训练 flow head）：**7-10 天**（设计+训练+调试）
- 建议：**暂缓适配**，优先完成 SmolVLA 和 π0.5 的 CRM 验证。如果确实需要第三个 VLA，噪声注入方案可作为 quick-and-dirty baseline 尝试。

---

Sources:
- [OpenVLA-OFT Paper (arXiv:2502.19645)](https://arxiv.org/abs/2502.19645)
- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)
- [OpenVLA-OFT Project Page](https://openvla-oft.github.io/)
- [HuggingFace: openvla-7b-oft-finetuned-libero-spatial](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial)
- [HuggingFace: openvla-7b-oft-finetuned-libero-object](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object)
- [HuggingFace: openvla-7b-oft-finetuned-libero-goal](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal)
- [HuggingFace: openvla-7b-oft-finetuned-libero-10](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 150574,
  "duration_api_ms": 211858,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "a048e076-e2b0-43c1-9ddf-0745b1053f08",
  "total_cost_usd": 0.7093272500000001,
  "usage": {
    "input_tokens": 3094,
    "cache_creation_input_tokens": 24617,
    "cache_read_input_tokens": 218474,
    "output_tokens": 4547,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24617,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 835,
        "output_tokens": 2708,
        "cache_read_input_tokens": 35287,
        "cache_creation_input_tokens": 1171,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1171
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-opus-4-6": {
      "inputTokens": 3094,
      "outputTokens": 4547,
      "cacheReadInputTokens": 218474,
      "cacheCreationInputTokens": 24617,
      "webSearchRequests": 0,
      "costUSD": 0.39223825,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-haiku-4-5-20251001": {
      "inputTokens": 167844,
      "outputTokens": 5849,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 12,
      "costUSD": 0.317089,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d43f5af0-6d66-4f94-b3d5-962932b47513"
}
```

</details>

---
