# research related work gap check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_research_related_work_gap_check_20260524T011417.log`
- **Structured JSON:** [`af57ba78ff0bf6795874.json`](../../sessions/af/af57ba78ff0bf6795874.json)

## Before a recorded user message

70 recorded events

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
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
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
  "uuid": "ed6f2805-9a4e-4d4b-bf2a-a6d7efbf9501",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779593400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "dff9fc0f-e9a8-46c6-8374-5b6d09403da6",
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223"
}
```

---

### Assistant

_source line 4_

我将并行搜索这8组关键词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "d2d9dc37-e428-4e15-a358-c4c6cf904906",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMyCshB5jG1CJY56A5HLQ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11775,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11775
      },
      "output_tokens": 3,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019NhYjFtgLPUU7yTVm7kL2j`</summary>

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
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "cdf4516c-036c-4741-a652-8fc1222048f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMyCshB5jG1CJY56A5HLQ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11775,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11775
      },
      "output_tokens": 3,
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

_source line 6 · 2026-05-24T01:14:29.058Z_

<details><summary>↩ Tool result · `toolu_019NhYjFtgLPUU7yTVm7kL2j`</summary>

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
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "8d3ef4f4-8afb-4d12-81a4-3694a925211b",
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

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I'll launch all 8 searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "191998a5-ee69-49b5-8cbf-a15dccd28e64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XBgLTWrVpdXHP172qKw7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 23616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FADifvgbVcRwM1kAprbSya`</summary>

```json
{
  "query": "VLA representation analysis vision language action internal representations 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "82b6069b-e4d7-4cb1-b72a-68690a59383b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XBgLTWrVpdXHP172qKw7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 23616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_012i5W9r94A6T68YKnHkPoAx`</summary>

```json
{
  "query": "instruction routing transformers attention head specialization VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "cc1a1f64-5c4a-4b12-98e4-441e4ddc7664",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XBgLTWrVpdXHP172qKw7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 23616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UbG8qze2xKJsmFzPJ78h2o`</summary>

```json
{
  "query": "OpenVLA analysis interpretability 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "3e1d338c-ce0b-4d40-b13a-05950e76dd96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XBgLTWrVpdXHP172qKw7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 23616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0186PYWJSJGaRgbd7VFiXgvN`</summary>

```json
{
  "query": "TracVLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "cb439964-0007-4cfe-958a-f0da826e756a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XBgLTWrVpdXHP172qKw7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 23616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X9UwzDc4E4XjsuCvDTVPwN`</summary>

```json
{
  "query": "NORA VLA robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "131467bd-906d-4759-ae1e-8d363680c84c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XBgLTWrVpdXHP172qKw7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 23616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uy28nrgHqbTzRkGTotXSTr`</summary>

```json
{
  "query": "VLA mechanistic interpretability probing robot policy 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "50b892da-9167-45b3-b221-1cd4eacd5bd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XBgLTWrVpdXHP172qKw7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 23616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 20,
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NUgDZ57PHrAE323vGfC6DJ`</summary>

```json
{
  "query": "robot action fine-tuning representation collapse 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "a52465ff-0221-4f5f-be2e-f7a6ce6a353c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XBgLTWrVpdXHP172qKw7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 23616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kw3YM4ppyNDw37jN7B3HXM`</summary>

```json
{
  "query": "\"exit collapse\" OR \"representational collapse\" fine-tuning language model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "54d8ba9b-96b9-40ca-87de-70855f2b7722",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XBgLTWrVpdXHP172qKw7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 23616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 20,
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

_source line 16 · 2026-05-24T01:14:39.778Z_

<details><summary>↩ Tool result · `toolu_01FADifvgbVcRwM1kAprbSya`</summary>

```text
Web search results for query: "VLA representation analysis vision language action internal representations 2025 2026"

