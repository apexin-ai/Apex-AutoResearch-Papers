# check westb available models

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_check_westb_available_models_20260518T094750.log`
- **Structured JSON:** [`dcbeddc41864e744015d.json`](../../sessions/dc/dcbeddc41864e744015d.json)

## Before a recorded user message

11 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c",
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
  "uuid": "5065f247-4834-4a56-a3bb-7e6ac89fb2b1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1779112800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "40e943ea-3ebb-49f1-b9c4-3e0468704f9e",
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to SSH to westb-23072 and check for available model checkpoints. Let me execute the command they specified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c",
  "uuid": "2bfe4e1b-b7bb-4de1-b1b1-5744fb09ec40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRXKGFvyHJffziKVBfXTtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12864,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12864
      },
      "output_tokens": 35,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018pCegnxxDXDMdTYN1CLdth`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
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
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c",
  "uuid": "195d2da2-8c7e-46dd-bec0-19309a817b3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRXKGFvyHJffziKVBfXTtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12864,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12864
      },
      "output_tokens": 35,
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

_source line 6 · 2026-05-18T09:48:03.548Z_

<details><summary>↩ Tool result · `toolu_018pCegnxxDXDMdTYN1CLdth`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c",
  "uuid": "ae00cc21-c444-40cf-bf3f-be371074c710",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Sq593t9GBUU4NugBeF3eHD`</summary>

```json
{
  "server": "westb-23072",
  "command": "echo \"=== /root/autodl-tmp/recovery_aware_struct_prune/ ===\"\nls -d /root/autodl-tmp/recovery_aware_struct_prune/*/ 2>/dev/null\n\necho \"=== checkpoints 目录 ===\"\nls -d /root/autodl-tmp/recovery_aware_struct_prune/checkpoints/*/ 2>/dev/null\n\necho \"=== 所有含 grpo 或 sft 的目录 ===\"\nfind /root/autodl-tmp/recovery_aware_struct_prune/ -maxdepth 2 -type d \\( -name \"*grpo*\" -o -name \"*sft*\" -o -name \"*standard*\" -o -name \"*rasp*\" \\) 2>/dev/null\n\necho \"=== Dense model ===\"\nls -d /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B 2>/dev/null && echo \"EXISTS\" || echo \"NOT FOUND\"",
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
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c",
  "uuid": "d6bdf97b-84a7-4bf7-86b1-9d3f3de99efc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019SkSGs2GVyNDmpZykWjepQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 24705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
      },
      "output_tokens": 70,
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

_source line 8 · 2026-05-18T09:48:11.547Z_

