# research lerobot official libero eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/workers/worker_research_lerobot_official_libero_eval_20260516T163536.log`
- **Structured JSON:** [`d6ab6af15b00e94b6ee5.json`](../../sessions/d6/d6ab6af15b00e94b6ee5.json)

## Before a recorded user message

46 recorded events

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
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "30766f10-b98c-4e74-83b7-07f60cee8cc9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1778962800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6f352aeb-4d89-4637-8d49-000d930bbd70",
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for existing LIBERO evaluation scripts in the huggingface/lerobot repository. Let me do this efficiently by:

1. Web searching for lerobot + LIBERO eval
2. Checking the server for installed lerobot package

Let me launch parallel searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "5a9f13ac-5f4c-4524-a9b2-5f4423eac777",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnN2nEjaueZ9wqqRLh9oYu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11782,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11782
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NkfCS43pLbnXxccC4R2YxY`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "23d48131-e233-42ce-a2c7-2f3b4b7457db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnN2nEjaueZ9wqqRLh9oYu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11782,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11782
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

_source line 6 · 2026-05-16T16:35:53.492Z_

<details><summary>↩ Tool result · `toolu_01NkfCS43pLbnXxccC4R2YxY`</summary>

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
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "1c96850e-9213-4a02-acfb-71080c2cc835",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me search the web and check the server in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "d3f5c111-51c6-4e1a-ac98-b385c1a25766",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cjm8NAUGC4i8fo5LBdKbrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 23623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

_source line 8_

并行搜索 lerobot 仓库和服务器本地安装。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "5e96d53f-fa7c-4513-8910-b8929c02f54a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cjm8NAUGC4i8fo5LBdKbrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 23623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ao8QNpkDRGN7t2ELD3VoDb`</summary>

```json
{
  "query": "site:github.com/huggingface/lerobot libero eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "8dbb0361-50f8-42f6-8f4f-502c431c6f8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cjm8NAUGC4i8fo5LBdKbrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 23623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PC8mBqzMHEihAAkjg8SfTG`</summary>

```json
{
  "query": "huggingface lerobot LIBERO evaluation script SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "837d9278-508d-4a5b-946d-cb73fe246ee2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cjm8NAUGC4i8fo5LBdKbrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 23623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YHTuvGb6SoLyapd6vVBPae`</summary>

```json
{
  "query": "site:github.com/huggingface/lerobot scripts/eval rollout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "67fd3128-f427-4b57-a022-7ec179b7650e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cjm8NAUGC4i8fo5LBdKbrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 23623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KBC4UdNhXtMe9wUv1s1ATa`</summary>

```json
{
  "server": "westd-27271",
  "command": "pip show lerobot 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "11724ce2-e646-455c-a444-1069d60db596",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cjm8NAUGC4i8fo5LBdKbrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 23623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

_source line 13 · 2026-05-16T16:36:04.680Z_

<details><summary>↩ Tool result · `toolu_01Ao8QNpkDRGN7t2ELD3VoDb`</summary>

```text
Web search results for query: "site:github.com/huggingface/lerobot libero eval"

Links: [{"title":"lerobot/docs/source/libero.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"},{"title":"eval on libero with joint action space model · Issue #2630 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2630"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"smolvla can not reproduce results in libero eval using official checkpoints · Issue #3264 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3264"},{"title":"How can i train and eval SmolVLA in libero? · Issue #2258 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2258"},{"title":"Reproducing pi0.5 results on libero · Issue #2375 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2375"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"feat(sim): Add Libero Env by jadechoghari · Pull Request #1984 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/pull/1984"},{"title":"lerobot/docs/source/xvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/xvla.mdx"},{"title":"Evaluation of Policies on Libero · Issue #2731 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2731"}]

The search results show information about LIBERO evaluation within the LeRobot framework. Here are the key findings:

## LIBERO Evaluation Documentation

LeRobot ported LIBERO into their framework and uses it mainly to evaluate SmolVLA, their lightweight Vision-Language-Action model. LIBERO is part of their multi-eval supported simulation, allowing benchmarking of policies on a single suite of tasks or across multiple suites at once.

## Basic Evaluation Command

You can evaluate policies using the command `lerobot-eval` with flags like `--env.task` to pick the suite (libero_object, libero_spatial, etc.), `--eval.batch_size` to control how many environments run in parallel, and `--eval.n_episodes` to set how many episodes to run in total.

## Multi-Suite Evaluation

You can pass a comma-separated list to `--env.task` for multi-suite evaluation, such as `--env.task=libero_object,libero_spatial`.

## Control Modes

LIBERO supports two control modes: relative and absolute, which matters because different VLA checkpoints are trained with different modes of action output and control parameterizations.

## Data Format Requirements

LeRobot enforces the `.images.*` prefix for any multi-modal visual features, and you should ensure your policy config input_features use the same naming keys, with dataset metadata keys following this convention during evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "f0a6af0b-561d-41c7-b1af-a3ee9801004f",
  "tool_use_result": {
    "query": "site:github.com/huggingface/lerobot libero eval",
    "results": [
      {
        "tool_use_id": "srvtoolu_016Leind3XBNuKRBPaWST3cn",
        "content": [
          {
            "title": "lerobot/docs/source/libero.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"
          },
          {
            "title": "eval on libero with joint action space model · Issue #2630 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2630"
          },
          {
            "title": "[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1316"
          },
          {
            "title": "smolvla can not reproduce results in libero eval using official checkpoints · Issue #3264 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3264"
          },
          {
            "title": "How can i train and eval SmolVLA in libero? · Issue #2258 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2258"
          },
          {
            "title": "Reproducing pi0.5 results on libero · Issue #2375 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2375"
          },
          {
            "title": "GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning",
            "url": "https://github.com/huggingface/lerobot"
          },
          {
            "title": "feat(sim): Add Libero Env by jadechoghari · Pull Request #1984 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/pull/1984"
          },
          {
            "title": "lerobot/docs/source/xvla.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/xvla.mdx"
          },
          {
            "title": "Evaluation of Policies on Libero · Issue #2731 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2731"
          }
        ]
      },
      "The search results show information about LIBERO evaluation within the LeRobot framework. Here are the key findings:\n\n## LIBERO Evaluation Documentation\n\nLeRobot ported LIBERO into their framework and uses it mainly to evaluate SmolVLA, their lightweight Vision-Language-Action model. LIBERO is part of their multi-eval supported simulation, allowing benchmarking of policies on a single suite of tasks or across multiple suites at once.\n\n## Basic Evaluation Command\n\nYou can evaluate policies using the command `lerobot-eval` with flags like `--env.task` to pick the suite (libero_object, libero_spatial, etc.), `--eval.batch_size` to control how many environments run in parallel, and `--eval.n_episodes` to set how many episodes to run in total.\n\n## Multi-Suite Evaluation\n\nYou can pass a comma-separated list to `--env.task` for multi-suite evaluation, such as `--env.task=libero_object,libero_spatial`.\n\n## Control Modes\n\nLIBERO supports two control modes: relative and absolute, which matters because different VLA checkpoints are trained with different modes of action output and control parameterizations.\n\n## Data Format Requirements\n\nLeRobot enforces the `.images.*` prefix for any multi-modal visual features, and you should ensure your policy config input_features use the same naming keys, with dataset metadata keys following this convention during evaluation."
    ],
    "durationSeconds": 7.2815341789999986
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T16:36:04.898Z_

<details><summary>↩ Tool result · `toolu_01PC8mBqzMHEihAAkjg8SfTG`</summary>

```text
Web search results for query: "huggingface lerobot LIBERO evaluation script SmolVLA"

Links: [{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"How can i train and eval SmolVLA in libero? · Issue #2258 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2258"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"}]

Based on the search results, here's what I found about the HuggingFace LeRobot LIBERO evaluation script and SmolVLA:

## LIBERO Evaluation with SmolVLA

At LeRobot, they ported LIBERO into their framework and used it mainly to evaluate SmolVLA, their lightweight Vision-Language-Action model. LIBERO is now part of LeRobot's multi-eval supported simulation, meaning you can benchmark your policies either on a single suite of tasks or across multiple suites at once with just a flag.

## The Evaluation Script

LeRobot provides a unified evaluation script to evaluate policies in simulation or on real hardware. The basic command structure for evaluating on LIBERO is:

The `lerobot-eval` command uses `--env.task` to pick the suite (libero_object, libero_spatial, etc.), `--eval.batch_size` to control how many environments run in parallel, and `--eval.n_episodes` to set how many episodes to run in total.

## Example Evaluation Commands

You can evaluate a single task suite or multiple suites:

For benchmarking a policy across multiple suites at once, you can pass a comma-separated list like: `lerobot-eval --policy.path="your-policy-id" --env.type=libero --env.task=libero_object,libero_spatial`

## SmolVLA Specifics

SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. This policy has been trained and pushed to the Hub using LeRobot.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "dcb5d00d-18ad-4a2b-b0bf-280e9efac8b7",
  "tool_use_result": {
    "query": "huggingface lerobot LIBERO evaluation script SmolVLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R3rbh7eJn3KwPdE66nV11E",
        "content": [
          {
            "title": "lerobot/smolvla_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/smolvla_base"
          },
          {
            "title": "[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1316"
          },
          {
            "title": "GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning",
            "url": "https://github.com/huggingface/lerobot"
          },
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/en/libero"
          },
          {
            "title": "SmolVLA · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/smolvla"
          },
          {
            "title": "How can i train and eval SmolVLA in libero? · Issue #2258 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2258"
          },
          {
            "title": "LIBERO-plus · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/main/libero_plus"
          },
          {
            "title": "Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2354"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero"
          },
          {
            "title": "SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data",
            "url": "https://huggingface.co/blog/smolvla"
          }
        ]
      },
      "Based on the search results, here's what I found about the HuggingFace LeRobot LIBERO evaluation script and SmolVLA:\n\n## LIBERO Evaluation with SmolVLA\n\nAt LeRobot, they ported LIBERO into their framework and used it mainly to evaluate SmolVLA, their lightweight Vision-Language-Action model. LIBERO is now part of LeRobot's multi-eval supported simulation, meaning you can benchmark your policies either on a single suite of tasks or across multiple suites at once with just a flag.\n\n## The Evaluation Script\n\nLeRobot provides a unified evaluation script to evaluate policies in simulation or on real hardware. The basic command structure for evaluating on LIBERO is:\n\nThe `lerobot-eval` command uses `--env.task` to pick the suite (libero_object, libero_spatial, etc.), `--eval.batch_size` to control how many environments run in parallel, and `--eval.n_episodes` to set how many episodes to run in total.\n\n## Example Evaluation Commands\n\nYou can evaluate a single task suite or multiple suites:\n\nFor benchmarking a policy across multiple suites at once, you can pass a comma-separated list like: `lerobot-eval --policy.path=\"your-policy-id\" --env.type=libero --env.task=libero_object,libero_spatial`\n\n## SmolVLA Specifics\n\nSmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. This policy has been trained and pushed to the Hub using LeRobot."
    ],
    "durationSeconds": 6.989152081999997
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T16:36:05.489Z_

