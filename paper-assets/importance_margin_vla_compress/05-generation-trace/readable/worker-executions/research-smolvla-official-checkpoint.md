# research smolvla official checkpoint

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_research_smolvla_official_checkpoint_20260518T115208.log`
- **Structured JSON:** [`7eed8f790d147b8568c1.json`](../../sessions/7e/7eed8f790d147b8568c1.json)

## Before a recorded user message

42 recorded events

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
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
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
  "uuid": "5ae1b5b2-ad0b-427e-8315-d8dcf8f1656f",
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
    "resetsAt": 1779122400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a49ec6a8-0a1c-42b5-bc30-ea6c48d24e64",
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for SmolVLA LIBERO finetuned checkpoints on HuggingFace. Let me use WebSearch to find this information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "ff6afe90-61db-47fe-80ff-a70f1f312ff6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4z3sRqNwmegLypR64rx6r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12549,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12549
      },
      "output_tokens": 39,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EDULmTKD31hZYW8XXuy5V8`</summary>

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
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "a4920be8-b70b-4b33-ae25-ba9ae1049fa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4z3sRqNwmegLypR64rx6r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12549,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12549
      },
      "output_tokens": 39,
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

_source line 6 · 2026-05-18T11:52:20.849Z_

<details><summary>↩ Tool result · `toolu_01EDULmTKD31hZYW8XXuy5V8`</summary>

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
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "1e765add-a7ec-439a-854c-81a0797c23c2",
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
Let me run multiple web searches in parallel to find SmolVLA LIBERO finetuned checkpoints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "672049e5-143f-4235-b252-abeb1083f274",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZwpyQtjAXyGWzLMr4qe3C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 24390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 657
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

