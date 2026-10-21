# knowledge v9d success memory

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_knowledge_v9d_success_memory_20260520T095446.log`
- **Structured JSON:** [`88984648b66350d088cb.json`](../../sessions/88/88984648b66350d088cb.json)

## Before a recorded user message

16 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
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
  "uuid": "08ffefe4-a071-41cc-a4e5-4b2409c47e3f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
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
    "resetsAt": 1779286200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a288d74e-248b-4dea-a01c-6bd8b1d977d3",
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37"
}
```

---

### Assistant

_source line 4_

我先读取当前 memory.md 内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "99910cc2-c63f-4c20-b109-512829a026b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUeskTJxHEWxWpJyrqGJ3B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12565,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12565
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EpUVLorWjS6AXRj2w7y1QN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "3c151736-c63c-4a1a-8871-b94bb319b57f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUeskTJxHEWxWpJyrqGJ3B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12565,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12565
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

_source line 6 · 2026-05-20T09:54:58.458Z_

<details><summary>↩ Tool result · `toolu_01EpUVLorWjS6AXRj2w7y1QN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "c9896454-b7e4-4592-a1ed-e897a285f8a3",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CkA8VDkBNfYDtZFSLpv1b1`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "aaddaf0a-b64f-4344-989a-4ade135dcdaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgcxanRS6obKp98YENReUM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 24406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
      },
      "output_tokens": 69,
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

_source line 8 · 2026-05-20T09:55:01.310Z_