<details><summary>↩ Tool result · `toolu_01YHTuvGb6SoLyapd6vVBPae`</summary>

```text
Web search results for query: "site:github.com/huggingface/lerobot scripts/eval rollout"

Links: [{"title":"lerobot/lerobot/scripts/eval.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/lerobot/scripts/eval.py"},{"title":"lerobot/src/lerobot/scripts/lerobot_eval.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_eval.py"},{"title":"Simulate latency v2 and use a policy wrapper to handle latency by alexander-soare · Pull Request #272 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/pull/272"},{"title":"Port HIL-SERL by michel-aractingi · Pull Request #565 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/pull/565"},{"title":"how to eval the policy trained by lerobot in real env? · Issue #305 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/305"},{"title":"Reproducing pi0.5 results on libero · Issue #2375 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2375"},{"title":"Release 0.6.0 · Issue #3134 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3134"},{"title":"[QUESTION] run a policy on a real robot · Issue #1439 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1439"},{"title":"fine tune SmolVLA in libero with tensor shape mismatch · Issue #2418 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2418"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"}]

I found the search results for the query `site:github.com/huggingface/lerobot scripts/eval rollout`. Here's what the results show:

## Key Findings:

The eval script is used to evaluate a policy on an environment by running rollouts and computing metrics.

### Rollout Function:

The search results reference rollout functionality within the evaluation scripts. The rollout_data function handles dictionaries, done_indices, start_episode_index, start_data_index, and fps parameters.

### Usage Examples:

To evaluate a model from the hub (e.g., lerobot/diffusion_pusht) for 10 episodes, you can run: `python lerobot/scripts/eval.py --policy.path=lerobot/diffusion_pusht --env.type=pusht --eval.batch_size=10 --eval.n_episodes=10 --use_amp=false --device=cuda`

Both examples require that the repo/folder contain at least `config.json` and `model.safetensors` files.

### Batch Environment Behavior:

All environments in the batch are run until the last environment is done, which means some data will probably need to be discarded for environments that aren't the first one to be done.

### Additional Features:

The eval.py::rollout function has a flag to simulate latency.

The main evaluation script is located at `lerobot/scripts/eval.py` (or `src/lerobot/scripts/lerobot_eval.py` in newer versions) and provides a comprehensive system for evaluating trained policies through simulated rollouts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "0ba8c15a-27f4-4bbf-8147-83cc0068bc6f",
  "tool_use_result": {
    "query": "site:github.com/huggingface/lerobot scripts/eval rollout",
    "results": [
      {
        "tool_use_id": "srvtoolu_012MvFj59JaPTXRVGNym2vmr",
        "content": [
          {
            "title": "lerobot/lerobot/scripts/eval.py at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/lerobot/scripts/eval.py"
          },
          {
            "title": "lerobot/src/lerobot/scripts/lerobot_eval.py at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_eval.py"
          },
          {
            "title": "Simulate latency v2 and use a policy wrapper to handle latency by alexander-soare · Pull Request #272 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/pull/272"
          },
          {
            "title": "Port HIL-SERL by michel-aractingi · Pull Request #565 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/pull/565"
          },
          {
            "title": "how to eval the policy trained by lerobot in real env? · Issue #305 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/305"
          },
          {
            "title": "Reproducing pi0.5 results on libero · Issue #2375 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2375"
          },
          {
            "title": "Release 0.6.0 · Issue #3134 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3134"
          },
          {
            "title": "[QUESTION] run a policy on a real robot · Issue #1439 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1439"
          },
          {
            "title": "fine tune SmolVLA in libero with tensor shape mismatch · Issue #2418 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2418"
          },
          {
            "title": "GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning",
            "url": "https://github.com/huggingface/lerobot"
          }
        ]
      },
      "I found the search results for the query `site:github.com/huggingface/lerobot scripts/eval rollout`. Here's what the results show:\n\n## Key Findings:\n\nThe eval script is used to evaluate a policy on an environment by running rollouts and computing metrics.\n\n### Rollout Function:\n\nThe search results reference rollout functionality within the evaluation scripts. The rollout_data function handles dictionaries, done_indices, start_episode_index, start_data_index, and fps parameters.\n\n### Usage Examples:\n\nTo evaluate a model from the hub (e.g., lerobot/diffusion_pusht) for 10 episodes, you can run: `python lerobot/scripts/eval.py --policy.path=lerobot/diffusion_pusht --env.type=pusht --eval.batch_size=10 --eval.n_episodes=10 --use_amp=false --device=cuda`\n\nBoth examples require that the repo/folder contain at least `config.json` and `model.safetensors` files.\n\n### Batch Environment Behavior:\n\nAll environments in the batch are run until the last environment is done, which means some data will probably need to be discarded for environments that aren't the first one to be done.\n\n### Additional Features:\n\nThe eval.py::rollout function has a flag to simulate latency.\n\nThe main evaluation script is located at `lerobot/scripts/eval.py` (or `src/lerobot/scripts/lerobot_eval.py` in newer versions) and provides a comprehensive system for evaluating trained policies through simulated rollouts."
    ],
    "durationSeconds": 6.940482739000003
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T16:36:05.511Z_

<details><summary>↩ Tool result · `toolu_01KBC4UdNhXtMe9wUv1s1ATa`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "9569f18e-5bd5-47b6-9d98-90295224625f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016BeW6EbYAsT82Mggotuyfz`</summary>

