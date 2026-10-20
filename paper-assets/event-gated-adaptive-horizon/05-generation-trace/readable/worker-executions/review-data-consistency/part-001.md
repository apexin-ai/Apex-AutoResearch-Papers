# review data consistency — Part 1 of 2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

[Transcript overview](../review-data-consistency.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/d5/d5df406346b781b9504d.json)

## Before a recorded user message

## Before a recorded user message

36 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
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
  "uuid": "6962c7ae-e9fd-4ee5-ae2f-e00f2e664b4b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779597600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "aae09b1b-ff35-48b9-9ecd-b9380b4e8080",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do a comprehensive consistency check between the paper's LaTeX files and the registry data. Let me start by:

1. Finding the tex files on the server
2. Reading the registry data
3. Comparing all quantitative claims

Let me launch parallel operations to gather all the data I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "139a7b76-c249-4601-8952-33bbdb875eec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaqwPomivPmF41dMEm46Az",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12419,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12419
      },
      "output_tokens": 23,
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

_source line 5_

开始执行论文数据一致性检查。先并行获取服务器上的 tex 文件和 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "25240dc3-897b-48f0-8e12-48cca5c2c483",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaqwPomivPmF41dMEm46Az",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12419,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12419
      },
      "output_tokens": 23,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RMi7vYScsfyWdeA6mqPiJi`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
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
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "537f6bf4-d51a-440c-8597-60fdeadff7a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaqwPomivPmF41dMEm46Az",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12419,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12419
      },
      "output_tokens": 23,
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

_source line 7 · 2026-05-24T02:13:15.614Z_

<details><summary>↩ Tool result · `toolu_01RMi7vYScsfyWdeA6mqPiJi`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "ff00835b-a629-4edc-8a0f-88f89363a81a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013h4NkiKAR23X7nSRs5Qi1Y`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "find /root/autodl-tmp/event-gated-adaptive-horizon -name \"*.tex\" -not -path \"*/logdir/*\" -not -path \"*/.git/*\"",
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
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "8eda3c96-0093-4507-a52e-b04d14567c34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpDu5snx5WQgpwe6gZVuTg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 23866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
      },
      "output_tokens": 46,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_012mn5hn8Eqx2YPC1iXASLoL`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "limit": 0,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "40071cba-199f-442a-b179-1d6d41ebe9e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpDu5snx5WQgpwe6gZVuTg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 23866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
      },
      "output_tokens": 46,
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

_source line 10 · 2026-05-24T02:13:23.393Z_

<details><summary>↩ Tool result · `toolu_013h4NkiKAR23X7nSRs5Qi1Y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "6c96ed18-f052-4107-a847-20980502fedf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.38}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-24T02:13:24.867Z_

<details><summary>↩ Tool result · `toolu_012mn5hn8Eqx2YPC1iXASLoL`</summary>

```text
Error: result (298,026 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "b8c30970-9a5e-47c9-b8b7-e4ca8bd54089",
  "tool_use_result": {
    "content": "Error: result (298,026 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_058_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:10:49.773Z\", \"updated_at\": \"2026-05-24T00:30:00.000Z\", \"hypothesis\": \"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\", \"parent\": \"exp_046_frozen_dt_emb_cheetah\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 164830, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:30:00.000Z\", \"metrics\": {\"total_steps\": 224000, \"ve_ratio_peak\": 0.231, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.107, \"ve_ratio_final_step\": 215000, \"eval_return_final\": 80.46, \"eval_return_final_step\": 215000, \"eval_return_peak\": 191.74, \"eval_return_peak_step\": 25000, \"nve_peak\": 0.78, \"nve_peak_step\": 45000, \"nve_classification\": \"no_civo\", \"note\": \"Cheetah frozen s1. NVE=0.78× (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\"}}, \"exp_056_peginsertion_frozen_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:02:23.683Z\", \"updated_at\": \"2026-05-24T00:00:00.000Z\", \"hypothesis\": \"D143 混合机制假说验证——PegInsertion frozen dt_emb 跨 seed 可复现性。exp_053 (s0) 显示 frozen 在 82.5K 回落到 1.82 而 trained 攀升到 10.05，s1 验证这个分叉是否可复现。如果 s1 也回落 → frozen 稳健阻止 dt_emb 放大；如果不回落 → seed-dependent。\", \"parent\": \"exp_053_peginsertion_frozen_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 346430, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_056_peginsertion_frozen_s1/train.log\", \"checkpoint_path\": \"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:00:00.000Z\", \"metrics\": {\"total_steps\": 222500, \"ve_ratio_peak\": 11.321, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 1.193, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 4.37, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.42, \"eval_return_peak_step\": 132500, \"nve_classification\": \"burst\", \"note\": \"Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 — frozen does NOT suppress ManiSkill transients.\", \"ve_ratio_trajectory\": {\"12500\": 0.316, \"22500\": 0.975, \"32500\": 1.839, \"42500\": 1.966, \"52500\": 5.422, \"62500\": 4.047, \"72500\": 8.408, \"82500\": 11.321, \"92500\": 3.724, \"102500\": 3.034, \"112500\": 2.204, \"122500\": 2.425, \"132500\": 0.842, \"142500\": 2.194, \"152500\": 2.203, \"162500\": 0.651, \"172500\": 1.085, \"182500\": 1.07, \"192500\": 0.467, \"202500\": 0.708, \"212500\": 1.193}}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:50:00.000Z\", \"updated_at\": \"2026-05-23T23:38:30.000Z\", \"hypothesis\": \"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，最终自修复到 0.379@212.5K）。如果 s1 也触发持续 CIVO → PegInsertion CIVO 可复现；如果不触发 → seed-specific 异常。\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 345223, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\"}, \"ve_ratio_peak\": \"3.08@92500\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T23:38:25.428Z\", \"metrics\": {\"total_steps\": 222400, \"ve_ratio_peak\": 3.08, \"ve_ratio_peak_step\": 92500, \"ve_ratio_final\": 0.498, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 11.44, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.05, \"eval_return_peak_step\": 112500, \"nve_classification\": \"transient\", \"civo_triggered\": true, \"civo_self_corrected\": \"partial\", \"note\": \"CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 — severity seed-dependent.\", \"ve_ratio_trajectory\": {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2.0, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}}, \"checkpoint_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/checkpoint_222500.pt\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:25:00.000Z\", \"updated_at\": \"2026-05-23T23:30:00.000Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\"}, \"completed_at\": \"2026-05-23T23:30:00.000Z\", \"metrics\": {\"total_steps\": 225000, \"ve_ratio_peak\": 1.283, \"ve_ratio_peak_step\": 115000, \"ve_ratio_final\": 0.177, \"ve_ratio_final_step\": 215000, \"nve_peak\": 1.88, \"nve_peak_step\": 115000, \"nve_classification\": \"transient\", \"note\": \"Walker frozen s2. NVE=1.88× (raw 1.283 / baseline 0.683 @115K). Peak transient at 115K, self-corrected. Walker frozen n=3: s0=0.19, s1=1.71, s2=1.88 — all transient, no sustained CIVO.\"}}, \"exp_054_pickcube_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:47:24.310Z\", \"updated_at\": \"2026-05-23T18:08:00.000Z\", \"hypothesis\": \"PickCube frozen dt_emb baseline (fixed_dt=2, subsample ON, H=8)。验证 CIVO frozen 配置在最简单 manipulation task 上的表现。如果 eval return 稳定高于 random → frozen dt_emb 在 easy task 上不影响学习；如果性能差 → frozen dt_emb 有问题。\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 133956, \"data_path\": \"ManiSkill PickCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PickCube-v1 (online eval)\", \"log_path\": \"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.81@62500\", \"eval_final\": 10.26, \"eval_final_step\": 212500, \"ve_ratio_final\": 0.583, \"ve_ratio_final_step\": 212500}, \"exp_053_peginsertion_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:23:10.381Z\", \"updated_at\": \"2026-05-23T15:00:00.000Z\", \"hypothesis\": \"Freezing dt_emb in PegInsertionSide-v1 (contact-rich manipulation) prevents CIVO while maintaining task performance, establishing that dt_emb freezing generalizes as CIVO prevention across task domains. If frozen prevents CIVO here → extends StackCube/locomotion frozen finding to insertion tasks; if CIVO still appears → freezing insufficient for contact-rich tasks.\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 123495, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\", \"checkpoint_path\": \"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.10@52500\", \"eval_final\": 5.89, \"ve_ratio_final\": 0.202, \"ve_ratio_final_step\": 212500}, \"exp_050_peginsertion_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:38:33.441Z\", \"updated_at\": \"2026-05-23T08:51:11.592Z\", \"hypothesis\": \"Fixed-dt=2 gate with CIVO trigger on PegInsertionSide-v1 (contact-rich manipulation) will demonstrate that temporal abstraction benefits extend beyond locomotion to precise insertion tasks, where event-gated horizons can skip redundant approach phases while preserving fine-grained control near contact.\", \"spec\": {\"command\": \"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\", \"server\": \"bjb1-40020\", \"data_path\": \"ManiSkill PegInsertionSide-v1 (state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\", \"seed\": 0, \"pid\": 304736, \"gpu_ids\": [0], \"log_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\", \"checkpoint_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0\"}, \"metrics\": {\"ve_ratio_peak\": 10.05, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 0.379, \"ve_ratio_final_step\": 212500, \"civo_self_corrected\": true, \"civo_correction_delay_steps\": 130000, \"eval_final\": 20.86, \"eval_final_step\": 212500, \"eval_peak\": 20.86, \"eval_peak_step\": 212500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:30:00.000Z\"}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:30:00.000Z\", \"updated_at\": \"2026-05-23T08:48:40.404Z\", \"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks. If frozen prevents CIVO → extends Walker/Cheetah frozen finding to manipulation; if not → domain-specific factors override dt_emb mechanism.\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\", \"checkpoint_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\"}, \"metrics\": {\"ve_ratio_peak\": 4.3, \"ve_ratio_peak_step\": 42500, \"ve_ratio_final\": 0.122, \"ve_ratio_final_step\": 212500, \"eval_final\": 45.31, \"eval_final_step\": 212500, \"eval_peak\": 45.31, \"eval_peak_step\": 212500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:48:40.404Z\"}, \"exp_052_stackcube_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:26:49.825Z\", \"updated_at\": \"2026-05-23T07:45:47.966Z\", \"hypothesis\": \"StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 CIVO（ve_ratio 3.27）。如果 s1 也触发 → CIVO 在 manipulation 领域可复现，非 seed-specific；如果不触发 → seed-dependent，需更多 seeds。\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 103781, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/train.log\"}, \"metrics\": {\"eval_final\": 29.458, \"eval_final_step\": 212500, \"eval_peak\": 39.873, \"eval_peak_step\": 162500, \"ve_ratio_final\": 0.133, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.67, \"ve_ratio_peak_step\": 52500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"checkpoint_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/checkpoint_202500.pt\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/metrics.jsonl\", \"completed_at\": \"2026-05-23T07:45:47.966Z\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:14:38.578Z\", \"updated_at\": \"2026-05-23T04:23:01.339Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"parent\": \"exp_048_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_049_stackcube_civo_trigger_s0/train.log\"}, \"metrics\": {\"eval_final\": 34.88, \"eval_final_step\": 212500, \"eval_peak\": 35.89, \"eval_peak_step\": 182500, \"ve_ratio_final\": 0.186, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 5.05, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222500, \"total_episodes\": 1112}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/checkpoint_202500.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/metrics.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:23:01.339Z\"}, \"exp_048_cheetah_civo_extension\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:40.050Z\", \"updated_at\": \"2026-05-22T21:18:00.000Z\", \"hypothesis\": \"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → severity determines recoverability narrative. If it does → CIVO is universally transient regardless of severity.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}, \"metrics\": {\"eval_final\": 23.4, \"eval_final_step\": 302000, \"eval_peak\": 32.8, \"eval_peak_step\": 252000, \"ve_ratio_initial\": 46.3, \"ve_ratio_peak\": 24.112, \"ve_ratio_peak_step\": 162000, \"ve_ratio_final\": 1.803, \"nve_initial\": 70.64, \"nve_peak_secondary\": 36.76, \"nve_final\": 2.75, \"total_steps\": 312000, \"civo_self_corrected\": false, \"civo_correction_pct\": 96, \"secondary_burst_step\": 152000, \"secondary_burst_nve\": 36.47, \"gate_collapsed\": true}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/checkpoint_300000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:18:00.000Z\"}, \"exp_047_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:03:31.428Z\", \"updated_at\": \"2026-05-22T19:01:30.894Z\", \"hypothesis\": \"Frozen dt_emb Walker seed 1: 增强 exp_042 (s0, NVE=0.19) 的统计力度。 如果 s1 也 NVE<1.5 且无持续 CIVO → frozen dt_emb mitigation 跨 seed robust。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"dreamer_gated_frozen_dt_emb\", \"seed\": 1, \"eval_data\": \"dmc_walker_walk (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T18:56:07.648Z\"}, \"metrics\": {\"eval_final\": 144.22, \"eval_final_step\": 215000, \"eval_peak\": 408.79, \"eval_peak_step\": 125000, \"ve_ratio_peak\": 1.099, \"ve_ratio_peak_step\": 75000, \"ve_ratio_final\": 0.277, \"nve_peak\": 1.71, \"nve_peak_step\": 95000, \"nve_final_105k\": 0.56, \"total_steps\": 225000}, \"checkpoint_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T19:01:30.894Z\"}, \"exp_046_frozen_dt_emb_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:41:53.934Z\", \"updated_at\": \"2026-05-22T18:32:34.105Z\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"hypothesis\": \"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-22T10:42:06.985Z\", \"finished_at\": \"2026-05-22T18:27:00.000Z\"}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"seed\": 0, \"model_name\": \"dreamerv3-cheetah-frozen-dt-emb\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"metrics\": {\"eval_final\": 150.5, \"eval_peak\": 207.4, \"eval_peak_step\": 145000, \"ve_ratio_peak\": 0.4, \"ve_ratio_final\": 0.1, \"nve_peak\": 1.35, \"nve_peak_step\": 45000, \"nve_final\": 0.17, \"total_steps\": 224000, \"civo_alert_count\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:31:00.933Z\"}, \"exp_044_gradient_stop_walker\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:03:45.656Z\", \"updated_at\": \"2026-05-22T16:08:22.684Z\", \"hypothesis\": \"Reviewer Q2 直接回应：gradient stopping（detach dt_emb gradient to reward head）是否能阻断 CIVO 的 reward-critic feedback loop。基于 008d 配置（trained dt_emb + subsample ON + H=8），仅阻断 dt_emb→reward_head 梯度路径。如果 gradient stopping 有效（NVE<1.5）→ 最简干预方案成立，推翻我们之前 SGS 1/17 的结论（SGS 阻断所有梯度 vs 这里只阻断 dt_emb→reward 路径）。如果无效 → 直接证据证明 gradient-level intervention 不足以解决 CIVO，支撑 Intervention Hierarchy 中 gradient-level 最弱的结论。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"68371\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"submitted_at\": \"2026-05-22T09:08:10.295Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"DMC Walker Walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + reward_dt_emb_detach\", \"seed\": 0, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 25212.4, \"gpu_hours\": 7.0}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:04:32.082Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:04:36.793540+00:00\"}]}, \"metrics\": {\"eval_final\": 538.6, \"eval_peak\": 561.2, \"eval_peak_step\": 185000, \"eval_civo_trough\": 44.3, \"eval_civo_trough_step\": 95000, \"ve_ratio_peak\": 4.4, \"ve_ratio_peak_step\": 95000, \"ve_ratio_final\": 0.1, \"civo_onset_step\": 85000, \"civo_resolved_step\": 125000, \"civo_duration_steps\": 40000, \"total_steps\": 224000, \"pre_civo_peak\": 545.6, \"pre_civo_peak_step\": 75000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_044_gradient_stop_walker/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:08:22.684Z\"}, \"exp_045_treatment_extension_008d_s3\": {\"created_at\": \"2026-05-22T09:40:52.894Z\", \"updated_at\": \"2026-05-22T15:41:43.036Z\", \"status\": \"DONE\", \"retry_count\": 0, \"hypothesis\": \"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": \"70945\", \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_final\": 867.6, \"eval_peak\": 869.7, \"eval_peak_step\": 242000, \"nve_peak\": 4.91, \"nve_peak_step\": 132000, \"nve_final\": 0.052, \"ve_ratio_final\": 0.052, \"total_steps\": 312000, \"civo_alerts\": 0, \"civo_self_corrected\": true, \"civo_correction_step\": 142000, \"eval_trajectory\": {\"112000\": 58.5, \"122000\": 41.8, \"132000\": 35.1, \"142000\": 350.2, \"152000\": 646.4, \"162000\": 482.3, \"172000\": 600.4, \"182000\": 600.5, \"192000\": 699.5, \"202000\": 684.3, \"212000\": 758.6, \"222000\": 744.6, \"232000\": 745.4, \"242000\": 869.7, \"252000\": 721.6, \"262000\": 820.6, \"272000\": 716.2, \"282000\": 755.6, \"292000\": 843, \"302000\": 867.6}, \"ve_ratio_trajectory\": {\"122000\": 4.77, \"132000\": 4.91, \"142000\": 0.43, \"152000\": 0.21, \"162000\": 0.25, \"172000\": 0.18, \"182000\": 0.16, \"192000\": 0.13, \"202000\": 0.12, \"212000\": 0.1, \"222000\": 0.1, \"232000\": 0.09, \"242000\": 0.07, \"252000\": 0.08, \"262000\": 0.07, \"272000\": 0.08, \"282000\": 0.07, \"292000\": 0.06, \"302000\": 0.05}}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/train.log\", \"completed_at\": \"2026-05-22T15:41:43.036Z\"}, \"exp_043_008f_walker_s1\": {\"created_at\": \"2026-05-22T02:35:37.558Z\", \"hypothesis\": \"Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\"trained dt_emb → CIVO\\\"。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"model_name\": \"DreamerV3 (no dt_emb, 008f control)\", \"pid\": \"250627\", \"seed\": 1, \"server\": \"bjb1-40020\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:38:36.474Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"metrics\": {\"eval_final\": 673.73, \"eval_peak\": 673.73, \"eval_peak_step\": 215000, \"nve_peak\": 0.808, \"nve_peak_step\": 105000, \"nve_final\": 0.123, \"civo_alert\": false, \"total_steps\": 224000, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"note\": \"No CIVO (peak NVE 0.808, well below 1.5). Gate fixed at dt=2. Seed 1 replicates seed 0 finding: dt_emb absence prevents CIVO.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:38:36.474Z\"}, \"exp_042_frozen_dt_emb_walker\": {\"created_at\": \"2026-05-22T02:13:59.183Z\", \"hypothesis\": \"dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb.\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"model_name\": \"DreamerV3 + frozen dt_emb\", \"pid\": \"251336\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:29:26.337Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"metrics\": {\"eval_final\": 612.45, \"eval_peak\": 682.38, \"eval_peak_step\": 205000, \"nve_peak\": 0.194, \"nve_final\": 0.051, \"civo_alert\": false, \"total_steps\": 224000, \"total_train_episodes\": 224}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:29:26.337Z\"}, \"exp_040_wide_dual_critic_cheetah\": {\"created_at\": \"2026-05-21T19:50:49.909Z\", \"hypothesis\": \"Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\", \"pid\": \"52397\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T19:51:11.519Z\", \"submitted_via\": \"submit_training_job\", \"seed\": 1, \"wall_clock_seconds\": 49438.9, \"gpu_hours\": 13.73}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:37:44.547Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:35:07.693Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:35:10.404Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:35:14.583680+00:00\"}]}}, \"exp_041_dual_critic_walker_s3\": {\"created_at\": \"2026-05-21T19:50:54.290Z\", \"hypothesis\": \"D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\", \"pid\": \"51103\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-22T02:38:20.728Z\", \"submitted_via\": \"submit_training_job\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/checkpoint.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 23112.0, \"gpu_hours\": 6.42}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:04:44.715Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:00:53.721Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:00:58.393731+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_peak\": 761.1, \"eval_return_final\": 544, \"eval_return_peak_step\": 165000, \"nve_peak\": 1.5, \"nve_final\": 0.1, \"civo_prevented\": true, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": false, \"steps\": 215000, \"note\": \"CIVO prevented (NVE≤1.5), no non-CIVO collapse. Eval stays 486-761 after peak. Non-CIVO collapse rate confirmed 1/4 (only s2).\"}, \"completed_at\": \"2026-05-22T09:03:32.751Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\"}, \"exp_039_narrow_dual_critic_walker_s1\": {\"completed_at\": \"2026-05-22T02:35:33.617Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T16:31:40.055Z\", \"hypothesis\": \"Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\", \"metrics\": {\"civo_recovery\": true, \"eval_return_final\": 592.7, \"note\": \"Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean≈645. Recovery 2/2.\", \"nve_peak\": 2.19, \"recovery_confirmed\": true}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\"\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 10.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\", \"pid\": \"198771\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T16:31:39.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 36234.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:35:33.617Z\"}, \"exp_038_dual_critic_walker_s2\": {\"completed_at\": \"2026-05-22T02:11:36.842Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:35.293Z\", \"hypothesis\": \"Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments.\", \"metrics\": {\"civo_alert\": 0, \"civo_prevented\": true, \"eval_return_collapse\": 99.6, \"eval_return_collapse_step\": 175000, \"eval_return_final\": 120.9, \"eval_return_peak\": 354, \"eval_return_peak_step\": 155000, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": true, \"note\": \"CIVO prevented (NVE≤0.3) but non-CIVO eval collapse at 175k (354→99.6). Different failure mode from value overestimation.\", \"nve_final\": 0.248, \"nve_peak\": 0.3, \"steps\": 224000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-22T02:07:51.177Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...dual_critic walker s2...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 13.88, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\", \"model_name\": \"DreamerV3 + Dual Critic (wide)\", \"pid\": \"175633\", \"seed\": 2, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T12:18:34.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 49982.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:11:36.842Z\"}, \"exp_037_wide_critic_cheetah\": {\"completed_at\": \"2026-05-21T19:45:52.311Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:33.040Z\", \"hypothesis\": \"Wide single critic on Cheetah: if capacity=recovery generalizes from Walker (exp_033, NVE 4.75→self-repair, eval 408) to Cheetah (high CIVO, baseline NVE ~70.64), then Recovery mechanism works across CIVO severity levels. Combined with exp_034 (dual-critic Cheetah, NVE 1.75, eval 97.5), establishes that both Prevention and Recovery are environment-dependent.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 146.1, \"eval_return_peak\": 350.1, \"gate_dt_2_frac\": 1, \"nve_final\": 0.1, \"nve_peak\": 3.6, \"steps\": 224000}, \"parent\": \"exp_033_wide_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...wide_critic cheetah...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.46, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Wide Single Critic\", \"pid\": \"14487\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T12:18:32.619Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26839.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:52.311Z\"}, \"exp_036_dual_critic_pickcube\": {\"completed_at\": \"2026-05-21T19:45:31.290Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T08:43:18.481296+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T19:38:29.196731+00:00\"}]}, \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"gate_dt_2_frac\": 1, \"nve_final\": 0.2, \"nve_peak\": 2.3, \"steps\": 212447}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T19:38:24.346Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 11.03, \"gpu_id\": 0, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"2476\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T08:43:44.544357+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 39706.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:31.290Z\"}, \"exp_035_narrow_dual_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_035_narrow_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T16:11:39.130025+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:47:55.131429+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T16:08:03.906985+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect from parameter count. If CIVO suppressed → min operation itself prevents overestimation cascade. If CIVO persists → parameter count is the key factor. Combined with exp_033 (wide single critic) forms 2×2 factorial: {single,dual} × {normal,scaled} → mechanism decomposition.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"metrics\": {\"actor_entropy_final\": -0.19, \"civo_alert_window\": \"65K-85K\", \"civo_prevented\": false, \"civo_recovery\": true, \"director_override\": \"Director ruled success: CIVO recovery (33.8→697.8) is the success criterion, not prevention\", \"eval_at_215K\": 697.8, \"eval_at_85K\": 33.8, \"eval_final\": 697.8, \"eval_peak\": 697.8, \"eval_trough\": 33.8, \"nve_final\": 0.066, \"nve_peak\": 2.75, \"nve_peak_step\": 85000, \"recovery_from\": 33.8, \"recovery_to\": 697.8, \"total_steps\": 215000, \"train_return_final_range\": \"708-806\", \"v1_v2_gap_max\": 0.08, \"v1_v2_gap_typical\": 0.01}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T16:07:58.973Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T07:48:17.595Z\", \"training_hours\": 8.33}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 8.31, \"gpu_id\": 1, \"hyperparams\": {\"critic_hidden\": 256, \"critic_layers\": 2, \"critic_params_each\": 525000, \"critic_params_total\": 1050000, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"narrow_dual_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\", \"pid\": \"162900\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T07:56:05.926445+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29900.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:14:26.099Z\"}, \"exp_034\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/\", \"completed_at\": \"2026-05-21T12:18:09.552Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:17:29.760Z\", \"hypothesis\": \"Dual-critic (min of two independent critics) will prevent CIVO in Cheetah Run by providing pessimistic value estimates, as it did in Walker Walk (exp_032). If value overestimation is environment-universal, the same mechanism should work across DMC tasks.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"CIVO_prevented\": false, \"civo_trigger_steps\": [55000, 105000], \"final_NVE\": 0.144, \"final_eval_return\": 97.5, \"max_NVE\": 1.753, \"peak_eval_return\": 315.7, \"total_steps\": 215000, \"v1_v2_max_divergence\": 0.004}, \"retry_count\": 0, \"spec\": {\"command\": \"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:18:09.552Z\"}, \"exp_034_dual_critic_cheetah\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah\", \"completed_at\": \"2026-05-21T12:14:19.189109+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T05:50:59.612345+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:46.032647+00:00\"}]}, \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"baseline_eval_final\": 0.83, \"baseline_nve_peak\": 70.64, \"civo_alert_steps\": [95000, 105000], \"civo_alerts\": 2, \"civo_prevented\": false, \"dual_wave_civo\": true, \"eval_final\": 97.5, \"eval_final_step\": 215000, \"eval_peak\": 315.7, \"eval_peak_step\": 45000, \"eval_vs_peak_pct\": 31, \"gate_dt2_frac\": 1, \"gate_entropy\": 0, \"v1_v2_gap\": \"<0.2 (min operation has no pessimism effect)\", \"value_mean_final\": 14.2, \"value_mean_peak\": 60.5, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:37.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"993925\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T05:51:51.325323+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:15:03.481Z\"}, \"exp_033_wide_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"logdir/exp_033_wide_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T12:08:15.252Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T03:45:53.644963+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:31.184962+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rather than pessimistic min operation, then a single critic with 2× parameters should also suppress CIVO. If wide-critic fails (CIVO persists) but dual-critic succeeds → min operation has implicit regularization effect beyond pessimism.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"metrics\": {\"civo_alert_step\": 105000, \"civo_alert_ve_ratio\": 1.958, \"civo_instability_duration_steps\": 75000, \"critic_params\": 2886911, \"eval_reward_final\": 407.9, \"eval_reward_peak\": 194.8, \"eval_reward_trough\": 31.8, \"value_loss_final\": 1.4, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 4.7}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:26.400Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T03:46:14.882Z\", \"training_hours\": 8.27}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.25, \"gpu_id\": 0, \"hyperparams\": {\"critic_hidden\": 1024, \"critic_layers\": 2, \"critic_params\": 2886911, \"dual_critic\": false, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"wide_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"model_name\": \"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\", \"pid\": \"151860\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T03:52:59.702597+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29715.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:08:15.252Z\"}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031b_tcn_pickcube_s0_sigma05/latest.pt\", \"completed_at\": \"2026-05-21T08:43:18.481253+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:46:39.136363+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T08:41:51.310620+00:00\"}]}, \"failure_reason\": \"NVE late-stage decline is floor effect (value signal collapse), not CIVO recovery. Eval flat 25-29 throughout — agent never learned meaningful manipulation. Confirmed by Reviewer. TCN PickCube: 0/2 (σ=0.2 and σ=0.5 both failed).\", \"hypothesis\": \"PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed with NVE peak 3.71. σ=0.5 tests whether higher noise amplitude can suppress CIVO in ManiSkill PickCube. Combined with σ=0.2 data, establishes dose-response curve for robotics manipulation domain.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"metrics\": {\"eval_reward_final\": 25.5, \"eval_reward_last5_avg\": 25.9, \"eval_reward_peak\": 29.1, \"nve_final\": 0.2, \"nve_peak\": 3.3, \"nve_peak_step\": 42500, \"nve_suppressed_from_step\": 72500, \"total_episodes\": 1062, \"total_steps\": 212400}, \"parent\": \"exp_031_tcn_pickcube_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T08:41:45.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"model_name\": \"DreamerV3 + TCN σ=0.5\", \"pid\": \"968495\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T22:33:14.695383+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T08:50:22.853581+00:00\"}, \"exp_032_dual_critic_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T07:47:55.131382+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:58:31.008200+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T07:45:13.742811+00:00\"}]}, \"hypothesis\": \"Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses 008d CIVO-trigger config (trained dt_emb + multi-rate exposure). If NVE stays below 1.5× and eval matches baseline, dual-critic is an effective architecture-level intervention.\", \"metrics\": {\"baseline_eval\": 900, \"civo_prevented\": true, \"eval_final\": 739.7, \"eval_final_step\": 215000, \"eval_peak\": 787.7, \"eval_peak_step\": 205000, \"eval_vs_baseline_pct\": 87.5, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"note\": \"CIVO prevented 2/2 seeds. v1≈v2 → mechanism is implicit value regularization, not min-of-two pessimism.\", \"nve_final\": 0.1, \"nve_peak\": 1.1, \"nve_peak_step\": 95000, \"v1_v2_gap\": \"<0.1% (min operation has no pessimism effect)\"}, \"parent\": \"exp_008d_civo_trigger_s2\", \"reproduce\": {\"finished_at\": \"2026-05-21T07:45:08.395Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"pid\": \"124556\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T23:19:57.690519+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:52:13.265445+00:00\"}, \"exp_032b_dual_critic_walker_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032b_dual_critic_walker_s1/latest.pt\", \"completed_at\": \"2026-05-21T05:50:59.612299+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T23:22:08.787456+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T05:48:16.069863+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust architecture-level CIVO intervention, strengthening Intervention Hierarchy evidence.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032b_dual_critic_walker_s1.log\", \"metrics\": {\"actor_loss_late\": \"≈0 (gradient signal weak)\", \"baseline_eval\": 900, \"director_override\": \"CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.\", \"eval_criterion_pass\": false, \"eval_trajectory\": \"75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516\", \"eval_vs_baseline_pct\": 57, \"final_eval_return\": 516, \"final_nve\": 0.1, \"gate_dt2_frac\": 1.0, \"nve_criterion_pass\": true, \"nve_trajectory\": \"15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1\", \"peak_eval_return\": 551.8, \"peak_nve\": 1.4, \"total_steps\": 224000, \"total_updates\": 52599, \"training_hours\": 6.42, \"value1_value2_gap\": \"<0.5 (min operation has no pessimism effect)\"}, \"notes\": \"NVE well controlled (peak 1.4 < 1.5, no CIVO), but eval only 57% of baseline (516 vs ~900). Dual-critic suppresses value overestimation at cost of policy performance. Gate collapsed to dt=2 throughout. Two critics converge to near-identical values, min operation ineffective.\", \"parent\": \"exp_032_dual_critic_walker\", \"pid\": \"973387\", \"reproduce\": {\"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032b_dual_critic_walker_s1\\\"\", \"finished_at\": \"2026-05-21T05:48:11.173Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-20T23:22:55.338Z\", \"training_hours\": 6.42}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0}, \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"seed\": 1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:55:05.353975+00:00\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"completed_at\": \"2026-05-21T03:39:24.356918+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:33:03.633Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T03:32:52.751412+00:00\"}]}, \"failure_reason\": \"Sudden CIVO blowup: NVE appeared healthy at 95K (0.666, declining from 0.855@85K), then catastrophic spike to 3.0@105K. Eval collapsed 349.6→71.8. Late-stage NVE recovery to 0.4@215K = value adaptation (eval stayed at 104.5, never recovered). TCN σ=0.2 Walker: 2/4 seeds CIVO failure (s2: NVE 2.77, s3: NVE 3.0).\", \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443, s3=869, s4=923@105K) for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"metrics\": {\"civo_onset_step\": 105000, \"civo_pattern\": \"sudden blowup (healthy 0.67@95K → 3.0@105K)\", \"eval_final\": 104.5, \"eval_last_step\": 215000, \"eval_peak\": 349.6, \"eval_peak_step\": 95000, \"eval_return_105K\": 71.8, \"eval_return_115K\": 69.8, \"eval_return_125K\": 61.5, \"eval_return_135K\": 141.8, \"eval_return_145K\": 98.66, \"eval_return_155K\": 88.86, \"eval_return_15K\": 159.1, \"eval_return_165K\": 86.22, \"eval_return_175K\": 123.53, \"eval_return_185K\": 153.71, \"eval_return_195K\": 68.84, \"eval_return_205K\": 63.71, \"eval_return_215K\": 104.5, \"eval_return_25K\": 155.7, \"eval_return_35K\": 190.8, \"eval_return_45K\": 137.1, \"eval_return_55K\": 210.7, \"eval_return_5K\": 31.7, \"eval_return_65K\": 189.5, \"eval_return_75K\": 253.2, \"eval_return_85K\": 259.5, \"eval_return_95K\": 349.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"nve_peak\": 3.0, \"nve_peak_step\": 105000, \"step\": 224000, \"value_mean_105K\": 218.37, \"value_mean_215K\": 42.55, \"value_mean_95K\": 232.74, \"ve_ratio_105K\": 3.0, \"ve_ratio_115K\": 2.5, \"ve_ratio_125K\": 2.4, \"ve_ratio_135K\": 0.9, \"ve_ratio_145K\": 1.141, \"ve_ratio_155K\": 1.06, \"ve_ratio_165K\": 0.91, \"ve_ratio_175K\": 0.556, \"ve_ratio_185K\": 0.396, \"ve_ratio_195K\": 0.78, \"ve_ratio_205K\": 0.747, \"ve_ratio_215K\": 0.4, \"ve_ratio_45K\": 0.695, \"ve_ratio_55K\": 0.598, \"ve_ratio_65K\": 0.863, \"ve_ratio_75K\": 0.791, \"ve_ratio_85K\": 0.9, \"ve_ratio_95K\": 0.7}, \"parent\": \"exp_029b_tcn_walker_s2_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T03:32:47.021Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"pid\": \"109826\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T19:33:48.032Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:39:24.356963+00:00\"}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031_tcn_pickcube_s0_sigma02\", \"completed_at\": \"2026-05-20T23:52:48.308Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T12:09:56.923Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T23:50:00.801433+00:00\"}]}, \"hypothesis\": \"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\", \"metrics\": {\"eval_peak\": 28.6, \"eval_peak_step\": 162500, \"eval_return_132K\": 23.45, \"eval_return_152K\": 23.1, \"eval_return_192K\": 11.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0, \"step\": 195600, \"train_return_range\": \"18-25\", \"ve_ratio_latest\": 0.18, \"ve_ratio_peak\": 3.71}, \"parent\": \"exp_019b_pickcube_civo_trigger\", \"reproduce\": {\"finished_at\": \"2026-05-20T23:49:56.649Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"none(train_from_scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"data_count\": \"200000(online)\", \"data_path\": \"maniskill_PickCube-v1\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 11.17, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"908459\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 40206.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:52:48.308Z\"}, \"exp_029b_tcn_walker_s2_sigma02\": {\"completed_at\": \"2026-05-20T22:58:31.008151+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:55:13.731Z\", \"failure_reason\": \"CIVO confirmed: NVE accelerated 1.01→1.65→2.77@105K (008d-like pattern), eval collapsed 177.7→32.0. Late-stage NVE decline to 1.06@155K = value adaptation to collapsed policy, NOT CIVO self-recovery (eval remained at 56.5, never recovered). Killed at 156K to free GPU for dual-critic experiment.\", \"hypothesis\": \"TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%. Third seed resolves whether high variance is systematic or s1 is outlier.\", \"metrics\": {\"civo_onset_step\": 65000, \"eval_last_step\": 165000, \"eval_peak\": 177.67, \"eval_peak_step\": 55000, \"eval_return_105K\": 31.97, \"eval_return_115K\": 35.45, \"eval_return_125K\": 33.04, \"eval_return_135K\": 42.47, \"eval_return_145K\": 51.66, \"eval_return_155K\": 56.5, \"eval_return_15K\": 168.41, \"eval_return_165K\": 44.9, \"eval_return_25K\": 159.56, \"eval_return_35K\": 168.05, \"eval_return_45K\": 171.51, \"eval_return_55K\": 177.67, \"eval_return_5K\": 30.46, \"eval_return_65K\": 106.57, \"eval_return_75K\": 64.01, \"eval_return_85K\": 62.82, \"eval_return_95K\": 44.66, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"late_stage_nve_decline\": \"value adaptation (value_mean 108→55), not recovery (eval stayed 32-57)\", \"nve_peak\": 2.765, \"nve_peak_step\": 105000, \"step\": 168000, \"value_mean_105K\": 88.38, \"value_mean_165K\": 55.03, \"value_mean_55K\": 103.62, \"ve_ratio_105K\": 2.765, \"ve_ratio_115K\": 2.326, \"ve_ratio_125K\": 2.278, \"ve_ratio_135K\": 1.648, \"ve_ratio_145K\": 1.234, \"ve_ratio_155K\": 1.061, \"ve_ratio_15K\": 0.03, \"ve_ratio_165K\": 1.226, \"ve_ratio_25K\": 0.174, \"ve_ratio_35K\": 0.335, \"ve_ratio_45K\": 0.477, \"ve_ratio_55K\": 0.583, \"ve_ratio_65K\": 1.014, \"ve_ratio_75K\": 1.65, \"ve_ratio_85K\": 1.623, \"ve_ratio_95K\": 2.109}, \"parent\": \"exp_029a_tcn_walker_s1_sigma02\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\", \"pid\": \"75543\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T16:56:24.781Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:58:31.008195+00:00\"}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"completed_at\": \"2026-05-20T22:34:07.916411+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:26:11.800Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T22:28:30.207347+00:00\"}]}, \"hypothesis\": \"TCN σ=1.0 on Cheetah tests whether higher noise amplitude further suppresses CIVO. σ=0.5 (exp_030b) was negative with NVE peaking at 10.67@55K then declining. σ=1.0 should provide stronger temporal regularization. If NVE stays below 1.5 throughout training and eval_return ≥ baseline → TCN generalizes to Cheetah with appropriate σ scaling.\", \"metrics\": {\"baseline_eval_avg\": 548, \"eval_final\": 47.2, \"eval_peak\": 371.7, \"eval_peak_step\": 35000, \"eval_return_105K\": 122.5, \"eval_return_115K\": 162.2, \"eval_return_125K\": 148.5, \"eval_return_135K\": 138.4, \"eval_return_145K\": 100.4, \"eval_return_155K\": 144.3, \"eval_return_15K\": 87.5, \"eval_return_165K\": 130.9, \"eval_return_175K\": 66.4, \"eval_return_185K\": 47.2, \"eval_return_195K\": 56.5, \"eval_return_205K\": 49.7, \"eval_return_215K\": 47.2, \"eval_return_25K\": 166.3, \"eval_return_35K\": 371.7, \"eval_return_45K\": 144.0, \"eval_return_55K\": 266.0, \"eval_return_5K\": 8.3, \"eval_return_65K\": 197.0, \"eval_return_75K\": 107.8, \"eval_return_85K\": 95.8, \"eval_return_95K\": 72.8, \"eval_vs_baseline\": \"8.6%\", \"gate_dt2_frac\": 1.0, \"gate_dt_mean\": 2.0, \"gate_entropy\": 0.0, \"step\": 224000, \"ve_ratio_max\": 0.4}, \"parent\": \"\", \"reproduce\": {\"finished_at\": \"2026-05-20T22:28:26.022Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\", \"command\": \"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\", \"data_count\": 210000, \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\", \"model_name\": \"dreamerv3\", \"pid\": \"920968\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T16:49:48.464Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:34:07.916452+00:00\"}, \"exp_029c_tcn_walker_s0_sigma01\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:09:50.913Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T19:30:34.687287+00:00\"}]}, \"hypothesis\": \"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\", \"metrics\": {\"eval_final\": 328.3, \"eval_peak\": 490.7, \"eval_peak_step\": \"165K\", \"eval_return_105K\": 204.7, \"eval_return_115K\": 296.4, \"eval_return_125K\": 232.3, \"eval_return_135K\": 247.4, \"eval_return_145K\": 323.1, \"eval_return_155K\": 359.7, \"eval_return_15K\": 99.1, \"eval_return_165K\": 490.7, \"eval_return_175K\": 246.2, \"eval_return_185K\": 220.6, \"eval_return_195K\": 212.8, \"eval_return_205K\": 256.9, \"eval_return_215K\": 328.3, \"eval_return_25K\": 140.7, \"eval_return_35K\": 155.7, \"eval_return_45K\": 160.9, \"eval_return_55K\": 254.8, \"eval_return_5K\": 35.6, \"eval_return_65K\": 268.7, \"eval_return_75K\": 295.5, \"eval_return_85K\": 220.8, \"eval_return_95K\": 188.6, \"nve_final\": 0.1, \"nve_max\": 1.0218, \"nve_max_step\": \"95K\", \"total_steps\": 224000, \"ve_ratio_105K\": 0.761, \"ve_ratio_115K\": 0.4514, \"ve_ratio_125K\": 0.4899, \"ve_ratio_135K\": 0.3995, \"ve_ratio_145K\": 0.2667, \"ve_ratio_155K\": 0.2, \"ve_ratio_15K\": 0.0306, \"ve_ratio_165K\": 0.1, \"ve_ratio_175K\": 0.3, \"ve_ratio_185K\": 0.3, \"ve_ratio_195K\": 0.3, \"ve_ratio_205K\": 0.2, \"ve_ratio_215K\": 0.1, \"ve_ratio_25K\": 0.1606, \"ve_ratio_35K\": 0.3162, \"ve_ratio_45K\": 0.4807, \"ve_ratio_55K\": 0.4368, \"ve_ratio_65K\": 0.5432, \"ve_ratio_75K\": 0.6211, \"ve_ratio_85K\": 0.9533, \"ve_ratio_95K\": 1.0218}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T19:30:28.923Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\", \"checkpoint_source\": \"from_scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"model_name\": \"dreamer\", \"pid\": \"59395\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:53:26.097Z\"}, \"exp_029a_tcn_walker_s1_sigma02\": {\"completed_at\": \"2026-05-20T16:47:18.789Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T08:31:29.514Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T16:47:29.902718+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\", \"metrics\": {\"current_step\": 215000, \"eval_last10_mean\": 282.15, \"eval_peak\": 401, \"eval_peak_step\": \"125K\", \"eval_return_105K\": 319.4, \"eval_return_115K\": 345.5, \"eval_return_125K\": 401, \"eval_return_135K\": 307.8, \"eval_return_145K\": 380.8, \"eval_return_155K\": 307.3, \"eval_return_15K\": 137.7, \"eval_return_165K\": 320.3, \"eval_return_175K\": 159, \"eval_return_185K\": 278.2, \"eval_return_195K\": 301.2, \"eval_return_205K\": 204.6, \"eval_return_215K\": 161.3, \"eval_return_25K\": 180.9, \"eval_return_35K\": 124, \"eval_return_45K\": 124.2, \"eval_return_55K\": 133.9, \"eval_return_5K\": 36.7, \"eval_return_65K\": 169.7, \"eval_return_75K\": 171.2, \"eval_return_85K\": 151.8, \"eval_return_95K\": 180.3, \"nve_final\": 0.1864, \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_15K\": 0.0248, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007}, \"notes\": \"Cron 误报: process exited without sentinel/W&B, 但实验已正常完成 (215K/210K target). NVE max 0.6428@55K (CIVO suppressed), eval peak 401@125K (45% baseline). 对比 parent s0: s0 eval 达 baseline, s1 仅 45% → 高 seed 方差暴露 TCN 脆弱性. 结论 conclusion=success 不变.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T16:47:17.713Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"50924\", \"seed\": 1, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:53:36.867Z\"}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"completed_at\": \"2026-05-20T16:49:02.778Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:07:53.975Z\", \"hypothesis\": \"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\", \"metrics\": {\"current_step\": 195000, \"eval_return_105K\": 104.4, \"eval_return_115K\": 137.7, \"eval_return_125K\": 211.7, \"eval_return_135K\": 97.2, \"eval_return_145K\": 79.4, \"eval_return_155K\": 76.8, \"eval_return_15K\": 78.3, \"eval_return_165K\": 77.5, \"eval_return_175K\": 85.7, \"eval_return_185K\": 68.7, \"eval_return_195K\": 77.6, \"eval_return_25K\": 219.3, \"eval_return_35K\": 296.5, \"eval_return_45K\": 32.8, \"eval_return_55K\": 6, \"eval_return_5K\": 8.3, \"eval_return_65K\": 71.2, \"eval_return_75K\": 23.3, \"eval_return_85K\": 34, \"eval_return_95K\": 143.6, \"nve_final\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_15K\": 0.0202, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253}, \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:49:02.778Z\"}, \"exp_027_tcn_walker_s1\": {\"completed_at\": \"2026-05-20T12:38:02.085Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T05:51:53.479Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T12:35:42.576855+00:00\"}]}, \"hypothesis\": \"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\", \"metrics\": {\"eval_last10_mean\": 233.1, \"eval_peak\": 364.9, \"eval_peak_step\": 75000, \"eval_return\": {\"105000\": 216.7, \"115000\": 318.9, \"125000\": 309.1, \"135000\": 216.1, \"145000\": 175.4, \"15000\": 140.5, \"155000\": 171, \"165000\": 209.5, \"175000\": 120.4, \"185000\": 355.4, \"195000\": 183.3, \"205000\": 240.2, \"215000\": 350.8, \"25000\": 163.6, \"35000\": 153, \"45000\": 136.8, \"5000\": 31, \"55000\": 158.3, \"65000\": 298.5, \"75000\": 364.9, \"85000\": 134, \"95000\": 94.6}, \"nve_final\": 0.1476, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"total_steps\": 215000, \"ve_ratio\": {\"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"15000\": 0.0246, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367}}, \"parent\": \"exp_027_tcn_walker_s0\", \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:38.092Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:45:31.028Z\"}, \"exp_027_tcn_walker_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:19:31.331Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:25:32.533Z\", \"hypothesis\": \"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\", \"metrics\": {\"eval_last10_mean\": 587.1, \"eval_peak\": 821.1, \"eval_peak_step\": \"175K\", \"eval_return_105K\": 236.4, \"eval_return_115K\": 543.8, \"eval_return_125K\": 458.4, \"eval_return_135K\": 496.7, \"eval_return_145K\": 542.7, \"eval_return_155K\": 660.5, \"eval_return_15K\": 150.6, \"eval_return_165K\": 653.3, \"eval_return_175K\": 821.1, \"eval_return_185K\": 560.5, \"eval_return_195K\": 567.9, \"eval_return_205K\": 558.7, \"eval_return_215K\": 551, \"eval_return_25K\": 199.4, \"eval_return_35K\": 278.2, \"eval_return_45K\": 315.6, \"eval_return_55K\": 278.6, \"eval_return_5K\": 35.6, \"eval_return_65K\": 331, \"eval_return_75K\": 293.1, \"eval_return_85K\": 363.9, \"eval_return_95K\": 171.4, \"nve_final\": 0.0955, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"total_steps\": 215000, \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_15K\": 0.0192, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081}, \"parent\": \"exp_027_tcn_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"data_count\": 215000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:06:21.855Z\"}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:10:00.827Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T09:24:38.711Z\", \"hypothesis\": \"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\", \"metrics\": {\"current_step\": 64000, \"eval_return_35K\": 299.5, \"eval_return_55K\": 31.9, \"note\": \"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\", \"target_steps\": 210000, \"ve_ratio_55K\": 1.903}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"checkpoint_source\": \"from_scratch\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:10:00.827Z\"}, \"exp_027_tcn_walker_s0\": {\"analysis_summary\": \"TCN (σ=0.5 noise on dt_embedding) FAILED to suppress CIVO. NVE breached 1.5× threshold 3 times: 55K(1.68×), 65K(1.54×), 85K(3.97×). Peak NVE 3.97× at 85K is HIGHER than typical CIVO, suggesting TCN destabilizes value learning. Eval peaked at 240 (35K), then collapsed to avg 117 in latter half — far below 450 target. Gate remained fixed at dt=2 throughout (zero entropy). The noise magnitude was insufficient to decorrelate critic estimates from dt conditioning. Training reached 120K/210K planned. Hypothesis falsified: forward-pass noise at σ=0.5 does not prevent critic from exploiting dt-specific value structure.\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s0/latest.pt\", \"completed_at\": \"2026-05-20T09:24:09.016Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:51.820Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T06:06:34.898602+00:00\"}]}, \"hypothesis\": \"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"metrics\": {\"eval_return_105K\": 95.5, \"eval_return_112K\": 99.5, \"eval_return_15K\": 154.6, \"eval_return_25K\": 223.6, \"eval_return_35K\": 240, \"eval_return_45K\": 101.2, \"eval_return_55K\": 70, \"eval_return_5K\": 37.4, \"eval_return_65K\": 95.1, \"eval_return_75K\": 189.2, \"eval_return_85K\": 36, \"eval_return_95K\": 166.4, \"final_step\": 120000, \"gate_dt_entropy\": 0, \"gate_dt_mean\": 2, \"last_5_eval_avg\": 117.3, \"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"peak_eval\": 240, \"peak_eval_step\": \"35K\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.916, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T06:06:30.806Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"pid\": \"888715\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11433.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:24:09.016Z\"}, \"exp_028_rave_walker_s0_ceil15\": {\"completed_at\": \"2026-05-20T08:31:12.389Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T03:25:34.045Z\", \"hypothesis\": \"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\", \"metrics\": {\"current_step\": 135000, \"eval_return_105K\": 76.2, \"eval_return_115K\": 41.2, \"eval_return_125K\": 36.6, \"eval_return_135K\": 39.1, \"eval_return_15K\": 99.4, \"eval_return_25K\": 155.3, \"eval_return_35K\": 180.1, \"eval_return_45K\": 166.9, \"eval_return_55K\": 131, \"eval_return_5K\": 31.6, \"eval_return_65K\": 91.5, \"eval_return_75K\": 120.9, \"eval_return_85K\": 137.3, \"eval_return_95K\": 70.2, \"target_steps\": 210000, \"ve_ratio_105K\": 0.984, \"ve_ratio_115K\": 1.513, \"ve_ratio_125K\": 1.462, \"ve_ratio_135K\": 1.171, \"ve_ratio_15K\": 0.03, \"ve_ratio_25K\": 0.128, \"ve_ratio_35K\": 0.247, \"ve_ratio_45K\": 0.428, \"ve_ratio_55K\": 0.737, \"ve_ratio_65K\": 1.294, \"ve_ratio_75K\": 0.937, \"ve_ratio_85K\": 0.727, \"ve_ratio_95K\": 1.28}, \"parent\": \"exp_028_rave_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"model_name\": \"dreamerv3_rave_ceil15\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\", \"pid\": \"38372\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:31:12.389Z\"}, \"exp_028_rave_walker_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/checkpoint.ckpt\", \"completed_at\": \"2026-05-20T06:14:31.720Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:53.882Z\", \"hypothesis\": \"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/\", \"metrics\": {\"current_steps\": 105000, \"eval_trajectory\": {\"105K\": {\"eval_return\": 29, \"value_mean\": 92.2, \"ve_ratio\": 3.183}, \"15K\": {\"eval_return\": 105.3, \"value_mean\": 2.93, \"ve_ratio\": 0.028}, \"25K\": {\"eval_return\": 191.9, \"value_mean\": 24.4, \"ve_ratio\": 0.127}, \"35K\": {\"eval_return\": 204.6, \"ve_ratio\": 0.267}, \"45K\": {\"eval_return\": 197.7, \"ve_ratio\": 0.439}, \"55K\": {\"eval_return\": 193, \"ve_ratio\": 0.62}, \"5K\": {\"eval_return\": 37.4, \"value_mean\": 0.001}, \"65K\": {\"eval_return\": 79.8, \"ve_ratio\": 1.832}, \"75K\": {\"eval_return\": 44.5, \"ve_ratio\": 3.415}, \"85K\": {\"eval_return\": 57.7, \"ve_ratio\": 2.126}, \"95K\": {\"eval_return\": 25.9, \"value_mean\": 105.87, \"ve_ratio\": 4.086}}, \"note\": \"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\"}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"model_name\": \"dreamerv3_rave_ceil20\", \"pid\": \"879636\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12005.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T06:14:31.720Z\"}, \"exp_025_obs_sgs_walker_s2\": {\"completed_at\": \"2026-05-20T03:14:06.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-19T16:39:26.941Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T03:14:13.011509+00:00\"}]}, \"failure_reason\": \"Reclassified: experiment completed 224K/210K steps normally. Cron misclassified as failed due to missing W&B sentinel. Actual result is negative — obs-decoder SGS suppressed CIVO (ve_ratio 0.8-1.4) but eval collapsed to ~90 (baseline ~930).\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"metrics\": {\"eval_return_215K\": 89.6, \"target_steps\": 210000, \"train_steps_completed\": 224000, \"ve_ratio_175K\": 1.2, \"ve_ratio_185K\": 1.4, \"ve_ratio_215K\": 0.8}, \"notes\": \"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:14:07.466Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7989\", \"seed\": 2, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s2\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:17:26.061Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"completed_at\": \"2026-05-20T03:02:46.556Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:29.171Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16346\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:46.556Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"completed_at\": \"2026-05-20T03:02:43.170Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:27.608Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16208\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s0\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:43.170Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"completed_at\": \"2026-05-20T03:02:39.948Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:29.810Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"851593\", \"seed\": 4, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s4\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:39.948Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"completed_at\": \"2026-05-20T03:02:36.670Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:28.402Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"847597\", \"seed\": 3, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s3\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:36.670Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"completed_at\": \"2026-05-20T03:02:32.583Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:25.583Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7833\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:32.583Z\"}, \"exp_001_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T23:06:42.122Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:31.737Z\", \"hypothesis\": \"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\", \"metrics\": {\"convergence_mean_250k_plus\": 935, \"final_eval_return\": 938.86, \"final_step\": 520000, \"peak_eval_return\": 960.6}, \"parent\": \"exp_001_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 112000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T23:06:42.122Z\"}, \"exp_001_baseline_s3_extended\": {\"completed_at\": \"2026-05-19T21:23:44.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:30.382Z\", \"hypothesis\": \"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\", \"metrics\": {\"eval_profile\": {\"102000\": 869.03, \"112000\": 898.89, \"120000\": 898.38, \"130000\": 837.74, \"140000\": 876.64, \"15000\": 224.27, \"150000\": 899.47, \"160000\": 922.77, \"170000\": 925.77, \"180000\": 912.89, \"190000\": 915.07, \"200000\": 894.77, \"210000\": 899.79, \"220000\": 951.18, \"230000\": 930.56, \"240000\": 910.47, \"25000\": 329.99, \"250000\": 914.02, \"260000\": 931.33, \"270000\": 954.65, \"280000\": 928.01, \"290000\": 947.4, \"300000\": 853.32, \"310000\": 906.35, \"320000\": 847.16, \"330000\": 934.78, \"340000\": 921.08, \"35000\": 413.12, \"350000\": 922.63, \"360000\": 844.99, \"370000\": 911.36, \"380000\": 917.73, \"390000\": 937.21, \"400000\": 928, \"410000\": 945.88, \"420000\": 897.2, \"430000\": 949.45, \"440000\": 937.28, \"45000\": 332.69, \"450000\": 924.24, \"460000\": 967.25, \"470000\": 940.55, \"480000\": 936.24, \"490000\": 944.67, \"5000\": 42.15, \"500000\": 957.09, \"510000\": 947.68, \"55000\": 519.91, \"65000\": 667.42, \"72000\": 771.33, \"82000\": 772.88, \"92000\": 854.6}, \"final_eval_return\": 947.68, \"final_step\": 520000, \"final_train_return_avg\": 945.4}, \"parent\": \"exp_001_baseline_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s3/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s3/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_001_baseline_s3/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 120000, \"seed\": 3, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s3_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:23:44.025Z\"}, \"exp_001_baseline_s2_extended\": {\"completed_at\": \"2026-05-19T17:44:27.212Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:10:10.948Z\", \"hypothesis\": \"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\", \"metrics\": {\"eval_return_at_105K\": 443.5, \"eval_return_final\": 945.7, \"eval_return_peak\": 962.6, \"total_steps\": 512000, \"value_mean_at_105K\": 329.16, \"value_mean_plateau\": 665, \"ve_ratio_at_105K\": 0.7422, \"ve_ratio_converged_range\": \"0.69-0.77\"}, \"parent\": \"exp_001_baseline_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s2/latest.pt\", \"checkpoint_source\": \"logdir/exp_001_baseline_s2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\", \"data_count\": 0, \"data_path\": \"logdir/exp_001_baseline_s2\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s2/train_extended.log\", \"model_name\": \"dreamerv3\", \"resumed_from_step\": 112000, \"seed\": 2, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s2_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:44:27.212Z\"}, \"exp_023_cheetah_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T09:02:40.466Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T06:27:42.161Z\", \"hypothesis\": \"Cheetah Run baseline seed=4 extended to 300K. Tests whether eval drop at 194K→204K (537→302) is transient fluctuation or permanent collapse. Informs baseline stability and NVE normalization robustness.\", \"metrics\": {\"eval_302k\": 580, \"eval_peak_ext\": 642.3, \"eval_peak_ext_step\": 272000, \"note\": \"延长到 300K 确认非 collapse。eval 恢复到 642 peak@272K，200K-300K 区间震荡上行 (301-642 range)，194K→204K 骤降为 transient fluctuation。\"}, \"parent\": \"exp_023_cheetah_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_023_cheetah_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_023_cheetah_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"300000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_023_cheetah_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 212000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 300000, \"tmux_session\": \"exp_023_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:02:40.466Z\"}, \"exp_001_baseline_s4\": {\"completed_at\": \"2026-05-19T09:00:10.632Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:47:01.105Z\", \"hypothesis\": \"Walker Walk baseline seed=4. Fourth seed for 4-seed baseline CI. Tests whether s2 (443.5) is outlier or bimodal distribution (s1=915.7, s3=869.0).\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 922.8, \"peak_eval\": 922.8, \"peak_eval_step\": 105000, \"target_steps\": 105000, \"value_mean_final\": 576.1, \"ve_ratio_105k\": 0.624}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:00:10.632Z\"}, \"exp_023_cheetah_baseline_s4\": {\"completed_at\": \"2026-05-19T06:26:03.295Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:02.288Z\", \"hypothesis\": \"Cheetah Run baseline seed=4. Fourth seed for tighter eval return CI and NVE normalization robustness.\", \"metrics\": {\"current_step\": 212000, \"eval_return_194k\": 537.03, \"eval_return_204k\": 301.69, \"note\": \"Cheetah baseline s4. Large eval drop 194K→204K (537→302). ve_ratio>1 indicates value overestimation at final step.\", \"peak_eval\": 537.03, \"peak_eval_step\": 194000, \"target_steps\": 200000, \"value_mean_204k\": 339.14, \"ve_ratio_204k\": 1.124}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"200K env steps\", \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"dmc_cheetah_run eval episodes\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774033, \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:26:03.295Z\"}, \"exp_023_cheetah_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:47.459Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:49:33.229Z\", \"hypothesis\": \"Cheetah Run baseline seed=3. Extends 023a/023b/023_s2 (3 seeds) to 4 seeds for tighter eval return CI.\", \"metrics\": {\"current_step\": 204000, \"eval_return_202k\": 642.13, \"peak_eval\": 685.93, \"peak_eval_step\": 172000, \"target_steps\": 200000, \"value_mean_final\": 445.42, \"ve_ratio_final\": 0.694}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3\", \"checkpoint_source\": \"N/A\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 3 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s3\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"768897\", \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:47.459Z\"}, \"exp_001_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:45.989Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:03.635Z\", \"hypothesis\": \"Walker Walk baseline seed=3. Third seed for tighter baseline eval CI.\", \"metrics\": {\"current_step\": 120000, \"eval_return_102k\": 869.03, \"peak_eval\": 898.89, \"peak_eval_step\": 112000, \"target_steps\": 105000, \"value_mean_final\": 622.2, \"ve_ratio_final\": 0.692}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"105K env steps\", \"data_path\": \"dmc_walker_walk (online RL)\", \"eval_data\": \"dmc_walker_walk eval episodes\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774106, \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:45.989Z\"}, \"exp_023_cheetah_baseline_s2\": {\"completed_at\": \"2026-05-19T00:13:55.909Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:14.249Z\", \"hypothesis\": \"Cheetah Run baseline additional seed for tighter CI. Extends 023a/023b (2 seeds) to 3 seeds.\", \"metrics\": {\"current_step\": 205000, \"eval_return_final\": 645.4, \"note\": \"Cheetah Run baseline seed=2. Third baseline seed for NVE normalization.\", \"target_steps\": 200000}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 2 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s2\\\"\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.13, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"753786\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:05:57.478Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29278.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:13:55.909Z\"}, \"exp_008f_s4\": {\"completed_at\": \"2026-05-18T23:18:51.672Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T18:41:00.894Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 008f control (existing seeds: 1/008f, 2/009c, 3/008f_s3). C2 causal contrast robustness.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_105k\": 306.5, \"note\": \"No CIVO. No-dt-emb control seed=4. Peak NVE 1.41x @85K (transient), settles to 0.58x @105K.\", \"nve_105k\": 0.58, \"peak_eval\": 487.5, \"peak_eval_step\": 55000, \"peak_nve\": 1.41, \"peak_nve_step\": 85000}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:18:51.672Z\"}, \"exp_009c_s3\": {\"completed_at\": \"2026-05-18T21:40:10.763Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T17:12:00.539Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=3. Additional seed for 009c (seed=2 NVE 1.14x at 105K on upward trajectory); tests whether NVE rise is reproducible across independent seeds or stochastic.\", \"metrics\": {\"current_step\": 108000, \"eval_return_105k\": 311.92, \"note\": \"eval peaked at 55-65K (~457) then declined to 311.92. NVE 0.52x (no CIVO). 009c seed=2 NVE 1.14x not reproduced.\", \"nve_105k\": 0.52, \"target_steps\": 105000, \"value_mean_105k\": 120.27, \"ve_ratio_105k\": 0.386}, \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:10.762Z\"}, \"exp_001_baseline_s2\": {\"completed_at\": \"2026-05-18T21:40:09.329Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:17.571Z\", \"hypothesis\": \"Walker Walk baseline additional seed for tighter evaluation return CI.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 443.46, \"target_steps\": 105000, \"value_mean_105k\": 329.16, \"ve_ratio_105k\": 0.742}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:09.329Z\"}, \"exp_008f_s2\": {\"completed_at\": \"2026-05-18T18:41:05.369Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:16.527Z\", \"hypothesis\": \"No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.58, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754063\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:00.248Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9305.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:41:05.369Z\"}, \"exp_008a_cheetah_unexposed_s1\": {\"completed_at\": \"2026-05-18T18:20:00.278Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:13.377Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=1. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 504.38, \"nve_105k\": 0.478, \"target_steps\": 105000, \"value_mean_105k\": 156.97, \"ve_ratio_105k\": 0.3112}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:20:00.278Z\"}, \"exp_008a_cheetah_unexposed_s0\": {\"completed_at\": \"2026-05-18T18:19:58.491Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:12.052Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=0. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 532.35, \"nve_105k\": 0.49, \"target_steps\": 105000, \"value_mean_105k\": 169.98, \"ve_ratio_105k\": 0.3193}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:19:58.491Z\"}, \"exp_009c_s2\": {\"completed_at\": \"2026-05-18T17:12:05.307Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:19.850Z\", \"hypothesis\": \"No-dt-emb H=15 additional seed. 009c seed=2 showed NVE 1.14x at 105K on upward trajectory; additional seed tests if this is reproducible or stochastic.\", \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.1, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754639\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:05.850Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3959.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:12:05.307Z\"}, \"exp_008e_v3_s4\": {\"completed_at\": \"2026-05-18T11:33:57.033Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:54:56.392Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:31:45.212576+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=4. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"civo\": false, \"eval_return\": 899.3, \"nve_note\": \"Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K\", \"nve_peak\": 0.99, \"nve_peak_step\": 95000, \"ve_ratio_105k\": 0.609}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:31:41.800Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s4.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:45.880Z\"}, \"exp_008e_v3_s3\": {\"completed_at\": \"2026-05-18T11:24:41.197Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T02:54:54.691Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:20:58.896484+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=3. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"actor_entropy_final\": -4.892, \"collapse_onset\": \"85K-95K\", \"eval_return\": 92.7, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"nve_note\": \"Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02\", \"nve_peak\": 4.02, \"nve_peak_step\": 105000, \"peak_eval\": 520.4, \"peak_step\": 85000, \"ve_ratio_105k\": 2.635}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:20:55.020Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s3.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:43.665Z\"}, \"exp_008a_unexposed_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/latest.pt\", \"completed_at\": \"2026-05-18T08:16:42.716Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:56.020Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:12:12.866455+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=1. 直接复现 008a_no_subsample_dt2 配置（eval=778, V-recovery, no CIVO）。C3 reproducibility rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.0028, \"civo_ve_ratio_final\": 0.43, \"eval_return_15k\": 167.12, \"eval_return_25k\": 139.94, \"eval_return_35k\": 394.15, \"eval_return_45k\": 414.32, \"eval_return_55k\": 441.48, \"eval_return_5k\": 31, \"eval_return_65k\": 491.74, \"eval_return_75k\": 452.34, \"eval_return_85k\": 546.82, \"eval_return_95k\": 628.57, \"eval_return_final\": 630.91, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 272.13, \"total_steps\": 105000, \"value_mean_final\": 271.36}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:12:09.402Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk (online RL)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724312\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:15:06.654Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10896.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:16:42.716Z\"}, \"exp_008a_unexposed_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/latest.pt\", \"completed_at\": \"2026-05-18T08:10:06.059Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:57.340Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:07:33.602043+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.003, \"civo_ve_ratio_final\": 0.333, \"eval_return_55k\": 607.5, \"eval_return_65k\": 653.8, \"eval_return_75k\": 534.4, \"eval_return_85k\": 605.4, \"eval_return_95k\": 819.4, \"eval_return_final\": 899.4, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"value_mean_final\": 299.4}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:07:27.087Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.84, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724965\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10239.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:10:17.263Z\"}, \"exp_008d_civo_trigger_s4\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/latest.pt\", \"completed_at\": \"2026-05-18T05:17:45.132Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:43.972Z\", \"hypothesis\": \"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/metrics.jsonl\", \"metrics\": {\"civo_alert_105K\": 1, \"civo_confirmed\": true, \"delta_ve_105K\": 2.05, \"eval_return_trajectory\": {\"105K\": 63.6, \"15K\": 171.4, \"25K\": 189.5, \"35K\": 153.8, \"45K\": 158.2, \"55K\": 229.3, \"5K\": 30.9, \"65K\": 333.6, \"75K\": 302.4, \"85K\": 383.3, \"95K\": 240.3}, \"final_eval_return_105K\": 63.6, \"final_step\": 112000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 383.3, \"peak_eval_step\": 85000, \"target_step\": 105000, \"value_mean_105K\": 192.65, \"value_mean_95K\": 235.42, \"ve_ratio_105K\": 3.03}, \"parent\": \"exp_008d_civo_trigger_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 4 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s4\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk_online\", \"gpu\": \"cuda:0\", \"model_name\": \"DreamerV3-walker-civo-trigger\", \"pid\": \"715124\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:17:45.132Z\"}, \"exp_008a_untrained_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:51.398Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：C3 rebuttal 应复现 008a (unexposed trained dt_emb, subsample OFF) 而非 015b (frozen)。替换为 exp_008a_unexposed_s1/s2。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_008a_untrained_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:53.011Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：同上。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\", \"completed_at\": \"2026-05-18T05:11:15.900Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:47.702Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + H=8. 第二 seed 复现 Cheetah CIVO (NVE>1.5×)，加强跨环境因果论证统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/metrics.jsonl\", \"metrics\": {\"civo\": true, \"civo_onset_step\": \"65K\", \"detector_alert_step\": \"95K\", \"eval_return_105K\": 0.83, \"eval_return_peak\": 247.77, \"eval_return_peak_step\": \"35K\", \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"nve_105K\": 70.64, \"nve_95K\": 6.34}, \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run (online RL)\", \"gpu\": \"cuda:1\", \"model_name\": \"DreamerV3-cheetah-civo-trigger\", \"pid\": \"715412\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:11:15.900Z\"}, \"exp_024b_cheetah_no_dt_emb_s0\": {\"completed_at\": \"2026-05-18T02:00:15.236Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:50:34.104Z\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角。\", \"metrics\": {\"civo\": false, \"eval_return_final\": 96.5, \"nve_peak\": 0.2}, \"notes\": \"No CIVO (NVE peak <0.2×). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. eval 96.5 = 17.6% of baseline (548.3). Cheetah causal triangle seed 1 complete. Director confirmed results in D089.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s0/latest.pt\", \"checkpoint_source\": \"N/A-training-from-scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run-online-eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s0.log\", \"model_name\": \"DreamerV3-cheetah-no-dt-emb\", \"pid\": \"705742\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:15.808Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11279.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:00:17.832Z\"}, \"exp_024b_cheetah_no_dt_emb_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-18T01:56:17.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:51:53.604Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T01:52:09.175571+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb 是 Cheetah CIVO 必要条件），加强因果三角的统计力度。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"metrics\": {\"baseline_pct\": 14.1, \"civo\": false, \"eval_return_final\": 77.3, \"eval_return_peak\": 129.6, \"gate_dt_2_frac\": 1, \"nve_peak\": 0.1, \"peak_step\": 15000}, \"notes\": \"No CIVO (NVE peak 0.10×, civo_alert=0 throughout). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. Gate locked at dt=2 (gate_dt_2_frac=1.0), eval 77.3 = 14% of baseline (548.3). Low performance expected: dt_embed_dim=0 removes temporal abstraction capability. Cheetah causal triangle seed 2 complete.\", \"parent\": \"exp_024_cheetah_no_dt_emb_s0\", \"pid\": \"706158\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-18T01:52:05.296Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/latest.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"pid\": \"706158\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:30.631Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11026.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:56:17.025Z\"}, \"exp_024_cheetah_no_dt_emb_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T20:35:13.253Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T20:34:13.657Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T20:35:16.021173+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T22:57:54.400584+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角（023a/b baseline健康 + 010b CIVO collapse + 本实验 no-emb 健康）。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:57:48.608Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL)\", \"model_name\": \"DreamerV3-no-dt-emb\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:21:27.867Z\"}, \"exp_021_full_sgs_cheetah_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T22:49:15.021Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T20:24:30.695Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T22:45:35.442053+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE 8.63×, collapse)。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"metrics\": {\"baseline_pct\": 38.7, \"civo\": true, \"civo_type\": \"transient_self_correcting\", \"eval_return_final\": 221.5, \"nve_peak\": 9.94, \"nve_peak_step\": \"45K\", \"nve_sustained_55K_105K\": 0.338, \"vs_010b\": \"221.5 vs 51.7 (4.3x better)\"}, \"notes\": \"P0 priority (D070 最重要数据缺口). 018_s2 完成后立即上 cuda:0. 排序: 021 先 → 008d_s1 后. Director 2026-05-16 确认.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"pid\": \"696201\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:45:32.093Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T19:28:08.484Z\", \"training_hours\": 3.29}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_021_full_sgs_cheetah_s1/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.32, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"pid\": \"696201\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T19:30:02.581Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11952.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T22:57:30.295Z\"}, \"exp_023a_cheetah_baseline_s0\": {\"completed_at\": \"2026-05-17T20:34:04.841Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:19.690Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T20:31:37.915652+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate). Establishes Cheetah-specific baseline for NVE normalization and cross-environment validation. Comparison target for 010b (Cheetah CIVO trigger, NVE 8.27×).\", \"metrics\": {\"civo\": false, \"eval_return_final\": 624.7, \"eval_return_peak\": 624.7, \"peak_step\": 205000}, \"notes\": \"Healthy baseline. Last-5 eval mean=554.4. 185K瞬态VE spike(0.906)触发警报但20K步内恢复(205K:624.7)，非CIVO。双seed baseline均值: last-5=548.3, peak=598.8。未接W&B。\", \"reproduce\": {\"finished_at\": \"2026-05-17T20:31:34.777Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023a_cheetah_baseline_s0/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023a_cheetah_baseline_s0.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.66, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023a_cheetah_baseline_s0.log\", \"model_name\": \"DreamerV3\", \"pid\": \"683708\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T14:54:17.553Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20387.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:57.147Z\"}, \"exp_010b_cheetah_civo_trigger\": {\"completed_at\": \"2026-05-16T16:16:00.478Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:04:55.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T16:11:35.101384+00:00\"}]}, \"hypothesis\": \"Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO (NVE>1.5x)。若成立→回应 reviewer \\\"single environment\\\" concern。\", \"metrics\": {\"civo\": true, \"eval_return_final\": 51.7, \"eval_return_peak\": 321.9, \"nve_peak\": 8.27, \"nve_peak_step\": 65000, \"peak_step\": 35000}, \"parent\": \"exp_010a_cheetah_baseline_s1\", \"reproduce\": {\"finished_at\": \"2026-05-16T16:11:32.766Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger/latest.pt\", \"checkpoint_source\": \"N/A (training from scratch, parent is baseline reference)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dm_control cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL, not eval experiment)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010b_cheetah_civo_trigger.log\", \"model_name\": \"DreamerV3+dt_emb(trained)+subsample+H8\", \"pid\": \"585826\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:05:10.473Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11450.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:38.129Z\"}, \"exp_023b_cheetah_baseline_s1\": {\"completed_at\": \"2026-05-17T19:29:52.643Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:21.197Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T19:25:39.255677+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate), seed=1. Second seed for Cheetah baseline to establish robust NVE normalization across seeds.\", \"metrics\": {\"civo\": false, \"eval_return_final\": 520.3, \"eval_return_peak\": 572.9, \"peak_step\": 195000, \"ve_ratio_range\": \"0.5-0.7\"}, \"notes\": \"Healthy baseline. Last-5 eval mean=542.2 (for NVE normalization). 125K后进入500-573区间震荡，无collapse。待023a完成后取双seed均值作为Cheetah baseline。未接W&B，数据在本地logdir。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:25:34.295Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023b_cheetah_baseline_s1/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023b_cheetah_baseline_s1.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.5, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023b_cheetah_baseline_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"680126\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T13:59:45.409Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19807.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:46.627Z\"}, \"exp_019b_pickcube_civo_trigger\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019b_pickcube_civo_trigger/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:35:47.561Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:23:51.568Z\", \"error_summary\": \"KeyError in dreamer.py:421 — configs[\\\"maniskill\\\"] not found. Config block missing from dreamer.py.\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T03:35:50.727034+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T14:49:42.379952+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-17 04:01: Registry shows DONE(failed) from first attempt (KeyError transient). Actual state: RUNNING (PID 646809, step 8400+, started 11:39 UTC). Cron monitoring via submit_on_allocated tmux session. Will need manual status correction when cron detects completion.\"}}, \"failure_reason\": \"Traceback → Traceback (most recent call last): File \\\"/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py\\\", line 421, in &lt;module> recursive_update(defaults, configs[name]) ~~~~~~~^^^^^^ KeyError: 'maniskill'\", \"gpu\": \"cuda:0\", \"hypothesis\": \"PickCube-v1 CIVO trigger — trained dt_emb, subsample ON, dt=2 imagination, H=8. 预期触发 CIVO（trained dt_emb → NVE>1.5x → collapse），验证 CIVO 在 manipulation 环境是否成立\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019b_pickcube_civo_trigger.log\", \"metrics\": {\"baseline_eval_final\": 58.56, \"baseline_ratio\": 0.455, \"eval_return_final\": 26.64, \"eval_return_peak\": 26.9, \"eval_return_peak_step\": 132500, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"nve_final\": 0.065, \"nve_peak\": 3.78, \"nve_peak_step\": 52500, \"pattern\": \"transient_civo_then_value_collapse\", \"total_steps\": 200000, \"value_baseline_final\": 144.57, \"value_mean_final\": 4.26}, \"notes\": \"Cross-env CIVO confirmation + detector TN. Raw V/E peak=5.66 @52.5K (NVE=3.78× vs baseline). Transient CIVO: onset ~22.5K → peak 52.5K → deflation → eval partial recovery. Detector correctly doesn't trigger (oscillating V/E, max streak=2 < threshold=3). Eval final 26.64 vs baseline 58.56 = 45.5%. Value permanently collapsed (4.26 vs baseline 144.57). PickCube pattern: acute crisis + permanent damage, vs Walker sustained escalation.\", \"parent\": \"exp_019a_v2_pickcube_baseline\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 1 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_019b_pickcube_civo_trigger\\\"\", \"finished_at\": \"2026-05-17T14:49:39.328Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T03:25:03.091Z\", \"training_hours\": 11.41}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_ID=0 bash scripts/exp_019b_pickcube_civo_trigger.sh\", \"data_count\": \"online\", \"data_path\": \"maniskill_PickCube-v1 (state-based, online RL)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu_id\": \"cuda:0\", \"model_name\": \"DreamerV3 + trained dt_emb + gate (maniskill_state config)\", \"pid\": 649577, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T15:20:38.182Z\"}, \"exp_022b_no_curriculum\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022b_no_curriculum/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T14:01:23.413Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:49:08.181Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T13:56:29.726988+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) + learned gate WITHOUT curriculum (phase1=0, phase2=0, gate fully unlocked from step 0). Tests whether frozen dt_emb prevents CIVO (NVE < 1.5×) while allowing the gate to learn meaningful temporal abstraction (gate_dt_1_frac < 1.0). exp_022 was inconclusive because curriculum locked gate for the entire run; this rerun removes that confound.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"metrics\": {\"civo_alert_max\": 0, \"eval_return_105K\": 300.7, \"gate_dt_1_frac_105K\": 0.145, \"gate_dt_mean_105K\": 3.41, \"gate_entropy_ratio_105K\": 0.912, \"gate_near_uniform\": true, \"nve_peak\": 1.22, \"ve_ratio_105K\": 0.075, \"ve_ratio_peak\": 0.218}, \"notes\": \"Frozen dt_emb (random init, no gradients) successfully prevents CIVO: ve_ratio peaked 0.218 (NVE≈1.22×), civo_alert=0 throughout. Confirms C2 (trained dt_emb is necessary for CIVO). Gate converges to near-uniform distribution (entropy_ratio=0.912, no temporal coherence), eval_return=300.7 (32.8% of baseline@105K=915.7). Frozen random dt_emb is sufficient CIVO fix but insufficient for meaningful temporal abstraction — multi-rate imagination's inherent performance limitation.\", \"parent\": \"exp_022_untrained_dt_emb_learned_gate\", \"pid\": \"670554\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"finished_at\": \"2026-05-17T13:56:27.483Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.16, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"pid\": \"670554\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T10:51:56.898Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11366.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:20:12.115Z\"}, \"exp_022_untrained_dt_emb_learned_gate\": {\"completed_at\": \"2026-05-17T07:44:38.596Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T04:16:57.150Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T07:44:42.334281+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T10:47:17.307752+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Config error: used --configs dmc_vision (CNN+image, wrong modality) instead of dmc_proprio, and --compile True (torch.compile inductor crash). Killed and resubmitting with correct config.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) prevents CIVO by blocking the trained-embedding-driven value overestimation feedback loop, while the learned gate (Gumbel-softmax, receives gradients) retains adaptive horizon selection capability. If successful, this decouples temporal abstraction benefits from CIVO vulnerability.\", \"metrics\": {\"civo_alert\": 0, \"civo_ve_ratio_105K\": 0.4, \"eval_return_105K\": 189.1, \"eval_return_65K\": 493.1, \"eval_return_75K\": 573.8, \"final_eval_return\": 189.1, \"gate_collapsed\": true, \"gate_dt_1_frac\": 1, \"gate_entropy\": 0, \"peak_eval_return\": 573.8, \"train_return_112K\": 91.8}, \"notes\": \"INCONCLUSIVE: Gate never activated due to curriculum misconfiguration. phase1=50000 × action_repeat=2 = 100K logger steps, experiment only 105K total. gate_scale reached only 0.006, gate locked at dt=1 entire run. eval_return: 75K=573.8 → 105K=189.1 (collapsed without gate involvement). Rerun as exp_022b with curriculum disabled.\", \"parent\": \"exp_008f_s3_no_dt_embed_walker + exp_005_gate_arch (combines safe dt_emb from 008f with gate architecture from 005 series)\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:47:12.534Z\"}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022_untrained_dt_emb_learned_gate/checkpoint.ckpt\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --imag_horizon 8 --logdir ./logdir/exp_022_untrained_dt_emb_learned_gate\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, proprio obs)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022_untrained_dt_emb_learned_gate.log\", \"model_name\": \"DreamerV3 + frozen dt_emb (d=32) + learned gate (Gumbel-softmax)\", \"pid\": 661595, \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T07:47:20.391Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10901.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:56:34.274Z\"}, \"exp_019a_v2_pickcube_baseline\": {\"completed_at\": \"2026-05-16T21:07:12.193Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T20:12:22.372Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\"}}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Vanilla DreamerV3 on ManiSkill3 PickCube establishes a cross-environment baseline; if stable, subsequent CIVO trigger experiment (019b) can test whether CIVO generalizes beyond DMC Walker Walk.\", \"metrics\": {\"eval_return_final\": 69.43, \"eval_return_peak\": 69.7, \"eval_return_peak_step\": 162500, \"steps_completed\": 200248, \"value_mean_final\": 143.4, \"ve_ratio_final\": 2.07, \"ve_ratio_range\": \"1.05-3.56\"}, \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\", \"parent\": \"exp_001_baseline\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline/checkpoint.ckpt\", \"checkpoint_source\": \"auto-resume from logdir\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled False --seed 1 --steps 200000 --compile False --device cuda:1 --logdir ./logdir/exp_019a_v2_pickcube_baseline\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill3 PickCube-v1 (online RL)\", \"eval_data\": \"N/A - training experiment\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline\", \"model_name\": \"DreamerV3-S\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:44:41.396Z\"}, \"exp_007_fixed_dt4\": {\"account\": \"root\", \"checkpoint_path\": \"N/A - killed, dt=4 confirmed too coarse for locomotion (D013)\", \"completed_at\": \"2026-05-13T22:32:00.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T22:15:44.218Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T22:32:01.413690+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\"}}, \"failure_reason\": \"dt=4 confirmed too coarse for locomotion: eval_return 127@35K vs baseline 389 (-67.4%). model_loss comparable to baseline — RSSM can learn 4-step dynamics, but action temporal resolution too coarse for Walker Walk. Confirms dt sweet spot ∈ {1,2}. See D013.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。\", \"metrics\": {\"baseline_45K\": 443, \"eval_return_15K\": 129.6, \"eval_return_25K\": 176.9, \"eval_return_35K\": 126.7, \"eval_return_45K\": 144.41, \"eval_return_55K\": 152.49, \"eval_return_5K\": 31, \"model_loss_15K\": 6.337, \"model_loss_25K\": 5.089, \"model_loss_35K\": 4.755, \"model_loss_5K\": 17.927, \"peak_return\": 176.9, \"peak_step\": \"25K\", \"step\": 48000, \"trend\": \"peak 176.9@25K, low plateau ~127-152; value extremely suppressed (v/e 6-13%), NOT delusional critic but severe learning failure\", \"value_eval_ratio_45K\": 0.126, \"value_eval_ratio_55K\": 0.061, \"value_mean_45K\": 18.26, \"value_mean_55K\": 9.28, \"vs_baseline_45K\": \"-67.4%\"}, \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\", \"parent\": \"exp_006_fixed_dt2\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"finished_at\": \"2026-05-13T22:32:00.443Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v2_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt4_v2_s1\", \"model_name\": \"DreamerV3+FixedDt4 (gate_fixed_dt=4, no learned gate, init_dt fix applied)\", \"pid\": \"90354\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.869Z\"}, \"exp_008c_no_subsample_dt2_h8\": {\"completed_at\": \"2026-05-14T04:09:46.829Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T01:33:31.413Z\", \"hypothesis\": \"隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。\", \"metrics\": {\"actor_loss_55K\": -0.082, \"actor_loss_65K\": -0.053, \"baseline_65K\": 616, \"data_source_35K\": \"from training logs metrics.jsonl\", \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.55, \"eval_return_55K\": 241.87, \"eval_return_65K\": 240.86, \"step\": 68000, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_35K\": 0.218, \"value_eval_ratio_55K\": 0.291, \"value_eval_ratio_65K\": 0.328, \"value_mean_35K\": 40.43, \"value_mean_55K\": 70.32, \"value_mean_65K\": 78.96, \"verdict_65K\": \"PLATEAU\", \"vs_baseline_65K\": \"-60.9%\"}, \"parent\": \"exp_006_fixed_dt2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008c_fixed_dt2_no_subsample_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.53, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=1, imag_horizon=8)\", \"pid\": \"107021\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:47.540Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9119.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.359Z\"}, \"exp_003_event_gated_v2\": {\"completed_at\": \"2026-05-13T09:58:31.673Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T04:52:22.660Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T09:58:32.493437+00:00\"}]}, \"failure_reason\": \"Return 崩塌至 baseline 13%。根因：_imagine 中 gate dt 无约束（输出 dt∈{1,...,8}），而 subsample curriculum 限制训练数据 dt≤effective_max_dt。RSSM 对未训练的大 dt 预测为噪声，progressive poisoning 导致 actor/critic 不可恢复。需修复 dt clipping + logits masking 后从头训练。\", \"metrics\": {\"eval_return_105K\": 92.3, \"eval_return_115K\": 118.7, \"fps\": 6.52, \"gate_dt_1_frac_116K\": 0.218, \"gate_dt_mean_116K\": 2.67, \"gate_dt_std_116K\": 1.46, \"gate_empirical_entropy_116K\": 1.655, \"gate_entropy_ratio_116K\": 0.796, \"gate_scale_116K\": 0.61, \"mvp_C1_return\": \"FAIL (0.13)\", \"mvp_C2_entropy\": \"PASS (1.655)\", \"mvp_C3_heff\": \"PASS (2.667x)\", \"mvp_C4_structure\": \"PASS (autocorr=0.652)\", \"return_ratio_105K\": 0.1, \"return_ratio_115K\": 0.13, \"step\": 120000}, \"parent\": \"exp_001_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-13T09:58:31.205Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"logdir/event_gated_s1_v2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1_v2 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Subsample curriculum prevents early destabilization while event gate learns meaningful variable-rate stepping\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v2 (final fix: env step sync + threshold 25K/75K)\", \"pid\": 27009, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:35.459Z\"}, \"exp_004_event_gated_v3\": {\"completed_at\": \"2026-05-13T15:23:26.384Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T10:05:16.227Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:27.393422+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_15K\": 153.86, \"fps\": 8.1, \"gate_dt_mean_15K\": 1, \"gate_scale_15K\": 0, \"step\": 20000}}}, \"failure_reason\": \"gate_loss 爆炸 bug：compute_gate_targets 使用 gate_max_dt=8 生成 target 分布但 logits masking 使用 effective_max_dt，cross-entropy loss ≈ 3e8。eval_return@125K=352 vs baseline@335K=942，ratio=0.37。第三次 train/imagine distribution mismatch。\", \"hypothesis\": \"修复 imagination dt 约束后（logits masking + clamp safety net），event gate 在 train/imagine 分布同步条件下能产生有意义的 variable-rate stepping 且 return ≥ 80% baseline\", \"parent\": \"exp_003_event_gated_v2\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A - killed due to gate_loss explosion bug\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v4_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.19, \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v4_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v3 (dt clipping + logits masking + dt alignment fix)\", \"pid\": 36645, \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T10:12:04.157Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:34.482Z\"}, \"exp_005_event_gated_v4\": {\"checkpoint_path\": \"N/A - killed due to structural failure of hard Gumbel gate\", \"completed_at\": \"2026-05-13T22:15:21.359Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T16:08:06.061Z\", \"failure_reason\": \"Hard Gumbel gate 结构性失败。3轮 bug 修复后仍崩塌：eval_return 峰值 541.18@55K → 持续下降 → 98.84@145K（baseline 同期 950.9）。Gate 机制有效（entropy/H_eff/structure 全 PASS），但 hard categorical gate + variable-rate imagination 与 actor-critic 优化存在结构性冲突。gate_scale>0.5 后 return 不可恢复。\", \"hypothesis\": \"Event-gated adaptive horizon (learned gate activation for dt selection) improves sample efficiency over fixed-horizon DreamerV3 by dynamically extending imagination when beneficial.\", \"latest_metrics\": {\"alert\": \"return_declining_at_phase2_onset\", \"baseline_at_65K\": 615.9, \"checked_at\": \"2026-05-13\", \"eval_return\": 465.67, \"eval_return_trajectory\": {\"15K\": 153.9, \"25K\": 254.2, \"35K\": 290.8, \"45K\": 443, \"55K\": 541.2, \"5K\": 31, \"65K\": 465.7}, \"fps\": 6.69, \"gap_vs_baseline\": -150.2, \"gate_dt_1_frac\": 0.965, \"gate_dt_2_frac\": 0.035, \"gate_dt_mean\": 1.035, \"gate_dt_std\": 0.036, \"gate_empirical_entropy\": 0.0499, \"gate_entropy_bonus\": 0.0865, \"gate_entropy_ratio\": 0.072, \"gate_loss\": 0.00663, \"gate_scale\": 0.10004, \"phase2_status\": \"gate刚进入phase2 (gate_scale=0.1), dt=1占比96.5%, gate几乎未激活。eval_return在55K→65K出现14%下降(541→466), 与phase2启动时机吻合, 类似exp_003崩塌前兆。但baseline同期也有小幅回调(626→616, -1.6%), 且gate尚未真正激活, 需继续观察75K数据确认是正常波动还是collapse。\", \"pid\": 51721, \"prev_eval_return\": 541.18, \"process_status\": \"running\", \"step\": 65000, \"train_return_latest\": 569.8, \"train_return_range\": [535.4, 602.1], \"uptime\": \"2h31m\"}, \"metrics\": {\"baseline_at_145K\": \"~950\", \"eval_return_105K\": 276.08, \"eval_return_145K\": 98.84, \"eval_return_15K\": 153.9, \"eval_return_35K\": 290.8, \"eval_return_55K\": 541.18, \"eval_return_5K\": 31, \"eval_return_65K\": 465.67, \"eval_return_85K\": 212.34, \"final_return\": 98.84, \"fps\": 6.69, \"gate_dt_mean_105K\": 2.054, \"gate_dt_std_105K\": 0.907, \"gate_entropy_105K\": 1.255, \"gate_scale_105K\": 0.5, \"note\": \"85K/105K metrics corrected from 319.3/337.8 to 212.34/276.08\", \"peak_return\": 541.18, \"peak_step\": \"55K\", \"return_ratio_final\": 0.104, \"step\": 145000}, \"parent\": \"exp_004_event_gated_v3\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 6.12, \"hypothesis\": \"修复 gate_target/masking 维度不匹配 + effective_max_dt 单一来源架构 + 全量审计后，event gate return >= 80% baseline\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_005_event_gated_v4.log\", \"model_name\": \"DreamerV3+EventGate_v4\", \"pid\": \"51721\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T16:08:11.913Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 22029.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:33.514Z\"}, \"exp_008d_civo_trigger_s3\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s3/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:24:26.004Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T00:25:47.784Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T03:18:40.430236+00:00\"}]}, \"hypothesis\": \"Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming CIVO onset is systematic across seeds regardless of replay sampling sequence (seed bug fix verification).\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"metrics\": {\"baseline_eval_105K\": 915.67, \"collapse_onset_step\": 95000, \"collapse_type\": \"late-onset\", \"eval_return_final\": 267.6, \"eval_return_final_step\": 105000, \"eval_return_peak\": 451.7, \"eval_return_peak_step\": 95000, \"nve_final\": 1.53, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.5, \"nve_peak\": 1.53, \"nve_peak_step\": 105000, \"nve_sustained_45K_55K\": true, \"total_steps\": 112000, \"train_return_final_avg\": 138, \"train_return_final_range\": \"82-214\", \"value_mean_final\": 268.4, \"vs_baseline_105K\": \"-70.8%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:18:37.221Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint, new logdir)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 3 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s3\\\"\", \"data_count\": 105000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"635744\", \"seed\": 3, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T00:25:59.245Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10706.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:24:26.004Z\"}, \"exp_018v2_full_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018v2_full_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-16T17:24:44.481Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T13:42:15.786Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T17:17:46.576638+00:00\"}]}, \"hypothesis\": \"Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways creating dt-specific representations, thereby preventing CIVO onset and collapse.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"metrics\": {\"civo_reduction_pct\": 79, \"eval_return_final\": 448.3, \"eval_return_final_step\": 105000, \"eval_return_peak\": 499.6, \"eval_return_peak_step\": 75000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"late_collapse_detected\": true, \"late_collapse_step\": 112000, \"nve_final\": 1.34, \"nve_mean_45k_105k\": 1.23, \"nve_peak\": 1.66, \"nve_peak_step\": 95000, \"total_steps\": 112000, \"total_updates\": 25099, \"value_loss_final\": 0.6}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-16T17:17:44.050Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (training from scratch, parent is predecessor not checkpoint source)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 1 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018v2_full_sgs_walker_s1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, no static dataset)\", \"eval_data\": \"dmc_walker_walk eval episodes (online)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.49, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"589564\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:55:10.231Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12574.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:18.423Z\"}, \"exp_008d_subsample_on_h8\": {\"completed_at\": \"2026-05-14T04:50:52.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:46:57.960Z\", \"hypothesis\": \"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\", \"metrics\": {\"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"baseline_35K\": 400, \"baseline_45K\": 443, \"data_source_45K\": \"from training logs metrics.jsonl\", \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"step\": 55000, \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\"}, \"parent\": \"exp_005_event_gated_v4\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008d_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.48, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8)\", \"pid\": \"109519\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T02:21:59.852Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8932.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:04.661Z\"}, \"exp_018_full_sgs_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_s2/checkpoint.pt\", \"completed_at\": \"2026-05-16T23:47:49.458Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T19:33:26.266Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mechanism for deployment.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"notes\": \"CIVO collapse confirmed: eval 40.8@105K (from peak ~488@75K). NVE peaked 1.66× at 95K (35K+ window). Full-SGS did NOT prevent collapse in seed 2 — contradicts 018v2 (seed 1) which avoided collapse. This invalidates SGS_full as a reliable CIVO prevention method. Key difference from 018v2: 018_s2 collapsed while 018v2 sustained. n=2 for SGS_full now shows collapse_rate=0.5.\", \"parent\": \"exp_018v2_full_sgs_walker_s1\", \"pid\": \"612876\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.04, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"pid\": \"612876\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T19:45:40.838Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 14528.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:37.385Z\"}, \"exp_009b_008d_walker_s2\": {\"account\": \"root\", \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 1 sustained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x→2.09x→4.12x) and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold (at 35K+ steps) is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009b_008d_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T18:51:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:25.186Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T18:47:21.873692+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"CIVO onset (NVE≥1.5×) reproduces on seed=2 with identical architecture, confirming the phenomenon is systematic rather than seed-specific. Collapse outcome may be stochastic.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009b_008d_walker_s2.log\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 0 sustained nve>1.5x across 4 consecutive checkpoints and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 39.27, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0, \"ve_ratio\": 0}, {\"baseline_ve\": null, \"eval_return\": 144.31, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 4.47, \"ve_ratio\": 0.031}, {\"baseline_ve\": 0.087, \"eval_return\": 141.12, \"normalized_ve\": 2.05, \"step\": 25000, \"value_mean\": 25.14, \"ve_ratio\": 0.178}, {\"baseline_ve\": 0.241, \"eval_return\": 164.14, \"normalized_ve\": 1.24, \"step\": 35000, \"value_mean\": 49.02, \"ve_ratio\": 0.299}, {\"baseline_ve\": 0.331, \"eval_return\": 141.04, \"normalized_ve\": 1.62, \"step\": 45000, \"value_mean\": 75.59, \"ve_ratio\": 0.536}, {\"baseline_ve\": 0.404, \"eval_return\": 172.33, \"normalized_ve\": 1.41, \"step\": 55000, \"value_mean\": 98.28, \"ve_ratio\": 0.57}, {\"baseline_ve\": 0.563, \"eval_return\": 209.16, \"normalized_ve\": 0.94, \"step\": 65000, \"value_mean\": 110.91, \"ve_ratio\": 0.53}, {\"baseline_ve\": 0.719, \"eval_return\": 197.46, \"normalized_ve\": 0.66, \"step\": 75000, \"value_mean\": 93.49, \"ve_ratio\": 0.474}, {\"baseline_ve\": 0.701, \"eval_return\": 236.49, \"normalized_ve\": 0.51, \"step\": 85000, \"value_mean\": 83.86, \"ve_ratio\": 0.355}, {\"baseline_ve\": 0.632, \"eval_return\": 278.54, \"normalized_ve\": 0.43, \"step\": 95000, \"value_mean\": 75.72, \"ve_ratio\": 0.272}, {\"baseline_ve\": 0.656, \"eval_return\": 267.93, \"normalized_ve\": 0.38, \"step\": 105000, \"value_mean\": 67.27, \"ve_ratio\": 0.251}], \"target_steps\": 105000, \"trend\": \"Eval rising throughout: 39→144→141→164→141→172→209→197→236→279→268. Value peaks at 110.91@65K then self-corrects downward to 67.27@105K. v/e ratio peaks 0.57@55K then monotonically declines to 0.25@105K. NO delusional critic collapse — value self-corrects while eval improves.\", \"verdict\": \"NEGATIVE — hypothesis was to replicate collapse, collapse NOT reproduced. However, pathological nve>1.5x episode confirmed (2.05x@25K, 1.62x@45K), consistent with trained dt_emb inducing pathological overestimation. Self-correction to 0.38x@105K distinguishes from seed 0's sustained overestimation → collapse.\", \"vs_baseline_105K\": \"-70.8%\"}, \"notes\": \"D032: Collapse NOT reproduced in seed 2. nve peaked 2.05x@25K (transient) then self-corrected to 0.38x@105K. Eval rose to 268. Contrast: seed 1 had SUSTAINED nve>1.5x at 35K+ (1.71x→2.09x→4.12x) → collapse to 83. Key finding: nve>1.5x threshold (35K+ steps) is reliable trained dt_emb marker (2/2 seeds), but collapse is stochastic (1/2). Framing proposal submitted to Director.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"887053\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-14T18:47:20.636Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, trained dt_embed)\", \"seed\": 2, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:34.989Z\"}, \"exp_008f_no_dt_embed_subsample_on_h8\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8/latest.pt\", \"completed_at\": \"2026-05-14T09:32:53.461Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:51:27.592Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:30:42.170428+00:00\"}]}, \"hypothesis\": \"Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as the necessary causal factor for CIVO.\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"trained dt_embedding → value overestimation → actor exploitation → collapse. Without dt_embedding, value self-corrects.\", \"current_step\": 105000, \"eval_checkpoints\": {\"105K\": {\"eval_return\": 503, \"normalized_ve\": 0.3, \"value_mean\": 98.2}, \"15K\": {\"eval_return\": 182.03, \"value_mean\": 2.989, \"ve_ratio\": 0.01642}, \"25K\": {\"baseline_ve\": 0.087, \"eval_return\": 196.78, \"normalized_ve\": 1.02, \"value_mean\": 17.507, \"ve_ratio\": 0.089}, \"35K\": {\"baseline_ve\": 0.241, \"eval_return\": 206.67, \"normalized_ve\": 0.73, \"value_mean\": 36.279, \"ve_ratio\": 0.176}, \"45K\": {\"baseline_ve\": 0.331, \"eval_return\": 194.08, \"normalized_ve\": 0.83, \"value_mean\": 53.429, \"ve_ratio\": 0.275}, \"55K\": {\"baseline_ve\": 0.404, \"eval_return\": 173.45, \"normalized_ve\": 0.97, \"value_mean\": 67.899, \"ve_ratio\": 0.391}, \"5K\": {\"eval_return\": 30.49, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, \"65K\": {\"eval_return\": 375, \"normalized_ve\": 0.37}, \"75K\": {\"eval_return\": 324, \"normalized_ve\": 0.42}, \"85K\": {\"eval_return\": 246, \"normalized_ve\": 0.65, \"value_mean\": 111.8}, \"95K\": {\"eval_return\": 319, \"normalized_ve\": 0.54}}, \"last_updated\": \"2026-05-14T09:50:00\", \"target_steps\": 105000, \"trend\": \"Zigzag recovery with high variance: eval 207→194→173@55K→375→324→246→319→503@105K. NOT a clean V-shape — high inter-eval variance throughout. Value self-corrected: peaked 111.8@85K then declined to 98.2@105K. Normalized v/e: 0.97x@55K→0.37x@65K→0.65x@85K→0.30x@105K. Key contrast with 008d: value only accelerates (69.3%@45K) vs 008f value self-corrects.\", \"verdict\": \"SUCCESS - zigzag recovery to 503@105K, normalized v/e=0.30x, C2 confirmed\", \"vs_baseline_105K\": \"-45.1%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:30:41.254Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_embed_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.68, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"pid\": \"127761\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:51:55.020Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16858.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:33.517Z\"}, \"exp_016d_sgs_walker_s1\": {\"completed_at\": \"2026-05-15T19:35:10.508Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:29:41.130Z\", \"failure_reason\": \"Same hang as 016c — SummaryWriter.flush() deadlock after add_video with moviepy 2.x. try/except insufficient because flush() blocks on incomplete async video encode. Fix: Logger.video() → no-op.\", \"hypothesis\": \"Selective Gradient Stopping (reward_dt_emb_detach) blocks reward-gradient pathway to dt_emb, preventing CIVO-inducing co-adaptation while preserving task performance.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"第5次启动。两项修复生效：MUJOCO_EGL_DEVICE_ID=1 + logger.video注释。旧PID 526153已自行退出。\", \"pid\": 526939, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:28.152Z\"}, \"exp_001_baseline\": {\"completed_at\": \"2026-05-13T15:23:24.593Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T02:09:53.875Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:25.663340+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:47:19.804301+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_205K\": 907.1, \"eval_return_215K\": 919.8, \"fps\": 8.3, \"step\": 245000, \"train_return_244K\": \"935-976\"}}}, \"failure_reason\": \"误报：cron 检测到进程退出但实际是正常完成（512K步）。已核实 checkpoint 229MB 有效。\", \"hypothesis\": \"Vanilla DreamerV3 on Walker Walk converges to stable high-return policy (>900) within 500K steps, establishing the performance ceiling for all gated variants.\", \"latest_metrics\": {\"checked_at\": \"2026-05-13\", \"eta_hours\": 1.8, \"eval_return\": 953.37, \"eval_step\": 445000, \"fps\": 7.29, \"pid\": 9409, \"prev_eval_return\": 964.96, \"process_status\": \"running\", \"step\": 452000, \"steps_remaining\": 48000, \"train_return_latest\": 958.07, \"train_return_range\": [917, 985.8], \"uptime\": \"16h35m\"}, \"metrics\": {\"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_last10_mean\": 950.9, \"eval_return_peak\": 970.41, \"eval_return_peak_step\": 505000, \"eval_trajectory\": {\"105K\": 915.67, \"115K\": 919.81, \"125K\": 921.37, \"135K\": 900, \"145K\": 932.16, \"155K\": 933.34, \"15K\": 206.61, \"165K\": 907.98, \"175K\": 918.87, \"185K\": 954.69, \"195K\": 936.09, \"205K\": 949.24, \"215K\": 913.4, \"225K\": 962.44, \"235K\": 937.24, \"245K\": 934.42, \"255K\": 948.45, \"25K\": 395.27, \"265K\": 925.09, \"275K\": 931.51, \"285K\": 925.75, \"295K\": 936.3, \"305K\": 939.33, \"315K\": 948.42, \"325K\": 967.75, \"335K\": 942.41, \"345K\": 969.83, \"355K\": 941.11, \"35K\": 388.47, \"365K\": 935.76, \"375K\": 918.24, \"385K\": 937.98, \"395K\": 955.38, \"405K\": 937.83, \"415K\": 948.99, \"425K\": 954.64, \"435K\": 964.96, \"445K\": 953.37, \"455K\": 945.84, \"45K\": 513.77, \"465K\": 947.81, \"475K\": 947.66, \"485K\": 930.6, \"495K\": 944.73, \"505K\": 970.41, \"55K\": 625.73, \"5K\": 31.77, \"65K\": 615.86, \"75K\": 596.28, \"85K\": 713.93, \"95K\": 871.06}, \"final\": true, \"step\": 512000, \"value_eval_ratio_105K\": 0.656, \"value_eval_ratio_25K\": 0.087, \"value_eval_ratio_35K\": 0.241, \"value_eval_ratio_45K\": 0.331, \"value_eval_ratio_55K\": 0.404, \"value_eval_ratio_65K\": 0.563, \"value_eval_ratio_75K\": 0.719, \"value_eval_ratio_85K\": 0.701, \"value_eval_ratio_95K\": 0.632, \"value_eval_ratio_stable\": \"~69-72% from 135K+\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:47:18.966Z\"}, \"retry_count\": 1, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"hypothesis\": \"DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"pid\": 9409, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:24.099Z\"}, \"exp_008d_civo_trigger_s2\": {\"completed_at\": \"2026-05-17T00:24:10.180Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T19:32:16.790Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 bootstrap CI 闭合 trained_dt_emb condition (现有: seed 0 = 008d, seed 2 = 009b)。注意: 原名 s2 但实际需跑 seed=1 (避免与 009b seed=2 重复)。\", \"notes\": \"Killed by Director order: seed bug confirmed. --seed 1 was parsed incorrectly, producing bit-for-bit identical results to seed=0. PID 628482 killed. Will resubmit after seed bug fix with seed=3.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint loaded)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/event-gated-adaptive-horizon && python train.py --configs dmc_vision --task dmc_walker_walk --logdir ./logdir/008d_civo_trigger_s2 --seed 1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --steps 120000\", \"data_count\": 120000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.57, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s2.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"628477\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T22:49:55.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 5654.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T00:24:10.180Z\"}, \"exp_008f_s3_no_dt_embed_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_s3_no_dt_embed_walker/checkpoint.ckpt\", \"completed_at\": \"2026-05-16T20:09:51.135Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:04:28.878Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=2，需 ≥3）。预期 NVE<1.5×，无 CIVO。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"metrics\": {\"collapse\": false, \"eval_return_final\": 363.8, \"nve_peak\": \"< 1.5x\"}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"601233\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"pid\": \"601233\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T17:21:24.538Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10106.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:09:51.135Z\"}, \"exp_020_vanilla_dreamerv3_s2\": {\"completed_at\": \"2026-05-16T19:43:57.604Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:23:55.837Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T19:40:49.938571+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Vanilla DreamerV3 (no dt_emb, no subsample, no gate) seed 2 — Pathway B 控制实验：验证 008e_v3_s2 的 eval-driven collapse 是否需要 trained dt_emb 作为必要条件。如果 vanilla s2 稳定 → C6 成立 (trained dt_emb 是 Pathway B 必要条件)。如果也崩溃 → Pathway B 是 DreamerV3 inherent fragility。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"metrics\": {\"collapse\": false, \"comparison_with_parent\": {\"c6_confirmed\": true, \"delta\": \"vanilla stable (836.5) vs trained dt_emb collapsed (136.96)\", \"parent_collapsed\": true, \"parent_eval_105K\": 136.96, \"parent_id\": \"exp_008e_v3_walker_s2\", \"parent_nve_105K\": 3.78}, \"eval_trajectory\": [{\"eval_return\": 41.2, \"step\": 5000}, {\"eval_return\": 534.1, \"step\": 55000}, {\"eval_return\": 688.9, \"step\": 65000}, {\"eval_return\": 596.2, \"step\": 95000}, {\"eval_return\": 836.5, \"step\": 105000}], \"final_eval_return\": 836.5, \"final_value_mean\": 539.3, \"peak_eval_return\": 836.5, \"peak_eval_step\": 105000, \"train_return_range_108K\": \"511-808\", \"ve_ratio_105K\": 0.645}, \"notes\": \"Pathway B 控制实验 (D6)。vanilla config: dt_embed_dim=0, subsample OFF, H=15, seed=2, 105K steps, Walker Walk。排队等 010b 完成后在 cuda:0 提交。命令: dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 2 --compile True --device cuda:0 --imag_horizon 15\", \"parent\": \"exp_008e_v3_walker_s2\", \"pid\": \"596344\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-16T19:40:47.795Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"logdir/exp_020_vanilla_dreamerv3_s2/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"pid\": \"596344\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T16:45:55.371Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:43:57.604Z\"}, \"exp_019a_pickcube_baseline\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T13:43:00.745Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T03:23:50.639Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中的适用性\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"notes\": \"ManiSkill3 Phase 1. 排队等 cuda:1 (010a 完成后). --compile False --device cuda:1. maniskill_state config.\", \"pid\": \"586751\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T12:00:04.473Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (killed before completion)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.37, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"pid\": \"586751\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:20:56.230Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1324.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:43:00.745Z\"}, \"exp_018_full_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T12:43:09.226Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T23:30:39.991Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T12:40:17.132664+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerability is representation-level; if eliminated → obs decoder gradient is root cause.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_walker_s1.log\", \"metrics\": {\"eval_return_final\": 915.7, \"eval_return_final_step\": 105000, \"eval_return_peak\": 915.7, \"eval_return_peak_step\": 105000, \"nve_peak\": 0.72, \"nve_peak_step\": 75000, \"nve_sustained_avg\": 0.55, \"nve_sustained_max\": 0.72, \"total_steps\": 112000, \"train_return_final_avg\": 899.4, \"value_mean_final\": 601.1}, \"notes\": \"⚠️ INVALID: 训练命令缺失 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8。gate_enabled=false → dt_embedding 未创建 → full_sgs 是空操作 → 实际等同 vanilla baseline。所有基于此实验的 claim (CIVO elimination, gradient-level vulnerability) 需要 018v2 重新验证。\", \"parent\": \"exp_016e_sgs_walker_s1\", \"pid\": \"577467\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_018_full_sgs_walker_s1 --steps 105000 --full_sgs True --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T12:40:14.687Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T09:50:18.238Z\", \"training_hours\": 2.83}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:42:11.339Z\"}, \"exp_010a_cheetah_baseline_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/latest.pt\", \"completed_at\": \"2026-05-16T12:01:01.080Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:27.101Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T11:59:12.312213+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log\", \"metrics\": {\"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"final_step\": 524000, \"total_eval_episodes\": 52, \"train_return_last\": 716}, \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"pid\": \"536890\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T11:59:09.914Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T22:48:05.456Z\", \"training_hours\": 13.18}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:01:11.169Z\"}, \"exp_009d_baseline_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T12:10:01.788Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:55:00.039Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:10:04.203907+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:24:17.652463+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T09:48:44.475703+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 0 — 第三独立 baseline seed，建立 v/e 校准参考（plan_010）\", \"metrics\": {\"eval_return\": 927.6, \"eval_return_at_508K\": 927.6, \"eval_return_peak\": 950.96, \"eval_return_peak_step\": 398000, \"note\": \"COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K\", \"step\": 508000}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\", \"parent\": \"exp_001_baseline\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T09:48:42.388Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T12:06:19.592Z\", \"training_hours\": 21.71}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/checkpoint.ckpt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/metrics.jsonl\", \"model_name\": \"DreamerV3_baseline\", \"pid\": \"149703\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:50:34.506Z\"}, \"exp_017_subsample_off_trained_dt_emb\": {\"completed_at\": \"2026-05-16T04:46:30.361Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T10:44:24.756Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample OFF + dt=2 imagination + H=15 seed 1 — 2×2 消融矩阵: 隔离 subsample 训练数据的因果效应。与 008a (untrained dt_emb, subsample OFF) 唯一差异是 dt_emb trained vs untrained。如果 017 崩而 008a 不崩 → 确认 trained dt_emb 是 CIVO 根因，即使训练数据全为 dt=1（plan_017, C2）\", \"notes\": \"D044: 取消。008a 配置验证确认 017 与 008a 完全重复（trained dt_emb + subsample OFF + H=15 + seed 1）。008a 的\\\"untrained\\\"含义是\\\"dt_emb 存在但未接触 dt>1 数据\\\"，不是 frozen/absent。2×2 矩阵已由 008a/008d/008f/015b 闭合。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:46:30.361Z\"}, \"016e\": {\"completed_at\": \"2026-05-16T01:39:17.916Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T22:21:09.251Z\", \"notes\": \"重复条目，权威数据在 exp_016e_sgs_walker_s1 (DONE/negative)。此条目为 NVE 诊断过程中误创建的冗余记录。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:39:17.916Z\"}, \"exp_016e_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T22:31:16.457Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T19:35:20.242Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016）。第五次重试，修复 Logger.video() → no-op 彻底消除 SummaryWriter.add_video/flush 死锁\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/\", \"metrics\": {\"actor_loss_sign_flip_step\": 95000, \"civo_catastrophic_step\": 95000, \"civo_detected\": true, \"civo_nve_peak\": 10.42, \"civo_nve_peak_step\": 95000, \"civo_onset_step\": 85000, \"civo_severity\": \"catastrophic\", \"current_step\": 100000, \"data_source\": \"metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25\", \"deep_analysis\": {\"016e_vs_008d_entropy_comparison\": {\"15K\": {\"008d\": 0.481, \"016e\": 1.049, \"delta\": 0.568}, \"25K\": {\"008d\": -1.862, \"016e\": -1.554, \"delta\": 0.308}, \"35K\": {\"008d\": -3.465, \"016e\": -2.118, \"delta\": 1.347}, \"45K\": {\"008d\": -4.575, \"016e\": -3.455, \"delta\": 1.12}, \"55K\": {\"008d\": -4.879, \"016e\": -3.617, \"delta\": 1.262}, \"interpretation\": \"SGS preserves ~1.0-1.3 nats higher entropy through 35-55K, enabling better exploration\"}, \"016e_vs_008d_value_at_crash\": {\"008d\": {\"disconnect_ratio\": 1.67, \"eval_return\": 82.75, \"value_mean\": 137.88}, \"016e\": {\"disconnect_ratio\": 6.58, \"eval_return\": 31.73, \"value_mean\": 208.88}, \"interpretation\": \"016e value completely decoupled from reality; 008d still weakly correlated\"}, \"actor_loss_sign_flip\": {\"008d_min_actor_loss\": -0.073, \"008d_never_flipped\": true, \"016e_flip_step\": 95000, \"016e_flip_value\": 0.014, \"interpretation\": \"sign flip = value critic drives actor toward worse actions, triggering catastrophic collapse\"}, \"train_return_collapse_timeline\": {\"100K\": [109, 111, 102, 108], \"88K\": [140, 145, 116, 116], \"92K\": [50, 29, 34, 75], \"96K\": [86, 41, 50, 101], \"interpretation\": \"collapse visible in train_return by 92K; partial recovery by 100K but far below peak\"}}, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, {\"eval_return\": 140.3, \"step\": 15000, \"value_mean\": 3.1, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 141.75, \"nve\": 1.86, \"step\": 25000, \"value_mean\": 22.97, \"ve_ratio\": 0.162}, {\"baseline_ve\": 0.241, \"eval_return\": 173.01, \"nve\": 1.28, \"step\": 35000, \"value_mean\": 53.55, \"ve_ratio\": 0.309}, {\"baseline_ve\": 0.331, \"eval_return\": 184.03, \"nve\": 1.4, \"step\": 45000, \"value_mean\": 85.32, \"ve_ratio\": 0.464}, {\"baseline_ve\": 0.404, \"eval_return\": 153.79, \"nve\": 1.86, \"step\": 55000, \"value_mean\": 115.63, \"ve_ratio\": 0.752}, {\"baseline_ve\": 0.563, \"eval_return\": 324.3, \"nve\": 0.83, \"step\": 65000, \"value_mean\": 152.3, \"ve_ratio\": 0.469}, {\"baseline_ve\": 0.719, \"eval_return\": 326.67, \"nve\": 0.81, \"step\": 75000, \"value_mean\": 190.04, \"ve_ratio\": 0.582}, {\"baseline_ve\": 0.701, \"eval_return\": 256.21, \"nve\": 1.2, \"step\": 85000, \"value_mean\": 215.39, \"ve_ratio\": 0.841}, {\"baseline_ve\": 0.632, \"eval_return\": 31.73, \"nve\": 10.42, \"step\": 95000, \"value_mean\": 208.88, \"ve_ratio\": 6.583}], \"final_eval_return\": 31.73, \"final_eval_step\": 95000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 326.67, \"peak_eval_step\": 75000, \"reward_dt_emb_detach\": true, \"sgs_verdict\": \"SGS delays CIVO onset ~50K steps by preserving entropy, yields 2x higher peak (327 vs 167), but does NOT prevent collapse. Collapse is more severe (NVE 10.42x vs 4.12x) due to accumulated value overestimation. Root cause is value dynamics, not reward-head gradient contamination.\", \"target_steps\": 105000}, \"notes\": \"logdir 路径修正：实际数据在 logdir/exp_016e_sgs_walker_s1（非 spec 中的 exp_016d）。SGS 崩溃确认@95K: eval 31.7, ve_ratio=6.59x, NVE=10.42x。\\n\\n**⚠️ 关键发现（Full-SGS 梯度验证）：reward loss 对 dt_emb.weight 的梯度贡献为 0。016e 的 reward_dt_emb_detach 实际上是 no-op——完全无效干预。** 真正的 dt_emb 梯度来源是 decoder heads（orientations=1.11, velocity=0.90, height=0.76, cont=0.27）。016e 与 008d 的差异（onset 延迟、更高峰值）应归因于随机变异或其他实验条件差异，不是 SGS 干预效果。\\n\\nFull-SGS（detach 所有 non-KL head 梯度）移除 93% dt_emb 梯度（1.624→0.119），是真正的测试。\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016e_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"logdir\": \"logdir/exp_016e_sgs_walker_s1\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"logdir 修正: 实际数据在 exp_016e（非 016d）\", \"pid\": 527392, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:30:11.433Z\"}, \"exp_016c_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:26:05.863Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:12:09.799Z\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer). EGL fix confirmed working: eval at step 5000 completed successfully (eval_return=31.0). OOM occurred during training loop startup after eval. Likely system RAM OOM (replay buffer + model + eval concurrent memory peak).\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心。GPU 1 清理+验证通过后重启（plan_016）\", \"metrics\": {\"egl_fix_verified\": true, \"eval_return_5K\": 31, \"step\": 5000}, \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"GPU 1 cleanup + CUDA/dm_control verification passed. logdir shared with 016b (fresh start).\", \"pid\": \"524244\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:24.104Z\"}, \"exp_009h_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:08:12.013Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:03:10.534Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:08:15.731787+00:00\"}]}, \"failure_reason\": \"误杀: Director 基于 Reviewer 错误诊断下令 kill（认为 zombie PID 522009 导致 eval deadlock），但日志证明 EGL fix (MUJOCO_EGL_DEVICE_ID=1) 已生效，eval 正常运行中 (iter=500, t=95.9s)。EGL fix 确认有效。\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009g（EGL device mismatch 修复：+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009h_008f_walker_s0.log\", \"notes\": \"日志显示进程正常完成 prefill → 到达 step 5000 → eval 正在运行（500 iter, 96s, 正常产出 debug 行）→ 被外部 SIGHUP (EXIT_CODE=129) 终止。非渲染死锁，非 OOM。诊断 Worker 排查外部终止原因中。009f/009g/009h 连续 3 次失败，分别因 seed 重复、EGL mismatch、外部 SIGHUP。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"522450\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T19:08:09.836Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"note\": \"EGL fix: MUJOCO_EGL_DEVICE_ID=1 to match physical GPU 1. 008f series seeds: 1(008f), 2(009c), 0(009h)\", \"pid\": \"522450\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:18:24.685Z\"}, \"exp_016b_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:10:52.235Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:08:00.667Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:10:53.928926+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016, 论文 method section 核心）。重跑 016_sgs，修复 EGL device mismatch（+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016b_sgs_walker_s1.log\", \"notes\": \"Restarted after GPU 1 cleanup. Old PID 523536 killed during GPU reset attempt. New PID 524244. GPU 1 diagnostics: no ECC/Xid errors, reset not supported (AutoDL container) but cleanup successful. CUDA + dm_control verification passed in 3s.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 524244, \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T19:10:51.013Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"Rerun of 016_sgs with EGL fix (MUJOCO_EGL_DEVICE_ID=1). Original 016 failed due to EGL device mismatch, not SGS code issue.\", \"pid\": \"523536\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:11:46.897Z\"}, \"exp_009g_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:59:55.315Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T18:54:23.385Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:59:59.820061+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM). Root cause: MUJOCO_GL=egl defaults to EGL device 0 while CUDA_VISIBLE_DEVICES=1 binds CUDA to GPU 1, causing cross-GPU context conflict and eval deadlock at step 5000.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009f（seed=1 与 parent 008f 重复）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009g_008f_walker_s0.log\", \"notes\": \"Hung at first eval (step 5000) due to osmesa rendering deadlock in dm_control render_executor thread. Same root cause as exp_016. Fixed by switching MUJOCO_GL to egl in dreamer.py.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"517413\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:59:53.840Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"note\": \"Replaces exp_009f which had seed=1 duplicating parent 008f. 008f series seeds: 1(008f), 2(009c), 0(009g)\", \"pid\": \"517413\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:03:53.591Z\"}, \"exp_009f_008f_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:46:03.293Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:15.806Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:46:05.155411+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:52:15.790170+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Seed duplication: 009f used seed=1 same as parent 008f, producing deterministic repeat (prefill returns identical). Killed by Director order.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 1 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"516110\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:52:12.322Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T18:44:58.143Z\", \"training_hours\": 0.12}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.07, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"pid\": \"516110\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:47:48.525Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 265.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:54:04.806Z\"}, \"exp_016_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:43:52.455Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:30:32.999Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:43:57.605618+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路。预期：不崩溃，nve < 1.5x baseline；imagination dt=2/dt=1 reward ratio 从 008d 的 2.90x 大幅下降（plan_016, 论文 method section 核心）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"notes\": \"Director 调整优先级：017 先于 016。cuda:1 释放后先跑 017，017 完成后再跑 016。SGS 诊断 bug 已修复（models.py L388-417 删除），dry-run 通过。[2026-05-15 18:43] PID 514422 hung: GPU 1 利用率 0%, 显存 794 MiB, metrics.jsonl 停 step=5000 持续 2.5h+。已 kill，Worker 诊断根因+修复+重启中。\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"514417\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T18:43:51.025Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"pid\": \"514417\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:36:15.693Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 456.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:43:52.455Z\"}, \"exp_015b_frozen_dt_emb\": {\"completed_at\": \"2026-05-15T12:12:25.846Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T10:21:05.572Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T18:27:09.189680+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次提交。首次失败原因: --device cuda:1 但 CUDA_VISIBLE_DEVICES=1 后进程内只有 cuda:0。已修正为 --device cuda:0。PID 144831, 从头开始 (step=0)。预计 ~5h 完成 105K steps。\"}}, \"hypothesis\": \"Walker Walk frozen dt_emb + subsample ON + dt=2 imagination + H=8 seed 1 — 2×2 消融矩阵: 隔离 dt_emb 训练 vs 存在的因果效应。如果 freeze 后不崩 → 确认 CIVO 根因是 dt_emb 训练而非结构存在（plan_015B, D041）\", \"metrics\": {\"actor_entropy_105K\": -4.855, \"actor_loss_105K\": 0.000179, \"collapse_mechanism\": \"gradient_starvation_from_frozen_dt_emb\", \"data_source\": \"worker SSH final analysis 2026-05-15T18:30\", \"eval_return_105K\": 204.2, \"eval_return_15K\": 167.9, \"eval_return_25K\": 171.8, \"eval_return_35K\": 201.6, \"eval_return_45K\": 122.3, \"eval_return_55K\": 105.8, \"eval_return_5K\": 31, \"eval_return_65K\": 160.3, \"eval_return_75K\": 80, \"eval_return_85K\": 183.5, \"eval_return_95K\": 238.4, \"final_eval\": 204.2, \"final_step\": 112000, \"gate_dt_1_frac\": 0, \"gate_dt_mean\": 2, \"nve_105K\": 0.42, \"nve_85K\": 0.467, \"nve_95K\": 0.394, \"summary\": \"NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss→0 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence\", \"value_mean_105K\": 56.212, \"value_std_105K\": 13.818}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD + MUJOCO_GL=egl + --device cuda:0 (CUDA_VISIBLE_DEVICES=1 隔离)。cuda:1, seed=1, 105K steps ~5h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:27:07.138Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_015b_frozen_dt_emb --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_015b_frozen_dt_emb.log\", \"pid\": \"149991\", \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:38:42.380Z\"}, \"exp_008a_no_subsample_dt2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample/latest.pt\", \"completed_at\": \"2026-05-14T06:16:58.196Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:33:27.311Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T06:15:01.796655+00:00\"}]}, \"hypothesis\": \"隔离 subsample 效应：trained dt_emb (unexposed to dt>1 data due to subsample OFF) + subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。\", \"metrics\": {\"baseline_105K\": 915.67, \"baseline_55K\": 625.7, \"baseline_65K\": 616, \"data_source\": \"from training logs metrics.jsonl\", \"eval_return_105K\": 777.66, \"eval_return_35K\": 500.84, \"eval_return_45K\": 563.41, \"eval_return_55K\": 487.92, \"eval_return_65K\": 608, \"eval_return_75K\": 469.93, \"eval_return_85K\": 583.73, \"eval_return_95K\": 572.24, \"nan_count\": 0, \"normalized_ve_105K\": 0.59, \"normalized_ve_55K\": 0.93, \"normalized_ve_65K\": 0.66, \"normalized_ve_75K\": 0.75, \"normalized_ve_85K\": 0.68, \"normalized_ve_95K\": 0.79, \"step\": 112000, \"trend\": \"Two V-shaped recoveries: 501→563→488→608→470→584→572→778; v/e suppressed 38-54% (normalized 0.59-0.79x baseline); no collapse at 105K\", \"value_eval_ratio_105K\": 0.386, \"value_eval_ratio_55K\": 0.376, \"value_eval_ratio_65K\": 0.372, \"value_eval_ratio_75K\": 0.536, \"value_eval_ratio_85K\": 0.475, \"value_eval_ratio_95K\": 0.497, \"value_mean_105K\": 300.27, \"value_mean_55K\": 183.5, \"value_mean_65K\": 226.1, \"value_mean_75K\": 251.78, \"value_mean_85K\": 277.36, \"value_mean_95K\": 284.28, \"verdict_105K\": \"NEW_PEAK_V_RECOVERY\", \"verdict_65K\": \"RECOVERED_NEW_HIGH\", \"vs_baseline_105K\": \"-15.1%\", \"vs_baseline_65K\": \"-1.3%\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T06:15:00.119Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.65, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (gate_fixed_dt=2, gate_subsample_max_dt=1, H=15)\", \"pid\": \"106942\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:46.034Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16752.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:50:59.046Z\"}, \"exp_009d_baseline_walker_s1\": {\"completed_at\": \"2026-05-15T11:54:55.153Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:14.363Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 1 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"notes\": \"⚠️ seed=1 与 exp_001_baseline 相同，eval 轨迹确定性复现。不构成独立 seed。如需第三 baseline seed 应 kill 并用 --seed 0 或 --seed 3 重跑。待 Director 决策。\", \"parent\": \"exp_001_baseline\", \"pid\": 122271, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009d_baseline_walker_s1.log\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:35:00Z\", \"wall_clock_seconds\": 19195.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:54:55.153Z\"}, \"exp_009e_008d_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T11:26:52.478Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T11:09:15.367Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + H=8 seed 1 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/metrics.jsonl\", \"metrics\": {\"actor_loss_sign_flip\": 85000, \"baseline_105K\": 915.67, \"collapse_rate_note\": \"Independent rate = 1/2 (seed 1 collapsed, seed 2 self-corrected). 008d and 009e share seed=1, count as one independent observation.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0, \"ve_ratio\": 0}, {\"eval_return\": 153.7, \"step\": 15000, \"value_mean\": 3.4, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 167.2, \"normalized_ve\": 1.78, \"step\": 25000, \"value_mean\": 25.9, \"ve_ratio\": 0.155}, {\"baseline_ve\": 0.241, \"eval_return\": 146.3, \"normalized_ve\": 1.71, \"step\": 35000, \"value_mean\": 60.2, \"ve_ratio\": 0.411}, {\"baseline_ve\": 0.331, \"eval_return\": 140.8, \"normalized_ve\": 2.09, \"step\": 45000, \"value_mean\": 97.5, \"ve_ratio\": 0.693}, {\"baseline_ve\": 0.404, \"eval_return\": 82.7, \"normalized_ve\": 4.12, \"step\": 55000, \"value_mean\": 137.9, \"ve_ratio\": 1.666}, {\"baseline_ve\": 0.563, \"eval_return\": 250, \"normalized_ve\": 1.23, \"step\": 65000, \"value_mean\": 173.8, \"ve_ratio\": 0.695}, {\"baseline_ve\": 0.719, \"eval_return\": 178.1, \"normalized_ve\": 1.48, \"step\": 75000, \"value_mean\": 189.9, \"ve_ratio\": 1.066}, {\"baseline_ve\": 0.701, \"eval_return\": 201.93, \"normalized_ve\": 1.15, \"step\": 85000, \"value_mean\": 163.08, \"ve_ratio\": 0.808}, {\"baseline_ve\": 0.632, \"eval_return\": 132.79, \"normalized_ve\": 1.73, \"step\": 95000, \"value_mean\": 144.82, \"ve_ratio\": 1.091}, {\"baseline_ve\": 0.656, \"eval_return\": 131.08, \"normalized_ve\": 1.57, \"step\": 105000, \"value_mean\": 135.37, \"ve_ratio\": 1.033}], \"final_eval_return\": 131.08, \"final_nve\": 1.57, \"final_value_mean\": 135.37, \"final_ve_ratio\": 1.033, \"peak_nve\": 4.12, \"peak_nve_step\": 55000, \"target_steps\": 105000, \"vs_baseline_105K\": \"-85.7%\"}, \"notes\": \"008d extended replication (same seed=1, 009e extends 008d from 55K to 105K). Eval trajectory 5K-55K identical to 008d (deterministic). Collapse confirmed at 105K: eval 131.08, nve@55K=4.12x (normalized). 65K bounce to 250 was transient, not recovery. actor_loss flipped positive @85K. Independent collapse rate = 1/2 (seed 1 collapsed, seed 2 self-corrected), NOT 2/3 — 008d and 009e are the same seed.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 119108, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009e_008d_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.43, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009e_008d_walker_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8\", \"pid\": \"119108\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:01:00Z\", \"wall_clock_seconds\": 19552.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:31:04.722Z\"}, \"exp_009a_baseline_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:33:12.892Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:24.247Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/\", \"metrics\": {\"cross_seed_ve_stable\": \"seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72\", \"eval_return_peak\": 966.94, \"eval_return_peak_step\": 395000, \"eval_trajectory\": [{\"eval_return\": 41.21, \"step\": 5000}, {\"eval_return\": 106.01, \"step\": 15000}, {\"eval_return\": 325.33, \"step\": 25000}, {\"eval_return\": 354.49, \"step\": 35000}, {\"eval_return\": 498.01, \"step\": 45000}, {\"eval_return\": 534.13, \"step\": 55000}, {\"eval_return\": 688.87, \"step\": 65000}, {\"eval_return\": 656.85, \"step\": 75000}, {\"eval_return\": 618.73, \"step\": 85000}, {\"eval_return\": 596.24, \"step\": 95000}, {\"eval_return\": 836.51, \"step\": 105000}, {\"eval_return\": 804.79, \"step\": 115000}, {\"eval_return\": 865.48, \"step\": 125000}, {\"eval_return\": 876.08, \"step\": 135000}, {\"eval_return\": 869.18, \"step\": 145000}, {\"eval_return\": 778.99, \"step\": 155000}, {\"eval_return\": 864.03, \"step\": 165000}, {\"eval_return\": 850.53, \"step\": 175000}, {\"eval_return\": 907.31, \"step\": 185000}, {\"eval_return\": 873.49, \"step\": 195000}, {\"eval_return\": 887.02, \"step\": 205000}, {\"eval_return\": 956.04, \"step\": 215000}, {\"eval_return\": 892.09, \"step\": 225000}, {\"eval_return\": 914.78, \"step\": 235000}, {\"eval_return\": 950.32, \"step\": 245000}, {\"eval_return\": 936.9, \"step\": 255000}, {\"eval_return\": 937.27, \"step\": 265000}, {\"eval_return\": 934.78, \"step\": 275000}, {\"eval_return\": 960.2, \"step\": 285000}, {\"eval_return\": 947.46, \"step\": 295000}, {\"eval_return\": 937.8, \"step\": 305000}, {\"eval_return\": 948.66, \"step\": 315000}, {\"eval_return\": 930.61, \"step\": 325000}, {\"eval_return\": 919.23, \"step\": 335000}, {\"eval_return\": 816.18, \"step\": 345000}, {\"eval_return\": 932.45, \"step\": 355000}, {\"eval_return\": 943.13, \"step\": 365000}, {\"eval_return\": 952.86, \"step\": 375000}, {\"eval_return\": 942.31, \"step\": 385000}, {\"eval_return\": 966.94, \"step\": 395000}, {\"eval_return\": 948.01, \"step\": 405000}, {\"eval_return\": 957.06, \"step\": 415000}, {\"eval_return\": 939.37, \"step\": 425000}, {\"eval_return\": 963.65, \"step\": 435000}, {\"eval_return\": 948.42, \"step\": 445000}, {\"eval_return\": 937.72, \"step\": 455000}, {\"eval_return\": 939.54, \"step\": 465000}, {\"eval_return\": 965.94, \"step\": 475000}, {\"eval_return\": 916.74, \"step\": 485000}, {\"eval_return\": 945.58, \"step\": 495000}, {\"eval_return\": 957.87, \"step\": 505000}], \"final_eval_return\": 957.87, \"final_eval_step\": 505000, \"final_value_mean\": 665.17, \"final_ve_ratio\": 0.694, \"last10_mean\": 947.19, \"n_evals\": 51, \"total_steps\": 505000, \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 25000, \"value_mean\": 45.78}, {\"step\": 55000, \"value_mean\": 253.49}, {\"step\": 105000, \"value_mean\": 539.34}, {\"step\": 155000, \"value_mean\": 633.42}, {\"step\": 205000, \"value_mean\": 658.92}, {\"step\": 255000, \"value_mean\": 663.87}, {\"step\": 305000, \"value_mean\": 663.86}, {\"step\": 355000, \"value_mean\": 663.78}, {\"step\": 405000, \"value_mean\": 663.95}, {\"step\": 455000, \"value_mean\": 664.42}, {\"step\": 505000, \"value_mean\": 665.17}], \"ve_ratio_trajectory\": [{\"step\": 25000, \"ve\": 0.141}, {\"step\": 55000, \"ve\": 0.475}, {\"step\": 105000, \"ve\": 0.645}, {\"step\": 155000, \"ve\": 0.813}, {\"step\": 205000, \"ve\": 0.743}, {\"step\": 255000, \"ve\": 0.709}, {\"step\": 305000, \"ve\": 0.708}, {\"step\": 355000, \"ve\": 0.712}, {\"step\": 405000, \"ve\": 0.7}, {\"step\": 455000, \"ve\": 0.709}, {\"step\": 505000, \"ve\": 0.694}], \"ve_stable_range\": \"0.69-0.72 from 235K+\", \"vs_exp001_105K\": \"836.51 vs 915.67 (-8.6%)\", \"vs_exp001_final\": \"957.87 vs 970.41 (-1.3%)\", \"vs_exp001_last10\": \"947.19 vs 950.90 (-0.4%)\", \"vs_exp001_peak\": \"966.94 vs 970.41 (-0.4%)\"}, \"notes\": \"Baseline seed 2 完成。与 exp_001 (seed 0/1) 高度一致: peak 966.94 vs 970.41 (-0.4%), last10 mean 947.19 vs 950.90 (-0.4%), v/e stable 0.69-0.72 匹配。105K 处 836.51 比 seed 0/1 的 915.67 低 8.6%，但 215K+ 后完全收敛。345K 有一个 dip 到 816 但迅速恢复。baseline 跨 seed 一致性确认。\", \"pid\": \"142508\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009a_baseline_walker_s2 --steps 500000 --seed 2 --compile False --device cuda:0\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:08.969Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:33:16.385Z\"}, \"exp_008e_v3_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:00:20.816Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T14:29:53.738Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/\", \"metrics\": {\"actor_entropy_collapse_signature\": \"entropy rose from -5.21@85K to -3.83@105K (policy destabilizing during collapse)\", \"actor_entropy_trajectory\": [{\"actor_entropy\": 8.239, \"step\": 5000}, {\"actor_entropy\": 2.352, \"step\": 15000}, {\"actor_entropy\": 0.17, \"step\": 25000}, {\"actor_entropy\": -3.498, \"step\": 35000}, {\"actor_entropy\": -4.915, \"step\": 45000}, {\"actor_entropy\": -5.121, \"step\": 55000}, {\"actor_entropy\": -5.135, \"step\": 65000}, {\"actor_entropy\": -5.224, \"step\": 75000}, {\"actor_entropy\": -5.208, \"step\": 85000}, {\"actor_entropy\": -4.529, \"step\": 95000}, {\"actor_entropy\": -3.828, \"step\": 105000}], \"baseline_105K\": 915.67, \"collapse_confirmed\": \"105K (nve=3.78x, eval 715→137)\", \"collapse_onset\": \"95K (nve jumped from 0.68x to 1.34x)\", \"eval_trajectory\": [{\"eval_return\": 39.27, \"step\": 5000}, {\"eval_return\": 180.85, \"step\": 15000}, {\"eval_return\": 211.82, \"step\": 25000}, {\"eval_return\": 320.39, \"step\": 35000}, {\"eval_return\": 356.93, \"step\": 45000}, {\"eval_return\": 418.32, \"step\": 55000}, {\"eval_return\": 435.09, \"step\": 65000}, {\"eval_return\": 576.54, \"step\": 75000}, {\"eval_return\": 715.21, \"step\": 85000}, {\"eval_return\": 452.43, \"step\": 95000}, {\"eval_return\": 136.96, \"step\": 105000}], \"final_eval_return\": 136.96, \"final_nve\": 3.78, \"final_value_mean\": 339.84, \"final_ve_ratio\": 2.481, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"peak_eval_return\": 715.21, \"peak_eval_step\": 85000, \"train_return_108K\": \"19-23 (random policy level)\", \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 15000, \"value_mean\": 3.91}, {\"step\": 25000, \"value_mean\": 30.27}, {\"step\": 35000, \"value_mean\": 79.75}, {\"step\": 45000, \"value_mean\": 125.25}, {\"step\": 55000, \"value_mean\": 172.89}, {\"step\": 65000, \"value_mean\": 220.47}, {\"step\": 75000, \"value_mean\": 272.64}, {\"step\": 85000, \"value_mean\": 339.3}, {\"step\": 95000, \"value_mean\": 384.39}, {\"step\": 105000, \"value_mean\": 339.84}], \"ve_ratio_trajectory\": [{\"nve\": 1.64, \"step\": 25000, \"ve\": 0.143}, {\"nve\": 1.03, \"step\": 35000, \"ve\": 0.249}, {\"nve\": 1.06, \"step\": 45000, \"ve\": 0.351}, {\"nve\": 1.02, \"step\": 55000, \"ve\": 0.413}, {\"nve\": 0.9, \"step\": 65000, \"ve\": 0.507}, {\"nve\": 0.66, \"step\": 75000, \"ve\": 0.473}, {\"nve\": 0.68, \"step\": 85000, \"ve\": 0.474}, {\"nve\": 1.34, \"step\": 95000, \"ve\": 0.85}, {\"nve\": 3.78, \"step\": 105000, \"ve\": 2.481}], \"vs_baseline_105K\": \"-85.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"C6 seed 2 COLLAPSED. Delusional critic collapse at 85K→105K despite gate_dt_mean=1.0 locked throughout. eval peaked 715@85K then crashed to 137@105K (v/e=2.48, nve=3.78x). Cross-seed: seed 0=869.9 (healthy), seed 1=869.9 (healthy), seed 2=137 (collapsed). Collapse is stochastic (1/3 seeds) even in dt=1 imagination config. Subsample ON training data (dt=2 transitions) appears sufficient to trigger delusional critic in some seeds. Train returns at 108K=19-23 (random policy).\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"43437\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.23, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log\", \"pid\": \"43437\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T00:46:45.424Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18815.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:24:21.709Z\"}, \"exp_008e_v3_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T00:44:53.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T14:29:53.120Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/\", \"metrics\": {\"eval_trajectory\": [{\"eval_return\": 31, \"step\": 5000}, {\"eval_return\": 131.2, \"step\": 15000}, {\"eval_return\": 155.7, \"step\": 25000}, {\"eval_return\": 276.5, \"step\": 35000}, {\"eval_return\": 382.2, \"step\": 45000}, {\"eval_return\": 486.8, \"step\": 55000}, {\"eval_return\": 580.7, \"step\": 65000}, {\"eval_return\": 574.1, \"step\": 75000}, {\"eval_return\": 657.3, \"step\": 85000}, {\"eval_return\": 851.9, \"step\": 95000}, {\"eval_return\": 869.9, \"step\": 105000}], \"exit_code\": 0, \"final_eval_return\": 869.9, \"final_value_mean\": 457.9, \"gate_dt_1_frac\": 1, \"total_steps\": 112000, \"ve_ratio_105k\": 0.527}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"Crown jewel C6 seed 1 SUCCESS. eval_return=869.9@105K, v/e=0.527 (healthy, no delusional critic). Gate locked dt=1 throughout. Trajectory: 31→131→156→276→382→487→581→574→657→852→870. Consistent with seed 0, confirms trained dt_emb + dt=1 imagination is safe.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"898127\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.92, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s1.log\", \"pid\": \"898127\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T18:49:27.945Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 21325.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:44:53.439Z\"}, \"exp_006\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T00:49:02.944Z\", \"metrics\": {\"baseline_return_at_55k\": 625.7, \"deficit_pct\": -42.4, \"deficit_vs_baseline_at_55k\": -265.3, \"eval_return\": {\"15000\": 256.9, \"25000\": 321.4, \"35000\": 485.3, \"45000\": 477, \"5000\": 31, \"55000\": 360.4}, \"gate_dt_mean\": 2, \"latest_return\": 360.4, \"latest_step\": 55000, \"model_loss_at_55k\": 4.853, \"peak_return\": 485.3, \"peak_step\": 35000}, \"notes\": \"早期条目，权威数据在 exp_006_fixed_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.922Z\"}, \"exp_008a\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:07:59.793Z\", \"metrics\": {\"eval_return_15K\": 167.2, \"eval_return_25K\": 230.8, \"eval_return_35K\": 500.8, \"eval_return_45K\": 563.4, \"eval_return_55K\": 487.9, \"eval_return_5K\": 31, \"eval_return_65K\": \"pending (eval in progress)\", \"step\": 65000, \"train_return_64K_avg\": 556.6, \"trend\": \"peaked @45K=563, dipped to @55K=488, 65K eval in progress; train returns @64K healthy (~557)\", \"value_eval_ratio_55K\": \"37.6%\", \"value_mean_55K\": 183.5}, \"notes\": \"早期条目，权威数据在 exp_008a_no_subsample_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.075Z\"}, \"exp_008c\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:02.608Z\", \"metrics\": {\"eval_return_15K\": 171.3, \"eval_return_25K\": 192.4, \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.6, \"eval_return_55K\": 241.9, \"eval_return_5K\": 31, \"eval_return_65K\": 240.9, \"step\": 68000, \"train_return_68K_avg\": 245.1, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_65K\": \"32.8%\", \"value_mean_65K\": 79}, \"notes\": \"早期条目，权威数据在正式命名实验中。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:52.611Z\"}, \"exp_008d\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:05.136Z\", \"metrics\": {\"eval_return_15K\": 153.7, \"eval_return_25K\": 167.2, \"eval_return_35K\": 146.3, \"eval_return_5K\": 31, \"step\": 40000, \"train_return_40K_avg\": 119.3, \"trend\": \"declining — train_return @40K avg=119 below @35K eval=146, value/eval=41.1% not yet >50% but train performance dropping\", \"value_eval_ratio_35K\": \"41.1%\", \"value_mean_35K\": 60.2}, \"notes\": \"早期条目，权威数据在 exp_008d_subsample_on_h8。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:51.696Z\"}, \"exp_008e_v2_subsample_on_dt1_h15\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:26:39.732Z\", \"notes\": \"已被 exp_008e_v3_subsample_on_dt1_h15 取代，进程已死。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v2_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v2_subsample_on_dt1_h15.log\", \"pid\": \"125392\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:27:30.720Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:49.814Z\"}, \"exp_rssm_fidelity_analysis\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T11:09:52.237Z\", \"hypothesis\": \"RSSM prediction quality analysis: 比较 baseline/008d/008f 在 dt=1 vs dt=2 transitions 上的 obs_MSE 和 reward_MAE，量化 RSSM fidelity gap (plan_030)\", \"metrics\": {\"008d_trained_dtEmb\": {\"dt1_obs_mse\": 41.31, \"dt1_reward_mae\": 0.0568, \"dt2_obs_mse\": 53.67, \"dt2_reward_mae\": 0.1579, \"obs_gap\": 1.3, \"reward_gap\": 2.78}, \"008f_no_dtEmb\": {\"dt1_obs_mse\": 8.01, \"dt1_reward_mae\": 0.7469, \"dt2_obs_mse\": 22.04, \"dt2_reward_mae\": 0.7526, \"obs_gap\": 2.75, \"reward_gap\": 1.01}, \"baseline\": {\"dt1_obs_mse\": 13.49, \"dt1_reward_mae\": 0.0102, \"dt2_obs_mse\": 27.5, \"dt2_reward_mae\": 0.0159, \"obs_gap\": 2.04, \"reward_gap\": 1.56}}, \"notes\": \"分析实验，非训练实验。conclusion=success，状态从 PREPARING 修正为 DONE（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:48.642Z\"}, \"exp_008e_v3_subsample_on_dt1_h15\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15/latest.pt\", \"completed_at\": \"2026-05-14T09:07:47.319Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:29:31.656Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:05:44.288431+00:00\"}]}, \"hypothesis\": \"B+ confound control：subsample ON + untrained dt_emb + dt=1 imagination + H=15。验证 subsample ON 训练数据（含 dt=2 transitions）是否本身导致性能下降，即使 imagination 只用 dt=1。对照 008a（subsample OFF）和 baseline。如果 008e_v3 性能接近 baseline → subsample ON 本身无害。如果下降 → subsample ON 改变了 RSSM dynamics。\", \"metrics\": {\"baseline_105K\": 915.67, \"current_step\": 112000, \"eval_return\": {\"105K\": 869.88, \"15K\": 131.2, \"25K\": 155.69, \"35K\": 276.47, \"45K\": 382.22, \"55K\": 486.84, \"5K\": 31, \"65K\": 580.67, \"75K\": 574.09, \"85K\": 657.31, \"95K\": 851.86}, \"fps\": 7.01, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"last_updated\": \"2026-05-14T09:09:00\", \"normalized_ve\": {\"105K\": 0.8, \"25K\": 1.93, \"35K\": 0.94, \"45K\": 0.88, \"55K\": 0.87, \"65K\": 0.72, \"75K\": 0.73, \"85K\": 0.76, \"95K\": 0.75}, \"target_steps\": 105000, \"value_eval_ratio\": {\"105K\": 0.527, \"25K\": 0.168, \"35K\": 0.227, \"45K\": 0.29, \"55K\": 0.35, \"65K\": 0.405, \"75K\": 0.523, \"85K\": 0.534, \"95K\": 0.476}, \"value_mean\": {\"105K\": 457.93, \"25K\": 26.19, \"35K\": 62.76, \"45K\": 110.67, \"55K\": 170.09, \"65K\": 235.05, \"75K\": 300.51, \"85K\": 351.33, \"95K\": 405.25}, \"verdict\": \"SUCCESS - 95% baseline, normalized v/e stable 0.72-0.80x, B+ hypothesis confirmed\", \"vs_baseline_105K\": \"-5.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:05:42.563Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 4.64, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, untrained dt_emb)\", \"pid\": \"126110\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:29:31.600Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16695.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:46:00.840Z\"}, \"exp_009c_008f_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T22:15:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:26.154Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T14:15:58.982844+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_008f_walker_s2.log\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 does NOT replicate seed 1's zigzag recovery. 008f seed 1 peaked at 503@105K with rising trend; seed 2 peaked at 359@75K then declined to 148@105K. The adaptive horizon mechanism's benefit appears seed-dependent and not robust.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 30.37, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0.0013, \"ve_ratio\": null}, {\"baseline_ve\": null, \"eval_return\": 157.15, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 3.057, \"ve_ratio\": 0.019}, {\"baseline_ve\": 0.087, \"eval_return\": 168.75, \"normalized_ve\": 1.26, \"step\": 25000, \"value_mean\": 18.536, \"ve_ratio\": 0.11}, {\"baseline_ve\": 0.241, \"eval_return\": 178.94, \"normalized_ve\": 0.79, \"step\": 35000, \"value_mean\": 34.263, \"ve_ratio\": 0.191}, {\"baseline_ve\": 0.331, \"eval_return\": 211.08, \"normalized_ve\": 0.72, \"step\": 45000, \"value_mean\": 50.099, \"ve_ratio\": 0.237}, {\"baseline_ve\": 0.404, \"eval_return\": 238.91, \"normalized_ve\": 0.66, \"step\": 55000, \"value_mean\": 63.267, \"ve_ratio\": 0.265}, {\"baseline_ve\": 0.563, \"eval_return\": 244.15, \"normalized_ve\": 0.53, \"step\": 65000, \"value_mean\": 72.717, \"ve_ratio\": 0.298}, {\"baseline_ve\": 0.719, \"eval_return\": 359.14, \"normalized_ve\": 0.33, \"step\": 75000, \"value_mean\": 83.91, \"ve_ratio\": 0.234}, {\"baseline_ve\": 0.701, \"eval_return\": 227.43, \"normalized_ve\": 0.6, \"step\": 85000, \"value_mean\": 96.071, \"ve_ratio\": 0.422}, {\"baseline_ve\": 0.632, \"eval_return\": 190.94, \"normalized_ve\": 0.9, \"step\": 95000, \"value_mean\": 108.29, \"ve_ratio\": 0.567}, {\"baseline_ve\": 0.656, \"eval_return\": 148.34, \"normalized_ve\": 1.14, \"step\": 105000, \"value_mean\": 111.247, \"ve_ratio\": 0.75}], \"target_steps\": 105000, \"trend\": \"Peak 359@75K then monotonic decline to 148@105K; no recovery pattern unlike 008f seed 1's zigzag recovery to 503\", \"verdict\": \"NEGATIVE - no delusional critic (normalized v/e < 1.5x) but persistent decline after 75K; cross-seed consistency with 008f seed 1 NOT confirmed\", \"vs_baseline_105K\": \"-83.8%\"}, \"notes\": \"D031 排期修正: 009c 延长 200K 降优先级，排在 009e/009f 之后。cuda:1 排期: 009b → 008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。105K 指标: eval=148.34, value=111.25, nve=1.14x。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"140980\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_008f_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-14T14:15:57.425Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:10.835Z\", \"training_hours\": 6.95}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:34:24.161Z\"}, \"exp_006_fixed_dt2\": {\"account\": \"root\", \"completed_at\": \"2026-05-14T01:13:11.533Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T21:10:58.851Z\", \"extra\": {\"audit_commit\": \"6159e46\", \"bugs_fixed\": \"_effective_max_dt not synced in fixed_dt mode; hardcoded curriculum phases ignoring config\", \"curriculum_audit\": \"Curriculum does NOT apply in fixed_dt mode (models.py:200-205). gate_fixed_dt>0 bypasses _update_gate_schedule(). subsample_variable_dt receives effective_max_dt=2.0 from step 0, training data is 58.5% dt=1 + 41.5% dt=2 throughout. Actual train/imagine mismatch: mixed dt training vs pure dt=2 imagination.\"}, \"gpu\": \"cuda:0\", \"hypothesis\": \"诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。\", \"latest_metrics\": {\"checked_at\": \"2026-05-14\", \"eval_return\": 485.3, \"eval_return_trajectory\": {\"15K\": 256.9, \"25K\": 321.4, \"35K\": 485.3, \"5K\": 31}, \"eval_step\": 35000, \"fps\": 6.6, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"grad_norm\": 8.6, \"pid\": 85029, \"prev_eval_return\": 321.4, \"process_status\": \"running\", \"step\": 36000}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_006_fixed_dt2.log\", \"metrics\": {\"baseline_35K\": 388.5, \"baseline_45K\": 513.8, \"baseline_55K\": 625.7, \"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_15K\": 256.9, \"eval_return_25K\": 321.4, \"eval_return_35K\": 485.3, \"eval_return_45K\": 477, \"eval_return_55K\": 360.4, \"eval_return_5K\": 31, \"eval_return_65K\": 132.86, \"fps\": 6.5, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"model_loss_15K\": 7.593, \"model_loss_25K\": 5.633, \"model_loss_35K\": 5.229, \"model_loss_45K\": 5.023, \"model_loss_55K\": 4.9, \"model_loss_5K\": 20.738, \"peak_return\": 485.3, \"peak_step\": \"35K\", \"step\": 65000, \"trend\": \"inverted-V: peak 485@35K, collapsing to 133@65K; v/e accelerating: 31.1%→53.3%→93.3%→272% (value 2.7x eval_return at 65K)\", \"value_eval_ratio_35K\": 0.311, \"value_eval_ratio_45K\": 0.533, \"value_eval_ratio_55K\": 0.933, \"value_eval_ratio_65K\": 2.722, \"value_mean_35K\": 151.1, \"value_mean_45K\": 254.29, \"value_mean_55K\": 336.44, \"value_mean_65K\": 361.69, \"vs_baseline_55K\": \"-42.4%\"}, \"parent\": \"exp_005_event_gated_v4\", \"pid\": \"85029\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-13T22:12:00.446Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"N/A - negative result, fixed dt=2 collapsed to 132.9@65K (21.6% baseline)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"failure_reason\": \"fixed dt=2 崩塌：训练分布混合（58.5% dt=1 + 41.5% dt=2 log-uniform）+ 想象纯 dt=2 条件下，eval_return 从 peak 485@35K 持续下降至 132.9@65K（baseline 同期 615.9）。与 learned gate 变体一致的崩塌模式。代码审计确认 curriculum 不生效（gate_fixed_dt>0 跳过 _update_gate_schedule）。\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt2_v1_s1\", \"model_name\": \"DreamerV3+FixedDt2 (gate_fixed_dt=2, no learned gate)\", \"pid\": \"85029\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T10:20:11.722Z\"}, \"exp_008e_subsample_on_fixed_dt1\": {\"checkpoint_path\": \"N/A - killed, duplicate registry entry, logdir contaminated by dual-process write\", \"completed_at\": \"2026-05-14T04:21:47.956Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:07.303Z\", \"failure_reason\": \"重复 registry 条目 + logdir 被两个进程交叉写入导致 tfevents/metrics.jsonl 损坏。Director 指令清理后以 exp_008e_subsample_on_dt1_h15 为准重跑。\", \"hypothesis\": \"验证 Reviewer D020 因果假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（delusional critic），即使 actor 不用 dt=2 imagination。对照：008a (subsample OFF, dt=2 imag) value/eval=37.6%@55K vs exp_006 (subsample ON, dt=2 imag) 53.3%。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.19, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"121636\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:22.915Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 685.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:58.056Z\"}, \"exp_008e_subsample_on_dt1_h15\": {\"checkpoint_path\": \"N/A - killed, logdir contaminated by duplicate process cross-write\", \"completed_at\": \"2026-05-14T04:21:48.584Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:37.655Z\", \"hypothesis\": \"验证 Reviewer D020 delusional critic 假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（即使 actor 不用 dt=2 imagination）。对照：008a（subsample OFF，dt=2 imagination）和 006（subsample ON，dt=2 imagination）。\", \"notes\": \"重复进程：与 exp_008e_subsample_on_fixed_dt1 命令完全相同，共享同一 logdir，导致 tfevents 文件互相污染。Kill PID 122038，保留 PID 121636。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.18, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"122038\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:46.045Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 662.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:57.658Z\"}, \"exp_002_event_gated\": {\"completed_at\": \"2026-05-13T04:50:14.987Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T02:09:54.240Z\", \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"kill_reason\": \"Phase 1 subsample 设计缺陷：subsample_variable_dt 在 Phase 1 (gate_scale=0) 也生效，RSSM 用 variable-Δt 数据训练但 imagination 只用 Δt=1，return 恶化到 baseline 的 25%。手动 kill 后部署 subsample curriculum 补丁并重启为 exp_003。\", \"retry_count\": 0, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1 --steps 500000 --seed 1 --compile False --device cuda:1 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM (K=8, τ=5→0.5, λ_H=0.1→0.01)\", \"pid\": 9769, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T04:52:18.089Z\"}}, \"count\": 132, \"total\": 132, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0003}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The tex files search returned empty stdout, meaning no .tex files were found in that path. Let me search more broadly. Also, the registry data is too large to read directly, so I need to use jq to extract relevant data.

Let me search for tex files in different locations and also probe the registry data structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "cfac28ef-23be-43da-aa75-4877d85688f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rz5GQ9WZxv9RHXKXy3GH7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 24757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 881
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

_source line 13_

没找到 tex 文件，需要扩大搜索范围。同时处理 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "8c9a0a7b-fb2f-4adf-8fe9-f837b260db10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rz5GQ9WZxv9RHXKXy3GH7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 24757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 881
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01W9s7kjbrbLS9H31RTUNshT`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "find /root/autodl-tmp -name \"*.tex\" -not -path \"*/logdir/*\" -not -path \"*/.git/*\" -not -path \"*/texlive/*\"",
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
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "9b224339-9524-46c9-91a8-5e98390c7335",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rz5GQ9WZxv9RHXKXy3GH7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 24757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 881
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

_source line 15 · 2026-05-24T02:13:31.193Z_

<details><summary>↩ Tool result · `toolu_01W9s7kjbrbLS9H31RTUNshT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "333d5690-ba67-410e-bbec-da67a717a58f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_012pkQPQsVron2rB57LyRxx8`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\n# Check structure\nif isinstance(result, list):\n    print(f'Total experiments: {len(result)}')\n    if result:\n        print(f'Keys: {list(result[0].keys())}')\n        # Print exp_id and key fields for all experiments\n        for exp in result:\n            eid = exp.get('exp_id', '?')\n            status = exp.get('status', '?')\n            conclusion = exp.get('conclusion', '')\n            metrics = exp.get('metrics', {})\n            tags = exp.get('tags', [])\n            desc = exp.get('description', '')[:80]\n            print(f'{eid} | {status} | tags={tags} | conclusion={str(conclusion)[:120]}')\nelif isinstance(result, dict):\n    print(f'Keys: {list(result.keys())}')\n    print(f'Type: dict with {len(result)} entries')\nelse:\n    print(f'Type: {type(result)}')\n\" 2>&1 | head -80",
  "description": "Parse registry data structure and list all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "5654bc72-403f-49ca-8264-0721a4581c0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rz5GQ9WZxv9RHXKXy3GH7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 24757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 881
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

_source line 17 · 2026-05-24T02:13:36.458Z_

<details><summary>↩ Tool result · `toolu_012pkQPQsVron2rB57LyRxx8`</summary>

```text
Keys: ['success', 'data', 'error', 'metadata']
Type: dict with 4 entries
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "f70e6014-2580-4f15-bca9-9f6d940c6e98",
  "tool_use_result": {
    "stdout": "Keys: ['success', 'data', 'error', 'metadata']\nType: dict with 4 entries",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
The result has a different structure. Let me dig deeper into the `data` field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "d8cfbba8-8c0b-4246-8972-8577226e51a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPLsB5x2ogNkAoEpg2fRK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 25638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
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

<details open><summary>🔧 Tool call — Bash · `toolu_01A36weysYUh7dbx9GLDmsMj`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\ninner = result['data']\nif isinstance(inner, list):\n    print(f'Total experiments: {len(inner)}')\n    if inner:\n        print(f'Keys: {list(inner[0].keys())}')\n        for exp in inner:\n            eid = exp.get('exp_id', '?')\n            status = exp.get('status', '?')\n            tags = exp.get('tags', [])\n            metrics = exp.get('metrics', {})\n            conclusion = str(exp.get('conclusion', ''))[:150]\n            print(f'{eid} | {status} | tags={tags} | metrics_keys={list(metrics.keys()) if isinstance(metrics, dict) else \\\"N/A\\\"} | {conclusion}')\nelif isinstance(inner, dict):\n    print(f'Data keys: {list(inner.keys())[:20]}')\n    # Maybe it's a dict of experiments\n    for k in list(inner.keys())[:5]:\n        print(f'  {k}: {type(inner[k])}')\n\" 2>&1 | head -80",
  "description": "Dig into registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "1d8c23c7-bb4f-4532-9d19-f45b58d9b390",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPLsB5x2ogNkAoEpg2fRK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 25638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
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

_source line 20 · 2026-05-24T02:13:44.622Z_

<details><summary>↩ Tool result · `toolu_01A36weysYUh7dbx9GLDmsMj`</summary>

```text
Data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: &lt;class 'dict'>
  count: &lt;class 'int'>
  total: &lt;class 'int'>
  baseline: &lt;class 'NoneType'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "9382da38-2fea-40bc-bc99-e32075fbbeb5",
  "tool_use_result": {
    "stdout": "Data keys: ['experiments', 'count', 'total', 'baseline']\n  experiments: &lt;class 'dict'>\n  count: &lt;class 'int'>\n  total: &lt;class 'int'>\n  baseline: &lt;class 'NoneType'>",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JjNdo1uuddKUVqXngQDCps`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/",
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
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "6b797762-b5e8-4073-8b78-1b0427e2cc6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPLsB5x2ogNkAoEpg2fRK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 25638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
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

_source line 22 · 2026-05-24T02:13:45.304Z_

<details><summary>↩ Tool result · `toolu_01JjNdo1uuddKUVqXngQDCps`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Dockerfile\\nLICENSE\\nREADME.md\\n__pycache__\\nanalysis\\nartifacts\\ncheckpoint_monitor.py\\ncheckpoint_results.jsonl\\nconfigs.yaml\\nconfigs.yaml.bak\\nconfigs.yaml.bak.pre_plan015\\ndetector_validation_v3.json\\ndocs\\ndreamer.py\\ndreamer.py.bak\\ndreamer.py.bak.step_sync\\nenvs\\neval_mvp.py\\neval_plots\\nexploration.py\\nextract_paper_data.py\\nfigures\\nimgs\\nlaunch_exp053.sh\\nlogdir\\nmodels.py\\nmodels.py.bak\\nmodels.py.bak.hotfix\\nmodels.py.bak.pre_autocorr\\nmodels.py.bak.pre_plan015\\nmodels.py.bak.threshold\\nmodels.py.bak_sgs_fix\\nnetworks.py\\nnetworks.py.bak\\nnetworks.py.bak.pre_plan015\\nnve_audit.py\\nnve_audit_results.txt\\nnve_audit_v2.py\\nnve_audit_v2.py.bak\\nnve_threshold_analysis.py\\nparallel.py\\npickcube_ve_comparison.png\\nprint_detail.py\\nprint_summary.py\\nrequirements.txt\\nscripts\\ntools.py\\ntools.py.bak\\nvalidate_detector.py\\nxvfb_run.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "c5da24f1-d14e-4930-8493-7d6b678a0398",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Dockerfile\\\\nLICENSE\\\\nREADME.md\\\\n__pycache__\\\\nanalysis\\\\nartifacts\\\\ncheckpoint_monitor.py\\\\ncheckpoint_results.jsonl\\\\nconfigs.yaml\\\\nconfigs.yaml.bak\\\\nconfigs.yaml.bak.pre_plan015\\\\ndetector_validation_v3.json\\\\ndocs\\\\ndreamer.py\\\\ndreamer.py.bak\\\\ndreamer.py.bak.step_sync\\\\nenvs\\\\neval_mvp.py\\\\neval_plots\\\\nexploration.py\\\\nextract_paper_data.py\\\\nfigures\\\\nimgs\\\\nlaunch_exp053.sh\\\\nlogdir\\\\nmodels.py\\\\nmodels.py.bak\\\\nmodels.py.bak.hotfix\\\\nmodels.py.bak.pre_autocorr\\\\nmodels.py.bak.pre_plan015\\\\nmodels.py.bak.threshold\\\\nmodels.py.bak_sgs_fix\\\\nnetworks.py\\\\nnetworks.py.bak\\\\nnetworks.py.bak.pre_plan015\\\\nnve_audit.py\\\\nnve_audit_results.txt\\\\nnve_audit_v2.py\\\\nnve_audit_v2.py.bak\\\\nnve_threshold_analysis.py\\\\nparallel.py\\\\npickcube_ve_comparison.png\\\\nprint_detail.py\\\\nprint_summary.py\\\\nrequirements.txt\\\\nscripts\\\\ntools.py\\\\ntools.py.bak\\\\nvalidate_detector.py\\\\nxvfb_run.sh\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Dockerfile\\nLICENSE\\nREADME.md\\n__pycache__\\nanalysis\\nartifacts\\ncheckpoint_monitor.py\\ncheckpoint_results.jsonl\\nconfigs.yaml\\nconfigs.yaml.bak\\nconfigs.yaml.bak.pre_plan015\\ndetector_validation_v3.json\\ndocs\\ndreamer.py\\ndreamer.py.bak\\ndreamer.py.bak.step_sync\\nenvs\\neval_mvp.py\\neval_plots\\nexploration.py\\nextract_paper_data.py\\nfigures\\nimgs\\nlaunch_exp053.sh\\nlogdir\\nmodels.py\\nmodels.py.bak\\nmodels.py.bak.hotfix\\nmodels.py.bak.pre_autocorr\\nmodels.py.bak.pre_plan015\\nmodels.py.bak.threshold\\nmodels.py.bak_sgs_fix\\nnetworks.py\\nnetworks.py.bak\\nnetworks.py.bak.pre_plan015\\nnve_audit.py\\nnve_audit_results.txt\\nnve_audit_v2.py\\nnve_audit_v2.py.bak\\nnve_threshold_analysis.py\\nparallel.py\\npickcube_ve_comparison.png\\nprint_detail.py\\nprint_summary.py\\nrequirements.txt\\nscripts\\ntools.py\\ntools.py.bak\\nvalidate_detector.py\\nxvfb_run.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
No .tex files found on the server. The paper might be in the local project directory. Let me check locally and also check common locations. Also, let me look at the `artifacts` directory and the `docs` directory.

Let me also parse the registry experiments data properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "a1ddd2a6-69e4-4ac9-b4df-297fd216e083",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJbshoh7MfYuNtVSQNbef3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 26490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
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

_source line 24_

没有 .tex 文件在服务器上。检查本地项目目录和服务器上的 artifacts/docs 目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "a0eb7178-9546-4407-82cb-72fbaa90f46d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJbshoh7MfYuNtVSQNbef3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 26490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
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

<details open><summary>🔧 Tool call — Glob · `toolu_01KroMriKUPTMo5HmGjkMHFj`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "bf77451e-472b-4b43-b774-bc7cdbda0d56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJbshoh7MfYuNtVSQNbef3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 26490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
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

_source line 26 · 2026-05-24T02:13:51.500Z_

<details><summary>↩ Tool result · `toolu_01KroMriKUPTMo5HmGjkMHFj`</summary>

```text
docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260514T062606/best/paper.tex
artifacts/dream_reports/dream_20260514T062606/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/best/paper.tex
artifacts/dream_reports/dream_20260515T004704/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/worst/paper.tex
artifacts/figures/archive/tab_rssm_fidelity.tex
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
artifacts/dream_reports/dream_20260514T062606/worst/paper.tex
artifacts/dream_reports/dream_20260516T115400/best/paper.tex
artifacts/dream_reports/dream_20260516T115400/median/paper.tex
artifacts/dream_reports/dream_20260516T115400/worst/paper.tex
artifacts/dream_reports/dream_20260516T133210/best/paper.tex
artifacts/dream_reports/dream_20260516T133210/median/paper.tex
artifacts/dream_reports/dream_20260516T133210/worst/paper.tex
artifacts/dream_reports/dream_20260516T172011/best/paper.tex
artifacts/dream_reports/dream_20260516T172011/median/paper.tex
artifacts/dream_reports/dream_20260516T172011/worst/paper.tex
artifacts/analysis/detector_table.tex
artifacts/_project/paper/nve_sensitivity_table.tex
paper/tables/nve_sensitivity_table.tex
artifacts/dream_reports/dream_20260520T155150/best/paper.tex
artifacts/dream_reports/dream_20260520T155150/median/paper.tex
artifacts/dream_reports/dream_20260520T155150/worst/paper.tex
artifacts/dream_reports/dream_20260520T210241/best/paper.tex
artifacts/dream_reports/dream_20260520T210241/median/paper.tex
docs/paper/main.tex
docs/paper/sections/methodology.tex
docs/paper/sections/related_work.tex
docs/paper/sections/abstract_body.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/results.tex
docs/paper/sections/analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "e5cb7d41-c7a9-4da6-8aa9-93f505f18bb0",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_corl_template/corl_2026_template_submission/example.tex",
      "docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex",
      "artifacts/dream_reports/dream_20260514T062606/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.tex",
      "artifacts/figures/archive/tab_rssm_fidelity.tex",
      "artifacts/_project/paper/nve_sensitivity_table_37b680.tex",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/worst/paper.tex",
      "artifacts/analysis/detector_table.tex",
      "artifacts/_project/paper/nve_sensitivity_table.tex",
      "paper/tables/nve_sensitivity_table.tex",
      "artifacts/dream_reports/dream_20260520T155150/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/worst/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/median/paper.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/methodology.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/abstract_body.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/results.tex",
      "docs/paper/sections/analysis.tex"
    ],
    "durationMs": 13,
    "numFiles": 36,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01P8x5Ej9Pvi3nbK76RxrJKk`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/artifacts/",
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
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "1ff2d0eb-3387-4f8d-af07-0a22eade9cb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJbshoh7MfYuNtVSQNbef3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 26490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
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

_source line 28 · 2026-05-24T02:13:52.294Z_

<details><summary>↩ Tool result · `toolu_01P8x5Ej9Pvi3nbK76RxrJKk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"actor_entropy_contrast.pdf\\nactor_entropy_contrast.png\\nactor_entropy_data.json\\nanalysis\\nbaseline_4seed_mean_ve_ratio.csv\\ncheetah_5seed_mean_ve_ratio.csv\\ncheetah_baseline_s0_ve_profile.csv\\ncheetah_baseline_s1_ve_profile.csv\\ncheetah_baseline_s2_ve_profile.csv\\ncheetah_baseline_s3_ve_profile.csv\\ncheetah_baseline_s4_ve_profile.csv\\nexp_001_baseline_s1_ve_profile_full.csv\\nexp_001_baseline_s2_ve_profile_full.csv\\nexp_001_baseline_s3_ve_profile_full.csv\\nexp_001_baseline_s4_ve_profile_full.csv\\nfig2_nve_trajectory_d054.pdf\\nfig2_nve_trajectory_d054.png\\nfig3_nve_diagnostic_d054.pdf\\nfig3_nve_diagnostic_d054.png\\nfig6_collapse_pathways_d054.pdf\\nfig6_collapse_pathways_d054.png\\nfigures\\ngradient_decomposition_008d.json\\ngradient_evolution_018v2.json\\nnve_4seed_robustness_analysis.csv\\nnve_4seed_robustness_summary.json\\nnve_threshold_v2.json\\nnve_threshold_v3.json\\nnve_threshold_v3_ci_supplement.json\\nnve_threshold_v3_ci_supplement_d054.json\\nscripts\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "fd21ce29-3c79-48b9-8d21-40c095fb13aa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"actor_entropy_contrast.pdf\\\\nactor_entropy_contrast.png\\\\nactor_entropy_data.json\\\\nanalysis\\\\nbaseline_4seed_mean_ve_ratio.csv\\\\ncheetah_5seed_mean_ve_ratio.csv\\\\ncheetah_baseline_s0_ve_profile.csv\\\\ncheetah_baseline_s1_ve_profile.csv\\\\ncheetah_baseline_s2_ve_profile.csv\\\\ncheetah_baseline_s3_ve_profile.csv\\\\ncheetah_baseline_s4_ve_profile.csv\\\\nexp_001_baseline_s1_ve_profile_full.csv\\\\nexp_001_baseline_s2_ve_profile_full.csv\\\\nexp_001_baseline_s3_ve_profile_full.csv\\\\nexp_001_baseline_s4_ve_profile_full.csv\\\\nfig2_nve_trajectory_d054.pdf\\\\nfig2_nve_trajectory_d054.png\\\\nfig3_nve_diagnostic_d054.pdf\\\\nfig3_nve_diagnostic_d054.png\\\\nfig6_collapse_pathways_d054.pdf\\\\nfig6_collapse_pathways_d054.png\\\\nfigures\\\\ngradient_decomposition_008d.json\\\\ngradient_evolution_018v2.json\\\\nnve_4seed_robustness_analysis.csv\\\\nnve_4seed_robustness_summary.json\\\\nnve_threshold_v2.json\\\\nnve_threshold_v3.json\\\\nnve_threshold_v3_ci_supplement.json\\\\nnve_threshold_v3_ci_supplement_d054.json\\\\nscripts\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"actor_entropy_contrast.pdf\\nactor_entropy_contrast.png\\nactor_entropy_data.json\\nanalysis\\nbaseline_4seed_mean_ve_ratio.csv\\ncheetah_5seed_mean_ve_ratio.csv\\ncheetah_baseline_s0_ve_profile.csv\\ncheetah_baseline_s1_ve_profile.csv\\ncheetah_baseline_s2_ve_profile.csv\\ncheetah_baseline_s3_ve_profile.csv\\ncheetah_baseline_s4_ve_profile.csv\\nexp_001_baseline_s1_ve_profile_full.csv\\nexp_001_baseline_s2_ve_profile_full.csv\\nexp_001_baseline_s3_ve_profile_full.csv\\nexp_001_baseline_s4_ve_profile_full.csv\\nfig2_nve_trajectory_d054.pdf\\nfig2_nve_trajectory_d054.png\\nfig3_nve_diagnostic_d054.pdf\\nfig3_nve_diagnostic_d054.png\\nfig6_collapse_pathways_d054.pdf\\nfig6_collapse_pathways_d054.png\\nfigures\\ngradient_decomposition_008d.json\\ngradient_evolution_018v2.json\\nnve_4seed_robustness_analysis.csv\\nnve_4seed_robustness_summary.json\\nnve_threshold_v2.json\\nnve_threshold_v3.json\\nnve_threshold_v3_ci_supplement.json\\nnve_threshold_v3_ci_supplement_d054.json\\nscripts\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015XkTPSEWrhRjF1KbvXK2x8`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/docs/",
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
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "541c9181-2f44-4d77-a8a4-6165343a2cf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJbshoh7MfYuNtVSQNbef3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 26490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
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

_source line 30 · 2026-05-24T02:13:53.516Z_

<details><summary>↩ Tool result · `toolu_015XkTPSEWrhRjF1KbvXK2x8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"pivot_analysis.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "17f31ebd-f3b8-4337-a13b-1cf987db0e3f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"pivot_analysis.md\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"pivot_analysis.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_014yHvYBtGGRxDZwTSjtc5NV`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nfor eid, exp in sorted(exps.items()):\n    status = exp.get('status', '?')\n    tags = exp.get('tags', [])\n    desc = str(exp.get('description', ''))[:100]\n    print(f'{eid} | {status} | tags={tags} | {desc}')\n\" 2>&1 | head -80",
  "description": "List all registry experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "38eeb7b1-b535-4949-a950-9d38c13338b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJbshoh7MfYuNtVSQNbef3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 26490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
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

_source line 32 · 2026-05-24T02:13:57.923Z_

<details><summary>↩ Tool result · `toolu_014yHvYBtGGRxDZwTSjtc5NV`</summary>

```text
Total experiments: 132
016e | DONE | tags=[] | 
exp_001_baseline | DONE | tags=[] | 
exp_001_baseline_s2 | DONE | tags=[] | 
exp_001_baseline_s2_extended | DONE | tags=[] | 
exp_001_baseline_s3 | DONE | tags=[] | 
exp_001_baseline_s3_extended | DONE | tags=[] | 
exp_001_baseline_s4 | DONE | tags=[] | 
exp_001_baseline_s4_extended | DONE | tags=[] | 
exp_002_event_gated | DONE | tags=[] | 
exp_003_event_gated_v2 | DONE | tags=[] | 
exp_004_event_gated_v3 | DONE | tags=[] | 
exp_005_event_gated_v4 | DONE | tags=[] | 
exp_006 | DONE | tags=[] | 
exp_006_fixed_dt2 | DONE | tags=[] | 
exp_007_fixed_dt4 | DONE | tags=[] | 
exp_008a | DONE | tags=[] | 
exp_008a_cheetah_unexposed_s0 | DONE | tags=[] | 
exp_008a_cheetah_unexposed_s1 | DONE | tags=[] | 
exp_008a_no_subsample_dt2 | DONE | tags=[] | 
exp_008a_unexposed_s1 | DONE | tags=[] | 
exp_008a_unexposed_s2 | DONE | tags=[] | 
exp_008a_untrained_s1 | DONE | tags=[] | 
exp_008a_untrained_s2 | DONE | tags=[] | 
exp_008c | DONE | tags=[] | 
exp_008c_no_subsample_dt2_h8 | DONE | tags=[] | 
exp_008d | DONE | tags=[] | 
exp_008d_civo_trigger_s2 | DONE | tags=[] | 
exp_008d_civo_trigger_s3 | DONE | tags=[] | 
exp_008d_civo_trigger_s4 | DONE | tags=[] | 
exp_008d_subsample_on_h8 | DONE | tags=[] | 
exp_008e_subsample_on_dt1_h15 | DONE | tags=[] | 
exp_008e_subsample_on_fixed_dt1 | DONE | tags=[] | 
exp_008e_v2_subsample_on_dt1_h15 | DONE | tags=[] | 
exp_008e_v3_s3 | DONE | tags=[] | 
exp_008e_v3_s4 | DONE | tags=[] | 
exp_008e_v3_subsample_on_dt1_h15 | DONE | tags=[] | 
exp_008e_v3_walker_s1 | DONE | tags=[] | 
exp_008e_v3_walker_s2 | DONE | tags=[] | 
exp_008f_no_dt_embed_subsample_on_h8 | DONE | tags=[] | 
exp_008f_s2 | DONE | tags=[] | 
exp_008f_s3_no_dt_embed_walker | DONE | tags=[] | 
exp_008f_s4 | DONE | tags=[] | 
exp_009a_baseline_walker_s2 | DONE | tags=[] | 
exp_009b_008d_walker_s2 | DONE | tags=[] | 
exp_009c_008f_walker_s2 | DONE | tags=[] | 
exp_009c_s2 | DONE | tags=[] | 
exp_009c_s3 | DONE | tags=[] | 
exp_009d_baseline_walker_s0 | DONE | tags=[] | 
exp_009d_baseline_walker_s1 | DONE | tags=[] | 
exp_009e_008d_walker_s1 | DONE | tags=[] | 
exp_009f_008f_walker_s1 | DONE | tags=[] | 
exp_009g_008f_walker_s0 | DONE | tags=[] | 
exp_009h_008f_walker_s0 | DONE | tags=[] | 
exp_010a_cheetah_baseline_s1 | DONE | tags=[] | 
exp_010b_cheetah_civo_trigger | DONE | tags=[] | 
exp_010b_cheetah_civo_trigger_s0 | DONE | tags=[] | 
exp_015b_frozen_dt_emb | DONE | tags=[] | 
exp_016_sgs_walker_s1 | DONE | tags=[] | 
exp_016b_sgs_walker_s1 | DONE | tags=[] | 
exp_016c_sgs_walker_s1 | DONE | tags=[] | 
exp_016d_sgs_walker_s1 | DONE | tags=[] | 
exp_016e_sgs_walker_s1 | DONE | tags=[] | 
exp_017_subsample_off_trained_dt_emb | DONE | tags=[] | 
exp_018_full_sgs_s2 | DONE | tags=[] | 
exp_018_full_sgs_walker_s1 | DONE | tags=[] | 
exp_018v2_full_sgs_walker_s1 | DONE | tags=[] | 
exp_019a_pickcube_baseline | DONE | tags=[] | 
exp_019a_v2_pickcube_baseline | DONE | tags=[] | 
exp_019b_pickcube_civo_trigger | DONE | tags=[] | 
exp_020_vanilla_dreamerv3_s2 | DONE | tags=[] | 
exp_021_full_sgs_cheetah_s1 | DONE | tags=[] | 
exp_022_untrained_dt_emb_learned_gate | DONE | tags=[] | 
exp_022b_no_curriculum | DONE | tags=[] | 
exp_023_cheetah_baseline_s2 | DONE | tags=[] | 
exp_023_cheetah_baseline_s3 | DONE | tags=[] | 
exp_023_cheetah_baseline_s4 | DONE | tags=[] | 
exp_023_cheetah_baseline_s4_extended | DONE | tags=[] | 
exp_023a_cheetah_baseline_s0 | DONE | tags=[] | 
exp_023b_cheetah_baseline_s1 | DONE | tags=[] |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "b26ed62a-6b0f-4c4f-a9ba-0030bf054162",
  "tool_use_result": {
    "stdout": "Total experiments: 132\n016e | DONE | tags=[] | \nexp_001_baseline | DONE | tags=[] | \nexp_001_baseline_s2 | DONE | tags=[] | \nexp_001_baseline_s2_extended | DONE | tags=[] | \nexp_001_baseline_s3 | DONE | tags=[] | \nexp_001_baseline_s3_extended | DONE | tags=[] | \nexp_001_baseline_s4 | DONE | tags=[] | \nexp_001_baseline_s4_extended | DONE | tags=[] | \nexp_002_event_gated | DONE | tags=[] | \nexp_003_event_gated_v2 | DONE | tags=[] | \nexp_004_event_gated_v3 | DONE | tags=[] | \nexp_005_event_gated_v4 | DONE | tags=[] | \nexp_006 | DONE | tags=[] | \nexp_006_fixed_dt2 | DONE | tags=[] | \nexp_007_fixed_dt4 | DONE | tags=[] | \nexp_008a | DONE | tags=[] | \nexp_008a_cheetah_unexposed_s0 | DONE | tags=[] | \nexp_008a_cheetah_unexposed_s1 | DONE | tags=[] | \nexp_008a_no_subsample_dt2 | DONE | tags=[] | \nexp_008a_unexposed_s1 | DONE | tags=[] | \nexp_008a_unexposed_s2 | DONE | tags=[] | \nexp_008a_untrained_s1 | DONE | tags=[] | \nexp_008a_untrained_s2 | DONE | tags=[] | \nexp_008c | DONE | tags=[] | \nexp_008c_no_subsample_dt2_h8 | DONE | tags=[] | \nexp_008d | DONE | tags=[] | \nexp_008d_civo_trigger_s2 | DONE | tags=[] | \nexp_008d_civo_trigger_s3 | DONE | tags=[] | \nexp_008d_civo_trigger_s4 | DONE | tags=[] | \nexp_008d_subsample_on_h8 | DONE | tags=[] | \nexp_008e_subsample_on_dt1_h15 | DONE | tags=[] | \nexp_008e_subsample_on_fixed_dt1 | DONE | tags=[] | \nexp_008e_v2_subsample_on_dt1_h15 | DONE | tags=[] | \nexp_008e_v3_s3 | DONE | tags=[] | \nexp_008e_v3_s4 | DONE | tags=[] | \nexp_008e_v3_subsample_on_dt1_h15 | DONE | tags=[] | \nexp_008e_v3_walker_s1 | DONE | tags=[] | \nexp_008e_v3_walker_s2 | DONE | tags=[] | \nexp_008f_no_dt_embed_subsample_on_h8 | DONE | tags=[] | \nexp_008f_s2 | DONE | tags=[] | \nexp_008f_s3_no_dt_embed_walker | DONE | tags=[] | \nexp_008f_s4 | DONE | tags=[] | \nexp_009a_baseline_walker_s2 | DONE | tags=[] | \nexp_009b_008d_walker_s2 | DONE | tags=[] | \nexp_009c_008f_walker_s2 | DONE | tags=[] | \nexp_009c_s2 | DONE | tags=[] | \nexp_009c_s3 | DONE | tags=[] | \nexp_009d_baseline_walker_s0 | DONE | tags=[] | \nexp_009d_baseline_walker_s1 | DONE | tags=[] | \nexp_009e_008d_walker_s1 | DONE | tags=[] | \nexp_009f_008f_walker_s1 | DONE | tags=[] | \nexp_009g_008f_walker_s0 | DONE | tags=[] | \nexp_009h_008f_walker_s0 | DONE | tags=[] | \nexp_010a_cheetah_baseline_s1 | DONE | tags=[] | \nexp_010b_cheetah_civo_trigger | DONE | tags=[] | \nexp_010b_cheetah_civo_trigger_s0 | DONE | tags=[] | \nexp_015b_frozen_dt_emb | DONE | tags=[] | \nexp_016_sgs_walker_s1 | DONE | tags=[] | \nexp_016b_sgs_walker_s1 | DONE | tags=[] | \nexp_016c_sgs_walker_s1 | DONE | tags=[] | \nexp_016d_sgs_walker_s1 | DONE | tags=[] | \nexp_016e_sgs_walker_s1 | DONE | tags=[] | \nexp_017_subsample_off_trained_dt_emb | DONE | tags=[] | \nexp_018_full_sgs_s2 | DONE | tags=[] | \nexp_018_full_sgs_walker_s1 | DONE | tags=[] | \nexp_018v2_full_sgs_walker_s1 | DONE | tags=[] | \nexp_019a_pickcube_baseline | DONE | tags=[] | \nexp_019a_v2_pickcube_baseline | DONE | tags=[] | \nexp_019b_pickcube_civo_trigger | DONE | tags=[] | \nexp_020_vanilla_dreamerv3_s2 | DONE | tags=[] | \nexp_021_full_sgs_cheetah_s1 | DONE | tags=[] | \nexp_022_untrained_dt_emb_learned_gate | DONE | tags=[] | \nexp_022b_no_curriculum | DONE | tags=[] | \nexp_023_cheetah_baseline_s2 | DONE | tags=[] | \nexp_023_cheetah_baseline_s3 | DONE | tags=[] | \nexp_023_cheetah_baseline_s4 | DONE | tags=[] | \nexp_023_cheetah_baseline_s4_extended | DONE | tags=[] | \nexp_023a_cheetah_baseline_s0 | DONE | tags=[] | \nexp_023b_cheetah_baseline_s1 | DONE | tags=[] |",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Good. The tex files are in the local project directory under `docs/paper/`. Let me now:
1. Read all the paper tex files
2. Extract the registry data for relevant experiments (frozen, CIVO trigger, manipulation, etc.)

Let me launch parallel agents for efficiency:
- One to read all the tex files and extract quantitative claims
- One to extract relevant registry data

Actually, let me be more targeted. Let me read the key tex files and extract the registry data for the specific experiments mentioned in the task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "dbdb5efa-7e9a-47af-a545-5b54d7c3135e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baw9vo6v92BSMByKhw6KPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3877,
      "cache_read_input_tokens": 27698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3877
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

_source line 34_

论文在本地 `docs/paper/` 目录。启动并行工作：读取论文 tex 文件 + 提取 registry 关键数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "59b25bb5-a0b5-4641-b7c6-fbc1084d230a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baw9vo6v92BSMByKhw6KPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3877,
      "cache_read_input_tokens": 27698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3877
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

<details open><summary>🔧 Tool call — Agent · `toolu_015tp1CEMzPpFQ1WtejthEt9`</summary>

```json
{
  "description": "Extract paper quantitative claims",
  "prompt": "Read all the LaTeX paper files in /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/ and extract every quantitative claim (numbers, ratios like \"6/6\", percentages, NVE values, seed counts, step counts, etc.).\n\nThe files to read are:\n- docs/paper/main.tex\n- docs/paper/sections/abstract_body.tex\n- docs/paper/sections/introduction.tex\n- docs/paper/sections/methodology.tex\n- docs/paper/sections/results.tex\n- docs/paper/sections/analysis.tex\n- docs/paper/sections/related_work.tex\n- docs/paper/sections/conclusion.tex\n- docs/paper/sections/appendix.tex\n\nAlso check:\n- paper/tables/nve_sensitivity_table.tex\n- artifacts/_project/paper/nve_sensitivity_table.tex\n- artifacts/_project/paper/nve_sensitivity_table_37b680.tex\n- artifacts/analysis/detector_table.tex\n\nFor each quantitative claim, report:\n1. File name and line number\n2. The exact text/context around the number\n3. The specific value claimed\n\nFocus especially on:\n- Cross-domain statistics like \"X/Y locomotion\", \"X/Y manipulation\", \"X/Y frozen\"\n- NVE values (especially Walker frozen and Cheetah frozen)\n- Seed counts (n=2, n=3, etc.)\n- Step counts (132.5K, 142.5K, etc.)\n- Any baseline comparison values (like \"trained s1 peak = 3.08\")\n- Table data in tabular environments\n\nReturn a comprehensive list organized by file. Be thorough - every number matters for this audit.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "a617c655-9442-4ac0-b6bf-2965fc489a7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baw9vo6v92BSMByKhw6KPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3877,
      "cache_read_input_tokens": 27698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3877
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

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Extract paper quantitative claims",
  "task_type": "local_agent",
  "prompt": "Read all the LaTeX paper files in /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/ and extract every quantitative claim (numbers, ratios like \"6/6\", percentages, NVE values, seed counts, step counts, etc.).\n\nThe files to read are:\n- docs/paper/main.tex\n- docs/paper/sections/abstract_body.tex\n- docs/paper/sections/introduction.tex\n- docs/paper/sections/methodology.tex\n- docs/paper/sections/results.tex\n- docs/paper/sections/analysis.tex\n- docs/paper/sections/related_work.tex\n- docs/paper/sections/conclusion.tex\n- docs/paper/sections/appendix.tex\n\nAlso check:\n- paper/tables/nve_sensitivity_table.tex\n- artifacts/_project/paper/nve_sensitivity_table.tex\n- artifacts/_project/paper/nve_sensitivity_table_37b680.tex\n- artifacts/analysis/detector_table.tex\n\nFor each quantitative claim, report:\n1. File name and line number\n2. The exact text/context around the number\n3. The specific value claimed\n\nFocus especially on:\n- Cross-domain statistics like \"X/Y locomotion\", \"X/Y manipulation\", \"X/Y frozen\"\n- NVE values (especially Walker frozen and Cheetah frozen)\n- Seed counts (n=2, n=3, etc.)\n- Step counts (132.5K, 142.5K, etc.)\n- Any baseline comparison values (like \"trained s1 peak = 3.08\")\n- Table data in tabular environments\n\nReturn a comprehensive list organized by file. Be thorough - every number matters for this audit.",
  "uuid": "b9fac1ec-b861-45c5-ae9b-58832a93ce30",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


## Round 1

## Round 1

23 recorded events


### User

_source line 37 · 2026-05-24T02:14:15.880Z_

Read all the LaTeX paper files in /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/ and extract every quantitative claim (numbers, ratios like "6/6", percentages, NVE values, seed counts, step counts, etc.).

The files to read are:
- docs/paper/main.tex
- docs/paper/sections/abstract_body.tex
- docs/paper/sections/introduction.tex
- docs/paper/sections/methodology.tex
- docs/paper/sections/results.tex
- docs/paper/sections/analysis.tex
- docs/paper/sections/related_work.tex
- docs/paper/sections/conclusion.tex
- docs/paper/sections/appendix.tex

Also check:
- paper/tables/nve_sensitivity_table.tex
- artifacts/_project/paper/nve_sensitivity_table.tex
- artifacts/_project/paper/nve_sensitivity_table_37b680.tex
- artifacts/analysis/detector_table.tex

For each quantitative claim, report:
1. File name and line number
2. The exact text/context around the number
3. The specific value claimed

Focus especially on:
- Cross-domain statistics like "X/Y locomotion", "X/Y manipulation", "X/Y frozen"
- NVE values (especially Walker frozen and Cheetah frozen)
- Seed counts (n=2, n=3, etc.)
- Step counts (132.5K, 142.5K, etc.)
- Any baseline comparison values (like "trained s1 peak = 3.08")
- Table data in tabular environments

Return a comprehensive list organized by file. Be thorough - every number matters for this audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "18a4ab85-fc30-48ff-98e5-accd22b7416a"
}
```

</details>

---


### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 14498,
    "tool_uses": 1,
    "duration_ms": 2987
  },
  "last_tool_name": "Read",
  "uuid": "3aaa1da7-d9c6-4616-af43-48aa0f261b44",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/abstract_body.tex",
  "usage": {
    "total_tokens": 14499,
    "tool_uses": 2,
    "duration_ms": 3199
  },
  "last_tool_name": "Read",
  "uuid": "0f2435a3-0beb-4444-878b-098de66d7a8b",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/introduction.tex",
  "usage": {
    "total_tokens": 16715,
    "tool_uses": 3,
    "duration_ms": 5291
  },
  "last_tool_name": "Read",
  "uuid": "982d9975-23e8-42b2-af07-d00b20ef2a7e",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/methodology.tex",
  "usage": {
    "total_tokens": 16756,
    "tool_uses": 4,
    "duration_ms": 5896
  },
  "last_tool_name": "Read",
  "uuid": "ea304939-4852-4ada-a285-7d4875102697",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/results.tex",
  "usage": {
    "total_tokens": 20273,
    "tool_uses": 5,
    "duration_ms": 9126
  },
  "last_tool_name": "Read",
  "uuid": "fb41f04f-c5f2-48ab-904e-094462c3ee04",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/analysis.tex",
  "usage": {
    "total_tokens": 20310,
    "tool_uses": 6,
    "duration_ms": 9666
  },
  "last_tool_name": "Read",
  "uuid": "197da25f-3dfb-4c45-9a38-902b0d4dff95",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01D49AVkmqsnYD53ZrmsdXed`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "8284fb62-c359-4aee-9173-bdce3210372d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NYELu1UwY8mrtb2s1YVrQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14493,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14493,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 45 · 2026-05-24T02:14:18.877Z_

<details><summary>↩ Tool result · `toolu_01D49AVkmqsnYD53ZrmsdXed`</summary>

```text
1	\documentclass{article}
2	
3	% Load xcolor before corl_2026 (which loads color internally)
4	\usepackage[table]{xcolor}
5	\usepackage{corl_2026}
6	
7	\usepackage[utf8]{inputenc}
8	\usepackage[T1]{fontenc}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{graphicx}
13	\graphicspath{{../../artifacts/}}
14	\usepackage{colortbl}
15	\usepackage{caption}
16	\usepackage{subcaption}
17	\usepackage{array}
18	\usepackage{enumitem}
19	\usepackage{wrapfig}
20	\usepackage{algorithm}
21	\usepackage{algorithmic}
22	
23	% Custom commands
24	\newcommand{\dt}{\mathrm{dt}}
25	\newcommand{\nve}{\mathrm{nve}}
26	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
27	\newcommand{\sgseval}{448.3}
28	\newcommand{\sgsnve}{1.66}
29	\newcommand{\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}
30	\newcommand{\ie}{\textit{i.e.}}
31	\newcommand{\eg}{\textit{e.g.}}
32	\newcommand{\cf}{\textit{cf.}}
33	\newcommand{\etal}{\textit{et al.}}
34	
35	\title{Why Temporal Abstraction Can Fail in Imagination-Based RL:\\
36	A Diagnostic Analysis of Variable-Rate DreamerV3}
37	
38	\author{
39	  Anonymous Authors
40	}
41	
42	\begin{document}
43	\maketitle
44	
45	\begin{abstract}
46	\input{sections/abstract_body}
47	\end{abstract}
48	
49	\keywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
50	
51	% --- INTRODUCTION ---
52	\input{sections/introduction}
53	
54	% --- RELATED WORK ---
55	\input{sections/related_work}
56	
57	% --- METHODOLOGY ---
58	\input{sections/methodology}
59	
60	% --- RESULTS ---
61	\input{sections/results}
62	
63	% --- ANALYSIS ---
64	\input{sections/analysis}
65	
66	% --- CONCLUSION ---
67	\input{sections/conclusion}
68	
69	% no \bibliographystyle needed — corl_2026.sty sets it automatically
70	\bibliography{references}
71	
72	% --- APPENDIX ---
73	\appendix
74	\input{sections/appendix}
75	
76	\end{document}
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "cad88e6e-e22f-47de-b98d-c7b4cf023466"
}
```

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01365Nt97XczqBqRvy55FEYj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "71a5cb41-aaea-4250-a1e0-f05c9579f593",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NYELu1UwY8mrtb2s1YVrQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14493,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14493,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 47 · 2026-05-24T02:14:19.085Z_

<details><summary>↩ Tool result · `toolu_01365Nt97XczqBqRvy55FEYj`</summary>

```text
1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--30\% of baseline. Factorial diagnostics on two continuous-control tasks isolate trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 26/29, AUROC${=}0.953$, LOEO cross-validated). The RSSM develops a $2.78\times$ reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as the structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination ($\rho > 0.999$), rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery. A lightweight NVE detector achieves 100\% sensitivity.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "6b08be9c-49a0-43b3-a210-dd330d4f8ba3"
}
```

</details>

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01BXTBABqsPLKT1iUMtV4L3g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "dd38c1d1-54e6-446c-a02d-e97ba12988fc",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TofJMGxnNTTFTux2EXsk52",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 14493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2177,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 49 · 2026-05-24T02:14:21.177Z_

<details><summary>↩ Tool result · `toolu_01BXTBABqsPLKT1iUMtV4L3g`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	World-model reinforcement learning enables sample-efficient learning directly on physical hardware \citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\dt$ mismatches between simulation and hardware. TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\% of baseline). Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\geq 1.5\times$ achieves 26/29 classification ($n{=}29$, two environments, AUROC${=}0.953$, in-sample; LOEO cross-validated, Appendix~Table~\ref{tab:nve_loeo}).
7	
8	Gradient decomposition reveals that gradient magnitude does not predict causal importance: the reward head contributes 38--49\% of $\nabla_\theta e_{\dt}$ yet reward-only stopping fails, while the observation decoder (16--22\%) carries the critical signal. A four-level intervention hierarchy (gradient, output, representation, architecture) shows that no tested intervention reliably eliminates CIVO across environments. In pure-imagination training, dual critics converge to identical value functions ($\rho > 0.999$), rendering Double Q pessimism ineffective; the min operation nonetheless enables CIVO recovery, while prevention requires min $+$ increased capacity. These findings are directly relevant to robotics: as world-model RL moves toward real systems with variable-rate sensing and multi-timescale control, understanding when temporal conditioning fails, and why standard countermeasures cannot fix it, is essential for safe deployment.
9	
10	\paragraph{Contributions.}
11	\begin{enumerate}[nosep,leftmargin=*]
12	    \item \textbf{Failure mode identification.} We identify CIVO as specific to imagination-based actor-critic with temporal conditioning and isolate trained $\dt$-embedding $+$ multi-rate exposure as jointly sufficient in tested configurations (6/6 seeds, two locomotion environments, AUROC${=}0.953$, in-sample; LOEO cross-validated). Cross-environment validation spanning locomotion and manipulation (ManiSkill) establishes that CIVO is locomotion-specific; frozen-embedding controls on three manipulation tasks identify value-ratio transients as environment-driven, demonstrating the diagnostic's specificity on non-CIVO dynamics.
13	    \item \textbf{Architectural boundary.} $\dt$-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping, where model errors compound into biased value targets with no real-data anchor.
14	    \item \textbf{Four-level intervention hierarchy.} Across gradient, output, representation, and architecture levels, no intervention reliably eliminates CIVO across environments. Gradient magnitude does not predict causal importance (reward head: 38--49\%, reward-only stopping fails). In pure-imagination training, dual critics converge ($\rho > 0.999$), eliminating Double Q pessimism, though the min operation enables recovery through a different mechanism.
15	    \item \textbf{Online detection.} A lightweight NVE-based detector achieves 100\% sensitivity (5/5) with predictive warning in 2/5 cases.
16	\end{enumerate}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "0ef7efdd-8e2c-4c89-937e-924b211294f9"
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_019yaqwvDuuWon2CQcYmZ14E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "a8d11d02-7f55-4c7a-a26d-a3b47ab7f17d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TofJMGxnNTTFTux2EXsk52",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 14493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2177,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 51 · 2026-05-24T02:14:21.782Z_

<details><summary>↩ Tool result · `toolu_019yaqwvDuuWon2CQcYmZ14E`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:methodology}
3	
4	\subsection{Base Architecture}
5	\label{sec:base_arch}
6	
7	All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\dt{=}1$, meaning each imagination step corresponds to one environment transition.
8	
9	\subsection{Variable-Rate Imagination Mechanism}
10	\label{sec:variable_rate}
11	
12	We introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.
13	
14	\paragraph{Temporal embedding.}
15	A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step to condition state predictions on the temporal scale. We test three modes:
16	\begin{itemize}[nosep,leftmargin=*]
17	\item \textbf{Trained}: embedding parameters are updated via backpropagation through the world model loss, so the RSSM can co-adapt its dynamics and reward predictions to the temporal scale.
18	\item \textbf{Frozen}: a fixed random projection of identical dimensionality (\texttt{requires\_grad=False}). The RSSM receives a temporal signal but cannot co-adapt to it.
19	\item \textbf{Removed}: embedding dimension set to zero; no temporal conditioning signal is provided.
20	\end{itemize}
21	We further distinguish \textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\dt{>}1$ transitions) from \textbf{trained-but-unexposed} (subsample OFF: $\dt{>}1$ used only during imagination). This four-way classification (trained/exposed, trained/unexposed, frozen, removed) is the key experimental structure of our factorial design.
22	
23	\paragraph{Temporal subsampling.}
24	When enabled, the replay buffer augments training data with variable-$\dt$ transitions by subsampling consecutive frames. Concretely, with a maximum subsampling factor of~2, the RSSM trains on both $\dt{=}1$ and $\dt{=}2$ transitions drawn from the same episodes. When disabled, only standard $\dt{=}1$ transitions are used. This factor controls whether the world model has seen multi-scale dynamics during training.
25	
26	\paragraph{Imagination horizon and step size.}
27	The imagination horizon $H$ sets the number of rollout steps. We test $H{=}15$ (default) and $H{=}8$. The reduced horizon controls for compounding error: $H{=}8$ steps at $\dt{=}2$ covers $16$ physical time steps, comparable to the $15$ physical steps of the default configuration. The parameter \texttt{gate\_fixed\_dt} forces all imagination steps to use a specific $\dt$ value ($1$, $2$, or $4$); this separates the effect of $\dt$-conditioning from any learned gating policy.
28	
29	\subsection{Factorial Design}
30	\label{sec:factorial}
31	
32	We adopt a factorial ablation across four factors: $\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and imagination step size ($\dt{=}1$, $2$, $4$). The design (12 conditions, Table~\ref{tab:factorial_design} in Appendix~\ref{sec:appendix_factorial}) isolates trained $\dt$-embedding and multi-rate data exposure as orthogonal factors. Key configurations use 4 seeds; following \citet{agarwal2021precipice}, we report per-seed trajectories.
33	
34	\subsection{Diagnostic Metrics}
35	\label{sec:metrics}
36	
37	\paragraph{Normalized value-to-eval ratio ($\nve$).}
38	We define $\nve_t = (v/e)_{\text{config},t} / (v/e)_{\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\_001, seed~1, 505K steps). We restrict to a \textbf{35K+ window} to avoid early-training inflation. The $\nve \geq 1.5\times$ threshold achieves 26/29 accuracy (AUROC${=}0.953$, in-sample; LOEO cross-validated, mean AUROC${=}0.981$, Appendix~Table~\ref{tab:nve_loeo}).
39	
40	\subsection{Selective Gradient Stopping}
41	\label{sec:sgs_method}
42	
43	To identify which gradient pathway through $e_{\Delta t}$ drives CIVO, we introduce \textit{selective gradient stopping} (SGS): $e_{\Delta t}$ is detached via $\operatorname{sg}(\cdot)$ before selected prediction heads during the backward pass, preventing those loss gradients from updating $e_{\Delta t}$ while preserving its forward-pass contribution. We test three variants: reward-only (exp\_016e), full-pathway (exp\_018, all non-KL gradients blocked), and obs-decoder-only (exp\_025/026). Gradient decomposition using $\nabla_\theta \mathcal{L}_i$ quantifies each pathway's contribution (Appendix~\ref{sec:sgs_gradient_analysis}).
44	
45	\subsection{Forward-Pass Interventions}
46	\label{sec:forward_pass_method}
47	
48	We test two forward-pass interventions as representation- and output-level probes: \textbf{TCN} adds Gaussian noise $\mathcal{N}(0, \sigma^2)$ to $e_{\Delta t}$ during imagination ($\sigma \in \{0.5, 0.2\}$, three environments); \textbf{RAVE} clips imagined values exceeding an EMA anchor ($c \in \{2.0, 1.5\}$).
49	
50	\subsection{Dual-Critic Mechanism Ablation}
51	\label{sec:dual_critic_method}
52	
53	To test whether standard overestimation countermeasures address CIVO, we conduct a $2{\times}2$ factorial: \{single, dual\} $\times$ \{narrow (${\sim}1.2$M), wide (${\sim}2.4$M)\} critic parameters. The dual-critic variant follows TD3 \citep{fujimoto2018td3}: two independent value heads trained on shared RSSM features, with the actor optimizing $\min(v_1, v_2)$. The wide variant doubles hidden dimensions to control for capacity independently of the min operation.
54	
55	\subsection{Environment and Training Details}
56	\label{sec:env_details}
57	
58	All experiments use Walker Walk and Cheetah Run from the DeepMind Control Suite (DMC; \citealt{tassa2018dmcontrol}) with proprioceptive observations, chosen for their contrasting dynamics (6-joint biped vs.\ 2-joint runner). Walker Walk serves as the primary environment with the full factorial design; Cheetah Run serves as a severity-dependent generalization probe: CIVO manifests at $8$--$70\times$ NVE on Cheetah versus $2$--$4\times$ on Walker, testing whether interventions transfer under amplified severity rather than replicating the full factorial. The baseline runs for 500K steps (peak return 970.4); treatments run for 105K steps, sufficient to observe collapse onset. All hyperparameters follow the DreamerV3 defaults \citep{hafner2023dreamerv3} without task-specific tuning ($d{=}32$ temporal embedding; full hyperparameters in Appendix~\ref{sec:hyperparameters}). Training uses a single NVIDIA RTX PRO 6000 GPU (${\sim}80$ GPU-hours total). The codebase extends the official DreamerV3 implementation\footnote{\url{https://github.com/danijar/dreamerv3}, accessed March 2026.} with the variable-rate modules described in \S\ref{sec:variable_rate}.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "b22b2389-fa81-4e9d-949d-8e4253658bf8"
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01EyZnqaExdMQX8tudCpZVVV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "89710e3e-2ebe-4e4d-8d4b-b0e3de148d83",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011e5KPeqofTy3NvT5WLr4Tm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3480,
      "cache_read_input_tokens": 16670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3480,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 53 · 2026-05-24T02:14:25.014Z_

<details><summary>↩ Tool result · `toolu_01EyZnqaExdMQX8tudCpZVVV`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{Key configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 42 configurations in Table~\ref{tab:complete_results}.}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\midrule
22	\rowcolor{gray!15}
23	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
24	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
25	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
26	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
27	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
28	\midrule
29	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
30	\rowcolor{gray!15}
31	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
32	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
33	049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\times$$^d$ & Env.\ transient \\
34	050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\times$$^e$ & Env.\ dynamics$^e$ \\
35	046 & Cheetah Run & frz$^b$ & ON & 8 & --- & 1.35$\times$ & No CIVO \\
36	\bottomrule
37	\end{tabular}
38	\vspace{1pt}
39	{\raggedright\footnotesize
40	trn = trained ($d{=}32$, subsample ON);
41	exp$^a$ = trained, subsample OFF;
42	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
43	--- = removed ($d{=}0$).\\
44	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
45	$^d$ StackCube transient: frozen control (exp\_051) exhibits identical spike (peak $4.30\times$ at 42.5K, self-correcting by 82.5K), indicating environment-specific phenomenon unrelated to $\dt$-embedding training.\\
46	$^e$ Seed~0 trained peaks at $10.05\times$ (82.5K) with delayed self-correction; seed~1 trained (exp\_055) peaks at $3.08\times$ (92.5K), final $0.50\times$; seed~1 frozen (exp\_056) peaks at $11.32\times$ (82.5K), final $1.19\times$. Environment-specific stochastic dynamics: frozen final exceeds trained final.\par}
47	\end{table*}
48	
49	%% ============================================================
50	%% F1: All dt>1 degrade
51	%% ============================================================
52	
53	\subsection{F1: All Variable-Rate Configurations Degrade}
54	\label{sec:f1}
55	
56	Every configuration that introduces $\dt > 1$ imagination degrades relative to the $\dt{=}1$ baseline (Figure~\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\%$ of baseline); fixed $\dt{=}4$ (007) never exceeds 176.9 ($19\%$); the learned gate (005) collapses to 98.8 ($11\%$).
57	
58	\begin{figure}[t]
59	\centering
60	\includegraphics[width=0.65\columnwidth]{figures/paper/fig1_learning_curves.pdf}
61	\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}
62	\label{fig:learning_curves}
63	\end{figure}
64	
65	%% ============================================================
66	%% F2: Trained dt_embedding → nve > 1.5x
67	%% ============================================================
68	
69	\subsection{F2: Trained Temporal Embedding Precedes Value Overestimation}
70	\label{sec:f2}
71	
72	The factorial design isolates trained $\dt$-embedding as the strongest predictor. The \emph{primary} comparison---008d (trained, subsample ON) vs.\ 008f (no embedding, subsample ON)---differs only in embedding training, yielding $\nve = 4.12\times$ (eval 82.8) vs.\ $\nve \leq 0.97\times$ (eval 503.0). \emph{Secondary} comparisons against 008a/008c (unexposed embedding) co-vary subsample status and horizon alongside the embedding factor. The $\nve \geq 1.5\times$ threshold (35K+ window) correctly classifies 26 of 29 experimental configurations across two environments (AUROC${=}0.953$, in-sample; LOEO cross-validated, Table~\ref{tab:nve_loeo}; Figure~\ref{fig:nve_trajectory}).
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=0.65\columnwidth]{figures/fig1_nve_trajectory.pdf}
77	\caption{NVE trajectories (mean $\pm$ seed range). Trained $\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\ref{tab:complete_results}) exceeds the $1.5\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}
78	\label{fig:nve_trajectory}
79	\end{figure}
80	
81	The trained $\dt$-embedding precedes CIVO in all four Walker Walk seeds (peak NVE: $4.62\times$, $4.12\times$, $1.62\times$, $1.53\times$), universally degrading performance to below 30\% of baseline (IQM $175.2$, mean $170.6$, $n{=}4$; \citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and one self-corrects to a stable but degraded state (29.3\% of baseline). Combined with Cheetah Run (\S\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments) with 5/6 progressing toward collapse (Appendix~\ref{sec:seed_divergence}).
82	
83	%% ============================================================
84	%% F3--F5: Summary (details in Appendix B)
85	%% ============================================================
86	
87	\subsection{F3--F5: Factorial Ablation (Appendix~\ref{sec:appendix_factorial})}
88	\label{sec:f3f5_summary}
89	
90	Trained $\dt$-embedding and multi-rate data exposure are \emph{jointly sufficient in tested configurations} for CIVO. Neither factor alone precedes pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, peak NVE $0.83$--$0.93\times$) and multi-rate exposure without embedding (008f, 3 seeds, peak NVE $\leq 1.41\times$) both remain below $1.5\times$. Cross-environment replication on Cheetah Run confirms generalization. Freezing the embedding (\texttt{requires\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.71\times$ vs.\ trained $1.53$--$4.62\times$; 3/4 seeds below threshold, 1/4 transient self-correcting spike; Table~\ref{tab:three_way_emb}); removing the embedding (008f) also avoids CIVO. Partial gradient blocking (exp\_044) does not prevent onset (peak NVE $4.45\times$) but permits delayed self-correction (final eval 538, 59\% baseline; Appendix~\ref{sec:appendix_factorial}), confirming that \emph{any} gradient pathway updating $e_{\dt}$ suffices to induce CIVO. Degradation scales monotonically with $\dt$ ($-47\%$ at $\dt{=}2$, $-81\%$ at $\dt{=}4$; Figure~\ref{fig:dt_amplification}).
91	
92	\paragraph{ManiSkill manipulation tasks.}
93	None of three ManiSkill environments exhibit $\dt$-embedding-dependent CIVO. StackCube-v1 value-ratio spikes are environment-specific: trained (049/052, NVE $5.05$/$4.67\times$) and frozen (051, $4.30\times$) match, all self-correcting by 82.5K. PegInsertionSide-v1 exhibits high-amplitude stochastic dynamics ($4$--$11\times$) whose trained/frozen ordering is seed-dependent: seed~0 trained peaks higher ($10.05\times$ vs.\ frozen $1.82\times$), but seed~1 reverses (frozen peak $11.32\times$ vs.\ trained peak $3.08\times$). PickCube-v1 frozen control (exp\_054, peak $8.81\times$ at 62.5K, self-correcting) confirms the same pattern. CIVO is locomotion-specific in DreamerV3; the frozen-embedding diagnostic correctly identifies these transients as non-CIVO.
94	
95	%% ============================================================
96	%% F6--F7: Interventions and cross-environment
97	%% ============================================================
98	
99	\subsection{F6--F7: Interventions and Multiple Pathways}
100	\label{sec:f6}
101	
102	\paragraph{F6: Trained embedding creates multiple vulnerability pathways.}
103	Exp\_008e\_v3 restricts imagination to $\dt{=}1$ while retaining the trained embedding. Two of four seeds collapse (50\%): Pathway~A (CIVO, $\nve = 4.02\times$) and preliminary Pathway~B (entropy \emph{increase}, $\nve = 3.78\times$; 2 seeds only, requires confirmation; Appendix~\ref{sec:pathways}). Pathway~B produces one of three non-CIVO false positives ($n{=}29$).
104	
105	\paragraph{F7: Full-pathway gradient stopping shows mixed results.}
106	Full-SGS (exp\_018) detaches all non-KL gradients from $e_{\dt}$. Seed~1 shows partial mitigation (eval 448.3, NVE $1.66\times$); seed~2 collapses (0/2 elimination; Appendix~\ref{sec:sgs_gradient_analysis}). Cross-environment validation on Cheetah (010b, NVE $8.27$--$108.52\times$) confirms CIVO generalization; full-SGS yields 0/3 elimination. Removing the embedding eliminates CIVO on Cheetah (024b, NVE $< 0.2\times$).
107	
108	\paragraph{Targeted obs-decoder-only SGS confirms pathway redundancy.}
109	Obs-decoder-only SGS (exp\_025/026) achieves 1/6 CIVO prevention (1/4 Walker, 0/2 Cheetah; Table~\ref{tab:intervention_hierarchy}), not meaningfully different from full-pathway SGS (0/3). CIVO operates through redundant gradient channels: blocking any single pathway shifts co-adaptation to the remaining ones (Appendix~\ref{sec:seed_divergence}).
110	
111	\begin{table}[t]
112	\centering
113	\caption{Intervention hierarchy. Prevention = peak NVE $< 1.5\times$ (35K+). No level reliably eliminates CIVO across environments.}
114	\label{tab:intervention_hierarchy}
115	\footnotesize
116	\setlength{\tabcolsep}{3pt}
117	\begin{tabular}{llccc}
118	\toprule
119	\textbf{Level} & \textbf{Intervention} & \textbf{Seeds} & \textbf{Prev.} & \textbf{Rate} \\
120	\midrule
121	--- & Untreated & 6 & 0/6 & 0\% \\
122	\midrule
123	Gradient & Reward-only SGS & 2 & 0/2 & 0\% \\
124	Gradient & Full-pathway SGS & 3 & 0/3 & 0\% \\
125	Gradient & Obs-decoder SGS & 6 & 1/6 & 17\% \\
126	\midrule
127	Output & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\% \\
128	\midrule
129	Repr. & TCN ($\sigma{=}0.1$) & 1 & 1/1$^\ddagger$ & 100\% \\
130	Repr. & TCN ($\sigma{=}0.2$) & 6$^\dagger$ & 2/6 & 33\% \\
131	Repr. & TCN ($\sigma{=}0.5$) & 3 & 0/3 & 0\% \\
132	Repr. & TCN ($\sigma{=}1.0$) & 1 & 1/1$^\S$ & 100\% \\
133	\midrule
134	Arch. & Wide single & 2 & 0/2 & 0\% \\
135	Arch. & Narrow dual (min) & 2 & 0/2 & 0\% \\
136	Arch. & Wide dual (min) & 4 & 3/4$^\|$ & 75\% \\
137	\midrule
138	--- & Embedding frozen & 7 & 5/7$^\#$ & 71\% \\
139	--- & Embedding removed & 5 & 5/5 & 100\% \\
140	\bottomrule
141	\end{tabular}
142	\vspace{1pt}
143	{\raggedright\footnotesize $^\dagger$Walker 2/4 (s2 NVE $2.11\times$; s3 late-onset CIVO, NVE $3.04\times$ at 105K); Cheetah 0/1, PickCube 0/1.
144	$^\ddagger$Borderline (NVE${=}1.02\times$, eval 55\%).
145	$^\S$CIVO prevented but progressive policy erosion (peak 116\%, final 15\% baseline).
146	$^\|$Walker 3/3 ($\nve \leq 1.4\times$; 1/3 non-CIVO eval collapse), Cheetah 0/1.\\
147	$^\#$Walker 5 + Cheetah 2. Exp\_047 (NVE $1.71\times$) and Exp\_057 (NVE $1.88\times$): both transient, self-correcting within 20K steps; remaining 5 seeds: NVE $0.19$--$1.45\times$.\par}
148	\end{table}
149	
150	%% ============================================================
151	%% Forward-pass interventions
152	%% ============================================================
153	
154	\subsection{Forward-Pass Interventions}
155	\label{sec:forward_results}
156	
157	We test two forward-pass alternatives (Table~\ref{tab:intervention_hierarchy}). \textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\sigma{=}0.2$ (NVE $< 1.0\times$, eval 45--91\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\sigma{=}1.0$) causes policy erosion to 15\% baseline; PickCube 0/1 (Appendix~\ref{sec:tcn_cross_env}). TCN is a \emph{diagnostic probe}, not a deployable mitigation.
158	
159	%% ============================================================
160	%% Architecture-Level Ablation
161	%% ============================================================
162	
163	\subsection{Architecture-Level Ablation}
164	\label{sec:arch_results}
165	
166	\paragraph{Critic convergence in pure imagination.}
167	Across all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\rho > 0.999$), with pessimism at 3--4\% of the independent-critic bound (\S\ref{sec:dual_critic_method}).
168	
169	\paragraph{$2{\times}2$ factorial: recovery vs.\ prevention.}
170	Min drives recovery: narrow dual-critic (${\sim}1.2$M) recovers fully (${\sim}16$--$19\times$ recovery ratio) despite $2\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\nve \leq 1.4\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\ref{sec:dual_critic_appendix}).
171	
172	%% ============================================================
173	%% Online CIVO Detection
174	%% ============================================================
175	
176	\subsection{Online CIVO Detection}
177	\label{sec:detector}
178	
179	We derive a lightweight online detector monitoring the value-to-evaluation ratio for superlinear growth. Applied to 14 runs across three environments, it achieves TPR${=}5/5$, FPR${=}2/9$, with predictive alerts in 2/5 cases (Appendix~\ref{sec:detector_appendix}).
180	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "14e8ddc2-381b-450f-b1bc-3e59f7970911"
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01Xb3D841YNJHakZhZWmJJim`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "a41cede8-d197-4f94-b589-914100121f2d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011e5KPeqofTy3NvT5WLr4Tm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3480,
      "cache_read_input_tokens": 16670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3480,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 55 · 2026-05-24T02:14:25.552Z_

<details><summary>↩ Tool result · `toolu_01Xb3D841YNJHakZhZWmJJim`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{CIVO mechanism.}
5	The RSSM develops a $2.78\times$ reward prediction gap under trained conditioning (Table~\ref{tab:rssm_fidelity}), analogous to delusional bias \citep{lu2018nondelusional}. Gradient magnitude $\neq$ causal importance: the reward head (38--49\% of $\nabla_\theta e_{\dt}$) fails when blocked alone; the observation decoder (16--22\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\S\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\ref{sec:mpc_immune}).
6	
7	\paragraph{Practitioner guidelines.}
8	Monitor via NVE diagnostic ($\geq 1.5\times$, AUROC${=}0.953$; Table~\ref{tab:nve_loeo}). Freezing the $\dt$-embedding converts sustained CIVO (4/4 trained, NVE $1.53$--$108\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\times$) causes irrecoverable damage (Appendix~\ref{sec:appendix_analysis}).
9	
10	\paragraph{Implications for robot learning.}
11	No $\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\times$), but frozen controls show comparable or higher peaks (Table~\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\dt$-embedding bias, while manipulation rewards are sparse and contact-gated.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "c9828cc7-5424-4e4c-9634-2e3d52455dca"
}
```

</details>

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Agent · `toolu_01HgEkLqDE5nyBUNnBawjh3J`</summary>

```json
{
  "description": "Extract registry CIVO/frozen data",
  "prompt": "I need to extract specific experiment data from a registry JSON file for a paper consistency audit.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt\n\nThe file is JSON with schema: {result: string} where result is itself a JSON string containing {success, data: {experiments: {...}, count, total, baseline}, error, metadata}.\n\nI need you to extract and report the following information from the registry:\n\n1. **All CIVO trigger experiments**: Any exp with \"civo_trigger\" in the name. Report exp_id, status, conclusion, metrics (especially NVE values).\n\n2. **All frozen dt_emb experiments**: Any exp with \"frozen\" in the name or description. Report exp_id, status, conclusion, metrics.\n\n3. **All manipulation/PickCube/PegInsertion experiments**: Any exp with \"pickcube\", \"peginsertion\", \"peg\", \"manipulation\" in name. Report exp_id, status, conclusion, metrics.\n\n4. **Walker baseline experiments**: exp_009d_baseline_walker_s0, exp_009d_baseline_walker_s1, exp_009a_baseline_walker_s2. Report metrics.\n\n5. **Cheetah baseline experiments**: Any exp with \"cheetah_baseline\" in name. Report exp_id, metrics.\n\n6. **Experiments exp_057 and exp_058**: If they exist, report full details.\n\n7. **Any experiment with \"frozen\" in the name**: Full details.\n\n8. **All experiments with NVE or nve in their metrics/conclusion**: Report the NVE values.\n\nFor each experiment, extract: exp_id, status, conclusion (full text), metrics (full dict), description, tags.\n\nUse python or jq to parse. Report results organized by category. Be precise with numbers - this is for a paper data audit.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "6a73df90-b43a-4723-b0b4-9a96f4aae424",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baw9vo6v92BSMByKhw6KPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3877,
      "cache_read_input_tokens": 27698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3877
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

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Extract registry CIVO/frozen data",
  "task_type": "local_agent",
  "prompt": "I need to extract specific experiment data from a registry JSON file for a paper consistency audit.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt\n\nThe file is JSON with schema: {result: string} where result is itself a JSON string containing {success, data: {experiments: {...}, count, total, baseline}, error, metadata}.\n\nI need you to extract and report the following information from the registry:\n\n1. **All CIVO trigger experiments**: Any exp with \"civo_trigger\" in the name. Report exp_id, status, conclusion, metrics (especially NVE values).\n\n2. **All frozen dt_emb experiments**: Any exp with \"frozen\" in the name or description. Report exp_id, status, conclusion, metrics.\n\n3. **All manipulation/PickCube/PegInsertion experiments**: Any exp with \"pickcube\", \"peginsertion\", \"peg\", \"manipulation\" in name. Report exp_id, status, conclusion, metrics.\n\n4. **Walker baseline experiments**: exp_009d_baseline_walker_s0, exp_009d_baseline_walker_s1, exp_009a_baseline_walker_s2. Report metrics.\n\n5. **Cheetah baseline experiments**: Any exp with \"cheetah_baseline\" in name. Report exp_id, metrics.\n\n6. **Experiments exp_057 and exp_058**: If they exist, report full details.\n\n7. **Any experiment with \"frozen\" in the name**: Full details.\n\n8. **All experiments with NVE or nve in their metrics/conclusion**: Report the NVE values.\n\nFor each experiment, extract: exp_id, status, conclusion (full text), metrics (full dict), description, tags.\n\nUse python or jq to parse. Report results organized by category. Be precise with numbers - this is for a paper data audit.",
  "uuid": "7d152d68-d014-4860-9b45-4bb554737062",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/related_work.tex",
  "usage": {
    "total_tokens": 26496,
    "tool_uses": 7,
    "duration_ms": 13325
  },
  "last_tool_name": "Read",
  "uuid": "b8974ae4-de52-43d6-bd62-a810909a562a",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_01V95WUkCTzpP6ehZ9jt69XY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "3ebdeb79-82fb-4d2b-b4df-8e8c1685b4b5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FwZ3zi7kiZq6RtYtbzWfaC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 20150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6149,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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


## Round 2

## Round 2

119 recorded events


### User

_source line 60 · 2026-05-24T02:14:29.130Z_

I need to extract specific experiment data from a registry JSON file for a paper consistency audit.

The file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt

The file is JSON with schema: {result: string} where result is itself a JSON string containing {success, data: {experiments: {...}, count, total, baseline}, error, metadata}.

I need you to extract and report the following information from the registry:

1. **All CIVO trigger experiments**: Any exp with "civo_trigger" in the name. Report exp_id, status, conclusion, metrics (especially NVE values).

2. **All frozen dt_emb experiments**: Any exp with "frozen" in the name or description. Report exp_id, status, conclusion, metrics.

3. **All manipulation/PickCube/PegInsertion experiments**: Any exp with "pickcube", "peginsertion", "peg", "manipulation" in name. Report exp_id, status, conclusion, metrics.

4. **Walker baseline experiments**: exp_009d_baseline_walker_s0, exp_009d_baseline_walker_s1, exp_009a_baseline_walker_s2. Report metrics.

5. **Cheetah baseline experiments**: Any exp with "cheetah_baseline" in name. Report exp_id, metrics.

6. **Experiments exp_057 and exp_058**: If they exist, report full details.

7. **Any experiment with "frozen" in the name**: Full details.

8. **All experiments with NVE or nve in their metrics/conclusion**: Report the NVE values.

For each experiment, extract: exp_id, status, conclusion (full text), metrics (full dict), description, tags.

Use python or jq to parse. Report results organized by category. Be precise with numbers - this is for a paper data audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "c09b066a-4e7f-4848-adc6-d0f1ed8d137a"
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-24T02:14:29.221Z_

<details><summary>↩ Tool result · `toolu_01V95WUkCTzpP6ehZ9jt69XY`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal abstraction in RL.}
5	The options framework \citep{sutton1999options}, option-critic \citep{bacon2017optioncritc}, HAM \citep{parr1998ham}, and MAXQ \citep{dietterich2000maxq} formalize temporal abstraction through hierarchical policies. Semi-MDP theory \citep{bradtke1995smdp} provides the mathematical foundation. Action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, park2021timediscretization} achieve simpler temporal abstraction via real transitions; \citet{wang2024elastic} learn elastic time steps that adapt step size to state dynamics. The Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3, hafner2025dreamerv4} trains policies in imagination at fixed $\dt{=}1$; hierarchical variants \citep{hafner2022director, gumbsch2024thick, mattes2024hieros, li2025lsimagine} use subgoals or separate dynamics per scale, avoiding flat $\dt$-conditioning. TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains; the critical distinction is that MPC re-plans from real states, so model errors do not accumulate into a critic (\S\ref{sec:discussion}).
6	
7	\paragraph{Value overestimation and model fidelity.}
8	Maximization bias \citep{thrun1993issues} has been addressed by Double Q-learning \citep{vanhasselt2016double}, TD3 \citep{fujimoto2018td3}, and ensemble methods \citep{chen2021redq}; in model-based settings, MBPO \citep{janner2019mbpo} and MOPO \citep{yu2020mopo} bound rollout error, while MOReL \citep{kidambi2020morel} and COMBO \citep{yu2021combo} penalize model uncertainty. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints. CIVO is mechanistically distinct: the amplifier is the world model's co-adaptation with a learned temporal embedding, producing systematic reward-prediction bias at $\dt > 1$. Multi-timestep world models \citep{benechehab2023multitimestep} learn predictions at variable horizons but do not examine the value overestimation pathology we isolate. Compounding error in multi-step rollouts \citep{lambert2020objective, asadi2019combating} is a related but distinct phenomenon: if CIVO were generic compounding error, untrained $\dt$-embeddings at $\dt{=}2$ should also produce overestimation, yet they do not (NVE${<}0.6\times$ for 008a/008c vs.\ $4.12\times$ for 008d). Furthermore, signed reward error analysis shows $\dt{=}2$ rewards are \emph{under}predicted (mean SE${=}{-}0.599$), ruling out observation-level overprediction and localizing CIVO to imagination-level prior drift (\S\ref{sec:discussion}). Compounding error decision-aware model learning \citep{hamrick2021planning} optimizes for planning performance but does not address $\dt$-conditioned co-adaptation. DreamSmooth \citep{lee2024dreamsmooth} smooths reward prediction targets but does not address the fidelity gap at $\dt > 1$. Our TCN intervention relates to training-with-noise \citep{bishop1995noise} and NoisyNet \citep{fortunato2018noisynet}; PETS \citep{chua2018pets} and STEVE \citep{buckman2018steve} use ensemble disagreement for epistemic uncertainty. TCN's environment-specific dose sensitivity (\S\ref{sec:forward_results}) suggests CIVO is a structural vulnerability, not a regularization deficiency. Our factorial diagnostic follows \citet{henderson2018deep}.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "be617776-bd09-457c-952b-4fbe1466a582"
}
```

</details>

---


### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/conclusion.tex",
  "usage": {
    "total_tokens": 26533,
    "tool_uses": 8,
    "duration_ms": 13521
  },
  "last_tool_name": "Read",
  "uuid": "08ce7e89-4931-4cf0-86dc-3739abca7255",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_01SARmcu68KkiXoaVJ4if1vF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "93b42562-8da9-4229-923c-dca40e19b218",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FwZ3zi7kiZq6RtYtbzWfaC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 20150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6149,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 64 · 2026-05-24T02:14:29.410Z_

<details><summary>↩ Tool result · `toolu_01SARmcu68KkiXoaVJ4if1vF`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We identify trained $\dt$-embedding with multi-rate data exposure as the strongest predictor of CIVO in DreamerV3 (26/29, AUROC${=}0.953$; LOEO cross-validated). No tested intervention reliably eliminates CIVO; in pure imagination, dual critics converge ($\rho > 0.999$), rendering Double Q pessimism ineffective. The feedback architecture---MPC re-planning versus imagination-based bootstrapping---is the structural factor.
5	
6	\paragraph{Limitations.}
7	Our analysis covers proprioceptive locomotion (DMC) and simulated manipulation (ManiSkill) but does not test pixel-based observations, Atari benchmarks, or real-robot deployments where sensor noise and actuation latency introduce additional confounds.
8	All experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures (e.g., IRIS \citep{micheli2023iris} or latent-space planners beyond TD-MPC2) remains open.
9	We characterize CIVO under fixed-$\dt$ subsampling; learned temporal gates warrant separate study.
10	Statistical power with 4 seeds per configuration is limited \citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.981$) may require recalibration for different reward scales.
11	Code: upon acceptance.
12	\label{sec:limitations}
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "57f53638-72d0-4cce-85fc-7f01b2092212"
}
```

</details>

---


### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 28245,
    "tool_uses": 9,
    "duration_ms": 15927
  },
  "last_tool_name": "Read",
  "uuid": "4d615eca-caa9-4035-94f1-734868f776d7",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01Cti7adRzrXRhTiVVpopA6n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "07030f61-8e82-4c20-b66e-9fbe4a944ee5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FKGdN3hrkDxohqrrAJKjys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1644,
      "cache_read_input_tokens": 26299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1644,
        "ephemeral_1h_input_tokens": 0
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

_source line 67 · 2026-05-24T02:14:32.070Z_

<details><summary>↩ Tool result · reported error · `toolu_01Cti7adRzrXRhTiVVpopA6n`</summary>

```text
File content (27878 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "d090e104-ba70-4a5a-aed2-1fe5fa6cdb75",
  "tool_use_result": "Error: File content (27878 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 28574,
    "tool_uses": 10,
    "duration_ms": 18302
  },
  "last_tool_name": "Read",
  "uuid": "1d5d3d64-ef66-4f7b-8623-3a3df2244d71",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_013sgckST71sF3ngKFHgzc4t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 0,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "0a64d9fd-4871-458c-b970-25937f056649",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01X1QuqZ64AcNcPUh8JKuuTj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 27943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 258,
        "ephemeral_1h_input_tokens": 0
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

_source line 70 · 2026-05-24T02:14:34.432Z_

<details><summary>↩ Tool result · `toolu_013sgckST71sF3ngKFHgzc4t`</summary>

```text
0	% --- APPENDIX ---
1	
2	\section{Complete Experimental Results}
3	\label{sec:complete_results}
4	
5	Table~\ref{tab:complete_results} reports all 42 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
6	
7	\begin{table*}[t]
8	\centering
9	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
10	\label{tab:complete_results}
11	\scriptsize
12	\setlength{\tabcolsep}{3pt}
13	\begin{tabular}{llcccccl}
14	\toprule
15	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
16	\midrule
17	001 & Baseline ($\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
18	001 s2 & Baseline ($\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\
19	\rowcolor{gray!15}
20	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
21	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
22	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
23	\midrule
24	\rowcolor{gray!15}
25	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
26	\rowcolor{gray!15}
27	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
28	\rowcolor{gray!15}
29	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
30	\rowcolor{gray!15}
31	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
32	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
33	008f s4 & No dt\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\times$ & Healthy \\
34	009c s3 & No dt\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\times$ & Healthy \\
35	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
36	008a\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\times$ & Healthy \\
37	008a\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\times$ & Healthy \\
38	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
39	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
40	042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\times$ & Healthy \\
41	057 & Frozen emb (s2) & frz$^b$ & ON & 8 & --- & 1.88$\times$ & Transient (self-corr.) \\
42	\midrule
43	018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & Partial mitig.\ (CIVO+) \\
44	\rowcolor{gray!15}
45	018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
46	008e\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\times$ & Healthy \\
47	008e\_v3 s2$^\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\times$ & Non-CIVO collapse \\
48	\rowcolor{gray!15}
49	008e\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\times$ & CIVO collapse \\
50	008e\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\times$ & Healthy \\
51	\midrule
52	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
53	\rowcolor{gray!15}
54	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
55	\rowcolor{gray!15}
56	010b\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\times$ & Full collapse \\
57	\rowcolor{gray!15}
58	021 & Cheetah Run & trn$^\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\times$$^d$ & Transient CIVO (self-corr.) \\
59	024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\times$ & Healthy \\
60	024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\times$ & Healthy \\
61	008a\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\times$ & Healthy \\
62	008a\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\times$ & Healthy \\
63	\rowcolor{gray!15}
64	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
65	054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\times$$^h$ & Env.\ transient (ctrl) \\
66	049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\times$$^f$ & Env.\ transient \\
67	052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\times$$^f$ & Env.\ transient \\
68	051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\times$$^f$ & Env.\ transient (ctrl) \\
69	050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\times$$^g$ & Env.\ dynamics \\
70	053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\times$$^g$ & Env.\ dynamics (ctrl) \\
71	055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\times$$^g$ & Env.\ dynamics \\
72	056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\times$$^g$ & Env.\ dynamics (ctrl) \\
73	046 & Cheetah Run & frz$^b$ & ON & 8 & --- & 1.35$\times$ & No CIVO \\
74	058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.23$\times$ & No CIVO \\
75	\bottomrule
76	\end{tabular}
77	\vspace{1pt}
78	{\raggedright\footnotesize
79	trn = trained ($d{=}32$, subsample ON);
80	trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
81	exp$^a$ = trained, subsample OFF;
82	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
83	--- = removed ($d{=}0$).\\
84	$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
85	$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\
86	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
87	$^d$ Peak NVE $9.94\times$ at 45K (transient, self-correcting to $<$1$\times$ by 55K); final eval 221.5.\\
88	$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\
89	$^f$ StackCube transient: frozen control (exp\_051, peak $4.30\times$ at 42.5K) matches trained (exp\_049/052), self-correcting by 82.5K; environment-specific, not $\dt$-embedding-driven.\\
90	$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\times$ (82.5K); seed~1 trained (exp\_055) peaks at $3.08\times$ (92.5K), final $0.50\times$ at 212.5K; seed~1 frozen (exp\_056) peaks at $11.32\times$ (82.5K), final $1.19\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\dt$-embedding causation.\\
91	$^h$ PickCube environment transient: frozen control peak $8.81\times$ at 62.5K, self-correcting to $0.55\times$ at 72.5K; matches trained (exp\_019b) trajectory.\par}
92	\end{table*}
93	
94	\begin{table}[h]
95	\centering
96	\caption{Cross-domain CIVO reproducibility. ``$\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}
97	\label{tab:cross_domain}
98	\footnotesize
99	\begin{tabular}{llccc}
100	\toprule
101	\textbf{Domain} & \textbf{Environment} & \textbf{Trained} & \textbf{Frz ctrl} & \textbf{$\dt$-emb-dep.\ CIVO} \\
102	\midrule
103	Locomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\times$) \\
104	Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\times$) \\
105	Manipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\approx$trained) \\
106	Manipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\ ordering) \\
107	Manipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\
108	\bottomrule
109	\end{tabular}
110	\end{table}
111	
112	\section{NVE Threshold Sensitivity Analysis}
113	\label{sec:appendix_sensitivity}
114	
115	We report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\nve \geq 1.5\times$). Here we additionally present Task~B1, which restricts the positive class to \emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.
116	
117	\subsection{Per-Experiment NVE Values}
118	
119	Table~\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\_v3\_s2 exhibits elevated NVE ($3.78\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\_v3\_s3 exhibits CIVO with NVE $4.02\times$ despite $\Delta t{=}1$ imagination.
120	
121	\begin{table}[ht]
122	\centering
123	\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\ = transient CIVO with self-correction.}
124	\label{tab:nve_raw}
125	\small
126	\begin{tabular}{@{}lrccc@{}}
127	\toprule
128	Experiment & NVE & Mechanism & B1 & B2 \\
129	\midrule
130	006          & 4.83 & sustained CIVO & $+$ & $+$ \\
131	008d         & 4.13 & sustained CIVO & $+$ & $+$ \\
132	008e\_v3\_s3 & 4.02 & CIVO           & $+$ & $+$ \\
133	008e\_v3\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\
134	009b         & 1.62 & transient CIVO & $-$ & $+$ \\
135	001          & 1.00 & non-CIVO       & $-$ & $-$ \\
136	008e\_v3\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\
137	008f         & 0.97 & non-CIVO       & $-$ & $-$ \\
138	008e\_v3\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\
139	008a         & 0.93 & non-CIVO       & $-$ & $-$ \\
140	\bottomrule
141	\end{tabular}
142	\end{table}
143	
144	\subsection{Multi-Threshold Classification Performance}
145	
146	Table~\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\text{AUROC} = 1.000$ because the minimum positive NVE ($4.02\times$, exp~008e\_v3\_s3) exceeds the maximum negative NVE ($3.78\times$, exp~008e\_v3\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\geq 3.9\times$ as a representative value. Table~\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\text{AUROC} = 0.958$, imperfect separation due to 008e\_v3\_s2).
147	
148	\begin{table*}[t]
149	\centering
150	\caption{\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\text{pos}}=3$, $n_{\text{neg}}=7$, $n=10$, $\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\alpha=0.05$). $^\dagger$Optimal threshold in $(3.78, 4.02]$.}
151	\label{tab:sensitivity_b1}
152	\small
153	\setlength{\tabcolsep}{5pt}
154	\begin{tabular}{@{}lcccccccc@{}}
155	\toprule
156	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
157	\midrule
158	$\geq 1.0\times$ & 3 & 3 & 0 & 4 & 70.0\% \; [34.8, 93.3] & 50.0\% & 100\% & 66.7\% \\
159	$\geq 1.2\times$ & 3 & 2 & 0 & 5 & 80.0\% \; [44.4, 97.5] & 60.0\% & 100\% & 75.0\% \\
160	$\geq 1.5\times$ & 3 & 2 & 0 & 5 & 80.0\% \; [44.4, 97.5] & 60.0\% & 100\% & 75.0\% \\
161	\rowcolor{gray!15}
162	$\geq 1.7\times$ & 3 & 1 & 0 & 6 & 90.0\% \; [55.5, 99.7] & 75.0\% & 100\% & 85.7\% \\
163	$\geq 2.0\times$ & 3 & 1 & 0 & 6 & 90.0\% \; [55.5, 99.7] & 75.0\% & 100\% & 85.7\% \\
164	\rowcolor{gray!15}
165	$\geq 3.9\times^\dagger$ & 3 & 0 & 0 & 7 & 100\% \; [69.2, 100] & 100\% & 100\% & 100\% \\
166	\bottomrule
167	\end{tabular}
168	\end{table*}
169	
170	\begin{table*}[t]
171	\centering
172	\caption{\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\text{pos}}=4$, $n_{\text{neg}}=6$, $n=10$, $\text{AUROC}=0.958$). The single false positive at $\geq 1.5\times$ is 008e\_v3\_s2 (IRD mechanism, not CIVO). The $1.5\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}
173	\label{tab:sensitivity_b2}
174	\small
175	\setlength{\tabcolsep}{5pt}
176	\begin{tabular}{@{}lcccccccc@{}}
177	\toprule
178	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
179	\midrule
180	$\geq 1.0\times$ & 4 & 2 & 0 & 4 & 80.0\% \; [44.4, 97.5] & 66.7\% & 100\% & 80.0\% \\
181	$\geq 1.2\times$ & 4 & 1 & 0 & 5 & 90.0\% \; [55.5, 99.7] & 80.0\% & 100\% & 88.9\% \\
182	\rowcolor{gray!15}
183	$\geq 1.5\times$ & 4 & 1 & 0 & 5 & 90.0\% \; [55.5, 99.7] & 80.0\% & 100\% & 88.9\% \\
184	$\geq 1.7\times$ & 3 & 1 & 1 & 5 & 80.0\% \; [44.4, 97.5] & 75.0\% & 75.0\% & 75.0\% \\
185	$\geq 2.0\times$ & 3 & 1 & 1 & 5 & 80.0\% \; [44.4, 97.5] & 75.0\% & 75.0\% & 75.0\% \\
186	$\geq 3.9\times$ & 3 & 0 & 1 & 6 & 90.0\% \; [55.5, 99.7] & 100\% & 75.0\% & 85.7\% \\
187	\bottomrule
188	\end{tabular}
189	\end{table*}
190	
191	\begin{table*}[t]
192	\centering
193	\caption{\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\text{pos}}=8$, $n_{\text{neg}}=8$, $n=16$, $\text{AUROC}=0.969$). Includes Walker Walk (14 configurations) and Cheetah Run (2 configurations).}
194	\label{tab:sensitivity_b2_full}
195	\small
196	\setlength{\tabcolsep}{5pt}
197	\begin{tabular}{@{}lcccccccc@{}}
198	\toprule
199	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
200	\midrule
201	$\geq 1.0\times$ & 8 & 2 & 0 & 6 & 87.5\% \; [61.7, 98.4] & 80.0\% & 100\% & 88.9\% \\
202	$\geq 1.2\times$ & 8 & 1 & 0 & 7 & 93.8\% \; [69.8, 99.8] & 88.9\% & 100\% & 94.1\% \\
203	\rowcolor{gray!15}
204	$\geq 1.5\times$ & 8 & 1 & 0 & 7 & 93.8\% \; [69.8, 99.8] & 88.9\% & 100\% & 94.1\% \\
205	$\geq 1.7\times$ & 6 & 1 & 2 & 7 & 81.3\% \; [54.4, 96.0] & 85.7\% & 75.0\% & 80.0\% \\
206	$\geq 2.0\times$ & 6 & 1 & 2 & 7 & 81.3\% \; [54.4, 96.0] & 85.7\% & 75.0\% & 80.0\% \\
207	$\geq 3.9\times$ & 6 & 0 & 2 & 8 & 87.5\% \; [61.7, 98.4] & 100\% & 75.0\% & 85.7\% \\
208	\bottomrule
209	\end{tabular}
210	\end{table*}
211	
212	\subsection{Threshold Recommendation}
213	
214	For the main diagnostic (Task~B2), we recommend $\nve \geq 1.5\times$ as the operating threshold for three reasons:
215	
216	\begin{enumerate}[nosep,leftmargin=*]
217	\item \textbf{Maximum recall.} The $1.5\times$ threshold achieves 100\% recall, detecting all four CIVO cases including the transient case (009b, $\nve = 1.62\times$). Raising the threshold to $1.7\times$ loses 009b, dropping recall to 75.0\%.
218	\item \textbf{Best F1.} At $1.5\times$, F1 = 88.9\%, the highest among all tested thresholds for B2. The single false positive (008e\_v3\_s2) is mechanistically identifiable as IRD rather than CIVO.
219	\item \textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\times$) add false positives without gaining true positives. Higher thresholds ($\geq 1.7\times$) sacrifice recall without eliminating the 008e\_v3\_s2 false positive (which requires $\tau > 3.78$).
220	\end{enumerate}
221	
222	For Task~B1 (sustained CIVO only), perfect classification is achievable at $\nve \geq 3.9\times$, but with only $n_{\text{pos}} = 3$ the statistical power remains limited (accuracy 95\% CI: [69.2\%, 100\%]).
223	
224	\subsection{Expanded ROC Analysis}
225	\label{sec:roc_analysis}
226	
227	The original $n{=}16$ analysis (Tables~\ref{tab:sensitivity_b1}--\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}29$ configurations spanning all tested interventions. Figure~\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\% bootstrap confidence interval (10{,}000 resamples).
228	
229	\begin{figure}[h]
230	\centering
231	\includegraphics[width=0.7\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}
232	\caption{NVE ROC curve ($n{=}29$ configurations, AUROC${=}0.953$, in-sample, post-hoc). The preset $\nve \geq 1.5\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}
233	\label{fig:nve_roc}
234	\end{figure}
235	
236	We label a configuration as CIVO-positive if and only if (i)~it uses a trained $\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.
237	
238	The three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\_008e\_v3 seed~2, actor entropy \emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \emph{decrease}). All three produce NVE $> 1.5\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\times$) lacks $\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\times$) exhibits the full CIVO causal chain: trained $\dt$-embedding, entropy decrease, and evaluation collapse to 14\% of baseline.
239	
240	\subsection{NVE Normalization Robustness}
241	\label{sec:nve_robustness}
242	
243	To assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\ref{tab:baseline_seeds}).
244	
245	\begin{table}[h]
246	\centering
247	\caption{Walker Walk baseline seeds at 105K and 505K steps.}
248	\label{tab:baseline_seeds}
249	\footnotesize
250	\begin{tabular}{lcccc}
251	\toprule
252	\textbf{Seed} & \textbf{Eval@105K} & \textbf{Eval@505K} & \textbf{ve@65K} & \textbf{ve@105K} \\
253	\midrule
254	s1 & 915.7 & 970.4 & 0.563 & 0.656 \\
255	s2 & 443.5 & 945.7 & 0.898 & 0.742 \\
256	s3 & 869.0 & 947.7 & --- & 0.664 \\
257	s4 & 922.8 & 938.9 & --- & 0.624 \\
258	\bottomrule
259	\end{tabular}
260	\end{table}
261	
262	Seed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\times$; 009b seed~2, peak NVE $1.62\times$) to fall below the $1.5\times$ threshold. Core CIVO cases (peak NVE $> 3\times$) remain correctly classified under all baseline seeds.
263	
264	Single-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\%): the boundary case exp\_009b flips from $\nve = 1.62\times$ (s1) to $1.23\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\times \to 4.52\times$; 008d: $4.13\times \to 3.54\times$). The $1.5\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\% of the threshold.
265	
266	\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).
267	
268	\paragraph{Limitations.} With $n = 10$ experiments, Clopper-Pearson confidence intervals remain wide (e.g., 90.0\% accuracy has 95\% CI [55.5\%, 99.7\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds. Table~\ref{tab:sensitivity_b2_full} reports the original $n{=}16$ evaluation set spanning both environments. The expanded analysis ($n{=}29$, including SGS variants, RAVE, and TCN configurations) yields AUROC${=}0.953$ (Figure~\ref{fig:nve_roc}, in-sample, post-hoc). The original $n{=}16$ core analysis yields AUROC${=}0.969$; the expanded $n{=}29$ set includes SGS, RAVE, TCN, and dual-critic configurations. Cross-architecture validation is deferred to future work.
269	
270	\subsection{Leave-One-Environment-Out Cross-Validation}
271	\label{sec:nve_loeo}
272	
273	To assess whether $\theta{=}1.5\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}13$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\theta{=}1.5\times$ on the held-out environment.
274	
275	\begin{table}[h]
276	\centering
277	\caption{Leave-one-environment-out cross-validation of NVE threshold $\theta=1.5\times$.
278	For each fold, the threshold is validated on an environment whose data was \emph{not} used
279	to select $\theta$. The optimal threshold range on each training set is reported;
280	$\theta=1.5$ falls within the optimal range in all three folds.}
281	\label{tab:nve_loeo}
282	\begin{tabular}{lccccc}
283	\toprule
284	Held-out & $N_{\text{train}}$ & $N_{\text{test}}$ & $\theta_{\text{opt}}$ range & Test Accuracy & Test AUROC \\
285	\midrule
286	PickCube & 18 & 2 & $(1.45,\, 1.53]$ & 2/2 (1.000) & 1.000 \\
287	Cheetah  & 15 & 5 & $(1.45,\, 1.53]$ & 5/5 (1.000) & 1.000 \\
288	Walker   &  7 & 13 & $(1.00,\, 3.78)$ & 12/13 (0.923) & 0.944 \\
289	\midrule
290	\textbf{Mean} & — & — & — & \textbf{0.974} & \textbf{0.981} \\
291	\bottomrule
292	\end{tabular}
293	\end{table}
294	
295	The threshold $\theta{=}1.5\times$ falls within the optimal accuracy range for all three training folds: $(1.45, 1.53]$ when Walker data is available, and the wider $(1.00, 3.78)$ when training on Cheetah$+$PickCube only (where CIVO and non-CIVO NVE values are well-separated). The single cross-validation error is exp\_008e\_v3 seed~2 (Walker), an IRD collapse mechanistically distinct from CIVO (\S\ref{sec:roc_analysis}). Mean held-out accuracy is 0.974 and mean AUROC is 0.981, confirming that $\theta{=}1.5\times$ generalizes across environments without retuning. PickCube fold confidence intervals remain wide (Clopper-Pearson 95\% CI: $[0.158, 1.000]$) due to $N_{\text{test}}{=}2$.
296	
297	% --- APPENDIX B: Factorial Ablation Details ---
298	
299	\section{Factorial Ablation Details}
300	\label{sec:appendix_factorial}
301	
302	This appendix provides the full factorial ablation results summarized in \S\ref{sec:f3f5_summary} of the main text.
303	
304	\paragraph{Embedding gradient analysis.}
305	Table~\ref{tab:three_way_emb} isolates embedding \emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\dt{=}2$ imagination).
306	
307	\begin{table}[h]
308	\centering
309	\caption{$\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}
310	\label{tab:three_way_emb}
311	\footnotesize
312	\begin{tabular}{lccccl}
313	\toprule
314	Condition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\
315	\midrule
316	Trained & all & 008d & $1.53$--$4.62\times$ & 64--268 & 4/4 \\
317	Reward detach & obs+KL only & 044 & $4.45\times$ & 44$\to$538$^\dagger$ & 1/1 \\
318	Full SGS & KL only & 018 & $1.66\times$ & 448 & 1/1$^*$ \\
319	Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\times$$^\ddagger$ & 204--612 & 2/4 \\
320	Removed & N/A & 008f & $0.97$--$1.41\times$ & 307--503 & 0/3 \\
321	\bottomrule
322	\end{tabular}
323	\vspace{1pt}
324	{\raggedright\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\times$); seed~2 collapsed. $^\dagger$Self-corrected at ${\sim}175$K (eval 44$\to$538, 59\% baseline; 224K run). $^\ddagger$Exp\_047 (NVE $1.71\times$) and Exp\_057 (NVE $1.88\times$): both transient, self-correcting within 20K steps.\par}
325	\end{table}
326	
327	The reward-detach condition (exp\_044, \texttt{reward\_dt\_emb\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\dt}$, complementing the framework-level Reward SGS (exp\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\_044 exhibits delayed CIVO onset (${\sim}95$K vs.\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\dt}$. Over a full 224K run, exp\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\_045: 868, 95\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.
328	
329	Table~\ref{tab:factorial_design} summarizes the experimental configurations.
330	
331	\begin{table}[ht]
332	\centering
333	\caption{Factorial design. Each row specifies one experimental configuration. \textbf{Emb}: $\dt$-embedding mode. \textbf{Sub}: temporal subsampling. \textbf{H}: imagination horizon. \textbf{Imag $\dt$}: temporal resolution used during imagination.}
334	\label{tab:factorial_design}
335	\small
336	\setlength{\tabcolsep}{3.5pt}
337	\begin{tabular}{@{}llcccc@{}}
338	\toprule
339	\textbf{ID} & \textbf{Purpose} & \textbf{Emb} & \textbf{Sub} & \textbf{H} & \textbf{Imag $\dt$} \\
340	\midrule
341	001 & Reference baseline & --- & --- & 15 & 1 \\
342	006 & Fixed $\dt{=}2$ & trn & on & 15 & 2 \\
343	007 & Fixed $\dt{=}4$ & trn & on & 15 & 4 \\
344	\midrule
345	008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\
346	008c & Horizon control & exp$^a$ & off & 8 & 2 \\
347	008d & Collapse condition & trn & on & 8 & 2 \\
348	008e\_v3 & $\dt{=}1$ imag control & trn & on & 15 & 1 \\
349	008f & Causal ablation & --- & on & 8 & 2 \\
350	\midrule
351	015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\
352	016e & Stop-grad (reward) & trn$^\dagger$ & on & 8 & 2 \\
353	018 & Full-SGS & trn$^\ddagger$ & on & 8 & 2 \\
354	\midrule
355	005 & Learned gate & adaptive & off & 15 & learned \\
356	\bottomrule
357	\end{tabular}
358	\vspace{-2pt}
359	{\raggedright\footnotesize
360	trn = trained ($d{=}32$, exposed to $\dt{>}1$ data via subsample ON);
361	exp$^a$ = trained ($d{=}32$) but never exposed to $\dt{>}1$ data (subsample OFF);
362	frz$^b$ = frozen random projection ($d{=}32$, \texttt{requires\_grad=False});
363	--- = removed ($d{=}0$).\\
364	$^\dagger$ \texttt{reward\_dt\_emb\_detach=True}; $^\ddagger$ all non-KL gradients to \texttt{dt\_emb} detached.\par}
365	\end{table}
366	
367	\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}
368	\label{sec:f3}
369	
370	\begin{figure}[t]
371	\centering
372	\includegraphics[width=\columnwidth]{figures/paper/fig3_factorial_grid.pdf}
373	\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}
374	\label{fig:factorial_grid}
375	\end{figure}
376	
377	The empirical finding that trained embedding \emph{plus} multi-rate exposure jointly predict CIVO rests on two complementary controls that each remove one factor while holding the other constant.
378	
379	\paragraph{Evidence A: exposure is necessary (exp\_008a).}
380	Exp\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\_008d, its NVE remains in the $0.83$--$0.93\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\% of baseline). The critical factor is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\dt{>}1$ state predictions within the RSSM.
381	
382	This contrasts with exp\_006 (trained $e_{\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\times$ at 45K to $2.31\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\dt{>}1$ transitions during training. This confirms that multi-rate data exposure, not embedding architecture, is the operative variable.
383	
384	\paragraph{Evidence B: trainability is necessary (exp\_015b).}
385	Exp\_015b uses a frozen random-projection embedding ($d{=}32$, \texttt{requires\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\_008d, but with a non-trainable temporal signal. Despite full exposure to $\dt{>}1$ transitions, the NVE peaks at $1.45\times$ at 55K but does not sustain escalation: it retreats to $0.65\times$ by 65K and settles at $0.42\times$ by 105K (trajectory: $0.81 \rightarrow 1.26 \rightarrow 1.45 \rightarrow 0.65 \rightarrow 1.05 \rightarrow 0.47 \rightarrow 0.39 \rightarrow 0.42$). The transient peak approaches but does not exceed the $1.5\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \S\ref{sec:pathways}), the frozen embedding provides no useful gradient signal for temporal adaptation.
386	
387	The contrast with exp\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\times$ with sustained monotonic escalation ($1.78 \rightarrow 1.71 \rightarrow 2.09 \rightarrow 4.12$) and precedes full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\times$ before self-correcting to $0.42\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\dt$-embedding must be able to \emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.
388	
389	Together, these two controls establish that in all tested configurations, CIVO occurs only with the \emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.
390	
391	Cross-environment validation on Cheetah Run replicates the empirical pattern: trained $e_{\dt}$ precedes CIVO in both tested seeds (exp\_010b, 2 seeds, NVE $8.27$--$108.52\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\_024b, 2 seeds, NVE $<0.2\times$, eval 96.5/77.3). Freezing the embedding on Cheetah (exp\_046, NVE${=}1.35\times$ vs.\ trained $70.64\times$, a $52\times$ reduction) further confirms that embedding trainability, not architecture, drives CIVO. This extends the sufficiency finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\ 2-joint).
392	
393	\begin{table}[ht]
394	\centering
395	\small
396	\caption{Causal isolation: $e_{\dt}$ configuration $\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole predictor of CIVO in tested configurations. Neither factor alone is sufficient.}
397	\label{tab:causal_matrix}
398	\begin{tabular}{lcc}
399	\toprule
400	& Multi-rate data (\textsc{on}) & Single-rate data (\textsc{off}) \\
401	\midrule
402	Trained $e_{\dt}$ & exp\_008d: \textbf{CIVO} & exp\_008a: healthy \\
403	 & NVE 4.12$\times$, collapse & NVE 0.93$\times$ \\
404	\midrule
405	Frozen $e_{\dt}$ & exp\_015b: grad.\ starvation & --- \\
406	 & peak NVE 1.45$\times$ (transient) & \\
407	\midrule
408	Removed $e_{\dt}$ & exp\_008f: no CIVO & --- \\
409	 & NVE $\leq$0.97$\times$ & \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	Only the upper-left cell (trained embedding with multi-rate exposure) precedes CIVO (Table~\ref{tab:causal_matrix}). This 2$\times$2 structure establishes that both factors are jointly sufficient in tested configurations.
415	
416	\subsection{F4: Degradation Scales Monotonically with \texorpdfstring{$\dt$}{dt}}
417	\label{sec:f4}
418	
419	\begin{figure}[t]
420	\centering
421	\includegraphics[width=\columnwidth]{figures/paper/fig5_dt_amplification.pdf}
422	\caption{Peak evaluation return as a function of imagination $\dt$. Performance degrades monotonically: $\dt{=}1$ (915.7) $>$ $\dt{=}2$ (485.3, $-47\%$) $>$ $\dt{=}4$ (176.9, $-81\%$).}
423	\label{fig:dt_amplification}
424	\end{figure}
425	
426	The magnitude of degradation scales monotonically with the imagination step size (Figure~\ref{fig:dt_amplification}). From the $\dt{=}1$ baseline (915.7 at 105K), fixed $\dt{=}2$ (exp\_006) achieves a peak of only 485.3 ($-47\%$), and fixed $\dt{=}4$ (exp\_007) peaks at 176.9 ($-81\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.
427	
428	\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}
429	\label{sec:f5}
430	
431	Neither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\nve < 0.93\times$ (\S\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\nve = 4.12\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\ 009c: 148.3) but neither exhibits $\nve > 1.5\times$; low evaluation alone does not indicate CIVO.
432	
433	The $3.2\times$ performance gap (008a: 777.7 vs.\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\leq$0.93$\times$).
434	
435	% --- APPENDIX C: Full Analysis & Discussion ---
436	
437	\section{Full Analysis \& Discussion}
438	\label{sec:appendix_analysis}
439	
440	This appendix provides the complete mechanistic analysis summarized in Section~\ref{sec:discussion} of the main text.
441	
442	\subsection{The CIVO Mechanism}
443	\label{sec:civo_mechanism}
444	
445	\begin{figure}[t]
446	\centering
447	\includegraphics[width=\columnwidth]{figures/paper/fig4_mechanism_diagram.pdf}
448	\caption{CIVO mechanism diagram. The trained $\dt$-embedding enables asymmetric reward prediction fidelity, initiating a feedback loop: biased RSSM rewards $\to$ optimistic critic values $\to$ actor exploitation $\to$ reinforced state-distribution skew.}
449	\label{fig:civo_mechanism}
450	\end{figure}
451	
452	\begin{table}[h]
453	\centering
454	\caption{RSSM fidelity at $\dt{=}1$ vs.\ $\dt{=}2$. Trained embedding (008d) produces $2.78\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}
455	\label{tab:rssm_fidelity}
456	\footnotesize
457	\setlength{\tabcolsep}{4pt}
458	\begin{tabular}{lcccccc}
459	\toprule
460	& \multicolumn{3}{c}{\textbf{obs\_MSE}} & \multicolumn{3}{c}{\textbf{reward\_MAE}} \\
461	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
462	\textbf{Config} & $\dt{=}1$ & $\dt{=}2$ & Gap & $\dt{=}1$ & $\dt{=}2$ & Gap \\
463	\midrule
464	Baseline & 13.49 & 27.50 & 2.04$\times$ & 0.0102 & 0.0159 & 1.56$\times$ \\
465	008d (trained) & 41.31 & 53.67 & 1.30$\times$ & 0.0568 & 0.1579 & 2.78$\times$ \\
466	008f (no emb) & 8.01 & 22.04 & 2.75$\times$ & 0.7469 & 0.7526 & 1.01$\times$ \\
467	\bottomrule
468	\end{tabular}
469	\end{table}
470	
471	The RSSM fidelity analysis (Table~\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO (Figure~\ref{fig:civo_mechanism}).  The trained $\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\dt{=}1$ is $0.0568$, while at $\dt{=}2$ it rises to $0.1579$, a $2.78\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\times$ gap, and the baseline shows $1.56\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.
472	
473	This asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\dt$-embedding causes RSSM predictions at $\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\nve$ above $1.5\times$, followed by evaluation collapse.
474	
475	A random-policy control experiment ($N{=}100$ rollouts, 95\% bootstrap CI) decomposes CIVO into two necessary stages.  \textbf{Stage~1 (dynamics bias):} even under a random policy, $\dt{=}2$ imagination produces $1.68\times$ higher mean reward than $\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\dt > 1$, independent of actor behavior.  \textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\times$ and the trained-actor ratio is $0.98\times$.  The decomposition attributes $\approx 36\%$ of the total effect to dynamics bias and $\approx 64\%$ to actor exploitation, which confirms that both stages are necessary for CIVO to manifest.
476	
477	This mechanism is analogous to delusional bias \citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.
478	
479	\paragraph{Signed reward error analysis.}
480	To test whether CIVO arises from one-step reward overprediction, we compute signed error (predicted $-$ actual) on posterior-conditioned RSSM predictions (Table~\ref{tab:signed_error}). The trained-embedding model (008d) shows \emph{negative} bias at $\dt{=}2$ (mean signed error $-0.599$, only 8\% of samples overpredicted), ruling out observation-level reward overprediction as the mechanism. The baseline is well-calibrated (mean SE $\approx 0$), confirming methodological soundness. Value overestimation therefore occurs during \emph{imagination-level} prior drift: the RSSM prior (unconditioned on observations) generates reward-favorable trajectories at $\dt > 1$ (Stage~1 above, $1.68\times$ ratio under random policy), and the critic accumulates these into overestimated returns. The one-step reward prediction is negatively biased when conditioned on real observations, but this posterior correction is unavailable during imagination. This also distinguishes CIVO from generic compounding error, which would produce \emph{positive} signed error accumulating with horizon; the negative observation-level bias confirms that CIVO is a prior-drift phenomenon, not a reward-prediction artifact.
481	
482	\begin{table}[h]
483	\centering
484	\caption{Signed reward error (predicted $-$ actual) on posterior-conditioned RSSM predictions. Negative values indicate underprediction. The trained-embedding model underpredicts at $\dt{=}2$, ruling out observation-level reward overprediction as the CIVO mechanism.}
485	\label{tab:signed_error}
486	\footnotesize
487	\setlength{\tabcolsep}{4pt}
488	\begin{tabular}{llrrrrr}
489	\toprule
490	\textbf{Config} & $\dt$ & \textbf{Mean SE} & \textbf{Std} & \textbf{\%Over} & \textbf{Actual} & \textbf{Pred} \\
491	\midrule
492	Baseline & 1 & $+0.001$ & 0.023 & 39.6\% & 1.893 & 1.894 \\
493	\midrule
494	008d (trained) & 1 & $+0.018$ & 0.072 & 61.8\% & 0.361 & 0.379 \\
495	008d (trained) & 2 & $\mathbf{-0.599}$ & 0.722 & 8.0\% & 0.721 & 0.121 \\
496	\midrule
497	008f (no emb) & 1 & $-0.710$ & 0.704 & 14.0\% & 0.921 & 0.211 \\
498	008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\% & 1.840 & 0.195 \\
499	\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "d9e65c3f-be32-4319-85a2-a7f94df2ab06"
}
```

</details>

---


### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 45323,
    "tool_uses": 11,
    "duration_ms": 22032
  },
  "last_tool_name": "Read",
  "uuid": "db93dafd-048a-413e-8585-12a89c7b43b3",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01G7H2rLigaZY9dZiKPr5Ras`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 499,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "3d88c442-8f5e-4e98-92ab-07e4dfc3a450",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015kQ7ZNf6hdprikadJ7byct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16712,
      "cache_read_input_tokens": 28201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16712,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 73 · 2026-05-24T02:14:38.209Z_

<details><summary>↩ Tool result · `toolu_01G7H2rLigaZY9dZiKPr5Ras`</summary>

```text
499	008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\% & 1.840 & 0.195 \\
500	\bottomrule
501	\end{tabular}
502	\end{table}
503	
504	\subsection{Selective Gradient Stopping and Gradient Decomposition}
505	\label{sec:sgs_gradient_analysis}
506	
507	\subsubsection{Gradient Decomposition Results}
508	\label{sec:gradient_decomposition}
509	
510	\begin{figure}[t]
511	\centering
512	\includegraphics[width=0.75\columnwidth]{figures/fig3_gradient_decomposition.pdf}
513	\caption{Gradient contribution to $e_{\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\%) yet reward-only SGS (exp\_016e) fails; the observation decoder channel (16--22\%) carries the critical $\dt$-specific spatial information that drives the RSSM fidelity gap.}
514	\label{fig:gradient_decomp}
515	\end{figure}
516	
517	Exp\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\times$. The SGS intervention neither prevented nor attenuated CIVO.
518	
519	To explain this null result, we performed a gradient decomposition analysis using \texttt{torch.autograd.grad} to measure each loss component's contribution to $\nabla_\theta e_{\Delta t}$, where $\theta$ denotes the temporal embedding parameters. Table~\ref{tab:gradient_decomposition} reports the results.
520	
521	\begin{table}[ht]
522	\centering
523	\caption{Gradient contributions to the temporal embedding $e_{\Delta t}$ by loss component, measured via \texttt{torch.autograd.grad} with training configuration \texttt{gate\_fixed\_dt=2}. Gradient norms are $\ell_2$ norms of $\nabla_\theta \mathcal{L}_i$ for each loss $\mathcal{L}_i$.}
524	\label{tab:gradient_decomposition}
525	\small
526	\begin{tabular}{lrrrr}
527	\toprule
528	& \multicolumn{2}{c}{\textbf{@55K}} & \multicolumn{2}{c}{\textbf{@112K}} \\
529	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
530	Loss component & Share & (\%) & Share & (\%) \\
531	\midrule
532	Reward head & --- & 49.0 & --- & 38.1 \\
533	KL dynamics & --- & 34.7 & --- & 40.4 \\
534	Observation decoders & --- & 16.3 & --- & 21.5 \\
535	\bottomrule
536	\end{tabular}
537	\end{table}
538	
539	The gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\% at 55K, 38.1\% at 112K), yet reward-only SGS (exp\_016e) fails catastrophically (NVE $10.42\times$). The observation decoder channel contributes the smallest share (16.3\% at 55K, 21.5\% at 112K) yet carries the critical $\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.
540	
541	The gradient structure is relatively stable across training (reward shifts from 49\% to 38\%, obs from 16\% to 22\%, KL from 35\% to 40\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.
542	
543	\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\times$ reward MAE ratio, Table~\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\Delta t}$, though its 0/2 CIVO elimination rate on Walker (seed~1: NVE reduced from $4.12\times$ to $1.66\times$ but remains CIVO-positive; seed~2: collapsed) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.
544	
545	\subsubsection{Implications for the CIVO Mechanism}
546	\label{sec:sgs_implications}
547	
548	The gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.
549	
550	\paragraph{Gradient importance $\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\%) to $e_{\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\dt$-specific structural information: it adjusts $e_{\Delta t}$ to minimize a scalar prediction error that is largely $\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\Delta t}$ learns scale-dependent latent biases.
551	
552	\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\_016e (NVE $10.42\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\_018) detaches $e_{\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\%).  However, this intervention eliminates CIVO in neither seed: seed~1 shows partial mitigation (eval 448.3, peak NVE $1.66\times$, still CIVO-positive) while seed~2 collapses (eval 40.8). Removing the observation decoder gradient channel is thus contributory but not sufficient. Figure~\ref{fig:civo_decomposition} decomposes evaluation returns across conditions.
553	
554	\begin{figure}[ht]
555	\centering
556	\includegraphics[width=0.75\columnwidth]{figures/fig2_civo_decomposition.pdf}
557	\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk across four conditions. \textbf{Baseline} (001): vanilla DreamerV3. \textbf{Trained dt-emb} (008d)\protect\footnotemark: learned $d{=}32$ temporal embedding with multi-rate data. \textbf{Full-SGS} (s1, s2): trained embedding with all non-KL gradients detached from $e_{\dt}$. Trained $\dt$-embedding degrades peak eval by $73\%$ and final eval by $86\%$. Full-SGS seed~1 shows partial mitigation ($-51\%$ final, NVE $1.66\times$, still CIVO-positive) while seed~2 collapses ($-96\%$ final). CIVO elimination rate $= 0/2$.}
558	\label{fig:civo_decomposition}
559	\end{figure}
560	\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}
561	
562	Cross-environment validation on Cheetah Run (exp\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\times$ at 45K (comparable to the unmitigated exp\_010b's $8.27\times$).  However, unlike exp\_010b, which collapsed permanently to eval 51.7, exp\_021 self-corrected within ${\sim}$10K steps, with sustained NVE dropping to $0.34\times$ (55K--105K) and final evaluation recovering to 221.5.  This transient self-correcting trajectory is not attributable to the SGS intervention: the initial CIVO onset and peak severity are comparable to the unmitigated case, and the self-correction may reflect Cheetah Run's simpler dynamics rather than SGS efficacy.  Performance remains at 38.7\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\_018's Walker results (0/2 CIVO elimination), these findings yield a 0/3 elimination rate across environments, indicating that gradient-level interventions alone do not eliminate the CIVO vulnerability. Additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.
563	
564	\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\_008d) shows a $2.78\times$ reward gap between $\Delta t{=}1$ and $\Delta t{=}2$ transitions (Table~\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\Delta t}$ to produce latent states that are spatially biased at $\dt{>}1$, and the reward head inherits these biases \textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\Delta t}$'s parameters but not causal responsibility for the fidelity gap.
565	
566	\subsubsection{Entropy Dynamics Across Configurations}
567	\label{sec:entropy_dynamics}
568	
569	\begin{figure}[ht]
570	\centering
571	\includegraphics[width=0.85\columnwidth]{figures/fig4_entropy_dynamics.pdf}
572	\caption{Actor entropy trajectories for three configurations. All start at ${\sim}8$ nats and converge to similar values (${\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}
573	\label{fig:entropy_dynamics}
574	\end{figure}
575	
576	\subsubsection{Exp\_016e Reinterpreted as Stochastic Variation}
577	\label{sec:016e_reinterp}
578	
579	The gradient decomposition establishes that exp\_016e targets the largest gradient pathway (reward: 38--49\%) but not the informationally critical one (observation decoders: 16--22\%).  The apparent timing differences between exp\_016e and exp\_008d (later collapse onset, 75K vs.\ 25K, and higher peak evaluation, 326.7 vs.\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\_008d, exp\_009b, exp\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\times$ pathological threshold at some point during training.
580	
581	\subsection{Post-CIVO Outcomes: Why Seeds Diverge}
582	\label{sec:seed_divergence}
583	
584	\begin{table}[ht]
585	\centering
586	\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}
587	\label{tab:post_civo}
588	\footnotesize
589	\setlength{\tabcolsep}{3pt}
590	\begin{tabular}{llcccl}
591	\toprule
592	\textbf{Env} & \textbf{Seed} & \textbf{Peak} & \textbf{Final} & \textbf{Eval} & \textbf{Outcome} \\
593	\midrule
594	Walker & s1 (008d) & 4.12$\times$ & 4.12$\times$ & 82.8 & Full collapse \\
595	Walker & s2 (009b) & 1.62$\times$ & 0.38$\times$ & 267.9 & Transient CIVO \\
596	Walker & s3 (008d\_s3) & 1.53$\times$ & 1.53$\times$ & 268$^\diamond$ & Late-onset collapse \\
597	Walker & s4 (008d\_s4) & 4.62$\times$ & 4.62$\times$ & 63.6 & Full collapse \\
598	\midrule
599	Cheetah & s1 (010b) & 8.27$\times$ & 8.27$\times$ & 51.7 & Full collapse \\
600	Cheetah & s0 (010b\_s0) & 108.52$\times$ & 108.52$\times$ & 0.83 & Full collapse \\
601	\bottomrule
602	\end{tabular}
603	\vspace{1pt}
604	{\raggedright\footnotesize $^\diamond$ Transitional; train returns still declining at 105K.\par}
605	\end{table}
606	
607	All six CIVO-positive seeds cross the $\nve > 1.5\times$ threshold (Table~\ref{tab:post_civo}), yet the downstream damage is stochastic.\footnote{Exp\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\times$ vs.\ Walker's $1.53$--$4.62\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).
608	
609	\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}
610	Obs-decoder SGS seed~3 (exp\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\nve < 1.0\times$, eval 818.6), CIVO onset at 135K ($\nve = 5.47\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\% of baseline) but persistent value collapse ($\nve = 0.14\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage may be irreversible even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\nve = 0.14\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\ref{tab:post_civo}.
611	
612	\subsubsection{Failure and Degradation Mode Taxonomy}
613	
614	Table~\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).
615	
616	\begin{table}[ht]
617	\centering
618	\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}
619	\label{tab:failure_modes}
620	\footnotesize
621	\setlength{\tabcolsep}{3pt}
622	\begin{tabular}{@{}llccl@{}}
623	\toprule
624	\textbf{Mode} & \textbf{Representative} & \textbf{NVE} & \textbf{Entropy} & \textbf{Mechanism} \\
625	\midrule
626	Monotonic CIVO & 008d, 008d\_s4, 010b\_s0 & $\uparrow$ sustained & $\downarrow$ & Reward bias $\to$ critic $\to$ actor \\
627	Late-onset CIVO & 008d\_s3 & $\uparrow$ delayed & $\downarrow$ & Same, delayed onset \\
628	Transient CIVO & 009b & Peak $\to$ $\downarrow$ & Stable & Self-correction via capacity \\
629	IRD collapse & 008e\_v3\_s2 & $\uparrow$ late & $\uparrow$ & Entropy-driven, values stable \\
630	Grad.\ starvation & 015b & Oscillates, decays & Stable & Frozen emb $\to$ zero actor grad \\
631	SGS-resistant & 018\_s2 & $\uparrow$ & $\downarrow$ & Forward-pass conditioning \\
632	SGS-paradoxical & 016e & $\uparrow$ sustained & $\downarrow$ & Reward SGS $\to$ obs-dec reliance \\
633	\bottomrule
634	\end{tabular}
635	\end{table}
636	
637	\subsection{Why MPC Is Immune}
638	\label{sec:mpc_immune}
639	
640	\citet{nhu2025tawm} show that $\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\dt > 1$ is amplified through the closed actor-critic loop.
641	
642	\subsection{The \texorpdfstring{$\dt$}{dt}-Embedding Dilemma}
643	\label{sec:embedding_dilemma}
644	
645	The factorial results reveal a fundamental tension: removing the $\dt$-embedding (008f) eliminates CIVO but at a $13\times$ cost to reward prediction quality ($0.7469$ vs.\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\dt{=}1$ while retaining the trained embedding (008e\_v3) avoids collapse in 2 of 4 seeds (50\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\times$) and Pathway~B (entropy-driven, entropy increase; s2, NVE $3.78\times$; \S\ref{sec:f6}).  Neither approach alone provides a complete solution.
646	
647	\subsection{Multiple Vulnerability Pathways}
648	\label{sec:pathways}
649	
650	The two collapse patterns identified in \S\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and a tentative second mode (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures. Pathway~B is observed in only two seeds (008e\_v3\_s2 and 038\_s2); we present it as preliminary evidence that the trained $\dt$-embedding's learned features may affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B), though additional data is needed to confirm this as a distinct mechanism.  This explains why $\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\times$ for 008e\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse (Figure~\ref{fig:multiple_pathways}).
651	
652	\begin{figure}[ht]
653	\centering
654	\includegraphics[width=0.75\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}
655	\caption{Contrasting collapse dynamics. \textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \textbf{Right:} 008e\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}
656	\label{fig:multiple_pathways}
657	\end{figure}
658	
659	\subsection{Implications for Temporal Abstraction in World Models}
660	\label{sec:implications}
661	
662	CIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \citep{gumbsch2024thick}, Hieros \citep{mattes2024hieros}, LS-Imagine \citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  The CIVO mechanism requires three structural properties: (1) a temporal embedding that co-adapts with dynamics via gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from the shared representation.  Transformer-based world models that share these properties may exhibit analogous vulnerability; architectures that decouple temporal conditioning from the reward prediction pathway would not.
663	
664	\subsection{Cross-Environment TCN Evaluation}
665	\label{sec:tcn_cross_env}
666	
667	Table~\ref{tab:tcn_full} reports the full TCN evaluation across environments and noise magnitudes.
668	
669	\begin{table}[h]
670	\centering
671	\caption{TCN results across environments and noise magnitudes. Prevention = peak NVE $< 1.5\times$ (35K+).}
672	\label{tab:tcn_full}
673	\footnotesize
674	\setlength{\tabcolsep}{4pt}
675	\begin{tabular}{llcccc}
676	\toprule
677	\textbf{Env} & $\sigma$ & \textbf{Seed} & \textbf{NVE$_{\max}$} & \textbf{Prevented?} & \textbf{Eval (\%)} \\
678	\midrule
679	Walker & 0.1 & s0 & 1.02 & \checkmark$^*$ & 55\% \\
680	Walker & 0.2 & s0 & 0.91 & \checkmark & 91\% \\
681	Walker & 0.2 & s1 & 0.64 & \checkmark & 45\% \\
682	Walker & 0.2 & s2 & 2.11$^\dagger$ & $\times$ & ${\sim}5\%$ \\
683	\rowcolor{gray!15}
684	Walker & 0.2 & s3 & 3.04$^\P$ & $\times$ & 11\% \\
685	Walker & 0.5 & s0 & 3.97 & $\times$ & 27\% \\
686	Walker & 0.5 & s1 & 1.64 & $\times$ & 41\% \\
687	\midrule
688	Cheetah & 0.2 & s0 & 1.90 & $\times$ & crashed \\
689	Cheetah & 0.5 & s0 & 10.67 & $\times$ & 26\% \\
690	Cheetah & 1.0 & s0 & $\leq$0.30 & \checkmark$^\S$ & 15\% \\
691	\midrule
692	PickCube & 0.2 & s0 & 3.71 & $\times$ & failing \\
693	\bottomrule
694	\end{tabular}
695	\vspace{1pt}
696	{\raggedright\footnotesize $^*$Borderline: NVE${=}1.02\times$ at 95K, below $1.5\times$ threshold but above $1.0\times$.\\
697	$^\dagger$NVE $= 2.11\times$ at 95K, still rising; eval ${\sim}5\%$ of baseline.\\
698	$^\P$Late-onset CIVO: NVE declined to $0.67\times$ at 95K before phase-transition-like spike to $3.04\times$ at 105K; eval 349.6 at 95K $\to$ 71.8 at 105K $\to$ 104.5 at 215K.\\
699	$^\S$CIVO prevented (NVE${\leq}0.30$); peak eval 116\% baseline at 35K, declining to 15\% by 215K via progressive policy erosion. See ``impossible dose'' discussion.\par}
700	\end{table}
701	
702	\paragraph{Cheetah Run $\sigma{=}0.5$: transient spike with permanent eval damage.}
703	Cheetah $\sigma{=}0.5$ exhibits a novel failure mode: a transient CIVO spike (NVE $= 10.67\times$ at 55K) followed by NVE recovery ($< 0.3\times$ by 95K), but permanent evaluation damage (26\% of baseline). The value signal self-corrects while the policy does not recover, suggesting that CIVO-induced representational damage during the spike is irreversible even when the critic subsequently recalibrates. This trajectory parallels the obs-decoder SGS seed~3 pattern (\S\ref{sec:seed_divergence}), where partial policy recovery coexists with persistent critic damage.
704	
705	\paragraph{Cheetah Run $\sigma{=}0.2$: insufficient dose.}
706	At $\sigma{=}0.2$, Cheetah reaches NVE $= 1.9\times$ at 55K---exceeding the $1.5\times$ threshold---consistent with Cheetah's higher baseline CIVO severity ($8$--$108\times$ vs.\ Walker's $2$--$6\times$). The noise magnitude that suffices for Walker is inadequate for Cheetah, but increasing $\sigma$ to 0.5 trades CIVO prevention for a different failure mode rather than achieving mitigation.
707	
708	\paragraph{PickCube-v1 $\sigma{=}0.2$: sparse-reward failure.}
709	PickCube reaches NVE $= 3.71\times$ at 52.5K with $\sigma{=}0.2$, indicating that TCN provides no protection in sparse-reward manipulation tasks. The combination of sparse rewards and temporal conditioning may amplify the fidelity gap beyond what representation-level noise can attenuate.
710	
711	\paragraph{Dose-response analysis.}
712	We observe $\sigma{=}0.2$ as a local optimum on Walker Walk, achieving complete CIVO suppression in 2 of 4 seeds. Seeds~2 and~3 both fail but via distinct CIVO onset dynamics: seed~2 shows gradual escalation (NVE $= 2.11\times$ at 95K, still rising, eval ${\sim}5\%$), while seed~3 exhibits a phase-transition-like onset---NVE declined to $0.67\times$ at 95K before spiking to $3.04\times$ at 105K (eval 349.6 $\to$ 71.8 in 10K steps). When TCN fails to prevent CIVO onset, the resulting trajectory qualitatively resembles untreated CIVO in its terminal outcome---runaway NVE and eval collapse. The two failure modes (gradual escalation vs.\ sudden onset after apparent suppression) reinforce that TCN operates as a binary gate on CIVO onset rather than providing graded attenuation. Below the optimum, we observe $\sigma{=}0.1$ as insufficient (NVE $= 1.02\times$---borderline, eval 55\%); above it, $\sigma{=}0.5$ overdoses (oscillatory CIVO, eval $\leq 41\%$). Cross-seed variance at $\sigma{=}0.2$ (eval 5--91\%) exceeds the cross-dose difference by a wide margin, reinforcing that seed effects dominate dose effects. TCN is the only tested intervention achieving complete CIVO suppression in any configuration, but its high seed sensitivity and failure to transfer across environments position it as a \emph{diagnostic probe}---identifying the representation level as the relevant intervention target---rather than a deployable mitigation.
713	
714	\paragraph{Cheetah Run ``impossible dose'' dilemma.}
715	Exp\_030c (224K steps) reveals a qualitatively different dose-response on Cheetah. At $\sigma{=}1.0$, CIVO is eliminated (NVE${\leq}0.30$ throughout) and initial learning is \emph{unimpaired}: peak eval reaches 372 at 35K (116\% of baseline), demonstrating that $\sigma{=}1.0$ noise does not prevent policy acquisition. However, cumulative actor gradient interference produces progressive policy erosion---eval declines from 372 to 47 by 215K (15\% of baseline)---while the critic remains well-calibrated (value\_mean${=}12.4$, NVE${=}0.26$ at 215K). This establishes that \emph{policy degradation $\neq$ value corruption}: accurate value signals are insufficient when the actor cannot optimize effectively in noise-perturbed imagination.
716	
717	This ``correct values, failed policy'' pattern provides indirect evidence that CIVO is mechanistically distinct from standard overestimation. Double Q-learning and ensemble methods address critic estimation error, but at $\sigma{=}1.0$ the critic is accurate and the policy still collapses---a failure mode orthogonal to what these countermeasures target. The impossible dose dilemma scales with environment complexity: Cheetah's baseline CIVO severity ($8$--$108\times$ NVE) requires $\sigma \geq 1.0$ to suppress, but this exceeds the actor's gradient signal-to-noise tolerance. On Walker, a narrow effective window exists around $\sigma{=}0.2$; on Cheetah, the effective dose ($\sigma \geq 1.0$) exceeds the tolerable dose, and environments with higher CIVO severity will systematically lack a viable dose window.
718	
719	\section{DreamerV3 Hyperparameters}
720	\label{sec:hyperparameters}
721	
722	Table~\ref{tab:hyperparams} lists the DreamerV3 hyperparameters used across all experiments. Unless otherwise noted, we use the default DreamerV3 configuration for continuous-control tasks (\texttt{dmc\_proprio}).
723	
724	\begin{table}[ht]
725	\centering
726	\caption{DreamerV3 hyperparameters for all experiments. Modifications from defaults are marked with $\diamond$.}
727	\label{tab:hyperparams}
728	\small
729	\begin{tabular}{ll}
730	\toprule
731	\textbf{Parameter} & \textbf{Value} \\
732	\midrule
733	\multicolumn{2}{l}{\textit{World Model}} \\
734	RSSM discrete states & 32 classes $\times$ 32 categories \\
735	RSSM stochastic dim & 32 \\
736	RSSM deterministic dim & 512 \\
737	MLP hidden size & 512 \\
738	MLP layers & 2 \\
739	Activation & SiLU \\
740	Normalization & LayerNorm \\
741	\midrule
742	\multicolumn{2}{l}{\textit{Training}} \\
743	Batch size & 16 sequences $\times$ 64 steps \\
744	Learning rate & $3 \times 10^{-4}$ (Adam, $\epsilon{=}10^{-8}$) \\
745	Sequence length & 64 \\
746	Training ratio & 512 \\
747	Free nats & 1.0 \\
748	KL balance ($\alpha$) & 0.8 \\
749	Discount ($\gamma$) & 0.997 \\
750	$\lambda$-return & 0.95 \\
751	\midrule
752	\multicolumn{2}{l}{\textit{Policy}} \\
753	Imagination horizon$^\diamond$ & 8 or 15 (see Table~\ref{tab:complete_results}) \\
754	Actor entropy scale & $3 \times 10^{-4}$ \\
755	Actor gradient & Reinforce + dynamics backprop \\
756	\midrule
757	\multicolumn{2}{l}{\textit{Temporal Abstraction}$^\diamond$} \\
758	Gate enabled & True (all non-baseline) \\
759	Gate fixed $\dt$ & 1 or 2 (per config) \\
760	Subsample max $\dt$ & 1 (OFF) or 2 (ON) \\
761	$\dt$-embedding dim & 32 \\
762	\midrule
763	\multicolumn{2}{l}{\textit{Environment}} \\
764	Action repeat & 2 (Walker Walk, Cheetah Run) \\
765	Observation & Proprioceptive (no pixels) \\
766	Total environment steps & 105K \\
767	Evaluation frequency & Every 10K steps \\
768	Evaluation episodes & 10 \\
769	\bottomrule
770	\end{tabular}
771	\end{table}
772	
773	\section{Online CIVO Detector Details}
774	\label{sec:detector_appendix}
775	
776	This appendix provides the full algorithm specification and validation results for the online CIVO detector described in \S\ref{sec:detector}.
777	
778	\subsection{Algorithm Specification}
779	
780	\begin{algorithm}[ht]
781	\caption{Online CIVO Detector}
782	\label{alg:civo_detector}
783	\begin{algorithmic}[1]
784	\REQUIRE Stream of $(\bar{V}_t, \bar{E}_t)$ at each checkpoint $t$
785	\STATE $\tau_\text{mag} \leftarrow 0.49$, \quad $\tau_\text{vel} \leftarrow 0.1$, \quad $\varepsilon \leftarrow 10^{-6}$
786	\STATE Initialize $r_\text{prev} \leftarrow 0$, $\Delta r_\text{prev} \leftarrow 0$, $\mathcal{H} \leftarrow []$
787	\FOR{each checkpoint $t$}
788	  \STATE $r_t \leftarrow \bar{V}_t \,/\, \max(\bar{E}_t,\, \varepsilon)$
789	  \STATE $\Delta r_t \leftarrow r_t - r_\text{prev}$
790	  \STATE $c_\text{mag} \leftarrow (r_t \geq \tau_\text{mag})$
791	  \STATE $c_\text{vel} \leftarrow (\Delta r_t > \tau_\text{vel})$
792	  \STATE $c_\text{acc} \leftarrow (\Delta r_\text{prev} > \tau_\text{vel}) \wedge (\Delta r_t > \Delta r_\text{prev})$
793	  \STATE $c_\text{dec} \leftarrow \bigl|\{i : \mathcal{H}[i] < \mathcal{H}[i{-}1],\; i \in \text{last 3}\}\bigr| \geq 2$
794	  \IF{$c_\text{mag} \wedge c_\text{vel} \wedge c_\text{acc} \wedge c_\text{dec}$}
795	    \STATE \textbf{Alert:} CIVO onset at step $t$
796	  \ENDIF
797	  \STATE $r_\text{prev} \leftarrow r_t$, \quad $\Delta r_\text{prev} \leftarrow \Delta r_t$
798	  \STATE Append $\bar{E}_t$ to $\mathcal{H}$
799	\ENDFOR
800	\end{algorithmic}
801	\end{algorithm}
802	
803	The four conditions capture complementary signals: (1)~\emph{Magnitude} ($r_t \geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\emph{Velocity} ($\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\emph{Acceleration} ($\Delta r_t > \Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths; (4)~\emph{Evaluation decline} ($\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A full comparison of window sizes appears in \S\ref{sec:appendix_sensitivity}.
804	
805	Sensitivity analysis over $\tau_\text{mag} \in [0.30, 0.70]$ confirms that $\tau_\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives. The velocity threshold $\tau_\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$).
806	
807	\subsection{Validation Results}
808	
809	\begin{table}[ht]
810	\centering
811	\caption{Retrospective CIVO detector validation ($n{=}14$). Detection type: ``predictive'' = alert precedes 20\% eval decline; ``reactive'' = alert follows decline onset.}
812	\label{tab:detector-validation}
813	\footnotesize
814	\setlength{\tabcolsep}{3pt}
815	\begin{tabular}{llccccc}
816	\toprule
817	\textbf{Exp} & \textbf{Config} & \textbf{Verdict} & \textbf{Trigger} & \textbf{Type} & \textbf{Peak Eval} & $r_\text{ve}$ \\
818	\midrule
819	008d s0 & trained $\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\
820	010b & trained $\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\
821	008d s3 & trained $\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\
822	008d s4 & trained $\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\
823	010b s0 & trained $\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\
824	\midrule
825	008f s3 & no $\dt$-emb & TN & -- & -- & 594 & -- \\
826	009b s2 & trained $\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\
827	baseline s1 & vanilla & TN & -- & -- & 970 & -- \\
828	009d s0 & vanilla & TN & -- & -- & 951 & -- \\
829	009d s1 & vanilla & TN & -- & -- & 920 & -- \\
830	019b & trained $\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\
831	\midrule
832	009c s2 & no $\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\
833	009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\
834	\midrule
835	009c s3 & no $\dt$-emb & TN & -- & -- & 457 & -- \\
836	\midrule
837	\multicolumn{7}{l}{TPR = 5/5 (1.00), \quad FPR = 2/9 (0.22)} \\
838	\bottomrule
839	\end{tabular}
840	\end{table}
841	
842	The detector identifies all five CIVO-positive runs (TPR = 5/5). Two are detected predictively (008d seeds~0 and~3, both at 45K). Two false positives occur among nine negative cases (FPR = 2/9, precision 71\%, F$_1$ = 0.83). Run 009c develops genuine late-stage value overestimation unrelated to CIVO; run 009a triggers during a transient eval dip at 85K before recovery to 966. Early alerts (before 70K) carry higher diagnostic confidence.
843	
844	\subsection{Cross-Simulator Specificity (PickCube)}
845	
846	Exp\_019b applies the CIVO-trigger configuration to PickCube-v1 in ManiSkill3, a manipulation task with sparse rewards. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K, then deflates to 1.38 by 72.5K. This trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. Across all 14 checkpoints through 132.5K, the detector correctly remains silent (TN), confirming that the acceleration filter distinguishes transient spikes from CIVO's sustained monotonic divergence. A frozen-embedding control (exp\_054) confirms this classification: frozen PickCube-v1 exhibits a comparable burst (peak $8.81\times$ at 62.5K) that resolves within a single evaluation cycle ($0.55\times$ at 72.5K), establishing environment-specific origin independent of $\dt$-embedding training.
847	
848	\subsection{Detector Limitations}
849	
850	Four constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse. Second, the acceleration condition assumes monotonically increasing overestimation during onset. Third, the detector identifies a \emph{pattern} rather than a \emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values were calibrated on fourteen runs across three environments; generalization to different reward scales requires further validation.
851	
852	\section{Dual-Critic Mechanism Ablation}
853	\label{sec:dual_critic_appendix}
854	
855	\subsection{\texorpdfstring{$2{\times}2$}{2x2} Factorial Design}
856	
857	We ablate the critic architecture in a $2{\times}2$ factorial: \{single, dual\} $\times$ \{narrow (${\sim}1.2$M), wide (${\sim}2.4$M)\} parameters. Table~\ref{tab:dual_critic_full} reports all configurations.
858	
859	\begin{table}[ht]
860	\centering
861	\caption{Dual-critic $2{\times}2$ factorial results. Walker Walk unless noted.}
862	\label{tab:dual_critic_full}
863	\footnotesize
864	\setlength{\tabcolsep}{3pt}
865	\begin{tabular}{llcccl}
866	\toprule
867	\textbf{Exp} & \textbf{Config} & \textbf{Params} & \textbf{NVE} & \textbf{Eval} & \textbf{Outcome} \\
868	\midrule
869	008d & Single narrow & 1.2M & 4.12$\times$ & 82.8 & Collapse \\
870	033 & Wide single & 2.4M & 4.75$\times$ & 407.9 & CIVO $\to$ self-repair \\
871	035 s0 & Narrow dual (min) & 1.2M & 2.75$\times$ & 697.8 & CIVO $\to$ recovery \\
872	039 s1 & Narrow dual (min) & 1.2M & 2.19$\times$ & 592.7 & CIVO $\to$ recovery \\
873	032 s0 & Wide dual (min) & 2.4M & $\leq$1.1$\times$ & 739.7 & CIVO prevented \\
874	032b s1 & Wide dual (min) & 2.4M & 1.4$\times$ & 551.8 & CIVO prevented \\
875	038 s2 & Wide dual (min) & 2.4M & $\leq$0.3$\times$ & 120.9$^*$ & Non-CIVO collapse \\
876	\midrule
877	\multicolumn{6}{l}{\textit{Cross-environment}} \\
878	034 & Cheetah dual & 2.4M & 1.75$\times$ & 97.5 & Partial recovery (31\%) \\
879	037 & Cheetah wide single & 2.4M & 3.60$\times$ & 146.1 & CIVO $\to$ self-repair \\
880	036 & PickCube dual & 2.4M & 2.3$\times$ & 27.7 & Transient CIVO \\
881	\bottomrule
882	\end{tabular}
883	\vspace{1pt}
884	{\raggedright\footnotesize $^*$CIVO prevented (NVE $\leq 0.3\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\par}
885	\end{table}
886	
887	\subsection{Critic Convergence (\texorpdfstring{$v_1 \approx v_2$}{v1 ≈ v2})}
888	
889	Across all dual-critic configurations and environments, the two critics converge to near-identical value functions. On Walker Walk, Pearson $\rho > 0.999$ between $v_1$ and $v_2$ outputs; on Cheetah Run and PickCube-v1, the gap is $< 0.2$ (exact match within numerical precision). Per-sample pessimism $\mathbb{E}[\max(v_1, v_2) - \min(v_1, v_2)]$ is 3--4\% of the theoretical bound for independent critics.
890	
891	This convergence occurs because both critics train on the same RSSM-generated latent features. Unlike model-free Double Q-learning, where each critic sees different mini-batches of real transitions and develops distinct function approximation errors, pure-imagination critics share identical inputs from the world model. The min operation therefore cannot provide the pessimism bias that makes Double Q effective in model-free settings.
892	
893	\subsection{Recovery vs.\ Prevention Mechanism}
894	
895	The $2{\times}2$ factorial reveals two separable dimensions:
896	
897	\paragraph{Recovery (min-dominated).} The min operation is the primary factor enabling recovery from CIVO. Both narrow dual-critic seeds experience CIVO and recover fully: exp\_035 (s0, $\nve = 2.75\times$, eval $33.8 \to 697.8$, recovery ratio $20.6\times$) and exp\_039 (s1, $\nve = 2.19\times$, eval $35.9 \to 592.7$, recovery ratio $16.5\times$). Both outperform wide single-critic (exp\_033, 2.4M params, eval 407.9) despite $2\times$ fewer parameters. The min operation reduces both peak CIVO severity (2.19--2.75$\times$ vs.\ 4.75$\times$ for the comparable single-critic) and enables consistent full recovery across seeds.
898	
899	\paragraph{Prevention (min $+$ capacity synergy).} CIVO prevention (NVE remaining below the $1.5\times$ threshold) requires both the min operation and increased capacity: only the wide dual-critic (exp\_032, 3 seeds) achieves this. The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.
900	
901	\paragraph{Cross-environment limits.} On Cheetah Run, the wide dual-critic (exp\_034) reduces NVE from $8.27\times$ (untreated baseline) to $1.75\times$ ($\geq 4\times$ reduction) but cannot prevent CIVO onset, and recovery reaches only 31\% of the pre-CIVO peak. This confirms that the min $+$ capacity synergy has environment-dependent limits: in high-CIVO-severity environments, architecture-level interventions attenuate but do not eliminate the pathology.
902	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "1372d623-d180-4dca-8d58-c3cd37429b3f"
}
```

</details>

---


### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 58800,
    "tool_uses": 12,
    "duration_ms": 25766
  },
  "last_tool_name": "Read",
  "uuid": "298f45c5-0185-4f9d-b3ee-b366e5740b89",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_012FQmcEUG5vCxX35SQjJ38W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 902,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "b0d013cc-54c0-45bb-9a07-54727555253f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LJJwQjgt2ddpGgFZXgNma1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13440,
      "cache_read_input_tokens": 44913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13440,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 76 · 2026-05-24T02:14:41.653Z_

<details><summary>↩ Tool result · `toolu_012FQmcEUG5vCxX35SQjJ38W`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (902). The file has 902 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "bbe093ad-7a3c-4dd9-be5c-b7e2feb63171"
}
```

</details>

---


### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Finding **/nve_sensitivity_table*.tex",
  "usage": {
    "total_tokens": 58971,
    "tool_uses": 13,
    "duration_ms": 28720
  },
  "last_tool_name": "Glob",
  "uuid": "390705e3-17ee-4586-b288-ec001d51398a",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Glob · `toolu_01BuoZQWGW4noX7811aCj4Pg`</summary>

```json
{
  "pattern": "**/nve_sensitivity_table*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "7fbfe359-ed4d-41ca-9733-1fb535f9cf2e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FNow5nZuyh1hhK2nvxMx3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 169,
      "cache_read_input_tokens": 58353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 169,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 79 · 2026-05-24T02:14:44.624Z_

<details><summary>↩ Tool result · `toolu_01BuoZQWGW4noX7811aCj4Pg`</summary>

```text
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
artifacts/_project/paper/nve_sensitivity_table.tex
paper/tables/nve_sensitivity_table.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "2ebab06c-1f28-46ad-af85-362ad025f73b"
}
```

</details>

---


### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Finding **/detector_table.tex",
  "usage": {
    "total_tokens": 58972,
    "tool_uses": 14,
    "duration_ms": 29278
  },
  "last_tool_name": "Glob",
  "uuid": "b5f31e26-26d6-46b5-a1f1-44f8d8d510c8",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Glob · `toolu_01MvPVqi6z8oH73KyvpZV69q`</summary>

```json
{
  "pattern": "**/detector_table.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "595cbe10-ae14-40c2-9128-6cfccff52041",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FNow5nZuyh1hhK2nvxMx3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 169,
      "cache_read_input_tokens": 58353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 169,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 82 · 2026-05-24T02:14:45.181Z_

<details><summary>↩ Tool result · `toolu_01MvPVqi6z8oH73KyvpZV69q`</summary>

```text
artifacts/analysis/detector_table.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "0403f296-7fb7-4506-97d3-3da78834fa76"
}
```

</details>

---


### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Running Parse registry JSON and extract requested experiment data",
  "usage": {
    "total_tokens": 14584,
    "tool_uses": 1,
    "duration_ms": 18759
  },
  "last_tool_name": "Bash",
  "uuid": "ce694a3a-62e1-465c-885e-6c5fb65086a8",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01MP3ke2mHFomS1pZheU92Zt`</summary>

```json
{
  "command": "python3 - << 'PYEOF'\nimport json, re\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ninner = json.loads(outer[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\nprint(f\"Total experiments: {inner['data']['count']} / {inner['data']['total']}\")\nprint(f\"Baseline: {inner['data']['baseline']}\")\nprint()\n\ndef report_exp(exp_id, exp):\n    print(f\"  exp_id: {exp_id}\")\n    print(f\"  status: {exp.get('status')}\")\n    print(f\"  description: {exp.get('description','')}\")\n    print(f\"  tags: {exp.get('tags','')}\")\n    print(f\"  conclusion: {exp.get('conclusion','')}\")\n    print(f\"  metrics: {json.dumps(exp.get('metrics',{}), indent=4)}\")\n    print()\n\n# 1. CIVO trigger experiments\nprint(\"=\"*60)\nprint(\"1. CIVO TRIGGER EXPERIMENTS\")\nprint(\"=\"*60)\ncivo = {k:v for k,v in experiments.items() if 'civo' in k.lower() or 'civo' in str(v.get('description','')).lower() or 'civo' in str(v.get('tags','')).lower()}\nprint(f\"Found {len(civo)}: {list(civo.keys())}\")\nfor k,v in sorted(civo.items()):\n    report_exp(k, v)\n\n# 2. Frozen dt_emb experiments\nprint(\"=\"*60)\nprint(\"2. FROZEN DT_EMB EXPERIMENTS\")\nprint(\"=\"*60)\nfrozen = {k:v for k,v in experiments.items() if 'frozen' in k.lower() or 'frozen' in str(v.get('description','')).lower() or 'frozen' in str(v.get('conclusion','')).lower()}\nprint(f\"Found {len(frozen)}: {list(frozen.keys())}\")\nfor k,v in sorted(frozen.items()):\n    report_exp(k, v)\n\n# 3. Manipulation / PickCube / PegInsertion\nprint(\"=\"*60)\nprint(\"3. MANIPULATION / PICKCUBE / PEGINSERTION EXPERIMENTS\")\nprint(\"=\"*60)\nmanip_keys = ['pickcube','peginsertion','peg','manipulation']\nmanip = {k:v for k,v in experiments.items() if any(m in k.lower() or m in str(v.get('description','')).lower() or m in str(v.get('tags','')).lower() for m in manip_keys)}\nprint(f\"Found {len(manip)}: {list(manip.keys())}\")\nfor k,v in sorted(manip.items()):\n    report_exp(k, v)\n\n# 4. Walker baseline\nprint(\"=\"*60)\nprint(\"4. WALKER BASELINE EXPERIMENTS\")\nprint(\"=\"*60)\nwalker_ids = ['exp_009d_baseline_walker_s0','exp_009d_baseline_walker_s1','exp_009a_baseline_walker_s2']\n# also search broadly\nwalker_all = {k:v for k,v in experiments.items() if 'walker' in k.lower() or 'walker' in str(v.get('description','')).lower()}\nprint(f\"All walker experiments ({len(walker_all)}): {list(walker_all.keys())}\")\nfor k,v in sorted(walker_all.items()):\n    report_exp(k, v)\n\n# 5. Cheetah baseline\nprint(\"=\"*60)\nprint(\"5. CHEETAH BASELINE EXPERIMENTS\")\nprint(\"=\"*60)\ncheetah = {k:v for k,v in experiments.items() if 'cheetah' in k.lower() or 'cheetah' in str(v.get('description','')).lower()}\nprint(f\"Found {len(cheetah)}: {list(cheetah.keys())}\")\nfor k,v in sorted(cheetah.items()):\n    report_exp(k, v)\n\n# 6. exp_057 and exp_058\nprint(\"=\"*60)\nprint(\"6. EXP_057 AND EXP_058\")\nprint(\"=\"*60)\nfor target in ['exp_057','exp_058']:\n    matches = {k:v for k,v in experiments.items() if k.startswith(target)}\n    print(f\"Matches for {target}: {list(matches.keys())}\")\n    for k,v in sorted(matches.items()):\n        report_exp(k, v)\n\n# 7. Any experiment with \"frozen\" in name (already covered but name-only)\nprint(\"=\"*60)\nprint(\"7. FROZEN IN NAME (name-only search)\")\nprint(\"=\"*60)\nfrozen_name = {k:v for k,v in experiments.items() if 'frozen' in k.lower()}\nprint(f\"Found {len(frozen_name)}: {list(frozen_name.keys())}\")\nfor k,v in sorted(frozen_name.items()):\n    report_exp(k, v)\n\n# 8. NVE in metrics or conclusion\nprint(\"=\"*60)\nprint(\"8. ALL EXPERIMENTS WITH NVE IN METRICS/CONCLUSION\")\nprint(\"=\"*60)\ndef has_nve(exp):\n    conc = str(exp.get('conclusion','')).lower()\n    metrics_str = json.dumps(exp.get('metrics',{})).lower()\n    return 'nve' in conc or 'nve' in metrics_str\n\nnve_exps = {k:v for k,v in experiments.items() if has_nve(v)}\nprint(f\"Found {len(nve_exps)}: {list(nve_exps.keys())}\")\nfor k,v in sorted(nve_exps.items()):\n    report_exp(k, v)\n\nPYEOF\n",
  "description": "Parse registry JSON and extract requested experiment data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "3f8fb75a-f49a-48d8-bb26-e68906cff6b8",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HuCd3bAJVaVVJWhiHd15G6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6464,
      "cache_read_input_tokens": 8115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6464,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading paper/tables/nve_sensitivity_table.tex",
  "usage": {
    "total_tokens": 59363,
    "tool_uses": 15,
    "duration_ms": 32067
  },
  "last_tool_name": "Read",
  "uuid": "c175de15-d475-46b2-a962-8b6a93dcb410",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Read · `toolu_017h6CUxDdPhbB1LV1QUpBXu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/tables/nve_sensitivity_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "eeaa76e1-02d6-4f6d-86a4-10b260859f4c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XMECrU9P58s96wWZHmS3zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 58522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 319,
        "ephemeral_1h_input_tokens": 0
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

_source line 87 · 2026-05-24T02:14:48.012Z_

<details><summary>↩ Tool result · `toolu_01MP3ke2mHFomS1pZheU92Zt`</summary>

```text
&lt;persisted-output>
Output too large (140.8KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt

Preview (first 2KB):
Total experiments: 132 / 132
Baseline: None

============================================================
1. CIVO TRIGGER EXPERIMENTS
============================================================
Found 11: ['exp_055_peginsertion_civo_trigger_s1', 'exp_050_peginsertion_civo_trigger_s0', 'exp_052_stackcube_civo_trigger_s1', 'exp_049_stackcube_civo_trigger_s0', 'exp_048_cheetah_civo_extension', 'exp_008d_civo_trigger_s4', 'exp_010b_cheetah_civo_trigger_s0', 'exp_010b_cheetah_civo_trigger', 'exp_019b_pickcube_civo_trigger', 'exp_008d_civo_trigger_s3', 'exp_008d_civo_trigger_s2']
  exp_id: exp_008d_civo_trigger_s2
  status: DONE
  description: 
  tags: 
  conclusion: killed
  metrics: {}

  exp_id: exp_008d_civo_trigger_s3
  status: DONE
  description: 
  tags: 
  conclusion: success
  metrics: {
    "baseline_eval_105K": 915.67,
    "collapse_onset_step": 95000,
    "collapse_type": "late-onset",
    "eval_return_final": 267.6,
    "eval_return_final_step": 105000,
    "eval_return_peak": 451.7,
    "eval_return_peak_step": 95000,
    "nve_final": 1.53,
    "nve_onset_step": 45000,
    "nve_onset_value": 1.5,
    "nve_peak": 1.53,
    "nve_peak_step": 105000,
    "nve_sustained_45K_55K": true,
    "total_steps": 112000,
    "train_return_final_avg": 138,
    "train_return_final_range": "82-214",
    "value_mean_final": 268.4,
    "vs_baseline_105K": "-70.8%"
}

  exp_id: exp_008d_civo_trigger_s4
  status: DONE
  description: 
  tags: 
  conclusion: success
  metrics: {
    "civo_alert_105K": 1,
    "civo_confirmed": true,
    "delta_ve_105K": 2.05,
    "eval_return_trajectory": {
        "105K": 63.6,
        "15K": 171.4,
        "25K": 189.5,
        "35K": 153.8,
        "45K": 158.2,
        "55K": 229.3,
        "5K": 30.9,
        "65K": 333.6,
        "75K": 302.4,
        "85K": 383.3,
        "95K": 240.3
    },
    "final_eval_return_105K": 63.6,
    "final_step": 112000,
    "gate_dt_2_frac": 1,
    "gate_dt_mean": 2,
    "peak_eval_return": 383.3,
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "0557c88c-94cf-493b-ac04-3f747fb2aee5"
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-24T02:14:47.970Z_

<details><summary>↩ Tool result · `toolu_017h6CUxDdPhbB1LV1QUpBXu`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\caption{NVE threshold sensitivity analysis for CIVO detection (summary). Task~B2 (main text) uses $\nve \geq 1.5\times$ yielding one false positive (008e\_v3\_s2, identified as non-CIVO Imagination-Reality Divergence). Task~B1 (Appendix~\ref{sec:appendix_sensitivity}) restricts the positive class to sustained CIVO ($n_{\text{pos}}=3$), achieving perfect rank separation ($\text{AUROC}=1.000$). All CIs are two-sided Clopper-Pearson exact binomial ($\alpha = 0.05$).}
4	\label{tab:nve_sensitivity}
5	\small
6	\setlength{\tabcolsep}{4pt}
7	\begin{tabular}{@{}lccccccc@{}}
8	\toprule
9	Task & Threshold & $n_{\text{pos}}/n_{\text{neg}}$ & AUROC & Accuracy & 95\% CI & F1 & Note \\
10	\midrule
11	B2 (main) & $\geq 1.5\times$ & 4\,/\,6 & 0.958 & 90.0\% & [55.5, 99.7] & 88.9\% & 1 FP (IRD) \\
12	B1 (app.) & $\geq 3.9\times$ & 3\,/\,7 & 1.000 & 100\% & [69.2, 100] & 100\% & $n_{\text{pos}}\!=\!3$ \\
13	\bottomrule
14	\end{tabular}
15	\end{table}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "f0cf1702-b6a5-4d14-bcd6-12938b0443fd"
}
```

</details>

---


### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading artifacts/_project/paper/nve_sensitivity_table.tex",
  "usage": {
    "total_tokens": 59435,
    "tool_uses": 16,
    "duration_ms": 32421
  },
  "last_tool_name": "Read",
  "uuid": "a80ece9e-7562-47aa-b74f-d8945fc047e2",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Read · `toolu_01T2k4zwjFZB18yPh6WTjCMs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "8d4d7ea6-ab0a-44ac-b9ac-b420e8f3bed0",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XMECrU9P58s96wWZHmS3zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 58522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 319,
        "ephemeral_1h_input_tokens": 0
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

_source line 91 · 2026-05-24T02:14:48.311Z_

<details><summary>↩ Tool result · `toolu_01T2k4zwjFZB18yPh6WTjCMs`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\caption{NVE threshold sensitivity analysis for CIVO detection. Task~B2 (main text) uses a 1.5$\times$ threshold yielding one false positive (008e\_v3\_s2, identified as non-CIVO Imagination-Reality Divergence). Task~B1 uses a stricter 1.7$\times$ threshold achieving perfect separation but with only 2 positive samples. All CIs are two-sided Clopper-Pearson exact binomial ($\alpha/2 = 0.025$).}
4	\label{tab:nve_sensitivity}
5	\small
6	\setlength{\tabcolsep}{4pt}
7	\begin{tabular}{@{}lcccccccl@{}}
8	\toprule
9	Task & Threshold & $n$ & Pos/Neg & AUROC & Accuracy & CP 95\% CI & Margin & Note \\
10	\midrule
11	B2 (main) & $\geq 1.5\times$ & 8 & 3\,/\,5 & 0.933 & 87.5\% & [0.474, 0.997] & $-2.16$ & 1 FP (008e\_v3\_s2: IRD) \\
12	B1 (sens.) & $\geq 1.7\times$ & 8 & 2\,/\,6 & 1.000 & 100\% & [0.631, 1.000] & $+0.35$ & $n_{\text{pos}}=2$, low power \\
13	\bottomrule
14	\end{tabular}
15	
16	\vspace{4pt}
17	\noindent\small\textit{The stricter 1.7$\times$ threshold (B1) achieves perfect separation but with only $n_{\text{pos}}=2$, limiting statistical power. The 1.5$\times$ threshold (B2) increases recall at the cost of one false positive driven by non-CIVO Imagination-Reality Divergence.}
18	\end{table}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "e9392b04-37a3-46e4-af97-264e290df589"
}
```

</details>

---


### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 18064,
    "tool_uses": 2,
    "duration_ms": 21952
  },
  "last_tool_name": "Read",
  "uuid": "158fa9a0-0843-4a6b-9c6b-e855f569110e",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Read · `toolu_014Va8SEwZFj6qpfiRDurgzH`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "7980cfc0-6a14-45e6-8d48-af82b6404e53",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RtSaHU2bVLo8V3Yy42hM3D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3480,
      "cache_read_input_tokens": 14579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3480,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading artifacts/_project/paper/nve_sensitivity_table_37b680.tex",
  "usage": {
    "total_tokens": 60752,
    "tool_uses": 17,
    "duration_ms": 35227
  },
  "last_tool_name": "Read",
  "uuid": "2f65a7d4-a84f-45ee-81e6-8cf08f868a33",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 95_

<details open><summary>🔧 Tool call — Read · `toolu_01MN1Z1kQn8uNSQiJaVGSGe9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table_37b680.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "931a7a0d-e14c-4215-a87e-a2679ab584e3",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019UGUQoAyjki2XsfGU1aZDU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 58841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1249,
        "ephemeral_1h_input_tokens": 0
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

_source line 96 · 2026-05-24T02:14:51.113Z_

<details><summary>↩ Tool result · `toolu_01MN1Z1kQn8uNSQiJaVGSGe9`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\caption{NVE threshold sensitivity analysis for CIVO detection. Task~B2 (main text) uses a 1.5$\times$ threshold yielding one false positive (008e\_v3\_s2, identified as non-CIVO Imagination-Reality Divergence). Task~B1 uses a stricter 1.7$\times$ threshold achieving perfect separation but with only 2 positive samples. All CIs are two-sided Clopper-Pearson exact binomial ($\alpha/2 = 0.025$).}
4	\label{tab:nve_sensitivity}
5	\small
6	\setlength{\tabcolsep}{4pt}
7	\begin{tabular}{@{}lcccccccl@{}}
8	\toprule
9	Task & Threshold & $n$ & Pos/Neg & AUROC & Accuracy & CP 95\% CI & Margin & Note \\
10	\midrule
11	B2 (main) & $\geq 1.5\times$ & 8 & 3\,/\,5 & 0.933 & 87.5\% & [0.474, 0.997] & $-2.16$ & 1 FP (008e\_v3\_s2: IRD) \\
12	B1 (sens.) & $\geq 1.7\times$ & 8 & 2\,/\,6 & 1.000 & 100\% & [0.631, 1.000] & $+0.35$ & $n_{\text{pos}}=2$, low power \\
13	\bottomrule
14	\end{tabular}
15	
16	\vspace{4pt}
17	\noindent\small\textit{The stricter 1.7$\times$ threshold (B1) achieves perfect separation but with only $n_{\text{pos}}=2$, limiting statistical power. The 1.5$\times$ threshold (B2) increases recall at the cost of one false positive driven by non-CIVO Imagination-Reality Divergence.}
18	\end{table}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "4a6ea31b-8f3c-4e22-b2cd-62b92b1611aa"
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-24T02:14:51.347Z_

<details><summary>↩ Tool result · reported error · `toolu_014Va8SEwZFj6qpfiRDurgzH`</summary>

```text
File content (60381 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "e1002ac1-e638-4cc6-b006-efec87d6d020",
  "tool_use_result": "Error: File content (60381 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "description": "Reading artifacts/analysis/detector_table.tex",
  "usage": {
    "total_tokens": 60820,
    "tool_uses": 18,
    "duration_ms": 35473
  },
  "last_tool_name": "Read",
  "uuid": "046640fe-24e8-459d-9cf5-758833a16f1a",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Read · `toolu_01EZipg7j6Tp9rgNL5qJzrPY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/detector_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "d4e2da6f-7478-417a-a31e-6eb2315c55b1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019UGUQoAyjki2XsfGU1aZDU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 58841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1249,
        "ephemeral_1h_input_tokens": 0
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

_source line 100 · 2026-05-24T02:14:51.364Z_

<details><summary>↩ Tool result · `toolu_01EZipg7j6Tp9rgNL5qJzrPY`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{CIVO Detector Validation Results. Trigger Step indicates when the detector first fires. Detection Type classifies timing relative to 20\% eval decline from peak.}
4	\label{tab:detector-validation}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{llcccccc}
7	\toprule
8	Experiment & Config & Verdict & Trigger & Det. Type & Peak Eval & $r_\text{ve}$@trig \\
9	\midrule
10	  exp\_008d\_s0 & dt_embed, subsample_on, h=8,.. & TP & 45K & predictive & 167 & 0.69 \\
11	  exp\_010b\_cheetah & dt_embed, cheetah, seed=1 & TP & 65K & reactive & 322 & 3.18 \\
12	  exp\_008d\_s3 & dt_embed, subsample_on, seed=3 & TP & 45K & predictive & 452 & 0.50 \\
13	  exp\_008f\_s3 & no_dt_embed, subsample_on, s.. & TN & -- & -- & 594 & -- \\
14	  exp\_009c\_008f\_s2 & no_dt_embed, walker, seed=2 & FP & 105K & reactive & 359 & 0.75 \\
15	  exp\_009b\_008d\_walker\_s2 & dt_embed, walker, seed=2 (se.. & TN & -- & -- & 279 & -- \\
16	  exp\_009a\_baseline\_walker\_s2 & vanilla DreamerV3 baseline, .. & FP & 85K & predictive & 967 & 0.73 \\
17	  baseline\_s1 & vanilla DreamerV3 baseline, .. & TN & -- & -- & 970 & -- \\
18	  exp\_009d\_baseline\_walker\_s0 & vanilla DreamerV3 baseline, .. & TN & -- & -- & 951 & -- \\
19	  exp\_009d\_baseline\_walker\_s1 & vanilla DreamerV3 baseline, .. & TN & -- & -- & 920 & -- \\
20	\midrule
21	  \multicolumn{7}{l}{TPR = 3/3 (1.00), FPR = 2/7 (0.286)} \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "b1b089b4-31f2-4aee-92ea-e77edfca4391"
}
```

</details>

---


### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 18343,
    "tool_uses": 3,
    "duration_ms": 25199
  },
  "last_tool_name": "Read",
  "uuid": "85a44f18-5aa4-4d87-baa2-2868d5c99862",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 102_

<details open><summary>🔧 Tool call — Read · `toolu_01Duzk1fNN1A9eUcrRnrCWwc`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "6c0c87e6-ccd3-4398-8789-f57d63319ce3",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q9531AWH3UX53xvkW4JP34",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 18059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 207,
        "ephemeral_1h_input_tokens": 0
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

_source line 103 · 2026-05-24T02:14:54.348Z_

<details><summary>↩ Tool result · `toolu_01Duzk1fNN1A9eUcrRnrCWwc`</summary>

```text
1	Total experiments: 132 / 132
2	Baseline: None
3	
4	============================================================
5	1. CIVO TRIGGER EXPERIMENTS
6	============================================================
7	Found 11: ['exp_055_peginsertion_civo_trigger_s1', 'exp_050_peginsertion_civo_trigger_s0', 'exp_052_stackcube_civo_trigger_s1', 'exp_049_stackcube_civo_trigger_s0', 'exp_048_cheetah_civo_extension', 'exp_008d_civo_trigger_s4', 'exp_010b_cheetah_civo_trigger_s0', 'exp_010b_cheetah_civo_trigger', 'exp_019b_pickcube_civo_trigger', 'exp_008d_civo_trigger_s3', 'exp_008d_civo_trigger_s2']
8	  exp_id: exp_008d_civo_trigger_s2
9	  status: DONE
10	  description: 
11	  tags: 
12	  conclusion: killed
13	  metrics: {}
14	
15	  exp_id: exp_008d_civo_trigger_s3
16	  status: DONE
17	  description: 
18	  tags: 
19	  conclusion: success
20	  metrics: {
21	    "baseline_eval_105K": 915.67,
22	    "collapse_onset_step": 95000,
23	    "collapse_type": "late-onset",
24	    "eval_return_final": 267.6,
25	    "eval_return_final_step": 105000,
26	    "eval_return_peak": 451.7,
27	    "eval_return_peak_step": 95000,
28	    "nve_final": 1.53,
29	    "nve_onset_step": 45000,
30	    "nve_onset_value": 1.5,
31	    "nve_peak": 1.53,
32	    "nve_peak_step": 105000,
33	    "nve_sustained_45K_55K": true,
34	    "total_steps": 112000,
35	    "train_return_final_avg": 138,
36	    "train_return_final_range": "82-214",
37	    "value_mean_final": 268.4,
38	    "vs_baseline_105K": "-70.8%"
39	}
40	
41	  exp_id: exp_008d_civo_trigger_s4
42	  status: DONE
43	  description: 
44	  tags: 
45	  conclusion: success
46	  metrics: {
47	    "civo_alert_105K": 1,
48	    "civo_confirmed": true,
49	    "delta_ve_105K": 2.05,
50	    "eval_return_trajectory": {
51	        "105K": 63.6,
52	        "15K": 171.4,
53	        "25K": 189.5,
54	        "35K": 153.8,
55	        "45K": 158.2,
56	        "55K": 229.3,
57	        "5K": 30.9,
58	        "65K": 333.6,
59	        "75K": 302.4,
60	        "85K": 383.3,
61	        "95K": 240.3
62	    },
63	    "final_eval_return_105K": 63.6,
64	    "final_step": 112000,
65	    "gate_dt_2_frac": 1,
66	    "gate_dt_mean": 2,
67	    "peak_eval_return": 383.3,
68	    "peak_eval_step": 85000,
69	    "target_step": 105000,
70	    "value_mean_105K": 192.65,
71	    "value_mean_95K": 235.42,
72	    "ve_ratio_105K": 3.03
73	}
74	
75	  exp_id: exp_010b_cheetah_civo_trigger
76	  status: DONE
77	  description: 
78	  tags: 
79	  conclusion: success
80	  metrics: {
81	    "civo": true,
82	    "eval_return_final": 51.7,
83	    "eval_return_peak": 321.9,
84	    "nve_peak": 8.27,
85	    "nve_peak_step": 65000,
86	    "peak_step": 35000
87	}
88	
89	  exp_id: exp_010b_cheetah_civo_trigger_s0
90	  status: DONE
91	  description: 
92	  tags: 
93	  conclusion: success
94	  metrics: {
95	    "civo": true,
96	    "civo_onset_step": "65K",
97	    "detector_alert_step": "95K",
98	    "eval_return_105K": 0.83,
99	    "eval_return_peak": 247.77,
100	    "eval_return_peak_step": "35K",
101	    "gate_dt_mean": 2,
102	    "gate_entropy": 0,
103	    "nve_105K": 70.64,
104	    "nve_95K": 6.34
105	}
106	
107	  exp_id: exp_019b_pickcube_civo_trigger
108	  status: DONE
109	  description: 
110	  tags: 
111	  conclusion: success
112	  metrics: {
113	    "baseline_eval_final": 58.56,
114	    "baseline_ratio": 0.455,
115	    "eval_return_final": 26.64,
116	    "eval_return_peak": 26.9,
117	    "eval_return_peak_step": 132500,
118	    "gate_dt_2_frac": 1,
119	    "gate_entropy": 0,
120	    "nve_final": 0.065,
121	    "nve_peak": 3.78,
122	    "nve_peak_step": 52500,
123	    "pattern": "transient_civo_then_value_collapse",
124	    "total_steps": 200000,
125	    "value_baseline_final": 144.57,
126	    "value_mean_final": 4.26
127	}
128	
129	  exp_id: exp_048_cheetah_civo_extension
130	  status: DONE
131	  description: 
132	  tags: 
133	  conclusion: success
134	  metrics: {
135	    "eval_final": 23.4,
136	    "eval_final_step": 302000,
137	    "eval_peak": 32.8,
138	    "eval_peak_step": 252000,
139	    "ve_ratio_initial": 46.3,
140	    "ve_ratio_peak": 24.112,
141	    "ve_ratio_peak_step": 162000,
142	    "ve_ratio_final": 1.803,
143	    "nve_initial": 70.64,
144	    "nve_peak_secondary": 36.76,
145	    "nve_final": 2.75,
146	    "total_steps": 312000,
147	    "civo_self_corrected": false,
148	    "civo_correction_pct": 96,
149	    "secondary_burst_step": 152000,
150	    "secondary_burst_nve": 36.47,
151	    "gate_collapsed": true
152	}
153	
154	  exp_id: exp_049_stackcube_civo_trigger_s0
155	  status: DONE
156	  description: 
157	  tags: 
158	  conclusion: success
159	  metrics: {
160	    "eval_final": 34.88,
161	    "eval_final_step": 212500,
162	    "eval_peak": 35.89,
163	    "eval_peak_step": 182500,
164	    "ve_ratio_final": 0.186,
165	    "ve_ratio_final_step": 212500,
166	    "ve_ratio_peak": 5.05,
167	    "ve_ratio_peak_step": 42500,
168	    "total_steps": 222500,
169	    "total_episodes": 1112
170	}
171	
172	  exp_id: exp_050_peginsertion_civo_trigger_s0
173	  status: DONE
174	  description: 
175	  tags: 
176	  conclusion: success
177	  metrics: {
178	    "ve_ratio_peak": 10.05,
179	    "ve_ratio_peak_step": 82500,
180	    "ve_ratio_final": 0.379,
181	    "ve_ratio_final_step": 212500,
182	    "civo_self_corrected": true,
183	    "civo_correction_delay_steps": 130000,
184	    "eval_final": 20.86,
185	    "eval_final_step": 212500,
186	    "eval_peak": 20.86,
187	    "eval_peak_step": 212500,
188	    "total_steps": 222400
189	}
190	
191	  exp_id: exp_052_stackcube_civo_trigger_s1
192	  status: DONE
193	  description: 
194	  tags: 
195	  conclusion: success
196	  metrics: {
197	    "eval_final": 29.458,
198	    "eval_final_step": 212500,
199	    "eval_peak": 39.873,
200	    "eval_peak_step": 162500,
201	    "ve_ratio_final": 0.133,
202	    "ve_ratio_final_step": 212500,
203	    "ve_ratio_peak": 4.67,
204	    "ve_ratio_peak_step": 52500,
205	    "total_steps": 222400
206	}
207	
208	  exp_id: exp_055_peginsertion_civo_trigger_s1
209	  status: DONE
210	  description: 
211	  tags: 
212	  conclusion: success
213	  metrics: {
214	    "total_steps": 222400,
215	    "ve_ratio_peak": 3.08,
216	    "ve_ratio_peak_step": 92500,
217	    "ve_ratio_final": 0.498,
218	    "ve_ratio_final_step": 212500,
219	    "eval_return_final": 11.44,
220	    "eval_return_final_step": 212500,
221	    "eval_return_peak": 24.05,
222	    "eval_return_peak_step": 112500,
223	    "nve_classification": "transient",
224	    "civo_triggered": true,
225	    "civo_self_corrected": "partial",
226	    "note": "CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 \u2014 severity seed-dependent.",
227	    "ve_ratio_trajectory": {
228	        "12500": 0.19,
229	        "22500": 0.81,
230	        "32500": 1.35,
231	        "42500": 2.0,
232	        "52500": 2.39,
233	        "62500": 2.85,
234	        "72500": 2.28,
235	        "82500": 2.48,
236	        "92500": 3.08,
237	        "102500": 2.51,
238	        "112500": 0.91,
239	        "122500": 1.21,
240	        "132500": 1.36,
241	        "142500": 0.75,
242	        "152500": 0.55,
243	        "162500": 1.17,
244	        "172500": 0.96,
245	        "182500": 0.94,
246	        "192500": 0.9,
247	        "202500": 0.73,
248	        "212500": 0.5
249	    }
250	}
251	
252	============================================================
253	2. FROZEN DT_EMB EXPERIMENTS
254	============================================================
255	Found 10: ['exp_058_frozen_dt_emb_cheetah_s1', 'exp_056_peginsertion_frozen_s1', 'exp_057_frozen_dt_emb_walker_s2', 'exp_054_pickcube_frozen_s0', 'exp_053_peginsertion_frozen_s0', 'exp_051_stackcube_frozen_dt_emb_s0', 'exp_047_frozen_dt_emb_walker_s1', 'exp_046_frozen_dt_emb_cheetah', 'exp_042_frozen_dt_emb_walker', 'exp_015b_frozen_dt_emb']
256	  exp_id: exp_015b_frozen_dt_emb
257	  status: DONE
258	  description: 
259	  tags: 
260	  conclusion: negative
261	  metrics: {
262	    "actor_entropy_105K": -4.855,
263	    "actor_loss_105K": 0.000179,
264	    "collapse_mechanism": "gradient_starvation_from_frozen_dt_emb",
265	    "data_source": "worker SSH final analysis 2026-05-15T18:30",
266	    "eval_return_105K": 204.2,
267	    "eval_return_15K": 167.9,
268	    "eval_return_25K": 171.8,
269	    "eval_return_35K": 201.6,
270	    "eval_return_45K": 122.3,
271	    "eval_return_55K": 105.8,
272	    "eval_return_5K": 31,
273	    "eval_return_65K": 160.3,
274	    "eval_return_75K": 80,
275	    "eval_return_85K": 183.5,
276	    "eval_return_95K": 238.4,
277	    "final_eval": 204.2,
278	    "final_step": 112000,
279	    "gate_dt_1_frac": 0,
280	    "gate_dt_mean": 2,
281	    "nve_105K": 0.42,
282	    "nve_85K": 0.467,
283	    "nve_95K": 0.394,
284	    "summary": "NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss\u21920 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence",
285	    "value_mean_105K": 56.212,
286	    "value_std_105K": 13.818
287	}
288	
289	  exp_id: exp_042_frozen_dt_emb_walker
290	  status: DONE
291	  description: 
292	  tags: 
293	  conclusion: success
294	  metrics: {
295	    "eval_final": 612.45,
296	    "eval_peak": 682.38,
297	    "eval_peak_step": 205000,
298	    "nve_peak": 0.194,
299	    "nve_final": 0.051,
300	    "civo_alert": false,
301	    "total_steps": 224000,
302	    "total_train_episodes": 224
303	}
304	
305	  exp_id: exp_046_frozen_dt_emb_cheetah
306	  status: DONE
307	  description: 
308	  tags: 
309	  conclusion: success
310	  metrics: {
311	    "eval_final": 150.5,
312	    "eval_peak": 207.4,
313	    "eval_peak_step": 145000,
314	    "ve_ratio_peak": 0.4,
315	    "ve_ratio_final": 0.1,
316	    "nve_peak": 1.35,
317	    "nve_peak_step": 45000,
318	    "nve_final": 0.17,
319	    "total_steps": 224000,
320	    "civo_alert_count": 0
321	}
322	
323	  exp_id: exp_047_frozen_dt_emb_walker_s1
324	  status: DONE
325	  description: 
326	  tags: 
327	  conclusion: success
328	  metrics: {
329	    "eval_final": 144.22,
330	    "eval_final_step": 215000,
331	    "eval_peak": 408.79,
332	    "eval_peak_step": 125000,
333	    "ve_ratio_peak": 1.099,
334	    "ve_ratio_peak_step": 75000,
335	    "ve_ratio_final": 0.277,
336	    "nve_peak": 1.71,
337	    "nve_peak_step": 95000,
338	    "nve_final_105k": 0.56,
339	    "total_steps": 225000
340	}
341	
342	  exp_id: exp_051_stackcube_frozen_dt_emb_s0
343	  status: DONE
344	  description: 
345	  tags: 
346	  conclusion: success
347	  metrics: {
348	    "ve_ratio_peak": 4.3,
349	    "ve_ratio_peak_step": 42500,
350	    "ve_ratio_final": 0.122,
351	    "ve_ratio_final_step": 212500,
352	    "eval_final": 45.31,
353	    "eval_final_step": 212500,
354	    "eval_peak": 45.31,
355	    "eval_peak_step": 212500,
356	    "total_steps": 222400
357	}
358	
359	  exp_id: exp_053_peginsertion_frozen_s0
360	  status: DONE
361	  description: 
362	  tags: 
363	  conclusion: success
364	  metrics: {}
365	
366	  exp_id: exp_054_pickcube_frozen_s0
367	  status: DONE
368	  description: 
369	  tags: 
370	  conclusion: success
371	  metrics: {}
372	
373	  exp_id: exp_056_peginsertion_frozen_s1
374	  status: DONE
375	  description: 
376	  tags: 
377	  conclusion: success
378	  metrics: {
379	    "total_steps": 222500,
380	    "ve_ratio_peak": 11.321,
381	    "ve_ratio_peak_step": 82500,
382	    "ve_ratio_final": 1.193,
383	    "ve_ratio_final_step": 212500,
384	    "eval_return_final": 4.37,
385	    "eval_return_final_step": 212500,
386	    "eval_return_peak": 24.42,
387	    "eval_return_peak_step": 132500,
388	    "nve_classification": "burst",
389	    "note": "Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 \u2014 frozen does NOT suppress ManiSkill transients.",
390	    "ve_ratio_trajectory": {
391	        "12500": 0.316,
392	        "22500": 0.975,
393	        "32500": 1.839,
394	        "42500": 1.966,
395	        "52500": 5.422,
396	        "62500": 4.047,
397	        "72500": 8.408,
398	        "82500": 11.321,
399	        "92500": 3.724,
400	        "102500": 3.034,
401	        "112500": 2.204,
402	        "122500": 2.425,
403	        "132500": 0.842,
404	        "142500": 2.194,
405	        "152500": 2.203,
406	        "162500": 0.651,
407	        "172500": 1.085,
408	        "182500": 1.07,
409	        "192500": 0.467,
410	        "202500": 0.708,
411	        "212500": 1.193
412	    }
413	}
414	
415	  exp_id: exp_057_frozen_dt_emb_walker_s2
416	  status: DONE
417	  description: 
418	  tags: 
419	  conclusion: success
420	  metrics: {
421	    "total_steps": 225000,
422	    "ve_ratio_peak": 1.283,
423	    "ve_ratio_peak_step": 115000,
424	    "ve_ratio_final": 0.177,
425	    "ve_ratio_final_step": 215000,
426	    "nve_peak": 1.88,
427	    "nve_peak_step": 115000,
428	    "nve_classification": "transient",
429	    "note": "Walker frozen s2. NVE=1.88\u00d7 (raw 1.283 / baseline 0.683 @115K). Peak transient at 115K, self-corrected. Walker frozen n=3: s0=0.19, s1=1.71, s2=1.88 \u2014 all transient, no sustained CIVO."
430	}
431	
432	  exp_id: exp_058_frozen_dt_emb_cheetah_s1
433	  status: DONE
434	  description: 
435	  tags: 
436	  conclusion: success
437	  metrics: {
438	    "total_steps": 224000,
439	    "ve_ratio_peak": 0.231,
440	    "ve_ratio_peak_step": 45000,
441	    "ve_ratio_final": 0.107,
442	    "ve_ratio_final_step": 215000,
443	    "eval_return_final": 80.46,
444	    "eval_return_final_step": 215000,
445	    "eval_return_peak": 191.74,
446	    "eval_return_peak_step": 25000,
447	    "nve_peak": 0.78,
448	    "nve_peak_step": 45000,
449	    "nve_classification": "no_civo",
450	    "note": "Cheetah frozen s1. NVE=0.78\u00d7 (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 \u2014 both clean, frozen \u7a33\u5065\u963b\u6b62 extreme CIVO (trained NVE 70-108)."
451	}
452	
453	============================================================
454	3. MANIPULATION / PICKCUBE / PEGINSERTION EXPERIMENTS
455	============================================================
456	Found 11: ['exp_056_peginsertion_frozen_s1', 'exp_055_peginsertion_civo_trigger_s1', 'exp_054_pickcube_frozen_s0', 'exp_053_peginsertion_frozen_s0', 'exp_050_peginsertion_civo_trigger_s0', 'exp_036_dual_critic_pickcube', 'exp_031b_tcn_pickcube_s0_sigma05', 'exp_031_tcn_pickcube_s0_sigma02', 'exp_019b_pickcube_civo_trigger', 'exp_019a_v2_pickcube_baseline', 'exp_019a_pickcube_baseline']
457	  exp_id: exp_019a_pickcube_baseline
458	  status: DONE
459	  description: 
460	  tags: 
461	  conclusion: killed
462	  metrics: {}
463	
464	  exp_id: exp_019a_v2_pickcube_baseline
465	  status: DONE
466	  description: 
467	  tags: 
468	  conclusion: success
469	  metrics: {
470	    "eval_return_final": 69.43,
471	    "eval_return_peak": 69.7,
472	    "eval_return_peak_step": 162500,
473	    "steps_completed": 200248,
474	    "value_mean_final": 143.4,
475	    "ve_ratio_final": 2.07,
476	    "ve_ratio_range": "1.05-3.56"
477	}
478	
479	  exp_id: exp_019b_pickcube_civo_trigger
480	  status: DONE
481	  description: 
482	  tags: 
483	  conclusion: success
484	  metrics: {
485	    "baseline_eval_final": 58.56,
486	    "baseline_ratio": 0.455,
487	    "eval_return_final": 26.64,
488	    "eval_return_peak": 26.9,
489	    "eval_return_peak_step": 132500,
490	    "gate_dt_2_frac": 1,
491	    "gate_entropy": 0,
492	    "nve_final": 0.065,
493	    "nve_peak": 3.78,
494	    "nve_peak_step": 52500,
495	    "pattern": "transient_civo_then_value_collapse",
496	    "total_steps": 200000,
497	    "value_baseline_final": 144.57,
498	    "value_mean_final": 4.26
499	}
500	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "2d33e9d1-90a9-48cd-b59f-4ef9fa10a141"
}
```

</details>

---


### System

_source line 104_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 25512,
    "tool_uses": 4,
    "duration_ms": 29698
  },
  "last_tool_name": "Read",
  "uuid": "08faf730-3ccc-476f-a026-8244833ed502",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Read · `toolu_01ThjVm4uZXG5gKmRPnXytYP`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "445ab392-4b97-4f4e-bbda-6af0f35b7530",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VKcACh2bBu5TNt7jYwS76f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7131,
      "cache_read_input_tokens": 18266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 106 · 2026-05-24T02:14:58.836Z_

<details><summary>↩ Tool result · `toolu_01ThjVm4uZXG5gKmRPnXytYP`</summary>

```text
500	
501	  exp_id: exp_031_tcn_pickcube_s0_sigma02
502	  status: DONE
503	  description: 
504	  tags: 
505	  conclusion: negative
506	  metrics: {
507	    "eval_peak": 28.6,
508	    "eval_peak_step": 162500,
509	    "eval_return_132K": 23.45,
510	    "eval_return_152K": 23.1,
511	    "eval_return_192K": 11.6,
512	    "gate_dt2_frac": 1.0,
513	    "gate_entropy": 0,
514	    "step": 195600,
515	    "train_return_range": "18-25",
516	    "ve_ratio_latest": 0.18,
517	    "ve_ratio_peak": 3.71
518	}
519	
520	  exp_id: exp_031b_tcn_pickcube_s0_sigma05
521	  status: DONE
522	  description: 
523	  tags: 
524	  conclusion: negative
525	  metrics: {
526	    "eval_reward_final": 25.5,
527	    "eval_reward_last5_avg": 25.9,
528	    "eval_reward_peak": 29.1,
529	    "nve_final": 0.2,
530	    "nve_peak": 3.3,
531	    "nve_peak_step": 42500,
532	    "nve_suppressed_from_step": 72500,
533	    "total_episodes": 1062,
534	    "total_steps": 212400
535	}
536	
537	  exp_id: exp_036_dual_critic_pickcube
538	  status: DONE
539	  description: 
540	  tags: 
541	  conclusion: negative
542	  metrics: {
543	    "civo_alert": 0,
544	    "eval_return_final": 27.7,
545	    "eval_return_peak": 27.7,
546	    "gate_dt_2_frac": 1,
547	    "nve_final": 0.2,
548	    "nve_peak": 2.3,
549	    "steps": 212447
550	}
551	
552	  exp_id: exp_050_peginsertion_civo_trigger_s0
553	  status: DONE
554	  description: 
555	  tags: 
556	  conclusion: success
557	  metrics: {
558	    "ve_ratio_peak": 10.05,
559	    "ve_ratio_peak_step": 82500,
560	    "ve_ratio_final": 0.379,
561	    "ve_ratio_final_step": 212500,
562	    "civo_self_corrected": true,
563	    "civo_correction_delay_steps": 130000,
564	    "eval_final": 20.86,
565	    "eval_final_step": 212500,
566	    "eval_peak": 20.86,
567	    "eval_peak_step": 212500,
568	    "total_steps": 222400
569	}
570	
571	  exp_id: exp_053_peginsertion_frozen_s0
572	  status: DONE
573	  description: 
574	  tags: 
575	  conclusion: success
576	  metrics: {}
577	
578	  exp_id: exp_054_pickcube_frozen_s0
579	  status: DONE
580	  description: 
581	  tags: 
582	  conclusion: success
583	  metrics: {}
584	
585	  exp_id: exp_055_peginsertion_civo_trigger_s1
586	  status: DONE
587	  description: 
588	  tags: 
589	  conclusion: success
590	  metrics: {
591	    "total_steps": 222400,
592	    "ve_ratio_peak": 3.08,
593	    "ve_ratio_peak_step": 92500,
594	    "ve_ratio_final": 0.498,
595	    "ve_ratio_final_step": 212500,
596	    "eval_return_final": 11.44,
597	    "eval_return_final_step": 212500,
598	    "eval_return_peak": 24.05,
599	    "eval_return_peak_step": 112500,
600	    "nve_classification": "transient",
601	    "civo_triggered": true,
602	    "civo_self_corrected": "partial",
603	    "note": "CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 \u2014 severity seed-dependent.",
604	    "ve_ratio_trajectory": {
605	        "12500": 0.19,
606	        "22500": 0.81,
607	        "32500": 1.35,
608	        "42500": 2.0,
609	        "52500": 2.39,
610	        "62500": 2.85,
611	        "72500": 2.28,
612	        "82500": 2.48,
613	        "92500": 3.08,
614	        "102500": 2.51,
615	        "112500": 0.91,
616	        "122500": 1.21,
617	        "132500": 1.36,
618	        "142500": 0.75,
619	        "152500": 0.55,
620	        "162500": 1.17,
621	        "172500": 0.96,
622	        "182500": 0.94,
623	        "192500": 0.9,
624	        "202500": 0.73,
625	        "212500": 0.5
626	    }
627	}
628	
629	  exp_id: exp_056_peginsertion_frozen_s1
630	  status: DONE
631	  description: 
632	  tags: 
633	  conclusion: success
634	  metrics: {
635	    "total_steps": 222500,
636	    "ve_ratio_peak": 11.321,
637	    "ve_ratio_peak_step": 82500,
638	    "ve_ratio_final": 1.193,
639	    "ve_ratio_final_step": 212500,
640	    "eval_return_final": 4.37,
641	    "eval_return_final_step": 212500,
642	    "eval_return_peak": 24.42,
643	    "eval_return_peak_step": 132500,
644	    "nve_classification": "burst",
645	    "note": "Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 \u2014 frozen does NOT suppress ManiSkill transients.",
646	    "ve_ratio_trajectory": {
647	        "12500": 0.316,
648	        "22500": 0.975,
649	        "32500": 1.839,
650	        "42500": 1.966,
651	        "52500": 5.422,
652	        "62500": 4.047,
653	        "72500": 8.408,
654	        "82500": 11.321,
655	        "92500": 3.724,
656	        "102500": 3.034,
657	        "112500": 2.204,
658	        "122500": 2.425,
659	        "132500": 0.842,
660	        "142500": 2.194,
661	        "152500": 2.203,
662	        "162500": 0.651,
663	        "172500": 1.085,
664	        "182500": 1.07,
665	        "192500": 0.467,
666	        "202500": 0.708,
667	        "212500": 1.193
668	    }
669	}
670	
671	============================================================
672	4. WALKER BASELINE EXPERIMENTS
673	============================================================
674	All walker experiments (44): ['exp_057_frozen_dt_emb_walker_s2', 'exp_047_frozen_dt_emb_walker_s1', 'exp_044_gradient_stop_walker', 'exp_043_008f_walker_s1', 'exp_042_frozen_dt_emb_walker', 'exp_041_dual_critic_walker_s3', 'exp_039_narrow_dual_critic_walker_s1', 'exp_038_dual_critic_walker_s2', 'exp_035_narrow_dual_critic_walker', 'exp_033_wide_critic_walker', 'exp_032_dual_critic_walker', 'exp_032b_dual_critic_walker_s1', 'exp_029d_tcn_walker_s3_sigma02', 'exp_029b_tcn_walker_s2_sigma02', 'exp_029c_tcn_walker_s0_sigma01', 'exp_029a_tcn_walker_s1_sigma02', 'exp_027_tcn_walker_s1', 'exp_027_tcn_walker_s0_sigma02', 'exp_027_tcn_walker_s0', 'exp_028_rave_walker_s0_ceil15', 'exp_028_rave_walker_s0', 'exp_025_obs_sgs_walker_s2', 'exp_025_obs_sgs_walker_s4', 'exp_025_obs_sgs_walker_s3', 'exp_025_obs_sgs_walker_s1', 'exp_018v2_full_sgs_walker_s1', 'exp_009b_008d_walker_s2', 'exp_016d_sgs_walker_s1', 'exp_008f_s3_no_dt_embed_walker', 'exp_018_full_sgs_walker_s1', 'exp_009d_baseline_walker_s0', 'exp_016e_sgs_walker_s1', 'exp_016c_sgs_walker_s1', 'exp_009h_008f_walker_s0', 'exp_016b_sgs_walker_s1', 'exp_009g_008f_walker_s0', 'exp_009f_008f_walker_s1', 'exp_016_sgs_walker_s1', 'exp_009d_baseline_walker_s1', 'exp_009e_008d_walker_s1', 'exp_009a_baseline_walker_s2', 'exp_008e_v3_walker_s2', 'exp_008e_v3_walker_s1', 'exp_009c_008f_walker_s2']
675	  exp_id: exp_008e_v3_walker_s1
676	  status: DONE
677	  description: 
678	  tags: 
679	  conclusion: success
680	  metrics: {
681	    "eval_trajectory": [
682	        {
683	            "eval_return": 31,
684	            "step": 5000
685	        },
686	        {
687	            "eval_return": 131.2,
688	            "step": 15000
689	        },
690	        {
691	            "eval_return": 155.7,
692	            "step": 25000
693	        },
694	        {
695	            "eval_return": 276.5,
696	            "step": 35000
697	        },
698	        {
699	            "eval_return": 382.2,
700	            "step": 45000
701	        },
702	        {
703	            "eval_return": 486.8,
704	            "step": 55000
705	        },
706	        {
707	            "eval_return": 580.7,
708	            "step": 65000
709	        },
710	        {
711	            "eval_return": 574.1,
712	            "step": 75000
713	        },
714	        {
715	            "eval_return": 657.3,
716	            "step": 85000
717	        },
718	        {
719	            "eval_return": 851.9,
720	            "step": 95000
721	        },
722	        {
723	            "eval_return": 869.9,
724	            "step": 105000
725	        }
726	    ],
727	    "exit_code": 0,
728	    "final_eval_return": 869.9,
729	    "final_value_mean": 457.9,
730	    "gate_dt_1_frac": 1,
731	    "total_steps": 112000,
732	    "ve_ratio_105k": 0.527
733	}
734	
735	  exp_id: exp_008e_v3_walker_s2
736	  status: DONE
737	  description: 
738	  tags: 
739	  conclusion: negative
740	  metrics: {
741	    "actor_entropy_collapse_signature": "entropy rose from -5.21@85K to -3.83@105K (policy destabilizing during collapse)",
742	    "actor_entropy_trajectory": [
743	        {
744	            "actor_entropy": 8.239,
745	            "step": 5000
746	        },
747	        {
748	            "actor_entropy": 2.352,
749	            "step": 15000
750	        },
751	        {
752	            "actor_entropy": 0.17,
753	            "step": 25000
754	        },
755	        {
756	            "actor_entropy": -3.498,
757	            "step": 35000
758	        },
759	        {
760	            "actor_entropy": -4.915,
761	            "step": 45000
762	        },
763	        {
764	            "actor_entropy": -5.121,
765	            "step": 55000
766	        },
767	        {
768	            "actor_entropy": -5.135,
769	            "step": 65000
770	        },
771	        {
772	            "actor_entropy": -5.224,
773	            "step": 75000
774	        },
775	        {
776	            "actor_entropy": -5.208,
777	            "step": 85000
778	        },
779	        {
780	            "actor_entropy": -4.529,
781	            "step": 95000
782	        },
783	        {
784	            "actor_entropy": -3.828,
785	            "step": 105000
786	        }
787	    ],
788	    "baseline_105K": 915.67,
789	    "collapse_confirmed": "105K (nve=3.78x, eval 715\u2192137)",
790	    "collapse_onset": "95K (nve jumped from 0.68x to 1.34x)",
791	    "eval_trajectory": [
792	        {
793	            "eval_return": 39.27,
794	            "step": 5000
795	        },
796	        {
797	            "eval_return": 180.85,
798	            "step": 15000
799	        },
800	        {
801	            "eval_return": 211.82,
802	            "step": 25000
803	        },
804	        {
805	            "eval_return": 320.39,
806	            "step": 35000
807	        },
808	        {
809	            "eval_return": 356.93,
810	            "step": 45000
811	        },
812	        {
813	            "eval_return": 418.32,
814	            "step": 55000
815	        },
816	        {
817	            "eval_return": 435.09,
818	            "step": 65000
819	        },
820	        {
821	            "eval_return": 576.54,
822	            "step": 75000
823	        },
824	        {
825	            "eval_return": 715.21,
826	            "step": 85000
827	        },
828	        {
829	            "eval_return": 452.43,
830	            "step": 95000
831	        },
832	        {
833	            "eval_return": 136.96,
834	            "step": 105000
835	        }
836	    ],
837	    "final_eval_return": 136.96,
838	    "final_nve": 3.78,
839	    "final_value_mean": 339.84,
840	    "final_ve_ratio": 2.481,
841	    "gate_dt_1_frac": 1,
842	    "gate_dt_mean": 1,
843	    "peak_eval_return": 715.21,
844	    "peak_eval_step": 85000,
845	    "train_return_108K": "19-23 (random policy level)",
846	    "value_trajectory": [
847	        {
848	            "step": 5000,
849	            "value_mean": 0
850	        },
851	        {
852	            "step": 15000,
853	            "value_mean": 3.91
854	        },
855	        {
856	            "step": 25000,
857	            "value_mean": 30.27
858	        },
859	        {
860	            "step": 35000,
861	            "value_mean": 79.75
862	        },
863	        {
864	            "step": 45000,
865	            "value_mean": 125.25
866	        },
867	        {
868	            "step": 55000,
869	            "value_mean": 172.89
870	        },
871	        {
872	            "step": 65000,
873	            "value_mean": 220.47
874	        },
875	        {
876	            "step": 75000,
877	            "value_mean": 272.64
878	        },
879	        {
880	            "step": 85000,
881	            "value_mean": 339.3
882	        },
883	        {
884	            "step": 95000,
885	            "value_mean": 384.39
886	        },
887	        {
888	            "step": 105000,
889	            "value_mean": 339.84
890	        }
891	    ],
892	    "ve_ratio_trajectory": [
893	        {
894	            "nve": 1.64,
895	            "step": 25000,
896	            "ve": 0.143
897	        },
898	        {
899	            "nve": 1.03,
900	            "step": 35000,
901	            "ve": 0.249
902	        },
903	        {
904	            "nve": 1.06,
905	            "step": 45000,
906	            "ve": 0.351
907	        },
908	        {
909	            "nve": 1.02,
910	            "step": 55000,
911	            "ve": 0.413
912	        },
913	        {
914	            "nve": 0.9,
915	            "step": 65000,
916	            "ve": 0.507
917	        },
918	        {
919	            "nve": 0.66,
920	            "step": 75000,
921	            "ve": 0.473
922	        },
923	        {
924	            "nve": 0.68,
925	            "step": 85000,
926	            "ve": 0.474
927	        },
928	        {
929	            "nve": 1.34,
930	            "step": 95000,
931	            "ve": 0.85
932	        },
933	        {
934	            "nve": 3.78,
935	            "step": 105000,
936	            "ve": 2.481
937	        }
938	    ],
939	    "vs_baseline_105K": "-85.0%"
940	}
941	
942	  exp_id: exp_008f_s3_no_dt_embed_walker
943	  status: DONE
944	  description: 
945	  tags: 
946	  conclusion: success
947	  metrics: {
948	    "collapse": false,
949	    "eval_return_final": 363.8,
950	    "nve_peak": "< 1.5x"
951	}
952	
953	  exp_id: exp_009a_baseline_walker_s2
954	  status: DONE
955	  description: 
956	  tags: 
957	  conclusion: success
958	  metrics: {
959	    "cross_seed_ve_stable": "seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72",
960	    "eval_return_peak": 966.94,
961	    "eval_return_peak_step": 395000,
962	    "eval_trajectory": [
963	        {
964	            "eval_return": 41.21,
965	            "step": 5000
966	        },
967	        {
968	            "eval_return": 106.01,
969	            "step": 15000
970	        },
971	        {
972	            "eval_return": 325.33,
973	            "step": 25000
974	        },
975	        {
976	            "eval_return": 354.49,
977	            "step": 35000
978	        },
979	        {
980	            "eval_return": 498.01,
981	            "step": 45000
982	        },
983	        {
984	            "eval_return": 534.13,
985	            "step": 55000
986	        },
987	        {
988	            "eval_return": 688.87,
989	            "step": 65000
990	        },
991	        {
992	            "eval_return": 656.85,
993	            "step": 75000
994	        },
995	        {
996	            "eval_return": 618.73,
997	            "step": 85000
998	        },
999	        {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "199ec3a0-ae39-491f-8eb1-4281ba562549"
}
```

</details>

---


### System

_source line 107_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 31633,
    "tool_uses": 5,
    "duration_ms": 34991
  },
  "last_tool_name": "Read",
  "uuid": "31ca3559-ef39-4ba1-8495-6ce070aa86a7",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 108_

<details open><summary>🔧 Tool call — Read · `toolu_01XGyKd6gkP8v1zVwnwK7VNi`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "offset": 1000,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "42bed636-fccd-43f8-bfff-a76e1550e7cb",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BpfySHYHWmc5WE8bSwTb77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6083,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6083,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 109 · 2026-05-24T02:15:04.135Z_

<details><summary>↩ Tool result · `toolu_01XGyKd6gkP8v1zVwnwK7VNi`</summary>

```text
1000	            "eval_return": 596.24,
1001	            "step": 95000
1002	        },
1003	        {
1004	            "eval_return": 836.51,
1005	            "step": 105000
1006	        },
1007	        {
1008	            "eval_return": 804.79,
1009	            "step": 115000
1010	        },
1011	        {
1012	            "eval_return": 865.48,
1013	            "step": 125000
1014	        },
1015	        {
1016	            "eval_return": 876.08,
1017	            "step": 135000
1018	        },
1019	        {
1020	            "eval_return": 869.18,
1021	            "step": 145000
1022	        },
1023	        {
1024	            "eval_return": 778.99,
1025	            "step": 155000
1026	        },
1027	        {
1028	            "eval_return": 864.03,
1029	            "step": 165000
1030	        },
1031	        {
1032	            "eval_return": 850.53,
1033	            "step": 175000
1034	        },
1035	        {
1036	            "eval_return": 907.31,
1037	            "step": 185000
1038	        },
1039	        {
1040	            "eval_return": 873.49,
1041	            "step": 195000
1042	        },
1043	        {
1044	            "eval_return": 887.02,
1045	            "step": 205000
1046	        },
1047	        {
1048	            "eval_return": 956.04,
1049	            "step": 215000
1050	        },
1051	        {
1052	            "eval_return": 892.09,
1053	            "step": 225000
1054	        },
1055	        {
1056	            "eval_return": 914.78,
1057	            "step": 235000
1058	        },
1059	        {
1060	            "eval_return": 950.32,
1061	            "step": 245000
1062	        },
1063	        {
1064	            "eval_return": 936.9,
1065	            "step": 255000
1066	        },
1067	        {
1068	            "eval_return": 937.27,
1069	            "step": 265000
1070	        },
1071	        {
1072	            "eval_return": 934.78,
1073	            "step": 275000
1074	        },
1075	        {
1076	            "eval_return": 960.2,
1077	            "step": 285000
1078	        },
1079	        {
1080	            "eval_return": 947.46,
1081	            "step": 295000
1082	        },
1083	        {
1084	            "eval_return": 937.8,
1085	            "step": 305000
1086	        },
1087	        {
1088	            "eval_return": 948.66,
1089	            "step": 315000
1090	        },
1091	        {
1092	            "eval_return": 930.61,
1093	            "step": 325000
1094	        },
1095	        {
1096	            "eval_return": 919.23,
1097	            "step": 335000
1098	        },
1099	        {
1100	            "eval_return": 816.18,
1101	            "step": 345000
1102	        },
1103	        {
1104	            "eval_return": 932.45,
1105	            "step": 355000
1106	        },
1107	        {
1108	            "eval_return": 943.13,
1109	            "step": 365000
1110	        },
1111	        {
1112	            "eval_return": 952.86,
1113	            "step": 375000
1114	        },
1115	        {
1116	            "eval_return": 942.31,
1117	            "step": 385000
1118	        },
1119	        {
1120	            "eval_return": 966.94,
1121	            "step": 395000
1122	        },
1123	        {
1124	            "eval_return": 948.01,
1125	            "step": 405000
1126	        },
1127	        {
1128	            "eval_return": 957.06,
1129	            "step": 415000
1130	        },
1131	        {
1132	            "eval_return": 939.37,
1133	            "step": 425000
1134	        },
1135	        {
1136	            "eval_return": 963.65,
1137	            "step": 435000
1138	        },
1139	        {
1140	            "eval_return": 948.42,
1141	            "step": 445000
1142	        },
1143	        {
1144	            "eval_return": 937.72,
1145	            "step": 455000
1146	        },
1147	        {
1148	            "eval_return": 939.54,
1149	            "step": 465000
1150	        },
1151	        {
1152	            "eval_return": 965.94,
1153	            "step": 475000
1154	        },
1155	        {
1156	            "eval_return": 916.74,
1157	            "step": 485000
1158	        },
1159	        {
1160	            "eval_return": 945.58,
1161	            "step": 495000
1162	        },
1163	        {
1164	            "eval_return": 957.87,
1165	            "step": 505000
1166	        }
1167	    ],
1168	    "final_eval_return": 957.87,
1169	    "final_eval_step": 505000,
1170	    "final_value_mean": 665.17,
1171	    "final_ve_ratio": 0.694,
1172	    "last10_mean": 947.19,
1173	    "n_evals": 51,
1174	    "total_steps": 505000,
1175	    "value_trajectory": [
1176	        {
1177	            "step": 5000,
1178	            "value_mean": 0
1179	        },
1180	        {
1181	            "step": 25000,
1182	            "value_mean": 45.78
1183	        },
1184	        {
1185	            "step": 55000,
1186	            "value_mean": 253.49
1187	        },
1188	        {
1189	            "step": 105000,
1190	            "value_mean": 539.34
1191	        },
1192	        {
1193	            "step": 155000,
1194	            "value_mean": 633.42
1195	        },
1196	        {
1197	            "step": 205000,
1198	            "value_mean": 658.92
1199	        },
1200	        {
1201	            "step": 255000,
1202	            "value_mean": 663.87
1203	        },
1204	        {
1205	            "step": 305000,
1206	            "value_mean": 663.86
1207	        },
1208	        {
1209	            "step": 355000,
1210	            "value_mean": 663.78
1211	        },
1212	        {
1213	            "step": 405000,
1214	            "value_mean": 663.95
1215	        },
1216	        {
1217	            "step": 455000,
1218	            "value_mean": 664.42
1219	        },
1220	        {
1221	            "step": 505000,
1222	            "value_mean": 665.17
1223	        }
1224	    ],
1225	    "ve_ratio_trajectory": [
1226	        {
1227	            "step": 25000,
1228	            "ve": 0.141
1229	        },
1230	        {
1231	            "step": 55000,
1232	            "ve": 0.475
1233	        },
1234	        {
1235	            "step": 105000,
1236	            "ve": 0.645
1237	        },
1238	        {
1239	            "step": 155000,
1240	            "ve": 0.813
1241	        },
1242	        {
1243	            "step": 205000,
1244	            "ve": 0.743
1245	        },
1246	        {
1247	            "step": 255000,
1248	            "ve": 0.709
1249	        },
1250	        {
1251	            "step": 305000,
1252	            "ve": 0.708
1253	        },
1254	        {
1255	            "step": 355000,
1256	            "ve": 0.712
1257	        },
1258	        {
1259	            "step": 405000,
1260	            "ve": 0.7
1261	        },
1262	        {
1263	            "step": 455000,
1264	            "ve": 0.709
1265	        },
1266	        {
1267	            "step": 505000,
1268	            "ve": 0.694
1269	        }
1270	    ],
1271	    "ve_stable_range": "0.69-0.72 from 235K+",
1272	    "vs_exp001_105K": "836.51 vs 915.67 (-8.6%)",
1273	    "vs_exp001_final": "957.87 vs 970.41 (-1.3%)",
1274	    "vs_exp001_last10": "947.19 vs 950.90 (-0.4%)",
1275	    "vs_exp001_peak": "966.94 vs 970.41 (-0.4%)"
1276	}
1277	
1278	  exp_id: exp_009b_008d_walker_s2
1279	  status: DONE
1280	  description: 
1281	  tags: 
1282	  conclusion: negative
1283	  metrics: {
1284	    "baseline_105K": 915.67,
1285	    "causal_conclusion": "Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x\u21920.38x@105K, eval 141\u2192268) while seed 0 sustained nve>1.5x across 4 consecutive checkpoints and collapsed (eval 167\u219283). Collapse is stochastic (1/2 seeds); nve>1.5x threshold is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).",
1286	    "current_step": 105000,
1287	    "eval_checkpoints": [
1288	        {
1289	            "baseline_ve": null,
1290	            "eval_return": 39.27,
1291	            "normalized_ve": null,
1292	            "step": 5000,
1293	            "value_mean": 0,
1294	            "ve_ratio": 0
1295	        },
1296	        {
1297	            "baseline_ve": null,
1298	            "eval_return": 144.31,
1299	            "normalized_ve": null,
1300	            "step": 15000,
1301	            "value_mean": 4.47,
1302	            "ve_ratio": 0.031
1303	        },
1304	        {
1305	            "baseline_ve": 0.087,
1306	            "eval_return": 141.12,
1307	            "normalized_ve": 2.05,
1308	            "step": 25000,
1309	            "value_mean": 25.14,
1310	            "ve_ratio": 0.178
1311	        },
1312	        {
1313	            "baseline_ve": 0.241,
1314	            "eval_return": 164.14,
1315	            "normalized_ve": 1.24,
1316	            "step": 35000,
1317	            "value_mean": 49.02,
1318	            "ve_ratio": 0.299
1319	        },
1320	        {
1321	            "baseline_ve": 0.331,
1322	            "eval_return": 141.04,
1323	            "normalized_ve": 1.62,
1324	            "step": 45000,
1325	            "value_mean": 75.59,
1326	            "ve_ratio": 0.536
1327	        },
1328	        {
1329	            "baseline_ve": 0.404,
1330	            "eval_return": 172.33,
1331	            "normalized_ve": 1.41,
1332	            "step": 55000,
1333	            "value_mean": 98.28,
1334	            "ve_ratio": 0.57
1335	        },
1336	        {
1337	            "baseline_ve": 0.563,
1338	            "eval_return": 209.16,
1339	            "normalized_ve": 0.94,
1340	            "step": 65000,
1341	            "value_mean": 110.91,
1342	            "ve_ratio": 0.53
1343	        },
1344	        {
1345	            "baseline_ve": 0.719,
1346	            "eval_return": 197.46,
1347	            "normalized_ve": 0.66,
1348	            "step": 75000,
1349	            "value_mean": 93.49,
1350	            "ve_ratio": 0.474
1351	        },
1352	        {
1353	            "baseline_ve": 0.701,
1354	            "eval_return": 236.49,
1355	            "normalized_ve": 0.51,
1356	            "step": 85000,
1357	            "value_mean": 83.86,
1358	            "ve_ratio": 0.355
1359	        },
1360	        {
1361	            "baseline_ve": 0.632,
1362	            "eval_return": 278.54,
1363	            "normalized_ve": 0.43,
1364	            "step": 95000,
1365	            "value_mean": 75.72,
1366	            "ve_ratio": 0.272
1367	        },
1368	        {
1369	            "baseline_ve": 0.656,
1370	            "eval_return": 267.93,
1371	            "normalized_ve": 0.38,
1372	            "step": 105000,
1373	            "value_mean": 67.27,
1374	            "ve_ratio": 0.251
1375	        }
1376	    ],
1377	    "target_steps": 105000,
1378	    "trend": "Eval rising throughout: 39\u2192144\u2192141\u2192164\u2192141\u2192172\u2192209\u2192197\u2192236\u2192279\u2192268. Value peaks at 110.91@65K then self-corrects downward to 67.27@105K. v/e ratio peaks 0.57@55K then monotonically declines to 0.25@105K. NO delusional critic collapse \u2014 value self-corrects while eval improves.",
1379	    "verdict": "NEGATIVE \u2014 hypothesis was to replicate collapse, collapse NOT reproduced. However, pathological nve>1.5x episode confirmed (2.05x@25K, 1.62x@45K), consistent with trained dt_emb inducing pathological overestimation. Self-correction to 0.38x@105K distinguishes from seed 0's sustained overestimation \u2192 collapse.",
1380	    "vs_baseline_105K": "-70.8%"
1381	}
1382	
1383	  exp_id: exp_009c_008f_walker_s2
1384	  status: DONE
1385	  description: 
1386	  tags: 
1387	  conclusion: negative
1388	  metrics: {
1389	    "baseline_105K": 915.67,
1390	    "causal_conclusion": "Seed 2 does NOT replicate seed 1's zigzag recovery. 008f seed 1 peaked at 503@105K with rising trend; seed 2 peaked at 359@75K then declined to 148@105K. The adaptive horizon mechanism's benefit appears seed-dependent and not robust.",
1391	    "current_step": 105000,
1392	    "eval_checkpoints": [
1393	        {
1394	            "baseline_ve": null,
1395	            "eval_return": 30.37,
1396	            "normalized_ve": null,
1397	            "step": 5000,
1398	            "value_mean": 0.0013,
1399	            "ve_ratio": null
1400	        },
1401	        {
1402	            "baseline_ve": null,
1403	            "eval_return": 157.15,
1404	            "normalized_ve": null,
1405	            "step": 15000,
1406	            "value_mean": 3.057,
1407	            "ve_ratio": 0.019
1408	        },
1409	        {
1410	            "baseline_ve": 0.087,
1411	            "eval_return": 168.75,
1412	            "normalized_ve": 1.26,
1413	            "step": 25000,
1414	            "value_mean": 18.536,
1415	            "ve_ratio": 0.11
1416	        },
1417	        {
1418	            "baseline_ve": 0.241,
1419	            "eval_return": 178.94,
1420	            "normalized_ve": 0.79,
1421	            "step": 35000,
1422	            "value_mean": 34.263,
1423	            "ve_ratio": 0.191
1424	        },
1425	        {
1426	            "baseline_ve": 0.331,
1427	            "eval_return": 211.08,
1428	            "normalized_ve": 0.72,
1429	            "step": 45000,
1430	            "value_mean": 50.099,
1431	            "ve_ratio": 0.237
1432	        },
1433	        {
1434	            "baseline_ve": 0.404,
1435	            "eval_return": 238.91,
1436	            "normalized_ve": 0.66,
1437	            "step": 55000,
1438	            "value_mean": 63.267,
1439	            "ve_ratio": 0.265
1440	        },
1441	        {
1442	            "baseline_ve": 0.563,
1443	            "eval_return": 244.15,
1444	            "normalized_ve": 0.53,
1445	            "step": 65000,
1446	            "value_mean": 72.717,
1447	            "ve_ratio": 0.298
1448	        },
1449	        {
1450	            "baseline_ve": 0.719,
1451	            "eval_return": 359.14,
1452	            "normalized_ve": 0.33,
1453	            "step": 75000,
1454	            "value_mean": 83.91,
1455	            "ve_ratio": 0.234
1456	        },
1457	        {
1458	            "baseline_ve": 0.701,
1459	            "eval_return": 227.43,
1460	            "normalized_ve": 0.6,
1461	            "step": 85000,
1462	            "value_mean": 96.071,
1463	            "ve_ratio": 0.422
1464	        },
1465	        {
1466	            "baseline_ve": 0.632,
1467	            "eval_return": 190.94,
1468	            "normalized_ve": 0.9,
1469	            "step": 95000,
1470	            "value_mean": 108.29,
1471	            "ve_ratio": 0.567
1472	        },
1473	        {
1474	            "baseline_ve": 0.656,
1475	            "eval_return": 148.34,
1476	            "normalized_ve": 1.14,
1477	            "step": 105000,
1478	            "value_mean": 111.247,
1479	            "ve_ratio": 0.75
1480	        }
1481	    ],
1482	    "target_steps": 105000,
1483	    "trend": "Peak 359@75K then monotonic decline to 148@105K; no recovery pattern unlike 008f seed 1's zigzag recovery to 503",
1484	    "verdict": "NEGATIVE - no delusional critic (normalized v/e < 1.5x) but persistent decline after 75K; cross-seed consistency with 008f seed 1 NOT confirmed",
1485	    "vs_baseline_105K": "-83.8%"
1486	}
1487	
1488	  exp_id: exp_009d_baseline_walker_s0
1489	  status: DONE
1490	  description: 
1491	  tags: 
1492	  conclusion: success
1493	  metrics: {
1494	    "eval_return": 927.6,
1495	    "eval_return_at_508K": 927.6,
1496	    "eval_return_peak": 950.96,
1497	    "eval_return_peak_step": 398000,
1498	    "note": "COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K",
1499	    "step": 508000
1500	}
1501	
1502	  exp_id: exp_009d_baseline_walker_s1
1503	  status: DONE
1504	  description: 
1505	  tags: 
1506	  conclusion: killed
1507	  metrics: {}
1508	
1509	  exp_id: exp_009e_008d_walker_s1
1510	  status: DONE
1511	  description: 
1512	  tags: 
1513	  conclusion: negative
1514	  metrics: {
1515	    "actor_loss_sign_flip": 85000,
1516	    "baseline_105K": 915.67,
1517	    "collapse_rate_note": "Independent rate = 1/2 (seed 1 collapsed, seed 2 self-corrected). 008d and 009e share seed=1, count as one independent observation.",
1518	    "current_step": 105000,
1519	    "eval_checkpoints": [
1520	        {
1521	            "eval_return": 31,
1522	            "step": 5000,
1523	            "value_mean": 0,
1524	            "ve_ratio": 0
1525	        },
1526	        {
1527	            "eval_return": 153.7,
1528	            "step": 15000,
1529	            "value_mean": 3.4,
1530	            "ve_ratio": 0.022
1531	        },
1532	        {
1533	            "baseline_ve": 0.087,
1534	            "eval_return": 167.2,
1535	            "normalized_ve": 1.78,
1536	            "step": 25000,
1537	            "value_mean": 25.9,
1538	            "ve_ratio": 0.155
1539	        },
1540	        {
1541	            "baseline_ve": 0.241,
1542	            "eval_return": 146.3,
1543	            "normalized_ve": 1.71,
1544	            "step": 35000,
1545	            "value_mean": 60.2,
1546	            "ve_ratio": 0.411
1547	        },
1548	        {
1549	            "baseline_ve": 0.331,
1550	            "eval_return": 140.8,
1551	            "normalized_ve": 2.09,
1552	            "step": 45000,
1553	            "value_mean": 97.5,
1554	            "ve_ratio": 0.693
1555	        },
1556	        {
1557	            "baseline_ve": 0.404,
1558	            "eval_return": 82.7,
1559	            "normalized_ve": 4.12,
1560	            "step": 55000,
1561	            "value_mean": 137.9,
1562	            "ve_ratio": 1.666
1563	        },
1564	        {
1565	            "baseline_ve": 0.563,
1566	            "eval_return": 250,
1567	            "normalized_ve": 1.23,
1568	            "step": 65000,
1569	            "value_mean": 173.8,
1570	            "ve_ratio": 0.695
1571	        },
1572	        {
1573	            "baseline_ve": 0.719,
1574	            "eval_return": 178.1,
1575	            "normalized_ve": 1.48,
1576	            "step": 75000,
1577	            "value_mean": 189.9,
1578	            "ve_ratio": 1.066
1579	        },
1580	        {
1581	            "baseline_ve": 0.701,
1582	            "eval_return": 201.93,
1583	            "normalized_ve": 1.15,
1584	            "step": 85000,
1585	            "value_mean": 163.08,
1586	            "ve_ratio": 0.808
1587	        },
1588	        {
1589	            "baseline_ve": 0.632,
1590	            "eval_return": 132.79,
1591	            "normalized_ve": 1.73,
1592	            "step": 95000,
1593	            "value_mean": 144.82,
1594	            "ve_ratio": 1.091
1595	        },
1596	        {
1597	            "baseline_ve": 0.656,
1598	            "eval_return": 131.08,
1599	            "normalized_ve": 1.57,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "28cdb3e6-ecfd-4729-a65e-3f3872271972"
}
```

</details>

---


### System

_source line 110_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 39028,
    "tool_uses": 6,
    "duration_ms": 39369
  },
  "last_tool_name": "Read",
  "uuid": "678822ba-59d4-4415-ba14-1b6e290fbb92",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 111_

<details open><summary>🔧 Tool call — Read · `toolu_01TruTf6EgrgiTVibpZ1iaBC`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "offset": 1600,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "a091418f-588d-45d8-b2a1-139fa1ddd9f7",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KfFejuJqwnrYfa63J5Z9Bk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7357,
      "cache_read_input_tokens": 31480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7357,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 112 · 2026-05-24T02:15:08.507Z_

<details><summary>↩ Tool result · `toolu_01TruTf6EgrgiTVibpZ1iaBC`</summary>

```text
1600	            "step": 105000,
1601	            "value_mean": 135.37,
1602	            "ve_ratio": 1.033
1603	        }
1604	    ],
1605	    "final_eval_return": 131.08,
1606	    "final_nve": 1.57,
1607	    "final_value_mean": 135.37,
1608	    "final_ve_ratio": 1.033,
1609	    "peak_nve": 4.12,
1610	    "peak_nve_step": 55000,
1611	    "target_steps": 105000,
1612	    "vs_baseline_105K": "-85.7%"
1613	}
1614	
1615	  exp_id: exp_009f_008f_walker_s1
1616	  status: DONE
1617	  description: 
1618	  tags: 
1619	  conclusion: killed
1620	  metrics: {}
1621	
1622	  exp_id: exp_009g_008f_walker_s0
1623	  status: DONE
1624	  description: 
1625	  tags: 
1626	  conclusion: killed
1627	  metrics: {}
1628	
1629	  exp_id: exp_009h_008f_walker_s0
1630	  status: DONE
1631	  description: 
1632	  tags: 
1633	  conclusion: failed
1634	  metrics: {}
1635	
1636	  exp_id: exp_016_sgs_walker_s1
1637	  status: DONE
1638	  description: 
1639	  tags: 
1640	  conclusion: failed
1641	  metrics: {}
1642	
1643	  exp_id: exp_016b_sgs_walker_s1
1644	  status: DONE
1645	  description: 
1646	  tags: 
1647	  conclusion: failed
1648	  metrics: {}
1649	
1650	  exp_id: exp_016c_sgs_walker_s1
1651	  status: DONE
1652	  description: 
1653	  tags: 
1654	  conclusion: failed
1655	  metrics: {
1656	    "egl_fix_verified": true,
1657	    "eval_return_5K": 31,
1658	    "step": 5000
1659	}
1660	
1661	  exp_id: exp_016d_sgs_walker_s1
1662	  status: DONE
1663	  description: 
1664	  tags: 
1665	  conclusion: failed
1666	  metrics: {}
1667	
1668	  exp_id: exp_016e_sgs_walker_s1
1669	  status: DONE
1670	  description: 
1671	  tags: 
1672	  conclusion: negative
1673	  metrics: {
1674	    "actor_loss_sign_flip_step": 95000,
1675	    "civo_catastrophic_step": 95000,
1676	    "civo_detected": true,
1677	    "civo_nve_peak": 10.42,
1678	    "civo_nve_peak_step": 95000,
1679	    "civo_onset_step": 85000,
1680	    "civo_severity": "catastrophic",
1681	    "current_step": 100000,
1682	    "data_source": "metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25",
1683	    "deep_analysis": {
1684	        "016e_vs_008d_entropy_comparison": {
1685	            "15K": {
1686	                "008d": 0.481,
1687	                "016e": 1.049,
1688	                "delta": 0.568
1689	            },
1690	            "25K": {
1691	                "008d": -1.862,
1692	                "016e": -1.554,
1693	                "delta": 0.308
1694	            },
1695	            "35K": {
1696	                "008d": -3.465,
1697	                "016e": -2.118,
1698	                "delta": 1.347
1699	            },
1700	            "45K": {
1701	                "008d": -4.575,
1702	                "016e": -3.455,
1703	                "delta": 1.12
1704	            },
1705	            "55K": {
1706	                "008d": -4.879,
1707	                "016e": -3.617,
1708	                "delta": 1.262
1709	            },
1710	            "interpretation": "SGS preserves ~1.0-1.3 nats higher entropy through 35-55K, enabling better exploration"
1711	        },
1712	        "016e_vs_008d_value_at_crash": {
1713	            "008d": {
1714	                "disconnect_ratio": 1.67,
1715	                "eval_return": 82.75,
1716	                "value_mean": 137.88
1717	            },
1718	            "016e": {
1719	                "disconnect_ratio": 6.58,
1720	                "eval_return": 31.73,
1721	                "value_mean": 208.88
1722	            },
1723	            "interpretation": "016e value completely decoupled from reality; 008d still weakly correlated"
1724	        },
1725	        "actor_loss_sign_flip": {
1726	            "008d_min_actor_loss": -0.073,
1727	            "008d_never_flipped": true,
1728	            "016e_flip_step": 95000,
1729	            "016e_flip_value": 0.014,
1730	            "interpretation": "sign flip = value critic drives actor toward worse actions, triggering catastrophic collapse"
1731	        },
1732	        "train_return_collapse_timeline": {
1733	            "100K": [
1734	                109,
1735	                111,
1736	                102,
1737	                108
1738	            ],
1739	            "88K": [
1740	                140,
1741	                145,
1742	                116,
1743	                116
1744	            ],
1745	            "92K": [
1746	                50,
1747	                29,
1748	                34,
1749	                75
1750	            ],
1751	            "96K": [
1752	                86,
1753	                41,
1754	                50,
1755	                101
1756	            ],
1757	            "interpretation": "collapse visible in train_return by 92K; partial recovery by 100K but far below peak"
1758	        }
1759	    },
1760	    "eval_checkpoints": [
1761	        {
1762	            "eval_return": 31,
1763	            "step": 5000,
1764	            "value_mean": 0.001,
1765	            "ve_ratio": 4e-05
1766	        },
1767	        {
1768	            "eval_return": 140.3,
1769	            "step": 15000,
1770	            "value_mean": 3.1,
1771	            "ve_ratio": 0.022
1772	        },
1773	        {
1774	            "baseline_ve": 0.087,
1775	            "eval_return": 141.75,
1776	            "nve": 1.86,
1777	            "step": 25000,
1778	            "value_mean": 22.97,
1779	            "ve_ratio": 0.162
1780	        },
1781	        {
1782	            "baseline_ve": 0.241,
1783	            "eval_return": 173.01,
1784	            "nve": 1.28,
1785	            "step": 35000,
1786	            "value_mean": 53.55,
1787	            "ve_ratio": 0.309
1788	        },
1789	        {
1790	            "baseline_ve": 0.331,
1791	            "eval_return": 184.03,
1792	            "nve": 1.4,
1793	            "step": 45000,
1794	            "value_mean": 85.32,
1795	            "ve_ratio": 0.464
1796	        },
1797	        {
1798	            "baseline_ve": 0.404,
1799	            "eval_return": 153.79,
1800	            "nve": 1.86,
1801	            "step": 55000,
1802	            "value_mean": 115.63,
1803	            "ve_ratio": 0.752
1804	        },
1805	        {
1806	            "baseline_ve": 0.563,
1807	            "eval_return": 324.3,
1808	            "nve": 0.83,
1809	            "step": 65000,
1810	            "value_mean": 152.3,
1811	            "ve_ratio": 0.469
1812	        },
1813	        {
1814	            "baseline_ve": 0.719,
1815	            "eval_return": 326.67,
1816	            "nve": 0.81,
1817	            "step": 75000,
1818	            "value_mean": 190.04,
1819	            "ve_ratio": 0.582
1820	        },
1821	        {
1822	            "baseline_ve": 0.701,
1823	            "eval_return": 256.21,
1824	            "nve": 1.2,
1825	            "step": 85000,
1826	            "value_mean": 215.39,
1827	            "ve_ratio": 0.841
1828	        },
1829	        {
1830	            "baseline_ve": 0.632,
1831	            "eval_return": 31.73,
1832	            "nve": 10.42,
1833	            "step": 95000,
1834	            "value_mean": 208.88,
1835	            "ve_ratio": 6.583
1836	        }
1837	    ],
1838	    "final_eval_return": 31.73,
1839	    "final_eval_step": 95000,
1840	    "gate_dt_2_frac": 1,
1841	    "gate_dt_mean": 2,
1842	    "peak_eval_return": 326.67,
1843	    "peak_eval_step": 75000,
1844	    "reward_dt_emb_detach": true,
1845	    "sgs_verdict": "SGS delays CIVO onset ~50K steps by preserving entropy, yields 2x higher peak (327 vs 167), but does NOT prevent collapse. Collapse is more severe (NVE 10.42x vs 4.12x) due to accumulated value overestimation. Root cause is value dynamics, not reward-head gradient contamination.",
1846	    "target_steps": 105000
1847	}
1848	
1849	  exp_id: exp_018_full_sgs_walker_s1
1850	  status: DONE
1851	  description: 
1852	  tags: 
1853	  conclusion: killed
1854	  metrics: {
1855	    "eval_return_final": 915.7,
1856	    "eval_return_final_step": 105000,
1857	    "eval_return_peak": 915.7,
1858	    "eval_return_peak_step": 105000,
1859	    "nve_peak": 0.72,
1860	    "nve_peak_step": 75000,
1861	    "nve_sustained_avg": 0.55,
1862	    "nve_sustained_max": 0.72,
1863	    "total_steps": 112000,
1864	    "train_return_final_avg": 899.4,
1865	    "value_mean_final": 601.1
1866	}
1867	
1868	  exp_id: exp_018v2_full_sgs_walker_s1
1869	  status: DONE
1870	  description: 
1871	  tags: 
1872	  conclusion: negative
1873	  metrics: {
1874	    "civo_reduction_pct": 79,
1875	    "eval_return_final": 448.3,
1876	    "eval_return_final_step": 105000,
1877	    "eval_return_peak": 499.6,
1878	    "eval_return_peak_step": 75000,
1879	    "gate_dt_2_frac": 1,
1880	    "gate_dt_mean": 2,
1881	    "late_collapse_detected": true,
1882	    "late_collapse_step": 112000,
1883	    "nve_final": 1.34,
1884	    "nve_mean_45k_105k": 1.23,
1885	    "nve_peak": 1.66,
1886	    "nve_peak_step": 95000,
1887	    "total_steps": 112000,
1888	    "total_updates": 25099,
1889	    "value_loss_final": 0.6
1890	}
1891	
1892	  exp_id: exp_025_obs_sgs_walker_s1
1893	  status: DONE
1894	  description: 
1895	  tags: 
1896	  conclusion: failed
1897	  metrics: {}
1898	
1899	  exp_id: exp_025_obs_sgs_walker_s2
1900	  status: DONE
1901	  description: 
1902	  tags: 
1903	  conclusion: negative
1904	  metrics: {
1905	    "eval_return_215K": 89.6,
1906	    "target_steps": 210000,
1907	    "train_steps_completed": 224000,
1908	    "ve_ratio_175K": 1.2,
1909	    "ve_ratio_185K": 1.4,
1910	    "ve_ratio_215K": 0.8
1911	}
1912	
1913	  exp_id: exp_025_obs_sgs_walker_s3
1914	  status: DONE
1915	  description: 
1916	  tags: 
1917	  conclusion: failed
1918	  metrics: {}
1919	
1920	  exp_id: exp_025_obs_sgs_walker_s4
1921	  status: DONE
1922	  description: 
1923	  tags: 
1924	  conclusion: failed
1925	  metrics: {}
1926	
1927	  exp_id: exp_027_tcn_walker_s0
1928	  status: DONE
1929	  description: 
1930	  tags: 
1931	  conclusion: negative
1932	  metrics: {
1933	    "eval_return_105K": 95.5,
1934	    "eval_return_112K": 99.5,
1935	    "eval_return_15K": 154.6,
1936	    "eval_return_25K": 223.6,
1937	    "eval_return_35K": 240,
1938	    "eval_return_45K": 101.2,
1939	    "eval_return_55K": 70,
1940	    "eval_return_5K": 37.4,
1941	    "eval_return_65K": 95.1,
1942	    "eval_return_75K": 189.2,
1943	    "eval_return_85K": 36,
1944	    "eval_return_95K": 166.4,
1945	    "final_step": 120000,
1946	    "gate_dt_entropy": 0,
1947	    "gate_dt_mean": 2,
1948	    "last_5_eval_avg": 117.3,
1949	    "nve_breach_count": 3,
1950	    "nve_breach_steps": "55K(1.68), 65K(1.54), 85K(3.97)",
1951	    "peak_eval": 240,
1952	    "peak_eval_step": "35K",
1953	    "peak_nve": 3.965,
1954	    "peak_nve_step": "85K",
1955	    "target_steps": 210000,
1956	    "ve_ratio_105K": 0.916,
1957	    "ve_ratio_15K": 0.02,
1958	    "ve_ratio_25K": 0.11,
1959	    "ve_ratio_35K": 0.235,
1960	    "ve_ratio_45K": 0.86,
1961	    "ve_ratio_55K": 1.679,
1962	    "ve_ratio_65K": 1.544,
1963	    "ve_ratio_75K": 0.831,
1964	    "ve_ratio_85K": 3.965,
1965	    "ve_ratio_95K": 0.675
1966	}
1967	
1968	  exp_id: exp_027_tcn_walker_s0_sigma02
1969	  status: DONE
1970	  description: 
1971	  tags: 
1972	  conclusion: success
1973	  metrics: {
1974	    "eval_last10_mean": 587.1,
1975	    "eval_peak": 821.1,
1976	    "eval_peak_step": "175K",
1977	    "eval_return_105K": 236.4,
1978	    "eval_return_115K": 543.8,
1979	    "eval_return_125K": 458.4,
1980	    "eval_return_135K": 496.7,
1981	    "eval_return_145K": 542.7,
1982	    "eval_return_155K": 660.5,
1983	    "eval_return_15K": 150.6,
1984	    "eval_return_165K": 653.3,
1985	    "eval_return_175K": 821.1,
1986	    "eval_return_185K": 560.5,
1987	    "eval_return_195K": 567.9,
1988	    "eval_return_205K": 558.7,
1989	    "eval_return_215K": 551,
1990	    "eval_return_25K": 199.4,
1991	    "eval_return_35K": 278.2,
1992	    "eval_return_45K": 315.6,
1993	    "eval_return_55K": 278.6,
1994	    "eval_return_5K": 35.6,
1995	    "eval_return_65K": 331,
1996	    "eval_return_75K": 293.1,
1997	    "eval_return_85K": 363.9,
1998	    "eval_return_95K": 171.4,
1999	    "nve_final": 0.0955,
2000	    "nve_max": 0.9081,
2001	    "nve_max_step": "95K",
2002	    "total_steps": 215000,
2003	    "ve_ratio_105K": 0.5625,
2004	    "ve_ratio_115K": 0.2105,
2005	    "ve_ratio_125K": 0.2182,
2006	    "ve_ratio_135K": 0.1764,
2007	    "ve_ratio_145K": 0.143,
2008	    "ve_ratio_155K": 0.106,
2009	    "ve_ratio_15K": 0.0192,
2010	    "ve_ratio_165K": 0.0979,
2011	    "ve_ratio_175K": 0.0729,
2012	    "ve_ratio_185K": 0.1048,
2013	    "ve_ratio_195K": 0.1026,
2014	    "ve_ratio_205K": 0.0995,
2015	    "ve_ratio_215K": 0.0955,
2016	    "ve_ratio_25K": 0.0961,
2017	    "ve_ratio_35K": 0.1875,
2018	    "ve_ratio_45K": 0.3009,
2019	    "ve_ratio_55K": 0.5231,
2020	    "ve_ratio_65K": 0.5654,
2021	    "ve_ratio_75K": 0.611,
2022	    "ve_ratio_85K": 0.4665,
2023	    "ve_ratio_95K": 0.9081
2024	}
2025	
2026	  exp_id: exp_027_tcn_walker_s1
2027	  status: DONE
2028	  description: 
2029	  tags: 
2030	  conclusion: negative
2031	  metrics: {
2032	    "eval_last10_mean": 233.1,
2033	    "eval_peak": 364.9,
2034	    "eval_peak_step": 75000,
2035	    "eval_return": {
2036	        "105000": 216.7,
2037	        "115000": 318.9,
2038	        "125000": 309.1,
2039	        "135000": 216.1,
2040	        "145000": 175.4,
2041	        "15000": 140.5,
2042	        "155000": 171,
2043	        "165000": 209.5,
2044	        "175000": 120.4,
2045	        "185000": 355.4,
2046	        "195000": 183.3,
2047	        "205000": 240.2,
2048	        "215000": 350.8,
2049	        "25000": 163.6,
2050	        "35000": 153,
2051	        "45000": 136.8,
2052	        "5000": 31,
2053	        "55000": 158.3,
2054	        "65000": 298.5,
2055	        "75000": 364.9,
2056	        "85000": 134,
2057	        "95000": 94.6
2058	    },
2059	    "nve_final": 0.1476,
2060	    "nve_max": 1.6367,
2061	    "nve_max_step": 95000,
2062	    "total_steps": 215000,
2063	    "ve_ratio": {
2064	        "105000": 0.6444,
2065	        "115000": 0.4021,
2066	        "125000": 0.38,
2067	        "135000": 0.5078,
2068	        "145000": 0.8469,
2069	        "15000": 0.0246,
2070	        "155000": 0.8568,
2071	        "165000": 0.5393,
2072	        "175000": 0.7355,
2073	        "185000": 0.211,
2074	        "195000": 0.3513,
2075	        "205000": 0.2376,
2076	        "215000": 0.1476,
2077	        "25000": 0.1416,
2078	        "35000": 0.3585,
2079	        "45000": 0.6101,
2080	        "55000": 0.7092,
2081	        "65000": 0.4875,
2082	        "75000": 0.4902,
2083	        "85000": 1.4104,
2084	        "95000": 1.6367
2085	    }
2086	}
2087	
2088	  exp_id: exp_028_rave_walker_s0
2089	  status: DONE
2090	  description: 
2091	  tags: 
2092	  conclusion: negative
2093	  metrics: {
2094	    "current_steps": 105000,
2095	    "eval_trajectory": {
2096	        "105K": {
2097	            "eval_return": 29,
2098	            "value_mean": 92.2,
2099	            "ve_ratio": 3.183
2100	        },
2101	        "15K": {
2102	            "eval_return": 105.3,
2103	            "value_mean": 2.93,
2104	            "ve_ratio": 0.028
2105	        },
2106	        "25K": {
2107	            "eval_return": 191.9,
2108	            "value_mean": 24.4,
2109	            "ve_ratio": 0.127
2110	        },
2111	        "35K": {
2112	            "eval_return": 204.6,
2113	            "ve_ratio": 0.267
2114	        },
2115	        "45K": {
2116	            "eval_return": 197.7,
2117	            "ve_ratio": 0.439
2118	        },
2119	        "55K": {
2120	            "eval_return": 193,
2121	            "ve_ratio": 0.62
2122	        },
2123	        "5K": {
2124	            "eval_return": 37.4,
2125	            "value_mean": 0.001
2126	        },
2127	        "65K": {
2128	            "eval_return": 79.8,
2129	            "ve_ratio": 1.832
2130	        },
2131	        "75K": {
2132	            "eval_return": 44.5,
2133	            "ve_ratio": 3.415
2134	        },
2135	        "85K": {
2136	            "eval_return": 57.7,
2137	            "ve_ratio": 2.126
2138	        },
2139	        "95K": {
2140	            "eval_return": 25.9,
2141	            "value_mean": 105.87,
2142	            "ve_ratio": 4.086
2143	        }
2144	    },
2145	    "note": "NEGATIVE. NVE diverged from 55K onward (0.62\u21924.09), eval collapsed 193\u219229. No self-correction."
2146	}
2147	
2148	  exp_id: exp_028_rave_walker_s0_ceil15
2149	  status: DONE
2150	  description: 
2151	  tags: 
2152	  conclusion: negative
2153	  metrics: {
2154	    "current_step": 135000,
2155	    "eval_return_105K": 76.2,
2156	    "eval_return_115K": 41.2,
2157	    "eval_return_125K": 36.6,
2158	    "eval_return_135K": 39.1,
2159	    "eval_return_15K": 99.4,
2160	    "eval_return_25K": 155.3,
2161	    "eval_return_35K": 180.1,
2162	    "eval_return_45K": 166.9,
2163	    "eval_return_55K": 131,
2164	    "eval_return_5K": 31.6,
2165	    "eval_return_65K": 91.5,
2166	    "eval_return_75K": 120.9,
2167	    "eval_return_85K": 137.3,
2168	    "eval_return_95K": 70.2,
2169	    "target_steps": 210000,
2170	    "ve_ratio_105K": 0.984,
2171	    "ve_ratio_115K": 1.513,
2172	    "ve_ratio_125K": 1.462,
2173	    "ve_ratio_135K": 1.171,
2174	    "ve_ratio_15K": 0.03,
2175	    "ve_ratio_25K": 0.128,
2176	    "ve_ratio_35K": 0.247,
2177	    "ve_ratio_45K": 0.428,
2178	    "ve_ratio_55K": 0.737,
2179	    "ve_ratio_65K": 1.294,
2180	    "ve_ratio_75K": 0.937,
2181	    "ve_ratio_85K": 0.727,
2182	    "ve_ratio_95K": 1.28
2183	}
2184	
2185	  exp_id: exp_029a_tcn_walker_s1_sigma02
2186	  status: DONE
2187	  description: 
2188	  tags: 
2189	  conclusion: success
2190	  metrics: {
2191	    "current_step": 215000,
2192	    "eval_last10_mean": 282.15,
2193	    "eval_peak": 401,
2194	    "eval_peak_step": "125K",
2195	    "eval_return_105K": 319.4,
2196	    "eval_return_115K": 345.5,
2197	    "eval_return_125K": 401,
2198	    "eval_return_135K": 307.8,
2199	    "eval_return_145K": 380.8,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "4e9b273c-3f65-4dae-93c0-ccb5d82a6682"
}
```

</details>

---


### System

_source line 113_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 47156,
    "tool_uses": 7,
    "duration_ms": 44027
  },
  "last_tool_name": "Read",
  "uuid": "d8d1f261-bd12-4db5-9e7e-9e1e297c364a",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 114_

<details open><summary>🔧 Tool call — Read · `toolu_01UusXgUXdyC6s6BMXdqijgo`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "offset": 2200,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "8df11cb9-697f-477a-a909-33645aa6c4d7",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01R3NHehfT9LXsw1xjyULaAL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8090,
      "cache_read_input_tokens": 38837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8090,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 115 · 2026-05-24T02:15:13.178Z_

<details><summary>↩ Tool result · `toolu_01UusXgUXdyC6s6BMXdqijgo`</summary>

```text
2200	    "eval_return_155K": 307.3,
2201	    "eval_return_15K": 137.7,
2202	    "eval_return_165K": 320.3,
2203	    "eval_return_175K": 159,
2204	    "eval_return_185K": 278.2,
2205	    "eval_return_195K": 301.2,
2206	    "eval_return_205K": 204.6,
2207	    "eval_return_215K": 161.3,
2208	    "eval_return_25K": 180.9,
2209	    "eval_return_35K": 124,
2210	    "eval_return_45K": 124.2,
2211	    "eval_return_55K": 133.9,
2212	    "eval_return_5K": 36.7,
2213	    "eval_return_65K": 169.7,
2214	    "eval_return_75K": 171.2,
2215	    "eval_return_85K": 151.8,
2216	    "eval_return_95K": 180.3,
2217	    "nve_final": 0.1864,
2218	    "nve_max": 0.6428,
2219	    "nve_max_step": "55K",
2220	    "target_steps": 210000,
2221	    "ve_ratio_105K": 0.1554,
2222	    "ve_ratio_115K": 0.1348,
2223	    "ve_ratio_125K": 0.116,
2224	    "ve_ratio_135K": 0.1449,
2225	    "ve_ratio_145K": 0.1088,
2226	    "ve_ratio_155K": 0.1287,
2227	    "ve_ratio_15K": 0.0248,
2228	    "ve_ratio_165K": 0.1142,
2229	    "ve_ratio_175K": 0.2138,
2230	    "ve_ratio_185K": 0.121,
2231	    "ve_ratio_195K": 0.1075,
2232	    "ve_ratio_205K": 0.1503,
2233	    "ve_ratio_215K": 0.1864,
2234	    "ve_ratio_25K": 0.1165,
2235	    "ve_ratio_35K": 0.3574,
2236	    "ve_ratio_45K": 0.5147,
2237	    "ve_ratio_55K": 0.6428,
2238	    "ve_ratio_65K": 0.4777,
2239	    "ve_ratio_75K": 0.398,
2240	    "ve_ratio_85K": 0.4033,
2241	    "ve_ratio_95K": 0.3007
2242	}
2243	
2244	  exp_id: exp_029b_tcn_walker_s2_sigma02
2245	  status: DONE
2246	  description: 
2247	  tags: 
2248	  conclusion: negative
2249	  metrics: {
2250	    "civo_onset_step": 65000,
2251	    "eval_last_step": 165000,
2252	    "eval_peak": 177.67,
2253	    "eval_peak_step": 55000,
2254	    "eval_return_105K": 31.97,
2255	    "eval_return_115K": 35.45,
2256	    "eval_return_125K": 33.04,
2257	    "eval_return_135K": 42.47,
2258	    "eval_return_145K": 51.66,
2259	    "eval_return_155K": 56.5,
2260	    "eval_return_15K": 168.41,
2261	    "eval_return_165K": 44.9,
2262	    "eval_return_25K": 159.56,
2263	    "eval_return_35K": 168.05,
2264	    "eval_return_45K": 171.51,
2265	    "eval_return_55K": 177.67,
2266	    "eval_return_5K": 30.46,
2267	    "eval_return_65K": 106.57,
2268	    "eval_return_75K": 64.01,
2269	    "eval_return_85K": 62.82,
2270	    "eval_return_95K": 44.66,
2271	    "gate_dt2_frac": 1.0,
2272	    "gate_entropy": 0.0,
2273	    "late_stage_nve_decline": "value adaptation (value_mean 108\u219255), not recovery (eval stayed 32-57)",
2274	    "nve_peak": 2.765,
2275	    "nve_peak_step": 105000,
2276	    "step": 168000,
2277	    "value_mean_105K": 88.38,
2278	    "value_mean_165K": 55.03,
2279	    "value_mean_55K": 103.62,
2280	    "ve_ratio_105K": 2.765,
2281	    "ve_ratio_115K": 2.326,
2282	    "ve_ratio_125K": 2.278,
2283	    "ve_ratio_135K": 1.648,
2284	    "ve_ratio_145K": 1.234,
2285	    "ve_ratio_155K": 1.061,
2286	    "ve_ratio_15K": 0.03,
2287	    "ve_ratio_165K": 1.226,
2288	    "ve_ratio_25K": 0.174,
2289	    "ve_ratio_35K": 0.335,
2290	    "ve_ratio_45K": 0.477,
2291	    "ve_ratio_55K": 0.583,
2292	    "ve_ratio_65K": 1.014,
2293	    "ve_ratio_75K": 1.65,
2294	    "ve_ratio_85K": 1.623,
2295	    "ve_ratio_95K": 2.109
2296	}
2297	
2298	  exp_id: exp_029c_tcn_walker_s0_sigma01
2299	  status: DONE
2300	  description: 
2301	  tags: 
2302	  conclusion: negative
2303	  metrics: {
2304	    "eval_final": 328.3,
2305	    "eval_peak": 490.7,
2306	    "eval_peak_step": "165K",
2307	    "eval_return_105K": 204.7,
2308	    "eval_return_115K": 296.4,
2309	    "eval_return_125K": 232.3,
2310	    "eval_return_135K": 247.4,
2311	    "eval_return_145K": 323.1,
2312	    "eval_return_155K": 359.7,
2313	    "eval_return_15K": 99.1,
2314	    "eval_return_165K": 490.7,
2315	    "eval_return_175K": 246.2,
2316	    "eval_return_185K": 220.6,
2317	    "eval_return_195K": 212.8,
2318	    "eval_return_205K": 256.9,
2319	    "eval_return_215K": 328.3,
2320	    "eval_return_25K": 140.7,
2321	    "eval_return_35K": 155.7,
2322	    "eval_return_45K": 160.9,
2323	    "eval_return_55K": 254.8,
2324	    "eval_return_5K": 35.6,
2325	    "eval_return_65K": 268.7,
2326	    "eval_return_75K": 295.5,
2327	    "eval_return_85K": 220.8,
2328	    "eval_return_95K": 188.6,
2329	    "nve_final": 0.1,
2330	    "nve_max": 1.0218,
2331	    "nve_max_step": "95K",
2332	    "total_steps": 224000,
2333	    "ve_ratio_105K": 0.761,
2334	    "ve_ratio_115K": 0.4514,
2335	    "ve_ratio_125K": 0.4899,
2336	    "ve_ratio_135K": 0.3995,
2337	    "ve_ratio_145K": 0.2667,
2338	    "ve_ratio_155K": 0.2,
2339	    "ve_ratio_15K": 0.0306,
2340	    "ve_ratio_165K": 0.1,
2341	    "ve_ratio_175K": 0.3,
2342	    "ve_ratio_185K": 0.3,
2343	    "ve_ratio_195K": 0.3,
2344	    "ve_ratio_205K": 0.2,
2345	    "ve_ratio_215K": 0.1,
2346	    "ve_ratio_25K": 0.1606,
2347	    "ve_ratio_35K": 0.3162,
2348	    "ve_ratio_45K": 0.4807,
2349	    "ve_ratio_55K": 0.4368,
2350	    "ve_ratio_65K": 0.5432,
2351	    "ve_ratio_75K": 0.6211,
2352	    "ve_ratio_85K": 0.9533,
2353	    "ve_ratio_95K": 1.0218
2354	}
2355	
2356	  exp_id: exp_029d_tcn_walker_s3_sigma02
2357	  status: DONE
2358	  description: 
2359	  tags: 
2360	  conclusion: negative
2361	  metrics: {
2362	    "civo_onset_step": 105000,
2363	    "civo_pattern": "sudden blowup (healthy 0.67@95K \u2192 3.0@105K)",
2364	    "eval_final": 104.5,
2365	    "eval_last_step": 215000,
2366	    "eval_peak": 349.6,
2367	    "eval_peak_step": 95000,
2368	    "eval_return_105K": 71.8,
2369	    "eval_return_115K": 69.8,
2370	    "eval_return_125K": 61.5,
2371	    "eval_return_135K": 141.8,
2372	    "eval_return_145K": 98.66,
2373	    "eval_return_155K": 88.86,
2374	    "eval_return_15K": 159.1,
2375	    "eval_return_165K": 86.22,
2376	    "eval_return_175K": 123.53,
2377	    "eval_return_185K": 153.71,
2378	    "eval_return_195K": 68.84,
2379	    "eval_return_205K": 63.71,
2380	    "eval_return_215K": 104.5,
2381	    "eval_return_25K": 155.7,
2382	    "eval_return_35K": 190.8,
2383	    "eval_return_45K": 137.1,
2384	    "eval_return_55K": 210.7,
2385	    "eval_return_5K": 31.7,
2386	    "eval_return_65K": 189.5,
2387	    "eval_return_75K": 253.2,
2388	    "eval_return_85K": 259.5,
2389	    "eval_return_95K": 349.6,
2390	    "gate_dt2_frac": 1.0,
2391	    "gate_entropy": 0.0,
2392	    "nve_peak": 3.0,
2393	    "nve_peak_step": 105000,
2394	    "step": 224000,
2395	    "value_mean_105K": 218.37,
2396	    "value_mean_215K": 42.55,
2397	    "value_mean_95K": 232.74,
2398	    "ve_ratio_105K": 3.0,
2399	    "ve_ratio_115K": 2.5,
2400	    "ve_ratio_125K": 2.4,
2401	    "ve_ratio_135K": 0.9,
2402	    "ve_ratio_145K": 1.141,
2403	    "ve_ratio_155K": 1.06,
2404	    "ve_ratio_165K": 0.91,
2405	    "ve_ratio_175K": 0.556,
2406	    "ve_ratio_185K": 0.396,
2407	    "ve_ratio_195K": 0.78,
2408	    "ve_ratio_205K": 0.747,
2409	    "ve_ratio_215K": 0.4,
2410	    "ve_ratio_45K": 0.695,
2411	    "ve_ratio_55K": 0.598,
2412	    "ve_ratio_65K": 0.863,
2413	    "ve_ratio_75K": 0.791,
2414	    "ve_ratio_85K": 0.9,
2415	    "ve_ratio_95K": 0.7
2416	}
2417	
2418	  exp_id: exp_032_dual_critic_walker
2419	  status: DONE
2420	  description: 
2421	  tags: 
2422	  conclusion: success
2423	  metrics: {
2424	    "baseline_eval": 900,
2425	    "civo_prevented": true,
2426	    "eval_final": 739.7,
2427	    "eval_final_step": 215000,
2428	    "eval_peak": 787.7,
2429	    "eval_peak_step": 205000,
2430	    "eval_vs_baseline_pct": 87.5,
2431	    "gate_dt2_frac": 1.0,
2432	    "gate_entropy": 0.0,
2433	    "note": "CIVO prevented 2/2 seeds. v1\u2248v2 \u2192 mechanism is implicit value regularization, not min-of-two pessimism.",
2434	    "nve_final": 0.1,
2435	    "nve_peak": 1.1,
2436	    "nve_peak_step": 95000,
2437	    "v1_v2_gap": "<0.1% (min operation has no pessimism effect)"
2438	}
2439	
2440	  exp_id: exp_032b_dual_critic_walker_s1
2441	  status: DONE
2442	  description: 
2443	  tags: 
2444	  conclusion: success
2445	  metrics: {
2446	    "actor_loss_late": "\u22480 (gradient signal weak)",
2447	    "baseline_eval": 900,
2448	    "director_override": "CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.",
2449	    "eval_criterion_pass": false,
2450	    "eval_trajectory": "75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516",
2451	    "eval_vs_baseline_pct": 57,
2452	    "final_eval_return": 516,
2453	    "final_nve": 0.1,
2454	    "gate_dt2_frac": 1.0,
2455	    "nve_criterion_pass": true,
2456	    "nve_trajectory": "15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1",
2457	    "peak_eval_return": 551.8,
2458	    "peak_nve": 1.4,
2459	    "total_steps": 224000,
2460	    "total_updates": 52599,
2461	    "training_hours": 6.42,
2462	    "value1_value2_gap": "<0.5 (min operation has no pessimism effect)"
2463	}
2464	
2465	  exp_id: exp_033_wide_critic_walker
2466	  status: DONE
2467	  description: 
2468	  tags: 
2469	  conclusion: success
2470	  metrics: {
2471	    "civo_alert_step": 105000,
2472	    "civo_alert_ve_ratio": 1.958,
2473	    "civo_instability_duration_steps": 75000,
2474	    "critic_params": 2886911,
2475	    "eval_reward_final": 407.9,
2476	    "eval_reward_peak": 194.8,
2477	    "eval_reward_trough": 31.8,
2478	    "value_loss_final": 1.4,
2479	    "ve_ratio_final": 0.1,
2480	    "ve_ratio_peak": 4.7
2481	}
2482	
2483	  exp_id: exp_035_narrow_dual_critic_walker
2484	  status: DONE
2485	  description: 
2486	  tags: 
2487	  conclusion: success
2488	  metrics: {
2489	    "actor_entropy_final": -0.19,
2490	    "civo_alert_window": "65K-85K",
2491	    "civo_prevented": false,
2492	    "civo_recovery": true,
2493	    "director_override": "Director ruled success: CIVO recovery (33.8\u2192697.8) is the success criterion, not prevention",
2494	    "eval_at_215K": 697.8,
2495	    "eval_at_85K": 33.8,
2496	    "eval_final": 697.8,
2497	    "eval_peak": 697.8,
2498	    "eval_trough": 33.8,
2499	    "nve_final": 0.066,
2500	    "nve_peak": 2.75,
2501	    "nve_peak_step": 85000,
2502	    "recovery_from": 33.8,
2503	    "recovery_to": 697.8,
2504	    "total_steps": 215000,
2505	    "train_return_final_range": "708-806",
2506	    "v1_v2_gap_max": 0.08,
2507	    "v1_v2_gap_typical": 0.01
2508	}
2509	
2510	  exp_id: exp_038_dual_critic_walker_s2
2511	  status: DONE
2512	  description: 
2513	  tags: 
2514	  conclusion: negative
2515	  metrics: {
2516	    "civo_alert": 0,
2517	    "civo_prevented": true,
2518	    "eval_return_collapse": 99.6,
2519	    "eval_return_collapse_step": 175000,
2520	    "eval_return_final": 120.9,
2521	    "eval_return_peak": 354,
2522	    "eval_return_peak_step": 155000,
2523	    "gate_dt_2_frac": 1,
2524	    "non_civo_collapse": true,
2525	    "note": "CIVO prevented (NVE\u22640.3) but non-CIVO eval collapse at 175k (354\u219299.6). Different failure mode from value overestimation.",
2526	    "nve_final": 0.248,
2527	    "nve_peak": 0.3,
2528	    "steps": 224000
2529	}
2530	
2531	  exp_id: exp_039_narrow_dual_critic_walker_s1
2532	  status: DONE
2533	  description: 
2534	  tags: 
2535	  conclusion: success
2536	  metrics: {
2537	    "civo_recovery": true,
2538	    "eval_return_final": 592.7,
2539	    "note": "Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean\u2248645. Recovery 2/2.",
2540	    "nve_peak": 2.19,
2541	    "recovery_confirmed": true
2542	}
2543	
2544	  exp_id: exp_041_dual_critic_walker_s3
2545	  status: DONE
2546	  description: 
2547	  tags: 
2548	  conclusion: success
2549	  metrics: {
2550	    "eval_return_peak": 761.1,
2551	    "eval_return_final": 544,
2552	    "eval_return_peak_step": 165000,
2553	    "nve_peak": 1.5,
2554	    "nve_final": 0.1,
2555	    "civo_prevented": true,
2556	    "gate_dt_2_frac": 1,
2557	    "non_civo_collapse": false,
2558	    "steps": 215000,
2559	    "note": "CIVO prevented (NVE\u22641.5), no non-CIVO collapse. Eval stays 486-761 after peak. Non-CIVO collapse rate confirmed 1/4 (only s2)."
2560	}
2561	
2562	  exp_id: exp_042_frozen_dt_emb_walker
2563	  status: DONE
2564	  description: 
2565	  tags: 
2566	  conclusion: success
2567	  metrics: {
2568	    "eval_final": 612.45,
2569	    "eval_peak": 682.38,
2570	    "eval_peak_step": 205000,
2571	    "nve_peak": 0.194,
2572	    "nve_final": 0.051,
2573	    "civo_alert": false,
2574	    "total_steps": 224000,
2575	    "total_train_episodes": 224
2576	}
2577	
2578	  exp_id: exp_043_008f_walker_s1
2579	  status: DONE
2580	  description: 
2581	  tags: 
2582	  conclusion: success
2583	  metrics: {
2584	    "eval_final": 673.73,
2585	    "eval_peak": 673.73,
2586	    "eval_peak_step": 215000,
2587	    "nve_peak": 0.808,
2588	    "nve_peak_step": 105000,
2589	    "nve_final": 0.123,
2590	    "civo_alert": false,
2591	    "total_steps": 224000,
2592	    "gate_dt_2_frac": 1,
2593	    "gate_entropy": 0,
2594	    "note": "No CIVO (peak NVE 0.808, well below 1.5). Gate fixed at dt=2. Seed 1 replicates seed 0 finding: dt_emb absence prevents CIVO."
2595	}
2596	
2597	  exp_id: exp_044_gradient_stop_walker
2598	  status: DONE
2599	  description: 
2600	  tags: 
2601	  conclusion: success
2602	  metrics: {
2603	    "eval_final": 538.6,
2604	    "eval_peak": 561.2,
2605	    "eval_peak_step": 185000,
2606	    "eval_civo_trough": 44.3,
2607	    "eval_civo_trough_step": 95000,
2608	    "ve_ratio_peak": 4.4,
2609	    "ve_ratio_peak_step": 95000,
2610	    "ve_ratio_final": 0.1,
2611	    "civo_onset_step": 85000,
2612	    "civo_resolved_step": 125000,
2613	    "civo_duration_steps": 40000,
2614	    "total_steps": 224000,
2615	    "pre_civo_peak": 545.6,
2616	    "pre_civo_peak_step": 75000
2617	}
2618	
2619	  exp_id: exp_047_frozen_dt_emb_walker_s1
2620	  status: DONE
2621	  description: 
2622	  tags: 
2623	  conclusion: success
2624	  metrics: {
2625	    "eval_final": 144.22,
2626	    "eval_final_step": 215000,
2627	    "eval_peak": 408.79,
2628	    "eval_peak_step": 125000,
2629	    "ve_ratio_peak": 1.099,
2630	    "ve_ratio_peak_step": 75000,
2631	    "ve_ratio_final": 0.277,
2632	    "nve_peak": 1.71,
2633	    "nve_peak_step": 95000,
2634	    "nve_final_105k": 0.56,
2635	    "total_steps": 225000
2636	}
2637	
2638	  exp_id: exp_057_frozen_dt_emb_walker_s2
2639	  status: DONE
2640	  description: 
2641	  tags: 
2642	  conclusion: success
2643	  metrics: {
2644	    "total_steps": 225000,
2645	    "ve_ratio_peak": 1.283,
2646	    "ve_ratio_peak_step": 115000,
2647	    "ve_ratio_final": 0.177,
2648	    "ve_ratio_final_step": 215000,
2649	    "nve_peak": 1.88,
2650	    "nve_peak_step": 115000,
2651	    "nve_classification": "transient",
2652	    "note": "Walker frozen s2. NVE=1.88\u00d7 (raw 1.283 / baseline 0.683 @115K). Peak transient at 115K, self-corrected. Walker frozen n=3: s0=0.19, s1=1.71, s2=1.88 \u2014 all transient, no sustained CIVO."
2653	}
2654	
2655	============================================================
2656	5. CHEETAH BASELINE EXPERIMENTS
2657	============================================================
2658	Found 26: ['exp_058_frozen_dt_emb_cheetah_s1', 'exp_048_cheetah_civo_extension', 'exp_046_frozen_dt_emb_cheetah', 'exp_040_wide_dual_critic_cheetah', 'exp_037_wide_critic_cheetah', 'exp_034_dual_critic_cheetah', 'exp_030c_tcn_cheetah_s0_sigma10', 'exp_030b_tcn_cheetah_s0_sigma05', 'exp_030a_tcn_cheetah_s0_sigma02', 'exp_026_obs_sgs_cheetah_s1', 'exp_026_obs_sgs_cheetah_s0', 'exp_023_cheetah_baseline_s4_extended', 'exp_023_cheetah_baseline_s4', 'exp_023_cheetah_baseline_s3', 'exp_023_cheetah_baseline_s2', 'exp_008a_cheetah_unexposed_s1', 'exp_008a_cheetah_unexposed_s0', 'exp_010b_cheetah_civo_trigger_s0', 'exp_024b_cheetah_no_dt_emb_s0', 'exp_024b_cheetah_no_dt_emb_s1', 'exp_024_cheetah_no_dt_emb_s0', 'exp_021_full_sgs_cheetah_s1', 'exp_023a_cheetah_baseline_s0', 'exp_010b_cheetah_civo_trigger', 'exp_023b_cheetah_baseline_s1', 'exp_010a_cheetah_baseline_s1']
2659	  exp_id: exp_008a_cheetah_unexposed_s0
2660	  status: DONE
2661	  description: 
2662	  tags: 
2663	  conclusion: success
2664	  metrics: {
2665	    "current_step": 112000,
2666	    "eval_return_105k": 532.35,
2667	    "nve_105k": 0.49,
2668	    "target_steps": 105000,
2669	    "value_mean_105k": 169.98,
2670	    "ve_ratio_105k": 0.3193
2671	}
2672	
2673	  exp_id: exp_008a_cheetah_unexposed_s1
2674	  status: DONE
2675	  description: 
2676	  tags: 
2677	  conclusion: success
2678	  metrics: {
2679	    "current_step": 112000,
2680	    "eval_return_105k": 504.38,
2681	    "nve_105k": 0.478,
2682	    "target_steps": 105000,
2683	    "value_mean_105k": 156.97,
2684	    "ve_ratio_105k": 0.3112
2685	}
2686	
2687	  exp_id: exp_010a_cheetah_baseline_s1
2688	  status: DONE
2689	  description: 
2690	  tags: 
2691	  conclusion: success
2692	  metrics: {
2693	    "eval_return_final": 849.8,
2694	    "eval_return_final_step": 515000,
2695	    "eval_return_peak": 849.8,
2696	    "eval_return_peak_step": 515000,
2697	    "final_step": 524000,
2698	    "total_eval_episodes": 52,
2699	    "train_return_last": 716
2700	}
2701	
2702	  exp_id: exp_010b_cheetah_civo_trigger
2703	  status: DONE
2704	  description: 
2705	  tags: 
2706	  conclusion: success
2707	  metrics: {
2708	    "civo": true,
2709	    "eval_return_final": 51.7,
2710	    "eval_return_peak": 321.9,
2711	    "nve_peak": 8.27,
2712	    "nve_peak_step": 65000,
2713	    "peak_step": 35000
2714	}
2715	
2716	  exp_id: exp_010b_cheetah_civo_trigger_s0
2717	  status: DONE
2718	  description: 
2719	  tags: 
2720	  conclusion: success
2721	  metrics: {
2722	    "civo": true,
2723	    "civo_onset_step": "65K",
2724	    "detector_alert_step": "95K",
2725	    "eval_return_105K": 0.83,
2726	    "eval_return_peak": 247.77,
2727	    "eval_return_peak_step": "35K",
2728	    "gate_dt_mean": 2,
2729	    "gate_entropy": 0,
2730	    "nve_105K": 70.64,
2731	    "nve_95K": 6.34
2732	}
2733	
2734	  exp_id: exp_021_full_sgs_cheetah_s1
2735	  status: DONE
2736	  description: 
2737	  tags: 
2738	  conclusion: negative
2739	  metrics: {
2740	    "baseline_pct": 38.7,
2741	    "civo": true,
2742	    "civo_type": "transient_self_correcting",
2743	    "eval_return_final": 221.5,
2744	    "nve_peak": 9.94,
2745	    "nve_peak_step": "45K",
2746	    "nve_sustained_55K_105K": 0.338,
2747	    "vs_010b": "221.5 vs 51.7 (4.3x better)"
2748	}
2749	
2750	  exp_id: exp_023_cheetah_baseline_s2
2751	  status: DONE
2752	  description: 
2753	  tags: 
2754	  conclusion: success
2755	  metrics: {
2756	    "current_step": 205000,
2757	    "eval_return_final": 645.4,
2758	    "note": "Cheetah Run baseline seed=2. Third baseline seed for NVE normalization.",
2759	    "target_steps": 200000
2760	}
2761	
2762	  exp_id: exp_023_cheetah_baseline_s3
2763	  status: DONE
2764	  description: 
2765	  tags: 
2766	  conclusion: success
2767	  metrics: {
2768	    "current_step": 204000,
2769	    "eval_return_202k": 642.13,
2770	    "peak_eval": 685.93,
2771	    "peak_eval_step": 172000,
2772	    "target_steps": 200000,
2773	    "value_mean_final": 445.42,
2774	    "ve_ratio_final": 0.694
2775	}
2776	
2777	  exp_id: exp_023_cheetah_baseline_s4
2778	  status: DONE
2779	  description: 
2780	  tags: 
2781	  conclusion: success
2782	  metrics: {
2783	    "current_step": 212000,
2784	    "eval_return_194k": 537.03,
2785	    "eval_return_204k": 301.69,
2786	    "note": "Cheetah baseline s4. Large eval drop 194K\u2192204K (537\u2192302). ve_ratio>1 indicates value overestimation at final step.",
2787	    "peak_eval": 537.03,
2788	    "peak_eval_step": 194000,
2789	    "target_steps": 200000,
2790	    "value_mean_204k": 339.14,
2791	    "ve_ratio_204k": 1.124
2792	}
2793	
2794	  exp_id: exp_023_cheetah_baseline_s4_extended
2795	  status: DONE
2796	  description: 
2797	  tags: 
2798	  conclusion: success
2799	  metrics: {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "f96149f8-d3a4-433d-88b4-6e6a20e732c9"
}
```

</details>

---


### System

_source line 116_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 56951,
    "tool_uses": 8,
    "duration_ms": 48447
  },
  "last_tool_name": "Read",
  "uuid": "81c50f74-ff58-4551-9120-938806793d73",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Read · `toolu_01Cioc9HVNjTkwgedox27MtB`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "offset": 2800,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "2beddde0-560f-4082-8a66-3fc418f357b2",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TvjKeGMNX3r757MxqoKU8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9757,
      "cache_read_input_tokens": 46927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9757,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 118 · 2026-05-24T02:15:17.588Z_

<details><summary>↩ Tool result · `toolu_01Cioc9HVNjTkwgedox27MtB`</summary>

```text
2800	    "eval_302k": 580,
2801	    "eval_peak_ext": 642.3,
2802	    "eval_peak_ext_step": 272000,
2803	    "note": "\u5ef6\u957f\u5230 300K \u786e\u8ba4\u975e collapse\u3002eval \u6062\u590d\u5230 642 peak@272K\uff0c200K-300K \u533a\u95f4\u9707\u8361\u4e0a\u884c (301-642 range)\uff0c194K\u2192204K \u9aa4\u964d\u4e3a transient fluctuation\u3002"
2804	}
2805	
2806	  exp_id: exp_023a_cheetah_baseline_s0
2807	  status: DONE
2808	  description: 
2809	  tags: 
2810	  conclusion: success
2811	  metrics: {
2812	    "civo": false,
2813	    "eval_return_final": 624.7,
2814	    "eval_return_peak": 624.7,
2815	    "peak_step": 205000
2816	}
2817	
2818	  exp_id: exp_023b_cheetah_baseline_s1
2819	  status: DONE
2820	  description: 
2821	  tags: 
2822	  conclusion: success
2823	  metrics: {
2824	    "civo": false,
2825	    "eval_return_final": 520.3,
2826	    "eval_return_peak": 572.9,
2827	    "peak_step": 195000,
2828	    "ve_ratio_range": "0.5-0.7"
2829	}
2830	
2831	  exp_id: exp_024_cheetah_no_dt_emb_s0
2832	  status: DONE
2833	  description: 
2834	  tags: 
2835	  conclusion: killed
2836	  metrics: {}
2837	
2838	  exp_id: exp_024b_cheetah_no_dt_emb_s0
2839	  status: DONE
2840	  description: 
2841	  tags: 
2842	  conclusion: success
2843	  metrics: {
2844	    "civo": false,
2845	    "eval_return_final": 96.5,
2846	    "nve_peak": 0.2
2847	}
2848	
2849	  exp_id: exp_024b_cheetah_no_dt_emb_s1
2850	  status: DONE
2851	  description: 
2852	  tags: 
2853	  conclusion: success
2854	  metrics: {
2855	    "baseline_pct": 14.1,
2856	    "civo": false,
2857	    "eval_return_final": 77.3,
2858	    "eval_return_peak": 129.6,
2859	    "gate_dt_2_frac": 1,
2860	    "nve_peak": 0.1,
2861	    "peak_step": 15000
2862	}
2863	
2864	  exp_id: exp_026_obs_sgs_cheetah_s0
2865	  status: DONE
2866	  description: 
2867	  tags: 
2868	  conclusion: failed
2869	  metrics: {}
2870	
2871	  exp_id: exp_026_obs_sgs_cheetah_s1
2872	  status: DONE
2873	  description: 
2874	  tags: 
2875	  conclusion: failed
2876	  metrics: {}
2877	
2878	  exp_id: exp_030a_tcn_cheetah_s0_sigma02
2879	  status: DONE
2880	  description: 
2881	  tags: 
2882	  conclusion: negative
2883	  metrics: {
2884	    "current_step": 64000,
2885	    "eval_return_35K": 299.5,
2886	    "eval_return_55K": 31.9,
2887	    "note": "WARNING: NVE breached 1.5\u00d7 at 55K (1.903), eval crashed 299\u219232. Possible CIVO despite TCN.",
2888	    "target_steps": 210000,
2889	    "ve_ratio_55K": 1.903
2890	}
2891	
2892	  exp_id: exp_030b_tcn_cheetah_s0_sigma05
2893	  status: DONE
2894	  description: 
2895	  tags: 
2896	  conclusion: negative
2897	  metrics: {
2898	    "current_step": 195000,
2899	    "eval_return_105K": 104.4,
2900	    "eval_return_115K": 137.7,
2901	    "eval_return_125K": 211.7,
2902	    "eval_return_135K": 97.2,
2903	    "eval_return_145K": 79.4,
2904	    "eval_return_155K": 76.8,
2905	    "eval_return_15K": 78.3,
2906	    "eval_return_165K": 77.5,
2907	    "eval_return_175K": 85.7,
2908	    "eval_return_185K": 68.7,
2909	    "eval_return_195K": 77.6,
2910	    "eval_return_25K": 219.3,
2911	    "eval_return_35K": 296.5,
2912	    "eval_return_45K": 32.8,
2913	    "eval_return_55K": 6,
2914	    "eval_return_5K": 8.3,
2915	    "eval_return_65K": 71.2,
2916	    "eval_return_75K": 23.3,
2917	    "eval_return_85K": 34,
2918	    "eval_return_95K": 143.6,
2919	    "nve_final": 0.1534,
2920	    "nve_max": 10.6657,
2921	    "nve_max_step": "55K",
2922	    "target_steps": 210000,
2923	    "ve_ratio_105K": 0.2686,
2924	    "ve_ratio_115K": 0.1789,
2925	    "ve_ratio_125K": 0.1037,
2926	    "ve_ratio_135K": 0.2153,
2927	    "ve_ratio_145K": 0.2478,
2928	    "ve_ratio_155K": 0.2392,
2929	    "ve_ratio_15K": 0.0202,
2930	    "ve_ratio_165K": 0.202,
2931	    "ve_ratio_175K": 0.1591,
2932	    "ve_ratio_185K": 0.1834,
2933	    "ve_ratio_195K": 0.1534,
2934	    "ve_ratio_25K": 0.0636,
2935	    "ve_ratio_35K": 0.1238,
2936	    "ve_ratio_45K": 1.9141,
2937	    "ve_ratio_55K": 10.6657,
2938	    "ve_ratio_65K": 0.8371,
2939	    "ve_ratio_75K": 1.9823,
2940	    "ve_ratio_85K": 1.0946,
2941	    "ve_ratio_95K": 0.2253
2942	}
2943	
2944	  exp_id: exp_030c_tcn_cheetah_s0_sigma10
2945	  status: DONE
2946	  description: 
2947	  tags: 
2948	  conclusion: negative
2949	  metrics: {
2950	    "baseline_eval_avg": 548,
2951	    "eval_final": 47.2,
2952	    "eval_peak": 371.7,
2953	    "eval_peak_step": 35000,
2954	    "eval_return_105K": 122.5,
2955	    "eval_return_115K": 162.2,
2956	    "eval_return_125K": 148.5,
2957	    "eval_return_135K": 138.4,
2958	    "eval_return_145K": 100.4,
2959	    "eval_return_155K": 144.3,
2960	    "eval_return_15K": 87.5,
2961	    "eval_return_165K": 130.9,
2962	    "eval_return_175K": 66.4,
2963	    "eval_return_185K": 47.2,
2964	    "eval_return_195K": 56.5,
2965	    "eval_return_205K": 49.7,
2966	    "eval_return_215K": 47.2,
2967	    "eval_return_25K": 166.3,
2968	    "eval_return_35K": 371.7,
2969	    "eval_return_45K": 144.0,
2970	    "eval_return_55K": 266.0,
2971	    "eval_return_5K": 8.3,
2972	    "eval_return_65K": 197.0,
2973	    "eval_return_75K": 107.8,
2974	    "eval_return_85K": 95.8,
2975	    "eval_return_95K": 72.8,
2976	    "eval_vs_baseline": "8.6%",
2977	    "gate_dt2_frac": 1.0,
2978	    "gate_dt_mean": 2.0,
2979	    "gate_entropy": 0.0,
2980	    "step": 224000,
2981	    "ve_ratio_max": 0.4
2982	}
2983	
2984	  exp_id: exp_034_dual_critic_cheetah
2985	  status: DONE
2986	  description: 
2987	  tags: 
2988	  conclusion: negative
2989	  metrics: {
2990	    "baseline_eval_final": 0.83,
2991	    "baseline_nve_peak": 70.64,
2992	    "civo_alert_steps": [
2993	        95000,
2994	        105000
2995	    ],
2996	    "civo_alerts": 2,
2997	    "civo_prevented": false,
2998	    "dual_wave_civo": true,
2999	    "eval_final": 97.5,
3000	    "eval_final_step": 215000,
3001	    "eval_peak": 315.7,
3002	    "eval_peak_step": 45000,
3003	    "eval_vs_peak_pct": 31,
3004	    "gate_dt2_frac": 1,
3005	    "gate_entropy": 0,
3006	    "v1_v2_gap": "<0.2 (min operation has no pessimism effect)",
3007	    "value_mean_final": 14.2,
3008	    "value_mean_peak": 60.5,
3009	    "ve_ratio_final": 0.1,
3010	    "ve_ratio_peak": 1.8,
3011	    "ve_ratio_peak_step": 55000
3012	}
3013	
3014	  exp_id: exp_037_wide_critic_cheetah
3015	  status: DONE
3016	  description: 
3017	  tags: 
3018	  conclusion: negative
3019	  metrics: {
3020	    "civo_alert": 0,
3021	    "eval_return_final": 146.1,
3022	    "eval_return_peak": 350.1,
3023	    "gate_dt_2_frac": 1,
3024	    "nve_final": 0.1,
3025	    "nve_peak": 3.6,
3026	    "steps": 224000
3027	}
3028	
3029	  exp_id: exp_040_wide_dual_critic_cheetah
3030	  status: DONE
3031	  description: 
3032	  tags: 
3033	  conclusion: success
3034	  metrics: {}
3035	
3036	  exp_id: exp_046_frozen_dt_emb_cheetah
3037	  status: DONE
3038	  description: 
3039	  tags: 
3040	  conclusion: success
3041	  metrics: {
3042	    "eval_final": 150.5,
3043	    "eval_peak": 207.4,
3044	    "eval_peak_step": 145000,
3045	    "ve_ratio_peak": 0.4,
3046	    "ve_ratio_final": 0.1,
3047	    "nve_peak": 1.35,
3048	    "nve_peak_step": 45000,
3049	    "nve_final": 0.17,
3050	    "total_steps": 224000,
3051	    "civo_alert_count": 0
3052	}
3053	
3054	  exp_id: exp_048_cheetah_civo_extension
3055	  status: DONE
3056	  description: 
3057	  tags: 
3058	  conclusion: success
3059	  metrics: {
3060	    "eval_final": 23.4,
3061	    "eval_final_step": 302000,
3062	    "eval_peak": 32.8,
3063	    "eval_peak_step": 252000,
3064	    "ve_ratio_initial": 46.3,
3065	    "ve_ratio_peak": 24.112,
3066	    "ve_ratio_peak_step": 162000,
3067	    "ve_ratio_final": 1.803,
3068	    "nve_initial": 70.64,
3069	    "nve_peak_secondary": 36.76,
3070	    "nve_final": 2.75,
3071	    "total_steps": 312000,
3072	    "civo_self_corrected": false,
3073	    "civo_correction_pct": 96,
3074	    "secondary_burst_step": 152000,
3075	    "secondary_burst_nve": 36.47,
3076	    "gate_collapsed": true
3077	}
3078	
3079	  exp_id: exp_058_frozen_dt_emb_cheetah_s1
3080	  status: DONE
3081	  description: 
3082	  tags: 
3083	  conclusion: success
3084	  metrics: {
3085	    "total_steps": 224000,
3086	    "ve_ratio_peak": 0.231,
3087	    "ve_ratio_peak_step": 45000,
3088	    "ve_ratio_final": 0.107,
3089	    "ve_ratio_final_step": 215000,
3090	    "eval_return_final": 80.46,
3091	    "eval_return_final_step": 215000,
3092	    "eval_return_peak": 191.74,
3093	    "eval_return_peak_step": 25000,
3094	    "nve_peak": 0.78,
3095	    "nve_peak_step": 45000,
3096	    "nve_classification": "no_civo",
3097	    "note": "Cheetah frozen s1. NVE=0.78\u00d7 (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 \u2014 both clean, frozen \u7a33\u5065\u963b\u6b62 extreme CIVO (trained NVE 70-108)."
3098	}
3099	
3100	============================================================
3101	6. EXP_057 AND EXP_058
3102	============================================================
3103	Matches for exp_057: ['exp_057_frozen_dt_emb_walker_s2']
3104	  exp_id: exp_057_frozen_dt_emb_walker_s2
3105	  status: DONE
3106	  description: 
3107	  tags: 
3108	  conclusion: success
3109	  metrics: {
3110	    "total_steps": 225000,
3111	    "ve_ratio_peak": 1.283,
3112	    "ve_ratio_peak_step": 115000,
3113	    "ve_ratio_final": 0.177,
3114	    "ve_ratio_final_step": 215000,
3115	    "nve_peak": 1.88,
3116	    "nve_peak_step": 115000,
3117	    "nve_classification": "transient",
3118	    "note": "Walker frozen s2. NVE=1.88\u00d7 (raw 1.283 / baseline 0.683 @115K). Peak transient at 115K, self-corrected. Walker frozen n=3: s0=0.19, s1=1.71, s2=1.88 \u2014 all transient, no sustained CIVO."
3119	}
3120	
3121	Matches for exp_058: ['exp_058_frozen_dt_emb_cheetah_s1']
3122	  exp_id: exp_058_frozen_dt_emb_cheetah_s1
3123	  status: DONE
3124	  description: 
3125	  tags: 
3126	  conclusion: success
3127	  metrics: {
3128	    "total_steps": 224000,
3129	    "ve_ratio_peak": 0.231,
3130	    "ve_ratio_peak_step": 45000,
3131	    "ve_ratio_final": 0.107,
3132	    "ve_ratio_final_step": 215000,
3133	    "eval_return_final": 80.46,
3134	    "eval_return_final_step": 215000,
3135	    "eval_return_peak": 191.74,
3136	    "eval_return_peak_step": 25000,
3137	    "nve_peak": 0.78,
3138	    "nve_peak_step": 45000,
3139	    "nve_classification": "no_civo",
3140	    "note": "Cheetah frozen s1. NVE=0.78\u00d7 (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 \u2014 both clean, frozen \u7a33\u5065\u963b\u6b62 extreme CIVO (trained NVE 70-108)."
3141	}
3142	
3143	============================================================
3144	7. FROZEN IN NAME (name-only search)
3145	============================================================
3146	Found 10: ['exp_058_frozen_dt_emb_cheetah_s1', 'exp_056_peginsertion_frozen_s1', 'exp_057_frozen_dt_emb_walker_s2', 'exp_054_pickcube_frozen_s0', 'exp_053_peginsertion_frozen_s0', 'exp_051_stackcube_frozen_dt_emb_s0', 'exp_047_frozen_dt_emb_walker_s1', 'exp_046_frozen_dt_emb_cheetah', 'exp_042_frozen_dt_emb_walker', 'exp_015b_frozen_dt_emb']
3147	  exp_id: exp_015b_frozen_dt_emb
3148	  status: DONE
3149	  description: 
3150	  tags: 
3151	  conclusion: negative
3152	  metrics: {
3153	    "actor_entropy_105K": -4.855,
3154	    "actor_loss_105K": 0.000179,
3155	    "collapse_mechanism": "gradient_starvation_from_frozen_dt_emb",
3156	    "data_source": "worker SSH final analysis 2026-05-15T18:30",
3157	    "eval_return_105K": 204.2,
3158	    "eval_return_15K": 167.9,
3159	    "eval_return_25K": 171.8,
3160	    "eval_return_35K": 201.6,
3161	    "eval_return_45K": 122.3,
3162	    "eval_return_55K": 105.8,
3163	    "eval_return_5K": 31,
3164	    "eval_return_65K": 160.3,
3165	    "eval_return_75K": 80,
3166	    "eval_return_85K": 183.5,
3167	    "eval_return_95K": 238.4,
3168	    "final_eval": 204.2,
3169	    "final_step": 112000,
3170	    "gate_dt_1_frac": 0,
3171	    "gate_dt_mean": 2,
3172	    "nve_105K": 0.42,
3173	    "nve_85K": 0.467,
3174	    "nve_95K": 0.394,
3175	    "summary": "NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss\u21920 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence",
3176	    "value_mean_105K": 56.212,
3177	    "value_std_105K": 13.818
3178	}
3179	
3180	  exp_id: exp_042_frozen_dt_emb_walker
3181	  status: DONE
3182	  description: 
3183	  tags: 
3184	  conclusion: success
3185	  metrics: {
3186	    "eval_final": 612.45,
3187	    "eval_peak": 682.38,
3188	    "eval_peak_step": 205000,
3189	    "nve_peak": 0.194,
3190	    "nve_final": 0.051,
3191	    "civo_alert": false,
3192	    "total_steps": 224000,
3193	    "total_train_episodes": 224
3194	}
3195	
3196	  exp_id: exp_046_frozen_dt_emb_cheetah
3197	  status: DONE
3198	  description: 
3199	  tags: 
3200	  conclusion: success
3201	  metrics: {
3202	    "eval_final": 150.5,
3203	    "eval_peak": 207.4,
3204	    "eval_peak_step": 145000,
3205	    "ve_ratio_peak": 0.4,
3206	    "ve_ratio_final": 0.1,
3207	    "nve_peak": 1.35,
3208	    "nve_peak_step": 45000,
3209	    "nve_final": 0.17,
3210	    "total_steps": 224000,
3211	    "civo_alert_count": 0
3212	}
3213	
3214	  exp_id: exp_047_frozen_dt_emb_walker_s1
3215	  status: DONE
3216	  description: 
3217	  tags: 
3218	  conclusion: success
3219	  metrics: {
3220	    "eval_final": 144.22,
3221	    "eval_final_step": 215000,
3222	    "eval_peak": 408.79,
3223	    "eval_peak_step": 125000,
3224	    "ve_ratio_peak": 1.099,
3225	    "ve_ratio_peak_step": 75000,
3226	    "ve_ratio_final": 0.277,
3227	    "nve_peak": 1.71,
3228	    "nve_peak_step": 95000,
3229	    "nve_final_105k": 0.56,
3230	    "total_steps": 225000
3231	}
3232	
3233	  exp_id: exp_051_stackcube_frozen_dt_emb_s0
3234	  status: DONE
3235	  description: 
3236	  tags: 
3237	  conclusion: success
3238	  metrics: {
3239	    "ve_ratio_peak": 4.3,
3240	    "ve_ratio_peak_step": 42500,
3241	    "ve_ratio_final": 0.122,
3242	    "ve_ratio_final_step": 212500,
3243	    "eval_final": 45.31,
3244	    "eval_final_step": 212500,
3245	    "eval_peak": 45.31,
3246	    "eval_peak_step": 212500,
3247	    "total_steps": 222400
3248	}
3249	
3250	  exp_id: exp_053_peginsertion_frozen_s0
3251	  status: DONE
3252	  description: 
3253	  tags: 
3254	  conclusion: success
3255	  metrics: {}
3256	
3257	  exp_id: exp_054_pickcube_frozen_s0
3258	  status: DONE
3259	  description: 
3260	  tags: 
3261	  conclusion: success
3262	  metrics: {}
3263	
3264	  exp_id: exp_056_peginsertion_frozen_s1
3265	  status: DONE
3266	  description: 
3267	  tags: 
3268	  conclusion: success
3269	  metrics: {
3270	    "total_steps": 222500,
3271	    "ve_ratio_peak": 11.321,
3272	    "ve_ratio_peak_step": 82500,
3273	    "ve_ratio_final": 1.193,
3274	    "ve_ratio_final_step": 212500,
3275	    "eval_return_final": 4.37,
3276	    "eval_return_final_step": 212500,
3277	    "eval_return_peak": 24.42,
3278	    "eval_return_peak_step": 132500,
3279	    "nve_classification": "burst",
3280	    "note": "Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 \u2014 frozen does NOT suppress ManiSkill transients.",
3281	    "ve_ratio_trajectory": {
3282	        "12500": 0.316,
3283	        "22500": 0.975,
3284	        "32500": 1.839,
3285	        "42500": 1.966,
3286	        "52500": 5.422,
3287	        "62500": 4.047,
3288	        "72500": 8.408,
3289	        "82500": 11.321,
3290	        "92500": 3.724,
3291	        "102500": 3.034,
3292	        "112500": 2.204,
3293	        "122500": 2.425,
3294	        "132500": 0.842,
3295	        "142500": 2.194,
3296	        "152500": 2.203,
3297	        "162500": 0.651,
3298	        "172500": 1.085,
3299	        "182500": 1.07,
3300	        "192500": 0.467,
3301	        "202500": 0.708,
3302	        "212500": 1.193
3303	    }
3304	}
3305	
3306	  exp_id: exp_057_frozen_dt_emb_walker_s2
3307	  status: DONE
3308	  description: 
3309	  tags: 
3310	  conclusion: success
3311	  metrics: {
3312	    "total_steps": 225000,
3313	    "ve_ratio_peak": 1.283,
3314	    "ve_ratio_peak_step": 115000,
3315	    "ve_ratio_final": 0.177,
3316	    "ve_ratio_final_step": 215000,
3317	    "nve_peak": 1.88,
3318	    "nve_peak_step": 115000,
3319	    "nve_classification": "transient",
3320	    "note": "Walker frozen s2. NVE=1.88\u00d7 (raw 1.283 / baseline 0.683 @115K). Peak transient at 115K, self-corrected. Walker frozen n=3: s0=0.19, s1=1.71, s2=1.88 \u2014 all transient, no sustained CIVO."
3321	}
3322	
3323	  exp_id: exp_058_frozen_dt_emb_cheetah_s1
3324	  status: DONE
3325	  description: 
3326	  tags: 
3327	  conclusion: success
3328	  metrics: {
3329	    "total_steps": 224000,
3330	    "ve_ratio_peak": 0.231,
3331	    "ve_ratio_peak_step": 45000,
3332	    "ve_ratio_final": 0.107,
3333	    "ve_ratio_final_step": 215000,
3334	    "eval_return_final": 80.46,
3335	    "eval_return_final_step": 215000,
3336	    "eval_return_peak": 191.74,
3337	    "eval_return_peak_step": 25000,
3338	    "nve_peak": 0.78,
3339	    "nve_peak_step": 45000,
3340	    "nve_classification": "no_civo",
3341	    "note": "Cheetah frozen s1. NVE=0.78\u00d7 (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 \u2014 both clean, frozen \u7a33\u5065\u963b\u6b62 extreme CIVO (trained NVE 70-108)."
3342	}
3343	
3344	============================================================
3345	8. ALL EXPERIMENTS WITH NVE IN METRICS/CONCLUSION
3346	============================================================
3347	Found 58: ['exp_058_frozen_dt_emb_cheetah_s1', 'exp_056_peginsertion_frozen_s1', 'exp_055_peginsertion_civo_trigger_s1', 'exp_057_frozen_dt_emb_walker_s2', 'exp_048_cheetah_civo_extension', 'exp_047_frozen_dt_emb_walker_s1', 'exp_046_frozen_dt_emb_cheetah', 'exp_045_treatment_extension_008d_s3', 'exp_043_008f_walker_s1', 'exp_042_frozen_dt_emb_walker', 'exp_041_dual_critic_walker_s3', 'exp_039_narrow_dual_critic_walker_s1', 'exp_038_dual_critic_walker_s2', 'exp_037_wide_critic_cheetah', 'exp_036_dual_critic_pickcube', 'exp_035_narrow_dual_critic_walker', 'exp_034', 'exp_034_dual_critic_cheetah', 'exp_031b_tcn_pickcube_s0_sigma05', 'exp_032_dual_critic_walker', 'exp_032b_dual_critic_walker_s1', 'exp_029d_tcn_walker_s3_sigma02', 'exp_029b_tcn_walker_s2_sigma02', 'exp_029c_tcn_walker_s0_sigma01', 'exp_029a_tcn_walker_s1_sigma02', 'exp_030b_tcn_cheetah_s0_sigma05', 'exp_027_tcn_walker_s1', 'exp_027_tcn_walker_s0_sigma02', 'exp_030a_tcn_cheetah_s0_sigma02', 'exp_027_tcn_walker_s0', 'exp_028_rave_walker_s0', 'exp_001_baseline_s4_extended', 'exp_001_baseline_s2_extended', 'exp_023_cheetah_baseline_s2', 'exp_008f_s4', 'exp_009c_s3', 'exp_008a_cheetah_unexposed_s1', 'exp_008a_cheetah_unexposed_s0', 'exp_008e_v3_s4', 'exp_008e_v3_s3', 'exp_010b_cheetah_civo_trigger_s0', 'exp_024b_cheetah_no_dt_emb_s0', 'exp_024b_cheetah_no_dt_emb_s1', 'exp_021_full_sgs_cheetah_s1', 'exp_010b_cheetah_civo_trigger', 'exp_019b_pickcube_civo_trigger', 'exp_022b_no_curriculum', 'exp_008d_civo_trigger_s3', 'exp_018v2_full_sgs_walker_s1', 'exp_009b_008d_walker_s2', 'exp_008f_s3_no_dt_embed_walker', 'exp_020_vanilla_dreamerv3_s2', 'exp_018_full_sgs_walker_s1', 'exp_016e_sgs_walker_s1', 'exp_015b_frozen_dt_emb', 'exp_009e_008d_walker_s1', 'exp_008e_v3_walker_s2', 'exp_006_fixed_dt2']
3348	  exp_id: exp_001_baseline_s2_extended
3349	  status: DONE
3350	  description: 
3351	  tags: 
3352	  conclusion: success
3353	  metrics: {
3354	    "eval_return_at_105K": 443.5,
3355	    "eval_return_final": 945.7,
3356	    "eval_return_peak": 962.6,
3357	    "total_steps": 512000,
3358	    "value_mean_at_105K": 329.16,
3359	    "value_mean_plateau": 665,
3360	    "ve_ratio_at_105K": 0.7422,
3361	    "ve_ratio_converged_range": "0.69-0.77"
3362	}
3363	
3364	  exp_id: exp_001_baseline_s4_extended
3365	  status: DONE
3366	  description: 
3367	  tags: 
3368	  conclusion: success
3369	  metrics: {
3370	    "convergence_mean_250k_plus": 935,
3371	    "final_eval_return": 938.86,
3372	    "final_step": 520000,
3373	    "peak_eval_return": 960.6
3374	}
3375	
3376	  exp_id: exp_006_fixed_dt2
3377	  status: DONE
3378	  description: 
3379	  tags: 
3380	  conclusion: negative
3381	  metrics: {
3382	    "baseline_35K": 388.5,
3383	    "baseline_45K": 513.8,
3384	    "baseline_55K": 625.7,
3385	    "data_source_ve": "from training logs metrics.jsonl",
3386	    "eval_return_15K": 256.9,
3387	    "eval_return_25K": 321.4,
3388	    "eval_return_35K": 485.3,
3389	    "eval_return_45K": 477,
3390	    "eval_return_55K": 360.4,
3391	    "eval_return_5K": 31,
3392	    "eval_return_65K": 132.86,
3393	    "fps": 6.5,
3394	    "gate_dt_mean": 2,
3395	    "gate_dt_std": 0,
3396	    "model_loss_15K": 7.593,
3397	    "model_loss_25K": 5.633,
3398	    "model_loss_35K": 5.229,
3399	    "model_loss_45K": 5.023,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "9612efc9-e4f1-4501-ab19-68be4b41d736"
}
```

</details>

---


### System

_source line 119_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 67188,
    "tool_uses": 9,
    "duration_ms": 53084
  },
  "last_tool_name": "Read",
  "uuid": "dd1f9eb5-06e3-4f55-a533-da43758e57ed",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 120_

<details open><summary>🔧 Tool call — Read · `toolu_016qe1H1RyPfkbLqTHTSuybt`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "offset": 3400,
  "limit": 700
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "99439ab0-2670-4845-b2a3-c6bb13f9a20f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01D74BxKj3UYHM6HWXZSaMou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10199,
      "cache_read_input_tokens": 56684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10199,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 121 · 2026-05-24T02:15:22.221Z_

<details><summary>↩ Tool result · `toolu_016qe1H1RyPfkbLqTHTSuybt`</summary>

```text
3400	    "model_loss_55K": 4.9,
3401	    "model_loss_5K": 20.738,
3402	    "peak_return": 485.3,
3403	    "peak_step": "35K",
3404	    "step": 65000,
3405	    "trend": "inverted-V: peak 485@35K, collapsing to 133@65K; v/e accelerating: 31.1%\u219253.3%\u219293.3%\u2192272% (value 2.7x eval_return at 65K)",
3406	    "value_eval_ratio_35K": 0.311,
3407	    "value_eval_ratio_45K": 0.533,
3408	    "value_eval_ratio_55K": 0.933,
3409	    "value_eval_ratio_65K": 2.722,
3410	    "value_mean_35K": 151.1,
3411	    "value_mean_45K": 254.29,
3412	    "value_mean_55K": 336.44,
3413	    "value_mean_65K": 361.69,
3414	    "vs_baseline_55K": "-42.4%"
3415	}
3416	
3417	  exp_id: exp_008a_cheetah_unexposed_s0
3418	  status: DONE
3419	  description: 
3420	  tags: 
3421	  conclusion: success
3422	  metrics: {
3423	    "current_step": 112000,
3424	    "eval_return_105k": 532.35,
3425	    "nve_105k": 0.49,
3426	    "target_steps": 105000,
3427	    "value_mean_105k": 169.98,
3428	    "ve_ratio_105k": 0.3193
3429	}
3430	
3431	  exp_id: exp_008a_cheetah_unexposed_s1
3432	  status: DONE
3433	  description: 
3434	  tags: 
3435	  conclusion: success
3436	  metrics: {
3437	    "current_step": 112000,
3438	    "eval_return_105k": 504.38,
3439	    "nve_105k": 0.478,
3440	    "target_steps": 105000,
3441	    "value_mean_105k": 156.97,
3442	    "ve_ratio_105k": 0.3112
3443	}
3444	
3445	  exp_id: exp_008d_civo_trigger_s3
3446	  status: DONE
3447	  description: 
3448	  tags: 
3449	  conclusion: success
3450	  metrics: {
3451	    "baseline_eval_105K": 915.67,
3452	    "collapse_onset_step": 95000,
3453	    "collapse_type": "late-onset",
3454	    "eval_return_final": 267.6,
3455	    "eval_return_final_step": 105000,
3456	    "eval_return_peak": 451.7,
3457	    "eval_return_peak_step": 95000,
3458	    "nve_final": 1.53,
3459	    "nve_onset_step": 45000,
3460	    "nve_onset_value": 1.5,
3461	    "nve_peak": 1.53,
3462	    "nve_peak_step": 105000,
3463	    "nve_sustained_45K_55K": true,
3464	    "total_steps": 112000,
3465	    "train_return_final_avg": 138,
3466	    "train_return_final_range": "82-214",
3467	    "value_mean_final": 268.4,
3468	    "vs_baseline_105K": "-70.8%"
3469	}
3470	
3471	  exp_id: exp_008e_v3_s3
3472	  status: DONE
3473	  description: 
3474	  tags: 
3475	  conclusion: negative
3476	  metrics: {
3477	    "actor_entropy_final": -4.892,
3478	    "collapse_onset": "85K-95K",
3479	    "eval_return": 92.7,
3480	    "gate_dt_1_frac": 1,
3481	    "gate_dt_mean": 1,
3482	    "nve_note": "Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02",
3483	    "nve_peak": 4.02,
3484	    "nve_peak_step": 105000,
3485	    "peak_eval": 520.4,
3486	    "peak_step": 85000,
3487	    "ve_ratio_105k": 2.635
3488	}
3489	
3490	  exp_id: exp_008e_v3_s4
3491	  status: DONE
3492	  description: 
3493	  tags: 
3494	  conclusion: success
3495	  metrics: {
3496	    "civo": false,
3497	    "eval_return": 899.3,
3498	    "nve_note": "Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K",
3499	    "nve_peak": 0.99,
3500	    "nve_peak_step": 95000,
3501	    "ve_ratio_105k": 0.609
3502	}
3503	
3504	  exp_id: exp_008e_v3_walker_s2
3505	  status: DONE
3506	  description: 
3507	  tags: 
3508	  conclusion: negative
3509	  metrics: {
3510	    "actor_entropy_collapse_signature": "entropy rose from -5.21@85K to -3.83@105K (policy destabilizing during collapse)",
3511	    "actor_entropy_trajectory": [
3512	        {
3513	            "actor_entropy": 8.239,
3514	            "step": 5000
3515	        },
3516	        {
3517	            "actor_entropy": 2.352,
3518	            "step": 15000
3519	        },
3520	        {
3521	            "actor_entropy": 0.17,
3522	            "step": 25000
3523	        },
3524	        {
3525	            "actor_entropy": -3.498,
3526	            "step": 35000
3527	        },
3528	        {
3529	            "actor_entropy": -4.915,
3530	            "step": 45000
3531	        },
3532	        {
3533	            "actor_entropy": -5.121,
3534	            "step": 55000
3535	        },
3536	        {
3537	            "actor_entropy": -5.135,
3538	            "step": 65000
3539	        },
3540	        {
3541	            "actor_entropy": -5.224,
3542	            "step": 75000
3543	        },
3544	        {
3545	            "actor_entropy": -5.208,
3546	            "step": 85000
3547	        },
3548	        {
3549	            "actor_entropy": -4.529,
3550	            "step": 95000
3551	        },
3552	        {
3553	            "actor_entropy": -3.828,
3554	            "step": 105000
3555	        }
3556	    ],
3557	    "baseline_105K": 915.67,
3558	    "collapse_confirmed": "105K (nve=3.78x, eval 715\u2192137)",
3559	    "collapse_onset": "95K (nve jumped from 0.68x to 1.34x)",
3560	    "eval_trajectory": [
3561	        {
3562	            "eval_return": 39.27,
3563	            "step": 5000
3564	        },
3565	        {
3566	            "eval_return": 180.85,
3567	            "step": 15000
3568	        },
3569	        {
3570	            "eval_return": 211.82,
3571	            "step": 25000
3572	        },
3573	        {
3574	            "eval_return": 320.39,
3575	            "step": 35000
3576	        },
3577	        {
3578	            "eval_return": 356.93,
3579	            "step": 45000
3580	        },
3581	        {
3582	            "eval_return": 418.32,
3583	            "step": 55000
3584	        },
3585	        {
3586	            "eval_return": 435.09,
3587	            "step": 65000
3588	        },
3589	        {
3590	            "eval_return": 576.54,
3591	            "step": 75000
3592	        },
3593	        {
3594	            "eval_return": 715.21,
3595	            "step": 85000
3596	        },
3597	        {
3598	            "eval_return": 452.43,
3599	            "step": 95000
3600	        },
3601	        {
3602	            "eval_return": 136.96,
3603	            "step": 105000
3604	        }
3605	    ],
3606	    "final_eval_return": 136.96,
3607	    "final_nve": 3.78,
3608	    "final_value_mean": 339.84,
3609	    "final_ve_ratio": 2.481,
3610	    "gate_dt_1_frac": 1,
3611	    "gate_dt_mean": 1,
3612	    "peak_eval_return": 715.21,
3613	    "peak_eval_step": 85000,
3614	    "train_return_108K": "19-23 (random policy level)",
3615	    "value_trajectory": [
3616	        {
3617	            "step": 5000,
3618	            "value_mean": 0
3619	        },
3620	        {
3621	            "step": 15000,
3622	            "value_mean": 3.91
3623	        },
3624	        {
3625	            "step": 25000,
3626	            "value_mean": 30.27
3627	        },
3628	        {
3629	            "step": 35000,
3630	            "value_mean": 79.75
3631	        },
3632	        {
3633	            "step": 45000,
3634	            "value_mean": 125.25
3635	        },
3636	        {
3637	            "step": 55000,
3638	            "value_mean": 172.89
3639	        },
3640	        {
3641	            "step": 65000,
3642	            "value_mean": 220.47
3643	        },
3644	        {
3645	            "step": 75000,
3646	            "value_mean": 272.64
3647	        },
3648	        {
3649	            "step": 85000,
3650	            "value_mean": 339.3
3651	        },
3652	        {
3653	            "step": 95000,
3654	            "value_mean": 384.39
3655	        },
3656	        {
3657	            "step": 105000,
3658	            "value_mean": 339.84
3659	        }
3660	    ],
3661	    "ve_ratio_trajectory": [
3662	        {
3663	            "nve": 1.64,
3664	            "step": 25000,
3665	            "ve": 0.143
3666	        },
3667	        {
3668	            "nve": 1.03,
3669	            "step": 35000,
3670	            "ve": 0.249
3671	        },
3672	        {
3673	            "nve": 1.06,
3674	            "step": 45000,
3675	            "ve": 0.351
3676	        },
3677	        {
3678	            "nve": 1.02,
3679	            "step": 55000,
3680	            "ve": 0.413
3681	        },
3682	        {
3683	            "nve": 0.9,
3684	            "step": 65000,
3685	            "ve": 0.507
3686	        },
3687	        {
3688	            "nve": 0.66,
3689	            "step": 75000,
3690	            "ve": 0.473
3691	        },
3692	        {
3693	            "nve": 0.68,
3694	            "step": 85000,
3695	            "ve": 0.474
3696	        },
3697	        {
3698	            "nve": 1.34,
3699	            "step": 95000,
3700	            "ve": 0.85
3701	        },
3702	        {
3703	            "nve": 3.78,
3704	            "step": 105000,
3705	            "ve": 2.481
3706	        }
3707	    ],
3708	    "vs_baseline_105K": "-85.0%"
3709	}
3710	
3711	  exp_id: exp_008f_s3_no_dt_embed_walker
3712	  status: DONE
3713	  description: 
3714	  tags: 
3715	  conclusion: success
3716	  metrics: {
3717	    "collapse": false,
3718	    "eval_return_final": 363.8,
3719	    "nve_peak": "< 1.5x"
3720	}
3721	
3722	  exp_id: exp_008f_s4
3723	  status: DONE
3724	  description: 
3725	  tags: 
3726	  conclusion: negative
3727	  metrics: {
3728	    "civo_alert": 0,
3729	    "eval_return_105k": 306.5,
3730	    "note": "No CIVO. No-dt-emb control seed=4. Peak NVE 1.41x @85K (transient), settles to 0.58x @105K.",
3731	    "nve_105k": 0.58,
3732	    "peak_eval": 487.5,
3733	    "peak_eval_step": 55000,
3734	    "peak_nve": 1.41,
3735	    "peak_nve_step": 85000
3736	}
3737	
3738	  exp_id: exp_009b_008d_walker_s2
3739	  status: DONE
3740	  description: 
3741	  tags: 
3742	  conclusion: negative
3743	  metrics: {
3744	    "baseline_105K": 915.67,
3745	    "causal_conclusion": "Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x\u21920.38x@105K, eval 141\u2192268) while seed 0 sustained nve>1.5x across 4 consecutive checkpoints and collapsed (eval 167\u219283). Collapse is stochastic (1/2 seeds); nve>1.5x threshold is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).",
3746	    "current_step": 105000,
3747	    "eval_checkpoints": [
3748	        {
3749	            "baseline_ve": null,
3750	            "eval_return": 39.27,
3751	            "normalized_ve": null,
3752	            "step": 5000,
3753	            "value_mean": 0,
3754	            "ve_ratio": 0
3755	        },
3756	        {
3757	            "baseline_ve": null,
3758	            "eval_return": 144.31,
3759	            "normalized_ve": null,
3760	            "step": 15000,
3761	            "value_mean": 4.47,
3762	            "ve_ratio": 0.031
3763	        },
3764	        {
3765	            "baseline_ve": 0.087,
3766	            "eval_return": 141.12,
3767	            "normalized_ve": 2.05,
3768	            "step": 25000,
3769	            "value_mean": 25.14,
3770	            "ve_ratio": 0.178
3771	        },
3772	        {
3773	            "baseline_ve": 0.241,
3774	            "eval_return": 164.14,
3775	            "normalized_ve": 1.24,
3776	            "step": 35000,
3777	            "value_mean": 49.02,
3778	            "ve_ratio": 0.299
3779	        },
3780	        {
3781	            "baseline_ve": 0.331,
3782	            "eval_return": 141.04,
3783	            "normalized_ve": 1.62,
3784	            "step": 45000,
3785	            "value_mean": 75.59,
3786	            "ve_ratio": 0.536
3787	        },
3788	        {
3789	            "baseline_ve": 0.404,
3790	            "eval_return": 172.33,
3791	            "normalized_ve": 1.41,
3792	            "step": 55000,
3793	            "value_mean": 98.28,
3794	            "ve_ratio": 0.57
3795	        },
3796	        {
3797	            "baseline_ve": 0.563,
3798	            "eval_return": 209.16,
3799	            "normalized_ve": 0.94,
3800	            "step": 65000,
3801	            "value_mean": 110.91,
3802	            "ve_ratio": 0.53
3803	        },
3804	        {
3805	            "baseline_ve": 0.719,
3806	            "eval_return": 197.46,
3807	            "normalized_ve": 0.66,
3808	            "step": 75000,
3809	            "value_mean": 93.49,
3810	            "ve_ratio": 0.474
3811	        },
3812	        {
3813	            "baseline_ve": 0.701,
3814	            "eval_return": 236.49,
3815	            "normalized_ve": 0.51,
3816	            "step": 85000,
3817	            "value_mean": 83.86,
3818	            "ve_ratio": 0.355
3819	        },
3820	        {
3821	            "baseline_ve": 0.632,
3822	            "eval_return": 278.54,
3823	            "normalized_ve": 0.43,
3824	            "step": 95000,
3825	            "value_mean": 75.72,
3826	            "ve_ratio": 0.272
3827	        },
3828	        {
3829	            "baseline_ve": 0.656,
3830	            "eval_return": 267.93,
3831	            "normalized_ve": 0.38,
3832	            "step": 105000,
3833	            "value_mean": 67.27,
3834	            "ve_ratio": 0.251
3835	        }
3836	    ],
3837	    "target_steps": 105000,
3838	    "trend": "Eval rising throughout: 39\u2192144\u2192141\u2192164\u2192141\u2192172\u2192209\u2192197\u2192236\u2192279\u2192268. Value peaks at 110.91@65K then self-corrects downward to 67.27@105K. v/e ratio peaks 0.57@55K then monotonically declines to 0.25@105K. NO delusional critic collapse \u2014 value self-corrects while eval improves.",
3839	    "verdict": "NEGATIVE \u2014 hypothesis was to replicate collapse, collapse NOT reproduced. However, pathological nve>1.5x episode confirmed (2.05x@25K, 1.62x@45K), consistent with trained dt_emb inducing pathological overestimation. Self-correction to 0.38x@105K distinguishes from seed 0's sustained overestimation \u2192 collapse.",
3840	    "vs_baseline_105K": "-70.8%"
3841	}
3842	
3843	  exp_id: exp_009c_s3
3844	  status: DONE
3845	  description: 
3846	  tags: 
3847	  conclusion: success
3848	  metrics: {
3849	    "current_step": 108000,
3850	    "eval_return_105k": 311.92,
3851	    "note": "eval peaked at 55-65K (~457) then declined to 311.92. NVE 0.52x (no CIVO). 009c seed=2 NVE 1.14x not reproduced.",
3852	    "nve_105k": 0.52,
3853	    "target_steps": 105000,
3854	    "value_mean_105k": 120.27,
3855	    "ve_ratio_105k": 0.386
3856	}
3857	
3858	  exp_id: exp_009e_008d_walker_s1
3859	  status: DONE
3860	  description: 
3861	  tags: 
3862	  conclusion: negative
3863	  metrics: {
3864	    "actor_loss_sign_flip": 85000,
3865	    "baseline_105K": 915.67,
3866	    "collapse_rate_note": "Independent rate = 1/2 (seed 1 collapsed, seed 2 self-corrected). 008d and 009e share seed=1, count as one independent observation.",
3867	    "current_step": 105000,
3868	    "eval_checkpoints": [
3869	        {
3870	            "eval_return": 31,
3871	            "step": 5000,
3872	            "value_mean": 0,
3873	            "ve_ratio": 0
3874	        },
3875	        {
3876	            "eval_return": 153.7,
3877	            "step": 15000,
3878	            "value_mean": 3.4,
3879	            "ve_ratio": 0.022
3880	        },
3881	        {
3882	            "baseline_ve": 0.087,
3883	            "eval_return": 167.2,
3884	            "normalized_ve": 1.78,
3885	            "step": 25000,
3886	            "value_mean": 25.9,
3887	            "ve_ratio": 0.155
3888	        },
3889	        {
3890	            "baseline_ve": 0.241,
3891	            "eval_return": 146.3,
3892	            "normalized_ve": 1.71,
3893	            "step": 35000,
3894	            "value_mean": 60.2,
3895	            "ve_ratio": 0.411
3896	        },
3897	        {
3898	            "baseline_ve": 0.331,
3899	            "eval_return": 140.8,
3900	            "normalized_ve": 2.09,
3901	            "step": 45000,
3902	            "value_mean": 97.5,
3903	            "ve_ratio": 0.693
3904	        },
3905	        {
3906	            "baseline_ve": 0.404,
3907	            "eval_return": 82.7,
3908	            "normalized_ve": 4.12,
3909	            "step": 55000,
3910	            "value_mean": 137.9,
3911	            "ve_ratio": 1.666
3912	        },
3913	        {
3914	            "baseline_ve": 0.563,
3915	            "eval_return": 250,
3916	            "normalized_ve": 1.23,
3917	            "step": 65000,
3918	            "value_mean": 173.8,
3919	            "ve_ratio": 0.695
3920	        },
3921	        {
3922	            "baseline_ve": 0.719,
3923	            "eval_return": 178.1,
3924	            "normalized_ve": 1.48,
3925	            "step": 75000,
3926	            "value_mean": 189.9,
3927	            "ve_ratio": 1.066
3928	        },
3929	        {
3930	            "baseline_ve": 0.701,
3931	            "eval_return": 201.93,
3932	            "normalized_ve": 1.15,
3933	            "step": 85000,
3934	            "value_mean": 163.08,
3935	            "ve_ratio": 0.808
3936	        },
3937	        {
3938	            "baseline_ve": 0.632,
3939	            "eval_return": 132.79,
3940	            "normalized_ve": 1.73,
3941	            "step": 95000,
3942	            "value_mean": 144.82,
3943	            "ve_ratio": 1.091
3944	        },
3945	        {
3946	            "baseline_ve": 0.656,
3947	            "eval_return": 131.08,
3948	            "normalized_ve": 1.57,
3949	            "step": 105000,
3950	            "value_mean": 135.37,
3951	            "ve_ratio": 1.033
3952	        }
3953	    ],
3954	    "final_eval_return": 131.08,
3955	    "final_nve": 1.57,
3956	    "final_value_mean": 135.37,
3957	    "final_ve_ratio": 1.033,
3958	    "peak_nve": 4.12,
3959	    "peak_nve_step": 55000,
3960	    "target_steps": 105000,
3961	    "vs_baseline_105K": "-85.7%"
3962	}
3963	
3964	  exp_id: exp_010b_cheetah_civo_trigger
3965	  status: DONE
3966	  description: 
3967	  tags: 
3968	  conclusion: success
3969	  metrics: {
3970	    "civo": true,
3971	    "eval_return_final": 51.7,
3972	    "eval_return_peak": 321.9,
3973	    "nve_peak": 8.27,
3974	    "nve_peak_step": 65000,
3975	    "peak_step": 35000
3976	}
3977	
3978	  exp_id: exp_010b_cheetah_civo_trigger_s0
3979	  status: DONE
3980	  description: 
3981	  tags: 
3982	  conclusion: success
3983	  metrics: {
3984	    "civo": true,
3985	    "civo_onset_step": "65K",
3986	    "detector_alert_step": "95K",
3987	    "eval_return_105K": 0.83,
3988	    "eval_return_peak": 247.77,
3989	    "eval_return_peak_step": "35K",
3990	    "gate_dt_mean": 2,
3991	    "gate_entropy": 0,
3992	    "nve_105K": 70.64,
3993	    "nve_95K": 6.34
3994	}
3995	
3996	  exp_id: exp_015b_frozen_dt_emb
3997	  status: DONE
3998	  description: 
3999	  tags: 
4000	  conclusion: negative
4001	  metrics: {
4002	    "actor_entropy_105K": -4.855,
4003	    "actor_loss_105K": 0.000179,
4004	    "collapse_mechanism": "gradient_starvation_from_frozen_dt_emb",
4005	    "data_source": "worker SSH final analysis 2026-05-15T18:30",
4006	    "eval_return_105K": 204.2,
4007	    "eval_return_15K": 167.9,
4008	    "eval_return_25K": 171.8,
4009	    "eval_return_35K": 201.6,
4010	    "eval_return_45K": 122.3,
4011	    "eval_return_55K": 105.8,
4012	    "eval_return_5K": 31,
4013	    "eval_return_65K": 160.3,
4014	    "eval_return_75K": 80,
4015	    "eval_return_85K": 183.5,
4016	    "eval_return_95K": 238.4,
4017	    "final_eval": 204.2,
4018	    "final_step": 112000,
4019	    "gate_dt_1_frac": 0,
4020	    "gate_dt_mean": 2,
4021	    "nve_105K": 0.42,
4022	    "nve_85K": 0.467,
4023	    "nve_95K": 0.394,
4024	    "summary": "NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss\u21920 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence",
4025	    "value_mean_105K": 56.212,
4026	    "value_std_105K": 13.818
4027	}
4028	
4029	  exp_id: exp_016e_sgs_walker_s1
4030	  status: DONE
4031	  description: 
4032	  tags: 
4033	  conclusion: negative
4034	  metrics: {
4035	    "actor_loss_sign_flip_step": 95000,
4036	    "civo_catastrophic_step": 95000,
4037	    "civo_detected": true,
4038	    "civo_nve_peak": 10.42,
4039	    "civo_nve_peak_step": 95000,
4040	    "civo_onset_step": 85000,
4041	    "civo_severity": "catastrophic",
4042	    "current_step": 100000,
4043	    "data_source": "metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25",
4044	    "deep_analysis": {
4045	        "016e_vs_008d_entropy_comparison": {
4046	            "15K": {
4047	                "008d": 0.481,
4048	                "016e": 1.049,
4049	                "delta": 0.568
4050	            },
4051	            "25K": {
4052	                "008d": -1.862,
4053	                "016e": -1.554,
4054	                "delta": 0.308
4055	            },
4056	            "35K": {
4057	                "008d": -3.465,
4058	                "016e": -2.118,
4059	                "delta": 1.347
4060	            },
4061	            "45K": {
4062	                "008d": -4.575,
4063	                "016e": -3.455,
4064	                "delta": 1.12
4065	            },
4066	            "55K": {
4067	                "008d": -4.879,
4068	                "016e": -3.617,
4069	                "delta": 1.262
4070	            },
4071	            "interpretation": "SGS preserves ~1.0-1.3 nats higher entropy through 35-55K, enabling better exploration"
4072	        },
4073	        "016e_vs_008d_value_at_crash": {
4074	            "008d": {
4075	                "disconnect_ratio": 1.67,
4076	                "eval_return": 82.75,
4077	                "value_mean": 137.88
4078	            },
4079	            "016e": {
4080	                "disconnect_ratio": 6.58,
4081	                "eval_return": 31.73,
4082	                "value_mean": 208.88
4083	            },
4084	            "interpretation": "016e value completely decoupled from reality; 008d still weakly correlated"
4085	        },
4086	        "actor_loss_sign_flip": {
4087	            "008d_min_actor_loss": -0.073,
4088	            "008d_never_flipped": true,
4089	            "016e_flip_step": 95000,
4090	            "016e_flip_value": 0.014,
4091	            "interpretation": "sign flip = value critic drives actor toward worse actions, triggering catastrophic collapse"
4092	        },
4093	        "train_return_collapse_timeline": {
4094	            "100K": [
4095	                109,
4096	                111,
4097	                102,
4098	                108
4099	            ],
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "4785e63d-d608-43d5-bc8d-7d00ea80994e"
}
```

</details>

---


### System

_source line 122_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 76587,
    "tool_uses": 10,
    "duration_ms": 57930
  },
  "last_tool_name": "Read",
  "uuid": "ac8fd744-e899-441e-826b-e83f2ab65d0f",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 123_

<details open><summary>🔧 Tool call — Read · `toolu_01Mbogx7t9NeC7k2Bb17Uoj6`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "offset": 4100,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "36061168-7981-4df0-98aa-5c1814d0914f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017FDQWyR9w2CgUdeQtzNpxa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9361,
      "cache_read_input_tokens": 66883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9361,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 124 · 2026-05-24T02:15:27.069Z_

<details><summary>↩ Tool result · `toolu_01Mbogx7t9NeC7k2Bb17Uoj6`</summary>

```text
4100	            "88K": [
4101	                140,
4102	                145,
4103	                116,
4104	                116
4105	            ],
4106	            "92K": [
4107	                50,
4108	                29,
4109	                34,
4110	                75
4111	            ],
4112	            "96K": [
4113	                86,
4114	                41,
4115	                50,
4116	                101
4117	            ],
4118	            "interpretation": "collapse visible in train_return by 92K; partial recovery by 100K but far below peak"
4119	        }
4120	    },
4121	    "eval_checkpoints": [
4122	        {
4123	            "eval_return": 31,
4124	            "step": 5000,
4125	            "value_mean": 0.001,
4126	            "ve_ratio": 4e-05
4127	        },
4128	        {
4129	            "eval_return": 140.3,
4130	            "step": 15000,
4131	            "value_mean": 3.1,
4132	            "ve_ratio": 0.022
4133	        },
4134	        {
4135	            "baseline_ve": 0.087,
4136	            "eval_return": 141.75,
4137	            "nve": 1.86,
4138	            "step": 25000,
4139	            "value_mean": 22.97,
4140	            "ve_ratio": 0.162
4141	        },
4142	        {
4143	            "baseline_ve": 0.241,
4144	            "eval_return": 173.01,
4145	            "nve": 1.28,
4146	            "step": 35000,
4147	            "value_mean": 53.55,
4148	            "ve_ratio": 0.309
4149	        },
4150	        {
4151	            "baseline_ve": 0.331,
4152	            "eval_return": 184.03,
4153	            "nve": 1.4,
4154	            "step": 45000,
4155	            "value_mean": 85.32,
4156	            "ve_ratio": 0.464
4157	        },
4158	        {
4159	            "baseline_ve": 0.404,
4160	            "eval_return": 153.79,
4161	            "nve": 1.86,
4162	            "step": 55000,
4163	            "value_mean": 115.63,
4164	            "ve_ratio": 0.752
4165	        },
4166	        {
4167	            "baseline_ve": 0.563,
4168	            "eval_return": 324.3,
4169	            "nve": 0.83,
4170	            "step": 65000,
4171	            "value_mean": 152.3,
4172	            "ve_ratio": 0.469
4173	        },
4174	        {
4175	            "baseline_ve": 0.719,
4176	            "eval_return": 326.67,
4177	            "nve": 0.81,
4178	            "step": 75000,
4179	            "value_mean": 190.04,
4180	            "ve_ratio": 0.582
4181	        },
4182	        {
4183	            "baseline_ve": 0.701,
4184	            "eval_return": 256.21,
4185	            "nve": 1.2,
4186	            "step": 85000,
4187	            "value_mean": 215.39,
4188	            "ve_ratio": 0.841
4189	        },
4190	        {
4191	            "baseline_ve": 0.632,
4192	            "eval_return": 31.73,
4193	            "nve": 10.42,
4194	            "step": 95000,
4195	            "value_mean": 208.88,
4196	            "ve_ratio": 6.583
4197	        }
4198	    ],
4199	    "final_eval_return": 31.73,
4200	    "final_eval_step": 95000,
4201	    "gate_dt_2_frac": 1,
4202	    "gate_dt_mean": 2,
4203	    "peak_eval_return": 326.67,
4204	    "peak_eval_step": 75000,
4205	    "reward_dt_emb_detach": true,
4206	    "sgs_verdict": "SGS delays CIVO onset ~50K steps by preserving entropy, yields 2x higher peak (327 vs 167), but does NOT prevent collapse. Collapse is more severe (NVE 10.42x vs 4.12x) due to accumulated value overestimation. Root cause is value dynamics, not reward-head gradient contamination.",
4207	    "target_steps": 105000
4208	}
4209	
4210	  exp_id: exp_018_full_sgs_walker_s1
4211	  status: DONE
4212	  description: 
4213	  tags: 
4214	  conclusion: killed
4215	  metrics: {
4216	    "eval_return_final": 915.7,
4217	    "eval_return_final_step": 105000,
4218	    "eval_return_peak": 915.7,
4219	    "eval_return_peak_step": 105000,
4220	    "nve_peak": 0.72,
4221	    "nve_peak_step": 75000,
4222	    "nve_sustained_avg": 0.55,
4223	    "nve_sustained_max": 0.72,
4224	    "total_steps": 112000,
4225	    "train_return_final_avg": 899.4,
4226	    "value_mean_final": 601.1
4227	}
4228	
4229	  exp_id: exp_018v2_full_sgs_walker_s1
4230	  status: DONE
4231	  description: 
4232	  tags: 
4233	  conclusion: negative
4234	  metrics: {
4235	    "civo_reduction_pct": 79,
4236	    "eval_return_final": 448.3,
4237	    "eval_return_final_step": 105000,
4238	    "eval_return_peak": 499.6,
4239	    "eval_return_peak_step": 75000,
4240	    "gate_dt_2_frac": 1,
4241	    "gate_dt_mean": 2,
4242	    "late_collapse_detected": true,
4243	    "late_collapse_step": 112000,
4244	    "nve_final": 1.34,
4245	    "nve_mean_45k_105k": 1.23,
4246	    "nve_peak": 1.66,
4247	    "nve_peak_step": 95000,
4248	    "total_steps": 112000,
4249	    "total_updates": 25099,
4250	    "value_loss_final": 0.6
4251	}
4252	
4253	  exp_id: exp_019b_pickcube_civo_trigger
4254	  status: DONE
4255	  description: 
4256	  tags: 
4257	  conclusion: success
4258	  metrics: {
4259	    "baseline_eval_final": 58.56,
4260	    "baseline_ratio": 0.455,
4261	    "eval_return_final": 26.64,
4262	    "eval_return_peak": 26.9,
4263	    "eval_return_peak_step": 132500,
4264	    "gate_dt_2_frac": 1,
4265	    "gate_entropy": 0,
4266	    "nve_final": 0.065,
4267	    "nve_peak": 3.78,
4268	    "nve_peak_step": 52500,
4269	    "pattern": "transient_civo_then_value_collapse",
4270	    "total_steps": 200000,
4271	    "value_baseline_final": 144.57,
4272	    "value_mean_final": 4.26
4273	}
4274	
4275	  exp_id: exp_020_vanilla_dreamerv3_s2
4276	  status: DONE
4277	  description: 
4278	  tags: 
4279	  conclusion: success
4280	  metrics: {
4281	    "collapse": false,
4282	    "comparison_with_parent": {
4283	        "c6_confirmed": true,
4284	        "delta": "vanilla stable (836.5) vs trained dt_emb collapsed (136.96)",
4285	        "parent_collapsed": true,
4286	        "parent_eval_105K": 136.96,
4287	        "parent_id": "exp_008e_v3_walker_s2",
4288	        "parent_nve_105K": 3.78
4289	    },
4290	    "eval_trajectory": [
4291	        {
4292	            "eval_return": 41.2,
4293	            "step": 5000
4294	        },
4295	        {
4296	            "eval_return": 534.1,
4297	            "step": 55000
4298	        },
4299	        {
4300	            "eval_return": 688.9,
4301	            "step": 65000
4302	        },
4303	        {
4304	            "eval_return": 596.2,
4305	            "step": 95000
4306	        },
4307	        {
4308	            "eval_return": 836.5,
4309	            "step": 105000
4310	        }
4311	    ],
4312	    "final_eval_return": 836.5,
4313	    "final_value_mean": 539.3,
4314	    "peak_eval_return": 836.5,
4315	    "peak_eval_step": 105000,
4316	    "train_return_range_108K": "511-808",
4317	    "ve_ratio_105K": 0.645
4318	}
4319	
4320	  exp_id: exp_021_full_sgs_cheetah_s1
4321	  status: DONE
4322	  description: 
4323	  tags: 
4324	  conclusion: negative
4325	  metrics: {
4326	    "baseline_pct": 38.7,
4327	    "civo": true,
4328	    "civo_type": "transient_self_correcting",
4329	    "eval_return_final": 221.5,
4330	    "nve_peak": 9.94,
4331	    "nve_peak_step": "45K",
4332	    "nve_sustained_55K_105K": 0.338,
4333	    "vs_010b": "221.5 vs 51.7 (4.3x better)"
4334	}
4335	
4336	  exp_id: exp_022b_no_curriculum
4337	  status: DONE
4338	  description: 
4339	  tags: 
4340	  conclusion: success
4341	  metrics: {
4342	    "civo_alert_max": 0,
4343	    "eval_return_105K": 300.7,
4344	    "gate_dt_1_frac_105K": 0.145,
4345	    "gate_dt_mean_105K": 3.41,
4346	    "gate_entropy_ratio_105K": 0.912,
4347	    "gate_near_uniform": true,
4348	    "nve_peak": 1.22,
4349	    "ve_ratio_105K": 0.075,
4350	    "ve_ratio_peak": 0.218
4351	}
4352	
4353	  exp_id: exp_023_cheetah_baseline_s2
4354	  status: DONE
4355	  description: 
4356	  tags: 
4357	  conclusion: success
4358	  metrics: {
4359	    "current_step": 205000,
4360	    "eval_return_final": 645.4,
4361	    "note": "Cheetah Run baseline seed=2. Third baseline seed for NVE normalization.",
4362	    "target_steps": 200000
4363	}
4364	
4365	  exp_id: exp_024b_cheetah_no_dt_emb_s0
4366	  status: DONE
4367	  description: 
4368	  tags: 
4369	  conclusion: success
4370	  metrics: {
4371	    "civo": false,
4372	    "eval_return_final": 96.5,
4373	    "nve_peak": 0.2
4374	}
4375	
4376	  exp_id: exp_024b_cheetah_no_dt_emb_s1
4377	  status: DONE
4378	  description: 
4379	  tags: 
4380	  conclusion: success
4381	  metrics: {
4382	    "baseline_pct": 14.1,
4383	    "civo": false,
4384	    "eval_return_final": 77.3,
4385	    "eval_return_peak": 129.6,
4386	    "gate_dt_2_frac": 1,
4387	    "nve_peak": 0.1,
4388	    "peak_step": 15000
4389	}
4390	
4391	  exp_id: exp_027_tcn_walker_s0
4392	  status: DONE
4393	  description: 
4394	  tags: 
4395	  conclusion: negative
4396	  metrics: {
4397	    "eval_return_105K": 95.5,
4398	    "eval_return_112K": 99.5,
4399	    "eval_return_15K": 154.6,
4400	    "eval_return_25K": 223.6,
4401	    "eval_return_35K": 240,
4402	    "eval_return_45K": 101.2,
4403	    "eval_return_55K": 70,
4404	    "eval_return_5K": 37.4,
4405	    "eval_return_65K": 95.1,
4406	    "eval_return_75K": 189.2,
4407	    "eval_return_85K": 36,
4408	    "eval_return_95K": 166.4,
4409	    "final_step": 120000,
4410	    "gate_dt_entropy": 0,
4411	    "gate_dt_mean": 2,
4412	    "last_5_eval_avg": 117.3,
4413	    "nve_breach_count": 3,
4414	    "nve_breach_steps": "55K(1.68), 65K(1.54), 85K(3.97)",
4415	    "peak_eval": 240,
4416	    "peak_eval_step": "35K",
4417	    "peak_nve": 3.965,
4418	    "peak_nve_step": "85K",
4419	    "target_steps": 210000,
4420	    "ve_ratio_105K": 0.916,
4421	    "ve_ratio_15K": 0.02,
4422	    "ve_ratio_25K": 0.11,
4423	    "ve_ratio_35K": 0.235,
4424	    "ve_ratio_45K": 0.86,
4425	    "ve_ratio_55K": 1.679,
4426	    "ve_ratio_65K": 1.544,
4427	    "ve_ratio_75K": 0.831,
4428	    "ve_ratio_85K": 3.965,
4429	    "ve_ratio_95K": 0.675
4430	}
4431	
4432	  exp_id: exp_027_tcn_walker_s0_sigma02
4433	  status: DONE
4434	  description: 
4435	  tags: 
4436	  conclusion: success
4437	  metrics: {
4438	    "eval_last10_mean": 587.1,
4439	    "eval_peak": 821.1,
4440	    "eval_peak_step": "175K",
4441	    "eval_return_105K": 236.4,
4442	    "eval_return_115K": 543.8,
4443	    "eval_return_125K": 458.4,
4444	    "eval_return_135K": 496.7,
4445	    "eval_return_145K": 542.7,
4446	    "eval_return_155K": 660.5,
4447	    "eval_return_15K": 150.6,
4448	    "eval_return_165K": 653.3,
4449	    "eval_return_175K": 821.1,
4450	    "eval_return_185K": 560.5,
4451	    "eval_return_195K": 567.9,
4452	    "eval_return_205K": 558.7,
4453	    "eval_return_215K": 551,
4454	    "eval_return_25K": 199.4,
4455	    "eval_return_35K": 278.2,
4456	    "eval_return_45K": 315.6,
4457	    "eval_return_55K": 278.6,
4458	    "eval_return_5K": 35.6,
4459	    "eval_return_65K": 331,
4460	    "eval_return_75K": 293.1,
4461	    "eval_return_85K": 363.9,
4462	    "eval_return_95K": 171.4,
4463	    "nve_final": 0.0955,
4464	    "nve_max": 0.9081,
4465	    "nve_max_step": "95K",
4466	    "total_steps": 215000,
4467	    "ve_ratio_105K": 0.5625,
4468	    "ve_ratio_115K": 0.2105,
4469	    "ve_ratio_125K": 0.2182,
4470	    "ve_ratio_135K": 0.1764,
4471	    "ve_ratio_145K": 0.143,
4472	    "ve_ratio_155K": 0.106,
4473	    "ve_ratio_15K": 0.0192,
4474	    "ve_ratio_165K": 0.0979,
4475	    "ve_ratio_175K": 0.0729,
4476	    "ve_ratio_185K": 0.1048,
4477	    "ve_ratio_195K": 0.1026,
4478	    "ve_ratio_205K": 0.0995,
4479	    "ve_ratio_215K": 0.0955,
4480	    "ve_ratio_25K": 0.0961,
4481	    "ve_ratio_35K": 0.1875,
4482	    "ve_ratio_45K": 0.3009,
4483	    "ve_ratio_55K": 0.5231,
4484	    "ve_ratio_65K": 0.5654,
4485	    "ve_ratio_75K": 0.611,
4486	    "ve_ratio_85K": 0.4665,
4487	    "ve_ratio_95K": 0.9081
4488	}
4489	
4490	  exp_id: exp_027_tcn_walker_s1
4491	  status: DONE
4492	  description: 
4493	  tags: 
4494	  conclusion: negative
4495	  metrics: {
4496	    "eval_last10_mean": 233.1,
4497	    "eval_peak": 364.9,
4498	    "eval_peak_step": 75000,
4499	    "eval_return": {
4500	        "105000": 216.7,
4501	        "115000": 318.9,
4502	        "125000": 309.1,
4503	        "135000": 216.1,
4504	        "145000": 175.4,
4505	        "15000": 140.5,
4506	        "155000": 171,
4507	        "165000": 209.5,
4508	        "175000": 120.4,
4509	        "185000": 355.4,
4510	        "195000": 183.3,
4511	        "205000": 240.2,
4512	        "215000": 350.8,
4513	        "25000": 163.6,
4514	        "35000": 153,
4515	        "45000": 136.8,
4516	        "5000": 31,
4517	        "55000": 158.3,
4518	        "65000": 298.5,
4519	        "75000": 364.9,
4520	        "85000": 134,
4521	        "95000": 94.6
4522	    },
4523	    "nve_final": 0.1476,
4524	    "nve_max": 1.6367,
4525	    "nve_max_step": 95000,
4526	    "total_steps": 215000,
4527	    "ve_ratio": {
4528	        "105000": 0.6444,
4529	        "115000": 0.4021,
4530	        "125000": 0.38,
4531	        "135000": 0.5078,
4532	        "145000": 0.8469,
4533	        "15000": 0.0246,
4534	        "155000": 0.8568,
4535	        "165000": 0.5393,
4536	        "175000": 0.7355,
4537	        "185000": 0.211,
4538	        "195000": 0.3513,
4539	        "205000": 0.2376,
4540	        "215000": 0.1476,
4541	        "25000": 0.1416,
4542	        "35000": 0.3585,
4543	        "45000": 0.6101,
4544	        "55000": 0.7092,
4545	        "65000": 0.4875,
4546	        "75000": 0.4902,
4547	        "85000": 1.4104,
4548	        "95000": 1.6367
4549	    }
4550	}
4551	
4552	  exp_id: exp_028_rave_walker_s0
4553	  status: DONE
4554	  description: 
4555	  tags: 
4556	  conclusion: negative
4557	  metrics: {
4558	    "current_steps": 105000,
4559	    "eval_trajectory": {
4560	        "105K": {
4561	            "eval_return": 29,
4562	            "value_mean": 92.2,
4563	            "ve_ratio": 3.183
4564	        },
4565	        "15K": {
4566	            "eval_return": 105.3,
4567	            "value_mean": 2.93,
4568	            "ve_ratio": 0.028
4569	        },
4570	        "25K": {
4571	            "eval_return": 191.9,
4572	            "value_mean": 24.4,
4573	            "ve_ratio": 0.127
4574	        },
4575	        "35K": {
4576	            "eval_return": 204.6,
4577	            "ve_ratio": 0.267
4578	        },
4579	        "45K": {
4580	            "eval_return": 197.7,
4581	            "ve_ratio": 0.439
4582	        },
4583	        "55K": {
4584	            "eval_return": 193,
4585	            "ve_ratio": 0.62
4586	        },
4587	        "5K": {
4588	            "eval_return": 37.4,
4589	            "value_mean": 0.001
4590	        },
4591	        "65K": {
4592	            "eval_return": 79.8,
4593	            "ve_ratio": 1.832
4594	        },
4595	        "75K": {
4596	            "eval_return": 44.5,
4597	            "ve_ratio": 3.415
4598	        },
4599	        "85K": {
4600	            "eval_return": 57.7,
4601	            "ve_ratio": 2.126
4602	        },
4603	        "95K": {
4604	            "eval_return": 25.9,
4605	            "value_mean": 105.87,
4606	            "ve_ratio": 4.086
4607	        }
4608	    },
4609	    "note": "NEGATIVE. NVE diverged from 55K onward (0.62\u21924.09), eval collapsed 193\u219229. No self-correction."
4610	}
4611	
4612	  exp_id: exp_029a_tcn_walker_s1_sigma02
4613	  status: DONE
4614	  description: 
4615	  tags: 
4616	  conclusion: success
4617	  metrics: {
4618	    "current_step": 215000,
4619	    "eval_last10_mean": 282.15,
4620	    "eval_peak": 401,
4621	    "eval_peak_step": "125K",
4622	    "eval_return_105K": 319.4,
4623	    "eval_return_115K": 345.5,
4624	    "eval_return_125K": 401,
4625	    "eval_return_135K": 307.8,
4626	    "eval_return_145K": 380.8,
4627	    "eval_return_155K": 307.3,
4628	    "eval_return_15K": 137.7,
4629	    "eval_return_165K": 320.3,
4630	    "eval_return_175K": 159,
4631	    "eval_return_185K": 278.2,
4632	    "eval_return_195K": 301.2,
4633	    "eval_return_205K": 204.6,
4634	    "eval_return_215K": 161.3,
4635	    "eval_return_25K": 180.9,
4636	    "eval_return_35K": 124,
4637	    "eval_return_45K": 124.2,
4638	    "eval_return_55K": 133.9,
4639	    "eval_return_5K": 36.7,
4640	    "eval_return_65K": 169.7,
4641	    "eval_return_75K": 171.2,
4642	    "eval_return_85K": 151.8,
4643	    "eval_return_95K": 180.3,
4644	    "nve_final": 0.1864,
4645	    "nve_max": 0.6428,
4646	    "nve_max_step": "55K",
4647	    "target_steps": 210000,
4648	    "ve_ratio_105K": 0.1554,
4649	    "ve_ratio_115K": 0.1348,
4650	    "ve_ratio_125K": 0.116,
4651	    "ve_ratio_135K": 0.1449,
4652	    "ve_ratio_145K": 0.1088,
4653	    "ve_ratio_155K": 0.1287,
4654	    "ve_ratio_15K": 0.0248,
4655	    "ve_ratio_165K": 0.1142,
4656	    "ve_ratio_175K": 0.2138,
4657	    "ve_ratio_185K": 0.121,
4658	    "ve_ratio_195K": 0.1075,
4659	    "ve_ratio_205K": 0.1503,
4660	    "ve_ratio_215K": 0.1864,
4661	    "ve_ratio_25K": 0.1165,
4662	    "ve_ratio_35K": 0.3574,
4663	    "ve_ratio_45K": 0.5147,
4664	    "ve_ratio_55K": 0.6428,
4665	    "ve_ratio_65K": 0.4777,
4666	    "ve_ratio_75K": 0.398,
4667	    "ve_ratio_85K": 0.4033,
4668	    "ve_ratio_95K": 0.3007
4669	}
4670	
4671	  exp_id: exp_029b_tcn_walker_s2_sigma02
4672	  status: DONE
4673	  description: 
4674	  tags: 
4675	  conclusion: negative
4676	  metrics: {
4677	    "civo_onset_step": 65000,
4678	    "eval_last_step": 165000,
4679	    "eval_peak": 177.67,
4680	    "eval_peak_step": 55000,
4681	    "eval_return_105K": 31.97,
4682	    "eval_return_115K": 35.45,
4683	    "eval_return_125K": 33.04,
4684	    "eval_return_135K": 42.47,
4685	    "eval_return_145K": 51.66,
4686	    "eval_return_155K": 56.5,
4687	    "eval_return_15K": 168.41,
4688	    "eval_return_165K": 44.9,
4689	    "eval_return_25K": 159.56,
4690	    "eval_return_35K": 168.05,
4691	    "eval_return_45K": 171.51,
4692	    "eval_return_55K": 177.67,
4693	    "eval_return_5K": 30.46,
4694	    "eval_return_65K": 106.57,
4695	    "eval_return_75K": 64.01,
4696	    "eval_return_85K": 62.82,
4697	    "eval_return_95K": 44.66,
4698	    "gate_dt2_frac": 1.0,
4699	    "gate_entropy": 0.0,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "7ad663da-a522-4fee-a406-00d5684bd5c5"
}
```

</details>

---


### System

_source line 125_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 85033,
    "tool_uses": 11,
    "duration_ms": 64339
  },
  "last_tool_name": "Read",
  "uuid": "5f57e3cb-5129-4085-9d5b-6dbaddca652b",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 126_

<details open><summary>🔧 Tool call — Read · `toolu_01RL2LVifjoCAeKyJbUmoy1K`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "offset": 4700,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "53ecf1f1-a256-4c85-9aad-a33cdfd47070",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01U3DNtCtKxeVnnZ77mV8SLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8444,
      "cache_read_input_tokens": 76244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8444,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 127 · 2026-05-24T02:15:33.476Z_

<details><summary>↩ Tool result · `toolu_01RL2LVifjoCAeKyJbUmoy1K`</summary>

```text
4700	    "late_stage_nve_decline": "value adaptation (value_mean 108\u219255), not recovery (eval stayed 32-57)",
4701	    "nve_peak": 2.765,
4702	    "nve_peak_step": 105000,
4703	    "step": 168000,
4704	    "value_mean_105K": 88.38,
4705	    "value_mean_165K": 55.03,
4706	    "value_mean_55K": 103.62,
4707	    "ve_ratio_105K": 2.765,
4708	    "ve_ratio_115K": 2.326,
4709	    "ve_ratio_125K": 2.278,
4710	    "ve_ratio_135K": 1.648,
4711	    "ve_ratio_145K": 1.234,
4712	    "ve_ratio_155K": 1.061,
4713	    "ve_ratio_15K": 0.03,
4714	    "ve_ratio_165K": 1.226,
4715	    "ve_ratio_25K": 0.174,
4716	    "ve_ratio_35K": 0.335,
4717	    "ve_ratio_45K": 0.477,
4718	    "ve_ratio_55K": 0.583,
4719	    "ve_ratio_65K": 1.014,
4720	    "ve_ratio_75K": 1.65,
4721	    "ve_ratio_85K": 1.623,
4722	    "ve_ratio_95K": 2.109
4723	}
4724	
4725	  exp_id: exp_029c_tcn_walker_s0_sigma01
4726	  status: DONE
4727	  description: 
4728	  tags: 
4729	  conclusion: negative
4730	  metrics: {
4731	    "eval_final": 328.3,
4732	    "eval_peak": 490.7,
4733	    "eval_peak_step": "165K",
4734	    "eval_return_105K": 204.7,
4735	    "eval_return_115K": 296.4,
4736	    "eval_return_125K": 232.3,
4737	    "eval_return_135K": 247.4,
4738	    "eval_return_145K": 323.1,
4739	    "eval_return_155K": 359.7,
4740	    "eval_return_15K": 99.1,
4741	    "eval_return_165K": 490.7,
4742	    "eval_return_175K": 246.2,
4743	    "eval_return_185K": 220.6,
4744	    "eval_return_195K": 212.8,
4745	    "eval_return_205K": 256.9,
4746	    "eval_return_215K": 328.3,
4747	    "eval_return_25K": 140.7,
4748	    "eval_return_35K": 155.7,
4749	    "eval_return_45K": 160.9,
4750	    "eval_return_55K": 254.8,
4751	    "eval_return_5K": 35.6,
4752	    "eval_return_65K": 268.7,
4753	    "eval_return_75K": 295.5,
4754	    "eval_return_85K": 220.8,
4755	    "eval_return_95K": 188.6,
4756	    "nve_final": 0.1,
4757	    "nve_max": 1.0218,
4758	    "nve_max_step": "95K",
4759	    "total_steps": 224000,
4760	    "ve_ratio_105K": 0.761,
4761	    "ve_ratio_115K": 0.4514,
4762	    "ve_ratio_125K": 0.4899,
4763	    "ve_ratio_135K": 0.3995,
4764	    "ve_ratio_145K": 0.2667,
4765	    "ve_ratio_155K": 0.2,
4766	    "ve_ratio_15K": 0.0306,
4767	    "ve_ratio_165K": 0.1,
4768	    "ve_ratio_175K": 0.3,
4769	    "ve_ratio_185K": 0.3,
4770	    "ve_ratio_195K": 0.3,
4771	    "ve_ratio_205K": 0.2,
4772	    "ve_ratio_215K": 0.1,
4773	    "ve_ratio_25K": 0.1606,
4774	    "ve_ratio_35K": 0.3162,
4775	    "ve_ratio_45K": 0.4807,
4776	    "ve_ratio_55K": 0.4368,
4777	    "ve_ratio_65K": 0.5432,
4778	    "ve_ratio_75K": 0.6211,
4779	    "ve_ratio_85K": 0.9533,
4780	    "ve_ratio_95K": 1.0218
4781	}
4782	
4783	  exp_id: exp_029d_tcn_walker_s3_sigma02
4784	  status: DONE
4785	  description: 
4786	  tags: 
4787	  conclusion: negative
4788	  metrics: {
4789	    "civo_onset_step": 105000,
4790	    "civo_pattern": "sudden blowup (healthy 0.67@95K \u2192 3.0@105K)",
4791	    "eval_final": 104.5,
4792	    "eval_last_step": 215000,
4793	    "eval_peak": 349.6,
4794	    "eval_peak_step": 95000,
4795	    "eval_return_105K": 71.8,
4796	    "eval_return_115K": 69.8,
4797	    "eval_return_125K": 61.5,
4798	    "eval_return_135K": 141.8,
4799	    "eval_return_145K": 98.66,
4800	    "eval_return_155K": 88.86,
4801	    "eval_return_15K": 159.1,
4802	    "eval_return_165K": 86.22,
4803	    "eval_return_175K": 123.53,
4804	    "eval_return_185K": 153.71,
4805	    "eval_return_195K": 68.84,
4806	    "eval_return_205K": 63.71,
4807	    "eval_return_215K": 104.5,
4808	    "eval_return_25K": 155.7,
4809	    "eval_return_35K": 190.8,
4810	    "eval_return_45K": 137.1,
4811	    "eval_return_55K": 210.7,
4812	    "eval_return_5K": 31.7,
4813	    "eval_return_65K": 189.5,
4814	    "eval_return_75K": 253.2,
4815	    "eval_return_85K": 259.5,
4816	    "eval_return_95K": 349.6,
4817	    "gate_dt2_frac": 1.0,
4818	    "gate_entropy": 0.0,
4819	    "nve_peak": 3.0,
4820	    "nve_peak_step": 105000,
4821	    "step": 224000,
4822	    "value_mean_105K": 218.37,
4823	    "value_mean_215K": 42.55,
4824	    "value_mean_95K": 232.74,
4825	    "ve_ratio_105K": 3.0,
4826	    "ve_ratio_115K": 2.5,
4827	    "ve_ratio_125K": 2.4,
4828	    "ve_ratio_135K": 0.9,
4829	    "ve_ratio_145K": 1.141,
4830	    "ve_ratio_155K": 1.06,
4831	    "ve_ratio_165K": 0.91,
4832	    "ve_ratio_175K": 0.556,
4833	    "ve_ratio_185K": 0.396,
4834	    "ve_ratio_195K": 0.78,
4835	    "ve_ratio_205K": 0.747,
4836	    "ve_ratio_215K": 0.4,
4837	    "ve_ratio_45K": 0.695,
4838	    "ve_ratio_55K": 0.598,
4839	    "ve_ratio_65K": 0.863,
4840	    "ve_ratio_75K": 0.791,
4841	    "ve_ratio_85K": 0.9,
4842	    "ve_ratio_95K": 0.7
4843	}
4844	
4845	  exp_id: exp_030a_tcn_cheetah_s0_sigma02
4846	  status: DONE
4847	  description: 
4848	  tags: 
4849	  conclusion: negative
4850	  metrics: {
4851	    "current_step": 64000,
4852	    "eval_return_35K": 299.5,
4853	    "eval_return_55K": 31.9,
4854	    "note": "WARNING: NVE breached 1.5\u00d7 at 55K (1.903), eval crashed 299\u219232. Possible CIVO despite TCN.",
4855	    "target_steps": 210000,
4856	    "ve_ratio_55K": 1.903
4857	}
4858	
4859	  exp_id: exp_030b_tcn_cheetah_s0_sigma05
4860	  status: DONE
4861	  description: 
4862	  tags: 
4863	  conclusion: negative
4864	  metrics: {
4865	    "current_step": 195000,
4866	    "eval_return_105K": 104.4,
4867	    "eval_return_115K": 137.7,
4868	    "eval_return_125K": 211.7,
4869	    "eval_return_135K": 97.2,
4870	    "eval_return_145K": 79.4,
4871	    "eval_return_155K": 76.8,
4872	    "eval_return_15K": 78.3,
4873	    "eval_return_165K": 77.5,
4874	    "eval_return_175K": 85.7,
4875	    "eval_return_185K": 68.7,
4876	    "eval_return_195K": 77.6,
4877	    "eval_return_25K": 219.3,
4878	    "eval_return_35K": 296.5,
4879	    "eval_return_45K": 32.8,
4880	    "eval_return_55K": 6,
4881	    "eval_return_5K": 8.3,
4882	    "eval_return_65K": 71.2,
4883	    "eval_return_75K": 23.3,
4884	    "eval_return_85K": 34,
4885	    "eval_return_95K": 143.6,
4886	    "nve_final": 0.1534,
4887	    "nve_max": 10.6657,
4888	    "nve_max_step": "55K",
4889	    "target_steps": 210000,
4890	    "ve_ratio_105K": 0.2686,
4891	    "ve_ratio_115K": 0.1789,
4892	    "ve_ratio_125K": 0.1037,
4893	    "ve_ratio_135K": 0.2153,
4894	    "ve_ratio_145K": 0.2478,
4895	    "ve_ratio_155K": 0.2392,
4896	    "ve_ratio_15K": 0.0202,
4897	    "ve_ratio_165K": 0.202,
4898	    "ve_ratio_175K": 0.1591,
4899	    "ve_ratio_185K": 0.1834,
4900	    "ve_ratio_195K": 0.1534,
4901	    "ve_ratio_25K": 0.0636,
4902	    "ve_ratio_35K": 0.1238,
4903	    "ve_ratio_45K": 1.9141,
4904	    "ve_ratio_55K": 10.6657,
4905	    "ve_ratio_65K": 0.8371,
4906	    "ve_ratio_75K": 1.9823,
4907	    "ve_ratio_85K": 1.0946,
4908	    "ve_ratio_95K": 0.2253
4909	}
4910	
4911	  exp_id: exp_031b_tcn_pickcube_s0_sigma05
4912	  status: DONE
4913	  description: 
4914	  tags: 
4915	  conclusion: negative
4916	  metrics: {
4917	    "eval_reward_final": 25.5,
4918	    "eval_reward_last5_avg": 25.9,
4919	    "eval_reward_peak": 29.1,
4920	    "nve_final": 0.2,
4921	    "nve_peak": 3.3,
4922	    "nve_peak_step": 42500,
4923	    "nve_suppressed_from_step": 72500,
4924	    "total_episodes": 1062,
4925	    "total_steps": 212400
4926	}
4927	
4928	  exp_id: exp_032_dual_critic_walker
4929	  status: DONE
4930	  description: 
4931	  tags: 
4932	  conclusion: success
4933	  metrics: {
4934	    "baseline_eval": 900,
4935	    "civo_prevented": true,
4936	    "eval_final": 739.7,
4937	    "eval_final_step": 215000,
4938	    "eval_peak": 787.7,
4939	    "eval_peak_step": 205000,
4940	    "eval_vs_baseline_pct": 87.5,
4941	    "gate_dt2_frac": 1.0,
4942	    "gate_entropy": 0.0,
4943	    "note": "CIVO prevented 2/2 seeds. v1\u2248v2 \u2192 mechanism is implicit value regularization, not min-of-two pessimism.",
4944	    "nve_final": 0.1,
4945	    "nve_peak": 1.1,
4946	    "nve_peak_step": 95000,
4947	    "v1_v2_gap": "<0.1% (min operation has no pessimism effect)"
4948	}
4949	
4950	  exp_id: exp_032b_dual_critic_walker_s1
4951	  status: DONE
4952	  description: 
4953	  tags: 
4954	  conclusion: success
4955	  metrics: {
4956	    "actor_loss_late": "\u22480 (gradient signal weak)",
4957	    "baseline_eval": 900,
4958	    "director_override": "CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.",
4959	    "eval_criterion_pass": false,
4960	    "eval_trajectory": "75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516",
4961	    "eval_vs_baseline_pct": 57,
4962	    "final_eval_return": 516,
4963	    "final_nve": 0.1,
4964	    "gate_dt2_frac": 1.0,
4965	    "nve_criterion_pass": true,
4966	    "nve_trajectory": "15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1",
4967	    "peak_eval_return": 551.8,
4968	    "peak_nve": 1.4,
4969	    "total_steps": 224000,
4970	    "total_updates": 52599,
4971	    "training_hours": 6.42,
4972	    "value1_value2_gap": "<0.5 (min operation has no pessimism effect)"
4973	}
4974	
4975	  exp_id: exp_034
4976	  status: DONE
4977	  description: 
4978	  tags: 
4979	  conclusion: negative
4980	  metrics: {
4981	    "CIVO_prevented": false,
4982	    "civo_trigger_steps": [
4983	        55000,
4984	        105000
4985	    ],
4986	    "final_NVE": 0.144,
4987	    "final_eval_return": 97.5,
4988	    "max_NVE": 1.753,
4989	    "peak_eval_return": 315.7,
4990	    "total_steps": 215000,
4991	    "v1_v2_max_divergence": 0.004
4992	}
4993	
4994	  exp_id: exp_034_dual_critic_cheetah
4995	  status: DONE
4996	  description: 
4997	  tags: 
4998	  conclusion: negative
4999	  metrics: {
5000	    "baseline_eval_final": 0.83,
5001	    "baseline_nve_peak": 70.64,
5002	    "civo_alert_steps": [
5003	        95000,
5004	        105000
5005	    ],
5006	    "civo_alerts": 2,
5007	    "civo_prevented": false,
5008	    "dual_wave_civo": true,
5009	    "eval_final": 97.5,
5010	    "eval_final_step": 215000,
5011	    "eval_peak": 315.7,
5012	    "eval_peak_step": 45000,
5013	    "eval_vs_peak_pct": 31,
5014	    "gate_dt2_frac": 1,
5015	    "gate_entropy": 0,
5016	    "v1_v2_gap": "<0.2 (min operation has no pessimism effect)",
5017	    "value_mean_final": 14.2,
5018	    "value_mean_peak": 60.5,
5019	    "ve_ratio_final": 0.1,
5020	    "ve_ratio_peak": 1.8,
5021	    "ve_ratio_peak_step": 55000
5022	}
5023	
5024	  exp_id: exp_035_narrow_dual_critic_walker
5025	  status: DONE
5026	  description: 
5027	  tags: 
5028	  conclusion: success
5029	  metrics: {
5030	    "actor_entropy_final": -0.19,
5031	    "civo_alert_window": "65K-85K",
5032	    "civo_prevented": false,
5033	    "civo_recovery": true,
5034	    "director_override": "Director ruled success: CIVO recovery (33.8\u2192697.8) is the success criterion, not prevention",
5035	    "eval_at_215K": 697.8,
5036	    "eval_at_85K": 33.8,
5037	    "eval_final": 697.8,
5038	    "eval_peak": 697.8,
5039	    "eval_trough": 33.8,
5040	    "nve_final": 0.066,
5041	    "nve_peak": 2.75,
5042	    "nve_peak_step": 85000,
5043	    "recovery_from": 33.8,
5044	    "recovery_to": 697.8,
5045	    "total_steps": 215000,
5046	    "train_return_final_range": "708-806",
5047	    "v1_v2_gap_max": 0.08,
5048	    "v1_v2_gap_typical": 0.01
5049	}
5050	
5051	  exp_id: exp_036_dual_critic_pickcube
5052	  status: DONE
5053	  description: 
5054	  tags: 
5055	  conclusion: negative
5056	  metrics: {
5057	    "civo_alert": 0,
5058	    "eval_return_final": 27.7,
5059	    "eval_return_peak": 27.7,
5060	    "gate_dt_2_frac": 1,
5061	    "nve_final": 0.2,
5062	    "nve_peak": 2.3,
5063	    "steps": 212447
5064	}
5065	
5066	  exp_id: exp_037_wide_critic_cheetah
5067	  status: DONE
5068	  description: 
5069	  tags: 
5070	  conclusion: negative
5071	  metrics: {
5072	    "civo_alert": 0,
5073	    "eval_return_final": 146.1,
5074	    "eval_return_peak": 350.1,
5075	    "gate_dt_2_frac": 1,
5076	    "nve_final": 0.1,
5077	    "nve_peak": 3.6,
5078	    "steps": 224000
5079	}
5080	
5081	  exp_id: exp_038_dual_critic_walker_s2
5082	  status: DONE
5083	  description: 
5084	  tags: 
5085	  conclusion: negative
5086	  metrics: {
5087	    "civo_alert": 0,
5088	    "civo_prevented": true,
5089	    "eval_return_collapse": 99.6,
5090	    "eval_return_collapse_step": 175000,
5091	    "eval_return_final": 120.9,
5092	    "eval_return_peak": 354,
5093	    "eval_return_peak_step": 155000,
5094	    "gate_dt_2_frac": 1,
5095	    "non_civo_collapse": true,
5096	    "note": "CIVO prevented (NVE\u22640.3) but non-CIVO eval collapse at 175k (354\u219299.6). Different failure mode from value overestimation.",
5097	    "nve_final": 0.248,
5098	    "nve_peak": 0.3,
5099	    "steps": 224000
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "f8931a4f-c005-4f2b-b491-65fe8266f607"
}
```

</details>

---


### System

_source line 128_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "usage": {
    "total_tokens": 91612,
    "tool_uses": 12,
    "duration_ms": 68758
  },
  "last_tool_name": "Read",
  "uuid": "7136e6ca-1321-48af-9e24-978f3f78fa6c",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool call

_source line 129_

<details open><summary>🔧 Tool call — Read · `toolu_01EftQMuKCyL2Z5JjVH9uLvN`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/brma6kldj.txt",
  "offset": 5100,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "5ed6855e-1f84-436a-a274-01b5d82f404b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PRMTPGdaUTxZc8WSTqtNHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6541,
      "cache_read_input_tokens": 84688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6541,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 130 · 2026-05-24T02:15:37.894Z_

<details><summary>↩ Tool result · `toolu_01EftQMuKCyL2Z5JjVH9uLvN`</summary>

```text
5100	}
5101	
5102	  exp_id: exp_039_narrow_dual_critic_walker_s1
5103	  status: DONE
5104	  description: 
5105	  tags: 
5106	  conclusion: success
5107	  metrics: {
5108	    "civo_recovery": true,
5109	    "eval_return_final": 592.7,
5110	    "note": "Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean\u2248645. Recovery 2/2.",
5111	    "nve_peak": 2.19,
5112	    "recovery_confirmed": true
5113	}
5114	
5115	  exp_id: exp_041_dual_critic_walker_s3
5116	  status: DONE
5117	  description: 
5118	  tags: 
5119	  conclusion: success
5120	  metrics: {
5121	    "eval_return_peak": 761.1,
5122	    "eval_return_final": 544,
5123	    "eval_return_peak_step": 165000,
5124	    "nve_peak": 1.5,
5125	    "nve_final": 0.1,
5126	    "civo_prevented": true,
5127	    "gate_dt_2_frac": 1,
5128	    "non_civo_collapse": false,
5129	    "steps": 215000,
5130	    "note": "CIVO prevented (NVE\u22641.5), no non-CIVO collapse. Eval stays 486-761 after peak. Non-CIVO collapse rate confirmed 1/4 (only s2)."
5131	}
5132	
5133	  exp_id: exp_042_frozen_dt_emb_walker
5134	  status: DONE
5135	  description: 
5136	  tags: 
5137	  conclusion: success
5138	  metrics: {
5139	    "eval_final": 612.45,
5140	    "eval_peak": 682.38,
5141	    "eval_peak_step": 205000,
5142	    "nve_peak": 0.194,
5143	    "nve_final": 0.051,
5144	    "civo_alert": false,
5145	    "total_steps": 224000,
5146	    "total_train_episodes": 224
5147	}
5148	
5149	  exp_id: exp_043_008f_walker_s1
5150	  status: DONE
5151	  description: 
5152	  tags: 
5153	  conclusion: success
5154	  metrics: {
5155	    "eval_final": 673.73,
5156	    "eval_peak": 673.73,
5157	    "eval_peak_step": 215000,
5158	    "nve_peak": 0.808,
5159	    "nve_peak_step": 105000,
5160	    "nve_final": 0.123,
5161	    "civo_alert": false,
5162	    "total_steps": 224000,
5163	    "gate_dt_2_frac": 1,
5164	    "gate_entropy": 0,
5165	    "note": "No CIVO (peak NVE 0.808, well below 1.5). Gate fixed at dt=2. Seed 1 replicates seed 0 finding: dt_emb absence prevents CIVO."
5166	}
5167	
5168	  exp_id: exp_045_treatment_extension_008d_s3
5169	  status: DONE
5170	  description: 
5171	  tags: 
5172	  conclusion: success
5173	  metrics: {
5174	    "eval_final": 867.6,
5175	    "eval_peak": 869.7,
5176	    "eval_peak_step": 242000,
5177	    "nve_peak": 4.91,
5178	    "nve_peak_step": 132000,
5179	    "nve_final": 0.052,
5180	    "ve_ratio_final": 0.052,
5181	    "total_steps": 312000,
5182	    "civo_alerts": 0,
5183	    "civo_self_corrected": true,
5184	    "civo_correction_step": 142000,
5185	    "eval_trajectory": {
5186	        "112000": 58.5,
5187	        "122000": 41.8,
5188	        "132000": 35.1,
5189	        "142000": 350.2,
5190	        "152000": 646.4,
5191	        "162000": 482.3,
5192	        "172000": 600.4,
5193	        "182000": 600.5,
5194	        "192000": 699.5,
5195	        "202000": 684.3,
5196	        "212000": 758.6,
5197	        "222000": 744.6,
5198	        "232000": 745.4,
5199	        "242000": 869.7,
5200	        "252000": 721.6,
5201	        "262000": 820.6,
5202	        "272000": 716.2,
5203	        "282000": 755.6,
5204	        "292000": 843,
5205	        "302000": 867.6
5206	    },
5207	    "ve_ratio_trajectory": {
5208	        "122000": 4.77,
5209	        "132000": 4.91,
5210	        "142000": 0.43,
5211	        "152000": 0.21,
5212	        "162000": 0.25,
5213	        "172000": 0.18,
5214	        "182000": 0.16,
5215	        "192000": 0.13,
5216	        "202000": 0.12,
5217	        "212000": 0.1,
5218	        "222000": 0.1,
5219	        "232000": 0.09,
5220	        "242000": 0.07,
5221	        "252000": 0.08,
5222	        "262000": 0.07,
5223	        "272000": 0.08,
5224	        "282000": 0.07,
5225	        "292000": 0.06,
5226	        "302000": 0.05
5227	    }
5228	}
5229	
5230	  exp_id: exp_046_frozen_dt_emb_cheetah
5231	  status: DONE
5232	  description: 
5233	  tags: 
5234	  conclusion: success
5235	  metrics: {
5236	    "eval_final": 150.5,
5237	    "eval_peak": 207.4,
5238	    "eval_peak_step": 145000,
5239	    "ve_ratio_peak": 0.4,
5240	    "ve_ratio_final": 0.1,
5241	    "nve_peak": 1.35,
5242	    "nve_peak_step": 45000,
5243	    "nve_final": 0.17,
5244	    "total_steps": 224000,
5245	    "civo_alert_count": 0
5246	}
5247	
5248	  exp_id: exp_047_frozen_dt_emb_walker_s1
5249	  status: DONE
5250	  description: 
5251	  tags: 
5252	  conclusion: success
5253	  metrics: {
5254	    "eval_final": 144.22,
5255	    "eval_final_step": 215000,
5256	    "eval_peak": 408.79,
5257	    "eval_peak_step": 125000,
5258	    "ve_ratio_peak": 1.099,
5259	    "ve_ratio_peak_step": 75000,
5260	    "ve_ratio_final": 0.277,
5261	    "nve_peak": 1.71,
5262	    "nve_peak_step": 95000,
5263	    "nve_final_105k": 0.56,
5264	    "total_steps": 225000
5265	}
5266	
5267	  exp_id: exp_048_cheetah_civo_extension
5268	  status: DONE
5269	  description: 
5270	  tags: 
5271	  conclusion: success
5272	  metrics: {
5273	    "eval_final": 23.4,
5274	    "eval_final_step": 302000,
5275	    "eval_peak": 32.8,
5276	    "eval_peak_step": 252000,
5277	    "ve_ratio_initial": 46.3,
5278	    "ve_ratio_peak": 24.112,
5279	    "ve_ratio_peak_step": 162000,
5280	    "ve_ratio_final": 1.803,
5281	    "nve_initial": 70.64,
5282	    "nve_peak_secondary": 36.76,
5283	    "nve_final": 2.75,
5284	    "total_steps": 312000,
5285	    "civo_self_corrected": false,
5286	    "civo_correction_pct": 96,
5287	    "secondary_burst_step": 152000,
5288	    "secondary_burst_nve": 36.47,
5289	    "gate_collapsed": true
5290	}
5291	
5292	  exp_id: exp_055_peginsertion_civo_trigger_s1
5293	  status: DONE
5294	  description: 
5295	  tags: 
5296	  conclusion: success
5297	  metrics: {
5298	    "total_steps": 222400,
5299	    "ve_ratio_peak": 3.08,
5300	    "ve_ratio_peak_step": 92500,
5301	    "ve_ratio_final": 0.498,
5302	    "ve_ratio_final_step": 212500,
5303	    "eval_return_final": 11.44,
5304	    "eval_return_final_step": 212500,
5305	    "eval_return_peak": 24.05,
5306	    "eval_return_peak_step": 112500,
5307	    "nve_classification": "transient",
5308	    "civo_triggered": true,
5309	    "civo_self_corrected": "partial",
5310	    "note": "CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 \u2014 severity seed-dependent.",
5311	    "ve_ratio_trajectory": {
5312	        "12500": 0.19,
5313	        "22500": 0.81,
5314	        "32500": 1.35,
5315	        "42500": 2.0,
5316	        "52500": 2.39,
5317	        "62500": 2.85,
5318	        "72500": 2.28,
5319	        "82500": 2.48,
5320	        "92500": 3.08,
5321	        "102500": 2.51,
5322	        "112500": 0.91,
5323	        "122500": 1.21,
5324	        "132500": 1.36,
5325	        "142500": 0.75,
5326	        "152500": 0.55,
5327	        "162500": 1.17,
5328	        "172500": 0.96,
5329	        "182500": 0.94,
5330	        "192500": 0.9,
5331	        "202500": 0.73,
5332	        "212500": 0.5
5333	    }
5334	}
5335	
5336	  exp_id: exp_056_peginsertion_frozen_s1
5337	  status: DONE
5338	  description: 
5339	  tags: 
5340	  conclusion: success
5341	  metrics: {
5342	    "total_steps": 222500,
5343	    "ve_ratio_peak": 11.321,
5344	    "ve_ratio_peak_step": 82500,
5345	    "ve_ratio_final": 1.193,
5346	    "ve_ratio_final_step": 212500,
5347	    "eval_return_final": 4.37,
5348	    "eval_return_final_step": 212500,
5349	    "eval_return_peak": 24.42,
5350	    "eval_return_peak_step": 132500,
5351	    "nve_classification": "burst",
5352	    "note": "Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 \u2014 frozen does NOT suppress ManiSkill transients.",
5353	    "ve_ratio_trajectory": {
5354	        "12500": 0.316,
5355	        "22500": 0.975,
5356	        "32500": 1.839,
5357	        "42500": 1.966,
5358	        "52500": 5.422,
5359	        "62500": 4.047,
5360	        "72500": 8.408,
5361	        "82500": 11.321,
5362	        "92500": 3.724,
5363	        "102500": 3.034,
5364	        "112500": 2.204,
5365	        "122500": 2.425,
5366	        "132500": 0.842,
5367	        "142500": 2.194,
5368	        "152500": 2.203,
5369	        "162500": 0.651,
5370	        "172500": 1.085,
5371	        "182500": 1.07,
5372	        "192500": 0.467,
5373	        "202500": 0.708,
5374	        "212500": 1.193
5375	    }
5376	}
5377	
5378	  exp_id: exp_057_frozen_dt_emb_walker_s2
5379	  status: DONE
5380	  description: 
5381	  tags: 
5382	  conclusion: success
5383	  metrics: {
5384	    "total_steps": 225000,
5385	    "ve_ratio_peak": 1.283,
5386	    "ve_ratio_peak_step": 115000,
5387	    "ve_ratio_final": 0.177,
5388	    "ve_ratio_final_step": 215000,
5389	    "nve_peak": 1.88,
5390	    "nve_peak_step": 115000,
5391	    "nve_classification": "transient",
5392	    "note": "Walker frozen s2. NVE=1.88\u00d7 (raw 1.283 / baseline 0.683 @115K). Peak transient at 115K, self-corrected. Walker frozen n=3: s0=0.19, s1=1.71, s2=1.88 \u2014 all transient, no sustained CIVO."
5393	}
5394	
5395	  exp_id: exp_058_frozen_dt_emb_cheetah_s1
5396	  status: DONE
5397	  description: 
5398	  tags: 
5399	  conclusion: success
5400	  metrics: {
5401	    "total_steps": 224000,
5402	    "ve_ratio_peak": 0.231,
5403	    "ve_ratio_peak_step": 45000,
5404	    "ve_ratio_final": 0.107,
5405	    "ve_ratio_final_step": 215000,
5406	    "eval_return_final": 80.46,
5407	    "eval_return_final_step": 215000,
5408	    "eval_return_peak": 191.74,
5409	    "eval_return_peak_step": 25000,
5410	    "nve_peak": 0.78,
5411	    "nve_peak_step": 45000,
5412	    "nve_classification": "no_civo",
5413	    "note": "Cheetah frozen s1. NVE=0.78\u00d7 (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 \u2014 both clean, frozen \u7a33\u5065\u963b\u6b62 extreme CIVO (trained NVE 70-108)."
5414	}
5415	
5416	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "4c25a807-8432-460d-988e-e0003db54f67"
}
```

</details>

---


### System

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ae30e999662486a85",
  "tool_use_id": "toolu_01HgEkLqDE5nyBUNnBawjh3J",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry CIVO/frozen data",
  "usage": {
    "total_tokens": 96372,
    "tool_uses": 12,
    "duration_ms": 174455
  },
  "uuid": "f1aedabf-3af0-45cd-a157-31622beb699d",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---


### Tool result

_source line 132 · 2026-05-24T02:17:23.589Z_

<details><summary>↩ Tool result · `toolu_01HgEkLqDE5nyBUNnBawjh3J`</summary>

```text
I now have all the data. Here is the complete organized audit report:

---

## Registry Audit Report

**Total experiments in registry: 132**

---

## 1. CIVO Trigger Experiments (11 found)

**exp_008d_civo_trigger_s2** — status: DONE, conclusion: killed, metrics: {}

**exp_008d_civo_trigger_s3** — status: DONE, conclusion: success
- nve_onset_step: 45000, nve_onset_value: 1.5
- nve_peak: 1.53 @ 105K, nve_final: 1.53
- nve_sustained_45K_55K: true
- eval_return_peak: 451.7 @ 95K, eval_return_final: 267.6 @ 105K
- baseline_eval_105K: 915.67, vs_baseline_105K: -70.8%

**exp_008d_civo_trigger_s4** — status: DONE, conclusion: success
- civo_confirmed: true, delta_ve_105K: 2.05
- gate_dt_mean: 2, gate_dt_2_frac: 1, gate_entropy: 0
- ve_ratio_105K: 3.03, value_mean_105K: 192.65
- peak_eval_return: 383.3 @ 85K, final_eval_return_105K: 63.6
- NVE values: not directly stored but civo_alert_105K: 1, nve implied by ve_ratio_105K=3.03

**exp_010b_cheetah_civo_trigger** — status: DONE, conclusion: success
- civo: true
- nve_peak: 8.27 @ 65K
- eval_return_peak: 321.9 @ 35K, eval_return_final: 51.7

**exp_010b_cheetah_civo_trigger_s0** — status: DONE, conclusion: success
- civo: true, civo_onset_step: 65K, detector_alert_step: 95K
- nve_95K: 6.34, nve_105K: 70.64
- eval_return_peak: 247.77 @ 35K, eval_return_105K: 0.83
- gate_dt_mean: 2, gate_entropy: 0

**exp_019b_pickcube_civo_trigger** — status: DONE, conclusion: success
- nve_peak: 3.78 @ 52.5K, nve_final: 0.065
- eval_return_peak: 26.9 @ 132.5K, eval_return_final: 26.64
- pattern: transient_civo_then_value_collapse
- baseline_eval_final: 58.56, value_baseline_final: 144.57, value_mean_final: 4.26

**exp_048_cheetah_civo_extension** — status: DONE, conclusion: success
- nve_initial: 70.64, nve_peak_secondary: 36.76, nve_final: 2.75
- secondary_burst_nve: 36.47 @ 152K
- ve_ratio_initial: 46.3, ve_ratio_peak: 24.112 @ 162K, ve_ratio_final: 1.803
- eval_peak: 32.8 @ 252K, eval_final: 23.4 @ 302K
- civo_self_corrected: false, civo_correction_pct: 96, gate_collapsed: true

**exp_049_stackcube_civo_trigger_s0** — status: DONE, conclusion: success
- ve_ratio_peak: 5.05 @ 42.5K, ve_ratio_final: 0.186 @ 212.5K
- eval_peak: 35.89 @ 182.5K, eval_final: 34.88 @ 212.5K
- (no nve fields stored)

**exp_050_peginsertion_civo_trigger_s0** — status: DONE, conclusion: success
- ve_ratio_peak: 10.05 @ 82.5K, ve_ratio_final: 0.379 @ 212.5K
- civo_self_corrected: true, civo_correction_delay_steps: 130000
- eval_peak: 20.86 @ 212.5K, eval_final: 20.86

**exp_052_stackcube_civo_trigger_s1** — status: DONE, conclusion: success
- ve_ratio_peak: 4.67 @ 52.5K, ve_ratio_final: 0.133 @ 212.5K
- eval_peak: 39.873 @ 162.5K, eval_final: 29.458 @ 212.5K

**exp_055_peginsertion_civo_trigger_s1** — status: DONE, conclusion: success
- ve_ratio_peak: 3.08 @ 92.5K, ve_ratio_final: 0.498 @ 212.5K
- nve_classification: transient
- civo_triggered: true, civo_self_corrected: partial
- eval_return_peak: 24.05 @ 112.5K, eval_return_final: 11.44 @ 212.5K
- Note: PegInsertion trained cross-seed: s0=10.05, s1=3.08 — severity seed-dependent

---

## 2. Frozen dt_emb Experiments (10 found)

**exp_015b_frozen_dt_emb** — status: DONE, conclusion: negative
- collapse_mechanism: gradient_starvation_from_frozen_dt_emb
- nve_85K: 0.467, nve_95K: 0.394, nve_105K: 0.42 (far below 1.0, critic under-estimates)
- eval_return_final: 204.2 (volatile 80-238, no stable convergence)
- gate_dt_mean: 2, gate_dt_1_frac: 0 (locked dt=2 100%)
- actor_loss_105K: 0.000179 (gradient starvation)

**exp_042_frozen_dt_emb_walker** (s0) — status: DONE, conclusion: success
- nve_peak: 0.194, nve_final: 0.051, civo_alert: false
- eval_final: 612.45, eval_peak: 682.38 @ 205K

**exp_046_frozen_dt_emb_cheetah** (s0) — status: DONE, conclusion: success
- nve_peak: 1.35 @ 45K, nve_final: 0.17, civo_alert_count: 0
- eval_final: 150.5, eval_peak: 207.4 @ 145K
- ve_ratio_peak: 0.4, ve_ratio_final: 0.1

**exp_047_frozen_dt_emb_walker_s1** — status: DONE, conclusion: success
- nve_peak: 1.71 @ 95K, nve_final_105k: 0.56
- ve_ratio_peak: 1.099 @ 75K, ve_ratio_final: 0.277
- eval_final: 144.22 @ 215K, eval_peak: 408.79 @ 125K

**exp_051_stackcube_frozen_dt_emb_s0** — status: DONE, conclusion: success
- ve_ratio_peak: 4.3 @ 42.5K, ve_ratio_final: 0.122 @ 212.5K
- eval_final: 45.31 @ 212.5K, eval_peak: 45.31
- (no nve fields)

**exp_053_peginsertion_frozen_s0** — status: DONE, conclusion: success, metrics: {}

**exp_054_pickcube_frozen_s0** — status: DONE, conclusion: success, metrics: {}

**exp_056_peginsertion_frozen_s1** — status: DONE, conclusion: success
- ve_ratio_peak: 11.321 @ 82.5K, ve_ratio_final: 1.193 @ 212.5K
- nve_classification: burst
- eval_return_peak: 24.42 @ 132.5K, eval_return_final: 4.37 @ 212.5K
- Note: Frozen s1 burst 11.32 > trained s1 peak 3.08 — frozen does NOT suppress ManiSkill transients

**exp_057_frozen_dt_emb_walker_s2** — status: DONE, conclusion: success
- nve_peak: 1.88 @ 115K, nve_classification: transient
- ve_ratio_peak: 1.283 @ 115K, ve_ratio_final: 0.177 @ 215K
- Note: NVE=1.88× (raw 1.283 / baseline 0.683 @115K). Walker frozen n=3: s0=0.19, s1=1.71, s2=1.88 — all transient, no sustained CIVO.

**exp_058_frozen_dt_emb_cheetah_s1** — status: DONE, conclusion: success
- nve_peak: 0.78 @ 45K, nve_classification: no_civo
- ve_ratio_peak: 0.231 @ 45K, ve_ratio_final: 0.107 @ 215K
- eval_return_final: 80.46 @ 215K, eval_return_peak: 191.74 @ 25K
- Note: Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen stably blocks extreme CIVO (trained NVE 70-108)

---

## 3. Manipulation / PickCube / PegInsertion (11 found)

(Overlaps with categories 1 & 2 above; unique entries below)

**exp_019a_pickcube_baseline** — status: DONE, conclusion: killed, metrics: {}

**exp_019a_v2_pickcube_baseline** — status: DONE, conclusion: success
- eval_return_final: 69.43, eval_return_peak: 69.7 @ 162.5K
- value_mean_final: 143.4, ve_ratio_final: 2.07, ve_ratio_range: 1.05-3.56
- steps_completed: 200248

**exp_031_tcn_pickcube_s0_sigma02** — status: DONE, conclusion: negative
- ve_ratio_peak: 3.71, ve_ratio_latest: 0.18
- eval_peak: 28.6 @ 162.5K
- gate_dt2_frac: 1.0, gate_entropy: 0
- (no explicit nve field)

**exp_031b_tcn_pickcube_s0_sigma05** — status: DONE, conclusion: negative
- nve_peak: 3.3 @ 42.5K, nve_final: 0.2, nve_suppressed_from_step: 72500
- eval_reward_peak: 29.1, eval_reward_final: 25.5

**exp_036_dual_critic_pickcube** — status: DONE, conclusion: negative
- nve_peak: 2.3, nve_final: 0.2, civo_alert: 0
- eval_return_final: 27.7, eval_return_peak: 27.7
- gate_dt_2_frac: 1

---

## 4. Walker Baseline Experiments (specifically requested 3)

**exp_009d_baseline_walker_s0** — status: DONE, conclusion: success
- eval_return: 927.6 @ 508K
- eval_return_peak: 950.96 @ 398K
- step: 508000

**exp_009d_baseline_walker_s1** — status: DONE, conclusion: killed, metrics: {}

**exp_009a_baseline_walker_s2** — status: DONE, conclusion: success
- eval_return_peak: 966.94 @ 395K, final_eval_return: 957.87 @ 505K
- final_value_mean: 665.17, final_ve_ratio: 0.694
- last10_mean: 947.19, n_evals: 51, total_steps: 505000
- ve_stable_range: 0.69-0.72 from 235K+
- vs_exp001 comparisons: peak 966.94 vs 970.41 (-0.4%), final 957.87 vs 970.41 (-1.3%), last10 947.19 vs 950.90 (-0.4%)

---

## 5. Cheetah Baseline Experiments

Named "cheetah_baseline" specifically: **exp_023a_cheetah_baseline_s0**, **exp_023b_cheetah_baseline_s1**, **exp_023_cheetah_baseline_s2**, **exp_023_cheetah_baseline_s3**, **exp_023_cheetah_baseline_s4**, **exp_023_cheetah_baseline_s4_extended**, **exp_010a_cheetah_baseline_s1**

**exp_023a_cheetah_baseline_s0** — conclusion: success
- eval_return_final: 624.7, eval_return_peak: 624.7 @ 205K, civo: false

**exp_023b_cheetah_baseline_s1** — conclusion: success
- eval_return_final: 520.3, eval_return_peak: 572.9 @ 195K
- ve_ratio_range: 0.5-0.7, civo: false

**exp_023_cheetah_baseline_s2** — conclusion: success
- eval_return_final: 645.4 @ 205K
- Note: "Third baseline seed for NVE normalization."

**exp_023_cheetah_baseline_s3** — conclusion: success
- eval_return_202k: 642.13, peak_eval: 685.93 @ 172K
- value_mean_final: 445.42, ve_ratio_final: 0.694

**exp_023_cheetah_baseline_s4** — conclusion: success
- eval_return_194k: 537.03, eval_return_204k: 301.69
- peak_eval: 537.03 @ 194K, ve_ratio_204k: 1.124

**exp_023_cheetah_baseline_s4_extended** — conclusion: success
- eval_302k: 580, eval_peak_ext: 642.3 @ 272K
- Note: extended to 300K confirms non-collapse; 194K→204K drop was transient fluctuation.

**exp_010a_cheetah_baseline_s1** — conclusion: success
- eval_return_final: 849.8 @ 515K, eval_return_peak: 849.8 @ 515K
- final_step: 524K, train_return_last: 716

Also cheetah-related baselines with NVE:
- **exp_008a_cheetah_unexposed_s0**: nve_105k: 0.49, eval_return_105k: 532.35, ve_ratio_105k: 0.3193
- **exp_008a_cheetah_unexposed_s1**: nve_105k: 0.478, eval_return_105k: 504.38, ve_ratio_105k: 0.3112

---

## 6. exp_057 and exp_058

**exp_057** → **exp_057_frozen_dt_emb_walker_s2** (full details in section 2 above)
- nve_peak: 1.88 @ 115K, nve_classification: transient
- ve_ratio_peak: 1.283, ve_ratio_final: 0.177
- Walker frozen n=3 summary: s0=0.19, s1=1.71, s2=1.88

**exp_058** → **exp_058_frozen_dt_emb_cheetah_s1** (full details in section 2 above)
- nve_peak: 0.78 @ 45K, nve_classification: no_civo
- ve_ratio_peak: 0.231, ve_ratio_final: 0.107
- eval_return_final: 80.46, eval_return_peak: 191.74

---

## 7. "Frozen" in experiment name — 10 experiments

Same list as section 2 above: exp_015b_frozen_dt_emb, exp_042_frozen_dt_emb_walker, exp_046_frozen_dt_emb_cheetah, exp_047_frozen_dt_emb_walker_s1, exp_051_stackcube_frozen_dt_emb_s0, exp_053_peginsertion_frozen_s0, exp_054_pickcube_frozen_s0, exp_056_peginsertion_frozen_s1, exp_057_frozen_dt_emb_walker_s2, exp_058_frozen_dt_emb_cheetah_s1.

---

## 8. All Experiments with NVE in Metrics/Conclusion (58 found)

Consolidated NVE values table (key experiments):

| exp_id | nve_peak | nve_peak_step | nve_final | classification |
|--------|----------|---------------|-----------|----------------|
| exp_008a_cheetah_unexposed_s0 | — | — | 0.49 (nve_105k) | — |
| exp_008a_cheetah_unexposed_s1 | — | — | 0.478 (nve_105k) | — |
| exp_008d_civo_trigger_s3 | 1.53 | 105K | 1.53 | late-onset collapse |
| exp_008e_v3_s3 | 4.02 | 105K | — | (corrected from 5.00) |
| exp_008e_v3_s4 | 0.99 | 95K | — | no CIVO |
| exp_008e_v3_walker_s2 | 3.78 | 105K | 3.78 | confirmed collapse |
| exp_008f_s3_no_dt_embed_walker | < 1.5 | — | — | no collapse |
| exp_008f_s4 | 1.41 | 85K | 0.58 (105K) | transient |
| exp_009b_008d_walker_s2 | 2.05 | 25K | 0.38 | self-corrected |
| exp_009c_s3 | — | — | 0.52 (105K) | no CIVO |
| exp_009e_008d_walker_s1 | 4.12 | 55K | 1.57 | sustained CIVO |
| exp_010b_cheetah_civo_trigger | 8.27 | 65K | — | civo |
| exp_010b_cheetah_civo_trigger_s0 | 70.64 (105K) | — | — | extreme CIVO |
| exp_015b_frozen_dt_emb | 0.467 | 85K | 0.42 (105K) | under-estimates |
| exp_016e_sgs_walker_s1 | 10.42 | 95K | — | catastrophic |
| exp_018_full_sgs_walker_s1 | 0.72 | 75K | — | no CIVO |
| exp_018v2_full_sgs_walker_s1 | 1.66 | 95K | 1.34 | late collapse |
| exp_019b_pickcube_civo_trigger | 3.78 | 52.5K | 0.065 | transient then collapse |
| exp_020_vanilla_dreamerv3_s2 | — | — | — | parent_nve_105K: 3.78 (reference) |
| exp_021_full_sgs_cheetah_s1 | 9.94 | 45K | 0.338 (55K-105K avg) | transient self-correcting |
| exp_022b_no_curriculum | 1.22 (peak) | — | — | no CIVO alert |
| exp_023_cheetah_baseline_s2 | — | — | — | note: NVE normalization baseline |
| exp_024b_cheetah_no_dt_emb_s0 | 0.2 | — | — | no CIVO |
| exp_024b_cheetah_no_dt_emb_s1 | 0.1 | — | — | no CIVO |
| exp_027_tcn_walker_s0 | 3.965 | 85K | — | breach: 55K(1.68), 65K(1.54), 85K(3.97) |
| exp_027_tcn_walker_s0_sigma02 | 0.9081 | 95K | 0.0955 | no sustained CIVO |
| exp_027_tcn_walker_s1 | 1.6367 | 95K | 0.1476 | transient |
| exp_028_rave_walker_s0 | ~4.09 (ve@95K) | 95K | — | diverged from 55K |
| exp_029a_tcn_walker_s1_sigma02 | 0.6428 | 55K | 0.1864 | clean |
| exp_029b_tcn_walker_s2_sigma02 | 2.765 | 105K | — | CIVO onset 65K |
| exp_029c_tcn_walker_s0_sigma01 | 1.0218 | 95K | 0.1 | transient |
| exp_029d_tcn_walker_s3_sigma02 | 3.0 | 105K | — | sudden blowup |
| exp_030a_tcn_cheetah_s0_sigma02 | 1.903 (ve@55K) | 55K | — | possible CIVO |
| exp_030b_tcn_cheetah_s0_sigma05 | 10.6657 | 55K | 0.1534 | extreme then self-corrected |
| exp_031b_tcn_pickcube_s0_sigma05 | 3.3 | 42.5K | 0.2 | suppressed from 72.5K |
| exp_032_dual_critic_walker | 1.1 | 95K | 0.1 | CIVO prevented |
| exp_032b_dual_critic_walker_s1 | 1.4 | 85K | 0.1 | CIVO suppressed |
| exp_034 | 1.753 (max_NVE) | — | 0.144 | CIVO not prevented |
| exp_034_dual_critic_cheetah | baseline_nve_peak: 70.64 | — | — | dual wave CIVO |
| exp_035_narrow_dual_critic_walker | 2.75 | 85K | 0.066 | CIVO recovery |
| exp_036_dual_critic_pickcube | 2.3 | — | 0.2 | negative |
| exp_037_wide_critic_cheetah | 3.6 | — | 0.1 | negative |
| exp_038_dual_critic_walker_s2 | 0.3 | — | 0.248 | CIVO prevented, non-CIVO collapse |
| exp_039_narrow_dual_critic_walker_s1 | 2.19 | — | — | CIVO recovery confirmed |
| exp_041_dual_critic_walker_s3 | 1.5 | — | 0.1 | CIVO prevented |
| exp_042_frozen_dt_emb_walker | 0.194 | — | 0.051 | no CIVO |
| exp_043_008f_walker_s1 | 0.808 | 105K | 0.123 | no CIVO |
| exp_045_treatment_extension_008d_s3 | 4.91 | 132K | 0.052 | self-corrected @142K |
| exp_046_frozen_dt_emb_cheetah | 1.35 | 45K | 0.17 | no alert |
| exp_047_frozen_dt_emb_walker_s1 | 1.71 | 95K | 0.56 (105K) | transient |
| exp_048_cheetah_civo_extension | 70.64 (initial) / 36.76 (secondary) | — | 2.75 | not self-corrected |
| exp_055_peginsertion_civo_trigger_s1 | — (nve_classification: transient) | — | — | ve_ratio_peak: 3.08 |
| exp_056_peginsertion_frozen_s1 | — (nve_classification: burst) | — | — | ve_ratio_peak: 11.321 |
| exp_057_frozen_dt_emb_walker_s2 | 1.88 | 115K | — | transient |
| exp_058_frozen_dt_emb_cheetah_s1 | 0.78 | 45K | — | no_civo |
| exp_001_baseline_s2_extended | — | — | — | ve_ratio_at_105K: 0.7422 |
| exp_001_baseline_s4_extended | — | — | — | no NVE values stored |

---

**Key summary for paper audit:**

- Walker baseline (exp_009a_baseline_walker_s2): final 957.87, peak 966.94, last10_mean 947.19
- Walker baseline (exp_009d_baseline_walker_s0): final 927.6, peak 950.96
- Cheetah baselines: s0=624.7, s1=520.3 (peak 572.9), s2=645.4, s3=642.13 (peak 685.93)
- Frozen Walker n=3 NVE: s0=0.194, s1=1.71, s2=1.88 — all transient, no sustained CIVO
- Frozen Cheetah n=2 NVE: s0=1.35, s1=0.78 — both no_civo, blocks trained CIVO (70–108×)
- Cheetah trained CIVO: exp_010b_cheetah_civo_trigger nve_peak=8.27; exp_010b_cheetah_civo_trigger_s0 nve_105K=70.64
- PegInsertion trained cross-seed: s0 ve_ratio_peak=10.05, s1 ve_ratio_peak=3.08
- PegInsertion frozen cross-seed: s0 metrics={} (no data), s1 ve_ratio_peak=11.321 (burst)
- exp_057 and exp_058 both exist (frozen walker s2 and frozen cheetah s1 respectively)

agentId: ae30e999662486a85 (use SendMessage with to: 'ae30e999662486a85' to continue this agent)
&lt;usage>total_tokens: 102943
tool_uses: 12
duration_ms: 174456&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "30ce86b2-d96d-422f-b843-c8f746ce631f",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to extract specific experiment data from a registry JSON file for a paper consistency audit.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt\n\nThe file is JSON with schema: {result: string} where result is itself a JSON string containing {success, data: {experiments: {...}, count, total, baseline}, error, metadata}.\n\nI need you to extract and report the following information from the registry:\n\n1. **All CIVO trigger experiments**: Any exp with \"civo_trigger\" in the name. Report exp_id, status, conclusion, metrics (especially NVE values).\n\n2. **All frozen dt_emb experiments**: Any exp with \"frozen\" in the name or description. Report exp_id, status, conclusion, metrics.\n\n3. **All manipulation/PickCube/PegInsertion experiments**: Any exp with \"pickcube\", \"peginsertion\", \"peg\", \"manipulation\" in name. Report exp_id, status, conclusion, metrics.\n\n4. **Walker baseline experiments**: exp_009d_baseline_walker_s0, exp_009d_baseline_walker_s1, exp_009a_baseline_walker_s2. Report metrics.\n\n5. **Cheetah baseline experiments**: Any exp with \"cheetah_baseline\" in name. Report exp_id, metrics.\n\n6. **Experiments exp_057 and exp_058**: If they exist, report full details.\n\n7. **Any experiment with \"frozen\" in the name**: Full details.\n\n8. **All experiments with NVE or nve in their metrics/conclusion**: Report the NVE values.\n\nFor each experiment, extract: exp_id, status, conclusion (full text), metrics (full dict), description, tags.\n\nUse python or jq to parse. Report results organized by category. Be precise with numbers - this is for a paper data audit.",
    "agentId": "ae30e999662486a85",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the data. Here is the complete organized audit report:\n\n---\n\n## Registry Audit Report\n\n**Total experiments in registry: 132**\n\n---\n\n## 1. CIVO Trigger Experiments (11 found)\n\n**exp_008d_civo_trigger_s2** — status: DONE, conclusion: killed, metrics: {}\n\n**exp_008d_civo_trigger_s3** — status: DONE, conclusion: success\n- nve_onset_step: 45000, nve_onset_value: 1.5\n- nve_peak: 1.53 @ 105K, nve_final: 1.53\n- nve_sustained_45K_55K: true\n- eval_return_peak: 451.7 @ 95K, eval_return_final: 267.6 @ 105K\n- baseline_eval_105K: 915.67, vs_baseline_105K: -70.8%\n\n**exp_008d_civo_trigger_s4** — status: DONE, conclusion: success\n- civo_confirmed: true, delta_ve_105K: 2.05\n- gate_dt_mean: 2, gate_dt_2_frac: 1, gate_entropy: 0\n- ve_ratio_105K: 3.03, value_mean_105K: 192.65\n- peak_eval_return: 383.3 @ 85K, final_eval_return_105K: 63.6\n- NVE values: not directly stored but civo_alert_105K: 1, nve implied by ve_ratio_105K=3.03\n\n**exp_010b_cheetah_civo_trigger** — status: DONE, conclusion: success\n- civo: true\n- nve_peak: 8.27 @ 65K\n- eval_return_peak: 321.9 @ 35K, eval_return_final: 51.7\n\n**exp_010b_cheetah_civo_trigger_s0** — status: DONE, conclusion: success\n- civo: true, civo_onset_step: 65K, detector_alert_step: 95K\n- nve_95K: 6.34, nve_105K: 70.64\n- eval_return_peak: 247.77 @ 35K, eval_return_105K: 0.83\n- gate_dt_mean: 2, gate_entropy: 0\n\n**exp_019b_pickcube_civo_trigger** — status: DONE, conclusion: success\n- nve_peak: 3.78 @ 52.5K, nve_final: 0.065\n- eval_return_peak: 26.9 @ 132.5K, eval_return_final: 26.64\n- pattern: transient_civo_then_value_collapse\n- baseline_eval_final: 58.56, value_baseline_final: 144.57, value_mean_final: 4.26\n\n**exp_048_cheetah_civo_extension** — status: DONE, conclusion: success\n- nve_initial: 70.64, nve_peak_secondary: 36.76, nve_final: 2.75\n- secondary_burst_nve: 36.47 @ 152K\n- ve_ratio_initial: 46.3, ve_ratio_peak: 24.112 @ 162K, ve_ratio_final: 1.803\n- eval_peak: 32.8 @ 252K, eval_final: 23.4 @ 302K\n- civo_self_corrected: false, civo_correction_pct: 96, gate_collapsed: true\n\n**exp_049_stackcube_civo_trigger_s0** — status: DONE, conclusion: success\n- ve_ratio_peak: 5.05 @ 42.5K, ve_ratio_final: 0.186 @ 212.5K\n- eval_peak: 35.89 @ 182.5K, eval_final: 34.88 @ 212.5K\n- (no nve fields stored)\n\n**exp_050_peginsertion_civo_trigger_s0** — status: DONE, conclusion: success\n- ve_ratio_peak: 10.05 @ 82.5K, ve_ratio_final: 0.379 @ 212.5K\n- civo_self_corrected: true, civo_correction_delay_steps: 130000\n- eval_peak: 20.86 @ 212.5K, eval_final: 20.86\n\n**exp_052_stackcube_civo_trigger_s1** — status: DONE, conclusion: success\n- ve_ratio_peak: 4.67 @ 52.5K, ve_ratio_final: 0.133 @ 212.5K\n- eval_peak: 39.873 @ 162.5K, eval_final: 29.458 @ 212.5K\n\n**exp_055_peginsertion_civo_trigger_s1** — status: DONE, conclusion: success\n- ve_ratio_peak: 3.08 @ 92.5K, ve_ratio_final: 0.498 @ 212.5K\n- nve_classification: transient\n- civo_triggered: true, civo_self_corrected: partial\n- eval_return_peak: 24.05 @ 112.5K, eval_return_final: 11.44 @ 212.5K\n- Note: PegInsertion trained cross-seed: s0=10.05, s1=3.08 — severity seed-dependent\n\n---\n\n## 2. Frozen dt_emb Experiments (10 found)\n\n**exp_015b_frozen_dt_emb** — status: DONE, conclusion: negative\n- collapse_mechanism: gradient_starvation_from_frozen_dt_emb\n- nve_85K: 0.467, nve_95K: 0.394, nve_105K: 0.42 (far below 1.0, critic under-estimates)\n- eval_return_final: 204.2 (volatile 80-238, no stable convergence)\n- gate_dt_mean: 2, gate_dt_1_frac: 0 (locked dt=2 100%)\n- actor_loss_105K: 0.000179 (gradient starvation)\n\n**exp_042_frozen_dt_emb_walker** (s0) — status: DONE, conclusion: success\n- nve_peak: 0.194, nve_final: 0.051, civo_alert: false\n- eval_final: 612.45, eval_peak: 682.38 @ 205K\n\n**exp_046_frozen_dt_emb_cheetah** (s0) — status: DONE, conclusion: success\n- nve_peak: 1.35 @ 45K, nve_final: 0.17, civo_alert_count: 0\n- eval_final: 150.5, eval_peak: 207.4 @ 145K\n- ve_ratio_peak: 0.4, ve_ratio_final: 0.1\n\n**exp_047_frozen_dt_emb_walker_s1** — status: DONE, conclusion: success\n- nve_peak: 1.71 @ 95K, nve_final_105k: 0.56\n- ve_ratio_peak: 1.099 @ 75K, ve_ratio_final: 0.277\n- eval_final: 144.22 @ 215K, eval_peak: 408.79 @ 125K\n\n**exp_051_stackcube_frozen_dt_emb_s0** — status: DONE, conclusion: success\n- ve_ratio_peak: 4.3 @ 42.5K, ve_ratio_final: 0.122 @ 212.5K\n- eval_final: 45.31 @ 212.5K, eval_peak: 45.31\n- (no nve fields)\n\n**exp_053_peginsertion_frozen_s0** — status: DONE, conclusion: success, metrics: {}\n\n**exp_054_pickcube_frozen_s0** — status: DONE, conclusion: success, metrics: {}\n\n**exp_056_peginsertion_frozen_s1** — status: DONE, conclusion: success\n- ve_ratio_peak: 11.321 @ 82.5K, ve_ratio_final: 1.193 @ 212.5K\n- nve_classification: burst\n- eval_return_peak: 24.42 @ 132.5K, eval_return_final: 4.37 @ 212.5K\n- Note: Frozen s1 burst 11.32 > trained s1 peak 3.08 — frozen does NOT suppress ManiSkill transients\n\n**exp_057_frozen_dt_emb_walker_s2** — status: DONE, conclusion: success\n- nve_peak: 1.88 @ 115K, nve_classification: transient\n- ve_ratio_peak: 1.283 @ 115K, ve_ratio_final: 0.177 @ 215K\n- Note: NVE=1.88× (raw 1.283 / baseline 0.683 @115K). Walker frozen n=3: s0=0.19, s1=1.71, s2=1.88 — all transient, no sustained CIVO.\n\n**exp_058_frozen_dt_emb_cheetah_s1** — status: DONE, conclusion: success\n- nve_peak: 0.78 @ 45K, nve_classification: no_civo\n- ve_ratio_peak: 0.231 @ 45K, ve_ratio_final: 0.107 @ 215K\n- eval_return_final: 80.46 @ 215K, eval_return_peak: 191.74 @ 25K\n- Note: Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen stably blocks extreme CIVO (trained NVE 70-108)\n\n---\n\n## 3. Manipulation / PickCube / PegInsertion (11 found)\n\n(Overlaps with categories 1 & 2 above; unique entries below)\n\n**exp_019a_pickcube_baseline** — status: DONE, conclusion: killed, metrics: {}\n\n**exp_019a_v2_pickcube_baseline** — status: DONE, conclusion: success\n- eval_return_final: 69.43, eval_return_peak: 69.7 @ 162.5K\n- value_mean_final: 143.4, ve_ratio_final: 2.07, ve_ratio_range: 1.05-3.56\n- steps_completed: 200248\n\n**exp_031_tcn_pickcube_s0_sigma02** — status: DONE, conclusion: negative\n- ve_ratio_peak: 3.71, ve_ratio_latest: 0.18\n- eval_peak: 28.6 @ 162.5K\n- gate_dt2_frac: 1.0, gate_entropy: 0\n- (no explicit nve field)\n\n**exp_031b_tcn_pickcube_s0_sigma05** — status: DONE, conclusion: negative\n- nve_peak: 3.3 @ 42.5K, nve_final: 0.2, nve_suppressed_from_step: 72500\n- eval_reward_peak: 29.1, eval_reward_final: 25.5\n\n**exp_036_dual_critic_pickcube** — status: DONE, conclusion: negative\n- nve_peak: 2.3, nve_final: 0.2, civo_alert: 0\n- eval_return_final: 27.7, eval_return_peak: 27.7\n- gate_dt_2_frac: 1\n\n---\n\n## 4. Walker Baseline Experiments (specifically requested 3)\n\n**exp_009d_baseline_walker_s0** — status: DONE, conclusion: success\n- eval_return: 927.6 @ 508K\n- eval_return_peak: 950.96 @ 398K\n- step: 508000\n\n**exp_009d_baseline_walker_s1** — status: DONE, conclusion: killed, metrics: {}\n\n**exp_009a_baseline_walker_s2** — status: DONE, conclusion: success\n- eval_return_peak: 966.94 @ 395K, final_eval_return: 957.87 @ 505K\n- final_value_mean: 665.17, final_ve_ratio: 0.694\n- last10_mean: 947.19, n_evals: 51, total_steps: 505000\n- ve_stable_range: 0.69-0.72 from 235K+\n- vs_exp001 comparisons: peak 966.94 vs 970.41 (-0.4%), final 957.87 vs 970.41 (-1.3%), last10 947.19 vs 950.90 (-0.4%)\n\n---\n\n## 5. Cheetah Baseline Experiments\n\nNamed \"cheetah_baseline\" specifically: **exp_023a_cheetah_baseline_s0**, **exp_023b_cheetah_baseline_s1**, **exp_023_cheetah_baseline_s2**, **exp_023_cheetah_baseline_s3**, **exp_023_cheetah_baseline_s4**, **exp_023_cheetah_baseline_s4_extended**, **exp_010a_cheetah_baseline_s1**\n\n**exp_023a_cheetah_baseline_s0** — conclusion: success\n- eval_return_final: 624.7, eval_return_peak: 624.7 @ 205K, civo: false\n\n**exp_023b_cheetah_baseline_s1** — conclusion: success\n- eval_return_final: 520.3, eval_return_peak: 572.9 @ 195K\n- ve_ratio_range: 0.5-0.7, civo: false\n\n**exp_023_cheetah_baseline_s2** — conclusion: success\n- eval_return_final: 645.4 @ 205K\n- Note: \"Third baseline seed for NVE normalization.\"\n\n**exp_023_cheetah_baseline_s3** — conclusion: success\n- eval_return_202k: 642.13, peak_eval: 685.93 @ 172K\n- value_mean_final: 445.42, ve_ratio_final: 0.694\n\n**exp_023_cheetah_baseline_s4** — conclusion: success\n- eval_return_194k: 537.03, eval_return_204k: 301.69\n- peak_eval: 537.03 @ 194K, ve_ratio_204k: 1.124\n\n**exp_023_cheetah_baseline_s4_extended** — conclusion: success\n- eval_302k: 580, eval_peak_ext: 642.3 @ 272K\n- Note: extended to 300K confirms non-collapse; 194K→204K drop was transient fluctuation.\n\n**exp_010a_cheetah_baseline_s1** — conclusion: success\n- eval_return_final: 849.8 @ 515K, eval_return_peak: 849.8 @ 515K\n- final_step: 524K, train_return_last: 716\n\nAlso cheetah-related baselines with NVE:\n- **exp_008a_cheetah_unexposed_s0**: nve_105k: 0.49, eval_return_105k: 532.35, ve_ratio_105k: 0.3193\n- **exp_008a_cheetah_unexposed_s1**: nve_105k: 0.478, eval_return_105k: 504.38, ve_ratio_105k: 0.3112\n\n---\n\n## 6. exp_057 and exp_058\n\n**exp_057** → **exp_057_frozen_dt_emb_walker_s2** (full details in section 2 above)\n- nve_peak: 1.88 @ 115K, nve_classification: transient\n- ve_ratio_peak: 1.283, ve_ratio_final: 0.177\n- Walker frozen n=3 summary: s0=0.19, s1=1.71, s2=1.88\n\n**exp_058** → **exp_058_frozen_dt_emb_cheetah_s1** (full details in section 2 above)\n- nve_peak: 0.78 @ 45K, nve_classification: no_civo\n- ve_ratio_peak: 0.231, ve_ratio_final: 0.107\n- eval_return_final: 80.46, eval_return_peak: 191.74\n\n---\n\n## 7. \"Frozen\" in experiment name — 10 experiments\n\nSame list as section 2 above: exp_015b_frozen_dt_emb, exp_042_frozen_dt_emb_walker, exp_046_frozen_dt_emb_cheetah, exp_047_frozen_dt_emb_walker_s1, exp_051_stackcube_frozen_dt_emb_s0, exp_053_peginsertion_frozen_s0, exp_054_pickcube_frozen_s0, exp_056_peginsertion_frozen_s1, exp_057_frozen_dt_emb_walker_s2, exp_058_frozen_dt_emb_cheetah_s1.\n\n---\n\n## 8. All Experiments with NVE in Metrics/Conclusion (58 found)\n\nConsolidated NVE values table (key experiments):\n\n| exp_id | nve_peak | nve_peak_step | nve_final | classification |\n|--------|----------|---------------|-----------|----------------|\n| exp_008a_cheetah_unexposed_s0 | — | — | 0.49 (nve_105k) | — |\n| exp_008a_cheetah_unexposed_s1 | — | — | 0.478 (nve_105k) | — |\n| exp_008d_civo_trigger_s3 | 1.53 | 105K | 1.53 | late-onset collapse |\n| exp_008e_v3_s3 | 4.02 | 105K | — | (corrected from 5.00) |\n| exp_008e_v3_s4 | 0.99 | 95K | — | no CIVO |\n| exp_008e_v3_walker_s2 | 3.78 | 105K | 3.78 | confirmed collapse |\n| exp_008f_s3_no_dt_embed_walker | < 1.5 | — | — | no collapse |\n| exp_008f_s4 | 1.41 | 85K | 0.58 (105K) | transient |\n| exp_009b_008d_walker_s2 | 2.05 | 25K | 0.38 | self-corrected |\n| exp_009c_s3 | — | — | 0.52 (105K) | no CIVO |\n| exp_009e_008d_walker_s1 | 4.12 | 55K | 1.57 | sustained CIVO |\n| exp_010b_cheetah_civo_trigger | 8.27 | 65K | — | civo |\n| exp_010b_cheetah_civo_trigger_s0 | 70.64 (105K) | — | — | extreme CIVO |\n| exp_015b_frozen_dt_emb | 0.467 | 85K | 0.42 (105K) | under-estimates |\n| exp_016e_sgs_walker_s1 | 10.42 | 95K | — | catastrophic |\n| exp_018_full_sgs_walker_s1 | 0.72 | 75K | — | no CIVO |\n| exp_018v2_full_sgs_walker_s1 | 1.66 | 95K | 1.34 | late collapse |\n| exp_019b_pickcube_civo_trigger | 3.78 | 52.5K | 0.065 | transient then collapse |\n| exp_020_vanilla_dreamerv3_s2 | — | — | — | parent_nve_105K: 3.78 (reference) |\n| exp_021_full_sgs_cheetah_s1 | 9.94 | 45K | 0.338 (55K-105K avg) | transient self-correcting |\n| exp_022b_no_curriculum | 1.22 (peak) | — | — | no CIVO alert |\n| exp_023_cheetah_baseline_s2 | — | — | — | note: NVE normalization baseline |\n| exp_024b_cheetah_no_dt_emb_s0 | 0.2 | — | — | no CIVO |\n| exp_024b_cheetah_no_dt_emb_s1 | 0.1 | — | — | no CIVO |\n| exp_027_tcn_walker_s0 | 3.965 | 85K | — | breach: 55K(1.68), 65K(1.54), 85K(3.97) |\n| exp_027_tcn_walker_s0_sigma02 | 0.9081 | 95K | 0.0955 | no sustained CIVO |\n| exp_027_tcn_walker_s1 | 1.6367 | 95K | 0.1476 | transient |\n| exp_028_rave_walker_s0 | ~4.09 (ve@95K) | 95K | — | diverged from 55K |\n| exp_029a_tcn_walker_s1_sigma02 | 0.6428 | 55K | 0.1864 | clean |\n| exp_029b_tcn_walker_s2_sigma02 | 2.765 | 105K | — | CIVO onset 65K |\n| exp_029c_tcn_walker_s0_sigma01 | 1.0218 | 95K | 0.1 | transient |\n| exp_029d_tcn_walker_s3_sigma02 | 3.0 | 105K | — | sudden blowup |\n| exp_030a_tcn_cheetah_s0_sigma02 | 1.903 (ve@55K) | 55K | — | possible CIVO |\n| exp_030b_tcn_cheetah_s0_sigma05 | 10.6657 | 55K | 0.1534 | extreme then self-corrected |\n| exp_031b_tcn_pickcube_s0_sigma05 | 3.3 | 42.5K | 0.2 | suppressed from 72.5K |\n| exp_032_dual_critic_walker | 1.1 | 95K | 0.1 | CIVO prevented |\n| exp_032b_dual_critic_walker_s1 | 1.4 | 85K | 0.1 | CIVO suppressed |\n| exp_034 | 1.753 (max_NVE) | — | 0.144 | CIVO not prevented |\n| exp_034_dual_critic_cheetah | baseline_nve_peak: 70.64 | — | — | dual wave CIVO |\n| exp_035_narrow_dual_critic_walker | 2.75 | 85K | 0.066 | CIVO recovery |\n| exp_036_dual_critic_pickcube | 2.3 | — | 0.2 | negative |\n| exp_037_wide_critic_cheetah | 3.6 | — | 0.1 | negative |\n| exp_038_dual_critic_walker_s2 | 0.3 | — | 0.248 | CIVO prevented, non-CIVO collapse |\n| exp_039_narrow_dual_critic_walker_s1 | 2.19 | — | — | CIVO recovery confirmed |\n| exp_041_dual_critic_walker_s3 | 1.5 | — | 0.1 | CIVO prevented |\n| exp_042_frozen_dt_emb_walker | 0.194 | — | 0.051 | no CIVO |\n| exp_043_008f_walker_s1 | 0.808 | 105K | 0.123 | no CIVO |\n| exp_045_treatment_extension_008d_s3 | 4.91 | 132K | 0.052 | self-corrected @142K |\n| exp_046_frozen_dt_emb_cheetah | 1.35 | 45K | 0.17 | no alert |\n| exp_047_frozen_dt_emb_walker_s1 | 1.71 | 95K | 0.56 (105K) | transient |\n| exp_048_cheetah_civo_extension | 70.64 (initial) / 36.76 (secondary) | — | 2.75 | not self-corrected |\n| exp_055_peginsertion_civo_trigger_s1 | — (nve_classification: transient) | — | — | ve_ratio_peak: 3.08 |\n| exp_056_peginsertion_frozen_s1 | — (nve_classification: burst) | — | — | ve_ratio_peak: 11.321 |\n| exp_057_frozen_dt_emb_walker_s2 | 1.88 | 115K | — | transient |\n| exp_058_frozen_dt_emb_cheetah_s1 | 0.78 | 45K | — | no_civo |\n| exp_001_baseline_s2_extended | — | — | — | ve_ratio_at_105K: 0.7422 |\n| exp_001_baseline_s4_extended | — | — | — | no NVE values stored |\n\n---\n\n**Key summary for paper audit:**\n\n- Walker baseline (exp_009a_baseline_walker_s2): final 957.87, peak 966.94, last10_mean 947.19\n- Walker baseline (exp_009d_baseline_walker_s0): final 927.6, peak 950.96\n- Cheetah baselines: s0=624.7, s1=520.3 (peak 572.9), s2=645.4, s3=642.13 (peak 685.93)\n- Frozen Walker n=3 NVE: s0=0.194, s1=1.71, s2=1.88 — all transient, no sustained CIVO\n- Frozen Cheetah n=2 NVE: s0=1.35, s1=0.78 — both no_civo, blocks trained CIVO (70–108×)\n- Cheetah trained CIVO: exp_010b_cheetah_civo_trigger nve_peak=8.27; exp_010b_cheetah_civo_trigger_s0 nve_105K=70.64\n- PegInsertion trained cross-seed: s0 ve_ratio_peak=10.05, s1 ve_ratio_peak=3.08\n- PegInsertion frozen cross-seed: s0 metrics={} (no data), s1 ve_ratio_peak=11.321 (burst)\n- exp_057 and exp_058 both exist (frozen walker s2 and frozen cheetah s1 respectively)"
      }
    ],
    "totalDurationMs": 174456,
    "totalTokens": 102943,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4759,
      "cache_read_input_tokens": 91229,
      "output_tokens": 6954,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4759
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6954,
          "cache_read_input_tokens": 91229,
          "cache_creation_input_tokens": 4759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4759,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 11,
      "searchCount": 0,
      "bashCount": 1,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### System

_source line 133_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a00056aa23f532ed4",
  "tool_use_id": "toolu_015tp1CEMzPpFQ1WtejthEt9",
  "status": "completed",
  "output_file": "",
  "summary": "Extract paper quantitative claims",
  "usage": {
    "total_tokens": 62379,
    "tool_uses": 18,
    "duration_ms": 266412
  },
  "uuid": "ddc634a7-f900-4a80-a3b7-3d6d19676d09",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84"
}
```

---