<details><summary>↩ Tool result · `toolu_01CkA8VDkBNfYDtZFSLpv1b1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\", \"content\": \"# Project Memory — cost-verify-agent-rl\\n\\n## 经验教训\\n\\n### max_prompt_length 必须严格小于 max_model_len (2026-05-19)\\nv9c 在 step 3/30 崩溃：`max_prompt_length: 16384 == max_model_len: 16384`，prompt 填满后 vLLM 报 \\\"prompt + requested output tokens > max_model_len\\\"。修复：`max_prompt_length = max_model_len - response_length`（15360 = 16384 - 1024）。写 config 时永远预留 generation headroom。\\n\\n### save_freq 不应设为 999 (2026-05-19)\\nv9c 崩溃后无 checkpoint 可恢复（save_freq: 999 = 实际不保存）。30 步训练建议 save_freq: 5~10，代价是少量磁盘但能从中间恢复。\\n\\n### FSDP2 兼容性修复模式 (2026-05-19)\\n- `_fsdp_wrapped_module` → `getattr(model, \\\"_fsdp_wrapped_module\\\", model)`\\n- `FSDP.summon_full_params(model)` → `FSDP.summon_full_params(model) if isinstance(model, FSDP) else nullcontext()`\\n- FSDP2 用 `fully_shard` composable API，不 wrap 模型，不存在 `_fsdp_wrapped_module`\\n\\n### ScienceWorld eval valid_action_rate bug (2026-05-19)\\n`action_is_valid` 必须对比完整 `valid_actions` 列表，不能对比截断的 `shown[:50]`（前 50 个几乎全是 `connect X to Y` 格式，模型输出的自然语言动作全被误判）。\\n\\n## 决策原因\\n\\n### 8B Cell C 用 FSDP2 + CPUOffloadPolicy (2026-05-19)\\nFSDP1 峰值 ~91 GB/GPU → OOM（v5-v8 全部失败）。FSDP2 CPUOffloadPolicy 将参数和优化器按 layer 搬到 CPU，峰值降至 ~83 GB/GPU，余量 ~12 GB。不需要租卡。\\n\\n### ScienceWorld GRPO reward 是 continuous sparse (2026-05-19)\\n公式：`reward = (score/100) * 10.0`，范围 0-10，仅 episode 结束发放。Cell A（step-level）预期失败：中间步 reward=0，最后一步有 continuous reward 但 step-level credit assignment 无法利用。Cell C（episode-level）自然兼容。\\n\\n## 约束\\n\\n### westd GPU 内存紧张 (2026-05-19)\\n8B FSDP2+CPUOffload 训练时 GPU 占用 ~83/95.6 GB (87%)。不要增加 batch size 或 max_model_len，无余量。\\n\", \"total_chars\": 1505, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "7cc65f61-2552-442c-ab95-2a9bca1b2f87",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\\\", \\\"content\\\": \\\"# Project Memory — cost-verify-agent-rl\\\\n\\\\n## 经验教训\\\\n\\\\n### max_prompt_length 必须严格小于 max_model_len (2026-05-19)\\\\nv9c 在 step 3/30 崩溃：`max_prompt_length: 16384 == max_model_len: 16384`，prompt 填满后 vLLM 报 \\\\\\\"prompt + requested output tokens > max_model_len\\\\\\\"。修复：`max_prompt_length = max_model_len - response_length`（15360 = 16384 - 1024）。写 config 时永远预留 generation headroom。\\\\n\\\\n### save_freq 不应设为 999 (2026-05-19)\\\\nv9c 崩溃后无 checkpoint 可恢复（save_freq: 999 = 实际不保存）。30 步训练建议 save_freq: 5~10，代价是少量磁盘但能从中间恢复。\\\\n\\\\n### FSDP2 兼容性修复模式 (2026-05-19)\\\\n- `_fsdp_wrapped_module` → `getattr(model, \\\\\\\"_fsdp_wrapped_module\\\\\\\", model)`\\\\n- `FSDP.summon_full_params(model)` → `FSDP.summon_full_params(model) if isinstance(model, FSDP) else nullcontext()`\\\\n- FSDP2 用 `fully_shard` composable API，不 wrap 模型，不存在 `_fsdp_wrapped_module`\\\\n\\\\n### ScienceWorld eval valid_action_rate bug (2026-05-19)\\\\n`action_is_valid` 必须对比完整 `valid_actions` 列表，不能对比截断的 `shown[:50]`（前 50 个几乎全是 `connect X to Y` 格式，模型输出的自然语言动作全被误判）。\\\\n\\\\n## 决策原因\\\\n\\\\n### 8B Cell C 用 FSDP2 + CPUOffloadPolicy (2026-05-19)\\\\nFSDP1 峰值 ~91 GB/GPU → OOM（v5-v8 全部失败）。FSDP2 CPUOffloadPolicy 将参数和优化器按 layer 搬到 CPU，峰值降至 ~83 GB/GPU，余量 ~12 GB。不需要租卡。\\\\n\\\\n### ScienceWorld GRPO reward 是 continuous sparse (2026-05-19)\\\\n公式：`reward = (score/100) * 10.0`，范围 0-10，仅 episode 结束发放。Cell A（step-level）预期失败：中间步 reward=0，最后一步有 continuous reward 但 step-level credit assignment 无法利用。Cell C（episode-level）自然兼容。\\\\n\\\\n## 约束\\\\n\\\\n### westd GPU 内存紧张 (2026-05-19)\\\\n8B FSDP2+CPUOffload 训练时 GPU 占用 ~83/95.6 GB (87%)。不要增加 batch size 或 max_model_len，无余量。\\\\n\\\", \\\"total_chars\\\": 1505, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\", \"content\": \"# Project Memory — cost-verify-agent-rl\\n\\n## 经验教训\\n\\n### max_prompt_length 必须严格小于 max_model_len (2026-05-19)\\nv9c 在 step 3/30 崩溃：`max_prompt_length: 16384 == max_model_len: 16384`，prompt 填满后 vLLM 报 \\\"prompt + requested output tokens > max_model_len\\\"。修复：`max_prompt_length = max_model_len - response_length`（15360 = 16384 - 1024）。写 config 时永远预留 generation headroom。\\n\\n### save_freq 不应设为 999 (2026-05-19)\\nv9c 崩溃后无 checkpoint 可恢复（save_freq: 999 = 实际不保存）。30 步训练建议 save_freq: 5~10，代价是少量磁盘但能从中间恢复。\\n\\n### FSDP2 兼容性修复模式 (2026-05-19)\\n- `_fsdp_wrapped_module` → `getattr(model, \\\"_fsdp_wrapped_module\\\", model)`\\n- `FSDP.summon_full_params(model)` → `FSDP.summon_full_params(model) if isinstance(model, FSDP) else nullcontext()`\\n- FSDP2 用 `fully_shard` composable API，不 wrap 模型，不存在 `_fsdp_wrapped_module`\\n\\n### ScienceWorld eval valid_action_rate bug (2026-05-19)\\n`action_is_valid` 必须对比完整 `valid_actions` 列表，不能对比截断的 `shown[:50]`（前 50 个几乎全是 `connect X to Y` 格式，模型输出的自然语言动作全被误判）。\\n\\n## 决策原因\\n\\n### 8B Cell C 用 FSDP2 + CPUOffloadPolicy (2026-05-19)\\nFSDP1 峰值 ~91 GB/GPU → OOM（v5-v8 全部失败）。FSDP2 CPUOffloadPolicy 将参数和优化器按 layer 搬到 CPU，峰值降至 ~83 GB/GPU，余量 ~12 GB。不需要租卡。\\n\\n### ScienceWorld GRPO reward 是 continuous sparse (2026-05-19)\\n公式：`reward = (score/100) * 10.0`，范围 0-10，仅 episode 结束发放。Cell A（step-level）预期失败：中间步 reward=0，最后一步有 continuous reward 但 step-level credit assignment 无法利用。Cell C（episode-level）自然兼容。\\n\\n## 约束\\n\\n### westd GPU 内存紧张 (2026-05-19)\\n8B FSDP2+CPUOffload 训练时 GPU 占用 ~83/95.6 GB (87%)。不要增加 batch size 或 max_model_len，无余量。\\n\", \"total_chars\": 1505, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
Now I need to add the v9d training experience to memory.md. Let me identify what's already there and what needs to be added:

Already present:
- max_prompt_length 必须严格小于 max_model_len — already covered
- save_freq 不应设为 999 — already covered
- FSDP2 兼容性修复模式 — already covered
- FSDP2 + CPUOffloadPolicy decision — already covered

Need to add:
1. save_contents yaml 路径必须在 actor_rollout_ref.actor.checkpoint 下（不是 trainer 下），错误位置导致 92GB vs 33GB checkpoint


2. FSDP2 checkpoints are sharded across world_size ranks and require a conversion script to merge them back into a single model
3. The 8B model's episode-level GRPO reward saturates quickly around 12 steps, so I need to plan OOD evaluation earlier in training
4. NCCL deadlocks show a distinctive pattern of 0% GPU utilization paired with 60GB memory usage that I can use to identify them

Let me organize these under the appropriate sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "4e7e56dd-921e-4bd8-865f-a527288845d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gk2o9YLA5mf8s8TSav4Zwt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 24857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1085
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

现在添加 v9d 经验。需要加载 save 工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "13f89269-87a5-4673-a379-a49086ac777e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gk2o9YLA5mf8s8TSav4Zwt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 24857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1085
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MoNCRfz1hAQJyHimNNbGmF`</summary>

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
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "51012e9b-3284-4133-b2a5-a47b558bb372",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gk2o9YLA5mf8s8TSav4Zwt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 24857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1085
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

_source line 12 · 2026-05-20T09:55:09.754Z_

<details><summary>↩ Tool result · `toolu_01MoNCRfz1hAQJyHimNNbGmF`</summary>

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
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "f23d9dac-2ed3-4ee6-af1b-645fc5decf89",
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

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_019z3XqMHjBKGePaPkTeJrTC`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "memory.md",
  "content": "# Project Memory — cost-verify-agent-rl\n\n## 经验教训\n\n### max_prompt_length 必须严格小于 max_model_len (2026-05-19)\nv9c 在 step 3/30 崩溃：`max_prompt_length: 16384 == max_model_len: 16384`，prompt 填满后 vLLM 报 \"prompt + requested output tokens > max_model_len\"。修复：`max_prompt_length = max_model_len - response_length`（15360 = 16384 - 1024）。写 config 时永远预留 generation headroom。\n\n### save_freq 不应设为 999 (2026-05-19)\nv9c 崩溃后无 checkpoint 可恢复（save_freq: 999 = 实际不保存）。30 步训练建议 save_freq: 5~10，代价是少量磁盘但能从中间恢复。\n\n### FSDP2 兼容性修复模式 (2026-05-19)\n- `_fsdp_wrapped_module` → `getattr(model, \"_fsdp_wrapped_module\", model)`\n- `FSDP.summon_full_params(model)` → `FSDP.summon_full_params(model) if isinstance(model, FSDP) else nullcontext()`\n- FSDP2 用 `fully_shard` composable API，不 wrap 模型，不存在 `_fsdp_wrapped_module`\n\n### save_contents 的 yaml 路径必须正确 (2026-05-20)\nverl checkpoint 的 `save_contents` 必须放在 `actor_rollout_ref.actor.checkpoint` 下，不是 `trainer` 下。错误路径导致保存完整 optimizer state（92GB），正确路径只保存 actor weights（33GB）。\n\n### FSDP2 checkpoint 是 rank shards 不是 HF 格式 (2026-05-20)\nFSDP2 保存的 checkpoint 是 `world_size_N` 目录下的 per-rank shards（`__0_0.distcp` 等），不是 HF safetensors。部署/评估前必须用 `convert_fsdp_to_hf.py` 合并为标准 HF 格式。\n\n### NCCL deadlock hang 的模式识别 (2026-05-20)\nv9d step 15 出现 NCCL deadlock：GPU utilization 0% 但显存仍占 ~60GB，进程不退出也不报错。这是典型的 collective 通信死锁（某 rank 未到达同步点）。发现后应直接 kill 进程，不要等待恢复。长训练建议设 `NCCL_TIMEOUT`。\n\n### 8B episode-level GRPO reward 饱和极快 (2026-05-20)\nv9d 训练曲线：40.6%(baseline) → 81.25%(step 5) → 96.875%(step 10) → 100%(step 12)。Step 12 后 advantage=0, pg_loss=0, grad_norm→0，完全无学习信号。教训：8B 模型在简单任务上 episode-level GRPO ≤15 steps 即可饱和，必须提前规划 OOD eval 和 early stopping，否则后续 steps 浪费算力且有 hang 风险。\n\n### ScienceWorld eval valid_action_rate bug (2026-05-19)\n`action_is_valid` 必须对比完整 `valid_actions` 列表，不能对比截断的 `shown[:50]`（前 50 个几乎全是 `connect X to Y` 格式，模型输出的自然语言动作全被误判）。\n\n## 决策原因\n\n### 8B Cell C 用 FSDP2 + CPUOffloadPolicy (2026-05-19)\nFSDP1 峰值 ~91 GB/GPU → OOM（v5-v8 全部失败）。FSDP2 CPUOffloadPolicy 将参数和优化器按 layer 搬到 CPU，峰值降至 ~83 GB/GPU，余量 ~12 GB。不需要租卡。\n\n### ScienceWorld GRPO reward 是 continuous sparse (2026-05-19)\n公式：`reward = (score/100) * 10.0`，范围 0-10，仅 episode 结束发放。Cell A（step-level）预期失败：中间步 reward=0，最后一步有 continuous reward 但 step-level credit assignment 无法利用。Cell C（episode-level）自然兼容。\n\n## 约束\n\n### westd GPU 内存紧张 (2026-05-19)\n8B FSDP2+CPUOffload 训练时 GPU 占用 ~83/95.6 GB (87%)。不要增加 batch size 或 max_model_len，无余量。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "7489ebce-968f-4dd7-b964-15bde709f1ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sght6JTsLEwRS4Wa6RdEax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 25942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 676
      },
      "output_tokens": 69,
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