```json
{
  "server": "westd-27271",
  "command": "pip show lerobot",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "3dbd4a32-5c4d-4077-8796-c1deed6c8be2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNvr6L4o8iqE8r4G8oA8TJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3311,
      "cache_read_input_tokens": 24632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3311
      },
      "output_tokens": 65,
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

_source line 18 · 2026-05-16T16:36:08.985Z_

<details><summary>↩ Tool result · `toolu_016BeW6EbYAsT82Mggotuyfz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'pip' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "7b1df485-fc29-40f4-ace1-3e80ad70afa1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'pip' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'pip' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LcmW6QYdRohkqXZhb9vpfn`</summary>

```json
{
  "query": "site:huggingface.co/docs/lerobot libero evaluation command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "72f43ec7-c9ea-47c8-8cb2-7a9988f5b54b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNvr6L4o8iqE8r4G8oA8TJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3311,
      "cache_read_input_tokens": 24632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3311
      },
      "output_tokens": 65,
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

_source line 20 · 2026-05-16T16:36:15.577Z_

<details><summary>↩ Tool result · `toolu_01LcmW6QYdRohkqXZhb9vpfn`</summary>

````text
Web search results for query: "site:huggingface.co/docs/lerobot libero evaluation command"

Links: [{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"π₀-FAST (Pi0-FAST) · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi0fast"},{"title":"Environment Processors - LeRobot","url":"https://huggingface.co/docs/lerobot/en/env_processor"},{"title":"Imitation Learning on Real-World Robots · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/il_robots"},{"title":"Meta-World","url":"https://huggingface.co/docs/lerobot/en/metaworld"},{"title":"π₀.₅ (Pi05) Policy · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi05"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"NVIDIA IsaacLab Arena & LeRobot · Hugging Face","url":"https://huggingface.co/docs/lerobot/envhub_isaaclab_arena"},{"title":"X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task","url":"https://huggingface.co/docs/lerobot/en/xvla"}]

I found the information about LIBERO evaluation commands from the Hugging Face LeRobot documentation. Here's what the search results show:

## LIBERO Evaluation Command

To evaluate a finetuned model using the LeRobot LIBERO implementation, you can run the following command:

```
lerobot-eval \
  --output_dir=/logs/ \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --policy.path=pi05_libero_finetuned \
  --policy.n_action_steps=10 \
  --output_dir=./eval_logs/ \
  --env.max_parallel_tasks=1
```

## Key Parameters

- `--env.task` picks the suite (libero_object, libero_spatial, etc.)
- `--eval.batch_size` controls how many environments run in parallel
- `--eval.n_episodes` sets how many episodes to run in total

You can pass a comma-separated list to `--env.task` for multi-suite evaluation.

The documentation also shows a simpler example: 
```
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_object \
  --eval.batch_size=2 \
  --eval.n_episodes=3
```


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "0f3dff29-bbfe-49b8-8bb1-af8ebff7dc9b",
  "tool_use_result": {
    "query": "site:huggingface.co/docs/lerobot libero evaluation command",
    "results": [
      {
        "tool_use_id": "srvtoolu_015GqutfLAvqYmRWS4xKTHhe",
        "content": [
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/en/libero"
          },
          {
            "title": "LIBERO-plus · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/main/libero_plus"
          },
          {
            "title": "π₀-FAST (Pi0-FAST) · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/pi0fast"
          },
          {
            "title": "Environment Processors - LeRobot",
            "url": "https://huggingface.co/docs/lerobot/en/env_processor"
          },
          {
            "title": "Imitation Learning on Real-World Robots · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/en/il_robots"
          },
          {
            "title": "Meta-World",
            "url": "https://huggingface.co/docs/lerobot/en/metaworld"
          },
          {
            "title": "π₀.₅ (Pi05) Policy · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/pi05"
          },
          {
            "title": "SmolVLA · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/en/smolvla"
          },
          {
            "title": "NVIDIA IsaacLab Arena & LeRobot · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/envhub_isaaclab_arena"
          },
          {
            "title": "X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task",
            "url": "https://huggingface.co/docs/lerobot/en/xvla"
          }
        ]
      },
      "I found the information about LIBERO evaluation commands from the Hugging Face LeRobot documentation. Here's what the search results show:\n\n## LIBERO Evaluation Command\n\nTo evaluate a finetuned model using the LeRobot LIBERO implementation, you can run the following command:\n\n```\nlerobot-eval \\\n  --output_dir=/logs/ \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --policy.path=pi05_libero_finetuned \\\n  --policy.n_action_steps=10 \\\n  --output_dir=./eval_logs/ \\\n  --env.max_parallel_tasks=1\n```\n\n## Key Parameters\n\n- `--env.task` picks the suite (libero_object, libero_spatial, etc.)\n- `--eval.batch_size` controls how many environments run in parallel\n- `--eval.n_episodes` sets how many episodes to run in total\n\nYou can pass a comma-separated list to `--env.task` for multi-suite evaluation.\n\nThe documentation also shows a simpler example: \n```\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_object \\\n  --eval.batch_size=2 \\\n  --eval.n_episodes=3\n```"
    ],
    "durationSeconds": 6.167495949999997
  }
}
````

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WMkKvNfu9hdhNcNpumpoAt`</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/autodl-tmp -maxdepth 3 -name \"lerobot\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "ba702e2e-2efa-4d5d-8c1d-8ba98b4fd25f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwQCDqb17ky6xQdqBYFwU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 27943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1124
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

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0146kBij75kTBqRanJ9omDqo`</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root -path \"*/lerobot/scripts/*eval*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "41e0bd3d-aec2-4d79-b106-1a090c1323f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwQCDqb17ky6xQdqBYFwU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 27943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1124
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

_source line 23 · 2026-05-16T16:36:20.929Z_

<details><summary>↩ Tool result · `toolu_01WMkKvNfu9hdhNcNpumpoAt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/lerobot\\n/root/autodl-tmp/.hf_cache/lerobot/lerobot\\n/root/autodl-tmp/.hf_cache/._____temp/lerobot\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "171e1d99-cb09-4af2-80da-d444b521c0e7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/.hf_cache/lerobot\\\\n/root/autodl-tmp/.hf_cache/lerobot/lerobot\\\\n/root/autodl-tmp/.hf_cache/._____temp/lerobot\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/lerobot\\n/root/autodl-tmp/.hf_cache/lerobot/lerobot\\n/root/autodl-tmp/.hf_cache/._____temp/lerobot\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014tHpcm3vGWVZiVMGWdAt1B`</summary>

```json
{
  "query": "github.com/huggingface/lerobot blob main lerobot scripts eval.py libero"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "17ba382a-a5be-4aac-a36d-c2084abe5bb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwQCDqb17ky6xQdqBYFwU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 27943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1124
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

_source line 25 · 2026-05-16T16:36:21.584Z_

<details><summary>↩ Tool result · `toolu_0146kBij75kTBqRanJ9omDqo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/lerobot_eval.py\\n/root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/__pycache__/lerobot_eval.cpython-312.pyc\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "953f9385-1267-42e7-a650-8004d45bfabf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/lerobot_eval.py\\\\n/root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/__pycache__/lerobot_eval.cpython-312.pyc\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.64}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/lerobot_eval.py\\n/root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/__pycache__/lerobot_eval.cpython-312.pyc\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T16:36:28.115Z_

<details><summary>↩ Tool result · `toolu_014tHpcm3vGWVZiVMGWdAt1B`</summary>

