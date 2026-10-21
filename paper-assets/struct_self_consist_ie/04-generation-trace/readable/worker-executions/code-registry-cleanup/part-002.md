# code registry cleanup — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-registry-cleanup.md) · [Structured JSON](../../../sessions/6a/6a1be7ddbb0da03045ff.json)

## Before a recorded user message

### Assistant

_source line 234_

Here's the cleanup report.

---

## Registry 清理报告

### 1. Degen_rate 字段验证

| 状态 | 数量 | 详情 |
|---|---|---|
| degen_rate 正确 + 已有 degen_rate_source | 22 | 全部与 unified audit 一致 ✓ |
| degen_rate 正确 + **新增** degen_rate_source | 2 | exp_029a (0.064), exp_029b (0.478) |
| 有 sample_f1_pct_zero 无 degen_rate | 2 | exp_003_ner_wnut17, exp_003_wnut17_eval (WNUT17 不在 unified audit 中) |
| degen_rate 值错误需更新 | **0** | — |

**结论**: 所有 24 个含 degen_rate 的实验值均已确认为 unified constant-F1 gold-filtered 定义，全部已标注 `degen_rate_source`。

### 2. 新注册实验

| 类别 | 数量 | 实验 |
|---|---|---|
| CoNLL N=16 多 seed | 2 | exp_002_conll_n16_seed123, exp_002_conll_n16_seed456 |
| FewNERD N=8 多 seed | 2 | exp_021_fewnerd_n8_seed123, exp_021_fewnerd_n8_seed456 |
| 温度消融多 seed（后台注册中）| 9 | exp_026_t{05,08,10,12}_seed{42,123,456} |
| **合计** | **13** | |

### 3. 仍未注册的 output 目录（31 个）

| 分类 | 数量 | 说明 |
|---|---|---|
| 旧命名规范重复 | 16 | exp001_* 已在 exp_001_* 下注册 |
| 子集/pilot/dryrun | 10 | 200only, backup, pilot, smoke 等 |
| 已注册实验别名 | 2 | exp_029a_scierc_3epoch → exp_029a |
| gate0 微调实验 | 2 | gate0_ft002v2, gate0_ft002v2_ckpt400 |
| **待决定是否注册** | **8** | 见下方 |

**8 个待决定实验**:
- `exp_002_conll_n8_seed123`, `exp_002_conll_n8_seed456` — CoNLL N=8 多 seed
- `exp_021_fewnerd_n8_seed789_shard0/1/2` — FewNERD seed=789 分片
- `exp_023_rank8_inference` — LoRA rank=8 推理
- `exp_003_wnut17_v2_infer` — WNUT17 v2 推理
- `exp_scale_qwen3_4b_conll` — Qwen3-4B CoNLL 扩展实验

### 4. 仍有问题的条目

- **exp_003_ner_wnut17** 和 **exp_003_wnut17_eval**: 仍有旧 `sample_f1_pct_zero=53.7` 字段，无 unified degen_rate（WNUT17 未纳入 unified audit）
- **exp_llama_fewnerd_lora**: 状态为 RUNNING，可能已过期

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05",
  "uuid": "05961d89-fd51-4f07-b22f-3a16cda0aafb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bMZkLR2mqZLgooZYPyARg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2798,
      "cache_read_input_tokens": 110118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2798
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


### System

_source line 235_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 46740,
    "tool_uses": 47,
    "duration_ms": 101995
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "e80fd279-c036-4354-b309-ca1168c3c5c8",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 236_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 46741,
    "tool_uses": 48,
    "duration_ms": 102948
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "8c072a0b-7030-4b65-bdab-390528f8a3ba",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 237_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 46742,
    "tool_uses": 49,
    "duration_ms": 103864
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "cbb871bd-9b25-4b82-89ba-59832187cfe2",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 238_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 46743,
    "tool_uses": 50,
    "duration_ms": 104897
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "803e6dc5-6714-4b08-877c-7a55b64c6938",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 239_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 46744,
    "tool_uses": 51,
    "duration_ms": 105783
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "c2150fa8-bbd1-4faf-bbca-c837c2f08b17",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 240_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 46745,
    "tool_uses": 52,
    "duration_ms": 106247
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "6a05ab5a-63d0-4394-8db9-0ca834200fde",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 241_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 46746,
    "tool_uses": 53,
    "duration_ms": 107183
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "a4d5294f-c79d-4c79-aa86-6e06b614d357",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 242_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 46747,
    "tool_uses": 54,
    "duration_ms": 108094
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "208d776f-5c72-4125-b858-cbac3ecf3769",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 243_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 46748,
    "tool_uses": 55,
    "duration_ms": 108626
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "00b0f260-47ec-46c7-a82e-1a0b65c27c94",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 244_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 51711,
    "tool_uses": 56,
    "duration_ms": 124452
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "0217fff4-a3fb-4e87-ac08-162f013039d5",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 245_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 51712,
    "tool_uses": 57,
    "duration_ms": 125878
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "4e6b7355-4ea6-4e1a-ae0d-d64d627735d0",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 246_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 51713,
    "tool_uses": 58,
    "duration_ms": 127317
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "0d693269-2db5-42f4-8693-f91784add0a3",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 247_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 51714,
    "tool_uses": 59,
    "duration_ms": 128902
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "bf02da29-daca-4a53-9b99-c62c39ae0f1c",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 248_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 51715,
    "tool_uses": 60,
    "duration_ms": 130310
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "9ae94406-ed5a-442a-b178-44597113c7ee",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 249_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 51716,
    "tool_uses": 61,
    "duration_ms": 131722
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "39552646-2ac6-413f-8cd3-ddb2565f64aa",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 250_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 51717,
    "tool_uses": 62,
    "duration_ms": 133050
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "8eaf4bc6-0b69-4d10-814f-72926da9b1d8",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 251_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 51718,
    "tool_uses": 63,
    "duration_ms": 134402
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "5da6a524-1d48-4f14-800e-3ac04a0fc261",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 252_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "description": "Register temp ablation experiments",
  "usage": {
    "total_tokens": 51719,
    "tool_uses": 64,
    "duration_ms": 135812
  },
  "last_tool_name": "mcp__agent-ml-research__update_registry",
  "uuid": "889faf22-83f5-4bd4-8089-4c703ed6238e",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 253_

