# ops eval progress and c2 config check

**tbab multi turn** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_ops_eval-progress-and-c2-config-check_20260518T180059.log`
- **Structured JSON:** [`29da9bdefc429f4af5b1.json`](../../sessions/29/29da9bdefc429f4af5b1.json)

## Before a recorded user message

10 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/tbab_multi_turn",
  "session_id": "4c41d6a9-98d7-4fad-8022-d06bb5a641d6",
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
  "uuid": "a298b303-d2c9-40ab-b479-cb85713a52d7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-tbab-multi-turn/memory/"
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
    "resetsAt": 1779141600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "928d6822-77b4-4370-85aa-2918d08e6d40",
  "session_id": "4c41d6a9-98d7-4fad-8022-d06bb5a641d6"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to SSH to westb-25721 and execute several commands. Let me use the ssh_execute tool. First, I need to load the tool schema.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4c41d6a9-98d7-4fad-8022-d06bb5a641d6",
  "uuid": "23102936-ca2d-4e67-b092-29c5abdd4b17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4awGhX5w9tL1RbrPQ3Koa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13091,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13091
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017RcGWhCMQh7mBjcAU8xnMv`</summary>

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
  "session_id": "4c41d6a9-98d7-4fad-8022-d06bb5a641d6",
  "uuid": "9defe2f3-037b-40d9-8326-3481df2952ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4awGhX5w9tL1RbrPQ3Koa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13091,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13091
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

_source line 6 · 2026-05-18T18:01:11.870Z_

<details><summary>↩ Tool result · `toolu_017RcGWhCMQh7mBjcAU8xnMv`</summary>

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
  "session_id": "4c41d6a9-98d7-4fad-8022-d06bb5a641d6",
  "uuid": "e0d60b78-2869-4b3e-a140-d153ba0d537d",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01CVnstiPcdfddEiL8SEVWvV`</summary>

```json
{
  "server": "westb-25721",
  "account": "root",
  "command": "\n# Task 1: Eval progress\necho \"=== C4_s42 eval ===\"\ntmux has-session -t eval_c4_s42 2>/dev/null && echo \"alive\" || echo \"dead\"\ntmux capture-pane -t eval_c4_s42 -p | tail -10\n\necho \"\"\necho \"=== C1_s137 eval ===\"\ntmux has-session -t eval_c1_s137 2>/dev/null && echo \"alive\" || echo \"dead\"\ntmux capture-pane -t eval_c1_s137 -p | tail -10\n\necho \"\"\necho \"=== GPU status ===\"\nnvidia-smi --query-compute-apps=pid,used_memory --format=csv\n\necho \"\"\necho \"=== Task 2: C2 config ===\"\ncat /root/tbab_multi_turn/scripts/configs/condition2_position_reset.yaml\n\necho \"\"\necho \"=== Task 2: C3 config ===\"\ncat /root/tbab_multi_turn/scripts/configs/condition3_bridge_standard_pos.yaml\n\necho \"\"\necho \"=== Task 3: C2_s42 training ===\"\ntmux has-session -t mvp_c2_s42 2>/dev/null && echo \"alive\" || echo \"dead\"\ntail -10 ~/runs/tbab_multi_turn/mvp_c2_s42.log 2>/dev/null || echo \"No log file found\"\n",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4c41d6a9-98d7-4fad-8022-d06bb5a641d6",
  "uuid": "2c990da0-50c6-446e-a7aa-55cba1b62c1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGk5Lqjg8z4KXgN4MsXGhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 398,
      "cache_read_input_tokens": 24538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 398
      },
      "output_tokens": 68,
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

_source line 8 · 2026-05-18T18:01:20.191Z_