```text
Web search results for query: "github.com/huggingface/lerobot blob main lerobot scripts eval.py libero"

Links: [{"title":"lerobot/src/lerobot/scripts/lerobot_eval.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_eval.py"},{"title":"lerobot/lerobot/scripts/eval.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/lerobot/scripts/eval.py"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"lerobot/README.md at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/README.md"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"lerobot/src/lerobot/scripts/lerobot_train.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_train.py"},{"title":"LeRobot/README.md at main · ai-completed/LeRobot","url":"https://github.com/ai-completed/LeRobot/blob/main/README.md"},{"title":"lerobot/docs/source/libero.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"},{"title":"lerobot/pyproject.toml at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/pyproject.toml"},{"title":"lerobot · PyPI","url":"https://pypi.org/project/lerobot/"}]

Based on the web search results, I found information about the LeRobot evaluation script and LIBERO benchmark integration. Here's what I found:

## Key Findings:

The evaluation script is located at `lerobot/lerobot/scripts/eval.py` and can be used to evaluate model checkpoints from the LeRobot training script.

LeRobot supports evaluating policies on the LIBERO benchmark using commands like: `lerobot-eval \ --policy.path=lerobot/pi0_libero_finetuned \ --env.type=libero \ --env.task=libero_object \ --eval.n_episodes=10`

The unified evaluation script allows you to evaluate your policies in simulation or on real hardware, and LeRobot supports standard benchmarks like LIBERO, MetaWorld and more.

The LIBERO benchmark offers several task suites including LIBERO-Spatial (tasks requiring spatial reasoning), LIBERO-Object (tasks centered on manipulating objects), LIBERO-Goal (goal-conditioned tasks), LIBERO-90 (90 short-horizon tasks), and LIBERO-Long (10 long-horizon tasks).

The search results point to the evaluation script functionality and how it integrates with LIBERO for benchmarking LeRobot policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "7e3392c3-3045-4c11-a9ec-7eec057b9f9d",
  "tool_use_result": {
    "query": "github.com/huggingface/lerobot blob main lerobot scripts eval.py libero",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B8bCy98RwBonmkvcgXqwtT",
        "content": [
          {
            "title": "lerobot/src/lerobot/scripts/lerobot_eval.py at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_eval.py"
          },
          {
            "title": "lerobot/lerobot/scripts/eval.py at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/lerobot/scripts/eval.py"
          },
          {
            "title": "GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning",
            "url": "https://github.com/huggingface/lerobot"
          },
          {
            "title": "lerobot/README.md at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/README.md"
          },
          {
            "title": "GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.",
            "url": "https://github.com/huggingface/lerobot-libero"
          },
          {
            "title": "lerobot/src/lerobot/scripts/lerobot_train.py at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_train.py"
          },
          {
            "title": "LeRobot/README.md at main · ai-completed/LeRobot",
            "url": "https://github.com/ai-completed/LeRobot/blob/main/README.md"
          },
          {
            "title": "lerobot/docs/source/libero.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"
          },
          {
            "title": "lerobot/pyproject.toml at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/pyproject.toml"
          },
          {
            "title": "lerobot · PyPI",
            "url": "https://pypi.org/project/lerobot/"
          }
        ]
      },
      "Based on the web search results, I found information about the LeRobot evaluation script and LIBERO benchmark integration. Here's what I found:\n\n## Key Findings:\n\nThe evaluation script is located at `lerobot/lerobot/scripts/eval.py` and can be used to evaluate model checkpoints from the LeRobot training script.\n\nLeRobot supports evaluating policies on the LIBERO benchmark using commands like: `lerobot-eval \\ --policy.path=lerobot/pi0_libero_finetuned \\ --env.type=libero \\ --env.task=libero_object \\ --eval.n_episodes=10`\n\nThe unified evaluation script allows you to evaluate your policies in simulation or on real hardware, and LeRobot supports standard benchmarks like LIBERO, MetaWorld and more.\n\nThe LIBERO benchmark offers several task suites including LIBERO-Spatial (tasks requiring spatial reasoning), LIBERO-Object (tasks centered on manipulating objects), LIBERO-Goal (goal-conditioned tasks), LIBERO-90 (90 short-horizon tasks), and LIBERO-Long (10 long-horizon tasks).\n\nThe search results point to the evaluation script functionality and how it integrates with LIBERO for benchmarking LeRobot policies."
    ],
    "durationSeconds": 6.526201838999994
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BsMz3sfEAyzUEpqt7tZHH5`</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/miniconda3/lib/python3.12/site-packages/lerobot -name \"*libero*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "a77fdd24-f08f-4a0f-a75a-5da40d2f801a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuKxVVZephobNnBxDhVweB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1672,
      "cache_read_input_tokens": 29067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1672
      },
      "output_tokens": 67,
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

_source line 28 · 2026-05-16T16:36:32.366Z_

<details><summary>↩ Tool result · `toolu_01BsMz3sfEAyzUEpqt7tZHH5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/lerobot/envs/libero.py\\n/root/miniconda3/lib/python3.12/site-packages/lerobot/envs/__pycache__/libero.cpython-312.pyc\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "3df3ee10-df43-420b-94eb-4b603a7f65c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/miniconda3/lib/python3.12/site-packages/lerobot/envs/libero.py\\\\n/root/miniconda3/lib/python3.12/site-packages/lerobot/envs/__pycache__/libero.cpython-312.pyc\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/lerobot/envs/libero.py\\n/root/miniconda3/lib/python3.12/site-packages/lerobot/envs/__pycache__/libero.cpython-312.pyc\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MwtoZ3rxUFnmXacUVvLbsr`</summary>

