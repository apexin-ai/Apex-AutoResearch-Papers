# research corl2026 literature update

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_research_corl2026-literature-update_20260515T013205.log`
- **Structured JSON:** [`5dc52151dc96498bbcd4.json`](../../sessions/5d/5dc52151dc96498bbcd4.json)

## Before a recorded user message

44 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
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
  "uuid": "6478f49b-f7ee-4785-b9a1-4680a45dd1e2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778816400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "be3d163b-47f4-4ae0-8616-2382e461f5c3",
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do a literature search for their ACR-VLA project targeting CoRL 2026. I need to search for recent papers on VLA action correction, conformal prediction in robotics, and related topics. Let me use WebSearch to find relevant papers, then compile a report.

Let me start by loading the WebSearch tool and the MCP tools I'll need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "0609e7f1-c647-44c2-915e-b749ae911509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWxR7yF7xAhUHJYLLLKq28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11570,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11570
      },
      "output_tokens": 33,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CELW5oTf6AavU8KZFFqJZi`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
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
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "24909c43-0641-47f3-b586-f5f96e5b530c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWxR7yF7xAhUHJYLLLKq28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11570,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11570
      },
      "output_tokens": 33,
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

_source line 6 · 2026-05-15T01:32:19.596Z_

<details><summary>↩ Tool result · `toolu_01CELW5oTf6AavU8KZFFqJZi`</summary>

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
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "b178368e-2776-4865-94ee-adf4e3980d86",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
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
Now let me perform the web searches in parallel for the different keyword combinations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "feec5669-19f1-4b16-a594-325cdaa4763d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvoyAR3UuRedHkJGHKB7k5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
      },
      "output_tokens": 18,
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

开始搜索竞品文献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "8586728f-3226-4d19-b314-9b897863c0d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvoyAR3UuRedHkJGHKB7k5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013q2puVWJ1stECu6tUn44Sj`</summary>

```json
{
  "query": "VLA action correction sample selection uncertainty 2025 2026 robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "b7c95a1c-5f40-4343-aaa1-03b59a543eba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvoyAR3UuRedHkJGHKB7k5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014kAQdSSLjrJ81HD6npHB6q`</summary>

```json
{
  "query": "conformal prediction robotics manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "069e8c5f-bd3d-42e6-a875-33be7845c844",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvoyAR3UuRedHkJGHKB7k5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F3QuuFf5e9XCVmVJvC133Q`</summary>

```json
{
  "query": "ReconVLA SC-VLA VLA-Pilot action selection robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "a2687957-e0a4-4e33-89ca-95c1ddcbbd5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvoyAR3UuRedHkJGHKB7k5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_018mNYDxqzGSPTqxURrjDVjP`</summary>

```json
{
  "query": "flow matching VLA robot policy 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "12b5c3e6-f499-45b2-8ae8-7c178bce02b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvoyAR3UuRedHkJGHKB7k5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ADLaQuDNPTyHFgBRxSGJkM`</summary>

```json
{
  "query": "LIBERO benchmark robot manipulation 2025 2026 new results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "7a832176-ce07-401a-beda-18563aa8fba7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvoyAR3UuRedHkJGHKB7k5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
      },
      "output_tokens": 18,
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

_source line 14 · 2026-05-15T01:32:30.972Z_

<details><summary>↩ Tool result · `toolu_01F3QuuFf5e9XCVmVJvC133Q`</summary>

```text
Web search results for query: "ReconVLA SC-VLA VLA-Pilot action selection robot"

Links: [{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"GitHub - OpenHelix-Team/ReconVLA: Official implementation of ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver. · GitHub","url":"https://github.com/OpenHelix-Team/ReconVLA"},{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"[PDF] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReconVLA:-Reconstructive-Vision-Language-Action-as-Song-Zhou/c87ea2afcd9212e5128e01daf17c733d285ac345"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=K4FAFNRpko"}]

Based on the search results, here's what I found about these robotics models:

## ReconVLA

ReconVLA is a reconstructive VLA model with an implicit grounding paradigm. Current VLAs struggle to allocate visual attention to target regions, with visual attention always dispersed, so ReconVLA proposes to guide the visual attention grounding on the correct target. 

Conditioned on the model's visual outputs, a diffusion transformer aims to reconstruct the gaze region of the image, which corresponds to the target manipulated objects, prompting the VLA model to learn fine-grained representations and accurately allocate visual attention. The model was constructed with a large-scale robot pretraining dataset containing more than 100k trajectories and 2 million data samples, which enhances the model's generalization of visual reconstruction capabilities.

## SC-VLA (or other VLA variants)

The search results show many Vision-Language-Action (VLA) models exist, but "SC-VLA" and "VLA-Pilot" don't appear specifically in the search results. However, the results do indicate that various VLA models exist, including RoboFlamingo, VLAS, OpenVLA, and UniVLA.

If you're looking for information about specific models like "SC-VLA" or "VLA-Pilot," you may want to provide additional context or search for those names directly, as they don't appear in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "b01e5dbf-2aec-4c85-9d6d-3c4bf37157d4",
  "tool_use_result": {
    "query": "ReconVLA SC-VLA VLA-Pilot action selection robot",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BsarN71Xc1vHVP6HxPKA8z",
        "content": [
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/html/2508.10333v1"
          },
          {
            "title": "GitHub - OpenHelix-Team/ReconVLA: Official implementation of ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver. · GitHub",
            "url": "https://github.com/OpenHelix-Team/ReconVLA"
          },
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/abs/2508.10333"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "[PDF] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ReconVLA:-Reconstructive-Vision-Language-Action-as-Song-Zhou/c87ea2afcd9212e5128e01daf17c733d285ac345"
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
            "title": "VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=K4FAFNRpko"
          }
        ]
      },
      "Based on the search results, here's what I found about these robotics models:\n\n## ReconVLA\n\nReconVLA is a reconstructive VLA model with an implicit grounding paradigm. Current VLAs struggle to allocate visual attention to target regions, with visual attention always dispersed, so ReconVLA proposes to guide the visual attention grounding on the correct target. \n\nConditioned on the model's visual outputs, a diffusion transformer aims to reconstruct the gaze region of the image, which corresponds to the target manipulated objects, prompting the VLA model to learn fine-grained representations and accurately allocate visual attention. The model was constructed with a large-scale robot pretraining dataset containing more than 100k trajectories and 2 million data samples, which enhances the model's generalization of visual reconstruction capabilities.\n\n## SC-VLA (or other VLA variants)\n\nThe search results show many Vision-Language-Action (VLA) models exist, but \"SC-VLA\" and \"VLA-Pilot\" don't appear specifically in the search results. However, the results do indicate that various VLA models exist, including RoboFlamingo, VLAS, OpenVLA, and UniVLA.\n\nIf you're looking for information about specific models like \"SC-VLA\" or \"VLA-Pilot,\" you may want to provide additional context or search for those names directly, as they don't appear in these results."
    ],
    "durationSeconds": 6.435350121
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T01:32:31.162Z_

<details><summary>↩ Tool result · `toolu_014kAQdSSLjrJ81HD6npHB6q`</summary>