Links: [{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.15618v2"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.19233"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.15618"},{"title":"How Visual-Language-Action (VLA) Models Work | Towards Data Science","url":"https://towardsdatascience.com/how-visual-language-action-vla-models-work/"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2602.01166"}]

Based on the search results, I found several recent studies and resources on VLA representation analysis from 2025-2026:

## Key Research on VLA Internal Representations

Existing VLA paradigms often treat visual processing as a black box, overlooking how visual information is internally utilized. A recent approach called DeepVision-VLA integrates multi-level features from visual foundation models into deeper VLA layers via a Vision-Language Mixture-of-Transformers architecture to enhance attention to task-relevant objects and improve action generation accuracy.

Research has moved beyond treating the LLM backbone in VLA models as opaque, instead investigating how visual information is processed across internal layers through layer-wise analysis of stacked Transformer layers to understand multimodal integration.

## Mechanistic Analysis Studies

Recent mechanistic studies have identified 82+ manipulation concepts through contrastive selection and created Action Atlas for interactive exploration of VLA representations across multiple models. These studies span five different VLAs with parameters ranging from 80M to 7B, covering three action generation paradigms and four benchmarks with over 394,000 rollout episodes.

## Latent Reasoning Approaches

A unified latent-reasoning VLA framework called LaRA-VLA performs reasoning and prediction entirely in latent space for robotic action.

These recent works represent significant advances in understanding and analyzing how VLA models develop and utilize internal representations for robotic control tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "e99f1bfb-f88a-46cb-bd6c-3d25dc155f39",
  "tool_use_result": {
    "query": "VLA representation analysis vision language action internal representations 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NigK6yG8Q5Xa2suTcehouh",
        "content": [
          {
            "title": "Vision-Language-Action (VLA) Guide for 2026",
            "url": "https://hyscaler.com/insights/vision-language-action-vla-guide/"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.15618v2"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.19233"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.15618"
          },
          {
            "title": "How Visual-Language-Action (VLA) Models Work | Towards Data Science",
            "url": "https://towardsdatascience.com/how-visual-language-action-vla-models-work/"
          },
          {
            "title": "Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2602.01166"
          }
        ]
      },
      "Based on the search results, I found several recent studies and resources on VLA representation analysis from 2025-2026:\n\n## Key Research on VLA Internal Representations\n\nExisting VLA paradigms often treat visual processing as a black box, overlooking how visual information is internally utilized. A recent approach called DeepVision-VLA integrates multi-level features from visual foundation models into deeper VLA layers via a Vision-Language Mixture-of-Transformers architecture to enhance attention to task-relevant objects and improve action generation accuracy.\n\nResearch has moved beyond treating the LLM backbone in VLA models as opaque, instead investigating how visual information is processed across internal layers through layer-wise analysis of stacked Transformer layers to understand multimodal integration.\n\n## Mechanistic Analysis Studies\n\nRecent mechanistic studies have identified 82+ manipulation concepts through contrastive selection and created Action Atlas for interactive exploration of VLA representations across multiple models. These studies span five different VLAs with parameters ranging from 80M to 7B, covering three action generation paradigms and four benchmarks with over 394,000 rollout episodes.\n\n## Latent Reasoning Approaches\n\nA unified latent-reasoning VLA framework called LaRA-VLA performs reasoning and prediction entirely in latent space for robotic action.\n\nThese recent works represent significant advances in understanding and analyzing how VLA models develop and utilize internal representations for robotic control tasks."
    ],
    "durationSeconds": 7.040200877999999
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T01:14:40.015Z_

<details><summary>↩ Tool result · `toolu_0186PYWJSJGaRgbd7VFiXgvN`</summary>

```text
Web search results for query: "TracVLA 2025 2026"

Links: [{"title":"The Traka","url":"https://www.granfondoguide.com/Events/Index/10556/the-traka"},{"title":"THE TRAKA 2026 in girona on April 30, 2026","url":"https://web.rockthesport.com/en/event/the-traka-2026"},{"title":"Transport Research Arena (TRA) 2026 | Ertico","url":"https://www.ertico.com/transport-research-arena-tra-2026"},{"title":"THE TRAKA | Girona","url":"https://www.thetraka.com/"},{"title":"The Traka: Everything You Need To Know | Apidura","url":"https://www.apidura.com/journal/the-traka-everything-you-need-to-know/"},{"title":"Submit your proposal for TRA 2026! | Clean Aviation","url":"https://www.clean-aviation.eu/news-events/submit-your-proposal-for-tra-2026"},{"title":"The Traka edition 2026 | Battistrada","url":"https://battistrada.com/en/cycling-calendar/edition/the-traka-2026/48258/"},{"title":"Transport Research Arena conference - Mobility and Transport","url":"https://transport.ec.europa.eu/news-events/events/transport-research-arena-conference-2026-05-18_en"},{"title":"Gravel Events Calendar 2025–2026 | Find Gravel Races Worldwide","url":"https://gravelevents.com/event/the-traka/"},{"title":"TRAC 2025 – TRAC","url":"https://traceth.net/trac-2025/"}]

Based on the search results, here's what I found about TracVLA 2025 2026:

The search results primarily returned information about **The Traka**, a gravel cycling event in Girona, Spain. Here are the key details:

## The Traka 2025-2026 Events

The Traka was launched in 2021 and is organised by Klassmark, capitalising on Girona's rich cycling culture.

**2026 Schedule:**
The 2026 dates are:
- May 1, 2026 – The Traka Adventure (560km)
- May 1, 2026 – 360km race
- May 2, 2026 – 200km race
- May 3, 2026 – 100km race

The Traka invites amateur riders to compete alongside professional gravel racers, with no entry requirements, though entries run out quickly.

In 2026, five events around Europe will carry the "By The Traka" seal, offering riders the same authentic experience that defines Girona's gravel scene.

The Traka 360 is one of the top-scoring events in the Gravel Earth Series, awarding 1,000 points to the winner, while the Traka 200 awards 750 points to the winner.

If you were looking for information about a different "TracVLA" event, please let me know and I can search more specifically for that.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "6b7452c2-223a-46db-a382-87ba3826b143",
  "tool_use_result": {
    "query": "TracVLA 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LY8jqAGFVCa2hYDJoPBapb",
        "content": [
          {
            "title": "The Traka",
            "url": "https://www.granfondoguide.com/Events/Index/10556/the-traka"
          },
          {
            "title": "THE TRAKA 2026 in girona on April 30, 2026",
            "url": "https://web.rockthesport.com/en/event/the-traka-2026"
          },
          {
            "title": "Transport Research Arena (TRA) 2026 | Ertico",
            "url": "https://www.ertico.com/transport-research-arena-tra-2026"
          },
          {
            "title": "THE TRAKA | Girona",
            "url": "https://www.thetraka.com/"
          },
          {
            "title": "The Traka: Everything You Need To Know | Apidura",
            "url": "https://www.apidura.com/journal/the-traka-everything-you-need-to-know/"
          },
          {
            "title": "Submit your proposal for TRA 2026! | Clean Aviation",
            "url": "https://www.clean-aviation.eu/news-events/submit-your-proposal-for-tra-2026"
          },
          {
            "title": "The Traka edition 2026 | Battistrada",
            "url": "https://battistrada.com/en/cycling-calendar/edition/the-traka-2026/48258/"
          },
          {
            "title": "Transport Research Arena conference - Mobility and Transport",
            "url": "https://transport.ec.europa.eu/news-events/events/transport-research-arena-conference-2026-05-18_en"
          },
          {
            "title": "Gravel Events Calendar 2025–2026 | Find Gravel Races Worldwide",
            "url": "https://gravelevents.com/event/the-traka/"
          },
          {
            "title": "TRAC 2025 – TRAC",
            "url": "https://traceth.net/trac-2025/"
          }
        ]
      },
      "Based on the search results, here's what I found about TracVLA 2025 2026:\n\nThe search results primarily returned information about **The Traka**, a gravel cycling event in Girona, Spain. Here are the key details:\n\n## The Traka 2025-2026 Events\n\nThe Traka was launched in 2021 and is organised by Klassmark, capitalising on Girona's rich cycling culture.\n\n**2026 Schedule:**\nThe 2026 dates are:\n- May 1, 2026 – The Traka Adventure (560km)\n- May 1, 2026 – 360km race\n- May 2, 2026 – 200km race\n- May 3, 2026 – 100km race\n\nThe Traka invites amateur riders to compete alongside professional gravel racers, with no entry requirements, though entries run out quickly.\n\nIn 2026, five events around Europe will carry the \"By The Traka\" seal, offering riders the same authentic experience that defines Girona's gravel scene.\n\nThe Traka 360 is one of the top-scoring events in the Gravel Earth Series, awarding 1,000 points to the winner, while the Traka 200 awards 750 points to the winner.\n\nIf you were looking for information about a different \"TracVLA\" event, please let me know and I can search more specifically for that."
    ],
    "durationSeconds": 5.796840571000001
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T01:14:40.237Z_

<details><summary>↩ Tool result · `toolu_012i5W9r94A6T68YKnHkPoAx`</summary>

```text
Web search results for query: "instruction routing transformers attention head specialization VLA 2025 2026"

Links: [{"title":"Interpreting Transformers Through Attention Head Intervention","url":"https://arxiv.org/html/2601.04398v1"},{"title":"Directional Routing in Transformers","url":"https://arxiv.org/pdf/2603.14923"},{"title":"All-or-Here Attention in Transformers","url":"https://www.emergentmind.com/papers/2512.22562"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/html/2510.21518v2"},{"title":"Differentiation and Specialization of Attention Heads via the Refined   Local Learning Coefficient","url":"https://arxiv.org/pdf/2410.02984"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/pdf/2510.21518"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers | OpenReview","url":"https://openreview.net/forum?id=WQ9rnkaUWm"},{"title":"[2510.21518v1] Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/abs/2510.21518v1"}]

Based on the web search results, here's what I found regarding instruction routing, transformer attention head specialization, and VLAs in 2025-2026:

## Key Research Findings

**Attention Head Specialization in Vision-Language Models:**

Basile et al. (2025) introduced a method for identifying and manipulating attention heads specialized for semantic properties in both language and vision-language models. This work was published as a NeurIPS 2025 spotlight, demonstrating that attention heads in text-generative models specialize in semantic and visual concepts.

**Directional Routing Approach:**

A directional routing mechanism has been proposed where each attention head learns K=4 unit-norm direction vectors in head-space, and a shared 4-layer MLP router produces per-input weights that control how much of each directional component is removed from the head's output. This mechanism adds only 3.9% parameters and 0.02% FLOPs to a standard transformer.

**Circuit Analysis:**

Routing becomes the load-bearing computational mechanism, with analysis showing that in factual recall and induction circuits, routing is the single non-redundant component while individual attention heads are interchangeable.

The research demonstrates that modern transformers and vision-language models exhibit significant specialization patterns in their attention mechanisms, which can be leveraged for model interpretation and control through specialized routing mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "757a9d4c-8efc-48dd-9e13-043e0bcd24cd",
  "tool_use_result": {
    "query": "instruction routing transformers attention head specialization VLA 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013KesSH6j2BLGAuxuVMeBW2",
        "content": [
          {
            "title": "Interpreting Transformers Through Attention Head Intervention",
            "url": "https://arxiv.org/html/2601.04398v1"
          },
          {
            "title": "Directional Routing in Transformers",
            "url": "https://arxiv.org/pdf/2603.14923"
          },
          {
            "title": "All-or-Here Attention in Transformers",
            "url": "https://www.emergentmind.com/papers/2512.22562"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/html/2510.21518v2"
          },
          {
            "title": "Differentiation and Specialization of Attention Heads via the Refined   Local Learning Coefficient",
            "url": "https://arxiv.org/pdf/2410.02984"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/pdf/2510.21518"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers | OpenReview",
            "url": "https://openreview.net/forum?id=WQ9rnkaUWm"
          },
          {
            "title": "[2510.21518v1] Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/abs/2510.21518v1"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding instruction routing, transformer attention head specialization, and VLAs in 2025-2026:\n\n## Key Research Findings\n\n**Attention Head Specialization in Vision-Language Models:**\n\nBasile et al. (2025) introduced a method for identifying and manipulating attention heads specialized for semantic properties in both language and vision-language models. This work was published as a NeurIPS 2025 spotlight, demonstrating that attention heads in text-generative models specialize in semantic and visual concepts.\n\n**Directional Routing Approach:**\n\nA directional routing mechanism has been proposed where each attention head learns K=4 unit-norm direction vectors in head-space, and a shared 4-layer MLP router produces per-input weights that control how much of each directional component is removed from the head's output. This mechanism adds only 3.9% parameters and 0.02% FLOPs to a standard transformer.\n\n**Circuit Analysis:**\n\nRouting becomes the load-bearing computational mechanism, with analysis showing that in factual recall and induction circuits, routing is the single non-redundant component while individual attention heads are interchangeable.\n\nThe research demonstrates that modern transformers and vision-language models exhibit significant specialization patterns in their attention mechanisms, which can be leveraged for model interpretation and control through specialized routing mechanisms."
    ],
    "durationSeconds": 6.996244675
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T01:14:40.855Z_

<details><summary>↩ Tool result · `toolu_01X9UwzDc4E4XjsuCvDTVPwN`</summary>

```text
Web search results for query: "NORA VLA robot 2025 2026"

Links: [{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://declare-lab.github.io/nora"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/html/2504.19854v1"},{"title":"declare-lab/nora · Hugging Face","url":"https://huggingface.co/declare-lab/nora"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"[2504.19854] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/abs/2504.19854"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Robotics Center of Silicon Valley","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"GitHub - declare-lab/nora: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub","url":"https://github.com/declare-lab/nora"},{"title":"Paper page - NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://huggingface.co/papers/2504.19854"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"[Literature Review] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://www.themoonlight.io/en/review/nora-a-small-open-sourced-generalist-vision-language-action-model-for-embodied-tasks"}]

Based on the search results, here's what I found about NORA VLA robot:

## NORA: Vision-Language-Action Model

NORA is a 3B-parameter model designed to reduce computational overhead while maintaining strong task performance. NORA adopts the Qwen-2.5-VL-3B multimodal model as its backbone, leveraging its superior visual-semantic understanding to enhance visual reasoning and action grounding.

NORA is trained on 970k real-world robot demonstrations and equipped with the FAST+ tokenizer for efficient action sequence generation. Experimental results demonstrate that NORA outperforms existing large-scale VLA models, achieving better task performance with significantly reduced computational overhead, making it a more practical solution for real-time robotic autonomy.

## Key Features and Development

NORA is an open vision-language-action model trained on robot manipulation episodes from the Open X-Embodiment dataset. The model takes language instructions and camera images as input and generates robot actions. All NORA checkpoints, as well as the training codebase are released under an MIT License.

## Recent Updates (2025)

NORA-1.5 was announced as the new VLA model from the NORA family, achieving state-of-the-art performance on several benchmarks.

The model represents part of the broader growth in VLA technology adoption for robotics in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "6e1642db-f928-4c8a-85b7-133082ebe362",
  "tool_use_result": {
    "query": "NORA VLA robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FPCiTE71jVmtjB1QjUAx8h",
        "content": [
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://declare-lab.github.io/nora"
          },
          {
            "title": "NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://arxiv.org/html/2504.19854v1"
          },
          {
            "title": "declare-lab/nora · Hugging Face",
            "url": "https://huggingface.co/declare-lab/nora"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "[2504.19854] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://arxiv.org/abs/2504.19854"
          },
          {
            "title": "State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Robotics Center of Silicon Valley",
            "url": "https://www.roboticscenter.ai/state-of-robotics-2026"
          },
          {
            "title": "GitHub - declare-lab/nora: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub",
            "url": "https://github.com/declare-lab/nora"
          },
          {
            "title": "Paper page - NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://huggingface.co/papers/2504.19854"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "[Literature Review] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks",
            "url": "https://www.themoonlight.io/en/review/nora-a-small-open-sourced-generalist-vision-language-action-model-for-embodied-tasks"
          }
        ]
      },
      "Based on the search results, here's what I found about NORA VLA robot:\n\n## NORA: Vision-Language-Action Model\n\nNORA is a 3B-parameter model designed to reduce computational overhead while maintaining strong task performance. NORA adopts the Qwen-2.5-VL-3B multimodal model as its backbone, leveraging its superior visual-semantic understanding to enhance visual reasoning and action grounding.\n\nNORA is trained on 970k real-world robot demonstrations and equipped with the FAST+ tokenizer for efficient action sequence generation. Experimental results demonstrate that NORA outperforms existing large-scale VLA models, achieving better task performance with significantly reduced computational overhead, making it a more practical solution for real-time robotic autonomy.\n\n## Key Features and Development\n\nNORA is an open vision-language-action model trained on robot manipulation episodes from the Open X-Embodiment dataset. The model takes language instructions and camera images as input and generates robot actions. All NORA checkpoints, as well as the training codebase are released under an MIT License.\n\n## Recent Updates (2025)\n\nNORA-1.5 was announced as the new VLA model from the NORA family, achieving state-of-the-art performance on several benchmarks.\n\nThe model represents part of the broader growth in VLA technology adoption for robotics in 2025-2026."
    ],
    "durationSeconds": 6.094586585999999
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T01:14:40.884Z_

<details><summary>↩ Tool result · `toolu_01UbG8qze2xKJsmFzPJ78h2o`</summary>

```text
Web search results for query: "OpenVLA analysis interpretability 2025 2026"

Links: [{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://proceedings.mlr.press/v270/kim25c.html"},{"title":"Probing a Vision-Language-Action Model for Symbolic States and   Integration into a Cognitive Architecture","url":"https://arxiv.org/pdf/2502.04558"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"},{"title":"Emergent World Representations in OpenVLA | OpenReview","url":"https://openreview.net/forum?id=cydXirmduY"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"Mechanistic interpretability for steering vision-language-action models","url":"https://arxiv.org/pdf/2509.00328"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"}]

I've found several recent studies on OpenVLA analysis and interpretability from 2025-2026. Here are the key findings:

## Mechanistic Interpretability

Recent mechanistic interpretability analyses show that specific transformer neurons in OpenVLA correspond to semantic directions (e.g., "fast", "up"), and activation steering can causally modulate robot behavior at inference time without retraining.

## Emergent World Models

Studies indicate that OpenVLA encodes an emergent internal world model; probes reveal latent knowledge of state transitions consistent with Koopman operator theory, emerging as training progresses and scalable via Sparse Autoencoder analysis.

## Symbolic State Probing

Recent work probes OpenVLA's hidden layers to uncover symbolic representations of object properties, relations, and action states, enabling integration with cognitive architectures for enhanced interpretability and robustness. Probing results show consistently high accuracies (> 0.90) for both object and action states across most layers.

## Additional Developments

The FailSafe framework systematically generates failures and corrective actions; when integrated, OpenVLA's success rates increase by up to 22.6% and the policy generalizes across spatial, viewpoint, and embodiment variations.

These studies represent a significant push toward making OpenVLA's decision-making processes more transparent and controllable for robotics applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "647146e8-f9a7-4871-8ef8-14250abf4cd0",
  "tool_use_result": {
    "query": "OpenVLA analysis interpretability 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011h9s73G5EpK5r15FiuanH5",
        "content": [
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://proceedings.mlr.press/v270/kim25c.html"
          },
          {
            "title": "Probing a Vision-Language-Action Model for Symbolic States and   Integration into a Cognitive Architecture",
            "url": "https://arxiv.org/pdf/2502.04558"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview",
            "url": "https://openreview.net/forum?id=ZMnD6QZAE6"
          },
          {
            "title": "Emergent World Representations in OpenVLA | OpenReview",
            "url": "https://openreview.net/forum?id=cydXirmduY"
          },
          {
            "title": "Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation",
            "url": "https://arxiv.org/html/2603.16044v1"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/pdf/2406.09246"
          },
          {
            "title": "Mechanistic interpretability for steering vision-language-action models",
            "url": "https://arxiv.org/pdf/2509.00328"
          },
          {
            "title": "Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1566253525011248"
          }
        ]
      },
      "I've found several recent studies on OpenVLA analysis and interpretability from 2025-2026. Here are the key findings:\n\n## Mechanistic Interpretability\n\nRecent mechanistic interpretability analyses show that specific transformer neurons in OpenVLA correspond to semantic directions (e.g., \"fast\", \"up\"), and activation steering can causally modulate robot behavior at inference time without retraining.\n\n## Emergent World Models\n\nStudies indicate that OpenVLA encodes an emergent internal world model; probes reveal latent knowledge of state transitions consistent with Koopman operator theory, emerging as training progresses and scalable via Sparse Autoencoder analysis.\n\n## Symbolic State Probing\n\nRecent work probes OpenVLA's hidden layers to uncover symbolic representations of object properties, relations, and action states, enabling integration with cognitive architectures for enhanced interpretability and robustness. Probing results show consistently high accuracies (> 0.90) for both object and action states across most layers.\n\n## Additional Developments\n\nThe FailSafe framework systematically generates failures and corrective actions; when integrated, OpenVLA's success rates increase by up to 22.6% and the policy generalizes across spatial, viewpoint, and embodiment variations.\n\nThese studies represent a significant push toward making OpenVLA's decision-making processes more transparent and controllable for robotics applications."
    ],
    "durationSeconds": 7.123599930999998
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T01:14:42.158Z_

<details><summary>↩ Tool result · `toolu_01Uy28nrgHqbTzRkGTotXSTr`</summary>

```text
Web search results for query: "VLA mechanistic interpretability probing robot policy 2025 2026"

Links: [{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=YvsUD8C9QS"},{"title":"Controlling Vision–Language–Action Policies through Sparse Latent Directions | OpenReview","url":"https://openreview.net/forum?id=wtf3ww1EOL"},{"title":"Paper page - Mechanistic interpretability for steering vision-language-action models","url":"https://huggingface.co/papers/2509.00328"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/html/2603.19183v1"},{"title":"Mechanistic Interpretability for Steering Vision Language Action Models","url":"https://vla-mech-interp.github.io/"},{"title":"Mechanistic interpretability for steering vision-language-action models","url":"https://arxiv.org/pdf/2509.00328"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"}]

I found several highly relevant research papers on mechanistic interpretability for Vision-Language-Action (VLA) models and robot policies from 2025-2026. Here are the key findings:

## Primary Research Framework

The first framework for interpreting and steering VLAs via their internal representations enables direct intervention in model behavior at inference time. This method has been evaluated on two recent open-source VLAs, Pi0 and OpenVLA, and demonstrates zero-shot behavioral control in simulation (LIBERO) and on a physical robot (UR5), establishing a new paradigm for transparent and steerable foundation models in robotics.

## Technical Approach

The framework projects feedforward activations within transformer layers onto the token embedding basis, identifying sparse semantic directions—such as speed and direction—that are causally linked to action selection. An activation steering method modulates behavior in real time, without fine-tuning, reward signals, or environment interaction.

## Related Work

A complementary approach steers the language backbone of a Vision-Language-Action model in the Sparse Autoencoder's latent space to achieve fine-grained control of robotic policies, addressing the opacity that limits trust and safe deployment in robotics.

These papers represent significant advances in understanding and controlling the internal mechanisms of VLA models for more interpretable and steerable robot behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "97aa54c1-4ae0-4082-8ef3-4f21adc26532",
  "tool_use_result": {
    "query": "VLA mechanistic interpretability probing robot policy 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ug8B1VNy3kMNopPr8gvu8X",
        "content": [
          {
            "title": "Mechanistic Interpretability for Steering Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=YvsUD8C9QS"
          },
          {
            "title": "Controlling Vision–Language–Action Policies through Sparse Latent Directions | OpenReview",
            "url": "https://openreview.net/forum?id=wtf3ww1EOL"
          },
          {
            "title": "Paper page - Mechanistic interpretability for steering vision-language-action models",
            "url": "https://huggingface.co/papers/2509.00328"
          },
          {
            "title": "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models",
            "url": "https://arxiv.org/html/2603.19183v1"
          },
          {
            "title": "Mechanistic Interpretability for Steering Vision Language Action Models",
            "url": "https://vla-mech-interp.github.io/"
          },
          {
            "title": "Mechanistic interpretability for steering vision-language-action models",
            "url": "https://arxiv.org/pdf/2509.00328"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "Mechanistic Interpretability for Steering Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2509.00328v1"
          }
        ]
      },
      "I found several highly relevant research papers on mechanistic interpretability for Vision-Language-Action (VLA) models and robot policies from 2025-2026. Here are the key findings:\n\n## Primary Research Framework\n\nThe first framework for interpreting and steering VLAs via their internal representations enables direct intervention in model behavior at inference time. This method has been evaluated on two recent open-source VLAs, Pi0 and OpenVLA, and demonstrates zero-shot behavioral control in simulation (LIBERO) and on a physical robot (UR5), establishing a new paradigm for transparent and steerable foundation models in robotics.\n\n## Technical Approach\n\nThe framework projects feedforward activations within transformer layers onto the token embedding basis, identifying sparse semantic directions—such as speed and direction—that are causally linked to action selection. An activation steering method modulates behavior in real time, without fine-tuning, reward signals, or environment interaction.\n\n## Related Work\n\nA complementary approach steers the language backbone of a Vision-Language-Action model in the Sparse Autoencoder's latent space to achieve fine-grained control of robotic policies, addressing the opacity that limits trust and safe deployment in robotics.\n\nThese papers represent significant advances in understanding and controlling the internal mechanisms of VLA models for more interpretable and steerable robot behavior."
    ],
    "durationSeconds": 6.5630264280000015
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T01:14:43.152Z_

<details><summary>↩ Tool result · `toolu_01Kw3YM4ppyNDw37jN7B3HXM`</summary>

```text
Web search results for query: ""exit collapse" OR "representational collapse" fine-tuning language model 2025 2026"

Links: [{"title":"Representational de-collapse: Interactions between supervised finetuning and in-context learning in language models | OpenReview","url":"https://openreview.net/forum?id=iZ9eKf1ZCK"},{"title":"Better Fine-Tuning by Reducing Representational Collapse","url":"https://arxiv.org/pdf/2008.03156"},{"title":"Better Fine-Tuning by Reducing Representational Collapse | OpenReview","url":"https://openreview.net/forum?id=OQ08SN70M1V"},{"title":"Better Fine-Tuning by Reducing Representational Collapse | Request PDF","url":"https://www.researchgate.net/publication/343547031_Better_Fine-Tuning_by_Reducing_Representational_Collapse"},{"title":"Privacy Collapse: Benign Fine-Tuning Can Break Contextual Privacy in Language Models","url":"https://arxiv.org/pdf/2601.15220"},{"title":"Representation Projection Invariance Mitigates Representation Collapse","url":"https://arxiv.org/pdf/2205.11603"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model Training∗","url":"https://openreview.net/pdf?id=xpY3C8HxNh"},{"title":"CTRAP: Embedding Collapse Trap to Safeguard Large Language Models from Harmful Fine-Tuning","url":"https://arxiv.org/pdf/2505.16559"}]

I found several relevant research papers on representational collapse and related phenomena in fine-tuning language models from 2025-2026. Here are the key findings:

## Representational Collapse

Representational collapse refers to the degradation of generalizable representations from pre-trained models as they are fine-tuned for a specific end task. Fine-tuning can lead to representation degradation (also known as representation collapse), which may result in instability, sub-optimal performance, and weak generalization.

## Recent 2026 Research

A recent paper titled "Representational de-collapse: Interactions between supervised finetuning and in-context learning in language models" published in March 2026 addresses this issue. The research finds that supervised fine-tuning (SFT) collapses representations along task labels. However, it shows that in-context learning (ICL) can reverse this collapse and recover rich representations, akin to the pre-SFT model state.

## Related Phenomena (2025)

Another recent finding from January 2025 involves "privacy collapse." Privacy collapse is a new failure mode for large language models (LLMs). In finetuned models, the original ability to withhold personal details can be lost, and models lose their ability to reason about contextual privacy norms, share information inappropriately with tools, and violate memory boundaries across contexts.

These papers suggest ongoing research into understanding and mitigating various types of representation degradation during fine-tuning processes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "2ea79e33-c97e-4e55-860a-2255c2955b92",
  "tool_use_result": {
    "query": "\"exit collapse\" OR \"representational collapse\" fine-tuning language model 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SdzoDp3rCV9YWnNMzZ3gWy",
        "content": [
          {
            "title": "Representational de-collapse: Interactions between supervised finetuning and in-context learning in language models | OpenReview",
            "url": "https://openreview.net/forum?id=iZ9eKf1ZCK"
          },
          {
            "title": "Better Fine-Tuning by Reducing Representational Collapse",
            "url": "https://arxiv.org/pdf/2008.03156"
          },
          {
            "title": "Better Fine-Tuning by Reducing Representational Collapse | OpenReview",
            "url": "https://openreview.net/forum?id=OQ08SN70M1V"
          },
          {
            "title": "Better Fine-Tuning by Reducing Representational Collapse | Request PDF",
            "url": "https://www.researchgate.net/publication/343547031_Better_Fine-Tuning_by_Reducing_Representational_Collapse"
          },
          {
            "title": "Privacy Collapse: Benign Fine-Tuning Can Break Contextual Privacy in Language Models",
            "url": "https://arxiv.org/pdf/2601.15220"
          },
          {
            "title": "Representation Projection Invariance Mitigates Representation Collapse",
            "url": "https://arxiv.org/pdf/2205.11603"
          },
          {
            "title": "Escaping Collapse: The Strength of Weak Data for Large Language Model Training∗",
            "url": "https://openreview.net/pdf?id=xpY3C8HxNh"
          },
          {
            "title": "CTRAP: Embedding Collapse Trap to Safeguard Large Language Models from Harmful Fine-Tuning",
            "url": "https://arxiv.org/pdf/2505.16559"
          }
        ]
      },
      "I found several relevant research papers on representational collapse and related phenomena in fine-tuning language models from 2025-2026. Here are the key findings:\n\n## Representational Collapse\n\nRepresentational collapse refers to the degradation of generalizable representations from pre-trained models as they are fine-tuned for a specific end task. Fine-tuning can lead to representation degradation (also known as representation collapse), which may result in instability, sub-optimal performance, and weak generalization.\n\n## Recent 2026 Research\n\nA recent paper titled \"Representational de-collapse: Interactions between supervised finetuning and in-context learning in language models\" published in March 2026 addresses this issue. The research finds that supervised fine-tuning (SFT) collapses representations along task labels. However, it shows that in-context learning (ICL) can reverse this collapse and recover rich representations, akin to the pre-SFT model state.\n\n## Related Phenomena (2025)\n\nAnother recent finding from January 2025 involves \"privacy collapse.\" Privacy collapse is a new failure mode for large language models (LLMs). In finetuned models, the original ability to withhold personal details can be lost, and models lose their ability to reason about contextual privacy norms, share information inappropriately with tools, and violate memory boundaries across contexts.\n\nThese papers suggest ongoing research into understanding and mitigating various types of representation degradation during fine-tuning processes."
    ],
    "durationSeconds": 6.684565589
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T01:14:44.040Z_

<details><summary>↩ Tool result · `toolu_01NUgDZ57PHrAE323vGfC6DJ`</summary>

```text
Web search results for query: "robot action fine-tuning representation collapse 2025 2026"

Links: [{"title":"Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations","url":"https://arxiv.org/pdf/2512.08548"},{"title":"Better Fine-Tuning by Reducing Representational Collapse","url":"https://arxiv.org/pdf/2008.03156"},{"title":"D2PPO: Diffusion Policy Policy Optimization with Dispersive Loss","url":"https://arxiv.org/pdf/2508.02644"},{"title":"DM1: MeanFlow with Dispersive Regularization for 1-Step Robotic Manipulation","url":"https://arxiv.org/pdf/2510.07865"},{"title":"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/pdf/2509.11417"},{"title":"A Data-Efficient Visual-Audio Representation with Intuitive Fine-tuning   for Voice-Controlled Robots","url":"https://arxiv.org/pdf/2301.09749"},{"title":"CARE: Multi-Task Pretraining for Latent Continuous Action Representation in Robot Control","url":"https://arxiv.org/pdf/2601.22467"}]

I found several relevant papers on robot action fine-tuning and representation collapse from 2025-2026:

## Key Findings:

**Representation Collapse in Robotic Manipulation:**

Representation collapse occurs when distinct observations map to overly similar embeddings, which limits the capacity to capture diverse multi-modal behaviors and is particularly detrimental to fine-grained manipulation tasks requiring discrimination of subtle variations.

**Recent Research Approaches:**

1. **D2PPO (Diffusion Policy Policy Optimization):** This method introduces dispersive loss regularization that combats representation collapse by treating all hidden representations within each batch as negative pairs, compelling the network to learn discriminative representations of similar observations. On RoboMimic benchmarks, D2PPO achieves an average improvement of 22.7% in pretraining and 26.1% after fine-tuning.

2. **DM1 (MeanFlow with Dispersive Regularization):** The research addresses representation collapse by enforcing feature separation at intermediate representation layers during training, since the mean-velocity formulation does not explicitly encourage diversity among learned representations.

3. **Language-Based Action Representations:** Language-conditioned action learning leverages both visual and linguistic inputs to guide robot actions, enabling more flexible and versatile manipulation capabilities.

4. **CARE (Multi-Task Pretraining):** This novel pretraining strategy integrates latent action model training into the pre-training process of Vision Language Models.

These papers address the critical challenge of maintaining generalization during fine-tuning in robotic learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "3e92a249-67b0-407c-a247-94aaeea68573",
  "tool_use_result": {
    "query": "robot action fine-tuning representation collapse 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EnpcatGJk8nx6qpKooCpR3",
        "content": [
          {
            "title": "Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations",
            "url": "https://arxiv.org/pdf/2512.08548"
          },
          {
            "title": "Better Fine-Tuning by Reducing Representational Collapse",
            "url": "https://arxiv.org/pdf/2008.03156"
          },
          {
            "title": "D2PPO: Diffusion Policy Policy Optimization with Dispersive Loss",
            "url": "https://arxiv.org/pdf/2508.02644"
          },
          {
            "title": "DM1: MeanFlow with Dispersive Regularization for 1-Step Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2510.07865"
          },
          {
            "title": "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations",
            "url": "https://arxiv.org/pdf/2509.11417"
          },
          {
            "title": "A Data-Efficient Visual-Audio Representation with Intuitive Fine-tuning   for Voice-Controlled Robots",
            "url": "https://arxiv.org/pdf/2301.09749"
          },
          {
            "title": "CARE: Multi-Task Pretraining for Latent Continuous Action Representation in Robot Control",
            "url": "https://arxiv.org/pdf/2601.22467"
          }
        ]
      },
      "I found several relevant papers on robot action fine-tuning and representation collapse from 2025-2026:\n\n## Key Findings:\n\n**Representation Collapse in Robotic Manipulation:**\n\nRepresentation collapse occurs when distinct observations map to overly similar embeddings, which limits the capacity to capture diverse multi-modal behaviors and is particularly detrimental to fine-grained manipulation tasks requiring discrimination of subtle variations.\n\n**Recent Research Approaches:**\n\n1. **D2PPO (Diffusion Policy Policy Optimization):** This method introduces dispersive loss regularization that combats representation collapse by treating all hidden representations within each batch as negative pairs, compelling the network to learn discriminative representations of similar observations. On RoboMimic benchmarks, D2PPO achieves an average improvement of 22.7% in pretraining and 26.1% after fine-tuning.\n\n2. **DM1 (MeanFlow with Dispersive Regularization):** The research addresses representation collapse by enforcing feature separation at intermediate representation layers during training, since the mean-velocity formulation does not explicitly encourage diversity among learned representations.\n\n3. **Language-Based Action Representations:** Language-conditioned action learning leverages both visual and linguistic inputs to guide robot actions, enabling more flexible and versatile manipulation capabilities.\n\n4. **CARE (Multi-Task Pretraining):** This novel pretraining strategy integrates latent action model training into the pre-training process of Vision Language Models.\n\nThese papers address the critical challenge of maintaining generalization during fine-tuning in robotic learning systems."
    ],
    "durationSeconds": 7.827491818
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the search results and identify papers that are potentially relevant to our work. Let me do some follow-up searches for specific papers that seem highly relevant but need more details.

Key papers found so far:

1. **"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"** (arxiv 2603.19233) - This seems very relevant. It mentions 82+ manipulation concepts, Action Atlas, contrastive selection across 5 VLAs. Need more details.

2. **"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models"** (arxiv 2603.15618) - DeepVision-VLA, multi-level features from visual foundation models. Could be relevant.


3. **"Head Pursuit: Probing Attention Specialization in Multimodal Transformers"** (Basile et al., NeurIPS 2025) - This looks directly relevant to understanding how attention heads specialize across different modalities in VLMs. Also found several other papers on mechanistic interpretability and world model probing in VLAs, including work on symbolic state representations and steering mechanisms that could inform our analysis approach.

4. **"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations"** (arxiv 2509.11417) - This is particularly relevant since it addresses how to maintain pretrained representations during VLA fine-tuning, which connects to our findings about representation collapse. There's also a recent paper on representational de-collapse in language models that might provide useful context for understanding similar dynamics in VLAs.

Now I'm looking at a few more papers on policy optimization and routing mechanisms in transformers, plus some work on latent reasoning in VLAs. I should verify which of these are already in the citations and focus on the ones that directly address representation collapse or steering in vision-language-action models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "9c69d51b-3c27-468c-b716-fb816c3a20d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HdVnEWrdUx87WGLum2Ro2B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 783,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 24236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5819
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

_source line 25_

找到一些潜在相关论文，需要进一步确认细节。做几个跟进搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "d5908b08-ac72-4c68-adf6-d976fd3bb361",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HdVnEWrdUx87WGLum2Ro2B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 783,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 24236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5819
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PAuPNgPxJ1ZPjnNxFW4Vzd`</summary>

```json
{
  "query": "\"Not All Features Are Created Equal\" mechanistic study vision language action models 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "815e315a-1350-4478-b924-bb7284991bce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HdVnEWrdUx87WGLum2Ro2B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 783,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 24236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5819
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015fDmG8ASLRoAezAgJCbyDb`</summary>

```json
{
  "query": "\"Emergent World Representations in OpenVLA\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "b3b9ea0d-6734-454b-bb92-535a87db3afe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HdVnEWrdUx87WGLum2Ro2B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 783,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 24236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5819
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CN1hmWCSJRuvpUpCUJ9XNc`</summary>

```json
{
  "query": "\"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "d9684331-a58a-4c70-a660-191587ea6402",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HdVnEWrdUx87WGLum2Ro2B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 783,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 24236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5819
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Q5R1vybePFmV7a8gY7EYV`</summary>

```json
{
  "query": "\"representational de-collapse\" supervised finetuning in-context learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "a81a0bab-d2f7-4d66-8a33-c623094d4b80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HdVnEWrdUx87WGLum2Ro2B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 783,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 24236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5819
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01McEBeYyhfshWWQEPSbn4an`</summary>

```json
{
  "query": "\"Look Before Acting\" DeepVision-VLA vision foundation representations 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "76899bde-cf9f-49c0-869d-396975f0fe37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HdVnEWrdUx87WGLum2Ro2B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 783,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 24236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5819
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

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016zeMua1BxPyL7EaEtSPS3b`</summary>

```json
{
  "query": "\"Controlling Vision Language Action Policies through Sparse Latent Directions\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "ca8f967f-14c8-4899-9ddc-6136a293522f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HdVnEWrdUx87WGLum2Ro2B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 783,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 24236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5819
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

_source line 32 · 2026-05-24T01:15:15.538Z_

<details><summary>↩ Tool result · `toolu_015fDmG8ASLRoAezAgJCbyDb`</summary>

```text
Web search results for query: ""Emergent World Representations in OpenVLA" 2025 2026"

Links: [{"title":"[2509.24559] Emergent World Representations in OpenVLA","url":"https://arxiv.org/abs/2509.24559"},{"title":"[Literature Review] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://www.themoonlight.io/en/review/openvla-an-open-source-vision-language-action-model"},{"title":"EMERGENT WORLD REPRESENTATIONS IN OPENVLA","url":"https://openreview.net/pdf/29a8206275eccf26833ddd34ed0574aa804b52f8.pdf"},{"title":"Emergent World Representations in OpenVLA","url":"https://arxiv.org/pdf/2509.24559"},{"title":"[Literature Review] Emergent World Representations in OpenVLA","url":"https://www.themoonlight.io/en/review/emergent-world-representations-in-openvla"},{"title":"Emergent World Representations in OpenVLA","url":"https://arxiv.org/html/2509.24559v1"},{"title":"Emergent World Representations in OpenVLA | OpenReview","url":"https://openreview.net/forum?id=cydXirmduY"}]

I found research on "Emergent World Representations in OpenVLA." Here are the key findings:

## Overview
The paper investigates whether Vision Language Action models (VLAs) trained with policy-based reinforcement learning implicitly learn world models, a hallmark of model-based RL.

## Research Methodology
The researchers propose an experimental methodology using embedding arithmetic on state representations to probe whether OpenVLA contains latent knowledge of state transitions by measuring the difference between embeddings of sequential environment states and testing whether this transition vector is recoverable from intermediate model activations.

## Key Findings
Using linear and non-linear probes trained on activations across layers, the researchers found statistically significant predictive ability on state transitions exceeding baselines, indicating that OpenVLA encodes an internal world model.

Key results include: (1) the world model emerges in the middle layers; (2) pre-training on diverse datasets is essential; (3) linear probes outperform MLPs, supporting interpretable representations; and (4) predictive performance improves with longer time horizons.

## Additional Analysis
The researchers investigate the predictive ability of an earlier checkpoint of OpenVLA and uncover hints that the world model emerges as training progresses, and they outline a pipeline leveraging Sparse Autoencoders (SAEs) to analyze OpenVLA's world model.

The paper was submitted to ICLR 2026 and appeared on arXiv in September 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "527059c1-2642-4c3f-be94-addcff4a5799",
  "tool_use_result": {
    "query": "\"Emergent World Representations in OpenVLA\" 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P4Qm8T9xiJ56ZMEURHFARF",
        "content": [
          {
            "title": "[2509.24559] Emergent World Representations in OpenVLA",
            "url": "https://arxiv.org/abs/2509.24559"
          },
          {
            "title": "[Literature Review] OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://www.themoonlight.io/en/review/openvla-an-open-source-vision-language-action-model"
          },
          {
            "title": "EMERGENT WORLD REPRESENTATIONS IN OPENVLA",
            "url": "https://openreview.net/pdf/29a8206275eccf26833ddd34ed0574aa804b52f8.pdf"
          },
          {
            "title": "Emergent World Representations in OpenVLA",
            "url": "https://arxiv.org/pdf/2509.24559"
          },
          {
            "title": "[Literature Review] Emergent World Representations in OpenVLA",
            "url": "https://www.themoonlight.io/en/review/emergent-world-representations-in-openvla"
          },
          {
            "title": "Emergent World Representations in OpenVLA",
            "url": "https://arxiv.org/html/2509.24559v1"
          },
          {
            "title": "Emergent World Representations in OpenVLA | OpenReview",
            "url": "https://openreview.net/forum?id=cydXirmduY"
          }
        ]
      },
      "I found research on \"Emergent World Representations in OpenVLA.\" Here are the key findings:\n\n## Overview\nThe paper investigates whether Vision Language Action models (VLAs) trained with policy-based reinforcement learning implicitly learn world models, a hallmark of model-based RL.\n\n## Research Methodology\nThe researchers propose an experimental methodology using embedding arithmetic on state representations to probe whether OpenVLA contains latent knowledge of state transitions by measuring the difference between embeddings of sequential environment states and testing whether this transition vector is recoverable from intermediate model activations.\n\n## Key Findings\nUsing linear and non-linear probes trained on activations across layers, the researchers found statistically significant predictive ability on state transitions exceeding baselines, indicating that OpenVLA encodes an internal world model.\n\nKey results include: (1) the world model emerges in the middle layers; (2) pre-training on diverse datasets is essential; (3) linear probes outperform MLPs, supporting interpretable representations; and (4) predictive performance improves with longer time horizons.\n\n## Additional Analysis\nThe researchers investigate the predictive ability of an earlier checkpoint of OpenVLA and uncover hints that the world model emerges as training progresses, and they outline a pipeline leveraging Sparse Autoencoders (SAEs) to analyze OpenVLA's world model.\n\nThe paper was submitted to ICLR 2026 and appeared on arXiv in September 2025."
    ],
    "durationSeconds": 6.058957664000001
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T01:15:15.915Z_

<details><summary>↩ Tool result · `toolu_01PAuPNgPxJ1ZPjnNxFW4Vzd`</summary>

```text
Web search results for query: ""Not All Features Are Created Equal" mechanistic study vision language action models 2026 arxiv"

Links: [{"title":"[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=w8Mw9zJt1y"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://www.wispaper.ai/en/blog/not-all-features-created-equal-mechanistic-study-vision-language-action-models-20260320/zho"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233v1"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.19233"},{"title":"GitHub - CWRU-AISM/action-atlas: Mechanistic Interpretability toolkit for Vision-Language-Action models · GitHub","url":"https://github.com/CWRU-AISM/action-atlas"},{"title":"Not All Features Are Created Equal: A Mechani... | arXiv Physical AI Research Summary","url":"https://www.teahose.com/paper/arXiv%20Physical%20AI/Not%20All%20Features%20Are%20Created%20Equal_%20A%20Mechanistic%20Study%20of%20Vision-Language-Action%20Models"},{"title":"Robotics Research arXiv on X: \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models Bryce Grant, Xijia Zhao, Peng Wang https://t.co/Mr1IyrLxt9 [𝚌𝚜.𝚁𝙾] https://t.co/9LLIgjodQp\" / X","url":"https://x.com/OWW/status/2034850674173788594"}]

I found the paper you're looking for! Here's what the search revealed:

"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models" was published on March 19, 2026 by Bryce Grant and 2 other authors (arxiv:2603.19233).

**Key Details:**

The study presents the first cross-architecture mechanistic study of visuomotor policies, applying activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M to 7B parameters across 394,000+ rollout episodes on four benchmarks.

**Main Findings:**

The visual pathway dominates action generation—injecting baseline activations into null-prompt episodes recovers near-identical behavior across architectures, while trajectory analysis reveals that cross-task injection masks successful behavioral transfer, with robots executing source-task motor programs in the wrong scene (99.8% of X-VLA episodes align with the source trajectory).

Language sensitivity depends on task structure rather than model design: when visual context uniquely specifies the task, language is ignored; when multiple goals share a scene, language becomes essential.

You can access the full paper at https://arxiv.org/abs/2603.19233


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "896fc080-1731-49d3-87fb-687a02df97bf",
  "tool_use_result": {
    "query": "\"Not All Features Are Created Equal\" mechanistic study vision language action models 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_015wQCKCrgnnXfH2mLqFscz7",
        "content": [
          {
            "title": "[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.19233"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=w8Mw9zJt1y"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.19233"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://www.wispaper.ai/en/blog/not-all-features-created-equal-mechanistic-study-vision-language-action-models-20260320/zho"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.19233v1"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.19233"
          },
          {
            "title": "GitHub - CWRU-AISM/action-atlas: Mechanistic Interpretability toolkit for Vision-Language-Action models · GitHub",
            "url": "https://github.com/CWRU-AISM/action-atlas"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechani... | arXiv Physical AI Research Summary",
            "url": "https://www.teahose.com/paper/arXiv%20Physical%20AI/Not%20All%20Features%20Are%20Created%20Equal_%20A%20Mechanistic%20Study%20of%20Vision-Language-Action%20Models"
          },
          {
            "title": "Robotics Research arXiv on X: \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models Bryce Grant, Xijia Zhao, Peng Wang https://t.co/Mr1IyrLxt9 [𝚌𝚜.𝚁𝙾] https://t.co/9LLIgjodQp\" / X",
            "url": "https://x.com/OWW/status/2034850674173788594"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\n\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\" was published on March 19, 2026 by Bryce Grant and 2 other authors (arxiv:2603.19233).\n\n**Key Details:**\n\nThe study presents the first cross-architecture mechanistic study of visuomotor policies, applying activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M to 7B parameters across 394,000+ rollout episodes on four benchmarks.\n\n**Main Findings:**\n\nThe visual pathway dominates action generation—injecting baseline activations into null-prompt episodes recovers near-identical behavior across architectures, while trajectory analysis reveals that cross-task injection masks successful behavioral transfer, with robots executing source-task motor programs in the wrong scene (99.8% of X-VLA episodes align with the source trajectory).\n\nLanguage sensitivity depends on task structure rather than model design: when visual context uniquely specifies the task, language is ignored; when multiple goals share a scene, language becomes essential.\n\nYou can access the full paper at https://arxiv.org/abs/2603.19233"
    ],
    "durationSeconds": 6.996435581999998
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-24T01:15:16.171Z_

<details><summary>↩ Tool result · `toolu_01CN1hmWCSJRuvpUpCUJ9XNc`</summary>

```text
Web search results for query: ""Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" 2025"

Links: [{"title":"Enhancing Generalization in Vision-Language-Action Models","url":"https://gen-vla.github.io/"},{"title":"[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/abs/2509.11417"},{"title":"[PDF] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Enhancing-Generalization-in-Vision-Language-Action-Grover-Gopalkrishnan/272525654b60ab7f4366e58244feadcfd2675aaf"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"Enhancing Generalization in Vision-Language-Action ...","url":"https://arxiv.org/pdf/2509.11417"},{"title":"MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization","url":"https://arxiv.org/pdf/2511.19878"}]

Based on the search results, here's information about the paper "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" (2025):

## Overview

The paper is authored by Grover, Gopalkrishnan, Ai, Christensen, Su, and Li, and was published as arXiv preprint arXiv:2509.11417 in 2025. Vision-language-action (VLA) models, finetuned from powerful pretrained vision-language models (VLMs), promise to create generalist robots.

## Problem Statement

However, the finetuning process often degrades the very representations that make them powerful, limiting generalization.

## Proposed Solution

The approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances.

## Results

Evaluations in simulation and on real robots show that the method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "76810737-af66-4076-bcad-abd032ded6d7",
  "tool_use_result": {
    "query": "\"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations\" 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UUyKGFmcutrhEcqyHXDV76",
        "content": [
          {
            "title": "Enhancing Generalization in Vision-Language-Action Models",
            "url": "https://gen-vla.github.io/"
          },
          {
            "title": "[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations",
            "url": "https://arxiv.org/abs/2509.11417"
          },
          {
            "title": "[PDF] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Enhancing-Generalization-in-Vision-Language-Action-Grover-Gopalkrishnan/272525654b60ab7f4366e58244feadcfd2675aaf"
          },
          {
            "title": "Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations",
            "url": "https://arxiv.org/html/2509.11417v1"
          },
          {
            "title": "Enhancing Generalization in Vision-Language-Action ...",
            "url": "https://arxiv.org/pdf/2509.11417"
          },
          {
            "title": "MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization",
            "url": "https://arxiv.org/pdf/2511.19878"
          }
        ]
      },
      "Based on the search results, here's information about the paper \"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations\" (2025):\n\n## Overview\n\nThe paper is authored by Grover, Gopalkrishnan, Ai, Christensen, Su, and Li, and was published as arXiv preprint arXiv:2509.11417 in 2025. Vision-language-action (VLA) models, finetuned from powerful pretrained vision-language models (VLMs), promise to create generalist robots.\n\n## Problem Statement\n\nHowever, the finetuning process often degrades the very representations that make them powerful, limiting generalization.\n\n## Proposed Solution\n\nThe approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances.\n\n## Results\n\nEvaluations in simulation and on real robots show that the method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines."
    ],
    "durationSeconds": 6.175785560999997
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T01:15:16.641Z_

<details><summary>↩ Tool result · `toolu_01McEBeYyhfshWWQEPSbn4an`</summary>

```text
Web search results for query: ""Look Before Acting" DeepVision-VLA vision foundation representations 2026"

Links: [{"title":"[2603.15618] Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.15618"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://deepvision-vla.github.io/"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.15618v2"},{"title":"Paper page - Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://huggingface.co/papers/2603.15618"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.15618"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/402482266_Look_Before_Acting_Enhancing_Vision_Foundation_Representations_for_Vision-Language-Action_Models"}]

I found relevant results for your search. Here's what I found about "Look Before Acting" and DeepVision-VLA:

## Overview

"Look Before Acting" is a research paper on Vision-Language-Action (VLA) models, which have emerged as a promising paradigm for robotic manipulation, where reliable action prediction depends on accurately interpreting and integrating visual observations conditioned on language instructions.

## Key Problem and Solution

Most approaches treat the LLM backbone as a black box with limited insight into how visual information is grounded into action generation, and the researchers observed that sensitivity to visual tokens progressively decreases in deeper layers during action generation.

The solution is DeepVision-VLA, built on a Vision-Language Mixture-of-Transformers (VL-MoT) framework that enables shared attention between the vision foundation model and the VLA backbone, injecting multi-level visual features into deeper layers to enhance visual representations for precise manipulation.

## Key Components

The framework introduces Action-Guided Visual Pruning (AGVP), which leverages shallow-layer attention to prune irrelevant visual tokens while preserving task-relevant ones, with minimal computational overhead.

## Results

DeepVision-VLA outperforms prior state-of-the-art methods by 9.0% and 7.5% on simulated and real-world tasks, respectively.

The paper was published on arXiv on March 17, 2026, with the arXiv identifier 2603.15618.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "f0a07cf7-5831-44b2-a017-02b9449f65b1",
  "tool_use_result": {
    "query": "\"Look Before Acting\" DeepVision-VLA vision foundation representations 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AKS9qP5yuE1VJ9PHSG5kGp",
        "content": [
          {
            "title": "[2603.15618] Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.15618"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://deepvision-vla.github.io/"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.15618v2"
          },
          {
            "title": "Paper page - Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2603.15618"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.15618"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/402482266_Look_Before_Acting_Enhancing_Vision_Foundation_Representations_for_Vision-Language-Action_Models"
          }
        ]
      },
      "I found relevant results for your search. Here's what I found about \"Look Before Acting\" and DeepVision-VLA:\n\n## Overview\n\n\"Look Before Acting\" is a research paper on Vision-Language-Action (VLA) models, which have emerged as a promising paradigm for robotic manipulation, where reliable action prediction depends on accurately interpreting and integrating visual observations conditioned on language instructions.\n\n## Key Problem and Solution\n\nMost approaches treat the LLM backbone as a black box with limited insight into how visual information is grounded into action generation, and the researchers observed that sensitivity to visual tokens progressively decreases in deeper layers during action generation.\n\nThe solution is DeepVision-VLA, built on a Vision-Language Mixture-of-Transformers (VL-MoT) framework that enables shared attention between the vision foundation model and the VLA backbone, injecting multi-level visual features into deeper layers to enhance visual representations for precise manipulation.\n\n## Key Components\n\nThe framework introduces Action-Guided Visual Pruning (AGVP), which leverages shallow-layer attention to prune irrelevant visual tokens while preserving task-relevant ones, with minimal computational overhead.\n\n## Results\n\nDeepVision-VLA outperforms prior state-of-the-art methods by 9.0% and 7.5% on simulated and real-world tasks, respectively.\n\nThe paper was published on arXiv on March 17, 2026, with the arXiv identifier 2603.15618."
    ],
    "durationSeconds": 5.710029352999998
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T01:15:17.541Z_

<details><summary>↩ Tool result · `toolu_018Q5R1vybePFmV7a8gY7EYV`</summary>

```text
Web search results for query: ""representational de-collapse" supervised finetuning in-context learning 2026"

Links: [{"title":"Representational de-collapse: Interactions between supervised finetuning and in-context learning in language models | OpenReview","url":"https://openreview.net/forum?id=iZ9eKf1ZCK"},{"title":"Better Fine-Tuning by Reducing Representational Collapse | OpenReview","url":"https://openreview.net/forum?id=OQ08SN70M1V"},{"title":"[2603.11201] Representation Finetuning for Continual Learning","url":"https://arxiv.org/abs/2603.11201"},{"title":"Better Fine-Tuning by Reducing Representational Collapse","url":"https://arxiv.org/pdf/2008.03156"},{"title":"Representation Projection Invariance Mitigates Representation Collapse","url":"https://arxiv.org/pdf/2205.11603"},{"title":"Better Fine-Tuning by Reducing Representational Collapse | Request PDF","url":"https://www.researchgate.net/publication/343547031_Better_Fine-Tuning_by_Reducing_Representational_Collapse"},{"title":"[2008.03156] Better Fine-Tuning by Reducing Representational Collapse","url":"https://arxiv.org/abs/2008.03156"},{"title":"Context Collapse: In-Context Learning and Model Collapse","url":"https://arxiv.org/pdf/2601.00923"},{"title":"Context Structure Reshapes the Representational Geometry of Language Models","url":"https://arxiv.org/pdf/2601.22364"}]

Based on the search results, here's what I found about "representational de-collapse" in relation to supervised finetuning and in-context learning:

The most directly relevant work is a 2026 ICLR paper titled "Representational de-collapse: Interactions between supervised finetuning and in-context learning in language models," published on March 2, 2026.

The key findings from this research are:

The paper examines how supervised fine-tuning (SFT) is used for safety alignment of language models, but notes that SFT is brittle and can be circumvented through in-context learning (ICL), where models learn from in-context demonstrations to overwrite previously acquired safety guardrails.

The researchers found that SFT collapses representations along task labels, but that ICL can reverse this collapse and recover rich representations, akin to the pre-SFT model state. This phenomenon of ICL reversing the representational collapse caused by SFT is what the "representational de-collapse" concept refers to.

The paper also demonstrates that the overwriting behavior of SFT by ICL scales with model size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "ff5f0be0-e810-4acb-bf30-32090aa48947",
  "tool_use_result": {
    "query": "\"representational de-collapse\" supervised finetuning in-context learning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0147tRKoNHX96gmbZBcomexG",
        "content": [
          {
            "title": "Representational de-collapse: Interactions between supervised finetuning and in-context learning in language models | OpenReview",
            "url": "https://openreview.net/forum?id=iZ9eKf1ZCK"
          },
          {
            "title": "Better Fine-Tuning by Reducing Representational Collapse | OpenReview",
            "url": "https://openreview.net/forum?id=OQ08SN70M1V"
          },
          {
            "title": "[2603.11201] Representation Finetuning for Continual Learning",
            "url": "https://arxiv.org/abs/2603.11201"
          },
          {
            "title": "Better Fine-Tuning by Reducing Representational Collapse",
            "url": "https://arxiv.org/pdf/2008.03156"
          },
          {
            "title": "Representation Projection Invariance Mitigates Representation Collapse",
            "url": "https://arxiv.org/pdf/2205.11603"
          },
          {
            "title": "Better Fine-Tuning by Reducing Representational Collapse | Request PDF",
            "url": "https://www.researchgate.net/publication/343547031_Better_Fine-Tuning_by_Reducing_Representational_Collapse"
          },
          {
            "title": "[2008.03156] Better Fine-Tuning by Reducing Representational Collapse",
            "url": "https://arxiv.org/abs/2008.03156"
          },
          {
            "title": "Context Collapse: In-Context Learning and Model Collapse",
            "url": "https://arxiv.org/pdf/2601.00923"
          },
          {
            "title": "Context Structure Reshapes the Representational Geometry of Language Models",
            "url": "https://arxiv.org/pdf/2601.22364"
          }
        ]
      },
      "Based on the search results, here's what I found about \"representational de-collapse\" in relation to supervised finetuning and in-context learning:\n\nThe most directly relevant work is a 2026 ICLR paper titled \"Representational de-collapse: Interactions between supervised finetuning and in-context learning in language models,\" published on March 2, 2026.\n\nThe key findings from this research are:\n\nThe paper examines how supervised fine-tuning (SFT) is used for safety alignment of language models, but notes that SFT is brittle and can be circumvented through in-context learning (ICL), where models learn from in-context demonstrations to overwrite previously acquired safety guardrails.\n\nThe researchers found that SFT collapses representations along task labels, but that ICL can reverse this collapse and recover rich representations, akin to the pre-SFT model state. This phenomenon of ICL reversing the representational collapse caused by SFT is what the \"representational de-collapse\" concept refers to.\n\nThe paper also demonstrates that the overwriting behavior of SFT by ICL scales with model size."
    ],
    "durationSeconds": 7.073665924000001
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T01:15:18.193Z_

<details><summary>↩ Tool result · `toolu_016zeMua1BxPyL7EaEtSPS3b`</summary>

```text
Web search results for query: ""Controlling Vision Language Action Policies through Sparse Latent Directions" 2025 2026"

Links: [{"title":"Controlling Vision–Language–Action Policies through Sparse Latent Directions | OpenReview","url":"https://openreview.net/forum?id=wtf3ww1EOL"},{"title":"LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Vision-Language-Action Policies","url":"https://www.emergentmind.com/topics/vision-language-action-policies"},{"title":"Latent Action Models Overview","url":"https://www.emergentmind.com/topics/latent-action-models"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/pdf/2512.06951"},{"title":"Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation","url":"https://arxiv.org/html/2512.20188v1"}]

I found the research paper you're looking for! Here are the details:

**Paper Title:** Controlling Vision–Language–Action Policies through Sparse Latent Directions

**Publication Date:** Published September 30, 2025

**Venue:** Mech Interp Workshop (NeurIPS 2025) Poster

**Key Contribution:** The work shows that discrete robot actions can be steered by identifying a small number of meaningful features inside the residual stream of a VLA policy.

**Problem Addressed:** Vision–language–action (VLA) agents combine perception, language, and control to perform general-purpose tasks, but their internal decision-making is poorly understood and hard to steer. This opacity limits trust and safe deployment in robotics (i.e., embodied AI).

**Technical Approach:** The paper steers the language backbone of a Vision-Language-Action model in the Sparse Autoencoder's latent space, achieving fine-grained control of robotic policies in the robot action space.

The paper is available on OpenReview at: https://openreview.net/forum?id=wtf3ww1EOL


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "9ed9379e-a0e5-496d-9d28-82f73f265bd8",
  "tool_use_result": {
    "query": "\"Controlling Vision Language Action Policies through Sparse Latent Directions\" 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BRGDvTcwa43pGBnh4NrCdn",
        "content": [
          {
            "title": "Controlling Vision–Language–Action Policies through Sparse Latent Directions | OpenReview",
            "url": "https://openreview.net/forum?id=wtf3ww1EOL"
          },
          {
            "title": "LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "Vision-Language-Action Policies",
            "url": "https://www.emergentmind.com/topics/vision-language-action-policies"
          },
          {
            "title": "Latent Action Models Overview",
            "url": "https://www.emergentmind.com/topics/latent-action-models"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/pdf/2512.06951"
          },
          {
            "title": "Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation",
            "url": "https://arxiv.org/html/2512.20188v1"
          }
        ]
      },
      "I found the research paper you're looking for! Here are the details:\n\n**Paper Title:** Controlling Vision–Language–Action Policies through Sparse Latent Directions\n\n**Publication Date:** Published September 30, 2025\n\n**Venue:** Mech Interp Workshop (NeurIPS 2025) Poster\n\n**Key Contribution:** The work shows that discrete robot actions can be steered by identifying a small number of meaningful features inside the residual stream of a VLA policy.\n\n**Problem Addressed:** Vision–language–action (VLA) agents combine perception, language, and control to perform general-purpose tasks, but their internal decision-making is poorly understood and hard to steer. This opacity limits trust and safe deployment in robotics (i.e., embodied AI).\n\n**Technical Approach:** The paper steers the language backbone of a Vision-Language-Action model in the Sparse Autoencoder's latent space, achieving fine-grained control of robotic policies in the robot action space.\n\nThe paper is available on OpenReview at: https://openreview.net/forum?id=wtf3ww1EOL"
    ],
    "durationSeconds": 6.446858184999997
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now let me do a few more targeted searches for papers I might have missed, and to confirm whether some of these are already cited papers.

Let me check:
1. Grant et al. 2026 - "Not All Features Are Created Equal" - yes, this is Grant et al. 2026 which is ALREADY CITED
2. "Controlling Vision–Language–Action Policies through Sparse Latent Directions" - this might be the same as Haon et al. 2025 or a different paper. Let me check.
3. "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models" (2603.19183) - might be Swann et al. 2026


Looking more carefully at Grant et al., it's definitely the same paper already cited for visual dominance. For the "Controlling Vision–Language–Action Policies" paper, I need to determine if it's distinct from Haon et al. 2025 on mechanistic interpretability for steering VLAs, or if they're the same work.

Now I'm searching for several other specific papers and topics to fill in gaps: the MAPS paper on module-wise proximity scheduling, confirming whether Fang et al. 2025 on reasoning erosion is already cited, VLA layer-wise probing analysis, and representation forgetting in fine-tuning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "c40bfde4-898d-423a-960c-33cd2a10601a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qYUk9MLz39yVUTJGr1P4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6427,
      "cache_read_input_tokens": 30055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6427
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

_source line 39_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011jbCbZuhCs5L6qLz4M9sgk`</summary>

```json
{
  "query": "MAPS \"Module-Wise Proximity Scheduling\" VLA generalization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "5a6548b2-05a0-42a2-9d40-e2773c70b2dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qYUk9MLz39yVUTJGr1P4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6427,
      "cache_read_input_tokens": 30055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6427
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

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017PkmxKAnHSPShjhR3eVvRb`</summary>

```json
{
  "query": "\"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA\" 2026 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "1bace74a-3bdf-42c6-94cb-7ae935bf95f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qYUk9MLz39yVUTJGr1P4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6427,
      "cache_read_input_tokens": 30055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6427
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

_source line 41_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFCBWW7eQkLRMvd7JewbQx`</summary>

```json
{
  "query": "VLA probing layer-wise analysis action prediction robot manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "5a3bc4f4-e085-4859-be63-506092ffa7ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qYUk9MLz39yVUTJGr1P4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6427,
      "cache_read_input_tokens": 30055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6427
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

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DMT2xNsPELnwGim5FHkhrZ`</summary>

```json
{
  "query": "\"Head Pursuit\" attention specialization multimodal transformers Basile 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "1ad96b3d-45ae-4a98-b25b-89c47d71f87c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qYUk9MLz39yVUTJGr1P4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6427,
      "cache_read_input_tokens": 30055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6427
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

_source line 43_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EpQpzo4ydPgNkqcWU5iHGk`</summary>

```json
{
  "query": "VLA fine-tuning forgetting catastrophic pretrained knowledge robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "95e64303-58f8-4d8d-9150-751183f1466f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qYUk9MLz39yVUTJGr1P4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6427,
      "cache_read_input_tokens": 30055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6427
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F889NP1Zrk8mrGFRKZN9vk`</summary>

```json
{
  "query": "\"reasoning erosion\" VLM fine-tuning Fang 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "94289170-301c-4dac-b8a1-c64c10871c38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qYUk9MLz39yVUTJGr1P4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6427,
      "cache_read_input_tokens": 30055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6427
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

_source line 45 · 2026-05-24T01:15:39.360Z_

<details><summary>↩ Tool result · `toolu_017PkmxKAnHSPShjhR3eVvRb`</summary>

```text
Web search results for query: ""Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA" 2026 authors"

Links: [{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.19183"},{"title":"[2603.19183] Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/abs/2603.19183"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/html/2603.19183v1"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable ...","url":"https://drvla.github.io/"},{"title":"[2512.10805] Interpretable and Steerable Concept Bottleneck Sparse Autoencoders","url":"https://arxiv.org/abs/2512.10805"},{"title":"SPARSE AUTOENCODERS REVEAL INTERPRETABLE ...","url":"https://openreview.net/pdf?id=5AuN6RD072"}]

Based on the search results, I found the paper you're looking for. The paper "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models" is authored by Aiden Swann and 4 other authors. The paper was published on March 19, 2026, according to the arXiv listing.

The search results from arXiv show the paper with the identifier 2603.19183, but the complete author list beyond Aiden Swann is not fully displayed in these search result excerpts. You can find the complete author list by visiting the full arXiv page at https://arxiv.org/abs/2603.19183.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "1b8b4237-310a-46ca-a7c1-52113b10aed5",
  "tool_use_result": {
    "query": "\"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA\" 2026 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_015qNGXTM6JMh4u7qbrUNFHv",
        "content": [
          {
            "title": "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.19183"
          },
          {
            "title": "[2603.19183] Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models",
            "url": "https://arxiv.org/abs/2603.19183"
          },
          {
            "title": "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models",
            "url": "https://arxiv.org/html/2603.19183v1"
          },
          {
            "title": "Sparse Autoencoders Reveal Interpretable and Steerable ...",
            "url": "https://drvla.github.io/"
          },
          {
            "title": "[2512.10805] Interpretable and Steerable Concept Bottleneck Sparse Autoencoders",
            "url": "https://arxiv.org/abs/2512.10805"
          },
          {
            "title": "SPARSE AUTOENCODERS REVEAL INTERPRETABLE ...",
            "url": "https://openreview.net/pdf?id=5AuN6RD072"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. The paper \"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models\" is authored by Aiden Swann and 4 other authors. The paper was published on March 19, 2026, according to the arXiv listing.\n\nThe search results from arXiv show the paper with the identifier 2603.19183, but the complete author list beyond Aiden Swann is not fully displayed in these search result excerpts. You can find the complete author list by visiting the full arXiv page at https://arxiv.org/abs/2603.19183."
    ],
    "durationSeconds": 4.3550525009999985
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-24T01:15:41.232Z_

<details><summary>↩ Tool result · `toolu_011jbCbZuhCs5L6qLz4M9sgk`</summary>

```text
Web search results for query: "MAPS "Module-Wise Proximity Scheduling" VLA generalization 2025 2026"

Links: [{"title":"MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization","url":"https://arxiv.org/pdf/2511.19878"},{"title":"[2511.19878] MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization","url":"https://arxiv.org/abs/2511.19878"},{"title":"NoTVLA: Semantics-Preserving Robot Adaptation via Narrative Action Interfaces","url":"https://arxiv.org/html/2510.03895"},{"title":"FUTURE-VLA: Forecasting Unified Trajectories Under Real-time Execution","url":"https://arxiv.org/pdf/2602.15882"},{"title":"arXiv:2506.24044v1 [cs.CV] 30 Jun 2025","url":"https://arxiv.org/pdf/2506.24044"}]

Based on the search results, I found relevant information about MAPS and VLA generalization:

MAPS (Module-Wise Proximity Scheduling) is the first robust fine-tuning framework for VLAs (Vision-Language-Action models). MAPS addresses how Vision-Language-Action models inherit strong priors from pretrained Vision-Language Models, but naive fine-tuning often disrupts these representations and harms generalization.

Through systematic analysis, the framework uncovers an empirical order in which proximity constraints should be relaxed to balance stability and flexibility, with MAPS linearly scheduling this relaxation to enable visual encoders to stay close to their pretrained priors while action-oriented language layers adapt more freely.

MAPS introduces no additional parameters or data, and can be seamlessly integrated into existing VLAs. Across MiniVLA-VQ, MiniVLA-OFT, OpenVLA-OFT, and challenging benchmarks such as SimplerEnv, CALVIN, LIBERO, as well as real-world evaluations on the Franka Emika Panda platform, MAPS consistently boosts both in-distribution and out-of-distribution performance (up to +30%).

The paper was posted on arXiv in November 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "aa7f6f9c-013a-4d38-84d9-5e17ca7d9ef3",
  "tool_use_result": {
    "query": "MAPS \"Module-Wise Proximity Scheduling\" VLA generalization 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H43rbm71pwSBiEgKi1HHu8",
        "content": [
          {
            "title": "MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization",
            "url": "https://arxiv.org/pdf/2511.19878"
          },
          {
            "title": "[2511.19878] MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization",
            "url": "https://arxiv.org/abs/2511.19878"
          },
          {
            "title": "NoTVLA: Semantics-Preserving Robot Adaptation via Narrative Action Interfaces",
            "url": "https://arxiv.org/html/2510.03895"
          },
          {
            "title": "FUTURE-VLA: Forecasting Unified Trajectories Under Real-time Execution",
            "url": "https://arxiv.org/pdf/2602.15882"
          },
          {
            "title": "arXiv:2506.24044v1 [cs.CV] 30 Jun 2025",
            "url": "https://arxiv.org/pdf/2506.24044"
          }
        ]
      },
      "Based on the search results, I found relevant information about MAPS and VLA generalization:\n\nMAPS (Module-Wise Proximity Scheduling) is the first robust fine-tuning framework for VLAs (Vision-Language-Action models). MAPS addresses how Vision-Language-Action models inherit strong priors from pretrained Vision-Language Models, but naive fine-tuning often disrupts these representations and harms generalization.\n\nThrough systematic analysis, the framework uncovers an empirical order in which proximity constraints should be relaxed to balance stability and flexibility, with MAPS linearly scheduling this relaxation to enable visual encoders to stay close to their pretrained priors while action-oriented language layers adapt more freely.\n\nMAPS introduces no additional parameters or data, and can be seamlessly integrated into existing VLAs. Across MiniVLA-VQ, MiniVLA-OFT, OpenVLA-OFT, and challenging benchmarks such as SimplerEnv, CALVIN, LIBERO, as well as real-world evaluations on the Franka Emika Panda platform, MAPS consistently boosts both in-distribution and out-of-distribution performance (up to +30%).\n\nThe paper was posted on arXiv in November 2025."
    ],
    "durationSeconds": 6.587911810000005
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-24T01:15:42.470Z_

<details><summary>↩ Tool result · `toolu_01SFCBWW7eQkLRMvd7JewbQx`</summary>

```text
Web search results for query: "VLA probing layer-wise analysis action prediction robot manipulation 2025 2026"

Links: [{"title":"DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation","url":"https://arxiv.org/html/2602.22896"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.15618v2"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.19233"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.01166v2"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"}]

The search results contain several highly relevant papers on VLA (Vision-Language-Action) models for robot manipulation from 2025-2026. Here are the key findings:

## Layer-wise Analysis and Action Prediction

Recent work conducts comprehensive analysis of layer-wise performance and action importance variations in VLA prediction. Specifically, DySL-VLA proposes to accelerate VLA inference via dynamic-static layer skipping.

## Mechanistic and Interpretability Studies

Research has demonstrated SAE steering on VLA models, probed for emergent world models, and explored mechanistic interpretability approaches to understand how features contribute to action generation.

## Vision Processing in VLAs

Existing paradigms often treat visual processing within VLA models as a black box, but recent work proposes integrating multi-level features from visual foundation models into deeper VLA layers via a Vision-Language Mixture-of-Transformers architecture.

## Recent VLA Developments

VLA models have seen extensive efforts devoted to architectural advances as well as training- and inference-time optimizations since the introduction of RT-2. Recent systematic reviews organize more than 100 VLA architectures and analyze their design choices.

These papers represent cutting-edge research on understanding and improving VLA models for robot manipulation tasks in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "f87c68fa-6743-45ec-85c3-258fbc72b2e1",
  "tool_use_result": {
    "query": "VLA probing layer-wise analysis action prediction robot manipulation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SR6gE7PHaDyAywnKbVqxgE",
        "content": [
          {
            "title": "DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation",
            "url": "https://arxiv.org/html/2602.22896"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.15618v2"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.19233"
          },
          {
            "title": "Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1566253525011248"
          },
          {
            "title": "Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.01166v2"
          },
          {
            "title": "2026-01-28 Work in progress.",
            "url": "https://arxiv.org/pdf/2601.15197"
          }
        ]
      },
      "The search results contain several highly relevant papers on VLA (Vision-Language-Action) models for robot manipulation from 2025-2026. Here are the key findings:\n\n## Layer-wise Analysis and Action Prediction\n\nRecent work conducts comprehensive analysis of layer-wise performance and action importance variations in VLA prediction. Specifically, DySL-VLA proposes to accelerate VLA inference via dynamic-static layer skipping.\n\n## Mechanistic and Interpretability Studies\n\nResearch has demonstrated SAE steering on VLA models, probed for emergent world models, and explored mechanistic interpretability approaches to understand how features contribute to action generation.\n\n## Vision Processing in VLAs\n\nExisting paradigms often treat visual processing within VLA models as a black box, but recent work proposes integrating multi-level features from visual foundation models into deeper VLA layers via a Vision-Language Mixture-of-Transformers architecture.\n\n## Recent VLA Developments\n\nVLA models have seen extensive efforts devoted to architectural advances as well as training- and inference-time optimizations since the introduction of RT-2. Recent systematic reviews organize more than 100 VLA architectures and analyze their design choices.\n\nThese papers represent cutting-edge research on understanding and improving VLA models for robot manipulation tasks in 2025-2026."
    ],
    "durationSeconds": 6.457967581000005
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-24T01:15:43.836Z_

<details><summary>↩ Tool result · `toolu_01DMT2xNsPELnwGim5FHkhrZ`</summary>

```text
Web search results for query: ""Head Pursuit" attention specialization multimodal transformers Basile 2025"

Links: [{"title":"[2510.21518] Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/abs/2510.21518"},{"title":"[2510.21518v1] Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/abs/2510.21518v1"},{"title":"GitHub - lorenzobasile/HeadPursuit: Code for the paper \"Head Pursuit: Probing Attention Specialization in Multimodal Transformers\" [NeurIPS 2025 spotlight]","url":"https://github.com/lorenzobasile/HeadPursuit"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://openreview.net/pdf/176f0ca9f3211540e905c788d2245175787392e4.pdf"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/html/2510.21518v1"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers - 专知论文","url":"https://zhuanzhi.ai/paper/cefe9bc0bc8e0762573d5efe911b0482"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers | OpenReview","url":"https://openreview.net/forum?id=WQ9rnkaUWm"},{"title":"Multimodal In-context Learning for ASR of Low-resource Languages","url":"https://arxiv.org/html/2601.05707v1"},{"title":"2026-01-09 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398"}]

Based on the search results, here's what I found about "Head Pursuit":

## Overview

"Head Pursuit: Probing Attention Specialization in Multimodal Transformers" is a paper by Lorenzo Basile and colleagues that studies how individual attention heads in text-generative models specialize in specific semantic or visual attributes.

## Key Findings

The results show consistent patterns of specialization at the head level across both unimodal and multimodal transformers. Editing as few as 1% of the heads, selected using their method, can reliably suppress or enhance targeted concepts in the model output.

## Methodology

The approach reinterprets the practice of probing intermediate activations with the final decoding layer through the lens of signal processing, allowing analysis of multiple samples in a principled way and ranking attention heads based on their relevance to target concepts. Their approach uses Simultaneous Orthogonal Matching Pursuit (SOMP) to discover which vocabulary directions best explain each head's outputs, effectively labeling heads by their semantic function.

## Applications

The approach is validated on language tasks such as question answering and toxicity mitigation, as well as vision-language tasks including image classification and captioning.

## Publication

The paper was accepted as a NeurIPS 2025 spotlight presentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "b5846af0-5242-4d8d-8240-fb4184ee0140",
  "tool_use_result": {
    "query": "\"Head Pursuit\" attention specialization multimodal transformers Basile 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015xXUuikxYAKkDvu47f4BXK",
        "content": [
          {
            "title": "[2510.21518] Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/abs/2510.21518"
          },
          {
            "title": "[2510.21518v1] Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/abs/2510.21518v1"
          },
          {
            "title": "GitHub - lorenzobasile/HeadPursuit: Code for the paper \"Head Pursuit: Probing Attention Specialization in Multimodal Transformers\" [NeurIPS 2025 spotlight]",
            "url": "https://github.com/lorenzobasile/HeadPursuit"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://openreview.net/pdf/176f0ca9f3211540e905c788d2245175787392e4.pdf"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/html/2510.21518v1"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers - 专知论文",
            "url": "https://zhuanzhi.ai/paper/cefe9bc0bc8e0762573d5efe911b0482"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers | OpenReview",
            "url": "https://openreview.net/forum?id=WQ9rnkaUWm"
          },
          {
            "title": "Multimodal In-context Learning for ASR of Low-resource Languages",
            "url": "https://arxiv.org/html/2601.05707v1"
          },
          {
            "title": "2026-01-09 Interpreting Transformers Through Attention Head Intervention",
            "url": "https://www.arxiv.org/pdf/2601.04398"
          }
        ]
      },
      "Based on the search results, here's what I found about \"Head Pursuit\":\n\n## Overview\n\n\"Head Pursuit: Probing Attention Specialization in Multimodal Transformers\" is a paper by Lorenzo Basile and colleagues that studies how individual attention heads in text-generative models specialize in specific semantic or visual attributes.\n\n## Key Findings\n\nThe results show consistent patterns of specialization at the head level across both unimodal and multimodal transformers. Editing as few as 1% of the heads, selected using their method, can reliably suppress or enhance targeted concepts in the model output.\n\n## Methodology\n\nThe approach reinterprets the practice of probing intermediate activations with the final decoding layer through the lens of signal processing, allowing analysis of multiple samples in a principled way and ranking attention heads based on their relevance to target concepts. Their approach uses Simultaneous Orthogonal Matching Pursuit (SOMP) to discover which vocabulary directions best explain each head's outputs, effectively labeling heads by their semantic function.\n\n## Applications\n\nThe approach is validated on language tasks such as question answering and toxicity mitigation, as well as vision-language tasks including image classification and captioning.\n\n## Publication\n\nThe paper was accepted as a NeurIPS 2025 spotlight presentation."
    ],
    "durationSeconds": 7.455866173999995
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-24T01:15:44.876Z_

<details><summary>↩ Tool result · `toolu_01F889NP1Zrk8mrGFRKZN9vk`</summary>

```text
Web search results for query: ""reasoning erosion" VLM fine-tuning Fang 2025"

Links: [{"title":"Implicit instruction reasoning by fine-tuning VLM for robotic manipulation | Industrial Robot | Emerald Publishing","url":"https://www.emerald.com/ir/article/doi/10.1108/IR-05-2025-0175/1302439/Implicit-instruction-reasoning-by-fine-tuning-VLM"},{"title":"Mitigating the Reasoning Tax in Vision-Language Fine-Tuning with Input-Adaptive Depth Aggregation","url":"https://arxiv.org/pdf/2603.26330"},{"title":"[2512.12690] Reassessing the Role of Supervised Fine-Tuning: An Empirical Study in VLM Reasoning","url":"https://arxiv.org/abs/2512.12690"},{"title":"GeoVLM-R1: Reinforcement Fine-Tuning for Improved Remote Sensing Reasoning","url":"https://arxiv.org/html/2509.25026v1"},{"title":"Fine-Tuning Large Vision-Language Models as Decision-Making Agents via   Reinforcement Learning","url":"https://arxiv.org/pdf/2405.10292"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/pdf/2509.22195"},{"title":"GitHub - om-ai-lab/VLM-FO1: VLM-FO1: Bridging the Gap Between High-Level Reasoning and Fine-Grained Perception in VLMs · GitHub","url":"https://github.com/om-ai-lab/VLM-FO1"},{"title":"Reinforcement Fine-Tuning Powers Reasoning Capability of Multimodal Large Language Models","url":"https://arxiv.org/html/2505.18536v1"}]

Based on the search results, I found relevant information about VLM fine-tuning and reasoning challenges. Here are the key findings:

## Reasoning Erosion in VLM Fine-Tuning

A prominent phenomenon is that supervised fine-tuning on visual instruction data, while improving perceptual capabilities, often weakens reasoning performance, particularly on mathematical, scientific, and complex visual inference tasks. This is referred to as "reasoning erosion" or the "reasoning tax."

### Recent Research (2025)

On Qwen3-VL-2B, IADA (Input-Adaptive Depth Aggregation) improves the average reasoning score by 9.5 points and the average perception score by 3.3 points over LoRA-only fine-tuning with only 0.14M additional parameters. This represents one approach to mitigating the reasoning degradation problem.

Additionally, findings show that SFT plays a crucial role, with SFT more reliably eliciting reasoning capabilities in smaller or weaker VLMs, suggesting that supervised fine-tuning remains valuable despite its challenges when properly implemented.

The search results indicate that multiple 2025 papers are addressing this challenge of maintaining reasoning capabilities while fine-tuning vision-language models for specialized tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "f200ac29-f3d5-4bed-ab11-34209638c274",
  "tool_use_result": {
    "query": "\"reasoning erosion\" VLM fine-tuning Fang 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SKcr3GzjkxGZQAhJmUqGZ1",
        "content": [
          {
            "title": "Implicit instruction reasoning by fine-tuning VLM for robotic manipulation | Industrial Robot | Emerald Publishing",
            "url": "https://www.emerald.com/ir/article/doi/10.1108/IR-05-2025-0175/1302439/Implicit-instruction-reasoning-by-fine-tuning-VLM"
          },
          {
            "title": "Mitigating the Reasoning Tax in Vision-Language Fine-Tuning with Input-Adaptive Depth Aggregation",
            "url": "https://arxiv.org/pdf/2603.26330"
          },
          {
            "title": "[2512.12690] Reassessing the Role of Supervised Fine-Tuning: An Empirical Study in VLM Reasoning",
            "url": "https://arxiv.org/abs/2512.12690"
          },
          {
            "title": "GeoVLM-R1: Reinforcement Fine-Tuning for Improved Remote Sensing Reasoning",
            "url": "https://arxiv.org/html/2509.25026v1"
          },
          {
            "title": "Fine-Tuning Large Vision-Language Models as Decision-Making Agents via   Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2405.10292"
          },
          {
            "title": "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting",
            "url": "https://arxiv.org/pdf/2509.22195"
          },
          {
            "title": "GitHub - om-ai-lab/VLM-FO1: VLM-FO1: Bridging the Gap Between High-Level Reasoning and Fine-Grained Perception in VLMs · GitHub",
            "url": "https://github.com/om-ai-lab/VLM-FO1"
          },
          {
            "title": "Reinforcement Fine-Tuning Powers Reasoning Capability of Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2505.18536v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about VLM fine-tuning and reasoning challenges. Here are the key findings:\n\n## Reasoning Erosion in VLM Fine-Tuning\n\nA prominent phenomenon is that supervised fine-tuning on visual instruction data, while improving perceptual capabilities, often weakens reasoning performance, particularly on mathematical, scientific, and complex visual inference tasks. This is referred to as \"reasoning erosion\" or the \"reasoning tax.\"\n\n### Recent Research (2025)\n\nOn Qwen3-VL-2B, IADA (Input-Adaptive Depth Aggregation) improves the average reasoning score by 9.5 points and the average perception score by 3.3 points over LoRA-only fine-tuning with only 0.14M additional parameters. This represents one approach to mitigating the reasoning degradation problem.\n\nAdditionally, findings show that SFT plays a crucial role, with SFT more reliably eliciting reasoning capabilities in smaller or weaker VLMs, suggesting that supervised fine-tuning remains valuable despite its challenges when properly implemented.\n\nThe search results indicate that multiple 2025 papers are addressing this challenge of maintaining reasoning capabilities while fine-tuning vision-language models for specialized tasks."
    ],
    "durationSeconds": 6.985804958000008
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-24T01:15:45.870Z_

<details><summary>↩ Tool result · `toolu_01EpQpzo4ydPgNkqcWU5iHGk`</summary>

```text
Web search results for query: "VLA fine-tuning forgetting catastrophic pretrained knowledge robot 2025 2026"

Links: [{"title":"[2605.06175] VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/abs/2605.06175"},{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"2026-01-21 Work in progress. TwinBrainVLA TwinBrainVLA","url":"https://arxiv.org/pdf/2601.14133"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://vlm2vla.github.io/"},{"title":"Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning","url":"https://arxiv.org/pdf/2602.10503"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/pdf/2509.22195"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/pdf/2603.03818"},{"title":"From Vision-Language Models to Robot Control — Without Forgetting – Princeton Laboratory for Artificial Intelligence Research Blog","url":"https://blog.ai.princeton.edu/2026/04/23/from-vision-language-models-to-robot-control-without-forgetting/"}]

Based on the search results, I found several recent papers and research addressing VLA (Vision-Language-Action) fine-tuning, catastrophic forgetting, and pretrained knowledge in robotic systems from 2025-2026:

## Key Research Areas:

**Catastrophic Forgetting Problem:**
Full fine-tuning is prone to overfitting on downstream robotic data and catastrophic forgetting of pretrained vision-language capabilities. The resulting VLA model loses the ability to follow complex open-ended instructions, fails to describe visual scenes accurately, and exhibits weakened general semantic reasoning.

**Solutions Proposed:**

1. **VLA-GSE (2025):** A parameter-efficient VLA fine-tuning framework that improves control adaptation while retaining knowledge preservation advantage. VLA-GSE successfully mitigates catastrophic forgetting by balancing knowledge retention with efficient adaptation, achieving the highest overall success rate of 81.2%.

2. **VLM2VLA (2025):** A data-centric approach that re-represents robot actions as natural language descriptions, thereby aligning the VLA fine-tuning data directly with the VLM's pretrained representation space. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting.

3. **LifeLong-RFT (2026):** A Reinforcement Fine-Tuning strategy for VLA models independent of online environmental feedback and pretrained reward models.

4. **TwinBrainVLA:** An architecture that operates on an asymmetric dual-stream paradigm to resolve the "catastrophic forgetting" dilemma.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "c2e33ab6-e9ee-4baa-b49d-0fe1690b7377",
  "tool_use_result": {
    "query": "VLA fine-tuning forgetting catastrophic pretrained knowledge robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Hka78wVoEhbGqHWUeqqBaF",
        "content": [
          {
            "title": "[2605.06175] VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts",
            "url": "https://arxiv.org/abs/2605.06175"
          },
          {
            "title": "VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts",
            "url": "https://arxiv.org/html/2605.06175v1"
          },
          {
            "title": "2026-01-21 Work in progress. TwinBrainVLA TwinBrainVLA",
            "url": "https://arxiv.org/pdf/2601.14133"
          },
          {
            "title": "2026-01-28 Work in progress.",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting",
            "url": "https://vlm2vla.github.io/"
          },
          {
            "title": "Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning",
            "url": "https://arxiv.org/pdf/2602.10503"
          },
          {
            "title": "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting",
            "url": "https://arxiv.org/pdf/2509.22195"
          },
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://arxiv.org/pdf/2603.03818"
          },
          {
            "title": "From Vision-Language Models to Robot Control — Without Forgetting – Princeton Laboratory for Artificial Intelligence Research Blog",
            "url": "https://blog.ai.princeton.edu/2026/04/23/from-vision-language-models-to-robot-control-without-forgetting/"
          }
        ]
      },
      "Based on the search results, I found several recent papers and research addressing VLA (Vision-Language-Action) fine-tuning, catastrophic forgetting, and pretrained knowledge in robotic systems from 2025-2026:\n\n## Key Research Areas:\n\n**Catastrophic Forgetting Problem:**\nFull fine-tuning is prone to overfitting on downstream robotic data and catastrophic forgetting of pretrained vision-language capabilities. The resulting VLA model loses the ability to follow complex open-ended instructions, fails to describe visual scenes accurately, and exhibits weakened general semantic reasoning.\n\n**Solutions Proposed:**\n\n1. **VLA-GSE (2025):** A parameter-efficient VLA fine-tuning framework that improves control adaptation while retaining knowledge preservation advantage. VLA-GSE successfully mitigates catastrophic forgetting by balancing knowledge retention with efficient adaptation, achieving the highest overall success rate of 81.2%.\n\n2. **VLM2VLA (2025):** A data-centric approach that re-represents robot actions as natural language descriptions, thereby aligning the VLA fine-tuning data directly with the VLM's pretrained representation space. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting.\n\n3. **LifeLong-RFT (2026):** A Reinforcement Fine-Tuning strategy for VLA models independent of online environmental feedback and pretrained reward models.\n\n4. **TwinBrainVLA:** An architecture that operates on an asymmetric dual-stream paradigm to resolve the \"catastrophic forgetting\" dilemma."
    ],
    "durationSeconds": 8.436886854000011
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile all the findings. Let me identify which papers are already cited and which are new and potentially relevant.

**Already cited papers (confirmed):**
1. Grant et al. 2026 - "Not All Features Are Created Equal" (2603.19233) - already cited for visual dominance
2. Haon et al. 2025 - "Mechanistic interpretability for steering VLAs" (2509.00328) - already cited for sparse semantic directions
3. Swann et al. 2026 - "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models" (2603.19183) - already cited for interpretable features


4. Lu et al. 2025 / Molinari et al. 2025 - symbolic representations - already cited
5. Fang et al. 2025 - reasoning erosion - already cited
6. Fan et al. 2026 - visual token redundancy - already cited

I'm finding a new paper on emergent world representations in OpenVLA that uses linear probes across layers to identify where world model knowledge emerges, which directly aligns with my layer-wise probing approach.

Then there's DeepVision-VLA showing that visual token sensitivity drops in deeper layers and proposing multi-level feature injection—their observation about visual information loss in deeper layers mirrors my exit collapse finding, though they're proposing a solution while I'm characterizing the underlying mechanism.

I'm also looking at a paper on preserving pretrained representations in VLA models by Grover and colleagues from September 2025. , Su, Li
   - Fine-tuning degrades pretrained representations, proposes dual-encoder + co-training
   - Directly relevant to our R² exit collapse finding about representation degradation during VLM→VLA fine-tuning
   - Relationship: Complementary - they address the same problem from an engineering perspective, we characterize it mechanistically

4. **"MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling"** (arxiv 2511.19878, Nov 2025)
   - First robust fine-tuning framework for VLAs
   - Addresses how fine-tuning disrupts pretrained representations
   - Relevant to our exit collapse finding
   - Relationship: Complementary - they propose a training solution, we provide mechanistic characterization

5. **"Head Pursuit: Probing Attention Specialization in Multimodal Transformers"** (Basile et al., NeurIPS 2025 spotlight, arxiv 2510.21518)
   - Examines how attention heads specialize in multimodal transformers using SOMP to identify vocabulary directions
   - Directly applicable to our attention head analysis showing instruction-dominant routing in L1
   - Relationship: Methodologically related - they characterize attention specialization in VLMs while we focus on the same phenomenon in VLAs

6. **"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting" (VLM2VLA)** (arxiv 2509.22195, Sep 2025)
   - Prevents catastrophic forgetting by representing robot actions as natural language tokens
   - Addresses the representation changes we observe during VLM→VLA transition
   - Relationship: Complementary approach to the same problem

7. **"Representational de-collapse

: Interactions between supervised finetuning and in-context learning in language models"** (ICLR 2026, Mar 2026)
   - Shows that supervised fine-tuning collapses representations along task dimensions while in-context learning can reverse this effect
   - Provides conceptual framework for understanding our exit collapse finding, though in NLP rather than VLA domain
   - Relationship: Conceptually related

8. **"DySL-VLA: Efficient VLA Model Inference via Dynamic-Static Layer-Skipping"** (arxiv 2602.22896, Feb 2026)
   - Analyzes layer-wise behavior for dynamic layer skipping during inference
   - Tangentially relevant to our layer-wise mechanistic analysis

9. **"Controlling Vision-Language-Action Policies through Sparse Latent Directions"** (NeurIPS 2025 workshop)
   - Uses sparse autoencoders to steer VLA behavior through latent directions
   - Might overlap with the Haon et al. 2025 work the user already cites on sparse semantic directions

10. **"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning"** (arxiv 2603.03818, Mar 2026)
    - Shows VLAs maintain performance across sequential tasks without catastrophic forgetting
    - Interesting counterpoint to our collapse findings, especially since VLA-to-VLA transitions don't show the same degradation

11. **"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts"** (arxiv 2605.06175, May 2026)
    - Recent work addressing catastrophic forgetting through mixture-of-experts approach during fine-tuning
    - Peripherally relevant to our findings

12. **"Mitigating the Reasoning Tax in Vision-Language Fine-Tuning with Input-Adaptive Depth Aggregation"** (arxiv 2603.26330, Mar 2026)
    - Tackles the performance cost of fine-tuning on reasoning tasks, conceptually similar to Fang et al.'s reasoning erosion problem

13. **"Probing a Vision-Language-Action Model for Symbolic States"** (arxiv 2502.04558)
    - Likely a duplicate citation—probably Lu et al. or Molinari et al. already in our references

14. **"NoTVLA: Semantics-Preserving Robot Adaptation via Narrative Action Interfaces"** (arxiv 2510.03895)
    - Directly addresses preserving semantic information during VLA adaptation, which connects to our collapse mechanism

Now I need to sort through these and figure out which ones actually strengthen the narrative.

The must-cite papers are the core ones—OpenVLA's layer-wise probing directly validates our approach, Basile et al.'s attention head work gives us the methodology framework, and Grover et al. tackles the exact problem we're solving. For complementary work, the papers on visual degradation in deeper layers, robust fine-tuning approaches, and catastrophic forgetting prevention all support different angles of our argument.

Now I'm checking whether "Controlling VLA Policies through Sparse Latent Directions" overlaps with the Haon et al. paper the user already cites. The Controlling paper is from the NeurIPS 2025 Mech Interp Workshop while Haon et al. is the full paper, and they both discuss sparse directions in VLAs—they might be the same work or closely related, so I need to verify before adding it as a separate citation.

I should also verify that Buurmeijer et al. 2026 on low-level motor features is distinct from the "Emergent World Representations" paper, then do a final check for any VLA cross-architecture analysis work I might have missed before compiling the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "5e62225d-19b3-45c3-a8da-07334c9c6548",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFUpMmcngzsCRWcoCvX8d6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 4355,
      "cache_read_input_tokens": 36482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4355
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

_source line 52_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EGtyszmqYHVZ1kj7WwdwpH`</summary>

```json
{
  "query": "VLA cross-architecture comparison analysis OpenVLA Pi0 representation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "0e5951c7-eea8-42e5-b2de-807f5a47da93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFUpMmcngzsCRWcoCvX8d6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 4355,
      "cache_read_input_tokens": 36482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4355
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

_source line 53_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011wY39R7BkC1Znob4QjU1nb`</summary>

```json
{
  "query": "\"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "dbd5cd95-6040-46d7-8912-fcb06b6ae3d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFUpMmcngzsCRWcoCvX8d6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 4355,
      "cache_read_input_tokens": 36482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4355
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

_source line 54_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Go1TvHMzBEf3ewqt1vmmq`</summary>

```json
{
  "query": "\"DySL-VLA\" dynamic static layer skipping 2026 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "9e9e66b6-61bb-4bec-a3ae-4abf147257f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFUpMmcngzsCRWcoCvX8d6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 4355,
      "cache_read_input_tokens": 36482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4355
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

_source line 55 · 2026-05-24T01:16:42.286Z_

<details><summary>↩ Tool result · `toolu_011wY39R7BkC1Znob4QjU1nb`</summary>

```text
Web search results for query: ""Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting" 2026"

Links: [{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | Deep Learning JP","url":"https://deeplearning.jp/en/pretrained-vision-language-action-models-are-surprisingly-resistant-to-forgetting-in-continual-learning/"},{"title":"Paper page - Simple Recipe Works: Vision-Language-Action Models are Natural Continual Learners with Reinforcement Learning","url":"https://huggingface.co/papers/2603.11653"},{"title":"Pretrained VLAs are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://continual-vlas.github.io/forget-me-not/"},{"title":"[2603.03818] Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/abs/2603.03818"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.03818"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/html/2603.03818v1"},{"title":"[Literature Review] Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://www.themoonlight.io/en/review/pretrained-vision-language-action-models-are-surprisingly-resistant-to-forgetting-in-continual-learning"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly","url":"https://arxiv.org/pdf/2603.03818"}]

I found the paper! Here are the search results for "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting" from 2026:

## Summary

The paper is authored by Liu, Huihan and Kim, Changyeon and Liu, Bo and Liu, Minghuan and Zhu, Yuke, published on arXiv in 2026.

## Main Findings

The research addresses continual learning in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. 

Key findings include:

1. **Resistance to Forgetting**: Pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch.

2. **Experience Replay Effectiveness**: Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size.

3. **Role of Pretraining**: Large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities.

4. **Knowledge Retention**: VLAs can retain relevant knowledge from prior tasks despite performance degradation during learning new tasks, and this knowledge retention enables rapid recovery of seemingly forgotten skills through finetuning.

The paper explores these phenomena across different Vision-Language-Action (VLA) architectures and provides insights into why large-scale pretraining significantly improves continual learning performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "1d96e5fd-c034-4ad8-b14a-14275eb20c50",
  "tool_use_result": {
    "query": "\"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting\" 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EGuJLUXTR6G9hkx8Lssfnf",
        "content": [
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | Deep Learning JP",
            "url": "https://deeplearning.jp/en/pretrained-vision-language-action-models-are-surprisingly-resistant-to-forgetting-in-continual-learning/"
          },
          {
            "title": "Paper page - Simple Recipe Works: Vision-Language-Action Models are Natural Continual Learners with Reinforcement Learning",
            "url": "https://huggingface.co/papers/2603.11653"
          },
          {
            "title": "Pretrained VLAs are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://continual-vlas.github.io/forget-me-not/"
          },
          {
            "title": "[2603.03818] Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://arxiv.org/abs/2603.03818"
          },
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.03818"
          },
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://arxiv.org/html/2603.03818v1"
          },
          {
            "title": "[Literature Review] Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://www.themoonlight.io/en/review/pretrained-vision-language-action-models-are-surprisingly-resistant-to-forgetting-in-continual-learning"
          },
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly",
            "url": "https://arxiv.org/pdf/2603.03818"
          }
        ]
      },
      "I found the paper! Here are the search results for \"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting\" from 2026:\n\n## Summary\n\nThe paper is authored by Liu, Huihan and Kim, Changyeon and Liu, Bo and Liu, Minghuan and Zhu, Yuke, published on arXiv in 2026.\n\n## Main Findings\n\nThe research addresses continual learning in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. \n\nKey findings include:\n\n1. **Resistance to Forgetting**: Pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch.\n\n2. **Experience Replay Effectiveness**: Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size.\n\n3. **Role of Pretraining**: Large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities.\n\n4. **Knowledge Retention**: VLAs can retain relevant knowledge from prior tasks despite performance degradation during learning new tasks, and this knowledge retention enables rapid recovery of seemingly forgotten skills through finetuning.\n\nThe paper explores these phenomena across different Vision-Language-Action (VLA) architectures and provides insights into why large-scale pretraining significantly improves continual learning performance."
    ],
    "durationSeconds": 6.656304692000005
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-24T01:16:43.635Z_

<details><summary>↩ Tool result · `toolu_01EGtyszmqYHVZ1kj7WwdwpH`</summary>

```text
Web search results for query: "VLA cross-architecture comparison analysis OpenVLA Pi0 representation 2025 2026"

Links: [{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/learn/vla-models-comparison"},{"title":"Physical Intelligence π0 vs OpenVLA: Best VLA Model for Robot Learning 2026 | SVRC","url":"https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla"},{"title":"Vision-Language-Action Models Explained: How VLAs Power Modern Robots | SVRC","url":"https://www.roboticscenter.ai/blog/vla-models-explained"},{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"},{"title":"Experiences from Benchmarking Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/pdf/2511.11298"},{"title":"Vision–language–action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Cross-Platform Scaling of Vision-Language-Action Models from Edge to Cloud GPUs","url":"https://arxiv.org/pdf/2509.11480"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"}]

I found comprehensive information about VLA (Vision-Language-Action) models with cross-architecture comparisons. Here's what the search revealed:

## Key VLA Models Compared

The main VLA models being compared include architecture, performance, data requirements, and hardware compatibility analyses. The primary models in comparison are:

**OpenVLA vs π0 (Pi-Zero):**
OpenVLA features open weights, Apache 2.0 license, consumer-GPU fine-tuning, and an active community, while π0 from Physical Intelligence delivers state-of-the-art dexterity performance but requires partnership access and cannot be self-hosted.

**Architectural Differences:**
Unlike OpenVLA, which inherits a language model backbone, pi0 uses a flow-matching action head that produces continuous, smooth action trajectories—more suited to dexterous tasks than discrete tokenized actions. What distinguishes pi0 architecturally is the separation between the "slow" language-conditioned reasoning pathway and the "fast" reactive motor control pathway, which mirrors insights from cognitive science about dual-process control systems.

**Deployment Considerations:**
OpenVLA's 7B parameters require A100 or H100 (80GB VRAM) for full-precision inference at 5 Hz, but with 4-bit quantization fits on RTX 4090 at 3-4 Hz. Pi0's 3B parameters are optimized for deployment and run on a single A100 at 10 Hz.

The search results also reference recent 2025-2026 research including comparative studies on VLA performance, scaling analysis, and specialized architectures like SmolVLA, GR00T, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "80fe7f96-b355-4faa-bd63-d0a9d1c0b52f",
  "tool_use_result": {
    "query": "VLA cross-architecture comparison analysis OpenVLA Pi0 representation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WmwYGW9MF8BYRhGoD8P2sb",
        "content": [
          {
            "title": "VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC",
            "url": "https://www.roboticscenter.ai/learn/vla-models-comparison"
          },
          {
            "title": "Physical Intelligence π0 vs OpenVLA: Best VLA Model for Robot Learning 2026 | SVRC",
            "url": "https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla"
          },
          {
            "title": "Vision-Language-Action Models Explained: How VLAs Power Modern Robots | SVRC",
            "url": "https://www.roboticscenter.ai/blog/vla-models-explained"
          },
          {
            "title": "GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.",
            "url": "https://github.com/keon/awesome-physical-ai"
          },
          {
            "title": "Experiences from Benchmarking Vision-Language-Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2511.11298"
          },
          {
            "title": "Vision–language–action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "Cross-Platform Scaling of Vision-Language-Action Models from Edge to Cloud GPUs",
            "url": "https://arxiv.org/pdf/2509.11480"
          },
          {
            "title": "OpenVLA-OFT",
            "url": "https://openvla-oft.github.io/"
          }
        ]
      },
      "I found comprehensive information about VLA (Vision-Language-Action) models with cross-architecture comparisons. Here's what the search revealed:\n\n## Key VLA Models Compared\n\nThe main VLA models being compared include architecture, performance, data requirements, and hardware compatibility analyses. The primary models in comparison are:\n\n**OpenVLA vs π0 (Pi-Zero):**\nOpenVLA features open weights, Apache 2.0 license, consumer-GPU fine-tuning, and an active community, while π0 from Physical Intelligence delivers state-of-the-art dexterity performance but requires partnership access and cannot be self-hosted.\n\n**Architectural Differences:**\nUnlike OpenVLA, which inherits a language model backbone, pi0 uses a flow-matching action head that produces continuous, smooth action trajectories—more suited to dexterous tasks than discrete tokenized actions. What distinguishes pi0 architecturally is the separation between the \"slow\" language-conditioned reasoning pathway and the \"fast\" reactive motor control pathway, which mirrors insights from cognitive science about dual-process control systems.\n\n**Deployment Considerations:**\nOpenVLA's 7B parameters require A100 or H100 (80GB VRAM) for full-precision inference at 5 Hz, but with 4-bit quantization fits on RTX 4090 at 3-4 Hz. Pi0's 3B parameters are optimized for deployment and run on a single A100 at 10 Hz.\n\nThe search results also reference recent 2025-2026 research including comparative studies on VLA performance, scaling analysis, and specialized architectures like SmolVLA, GR00T, and others."
    ],
    "durationSeconds": 8.228433203000023
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-24T01:16:44.074Z_

<details><summary>↩ Tool result · `toolu_012Go1TvHMzBEf3ewqt1vmmq`</summary>

```text
Web search results for query: ""DySL-VLA" dynamic static layer skipping 2026 authors"

Links: [{"title":"[2602.22896] DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation","url":"https://arxiv.org/abs/2602.22896"},{"title":"DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=sZrjfrFPdj"},{"title":"GitHub - guanweifan/awesome-efficient-vla: 🔥 A curated roadmap to the Efficient VLA landscape. We’re keeping this list live—contribute your latest work!","url":"https://github.com/guanweifan/awesome-efficient-vla"},{"title":"DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation","url":"https://arxiv.org/html/2602.22896v3"},{"title":"DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation","url":"https://arxiv.org/pdf/2602.22896"},{"title":"DYSL-VLA: EFFICIENT VISION-LANGUAGE-ACTION","url":"https://openreview.net/pdf/020da3ac66aba08fad5413937702ed5518db8431.pdf"}]

Based on the search results, here's the information about DySL-VLA:

## DySL-VLA: Dynamic-Static Layer Skipping for VLA Models

DySL-VLA is a novel framework that addresses computational cost by dynamically skipping Vision-Language-Action (VLA) layers based on each action's importance.

### Key Technical Approach

DySL-VLA categorizes its layers into two types: informative layers, which are consistently executed, and incremental layers, which can be selectively skipped. To intelligently skip layers without sacrificing accuracy, the framework uses a prior-post skipping guidance mechanism to determine when to initiate layer-skipping.

### Authors

The authors are Zebin Yang, Yijiahao Qi, Tong Xie, Bo Yu, Shaoshan Liu, and Meng Li.

### Performance Results

DySL-VLA achieves a 2.1% improvement in success length over Deer-VLA (NeurIPS'24) on the Calvin dataset, while simultaneously reducing trainable parameters by a factor of 85.7 and providing a 3.75× speedup relative to the RoboFlamingo baseline at iso-accuracy.

The paper was submitted on February 26, 2026, with the latest revision on March 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "a9f6fb9c-40ab-4750-8c62-31ec41735b29",
  "tool_use_result": {
    "query": "\"DySL-VLA\" dynamic static layer skipping 2026 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WtHxo94yJsMxjpuTqGMdh7",
        "content": [
          {
            "title": "[2602.22896] DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation",
            "url": "https://arxiv.org/abs/2602.22896"
          },
          {
            "title": "DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=sZrjfrFPdj"
          },
          {
            "title": "GitHub - guanweifan/awesome-efficient-vla: 🔥 A curated roadmap to the Efficient VLA landscape. We’re keeping this list live—contribute your latest work!",
            "url": "https://github.com/guanweifan/awesome-efficient-vla"
          },
          {
            "title": "DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation",
            "url": "https://arxiv.org/html/2602.22896v3"
          },
          {
            "title": "DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation",
            "url": "https://arxiv.org/pdf/2602.22896"
          },
          {
            "title": "DYSL-VLA: EFFICIENT VISION-LANGUAGE-ACTION",
            "url": "https://openreview.net/pdf/020da3ac66aba08fad5413937702ed5518db8431.pdf"
          }
        ]
      },
      "Based on the search results, here's the information about DySL-VLA:\n\n## DySL-VLA: Dynamic-Static Layer Skipping for VLA Models\n\nDySL-VLA is a novel framework that addresses computational cost by dynamically skipping Vision-Language-Action (VLA) layers based on each action's importance.\n\n### Key Technical Approach\n\nDySL-VLA categorizes its layers into two types: informative layers, which are consistently executed, and incremental layers, which can be selectively skipped. To intelligently skip layers without sacrificing accuracy, the framework uses a prior-post skipping guidance mechanism to determine when to initiate layer-skipping.\n\n### Authors\n\nThe authors are Zebin Yang, Yijiahao Qi, Tong Xie, Bo Yu, Shaoshan Liu, and Meng Li.\n\n### Performance Results\n\nDySL-VLA achieves a 2.1% improvement in success length over Deer-VLA (NeurIPS'24) on the Calvin dataset, while simultaneously reducing trainable parameters by a factor of 85.7 and providing a 3.75× speedup relative to the RoboFlamingo baseline at iso-accuracy.\n\nThe paper was submitted on February 26, 2026, with the latest revision on March 17, 2026."
    ],
    "durationSeconds": 8.110757366000005
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Now let me also search for the "Emergent World Representations in OpenVLA" paper authors and the "Buurmeijer" paper to make sure I correctly identify what's already cited.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "2991c16f-d609-4b4c-a904-e8578ca28b2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQpJJjg2y1x4H5uvGLLSBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5467,
      "cache_read_input_tokens": 40837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5467
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

_source line 59_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016WUkxZHADgZBftAB1sJ3em`</summary>

```json
{
  "query": "\"Emergent World Representations in OpenVLA\" authors arxiv 2509.24559"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "4d1bf946-cf06-4eb8-a78f-60212fb4b85a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQpJJjg2y1x4H5uvGLLSBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5467,
      "cache_read_input_tokens": 40837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5467
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

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NdKPkd6Ewc9W5QPZiPSA6T`</summary>

```json
{
  "query": "Buurmeijer VLA probing low-level motor features OpenVLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "3d2e9a39-a58e-4ae2-b3cf-82e4e0dc89cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQpJJjg2y1x4H5uvGLLSBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5467,
      "cache_read_input_tokens": 40837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5467
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

_source line 61 · 2026-05-24T01:16:54.727Z_

<details><summary>↩ Tool result · `toolu_016WUkxZHADgZBftAB1sJ3em`</summary>

```text
Web search results for query: ""Emergent World Representations in OpenVLA" authors arxiv 2509.24559"

Links: [{"title":"Emergent World Representations in OpenVLA","url":"https://arxiv.org/pdf/2509.24559"},{"title":"Emergent World Representations in OpenVLA","url":"https://arxiv.org/html/2509.24559v1"},{"title":"[Literature Review] Emergent World Representations in OpenVLA","url":"https://www.themoonlight.io/en/review/emergent-world-representations-in-openvla"},{"title":"[2509.24559] Emergent World Representations in OpenVLA","url":"https://arxiv.org/abs/2509.24559"},{"title":"Emergent World Representations in OpenVLA | OpenReview","url":"https://openreview.net/forum?id=cydXirmduY"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=2050&show=50"}]

Based on the search results, I found the paper "Emergent World Representations in OpenVLA" with arxiv ID 2509.24559.

**Authors:** Marco Molinari, Leonardo Nevali, Saharsha Navani, and Omar G. Younis

**Summary:**

The paper investigates whether Vision Language Action models (VLAs) trained with policy-based reinforcement learning implicitly learn world models, a hallmark of model-based RL. 

The authors propose an experimental methodology using embedding arithmetic on state representations to probe whether OpenVLA contains latent knowledge of state transitions by measuring the difference between embeddings of sequential environment states and testing whether this transition vector is recoverable from intermediate model activations.

**Key Findings:**

- Using linear and non-linear probes trained on activations across layers, they find statistically significant predictive ability on state transitions exceeding baselines, indicating that OpenVLA encodes an internal world model.

- The world model appears to emerge as training progresses.

- The authors outline a pipeline leveraging Sparse Autoencoders (SAEs) to analyze OpenVLA's world model.

The paper was submitted to arXiv on September 29, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "96821306-dd06-401c-ae83-5b8c1b592f53",
  "tool_use_result": {
    "query": "\"Emergent World Representations in OpenVLA\" authors arxiv 2509.24559",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DvCE4s3PjhZMP2Pk3fgDq7",
        "content": [
          {
            "title": "Emergent World Representations in OpenVLA",
            "url": "https://arxiv.org/pdf/2509.24559"
          },
          {
            "title": "Emergent World Representations in OpenVLA",
            "url": "https://arxiv.org/html/2509.24559v1"
          },
          {
            "title": "[Literature Review] Emergent World Representations in OpenVLA",
            "url": "https://www.themoonlight.io/en/review/emergent-world-representations-in-openvla"
          },
          {
            "title": "[2509.24559] Emergent World Representations in OpenVLA",
            "url": "https://arxiv.org/abs/2509.24559"
          },
          {
            "title": "Emergent World Representations in OpenVLA | OpenReview",
            "url": "https://openreview.net/forum?id=cydXirmduY"
          },
          {
            "title": "Machine Learning Sep 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-09?skip=2050&show=50"
          }
        ]
      },
      "Based on the search results, I found the paper \"Emergent World Representations in OpenVLA\" with arxiv ID 2509.24559.\n\n**Authors:** Marco Molinari, Leonardo Nevali, Saharsha Navani, and Omar G. Younis\n\n**Summary:**\n\nThe paper investigates whether Vision Language Action models (VLAs) trained with policy-based reinforcement learning implicitly learn world models, a hallmark of model-based RL. \n\nThe authors propose an experimental methodology using embedding arithmetic on state representations to probe whether OpenVLA contains latent knowledge of state transitions by measuring the difference between embeddings of sequential environment states and testing whether this transition vector is recoverable from intermediate model activations.\n\n**Key Findings:**\n\n- Using linear and non-linear probes trained on activations across layers, they find statistically significant predictive ability on state transitions exceeding baselines, indicating that OpenVLA encodes an internal world model.\n\n- The world model appears to emerge as training progresses.\n\n- The authors outline a pipeline leveraging Sparse Autoencoders (SAEs) to analyze OpenVLA's world model.\n\nThe paper was submitted to arXiv on September 29, 2025."
    ],
    "durationSeconds": 6.48905899999998
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-24T01:16:56.097Z_

<details><summary>↩ Tool result · `toolu_01NdKPkd6Ewc9W5QPZiPSA6T`</summary>

```text
Web search results for query: "Buurmeijer VLA probing low-level motor features OpenVLA 2026"

Links: [{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.09930"},{"title":"Probing a Vision-Language-Action Model for Symbolic States and   Integration into a Cognitive Architecture","url":"https://arxiv.org/pdf/2502.04558"},{"title":"Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.05487"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.19233"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/html/2506.09930v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"},{"title":"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture","url":"https://arxiv.org/html/2502.04558v1"}]

Based on the web search results, I found research by Hugo Buurmeijer related to VLA (Vision-Language-Action) models:

The paper "Observing and Controlling Features in Vision-Language-Action Models" is authored by Hugo Buurmeijer and colleagues from Stanford University and NVIDIA Research. This appears to be the most directly relevant result to your search query.

The research addresses how Vision-Language-Action Models have shown remarkable progress towards embodied intelligence, while noting that VLAs exhibit higher complexity due to their multimodal inputs/outputs and hybrid nature, making it difficult to apply mechanistic interpretability insights from LLMs to VLAs.

The search results also show related work in this area. A mechanistic study across five VLAs including OpenVLA-OFT spans 80M to 7B parameters across three action generation paradigms and four benchmarks with over 394,000 rollout episodes, which relates to the investigation of low-level motor features in these models.

For more specific details about the Buurmeijer paper's findings on low-level motor features, you may want to access the full PDF from the arxiv link provided in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "c4fa8637-a687-43fd-ae47-60eafffc35dd",
  "tool_use_result": {
    "query": "Buurmeijer VLA probing low-level motor features OpenVLA 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NdNpFotAyjJQfsMa7d7UHd",
        "content": [
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2506.09930"
          },
          {
            "title": "Probing a Vision-Language-Action Model for Symbolic States and   Integration into a Cognitive Architecture",
            "url": "https://arxiv.org/pdf/2502.04558"
          },
          {
            "title": "Observing and Controlling Features in Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.05487"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.19233"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.09930v1"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview",
            "url": "https://openreview.net/forum?id=ZMnD6QZAE6"
          },
          {
            "title": "Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture",
            "url": "https://arxiv.org/html/2502.04558v1"
          }
        ]
      },
      "Based on the web search results, I found research by Hugo Buurmeijer related to VLA (Vision-Language-Action) models:\n\nThe paper \"Observing and Controlling Features in Vision-Language-Action Models\" is authored by Hugo Buurmeijer and colleagues from Stanford University and NVIDIA Research. This appears to be the most directly relevant result to your search query.\n\nThe research addresses how Vision-Language-Action Models have shown remarkable progress towards embodied intelligence, while noting that VLAs exhibit higher complexity due to their multimodal inputs/outputs and hybrid nature, making it difficult to apply mechanistic interpretability insights from LLMs to VLAs.\n\nThe search results also show related work in this area. A mechanistic study across five VLAs including OpenVLA-OFT spans 80M to 7B parameters across three action generation paradigms and four benchmarks with over 394,000 rollout episodes, which relates to the investigation of low-level motor features in these models.\n\nFor more specific details about the Buurmeijer paper's findings on low-level motor features, you may want to access the full PDF from the arxiv link provided in the search results."
    ],
    "durationSeconds": 7.1239858479999825
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Now I have a more complete picture. Let me check if "Emergent World Representations in OpenVLA" (Molinari et al. 2025) is the same as the already-cited "Molinari et al. 2025 — symbolic representations." The authors include Marco Molinari, so this is likely the same Molinari. But the user listed "Molinari et al. 2025 — symbolic representations" and "Lu et al. 2025 — symbolic representations" as separate entries. Let me check.

The "Probing a Vision-Language-Action Model for Symbolic States" (2502.04558) is likely Lu et al. 

So I'm trying to figure out whether "Emergent World Representations in OpenVLA" by Molinari et al. is actually the same paper as the "Molinari et al. 2025 — symbolic representations" the user already cited, or if they're distinct works. The titles suggest different focuses—one on world model emergence and one on symbolic representations—but they could overlap or even be the same paper with different emphasis.

I'm also cross-checking the Buurmeijer citation against what the user listed, and it looks like "Observing and Controlling Features in Vision-Language-Action Models" matches up with their reference to low-level motor feature probing in OpenVLA. There's another paper on generalization boundaries in vision-language-action models that I'm noting as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "2893f97e-394f-4cbf-823c-35f0f18eaa3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxWSivDBofmUxnbes1wEdu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 46304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1415
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

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A3iJAAaiSAStuFy6cXmEbU`</summary>

```json
{
  "query": "\"From Intention to Execution\" probing generalization boundaries VLA models 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "d0135bdd-cb5f-4671-8225-a0054c13e8de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxWSivDBofmUxnbes1wEdu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 46304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1415
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

_source line 65_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GLTwq3S8LhWpUsKC1hnJWM`</summary>

```json
{
  "query": "\"NoTVLA\" semantics preserving robot adaptation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "51174cd2-c374-4784-aa6f-cee1259b1b98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxWSivDBofmUxnbes1wEdu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 46304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1415
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

_source line 66 · 2026-05-24T01:17:18.357Z_

<details><summary>↩ Tool result · `toolu_01GLTwq3S8LhWpUsKC1hnJWM`</summary>

```text
Web search results for query: ""NoTVLA" semantics preserving robot adaptation 2025"

Links: [{"title":"[2510.03895] NoTVLA: Semantics-Preserving Robot Adaptation via Narrative Action Interfaces","url":"https://arxiv.org/abs/2510.03895"},{"title":"NoTVLA: Semantics-Preserving Robot Adaptation via Narrative Action Interfaces","url":"https://arxiv.org/html/2510.03895"},{"title":"NoTVLA: Sparse Trajectory for VLA Robotics","url":"https://www.emergentmind.com/topics/narrowing-of-trajectory-vla-notvla"},{"title":"NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=GtyMclqDqY"},{"title":"NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robotic Manipulation","url":"https://arxiv.org/html/2510.03895v1"},{"title":"NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robot Manipulation","url":"https://arxiv.org/pdf/2510.03895"}]

Based on the search results, here's what I found about NoTVLA:

## Overview

NoTVLA (Narrowing of Trajectory VLA) is a framework that addresses catastrophic forgetting in Vision-Language-Action (VLA) models. This issue stems from VLA models' overreliance on continuous action sequences or action chunks, which create isolated data silos that disrupt knowledge retention across tasks.

## Key Approach

NoTVLA learns to predict sparse, semantically meaningful trajectory 3D points leading to keyframes instead of dense trajectories. The claim is that changing the robot adaptation target from dense low-level control to a sparse narrative action interface can preserve more task-grounded semantic competence.

## Technical Features

The model predicts waypoints relative to a task-relevant 2D anchor augmented with depth to preserve geometric grounding without requiring dense metric trajectory regression, and a deterministic detokenizer reconstructs smooth high-frequency motion from the sparse outputs.

## Benefits

NoTVLA supports robust multi-task scenarios, enhances zero-shot generalization, and maintains intrinsic language understanding, thereby facilitating unified deployment across diverse robot platforms without dependency on dense data streams. The approach attains superior multi-task generalization while using over an order of magnitude less compute.

The paper was submitted on October 4, 2025 and last revised on May 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "818726ec-cc84-4393-896e-709fcb40d2c3",
  "tool_use_result": {
    "query": "\"NoTVLA\" semantics preserving robot adaptation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JUfdawWRwmzuD5ECAL6Avq",
        "content": [
          {
            "title": "[2510.03895] NoTVLA: Semantics-Preserving Robot Adaptation via Narrative Action Interfaces",
            "url": "https://arxiv.org/abs/2510.03895"
          },
          {
            "title": "NoTVLA: Semantics-Preserving Robot Adaptation via Narrative Action Interfaces",
            "url": "https://arxiv.org/html/2510.03895"
          },
          {
            "title": "NoTVLA: Sparse Trajectory for VLA Robotics",
            "url": "https://www.emergentmind.com/topics/narrowing-of-trajectory-vla-notvla"
          },
          {
            "title": "NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robot Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=GtyMclqDqY"
          },
          {
            "title": "NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robotic Manipulation",
            "url": "https://arxiv.org/html/2510.03895v1"
          },
          {
            "title": "NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robot Manipulation",
            "url": "https://arxiv.org/pdf/2510.03895"
          }
        ]
      },
      "Based on the search results, here's what I found about NoTVLA:\n\n## Overview\n\nNoTVLA (Narrowing of Trajectory VLA) is a framework that addresses catastrophic forgetting in Vision-Language-Action (VLA) models. This issue stems from VLA models' overreliance on continuous action sequences or action chunks, which create isolated data silos that disrupt knowledge retention across tasks.\n\n## Key Approach\n\nNoTVLA learns to predict sparse, semantically meaningful trajectory 3D points leading to keyframes instead of dense trajectories. The claim is that changing the robot adaptation target from dense low-level control to a sparse narrative action interface can preserve more task-grounded semantic competence.\n\n## Technical Features\n\nThe model predicts waypoints relative to a task-relevant 2D anchor augmented with depth to preserve geometric grounding without requiring dense metric trajectory regression, and a deterministic detokenizer reconstructs smooth high-frequency motion from the sparse outputs.\n\n## Benefits\n\nNoTVLA supports robust multi-task scenarios, enhances zero-shot generalization, and maintains intrinsic language understanding, thereby facilitating unified deployment across diverse robot platforms without dependency on dense data streams. The approach attains superior multi-task generalization while using over an order of magnitude less compute.\n\nThe paper was submitted on October 4, 2025 and last revised on May 11, 2026."
    ],
    "durationSeconds": 6.800423508999986
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T01:17:18.560Z_

<details><summary>↩ Tool result · `toolu_01A3iJAAaiSAStuFy6cXmEbU`</summary>

```text
Web search results for query: ""From Intention to Execution" probing generalization boundaries VLA models 2025"

Links: [{"title":"GitHub - ai4ce/INT-ACT: Official repo for From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://github.com/ai4ce/INT-ACT"},{"title":"[2506.09930] From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.09930"},{"title":"Paper page - From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.09930"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.09930"},{"title":"[Literature Review] From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/from-intention-to-execution-probing-the-generalization-boundaries-of-vision-language-action-models"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/html/2506.09930v1"},{"title":"(PDF) From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://www.researchgate.net/publication/392597875_From_Intention_to_Execution_Probing_the_Generalization_Boundaries_of_Vision-Language-Action_Models"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250609930F/abstract"}]

I found comprehensive information about this paper. Here's what the search revealed:

## Overview

"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models" is authored by Irving Fang, Juexiao Zhang, Shengbang Tong, and Chen Feng from New York University.

## Key Focus

The paper addresses the promise of Vision-Language-Action (VLA) models to leverage the broad generalization capabilities of large Vision-Language Models (VLMs) to produce versatile, "generalist" robot policies. The authors argue that current evaluations of VLAs remain insufficient, as emerging benchmarks for VLAs that incorporate language often come with limited evaluation tasks and do not investigate how much VLM pretraining truly contributes to the generalization capabilities of the downstream robotic policy.

## Methodology

The researchers introduce a unified probing suite of 50 simulation-based tasks across 10 subcategories spanning language instruction, vision, and objects. Their probing suite extends the SimplerEnv benchmark, which is built on the Maniskill2 simulator and stands out by being designed to closely match models' performance in the real world.

## Key Findings

The results show that while VLM backbones endow VLAs with robust perceptual understanding and high level planning ("good intentions"), this does not reliably translate into precise motor execution: when faced with out-of-distribution observations, policies often exhibit coherent intentions, but falter in action execution. Additionally, finetuning on action data can erode the original VLM's generalist reasoning abilities.

The official GitHub repository for this work was last updated on 06/26/2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "7464868a-ea65-4d0c-8eab-9258b92477f7",
  "tool_use_result": {
    "query": "\"From Intention to Execution\" probing generalization boundaries VLA models 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XFEHZABswTJYB1dqsa9bq6",
        "content": [
          {
            "title": "GitHub - ai4ce/INT-ACT: Official repo for From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://github.com/ai4ce/INT-ACT"
          },
          {
            "title": "[2506.09930] From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2506.09930"
          },
          {
            "title": "Paper page - From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2506.09930"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2506.09930"
          },
          {
            "title": "[Literature Review] From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://www.themoonlight.io/en/review/from-intention-to-execution-probing-the-generalization-boundaries-of-vision-language-action-models"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.09930v1"
          },
          {
            "title": "(PDF) From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/392597875_From_Intention_to_Execution_Probing_the_Generalization_Boundaries_of_Vision-Language-Action_Models"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250609930F/abstract"
          }
        ]
      },
      "I found comprehensive information about this paper. Here's what the search revealed:\n\n## Overview\n\n\"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models\" is authored by Irving Fang, Juexiao Zhang, Shengbang Tong, and Chen Feng from New York University.\n\n## Key Focus\n\nThe paper addresses the promise of Vision-Language-Action (VLA) models to leverage the broad generalization capabilities of large Vision-Language Models (VLMs) to produce versatile, \"generalist\" robot policies. The authors argue that current evaluations of VLAs remain insufficient, as emerging benchmarks for VLAs that incorporate language often come with limited evaluation tasks and do not investigate how much VLM pretraining truly contributes to the generalization capabilities of the downstream robotic policy.\n\n## Methodology\n\nThe researchers introduce a unified probing suite of 50 simulation-based tasks across 10 subcategories spanning language instruction, vision, and objects. Their probing suite extends the SimplerEnv benchmark, which is built on the Maniskill2 simulator and stands out by being designed to closely match models' performance in the real world.\n\n## Key Findings\n\nThe results show that while VLM backbones endow VLAs with robust perceptual understanding and high level planning (\"good intentions\"), this does not reliably translate into precise motor execution: when faced with out-of-distribution observations, policies often exhibit coherent intentions, but falter in action execution. Additionally, finetuning on action data can erode the original VLM's generalist reasoning abilities.\n\nThe official GitHub repository for this work was last updated on 06/26/2025."
    ],
    "durationSeconds": 7.189169052000012
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check one more thing - whether "From Intention to Execution" by Irving Fang et al. is the same as the already-cited "Fang et al. 2025 — reasoning erosion." Let me check.

The user cites:
- "Fang et al. 2026 'When' — counterfactual behavioral benchmark on LIBERO" 
- "Fang et al. 2025 — reasoning erosion"

"From Intention to Execution" is by Irving Fang et al. 2025, and its findings mention that "finetuning on action data can erode the original VLM's generalist reasoning abilities." This sounds exactly like "reasoning erosion." So this IS likely the already-cited "Fang et al. 2025 — reasoning erosion."


Now I'm ready to compile the final report with all the confirmed papers.

I need to flag the Molinari et al. 2025 paper on emergent world representations as potentially relevant but unconfirmed. Beyond that, I'm seeing a critical new paper from Grover et al. that directly addresses the same representation degradation problem we're characterizing—their work on dual-encoder approaches and co-training to preserve pretrained representations during VLA fine-tuning maps directly onto our R² exit collapse findings.

Then there's MAPS, which offers a practical fine-tuning framework to mitigate representation disruption, complementing our mechanistic analysis. And Basile et al.'s work on attention head specialization in multimodal transformers using spectral analysis could provide additional lens for understanding how representations break down during adaptation.

Looking at DeepVision-VLA, they observe that visual token sensitivity decreases in deeper layers during action generation—directly aligned with our findings about representation changes across the network. Finally, VLM2VLA takes a different approach by re-representing actions as language tokens to avoid catastrophic forgetting, which relates to the core problem we're investigating. avoid catastrophic forgetting during VLM→VLA transition
   - Relevant to our VLM→VLA transition analysis
   - Citation: **建议引用**

6. **"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning"** (Liu et al., Mar 2026, arXiv 2603.03818)
   - VLAs resist forgetting in continual learning (VLA→VLA transition)
   - Directly relevant to our finding that VLA→VLA transition shows no significant collapse
   - Citation: **建议引用**

7. **"Representational de-collapse: Interactions between supervised finetuning and in-context learning"** (ICLR 2026)
   - SFT collapses representations along task labels
   - Conceptually relevant to our "exit collapse" finding, though from NLP domain
   - Citation: **可以引用**

8. **"Emergent World Representations in OpenVLA"** (Molinari et al., Sep 2025, arXiv 2509.24559)
   - Layer-wise probing of OpenVLA for world model representations
   - Highly relevant to our layer-wise analysis, though need to verify if this is distinct from the earlier Molinari citation
   - Citation: **需要确认是否已引用**

9. **"DySL-VLA: Efficient VLA Inference via Dynamic-Static Layer-Skipping"** (Yang et al., Feb 2026, arXiv 2602.22896)
   - Examining layer-wise efficiency mechanisms in VLA inference
   - Their layer importance findings could tangentially relate to our analysis, but the focus on efficiency rather than interpretability makes it less critical
   - Citation: **不需要**

10. **"NoTVLA: Semantics-Preserving Robot Adaptation"** (Oct 2025, arXiv 2510.03895)
    - Using sparse trajectory prediction to maintain semantic competence during adaptation
    - Tangentially relevant to how VLM representations persist through VLA fine-tuning
    - Citation: **不需要**

11. **"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA"** (May 2026, arXiv 2605.06175)
    - Parameter-efficient fine-tuning methods to mitigate forgetting
    - Tangentially relevant to our transition analysis
    - Citation: **不需要**

12. **"Controlling Vision-Language-Action Policies through Sparse Latent Representations"** (Jun 2026, arXiv 2606.xxxxx)
    - Sparse latent control mechanisms in VLA policies
    - Tangentially relevant to representation structure
    - Citation: **不需要**

Now I need to check if this last paper overlaps with Haon et al. 2025 — if it's from the same group or a companion work, I'll skip the citation; if it's distinct, I should include it.

Let me compile the final report with all the relevant citations organized by theme.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "9fe6c7fc-21b3-4718-9da1-cbfb81aea8da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2egCAfnEH3z58MGLUWLuv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 662,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 47719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1636
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

_source line 69_

搜索完成，整理结果。

## 搜索结果汇总
- 搜索了 8 组主要关键词 + 8 组跟进关键词
- 发现 **10 篇**潜在相关论文（排除已引用的）

---

## 需要关注的论文

### Paper 1: "Enhancing Generalization in VLA Models by Preserving Pretrained Representations"
- **作者**: Grover, Gopalkrishnan, Ai, Christensen, Su, Li
- **时间**: Sep 2025, [arXiv 2509.11417](https://arxiv.org/abs/2509.11417)
- **核心结论**: VLM→VLA fine-tuning 降解 pretrained representations，提出 dual-encoder（一个 frozen、一个 trainable）+ string-based action tokenizer + co-training 策略缓解
- **与我们的关系**: **直接互补** — 他们文档化了我们发现的同一现象（fine-tuning 导致 representation degradation），但从工程方案角度解决，我们从 mechanistic 角度刻画（R² exit collapse）
- **引用建议**: **建议引用** — Related Work 中作为"representation degradation during VLM→VLA fine-tuning"的工程方案对照

### Paper 2: "MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling"
- **作者**: 未完全确认
- **时间**: Nov 2025, [arXiv 2511.19878](https://arxiv.org/abs/2511.19878)
- **核心结论**: 首个 VLA robust fine-tuning 框架；visual encoders 保持接近 pretrained priors，action-oriented language layers 更自由适配。跨 MiniVLA / OpenVLA-OFT / CALVIN / LIBERO 提升 up to +30%
- **与我们的关系**: **互补** — 他们发现 visual encoder 需要保持稳定、language layers 可以更大幅适配，与我们发现的 exit layer action collapse 一致（deeper language layers 变化最大）
- **引用建议**: **建议引用** — 支撑我们 exit collapse 发现的实用验证

### Paper 3: "Head Pursuit: Probing Attention Specialization in Multimodal Transformers"
- **作者**: Lorenzo Basile et al.
- **时间**: Oct 2025, NeurIPS 2025 spotlight, [arXiv 2510.21518](https://arxiv.org/abs/2510.21518)
- **核心结论**: 用 SOMP 发现 VLM 中 attention heads 对语义/视觉概念的 specialization；editing 1% heads 可 suppress/enhance 目标概念
- **与我们的关系**: **方法论相关** — 他们研究 VLM attention head specialization，我们研究 VLA 中 instruction-dominant attention heads。他们的发现（头部 specialization 是普遍现象）支撑我们的 L1 attention 分析
- **引用建议**: **建议引用** — Related Work 中作为 attention specialization 的一般性方法论参考

### Paper 4: "Look Before Acting: Enhancing Vision Foundation Representations for VLA Models" (DeepVision-VLA)
- **作者**: 未完全确认
- **时间**: Mar 2026, [arXiv 2603.15618](https://arxiv.org/abs/2603.15618)
- **核心结论**: 发现 VLA 中 visual token sensitivity 在 deeper layers 逐渐降低；提出 VL-MoT 架构注入多层级 visual features 到深层，提升 9.0%/7.5%
- **与我们的关系**: **互补** — 他们独立观察到类似现象（deeper layers visual info loss），我们的 R² exit collapse 提供了 mechanistic 解释（action fine-tuning 重写了 exit layer representations）
- **引用建议**: **建议引用** — 独立验证了 deep-layer representation 变化的现象

### Paper 5: "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting" (VLM2VLA)
- **作者**: 未完全确认
- **时间**: Sep 2025, [arXiv 2509.22195](https://arxiv.org/abs/2509.22195)
- **核心结论**: 将 robot actions 重表示为自然语言描述，使 fine-tuning 数据与 VLM pretrained representation space 对齐，仅用 LoRA 即可避免 catastrophic forgetting
- **与我们的关系**: **互补** — 他们的方案本质上是减少 VLM→VLA transition 对表征空间的冲击，与我们发现的 exit collapse 机制一致
- **引用建议**: **建议引用**

### Paper 6: "Pretrained VLAs are Surprisingly Resistant to Forgetting in Continual Learning"
- **作者**: Liu, Huihan; Kim, Changyeon; Liu, Bo; Liu, Minghuan; Zhu, Yuke
- **时间**: Mar 2026, [arXiv 2603.03818](https://arxiv.org/abs/2603.03818)
- **核心结论**: Pretrained VLAs 在 continual learning 中极少遗忘；simple experience replay 几乎 zero forgetting；知识保留能力使技能快速恢复
- **与我们的关系**: **直接相关** — 他们的 "VLA→VLA resistant to forgetting" 与我们的 "VLA→VLA transition 无显著 collapse" 发现高度一致，从 continual learning 角度提供了互证
- **引用建议**: **建议引用** — 强烈互证我们的 VLA→VLA no-collapse 发现

### Paper 7: "Representational de-collapse: Interactions between SFT and ICL in Language Models"
- **作者**: 未完全确认
- **时间**: Mar 2026, ICLR 2026, [OpenReview](https://openreview.net/forum?id=iZ9eKf1ZCK)
- **核心结论**: SFT 沿 task labels 折叠 representations；ICL 可逆转此折叠恢复丰富表征
- **与我们的关系**: **概念相关** — "representational collapse from SFT" 的理论框架与我们的 "exit collapse from action fine-tuning" 概念相近，但在 NLP 而非 VLA 领域
- **引用建议**: **可以引用** — 作为 representation collapse 的 NLP 理论基础

### Paper 8: "Emergent World Representations in OpenVLA"
- **作者**: Marco Molinari, Leonardo Nevali, Saharsha Navani, Omar G. Younis
- **时间**: Sep 2025, [arXiv 2509.24559](https://arxiv.org/abs/2509.24559)
- **核心结论**: OpenVLA 内部编码了 emergent world model；linear probes 在 middle layers 发现 state transition 预测能力
- **与我们的关系**: **高度相关** — 同样对 OpenVLA 做 layer-wise probing 分析，发现 middle layers 信息最丰富
- **引用建议**: **需要确认** — 第一作者是 Marco Molinari，你们已引用的 "Molinari et al. 2025 — symbolic representations" 可能就是这篇。如果不是同一篇，则**必须引用**

### Paper 9: "From Intention to Execution: Probing the Generalization Boundaries of VLA Models"
- **作者**: Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng (NYU)
- **时间**: Jun 2025, [arXiv 2506.09930](https://arxiv.org/abs/2506.09930)
- **核心结论**: VLM backbone 赋予 VLA robust perceptual understanding 和 high-level planning ("good intentions")，但不能可靠转化为精确运动执行；fine-tuning 侵蚀 VLM 推理能力
- **与我们的关系**: 第一作者 Irving Fang 与你们已引用的 "Fang et al. 2025 — reasoning erosion" 可能是同一篇。如果不是，则**建议引用**
- **引用建议**: **需要确认是否已引用**

### Paper 10: "Controlling Vision-Language-Action Policies through Sparse Latent Directions"
- **作者**: 未完全确认
- **时间**: Sep 2025, NeurIPS 2025 Mech Interp Workshop, [OpenReview](https://openreview.net/forum?id=wtf3ww1EOL)
- **核心结论**: 在 SAE latent space 中 steer VLA 的 language backbone 实现 fine-grained action control
- **与我们的关系**: 可能与已引用的 Haon et al. 2025 是同一工作的 workshop 版本
- **引用建议**: **需要确认** — 如果是 Haon et al. 的 companion paper 则无需额外引用

---

## 结论

**无重大遗漏，但有几篇值得补充引用。**

核心发现：
1. **没有发现直接竞争论文** — 没有其他团队做过跨架构的 VLM→VLA exit collapse 机制分析，我们的工作在这个方向上是首创
2. **有 6 篇建议引用的互补论文**（Paper 1-6），它们从工程/训练/continual learning 角度验证了与我们发现一致的现象（representation degradation, forgetting resistance, attention specialization）
3. **有 2 篇需要确认是否已引用**（Paper 8 Molinari, Paper 9 Fang）— 请核实 bib 文件中 Molinari et al. 2025 和 Fang et al. 2025 对应的具体论文
4. Paper 6 (Liu et al. 2026 continual learning) 对我们 "VLA→VLA no collapse" 发现提供了最强独立互证

Sources:
- [Enhancing Generalization in VLA Models](https://arxiv.org/abs/2509.11417)
- [MAPS: Module-Wise Proximity Scheduling](https://arxiv.org/abs/2511.19878)
- [Head Pursuit: Attention Specialization](https://arxiv.org/abs/2510.21518)
- [Look Before Acting: DeepVision-VLA](https://arxiv.org/abs/2603.15618)
- [Actions as Language: VLM2VLA](https://arxiv.org/abs/2509.22195)
- [Pretrained VLAs Resistant to Forgetting](https://arxiv.org/abs/2603.03818)
- [Representational de-collapse (ICLR 2026)](https://openreview.net/forum?id=iZ9eKf1ZCK)
- [Emergent World Representations in OpenVLA](https://arxiv.org/abs/2509.24559)
- [From Intention to Execution](https://arxiv.org/abs/2506.09930)
- [Controlling VLA through Sparse Latent Directions](https://openreview.net/forum?id=wtf3ww1EOL)
- [Not All Features Are Created Equal](https://arxiv.org/abs/2603.19233)
- [Mechanistic Interpretability for Steering VLAs](https://arxiv.org/abs/2509.00328)
- [Sparse Autoencoders in VLA Models](https://arxiv.org/abs/2603.19183)
- [DySL-VLA](https://arxiv.org/abs/2602.22896)
- [NoTVLA](https://arxiv.org/abs/2510.03895)
- [VLA-GSE](https://arxiv.org/abs/2605.06175)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "uuid": "fdba3fe2-0ed5-43ac-bd36-ddd314f4a369",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2egCAfnEH3z58MGLUWLuv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 662,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 47719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1636
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

_source line 70_

搜索完成，整理结果。

## 搜索结果汇总
- 搜索了 8 组主要关键词 + 8 组跟进关键词
- 发现 **10 篇**潜在相关论文（排除已引用的）

---

## 需要关注的论文

### Paper 1: "Enhancing Generalization in VLA Models by Preserving Pretrained Representations"
- **作者**: Grover, Gopalkrishnan, Ai, Christensen, Su, Li
- **时间**: Sep 2025, [arXiv 2509.11417](https://arxiv.org/abs/2509.11417)
- **核心结论**: VLM→VLA fine-tuning 降解 pretrained representations，提出 dual-encoder（一个 frozen、一个 trainable）+ string-based action tokenizer + co-training 策略缓解
- **与我们的关系**: **直接互补** — 他们文档化了我们发现的同一现象（fine-tuning 导致 representation degradation），但从工程方案角度解决，我们从 mechanistic 角度刻画（R² exit collapse）
- **引用建议**: **建议引用** — Related Work 中作为"representation degradation during VLM→VLA fine-tuning"的工程方案对照

### Paper 2: "MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling"
- **作者**: 未完全确认
- **时间**: Nov 2025, [arXiv 2511.19878](https://arxiv.org/abs/2511.19878)
- **核心结论**: 首个 VLA robust fine-tuning 框架；visual encoders 保持接近 pretrained priors，action-oriented language layers 更自由适配。跨 MiniVLA / OpenVLA-OFT / CALVIN / LIBERO 提升 up to +30%
- **与我们的关系**: **互补** — 他们发现 visual encoder 需要保持稳定、language layers 可以更大幅适配，与我们发现的 exit layer action collapse 一致（deeper language layers 变化最大）
- **引用建议**: **建议引用** — 支撑我们 exit collapse 发现的实用验证

### Paper 3: "Head Pursuit: Probing Attention Specialization in Multimodal Transformers"
- **作者**: Lorenzo Basile et al.
- **时间**: Oct 2025, NeurIPS 2025 spotlight, [arXiv 2510.21518](https://arxiv.org/abs/2510.21518)
- **核心结论**: 用 SOMP 发现 VLM 中 attention heads 对语义/视觉概念的 specialization；editing 1% heads 可 suppress/enhance 目标概念
- **与我们的关系**: **方法论相关** — 他们研究 VLM attention head specialization，我们研究 VLA 中 instruction-dominant attention heads。他们的发现（头部 specialization 是普遍现象）支撑我们的 L1 attention 分析
- **引用建议**: **建议引用** — Related Work 中作为 attention specialization 的一般性方法论参考

### Paper 4: "Look Before Acting: Enhancing Vision Foundation Representations for VLA Models" (DeepVision-VLA)
- **作者**: 未完全确认
- **时间**: Mar 2026, [arXiv 2603.15618](https://arxiv.org/abs/2603.15618)
- **核心结论**: 发现 VLA 中 visual token sensitivity 在 deeper layers 逐渐降低；提出 VL-MoT 架构注入多层级 visual features 到深层，提升 9.0%/7.5%
- **与我们的关系**: **互补** — 他们独立观察到类似现象（deeper layers visual info loss），我们的 R² exit collapse 提供了 mechanistic 解释（action fine-tuning 重写了 exit layer representations）
- **引用建议**: **建议引用** — 独立验证了 deep-layer representation 变化的现象

### Paper 5: "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting" (VLM2VLA)
- **作者**: 未完全确认
- **时间**: Sep 2025, [arXiv 2509.22195](https://arxiv.org/abs/2509.22195)
- **核心结论**: 将 robot actions 重表示为自然语言描述，使 fine-tuning 数据与 VLM pretrained representation space 对齐，仅用 LoRA 即可避免 catastrophic forgetting
- **与我们的关系**: **互补** — 他们的方案本质上是减少 VLM→VLA transition 对表征空间的冲击，与我们发现的 exit collapse 机制一致
- **引用建议**: **建议引用**

### Paper 6: "Pretrained VLAs are Surprisingly Resistant to Forgetting in Continual Learning"
- **作者**: Liu, Huihan; Kim, Changyeon; Liu, Bo; Liu, Minghuan; Zhu, Yuke
- **时间**: Mar 2026, [arXiv 2603.03818](https://arxiv.org/abs/2603.03818)
- **核心结论**: Pretrained VLAs 在 continual learning 中极少遗忘；simple experience replay 几乎 zero forgetting；知识保留能力使技能快速恢复
- **与我们的关系**: **直接相关** — 他们的 "VLA→VLA resistant to forgetting" 与我们的 "VLA→VLA transition 无显著 collapse" 发现高度一致，从 continual learning 角度提供了互证
- **引用建议**: **建议引用** — 强烈互证我们的 VLA→VLA no-collapse 发现

### Paper 7: "Representational de-collapse: Interactions between SFT and ICL in Language Models"
- **作者**: 未完全确认
- **时间**: Mar 2026, ICLR 2026, [OpenReview](https://openreview.net/forum?id=iZ9eKf1ZCK)
- **核心结论**: SFT 沿 task labels 折叠 representations；ICL 可逆转此折叠恢复丰富表征
- **与我们的关系**: **概念相关** — "representational collapse from SFT" 的理论框架与我们的 "exit collapse from action fine-tuning" 概念相近，但在 NLP 而非 VLA 领域
- **引用建议**: **可以引用** — 作为 representation collapse 的 NLP 理论基础

### Paper 8: "Emergent World Representations in OpenVLA"
- **作者**: Marco Molinari, Leonardo Nevali, Saharsha Navani, Omar G. Younis
- **时间**: Sep 2025, [arXiv 2509.24559](https://arxiv.org/abs/2509.24559)
- **核心结论**: OpenVLA 内部编码了 emergent world model；linear probes 在 middle layers 发现 state transition 预测能力
- **与我们的关系**: **高度相关** — 同样对 OpenVLA 做 layer-wise probing 分析，发现 middle layers 信息最丰富
- **引用建议**: **需要确认** — 第一作者是 Marco Molinari，你们已引用的 "Molinari et al. 2025 — symbolic representations" 可能就是这篇。如果不是同一篇，则**必须引用**

### Paper 9: "From Intention to Execution: Probing the Generalization Boundaries of VLA Models"
- **作者**: Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng (NYU)
- **时间**: Jun 2025, [arXiv 2506.09930](https://arxiv.org/abs/2506.09930)
- **核心结论**: VLM backbone 赋予 VLA robust perceptual understanding 和 high-level planning ("good intentions")，但不能可靠转化为精确运动执行；fine-tuning 侵蚀 VLM 推理能力
- **与我们的关系**: 第一作者 Irving Fang 与你们已引用的 "Fang et al. 2025 — reasoning erosion" 可能是同一篇。如果不是，则**建议引用**
- **引用建议**: **需要确认是否已引用**

### Paper 10: "Controlling Vision-Language-Action Policies through Sparse Latent Directions"
- **作者**: 未完全确认
- **时间**: Sep 2025, NeurIPS 2025 Mech Interp Workshop, [OpenReview](https://openreview.net/forum?id=wtf3ww1EOL)
- **核心结论**: 在 SAE latent space 中 steer VLA 的 language backbone 实现 fine-grained action control
- **与我们的关系**: 可能与已引用的 Haon et al. 2025 是同一工作的 workshop 版本
- **引用建议**: **需要确认** — 如果是 Haon et al. 的 companion paper 则无需额外引用

---

## 结论

**无重大遗漏，但有几篇值得补充引用。**

核心发现：
1. **没有发现直接竞争论文** — 没有其他团队做过跨架构的 VLM→VLA exit collapse 机制分析，我们的工作在这个方向上是首创
2. **有 6 篇建议引用的互补论文**（Paper 1-6），它们从工程/训练/continual learning 角度验证了与我们发现一致的现象（representation degradation, forgetting resistance, attention specialization）
3. **有 2 篇需要确认是否已引用**（Paper 8 Molinari, Paper 9 Fang）— 请核实 bib 文件中 Molinari et al. 2025 和 Fang et al. 2025 对应的具体论文
4. Paper 6 (Liu et al. 2026 continual learning) 对我们 "VLA→VLA no collapse" 发现提供了最强独立互证

Sources:
- [Enhancing Generalization in VLA Models](https://arxiv.org/abs/2509.11417)
- [MAPS: Module-Wise Proximity Scheduling](https://arxiv.org/abs/2511.19878)
- [Head Pursuit: Attention Specialization](https://arxiv.org/abs/2510.21518)
- [Look Before Acting: DeepVision-VLA](https://arxiv.org/abs/2603.15618)
- [Actions as Language: VLM2VLA](https://arxiv.org/abs/2509.22195)
- [Pretrained VLAs Resistant to Forgetting](https://arxiv.org/abs/2603.03818)
- [Representational de-collapse (ICLR 2026)](https://openreview.net/forum?id=iZ9eKf1ZCK)
- [Emergent World Representations in OpenVLA](https://arxiv.org/abs/2509.24559)
- [From Intention to Execution](https://arxiv.org/abs/2506.09930)
- [Controlling VLA through Sparse Latent Directions](https://openreview.net/forum?id=wtf3ww1EOL)
- [Not All Features Are Created Equal](https://arxiv.org/abs/2603.19233)
- [Mechanistic Interpretability for Steering VLAs](https://arxiv.org/abs/2509.00328)
- [Sparse Autoencoders in VLA Models](https://arxiv.org/abs/2603.19183)
- [DySL-VLA](https://arxiv.org/abs/2602.22896)
- [NoTVLA](https://arxiv.org/abs/2510.03895)
- [VLA-GSE](https://arxiv.org/abs/2605.06175)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 269889,
  "duration_api_ms": 410726,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "1adb089a-6575-4e75-a1f4-cf573850b223",
  "total_cost_usd": 1.2547875,
  "usage": {
    "input_tokens": 2253,
    "cache_creation_input_tokens": 37514,
    "cache_read_input_tokens": 261090,
    "output_tokens": 10888,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37514,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 662,
        "output_tokens": 5030,
        "cache_read_input_tokens": 47719,
        "cache_creation_input_tokens": 1636,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1636
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 275980,
      "outputTokens": 12067,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 27,
      "costUSD": 0.606315,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2253,
      "outputTokens": 10888,
      "cacheReadInputTokens": 261090,
      "cacheCreationInputTokens": 37514,
      "webSearchRequests": 0,
      "costUSD": 0.6484725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3cecbbc5-c9fe-48f4-9f04-6093333424f3"
}
```

</details>

---