```json
{
  "server": "westd-27271",
  "command": "head -80 /root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/lerobot_eval.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "0c891354-111e-40b1-a1b3-1d96e0ad698d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuKxVVZephobNnBxDhVweB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1672,
      "cache_read_input_tokens": 29067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1672
      },
      "output_tokens": 67,
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

_source line 30 · 2026-05-16T16:36:33.112Z_

<details><summary>↩ Tool result · `toolu_01MwtoZ3rxUFnmXacUVvLbsr`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python\\n\\n# Copyright 2024 The HuggingFace Inc. team. All rights reserved.\\n#\\n# Licensed under the Apache License, Version 2.0 (the \\\"License\\\");\\n# you may not use this file except in compliance with the License.\\n# You may obtain a copy of the License at\\n#\\n#     http://www.apache.org/licenses/LICENSE-2.0\\n#\\n# Unless required by applicable law or agreed to in writing, software\\n# distributed under the License is distributed on an \\\"AS IS\\\" BASIS,\\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\n# See the License for the specific language governing permissions and\\n# limitations under the License.\\n\\\"\\\"\\\"Evaluate a policy on an environment by running rollouts and computing metrics.\\n\\nUsage examples:\\n\\nYou want to evaluate a model from the hub (eg: https://huggingface.co/lerobot/diffusion_pusht)\\nfor 10 episodes.\\n\\n```\\nlerobot-eval \\\\\\n    --policy.path=lerobot/diffusion_pusht \\\\\\n    --env.type=pusht \\\\\\n    --eval.batch_size=10 \\\\\\n    --eval.n_episodes=10 \\\\\\n    --policy.use_amp=false \\\\\\n    --policy.device=cuda\\n```\\n\\nOR, you want to evaluate a model checkpoint from the LeRobot training script for 10 episodes.\\n```\\nlerobot-eval \\\\\\n    --policy.path=outputs/train/diffusion_pusht/checkpoints/005000/pretrained_model \\\\\\n    --env.type=pusht \\\\\\n    --eval.batch_size=10 \\\\\\n    --eval.n_episodes=10 \\\\\\n    --policy.use_amp=false \\\\\\n    --policy.device=cuda\\n```\\n\\nNote that in both examples, the repo/folder should contain at least `config.json` and `model.safetensors` files.\\n\\nYou can learn about the CLI options for this script in the `EvalPipelineConfig` in lerobot/configs/eval.py\\n\\\"\\\"\\\"\\n\\nimport concurrent.futures as cf\\nimport json\\nimport logging\\nimport threading\\nimport time\\nfrom collections import defaultdict\\nfrom collections.abc import Callable\\nfrom contextlib import nullcontext\\nfrom copy import deepcopy\\nfrom dataclasses import asdict\\nfrom functools import partial\\nfrom pathlib import Path\\nfrom pprint import pformat\\nfrom typing import Any, TypedDict\\n\\nimport einops\\nimport gymnasium as gym\\nimport numpy as np\\nimport torch\\nfrom termcolor import colored\\nfrom torch import Tensor, nn\\nfrom tqdm import trange\\n\\nfrom lerobot.configs import parser\\nfrom lerobot.configs.eval import EvalPipelineConfig\\nfrom lerobot.envs.factory import make_env, make_env_pre_post_processors\\nfrom lerobot.envs.utils import (\\n    add_envs_task,\\n    check_env_attributes_and_types,\\n    close_envs,\\n    preprocess_observation,\\n)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "f3324aef-4075-4971-8335-c92036aff88d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python\\\\n\\\\n# Copyright 2024 The HuggingFace Inc. team. All rights reserved.\\\\n#\\\\n# Licensed under the Apache License, Version 2.0 (the \\\\\\\"License\\\\\\\");\\\\n# you may not use this file except in compliance with the License.\\\\n# You may obtain a copy of the License at\\\\n#\\\\n#     http://www.apache.org/licenses/LICENSE-2.0\\\\n#\\\\n# Unless required by applicable law or agreed to in writing, software\\\\n# distributed under the License is distributed on an \\\\\\\"AS IS\\\\\\\" BASIS,\\\\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\\\n# See the License for the specific language governing permissions and\\\\n# limitations under the License.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Evaluate a policy on an environment by running rollouts and computing metrics.\\\\n\\\\nUsage examples:\\\\n\\\\nYou want to evaluate a model from the hub (eg: https://huggingface.co/lerobot/diffusion_pusht)\\\\nfor 10 episodes.\\\\n\\\\n```\\\\nlerobot-eval \\\\\\\\\\\\n    --policy.path=lerobot/diffusion_pusht \\\\\\\\\\\\n    --env.type=pusht \\\\\\\\\\\\n    --eval.batch_size=10 \\\\\\\\\\\\n    --eval.n_episodes=10 \\\\\\\\\\\\n    --policy.use_amp=false \\\\\\\\\\\\n    --policy.device=cuda\\\\n```\\\\n\\\\nOR, you want to evaluate a model checkpoint from the LeRobot training script for 10 episodes.\\\\n```\\\\nlerobot-eval \\\\\\\\\\\\n    --policy.path=outputs/train/diffusion_pusht/checkpoints/005000/pretrained_model \\\\\\\\\\\\n    --env.type=pusht \\\\\\\\\\\\n    --eval.batch_size=10 \\\\\\\\\\\\n    --eval.n_episodes=10 \\\\\\\\\\\\n    --policy.use_amp=false \\\\\\\\\\\\n    --policy.device=cuda\\\\n```\\\\n\\\\nNote that in both examples, the repo/folder should contain at least `config.json` and `model.safetensors` files.\\\\n\\\\nYou can learn about the CLI options for this script in the `EvalPipelineConfig` in lerobot/configs/eval.py\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport concurrent.futures as cf\\\\nimport json\\\\nimport logging\\\\nimport threading\\\\nimport time\\\\nfrom collections import defaultdict\\\\nfrom collections.abc import Callable\\\\nfrom contextlib import nullcontext\\\\nfrom copy import deepcopy\\\\nfrom dataclasses import asdict\\\\nfrom functools import partial\\\\nfrom pathlib import Path\\\\nfrom pprint import pformat\\\\nfrom typing import Any, TypedDict\\\\n\\\\nimport einops\\\\nimport gymnasium as gym\\\\nimport numpy as np\\\\nimport torch\\\\nfrom termcolor import colored\\\\nfrom torch import Tensor, nn\\\\nfrom tqdm import trange\\\\n\\\\nfrom lerobot.configs import parser\\\\nfrom lerobot.configs.eval import EvalPipelineConfig\\\\nfrom lerobot.envs.factory import make_env, make_env_pre_post_processors\\\\nfrom lerobot.envs.utils import (\\\\n    add_envs_task,\\\\n    check_env_attributes_and_types,\\\\n    close_envs,\\\\n    preprocess_observation,\\\\n)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python\\n\\n# Copyright 2024 The HuggingFace Inc. team. All rights reserved.\\n#\\n# Licensed under the Apache License, Version 2.0 (the \\\"License\\\");\\n# you may not use this file except in compliance with the License.\\n# You may obtain a copy of the License at\\n#\\n#     http://www.apache.org/licenses/LICENSE-2.0\\n#\\n# Unless required by applicable law or agreed to in writing, software\\n# distributed under the License is distributed on an \\\"AS IS\\\" BASIS,\\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\n# See the License for the specific language governing permissions and\\n# limitations under the License.\\n\\\"\\\"\\\"Evaluate a policy on an environment by running rollouts and computing metrics.\\n\\nUsage examples:\\n\\nYou want to evaluate a model from the hub (eg: https://huggingface.co/lerobot/diffusion_pusht)\\nfor 10 episodes.\\n\\n```\\nlerobot-eval \\\\\\n    --policy.path=lerobot/diffusion_pusht \\\\\\n    --env.type=pusht \\\\\\n    --eval.batch_size=10 \\\\\\n    --eval.n_episodes=10 \\\\\\n    --policy.use_amp=false \\\\\\n    --policy.device=cuda\\n```\\n\\nOR, you want to evaluate a model checkpoint from the LeRobot training script for 10 episodes.\\n```\\nlerobot-eval \\\\\\n    --policy.path=outputs/train/diffusion_pusht/checkpoints/005000/pretrained_model \\\\\\n    --env.type=pusht \\\\\\n    --eval.batch_size=10 \\\\\\n    --eval.n_episodes=10 \\\\\\n    --policy.use_amp=false \\\\\\n    --policy.device=cuda\\n```\\n\\nNote that in both examples, the repo/folder should contain at least `config.json` and `model.safetensors` files.\\n\\nYou can learn about the CLI options for this script in the `EvalPipelineConfig` in lerobot/configs/eval.py\\n\\\"\\\"\\\"\\n\\nimport concurrent.futures as cf\\nimport json\\nimport logging\\nimport threading\\nimport time\\nfrom collections import defaultdict\\nfrom collections.abc import Callable\\nfrom contextlib import nullcontext\\nfrom copy import deepcopy\\nfrom dataclasses import asdict\\nfrom functools import partial\\nfrom pathlib import Path\\nfrom pprint import pformat\\nfrom typing import Any, TypedDict\\n\\nimport einops\\nimport gymnasium as gym\\nimport numpy as np\\nimport torch\\nfrom termcolor import colored\\nfrom torch import Tensor, nn\\nfrom tqdm import trange\\n\\nfrom lerobot.configs import parser\\nfrom lerobot.configs.eval import EvalPipelineConfig\\nfrom lerobot.envs.factory import make_env, make_env_pre_post_processors\\nfrom lerobot.envs.utils import (\\n    add_envs_task,\\n    check_env_attributes_and_types,\\n    close_envs,\\n    preprocess_observation,\\n)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
````

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013E8UuqYysSHV7M6b9Vhq6g`</summary>