```text
Web search results for query: "conformal prediction robotics manipulation 2025 2026"

Links: [{"title":"Conformal Prediction for Robotics | xLAB: Safe Autonomous Systems Lab","url":"https://xlab.upenn.edu/conformal-prediction-robotics/"},{"title":"End-to-End Conformal Prediction for Trajectory Optimization | OpenReview","url":"https://openreview.net/forum?id=ilcsm8B7Pe"},{"title":"Formal Verification and Control With Conformal Prediction: Practical Safety Guarantees For Autonomous Systems | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/5488303/11274416/11274485.pdf"},{"title":"A Review of Theoretical Advances and Practical Applications of Conformal Prediction in China | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-15120-9_11"},{"title":"Conformal Prediction Conference 2026","url":"https://copa-conference.com/"},{"title":"Conformal Prediction Conference 2025","url":"https://copa-conference.com/copa2025/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Conformal prediction - Google Groups","url":"https://groups.google.com/g/conformal-prediction"},{"title":"What foundation models can bring for robot learning in manipulation: A survey - Dingzhe Li, Yixiang Jin, YuHao Sun, Yong A, Hongze Yu, Jun Shi, Xiaoshuai Hao, Peng Hao, Huaping Liu, Xiang Li, Xinde Li, Fuchun Sun, Jianwei Zhang, Bin Fang, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251390579"},{"title":"Extreme conformal prediction: Reliable intervals for high-impact events | Extremes | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10687-026-00536-9"}]

Here are the search results for "conformal prediction robotics manipulation 2025 2026":

## Key Findings

### Conformal Prediction for Robotics Applications

Research at the xLAB Safe Autonomous Systems Lab has developed multi-modal conformal prediction regions that are convex and can be easily incorporated into downstream tasks, such as motion planners. Recent research focuses on developing data-driven non-conformity scores that leverage machine learning models to better capture the underlying structure of robotic data.

### Research Directions and Challenges

A critical problem in applying conformal prediction to robotics is overcoming distribution shifts in multi-agent settings, where one agent's behavior can influence the environment and data distribution observed by other agents, requiring methods that can adapt to these shifts.

Recent work includes "AdaptNC: Adaptive Nonconformity Scores for Uncertainty-Aware Autonomous Systems in Dynamic Environments," listed as a preprint for 2026.

### Trajectory Optimization Applications

Conformal prediction is used to construct uncertainty sets with coverage guarantees for decision-making tasks such as trajectory optimization in uncertain environments. Researchers have proposed an End-to-End CP framework for shrinking-horizon trajectory optimization with joint risk constraints over mission time.

### Safety for Autonomous Systems

Conformal prediction research promises to enable future technologies such as autonomous driving, intelligent transportation, and robotics.

### Upcoming Conferences

The Conformal Prediction Conference 2026 is scheduled for September 2-4, 2026, with focus areas including applications across various domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "542f04d7-a8c0-4e9c-8162-451b372daf5f",
  "tool_use_result": {
    "query": "conformal prediction robotics manipulation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E4Rn3BC1ErWfzLkAKJZ1Up",
        "content": [
          {
            "title": "Conformal Prediction for Robotics | xLAB: Safe Autonomous Systems Lab",
            "url": "https://xlab.upenn.edu/conformal-prediction-robotics/"
          },
          {
            "title": "End-to-End Conformal Prediction for Trajectory Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=ilcsm8B7Pe"
          },
          {
            "title": "Formal Verification and Control With Conformal Prediction: Practical Safety Guarantees For Autonomous Systems | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/iel8/5488303/11274416/11274485.pdf"
          },
          {
            "title": "A Review of Theoretical Advances and Practical Applications of Conformal Prediction in China | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-15120-9_11"
          },
          {
            "title": "Conformal Prediction Conference 2026",
            "url": "https://copa-conference.com/"
          },
          {
            "title": "Conformal Prediction Conference 2025",
            "url": "https://copa-conference.com/copa2025/"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Conformal prediction - Google Groups",
            "url": "https://groups.google.com/g/conformal-prediction"
          },
          {
            "title": "What foundation models can bring for robot learning in manipulation: A survey - Dingzhe Li, Yixiang Jin, YuHao Sun, Yong A, Hongze Yu, Jun Shi, Xiaoshuai Hao, Peng Hao, Huaping Liu, Xiang Li, Xinde Li, Fuchun Sun, Jianwei Zhang, Bin Fang, 2025",
            "url": "https://journals.sagepub.com/doi/10.1177/02783649251390579"
          },
          {
            "title": "Extreme conformal prediction: Reliable intervals for high-impact events | Extremes | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10687-026-00536-9"
          }
        ]
      },
      "Here are the search results for \"conformal prediction robotics manipulation 2025 2026\":\n\n## Key Findings\n\n### Conformal Prediction for Robotics Applications\n\nResearch at the xLAB Safe Autonomous Systems Lab has developed multi-modal conformal prediction regions that are convex and can be easily incorporated into downstream tasks, such as motion planners. Recent research focuses on developing data-driven non-conformity scores that leverage machine learning models to better capture the underlying structure of robotic data.\n\n### Research Directions and Challenges\n\nA critical problem in applying conformal prediction to robotics is overcoming distribution shifts in multi-agent settings, where one agent's behavior can influence the environment and data distribution observed by other agents, requiring methods that can adapt to these shifts.\n\nRecent work includes \"AdaptNC: Adaptive Nonconformity Scores for Uncertainty-Aware Autonomous Systems in Dynamic Environments,\" listed as a preprint for 2026.\n\n### Trajectory Optimization Applications\n\nConformal prediction is used to construct uncertainty sets with coverage guarantees for decision-making tasks such as trajectory optimization in uncertain environments. Researchers have proposed an End-to-End CP framework for shrinking-horizon trajectory optimization with joint risk constraints over mission time.\n\n### Safety for Autonomous Systems\n\nConformal prediction research promises to enable future technologies such as autonomous driving, intelligent transportation, and robotics.\n\n### Upcoming Conferences\n\nThe Conformal Prediction Conference 2026 is scheduled for September 2-4, 2026, with focus areas including applications across various domains."
    ],
    "durationSeconds": 7.097213166999998
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T01:32:32.014Z_

<details><summary>↩ Tool result · `toolu_013q2puVWJ1stECu6tUn44Sj`</summary>

```text
Web search results for query: "VLA action correction sample selection uncertainty 2025 2026 robot manipulation"

Links: [{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095741742600655X"}]

I've completed a web search for your query about VLA (Vision-Language-Action) models with focus on action correction, sample selection, uncertainty, and robot manipulation research from 2025-2026.

The search results show significant recent developments in VLA research:

**Key Research Areas Found:**

VLA-OPD addresses epistemic uncertainty by using a bounded mode-seeking objective to ensure stable policy learning while maintaining action diversity, with experiments showing improved sample efficiency and robustness.

Recent work addresses the challenge of real-world uncertainty that makes it difficult for robot policies to anticipate action consequences, with vision-language-action policies emerging as a new paradigm.

**Failure Prediction and Correction:**

FPC-VLA proposes a pipeline with three modules: a robot failure dataset generation method, a VLM-based supervisor for failure prediction and correction, and a dual-stream action fusion module.

**Uncertainty-Driven Approaches:**

Recent work proposes an agentic VLA framework where LLM planners verify and re-plan actions using uncertainty-driven feedback for self-improving robotic autonomy.

**Sample Efficiency:**

VLAC (Vision-Language-Action-Critic) lifts manipulation success rates from about 30% to about 90% within 200 real-world interaction episodes.

The search results show active research into improving VLA models with better uncertainty handling, action correction mechanisms, and sample-efficient learning for robot manipulation tasks in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "b9b236dc-7863-4a4d-ae15-a137843ac44e",
  "tool_use_result": {
    "query": "VLA action correction sample selection uncertainty 2025 2026 robot manipulation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WSQY6Epu7jHC7rUDwdFfx8",
        "content": [
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666v1"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1566253525011248"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "2025-9-22 A Vision-Language-Action-Critic Model",
            "url": "https://arxiv.org/pdf/2509.15937"
          },
          {
            "title": "World Model for Robot Learning: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2605.00080"
          },
          {
            "title": "FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S095741742600655X"
          }
        ]
      },
      "I've completed a web search for your query about VLA (Vision-Language-Action) models with focus on action correction, sample selection, uncertainty, and robot manipulation research from 2025-2026.\n\nThe search results show significant recent developments in VLA research:\n\n**Key Research Areas Found:**\n\nVLA-OPD addresses epistemic uncertainty by using a bounded mode-seeking objective to ensure stable policy learning while maintaining action diversity, with experiments showing improved sample efficiency and robustness.\n\nRecent work addresses the challenge of real-world uncertainty that makes it difficult for robot policies to anticipate action consequences, with vision-language-action policies emerging as a new paradigm.\n\n**Failure Prediction and Correction:**\n\nFPC-VLA proposes a pipeline with three modules: a robot failure dataset generation method, a VLM-based supervisor for failure prediction and correction, and a dual-stream action fusion module.\n\n**Uncertainty-Driven Approaches:**\n\nRecent work proposes an agentic VLA framework where LLM planners verify and re-plan actions using uncertainty-driven feedback for self-improving robotic autonomy.\n\n**Sample Efficiency:**\n\nVLAC (Vision-Language-Action-Critic) lifts manipulation success rates from about 30% to about 90% within 200 real-world interaction episodes.\n\nThe search results show active research into improving VLA models with better uncertainty handling, action correction mechanisms, and sample-efficient learning for robot manipulation tasks in 2025-2026."
    ],
    "durationSeconds": 8.419169277000002
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T01:32:33.387Z_

<details><summary>↩ Tool result · `toolu_018mNYDxqzGSPTqxURrjDVjP`</summary>