<details><summary>↩ Tool result · `toolu_01Sq593t9GBUU4NugBeF3eHD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== /root/autodl-tmp/recovery_aware_struct_prune/ ===\\n/root/autodl-tmp/recovery_aware_struct_prune/artifacts/\\n/root/autodl-tmp/recovery_aware_struct_prune/eval_results/\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/logs/\\n/root/autodl-tmp/recovery_aware_struct_prune/models/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_gradient_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_magnitude_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30/\\n/root/autodl-tmp/recovery_aware_struct_prune/results/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/\\n=== checkpoints 目录 ===\\n=== 所有含 grpo 或 sft 的目录 ===\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\\n=== Dense model ===\\n/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\\nEXISTS\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.96}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c",
  "uuid": "c0f970ed-e88e-4177-8268-978833d95297",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== /root/autodl-tmp/recovery_aware_struct_prune/ ===\\\\n/root/autodl-tmp/recovery_aware_struct_prune/artifacts/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/eval_results/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/logs/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/models/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_gradient_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_magnitude_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/results/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/\\\\n=== checkpoints 目录 ===\\\\n=== 所有含 grpo 或 sft 的目录 ===\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30\\\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20\\\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\\\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20\\\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\\\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\\\\n=== Dense model ===\\\\n/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\\\\nEXISTS\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.96}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== /root/autodl-tmp/recovery_aware_struct_prune/ ===\\n/root/autodl-tmp/recovery_aware_struct_prune/artifacts/\\n/root/autodl-tmp/recovery_aware_struct_prune/eval_results/\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/logs/\\n/root/autodl-tmp/recovery_aware_struct_prune/models/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_gradient_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_magnitude_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30/\\n/root/autodl-tmp/recovery_aware_struct_prune/results/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/\\n=== checkpoints 目录 ===\\n=== 所有含 grpo 或 sft 的目录 ===\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\\n=== Dense model ===\\n/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\\nEXISTS\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.96}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me summarize what's found on westb-23072. The user is looking for specific checkpoints that were on westd-11672. Let me compare what they need vs what's available.

Needed:
- grpo_standard_20 or grpo_standard_20_fair — NOT FOUND
- grpo_rasp_20 or grpo_stage2_rasp_20_v9 — NOT FOUND
- sft_standard_20 — NOT FOUND
- sft_rasp_20 — NOT FOUND


- grpo_unpruned_v2 — NOT FOUND

What's on westb instead: pruned variants across different methods (CKA, gradient, magnitude, random, RASP), some SFT models with similar pruning approaches, a few GRPO models, but nothing matching the standard or unpruned versions they're after.

The models they actually need—20% sparsity GRPO and SFT with standard/RASP pruning plus the unpruned GRPO variant—aren't available on westb. The server has different sparsity levels (25%, 30%) and alternative pruning strategies instead. I'm also seeing a reference to a DeepSeek model path that might be relevant to check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c",
  "uuid": "204d080e-c981-4f19-9c65-c967526fb1e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ZNWgkcXsL8DNFDB8xunUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 25095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1496
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

_source line 10_

westb-23072 上的模型清单：

**Dense model**
- `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` ✅

**Pruned models (未训练)**
| 路径 | 说明 |
|------|------|
| `pruned_cka_only_20/` | CKA-only 剪枝 20% |
| `pruned_gradient_20/` | Gradient 剪枝 20% |
| `pruned_magnitude_20/` | Magnitude 剪枝 20% |
| `pruned_random_20/` | Random 剪枝 20% |
| `pruned_rasp_25/` | RASP 剪枝 25% |
| `pruned_rasp_30/` | RASP 剪枝 30% |
| `pruned_rasp_rlvr_20/` | RASP-RLVR 剪枝 20% |
| `pruned_standard_25/` | Standard 剪枝 25% |
| `pruned_standard_30/` | Standard 剪枝 30% |

**SFT checkpoints**
| 路径 | 说明 |
|------|------|
| `sft_cka_only_20/` | CKA-only 20% SFT |
| `sft_gradient_20/` | Gradient 20% SFT |
| `sft_random_20/` | Random 20% SFT |
| `sft_rasp_25/` | RASP 25% SFT |
| `sft_rasp_rlvr_20/` | RASP-RLVR 20% SFT |
| `sft_standard_25/` | Standard 25% SFT |

**GRPO checkpoints**
| 路径 | 说明 |
|------|------|
| `grpo_cka_only_20/` | CKA-only 20% GRPO |
| `grpo_random_20/` | Random 20% GRPO |
| `grpo_rasp_25/` | RASP 25% GRPO |

所有路径前缀均为 `/root/autodl-tmp/recovery_aware_struct_prune/`。

---

**你要找的 5 个模型全部不在 westb 上：**

| 需要的模型 | westb 状态 |
|-----------|-----------|
| `grpo_standard_20` / `grpo_standard_20_fair` | ❌ 没有（只有 25% 的 `grpo` 没有 standard 20%） |
| `grpo_rasp_20` / `grpo_stage2_rasp_20_v9` | ❌ 没有（只有 `grpo_rasp_25`） |
| `sft_standard_20` | ❌ 没有（只有 `sft_standard_25`） |
| `sft_rasp_20` | ❌ 没有（只有 `sft_rasp_25`） |
| `grpo_unpruned_v2` | ❌ 没有 |

westb 上有的是另一批实验（25%/30% sparsity 以及 cka_only/gradient/random/rasp_rlvr 等 ablation 变体），核心的 20% standard/rasp GRPO/SFT checkpoint 都只在 westd-11672 上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c",
  "uuid": "1df9084c-9be9-4bcc-8146-09c6ae0a6c0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ZNWgkcXsL8DNFDB8xunUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 25095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1496
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

_source line 11_

westb-23072 上的模型清单：

**Dense model**
- `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` ✅

**Pruned models (未训练)**
| 路径 | 说明 |
|------|------|
| `pruned_cka_only_20/` | CKA-only 剪枝 20% |
| `pruned_gradient_20/` | Gradient 剪枝 20% |
| `pruned_magnitude_20/` | Magnitude 剪枝 20% |
| `pruned_random_20/` | Random 剪枝 20% |
| `pruned_rasp_25/` | RASP 剪枝 25% |
| `pruned_rasp_30/` | RASP 剪枝 30% |
| `pruned_rasp_rlvr_20/` | RASP-RLVR 剪枝 20% |
| `pruned_standard_25/` | Standard 剪枝 25% |
| `pruned_standard_30/` | Standard 剪枝 30% |

**SFT checkpoints**
| 路径 | 说明 |
|------|------|
| `sft_cka_only_20/` | CKA-only 20% SFT |
| `sft_gradient_20/` | Gradient 20% SFT |
| `sft_random_20/` | Random 20% SFT |
| `sft_rasp_25/` | RASP 25% SFT |
| `sft_rasp_rlvr_20/` | RASP-RLVR 20% SFT |
| `sft_standard_25/` | Standard 25% SFT |

**GRPO checkpoints**
| 路径 | 说明 |
|------|------|
| `grpo_cka_only_20/` | CKA-only 20% GRPO |
| `grpo_random_20/` | Random 20% GRPO |
| `grpo_rasp_25/` | RASP 25% GRPO |

所有路径前缀均为 `/root/autodl-tmp/recovery_aware_struct_prune/`。

---

**你要找的 5 个模型全部不在 westb 上：**

| 需要的模型 | westb 状态 |
|-----------|-----------|
| `grpo_standard_20` / `grpo_standard_20_fair` | ❌ 没有（只有 25% 的 `grpo` 没有 standard 20%） |
| `grpo_rasp_20` / `grpo_stage2_rasp_20_v9` | ❌ 没有（只有 `grpo_rasp_25`） |
| `sft_standard_20` | ❌ 没有（只有 `sft_standard_25`） |
| `sft_rasp_20` | ❌ 没有（只有 `sft_rasp_25`） |
| `grpo_unpruned_v2` | ❌ 没有 |

westb 上有的是另一批实验（25%/30% sparsity 以及 cka_only/gradient/random/rasp_rlvr 等 ablation 变体），核心的 20% standard/rasp GRPO/SFT checkpoint 都只在 westd-11672 上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 30496,
  "duration_api_ms": 28601,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "0c0c787a-5d8a-4902-96d8-f2027f2c225c",
  "total_cost_usd": 0.170665,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 14750,
    "cache_read_input_tokens": 61641,
    "output_tokens": 1843,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 14750,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1364,
        "cache_read_input_tokens": 25095,
        "cache_creation_input_tokens": 1496,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1496
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1452,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001547,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 1843,
      "cacheReadInputTokens": 61641,
      "cacheCreationInputTokens": 14750,
      "webSearchRequests": 0,
      "costUSD": 0.169118,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f7c55c62-3c93-4ea9-a0d6-4af7da41af89"
}
```

</details>

---