```json
{
  "server": "westd-27271",
  "command": "head -60 /root/miniconda3/lib/python3.12/site-packages/lerobot/envs/libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "4a80e53c-b569-4eda-b8eb-56877fe34f63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWz9gpN8wp3eXc2HsvaRKL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1387,
      "cache_read_input_tokens": 30739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1387
      },
      "output_tokens": 71,
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

_source line 32 · 2026-05-16T16:36:37.916Z_

<details><summary>↩ Tool result · `toolu_013E8UuqYysSHV7M6b9Vhq6g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python\\n\\n# Copyright 2025 The HuggingFace Inc. team. All rights reserved.\\n#\\n# Licensed under the Apache License, Version 2.0 (the \\\"License\\\");\\n# you may not use this file except in compliance with the License.\\n# You may obtain a copy of the License at\\n#\\n#     http://www.apache.org/licenses/LICENSE-2.0\\n#\\n# Unless required by applicable law or agreed to in writing, software\\n# distributed under the License is distributed on an \\\"AS IS\\\" BASIS,\\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\n# See the License for the specific language governing permissions and\\n# limitations under the License.\\nfrom __future__ import annotations\\n\\nimport os\\nfrom collections import defaultdict\\nfrom collections.abc import Callable, Iterable, Mapping, Sequence\\nfrom functools import partial\\nfrom pathlib import Path\\nfrom typing import Any\\n\\nimport gymnasium as gym\\nimport numpy as np\\nimport torch\\nfrom gymnasium import spaces\\nfrom libero.libero import benchmark, get_libero_path\\nfrom libero.libero.envs import OffScreenRenderEnv\\n\\nfrom lerobot.types import RobotObservation\\n\\n\\ndef _parse_camera_names(camera_name: str | Sequence[str]) -> list[str]:\\n    \\\"\\\"\\\"Normalize camera_name into a non-empty list of strings.\\\"\\\"\\\"\\n    if isinstance(camera_name, str):\\n        cams = [c.strip() for c in camera_name.split(\\\",\\\") if c.strip()]\\n    elif isinstance(camera_name, (list | tuple)):\\n        cams = [str(c).strip() for c in camera_name if str(c).strip()]\\n    else:\\n        raise TypeError(f\\\"camera_name must be str or sequence[str], got {type(camera_name).__name__}\\\")\\n    if not cams:\\n        raise ValueError(\\\"camera_name resolved to an empty list.\\\")\\n    return cams\\n\\n\\ndef _get_suite(name: str) -> benchmark.Benchmark:\\n    \\\"\\\"\\\"Instantiate a LIBERO suite by name with clear validation.\\\"\\\"\\\"\\n    bench = benchmark.get_benchmark_dict()\\n    if name not in bench:\\n        raise ValueError(f\\\"Unknown LIBERO suite '{name}'. Available: {', '.join(sorted(bench.keys()))}\\\")\\n    suite = bench[name]()\\n    if not getattr(suite, \\\"tasks\\\", None):\\n        raise ValueError(f\\\"Suite '{name}' has no tasks.\\\")\\n    return suite\\n\\n\\ndef _select_task_ids(total_tasks: int, task_ids: Iterable[int] | None) -> list[int]:\\n    \\\"\\\"\\\"Validate/normalize task ids. If None → all tasks.\\\"\\\"\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "821842a0-e0f7-456b-970b-1399b5ec21f3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python\\\\n\\\\n# Copyright 2025 The HuggingFace Inc. team. All rights reserved.\\\\n#\\\\n# Licensed under the Apache License, Version 2.0 (the \\\\\\\"License\\\\\\\");\\\\n# you may not use this file except in compliance with the License.\\\\n# You may obtain a copy of the License at\\\\n#\\\\n#     http://www.apache.org/licenses/LICENSE-2.0\\\\n#\\\\n# Unless required by applicable law or agreed to in writing, software\\\\n# distributed under the License is distributed on an \\\\\\\"AS IS\\\\\\\" BASIS,\\\\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\\\n# See the License for the specific language governing permissions and\\\\n# limitations under the License.\\\\nfrom __future__ import annotations\\\\n\\\\nimport os\\\\nfrom collections import defaultdict\\\\nfrom collections.abc import Callable, Iterable, Mapping, Sequence\\\\nfrom functools import partial\\\\nfrom pathlib import Path\\\\nfrom typing import Any\\\\n\\\\nimport gymnasium as gym\\\\nimport numpy as np\\\\nimport torch\\\\nfrom gymnasium import spaces\\\\nfrom libero.libero import benchmark, get_libero_path\\\\nfrom libero.libero.envs import OffScreenRenderEnv\\\\n\\\\nfrom lerobot.types import RobotObservation\\\\n\\\\n\\\\ndef _parse_camera_names(camera_name: str | Sequence[str]) -> list[str]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Normalize camera_name into a non-empty list of strings.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    if isinstance(camera_name, str):\\\\n        cams = [c.strip() for c in camera_name.split(\\\\\\\",\\\\\\\") if c.strip()]\\\\n    elif isinstance(camera_name, (list | tuple)):\\\\n        cams = [str(c).strip() for c in camera_name if str(c).strip()]\\\\n    else:\\\\n        raise TypeError(f\\\\\\\"camera_name must be str or sequence[str], got {type(camera_name).__name__}\\\\\\\")\\\\n    if not cams:\\\\n        raise ValueError(\\\\\\\"camera_name resolved to an empty list.\\\\\\\")\\\\n    return cams\\\\n\\\\n\\\\ndef _get_suite(name: str) -> benchmark.Benchmark:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Instantiate a LIBERO suite by name with clear validation.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    bench = benchmark.get_benchmark_dict()\\\\n    if name not in bench:\\\\n        raise ValueError(f\\\\\\\"Unknown LIBERO suite '{name}'. Available: {', '.join(sorted(bench.keys()))}\\\\\\\")\\\\n    suite = bench[name]()\\\\n    if not getattr(suite, \\\\\\\"tasks\\\\\\\", None):\\\\n        raise ValueError(f\\\\\\\"Suite '{name}' has no tasks.\\\\\\\")\\\\n    return suite\\\\n\\\\n\\\\ndef _select_task_ids(total_tasks: int, task_ids: Iterable[int] | None) -> list[int]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Validate/normalize task ids. If None → all tasks.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python\\n\\n# Copyright 2025 The HuggingFace Inc. team. All rights reserved.\\n#\\n# Licensed under the Apache License, Version 2.0 (the \\\"License\\\");\\n# you may not use this file except in compliance with the License.\\n# You may obtain a copy of the License at\\n#\\n#     http://www.apache.org/licenses/LICENSE-2.0\\n#\\n# Unless required by applicable law or agreed to in writing, software\\n# distributed under the License is distributed on an \\\"AS IS\\\" BASIS,\\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\n# See the License for the specific language governing permissions and\\n# limitations under the License.\\nfrom __future__ import annotations\\n\\nimport os\\nfrom collections import defaultdict\\nfrom collections.abc import Callable, Iterable, Mapping, Sequence\\nfrom functools import partial\\nfrom pathlib import Path\\nfrom typing import Any\\n\\nimport gymnasium as gym\\nimport numpy as np\\nimport torch\\nfrom gymnasium import spaces\\nfrom libero.libero import benchmark, get_libero_path\\nfrom libero.libero.envs import OffScreenRenderEnv\\n\\nfrom lerobot.types import RobotObservation\\n\\n\\ndef _parse_camera_names(camera_name: str | Sequence[str]) -> list[str]:\\n    \\\"\\\"\\\"Normalize camera_name into a non-empty list of strings.\\\"\\\"\\\"\\n    if isinstance(camera_name, str):\\n        cams = [c.strip() for c in camera_name.split(\\\",\\\") if c.strip()]\\n    elif isinstance(camera_name, (list | tuple)):\\n        cams = [str(c).strip() for c in camera_name if str(c).strip()]\\n    else:\\n        raise TypeError(f\\\"camera_name must be str or sequence[str], got {type(camera_name).__name__}\\\")\\n    if not cams:\\n        raise ValueError(\\\"camera_name resolved to an empty list.\\\")\\n    return cams\\n\\n\\ndef _get_suite(name: str) -> benchmark.Benchmark:\\n    \\\"\\\"\\\"Instantiate a LIBERO suite by name with clear validation.\\\"\\\"\\\"\\n    bench = benchmark.get_benchmark_dict()\\n    if name not in bench:\\n        raise ValueError(f\\\"Unknown LIBERO suite '{name}'. Available: {', '.join(sorted(bench.keys()))}\\\")\\n    suite = bench[name]()\\n    if not getattr(suite, \\\"tasks\\\", None):\\n        raise ValueError(f\\\"Suite '{name}' has no tasks.\\\")\\n    return suite\\n\\n\\ndef _select_task_ids(total_tasks: int, task_ids: Iterable[int] | None) -> list[int]:\\n    \\\"\\\"\\\"Validate/normalize task ids. If None → all tasks.\\\"\\\"\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CuJCZE5z8AezifmznKF8H6`</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/miniconda3/lib/python3.12/site-packages/lerobot/configs -name \"*libero*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "bc90622c-6ee8-4a10-9670-53d3de028c46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWz9gpN8wp3eXc2HsvaRKL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1387,
      "cache_read_input_tokens": 30739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1387
      },
      "output_tokens": 71,
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

_source line 34 · 2026-05-16T16:36:38.522Z_

<details><summary>↩ Tool result · `toolu_01CuJCZE5z8AezifmznKF8H6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "7de9f5fb-e844-4842-88ca-401762bb42ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012z8m5oxtWjTYrpJEMHiU3x`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"success\" /root/miniconda3/lib/python3.12/site-packages/lerobot/envs/libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "8e2d789a-d3b2-4853-af9d-ceac6a15b256",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiNbuEmy4gkAnRCv9LGy6V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1233,
      "cache_read_input_tokens": 32126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1233
      },
      "output_tokens": 67,
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

_source line 36 · 2026-05-16T16:36:42.676Z_