<details><summary>↩ Tool result · `toolu_01CVnstiPcdfddEiL8SEVWvV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== C4_s42 eval ===\\nalive\\n[62/91] repeat=1 task=code id=sharded-livecodebench/2855\\n  -> wrong (score=0, turns=9)\\n[63/91] repeat=1 task=code id=sharded-livecodebench/2856\\n  -> wrong (score=0, turns=7)\\n[64/91] repeat=1 task=code id=sharded-livecodebench/2857\\n  -> wrong (score=0, turns=8)\\n[65/91] repeat=1 task=code id=sharded-livecodebench/2866\\n  -> wrong (score=0, turns=8)\\n[66/91] repeat=1 task=code id=sharded-livecodebench/2867\\n\\n\\n=== C1_s137 eval ===\\nalive\\n[60/91] repeat=1 task=code id=sharded-livecodebench/2847\\n  -> wrong (score=0, turns=10)\\n[61/91] repeat=1 task=code id=sharded-livecodebench/2850\\n  -> wrong (score=0, turns=6)\\n[62/91] repeat=1 task=code id=sharded-livecodebench/2855\\n  -> wrong (score=0, turns=9)\\n[63/91] repeat=1 task=code id=sharded-livecodebench/2856\\n  -> wrong (score=0, turns=7)\\n[64/91] repeat=1 task=code id=sharded-livecodebench/2857\\n\\n\\n=== GPU status ===\\npid, used_gpu_memory [MiB]\\n48198, 17160 MiB\\n50027, 17254 MiB\\n\\n=== Task 2: C2 config ===\\ncondition_name: c2_pos_reset\\nuse_bridge_tokens: false\\nuse_position_reset: true\\nnum_bridge_tokens: 0\\n\\nmodel_name_or_path: /root/autodl-tmp/models/Mistral-7B-Instruct-v0.1\\n\\nlora_r: 32\\nlora_alpha: 64\\nlora_dropout: 0.05\\n\\nlearning_rate: 2.0e-4\\nnum_epochs: 3\\nper_device_train_batch_size: 2\\ngradient_accumulation_steps: 8\\nmax_seq_length: 4096\\nwarmup_ratio: 0.03\\nlogging_steps: 10\\ngradient_checkpointing: true\\n\\ndata_path: /root/tbab_multi_turn/data/training_data.json\\n\\n=== Task 2: C3 config ===\\ncondition_name: c3_bridge_standard\\nuse_bridge_tokens: true\\nuse_position_reset: false\\nnum_bridge_tokens: 4\\n\\nmodel_name_or_path: /root/autodl-tmp/models/Mistral-7B-Instruct-v0.1\\n\\nlora_r: 32\\nlora_alpha: 64\\nlora_dropout: 0.05\\n\\nlearning_rate: 2.0e-4\\nnum_epochs: 3\\nper_device_train_batch_size: 2\\ngradient_accumulation_steps: 8\\nmax_seq_length: 4096\\nwarmup_ratio: 0.03\\nlogging_steps: 10\\ngradient_checkpointing: true\\n\\ndata_path: /root/tbab_multi_turn/data/training_data.json\\n\\n=== Task 3: C2_s42 training ===\\ndead\\n[INFO] Running in WANDB offline mode\\nTraceback (most recent call last):\\n  File \\\"/root/tbab_multi_turn/scripts/train.py\\\", line 173, in &lt;module>\\n    main()\\n  File \\\"/root/tbab_multi_turn/scripts/train.py\\\", line 87, in main\\n    config = load_config(args.config)\\n  File \\\"/root/tbab_multi_turn/scripts/train.py\\\", line 31, in load_config\\n    with open(config_path) as f:\\nFileNotFoundError: [Errno 2] No such file or directory: 'configs/condition2_position_reset.yaml'\\nEXIT_CODE=1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4c41d6a9-98d7-4fad-8022-d06bb5a641d6",
  "uuid": "6c18817c-094a-4684-8b0f-d0e6d7b4e49c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== C4_s42 eval ===\\\\nalive\\\\n[62/91] repeat=1 task=code id=sharded-livecodebench/2855\\\\n  -> wrong (score=0, turns=9)\\\\n[63/91] repeat=1 task=code id=sharded-livecodebench/2856\\\\n  -> wrong (score=0, turns=7)\\\\n[64/91] repeat=1 task=code id=sharded-livecodebench/2857\\\\n  -> wrong (score=0, turns=8)\\\\n[65/91] repeat=1 task=code id=sharded-livecodebench/2866\\\\n  -> wrong (score=0, turns=8)\\\\n[66/91] repeat=1 task=code id=sharded-livecodebench/2867\\\\n\\\\n\\\\n=== C1_s137 eval ===\\\\nalive\\\\n[60/91] repeat=1 task=code id=sharded-livecodebench/2847\\\\n  -> wrong (score=0, turns=10)\\\\n[61/91] repeat=1 task=code id=sharded-livecodebench/2850\\\\n  -> wrong (score=0, turns=6)\\\\n[62/91] repeat=1 task=code id=sharded-livecodebench/2855\\\\n  -> wrong (score=0, turns=9)\\\\n[63/91] repeat=1 task=code id=sharded-livecodebench/2856\\\\n  -> wrong (score=0, turns=7)\\\\n[64/91] repeat=1 task=code id=sharded-livecodebench/2857\\\\n\\\\n\\\\n=== GPU status ===\\\\npid, used_gpu_memory [MiB]\\\\n48198, 17160 MiB\\\\n50027, 17254 MiB\\\\n\\\\n=== Task 2: C2 config ===\\\\ncondition_name: c2_pos_reset\\\\nuse_bridge_tokens: false\\\\nuse_position_reset: true\\\\nnum_bridge_tokens: 0\\\\n\\\\nmodel_name_or_path: /root/autodl-tmp/models/Mistral-7B-Instruct-v0.1\\\\n\\\\nlora_r: 32\\\\nlora_alpha: 64\\\\nlora_dropout: 0.05\\\\n\\\\nlearning_rate: 2.0e-4\\\\nnum_epochs: 3\\\\nper_device_train_batch_size: 2\\\\ngradient_accumulation_steps: 8\\\\nmax_seq_length: 4096\\\\nwarmup_ratio: 0.03\\\\nlogging_steps: 10\\\\ngradient_checkpointing: true\\\\n\\\\ndata_path: /root/tbab_multi_turn/data/training_data.json\\\\n\\\\n=== Task 2: C3 config ===\\\\ncondition_name: c3_bridge_standard\\\\nuse_bridge_tokens: true\\\\nuse_position_reset: false\\\\nnum_bridge_tokens: 4\\\\n\\\\nmodel_name_or_path: /root/autodl-tmp/models/Mistral-7B-Instruct-v0.1\\\\n\\\\nlora_r: 32\\\\nlora_alpha: 64\\\\nlora_dropout: 0.05\\\\n\\\\nlearning_rate: 2.0e-4\\\\nnum_epochs: 3\\\\nper_device_train_batch_size: 2\\\\ngradient_accumulation_steps: 8\\\\nmax_seq_length: 4096\\\\nwarmup_ratio: 0.03\\\\nlogging_steps: 10\\\\ngradient_checkpointing: true\\\\n\\\\ndata_path: /root/tbab_multi_turn/data/training_data.json\\\\n\\\\n=== Task 3: C2_s42 training ===\\\\ndead\\\\n[INFO] Running in WANDB offline mode\\\\nTraceback (most recent call last):\\\\n  File \\\\\\\"/root/tbab_multi_turn/scripts/train.py\\\\\\\", line 173, in &lt;module>\\\\n    main()\\\\n  File \\\\\\\"/root/tbab_multi_turn/scripts/train.py\\\\\\\", line 87, in main\\\\n    config = load_config(args.config)\\\\n  File \\\\\\\"/root/tbab_multi_turn/scripts/train.py\\\\\\\", line 31, in load_config\\\\n    with open(config_path) as f:\\\\nFileNotFoundError: [Errno 2] No such file or directory: 'configs/condition2_position_reset.yaml'\\\\nEXIT_CODE=1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== C4_s42 eval ===\\nalive\\n[62/91] repeat=1 task=code id=sharded-livecodebench/2855\\n  -> wrong (score=0, turns=9)\\n[63/91] repeat=1 task=code id=sharded-livecodebench/2856\\n  -> wrong (score=0, turns=7)\\n[64/91] repeat=1 task=code id=sharded-livecodebench/2857\\n  -> wrong (score=0, turns=8)\\n[65/91] repeat=1 task=code id=sharded-livecodebench/2866\\n  -> wrong (score=0, turns=8)\\n[66/91] repeat=1 task=code id=sharded-livecodebench/2867\\n\\n\\n=== C1_s137 eval ===\\nalive\\n[60/91] repeat=1 task=code id=sharded-livecodebench/2847\\n  -> wrong (score=0, turns=10)\\n[61/91] repeat=1 task=code id=sharded-livecodebench/2850\\n  -> wrong (score=0, turns=6)\\n[62/91] repeat=1 task=code id=sharded-livecodebench/2855\\n  -> wrong (score=0, turns=9)\\n[63/91] repeat=1 task=code id=sharded-livecodebench/2856\\n  -> wrong (score=0, turns=7)\\n[64/91] repeat=1 task=code id=sharded-livecodebench/2857\\n\\n\\n=== GPU status ===\\npid, used_gpu_memory [MiB]\\n48198, 17160 MiB\\n50027, 17254 MiB\\n\\n=== Task 2: C2 config ===\\ncondition_name: c2_pos_reset\\nuse_bridge_tokens: false\\nuse_position_reset: true\\nnum_bridge_tokens: 0\\n\\nmodel_name_or_path: /root/autodl-tmp/models/Mistral-7B-Instruct-v0.1\\n\\nlora_r: 32\\nlora_alpha: 64\\nlora_dropout: 0.05\\n\\nlearning_rate: 2.0e-4\\nnum_epochs: 3\\nper_device_train_batch_size: 2\\ngradient_accumulation_steps: 8\\nmax_seq_length: 4096\\nwarmup_ratio: 0.03\\nlogging_steps: 10\\ngradient_checkpointing: true\\n\\ndata_path: /root/tbab_multi_turn/data/training_data.json\\n\\n=== Task 2: C3 config ===\\ncondition_name: c3_bridge_standard\\nuse_bridge_tokens: true\\nuse_position_reset: false\\nnum_bridge_tokens: 4\\n\\nmodel_name_or_path: /root/autodl-tmp/models/Mistral-7B-Instruct-v0.1\\n\\nlora_r: 32\\nlora_alpha: 64\\nlora_dropout: 0.05\\n\\nlearning_rate: 2.0e-4\\nnum_epochs: 3\\nper_device_train_batch_size: 2\\ngradient_accumulation_steps: 8\\nmax_seq_length: 4096\\nwarmup_ratio: 0.03\\nlogging_steps: 10\\ngradient_checkpointing: true\\n\\ndata_path: /root/tbab_multi_turn/data/training_data.json\\n\\n=== Task 3: C2_s42 training ===\\ndead\\n[INFO] Running in WANDB offline mode\\nTraceback (most recent call last):\\n  File \\\"/root/tbab_multi_turn/scripts/train.py\\\", line 173, in &lt;module>\\n    main()\\n  File \\\"/root/tbab_multi_turn/scripts/train.py\\\", line 87, in main\\n    config = load_config(args.config)\\n  File \\\"/root/tbab_multi_turn/scripts/train.py\\\", line 31, in load_config\\n    with open(config_path) as f:\\nFileNotFoundError: [Errno 2] No such file or directory: 'configs/condition2_position_reset.yaml'\\nEXIT_CODE=1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

## 结果汇总

### Eval 进度
| Session | 状态 | 进度 |
|---------|------|------|
| C4_s42 | alive | **66/91**（正在跑第 66 个） |
| C1_s137 | alive | **64/91**（正在跑第 64 个） |

GPU 占用：两个进程分别占 17160 MiB 和 17254 MiB。

### C2/C3 配置 — 均正确

- **C2** (`condition2_position_reset.yaml`): `use_bridge_tokens: false`, `use_position_reset: true` ✓
- **C3** (`condition3_bridge_standard_pos.yaml`): `use_bridge_tokens: true`, `use_position_reset: false` ✓

### C2_s42 训练 — 已崩溃

tmux session `mvp_c2_s42` 已 **dead**。日志显示启动即报错：

```
FileNotFoundError: No such file or directory: 'configs/condition2_position_reset.yaml'
```

原因：训练脚本用了**相对路径** `configs/condition2_position_reset.yaml`，而 `cwd` 不在 `/root/tbab_multi_turn/scripts/`。需要改为绝对路径或确保启动命令先 `cd /root/tbab_multi_turn/scripts/` 再运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4c41d6a9-98d7-4fad-8022-d06bb5a641d6",
  "uuid": "cc95ff2a-969c-4dc6-9dea-778cdf81a98a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ru47ymnX4dkneEd1d1x67j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1707,
      "cache_read_input_tokens": 24936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1707
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

_source line 10_

## 结果汇总

### Eval 进度
| Session | 状态 | 进度 |
|---------|------|------|
| C4_s42 | alive | **66/91**（正在跑第 66 个） |
| C1_s137 | alive | **64/91**（正在跑第 64 个） |

GPU 占用：两个进程分别占 17160 MiB 和 17254 MiB。

### C2/C3 配置 — 均正确

- **C2** (`condition2_position_reset.yaml`): `use_bridge_tokens: false`, `use_position_reset: true` ✓
- **C3** (`condition3_bridge_standard_pos.yaml`): `use_bridge_tokens: true`, `use_position_reset: false` ✓

### C2_s42 训练 — 已崩溃

tmux session `mvp_c2_s42` 已 **dead**。日志显示启动即报错：

```
FileNotFoundError: No such file or directory: 'configs/condition2_position_reset.yaml'
```

原因：训练脚本用了**相对路径** `configs/condition2_position_reset.yaml`，而 `cwd` 不在 `/root/tbab_multi_turn/scripts/`。需要改为绝对路径或确保启动命令先 `cd /root/tbab_multi_turn/scripts/` 再运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 20200,
  "duration_api_ms": 19565,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "4c41d6a9-98d7-4fad-8022-d06bb5a641d6",
  "total_cost_usd": 0.1519275,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 15196,
    "cache_read_input_tokens": 60921,
    "output_tokens": 1004,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 15196,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 389,
        "cache_read_input_tokens": 24936,
        "cache_creation_input_tokens": 1707,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1707
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1287,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001357,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 1004,
      "cacheReadInputTokens": 60921,
      "cacheCreationInputTokens": 15196,
      "webSearchRequests": 0,
      "costUSD": 0.1505705,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "14387ec7-a119-4a9b-a5f9-d97e6f71c2b0"
}
```

</details>

---