```text
Web search results for query: "flow matching VLA robot policy 2025 2026"

Links: [{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"VLM, VLA, Diffusion Policy, Flow Matching in Robotics | by Ranko Mosic | Medium","url":"https://ranko-mosic.medium.com/vla-9bd14b1a23ee"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://www.pi.website/download/pi0.pdf"},{"title":"VLS: Steering Pretrained Robot Policies via Vision–Language Models","url":"https://arxiv.org/html/2602.03973v1"}]

Based on the search results, here's what I found regarding flow matching VLA robot policy in 2025-2026:

## Key Developments

**Flow Matching as a Core Technology:**
Flow matching is more effective at generating continuous actions, though it is slower to train than autoregressive architectures. Flow matching can result in faster inference than autoregressive prediction since we can predict a whole chunk at once.

**π0 and Physical Intelligence's Leadership:**
π0 (pi-zero) is a large-scale generalist VLA announced in late 2024 by the startup Physical Intelligence. π0 also introduced flow-matching model to generate high-frequency continuous actions, up to 50 Hz, while the action head takes advantage of a diffusion policy.

**Recent Advances (2025-2026):**
Physical Intelligence open sourced π family of models (π0.6 being the latest). A small team lead by Ilia Larchenko won NeurIPS 2025 robotics competition (beating NVIDIA team) using a modified version of π0.5.

**Other VLA Models Using Flow Matching:**
GR-3 unifies vision-language understanding with robot trajectory learning using flow-matching. GR00T N1, released by NVIDIA in March 2025, is a VLA for humanoid robots.

**Architectural Applications:**
π 0.5 from Physical Intelligence has their "System 2" output a set of discrete tokens, learned via the FAST action tokenizer, which are then inputs into the flow matching System 1 architecture.

Flow matching has become a dominant approach in 2025-2026 for enabling high-frequency, continuous robot control in Vision-Language-Action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "435e5441-420b-496d-bf31-b81526671aff",
  "tool_use_result": {
    "query": "flow matching VLA robot policy 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JBvSLxuMNz3GGiWEWJn7Ma",
        "content": [
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "VLM, VLA, Diffusion Policy, Flow Matching in Robotics | by Ranko Mosic | Medium",
            "url": "https://ranko-mosic.medium.com/vla-9bd14b1a23ee"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Vision-Language-Action Models and the Search for a Generalist Robot Policy",
            "url": "https://itcanthink.substack.com/p/vision-language-action-models-and"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2508.13073v1"
          },
          {
            "title": "π0: A Vision-Language-Action Flow Model for General Robot Control",
            "url": "https://www.pi.website/download/pi0.pdf"
          },
          {
            "title": "VLS: Steering Pretrained Robot Policies via Vision–Language Models",
            "url": "https://arxiv.org/html/2602.03973v1"
          }
        ]
      },
      "Based on the search results, here's what I found regarding flow matching VLA robot policy in 2025-2026:\n\n## Key Developments\n\n**Flow Matching as a Core Technology:**\nFlow matching is more effective at generating continuous actions, though it is slower to train than autoregressive architectures. Flow matching can result in faster inference than autoregressive prediction since we can predict a whole chunk at once.\n\n**π0 and Physical Intelligence's Leadership:**\nπ0 (pi-zero) is a large-scale generalist VLA announced in late 2024 by the startup Physical Intelligence. π0 also introduced flow-matching model to generate high-frequency continuous actions, up to 50 Hz, while the action head takes advantage of a diffusion policy.\n\n**Recent Advances (2025-2026):**\nPhysical Intelligence open sourced π family of models (π0.6 being the latest). A small team lead by Ilia Larchenko won NeurIPS 2025 robotics competition (beating NVIDIA team) using a modified version of π0.5.\n\n**Other VLA Models Using Flow Matching:**\nGR-3 unifies vision-language understanding with robot trajectory learning using flow-matching. GR00T N1, released by NVIDIA in March 2025, is a VLA for humanoid robots.\n\n**Architectural Applications:**\nπ 0.5 from Physical Intelligence has their \"System 2\" output a set of discrete tokens, learned via the FAST action tokenizer, which are then inputs into the flow matching System 1 architecture.\n\nFlow matching has become a dominant approach in 2025-2026 for enabling high-frequency, continuous robot control in Vision-Language-Action models."
    ],
    "durationSeconds": 8.341381659000003
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T01:32:33.641Z_

<details><summary>↩ Tool result · `toolu_01ADLaQuDNPTyHFgBRxSGJkM`</summary>

```text
Web search results for query: "LIBERO benchmark robot manipulation 2025 2026 new results"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"}]

Based on the web search results, here are the key findings on LIBERO benchmark robot manipulation results from 2025-2026:

## Recent Performance Results

Strong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically achieve 70-90% success on Spatial, Object, and Goal tasks, and 30-60% on LIBERO-100.

## 2025-2026 Developments

Several important extensions and analyses have emerged:

**LIBERO-Plus (October 2025):** Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

**LIBERO-PRO (October 2025):** Although existing models achieve over 90% accuracy under standard LIBERO evaluation, their performance collapses to 0.0% under generalized settings. Models exhibit near-complete failure under several perturbation settings: they cannot cope with changes in object positions, nor can they correctly follow slightly rephrased task instructions—findings reveal that commonly reported accuracies over 90% are largely artifacts of task memorization.

**Recent Innovations:**
- Slot-object architectures (SlotVLA) reduce perception cost by > 85%, enabling interpretable policy heads while matching dense-token models on object/goal/generalization (November 2025)
- RLinf-VLA demonstrates >1.6× throughput gains for parallelized training on LIBERO (October 2025)

## Key Insight

These findings challenge the assumption that high benchmark scores equate to true competency and highlight the need for evaluation practices that assess reliability under realistic variation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "21ead10a-64f8-47a6-a361-da59c2cd415e",
  "tool_use_result": {
    "query": "LIBERO benchmark robot manipulation 2025 2026 new results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gd8fPHF7GxdaSZgDM1Lz82",
        "content": [
          {
            "title": "GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub",
            "url": "https://github.com/Lifelong-Robot-Learning/LIBERO"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview",
            "url": "https://openreview.net/forum?id=xzEtNSuDJk"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
            "url": "https://arxiv.org/abs/2306.03310"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"
          }
        ]
      },
      "Based on the web search results, here are the key findings on LIBERO benchmark robot manipulation results from 2025-2026:\n\n## Recent Performance Results\n\nStrong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically achieve 70-90% success on Spatial, Object, and Goal tasks, and 30-60% on LIBERO-100.\n\n## 2025-2026 Developments\n\nSeveral important extensions and analyses have emerged:\n\n**LIBERO-Plus (October 2025):** Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\n**LIBERO-PRO (October 2025):** Although existing models achieve over 90% accuracy under standard LIBERO evaluation, their performance collapses to 0.0% under generalized settings. Models exhibit near-complete failure under several perturbation settings: they cannot cope with changes in object positions, nor can they correctly follow slightly rephrased task instructions—findings reveal that commonly reported accuracies over 90% are largely artifacts of task memorization.\n\n**Recent Innovations:**\n- Slot-object architectures (SlotVLA) reduce perception cost by > 85%, enabling interpretable policy heads while matching dense-token models on object/goal/generalization (November 2025)\n- RLinf-VLA demonstrates >1.6× throughput gains for parallelized training on LIBERO (October 2025)\n\n## Key Insight\n\nThese findings challenge the assumption that high benchmark scores equate to true competency and highlight the need for evaluation practices that assess reliability under realistic variation."
    ],
    "durationSeconds": 8.450988842
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Good, I found some interesting results. Let me search for more specific papers now - the uncertainty-aware ReconVLA paper (2604.16677), SC-VLA, VLA-Pilot, ACoT-VLA, and also some more specific topics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "1f2e414c-6ef1-466b-a029-34959f8bb022",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Abz8Lk9vBodEPgYzWZaQ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 24376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5135
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