<details><summary>↩ Tool result · `toolu_012z8m5oxtWjTYrpJEMHiU3x`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"319:        info = {\\\"is_success\\\": False}\\n330:        is_success = self._env.check_success()\\n331:        terminated = done or is_success\\n337:                \\\"is_success\\\": is_success,\\n346:                \\\"is_success\\\": bool(is_success),\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "aef7aec0-4c77-44a3-b37b-b64858546aa0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"319:        info = {\\\\\\\"is_success\\\\\\\": False}\\\\n330:        is_success = self._env.check_success()\\\\n331:        terminated = done or is_success\\\\n337:                \\\\\\\"is_success\\\\\\\": is_success,\\\\n346:                \\\\\\\"is_success\\\\\\\": bool(is_success),\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"319:        info = {\\\"is_success\\\": False}\\n330:        is_success = self._env.check_success()\\n331:        terminated = done or is_success\\n337:                \\\"is_success\\\": is_success,\\n346:                \\\"is_success\\\": bool(is_success),\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01U9TSYFsHB5SnHdPG37h5ud`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"libero\" /root/miniconda3/lib/python3.12/site-packages/lerobot/configs/ ",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "5de16298-96b8-4362-9e4b-e4feefb60581",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiNbuEmy4gkAnRCv9LGy6V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1233,
      "cache_read_input_tokens": 32126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1233
      },
      "output_tokens": 67,
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

_source line 38 · 2026-05-16T16:36:43.402Z_

<details><summary>↩ Tool result · `toolu_01U9TSYFsHB5SnHdPG37h5ud`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "bf4e6fc8-4c7b-4bce-b73d-47476d2bb027",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011GYbiJr42kKJmtgpRQ5CRa`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"libero\" /root/miniconda3/lib/python3.12/site-packages/lerobot/configs/eval.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "dfb6c8e8-bc40-4364-98d4-992d580b7b08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtEj8b728nosnsW6mV4csf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 33359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 551
      },
      "output_tokens": 72,
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

_source line 40 · 2026-05-16T16:36:52.417Z_

<details><summary>↩ Tool result · `toolu_011GYbiJr42kKJmtgpRQ5CRa`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "5ff32b2e-1747-48e5-be3a-9ba870074b5c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E3GXFCaoHZdjWKkVUTgp9g`</summary>

```json
{
  "server": "westd-27271",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "46388ce2-6858-40d9-bc19-ee2f7da286cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtEj8b728nosnsW6mV4csf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 33359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 551
      },
      "output_tokens": 72,
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

_source line 42 · 2026-05-16T16:36:53.195Z_

<details><summary>↩ Tool result · `toolu_01E3GXFCaoHZdjWKkVUTgp9g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\n_lerobot_compat.py\\nanalyze_gate.py\\nartifacts\\ncheckpoints\\nconfigs\\ndiag_ep42.py\\neval_acis_overhead.py\\neval_formal_bound.py\\neval_pruning_sweep.py\\neval_pruning_sweep.py.bak\\neval_results\\neval_sim.py\\neval_success_rate.py\\neval_success_rate.py.bak\\neval_token_importance.py\\nevaluate.py\\nevaluate.py.bak\\nevaluate.py.bak2\\nevaluate.py.bak_pre_d028\\nimm\\nlogs\\nresults\\nrun_d014_eval.sh\\nrun_eval_v8_fixed.sh\\nrun_mvp.sh\\nrun_traj_28k_30k_v2.sh\\nrun_traj_eval_28k_30k.sh\\nrun_traj_eval_补跑.sh\\nrun_v8_1_final_eval.sh\\nrun_v8_final_eval.sh\\nrun_v8b_final_eval.sh\\nrun_v8c_final_eval.sh\\nscan_collapse.py\\nscripts\\ntest_inference_fixes.py\\ntest_mode_collapse.py\\ntest_pretrained_sim.py\\ntrain.py\\ntrain_twostage.py\\nverify_grad_isolation.py\\nwandb\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "03e4e623-29fb-46f6-a43e-90c616ba2420",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"__pycache__\\\\n_lerobot_compat.py\\\\nanalyze_gate.py\\\\nartifacts\\\\ncheckpoints\\\\nconfigs\\\\ndiag_ep42.py\\\\neval_acis_overhead.py\\\\neval_formal_bound.py\\\\neval_pruning_sweep.py\\\\neval_pruning_sweep.py.bak\\\\neval_results\\\\neval_sim.py\\\\neval_success_rate.py\\\\neval_success_rate.py.bak\\\\neval_token_importance.py\\\\nevaluate.py\\\\nevaluate.py.bak\\\\nevaluate.py.bak2\\\\nevaluate.py.bak_pre_d028\\\\nimm\\\\nlogs\\\\nresults\\\\nrun_d014_eval.sh\\\\nrun_eval_v8_fixed.sh\\\\nrun_mvp.sh\\\\nrun_traj_28k_30k_v2.sh\\\\nrun_traj_eval_28k_30k.sh\\\\nrun_traj_eval_补跑.sh\\\\nrun_v8_1_final_eval.sh\\\\nrun_v8_final_eval.sh\\\\nrun_v8b_final_eval.sh\\\\nrun_v8c_final_eval.sh\\\\nscan_collapse.py\\\\nscripts\\\\ntest_inference_fixes.py\\\\ntest_mode_collapse.py\\\\ntest_pretrained_sim.py\\\\ntrain.py\\\\ntrain_twostage.py\\\\nverify_grad_isolation.py\\\\nwandb\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\n_lerobot_compat.py\\nanalyze_gate.py\\nartifacts\\ncheckpoints\\nconfigs\\ndiag_ep42.py\\neval_acis_overhead.py\\neval_formal_bound.py\\neval_pruning_sweep.py\\neval_pruning_sweep.py.bak\\neval_results\\neval_sim.py\\neval_success_rate.py\\neval_success_rate.py.bak\\neval_token_importance.py\\nevaluate.py\\nevaluate.py.bak\\nevaluate.py.bak2\\nevaluate.py.bak_pre_d028\\nimm\\nlogs\\nresults\\nrun_d014_eval.sh\\nrun_eval_v8_fixed.sh\\nrun_mvp.sh\\nrun_traj_28k_30k_v2.sh\\nrun_traj_eval_28k_30k.sh\\nrun_traj_eval_补跑.sh\\nrun_v8_1_final_eval.sh\\nrun_v8_final_eval.sh\\nrun_v8b_final_eval.sh\\nrun_v8c_final_eval.sh\\nscan_collapse.py\\nscripts\\ntest_inference_fixes.py\\ntest_mode_collapse.py\\ntest_pretrained_sim.py\\ntrain.py\\ntrain_twostage.py\\nverify_grad_isolation.py\\nwandb\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0121eu1H46JK52A6jU71EDx5`</summary>