_source line 8_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AQAUXDGwRCvekwWoz8GFH6`</summary>

```json
{
  "query": "SmolVLA HuggingFace LIBERO finetuned checkpoint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "796e9e38-b343-4e51-8f3a-64c0c86a1a1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZwpyQtjAXyGWzLMr4qe3C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 24390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 657
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HuYEG7KxmoUtzZZSo6cvkq`</summary>

```json
{
  "query": "site:huggingface.co SmolVLA LIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "ffedb3db-4b30-4568-a8a6-5641cfcb2d3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZwpyQtjAXyGWzLMr4qe3C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 24390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 657
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015UdE7zSWbR5kgo2mo66DhL`</summary>

```json
{
  "query": "HuggingFaceVLA SmolVLA LIBERO batch 64"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "3707fa81-ecdf-4b1a-8331-60edeed7588d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZwpyQtjAXyGWzLMr4qe3C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 24390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 657
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

_source line 11 · 2026-05-18T11:52:29.226Z_

<details><summary>↩ Tool result · `toolu_01HuYEG7KxmoUtzZZSo6cvkq`</summary>

```text
Web search results for query: "site:huggingface.co SmolVLA LIBERO"

Links: [{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"bicmol/smolvla-libero · Hugging Face","url":"https://huggingface.co/bicmol/smolvla-libero"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"Alkatt/smolvla-libero-100000 · Hugging Face","url":"https://huggingface.co/Alkatt/smolvla-libero-100000"},{"title":"irisWU23/smolVLA_libero · Hugging Face","url":"https://huggingface.co/irisWU23/smolVLA_libero"},{"title":"HuggingFaceVLA/smolvla_libero_ckpts · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts"}]

I found search results for SmolVLA and LIBERO on Hugging Face. Here's what I found:

SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. This policy has been trained and pushed to the Hub using LeRobot.

Regarding SmolVLA's performance on LIBERO, SmolVLA-450M outperforms much larger VLAs and strong baselines such as ACT on simulation (LIBERO, Meta-World) and real-world tasks (SO100, SO101).

Additionally, there's a related resource called Smol-LIBERO, a compact version of the LIBERO benchmark built to make experimentation fast and accessible at just 1.79 GB (compared to ~34 GB for the full LIBERO).

The main model repository is available at: https://huggingface.co/HuggingFaceVLA/smolvla_libero


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "3714932c-4b9f-4d4e-a9a2-7c475f92a5db",
  "tool_use_result": {
    "query": "site:huggingface.co SmolVLA LIBERO",
    "results": [
      {
        "tool_use_id": "srvtoolu_012VUoiXBRqYawbvD8NSWUEL",
        "content": [
          {
            "title": "HuggingFaceVLA/smolvla_libero · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero"
          },
          {
            "title": "SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data",
            "url": "https://huggingface.co/blog/smolvla"
          },
          {
            "title": "HuggingFaceVLA/smol-libero · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"
          },
          {
            "title": "bicmol/smolvla-libero · Hugging Face",
            "url": "https://huggingface.co/bicmol/smolvla-libero"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero at main",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"
          },
          {
            "title": "lerobot/smolvla_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/smolvla_base"
          },
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/en/libero"
          },
          {
            "title": "Alkatt/smolvla-libero-100000 · Hugging Face",
            "url": "https://huggingface.co/Alkatt/smolvla-libero-100000"
          },
          {
            "title": "irisWU23/smolVLA_libero · Hugging Face",
            "url": "https://huggingface.co/irisWU23/smolVLA_libero"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero_ckpts · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts"
          }
        ]
      },
      "I found search results for SmolVLA and LIBERO on Hugging Face. Here's what I found:\n\nSmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. This policy has been trained and pushed to the Hub using LeRobot.\n\nRegarding SmolVLA's performance on LIBERO, SmolVLA-450M outperforms much larger VLAs and strong baselines such as ACT on simulation (LIBERO, Meta-World) and real-world tasks (SO100, SO101).\n\nAdditionally, there's a related resource called Smol-LIBERO, a compact version of the LIBERO benchmark built to make experimentation fast and accessible at just 1.79 GB (compared to ~34 GB for the full LIBERO).\n\nThe main model repository is available at: https://huggingface.co/HuggingFaceVLA/smolvla_libero"
    ],
    "durationSeconds": 4.687483013000001
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T11:52:30.348Z_

<details><summary>↩ Tool result · `toolu_01AQAUXDGwRCvekwWoz8GFH6`</summary>

```text
Web search results for query: "SmolVLA HuggingFace LIBERO finetuned checkpoint"

Links: [{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"bicmol/smolvla-libero · Hugging Face","url":"https://huggingface.co/bicmol/smolvla-libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"k1000dai/smolvla_libero_finetune · Hugging Face","url":"https://huggingface.co/k1000dai/smolvla_libero_finetune"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"},{"title":"Alkatt/smolvla-libero-100000 · Hugging Face","url":"https://huggingface.co/Alkatt/smolvla-libero-100000"},{"title":"ezzzeee/my_smolvla · Hugging Face","url":"https://huggingface.co/ezzzeee/my_smolvla"}]

Based on the search results, here's what I found about SmolVLA HuggingFace LIBERO finetuned checkpoints:

## Official SmolVLA LIBERO Checkpoint

SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. The official HuggingFace checkpoint is available at **HuggingFaceVLA/smolvla_libero** on Hugging Face Hub.

## Multiple Finetuned Variants

There are several community-created SmolVLA LIBERO finetuned checkpoints available on Hugging Face Hub:

1. **HuggingFaceVLA/smolvla_libero** - The official checkpoint with 4,446 finetuned steps
2. **bicmol/smolvla-libero** - A community checkpoint with 1,299 finetuned steps
3. **k1000dai/smolvla_libero_finetune** - Another variant with 4,634 finetuned steps
4. **Alkatt/smolvla-libero-100000** - A version trained for 100,000 steps

## Usage Notes

Since LIBERO is a common benchmark dataset, there's a pretrained SmolVLA checkpoint available, which provides a good starting point for fine-tuning. This policy has been trained and pushed to the Hub using LeRobot.

All of these checkpoints are based on the `lerobot/smolvla_base` model and are trained for robotics tasks using the LeRobot framework. You can find and compare these checkpoints directly on the Hugging Face Hub by searching for "smolvla_libero".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "b20a4d83-503a-4401-9c4d-4935c8e32143",
  "tool_use_result": {
    "query": "SmolVLA HuggingFace LIBERO finetuned checkpoint",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GoMduHH7th8Me2DLGrFErz",
        "content": [
          {
            "title": "HuggingFaceVLA/smolvla_libero · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero"
          },
          {
            "title": "Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"
          },
          {
            "title": "SmolVLA · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/smolvla"
          },
          {
            "title": "bicmol/smolvla-libero · Hugging Face",
            "url": "https://huggingface.co/bicmol/smolvla-libero"
          },
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/en/libero"
          },
          {
            "title": "k1000dai/smolvla_libero_finetune · Hugging Face",
            "url": "https://huggingface.co/k1000dai/smolvla_libero_finetune"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"
          },
          {
            "title": "Alkatt/smolvla-libero-100000 · Hugging Face",
            "url": "https://huggingface.co/Alkatt/smolvla-libero-100000"
          },
          {
            "title": "ezzzeee/my_smolvla · Hugging Face",
            "url": "https://huggingface.co/ezzzeee/my_smolvla"
          }
        ]
      },
      "Based on the search results, here's what I found about SmolVLA HuggingFace LIBERO finetuned checkpoints:\n\n## Official SmolVLA LIBERO Checkpoint\n\nSmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. The official HuggingFace checkpoint is available at **HuggingFaceVLA/smolvla_libero** on Hugging Face Hub.\n\n## Multiple Finetuned Variants\n\nThere are several community-created SmolVLA LIBERO finetuned checkpoints available on Hugging Face Hub:\n\n1. **HuggingFaceVLA/smolvla_libero** - The official checkpoint with 4,446 finetuned steps\n2. **bicmol/smolvla-libero** - A community checkpoint with 1,299 finetuned steps\n3. **k1000dai/smolvla_libero_finetune** - Another variant with 4,634 finetuned steps\n4. **Alkatt/smolvla-libero-100000** - A version trained for 100,000 steps\n\n## Usage Notes\n\nSince LIBERO is a common benchmark dataset, there's a pretrained SmolVLA checkpoint available, which provides a good starting point for fine-tuning. This policy has been trained and pushed to the Hub using LeRobot.\n\nAll of these checkpoints are based on the `lerobot/smolvla_base` model and are trained for robotics tasks using the LeRobot framework. You can find and compare these checkpoints directly on the Hugging Face Hub by searching for \"smolvla_libero\"."
    ],
    "durationSeconds": 5.940343281
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T11:52:31.102Z_

<details><summary>↩ Tool result · `toolu_015UdE7zSWbR5kgo2mo66DhL`</summary>

```text
Web search results for query: "HuggingFaceVLA SmolVLA LIBERO batch 64"

Links: [{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"The performance of SmolVLA on LIBERO cannot be replicated · Issue #1369 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1369"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"LIBERO Leaderboard - a Hugging Face Space by HuggingFaceVLA","url":"https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"Question about the HuggingFaceVLA/smolvla_libero Model Configuration · Issue #2294 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2294"},{"title":"blog/smolvla.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/smolvla.md"},{"title":"HuggingFaceVLA/smolvla_libero_ckpts · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts"}]

Based on the search results, here's what I found about HuggingFaceVLA SmolVLA, LIBERO, and batch 64:

## SmolVLA Overview
SmolVLA is a 450M parameter vision-language-action model designed for affordable and efficient robotics, optimized to run on consumer hardware while maintaining competitive performance. SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware.

## LIBERO Benchmark
There's a pretrained SmolVLA checkpoint available for LIBERO, which provides a good starting point for fine-tuning. SmolVLA-450M outperforms much larger VLAs and strong baselines such as ACT on simulation (LIBERO, Meta-World) and real-world tasks (SO100, SO101).

## Training with Batch Size 64
Training SmolVLA can be performed using the HuggingFaceVLA/smolvla_libero pretrained path with a batch size of 64 in training scripts. Additionally, batch_size=64 is commonly used in training configurations for SmolVLA fine-tuning.

The search results show practical examples of using SmolVLA with the LIBERO dataset and batch size 64 for training and fine-tuning robotics policies through the LeRobot framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "839edde1-e58e-4001-b69e-a216318771a6",
  "tool_use_result": {
    "query": "HuggingFaceVLA SmolVLA LIBERO batch 64",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UwbPnrxFhAkZWKnkFc3TXk",
        "content": [
          {
            "title": "Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero"
          },
          {
            "title": "HuggingFaceVLA/smol-libero · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"
          },
          {
            "title": "The performance of SmolVLA on LIBERO cannot be replicated · Issue #1369 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1369"
          },
          {
            "title": "SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics",
            "url": "https://smolvla.net/index_en"
          },
          {
            "title": "LIBERO Leaderboard - a Hugging Face Space by HuggingFaceVLA",
            "url": "https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero at main",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"
          },
          {
            "title": "Question about the HuggingFaceVLA/smolvla_libero Model Configuration · Issue #2294 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2294"
          },
          {
            "title": "blog/smolvla.md at main · huggingface/blog",
            "url": "https://github.com/huggingface/blog/blob/main/smolvla.md"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero_ckpts · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts"
          }
        ]
      },
      "Based on the search results, here's what I found about HuggingFaceVLA SmolVLA, LIBERO, and batch 64:\n\n## SmolVLA Overview\nSmolVLA is a 450M parameter vision-language-action model designed for affordable and efficient robotics, optimized to run on consumer hardware while maintaining competitive performance. SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware.\n\n## LIBERO Benchmark\nThere's a pretrained SmolVLA checkpoint available for LIBERO, which provides a good starting point for fine-tuning. SmolVLA-450M outperforms much larger VLAs and strong baselines such as ACT on simulation (LIBERO, Meta-World) and real-world tasks (SO100, SO101).\n\n## Training with Batch Size 64\nTraining SmolVLA can be performed using the HuggingFaceVLA/smolvla_libero pretrained path with a batch size of 64 in training scripts. Additionally, batch_size=64 is commonly used in training configurations for SmolVLA fine-tuning.\n\nThe search results show practical examples of using SmolVLA with the LIBERO dataset and batch size 64 for training and fine-tuning robotics policies through the LeRobot framework."
    ],
    "durationSeconds": 6.211672549999999
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
I found the key results. Let me now dig deeper into two important findings:

1. `HuggingFaceVLA/smolvla_libero` - the official checkpoint
2. `HuggingFaceVLA/smolvla_libero_ckpts` - checkpoints repo
3. The GitHub issue about performance replication (#1369)

Let me search for more details on these.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "caf01cdf-5c5f-4753-97f1-4964a7385e05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184i42LNMhF8LSg57omcTqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 25047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2901
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

_source line 15_

找到了官方 checkpoint。让我进一步确认训练配置和 SR。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "8b1cfca0-0153-402f-9c56-2eda3671edeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184i42LNMhF8LSg57omcTqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 25047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2901
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UAANrCirsLfZTWvc1BmPuW`</summary>

```json
{
  "query": "site:huggingface.co HuggingFaceVLA/smolvla_libero training config batch_size steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "c8ecf683-0371-4566-8b6a-68524b65d3d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184i42LNMhF8LSg57omcTqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 25047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2901
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014htGBKyhUU9yvZgfayZj8a`</summary>

```json
{
  "query": "github huggingface lerobot issue 1369 SmolVLA LIBERO replicate performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "1caccf5f-dfe0-47f6-bc62-502ee4bba0fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184i42LNMhF8LSg57omcTqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 25047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2901
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QMZwdz6o11Xwgt25LXnmPD`</summary>

```json
{
  "query": "SmolVLA LIBERO 87.3 success rate batch_size 64 training details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "a2fd0224-d17d-4eff-9ae7-a0ad57a5bc4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184i42LNMhF8LSg57omcTqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 25047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2901
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

_source line 19 · 2026-05-18T11:52:42.019Z_

<details><summary>↩ Tool result · `toolu_01UAANrCirsLfZTWvc1BmPuW`</summary>

```text
Web search results for query: "site:huggingface.co HuggingFaceVLA/smolvla_libero training config batch_size steps"

Links: [{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"Meta-World · Hugging Face","url":"https://huggingface.co/docs/lerobot/metaworld"},{"title":"train_config.json · Alkatt/smolvla-libero-100000 at main","url":"https://huggingface.co/Alkatt/smolvla-libero-100000/blob/main/train_config.json"}]

Based on the search results, I found relevant information about the HuggingFaceVLA/smolvla_libero training configuration:

The training command for SmolVLA on LIBERO uses 100,000 steps and a batch size of 4, as shown in the documented training example. 

Additionally, the Physical Intelligence LIBERO base model (pi05_libero) was finetuned for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset.

The search results show example training configurations, though the specific original training config for HuggingFaceVLA/smolvla_libero with its exact hyperparameters may be accessible through the model repository files (such as the train_config.json files mentioned in the results).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "b4ed7e35-da31-4f58-aba8-6a1bd04335dd",
  "tool_use_result": {
    "query": "site:huggingface.co HuggingFaceVLA/smolvla_libero training config batch_size steps",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EGhxzX126cuKEGNRofhxke",
        "content": [
          {
            "title": "SmolVLA · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/smolvla"
          },
          {
            "title": "LIBERO · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/libero"
          },
          {
            "title": "lerobot/smolvla_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/smolvla_base"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero"
          },
          {
            "title": "HuggingFaceVLA/smol-libero · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"
          },
          {
            "title": "LIBERO-plus · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/main/libero_plus"
          },
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/main/en/libero"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero at main",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"
          },
          {
            "title": "Meta-World · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/metaworld"
          },
          {
            "title": "train_config.json · Alkatt/smolvla-libero-100000 at main",
            "url": "https://huggingface.co/Alkatt/smolvla-libero-100000/blob/main/train_config.json"
          }
        ]
      },
      "Based on the search results, I found relevant information about the HuggingFaceVLA/smolvla_libero training configuration:\n\nThe training command for SmolVLA on LIBERO uses 100,000 steps and a batch size of 4, as shown in the documented training example. \n\nAdditionally, the Physical Intelligence LIBERO base model (pi05_libero) was finetuned for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset.\n\nThe search results show example training configurations, though the specific original training config for HuggingFaceVLA/smolvla_libero with its exact hyperparameters may be accessible through the model repository files (such as the train_config.json files mentioned in the results)."
    ],
    "durationSeconds": 5.205719408999998
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T11:52:43.469Z_

<details><summary>↩ Tool result · `toolu_014htGBKyhUU9yvZgfayZj8a`</summary>

```text
Web search results for query: "github huggingface lerobot issue 1369 SmolVLA LIBERO replicate performance"

Links: [{"title":"The performance of SmolVLA on LIBERO cannot be replicated · Issue #1369 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1369"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2107"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"smolvla can not reproduce results in libero eval using official checkpoints · Issue #3264 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3264"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"}]

Based on the web search results, I found information about GitHub issue #1369 in the Hugging Face LeRobot repository:

Issue #1369, opened on June 23, 2025, reports that a user trained SmolVLA from scratch on the LIBERO dataset but couldn't reproduce its results from the paper during testing. The user questioned whether there was a problem with their reproduction code or process and requested a reproduction tutorial.

This appears to be part of a broader pattern in the LeRobot community. Multiple related issues have been filed about similar reproduction challenges with SmolVLA on LIBERO:

- Another issue (#2354) indicates users are trying to reproduce LIBERO benchmark results of SmolVLA but can't reproduce results on the leaderboard or paper
- Issue #3287 mentions observing a significant gap between evaluation results and the performance reported in the paper, which reports 0.45B model success rates of approximately 90%, 96%, 92%, and 71% (Spatial, Object, Goal, Long), averaging 87.3%

The search results suggest this is a known challenge in the community related to reproducing SmolVLA's reported performance metrics on the LIBERO benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "0f993201-6e01-422a-926f-f95280cfb750",
  "tool_use_result": {
    "query": "github huggingface lerobot issue 1369 SmolVLA LIBERO replicate performance",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XMLGp4gfSXGBhdXiUKUUj1",
        "content": [
          {
            "title": "The performance of SmolVLA on LIBERO cannot be replicated · Issue #1369 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1369"
          },
          {
            "title": "Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2354"
          },
          {
            "title": "[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1316"
          },
          {
            "title": "Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3287"
          },
          {
            "title": "Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2107"
          },
          {
            "title": "GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning",
            "url": "https://github.com/huggingface/lerobot"
          },
          {
            "title": "LIBERO · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/libero"
          },
          {
            "title": "GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.",
            "url": "https://github.com/huggingface/lerobot-libero"
          },
          {
            "title": "smolvla can not reproduce results in libero eval using official checkpoints · Issue #3264 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3264"
          },
          {
            "title": "SmolVLA · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/smolvla"
          }
        ]
      },
      "Based on the web search results, I found information about GitHub issue #1369 in the Hugging Face LeRobot repository:\n\nIssue #1369, opened on June 23, 2025, reports that a user trained SmolVLA from scratch on the LIBERO dataset but couldn't reproduce its results from the paper during testing. The user questioned whether there was a problem with their reproduction code or process and requested a reproduction tutorial.\n\nThis appears to be part of a broader pattern in the LeRobot community. Multiple related issues have been filed about similar reproduction challenges with SmolVLA on LIBERO:\n\n- Another issue (#2354) indicates users are trying to reproduce LIBERO benchmark results of SmolVLA but can't reproduce results on the leaderboard or paper\n- Issue #3287 mentions observing a significant gap between evaluation results and the performance reported in the paper, which reports 0.45B model success rates of approximately 90%, 96%, 92%, and 71% (Spatial, Object, Goal, Long), averaging 87.3%\n\nThe search results suggest this is a known challenge in the community related to reproducing SmolVLA's reported performance metrics on the LIBERO benchmark."
    ],
    "durationSeconds": 6.356309625999998
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T11:52:48.614Z_

<details><summary>↩ Tool result · `toolu_01QMZwdz6o11Xwgt25LXnmPD`</summary>

```text
Web search results for query: "SmolVLA LIBERO 87.3 success rate batch_size 64 training details"

Links: [{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2107"},{"title":"SmolVLA: Compact Vision-Language-Action Model","url":"https://www.emergentmind.com/topics/smolvla"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]","url":"https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"SmolVLA: compact VLA for robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/smolvla-compact-vla-for-robot-policy-b30604ac23c5"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"How can i train and eval SmolVLA in libero? · Issue #2258 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2258"}]

Based on the search results, here's what I found about SmolVLA's 87.3% success rate on LIBERO with batch_size 64 training details:

## Performance Metrics

The 0.45B SmolVLA model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3% on LIBERO.

## Training Configuration

For fine-tuning on simulation benchmarks, SmolVLA trains for 100,000 steps with a batch size of 64.

## Pretraining Details

During pretraining, SmolVLA trains for 200,000 steps with a global batch size of 256 on all community datasets. After a 100-step warmup, it uses a cosine learning rate schedule starting at 1e-4 and decaying to a minimum of 2.5e-6.

## Model Architecture

SmolVLA's main model contains 450 million parameters, with approximately 100 million dedicated to the action expert. The model uses only the first 16 layers of the large language model (LLM) within the VLM.

During fine-tuning, only the action expert module is trained, keeping the VLM frozen.

The search results also reveal that users have encountered challenges when trying to replicate these results, suggesting that exact training configurations and hyperparameters are important for achieving the reported 87.3% success rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "12d19f87-86b5-4f2c-81fa-fb3061b05a7d",
  "tool_use_result": {
    "query": "SmolVLA LIBERO 87.3 success rate batch_size 64 training details",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AkpzVt4t7NUyxPUQEha3Fu",
        "content": [
          {
            "title": "Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3287"
          },
          {
            "title": "Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"
          },
          {
            "title": "SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics",
            "url": "https://smolvla.net/index_en"
          },
          {
            "title": "Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2107"
          },
          {
            "title": "SmolVLA: Compact Vision-Language-Action Model",
            "url": "https://www.emergentmind.com/topics/smolvla"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]",
            "url": "https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "SmolVLA: compact VLA for robot policy | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/smolvla-compact-vla-for-robot-policy-b30604ac23c5"
          },
          {
            "title": "Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"
          },
          {
            "title": "How can i train and eval SmolVLA in libero? · Issue #2258 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2258"
          }
        ]
      },
      "Based on the search results, here's what I found about SmolVLA's 87.3% success rate on LIBERO with batch_size 64 training details:\n\n## Performance Metrics\n\nThe 0.45B SmolVLA model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3% on LIBERO.\n\n## Training Configuration\n\nFor fine-tuning on simulation benchmarks, SmolVLA trains for 100,000 steps with a batch size of 64.\n\n## Pretraining Details\n\nDuring pretraining, SmolVLA trains for 200,000 steps with a global batch size of 256 on all community datasets. After a 100-step warmup, it uses a cosine learning rate schedule starting at 1e-4 and decaying to a minimum of 2.5e-6.\n\n## Model Architecture\n\nSmolVLA's main model contains 450 million parameters, with approximately 100 million dedicated to the action expert. The model uses only the first 16 layers of the large language model (LLM) within the VLM.\n\nDuring fine-tuning, only the action expert module is trained, keeping the VLM frozen.\n\nThe search results also reveal that users have encountered challenges when trying to replicate these results, suggesting that exact training configurations and hyperparameters are important for achieving the reported 87.3% success rate."
    ],
    "durationSeconds": 10.871225091999998
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now let me get the specific details from the GitHub issue #3287 about training configurations, and check the actual model card of HuggingFaceVLA/smolvla_libero and HuggingFaceVLA/smolvla_libero_ckpts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "c1b08a13-82d2-4e2f-a8f0-458bfbfc361e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2FWRyPaXvmeNgJbGEE1qq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2945,
      "cache_read_input_tokens": 27948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2945
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

_source line 23_

让我进一步确认官方 checkpoint 的具体训练配置和是否是 batch_size=64 训练的版本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "b9137da9-5f41-4963-919b-321e3da4f638",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2FWRyPaXvmeNgJbGEE1qq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2945,
      "cache_read_input_tokens": 27948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2945
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETHRcrSHb1Ys7UzCKC3yAo`</summary>

```json
{
  "query": "site:github.com huggingface lerobot issues 3287 training configurations batch size SmolVLA LIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "1e31acb1-5fce-42e3-94c8-6359af1fd1a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2FWRyPaXvmeNgJbGEE1qq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2945,
      "cache_read_input_tokens": 27948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2945
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013VWVLDVZhcHc759MmuMuUr`</summary>

```json
{
  "query": "site:huggingface.co HuggingFaceVLA/smolvla_libero_ckpts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "234314f9-2dcd-4dc2-a537-6657c260cdac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2FWRyPaXvmeNgJbGEE1qq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2945,
      "cache_read_input_tokens": 27948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2945
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

_source line 26 · 2026-05-18T11:52:59.489Z_

<details><summary>↩ Tool result · `toolu_013VWVLDVZhcHc759MmuMuUr`</summary>

```text
Web search results for query: "site:huggingface.co HuggingFaceVLA/smolvla_libero_ckpts"

Links: [{"title":"HuggingFaceVLA/smolvla_libero_ckpts · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"HuggingFaceVLA (Hugging Face Vision Language Action Models Research)","url":"https://huggingface.co/HuggingFaceVLA"},{"title":"LIBERO Leaderboard - a Hugging Face Space by HuggingFaceVLA","url":"https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard"},{"title":"LIBERO - a HuggingFaceVLA Collection","url":"https://huggingface.co/collections/HuggingFaceVLA/libero"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"policy_preprocessor.json · HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/blame/main/policy_preprocessor.json"}]

Based on the search results, here's what I found:

The HuggingFaceVLA/smolvla_libero_ckpts model is deprecated and users should use the updated version at https://huggingface.co/HuggingFaceVLA/smolvla_libero instead.

The updated model page shows that SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. This policy has been trained and pushed to the Hub using LeRobot.

The repository contains 1.22 GB of model weights and configuration files, with recent updates migrating the policy to a PolicyProcessorPipeline system.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "0028fea0-8154-4b5c-ba53-3fb60e9902d4",
  "tool_use_result": {
    "query": "site:huggingface.co HuggingFaceVLA/smolvla_libero_ckpts",
    "results": [
      {
        "tool_use_id": "srvtoolu_013iP9Zy8AsxvcoDTXHkiUv1",
        "content": [
          {
            "title": "HuggingFaceVLA/smolvla_libero_ckpts · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero"
          },
          {
            "title": "HuggingFaceVLA/smol-libero · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero at main",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"
          },
          {
            "title": "HuggingFaceVLA (Hugging Face Vision Language Action Models Research)",
            "url": "https://huggingface.co/HuggingFaceVLA"
          },
          {
            "title": "LIBERO Leaderboard - a Hugging Face Space by HuggingFaceVLA",
            "url": "https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard"
          },
          {
            "title": "LIBERO - a HuggingFaceVLA Collection",
            "url": "https://huggingface.co/collections/HuggingFaceVLA/libero"
          },
          {
            "title": "HuggingFaceVLA/libero · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero"
          },
          {
            "title": "SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data",
            "url": "https://huggingface.co/blog/smolvla"
          },
          {
            "title": "policy_preprocessor.json · HuggingFaceVLA/smolvla_libero at main",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero/blame/main/policy_preprocessor.json"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nThe HuggingFaceVLA/smolvla_libero_ckpts model is deprecated and users should use the updated version at https://huggingface.co/HuggingFaceVLA/smolvla_libero instead.\n\nThe updated model page shows that SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. This policy has been trained and pushed to the Hub using LeRobot.\n\nThe repository contains 1.22 GB of model weights and configuration files, with recent updates migrating the policy to a PolicyProcessorPipeline system."
    ],
    "durationSeconds": 4.1754533540000045
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T11:53:02.425Z_

<details><summary>↩ Tool result · `toolu_01ETHRcrSHb1Ys7UzCKC3yAo`</summary>

```text
Web search results for query: "site:github.com huggingface lerobot issues 3287 training configurations batch size SmolVLA LIBERO"

Links: [{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2107"},{"title":"smolvla training bugs on 3090 · Issue #1234 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1234"},{"title":"Evaluation of Policies on Libero · Issue #2731 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2731"},{"title":"`smolvla_base training`: `Expected all tensors to be on the same device` · Issue #1377 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1377"},{"title":"smolvla issue · Issue #2790 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2790"},{"title":"Using the latest version of training in libero the loss is as high as 0.05 · Issue #1842 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1842"}]

I found GitHub Issue #3287 from the HuggingFace LeRobot repository. Here's what the search revealed:

The issue is titled "Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark" and describes an attempt to reproduce SmolVLA results on the LIBERO benchmark while observing a significant gap between evaluation results and the performance reported in the paper.

According to the paper, the 0.45B model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3%.

The issue asks about specific hyperparameter tweaks used for the LIBERO benchmark.

Additionally, I found relevant training configuration documentation that shows an example training command with batch_size=32 for PEFT training of SmolVLA on LIBERO, along with optimizer learning rate of 1e-3 and scheduler decay learning rate of 1e-4.

The issue was opened on April 5, 2026, and relates to reproducing the baseline SmolVLA model performance on the LIBERO benchmark tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "3e7c2639-bcda-4646-b42b-136cf4ea8b8c",
  "tool_use_result": {
    "query": "site:github.com huggingface lerobot issues 3287 training configurations batch size SmolVLA LIBERO",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GuLaCNuM3SdN1C2bVqSygk",
        "content": [
          {
            "title": "Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3287"
          },
          {
            "title": "lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"
          },
          {
            "title": "Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2354"
          },
          {
            "title": "Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2259"
          },
          {
            "title": "Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2107"
          },
          {
            "title": "smolvla training bugs on 3090 · Issue #1234 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1234"
          },
          {
            "title": "Evaluation of Policies on Libero · Issue #2731 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2731"
          },
          {
            "title": "`smolvla_base training`: `Expected all tensors to be on the same device` · Issue #1377 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1377"
          },
          {
            "title": "smolvla issue · Issue #2790 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2790"
          },
          {
            "title": "Using the latest version of training in libero the loss is as high as 0.05 · Issue #1842 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1842"
          }
        ]
      },
      "I found GitHub Issue #3287 from the HuggingFace LeRobot repository. Here's what the search revealed:\n\nThe issue is titled \"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark\" and describes an attempt to reproduce SmolVLA results on the LIBERO benchmark while observing a significant gap between evaluation results and the performance reported in the paper.\n\nAccording to the paper, the 0.45B model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3%.\n\nThe issue asks about specific hyperparameter tweaks used for the LIBERO benchmark.\n\nAdditionally, I found relevant training configuration documentation that shows an example training command with batch_size=32 for PEFT training of SmolVLA on LIBERO, along with optimizer learning rate of 1e-3 and scheduler decay learning rate of 1e-4.\n\nThe issue was opened on April 5, 2026, and relates to reproducing the baseline SmolVLA model performance on the LIBERO benchmark tasks."
    ],
    "durationSeconds": 7.283083998000002
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the actual model card and config to see if the checkpoint was trained with batch_size=64. Let me also look at the SmolVLA paper or documentation for the exact training config.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "579bc0de-f5a4-491b-a418-21eccb9234cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X26w4QZuk68oNUCnSGtwCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 30893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1290
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

_source line 29_

让我直接获取官方 checkpoint 的训练配置文件来确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "2c5d70f6-50a4-459e-8009-c799092d06c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X26w4QZuk68oNUCnSGtwCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 30893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1290
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H1CPHdV8vBHvFmy8SZEAvz`</summary>

```json
{
  "query": "huggingface.co HuggingFaceVLA smolvla_libero train_config.json batch_size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "4d1e497b-9e54-4404-962a-1cfb9f5d4450",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X26w4QZuk68oNUCnSGtwCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 30893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1290
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UM1D6sJqM1q3mgCs9bWxL4`</summary>

```json
{
  "query": "SmolVLA paper arxiv 2506.01844 LIBERO training batch size 64 100000 steps configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "4f455a30-71fc-4168-9489-ffd4d8a99613",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X26w4QZuk68oNUCnSGtwCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 30893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1290
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

_source line 32 · 2026-05-18T11:53:12.474Z_

<details><summary>↩ Tool result · `toolu_01H1CPHdV8vBHvFmy8SZEAvz`</summary>

```text
Web search results for query: "huggingface.co HuggingFaceVLA smolvla_libero train_config.json batch_size"

Links: [{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"train_config.json · Alkatt/smolvla-libero-100000 at main","url":"https://huggingface.co/Alkatt/smolvla-libero-100000/blob/main/train_config.json"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"HuggingFaceTB/SmolVLM-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct"}]

I found search results related to your query about HuggingFaceVLA's SmolVLA model and LIBERO training. Here are the relevant findings:

The search results show that SmolVLA is a compact, efficient vision-language-action model that has been trained and pushed to the Hub using LeRobot. The HuggingFaceVLA/smolvla_libero repository contains the trained policy.

Regarding batch size configurations, the search results show training examples with different batch sizes:

- A training command example uses `--batch_size=4` for LIBERO training
- Another fine-tuning example uses `--batch_size=32` for custom tasks
- The Physical Intelligence LIBERO base model was fine-tuned with a batch size of 256 on 8 H100 GPUs

While I found reference to a `train_config.json` file in the Alkatt/smolvla-libero-100000 repository (result index 2), the search results don't display the actual contents of the train_config.json file with the specific batch_size configuration. To view the exact batch_size value in that file, you would need to access it directly on the Hugging Face Hub at the repository page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "9f0fed33-a228-47ce-9762-b118afdde15a",
  "tool_use_result": {
    "query": "huggingface.co HuggingFaceVLA smolvla_libero train_config.json batch_size",
    "results": [
      {
        "tool_use_id": "srvtoolu_017pywLv8xTRsgC5pCEYfwpm",
        "content": [
          {
            "title": "SmolVLA · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/smolvla"
          },
          {
            "title": "train_config.json · Alkatt/smolvla-libero-100000 at main",
            "url": "https://huggingface.co/Alkatt/smolvla-libero-100000/blob/main/train_config.json"
          },
          {
            "title": "LIBERO · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/libero"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero at main",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"
          },
          {
            "title": "HuggingFaceVLA/smolvla_libero · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero"
          },
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/main/en/libero"
          },
          {
            "title": "lerobot/smolvla_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/smolvla_base"
          },
          {
            "title": "HuggingFaceVLA/smol-libero · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"
          },
          {
            "title": "Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2259"
          },
          {
            "title": "HuggingFaceTB/SmolVLM-Instruct · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct"
          }
        ]
      },
      "I found search results related to your query about HuggingFaceVLA's SmolVLA model and LIBERO training. Here are the relevant findings:\n\nThe search results show that SmolVLA is a compact, efficient vision-language-action model that has been trained and pushed to the Hub using LeRobot. The HuggingFaceVLA/smolvla_libero repository contains the trained policy.\n\nRegarding batch size configurations, the search results show training examples with different batch sizes:\n\n- A training command example uses `--batch_size=4` for LIBERO training\n- Another fine-tuning example uses `--batch_size=32` for custom tasks\n- The Physical Intelligence LIBERO base model was fine-tuned with a batch size of 256 on 8 H100 GPUs\n\nWhile I found reference to a `train_config.json` file in the Alkatt/smolvla-libero-100000 repository (result index 2), the search results don't display the actual contents of the train_config.json file with the specific batch_size configuration. To view the exact batch_size value in that file, you would need to access it directly on the Hugging Face Hub at the repository page."
    ],
    "durationSeconds": 5.733202905999999
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-18T11:53:13.793Z_

<details><summary>↩ Tool result · `toolu_01UM1D6sJqM1q3mgCs9bWxL4`</summary>

```text
Web search results for query: "SmolVLA paper arxiv 2506.01844 LIBERO training batch size 64 100000 steps configuration"

Links: [{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.researchgate.net/publication/392370918_SmolVLA_A_Vision-Language-Action_Model_for_Affordable_and_Efficient_Robotics"},{"title":"Alkatt/smolvla-libero-100000 · Hugging Face","url":"https://huggingface.co/Alkatt/smolvla-libero-100000"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"}]

I've found search results related to the SmolVLA paper (arxiv 2506.01844). The search results include information about the paper and its evaluation on LIBERO benchmarks. However, the specific training configuration details you mentioned (batch size 64 and 100000 steps) are not prominently featured in these initial results.

From the search results, I can see:

1. SmolVLA is evaluated on the LIBERO benchmark with a multi-task training setup across four categories (Spatial, Object, Goal, and Long) with 10 tasks per category (40 total), using a dataset of 1,693 episodes.

2. The Hugging Face model card shows an example training command with `--steps=100000 --batch_size=4`, though this appears to be an example with batch size 4, not 64.

3. Another related paper references Table 5 which contains "Training hyperparameters for LIBERO with SmolVLA", suggesting such configuration details are documented in training tables within the papers.

The specific batch size 64 with 100000 steps configuration you're asking about may be contained in the detailed training hyperparameter tables within the full paper PDF, which the search results reference but don't fully display the specific values.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "e989e989-59a6-46ad-98c0-eca0c2e721af",
  "tool_use_result": {
    "query": "SmolVLA paper arxiv 2506.01844 LIBERO training batch size 64 100000 steps configuration",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JYToaLFTKxkLZ2Znw92mPt",
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
            "title": "arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model",
            "url": "https://arxiv.org/pdf/2506.01844"
          },
          {
            "title": "Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://huggingface.co/papers/2506.01844"
          },
          {
            "title": "lerobot/smolvla_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/smolvla_base"
          },
          {
            "title": "Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3287"
          },
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "http://export.arxiv.org/abs/2506.01844"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://www.researchgate.net/publication/392370918_SmolVLA_A_Vision-Language-Action_Model_for_Affordable_and_Efficient_Robotics"
          },
          {
            "title": "Alkatt/smolvla-libero-100000 · Hugging Face",
            "url": "https://huggingface.co/Alkatt/smolvla-libero-100000"
          },
          {
            "title": "Leave No Observation Behind: Real-time Correction for VLA Action Chunks",
            "url": "https://arxiv.org/html/2509.23224v1"
          }
        ]
      },
      "I've found search results related to the SmolVLA paper (arxiv 2506.01844). The search results include information about the paper and its evaluation on LIBERO benchmarks. However, the specific training configuration details you mentioned (batch size 64 and 100000 steps) are not prominently featured in these initial results.\n\nFrom the search results, I can see:\n\n1. SmolVLA is evaluated on the LIBERO benchmark with a multi-task training setup across four categories (Spatial, Object, Goal, and Long) with 10 tasks per category (40 total), using a dataset of 1,693 episodes.\n\n2. The Hugging Face model card shows an example training command with `--steps=100000 --batch_size=4`, though this appears to be an example with batch size 4, not 64.\n\n3. Another related paper references Table 5 which contains \"Training hyperparameters for LIBERO with SmolVLA\", suggesting such configuration details are documented in training tables within the papers.\n\nThe specific batch size 64 with 100000 steps configuration you're asking about may be contained in the detailed training hyperparameter tables within the full paper PDF, which the search results reference but don't fully display the specific values."
    ],
    "durationSeconds": 6.240157403000005
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Let me try to fetch the actual SmolVLA paper to see the training hyperparameters, and also check the LeRobot docs for the LIBERO fine-tuning config.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "a031c8a9-404b-42da-b391-6d3af55dd320",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgXDKhDfGfwZx2HD3JNStC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2724,
      "cache_read_input_tokens": 32183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2724
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

让我直接获取论文中的训练超参数和 LeRobot 官方文档的配置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "b61fa29e-def5-49c6-9bdd-4936dd31121a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgXDKhDfGfwZx2HD3JNStC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2724,
      "cache_read_input_tokens": 32183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2724
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G6tLNXTBKbCmBB6WQRQfv2`</summary>

```json
{
  "query": "SmolVLA arxiv \"batch size\" \"64\" LIBERO \"100,000\" OR \"100000\" OR \"100k\" steps fine-tuning hyperparameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "23d467bf-b742-41e2-b157-91b5919b774a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgXDKhDfGfwZx2HD3JNStC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2724,
      "cache_read_input_tokens": 32183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2724
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FRRYZvpTtptqDdxwuxK5M7`</summary>

```json
{
  "query": "lerobot docs smolvla LIBERO fine-tuning command batch_size 64 steps 100000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "f11112db-1b9c-4906-a120-113aff28e8f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgXDKhDfGfwZx2HD3JNStC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2724,
      "cache_read_input_tokens": 32183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2724
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

_source line 38 · 2026-05-18T11:53:25.072Z_

<details><summary>↩ Tool result · `toolu_01G6tLNXTBKbCmBB6WQRQfv2`</summary>

```text
Web search results for query: "SmolVLA arxiv "batch size" "64" LIBERO "100,000" OR "100000" OR "100k" steps fine-tuning hyperparameters"

Links: [{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]","url":"https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"SmolVLA - ArXivIQ","url":"https://arxiviq.substack.com/p/smolvla"}]

Perfect! I found the exact information you were looking for. Here are the key findings from the SmolVLA arXiv paper:

For fine-tuning on simulation benchmarks, SmolVLA trains for 100,000 steps with a batch size of 64, while for real-world tasks, it fine-tunes for 200,000 steps.

SmolVLA is evaluated in the LIBERO benchmark, which assesses diverse visuomotor skills across four categories–Spatial, Object, Goal, and Long–with 10 tasks per category (40 total).

Additional context on the model architecture: The main SmolVLA model contains 450 million parameters, with approximately 100 million dedicated to the action expert. The model trains only the action expert module, keeping the VLM frozen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "e4c669c4-3069-47be-85e2-e56c8f2d0416",
  "tool_use_result": {
    "query": "SmolVLA arxiv \"batch size\" \"64\" LIBERO \"100,000\" OR \"100000\" OR \"100k\" steps fine-tuning hyperparameters",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KTUJ5BXVWdB8Dma5zam1Gk",
        "content": [
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"
          },
          {
            "title": "SmolVLA · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/en/smolvla"
          },
          {
            "title": "Leave No Observation Behind: Real-time Correction for VLA Action Chunks",
            "url": "https://arxiv.org/html/2509.23224v1"
          },
          {
            "title": "Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3287"
          },
          {
            "title": "VLA-0-Smol",
            "url": "https://robot-learning-collective.github.io/vla-0-smol"
          },
          {
            "title": "SmolVLA fine-tuning | EmbodiFlow",
            "url": "https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]",
            "url": "https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"
          },
          {
            "title": "SmolVLA: Efficient Vision Language Action Model - LeRobot",
            "url": "https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"
          },
          {
            "title": "SmolVLA - ArXivIQ",
            "url": "https://arxiviq.substack.com/p/smolvla"
          }
        ]
      },
      "Perfect! I found the exact information you were looking for. Here are the key findings from the SmolVLA arXiv paper:\n\nFor fine-tuning on simulation benchmarks, SmolVLA trains for 100,000 steps with a batch size of 64, while for real-world tasks, it fine-tunes for 200,000 steps.\n\nSmolVLA is evaluated in the LIBERO benchmark, which assesses diverse visuomotor skills across four categories–Spatial, Object, Goal, and Long–with 10 tasks per category (40 total).\n\nAdditional context on the model architecture: The main SmolVLA model contains 450 million parameters, with approximately 100 million dedicated to the action expert. The model trains only the action expert module, keeping the VLM frozen."
    ],
    "durationSeconds": 5.148694449000002
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T11:53:27.584Z_

<details><summary>↩ Tool result · `toolu_01FRRYZvpTtptqDdxwuxK5M7`</summary>

```text
Web search results for query: "lerobot docs smolvla LIBERO fine-tuning command batch_size 64 steps 100000"

Links: [{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"fine tune SmolVLA in libero with tensor shape mismatch · Issue #2418 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2418"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"}]

Based on the search results, I found relevant documentation about SmolVLA fine-tuning with LeRobot on LIBERO. Here are the key findings:

## SmolVLA Fine-tuning with LIBERO

A basic example fine-tuning command uses `lerobot-train` with parameters like `--policy.path=lerobot/smolvla_base`, `--batch_size=64`, and `--steps=20000`.

For LIBERO-specific fine-tuning, there's a training command that uses `--policy.type=smolvla`, `--dataset.repo_id=HuggingFaceVLA/libero`, `--env.type=libero`, `--env.task=libero_10`, `--steps=100000`, and `--batch_size=4`.

If you want to use the parameters you specified (batch_size=64, steps=100000), you could structure a command like this based on the official documentation:

For PEFT-based fine-tuning with SmolVLA on LIBERO, you can use a command with `--policy.path=lerobot/smolvla_base`, `--dataset.repo_id=HuggingFaceVLA/libero`, `--env.type=libero`, `--env.task=libero_spatial`, `--steps=100000`, and `--batch_size=32`.

The exact batch_size of 64 with 100000 steps combination you mentioned appears to be a custom configuration beyond the standard examples in the documentation. The documentation recommends that you can start with a small batch size and increase it incrementally if the GPU allows it, as long as loading times remain short.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "cfc54cc3-9726-4a3a-bde6-b48fd5c141b8",
  "tool_use_result": {
    "query": "lerobot docs smolvla LIBERO fine-tuning command batch_size 64 steps 100000",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U6aVt3unsW55yx1ShYddh9",
        "content": [
          {
            "title": "SmolVLA · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/smolvla"
          },
          {
            "title": "lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"
          },
          {
            "title": "Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3287"
          },
          {
            "title": "fine tune SmolVLA in libero with tensor shape mismatch · Issue #2418 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2418"
          },
          {
            "title": "Train SmolVLA",
            "url": "https://docs.phospho.ai/learn/train-smolvla"
          },
          {
            "title": "SmolVLA fine-tuning | EmbodiFlow",
            "url": "https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"
          },
          {
            "title": "Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"
          },
          {
            "title": "LIBERO · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/libero"
          },
          {
            "title": "lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"
          },
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/main/en/libero"
          }
        ]
      },
      "Based on the search results, I found relevant documentation about SmolVLA fine-tuning with LeRobot on LIBERO. Here are the key findings:\n\n## SmolVLA Fine-tuning with LIBERO\n\nA basic example fine-tuning command uses `lerobot-train` with parameters like `--policy.path=lerobot/smolvla_base`, `--batch_size=64`, and `--steps=20000`.\n\nFor LIBERO-specific fine-tuning, there's a training command that uses `--policy.type=smolvla`, `--dataset.repo_id=HuggingFaceVLA/libero`, `--env.type=libero`, `--env.task=libero_10`, `--steps=100000`, and `--batch_size=4`.\n\nIf you want to use the parameters you specified (batch_size=64, steps=100000), you could structure a command like this based on the official documentation:\n\nFor PEFT-based fine-tuning with SmolVLA on LIBERO, you can use a command with `--policy.path=lerobot/smolvla_base`, `--dataset.repo_id=HuggingFaceVLA/libero`, `--env.type=libero`, `--env.task=libero_spatial`, `--steps=100000`, and `--batch_size=32`.\n\nThe exact batch_size of 64 with 100000 steps combination you mentioned appears to be a custom configuration beyond the standard examples in the documentation. The documentation recommends that you can start with a small batch size and increase it incrementally if the GPU allows it, as long as loading times remain short."
    ],
    "durationSeconds": 7.252784227000011
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Interesting. So the LeRobot docs show the default training command for LIBERO uses `--batch_size=4` and `--steps=100000`. But the SmolVLA paper says they trained with batch_size=64 for 100K steps. The official checkpoint `HuggingFaceVLA/smolvla_libero` is available on HuggingFace.

The key question is: is `HuggingFaceVLA/smolvla_libero` the batch_size=64 trained version that achieves 87.3%? Based on the evidence:

1. The paper reports 87.3% average SR with batch_size=64, 100K steps


2. The official HF checkpoint is from the HuggingFaceVLA org, which strongly suggests it's the batch_size=64 version that achieves that performance
3. Multiple reproduction attempts have failed to match the 87.3% result, and the LeRobot example uses batch_size=4 (which aligns with our 44.8% result)

So the official checkpoint likely is the properly trained version, but I should verify what the model card actually specifies about its training configuration.

I've got the key details now—there's also a deprecated checkpoint repo I should mention. The official model is `HuggingFaceVLA/smolvla_libero` from the HuggingFaceVLA organization, trained with batch_size=64 for 100K steps to achieve around 87.3% average success rate across the different task categories. There's a deprecated variant called `HuggingFaceVLA/smolvla_libero_ckpts` that's no longer in use, and several GitHub issues document reproduction challenges when trying to match those reported results.

The core issue is that while the official checkpoint exists and is downloadable, multiple users report they can't reproduce the 87.3% performance—the LeRobot documentation defaults to batch_size=4 (which is what the user tried and got 44.8%), and issue #3264 explicitly states the checkpoint fails to reproduce the reported LIBERO evaluation scores. So the checkpoint is real and available, but there's a known gap between the paper's results and what people actually get when using it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "6b13d3d1-4b97-4914-880a-c1cfe62f962b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WryipQBv2X4R6WwZPh6zFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 34907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1987
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

### Assistant

_source line 41_

## 结果

### 官方 LIBERO finetuned checkpoint: **存在**

| 项目 | 值 |
|---|---|
| **Model ID** | `HuggingFaceVLA/smolvla_libero` |
| **Size** | ~1.22 GB |
| **Base model** | `lerobot/smolvla_base` |
| **论文报告训练配置** | batch_size=64, 100K steps, 只训练 action expert，VLM frozen |
| **论文报告 SR** | Spatial 90%, Object 96%, Goal 92%, Long 71%, **平均 87.3%** |
| **旧版 (deprecated)** | `HuggingFaceVLA/smolvla_libero_ckpts` → 已指向上面的新版 |

### 重要警告：复现问题

社区有多个 issue 报告无法复现 87.3%：
- [#1369](https://github.com/huggingface/lerobot/issues/1369) — 从头训练无法复现
- [#2354](https://github.com/huggingface/lerobot/issues/2354) — 无法复现 benchmark 结果
- [#3264](https://github.com/huggingface/lerobot/issues/3264) — **用官方 checkpoint eval 也无法复现**
- [#3287](https://github.com/huggingface/lerobot/issues/3287) — 询问精确训练配置（batch size, LR, commit hash）

这意味着：
1. 官方 checkpoint 存在且可下载，但用它直接 eval 可能因 lerobot 版本/eval 协议差异拿不到 87.3%
2. 论文的 87.3% 可能依赖特定 lerobot commit 和 eval 设置

### 对我们项目的影响

可以直接下载 `HuggingFaceVLA/smolvla_libero` 做 pruning 实验。即使 eval SR 不到 87.3%，只要比我们 batch_size=4 的 44.8% baseline 显著更高，就足以验证 cliff-edge 在强 baseline 上的存在。关键是要用**同一 eval 流程**对比 pruned vs unpruned，保证内部一致性。

Sources:
- [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)
- [SmolVLA paper (arXiv:2506.01844)](https://arxiv.org/abs/2506.01844)
- [Issue #3287 - Training config inquiry](https://github.com/huggingface/lerobot/issues/3287)
- [Issue #3264 - Cannot reproduce with official checkpoints](https://github.com/huggingface/lerobot/issues/3264)
- [HuggingFaceVLA/smolvla_libero_ckpts (deprecated)](https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts)
- [SmolVLA docs](https://huggingface.co/docs/lerobot/smolvla)
- [LIBERO Leaderboard](https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "uuid": "02d95d3a-87e3-4201-8358-0af086031d1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WryipQBv2X4R6WwZPh6zFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 34907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1987
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

### Task result

_source line 42_

## 结果

### 官方 LIBERO finetuned checkpoint: **存在**

| 项目 | 值 |
|---|---|
| **Model ID** | `HuggingFaceVLA/smolvla_libero` |
| **Size** | ~1.22 GB |
| **Base model** | `lerobot/smolvla_base` |
| **论文报告训练配置** | batch_size=64, 100K steps, 只训练 action expert，VLM frozen |
| **论文报告 SR** | Spatial 90%, Object 96%, Goal 92%, Long 71%, **平均 87.3%** |
| **旧版 (deprecated)** | `HuggingFaceVLA/smolvla_libero_ckpts` → 已指向上面的新版 |

### 重要警告：复现问题

社区有多个 issue 报告无法复现 87.3%：
- [#1369](https://github.com/huggingface/lerobot/issues/1369) — 从头训练无法复现
- [#2354](https://github.com/huggingface/lerobot/issues/2354) — 无法复现 benchmark 结果
- [#3264](https://github.com/huggingface/lerobot/issues/3264) — **用官方 checkpoint eval 也无法复现**
- [#3287](https://github.com/huggingface/lerobot/issues/3287) — 询问精确训练配置（batch size, LR, commit hash）

这意味着：
1. 官方 checkpoint 存在且可下载，但用它直接 eval 可能因 lerobot 版本/eval 协议差异拿不到 87.3%
2. 论文的 87.3% 可能依赖特定 lerobot commit 和 eval 设置

### 对我们项目的影响

可以直接下载 `HuggingFaceVLA/smolvla_libero` 做 pruning 实验。即使 eval SR 不到 87.3%，只要比我们 batch_size=4 的 44.8% baseline 显著更高，就足以验证 cliff-edge 在强 baseline 上的存在。关键是要用**同一 eval 流程**对比 pruned vs unpruned，保证内部一致性。

Sources:
- [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)
- [SmolVLA paper (arXiv:2506.01844)](https://arxiv.org/abs/2506.01844)
- [Issue #3287 - Training config inquiry](https://github.com/huggingface/lerobot/issues/3287)
- [Issue #3264 - Cannot reproduce with official checkpoints](https://github.com/huggingface/lerobot/issues/3264)
- [HuggingFaceVLA/smolvla_libero_ckpts (deprecated)](https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts)
- [SmolVLA docs](https://huggingface.co/docs/lerobot/smolvla)
- [LIBERO Leaderboard](https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 100224,
  "duration_api_ms": 139089,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "5fdc16fb-2b96-43b4-97d9-42ef659771bd",
  "total_cost_usd": 0.64385875,
  "usage": {
    "input_tokens": 781,
    "cache_creation_input_tokens": 25053,
    "cache_read_input_tokens": 187209,
    "output_tokens": 2934,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25053,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1558,
        "cache_read_input_tokens": 34907,
        "cache_creation_input_tokens": 1987,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1987
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 172298,
      "outputTokens": 4824,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 12,
      "costUSD": 0.31641800000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 781,
      "outputTokens": 2934,
      "cacheReadInputTokens": 187209,
      "cacheCreationInputTokens": 25053,
      "webSearchRequests": 0,
      "costUSD": 0.32744075,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1cfe528e-f316-4deb-9599-634da8577a9a"
}
```

</details>

---