找到第一批结果。注意到有一个新的 ReconVLA 论文（2604.16677）专门做 uncertainty-guided 的。继续深挖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "93358c81-b919-46a0-b97e-b0ab18852ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Abz8Lk9vBodEPgYzWZaQ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 24376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5135
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YZnv5d26SiwQNW15ZtAyFt`</summary>

```json
{
  "query": "arXiv 2604.16677 ReconVLA uncertainty-guided failure-aware"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "39fccb88-7040-43d1-ae58-d13607a1b9ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Abz8Lk9vBodEPgYzWZaQ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 24376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5135
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015woGt6spXP7nZm1PW1MCrh`</summary>

```json
{
  "query": "SC-VLA sample consensus vision language action model robot 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "77d33298-5016-4c1d-9a50-4a4b7fbba941",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Abz8Lk9vBodEPgYzWZaQ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 24376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5135
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014dgMAwYvYDvfMX7VFLVLuf`</summary>

```json
{
  "query": "ACoT-VLA action chain of thought VLA robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "3ff274a0-b7a5-417f-80b4-b634ecb6e44c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Abz8Lk9vBodEPgYzWZaQ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 24376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5135
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JMUkf35tUyZ3P3qsqLGDpq`</summary>

```json
{
  "query": "VLA-Pilot multi-sample selection robot manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "6352509a-ff22-4a72-a783-e76561d4b580",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Abz8Lk9vBodEPgYzWZaQ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 24376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5135
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FzSbLbkXMTbf4h6YgPLzDn`</summary>

```json
{
  "query": "VLAC vision language action critic robot manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "a0003fb0-f169-4dc0-b2fa-12aac9db3195",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Abz8Lk9vBodEPgYzWZaQ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 24376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5135
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

_source line 26 · 2026-05-15T01:32:49.346Z_

<details><summary>↩ Tool result · `toolu_01YZnv5d26SiwQNW15ZtAyFt`</summary>

```text
Web search results for query: "arXiv 2604.16677 ReconVLA uncertainty-guided failure-aware"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"Dyna-Style Safety Augmented Reinforcement Learning: Staying Safe in the Face of Uncertainty","url":"https://arxiv.org/html/2604.25508"},{"title":"Entropy-Guided Loop: Achieving Reasoning through Uncertainty-Aware Generation","url":"https://arxiv.org/html/2509.00079v1"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=25&show=2000"},{"title":"PiGGO: Physics-Guided Learnable Graph Kalman Filters for Virtual Sensing of Nonlinear Dynamic Structures under Uncertainty","url":"https://arxiv.org/html/2604.26593"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=550&show=2000"},{"title":"[2604.13352] A Machine Learning Framework for Uncertainty-Calibrated Capability Decision under Finite Samples","url":"https://arxiv.org/abs/2604.13352"},{"title":"Towards Reliable Truth-Aligned Uncertainty Estimation in Large Language Models","url":"https://arxiv.org/html/2604.00445"},{"title":"[2604.11036] Uncertainty-Aware Web-Conditioned Scientific Fact-Checking","url":"https://arxiv.org/abs/2604.11036"},{"title":"Uncertainty-aware Generative Learning Path Recommendation with Cognition-Adaptive Diffusion","url":"https://arxiv.org/html/2604.14613"}]

Based on the search results, I found the paper you're looking for:

**ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework** is a reliable conformal model that produces uncertainty-guided and failure-aware control signals.

Vision-language-action (VLA) models have emerged as generalist robotic controllers capable of mapping visual observations and natural language instructions to continuous action sequences, but VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated.

The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success, and extends conformal prediction to the robot state space to detect outliers or unsafe states before failures occur.

The paper was submitted to arXiv on April 17, 2026 (arXiv:2604.16677v1), and the authors are from The University of Texas at Arlington's Department of Computer Science and Engineering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "89e2ee7d-4446-4458-99d8-ab9f81c65e38",
  "tool_use_result": {
    "query": "arXiv 2604.16677 ReconVLA uncertainty-guided failure-aware",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xb5mD1Duzv65xeYpDfv8a7",
        "content": [
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "Dyna-Style Safety Augmented Reinforcement Learning: Staying Safe in the Face of Uncertainty",
            "url": "https://arxiv.org/html/2604.25508"
          },
          {
            "title": "Entropy-Guided Loop: Achieving Reasoning through Uncertainty-Aware Generation",
            "url": "https://arxiv.org/html/2509.00079v1"
          },
          {
            "title": "Machine Learning Jul 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-07?skip=25&show=2000"
          },
          {
            "title": "PiGGO: Physics-Guided Learnable Graph Kalman Filters for Virtual Sensing of Nonlinear Dynamic Structures under Uncertainty",
            "url": "https://arxiv.org/html/2604.26593"
          },
          {
            "title": "Machine Learning Sep 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-09?skip=550&show=2000"
          },
          {
            "title": "[2604.13352] A Machine Learning Framework for Uncertainty-Calibrated Capability Decision under Finite Samples",
            "url": "https://arxiv.org/abs/2604.13352"
          },
          {
            "title": "Towards Reliable Truth-Aligned Uncertainty Estimation in Large Language Models",
            "url": "https://arxiv.org/html/2604.00445"
          },
          {
            "title": "[2604.11036] Uncertainty-Aware Web-Conditioned Scientific Fact-Checking",
            "url": "https://arxiv.org/abs/2604.11036"
          },
          {
            "title": "Uncertainty-aware Generative Learning Path Recommendation with Cognition-Adaptive Diffusion",
            "url": "https://arxiv.org/html/2604.14613"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework** is a reliable conformal model that produces uncertainty-guided and failure-aware control signals.\n\nVision-language-action (VLA) models have emerged as generalist robotic controllers capable of mapping visual observations and natural language instructions to continuous action sequences, but VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated.\n\nThe approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success, and extends conformal prediction to the robot state space to detect outliers or unsafe states before failures occur.\n\nThe paper was submitted to arXiv on April 17, 2026 (arXiv:2604.16677v1), and the authors are from The University of Texas at Arlington's Department of Computer Science and Engineering."
    ],
    "durationSeconds": 6.723318389
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T01:32:50.196Z_

<details><summary>↩ Tool result · `toolu_01JMUkf35tUyZ3P3qsqLGDpq`</summary>

```text
Web search results for query: "VLA-Pilot multi-sample selection robot manipulation 2025"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"VLAbot: A human Vision–Language–Action models interaction framework for robotic assembly - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0736584526000475"},{"title":"Shake-VLA: Vision-Language-Action Model-Based System for Bimanual Robotic Manipulations and Liquid Mixing | Proceedings of the 2025 ACM/IEEE International Conference on Human-Robot Interaction","url":"https://dl.acm.org/doi/10.5555/3721488.3721686"}]

I've performed a web search for "VLA-Pilot multi-sample selection robot manipulation 2025". The search results show a rich landscape of Vision-Language-Action (VLA) models and research in robot manipulation from 2025, though I didn't find a specific project or paper explicitly titled "VLA-Pilot" focused on multi-sample selection.

However, the search results reveal relevant context about VLA research in 2025:

In 2025, there have been numerous VLA-related developments including models from Microsoft Research (OmniVLA), Physical Intelligence (π0.6), Nvidia (VLA-0), and others focused on robotic manipulation.

There has been a rapid acceleration in VLA model development, particularly in 2025, with a focus on vision-language-action models and related multimodal learning approaches for embodied AI and robot learning.

The broader context includes systems like Shake-VLA, a Vision-Language-Action model-based system designed for bimanual robotic manipulation, demonstrating various specialized applications of VLAs.

If you're looking for information about a specific "VLA-Pilot" project or paper on multi-sample selection, you may want to search for it on academic databases like arXiv, or provide additional context about the authors or institution involved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "96a6e240-57b4-4cb0-b70a-4529b37d0f79",
  "tool_use_result": {
    "query": "VLA-Pilot multi-sample selection robot manipulation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0178eHnrPv9W6Gtjf1hPfKfM",
        "content": [
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "LangForce: Bayesian Decomposition of Vision Language ...",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
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
            "title": "GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub",
            "url": "https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"
          },
          {
            "title": "VLAbot: A human Vision–Language–Action models interaction framework for robotic assembly - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0736584526000475"
          },
          {
            "title": "Shake-VLA: Vision-Language-Action Model-Based System for Bimanual Robotic Manipulations and Liquid Mixing | Proceedings of the 2025 ACM/IEEE International Conference on Human-Robot Interaction",
            "url": "https://dl.acm.org/doi/10.5555/3721488.3721686"
          }
        ]
      },
      "I've performed a web search for \"VLA-Pilot multi-sample selection robot manipulation 2025\". The search results show a rich landscape of Vision-Language-Action (VLA) models and research in robot manipulation from 2025, though I didn't find a specific project or paper explicitly titled \"VLA-Pilot\" focused on multi-sample selection.\n\nHowever, the search results reveal relevant context about VLA research in 2025:\n\nIn 2025, there have been numerous VLA-related developments including models from Microsoft Research (OmniVLA), Physical Intelligence (π0.6), Nvidia (VLA-0), and others focused on robotic manipulation.\n\nThere has been a rapid acceleration in VLA model development, particularly in 2025, with a focus on vision-language-action models and related multimodal learning approaches for embodied AI and robot learning.\n\nThe broader context includes systems like Shake-VLA, a Vision-Language-Action model-based system designed for bimanual robotic manipulation, demonstrating various specialized applications of VLAs.\n\nIf you're looking for information about a specific \"VLA-Pilot\" project or paper on multi-sample selection, you may want to search for it on academic databases like arXiv, or provide additional context about the authors or institution involved."
    ],
    "durationSeconds": 6.0842967219999995
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T01:32:50.589Z_

<details><summary>↩ Tool result · `toolu_014dgMAwYvYDvfMX7VFLVLuf`</summary>

```text
Web search results for query: "ACoT-VLA action chain of thought VLA robot 2025 2026"

Links: [{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/abs/2601.11404"},{"title":"[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"},{"title":"(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/html/2601.11404v2"},{"title":"[2503.22020] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.22020"},{"title":"Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://huggingface.co/papers/2601.11404"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.11404"},{"title":"CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2025/poster/33233"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"}]

## Search Results: ACoT-VLA

I found comprehensive information about ACoT-VLA. Here's what the search revealed:

### Overview

ACoT-VLA is a novel paradigm designed to bridge the fundamental semantic-kinematic gap in modern robotic policies. It introduces Action Chain-of-Thought (ACoT), a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy.

### Architecture

The approach introduces two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR). The former proposes coarse reference trajectories as explicit action-level reasoning steps, while the latter extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning.

### Performance

The method achieves 98.5%, 84.1%, and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively. ACoT-VLA achieves state-of-the-art performance on multiple simulation benchmarks and exhibits superior robustness under distribution shifts.

### Academic Status

The paper is accepted at CVPR 2026, and the repository serves as the official baseline implementation for the AgiBot World Challenge @ ICRA 2026. The official implementation is available on GitHub at AgibotTech/ACoT-VLA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "544d53e3-04df-4a9a-9eaf-0adee3d80c5c",
  "tool_use_result": {
    "query": "ACoT-VLA action chain of thought VLA robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QNDSHH9NTod9deQz7YsF5g",
        "content": [
          {
            "title": "GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub",
            "url": "https://github.com/AgibotTech/ACoT-VLA"
          },
          {
            "title": "[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2601.11404"
          },
          {
            "title": "[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"
          },
          {
            "title": "(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2601.11404v2"
          },
          {
            "title": "[2503.22020] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2503.22020"
          },
          {
            "title": "Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2601.11404"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2601.11404"
          },
          {
            "title": "CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2025/poster/33233"
          },
          {
            "title": "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"
          }
        ]
      },
      "## Search Results: ACoT-VLA\n\nI found comprehensive information about ACoT-VLA. Here's what the search revealed:\n\n### Overview\n\nACoT-VLA is a novel paradigm designed to bridge the fundamental semantic-kinematic gap in modern robotic policies. It introduces Action Chain-of-Thought (ACoT), a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy.\n\n### Architecture\n\nThe approach introduces two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR). The former proposes coarse reference trajectories as explicit action-level reasoning steps, while the latter extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning.\n\n### Performance\n\nThe method achieves 98.5%, 84.1%, and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively. ACoT-VLA achieves state-of-the-art performance on multiple simulation benchmarks and exhibits superior robustness under distribution shifts.\n\n### Academic Status\n\nThe paper is accepted at CVPR 2026, and the repository serves as the official baseline implementation for the AgiBot World Challenge @ ICRA 2026. The official implementation is available on GitHub at AgibotTech/ACoT-VLA."
    ],
    "durationSeconds": 7.013872067000004
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T01:32:51.825Z_

<details><summary>↩ Tool result · `toolu_015woGt6spXP7nZm1PW1MCrh`</summary>

```text
Web search results for query: "SC-VLA sample consensus vision language action model robot 2025"

Links: [{"title":"Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://vla-survey.github.io/"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - Psi-Robot/Awesome-VLA-Papers: Paper list in the survey: A Survey on Vision-Language-Action Models: An Action Tokenization Perspective · GitHub","url":"https://github.com/Psi-Robot/Awesome-VLA-Papers"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"NeurIPS Poster ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning","url":"https://neurips.cc/virtual/2025/poster/120199"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/abs/2505.04769"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"}]

The search results cover Vision-Language-Action (VLA) models in robotics broadly, but I don't see a specific model called "SC-VLA" mentioned in these results. The results show various VLA models from 2025 like Helix, GR00T N1, Gemini Robotics, π0, SmolVLA, ChatVLA-2, and others, but no reference to "SC-VLA" or "Sample Consensus VLA."

Let me search more specifically for SC-VLA:

Links: [{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"How to use Random Sample Consensus model — pcl 1.9.1 documentation","url":"https://pcl-docs.readthedocs.io/en/latest/pcl/doc/tutorials/content/random_sample_consensus.html"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"How to use Random Sample Consensus model — Point Cloud Library 0.0 documentation","url":"https://pcl.readthedocs.io/projects/tutorials/en/master/random_sample_consensus.html"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"[2001.02643] CONSAC: Robust Multi-Model Fitting by Conditional Sample Consensus","url":"https://arxiv.org/abs/2001.02643"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"ChatVLA: Unified Multimodal Understanding and Robot ...","url":"https://aclanthology.org/2025.emnlp-main.273.pdf"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"}]

Perfect! I found information about SC-VLA. Based on the search results, here's what I found:

## SC-VLA: Self-Correcting Vision-Language-Action Model

SC-VLA (Self-Correcting VLA) is a novel framework designed to enhance physical grounding through intrinsic self-improvement. The model is equipped with Sparse World Imagination (SPI) to forecast task progress and future trajectory trends, and Online Action Refinement (OAR) to dynamically optimize policies via residual adjustments and reshaped rewards.

### Performance

SC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput.

### Publication Details

SC-VLA was authored by Chenyv Liu, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li, Guoli Yang, and Heng Tao Shen, published as an arXiv preprint (arXiv:2602.21633) in 2026. The full title is "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination."

The model builds upon foundation models like GR00T N1.5 and is designed to work with both simulation environments (ManiSkill) and real-world robotic platforms (ARX-5).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "f265504f-33c4-4d7b-a1e8-70a980268d07",
  "tool_use_result": {
    "query": "SC-VLA sample consensus vision language action model robot 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011JXGZS1n69u6QV4ZqB1ms4",
        "content": [
          {
            "title": "Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications",
            "url": "https://vla-survey.github.io/"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "GitHub - Psi-Robot/Awesome-VLA-Papers: Paper list in the survey: A Survey on Vision-Language-Action Models: An Action Tokenization Perspective · GitHub",
            "url": "https://github.com/Psi-Robot/Awesome-VLA-Papers"
          },
          {
            "title": "arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model",
            "url": "https://arxiv.org/pdf/2506.01844"
          },
          {
            "title": "NeurIPS Poster ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning",
            "url": "https://neurips.cc/virtual/2025/poster/120199"
          },
          {
            "title": "Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1566253525011248"
          },
          {
            "title": "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v2"
          },
          {
            "title": "[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/abs/2505.04769"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          }
        ]
      },
      "The search results cover Vision-Language-Action (VLA) models in robotics broadly, but I don't see a specific model called \"SC-VLA\" mentioned in these results. The results show various VLA models from 2025 like Helix, GR00T N1, Gemini Robotics, π0, SmolVLA, ChatVLA-2, and others, but no reference to \"SC-VLA\" or \"Sample Consensus VLA.\"\n\nLet me search more specifically for SC-VLA:",
      {
        "tool_use_id": "srvtoolu_017ZcSqZTA7ke8hxZUENsUDb",
        "content": [
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "How to use Random Sample Consensus model — pcl 1.9.1 documentation",
            "url": "https://pcl-docs.readthedocs.io/en/latest/pcl/doc/tutorials/content/random_sample_consensus.html"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "How to use Random Sample Consensus model — Point Cloud Library 0.0 documentation",
            "url": "https://pcl.readthedocs.io/projects/tutorials/en/master/random_sample_consensus.html"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "[2001.02643] CONSAC: Robust Multi-Model Fitting by Conditional Sample Consensus",
            "url": "https://arxiv.org/abs/2001.02643"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "ChatVLA: Unified Multimodal Understanding and Robot ...",
            "url": "https://aclanthology.org/2025.emnlp-main.273.pdf"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          }
        ]
      },
      "Perfect! I found information about SC-VLA. Based on the search results, here's what I found:\n\n## SC-VLA: Self-Correcting Vision-Language-Action Model\n\nSC-VLA (Self-Correcting VLA) is a novel framework designed to enhance physical grounding through intrinsic self-improvement. The model is equipped with Sparse World Imagination (SPI) to forecast task progress and future trajectory trends, and Online Action Refinement (OAR) to dynamically optimize policies via residual adjustments and reshaped rewards.\n\n### Performance\n\nSC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput.\n\n### Publication Details\n\nSC-VLA was authored by Chenyv Liu, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li, Guoli Yang, and Heng Tao Shen, published as an arXiv preprint (arXiv:2602.21633) in 2026. The full title is \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination.\"\n\nThe model builds upon foundation models like GR00T N1.5 and is designed to work with both simulation environments (ManiSkill) and real-world robotic platforms (ARX-5)."
    ],
    "durationSeconds": 8.708625889000002
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T01:32:52.287Z_

<details><summary>↩ Tool result · `toolu_01FzSbLbkXMTbf4h6YgPLzDn`</summary>

```text
Web search results for query: "VLAC vision language action critic robot manipulation 2025"

Links: [{"title":"GitHub - InternRobotics/VLAC: VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning · GitHub","url":"https://github.com/InternRobotics/VLAC"},{"title":"VLAC: A Generalist Action-Critic Model via Pair-wise Progress Understanding | OpenReview","url":"https://openreview.net/forum?id=PmYX0XiQQ0"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"[2509.15937] A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://arxiv.org/abs/2509.15937"},{"title":"Paper page - A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://huggingface.co/papers/2509.15937"},{"title":"A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://arxiv.org/html/2509.15937v1"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"[Quick Review] A Vision-Language-Action-Critic Model for Robotic Real-World\\n Reinforcement Learning","url":"https://liner.com/review/visionlanguageactioncritic-model-for-robotic-realworld-reinforcement-learning"},{"title":"[2507.10672] Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/abs/2507.10672"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"}]

Based on the search results, here's what I found about VLAC:

## Overview

VLAC is a general-purpose pair-wise critic and manipulation model which designed for real world robot reinforcement learning and data refinement.

## Key Features

VLAC is a generalist Vision Language Action-Critic model, which can integrate both human and robot data, and unify action generation and task progress understanding within a single autoregressive architecture. 

VLAC supports process tracking, task completion judgment, task description estimation, visual question answering, and even embodied action output, equipped with VLA capabilities.

## Training and Data

VLAC trained on 3000h+ human egocentric data, 1200h+ comprehensive public robotic manipulation data, and 15h+ self-collected manipulation data.

## Technical Approach

The model proposes a scalable and generalizable pair-wise progress understanding approach to predict the task progress delta between any two images in one visual trajectory, and generate the action based on the first image.

## Real-World Performance

Across four distinct real-world manipulation tasks, VLAC lifts success rates from about 30% to about 90% within 200 real-world interaction episodes; incorporating human-in-the-loop interventions yields a further 50% improvement in sample efficiency and achieves up to 100% final success.

The model was published on arXiv in 2025 with the full paper available as arXiv preprint 2509.15937.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "633b473e-e072-4e6d-b75f-2d2550be5fff",
  "tool_use_result": {
    "query": "VLAC vision language action critic robot manipulation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018UCH1yzYkBAbaQsWrWr5jE",
        "content": [
          {
            "title": "GitHub - InternRobotics/VLAC: VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning · GitHub",
            "url": "https://github.com/InternRobotics/VLAC"
          },
          {
            "title": "VLAC: A Generalist Action-Critic Model via Pair-wise Progress Understanding | OpenReview",
            "url": "https://openreview.net/forum?id=PmYX0XiQQ0"
          },
          {
            "title": "2025-9-22 A Vision-Language-Action-Critic Model",
            "url": "https://arxiv.org/pdf/2509.15937"
          },
          {
            "title": "[2509.15937] A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning",
            "url": "https://arxiv.org/abs/2509.15937"
          },
          {
            "title": "Paper page - A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning",
            "url": "https://huggingface.co/papers/2509.15937"
          },
          {
            "title": "A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.15937v1"
          },
          {
            "title": "GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub",
            "url": "https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"
          },
          {
            "title": "[Quick Review] A Vision-Language-Action-Critic Model for Robotic Real-World\\n Reinforcement Learning",
            "url": "https://liner.com/review/visionlanguageactioncritic-model-for-robotic-realworld-reinforcement-learning"
          },
          {
            "title": "[2507.10672] Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/abs/2507.10672"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          }
        ]
      },
      "Based on the search results, here's what I found about VLAC:\n\n## Overview\n\nVLAC is a general-purpose pair-wise critic and manipulation model which designed for real world robot reinforcement learning and data refinement.\n\n## Key Features\n\nVLAC is a generalist Vision Language Action-Critic model, which can integrate both human and robot data, and unify action generation and task progress understanding within a single autoregressive architecture. \n\nVLAC supports process tracking, task completion judgment, task description estimation, visual question answering, and even embodied action output, equipped with VLA capabilities.\n\n## Training and Data\n\nVLAC trained on 3000h+ human egocentric data, 1200h+ comprehensive public robotic manipulation data, and 15h+ self-collected manipulation data.\n\n## Technical Approach\n\nThe model proposes a scalable and generalizable pair-wise progress understanding approach to predict the task progress delta between any two images in one visual trajectory, and generate the action based on the first image.\n\n## Real-World Performance\n\nAcross four distinct real-world manipulation tasks, VLAC lifts success rates from about 30% to about 90% within 200 real-world interaction episodes; incorporating human-in-the-loop interventions yields a further 50% improvement in sample efficiency and achieves up to 100% final success.\n\nThe model was published on arXiv in 2025 with the full paper available as arXiv preprint 2509.15937."
    ],
    "durationSeconds": 7.511384093
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Great findings. Let me now search for more specific information about:
1. The new ReconVLA uncertainty paper (2604.16677) - specifically its conformal prediction approach to understand if it overlaps with our work
2. FPC-VLA (failure prediction and correction)
3. Any per-DOF conformal prediction work
4. VLA-OPD (the on-policy distillation paper)
5. ICLR 2026 VLA summary blog
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "d78907f9-375a-4291-b938-f6473c33406a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112shnVm3KuCybfWNqA2RkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 29511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

关键发现：arXiv 2604.16677 也用了 conformal prediction on VLA。这是最大的 novelty 威胁。继续深挖细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "1e1fa1dc-af28-4a3e-8aa3-e2e2fa599670",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112shnVm3KuCybfWNqA2RkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 29511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VnJMt25ksV29NQ6KXk2P27`</summary>

```json
{
  "query": "\"ReconVLA\" \"conformal prediction\" \"action token\" per-DOF nonconformity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "3bbf39ff-5733-44f5-8806-fcfbd0485efe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112shnVm3KuCybfWNqA2RkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 29511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LAw3vYnenn2Wopwkij2a1A`</summary>

```json
{
  "query": "FPC-VLA failure prediction correction VLA supervisor 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "0e12af4c-ca95-4d34-9e7c-eec14c1967e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112shnVm3KuCybfWNqA2RkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 29511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0147zu4Pc19hM4v6dTtZQUGG`</summary>

```json
{
  "query": "VLA-OPD on-policy distillation epistemic uncertainty 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "f84c3a99-4590-4c13-8a24-854773523e70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112shnVm3KuCybfWNqA2RkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 29511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RjK3pH6NCAUTnMRtQ5yWJw`</summary>

```json
{
  "query": "\"per-DOF\" OR \"per-dimension\" conformal prediction action robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "0a307d62-f919-41f3-b831-09e4d5e50cd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112shnVm3KuCybfWNqA2RkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 29511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KGz2rXCGecgNxHaSn1dttq`</summary>

```json
{
  "query": "CoRL 2026 robot learning VLA submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "d221c60e-2f59-4238-ae65-6611fbe3f9f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112shnVm3KuCybfWNqA2RkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 29511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

_source line 38 · 2026-05-15T01:33:05.810Z_

<details><summary>↩ Tool result · `toolu_01VnJMt25ksV29NQ6KXk2P27`</summary>

```text
Web search results for query: ""ReconVLA" "conformal prediction" "action token" per-DOF nonconformity 2026"

Links: [{"title":"TECP: Token-Entropy Conformal Prediction for LLMs","url":"https://www.mdpi.com/2227-7390/13/20/3351"},{"title":"1 INTRODUCTION","url":"https://arxiv.org/html/2510.04318"},{"title":"Online Conformal Prediction: Enforcing monotonicity via Online Optimization","url":"https://arxiv.org/html/2605.12668"},{"title":"TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models","url":"https://arxiv.org/html/2605.07100"},{"title":"GitHub - valeman/awesome-conformal-prediction: A professionally curated list of awesome Conformal Prediction videos, tutorials, books, papers, PhD and MSc theses, articles and open-source libraries. · GitHub","url":"https://github.com/valeman/awesome-conformal-prediction"},{"title":"Task-Driven Uncertainty Quantification in Inverse Problems via Conformal Prediction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12109201/"},{"title":"Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations","url":"https://arxiv.org/html/2604.16217"},{"title":"Conformal prediction - Wikipedia","url":"https://en.wikipedia.org/wiki/Conformal_prediction"},{"title":"A Review of Nonconformity Measures for Conformal ...","url":"https://proceedings.mlr.press/v204/kato23a/kato23a.pdf"},{"title":"Reliable TV Audience Forecasting with Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-06164-5_6"}]

I searched for "ReconVLA conformal prediction action token per-DOF nonconformity 2026" but the results did not contain any papers or resources specifically about "ReconVLA" combined with conformal prediction and action tokens. 

The search returned several recent papers about conformal prediction in various applications (LLMs, time series, image inverse problems, etc.), but none mentioning "ReconVLA" or the specific combination of concepts you're asking about.

This could mean:
- The work may be very recent or not yet widely indexed by search engines
- The terminology or exact phrasing may differ from what I searched
- It could be a technical report or preprint not yet broadly available

Would you like me to:
1. Search for "ReconVLA" alone to see what that refers to?
2. Search for "action token" with "conformal prediction" to find related work?
3. Try a different search query or combination of terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "8775342f-44ac-4ec1-b245-1679b536eaf0",
  "tool_use_result": {
    "query": "\"ReconVLA\" \"conformal prediction\" \"action token\" per-DOF nonconformity 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RewnxtESuU9eFGr78d9RcP",
        "content": [
          {
            "title": "TECP: Token-Entropy Conformal Prediction for LLMs",
            "url": "https://www.mdpi.com/2227-7390/13/20/3351"
          },
          {
            "title": "1 INTRODUCTION",
            "url": "https://arxiv.org/html/2510.04318"
          },
          {
            "title": "Online Conformal Prediction: Enforcing monotonicity via Online Optimization",
            "url": "https://arxiv.org/html/2605.12668"
          },
          {
            "title": "TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models",
            "url": "https://arxiv.org/html/2605.07100"
          },
          {
            "title": "GitHub - valeman/awesome-conformal-prediction: A professionally curated list of awesome Conformal Prediction videos, tutorials, books, papers, PhD and MSc theses, articles and open-source libraries. · GitHub",
            "url": "https://github.com/valeman/awesome-conformal-prediction"
          },
          {
            "title": "Task-Driven Uncertainty Quantification in Inverse Problems via Conformal Prediction - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12109201/"
          },
          {
            "title": "Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations",
            "url": "https://arxiv.org/html/2604.16217"
          },
          {
            "title": "Conformal prediction - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Conformal_prediction"
          },
          {
            "title": "A Review of Nonconformity Measures for Conformal ...",
            "url": "https://proceedings.mlr.press/v204/kato23a/kato23a.pdf"
          },
          {
            "title": "Reliable TV Audience Forecasting with Conformal Prediction | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-06164-5_6"
          }
        ]
      },
      "I searched for \"ReconVLA conformal prediction action token per-DOF nonconformity 2026\" but the results did not contain any papers or resources specifically about \"ReconVLA\" combined with conformal prediction and action tokens. \n\nThe search returned several recent papers about conformal prediction in various applications (LLMs, time series, image inverse problems, etc.), but none mentioning \"ReconVLA\" or the specific combination of concepts you're asking about.\n\nThis could mean:\n- The work may be very recent or not yet widely indexed by search engines\n- The terminology or exact phrasing may differ from what I searched\n- It could be a technical report or preprint not yet broadly available\n\nWould you like me to:\n1. Search for \"ReconVLA\" alone to see what that refers to?\n2. Search for \"action token\" with \"conformal prediction\" to find related work?\n3. Try a different search query or combination of terms?"
    ],
    "durationSeconds": 5.757956352000001
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T01:33:07.234Z_

<details><summary>↩ Tool result · `toolu_01LAw3vYnenn2Wopwkij2a1A`</summary>

```text
Web search results for query: "FPC-VLA failure prediction correction VLA supervisor 2025 2026 arXiv"

Links: [{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://arxiv.org/html/2509.04018"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor","url":"https://arxiv.org/pdf/2509.04018"},{"title":"[2509.04018] FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://arxiv.org/abs/2509.04018"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction by Yifan Yang, Zhixiang Duan, Tianshi Xie, Fuyu Cao, Pinxi Shen, Peili Song, Chenyang Zhao, Piaopiao Jin, Guokang Sun, Shaoqing Xu, Yangwei You, Jingtai Liu :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/fb935762-45ef-4d2a-9621-dd505dfaf134-MECA.pdf?abstractid=5912300&mirid=1"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/fpc-vla-vision-language-action-framework-supervisor"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095741742600655X"},{"title":"[Literature Review] FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://www.themoonlight.io/en/review/fpc-vla-a-vision-language-action-framework-with-a-supervisor-for-failure-prediction-and-correction"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://fpcvla.github.io/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"[2505.12224] RoboFAC: A Comprehensive Framework for Robotic Failure Analysis and Correction","url":"https://arxiv.org/abs/2505.12224"}]

I found the paper you're looking for! Here are the search results for FPC-VLA:

## FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction

FPC-VLA is a dual-model framework that integrates VLA with a supervisor for failure prediction and correction.

**Key Features:**
- Unlike conventional end-to-end VLA models that directly execute predicted actions without verification, FPC-VLA introduces a VLM-based supervisor that actively evaluates the feasibility and safety of proposed actions before execution.
- The supervisor is triggered at keyframes and evaluates action viability through structured vision–language queries. If a potential failure is detected, it generates natural language corrections specifying direction and magnitude of adjustment.
- An automated pipeline generates large-scale failure prediction and correction datasets from existing robotic data without manual labeling.

**Performance:**
Evaluation results on SIMPLER and LIBERO benchmarks, using WidowX, Google Robot and Franka, and real-world experiments on Xiaomi robot and ALOHA, show that FPC-VLA outperforms other state-of-the-art methods.

**Paper Details:**
- **arXiv ID:** 2509.04018
- **Publication Date:** September 4, 2025 (v1); December 3, 2025 (v2)
- **Lead Author:** Yifan Yang
- **Available at:** https://arxiv.org/abs/2509.04018


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "e1bd35e1-0630-4007-9f8c-c66cbae9adbd",
  "tool_use_result": {
    "query": "FPC-VLA failure prediction correction VLA supervisor 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U1VRePB5qe9qhgxhEYnMc6",
        "content": [
          {
            "title": "FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction",
            "url": "https://arxiv.org/html/2509.04018"
          },
          {
            "title": "FPC-VLA: A Vision-Language-Action Framework with a Supervisor",
            "url": "https://arxiv.org/pdf/2509.04018"
          },
          {
            "title": "[2509.04018] FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction",
            "url": "https://arxiv.org/abs/2509.04018"
          },
          {
            "title": "FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction by Yifan Yang, Zhixiang Duan, Tianshi Xie, Fuyu Cao, Pinxi Shen, Peili Song, Chenyang Zhao, Piaopiao Jin, Guokang Sun, Shaoqing Xu, Yangwei You, Jingtai Liu :: SSRN",
            "url": "https://papers.ssrn.com/sol3/Delivery.cfm/fb935762-45ef-4d2a-9621-dd505dfaf134-MECA.pdf?abstractid=5912300&mirid=1"
          },
          {
            "title": "FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/fpc-vla-vision-language-action-framework-supervisor"
          },
          {
            "title": "FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S095741742600655X"
          },
          {
            "title": "[Literature Review] FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction",
            "url": "https://www.themoonlight.io/en/review/fpc-vla-a-vision-language-action-framework-with-a-supervisor-for-failure-prediction-and-correction"
          },
          {
            "title": "FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction",
            "url": "https://fpcvla.github.io/"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "[2505.12224] RoboFAC: A Comprehensive Framework for Robotic Failure Analysis and Correction",
            "url": "https://arxiv.org/abs/2505.12224"
          }
        ]
      },
      "I found the paper you're looking for! Here are the search results for FPC-VLA:\n\n## FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction\n\nFPC-VLA is a dual-model framework that integrates VLA with a supervisor for failure prediction and correction.\n\n**Key Features:**\n- Unlike conventional end-to-end VLA models that directly execute predicted actions without verification, FPC-VLA introduces a VLM-based supervisor that actively evaluates the feasibility and safety of proposed actions before execution.\n- The supervisor is triggered at keyframes and evaluates action viability through structured vision–language queries. If a potential failure is detected, it generates natural language corrections specifying direction and magnitude of adjustment.\n- An automated pipeline generates large-scale failure prediction and correction datasets from existing robotic data without manual labeling.\n\n**Performance:**\nEvaluation results on SIMPLER and LIBERO benchmarks, using WidowX, Google Robot and Franka, and real-world experiments on Xiaomi robot and ALOHA, show that FPC-VLA outperforms other state-of-the-art methods.\n\n**Paper Details:**\n- **arXiv ID:** 2509.04018\n- **Publication Date:** September 4, 2025 (v1); December 3, 2025 (v2)\n- **Lead Author:** Yifan Yang\n- **Available at:** https://arxiv.org/abs/2509.04018"
    ],
    "durationSeconds": 6.698559956999998
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T01:33:07.660Z_

<details><summary>↩ Tool result · `toolu_0147zu4Pc19hM4v6dTtZQUGG`</summary>

```text
Web search results for query: "VLA-OPD on-policy distillation epistemic uncertainty 2026"

Links: [{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Hindsight-Guided+On-Policy+Distillation"},{"title":"(PDF) Retrieval-Guided Policy Distillation for Accelerating Vision-Language-Action Specialization Under Demonstration Scarcity","url":"https://www.researchgate.net/publication/401513215_Retrieval-Guided_Policy_Distillation_for_Accelerating_Vision-Language-Action_Specialization_Under_Demonstration_Scarcity"},{"title":"TRACE: Distilling Where It Matters via Token-Routed Self On-Policy Alignment","url":"https://arxiv.org/html/2605.10194v1"},{"title":"Training Driving AI at 50,000× Real Time - IEEE Spectrum","url":"https://spectrum.ieee.org/gm-scalable-driving-ai"},{"title":"GitHub - thinkwee/AwesomeOPD: Awesome List for On-Policy Distillation · GitHub","url":"https://github.com/thinkwee/AwesomeOPD"},{"title":"On-Policy Distillation (OPD) - Research Survey 2026 - Amy's Blog","url":"https://amysheng-ai.github.io/AmyBlog/posts/opd-survey-2026/"},{"title":"[2604.00626] A Survey of On-Policy Distillation for Large Language Models","url":"https://arxiv.org/abs/2604.00626"},{"title":"Paper page - A Survey of On-Policy Distillation for Large Language Models","url":"https://huggingface.co/papers/2604.00626"},{"title":"(PDF) Self-Distilled RLVR","url":"https://www.researchgate.net/publication/403530504_Self-Distilled_RLVR"}]

Based on the search results, here's what I found about VLA-OPD on-policy distillation and epistemic uncertainty:

## VLA-OPD (Vision-Language-Action On-Policy Distillation)

VLA-OPD is a framework that bridges the efficiency of Supervised Fine-Tuning (SFT) with the robustness of Reinforcement Learning (RL). Instead of relying on sparse environmental rewards, VLA-OPD leverages an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories.

## Handling Epistemic Uncertainty

A key innovation of VLA-OPD is how it addresses epistemic uncertainty. VLA-OPD is formulated via a Reverse-KL objective. Unlike standard Forward-KL that induces mode-covering entropy explosion, or Hard-CE that causes premature entropy collapse, the bounded mode-seeking objective ensures stable policy learning by filtering out the teacher's epistemic uncertainty.

The bounded mode-seeking property effectively filters out the teacher's epistemic uncertainty while maintaining action diversity, preventing both the entropy explosion of Forward-KL and the premature entropy collapse of Hard-CE.

## Performance and Applications

Extensive evaluations across LIBERO and RoboTwin2.0 benchmarks demonstrate that VLA-OPD achieves superior robustness and success rates compared to SFT. The framework was published in 2026 (arxiv 2603.26666) and represents a significant advancement in training Vision-Language-Action models effectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "a53669cb-8c2d-40d5-929f-cac4b039465c",
  "tool_use_result": {
    "query": "VLA-OPD on-policy distillation epistemic uncertainty 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011unW9cP2xxghh5seJxGp81",
        "content": [
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666v1"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Hindsight-Guided+On-Policy+Distillation"
          },
          {
            "title": "(PDF) Retrieval-Guided Policy Distillation for Accelerating Vision-Language-Action Specialization Under Demonstration Scarcity",
            "url": "https://www.researchgate.net/publication/401513215_Retrieval-Guided_Policy_Distillation_for_Accelerating_Vision-Language-Action_Specialization_Under_Demonstration_Scarcity"
          },
          {
            "title": "TRACE: Distilling Where It Matters via Token-Routed Self On-Policy Alignment",
            "url": "https://arxiv.org/html/2605.10194v1"
          },
          {
            "title": "Training Driving AI at 50,000× Real Time - IEEE Spectrum",
            "url": "https://spectrum.ieee.org/gm-scalable-driving-ai"
          },
          {
            "title": "GitHub - thinkwee/AwesomeOPD: Awesome List for On-Policy Distillation · GitHub",
            "url": "https://github.com/thinkwee/AwesomeOPD"
          },
          {
            "title": "On-Policy Distillation (OPD) - Research Survey 2026 - Amy's Blog",
            "url": "https://amysheng-ai.github.io/AmyBlog/posts/opd-survey-2026/"
          },
          {
            "title": "[2604.00626] A Survey of On-Policy Distillation for Large Language Models",
            "url": "https://arxiv.org/abs/2604.00626"
          },
          {
            "title": "Paper page - A Survey of On-Policy Distillation for Large Language Models",
            "url": "https://huggingface.co/papers/2604.00626"
          },
          {
            "title": "(PDF) Self-Distilled RLVR",
            "url": "https://www.researchgate.net/publication/403530504_Self-Distilled_RLVR"
          }
        ]
      },
      "Based on the search results, here's what I found about VLA-OPD on-policy distillation and epistemic uncertainty:\n\n## VLA-OPD (Vision-Language-Action On-Policy Distillation)\n\nVLA-OPD is a framework that bridges the efficiency of Supervised Fine-Tuning (SFT) with the robustness of Reinforcement Learning (RL). Instead of relying on sparse environmental rewards, VLA-OPD leverages an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories.\n\n## Handling Epistemic Uncertainty\n\nA key innovation of VLA-OPD is how it addresses epistemic uncertainty. VLA-OPD is formulated via a Reverse-KL objective. Unlike standard Forward-KL that induces mode-covering entropy explosion, or Hard-CE that causes premature entropy collapse, the bounded mode-seeking objective ensures stable policy learning by filtering out the teacher's epistemic uncertainty.\n\nThe bounded mode-seeking property effectively filters out the teacher's epistemic uncertainty while maintaining action diversity, preventing both the entropy explosion of Forward-KL and the premature entropy collapse of Hard-CE.\n\n## Performance and Applications\n\nExtensive evaluations across LIBERO and RoboTwin2.0 benchmarks demonstrate that VLA-OPD achieves superior robustness and success rates compared to SFT. The framework was published in 2026 (arxiv 2603.26666) and represents a significant advancement in training Vision-Language-Action models effectively."
    ],
    "durationSeconds": 6.644542688000001
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T01:33:09.741Z_

<details><summary>↩ Tool result · `toolu_01KGz2rXCGecgNxHaSn1dttq`</summary>

```text
Web search results for query: "CoRL 2026 robot learning VLA submission deadline"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here are the submission deadlines for CoRL 2026:

The abstract submission deadline is May 26, 2026 11:59 UTC, and the paper submission deadline is May 29, 2026 11:59 UTC. However, the paper submission deadline is Thursday (5/28) EOD rather than Friday, which indicates the actual paper deadline may be May 28, 2026.

CoRL 2026 will be held in Austin, Texas, US, and the conference dates are November 9-12, 2026.

The search results focused on general paper submissions to CoRL 2026. While the results mention video models and latent world models as topics of interest, I did not find specific information about a separate "VLA (Vision Language Action) submission deadline" - it appears VLA-related work would be submitted through the regular paper submission process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "eb872a9f-698d-430a-8a76-25078dc74c0c",
  "tool_use_result": {
    "query": "CoRL 2026 robot learning VLA submission deadline",
    "results": [
      {
        "tool_use_id": "srvtoolu_015Acm79wxEfbPLF8uk5j4F8",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf"
          },
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          }
        ]
      },
      "Based on the search results, here are the submission deadlines for CoRL 2026:\n\nThe abstract submission deadline is May 26, 2026 11:59 UTC, and the paper submission deadline is May 29, 2026 11:59 UTC. However, the paper submission deadline is Thursday (5/28) EOD rather than Friday, which indicates the actual paper deadline may be May 28, 2026.\n\nCoRL 2026 will be held in Austin, Texas, US, and the conference dates are November 9-12, 2026.\n\nThe search results focused on general paper submissions to CoRL 2026. While the results mention video models and latent world models as topics of interest, I did not find specific information about a separate \"VLA (Vision Language Action) submission deadline\" - it appears VLA-related work would be submitted through the regular paper submission process."
    ],
    "durationSeconds": 4.628960718000002
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T01:33:15.573Z_

<details><summary>↩ Tool result · `toolu_01RjK3pH6NCAUTnMRtQ5yWJw`</summary>

```text
Web search results for query: ""per-DOF" OR "per-dimension" conformal prediction action robot manipulation"

Links: [{"title":"Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024","url":"https://www.roboticsproceedings.org/rss20/p008.pdf"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/html/2406.07767v2"},{"title":"Interaction-aware Conformal Prediction for Crowd Navigation","url":"https://arxiv.org/html/2502.06221"},{"title":"Learning Robot Safety from Sparse Human Feedback using Conformal Prediction","url":"https://arxiv.org/html/2501.04823"},{"title":"Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction","url":"https://arxiv.org/html/2402.15368"},{"title":"Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction","url":"https://arxiv.org/html/2402.15368v1"},{"title":"Adaptive Conformal Prediction for Motion Planning among ...","url":"https://proceedings.mlr.press/v211/dixit23a/dixit23a.pdf"},{"title":"[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/abs/2406.07767"},{"title":"Preprint WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA","url":"https://opendrivelab.com/WholeBodyVLA/static/pdf/WholeBodyVLA.pdf"},{"title":"GitHub - Argo-Robot/foundation_models: Overview about state-of-art imitation learning techniques for robotic manipulation, enabling generalization across diverse tasks and environments. · GitHub","url":"https://github.com/Argo-Robot/foundation_models"}]

Based on the search results, I found relevant research on conformal prediction applied to robot manipulation and action prediction. Here are the key findings:

## Conformalized Teleoperation

The most directly relevant work seeks to rigorously quantify if a learned assistive controller can confidently infer a user's intended high-dimensional action from only low-dimensional states and inputs, using adaptive conformal prediction to calibrate the uncertainty of high-DoF action quantiles.

This approach leverages conformal methods to quantify if the robot's learned controller can reliably lift the human's low-DoF input (joystick) to their desired high-DoF action (7 joint velocities).

### Key Technical Approach

The method involves training the robot's initial assistive mapping with paired low-DoF inputs and high-dimensional-DoF outputs while forcing the model to approximate its own uncertainty by predicting empirical quantiles, then using ACQR to calibrate this base model to data from a target user.

### Coverage Guarantees

The approach leverages adaptive conformal prediction which adjusts the intervals over time, reducing the uncertainty bounds when the mapping is performant and increasing the bounds when the mapping consistently mis-predicts.

## Evaluation Context

The approach was evaluated in a 2D assistive navigation task and two 7DOF Kinova Jaco tasks involving assistive cup grasping and goal reaching.

This research represents state-of-the-art work in applying per-dimension (or per-DOF) conformal prediction to robot manipulation tasks, specifically for mapping uncertain human inputs to high-dimensional robot actions while providing statistical guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "148f479a-e6b8-4b66-832e-20300443c917",
  "tool_use_result": {
    "query": "\"per-DOF\" OR \"per-dimension\" conformal prediction action robot manipulation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MLg3wWZP8ZQmgctLWCRbzZ",
        "content": [
          {
            "title": "Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024",
            "url": "https://www.roboticsproceedings.org/rss20/p008.pdf"
          },
          {
            "title": "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions",
            "url": "https://arxiv.org/html/2406.07767v2"
          },
          {
            "title": "Interaction-aware Conformal Prediction for Crowd Navigation",
            "url": "https://arxiv.org/html/2502.06221"
          },
          {
            "title": "Learning Robot Safety from Sparse Human Feedback using Conformal Prediction",
            "url": "https://arxiv.org/html/2501.04823"
          },
          {
            "title": "Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction",
            "url": "https://arxiv.org/html/2402.15368"
          },
          {
            "title": "Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction",
            "url": "https://arxiv.org/html/2402.15368v1"
          },
          {
            "title": "Adaptive Conformal Prediction for Motion Planning among ...",
            "url": "https://proceedings.mlr.press/v211/dixit23a/dixit23a.pdf"
          },
          {
            "title": "[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions",
            "url": "https://arxiv.org/abs/2406.07767"
          },
          {
            "title": "Preprint WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA",
            "url": "https://opendrivelab.com/WholeBodyVLA/static/pdf/WholeBodyVLA.pdf"
          },
          {
            "title": "GitHub - Argo-Robot/foundation_models: Overview about state-of-art imitation learning techniques for robotic manipulation, enabling generalization across diverse tasks and environments. · GitHub",
            "url": "https://github.com/Argo-Robot/foundation_models"
          }
        ]
      },
      "Based on the search results, I found relevant research on conformal prediction applied to robot manipulation and action prediction. Here are the key findings:\n\n## Conformalized Teleoperation\n\nThe most directly relevant work seeks to rigorously quantify if a learned assistive controller can confidently infer a user's intended high-dimensional action from only low-dimensional states and inputs, using adaptive conformal prediction to calibrate the uncertainty of high-DoF action quantiles.\n\nThis approach leverages conformal methods to quantify if the robot's learned controller can reliably lift the human's low-DoF input (joystick) to their desired high-DoF action (7 joint velocities).\n\n### Key Technical Approach\n\nThe method involves training the robot's initial assistive mapping with paired low-DoF inputs and high-dimensional-DoF outputs while forcing the model to approximate its own uncertainty by predicting empirical quantiles, then using ACQR to calibrate this base model to data from a target user.\n\n### Coverage Guarantees\n\nThe approach leverages adaptive conformal prediction which adjusts the intervals over time, reducing the uncertainty bounds when the mapping is performant and increasing the bounds when the mapping consistently mis-predicts.\n\n## Evaluation Context\n\nThe approach was evaluated in a 2D assistive navigation task and two 7DOF Kinova Jaco tasks involving assistive cup grasping and goal reaching.\n\nThis research represents state-of-the-art work in applying per-dimension (or per-DOF) conformal prediction to robot manipulation tasks, specifically for mapping uncertain human inputs to high-dimensional robot actions while providing statistical guarantees."
    ],
    "durationSeconds": 10.576308792999997
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Excellent findings. Let me now dig deeper into two critical papers:
1. The new ReconVLA (2604.16677) which explicitly applies conformal prediction to VLA - this is the biggest novelty threat
2. The Conformalized Teleoperation paper (2406.07767) which does per-DOF conformal prediction for robot actions

Let me also check for the ICLR 2026 VLA blog post and any other recent work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "43536cce-2925-4e9c-b6b5-b149e0e1502e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQakPiVDkaKfDh2ZSm9jYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 675,
      "cache_creation_input_tokens": 4164,
      "cache_read_input_tokens": 35113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4164
      },
      "output_tokens": 22,
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

_source line 44_

关键发现：CoRL 2026 abstract DDL 确认 May 26。新 ReconVLA (2604.16677) 和 Conformalized Teleoperation (2406.07767) 是主要 novelty 威胁。继续深入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e78d564b-0ec6-4348-a773-23d5da8826f1",
  "uuid": "ae6cb019-9659-4ab5-8ffb-9ceb207727e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQakPiVDkaKfDh2ZSm9jYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 675,
      "cache_creation_input_tokens": 4164,
      "cache_read_input_tokens": 35113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4164
      },
      "output_tokens": 22,
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