```json
{
  "type": "system",
  "subtype": "task_updated",
  "task_id": "a8c98754d66e6ac34",
  "patch": {
    "status": "completed",
    "end_time": 1779142053616
  },
  "uuid": "20dfe7ac-2bba-4a22-8b9a-74f3998d7b93",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05"
}
```

---


### System

_source line 254_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a8c98754d66e6ac34",
  "tool_use_id": "toolu_012PK5yNw5GPJwbwT75QJhgq",
  "status": "completed",
  "output_file": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/f7660589-73d5-4b7d-9ccf-30435e81fc05/tasks/a8c98754d66e6ac34.output",
  "summary": "Agent \"Register temp ablation experiments\" completed",
  "usage": {
    "total_tokens": 58169,
    "tool_uses": 64,
    "duration_ms": 145322
  },
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05",
  "uuid": "813a62af-e28e-42d6-9a40-445fe24ff5c6"
}
```

---


### System

_source line 255_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "ac72329e-63aa-4161-8328-a5d70a87c2ee",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
  },
  "fast_mode_state": "off"
}
```

---


### Assistant

_source line 256_

后台 agent 完成，9 个温度消融多 seed 实验全部注册成功。

**最终汇总**:

| 操作 | 数量 |
|---|---|
| degen_rate_source 新增标注 | 2 (exp_029a, exp_029b) |
| degen_rate 值需修正 | 0 |
| 新注册实验 | **13** (4 CoNLL/FewNERD 多 seed + 9 温度消融多 seed) |
| 仍有旧 sample_f1_pct_zero 残留 | 2 (exp_003_ner_wnut17, exp_003_wnut17_eval — WNUT17 无 unified audit) |
| 待决定是否注册 | 8 (N=8 CoNLL, FewNERD seed789 分片, rank8, scale 等) |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05",
  "uuid": "afb70ea4-d7da-4daa-97b3-d3507eae67b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNuJKyxWiz87KiR6fGFmuK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2409,
      "cache_read_input_tokens": 112916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2409
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

_source line 257_

后台 agent 完成，9 个温度消融多 seed 实验全部注册成功。

**最终汇总**:

| 操作 | 数量 |
|---|---|
| degen_rate_source 新增标注 | 2 (exp_029a, exp_029b) |
| degen_rate 值需修正 | 0 |
| 新注册实验 | **13** (4 CoNLL/FewNERD 多 seed + 9 温度消融多 seed) |
| 仍有旧 sample_f1_pct_zero 残留 | 2 (exp_003_ner_wnut17, exp_003_wnut17_eval — WNUT17 无 unified audit) |
| 待决定是否注册 | 8 (N=8 CoNLL, FewNERD seed789 分片, rank8, scale 等) |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 5409,
  "duration_api_ms": 657550,
  "num_turns": 1,
  "stop_reason": "end_turn",
  "session_id": "f7660589-73d5-4b7d-9ccf-30435e81fc05",
  "total_cost_usd": 3.5283162499999996,
  "usage": {
    "input_tokens": 3,
    "cache_creation_input_tokens": 2409,
    "cache_read_input_tokens": 112916,
    "output_tokens": 248,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 2409,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 248,
        "cache_read_input_tokens": 112916,
        "cache_creation_input_tokens": 2409,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2409
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1320,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00142,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 49,
      "outputTokens": 47493,
      "cacheReadInputTokens": 2497965,
      "cacheCreationInputTokens": 174455,
      "webSearchRequests": 0,
      "costUSD": 3.52689625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "origin": {
    "kind": "task-notification"
  },
  "uuid": "c5dbff5e-35e4-4d1d-82fc-742a19ba6f32"
}
```

</details>

---