```json
{
  "server": "westd-27271",
  "command": "head -50 /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "8a4e1485-f914-429b-942b-3ead08c93a47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FV8ikaQxozb5gauNqntxzH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 33910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
      },
      "output_tokens": 65,
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

_source line 44 · 2026-05-16T16:36:57.287Z_

<details><summary>↩ Tool result · `toolu_0121eu1H46JK52A6jU71EDx5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\neval_success_rate.py — Closed-loop rollout success rate evaluation in gym_aloha.\\n\\nUsage:\\n    python eval_success_rate.py --checkpoint_path checkpoints/baseline_v6_alpha16/latest/checkpoint.pt \\\\\\n        --config_path configs/baseline_v6_alpha16.yaml --mode baseline --num_episodes 50\\n    python eval_success_rate.py --checkpoint_path checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt \\\\\\n        --config_path configs/imm_anchor_v8b_twostage.yaml --mode acis_prune --num_episodes 50\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nTASK_TEXT = \\\"Insert the peg into the socket.\\\\n\\\"\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(\\n        description=\\\"Closed-loop rollout success rate evaluation for SmolVLA\\\"\\n    )\\n    p.add_argument(\\\"--checkpoint_path\\\", type=str, required=True,\\n                   help=\\\"Path to checkpoint.pt file\\\")\\n    p.add_argument(\\\"--config_path\\\", type=str, required=True,\\n                   help=\\\"Path to YAML config (e.g. configs/baseline_v6_alpha16.yaml)\\\")\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"acis_prune\\\", \\\"bypass\\\"], default=\\\"baseline\\\",\\n                   help=\\\"Evaluation mode: baseline (no ACIS), acis_prune (with ACIS), bypass (IMM model without ACIS)\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "fd8f0045-8ed0-451d-949d-d2ffd579f9eb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\neval_success_rate.py — Closed-loop rollout success rate evaluation in gym_aloha.\\\\n\\\\nUsage:\\\\n    python eval_success_rate.py --checkpoint_path checkpoints/baseline_v6_alpha16/latest/checkpoint.pt \\\\\\\\\\\\n        --config_path configs/baseline_v6_alpha16.yaml --mode baseline --num_episodes 50\\\\n    python eval_success_rate.py --checkpoint_path checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt \\\\\\\\\\\\n        --config_path configs/imm_anchor_v8b_twostage.yaml --mode acis_prune --num_episodes 50\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport sys\\\\nimport time as time_mod\\\\nfrom pathlib import Path\\\\n\\\\nos.environ.setdefault(\\\\\\\"MUJOCO_GL\\\\\\\", \\\\\\\"egl\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"TRANSFORMERS_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"HF_HUB_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\n\\\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%Y-%m-%d %H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\nTASK_TEXT = \\\\\\\"Insert the peg into the socket.\\\\\\\\n\\\\\\\"\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(\\\\n        description=\\\\\\\"Closed-loop rollout success rate evaluation for SmolVLA\\\\\\\"\\\\n    )\\\\n    p.add_argument(\\\\\\\"--checkpoint_path\\\\\\\", type=str, required=True,\\\\n                   help=\\\\\\\"Path to checkpoint.pt file\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--config_path\\\\\\\", type=str, required=True,\\\\n                   help=\\\\\\\"Path to YAML config (e.g. configs/baseline_v6_alpha16.yaml)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--mode\\\\\\\", choices=[\\\\\\\"baseline\\\\\\\", \\\\\\\"acis_prune\\\\\\\", \\\\\\\"bypass\\\\\\\"], default=\\\\\\\"baseline\\\\\\\",\\\\n                   help=\\\\\\\"Evaluation mode: baseline (no ACIS), acis_prune (with ACIS), bypass (IMM model without ACIS)\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\neval_success_rate.py — Closed-loop rollout success rate evaluation in gym_aloha.\\n\\nUsage:\\n    python eval_success_rate.py --checkpoint_path checkpoints/baseline_v6_alpha16/latest/checkpoint.pt \\\\\\n        --config_path configs/baseline_v6_alpha16.yaml --mode baseline --num_episodes 50\\n    python eval_success_rate.py --checkpoint_path checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt \\\\\\n        --config_path configs/imm_anchor_v8b_twostage.yaml --mode acis_prune --num_episodes 50\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nTASK_TEXT = \\\"Insert the peg into the socket.\\\\n\\\"\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(\\n        description=\\\"Closed-loop rollout success rate evaluation for SmolVLA\\\"\\n    )\\n    p.add_argument(\\\"--checkpoint_path\\\", type=str, required=True,\\n                   help=\\\"Path to checkpoint.pt file\\\")\\n    p.add_argument(\\\"--config_path\\\", type=str, required=True,\\n                   help=\\\"Path to YAML config (e.g. configs/baseline_v6_alpha16.yaml)\\\")\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"acis_prune\\\", \\\"bypass\\\"], default=\\\"baseline\\\",\\n                   help=\\\"Evaluation mode: baseline (no ACIS), acis_prune (with ACIS), bypass (IMM model without ACIS)\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

## 结论：**B. 有官方通用 eval pipeline 支持 LIBERO，且服务器已安装**

### 官方方案

lerobot 已内置 LIBERO eval 支持，服务器上已安装：
- **eval 脚本**: `/root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/lerobot_eval.py`
- **LIBERO env wrapper**: `/root/miniconda3/lib/python3.12/site-packages/lerobot/envs/libero.py`（内含 `check_success()` → `is_success` metric）

### 官方 eval 命令

```bash
lerobot-eval \
  --policy.path=&lt;checkpoint_path_or_hub_id> \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --policy.device=cuda
```

`--policy.path` 接受 Hub model ID 或本地目录（需包含 `config.json` + `model.safetensors`）。

### 与项目 checkpoint 的兼容性

项目已有自写的 `eval_success_rate.py`（基于 gym_aloha 环境，非 LIBERO）。要用官方 `lerobot-eval` 跑 LIBERO，checkpoint 需为 lerobot 标准格式（`config.json` + `model.safetensors`）。项目当前 checkpoint 是 `checkpoint.pt` 格式，**需要格式转换**才能使用官方 pipeline。

### 两个可选路径

| 方案 | 优点 | 缺点 |
|------|------|------|
| 用官方 `lerobot-eval --env.type=libero` | 零代码、multi-suite 一键跑、metric 标准化 | 需将 checkpoint 转为 lerobot pretrained_model 格式 |
| 自写 eval（参考已有 `eval_success_rate.py`，把 env 从 gym_aloha 换成 libero） | 直接读 `.pt` checkpoint、灵活控制 ACIS pruning 逻辑 | 需自己集成 libero env + rollout 逻辑 |

Sources:
- [lerobot LIBERO 官方文档](https://huggingface.co/docs/lerobot/en/libero)
- [lerobot_eval.py 源码](https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_eval.py)
- [SmolVLA LIBERO eval issue #1316](https://github.com/huggingface/lerobot/issues/1316)
- [lerobot-libero fork](https://github.com/huggingface/lerobot-libero)
- [SmolVLA 文档](https://huggingface.co/docs/lerobot/en/smolvla)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "uuid": "19e7b770-9e51-4475-8d5c-ea00bb431379",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVPzo7L1BLX3xg1TPGEgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 34745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 924
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

_source line 46_

## 结论：**B. 有官方通用 eval pipeline 支持 LIBERO，且服务器已安装**

### 官方方案

lerobot 已内置 LIBERO eval 支持，服务器上已安装：
- **eval 脚本**: `/root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/lerobot_eval.py`
- **LIBERO env wrapper**: `/root/miniconda3/lib/python3.12/site-packages/lerobot/envs/libero.py`（内含 `check_success()` → `is_success` metric）

### 官方 eval 命令

```bash
lerobot-eval \
  --policy.path=&lt;checkpoint_path_or_hub_id> \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --policy.device=cuda
```

`--policy.path` 接受 Hub model ID 或本地目录（需包含 `config.json` + `model.safetensors`）。

### 与项目 checkpoint 的兼容性

项目已有自写的 `eval_success_rate.py`（基于 gym_aloha 环境，非 LIBERO）。要用官方 `lerobot-eval` 跑 LIBERO，checkpoint 需为 lerobot 标准格式（`config.json` + `model.safetensors`）。项目当前 checkpoint 是 `checkpoint.pt` 格式，**需要格式转换**才能使用官方 pipeline。

### 两个可选路径

| 方案 | 优点 | 缺点 |
|------|------|------|
| 用官方 `lerobot-eval --env.type=libero` | 零代码、multi-suite 一键跑、metric 标准化 | 需将 checkpoint 转为 lerobot pretrained_model 格式 |
| 自写 eval（参考已有 `eval_success_rate.py`，把 env 从 gym_aloha 换成 libero） | 直接读 `.pt` checkpoint、灵活控制 ACIS pruning 逻辑 | 需自己集成 libero env + rollout 逻辑 |

Sources:
- [lerobot LIBERO 官方文档](https://huggingface.co/docs/lerobot/en/libero)
- [lerobot_eval.py 源码](https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_eval.py)
- [SmolVLA LIBERO eval issue #1316](https://github.com/huggingface/lerobot/issues/1316)
- [lerobot-libero fork](https://github.com/huggingface/lerobot-libero)
- [SmolVLA 文档](https://huggingface.co/docs/lerobot/en/smolvla)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 88351,
  "duration_api_ms": 101806,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "2ec157bf-0179-4412-8687-fd2470c34fcf",
  "total_cost_usd": 0.5071035,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 23828,
    "cache_read_input_tokens": 281985,
    "output_tokens": 2893,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 23828,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 830,
        "cache_read_input_tokens": 34745,
        "cache_creation_input_tokens": 924,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 924
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 82371,
      "outputTokens": 2485,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.144796,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 2893,
      "cacheReadInputTokens": 281985,
      "cacheCreationInputTokens": 23828,
      "webSearchRequests": 0,
      "costUSD": 0.36230750000000006,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "39b02bc6-4d8b-4bfb-ab38-9e7f22fb476f"
}
```

</details>

---