_source line 14 · 2026-05-20T09:55:30.113Z_

<details><summary>↩ Tool result · `toolu_019z3XqMHjBKGePaPkTeJrTC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "3f443baa-ecd8-4ece-8847-fbb7c8ece361",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

已写入 4 条新经验：

1. **save_contents yaml 路径** — 必须在 `actor_rollout_ref.actor.checkpoint` 下，错误路径导致 92GB vs 33GB checkpoint
2. **FSDP2 checkpoint 格式** — rank shards 需 `convert_fsdp_to_hf.py` 合并才能部署
3. **NCCL deadlock 模式** — 0% GPU util + 高显存占用 = collective 死锁，直接 kill
4. **8B GRPO 饱和速度** — ≤15 steps 即饱和，需提前规划 OOD eval 和 early stopping

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "uuid": "f5a4f510-cb78-4055-b155-12d2c3421342",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvR7sUsFfT4oFbkskMJ5Ef",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 26618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1549
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

_source line 16_

已写入 4 条新经验：

1. **save_contents yaml 路径** — 必须在 `actor_rollout_ref.actor.checkpoint` 下，错误路径导致 92GB vs 33GB checkpoint
2. **FSDP2 checkpoint 格式** — rank shards 需 `convert_fsdp_to_hf.py` 合并才能部署
3. **NCCL deadlock 模式** — 0% GPU util + 高显存占用 = collective 死锁，直接 kill
4. **8B GRPO 饱和速度** — ≤15 steps 即饱和，需提前规划 OOD eval 和 early stopping

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 40612,
  "duration_api_ms": 41758,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "9ca195d1-cc7e-4300-988c-ca251e873b37",
  "total_cost_usd": 0.2175255,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 16326,
    "cache_read_input_tokens": 113664,
    "output_tokens": 2262,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 16326,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 187,
        "cache_read_input_tokens": 26618,
        "cache_creation_input_tokens": 1549,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1549
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1956,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002051,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 2262,
      "cacheReadInputTokens": 113664,
      "cacheCreationInputTokens": 16326,
      "webSearchRequests": 0,
      "costUSD": 0.2154745,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "82688ef0-2ca8-48a9-aed8-f802833f6a3d"
}
```

</details>

---
