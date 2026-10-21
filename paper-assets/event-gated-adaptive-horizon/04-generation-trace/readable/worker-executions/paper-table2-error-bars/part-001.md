# paper table2 error bars — Part 1 of 2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

[Transcript overview](../paper-table2-error-bars.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/a0/a0597f58d1c8194e9a23.json)

## Before a recorded user message

## Before a recorded user message

33 recorded events


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
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "b6162002-aed6-4c66-9b7a-3474d550cac1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1780022400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e31a284e-12de-4ad8-8370-d1c203ffc3e9",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task. I need to:
1. Read the registry to get all DONE experiments
2. Map them to Table 2 rows
3. Calculate mean±std for eval_return
4. Edit the table in the LaTeX file
5. Compile and verify

Let me begin by reading the registry and the current table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "acf925ec-672d-40ee-a5e1-c71fa8db0343",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2xJMU4cQyax7K3WLiV281",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12429,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12429
      },
      "output_tokens": 36,
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

先读取 registry 和当前表格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "bd4b4d22-3daf-4846-b4c2-7e2e2fad5b89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2xJMU4cQyax7K3WLiV281",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12429,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12429
      },
      "output_tokens": 36,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0114X75AHmKuHv2HP6KYq6UW`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ad4083f1-ad99-4de6-bda7-ee91317b4e68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2xJMU4cQyax7K3WLiV281",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12429,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12429
      },
      "output_tokens": 36,
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

_source line 7 · 2026-05-29T00:34:20.584Z_

<details><summary>↩ Tool result · `toolu_0114X75AHmKuHv2HP6KYq6UW`</summary>

````text
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
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "0fe74119-564c-48fd-ad26-cb7b08636cea",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01JX9RXCDmaW6GwtGX8TK4Wh`</summary>

```json
{
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "*"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "02bad95e-7038-4e09-8966-03928ac5855c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kXeQeZuaw98mFsJ8UZh4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 24274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 553
      },
      "output_tokens": 66,
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

_source line 9 · 2026-05-29T00:34:24.043Z_

<details><summary>↩ Tool result · `toolu_01JX9RXCDmaW6GwtGX8TK4Wh`</summary>

```text
&lt;persisted-output>
Output too large (55.5KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/toolu_01JX9RXCDmaW6GwtGX8TK4Wh.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_walker_no_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T11:10:24.895Z\", \"updated_at\": \"2026-05-27T11:14:46.202Z\", \"parent\": \"exp_008f\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-51268\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"105000 steps\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"checkpoint_source\": \"none (train from scratch)\", \"eval_data\": \"dmc_walker_walk (built-in env)\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-27T11:14:46.202Z\"}, \"exp_hopper_frozen_s0_ext\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T10:47:14.544Z\", \"updated_at\": \"2026-05-27T10:48:10.979Z\", \"conclusion\": \"negative\", \"metrics\": {\"eval_return_final\": 0.56, \"eval_return_peak\": 3.58, \"eval_return_peak_step\": 85000, \"ve_ratio_final\": 15.08, \"ve_ratio_peak\": 4335664.27, \"ve_ratio_peak_step\": 105000, \"value_mean_final\": 8.46, \"civo_alerts\": 2, \"civo_alert_steps\": [65000, 105000], \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"total_steps\": 160000, \"recovery\": false}, \"spec\": {\"checkpoint_path\": \"logdir/exp_hopper_frozen_s0/latest.pt\", \"log_path\": \"logdir/exp_hopper_frozen_s0/metrics.jsonl\", \"command\": \"python train.py --config hopper_frozen_s0 --steps 160000\", \"server\": \"westd-51268\", \"data_path\": \"Hopper-v4\", \"dat
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ff2b701f-957c-4324-a942-c09920248ab1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_walker_no_dt_emb_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T11:10:24.895Z\\\", \\\"updated_at\\\": \\\"2026-05-27T11:14:46.202Z\\\", \\\"parent\\\": \\\"exp_008f\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"105000 steps\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"none (train from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (built-in env)\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-27T11:14:46.202Z\\\"}, \\\"exp_hopper_frozen_s0_ext\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T10:47:14.544Z\\\", \\\"updated_at\\\": \\\"2026-05-27T10:48:10.979Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 0.56, \\\"eval_return_peak\\\": 3.58, \\\"eval_return_peak_step\\\": 85000, \\\"ve_ratio_final\\\": 15.08, \\\"ve_ratio_peak\\\": 4335664.27, \\\"ve_ratio_peak_step\\\": 105000, \\\"value_mean_final\\\": 8.46, \\\"civo_alerts\\\": 2, \\\"civo_alert_steps\\\": [65000, 105000], \\\"gate_dt_mean\\\": 2, \\\"gate_entropy\\\": 0, \\\"total_steps\\\": 160000, \\\"recovery\\\": false}, \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_hopper_frozen_s0/latest.pt\\\", \\\"log_path\\\": \\\"logdir/exp_hopper_frozen_s0/metrics.jsonl\\\", \\\"command\\\": \\\"python train.py --config hopper_frozen_s0 --steps 160000\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"data_path\\\": \\\"Hopper-v4\\\", \\\"data_count\\\": 160000, \\\"model_name\\\": \\\"dreamer_v3_frozen_dt_emb\\\", \\\"seed\\\": 0}, \\\"hypothesis\\\": \\\"Extending frozen_s0 from 105K to 150K will show eval_return recovery with ve_ratio declining, confirming frozen_s0's degenerate CIVO at 95K is transient instability during severe learning delay rather than a permanent structural failure caused by the frozen dt_embedding.\\\", \\\"completed_at\\\": \\\"2026-05-27T10:48:10.979Z\\\"}, \\\"exp_hopper_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T05:51:24.680Z\\\", \\\"updated_at\\\": \\\"2026-05-27T05:52:01.157Z\\\", \\\"metrics\\\": {\\\"step\\\": 105000, \\\"eval_final\\\": 96.43, \\\"eval_return_trajectory\\\": {\\\"5000\\\": 0.06, \\\"15000\\\": 1.04, \\\"25000\\\": 1.7, \\\"35000\\\": 6.55, \\\"45000\\\": 19.09, \\\"55000\\\": 22.52, \\\"65000\\\": 3.5, \\\"75000\\\": 62.2, \\\"85000\\\": 67.62, \\\"95000\\\": 86.47, \\\"105000\\\": 96.43}, \\\"ve_ratio_trajectory\\\": {\\\"15000\\\": 0.08, \\\"25000\\\": 0.098, \\\"35000\\\": 0.166, \\\"45000\\\": 0.19, \\\"55000\\\": 0.279, \\\"65000\\\": 3.479, \\\"75000\\\": 0.341, \\\"85000\\\": 0.502, \\\"95000\\\": 0.517, \\\"105000\\\": 0.559}, \\\"nve_peak\\\": 3.48, \\\"nve_peak_step\\\": 65000, \\\"nve_final\\\": 0.559, \\\"civo_onset\\\": false, \\\"civo_alert_count\\\": 0, \\\"value_mean_final\\\": 53.9, \\\"target_mean_final\\\": 54.2, \\\"training_steps\\\": 105000, \\\"update_count\\\": 25099, \\\"fps\\\": 11}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_baseline/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_hopper_baseline.log\\\", \\\"hypothesis\\\": \\\"Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE < 1.5×). Source: C1/C2 third-environment verification (D160).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"data_path\\\": \\\"dmc_hopper_hop\\\", \\\"data_count\\\": 105000, \\\"model_name\\\": \\\"DreamerV3 baseline (dt=1, no gate)\\\", \\\"seed\\\": 0}, \\\"completed_at\\\": \\\"2026-05-27T05:52:01.157Z\\\"}, \\\"exp_097_cheetah_008d_s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T03:03:25.871Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:32:48.497Z\\\", \\\"hypothesis\\\": \\\"C1 trigger seed 3: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 Cheetah 上的第四个 seed（s3）。当前 onset rate 2/3（s0 NVE=4.1×✓, s1 NVE=0.517✗, s2 NVE=138.7×✓）。s3 完成后可计算完整 onset rate（n=4）。如果 onset ≥3/4 → 高 onset rate 支持 CIVO 是 systematic phenomenon；如果 2/4 → 50% onset rate 仍有意义但需讨论。\\\", \\\"parent\\\": \\\"exp_078_cheetah_008d_s0\\\", \\\"notes\\\": \\\"重新提交到 westd-51268 cuda:0。原 bjb1 提交 (PID 324959) 已死（服务器无卡）。exp_094 同配置在 westd 跑了 1.72h 后因 SSH 断连失败，检查其 checkpoint 是否可复用。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_097_cheetah_008d_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\\\\\"\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 3794, \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": 105000, \\\"model_name\\\": \\\"DreamerV3+FixedDt2_Subsample_H8 (trained dt_emb)\\\", \\\"seed\\\": 3, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_097_cheetah_008d_s3/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_097_cheetah_008d_s3/latest.pt\\\"}, \\\"metrics\\\": {\\\"step\\\": 105000, \\\"nve_peak\\\": 2.3, \\\"nve_peak_step\\\": 45000, \\\"nve_final\\\": 0.3, \\\"civo_onset\\\": true, \\\"civo_onset_step\\\": 45000, \\\"civo_pattern\\\": \\\"transient→degraded\\\", \\\"eval_final\\\": 61.7, \\\"eval_final_pct_baseline\\\": -86, \\\"baseline_eval_return\\\": 446.1, \\\"gate_dt_2_frac\\\": 1}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-26T11:32:48.497Z\\\"}, \\\"exp_100_walker_008a_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T03:39:24.456Z\\\", \\\"updated_at\\\": \\\"2026-05-26T07:52:52.927Z\\\", \\\"hypothesis\\\": \\\"Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 Walker 008a 第 2 seed。与 exp_008a_no_subsample_dt2 (s0) 和 exp_074_008a_walker_s3 (s3) 共同建立 C3 value suppression 多 seed 证据。训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练，预期无 CIVO。plan_013。\\\", \\\"parent\\\": \\\"exp_008a_no_subsample_dt2\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_100_walker_008a_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\\\\\"\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 5591, \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 105000, \\\"model_name\\\": \\\"DreamerV3+FixedDt2_NoSubsample (trained dt_emb, unexposed)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_100_walker_008a_s1/metrics.jsonl\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_100_walker_008a_s1/latest.pt\\\"}, \\\"metrics\\\": {\\\"step\\\": 105000, \\\"eval_return_trajectory\\\": {\\\"5000\\\": 31, \\\"15000\\\": 168.77, \\\"25000\\\": 158.03, \\\"35000\\\": 202.91, \\\"45000\\\": 305.98, \\\"55000\\\": 457.28, \\\"65000\\\": 628.82, \\\"75000\\\": 686.98, \\\"85000\\\": 656.64, \\\"95000\\\": 717.74, \\\"105000\\\": 750.59}, \\\"ve_ratio_trajectory\\\": {\\\"15000\\\": 0.035, \\\"25000\\\": 0.206, \\\"35000\\\": 0.279, \\\"45000\\\": 0.261, \\\"55000\\\": 0.248, \\\"65000\\\": 0.234, \\\"75000\\\": 0.26, \\\"85000\\\": 0.315, \\\"95000\\\": 0.325, \\\"105000\\\": 0.328}, \\\"value_mean_trajectory\\\": {\\\"15000\\\": 5.98, \\\"25000\\\": 32.58, \\\"35000\\\": 56.55, \\\"45000\\\": 79.94, \\\"55000\\\": 113.33, \\\"65000\\\": 147.14, \\\"75000\\\": 178.73, \\\"85000\\\": 206.95, \\\"95000\\\": 233.17, \\\"105000\\\": 246.06}, \\\"nve_peak\\\": 0.328, \\\"nve_final\\\": 0.328, \\\"civo_onset\\\": false, \\\"eval_final\\\": 750.59, \\\"eval_final_pct_baseline\\\": -18, \\\"baseline_eval_return\\\": 915.67, \\\"gate_dt_mean\\\": 2, \\\"gate_dt_2_frac\\\": 1}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-26T07:52:45.733Z\\\", \\\"notes\\\": \\\"C3 Walker 008a s1 完成。训练正常结束(105K steps)。eval_return@105K=750.59 (baseline 915.67, -18.0%)。ve_ratio 全程 0.035-0.328，NVE_peak=0.328，远低于 τ=1.5×，civo/alert 全程 0.0，无 CIVO onset。Value suppression 确认（value_mean 持续低于 eval_return）。与 parent s0 (eval@105K=777.66, -15.1%, ve_ratio 0.37-0.54) 一致：s1 性能略低但趋势相同，两个 seed 均无 CIVO 且呈现 value suppression，C3 Walker 008a 2-seed 证据闭合。gate_dt 全程固定为 2.0 (100% dt_2_frac)，符合 gate_fixed_dt=2 配置。\\\"}, \\\"rssm_fidelity_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T03:47:46.584Z\\\", \\\"updated_at\\\": \\\"2026-05-26T03:47:59.871Z\\\", \\\"hypothesis\\\": \\\"RSSM fidelity v2 分析：对比 4 类模型（baseline/trained_dt_emb/no_dt_emb/frozen）在 dt=1 vs dt=2 下的 observation/reward reconstruction loss。使用 Walker checkpoint (n=800)。结果：trained_dt_emb reward ratio 1.50×, obs ratio 1.44×; baseline obs ratio 1.55×; no_dt_emb gap 最小 (1.23×/1.16×)。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python analyze_rssm_fidelity_v2.py --device cuda:0\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"data_path\\\": \\\"Walker logdirs (exp_008d/009d/009c/084)\\\", \\\"data_count\\\": 800, \\\"model_name\\\": \\\"RSSM fidelity analysis v2\\\", \\\"seed\\\": 0, \\\"checkpoint_path\\\": \\\"analysis_rssm_fidelity_v2.json\\\", \\\"log_path\\\": \\\"N/A (analysis task)\\\"}, \\\"completed_at\\\": \\\"2026-05-26T03:47:59.871Z\\\"}, \\\"exp_057_frozen_dt_emb_walker_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T15:26:00.391Z\\\", \\\"updated_at\\\": \\\"2026-05-26T03:03:45.406Z\\\", \\\"hypothesis\\\": \\\"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\\\", \\\"parent\\\": \\\"exp_042_frozen_dt_emb_walker\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 157775, \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Walker s2)\\\", \\\"seed\\\": 2, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"log_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"checkpoint_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"failure_reason\\\": \\\"bjb1-45299 server lost GPU allocation, experiment terminated\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-26T03:03:45.406Z\\\"}, \\\"exp_051_stackcube_frozen_dt_emb_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T18:42:39.309Z\\\", \\\"updated_at\\\": \\\"2026-05-26T03:03:44.692Z\\\", \\\"hypothesis\\\": \\\"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks\\\", \\\"parent\\\": \\\"exp_049\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 305974, \\\"data_path\\\": \\\"maniskill_StackCube-v1 (online RL)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, StackCube s0)\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"maniskill_StackCube-v1 (online eval)\\\", \\\"checkpoint_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"failure_reason\\\": \\\"bjb1-45299 server lost GPU allocation, experiment terminated\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-26T03:03:44.692Z\\\"}, \\\"exp_049_stackcube_civo_trigger_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T17:14:38.578Z\\\", \\\"updated_at\\\": \\\"2026-05-26T03:03:42.946Z\\\", \\\"hypothesis\\\": \\\"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion（Walker/Cheetah）推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack），比 PickCube 更难。如果触发 CIVO → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\\\", \\\"parent\\\": \\\"exp_048_stackcube_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 91395, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"checkpoint_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"failure_reason\\\": \\\"bjb1-45299 server lost GPU allocation, experiment terminated\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-26T03:03:42.946Z\\\"}, \\\"exp_081_008e_v3_walker_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T15:42:24.765Z\\\", \\\"updated_at\\\": \\\"2026-05-25T15:43:10.949Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_return_105K\\\": 597.1, \\\"vs_baseline\\\": \\\"-34.8%\\\", \\\"vs_baseline_pct\\\": 65.2, \\\"baseline_105K\\\": 915.67, \\\"ve_ratio_peak\\\": 0.6, \\\"ve_ratio_final\\\": 0.5, \\\"NVE_est_peak\\\": 0.8, \\\"NVE_est_final\\\": 0.7, \\\"gate_dt_mean\\\": 1, \\\"gate_dt_1_frac\\\": 1, \\\"civo_alert_count\\\": 0, \\\"training_steps\\\": 105000, \\\"update_count\\\": 25099, \\\"value_mean_final\\\": 295}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_081_008e_v3_walker_s2/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --config 008e_v3 --env walker_walk --seed 2\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3_008e_v3\\\", \\\"seed\\\": 2}, \\\"hypothesis\\\": \\\"Trained dt_emb with dt=1 imagination and subsample ON (max_dt=2) does not trigger CIVO in Walker Walk, as the value function sees only single-step predictions that match the world model's training distribution, preventing value inflation even with learned temporal embeddings.\\\", \\\"completed_at\\\": \\\"2026-05-25T15:43:10.949Z\\\"}, \\\"exp_073_008f_walker_s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T09:52:07.413Z\\\", \\\"updated_at\\\": \\\"2026-05-25T09:52:34.845Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 289.3, \\\"eval_return_peak\\\": 486.5, \\\"eval_return_peak_step\\\": 75000, \\\"ve_ratio_max\\\": 0.5, \\\"civo_alert_max\\\": 0, \\\"gate_dt_mean\\\": 2, \\\"gate_dt_2_frac\\\": 1, \\\"gate_empirical_entropy\\\": 0, \\\"total_env_steps\\\": 112000, \\\"total_updates\\\": 25099}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_073_008f_walker_s4/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --config 008f --seed 4\\\", \\\"server\\\": \\\"westd-19154\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_v3_008f\\\", \\\"seed\\\": 4}, \\\"hypothesis\\\": \\\"Removing dt_embedding (dt_embed_dim=0) in the 008f control config prevents CIVO onset because the agent cannot form temporally-conditioned value predictions that compound imagination-driven overestimation. With fixed dt=2 and no temporal embedding, value error ratio should remain below the 1.5x CIVO threshold across seeds.\\\", \\\"completed_at\\\": \\\"2026-05-25T09:52:34.845Z\\\"}, \\\"exp_069_008f_walker_repro_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T07:20:25.632Z\\\", \\\"updated_at\\\": \\\"2026-05-25T07:21:13.407Z\\\", \\\"hypothesis\\\": \\\"Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk. With no learned temporal embedding, the value network cannot develop the compounding overestimation pattern that causes CIVO collapse. This seed=1 run extends the evidence from exp_008f (seed=0).\\\", \\\"parent\\\": \\\"exp_008f_no_dt_embed_subsample_on_h8\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs dmc_vision --task dmc_walker_walk --seed 1 --logdir logdir/exp_069_008f_walker_repro_s1\\\", \\\"server\\\": \\\"westd-19154\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv2_no_dt_embed_h8\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"dmc_walker_walk_online\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_069_008f_walker_repro_s1/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T07:20:58.159Z\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 237.8, \\\"eval_return_final_step\\\": 105000, \\\"eval_return_peak\\\": 390.1, \\\"eval_return_peak_step\\\": 95000, \\\"steps_completed\\\": 112000, \\\"eval_steps\\\": 105000, \\\"civo_triggered\\\": false, \\\"civo_alert_count\\\": 0, \\\"ve_ratio_max\\\": 0.447, \\\"ve_ratio_max_step\\\": 105000, \\\"ve_ratio_final\\\": 0.447, \\\"gate_dt_mean\\\": 2, \\\"gate_dt_2_frac\\\": 1, \\\"gate_empirical_entropy\\\": 0, \\\"value_mean_final\\\": 106.3, \\\"target_mean_final\\\": 106.4, \\\"value_loss_final\\\": 0.99, \\\"seed\\\": 1, \\\"eval_return_trajectory\\\": {\\\"5K\\\": 30.5, \\\"15K\\\": 158.7, \\\"25K\\\": 180.8, \\\"35K\\\": 250.3, \\\"45K\\\": 293.6, \\\"55K\\\": 272.2, \\\"65K\\\": 328.1, \\\"75K\\\": 244.8, \\\"85K\\\": 382.5, \\\"95K\\\": 390.1, \\\"105K\\\": 237.8}, \\\"ve_ratio_trajectory\\\": {\\\"15K\\\": 0.021, \\\"25K\\\": 0.111, \\\"35K\\\": 0.171, \\\"95K\\\": 0.275, \\\"105K\\\": 0.447}, \\\"note\\\": \\\"C2 causal control: no dt_embedding, fixed dt=2. No CIVO triggered. ve_ratio stayed <0.5 throughout. Late eval dip (390→238) is normal Walker variance, not CIVO-driven (value_mean≈target_mean, no overestimation).\\\"}}, \\\"exp_055_peginsertion_civo_trigger_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T05:16:11.755Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:34:24.080Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PegInsertionSide-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_055_peginsertion_civo_trigger_s1.log\\\"}, \\\"hypothesis\\\": \\\"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，162.5K 时仍 1.94）。如果 s1 也触发持续 CIVO → PegInsertion 是最严重的 CIVO 环境（比 StackCube 自修复更难），支持 severity-dependent narrative；如果不触发 → seed-specific 异常。\\\", \\\"parent\\\": \\\"exp_050_peginsertion_civo_trigger_s0\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_055_peginsertion_civo_trigger_s1/latest.pt\\\", \\\"log_path\\\": \\\"logdir/exp_055_peginsertion_civo_trigger_s1.log\\\", \\\"metrics\\\": {\\\"total_steps\\\": 222400, \\\"ve_ratio_max\\\": 3.08, \\\"ve_ratio_max_step\\\": 92500, \\\"ve_ratio_final\\\": 0.5, \\\"ve_ratio_final_step\\\": 212500, \\\"eval_peak\\\": 24.05, \\\"eval_peak_step\\\": 112500, \\\"eval_final\\\": 11.44, \\\"eval_final_step\\\": 212500, \\\"civo_triggered\\\": true, \\\"civo_self_corrected\\\": \\\"partial\\\", \\\"civo_onset_step\\\": 32500, \\\"civo_peak_step\\\": 92500, \\\"ve_ratio_trajectory\\\": {\\\"12500\\\": 0.19, \\\"22500\\\": 0.81, \\\"32500\\\": 1.35, \\\"42500\\\": 2, \\\"52500\\\": 2.39, \\\"62500\\\": 2.85, \\\"72500\\\": 2.28, \\\"82500\\\": 2.48, \\\"92500\\\": 3.08, \\\"102500\\\": 2.51, \\\"112500\\\": 0.91, \\\"122500\\\": 1.21, \\\"132500\\\": 1.36, \\\"142500\\\": 0.75, \\\"152500\\\": 0.55, \\\"162500\\\": 1.17, \\\"172500\\\": 0.96, \\\"182500\\\": 0.94, \\\"192500\\\": 0.9, \\\"202500\\\": 0.73, \\\"212500\\\": 0.5}, \\\"eval_trajectory\\\": {\\\"2500\\\": 2.01, \\\"12500\\\": 10.12, \\\"22500\\\": 11.47, \\\"32500\\\": 12.01, \\\"42500\\\": 10.13, \\\"52500\\\": 10.31, \\\"62500\\\": 9.02, \\\"72500\\\": 10.07, \\\"82500\\\": 8.78, \\\"92500\\\": 7.24, \\\"102500\\\": 9.2, \\\"112500\\\": 24.05, \\\"122500\\\": 16.46, \\\"132500\\\": 13.15, \\\"142500\\\": 20.44, \\\"152500\\\": 23.4, \\\"162500\\\": 9.07, \\\"172500\\\": 9.46, \\\"182500\\\": 8.51, \\\"192500\\\": 7.81, \\\"202500\\\": 8.58, \\\"212500\\\": 11.44}, \\\"note\\\": \\\"CIVO triggered (ve_ratio 3.08@92.5K), less severe than s0 (10.05). Partial self-correction to 0.50 by 212.5K. Eval poor throughout (~10-24), PegInsertion is hard task.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T23:34:24.080Z\\\"}, \\\"exp_048_cheetah_civo_extension\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:30:40.050Z\\\", \\\"updated_at\\\": \\\"2026-05-22T21:17:46.852Z\\\", \\\"hypothesis\\\": \\\"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → \\\\\\\"severity determines recoverability\\\\\\\" narrative, strongest paper defense. If it does → CIVO is universally transient regardless of severity.\\\", \\\"parent\\\": \\\"exp_010b_cheetah_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 88654, \\\"data_path\\\": \\\"dmc_cheetah_run (online RL)\\\", \\\"data_count\\\": 300000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_048_cheetah_civo_extension/train.log\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 23.423, \\\"eval_peak\\\": 32.835, \\\"eval_peak_step\\\": 252000, \\\"ve_ratio_initial_measured\\\": 6.135, \\\"ve_ratio_initial_measured_step\\\": 122000, \\\"ve_ratio_inherited_from_exp010b\\\": 46.34, \\\"ve_ratio_peak_in_run\\\": 24.112, \\\"ve_ratio_peak_step\\\": 162000, \\\"ve_ratio_final\\\": 1.803, \\\"nve_inherited\\\": 70.64, \\\"nve_peak_in_run\\\": 36.76, \\\"nve_final\\\": 2.75, \\\"baseline_ve_ratio\\\": 0.656, \\\"total_steps\\\": 312000, \\\"last_eval_step\\\": 302000, \\\"civo_self_corrected\\\": \\\"partial\\\", \\\"civo_reduction_pct\\\": 96.1, \\\"civo_correction_duration_steps\\\": 197000, \\\"gate_collapsed\\\": true, \\\"gate_dt_final\\\": 2, \\\"gate_dt_2_frac_final\\\": 1}, \\\"checkpoint_path\\\": \\\"logdir/exp_048_cheetah_civo_extension/checkpoint_302000.pt\\\", \\\"log_path\\\": \\\"logdir/exp_048_cheetah_civo_extension/train.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T21:17:46.852Z\\\"}, \\\"exp_047_frozen_dt_emb_walker_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:42:12.914Z\\\", \\\"updated_at\\\": \\\"2026-05-22T19:01:30.894Z\\\", \\\"hypothesis\\\": \\\"Freezing dt_emb in Walker Walk (seed 1) prevents sustained CIVO collapse, replicating exp_042 (seed 0, NVE=0.19) finding that removing dt conditioning blocks the overestimation feedback loop\\\", \\\"parent\\\": \\\"exp_042_frozen_dt_emb_walker\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 282452, \\\"data_path\\\": \\\"dmc_walker_walk (online RL)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Walker s1)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\\\"}, \\\"metrics\\\": {\\\"eval_peak\\\": 408.79, \\\"eval_peak_step\\\": 125000, \\\"eval_final\\\": 144.22, \\\"eval_final_step\\\": 215000, \\\"ve_ratio_peak\\\": 1.099, \\\"ve_ratio_peak_step\\\": 75000, \\\"ve_ratio_final\\\": 0.277, \\\"nve_peak\\\": 1.71, \\\"nve_peak_step\\\": 95000, \\\"nve_final_105k\\\": 0.56, \\\"total_steps\\\": 225000, \\\"note\\\": \\\"Transient NVE>1.5x at 75K-95K with full self-correction by 105K. Late eval decline (408->144) NOT CIVO-driven (ve_ratio=0.28). No sustained collapse.\\\"}, \\\"checkpoint_path\\\": \\\"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\\\", \\\"log_path\\\": \\\"logdir/exp_047_frozen_dt_emb_walker_s1/\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T18:50:46.948Z\\\"}, \\\"exp_046_frozen_dt_emb_cheetah\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:40:43.182Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:32:34.105Z\\\", \\\"hypothesis\\\": \\\"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation. Source: D133 + exp_042 result + R1-N4 cross-environment concern.\\\", \\\"parent\\\": \\\"exp_042_frozen_dt_emb_walker\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 281513, \\\"data_path\\\": \\\"dmc_cheetah_run (online RL)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Cheetah)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_046_frozen_dt_emb_cheetah/train.log\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 150.5, \\\"eval_peak\\\": 207.4, \\\"eval_peak_step\\\": 145000, \\\"ve_ratio_peak\\\": 0.4, \\\"ve_ratio_final\\\": 0.1, \\\"nve_peak\\\": 1.35, \\\"nve_peak_step\\\": 45000, \\\"nve_final\\\": 0.17, \\\"total_steps\\\": 224000, \\\"civo_alert_count\\\": 0, \\\"eval_trajectory\\\": \\\"5K:8.3, 15K:110, 35K:160, 95K:181, 105K:206, 115K:46, 145K:207, 155K:161, 215K:150.5\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T18:31:00.933Z\\\"}, \\\"exp_048_stackcube_civo_trigger_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:44:55.613Z\\\", \\\"updated_at\\\": \\\"2026-05-22T17:14:16.564Z\\\", \\\"hypothesis\\\": \\\"ManiSkill Phase 1 scout: CIVO trigger config (trained dt_emb + subsample ON + H=8) on StackCube-v1 manipulation task. Tests whether CIVO generalizes beyond locomotion (Walker/Cheetah) to manipulation domains. exp_019b showed transient CIVO on PickCube; StackCube is harder (multi-stage). If CIVO triggers → extends cross-domain evidence; if not → supports locomotion-specific scope.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_stackcube_civo_trigger_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 87609, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, ManiSkill)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"/tmp/exp_048.log\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-22T17:14:16.564Z\\\"}, \\\"exp_045_treatment_extension_008d_s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T09:40:52.894Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:44:50.990Z\\\", \\\"hypothesis\\\": \\\"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\\\", \\\"parent\\\": \\\"exp_008d_civo_trigger_s3\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 70945, \\\"data_path\\\": \\\"dmc_walker_walk (online RL)\\\", \\\"data_count\\\": 300000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config)\\\", \\\"seed\\\": 3, \\\"checkpoint_source\\\": \\\"exp_008d_civo_trigger_s3/latest.pt (step 112K)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval, same as training env)\\\", \\\"log_path\\\": \\\"logdir/exp_045_treatment_extension_008d_s3/train.log\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 867.6, \\\"eval_peak\\\": 869.7, \\\"eval_peak_step\\\": 242000, \\\"ve_ratio_final\\\": 0.05, \\\"ve_ratio_peak\\\": 4.91, \\\"ve_ratio_peak_step\\\": 132000, \\\"nve_final\\\": 0.052, \\\"total_steps\\\": 312000, \\\"self_correction_onset\\\": 142000, \\\"finding\\\": \\\"CIVO self-correction: ve_ratio 4.91→0.05, eval 35→868 over 170K steps\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\\\", \\\"completed_at\\\": \\\"2026-05-22T15:44:50.990Z\\\"}, \\\"exp_036_dual_critic_pickcube\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T19:45:02.066Z\\\", \\\"updated_at\\\": \\\"2026-05-21T19:45:46.721Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --task ManiSkill_PickCube-v1 --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 0 --steps 200000\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"ManiSkill_PickCube-v1\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3_dual_critic\\\", \\\"seed\\\": 0}, \\\"hypothesis\\\": \\\"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\\\", \\\"parent\\\": \\\"exp_032_dual_critic_walker\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_036_dual_critic_pickcube\\\", \\\"log_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 212447, \\\"total_env_steps\\\": 212447, \\\"eval_return_final\\\": 27.7, \\\"eval_return_peak\\\": 27.7, \\\"eval_return_peak_step\\\": 202500, \\\"ve_ratio_peak\\\": 2.3, \\\"ve_ratio_peak_step\\\": 32500, \\\"ve_ratio_final\\\": 0.2, \\\"civo_alerts\\\": 0, \\\"v1_v2_max_divergence\\\": 0, \\\"v1_v2_correlated\\\": true, \\\"CIVO_prevented\\\": \\\"vacuous_no_civo_in_baseline\\\", \\\"gate_dt_2_frac\\\": 1, \\\"gate_entropy\\\": 0, \\\"exit_code\\\": 0, \\\"eval_return_trajectory\\\": {\\\"2.5K\\\": 2, \\\"12.5K\\\": 17.5, \\\"22.5K\\\": 17.5, \\\"32.5K\\\": 11.6, \\\"42.5K\\\": 15.6, \\\"52.5K\\\": 11.7, \\\"62.5K\\\": 18.8, \\\"72.5K\\\": 5.4, \\\"82.5K\\\": 22.5, \\\"92.5K\\\": 18.1, \\\"102.5K\\\": 8.4, \\\"112.5K\\\": 7.1, \\\"122.5K\\\": 9.1, \\\"132.5K\\\": 12.8, \\\"142.5K\\\": 14, \\\"152.5K\\\": 13.1, \\\"162.5K\\\": 16.2, \\\"172.5K\\\": 19.7, \\\"182.5K\\\": 16.8, \\\"192.5K\\\": 13.7, \\\"202.5K\\\": 27.7}, \\\"ve_ratio_trajectory\\\": {\\\"12.5K\\\": 0.2, \\\"22.5K\\\": 1, \\\"32.5K\\\": 2.3, \\\"42.5K\\\": 1.4, \\\"52.5K\\\": 1.4, \\\"62.5K\\\": 0.6, \\\"72.5K\\\": 1.6, \\\"82.5K\\\": 0.3, \\\"92.5K\\\": 0.3, \\\"102.5K\\\": 0.6, \\\"112.5K\\\": 0.7, \\\"122.5K\\\": 0.5, \\\"132.5K\\\": 0.4, \\\"142.5K\\\": 0.3, \\\"152.5K\\\": 0.4, \\\"162.5K\\\": 0.3, \\\"172.5K\\\": 0.3, \\\"182.5K\\\": 0.3, \\\"192.5K\\\": 0.4, \\\"202.5K\\\": 0.2}, \\\"value1_mean_trajectory\\\": {\\\"2.5K\\\": 0, \\\"12.5K\\\": 3.8, \\\"22.5K\\\": 17.9, \\\"32.5K\\\": 26.9, \\\"42.5K\\\": 21.2, \\\"52.5K\\\": 16.1, \\\"62.5K\\\": 11.6, \\\"72.5K\\\": 8.7, \\\"82.5K\\\": 7.2, \\\"92.5K\\\": 6, \\\"102.5K\\\": 5.3, \\\"112.5K\\\": 5.1, \\\"122.5K\\\": 5, \\\"132.5K\\\": 4.9, \\\"142.5K\\\": 4.9, \\\"152.5K\\\": 5.3, \\\"162.5K\\\": 5.7, \\\"172.5K\\\": 5.6, \\\"182.5K\\\": 5.6, \\\"192.5K\\\": 5.6, \\\"202.5K\\\": 5.8}, \\\"baseline_comparison\\\": {\\\"exp_019a_v2_vanilla_baseline_final\\\": 58.6, \\\"exp_019b_civo_config_baseline_final\\\": 26.6, \\\"exp_031_tcn_sigma02_final\\\": 17.2, \\\"exp_031b_tcn_sigma05_final\\\": 25.5}, \\\"conclusion_detail\\\": \\\"CIVO never manifested on PickCube (with or without dual-critic). ve_ratio peaked at 2.3 early (32.5K) and self-corrected — same pattern as TCN experiments (peak 3.7, 3.3). Eval 27.7 is indistinguishable from CIVO-config baseline (26.6). The subsample+dt_emb config itself degrades PickCube from 58.6 to ~27, and dual-critic does not recover this gap. Hypothesis rejected: PickCube is CIVO-immune at this training scale, making it a poor test for intervention generality.\\\"}, \\\"completed_at\\\": \\\"2026-05-21T19:45:46.721Z\\\"}, \\\"exp_034_dual_critic_cheetah\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T12:09:08.035Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:09:56.881Z\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"total_env_steps\\\": 224000, \\\"eval_return_peak\\\": 315.7, \\\"eval_return_peak_step\\\": 45000, \\\"eval_return_final\\\": 97.5, \\\"ve_ratio_peak\\\": 1.8, \\\"ve_ratio_peak_step\\\": 55000, \\\"ve_ratio_final\\\": 0.1, \\\"civo_alerts\\\": 2, \\\"civo_alert_steps\\\": [95000, 105000], \\\"v1_v2_correlated\\\": true, \\\"gate_dt_2_frac\\\": 1, \\\"gate_entropy\\\": 0, \\\"exit_code\\\": 0, \\\"eval_return_trajectory\\\": {\\\"5K\\\": 8.3, \\\"15K\\\": 27.8, \\\"25K\\\": 108.7, \\\"35K\\\": 110, \\\"45K\\\": 315.7, \\\"55K\\\": 34.5, \\\"65K\\\": 81.5, \\\"75K\\\": 183, \\\"85K\\\": 88.4, \\\"95K\\\": 41, \\\"105K\\\": 27.2, \\\"115K\\\": 45.9, \\\"125K\\\": 58.7, \\\"135K\\\": 71.6, \\\"145K\\\": 61.9, \\\"155K\\\": 52.1, \\\"165K\\\": 153.8, \\\"175K\\\": 104.9, \\\"185K\\\": 101.4, \\\"195K\\\": 115.3, \\\"205K\\\": 101.5, \\\"215K\\\": 97.5}, \\\"ve_ratio_trajectory\\\": {\\\"15K\\\": 0.1, \\\"25K\\\": 0.1, \\\"35K\\\": 0.2, \\\"45K\\\": 0.1, \\\"55K\\\": 1.8, \\\"65K\\\": 0.7, \\\"75K\\\": 0.3, \\\"85K\\\": 0.5, \\\"95K\\\": 1, \\\"105K\\\": 1.6, \\\"115K\\\": 0.9, \\\"125K\\\": 0.6, \\\"135K\\\": 0.4, \\\"145K\\\": 0.4, \\\"155K\\\": 0.4, \\\"165K\\\": 0.1, \\\"175K\\\": 0.2, \\\"185K\\\": 0.2, \\\"195K\\\": 0.1, \\\"205K\\\": 0.1, \\\"215K\\\": 0.1}, \\\"value1_mean_trajectory\\\": {\\\"15K\\\": 1.8, \\\"25K\\\": 10.9, \\\"35K\\\": 23.7, \\\"45K\\\": 39, \\\"55K\\\": 60.5, \\\"65K\\\": 59.3, \\\"75K\\\": 52.6, \\\"85K\\\": 46.7, \\\"95K\\\": 41.7, \\\"105K\\\": 43.4, \\\"115K\\\": 39.3, \\\"125K\\\": 33.8, \\\"135K\\\": 28.5, \\\"145K\\\": 24.6, \\\"155K\\\": 21.5, \\\"165K\\\": 19.2, \\\"175K\\\": 17.8, \\\"185K\\\": 16.7, \\\"195K\\\": 15.7, \\\"205K\\\": 14.8, \\\"215K\\\": 14.2}, \\\"conclusion_detail\\\": \\\"CIVO triggered but partially mitigated. Two CIVO alerts (95K, 105K), peak ve_ratio=1.8 at 55K. Eval crashed from peak 315.7 to 27.2 (105K), recovered to 97.5. Dual-critic provided 40x reduction in overestimation vs baseline (ve_ratio 1.8 vs NVE 70.64) and prevented catastrophic collapse (eval 97.5 vs 0.83). But CIVO not fully suppressed — hypothesis of cross-environment generality not supported. v1≈v2 throughout (no critic disagreement).\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_034_dual_critic_cheetah --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --dual_critic True\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3_dual_critic\\\", \\\"seed\\\": 0, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\\\", \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run\\\"}, \\\"hypothesis\\\": \\\"Dual-critic on Cheetah Run: TCN failed at all σ on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\\\", \\\"parent\\\": \\\"exp_032_dual_critic_walker\\\", \\\"completed_at\\\": \\\"2026-05-21T12:09:56.881Z\\\"}, \\\"exp_029d_tcn_walker_s3_sigma02\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T19:43:05.327Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:38:07.906Z\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"total_env_steps\\\": 224000, \\\"eval_return_final\\\": 104.5, \\\"eval_return_peak\\\": 349.6, \\\"eval_return_peak_step\\\": 95000, \\\"eval_return_105K\\\": 71.8, \\\"ve_ratio_final\\\": 0.4, \\\"ve_ratio_peak\\\": 3, \\\"ve_ratio_peak_step\\\": 105000, \\\"civo_blowup\\\": true, \\\"civo_blowup_step\\\": 105000, \\\"eval_return_trajectory\\\": {\\\"5K\\\": 31.7, \\\"15K\\\": 159.1, \\\"25K\\\": 155.7, \\\"35K\\\": 190.8, \\\"45K\\\": 137.1, \\\"55K\\\": 210.7, \\\"65K\\\": 189.5, \\\"75K\\\": 253.2, \\\"85K\\\": 259.5, \\\"95K\\\": 349.6, \\\"105K\\\": 71.8, \\\"115K\\\": 69.8, \\\"125K\\\": 61.5, \\\"135K\\\": 141.8, \\\"145K\\\": 98.7, \\\"155K\\\": 88.9, \\\"165K\\\": 86.2, \\\"175K\\\": 123.5, \\\"185K\\\": 153.7, \\\"195K\\\": 68.8, \\\"205K\\\": 63.7, \\\"215K\\\": 104.5}, \\\"ve_ratio_trajectory\\\": {\\\"15K\\\": 0, \\\"25K\\\": 0.2, \\\"35K\\\": 0.3, \\\"45K\\\": 0.7, \\\"55K\\\": 0.6, \\\"65K\\\": 0.9, \\\"75K\\\": 0.8, \\\"85K\\\": 0.9, \\\"95K\\\": 0.7, \\\"105K\\\": 3, \\\"115K\\\": 2.5, \\\"125K\\\": 2.4, \\\"135K\\\": 0.9, \\\"145K\\\": 1.1, \\\"155K\\\": 1.1, \\\"165K\\\": 0.9, \\\"175K\\\": 0.6, \\\"185K\\\": 0.4, \\\"195K\\\": 0.8, \\\"205K\\\": 0.7, \\\"215K\\\": 0.4}, \\\"exit_code\\\": 0}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --config walker_walk_tcn --seed 3 --tcn_sigma 0.2\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"walker_walk\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_tcn_sigma02\\\", \\\"seed\\\": 3}, \\\"hypothesis\\\": \\\"Fourth TCN σ=0.2 seed to match 4 baseline seeds for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\\\", \\\"completed_at\\\": \\\"2026-05-21T03:38:07.906Z\\\"}, \\\"exp_025_obs_sgs_walker_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T02:40:59.914Z\\\", \\\"updated_at\\\": \\\"2026-05-20T02:41:29.954Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python dreamer.py --configs dmc_vision --task dmc_walker_walk --obs_decoder_sgs true --seed 1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3-obs-sgs\\\", \\\"seed\\\": 1}, \\\"hypothesis\\\": \\\"Obs-decoder stop-gradient on symlog (SGS) prevents CIVO in Walker by breaking the value→decoder→representation gradient pathway, keeping NVE below 1.5× baseline throughout training.\\\", \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/checkpoint.ckpt\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"final_eval_return\\\": 726.41, \\\"peak_ve_ratio\\\": 0.8313, \\\"peak_ve_ratio_step\\\": 95000, \\\"peak_NVE_approx\\\": 1.28, \\\"ve_ratio_5K\\\": 0, \\\"ve_ratio_25K\\\": 0.1585, \\\"ve_ratio_45K\\\": 0.478, \\\"ve_ratio_65K\\\": 0.5932, \\\"ve_ratio_75K\\\": 0.5522, \\\"ve_ratio_85K\\\": 0.6419, \\\"ve_ratio_95K\\\": 0.8313, \\\"ve_ratio_105K\\\": 0.5093, \\\"ve_ratio_115K\\\": 0.4117, \\\"ve_ratio_125K\\\": 0.3476, \\\"ve_ratio_135K\\\": 0.2809, \\\"ve_ratio_145K\\\": 0.1883, \\\"ve_ratio_155K\\\": 0.1842, \\\"ve_ratio_165K\\\": 0.1099, \\\"ve_ratio_175K\\\": 0.0905, \\\"ve_ratio_185K\\\": 0.1088, \\\"ve_ratio_195K\\\": 0.2013, \\\"ve_ratio_205K\\\": 0.0725, \\\"ve_ratio_215K\\\": 0.0563, \\\"conclusion_detail\\\": \\\"CIVO prevented. Peak NVE ~1.28x at 95K (baseline ~0.648 interpolated), well below 1.5x threshold. ve_ratio monotonically declines from 95K onward to 0.056 at 215K. Obs-decoder SGS Walker seed 1 is 1/4 healthy prevention seed.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T02:41:29.954Z\\\"}, \\\"exp_025_obs_sgs_walker_s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T02:00:40.376Z\\\", \\\"updated_at\\\": \\\"2026-05-20T02:01:23.024Z\\\", \\\"hypothesis\\\": \\\"Blocking observation-decoder gradients via stop-gradient (SGS) on Walker will prevent early-onset CIVO by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/checkpoint.pt\\\", \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs walker_obs_sgs --seed 4\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_obs_sgs\\\", \\\"seed\\\": 4}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"final_eval_return\\\": 241.47, \\\"final_value_mean\\\": 34.3, \\\"final_ve_ratio\\\": 0.1421, \\\"peak_ve_ratio\\\": 6.0622, \\\"peak_ve_step\\\": 75000, \\\"ve_trajectory\\\": {\\\"5000\\\": 0, \\\"15000\\\": 0.0206, \\\"25000\\\": 0.1623, \\\"35000\\\": 0.7183, \\\"45000\\\": 0.67, \\\"55000\\\": 1.2924, \\\"65000\\\": 2.1521, \\\"75000\\\": 6.0622, \\\"85000\\\": 4.0813, \\\"95000\\\": 2.0202, \\\"105000\\\": 1.5704, \\\"115000\\\": 2.1303, \\\"125000\\\": 1.2078, \\\"135000\\\": 1.2884, \\\"145000\\\": 1.2645, \\\"155000\\\": 0.6109, \\\"165000\\\": 0.6521, \\\"175000\\\": 0.5908, \\\"185000\\\": 0.3178, \\\"195000\\\": 0.2701, \\\"205000\\\": 0.4087, \\\"215000\\\": 0.1421}, \\\"conclusion_detail\\\": \\\"Obs-decoder SGS failed to prevent early-onset CIVO on Walker seed 4. Severe CIVO collapse 55K-115K with peak ve_ratio=6.06 at 75K (eval crashed from 179 at 25K to 34 at 75K). Value overestimation gradually decayed through second half of training (1.26@145K → 0.14@215K) and eval eventually recovered to 241.5@215K. However, the SGS intervention did not prevent the CIVO onset — the recovery was driven by natural value decay over extended training, not by the SGS mechanism.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T02:01:23.024Z\\\"}, \\\"exp_026_obs_sgs_cheetah_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T01:38:04.002Z\\\", \\\"updated_at\\\": \\\"2026-05-20T01:38:47.743Z\\\", \\\"hypothesis\\\": \\\"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/checkpoint.pt\\\", \\\"log_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs cheetah_obs_sgs --seed 1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_obs_sgs\\\", \\\"seed\\\": 1}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 105000, \\\"final_eval_return\\\": 38.26, \\\"final_value_mean\\\": 37.84, \\\"final_ve_ratio\\\": 0.9891, \\\"peak_ve_ratio\\\": 11.8091, \\\"peak_ve_step\\\": 75000, \\\"ve_trajectory\\\": {\\\"5000\\\": 0.0001, \\\"15000\\\": 0.0262, \\\"25000\\\": 0.0657, \\\"35000\\\": 0.1056, \\\"45000\\\": 0.979, \\\"55000\\\": 7.3924, \\\"65000\\\": 10.8375, \\\"75000\\\": 11.8091, \\\"85000\\\": 7.5096, \\\"95000\\\": 5.7255, \\\"105000\\\": 0.9891}, \\\"conclusion_detail\\\": \\\"Obs-decoder SGS failed on Cheetah seed 1: severe CIVO collapse 45K-95K, peak ve_ratio=11.81 at 75K. Eval_return crashed from 271.9 (35K) to 3.65 (75K). Late ve_ratio recovery to ~1.0 at 105K but eval_return (38.3) remained 86% below pre-collapse peak. Consistent with s0 result — SGS intervention is counterproductive on Cheetah, amplifying rather than suppressing CIVO.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T01:38:47.743Z\\\"}, \\\"exp_026_obs_sgs_cheetah_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T01:32:40.958Z\\\", \\\"updated_at\\\": \\\"2026-05-20T01:33:21.724Z\\\", \\\"hypothesis\\\": \\\"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs cheetah_obs_sgs --seed 0\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_obs_sgs\\\", \\\"seed\\\": 0}, \\\"checkpoint_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/checkpoint.pt\\\", \\\"log_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 105000, \\\"final_eval_return\\\": 38.76, \\\"final_value_mean\\\": 51.16, \\\"final_ve_ratio\\\": 1.3199, \\\"peak_ve_ratio\\\": 8.5607, \\\"peak_ve_step\\\": 65000, \\\"ve_trajectory\\\": {\\\"5000\\\": 0.0001, \\\"15000\\\": 0.0244, \\\"25000\\\": 0.094, \\\"35000\\\": 0.177, \\\"45000\\\": 0.3098, \\\"55000\\\": 0.9939, \\\"65000\\\": 8.5607, \\\"75000\\\": 1.2188, \\\"85000\\\": 0.9696, \\\"95000\\\": 1.486, \\\"105000\\\": 1.3199}, \\\"conclusion_detail\\\": \\\"Obs-decoder SGS failed on Cheetah: full CIVO collapse at 65K (ve_ratio=8.56, NVE=21.85x 5-seed normalized). Partial recovery by 75K but performance remained degraded (eval_return=38.8 vs baseline ~160). Consistent with compensatory amplification — blocking obs decoder gradient worsened CIVO vs untreated baseline (010b NVE=8.27x). SGS intervention is counterproductive on Cheetah.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T01:33:21.724Z\\\"}, \\\"exp_025_obs_sgs_walker_s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T00:48:33.067Z\\\", \\\"updated_at\\\": \\\"2026-05-20T00:49:00.531Z\\\", \\\"hypothesis\\\": \\\"Observation-decoder SGS regularization will prevent CIVO collapse by grounding value estimates through auxiliary reconstruction loss, maintaining healthy NVE ratios throughout training.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 train.py --config configs/exp_025_obs_sgs_walker_s3.yaml\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/\\\", \\\"data_count\\\": 215000, \\\"model_name\\\": \\\"dreamer_obs_sgs\\\", \\\"seed\\\": 3}, \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/\\\", \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"eval_return_105k\\\": 818.58, \\\"ve_ratio_105k\\\": 0.5621, \\\"eval_return_135k\\\": 66.95, \\\"ve_ratio_135k\\\": 5.4659, \\\"eval_return_145k\\\": 43.75, \\\"ve_ratio_145k\\\": 6.8121, \\\"eval_return_175k\\\": 193.92, \\\"ve_ratio_175k\\\": 0.8274, \\\"eval_return_215k\\\": 590.17, \\\"ve_ratio_215k\\\": 0.1365, \\\"peak_ve_ratio\\\": 6.8121, \\\"peak_ve_step\\\": 145000, \\\"conclusion_detail\\\": \\\"Obs-decoder SGS delayed CIVO onset (healthy at 105K, NVE=0.56x) but failed to prevent late collapse (135K NVE=5.47x, peak 6.81x at 145K, partial recovery to 0.83x at 175K). Final eval_return recovered to 590 but value_mean collapsed to 80.6 (ve_ratio=0.14x). Late-onset CIVO variant.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T00:49:00.531Z\\\"}, \\\"exp_001_baseline_s4_extended\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T23:03:24.044Z\\\", \\\"updated_at\\\": \\\"2026-05-19T23:03:47.714Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py (extended from 250k to 520k steps)\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_s4_baseline\\\", \\\"seed\\\": 4}, \\\"hypothesis\\\": \\\"Extending baseline S4 training from 250k to 520k steps will show whether eval_return plateaus or continues improving, establishing the convergence profile for NVE robustness analysis.\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/checkpoint.ckpt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/train_extended.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T23:03:46.304Z\\\", \\\"metrics\\\": {\\\"final_step\\\": 520000, \\\"final_eval_step\\\": 512000, \\\"final_eval_return\\\": 938.86, \\\"total_eval_checkpoints\\\": 52}}, \\\"exp_008e_v3_s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T11:35:59.034Z\\\", \\\"updated_at\\\": \\\"2026-05-18T11:36:30.618Z\\\", \\\"metrics\\\": {\\\"eval_trajectory\\\": {\\\"5K\\\": 30.91, \\\"15K\\\": 343.66, \\\"25K\\\": 450.28, \\\"35K\\\": 527.44, \\\"45K\\\": 652.29, \\\"55K\\\": 717.96, \\\"65K\\\": 736.58, \\\"75K\\\": 751.73, \\\"85K\\\": 818.75, \\\"95K\\\": 835.34, \\\"105K\\\": 899.33}, \\\"value_trajectory\\\": {\\\"5K\\\": 0.002, \\\"15K\\\": 5.03, \\\"25K\\\": 46.89, \\\"35K\\\": 112.41, \\\"45K\\\": 186.9, \\\"55K\\\": 264.08, \\\"65K\\\": 343.83, \\\"75K\\\": 413.29, \\\"85K\\\": 467.89, \\\"95K\\\": 523.46, \\\"105K\\\": 547.4}, \\\"actor_entropy_trajectory\\\": {\\\"5K\\\": 8.19, \\\"15K\\\": 0.856, \\\"25K\\\": -2.478, \\\"35K\\\": -3.568, \\\"45K\\\": -4.167, \\\"55K\\\": -4.515, \\\"65K\\\": -4.7, \\\"75K\\\": -4.646, \\\"85K\\\": -5.029, \\\"95K\\\": -5.103, \\\"105K\\\": -5.084}, \\\"ve_ratio_trajectory\\\": {\\\"15K\\\": 0.0146, \\\"25K\\\": 0.1041, \\\"35K\\\": 0.2131, \\\"45K\\\": 0.2865, \\\"55K\\\": 0.3678, \\\"65K\\\": 0.4667, \\\"75K\\\": 0.5497, \\\"85K\\\": 0.5714, \\\"95K\\\": 0.6266, \\\"105K\\\": 0.6087}, \\\"nve_trajectory\\\": {\\\"15K\\\": 0.022, \\\"25K\\\": 0.16, \\\"35K\\\": 0.328, \\\"45K\\\": 0.441, \\\"55K\\\": 0.567, \\\"65K\\\": 0.719, \\\"75K\\\": 0.847, \\\"85K\\\": 0.88, \\\"95K\\\": 0.965, \\\"105K\\\": 0.938}, \\\"final_eval_return\\\": 899.33, \\\"peak_eval_return\\\": 899.33, \\\"peak_eval_step\\\": 105000, \\\"final_value_mean\\\": 547.4, \\\"final_ve_ratio\\\": 0.6087, \\\"final_nve\\\": 0.938, \\\"gate_dt_mean\\\": 1, \\\"gate_dt_1_frac\\\": 1, \\\"gate_dt_std\\\": 0, \\\"gate_empirical_entropy\\\": 0}, \\\"conclusion\\\": \\\"success\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15 --checkpoint_every 25000\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3\\\", \\\"seed\\\": 4}, \\\"hypothesis\\\": \\\"C6 dual-pathway (trained dt_emb + subsample ON, gate_fixed_dt=1, gate_subsample_max_dt=2, H=15) will maintain stable training without value-overestimation collapse across multiple seeds on Walker Walk 105K, validating that the subsample pathway does not introduce systematic instability.\\\", \\\"parent\\\": \\\"exp_008e_v3_subsample_on_dt1_h15\\\", \\\"completed_at\\\": \\\"2026-05-18T11:36:30.618Z\\\"}, \\\"exp_010b_cheetah_civo_trigger_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T05:08:57.636Z\\\", \\\"updated_at\\\": \\\"2026-05-18T05:09:31.471Z\\\", \\\"hypothesis\\\": \\\"CIVO (value overestimation collapse) in Cheetah Run with dt_emb + subsample ON + H=8 is reproducible across seeds. Seed=0 should exhibit NVE>1.5× and eval return collapse similar to seed=1 (NVE=8.27×).\\\", \\\"parent\\\": \\\"exp_010b_cheetah_civo_trigger\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --config cheetah_civo_trigger --seed 0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"dm_control/cheetah_run\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3_event_gated\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"dm_control/cheetah_run\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-18T05:09:28.232Z\\\", \\\"metrics\\\": {\\\"final_step\\\": 112000, \\\"peak_eval_return\\\": 247.77, \\\"peak_eval_step\\\": 35000, \\\"final_eval_return\\\": 0.83, \\\"final_NVE\\\": 70.64, \\\"first_civo_alert_step\\\": 95000, \\\"first_civo_alert_NVE\\\": 6.34, \\\"value_mean_at_105k\\\": 58.58, \\\"gate_dt_mean\\\": 2, \\\"gate_entropy\\\": 0, \\\"gate_dt_2_frac\\\": 1}}, \\\"exp_016d_sgs_walker_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T19:29:07.960Z\\\", \\\"updated_at\\\": \\\"2026-05-16T01:43:55.477Z\\\", \\\"hypothesis\\\": \\\"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心（plan_016）。修复 eval video deadlock (D056) 后重试\\\", \\\"parent\\\": \\\"exp_008d_subsample_on_h8\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 105000, \\\"model_name\\\": \\\"dreamerv3-sgs\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"exp_008d_subsample_on_h8\\\", \\\"eval_data\\\": \\\"dmc_walker_walk\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-16T01:43:55.477Z\\\"}, \\\"exp_005_event_gated_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T21:53:45.066Z\\\", \\\"updated_at\\\": \\\"2026-05-13T21:54:17.129Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"failure_reason\\\": \\\"结构性失败(D009): return最终47.4(baseline 5%), gate激活后return单调下降无恢复。85K/105K registry数据已修正为metrics.jsonl实际值(212.3/276.1, 旧值319.3/337.8系误录)。\\\", \\\"metrics\\\": {\\\"step\\\": 145000, \\\"final_eval_return\\\": 98.84, \\\"peak_eval_return\\\": 541.18, \\\"peak_eval_step\\\": 55000, \\\"eval_return_85K\\\": 212.34, \\\"eval_return_105K\\\": 276.08, \\\"eval_return_115K\\\": 25.67, \\\"eval_return_145K\\\": 98.84}, \\\"spec\\\": {\\\"command\\\": \\\"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --gate_enabled True\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3-event-gated-v4\\\", \\\"seed\\\": 1, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1\\\"}, \\\"completed_at\\\": \\\"2026-05-13T21:54:17.129Z\\\"}, \\\"exp_001_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T20:57:32.713Z\\\", \\\"updated_at\\\": \\\"2026-05-13T21:53:44.698Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"step\\\": 512000, \\\"final_eval_return\\\": 970.4, \\\"eval_return_last10_mean\\\": 950.9, \\\"eval_return_last10_std\\\": 10.5, \\\"fps\\\": 7.59}, \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs walker_walk --run.steps 512000\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3-baseline\\\", \\\"seed\\\": 1, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\\\"}, \\\"completed_at\\\": \\\"2026-05-13T20:58:00.944Z\\\"}}, \\\"count\\\": 32, \\\"total\\\": 32, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1157}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_walker_no_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T11:10:24.895Z\", \"updated_at\": \"2026-05-27T11:14:46.202Z\", \"parent\": \"exp_008f\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-51268\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"105000 steps\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"checkpoint_source\": \"none (train from scratch)\", \"eval_data\": \"dmc_walker_walk (built-in env)\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-27T11:14:46.202Z\"}, \"exp_hopper_frozen_s0_ext\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T10:47:14.544Z\", \"updated_at\": \"2026-05-27T10:48:10.979Z\", \"conclusion\": \"negative\", \"metrics\": {\"eval_return_final\": 0.56, \"eval_return_peak\": 3.58, \"eval_return_peak_step\": 85000, \"ve_ratio_final\": 15.08, \"ve_ratio_peak\": 4335664.27, \"ve_ratio_peak_step\": 105000, \"value_mean_final\": 8.46, \"civo_alerts\": 2, \"civo_alert_steps\": [65000, 105000], \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"total_steps\": 160000, \"recovery\": false}, \"spec\": {\"checkpoint_path\": \"logdir/exp_hopper_frozen_s0/latest.pt\", \"log_path\": \"logdir/exp_hopper_frozen_s0/metrics.jsonl\", \"command\": \"python train.py --config hopper_frozen_s0 --steps 160000\", \"server\": \"westd-51268\", \"data_path\": \"Hopper-v4\", \"data_count\": 160000, \"model_name\": \"dreamer_v3_frozen_dt_emb\", \"seed\": 0}, \"hypothesis\": \"Extending frozen_s0 from 105K to 150K will show eval_return recovery with ve_ratio declining, confirming frozen_s0's degenerate CIVO at 95K is transient instability during severe learning delay rather than a permanent structural failure caused by the frozen dt_embedding.\", \"completed_at\": \"2026-05-27T10:48:10.979Z\"}, \"exp_hopper_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T05:51:24.680Z\", \"updated_at\": \"2026-05-27T05:52:01.157Z\", \"metrics\": {\"step\": 105000, \"eval_final\": 96.43, \"eval_return_trajectory\": {\"5000\": 0.06, \"15000\": 1.04, \"25000\": 1.7, \"35000\": 6.55, \"45000\": 19.09, \"55000\": 22.52, \"65000\": 3.5, \"75000\": 62.2, \"85000\": 67.62, \"95000\": 86.47, \"105000\": 96.43}, \"ve_ratio_trajectory\": {\"15000\": 0.08, \"25000\": 0.098, \"35000\": 0.166, \"45000\": 0.19, \"55000\": 0.279, \"65000\": 3.479, \"75000\": 0.341, \"85000\": 0.502, \"95000\": 0.517, \"105000\": 0.559}, \"nve_peak\": 3.48, \"nve_peak_step\": 65000, \"nve_final\": 0.559, \"civo_onset\": false, \"civo_alert_count\": 0, \"value_mean_final\": 53.9, \"target_mean_final\": 54.2, \"training_steps\": 105000, \"update_count\": 25099, \"fps\": 11}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_baseline/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_baseline.log\", \"hypothesis\": \"Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE < 1.5×). Source: C1/C2 third-environment verification (D160).\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0\", \"server\": \"westd-51268\", \"data_path\": \"dmc_hopper_hop\", \"data_count\": 105000, \"model_name\": \"DreamerV3 baseline (dt=1, no gate)\", \"seed\": 0}, \"completed_at\": \"2026-05-27T05:52:01.157Z\"}, \"exp_097_cheetah_008d_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:03:25.871Z\", \"updated_at\": \"2026-05-26T11:32:48.497Z\", \"hypothesis\": \"C1 trigger seed 3: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 Cheetah 上的第四个 seed（s3）。当前 onset rate 2/3（s0 NVE=4.1×✓, s1 NVE=0.517✗, s2 NVE=138.7×✓）。s3 完成后可计算完整 onset rate（n=4）。如果 onset ≥3/4 → 高 onset rate 支持 CIVO 是 systematic phenomenon；如果 2/4 → 50% onset rate 仍有意义但需讨论。\", \"parent\": \"exp_078_cheetah_008d_s0\", \"notes\": \"重新提交到 westd-51268 cuda:0。原 bjb1 提交 (PID 324959) 已死（服务器无卡）。exp_094 同配置在 westd 跑了 1.72h 后因 SSH 断连失败，检查其 checkpoint 是否可复用。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_097_cheetah_008d_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu_ids\": [0], \"pid\": 3794, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (trained dt_emb)\", \"seed\": 3, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_097_cheetah_008d_s3/train.log\", \"checkpoint_path\": \"logdir/exp_097_cheetah_008d_s3/latest.pt\"}, \"metrics\": {\"step\": 105000, \"nve_peak\": 2.3, \"nve_peak_step\": 45000, \"nve_final\": 0.3, \"civo_onset\": true, \"civo_onset_step\": 45000, \"civo_pattern\": \"transient→degraded\", \"eval_final\": 61.7, \"eval_final_pct_baseline\": -86, \"baseline_eval_return\": 446.1, \"gate_dt_2_frac\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T11:32:48.497Z\"}, \"exp_100_walker_008a_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:39:24.456Z\", \"updated_at\": \"2026-05-26T07:52:52.927Z\", \"hypothesis\": \"Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 Walker 008a 第 2 seed。与 exp_008a_no_subsample_dt2 (s0) 和 exp_074_008a_walker_s3 (s3) 共同建立 C3 value suppression 多 seed 证据。训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练，预期无 CIVO。plan_013。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_100_walker_008a_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"server\": \"westd-51268\", \"gpu_ids\": [1], \"pid\": 5591, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (trained dt_emb, unexposed)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_100_walker_008a_s1/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_100_walker_008a_s1/latest.pt\"}, \"metrics\": {\"step\": 105000, \"eval_return_trajectory\": {\"5000\": 31, \"15000\": 168.77, \"25000\": 158.03, \"35000\": 202.91, \"45000\": 305.98, \"55000\": 457.28, \"65000\": 628.82, \"75000\": 686.98, \"85000\": 656.64, \"95000\": 717.74, \"105000\": 750.59}, \"ve_ratio_trajectory\": {\"15000\": 0.035, \"25000\": 0.206, \"35000\": 0.279, \"45000\": 0.261, \"55000\": 0.248, \"65000\": 0.234, \"75000\": 0.26, \"85000\": 0.315, \"95000\": 0.325, \"105000\": 0.328}, \"value_mean_trajectory\": {\"15000\": 5.98, \"25000\": 32.58, \"35000\": 56.55, \"45000\": 79.94, \"55000\": 113.33, \"65000\": 147.14, \"75000\": 178.73, \"85000\": 206.95, \"95000\": 233.17, \"105000\": 246.06}, \"nve_peak\": 0.328, \"nve_final\": 0.328, \"civo_onset\": false, \"eval_final\": 750.59, \"eval_final_pct_baseline\": -18, \"baseline_eval_return\": 915.67, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T07:52:45.733Z\", \"notes\": \"C3 Walker 008a s1 完成。训练正常结束(105K steps)。eval_return@105K=750.59 (baseline 915.67, -18.0%)。ve_ratio 全程 0.035-0.328，NVE_peak=0.328，远低于 τ=1.5×，civo/alert 全程 0.0，无 CIVO onset。Value suppression 确认（value_mean 持续低于 eval_return）。与 parent s0 (eval@105K=777.66, -15.1%, ve_ratio 0.37-0.54) 一致：s1 性能略低但趋势相同，两个 seed 均无 CIVO 且呈现 value suppression，C3 Walker 008a 2-seed 证据闭合。gate_dt 全程固定为 2.0 (100% dt_2_frac)，符合 gate_fixed_dt=2 配置。\"}, \"rssm_fidelity_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:47:46.584Z\", \"updated_at\": \"2026-05-26T03:47:59.871Z\", \"hypothesis\": \"RSSM fidelity v2 分析：对比 4 类模型（baseline/trained_dt_emb/no_dt_emb/frozen）在 dt=1 vs dt=2 下的 observation/reward reconstruction loss。使用 Walker checkpoint (n=800)。结果：trained_dt_emb reward ratio 1.50×, obs ratio 1.44×; baseline obs ratio 1.55×; no_dt_emb gap 最小 (1.23×/1.16×)。\", \"conclusion\": \"success\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python analyze_rssm_fidelity_v2.py --device cuda:0\", \"server\": \"westd-51268\", \"data_path\": \"Walker logdirs (exp_008d/009d/009c/084)\", \"data_count\": 800, \"model_name\": \"RSSM fidelity analysis v2\", \"seed\": 0, \"checkpoint_path\": \"analysis_rssm_fidelity_v2.json\", \"log_path\": \"N/A (analysis task)\"}, \"completed_at\": \"2026-05-26T03:47:59.871Z\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:26:00.391Z\", \"updated_at\": \"2026-05-26T03:03:45.406Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"N/A - bjb1-45299 lost GPU\", \"checkpoint_path\": \"N/A - bjb1-45299 lost GPU\", \"failure_reason\": \"bjb1-45299 server lost GPU allocation, experiment terminated\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T03:03:45.406Z\"}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:42:39.309Z\", \"updated_at\": \"2026-05-26T03:03:44.692Z\", \"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks\", \"parent\": \"exp_049\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"maniskill_StackCube-v1 (online RL)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, StackCube s0)\", \"seed\": 0, \"log_path\": \"N/A - bjb1-45299 lost GPU\", \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"maniskill_StackCube-v1 (online eval)\", \"checkpoint_path\": \"N/A - bjb1-45299 lost GPU\", \"failure_reason\": \"bjb1-45299 server lost GPU allocation, experiment terminated\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T03:03:44.692Z\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:14:38.578Z\", \"updated_at\": \"2026-05-26T03:03:42.946Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion（Walker/Cheetah）推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack），比 PickCube 更难。如果触发 CIVO → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"parent\": \"exp_048_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"N/A - bjb1-45299 lost GPU\", \"checkpoint_path\": \"N/A - bjb1-45299 lost GPU\", \"failure_reason\": \"bjb1-45299 server lost GPU allocation, experiment terminated\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T03:03:42.946Z\"}, \"exp_081_008e_v3_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T15:42:24.765Z\", \"updated_at\": \"2026-05-25T15:43:10.949Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 597.1, \"vs_baseline\": \"-34.8%\", \"vs_baseline_pct\": 65.2, \"baseline_105K\": 915.67, \"ve_ratio_peak\": 0.6, \"ve_ratio_final\": 0.5, \"NVE_est_peak\": 0.8, \"NVE_est_final\": 0.7, \"gate_dt_mean\": 1, \"gate_dt_1_frac\": 1, \"civo_alert_count\": 0, \"training_steps\": 105000, \"update_count\": 25099, \"value_mean_final\": 295}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_081_008e_v3_walker_s2/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"spec\": {\"command\": \"python train.py --config 008e_v3 --env walker_walk --seed 2\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3_008e_v3\", \"seed\": 2}, \"hypothesis\": \"Trained dt_emb with dt=1 imagination and subsample ON (max_dt=2) does not trigger CIVO in Walker Walk, as the value function sees only single-step predictions that match the world model's training distribution, preventing value inflation even with learned temporal embeddings.\", \"completed_at\": \"2026-05-25T15:43:10.949Z\"}, \"exp_073_008f_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:52:07.413Z\", \"updated_at\": \"2026-05-25T09:52:34.845Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 289.3, \"eval_return_peak\": 486.5, \"eval_return_peak_step\": 75000, \"ve_ratio_max\": 0.5, \"civo_alert_max\": 0, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"total_env_steps\": 112000, \"total_updates\": 25099}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_073_008f_walker_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\", \"spec\": {\"command\": \"python train.py --config 008f --seed 4\", \"server\": \"westd-19154\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamer_v3_008f\", \"seed\": 4}, \"hypothesis\": \"Removing dt_embedding (dt_embed_dim=0) in the 008f control config prevents CIVO onset because the agent cannot form temporally-conditioned value predictions that compound imagination-driven overestimation. With fixed dt=2 and no temporal embedding, value error ratio should remain below the 1.5x CIVO threshold across seeds.\", \"completed_at\": \"2026-05-25T09:52:34.845Z\"}, \"exp_069_008f_walker_repro_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:20:25.632Z\", \"updated_at\": \"2026-05-25T07:21:13.407Z\", \"hypothesis\": \"Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk. With no learned temporal embedding, the value network cannot develop the compounding overestimation pattern that causes CIVO collapse. This seed=1 run extends the evidence from exp_008f (seed=0).\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"spec\": {\"command\": \"python train.py --configs dmc_vision --task dmc_walker_walk --seed 1 --logdir logdir/exp_069_008f_walker_repro_s1\", \"server\": \"westd-19154\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 0, \"model_name\": \"dreamerv2_no_dt_embed_h8\", \"seed\": 1, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_walker_walk_online\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_069_008f_walker_repro_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T07:20:58.159Z\", \"metrics\": {\"eval_return_final\": 237.8, \"eval_return_final_step\": 105000, \"eval_return_peak\": 390.1, \"eval_return_peak_step\": 95000, \"steps_completed\": 112000, \"eval_steps\": 105000, \"civo_triggered\": false, \"civo_alert_count\": 0, \"ve_ratio_max\": 0.447, \"ve_ratio_max_step\": 105000, \"ve_ratio_final\": 0.447, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"value_mean_final\": 106.3, \"target_mean_final\": 106.4, \"value_loss_final\": 0.99, \"seed\": 1, \"eval_return_trajectory\": {\"5K\": 30.5, \"15K\": 158.7, \"25K\": 180.8, \"35K\": 250.3, \"45K\": 293.6, \"55K\": 272.2, \"65K\": 328.1, \"75K\": 244.8, \"85K\": 382.5, \"95K\": 390.1, \"105K\": 237.8}, \"ve_ratio_trajectory\": {\"15K\": 0.021, \"25K\": 0.111, \"35K\": 0.171, \"95K\": 0.275, \"105K\": 0.447}, \"note\": \"C2 causal control: no dt_embedding, fixed dt=2. No CIVO triggered. ve_ratio stayed <0.5 throughout. Late eval dip (390→238) is normal Walker variance, not CIVO-driven (value_mean≈target_mean, no overestimation).\"}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:16:11.755Z\", \"updated_at\": \"2026-05-23T23:34:24.080Z\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1.log\"}, \"hypothesis\": \"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，162.5K 时仍 1.94）。如果 s1 也触发持续 CIVO → PegInsertion 是最严重的 CIVO 环境（比 StackCube 自修复更难），支持 severity-dependent narrative；如果不触发 → seed-specific 异常。\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"checkpoint_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/latest.pt\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1.log\", \"metrics\": {\"total_steps\": 222400, \"ve_ratio_max\": 3.08, \"ve_ratio_max_step\": 92500, \"ve_ratio_final\": 0.5, \"ve_ratio_final_step\": 212500, \"eval_peak\": 24.05, \"eval_peak_step\": 112500, \"eval_final\": 11.44, \"eval_final_step\": 212500, \"civo_triggered\": true, \"civo_self_corrected\": \"partial\", \"civo_onset_step\": 32500, \"civo_peak_step\": 92500, \"ve_ratio_trajectory\": {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}, \"eval_trajectory\": {\"2500\": 2.01, \"12500\": 10.12, \"22500\": 11.47, \"32500\": 12.01, \"42500\": 10.13, \"52500\": 10.31, \"62500\": 9.02, \"72500\": 10.07, \"82500\": 8.78, \"92500\": 7.24, \"102500\": 9.2, \"112500\": 24.05, \"122500\": 16.46, \"132500\": 13.15, \"142500\": 20.44, \"152500\": 23.4, \"162500\": 9.07, \"172500\": 9.46, \"182500\": 8.51, \"192500\": 7.81, \"202500\": 8.58, \"212500\": 11.44}, \"note\": \"CIVO triggered (ve_ratio 3.08@92.5K), less severe than s0 (10.05). Partial self-correction to 0.50 by 212.5K. Eval poor throughout (~10-24), PegInsertion is hard task.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T23:34:24.080Z\"}, \"exp_048_cheetah_civo_extension\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:40.050Z\", \"updated_at\": \"2026-05-22T21:17:46.852Z\", \"hypothesis\": \"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → \\\"severity determines recoverability\\\" narrative, strongest paper defense. If it does → CIVO is universally transient regardless of severity.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}, \"metrics\": {\"eval_final\": 23.423, \"eval_peak\": 32.835, \"eval_peak_step\": 252000, \"ve_ratio_initial_measured\": 6.135, \"ve_ratio_initial_measured_step\": 122000, \"ve_ratio_inherited_from_exp010b\": 46.34, \"ve_ratio_peak_in_run\": 24.112, \"ve_ratio_peak_step\": 162000, \"ve_ratio_final\": 1.803, \"nve_inherited\": 70.64, \"nve_peak_in_run\": 36.76, \"nve_final\": 2.75, \"baseline_ve_ratio\": 0.656, \"total_steps\": 312000, \"last_eval_step\": 302000, \"civo_self_corrected\": \"partial\", \"civo_reduction_pct\": 96.1, \"civo_correction_duration_steps\": 197000, \"gate_collapsed\": true, \"gate_dt_final\": 2, \"gate_dt_2_frac_final\": 1}, \"checkpoint_path\": \"logdir/exp_048_cheetah_civo_extension/checkpoint_302000.pt\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:17:46.852Z\"}, \"exp_047_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:42:12.914Z\", \"updated_at\": \"2026-05-22T19:01:30.894Z\", \"hypothesis\": \"Freezing dt_emb in Walker Walk (seed 1) prevents sustained CIVO collapse, replicating exp_042 (seed 0, NVE=0.19) finding that removing dt conditioning blocks the overestimation feedback loop\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 282452, \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\"}, \"metrics\": {\"eval_peak\": 408.79, \"eval_peak_step\": 125000, \"eval_final\": 144.22, \"eval_final_step\": 215000, \"ve_ratio_peak\": 1.099, \"ve_ratio_peak_step\": 75000, \"ve_ratio_final\": 0.277, \"nve_peak\": 1.71, \"nve_peak_step\": 95000, \"nve_final_105k\": 0.56, \"total_steps\": 225000, \"note\": \"Transient NVE>1.5x at 75K-95K with full self-correction by 105K. Late eval decline (408->144) NOT CIVO-driven (ve_ratio=0.28). No sustained collapse.\"}, \"checkpoint_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:50:46.948Z\"}, \"exp_046_frozen_dt_emb_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:40:43.182Z\", \"updated_at\": \"2026-05-22T18:32:34.105Z\", \"hypothesis\": \"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation. Source: D133 + exp_042 result + R1-N4 cross-environment concern.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 281513, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_046_frozen_dt_emb_cheetah/train.log\"}, \"metrics\": {\"eval_final\": 150.5, \"eval_peak\": 207.4, \"eval_peak_step\": 145000, \"ve_ratio_peak\": 0.4, \"ve_ratio_final\": 0.1, \"nve_peak\": 1.35, \"nve_peak_step\": 45000, \"nve_final\": 0.17, \"total_steps\": 224000, \"civo_alert_count\": 0, \"eval_trajectory\": \"5K:8.3, 15K:110, 35K:160, 95K:181, 105K:206, 115K:46, 145K:207, 155K:161, 215K:150.5\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:31:00.933Z\"}, \"exp_048_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:44:55.613Z\", \"updated_at\": \"2026-05-22T17:14:16.564Z\", \"hypothesis\": \"ManiSkill Phase 1 scout: CIVO trigger config (trained dt_emb + subsample ON + H=8) on StackCube-v1 manipulation task. Tests whether CIVO generalizes beyond locomotion (Walker/Cheetah) to manipulation domains. exp_019b showed transient CIVO on PickCube; StackCube is harder (multi-stage). If CIVO triggers → extends cross-domain evidence; if not → supports locomotion-specific scope.\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 87609, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"/tmp/exp_048.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-22T17:14:16.564Z\"}, \"exp_045_treatment_extension_008d_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:40:52.894Z\", \"updated_at\": \"2026-05-22T15:44:50.990Z\", \"hypothesis\": \"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 70945, \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}, \"metrics\": {\"eval_final\": 867.6, \"eval_peak\": 869.7, \"eval_peak_step\": 242000, \"ve_ratio_final\": 0.05, \"ve_ratio_peak\": 4.91, \"ve_ratio_peak_step\": 132000, \"nve_final\": 0.052, \"total_steps\": 312000, \"self_correction_onset\": 142000, \"finding\": \"CIVO self-correction: ve_ratio 4.91→0.05, eval 35→868 over 170K steps\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\", \"completed_at\": \"2026-05-22T15:44:50.990Z\"}, \"exp_036_dual_critic_pickcube\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T19:45:02.066Z\", \"updated_at\": \"2026-05-21T19:45:46.721Z\", \"spec\": {\"command\": \"python train.py --task ManiSkill_PickCube-v1 --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 0 --steps 200000\", \"server\": \"bjb1-45299\", \"data_path\": \"ManiSkill_PickCube-v1\", \"data_count\": 0, \"model_name\": \"dreamerv3_dual_critic\", \"seed\": 0}, \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"parent\": \"exp_032_dual_critic_walker\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_036_dual_critic_pickcube\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 212447, \"total_env_steps\": 212447, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"eval_return_peak_step\": 202500, \"ve_ratio_peak\": 2.3, \"ve_ratio_peak_step\": 32500, \"ve_ratio_final\": 0.2, \"civo_alerts\": 0, \"v1_v2_max_divergence\": 0, \"v1_v2_correlated\": true, \"CIVO_prevented\": \"vacuous_no_civo_in_baseline\", \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"exit_code\": 0, \"eval_return_trajectory\": {\"2.5K\": 2, \"12.5K\": 17.5, \"22.5K\": 17.5, \"32.5K\": 11.6, \"42.5K\": 15.6, \"52.5K\": 11.7, \"62.5K\": 18.8, \"72.5K\": 5.4, \"82.5K\": 22.5, \"92.5K\": 18.1, \"102.5K\": 8.4, \"112.5K\": 7.1, \"122.5K\": 9.1, \"132.5K\": 12.8, \"142.5K\": 14, \"152.5K\": 13.1, \"162.5K\": 16.2, \"172.5K\": 19.7, \"182.5K\": 16.8, \"192.5K\": 13.7, \"202.5K\": 27.7}, \"ve_ratio_trajectory\": {\"12.5K\": 0.2, \"22.5K\": 1, \"32.5K\": 2.3, \"42.5K\": 1.4, \"52.5K\": 1.4, \"62.5K\": 0.6, \"72.5K\": 1.6, \"82.5K\": 0.3, \"92.5K\": 0.3, \"102.5K\": 0.6, \"112.5K\": 0.7, \"122.5K\": 0.5, \"132.5K\": 0.4, \"142.5K\": 0.3, \"152.5K\": 0.4, \"162.5K\": 0.3, \"172.5K\": 0.3, \"182.5K\": 0.3, \"192.5K\": 0.4, \"202.5K\": 0.2}, \"value1_mean_trajectory\": {\"2.5K\": 0, \"12.5K\": 3.8, \"22.5K\": 17.9, \"32.5K\": 26.9, \"42.5K\": 21.2, \"52.5K\": 16.1, \"62.5K\": 11.6, \"72.5K\": 8.7, \"82.5K\": 7.2, \"92.5K\": 6, \"102.5K\": 5.3, \"112.5K\": 5.1, \"122.5K\": 5, \"132.5K\": 4.9, \"142.5K\": 4.9, \"152.5K\": 5.3, \"162.5K\": 5.7, \"172.5K\": 5.6, \"182.5K\": 5.6, \"192.5K\": 5.6, \"202.5K\": 5.8}, \"baseline_comparison\": {\"exp_019a_v2_vanilla_baseline_final\": 58.6, \"exp_019b_civo_config_baseline_final\": 26.6, \"exp_031_tcn_sigma02_final\": 17.2, \"exp_031b_tcn_sigma05_final\": 25.5}, \"conclusion_detail\": \"CIVO never manifested on PickCube (with or without dual-critic). ve_ratio peaked at 2.3 early (32.5K) and self-corrected — same pattern as TCN experiments (peak 3.7, 3.3). Eval 27.7 is indistinguishable from CIVO-config baseline (26.6). The subsample+dt_emb config itself degrades PickCube from 58.6 to ~27, and dual-critic does not recover this gap. Hypothesis rejected: PickCube is CIVO-immune at this training scale, making it a poor test for intervention generality.\"}, \"completed_at\": \"2026-05-21T19:45:46.721Z\"}, \"exp_034_dual_critic_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:09:08.035Z\", \"updated_at\": \"2026-05-21T12:09:56.881Z\", \"metrics\": {\"final_step\": 215000, \"total_env_steps\": 224000, \"eval_return_peak\": 315.7, \"eval_return_peak_step\": 45000, \"eval_return_final\": 97.5, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 0.1, \"civo_alerts\": 2, \"civo_alert_steps\": [95000, 105000], \"v1_v2_correlated\": true, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"exit_code\": 0, \"eval_return_trajectory\": {\"5K\": 8.3, \"15K\": 27.8, \"25K\": 108.7, \"35K\": 110, \"45K\": 315.7, \"55K\": 34.5, \"65K\": 81.5, \"75K\": 183, \"85K\": 88.4, \"95K\": 41, \"105K\": 27.2, \"115K\": 45.9, \"125K\": 58.7, \"135K\": 71.6, \"145K\": 61.9, \"155K\": 52.1, \"165K\": 153.8, \"175K\": 104.9, \"185K\": 101.4, \"195K\": 115.3, \"205K\": 101.5, \"215K\": 97.5}, \"ve_ratio_trajectory\": {\"15K\": 0.1, \"25K\": 0.1, \"35K\": 0.2, \"45K\": 0.1, \"55K\": 1.8, \"65K\": 0.7, \"75K\": 0.3, \"85K\": 0.5, \"95K\": 1, \"105K\": 1.6, \"115K\": 0.9, \"125K\": 0.6, \"135K\": 0.4, \"145K\": 0.4, \"155K\": 0.4, \"165K\": 0.1, \"175K\": 0.2, \"185K\": 0.2, \"195K\": 0.1, \"205K\": 0.1, \"215K\": 0.1}, \"value1_mean_trajectory\": {\"15K\": 1.8, \"25K\": 10.9, \"35K\": 23.7, \"45K\": 39, \"55K\": 60.5, \"65K\": 59.3, \"75K\": 52.6, \"85K\": 46.7, \"95K\": 41.7, \"105K\": 43.4, \"115K\": 39.3, \"125K\": 33.8, \"135K\": 28.5, \"145K\": 24.6, \"155K\": 21.5, \"165K\": 19.2, \"175K\": 17.8, \"185K\": 16.7, \"195K\": 15.7, \"205K\": 14.8, \"215K\": 14.2}, \"conclusion_detail\": \"CIVO triggered but partially mitigated. Two CIVO alerts (95K, 105K), peak ve_ratio=1.8 at 55K. Eval crashed from peak 315.7 to 27.2 (105K), recovered to 97.5. Dual-critic provided 40x reduction in overestimation vs baseline (ve_ratio 1.8 vs NVE 70.64) and prevented catastrophic collapse (eval 97.5 vs 0.83). But CIVO not fully suppressed — hypothesis of cross-environment generality not supported. v1≈v2 throughout (no critic disagreement).\"}, \"conclusion\": \"negative\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_034_dual_critic_cheetah --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --dual_critic True\", \"server\": \"bjb1-45299\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 0, \"model_name\": \"dreamerv3_dual_critic\", \"seed\": 0, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/checkpoint.pt\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_cheetah_run\"}, \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"parent\": \"exp_032_dual_critic_walker\", \"completed_at\": \"2026-05-21T12:09:56.881Z\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:43:05.327Z\", \"updated_at\": \"2026-05-21T03:38:07.906Z\", \"metrics\": {\"final_step\": 215000, \"total_env_steps\": 224000, \"eval_return_final\": 104.5, \"eval_return_peak\": 349.6, \"eval_return_peak_step\": 95000, \"eval_return_105K\": 71.8, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 3, \"ve_ratio_peak_step\": 105000, \"civo_blowup\": true, \"civo_blowup_step\": 105000, \"eval_return_trajectory\": {\"5K\": 31.7, \"15K\": 159.1, \"25K\": 155.7, \"35K\": 190.8, \"45K\": 137.1, \"55K\": 210.7, \"65K\": 189.5, \"75K\": 253.2, \"85K\": 259.5, \"95K\": 349.6, \"105K\": 71.8, \"115K\": 69.8, \"125K\": 61.5, \"135K\": 141.8, \"145K\": 98.7, \"155K\": 88.9, \"165K\": 86.2, \"175K\": 123.5, \"185K\": 153.7, \"195K\": 68.8, \"205K\": 63.7, \"215K\": 104.5}, \"ve_ratio_trajectory\": {\"15K\": 0, \"25K\": 0.2, \"35K\": 0.3, \"45K\": 0.7, \"55K\": 0.6, \"65K\": 0.9, \"75K\": 0.8, \"85K\": 0.9, \"95K\": 0.7, \"105K\": 3, \"115K\": 2.5, \"125K\": 2.4, \"135K\": 0.9, \"145K\": 1.1, \"155K\": 1.1, \"165K\": 0.9, \"175K\": 0.6, \"185K\": 0.4, \"195K\": 0.8, \"205K\": 0.7, \"215K\": 0.4}, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python train.py --config walker_walk_tcn --seed 3 --tcn_sigma 0.2\", \"server\": \"bjb1-40020\", \"data_path\": \"walker_walk\", \"data_count\": 0, \"model_name\": \"dreamer_tcn_sigma02\", \"seed\": 3}, \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"completed_at\": \"2026-05-21T03:38:07.906Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:40:59.914Z\", \"updated_at\": \"2026-05-20T02:41:29.954Z\", \"spec\": {\"command\": \"python dreamer.py --configs dmc_vision --task dmc_walker_walk --obs_decoder_sgs true --seed 1\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"data_count\": 0, \"model_name\": \"dreamerv3-obs-sgs\", \"seed\": 1}, \"hypothesis\": \"Obs-decoder stop-gradient on symlog (SGS) prevents CIVO in Walker by breaking the value→decoder→representation gradient pathway, keeping NVE below 1.5× baseline throughout training.\", \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/checkpoint.ckpt\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 215000, \"final_eval_return\": 726.41, \"peak_ve_ratio\": 0.8313, \"peak_ve_ratio_step\": 95000, \"peak_NVE_approx\": 1.28, \"ve_ratio_5K\": 0, \"ve_ratio_25K\": 0.1585, \"ve_ratio_45K\": 0.478, \"ve_ratio_65K\": 0.5932, \"ve_ratio_75K\": 0.5522, \"ve_ratio_85K\": 0.6419, \"ve_ratio_95K\": 0.8313, \"ve_ratio_105K\": 0.5093, \"ve_ratio_115K\": 0.4117, \"ve_ratio_125K\": 0.3476, \"ve_ratio_135K\": 0.2809, \"ve_ratio_145K\": 0.1883, \"ve_ratio_155K\": 0.1842, \"ve_ratio_165K\": 0.1099, \"ve_ratio_175K\": 0.0905, \"ve_ratio_185K\": 0.1088, \"ve_ratio_195K\": 0.2013, \"ve_ratio_205K\": 0.0725, \"ve_ratio_215K\": 0.0563, \"conclusion_detail\": \"CIVO prevented. Peak NVE ~1.28x at 95K (baseline ~0.648 interpolated), well below 1.5x threshold. ve_ratio monotonically declines from 95K onward to 0.056 at 215K. Obs-decoder SGS Walker seed 1 is 1/4 healthy prevention seed.\"}, \"completed_at\": \"2026-05-20T02:41:29.954Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:00:40.376Z\", \"updated_at\": \"2026-05-20T02:01:23.024Z\", \"hypothesis\": \"Blocking observation-decoder gradients via stop-gradient (SGS) on Walker will prevent early-onset CIVO by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/checkpoint.pt\", \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"spec\": {\"command\": \"python train.py --configs walker_obs_sgs --seed 4\", \"server\": \"bjb1-45299\", \"data_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"data_count\": 0, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 4}, \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 215000, \"final_eval_return\": 241.47, \"final_value_mean\": 34.3, \"final_ve_ratio\": 0.1421, \"peak_ve_ratio\": 6.0622, \"peak_ve_step\": 75000, \"ve_trajectory\": {\"5000\": 0, \"15000\": 0.0206, \"25000\": 0.1623, \"35000\": 0.7183, \"45000\": 0.67, \"55000\": 1.2924, \"65000\": 2.1521, \"75000\": 6.0622, \"85000\": 4.0813, \"95000\": 2.0202, \"105000\": 1.5704, \"115000\": 2.1303, \"125000\": 1.2078, \"135000\": 1.2884, \"145000\": 1.2645, \"155000\": 0.6109, \"165000\": 0.6521, \"175000\": 0.5908, \"185000\": 0.3178, \"195000\": 0.2701, \"205000\": 0.4087, \"215000\": 0.1421}, \"conclusion_detail\": \"Obs-decoder SGS failed to prevent early-onset CIVO on Walker seed 4. Severe CIVO collapse 55K-115K with peak ve_ratio=6.06 at 75K (eval crashed from 179 at 25K to 34 at 75K). Value overestimation gradually decayed through second half of training (1.26@145K → 0.14@215K) and eval eventually recovered to 241.5@215K. However, the SGS intervention did not prevent the CIVO onset — the recovery was driven by natural value decay over extended training, not by the SGS mechanism.\"}, \"completed_at\": \"2026-05-20T02:01:23.024Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:38:04.002Z\", \"updated_at\": \"2026-05-20T01:38:47.743Z\", \"hypothesis\": \"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\", \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/checkpoint.pt\", \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"spec\": {\"command\": \"python train.py --configs cheetah_obs_sgs --seed 1\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"data_count\": 0, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 1}, \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 105000, \"final_eval_return\": 38.26, \"final_value_mean\": 37.84, \"final_ve_ratio\": 0.9891, \"peak_ve_ratio\": 11.8091, \"peak_ve_step\": 75000, \"ve_trajectory\": {\"5000\": 0.0001, \"15000\": 0.0262, \"25000\": 0.0657, \"35000\": 0.1056, \"45000\": 0.979, \"55000\": 7.3924, \"65000\": 10.8375, \"75000\": 11.8091, \"85000\": 7.5096, \"95000\": 5.7255, \"105000\": 0.9891}, \"conclusion_detail\": \"Obs-decoder SGS failed on Cheetah seed 1: severe CIVO collapse 45K-95K, peak ve_ratio=11.81 at 75K. Eval_return crashed from 271.9 (35K) to 3.65 (75K). Late ve_ratio recovery to ~1.0 at 105K but eval_return (38.3) remained 86% below pre-collapse peak. Consistent with s0 result — SGS intervention is counterproductive on Cheetah, amplifying rather than suppressing CIVO.\"}, \"completed_at\": \"2026-05-20T01:38:47.743Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:32:40.958Z\", \"updated_at\": \"2026-05-20T01:33:21.724Z\", \"hypothesis\": \"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\", \"spec\": {\"command\": \"python train.py --configs cheetah_obs_sgs --seed 0\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"data_count\": 0, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 0}, \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/checkpoint.pt\", \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 105000, \"final_eval_return\": 38.76, \"final_value_mean\": 51.16, \"final_ve_ratio\": 1.3199, \"peak_ve_ratio\": 8.5607, \"peak_ve_step\": 65000, \"ve_trajectory\": {\"5000\": 0.0001, \"15000\": 0.0244, \"25000\": 0.094, \"35000\": 0.177, \"45000\": 0.3098, \"55000\": 0.9939, \"65000\": 8.5607, \"75000\": 1.2188, \"85000\": 0.9696, \"95000\": 1.486, \"105000\": 1.3199}, \"conclusion_detail\": \"Obs-decoder SGS failed on Cheetah: full CIVO collapse at 65K (ve_ratio=8.56, NVE=21.85x 5-seed normalized). Partial recovery by 75K but performance remained degraded (eval_return=38.8 vs baseline ~160). Consistent with compensatory amplification — blocking obs decoder gradient worsened CIVO vs untreated baseline (010b NVE=8.27x). SGS intervention is counterproductive on Cheetah.\"}, \"completed_at\": \"2026-05-20T01:33:21.724Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:48:33.067Z\", \"updated_at\": \"2026-05-20T00:49:00.531Z\", \"hypothesis\": \"Observation-decoder SGS regularization will prevent CIVO collapse by grounding value estimates through auxiliary reconstruction loss, maintaining healthy NVE ratios throughout training.\", \"spec\": {\"command\": \"python3 train.py --config configs/exp_025_obs_sgs_walker_s3.yaml\", \"server\": \"bjb1-45299\", \"data_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"data_count\": 215000, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 3}, \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 215000, \"eval_return_105k\": 818.58, \"ve_ratio_105k\": 0.5621, \"eval_return_135k\": 66.95, \"ve_ratio_135k\": 5.4659, \"eval_return_145k\": 43.75, \"ve_ratio_145k\": 6.8121, \"eval_return_175k\": 193.92, \"ve_ratio_175k\": 0.8274, \"eval_return_215k\": 590.17, \"ve_ratio_215k\": 0.1365, \"peak_ve_ratio\": 6.8121, \"peak_ve_step\": 145000, \"conclusion_detail\": \"Obs-decoder SGS delayed CIVO onset (healthy at 105K, NVE=0.56x) but failed to prevent late collapse (135K NVE=5.47x, peak 6.81x at 145K, partial recovery to 0.83x at 175K). Final eval_return recovered to 590 but value_mean collapsed to 80.6 (ve_ratio=0.14x). Late-onset CIVO variant.\"}, \"completed_at\": \"2026-05-20T00:49:00.531Z\"}, \"exp_001_baseline_s4_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:03:24.044Z\", \"updated_at\": \"2026-05-19T23:03:47.714Z\", \"spec\": {\"command\": \"python train.py (extended from 250k to 520k steps)\", \"server\": \"bjb1-45299\", \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/\", \"data_count\": 0, \"model_name\": \"dreamer_s4_baseline\", \"seed\": 4}, \"hypothesis\": \"Extending baseline S4 training from 250k to 520k steps will show whether eval_return plateaus or continues improving, establishing the convergence profile for NVE robustness analysis.\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/checkpoint.ckpt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/train_extended.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:03:46.304Z\", \"metrics\": {\"final_step\": 520000, \"final_eval_step\": 512000, \"final_eval_return\": 938.86, \"total_eval_checkpoints\": 52}}, \"exp_008e_v3_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:35:59.034Z\", \"updated_at\": \"2026-05-18T11:36:30.618Z\", \"metrics\": {\"eval_trajectory\": {\"5K\": 30.91, \"15K\": 343.66, \"25K\": 450.28, \"35K\": 527.44, \"45K\": 652.29, \"55K\": 717.96, \"65K\": 736.58, \"75K\": 751.73, \"85K\": 818.75, \"95K\": 835.34, \"105K\": 899.33}, \"value_trajectory\": {\"5K\": 0.002, \"15K\": 5.03, \"25K\": 46.89, \"35K\": 112.41, \"45K\": 186.9, \"55K\": 264.08, \"65K\": 343.83, \"75K\": 413.29, \"85K\": 467.89, \"95K\": 523.46, \"105K\": 547.4}, \"actor_entropy_trajectory\": {\"5K\": 8.19, \"15K\": 0.856, \"25K\": -2.478, \"35K\": -3.568, \"45K\": -4.167, \"55K\": -4.515, \"65K\": -4.7, \"75K\": -4.646, \"85K\": -5.029, \"95K\": -5.103, \"105K\": -5.084}, \"ve_ratio_trajectory\": {\"15K\": 0.0146, \"25K\": 0.1041, \"35K\": 0.2131, \"45K\": 0.2865, \"55K\": 0.3678, \"65K\": 0.4667, \"75K\": 0.5497, \"85K\": 0.5714, \"95K\": 0.6266, \"105K\": 0.6087}, \"nve_trajectory\": {\"15K\": 0.022, \"25K\": 0.16, \"35K\": 0.328, \"45K\": 0.441, \"55K\": 0.567, \"65K\": 0.719, \"75K\": 0.847, \"85K\": 0.88, \"95K\": 0.965, \"105K\": 0.938}, \"final_eval_return\": 899.33, \"peak_eval_return\": 899.33, \"peak_eval_step\": 105000, \"final_value_mean\": 547.4, \"final_ve_ratio\": 0.6087, \"final_nve\": 0.938, \"gate_dt_mean\": 1, \"gate_dt_1_frac\": 1, \"gate_dt_std\": 0, \"gate_empirical_entropy\": 0}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15 --checkpoint_every 25000\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3\", \"seed\": 4}, \"hypothesis\": \"C6 dual-pathway (trained dt_emb + subsample ON, gate_fixed_dt=1, gate_subsample_max_dt=2, H=15) will maintain stable training without value-overestimation collapse across multiple seeds on Walker Walk 105K, validating that the subsample pathway does not introduce systematic instability.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"completed_at\": \"2026-05-18T11:36:30.618Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:08:57.636Z\", \"updated_at\": \"2026-05-18T05:09:31.471Z\", \"hypothesis\": \"CIVO (value overestimation collapse) in Cheetah Run with dt_emb + subsample ON + H=8 is reproducible across seeds. Seed=0 should exhibit NVE>1.5× and eval return collapse similar to seed=1 (NVE=8.27×).\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"python train.py --config cheetah_civo_trigger --seed 0\", \"server\": \"bjb1-45299\", \"data_path\": \"dm_control/cheetah_run\", \"data_count\": 0, \"model_name\": \"dreamerv3_event_gated\", \"seed\": 0, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dm_control/cheetah_run\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T05:09:28.232Z\", \"metrics\": {\"final_step\": 112000, \"peak_eval_return\": 247.77, \"peak_eval_step\": 35000, \"final_eval_return\": 0.83, \"final_NVE\": 70.64, \"first_civo_alert_step\": 95000, \"first_civo_alert_NVE\": 6.34, \"value_mean_at_105k\": 58.58, \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"gate_dt_2_frac\": 1}}, \"exp_016d_sgs_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:29:07.960Z\", \"updated_at\": \"2026-05-16T01:43:55.477Z\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心（plan_016）。修复 eval video deadlock (D056) 后重试\", \"parent\": \"exp_008d_subsample_on_h8\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"server\": \"bjb1-45299\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"dreamerv3-sgs\", \"seed\": 1, \"checkpoint_source\": \"exp_008d_subsample_on_h8\", \"eval_data\": \"dmc_walker_walk\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:43:55.477Z\"}, \"exp_005_event_gated_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:53:45.066Z\", \"updated_at\": \"2026-05-13T21:54:17.129Z\", \"conclusion\": \"negative\", \"failure_reason\": \"结构性失败(D009): return最终47.4(baseline 5%), gate激活后return单调下降无恢复。85K/105K registry数据已修正为metrics.jsonl实际值(212.3/276.1, 旧值319.3/337.8系误录)。\", \"metrics\": {\"step\": 145000, \"final_eval_return\": 98.84, \"peak_eval_return\": 541.18, \"peak_eval_step\": 55000, \"eval_return_85K\": 212.34, \"eval_return_105K\": 276.08, \"eval_return_115K\": 25.67, \"eval_return_145K\": 98.84}, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --gate_enabled True\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3-event-gated-v4\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1\"}, \"completed_at\": \"2026-05-13T21:54:17.129Z\"}, \"exp_001_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:57:32.713Z\", \"updated_at\": \"2026-05-13T21:53:44.698Z\", \"conclusion\": \"success\", \"metrics\": {\"step\": 512000, \"final_eval_return\": 970.4, \"eval_return_last10_mean\": 950.9, \"eval_return_last10_std\": 10.5, \"fps\": 7.59}, \"spec\": {\"command\": \"python train.py --configs walker_walk --run.steps 512000\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3-baseline\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\"}, \"completed_at\": \"2026-05-13T20:58:00.944Z\"}}, \"count\": 32, \"total\": 32, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1157}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01PV6BdwVR4T1deFu2YyMJRt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
  "offset": 155,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "83efb778-7c7e-4241-8c07-3f16579ead0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kXeQeZuaw98mFsJ8UZh4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 24274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 553
      },
      "output_tokens": 66,
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

_source line 11 · 2026-05-29T00:34:24.329Z_

<details><summary>↩ Tool result · `toolu_01PV6BdwVR4T1deFu2YyMJRt`</summary>

```text
155	%% ============================================================
156	
157	\subsection{Forward-Pass Interventions}
158	\label{sec:forward_results}
159	
160	\begin{table}[t]
161	\centering
162	\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\times$ (35K+). No level reliably eliminates CIVO across environments.
163	$^\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.
164	$^\ddagger$Borderline (NVE${=}1.02\times$, eval 55\%).
165	$^\S$Policy erosion (final 15\% baseline).
166	$^\|$Walker 3/3, Cheetah 0/1.
167	$^\#$7 seeds, all NVE $< 2.0\times$.
168	$^\P$6 seeds, all NVE $< 2.0\times$.}
169	\label{tab:intervention_hierarchy}
170	\footnotesize
171	\setlength{\tabcolsep}{3pt}
172	\begin{tabular}{llccc}
173	\toprule
174	\textbf{Level} & \textbf{Intervention} & \textbf{Seeds} & \textbf{Prev.} & \textbf{Rate} \\
175	\midrule
176	--- & Untreated & 10 & 0/10 & 0\% \\
177	\midrule
178	Gradient & Reward-only SGS & 2 & 0/2 & 0\% \\
179	Gradient & Full-pathway SGS & 3 & 0/3 & 0\% \\
180	Gradient & Obs-decoder SGS & 6 & 1/6 & 17\% \\
181	\midrule
182	Output & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\% \\
183	\midrule
184	Repr. & TCN ($\sigma{=}0.1$) & 1 & 1/1$^\ddagger$ & 100\% \\
185	Repr. & TCN ($\sigma{=}0.2$) & 6$^\dagger$ & 3/6 & 50\% \\
186	Repr. & TCN ($\sigma{=}0.5$) & 3 & 1/3 & 33\% \\
187	Repr. & TCN ($\sigma{=}1.0$) & 1 & 1/1$^\S$ & 100\% \\
188	\midrule
189	Arch. & Wide single & 2 & 0/2 & 0\% \\
190	Arch. & Narrow dual (min) & 2 & 0/2 & 0\% \\
191	Arch. & Wide dual (min) & 4 & 3/4$^\|$ & 75\% \\
192	\midrule
193	--- & Embedding frozen & 7 & 7/7$^\#$ & 100\% \\
194	--- & Embedding removed & 6 & 6/6$^\P$ & 100\% \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	We test two forward-pass alternatives (Table~\ref{tab:intervention_hierarchy}). \textbf{RAVE} (value-level capping) fails because the EMA anchor tracks biased values during CIVO onset. \textbf{TCN} (representation-level noise) shows binary behavior---suppressing CIVO in 2/4 Walker seeds ($\sigma{=}0.2$) while remaining seeds escalate---and cross-environment transfer fails ($\sigma{=}1.0$ erodes Cheetah policy to 15\% of baseline; Appendix~\ref{sec:tcn_cross_env}).
200	
201	%% ============================================================
202	%% Architecture-Level Ablation
203	%% ============================================================
204	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "52414016-3725-423e-9479-cc9de8f34ac7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
      "content": "%% ============================================================\n\n\\subsection{Forward-Pass Interventions}\n\\label{sec:forward_results}\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). No level reliably eliminates CIVO across environments.\n$^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$Policy erosion (final 15\\% baseline).\n$^\\|$Walker 3/3, Cheetah 0/1.\n$^\\#$7 seeds, all NVE $< 2.0\\times$.\n$^\\P$6 seeds, all NVE $< 2.0\\times$.}\n\\label{tab:intervention_hierarchy}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\\n\\midrule\n--- & Untreated & 10 & 0/10 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% \\\\\n--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails because the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) shows binary behavior---suppressing CIVO in 2/4 Walker seeds ($\\sigma{=}0.2$) while remaining seeds escalate---and cross-environment transfer fails ($\\sigma{=}1.0$ erodes Cheetah policy to 15\\% of baseline; Appendix~\\ref{sec:tcn_cross_env}).\n\n%% ============================================================\n%% Architecture-Level Ablation\n%% ============================================================\n",
      "numLines": 50,
      "startLine": 155,
      "totalLines": 214
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
Let me read the full registry output to extract the experiment data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "18bfcd29-a9b1-45ba-a883-ff0f06331765",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeYPMgK1a9wPU6Vq5N8gUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2316,
      "cache_read_input_tokens": 24827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2316
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

Registry 数据较大，先读取完整内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "59b87977-8d84-4174-aa8d-edfd84553ce0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeYPMgK1a9wPU6Vq5N8gUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2316,
      "cache_read_input_tokens": 24827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2316
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

<details open><summary>🔧 Tool call — Read · `toolu_01FqMcDc7wQcYMKWkMWKj2pj`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/toolu_01JX9RXCDmaW6GwtGX8TK4Wh.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "de83be8c-07c5-41b1-8485-704dcc65f83f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeYPMgK1a9wPU6Vq5N8gUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2316,
      "cache_read_input_tokens": 24827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2316
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

_source line 15 · 2026-05-29T00:34:30.322Z_

<details><summary>↩ Tool result · `toolu_01FqMcDc7wQcYMKWkMWKj2pj`</summary>

```text
1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_walker_no_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T11:10:24.895Z\", \"updated_at\": \"2026-05-27T11:14:46.202Z\", \"parent\": \"exp_008f\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-51268\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"105000 steps\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"checkpoint_source\": \"none (train from scratch)\", \"eval_data\": \"dmc_walker_walk (built-in env)\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-27T11:14:46.202Z\"}, \"exp_hopper_frozen_s0_ext\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T10:47:14.544Z\", \"updated_at\": \"2026-05-27T10:48:10.979Z\", \"conclusion\": \"negative\", \"metrics\": {\"eval_return_final\": 0.56, \"eval_return_peak\": 3.58, \"eval_return_peak_step\": 85000, \"ve_ratio_final\": 15.08, \"ve_ratio_peak\": 4335664.27, \"ve_ratio_peak_step\": 105000, \"value_mean_final\": 8.46, \"civo_alerts\": 2, \"civo_alert_steps\": [65000, 105000], \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"total_steps\": 160000, \"recovery\": false}, \"spec\": {\"checkpoint_path\": \"logdir/exp_hopper_frozen_s0/latest.pt\", \"log_path\": \"logdir/exp_hopper_frozen_s0/metrics.jsonl\", \"command\": \"python train.py --config hopper_frozen_s0 --steps 160000\", \"server\": \"westd-51268\", \"data_path\": \"Hopper-v4\", \"data_count\": 160000, \"model_name\": \"dreamer_v3_frozen_dt_emb\", \"seed\": 0}, \"hypothesis\": \"Extending frozen_s0 from 105K to 150K will show eval_return recovery with ve_ratio declining, confirming frozen_s0's degenerate CIVO at 95K is transient instability during severe learning delay rather than a permanent structural failure caused by the frozen dt_embedding.\", \"completed_at\": \"2026-05-27T10:48:10.979Z\"}, \"exp_hopper_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T05:51:24.680Z\", \"updated_at\": \"2026-05-27T05:52:01.157Z\", \"metrics\": {\"step\": 105000, \"eval_final\": 96.43, \"eval_return_trajectory\": {\"5000\": 0.06, \"15000\": 1.04, \"25000\": 1.7, \"35000\": 6.55, \"45000\": 19.09, \"55000\": 22.52, \"65000\": 3.5, \"75000\": 62.2, \"85000\": 67.62, \"95000\": 86.47, \"105000\": 96.43}, \"ve_ratio_trajectory\": {\"15000\": 0.08, \"25000\": 0.098, \"35000\": 0.166, \"45000\": 0.19, \"55000\": 0.279, \"65000\": 3.479, \"75000\": 0.341, \"85000\": 0.502, \"95000\": 0.517, \"105000\": 0.559}, \"nve_peak\": 3.48, \"nve_peak_step\": 65000, \"nve_final\": 0.559, \"civo_onset\": false, \"civo_alert_count\": 0, \"value_mean_final\": 53.9, \"target_mean_final\": 54.2, \"training_steps\": 105000, \"update_count\": 25099, \"fps\": 11}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_baseline/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_baseline.log\", \"hypothesis\": \"Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE < 1.5×). Source: C1/C2 third-environment verification (D160).\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0\", \"server\": \"westd-51268\", \"data_path\": \"dmc_hopper_hop\", \"data_count\": 105000, \"model_name\": \"DreamerV3 baseline (dt=1, no gate)\", \"seed\": 0}, \"completed_at\": \"2026-05-27T05:52:01.157Z\"}, \"exp_097_cheetah_008d_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:03:25.871Z\", \"updated_at\": \"2026-05-26T11:32:48.497Z\", \"hypothesis\": \"C1 trigger seed 3: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 Cheetah 上的第四个 seed（s3）。当前 onset rate 2/3（s0 NVE=4.1×✓, s1 NVE=0.517✗, s2 NVE=138.7×✓）。s3 完成后可计算完整 onset rate（n=4）。如果 onset ≥3/4 → 高 onset rate 支持 CIVO 是 systematic phenomenon；如果 2/4 → 50% onset rate 仍有意义但需讨论。\", \"parent\": \"exp_078_cheetah_008d_s0\", \"notes\": \"重新提交到 westd-51268 cuda:0。原 bjb1 提交 (PID 324959) 已死（服务器无卡）。exp_094 同配置在 westd 跑了 1.72h 后因 SSH 断连失败，检查其 checkpoint 是否可复用。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_097_cheetah_008d_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu_ids\": [0], \"pid\": 3794, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (trained dt_emb)\", \"seed\": 3, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_097_cheetah_008d_s3/train.log\", \"checkpoint_path\": \"logdir/exp_097_cheetah_008d_s3/latest.pt\"}, \"metrics\": {\"step\": 105000, \"nve_peak\": 2.3, \"nve_peak_step\": 45000, \"nve_final\": 0.3, \"civo_onset\": true, \"civo_onset_step\": 45000, \"civo_pattern\": \"transient→degraded\", \"eval_final\": 61.7, \"eval_final_pct_baseline\": -86, \"baseline_eval_return\": 446.1, \"gate_dt_2_frac\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T11:32:48.497Z\"}, \"exp_100_walker_008a_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:39:24.456Z\", \"updated_at\": \"2026-05-26T07:52:52.927Z\", \"hypothesis\": \"Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 Walker 008a 第 2 seed。与 exp_008a_no_subsample_dt2 (s0) 和 exp_074_008a_walker_s3 (s3) 共同建立 C3 value suppression 多 seed 证据。训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练，预期无 CIVO。plan_013。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_100_walker_008a_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"server\": \"westd-51268\", \"gpu_ids\": [1], \"pid\": 5591, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (trained dt_emb, unexposed)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_100_walker_008a_s1/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_100_walker_008a_s1/latest.pt\"}, \"metrics\": {\"step\": 105000, \"eval_return_trajectory\": {\"5000\": 31, \"15000\": 168.77, \"25000\": 158.03, \"35000\": 202.91, \"45000\": 305.98, \"55000\": 457.28, \"65000\": 628.82, \"75000\": 686.98, \"85000\": 656.64, \"95000\": 717.74, \"105000\": 750.59}, \"ve_ratio_trajectory\": {\"15000\": 0.035, \"25000\": 0.206, \"35000\": 0.279, \"45000\": 0.261, \"55000\": 0.248, \"65000\": 0.234, \"75000\": 0.26, \"85000\": 0.315, \"95000\": 0.325, \"105000\": 0.328}, \"value_mean_trajectory\": {\"15000\": 5.98, \"25000\": 32.58, \"35000\": 56.55, \"45000\": 79.94, \"55000\": 113.33, \"65000\": 147.14, \"75000\": 178.73, \"85000\": 206.95, \"95000\": 233.17, \"105000\": 246.06}, \"nve_peak\": 0.328, \"nve_final\": 0.328, \"civo_onset\": false, \"eval_final\": 750.59, \"eval_final_pct_baseline\": -18, \"baseline_eval_return\": 915.67, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T07:52:45.733Z\", \"notes\": \"C3 Walker 008a s1 完成。训练正常结束(105K steps)。eval_return@105K=750.59 (baseline 915.67, -18.0%)。ve_ratio 全程 0.035-0.328，NVE_peak=0.328，远低于 τ=1.5×，civo/alert 全程 0.0，无 CIVO onset。Value suppression 确认（value_mean 持续低于 eval_return）。与 parent s0 (eval@105K=777.66, -15.1%, ve_ratio 0.37-0.54) 一致：s1 性能略低但趋势相同，两个 seed 均无 CIVO 且呈现 value suppression，C3 Walker 008a 2-seed 证据闭合。gate_dt 全程固定为 2.0 (100% dt_2_frac)，符合 gate_fixed_dt=2 配置。\"}, \"rssm_fidelity_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:47:46.584Z\", \"updated_at\": \"2026-05-26T03:47:59.871Z\", \"hypothesis\": \"RSSM fidelity v2 分析：对比 4 类模型（baseline/trained_dt_emb/no_dt_emb/frozen）在 dt=1 vs dt=2 下的 observation/reward reconstruction loss。使用 Walker checkpoint (n=800)。结果：trained_dt_emb reward ratio 1.50×, obs ratio 1.44×; baseline obs ratio 1.55×; no_dt_emb gap 最小 (1.23×/1.16×)。\", \"conclusion\": \"success\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python analyze_rssm_fidelity_v2.py --device cuda:0\", \"server\": \"westd-51268\", \"data_path\": \"Walker logdirs (exp_008d/009d/009c/084)\", \"data_count\": 800, \"model_name\": \"RSSM fidelity analysis v2\", \"seed\": 0, \"checkpoint_path\": \"analysis_rssm_fidelity_v2.json\", \"log_path\": \"N/A (analysis task)\"}, \"completed_at\": \"2026-05-26T03:47:59.871Z\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:26:00.391Z\", \"updated_at\": \"2026-05-26T03:03:45.406Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"N/A - bjb1-45299 lost GPU\", \"checkpoint_path\": \"N/A - bjb1-45299 lost GPU\", \"failure_reason\": \"bjb1-45299 server lost GPU allocation, experiment terminated\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T03:03:45.406Z\"}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:42:39.309Z\", \"updated_at\": \"2026-05-26T03:03:44.692Z\", \"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks\", \"parent\": \"exp_049\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"maniskill_StackCube-v1 (online RL)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, StackCube s0)\", \"seed\": 0, \"log_path\": \"N/A - bjb1-45299 lost GPU\", \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"maniskill_StackCube-v1 (online eval)\", \"checkpoint_path\": \"N/A - bjb1-45299 lost GPU\", \"failure_reason\": \"bjb1-45299 server lost GPU allocation, experiment terminated\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T03:03:44.692Z\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:14:38.578Z\", \"updated_at\": \"2026-05-26T03:03:42.946Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion（Walker/Cheetah）推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack），比 PickCube 更难。如果触发 CIVO → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"parent\": \"exp_048_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"N/A - bjb1-45299 lost GPU\", \"checkpoint_path\": \"N/A - bjb1-45299 lost GPU\", \"failure_reason\": \"bjb1-45299 server lost GPU allocation, experiment terminated\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T03:03:42.946Z\"}, \"exp_081_008e_v3_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T15:42:24.765Z\", \"updated_at\": \"2026-05-25T15:43:10.949Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 597.1, \"vs_baseline\": \"-34.8%\", \"vs_baseline_pct\": 65.2, \"baseline_105K\": 915.67, \"ve_ratio_peak\": 0.6, \"ve_ratio_final\": 0.5, \"NVE_est_peak\": 0.8, \"NVE_est_final\": 0.7, \"gate_dt_mean\": 1, \"gate_dt_1_frac\": 1, \"civo_alert_count\": 0, \"training_steps\": 105000, \"update_count\": 25099, \"value_mean_final\": 295}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_081_008e_v3_walker_s2/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"spec\": {\"command\": \"python train.py --config 008e_v3 --env walker_walk --seed 2\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3_008e_v3\", \"seed\": 2}, \"hypothesis\": \"Trained dt_emb with dt=1 imagination and subsample ON (max_dt=2) does not trigger CIVO in Walker Walk, as the value function sees only single-step predictions that match the world model's training distribution, preventing value inflation even with learned temporal embeddings.\", \"completed_at\": \"2026-05-25T15:43:10.949Z\"}, \"exp_073_008f_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:52:07.413Z\", \"updated_at\": \"2026-05-25T09:52:34.845Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 289.3, \"eval_return_peak\": 486.5, \"eval_return_peak_step\": 75000, \"ve_ratio_max\": 0.5, \"civo_alert_max\": 0, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"total_env_steps\": 112000, \"total_updates\": 25099}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_073_008f_walker_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\", \"spec\": {\"command\": \"python train.py --config 008f --seed 4\", \"server\": \"westd-19154\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamer_v3_008f\", \"seed\": 4}, \"hypothesis\": \"Removing dt_embedding (dt_embed_dim=0) in the 008f control config prevents CIVO onset because the agent cannot form temporally-conditioned value predictions that compound imagination-driven overestimation. With fixed dt=2 and no temporal embedding, value error ratio should remain below the 1.5x CIVO threshold across seeds.\", \"completed_at\": \"2026-05-25T09:52:34.845Z\"}, \"exp_069_008f_walker_repro_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:20:25.632Z\", \"updated_at\": \"2026-05-25T07:21:13.407Z\", \"hypothesis\": \"Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk. With no learned temporal embedding, the value network cannot develop the compounding overestimation pattern that causes CIVO collapse. This seed=1 run extends the evidence from exp_008f (seed=0).\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"spec\": {\"command\": \"python train.py --configs dmc_vision --task dmc_walker_walk --seed 1 --logdir logdir/exp_069_008f_walker_repro_s1\", \"server\": \"westd-19154\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 0, \"model_name\": \"dreamerv2_no_dt_embed_h8\", \"seed\": 1, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_walker_walk_online\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_069_008f_walker_repro_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T07:20:58.159Z\", \"metrics\": {\"eval_return_final\": 237.8, \"eval_return_final_step\": 105000, \"eval_return_peak\": 390.1, \"eval_return_peak_step\": 95000, \"steps_completed\": 112000, \"eval_steps\": 105000, \"civo_triggered\": false, \"civo_alert_count\": 0, \"ve_ratio_max\": 0.447, \"ve_ratio_max_step\": 105000, \"ve_ratio_final\": 0.447, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"value_mean_final\": 106.3, \"target_mean_final\": 106.4, \"value_loss_final\": 0.99, \"seed\": 1, \"eval_return_trajectory\": {\"5K\": 30.5, \"15K\": 158.7, \"25K\": 180.8, \"35K\": 250.3, \"45K\": 293.6, \"55K\": 272.2, \"65K\": 328.1, \"75K\": 244.8, \"85K\": 382.5, \"95K\": 390.1, \"105K\": 237.8}, \"ve_ratio_trajectory\": {\"15K\": 0.021, \"25K\": 0.111, \"35K\": 0.171, \"95K\": 0.275, \"105K\": 0.447}, \"note\": \"C2 causal control: no dt_embedding, fixed dt=2. No CIVO triggered. ve_ratio stayed <0.5 throughout. Late eval dip (390→238) is normal Walker variance, not CIVO-driven (value_mean≈target_mean, no overestimation).\"}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:16:11.755Z\", \"updated_at\": \"2026-05-23T23:34:24.080Z\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1.log\"}, \"hypothesis\": \"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，162.5K 时仍 1.94）。如果 s1 也触发持续 CIVO → PegInsertion 是最严重的 CIVO 环境（比 StackCube 自修复更难），支持 severity-dependent narrative；如果不触发 → seed-specific 异常。\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"checkpoint_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/latest.pt\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1.log\", \"metrics\": {\"total_steps\": 222400, \"ve_ratio_max\": 3.08, \"ve_ratio_max_step\": 92500, \"ve_ratio_final\": 0.5, \"ve_ratio_final_step\": 212500, \"eval_peak\": 24.05, \"eval_peak_step\": 112500, \"eval_final\": 11.44, \"eval_final_step\": 212500, \"civo_triggered\": true, \"civo_self_corrected\": \"partial\", \"civo_onset_step\": 32500, \"civo_peak_step\": 92500, \"ve_ratio_trajectory\": {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}, \"eval_trajectory\": {\"2500\": 2.01, \"12500\": 10.12, \"22500\": 11.47, \"32500\": 12.01, \"42500\": 10.13, \"52500\": 10.31, \"62500\": 9.02, \"72500\": 10.07, \"82500\": 8.78, \"92500\": 7.24, \"102500\": 9.2, \"112500\": 24.05, \"122500\": 16.46, \"132500\": 13.15, \"142500\": 20.44, \"152500\": 23.4, \"162500\": 9.07, \"172500\": 9.46, \"182500\": 8.51, \"192500\": 7.81, \"202500\": 8.58, \"212500\": 11.44}, \"note\": \"CIVO triggered (ve_ratio 3.08@92.5K), less severe than s0 (10.05). Partial self-correction to 0.50 by 212.5K. Eval poor throughout (~10-24), PegInsertion is hard task.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T23:34:24.080Z\"}, \"exp_048_cheetah_civo_extension\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:40.050Z\", \"updated_at\": \"2026-05-22T21:17:46.852Z\", \"hypothesis\": \"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → \\\"severity determines recoverability\\\" narrative, strongest paper defense. If it does → CIVO is universally transient regardless of severity.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}, \"metrics\": {\"eval_final\": 23.423, \"eval_peak\": 32.835, \"eval_peak_step\": 252000, \"ve_ratio_initial_measured\": 6.135, \"ve_ratio_initial_measured_step\": 122000, \"ve_ratio_inherited_from_exp010b\": 46.34, \"ve_ratio_peak_in_run\": 24.112, \"ve_ratio_peak_step\": 162000, \"ve_ratio_final\": 1.803, \"nve_inherited\": 70.64, \"nve_peak_in_run\": 36.76, \"nve_final\": 2.75, \"baseline_ve_ratio\": 0.656, \"total_steps\": 312000, \"last_eval_step\": 302000, \"civo_self_corrected\": \"partial\", \"civo_reduction_pct\": 96.1, \"civo_correction_duration_steps\": 197000, \"gate_collapsed\": true, \"gate_dt_final\": 2, \"gate_dt_2_frac_final\": 1}, \"checkpoint_path\": \"logdir/exp_048_cheetah_civo_extension/checkpoint_302000.pt\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:17:46.852Z\"}, \"exp_047_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:42:12.914Z\", \"updated_at\": \"2026-05-22T19:01:30.894Z\", \"hypothesis\": \"Freezing dt_emb in Walker Walk (seed 1) prevents sustained CIVO collapse, replicating exp_042 (seed 0, NVE=0.19) finding that removing dt conditioning blocks the overestimation feedback loop\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 282452, \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\"}, \"metrics\": {\"eval_peak\": 408.79, \"eval_peak_step\": 125000, \"eval_final\": 144.22, \"eval_final_step\": 215000, \"ve_ratio_peak\": 1.099, \"ve_ratio_peak_step\": 75000, \"ve_ratio_final\": 0.277, \"nve_peak\": 1.71, \"nve_peak_step\": 95000, \"nve_final_105k\": 0.56, \"total_steps\": 225000, \"note\": \"Transient NVE>1.5x at 75K-95K with full self-correction by 105K. Late eval decline (408->144) NOT CIVO-driven (ve_ratio=0.28). No sustained collapse.\"}, \"checkpoint_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:50:46.948Z\"}, \"exp_046_frozen_dt_emb_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:40:43.182Z\", \"updated_at\": \"2026-05-22T18:32:34.105Z\", \"hypothesis\": \"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation. Source: D133 + exp_042 result + R1-N4 cross-environment concern.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 281513, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_046_frozen_dt_emb_cheetah/train.log\"}, \"metrics\": {\"eval_final\": 150.5, \"eval_peak\": 207.4, \"eval_peak_step\": 145000, \"ve_ratio_peak\": 0.4, \"ve_ratio_final\": 0.1, \"nve_peak\": 1.35, \"nve_peak_step\": 45000, \"nve_final\": 0.17, \"total_steps\": 224000, \"civo_alert_count\": 0, \"eval_trajectory\": \"5K:8.3, 15K:110, 35K:160, 95K:181, 105K:206, 115K:46, 145K:207, 155K:161, 215K:150.5\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:31:00.933Z\"}, \"exp_048_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:44:55.613Z\", \"updated_at\": \"2026-05-22T17:14:16.564Z\", \"hypothesis\": \"ManiSkill Phase 1 scout: CIVO trigger config (trained dt_emb + subsample ON + H=8) on StackCube-v1 manipulation task. Tests whether CIVO generalizes beyond locomotion (Walker/Cheetah) to manipulation domains. exp_019b showed transient CIVO on PickCube; StackCube is harder (multi-stage). If CIVO triggers → extends cross-domain evidence; if not → supports locomotion-specific scope.\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 87609, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"/tmp/exp_048.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-22T17:14:16.564Z\"}, \"exp_045_treatment_extension_008d_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:40:52.894Z\", \"updated_at\": \"2026-05-22T15:44:50.990Z\", \"hypothesis\": \"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 70945, \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}, \"metrics\": {\"eval_final\": 867.6, \"eval_peak\": 869.7, \"eval_peak_step\": 242000, \"ve_ratio_final\": 0.05, \"ve_ratio_peak\": 4.91, \"ve_ratio_peak_step\": 132000, \"nve_final\": 0.052, \"total_steps\": 312000, \"self_correction_onset\": 142000, \"finding\": \"CIVO self-correction: ve_ratio 4.91→0.05, eval 35→868 over 170K steps\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\", \"completed_at\": \"2026-05-22T15:44:50.990Z\"}, \"exp_036_dual_critic_pickcube\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T19:45:02.066Z\", \"updated_at\": \"2026-05-21T19:45:46.721Z\", \"spec\": {\"command\": \"python train.py --task ManiSkill_PickCube-v1 --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 0 --steps 200000\", \"server\": \"bjb1-45299\", \"data_path\": \"ManiSkill_PickCube-v1\", \"data_count\": 0, \"model_name\": \"dreamerv3_dual_critic\", \"seed\": 0}, \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"parent\": \"exp_032_dual_critic_walker\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_036_dual_critic_pickcube\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 212447, \"total_env_steps\": 212447, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"eval_return_peak_step\": 202500, \"ve_ratio_peak\": 2.3, \"ve_ratio_peak_step\": 32500, \"ve_ratio_final\": 0.2, \"civo_alerts\": 0, \"v1_v2_max_divergence\": 0, \"v1_v2_correlated\": true, \"CIVO_prevented\": \"vacuous_no_civo_in_baseline\", \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"exit_code\": 0, \"eval_return_trajectory\": {\"2.5K\": 2, \"12.5K\": 17.5, \"22.5K\": 17.5, \"32.5K\": 11.6, \"42.5K\": 15.6, \"52.5K\": 11.7, \"62.5K\": 18.8, \"72.5K\": 5.4, \"82.5K\": 22.5, \"92.5K\": 18.1, \"102.5K\": 8.4, \"112.5K\": 7.1, \"122.5K\": 9.1, \"132.5K\": 12.8, \"142.5K\": 14, \"152.5K\": 13.1, \"162.5K\": 16.2, \"172.5K\": 19.7, \"182.5K\": 16.8, \"192.5K\": 13.7, \"202.5K\": 27.7}, \"ve_ratio_trajectory\": {\"12.5K\": 0.2, \"22.5K\": 1, \"32.5K\": 2.3, \"42.5K\": 1.4, \"52.5K\": 1.4, \"62.5K\": 0.6, \"72.5K\": 1.6, \"82.5K\": 0.3, \"92.5K\": 0.3, \"102.5K\": 0.6, \"112.5K\": 0.7, \"122.5K\": 0.5, \"132.5K\": 0.4, \"142.5K\": 0.3, \"152.5K\": 0.4, \"162.5K\": 0.3, \"172.5K\": 0.3, \"182.5K\": 0.3, \"192.5K\": 0.4, \"202.5K\": 0.2}, \"value1_mean_trajectory\": {\"2.5K\": 0, \"12.5K\": 3.8, \"22.5K\": 17.9, \"32.5K\": 26.9, \"42.5K\": 21.2, \"52.5K\": 16.1, \"62.5K\": 11.6, \"72.5K\": 8.7, \"82.5K\": 7.2, \"92.5K\": 6, \"102.5K\": 5.3, \"112.5K\": 5.1, \"122.5K\": 5, \"132.5K\": 4.9, \"142.5K\": 4.9, \"152.5K\": 5.3, \"162.5K\": 5.7, \"172.5K\": 5.6, \"182.5K\": 5.6, \"192.5K\": 5.6, \"202.5K\": 5.8}, \"baseline_comparison\": {\"exp_019a_v2_vanilla_baseline_final\": 58.6, \"exp_019b_civo_config_baseline_final\": 26.6, \"exp_031_tcn_sigma02_final\": 17.2, \"exp_031b_tcn_sigma05_final\": 25.5}, \"conclusion_detail\": \"CIVO never manifested on PickCube (with or without dual-critic). ve_ratio peaked at 2.3 early (32.5K) and self-corrected — same pattern as TCN experiments (peak 3.7, 3.3). Eval 27.7 is indistinguishable from CIVO-config baseline (26.6). The subsample+dt_emb config itself degrades PickCube from 58.6 to ~27, and dual-critic does not recover this gap. Hypothesis rejected: PickCube is CIVO-immune at this training scale, making it a poor test for intervention generality.\"}, \"completed_at\": \"2026-05-21T19:45:46.721Z\"}, \"exp_034_dual_critic_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:09:08.035Z\", \"updated_at\": \"2026-05-21T12:09:56.881Z\", \"metrics\": {\"final_step\": 215000, \"total_env_steps\": 224000, \"eval_return_peak\": 315.7, \"eval_return_peak_step\": 45000, \"eval_return_final\": 97.5, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 0.1, \"civo_alerts\": 2, \"civo_alert_steps\": [95000, 105000], \"v1_v2_correlated\": true, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"exit_code\": 0, \"eval_return_trajectory\": {\"5K\": 8.3, \"15K\": 27.8, \"25K\": 108.7, \"35K\": 110, \"45K\": 315.7, \"55K\": 34.5, \"65K\": 81.5, \"75K\": 183, \"85K\": 88.4, \"95K\": 41, \"105K\": 27.2, \"115K\": 45.9, \"125K\": 58.7, \"135K\": 71.6, \"145K\": 61.9, \"155K\": 52.1, \"165K\": 153.8, \"175K\": 104.9, \"185K\": 101.4, \"195K\": 115.3, \"205K\": 101.5, \"215K\": 97.5}, \"ve_ratio_trajectory\": {\"15K\": 0.1, \"25K\": 0.1, \"35K\": 0.2, \"45K\": 0.1, \"55K\": 1.8, \"65K\": 0.7, \"75K\": 0.3, \"85K\": 0.5, \"95K\": 1, \"105K\": 1.6, \"115K\": 0.9, \"125K\": 0.6, \"135K\": 0.4, \"145K\": 0.4, \"155K\": 0.4, \"165K\": 0.1, \"175K\": 0.2, \"185K\": 0.2, \"195K\": 0.1, \"205K\": 0.1, \"215K\": 0.1}, \"value1_mean_trajectory\": {\"15K\": 1.8, \"25K\": 10.9, \"35K\": 23.7, \"45K\": 39, \"55K\": 60.5, \"65K\": 59.3, \"75K\": 52.6, \"85K\": 46.7, \"95K\": 41.7, \"105K\": 43.4, \"115K\": 39.3, \"125K\": 33.8, \"135K\": 28.5, \"145K\": 24.6, \"155K\": 21.5, \"165K\": 19.2, \"175K\": 17.8, \"185K\": 16.7, \"195K\": 15.7, \"205K\": 14.8, \"215K\": 14.2}, \"conclusion_detail\": \"CIVO triggered but partially mitigated. Two CIVO alerts (95K, 105K), peak ve_ratio=1.8 at 55K. Eval crashed from peak 315.7 to 27.2 (105K), recovered to 97.5. Dual-critic provided 40x reduction in overestimation vs baseline (ve_ratio 1.8 vs NVE 70.64) and prevented catastrophic collapse (eval 97.5 vs 0.83). But CIVO not fully suppressed — hypothesis of cross-environment generality not supported. v1≈v2 throughout (no critic disagreement).\"}, \"conclusion\": \"negative\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_034_dual_critic_cheetah --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --dual_critic True\", \"server\": \"bjb1-45299\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 0, \"model_name\": \"dreamerv3_dual_critic\", \"seed\": 0, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/checkpoint.pt\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_cheetah_run\"}, \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"parent\": \"exp_032_dual_critic_walker\", \"completed_at\": \"2026-05-21T12:09:56.881Z\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:43:05.327Z\", \"updated_at\": \"2026-05-21T03:38:07.906Z\", \"metrics\": {\"final_step\": 215000, \"total_env_steps\": 224000, \"eval_return_final\": 104.5, \"eval_return_peak\": 349.6, \"eval_return_peak_step\": 95000, \"eval_return_105K\": 71.8, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 3, \"ve_ratio_peak_step\": 105000, \"civo_blowup\": true, \"civo_blowup_step\": 105000, \"eval_return_trajectory\": {\"5K\": 31.7, \"15K\": 159.1, \"25K\": 155.7, \"35K\": 190.8, \"45K\": 137.1, \"55K\": 210.7, \"65K\": 189.5, \"75K\": 253.2, \"85K\": 259.5, \"95K\": 349.6, \"105K\": 71.8, \"115K\": 69.8, \"125K\": 61.5, \"135K\": 141.8, \"145K\": 98.7, \"155K\": 88.9, \"165K\": 86.2, \"175K\": 123.5, \"185K\": 153.7, \"195K\": 68.8, \"205K\": 63.7, \"215K\": 104.5}, \"ve_ratio_trajectory\": {\"15K\": 0, \"25K\": 0.2, \"35K\": 0.3, \"45K\": 0.7, \"55K\": 0.6, \"65K\": 0.9, \"75K\": 0.8, \"85K\": 0.9, \"95K\": 0.7, \"105K\": 3, \"115K\": 2.5, \"125K\": 2.4, \"135K\": 0.9, \"145K\": 1.1, \"155K\": 1.1, \"165K\": 0.9, \"175K\": 0.6, \"185K\": 0.4, \"195K\": 0.8, \"205K\": 0.7, \"215K\": 0.4}, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python train.py --config walker_walk_tcn --seed 3 --tcn_sigma 0.2\", \"server\": \"bjb1-40020\", \"data_path\": \"walker_walk\", \"data_count\": 0, \"model_name\": \"dreamer_tcn_sigma02\", \"seed\": 3}, \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"completed_at\": \"2026-05-21T03:38:07.906Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:40:59.914Z\", \"updated_at\": \"2026-05-20T02:41:29.954Z\", \"spec\": {\"command\": \"python dreamer.py --configs dmc_vision --task dmc_walker_walk --obs_decoder_sgs true --seed 1\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"data_count\": 0, \"model_name\": \"dreamerv3-obs-sgs\", \"seed\": 1}, \"hypothesis\": \"Obs-decoder stop-gradient on symlog (SGS) prevents CIVO in Walker by breaking the value→decoder→representation gradient pathway, keeping NVE below 1.5× baseline throughout training.\", \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/checkpoint.ckpt\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 215000, \"final_eval_return\": 726.41, \"peak_ve_ratio\": 0.8313, \"peak_ve_ratio_step\": 95000, \"peak_NVE_approx\": 1.28, \"ve_ratio_5K\": 0, \"ve_ratio_25K\": 0.1585, \"ve_ratio_45K\": 0.478, \"ve_ratio_65K\": 0.5932, \"ve_ratio_75K\": 0.5522, \"ve_ratio_85K\": 0.6419, \"ve_ratio_95K\": 0.8313, \"ve_ratio_105K\": 0.5093, \"ve_ratio_115K\": 0.4117, \"ve_ratio_125K\": 0.3476, \"ve_ratio_135K\": 0.2809, \"ve_ratio_145K\": 0.1883, \"ve_ratio_155K\": 0.1842, \"ve_ratio_165K\": 0.1099, \"ve_ratio_175K\": 0.0905, \"ve_ratio_185K\": 0.1088, \"ve_ratio_195K\": 0.2013, \"ve_ratio_205K\": 0.0725, \"ve_ratio_215K\": 0.0563, \"conclusion_detail\": \"CIVO prevented. Peak NVE ~1.28x at 95K (baseline ~0.648 interpolated), well below 1.5x threshold. ve_ratio monotonically declines from 95K onward to 0.056 at 215K. Obs-decoder SGS Walker seed 1 is 1/4 healthy prevention seed.\"}, \"completed_at\": \"2026-05-20T02:41:29.954Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:00:40.376Z\", \"updated_at\": \"2026-05-20T02:01:23.024Z\", \"hypothesis\": \"Blocking observation-decoder gradients via stop-gradient (SGS) on Walker will prevent early-onset CIVO by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/checkpoint.pt\", \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"spec\": {\"command\": \"python train.py --configs walker_obs_sgs --seed 4\", \"server\": \"bjb1-45299\", \"data_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"data_count\": 0, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 4}, \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 215000, \"final_eval_return\": 241.47, \"final_value_mean\": 34.3, \"final_ve_ratio\": 0.1421, \"peak_ve_ratio\": 6.0622, \"peak_ve_step\": 75000, \"ve_trajectory\": {\"5000\": 0, \"15000\": 0.0206, \"25000\": 0.1623, \"35000\": 0.7183, \"45000\": 0.67, \"55000\": 1.2924, \"65000\": 2.1521, \"75000\": 6.0622, \"85000\": 4.0813, \"95000\": 2.0202, \"105000\": 1.5704, \"115000\": 2.1303, \"125000\": 1.2078, \"135000\": 1.2884, \"145000\": 1.2645, \"155000\": 0.6109, \"165000\": 0.6521, \"175000\": 0.5908, \"185000\": 0.3178, \"195000\": 0.2701, \"205000\": 0.4087, \"215000\": 0.1421}, \"conclusion_detail\": \"Obs-decoder SGS failed to prevent early-onset CIVO on Walker seed 4. Severe CIVO collapse 55K-115K with peak ve_ratio=6.06 at 75K (eval crashed from 179 at 25K to 34 at 75K). Value overestimation gradually decayed through second half of training (1.26@145K → 0.14@215K) and eval eventually recovered to 241.5@215K. However, the SGS intervention did not prevent the CIVO onset — the recovery was driven by natural value decay over extended training, not by the SGS mechanism.\"}, \"completed_at\": \"2026-05-20T02:01:23.024Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:38:04.002Z\", \"updated_at\": \"2026-05-20T01:38:47.743Z\", \"hypothesis\": \"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\", \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/checkpoint.pt\", \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"spec\": {\"command\": \"python train.py --configs cheetah_obs_sgs --seed 1\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"data_count\": 0, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 1}, \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 105000, \"final_eval_return\": 38.26, \"final_value_mean\": 37.84, \"final_ve_ratio\": 0.9891, \"peak_ve_ratio\": 11.8091, \"peak_ve_step\": 75000, \"ve_trajectory\": {\"5000\": 0.0001, \"15000\": 0.0262, \"25000\": 0.0657, \"35000\": 0.1056, \"45000\": 0.979, \"55000\": 7.3924, \"65000\": 10.8375, \"75000\": 11.8091, \"85000\": 7.5096, \"95000\": 5.7255, \"105000\": 0.9891}, \"conclusion_detail\": \"Obs-decoder SGS failed on Cheetah seed 1: severe CIVO collapse 45K-95K, peak ve_ratio=11.81 at 75K. Eval_return crashed from 271.9 (35K) to 3.65 (75K). Late ve_ratio recovery to ~1.0 at 105K but eval_return (38.3) remained 86% below pre-collapse peak. Consistent with s0 result — SGS intervention is counterproductive on Cheetah, amplifying rather than suppressing CIVO.\"}, \"completed_at\": \"2026-05-20T01:38:47.743Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:32:40.958Z\", \"updated_at\": \"2026-05-20T01:33:21.724Z\", \"hypothesis\": \"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\", \"spec\": {\"command\": \"python train.py --configs cheetah_obs_sgs --seed 0\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"data_count\": 0, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 0}, \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/checkpoint.pt\", \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 105000, \"final_eval_return\": 38.76, \"final_value_mean\": 51.16, \"final_ve_ratio\": 1.3199, \"peak_ve_ratio\": 8.5607, \"peak_ve_step\": 65000, \"ve_trajectory\": {\"5000\": 0.0001, \"15000\": 0.0244, \"25000\": 0.094, \"35000\": 0.177, \"45000\": 0.3098, \"55000\": 0.9939, \"65000\": 8.5607, \"75000\": 1.2188, \"85000\": 0.9696, \"95000\": 1.486, \"105000\": 1.3199}, \"conclusion_detail\": \"Obs-decoder SGS failed on Cheetah: full CIVO collapse at 65K (ve_ratio=8.56, NVE=21.85x 5-seed normalized). Partial recovery by 75K but performance remained degraded (eval_return=38.8 vs baseline ~160). Consistent with compensatory amplification — blocking obs decoder gradient worsened CIVO vs untreated baseline (010b NVE=8.27x). SGS intervention is counterproductive on Cheetah.\"}, \"completed_at\": \"2026-05-20T01:33:21.724Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:48:33.067Z\", \"updated_at\": \"2026-05-20T00:49:00.531Z\", \"hypothesis\": \"Observation-decoder SGS regularization will prevent CIVO collapse by grounding value estimates through auxiliary reconstruction loss, maintaining healthy NVE ratios throughout training.\", \"spec\": {\"command\": \"python3 train.py --config configs/exp_025_obs_sgs_walker_s3.yaml\", \"server\": \"bjb1-45299\", \"data_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"data_count\": 215000, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 3}, \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 215000, \"eval_return_105k\": 818.58, \"ve_ratio_105k\": 0.5621, \"eval_return_135k\": 66.95, \"ve_ratio_135k\": 5.4659, \"eval_return_145k\": 43.75, \"ve_ratio_145k\": 6.8121, \"eval_return_175k\": 193.92, \"ve_ratio_175k\": 0.8274, \"eval_return_215k\": 590.17, \"ve_ratio_215k\": 0.1365, \"peak_ve_ratio\": 6.8121, \"peak_ve_step\": 145000, \"conclusion_detail\": \"Obs-decoder SGS delayed CIVO onset (healthy at 105K, NVE=0.56x) but failed to prevent late collapse (135K NVE=5.47x, peak 6.81x at 145K, partial recovery to 0.83x at 175K). Final eval_return recovered to 590 but value_mean collapsed to 80.6 (ve_ratio=0.14x). Late-onset CIVO variant.\"}, \"completed_at\": \"2026-05-20T00:49:00.531Z\"}, \"exp_001_baseline_s4_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:03:24.044Z\", \"updated_at\": \"2026-05-19T23:03:47.714Z\", \"spec\": {\"command\": \"python train.py (extended from 250k to 520k steps)\", \"server\": \"bjb1-45299\", \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/\", \"data_count\": 0, \"model_name\": \"dreamer_s4_baseline\", \"seed\": 4}, \"hypothesis\": \"Extending baseline S4 training from 250k to 520k steps will show whether eval_return plateaus or continues improving, establishing the convergence profile for NVE robustness analysis.\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/checkpoint.ckpt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/train_extended.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:03:46.304Z\", \"metrics\": {\"final_step\": 520000, \"final_eval_step\": 512000, \"final_eval_return\": 938.86, \"total_eval_checkpoints\": 52}}, \"exp_008e_v3_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:35:59.034Z\", \"updated_at\": \"2026-05-18T11:36:30.618Z\", \"metrics\": {\"eval_trajectory\": {\"5K\": 30.91, \"15K\": 343.66, \"25K\": 450.28, \"35K\": 527.44, \"45K\": 652.29, \"55K\": 717.96, \"65K\": 736.58, \"75K\": 751.73, \"85K\": 818.75, \"95K\": 835.34, \"105K\": 899.33}, \"value_trajectory\": {\"5K\": 0.002, \"15K\": 5.03, \"25K\": 46.89, \"35K\": 112.41, \"45K\": 186.9, \"55K\": 264.08, \"65K\": 343.83, \"75K\": 413.29, \"85K\": 467.89, \"95K\": 523.46, \"105K\": 547.4}, \"actor_entropy_trajectory\": {\"5K\": 8.19, \"15K\": 0.856, \"25K\": -2.478, \"35K\": -3.568, \"45K\": -4.167, \"55K\": -4.515, \"65K\": -4.7, \"75K\": -4.646, \"85K\": -5.029, \"95K\": -5.103, \"105K\": -5.084}, \"ve_ratio_trajectory\": {\"15K\": 0.0146, \"25K\": 0.1041, \"35K\": 0.2131, \"45K\": 0.2865, \"55K\": 0.3678, \"65K\": 0.4667, \"75K\": 0.5497, \"85K\": 0.5714, \"95K\": 0.6266, \"105K\": 0.6087}, \"nve_trajectory\": {\"15K\": 0.022, \"25K\": 0.16, \"35K\": 0.328, \"45K\": 0.441, \"55K\": 0.567, \"65K\": 0.719, \"75K\": 0.847, \"85K\": 0.88, \"95K\": 0.965, \"105K\": 0.938}, \"final_eval_return\": 899.33, \"peak_eval_return\": 899.33, \"peak_eval_step\": 105000, \"final_value_mean\": 547.4, \"final_ve_ratio\": 0.6087, \"final_nve\": 0.938, \"gate_dt_mean\": 1, \"gate_dt_1_frac\": 1, \"gate_dt_std\": 0, \"gate_empirical_entropy\": 0}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15 --checkpoint_every 25000\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3\", \"seed\": 4}, \"hypothesis\": \"C6 dual-pathway (trained dt_emb + subsample ON, gate_fixed_dt=1, gate_subsample_max_dt=2, H=15) will maintain stable training without value-overestimation collapse across multiple seeds on Walker Walk 105K, validating that the subsample pathway does not introduce systematic instability.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"completed_at\": \"2026-05-18T11:36:30.618Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:08:57.636Z\", \"updated_at\": \"2026-05-18T05:09:31.471Z\", \"hypothesis\": \"CIVO (value overestimation collapse) in Cheetah Run with dt_emb + subsample ON + H=8 is reproducible across seeds. Seed=0 should exhibit NVE>1.5× and eval return collapse similar to seed=1 (NVE=8.27×).\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"python train.py --config cheetah_civo_trigger --seed 0\", \"server\": \"bjb1-45299\", \"data_path\": \"dm_control/cheetah_run\", \"data_count\": 0, \"model_name\": \"dreamerv3_event_gated\", \"seed\": 0, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dm_control/cheetah_run\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T05:09:28.232Z\", \"metrics\": {\"final_step\": 112000, \"peak_eval_return\": 247.77, \"peak_eval_step\": 35000, \"final_eval_return\": 0.83, \"final_NVE\": 70.64, \"first_civo_alert_step\": 95000, \"first_civo_alert_NVE\": 6.34, \"value_mean_at_105k\": 58.58, \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"gate_dt_2_frac\": 1}}, \"exp_016d_sgs_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:29:07.960Z\", \"updated_at\": \"2026-05-16T01:43:55.477Z\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心（plan_016）。修复 eval video deadlock (D056) 后重试\", \"parent\": \"exp_008d_subsample_on_h8\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"server\": \"bjb1-45299\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"dreamerv3-sgs\", \"seed\": 1, \"checkpoint_source\": \"exp_008d_subsample_on_h8\", \"eval_data\": \"dmc_walker_walk\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:43:55.477Z\"}, \"exp_005_event_gated_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:53:45.066Z\", \"updated_at\": \"2026-05-13T21:54:17.129Z\", \"conclusion\": \"negative\", \"failure_reason\": \"结构性失败(D009): return最终47.4(baseline 5%), gate激活后return单调下降无恢复。85K/105K registry数据已修正为metrics.jsonl实际值(212.3/276.1, 旧值319.3/337.8系误录)。\", \"metrics\": {\"step\": 145000, \"final_eval_return\": 98.84, \"peak_eval_return\": 541.18, \"peak_eval_step\": 55000, \"eval_return_85K\": 212.34, \"eval_return_105K\": 276.08, \"eval_return_115K\": 25.67, \"eval_return_145K\": 98.84}, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --gate_enabled True\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3-event-gated-v4\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1\"}, \"completed_at\": \"2026-05-13T21:54:17.129Z\"}, \"exp_001_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:57:32.713Z\", \"updated_at\": \"2026-05-13T21:53:44.698Z\", \"conclusion\": \"success\", \"metrics\": {\"step\": 512000, \"final_eval_return\": 970.4, \"eval_return_last10_mean\": 950.9, \"eval_return_last10_std\": 10.5, \"fps\": 7.59}, \"spec\": {\"command\": \"python train.py --configs walker_walk --run.steps 512000\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3-baseline\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\"}, \"completed_at\": \"2026-05-13T20:58:00.944Z\"}}, \"count\": 32, \"total\": 32, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1157}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "0ad4272a-ec9a-4b61-896e-ec070ba03481",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/toolu_01JX9RXCDmaW6GwtGX8TK4Wh.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_walker_no_dt_emb_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T11:10:24.895Z\\\", \\\"updated_at\\\": \\\"2026-05-27T11:14:46.202Z\\\", \\\"parent\\\": \\\"exp_008f\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"105000 steps\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"none (train from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (built-in env)\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-27T11:14:46.202Z\\\"}, \\\"exp_hopper_frozen_s0_ext\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T10:47:14.544Z\\\", \\\"updated_at\\\": \\\"2026-05-27T10:48:10.979Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 0.56, \\\"eval_return_peak\\\": 3.58, \\\"eval_return_peak_step\\\": 85000, \\\"ve_ratio_final\\\": 15.08, \\\"ve_ratio_peak\\\": 4335664.27, \\\"ve_ratio_peak_step\\\": 105000, \\\"value_mean_final\\\": 8.46, \\\"civo_alerts\\\": 2, \\\"civo_alert_steps\\\": [65000, 105000], \\\"gate_dt_mean\\\": 2, \\\"gate_entropy\\\": 0, \\\"total_steps\\\": 160000, \\\"recovery\\\": false}, \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_hopper_frozen_s0/latest.pt\\\", \\\"log_path\\\": \\\"logdir/exp_hopper_frozen_s0/metrics.jsonl\\\", \\\"command\\\": \\\"python train.py --config hopper_frozen_s0 --steps 160000\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"data_path\\\": \\\"Hopper-v4\\\", \\\"data_count\\\": 160000, \\\"model_name\\\": \\\"dreamer_v3_frozen_dt_emb\\\", \\\"seed\\\": 0}, \\\"hypothesis\\\": \\\"Extending frozen_s0 from 105K to 150K will show eval_return recovery with ve_ratio declining, confirming frozen_s0's degenerate CIVO at 95K is transient instability during severe learning delay rather than a permanent structural failure caused by the frozen dt_embedding.\\\", \\\"completed_at\\\": \\\"2026-05-27T10:48:10.979Z\\\"}, \\\"exp_hopper_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T05:51:24.680Z\\\", \\\"updated_at\\\": \\\"2026-05-27T05:52:01.157Z\\\", \\\"metrics\\\": {\\\"step\\\": 105000, \\\"eval_final\\\": 96.43, \\\"eval_return_trajectory\\\": {\\\"5000\\\": 0.06, \\\"15000\\\": 1.04, \\\"25000\\\": 1.7, \\\"35000\\\": 6.55, \\\"45000\\\": 19.09, \\\"55000\\\": 22.52, \\\"65000\\\": 3.5, \\\"75000\\\": 62.2, \\\"85000\\\": 67.62, \\\"95000\\\": 86.47, \\\"105000\\\": 96.43}, \\\"ve_ratio_trajectory\\\": {\\\"15000\\\": 0.08, \\\"25000\\\": 0.098, \\\"35000\\\": 0.166, \\\"45000\\\": 0.19, \\\"55000\\\": 0.279, \\\"65000\\\": 3.479, \\\"75000\\\": 0.341, \\\"85000\\\": 0.502, \\\"95000\\\": 0.517, \\\"105000\\\": 0.559}, \\\"nve_peak\\\": 3.48, \\\"nve_peak_step\\\": 65000, \\\"nve_final\\\": 0.559, \\\"civo_onset\\\": false, \\\"civo_alert_count\\\": 0, \\\"value_mean_final\\\": 53.9, \\\"target_mean_final\\\": 54.2, \\\"training_steps\\\": 105000, \\\"update_count\\\": 25099, \\\"fps\\\": 11}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_baseline/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_hopper_baseline.log\\\", \\\"hypothesis\\\": \\\"Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE < 1.5×). Source: C1/C2 third-environment verification (D160).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"data_path\\\": \\\"dmc_hopper_hop\\\", \\\"data_count\\\": 105000, \\\"model_name\\\": \\\"DreamerV3 baseline (dt=1, no gate)\\\", \\\"seed\\\": 0}, \\\"completed_at\\\": \\\"2026-05-27T05:52:01.157Z\\\"}, \\\"exp_097_cheetah_008d_s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T03:03:25.871Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:32:48.497Z\\\", \\\"hypothesis\\\": \\\"C1 trigger seed 3: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 Cheetah 上的第四个 seed（s3）。当前 onset rate 2/3（s0 NVE=4.1×✓, s1 NVE=0.517✗, s2 NVE=138.7×✓）。s3 完成后可计算完整 onset rate（n=4）。如果 onset ≥3/4 → 高 onset rate 支持 CIVO 是 systematic phenomenon；如果 2/4 → 50% onset rate 仍有意义但需讨论。\\\", \\\"parent\\\": \\\"exp_078_cheetah_008d_s0\\\", \\\"notes\\\": \\\"重新提交到 westd-51268 cuda:0。原 bjb1 提交 (PID 324959) 已死（服务器无卡）。exp_094 同配置在 westd 跑了 1.72h 后因 SSH 断连失败，检查其 checkpoint 是否可复用。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_097_cheetah_008d_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\\\\\"\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 3794, \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": 105000, \\\"model_name\\\": \\\"DreamerV3+FixedDt2_Subsample_H8 (trained dt_emb)\\\", \\\"seed\\\": 3, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_097_cheetah_008d_s3/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_097_cheetah_008d_s3/latest.pt\\\"}, \\\"metrics\\\": {\\\"step\\\": 105000, \\\"nve_peak\\\": 2.3, \\\"nve_peak_step\\\": 45000, \\\"nve_final\\\": 0.3, \\\"civo_onset\\\": true, \\\"civo_onset_step\\\": 45000, \\\"civo_pattern\\\": \\\"transient→degraded\\\", \\\"eval_final\\\": 61.7, \\\"eval_final_pct_baseline\\\": -86, \\\"baseline_eval_return\\\": 446.1, \\\"gate_dt_2_frac\\\": 1}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-26T11:32:48.497Z\\\"}, \\\"exp_100_walker_008a_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T03:39:24.456Z\\\", \\\"updated_at\\\": \\\"2026-05-26T07:52:52.927Z\\\", \\\"hypothesis\\\": \\\"Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 Walker 008a 第 2 seed。与 exp_008a_no_subsample_dt2 (s0) 和 exp_074_008a_walker_s3 (s3) 共同建立 C3 value suppression 多 seed 证据。训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练，预期无 CIVO。plan_013。\\\", \\\"parent\\\": \\\"exp_008a_no_subsample_dt2\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_100_walker_008a_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\\\\\"\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 5591, \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 105000, \\\"model_name\\\": \\\"DreamerV3+FixedDt2_NoSubsample (trained dt_emb, unexposed)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_100_walker_008a_s1/metrics.jsonl\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_100_walker_008a_s1/latest.pt\\\"}, \\\"metrics\\\": {\\\"step\\\": 105000, \\\"eval_return_trajectory\\\": {\\\"5000\\\": 31, \\\"15000\\\": 168.77, \\\"25000\\\": 158.03, \\\"35000\\\": 202.91, \\\"45000\\\": 305.98, \\\"55000\\\": 457.28, \\\"65000\\\": 628.82, \\\"75000\\\": 686.98, \\\"85000\\\": 656.64, \\\"95000\\\": 717.74, \\\"105000\\\": 750.59}, \\\"ve_ratio_trajectory\\\": {\\\"15000\\\": 0.035, \\\"25000\\\": 0.206, \\\"35000\\\": 0.279, \\\"45000\\\": 0.261, \\\"55000\\\": 0.248, \\\"65000\\\": 0.234, \\\"75000\\\": 0.26, \\\"85000\\\": 0.315, \\\"95000\\\": 0.325, \\\"105000\\\": 0.328}, \\\"value_mean_trajectory\\\": {\\\"15000\\\": 5.98, \\\"25000\\\": 32.58, \\\"35000\\\": 56.55, \\\"45000\\\": 79.94, \\\"55000\\\": 113.33, \\\"65000\\\": 147.14, \\\"75000\\\": 178.73, \\\"85000\\\": 206.95, \\\"95000\\\": 233.17, \\\"105000\\\": 246.06}, \\\"nve_peak\\\": 0.328, \\\"nve_final\\\": 0.328, \\\"civo_onset\\\": false, \\\"eval_final\\\": 750.59, \\\"eval_final_pct_baseline\\\": -18, \\\"baseline_eval_return\\\": 915.67, \\\"gate_dt_mean\\\": 2, \\\"gate_dt_2_frac\\\": 1}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-26T07:52:45.733Z\\\", \\\"notes\\\": \\\"C3 Walker 008a s1 完成。训练正常结束(105K steps)。eval_return@105K=750.59 (baseline 915.67, -18.0%)。ve_ratio 全程 0.035-0.328，NVE_peak=0.328，远低于 τ=1.5×，civo/alert 全程 0.0，无 CIVO onset。Value suppression 确认（value_mean 持续低于 eval_return）。与 parent s0 (eval@105K=777.66, -15.1%, ve_ratio 0.37-0.54) 一致：s1 性能略低但趋势相同，两个 seed 均无 CIVO 且呈现 value suppression，C3 Walker 008a 2-seed 证据闭合。gate_dt 全程固定为 2.0 (100% dt_2_frac)，符合 gate_fixed_dt=2 配置。\\\"}, \\\"rssm_fidelity_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T03:47:46.584Z\\\", \\\"updated_at\\\": \\\"2026-05-26T03:47:59.871Z\\\", \\\"hypothesis\\\": \\\"RSSM fidelity v2 分析：对比 4 类模型（baseline/trained_dt_emb/no_dt_emb/frozen）在 dt=1 vs dt=2 下的 observation/reward reconstruction loss。使用 Walker checkpoint (n=800)。结果：trained_dt_emb reward ratio 1.50×, obs ratio 1.44×; baseline obs ratio 1.55×; no_dt_emb gap 最小 (1.23×/1.16×)。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python analyze_rssm_fidelity_v2.py --device cuda:0\\\", \\\"server\\\": \\\"westd-51268\\\", \\\"data_path\\\": \\\"Walker logdirs (exp_008d/009d/009c/084)\\\", \\\"data_count\\\": 800, \\\"model_name\\\": \\\"RSSM fidelity analysis v2\\\", \\\"seed\\\": 0, \\\"checkpoint_path\\\": \\\"analysis_rssm_fidelity_v2.json\\\", \\\"log_path\\\": \\\"N/A (analysis task)\\\"}, \\\"completed_at\\\": \\\"2026-05-26T03:47:59.871Z\\\"}, \\\"exp_057_frozen_dt_emb_walker_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T15:26:00.391Z\\\", \\\"updated_at\\\": \\\"2026-05-26T03:03:45.406Z\\\", \\\"hypothesis\\\": \\\"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\\\", \\\"parent\\\": \\\"exp_042_frozen_dt_emb_walker\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 157775, \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Walker s2)\\\", \\\"seed\\\": 2, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"log_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"checkpoint_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"failure_reason\\\": \\\"bjb1-45299 server lost GPU allocation, experiment terminated\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-26T03:03:45.406Z\\\"}, \\\"exp_051_stackcube_frozen_dt_emb_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T18:42:39.309Z\\\", \\\"updated_at\\\": \\\"2026-05-26T03:03:44.692Z\\\", \\\"hypothesis\\\": \\\"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks\\\", \\\"parent\\\": \\\"exp_049\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 305974, \\\"data_path\\\": \\\"maniskill_StackCube-v1 (online RL)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, StackCube s0)\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"maniskill_StackCube-v1 (online eval)\\\", \\\"checkpoint_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"failure_reason\\\": \\\"bjb1-45299 server lost GPU allocation, experiment terminated\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-26T03:03:44.692Z\\\"}, \\\"exp_049_stackcube_civo_trigger_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T17:14:38.578Z\\\", \\\"updated_at\\\": \\\"2026-05-26T03:03:42.946Z\\\", \\\"hypothesis\\\": \\\"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion（Walker/Cheetah）推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack），比 PickCube 更难。如果触发 CIVO → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\\\", \\\"parent\\\": \\\"exp_048_stackcube_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 91395, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"checkpoint_path\\\": \\\"N/A - bjb1-45299 lost GPU\\\", \\\"failure_reason\\\": \\\"bjb1-45299 server lost GPU allocation, experiment terminated\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-26T03:03:42.946Z\\\"}, \\\"exp_081_008e_v3_walker_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T15:42:24.765Z\\\", \\\"updated_at\\\": \\\"2026-05-25T15:43:10.949Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_return_105K\\\": 597.1, \\\"vs_baseline\\\": \\\"-34.8%\\\", \\\"vs_baseline_pct\\\": 65.2, \\\"baseline_105K\\\": 915.67, \\\"ve_ratio_peak\\\": 0.6, \\\"ve_ratio_final\\\": 0.5, \\\"NVE_est_peak\\\": 0.8, \\\"NVE_est_final\\\": 0.7, \\\"gate_dt_mean\\\": 1, \\\"gate_dt_1_frac\\\": 1, \\\"civo_alert_count\\\": 0, \\\"training_steps\\\": 105000, \\\"update_count\\\": 25099, \\\"value_mean_final\\\": 295}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_081_008e_v3_walker_s2/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --config 008e_v3 --env walker_walk --seed 2\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3_008e_v3\\\", \\\"seed\\\": 2}, \\\"hypothesis\\\": \\\"Trained dt_emb with dt=1 imagination and subsample ON (max_dt=2) does not trigger CIVO in Walker Walk, as the value function sees only single-step predictions that match the world model's training distribution, preventing value inflation even with learned temporal embeddings.\\\", \\\"completed_at\\\": \\\"2026-05-25T15:43:10.949Z\\\"}, \\\"exp_073_008f_walker_s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T09:52:07.413Z\\\", \\\"updated_at\\\": \\\"2026-05-25T09:52:34.845Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 289.3, \\\"eval_return_peak\\\": 486.5, \\\"eval_return_peak_step\\\": 75000, \\\"ve_ratio_max\\\": 0.5, \\\"civo_alert_max\\\": 0, \\\"gate_dt_mean\\\": 2, \\\"gate_dt_2_frac\\\": 1, \\\"gate_empirical_entropy\\\": 0, \\\"total_env_steps\\\": 112000, \\\"total_updates\\\": 25099}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_073_008f_walker_s4/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --config 008f --seed 4\\\", \\\"server\\\": \\\"westd-19154\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_v3_008f\\\", \\\"seed\\\": 4}, \\\"hypothesis\\\": \\\"Removing dt_embedding (dt_embed_dim=0) in the 008f control config prevents CIVO onset because the agent cannot form temporally-conditioned value predictions that compound imagination-driven overestimation. With fixed dt=2 and no temporal embedding, value error ratio should remain below the 1.5x CIVO threshold across seeds.\\\", \\\"completed_at\\\": \\\"2026-05-25T09:52:34.845Z\\\"}, \\\"exp_069_008f_walker_repro_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T07:20:25.632Z\\\", \\\"updated_at\\\": \\\"2026-05-25T07:21:13.407Z\\\", \\\"hypothesis\\\": \\\"Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk. With no learned temporal embedding, the value network cannot develop the compounding overestimation pattern that causes CIVO collapse. This seed=1 run extends the evidence from exp_008f (seed=0).\\\", \\\"parent\\\": \\\"exp_008f_no_dt_embed_subsample_on_h8\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs dmc_vision --task dmc_walker_walk --seed 1 --logdir logdir/exp_069_008f_walker_repro_s1\\\", \\\"server\\\": \\\"westd-19154\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv2_no_dt_embed_h8\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"dmc_walker_walk_online\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_069_008f_walker_repro_s1/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-25T07:20:58.159Z\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 237.8, \\\"eval_return_final_step\\\": 105000, \\\"eval_return_peak\\\": 390.1, \\\"eval_return_peak_step\\\": 95000, \\\"steps_completed\\\": 112000, \\\"eval_steps\\\": 105000, \\\"civo_triggered\\\": false, \\\"civo_alert_count\\\": 0, \\\"ve_ratio_max\\\": 0.447, \\\"ve_ratio_max_step\\\": 105000, \\\"ve_ratio_final\\\": 0.447, \\\"gate_dt_mean\\\": 2, \\\"gate_dt_2_frac\\\": 1, \\\"gate_empirical_entropy\\\": 0, \\\"value_mean_final\\\": 106.3, \\\"target_mean_final\\\": 106.4, \\\"value_loss_final\\\": 0.99, \\\"seed\\\": 1, \\\"eval_return_trajectory\\\": {\\\"5K\\\": 30.5, \\\"15K\\\": 158.7, \\\"25K\\\": 180.8, \\\"35K\\\": 250.3, \\\"45K\\\": 293.6, \\\"55K\\\": 272.2, \\\"65K\\\": 328.1, \\\"75K\\\": 244.8, \\\"85K\\\": 382.5, \\\"95K\\\": 390.1, \\\"105K\\\": 237.8}, \\\"ve_ratio_trajectory\\\": {\\\"15K\\\": 0.021, \\\"25K\\\": 0.111, \\\"35K\\\": 0.171, \\\"95K\\\": 0.275, \\\"105K\\\": 0.447}, \\\"note\\\": \\\"C2 causal control: no dt_embedding, fixed dt=2. No CIVO triggered. ve_ratio stayed <0.5 throughout. Late eval dip (390→238) is normal Walker variance, not CIVO-driven (value_mean≈target_mean, no overestimation).\\\"}}, \\\"exp_055_peginsertion_civo_trigger_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T05:16:11.755Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:34:24.080Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PegInsertionSide-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_055_peginsertion_civo_trigger_s1.log\\\"}, \\\"hypothesis\\\": \\\"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，162.5K 时仍 1.94）。如果 s1 也触发持续 CIVO → PegInsertion 是最严重的 CIVO 环境（比 StackCube 自修复更难），支持 severity-dependent narrative；如果不触发 → seed-specific 异常。\\\", \\\"parent\\\": \\\"exp_050_peginsertion_civo_trigger_s0\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_055_peginsertion_civo_trigger_s1/latest.pt\\\", \\\"log_path\\\": \\\"logdir/exp_055_peginsertion_civo_trigger_s1.log\\\", \\\"metrics\\\": {\\\"total_steps\\\": 222400, \\\"ve_ratio_max\\\": 3.08, \\\"ve_ratio_max_step\\\": 92500, \\\"ve_ratio_final\\\": 0.5, \\\"ve_ratio_final_step\\\": 212500, \\\"eval_peak\\\": 24.05, \\\"eval_peak_step\\\": 112500, \\\"eval_final\\\": 11.44, \\\"eval_final_step\\\": 212500, \\\"civo_triggered\\\": true, \\\"civo_self_corrected\\\": \\\"partial\\\", \\\"civo_onset_step\\\": 32500, \\\"civo_peak_step\\\": 92500, \\\"ve_ratio_trajectory\\\": {\\\"12500\\\": 0.19, \\\"22500\\\": 0.81, \\\"32500\\\": 1.35, \\\"42500\\\": 2, \\\"52500\\\": 2.39, \\\"62500\\\": 2.85, \\\"72500\\\": 2.28, \\\"82500\\\": 2.48, \\\"92500\\\": 3.08, \\\"102500\\\": 2.51, \\\"112500\\\": 0.91, \\\"122500\\\": 1.21, \\\"132500\\\": 1.36, \\\"142500\\\": 0.75, \\\"152500\\\": 0.55, \\\"162500\\\": 1.17, \\\"172500\\\": 0.96, \\\"182500\\\": 0.94, \\\"192500\\\": 0.9, \\\"202500\\\": 0.73, \\\"212500\\\": 0.5}, \\\"eval_trajectory\\\": {\\\"2500\\\": 2.01, \\\"12500\\\": 10.12, \\\"22500\\\": 11.47, \\\"32500\\\": 12.01, \\\"42500\\\": 10.13, \\\"52500\\\": 10.31, \\\"62500\\\": 9.02, \\\"72500\\\": 10.07, \\\"82500\\\": 8.78, \\\"92500\\\": 7.24, \\\"102500\\\": 9.2, \\\"112500\\\": 24.05, \\\"122500\\\": 16.46, \\\"132500\\\": 13.15, \\\"142500\\\": 20.44, \\\"152500\\\": 23.4, \\\"162500\\\": 9.07, \\\"172500\\\": 9.46, \\\"182500\\\": 8.51, \\\"192500\\\": 7.81, \\\"202500\\\": 8.58, \\\"212500\\\": 11.44}, \\\"note\\\": \\\"CIVO triggered (ve_ratio 3.08@92.5K), less severe than s0 (10.05). Partial self-correction to 0.50 by 212.5K. Eval poor throughout (~10-24), PegInsertion is hard task.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T23:34:24.080Z\\\"}, \\\"exp_048_cheetah_civo_extension\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:30:40.050Z\\\", \\\"updated_at\\\": \\\"2026-05-22T21:17:46.852Z\\\", \\\"hypothesis\\\": \\\"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → \\\\\\\"severity determines recoverability\\\\\\\" narrative, strongest paper defense. If it does → CIVO is universally transient regardless of severity.\\\", \\\"parent\\\": \\\"exp_010b_cheetah_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 88654, \\\"data_path\\\": \\\"dmc_cheetah_run (online RL)\\\", \\\"data_count\\\": 300000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_048_cheetah_civo_extension/train.log\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 23.423, \\\"eval_peak\\\": 32.835, \\\"eval_peak_step\\\": 252000, \\\"ve_ratio_initial_measured\\\": 6.135, \\\"ve_ratio_initial_measured_step\\\": 122000, \\\"ve_ratio_inherited_from_exp010b\\\": 46.34, \\\"ve_ratio_peak_in_run\\\": 24.112, \\\"ve_ratio_peak_step\\\": 162000, \\\"ve_ratio_final\\\": 1.803, \\\"nve_inherited\\\": 70.64, \\\"nve_peak_in_run\\\": 36.76, \\\"nve_final\\\": 2.75, \\\"baseline_ve_ratio\\\": 0.656, \\\"total_steps\\\": 312000, \\\"last_eval_step\\\": 302000, \\\"civo_self_corrected\\\": \\\"partial\\\", \\\"civo_reduction_pct\\\": 96.1, \\\"civo_correction_duration_steps\\\": 197000, \\\"gate_collapsed\\\": true, \\\"gate_dt_final\\\": 2, \\\"gate_dt_2_frac_final\\\": 1}, \\\"checkpoint_path\\\": \\\"logdir/exp_048_cheetah_civo_extension/checkpoint_302000.pt\\\", \\\"log_path\\\": \\\"logdir/exp_048_cheetah_civo_extension/train.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T21:17:46.852Z\\\"}, \\\"exp_047_frozen_dt_emb_walker_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:42:12.914Z\\\", \\\"updated_at\\\": \\\"2026-05-22T19:01:30.894Z\\\", \\\"hypothesis\\\": \\\"Freezing dt_emb in Walker Walk (seed 1) prevents sustained CIVO collapse, replicating exp_042 (seed 0, NVE=0.19) finding that removing dt conditioning blocks the overestimation feedback loop\\\", \\\"parent\\\": \\\"exp_042_frozen_dt_emb_walker\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 282452, \\\"data_path\\\": \\\"dmc_walker_walk (online RL)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Walker s1)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\\\"}, \\\"metrics\\\": {\\\"eval_peak\\\": 408.79, \\\"eval_peak_step\\\": 125000, \\\"eval_final\\\": 144.22, \\\"eval_final_step\\\": 215000, \\\"ve_ratio_peak\\\": 1.099, \\\"ve_ratio_peak_step\\\": 75000, \\\"ve_ratio_final\\\": 0.277, \\\"nve_peak\\\": 1.71, \\\"nve_peak_step\\\": 95000, \\\"nve_final_105k\\\": 0.56, \\\"total_steps\\\": 225000, \\\"note\\\": \\\"Transient NVE>1.5x at 75K-95K with full self-correction by 105K. Late eval decline (408->144) NOT CIVO-driven (ve_ratio=0.28). No sustained collapse.\\\"}, \\\"checkpoint_path\\\": \\\"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\\\", \\\"log_path\\\": \\\"logdir/exp_047_frozen_dt_emb_walker_s1/\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T18:50:46.948Z\\\"}, \\\"exp_046_frozen_dt_emb_cheetah\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:40:43.182Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:32:34.105Z\\\", \\\"hypothesis\\\": \\\"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation. Source: D133 + exp_042 result + R1-N4 cross-environment concern.\\\", \\\"parent\\\": \\\"exp_042_frozen_dt_emb_walker\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 281513, \\\"data_path\\\": \\\"dmc_cheetah_run (online RL)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Cheetah)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_046_frozen_dt_emb_cheetah/train.log\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 150.5, \\\"eval_peak\\\": 207.4, \\\"eval_peak_step\\\": 145000, \\\"ve_ratio_peak\\\": 0.4, \\\"ve_ratio_final\\\": 0.1, \\\"nve_peak\\\": 1.35, \\\"nve_peak_step\\\": 45000, \\\"nve_final\\\": 0.17, \\\"total_steps\\\": 224000, \\\"civo_alert_count\\\": 0, \\\"eval_trajectory\\\": \\\"5K:8.3, 15K:110, 35K:160, 95K:181, 105K:206, 115K:46, 145K:207, 155K:161, 215K:150.5\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T18:31:00.933Z\\\"}, \\\"exp_048_stackcube_civo_trigger_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:44:55.613Z\\\", \\\"updated_at\\\": \\\"2026-05-22T17:14:16.564Z\\\", \\\"hypothesis\\\": \\\"ManiSkill Phase 1 scout: CIVO trigger config (trained dt_emb + subsample ON + H=8) on StackCube-v1 manipulation task. Tests whether CIVO generalizes beyond locomotion (Walker/Cheetah) to manipulation domains. exp_019b showed transient CIVO on PickCube; StackCube is harder (multi-stage). If CIVO triggers → extends cross-domain evidence; if not → supports locomotion-specific scope.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_stackcube_civo_trigger_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 87609, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, ManiSkill)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"/tmp/exp_048.log\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-22T17:14:16.564Z\\\"}, \\\"exp_045_treatment_extension_008d_s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T09:40:52.894Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:44:50.990Z\\\", \\\"hypothesis\\\": \\\"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\\\", \\\"parent\\\": \\\"exp_008d_civo_trigger_s3\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 70945, \\\"data_path\\\": \\\"dmc_walker_walk (online RL)\\\", \\\"data_count\\\": 300000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config)\\\", \\\"seed\\\": 3, \\\"checkpoint_source\\\": \\\"exp_008d_civo_trigger_s3/latest.pt (step 112K)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval, same as training env)\\\", \\\"log_path\\\": \\\"logdir/exp_045_treatment_extension_008d_s3/train.log\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 867.6, \\\"eval_peak\\\": 869.7, \\\"eval_peak_step\\\": 242000, \\\"ve_ratio_final\\\": 0.05, \\\"ve_ratio_peak\\\": 4.91, \\\"ve_ratio_peak_step\\\": 132000, \\\"nve_final\\\": 0.052, \\\"total_steps\\\": 312000, \\\"self_correction_onset\\\": 142000, \\\"finding\\\": \\\"CIVO self-correction: ve_ratio 4.91→0.05, eval 35→868 over 170K steps\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\\\", \\\"completed_at\\\": \\\"2026-05-22T15:44:50.990Z\\\"}, \\\"exp_036_dual_critic_pickcube\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T19:45:02.066Z\\\", \\\"updated_at\\\": \\\"2026-05-21T19:45:46.721Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --task ManiSkill_PickCube-v1 --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 0 --steps 200000\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"ManiSkill_PickCube-v1\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3_dual_critic\\\", \\\"seed\\\": 0}, \\\"hypothesis\\\": \\\"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\\\", \\\"parent\\\": \\\"exp_032_dual_critic_walker\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_036_dual_critic_pickcube\\\", \\\"log_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 212447, \\\"total_env_steps\\\": 212447, \\\"eval_return_final\\\": 27.7, \\\"eval_return_peak\\\": 27.7, \\\"eval_return_peak_step\\\": 202500, \\\"ve_ratio_peak\\\": 2.3, \\\"ve_ratio_peak_step\\\": 32500, \\\"ve_ratio_final\\\": 0.2, \\\"civo_alerts\\\": 0, \\\"v1_v2_max_divergence\\\": 0, \\\"v1_v2_correlated\\\": true, \\\"CIVO_prevented\\\": \\\"vacuous_no_civo_in_baseline\\\", \\\"gate_dt_2_frac\\\": 1, \\\"gate_entropy\\\": 0, \\\"exit_code\\\": 0, \\\"eval_return_trajectory\\\": {\\\"2.5K\\\": 2, \\\"12.5K\\\": 17.5, \\\"22.5K\\\": 17.5, \\\"32.5K\\\": 11.6, \\\"42.5K\\\": 15.6, \\\"52.5K\\\": 11.7, \\\"62.5K\\\": 18.8, \\\"72.5K\\\": 5.4, \\\"82.5K\\\": 22.5, \\\"92.5K\\\": 18.1, \\\"102.5K\\\": 8.4, \\\"112.5K\\\": 7.1, \\\"122.5K\\\": 9.1, \\\"132.5K\\\": 12.8, \\\"142.5K\\\": 14, \\\"152.5K\\\": 13.1, \\\"162.5K\\\": 16.2, \\\"172.5K\\\": 19.7, \\\"182.5K\\\": 16.8, \\\"192.5K\\\": 13.7, \\\"202.5K\\\": 27.7}, \\\"ve_ratio_trajectory\\\": {\\\"12.5K\\\": 0.2, \\\"22.5K\\\": 1, \\\"32.5K\\\": 2.3, \\\"42.5K\\\": 1.4, \\\"52.5K\\\": 1.4, \\\"62.5K\\\": 0.6, \\\"72.5K\\\": 1.6, \\\"82.5K\\\": 0.3, \\\"92.5K\\\": 0.3, \\\"102.5K\\\": 0.6, \\\"112.5K\\\": 0.7, \\\"122.5K\\\": 0.5, \\\"132.5K\\\": 0.4, \\\"142.5K\\\": 0.3, \\\"152.5K\\\": 0.4, \\\"162.5K\\\": 0.3, \\\"172.5K\\\": 0.3, \\\"182.5K\\\": 0.3, \\\"192.5K\\\": 0.4, \\\"202.5K\\\": 0.2}, \\\"value1_mean_trajectory\\\": {\\\"2.5K\\\": 0, \\\"12.5K\\\": 3.8, \\\"22.5K\\\": 17.9, \\\"32.5K\\\": 26.9, \\\"42.5K\\\": 21.2, \\\"52.5K\\\": 16.1, \\\"62.5K\\\": 11.6, \\\"72.5K\\\": 8.7, \\\"82.5K\\\": 7.2, \\\"92.5K\\\": 6, \\\"102.5K\\\": 5.3, \\\"112.5K\\\": 5.1, \\\"122.5K\\\": 5, \\\"132.5K\\\": 4.9, \\\"142.5K\\\": 4.9, \\\"152.5K\\\": 5.3, \\\"162.5K\\\": 5.7, \\\"172.5K\\\": 5.6, \\\"182.5K\\\": 5.6, \\\"192.5K\\\": 5.6, \\\"202.5K\\\": 5.8}, \\\"baseline_comparison\\\": {\\\"exp_019a_v2_vanilla_baseline_final\\\": 58.6, \\\"exp_019b_civo_config_baseline_final\\\": 26.6, \\\"exp_031_tcn_sigma02_final\\\": 17.2, \\\"exp_031b_tcn_sigma05_final\\\": 25.5}, \\\"conclusion_detail\\\": \\\"CIVO never manifested on PickCube (with or without dual-critic). ve_ratio peaked at 2.3 early (32.5K) and self-corrected — same pattern as TCN experiments (peak 3.7, 3.3). Eval 27.7 is indistinguishable from CIVO-config baseline (26.6). The subsample+dt_emb config itself degrades PickCube from 58.6 to ~27, and dual-critic does not recover this gap. Hypothesis rejected: PickCube is CIVO-immune at this training scale, making it a poor test for intervention generality.\\\"}, \\\"completed_at\\\": \\\"2026-05-21T19:45:46.721Z\\\"}, \\\"exp_034_dual_critic_cheetah\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T12:09:08.035Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:09:56.881Z\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"total_env_steps\\\": 224000, \\\"eval_return_peak\\\": 315.7, \\\"eval_return_peak_step\\\": 45000, \\\"eval_return_final\\\": 97.5, \\\"ve_ratio_peak\\\": 1.8, \\\"ve_ratio_peak_step\\\": 55000, \\\"ve_ratio_final\\\": 0.1, \\\"civo_alerts\\\": 2, \\\"civo_alert_steps\\\": [95000, 105000], \\\"v1_v2_correlated\\\": true, \\\"gate_dt_2_frac\\\": 1, \\\"gate_entropy\\\": 0, \\\"exit_code\\\": 0, \\\"eval_return_trajectory\\\": {\\\"5K\\\": 8.3, \\\"15K\\\": 27.8, \\\"25K\\\": 108.7, \\\"35K\\\": 110, \\\"45K\\\": 315.7, \\\"55K\\\": 34.5, \\\"65K\\\": 81.5, \\\"75K\\\": 183, \\\"85K\\\": 88.4, \\\"95K\\\": 41, \\\"105K\\\": 27.2, \\\"115K\\\": 45.9, \\\"125K\\\": 58.7, \\\"135K\\\": 71.6, \\\"145K\\\": 61.9, \\\"155K\\\": 52.1, \\\"165K\\\": 153.8, \\\"175K\\\": 104.9, \\\"185K\\\": 101.4, \\\"195K\\\": 115.3, \\\"205K\\\": 101.5, \\\"215K\\\": 97.5}, \\\"ve_ratio_trajectory\\\": {\\\"15K\\\": 0.1, \\\"25K\\\": 0.1, \\\"35K\\\": 0.2, \\\"45K\\\": 0.1, \\\"55K\\\": 1.8, \\\"65K\\\": 0.7, \\\"75K\\\": 0.3, \\\"85K\\\": 0.5, \\\"95K\\\": 1, \\\"105K\\\": 1.6, \\\"115K\\\": 0.9, \\\"125K\\\": 0.6, \\\"135K\\\": 0.4, \\\"145K\\\": 0.4, \\\"155K\\\": 0.4, \\\"165K\\\": 0.1, \\\"175K\\\": 0.2, \\\"185K\\\": 0.2, \\\"195K\\\": 0.1, \\\"205K\\\": 0.1, \\\"215K\\\": 0.1}, \\\"value1_mean_trajectory\\\": {\\\"15K\\\": 1.8, \\\"25K\\\": 10.9, \\\"35K\\\": 23.7, \\\"45K\\\": 39, \\\"55K\\\": 60.5, \\\"65K\\\": 59.3, \\\"75K\\\": 52.6, \\\"85K\\\": 46.7, \\\"95K\\\": 41.7, \\\"105K\\\": 43.4, \\\"115K\\\": 39.3, \\\"125K\\\": 33.8, \\\"135K\\\": 28.5, \\\"145K\\\": 24.6, \\\"155K\\\": 21.5, \\\"165K\\\": 19.2, \\\"175K\\\": 17.8, \\\"185K\\\": 16.7, \\\"195K\\\": 15.7, \\\"205K\\\": 14.8, \\\"215K\\\": 14.2}, \\\"conclusion_detail\\\": \\\"CIVO triggered but partially mitigated. Two CIVO alerts (95K, 105K), peak ve_ratio=1.8 at 55K. Eval crashed from peak 315.7 to 27.2 (105K), recovered to 97.5. Dual-critic provided 40x reduction in overestimation vs baseline (ve_ratio 1.8 vs NVE 70.64) and prevented catastrophic collapse (eval 97.5 vs 0.83). But CIVO not fully suppressed — hypothesis of cross-environment generality not supported. v1≈v2 throughout (no critic disagreement).\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_034_dual_critic_cheetah --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --dual_critic True\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3_dual_critic\\\", \\\"seed\\\": 0, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\\\", \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run\\\"}, \\\"hypothesis\\\": \\\"Dual-critic on Cheetah Run: TCN failed at all σ on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\\\", \\\"parent\\\": \\\"exp_032_dual_critic_walker\\\", \\\"completed_at\\\": \\\"2026-05-21T12:09:56.881Z\\\"}, \\\"exp_029d_tcn_walker_s3_sigma02\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T19:43:05.327Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:38:07.906Z\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"total_env_steps\\\": 224000, \\\"eval_return_final\\\": 104.5, \\\"eval_return_peak\\\": 349.6, \\\"eval_return_peak_step\\\": 95000, \\\"eval_return_105K\\\": 71.8, \\\"ve_ratio_final\\\": 0.4, \\\"ve_ratio_peak\\\": 3, \\\"ve_ratio_peak_step\\\": 105000, \\\"civo_blowup\\\": true, \\\"civo_blowup_step\\\": 105000, \\\"eval_return_trajectory\\\": {\\\"5K\\\": 31.7, \\\"15K\\\": 159.1, \\\"25K\\\": 155.7, \\\"35K\\\": 190.8, \\\"45K\\\": 137.1, \\\"55K\\\": 210.7, \\\"65K\\\": 189.5, \\\"75K\\\": 253.2, \\\"85K\\\": 259.5, \\\"95K\\\": 349.6, \\\"105K\\\": 71.8, \\\"115K\\\": 69.8, \\\"125K\\\": 61.5, \\\"135K\\\": 141.8, \\\"145K\\\": 98.7, \\\"155K\\\": 88.9, \\\"165K\\\": 86.2, \\\"175K\\\": 123.5, \\\"185K\\\": 153.7, \\\"195K\\\": 68.8, \\\"205K\\\": 63.7, \\\"215K\\\": 104.5}, \\\"ve_ratio_trajectory\\\": {\\\"15K\\\": 0, \\\"25K\\\": 0.2, \\\"35K\\\": 0.3, \\\"45K\\\": 0.7, \\\"55K\\\": 0.6, \\\"65K\\\": 0.9, \\\"75K\\\": 0.8, \\\"85K\\\": 0.9, \\\"95K\\\": 0.7, \\\"105K\\\": 3, \\\"115K\\\": 2.5, \\\"125K\\\": 2.4, \\\"135K\\\": 0.9, \\\"145K\\\": 1.1, \\\"155K\\\": 1.1, \\\"165K\\\": 0.9, \\\"175K\\\": 0.6, \\\"185K\\\": 0.4, \\\"195K\\\": 0.8, \\\"205K\\\": 0.7, \\\"215K\\\": 0.4}, \\\"exit_code\\\": 0}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --config walker_walk_tcn --seed 3 --tcn_sigma 0.2\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"walker_walk\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_tcn_sigma02\\\", \\\"seed\\\": 3}, \\\"hypothesis\\\": \\\"Fourth TCN σ=0.2 seed to match 4 baseline seeds for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\\\", \\\"completed_at\\\": \\\"2026-05-21T03:38:07.906Z\\\"}, \\\"exp_025_obs_sgs_walker_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T02:40:59.914Z\\\", \\\"updated_at\\\": \\\"2026-05-20T02:41:29.954Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python dreamer.py --configs dmc_vision --task dmc_walker_walk --obs_decoder_sgs true --seed 1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3-obs-sgs\\\", \\\"seed\\\": 1}, \\\"hypothesis\\\": \\\"Obs-decoder stop-gradient on symlog (SGS) prevents CIVO in Walker by breaking the value→decoder→representation gradient pathway, keeping NVE below 1.5× baseline throughout training.\\\", \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/checkpoint.ckpt\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"final_eval_return\\\": 726.41, \\\"peak_ve_ratio\\\": 0.8313, \\\"peak_ve_ratio_step\\\": 95000, \\\"peak_NVE_approx\\\": 1.28, \\\"ve_ratio_5K\\\": 0, \\\"ve_ratio_25K\\\": 0.1585, \\\"ve_ratio_45K\\\": 0.478, \\\"ve_ratio_65K\\\": 0.5932, \\\"ve_ratio_75K\\\": 0.5522, \\\"ve_ratio_85K\\\": 0.6419, \\\"ve_ratio_95K\\\": 0.8313, \\\"ve_ratio_105K\\\": 0.5093, \\\"ve_ratio_115K\\\": 0.4117, \\\"ve_ratio_125K\\\": 0.3476, \\\"ve_ratio_135K\\\": 0.2809, \\\"ve_ratio_145K\\\": 0.1883, \\\"ve_ratio_155K\\\": 0.1842, \\\"ve_ratio_165K\\\": 0.1099, \\\"ve_ratio_175K\\\": 0.0905, \\\"ve_ratio_185K\\\": 0.1088, \\\"ve_ratio_195K\\\": 0.2013, \\\"ve_ratio_205K\\\": 0.0725, \\\"ve_ratio_215K\\\": 0.0563, \\\"conclusion_detail\\\": \\\"CIVO prevented. Peak NVE ~1.28x at 95K (baseline ~0.648 interpolated), well below 1.5x threshold. ve_ratio monotonically declines from 95K onward to 0.056 at 215K. Obs-decoder SGS Walker seed 1 is 1/4 healthy prevention seed.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T02:41:29.954Z\\\"}, \\\"exp_025_obs_sgs_walker_s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T02:00:40.376Z\\\", \\\"updated_at\\\": \\\"2026-05-20T02:01:23.024Z\\\", \\\"hypothesis\\\": \\\"Blocking observation-decoder gradients via stop-gradient (SGS) on Walker will prevent early-onset CIVO by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/checkpoint.pt\\\", \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs walker_obs_sgs --seed 4\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_obs_sgs\\\", \\\"seed\\\": 4}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"final_eval_return\\\": 241.47, \\\"final_value_mean\\\": 34.3, \\\"final_ve_ratio\\\": 0.1421, \\\"peak_ve_ratio\\\": 6.0622, \\\"peak_ve_step\\\": 75000, \\\"ve_trajectory\\\": {\\\"5000\\\": 0, \\\"15000\\\": 0.0206, \\\"25000\\\": 0.1623, \\\"35000\\\": 0.7183, \\\"45000\\\": 0.67, \\\"55000\\\": 1.2924, \\\"65000\\\": 2.1521, \\\"75000\\\": 6.0622, \\\"85000\\\": 4.0813, \\\"95000\\\": 2.0202, \\\"105000\\\": 1.5704, \\\"115000\\\": 2.1303, \\\"125000\\\": 1.2078, \\\"135000\\\": 1.2884, \\\"145000\\\": 1.2645, \\\"155000\\\": 0.6109, \\\"165000\\\": 0.6521, \\\"175000\\\": 0.5908, \\\"185000\\\": 0.3178, \\\"195000\\\": 0.2701, \\\"205000\\\": 0.4087, \\\"215000\\\": 0.1421}, \\\"conclusion_detail\\\": \\\"Obs-decoder SGS failed to prevent early-onset CIVO on Walker seed 4. Severe CIVO collapse 55K-115K with peak ve_ratio=6.06 at 75K (eval crashed from 179 at 25K to 34 at 75K). Value overestimation gradually decayed through second half of training (1.26@145K → 0.14@215K) and eval eventually recovered to 241.5@215K. However, the SGS intervention did not prevent the CIVO onset — the recovery was driven by natural value decay over extended training, not by the SGS mechanism.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T02:01:23.024Z\\\"}, \\\"exp_026_obs_sgs_cheetah_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T01:38:04.002Z\\\", \\\"updated_at\\\": \\\"2026-05-20T01:38:47.743Z\\\", \\\"hypothesis\\\": \\\"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/checkpoint.pt\\\", \\\"log_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs cheetah_obs_sgs --seed 1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_obs_sgs\\\", \\\"seed\\\": 1}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 105000, \\\"final_eval_return\\\": 38.26, \\\"final_value_mean\\\": 37.84, \\\"final_ve_ratio\\\": 0.9891, \\\"peak_ve_ratio\\\": 11.8091, \\\"peak_ve_step\\\": 75000, \\\"ve_trajectory\\\": {\\\"5000\\\": 0.0001, \\\"15000\\\": 0.0262, \\\"25000\\\": 0.0657, \\\"35000\\\": 0.1056, \\\"45000\\\": 0.979, \\\"55000\\\": 7.3924, \\\"65000\\\": 10.8375, \\\"75000\\\": 11.8091, \\\"85000\\\": 7.5096, \\\"95000\\\": 5.7255, \\\"105000\\\": 0.9891}, \\\"conclusion_detail\\\": \\\"Obs-decoder SGS failed on Cheetah seed 1: severe CIVO collapse 45K-95K, peak ve_ratio=11.81 at 75K. Eval_return crashed from 271.9 (35K) to 3.65 (75K). Late ve_ratio recovery to ~1.0 at 105K but eval_return (38.3) remained 86% below pre-collapse peak. Consistent with s0 result — SGS intervention is counterproductive on Cheetah, amplifying rather than suppressing CIVO.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T01:38:47.743Z\\\"}, \\\"exp_026_obs_sgs_cheetah_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T01:32:40.958Z\\\", \\\"updated_at\\\": \\\"2026-05-20T01:33:21.724Z\\\", \\\"hypothesis\\\": \\\"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs cheetah_obs_sgs --seed 0\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_obs_sgs\\\", \\\"seed\\\": 0}, \\\"checkpoint_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/checkpoint.pt\\\", \\\"log_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 105000, \\\"final_eval_return\\\": 38.76, \\\"final_value_mean\\\": 51.16, \\\"final_ve_ratio\\\": 1.3199, \\\"peak_ve_ratio\\\": 8.5607, \\\"peak_ve_step\\\": 65000, \\\"ve_trajectory\\\": {\\\"5000\\\": 0.0001, \\\"15000\\\": 0.0244, \\\"25000\\\": 0.094, \\\"35000\\\": 0.177, \\\"45000\\\": 0.3098, \\\"55000\\\": 0.9939, \\\"65000\\\": 8.5607, \\\"75000\\\": 1.2188, \\\"85000\\\": 0.9696, \\\"95000\\\": 1.486, \\\"105000\\\": 1.3199}, \\\"conclusion_detail\\\": \\\"Obs-decoder SGS failed on Cheetah: full CIVO collapse at 65K (ve_ratio=8.56, NVE=21.85x 5-seed normalized). Partial recovery by 75K but performance remained degraded (eval_return=38.8 vs baseline ~160). Consistent with compensatory amplification — blocking obs decoder gradient worsened CIVO vs untreated baseline (010b NVE=8.27x). SGS intervention is counterproductive on Cheetah.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T01:33:21.724Z\\\"}, \\\"exp_025_obs_sgs_walker_s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T00:48:33.067Z\\\", \\\"updated_at\\\": \\\"2026-05-20T00:49:00.531Z\\\", \\\"hypothesis\\\": \\\"Observation-decoder SGS regularization will prevent CIVO collapse by grounding value estimates through auxiliary reconstruction loss, maintaining healthy NVE ratios throughout training.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 train.py --config configs/exp_025_obs_sgs_walker_s3.yaml\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/\\\", \\\"data_count\\\": 215000, \\\"model_name\\\": \\\"dreamer_obs_sgs\\\", \\\"seed\\\": 3}, \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/\\\", \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_step\\\": 215000, \\\"eval_return_105k\\\": 818.58, \\\"ve_ratio_105k\\\": 0.5621, \\\"eval_return_135k\\\": 66.95, \\\"ve_ratio_135k\\\": 5.4659, \\\"eval_return_145k\\\": 43.75, \\\"ve_ratio_145k\\\": 6.8121, \\\"eval_return_175k\\\": 193.92, \\\"ve_ratio_175k\\\": 0.8274, \\\"eval_return_215k\\\": 590.17, \\\"ve_ratio_215k\\\": 0.1365, \\\"peak_ve_ratio\\\": 6.8121, \\\"peak_ve_step\\\": 145000, \\\"conclusion_detail\\\": \\\"Obs-decoder SGS delayed CIVO onset (healthy at 105K, NVE=0.56x) but failed to prevent late collapse (135K NVE=5.47x, peak 6.81x at 145K, partial recovery to 0.83x at 175K). Final eval_return recovered to 590 but value_mean collapsed to 80.6 (ve_ratio=0.14x). Late-onset CIVO variant.\\\"}, \\\"completed_at\\\": \\\"2026-05-20T00:49:00.531Z\\\"}, \\\"exp_001_baseline_s4_extended\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T23:03:24.044Z\\\", \\\"updated_at\\\": \\\"2026-05-19T23:03:47.714Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py (extended from 250k to 520k steps)\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamer_s4_baseline\\\", \\\"seed\\\": 4}, \\\"hypothesis\\\": \\\"Extending baseline S4 training from 250k to 520k steps will show whether eval_return plateaus or continues improving, establishing the convergence profile for NVE robustness analysis.\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/checkpoint.ckpt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/train_extended.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T23:03:46.304Z\\\", \\\"metrics\\\": {\\\"final_step\\\": 520000, \\\"final_eval_step\\\": 512000, \\\"final_eval_return\\\": 938.86, \\\"total_eval_checkpoints\\\": 52}}, \\\"exp_008e_v3_s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T11:35:59.034Z\\\", \\\"updated_at\\\": \\\"2026-05-18T11:36:30.618Z\\\", \\\"metrics\\\": {\\\"eval_trajectory\\\": {\\\"5K\\\": 30.91, \\\"15K\\\": 343.66, \\\"25K\\\": 450.28, \\\"35K\\\": 527.44, \\\"45K\\\": 652.29, \\\"55K\\\": 717.96, \\\"65K\\\": 736.58, \\\"75K\\\": 751.73, \\\"85K\\\": 818.75, \\\"95K\\\": 835.34, \\\"105K\\\": 899.33}, \\\"value_trajectory\\\": {\\\"5K\\\": 0.002, \\\"15K\\\": 5.03, \\\"25K\\\": 46.89, \\\"35K\\\": 112.41, \\\"45K\\\": 186.9, \\\"55K\\\": 264.08, \\\"65K\\\": 343.83, \\\"75K\\\": 413.29, \\\"85K\\\": 467.89, \\\"95K\\\": 523.46, \\\"105K\\\": 547.4}, \\\"actor_entropy_trajectory\\\": {\\\"5K\\\": 8.19, \\\"15K\\\": 0.856, \\\"25K\\\": -2.478, \\\"35K\\\": -3.568, \\\"45K\\\": -4.167, \\\"55K\\\": -4.515, \\\"65K\\\": -4.7, \\\"75K\\\": -4.646, \\\"85K\\\": -5.029, \\\"95K\\\": -5.103, \\\"105K\\\": -5.084}, \\\"ve_ratio_trajectory\\\": {\\\"15K\\\": 0.0146, \\\"25K\\\": 0.1041, \\\"35K\\\": 0.2131, \\\"45K\\\": 0.2865, \\\"55K\\\": 0.3678, \\\"65K\\\": 0.4667, \\\"75K\\\": 0.5497, \\\"85K\\\": 0.5714, \\\"95K\\\": 0.6266, \\\"105K\\\": 0.6087}, \\\"nve_trajectory\\\": {\\\"15K\\\": 0.022, \\\"25K\\\": 0.16, \\\"35K\\\": 0.328, \\\"45K\\\": 0.441, \\\"55K\\\": 0.567, \\\"65K\\\": 0.719, \\\"75K\\\": 0.847, \\\"85K\\\": 0.88, \\\"95K\\\": 0.965, \\\"105K\\\": 0.938}, \\\"final_eval_return\\\": 899.33, \\\"peak_eval_return\\\": 899.33, \\\"peak_eval_step\\\": 105000, \\\"final_value_mean\\\": 547.4, \\\"final_ve_ratio\\\": 0.6087, \\\"final_nve\\\": 0.938, \\\"gate_dt_mean\\\": 1, \\\"gate_dt_1_frac\\\": 1, \\\"gate_dt_std\\\": 0, \\\"gate_empirical_entropy\\\": 0}, \\\"conclusion\\\": \\\"success\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15 --checkpoint_every 25000\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3\\\", \\\"seed\\\": 4}, \\\"hypothesis\\\": \\\"C6 dual-pathway (trained dt_emb + subsample ON, gate_fixed_dt=1, gate_subsample_max_dt=2, H=15) will maintain stable training without value-overestimation collapse across multiple seeds on Walker Walk 105K, validating that the subsample pathway does not introduce systematic instability.\\\", \\\"parent\\\": \\\"exp_008e_v3_subsample_on_dt1_h15\\\", \\\"completed_at\\\": \\\"2026-05-18T11:36:30.618Z\\\"}, \\\"exp_010b_cheetah_civo_trigger_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T05:08:57.636Z\\\", \\\"updated_at\\\": \\\"2026-05-18T05:09:31.471Z\\\", \\\"hypothesis\\\": \\\"CIVO (value overestimation collapse) in Cheetah Run with dt_emb + subsample ON + H=8 is reproducible across seeds. Seed=0 should exhibit NVE>1.5× and eval return collapse similar to seed=1 (NVE=8.27×).\\\", \\\"parent\\\": \\\"exp_010b_cheetah_civo_trigger\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train.py --config cheetah_civo_trigger --seed 0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"dm_control/cheetah_run\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3_event_gated\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"dm_control/cheetah_run\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-18T05:09:28.232Z\\\", \\\"metrics\\\": {\\\"final_step\\\": 112000, \\\"peak_eval_return\\\": 247.77, \\\"peak_eval_step\\\": 35000, \\\"final_eval_return\\\": 0.83, \\\"final_NVE\\\": 70.64, \\\"first_civo_alert_step\\\": 95000, \\\"first_civo_alert_NVE\\\": 6.34, \\\"value_mean_at_105k\\\": 58.58, \\\"gate_dt_mean\\\": 2, \\\"gate_entropy\\\": 0, \\\"gate_dt_2_frac\\\": 1}}, \\\"exp_016d_sgs_walker_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T19:29:07.960Z\\\", \\\"updated_at\\\": \\\"2026-05-16T01:43:55.477Z\\\", \\\"hypothesis\\\": \\\"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心（plan_016）。修复 eval video deadlock (D056) 后重试\\\", \\\"parent\\\": \\\"exp_008d_subsample_on_h8\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 105000, \\\"model_name\\\": \\\"dreamerv3-sgs\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"exp_008d_subsample_on_h8\\\", \\\"eval_data\\\": \\\"dmc_walker_walk\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-16T01:43:55.477Z\\\"}, \\\"exp_005_event_gated_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T21:53:45.066Z\\\", \\\"updated_at\\\": \\\"2026-05-13T21:54:17.129Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"failure_reason\\\": \\\"结构性失败(D009): return最终47.4(baseline 5%), gate激活后return单调下降无恢复。85K/105K registry数据已修正为metrics.jsonl实际值(212.3/276.1, 旧值319.3/337.8系误录)。\\\", \\\"metrics\\\": {\\\"step\\\": 145000, \\\"final_eval_return\\\": 98.84, \\\"peak_eval_return\\\": 541.18, \\\"peak_eval_step\\\": 55000, \\\"eval_return_85K\\\": 212.34, \\\"eval_return_105K\\\": 276.08, \\\"eval_return_115K\\\": 25.67, \\\"eval_return_145K\\\": 98.84}, \\\"spec\\\": {\\\"command\\\": \\\"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --gate_enabled True\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3-event-gated-v4\\\", \\\"seed\\\": 1, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1\\\"}, \\\"completed_at\\\": \\\"2026-05-13T21:54:17.129Z\\\"}, \\\"exp_001_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T20:57:32.713Z\\\", \\\"updated_at\\\": \\\"2026-05-13T21:53:44.698Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"step\\\": 512000, \\\"final_eval_return\\\": 970.4, \\\"eval_return_last10_mean\\\": 950.9, \\\"eval_return_last10_std\\\": 10.5, \\\"fps\\\": 7.59}, \\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs walker_walk --run.steps 512000\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"dreamerv3-baseline\\\", \\\"seed\\\": 1, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\\\"}, \\\"completed_at\\\": \\\"2026-05-13T20:58:00.944Z\\\"}}, \\\"count\\\": 32, \\\"total\\\": 32, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1157}}\"}",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---


### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
The registry output is very large. Let me read the full file to get all experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a2a04368-af9e-4cde-abd9-79bc208d7897",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EPBPADo7undivsq7kKcs6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24878,
      "cache_read_input_tokens": 27143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24878
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

数据量大，我需要读取完整的 registry 输出来解析所有实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a868fe9b-d605-442c-bcd2-c164aed3e772",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EPBPADo7undivsq7kKcs6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24878,
      "cache_read_input_tokens": 27143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24878
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

<details open><summary>🔧 Tool call — Read · `toolu_01PELXYFLWWgTB3NoudehXF5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/toolu_01JX9RXCDmaW6GwtGX8TK4Wh.txt",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "442f7c28-f82c-4f23-93da-3cf79fabc7b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EPBPADo7undivsq7kKcs6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24878,
      "cache_read_input_tokens": 27143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24878
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

_source line 19 · 2026-05-29T00:34:38.047Z_

<details><summary>↩ Tool result · `toolu_01PELXYFLWWgTB3NoudehXF5`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (200). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "4ab3335f-b44e-45b7-9396-d3fb51202966",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/toolu_01JX9RXCDmaW6GwtGX8TK4Wh.txt",
      "content": "",
      "numLines": 0,
      "startLine": 200,
      "totalLines": 1
    }
  }
}
```

</details>

---


### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
The file is only 1 line long but contains a massive JSON. Let me use a different approach - parse the data with a script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "3a943353-796d-41c5-b30d-653d27cb8e74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRGu6CHD1YLrsyf9mG5tXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 52021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 286
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

_source line 21_

用脚本解析 registry 数据并按分组提取 eval_return。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "57316e0a-0320-4b77-89b4-8ffd5634f4b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRGu6CHD1YLrsyf9mG5tXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 52021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 286
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

<details open><summary>🔧 Tool call — Bash · `toolu_01SeiGpGq6gdfpitLNYG23NE`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results && python3 << 'PYEOF'\nimport json\n\nwith open(\"toolu_01JX9RXCDmaW6GwtGX8TK4Wh.txt\") as f:\n    raw = json.loads(f.read())\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\n# Print all experiments with key info\nfor eid, exp in experiments.items():\n    hyp = exp.get(\"hypothesis\", \"\")\n    conclusion = exp.get(\"conclusion\", \"\")\n    metrics = exp.get(\"metrics\", {})\n    \n    # Find eval_return fields\n    eval_keys = [k for k in metrics.keys() if \"eval\" in k.lower() and (\"return\" in k.lower() or \"final\" in k.lower())]\n    eval_vals = {k: metrics[k] for k in eval_keys}\n    \n    spec = exp.get(\"spec\", {})\n    cmd = spec.get(\"command\", \"\")\n    \n    print(f\"\\n=== {eid} ===\")\n    print(f\"  conclusion: {conclusion}\")\n    print(f\"  hypothesis: {hyp[:150]}\")\n    print(f\"  eval fields: {eval_vals}\")\n    print(f\"  command snippet: {cmd[:120]}\")\nPYEOF\n",
  "description": "Parse registry JSON and list all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "be4246ea-f875-4da6-a3f5-ad9d89c3f6f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRGu6CHD1YLrsyf9mG5tXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 52021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 286
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

_source line 23 · 2026-05-29T00:34:47.088Z_

<details><summary>↩ Tool result · `toolu_01SeiGpGq6gdfpitLNYG23NE`</summary>

```text
=== exp_walker_no_dt_emb_s0 ===
  conclusion: killed
  hypothesis: 
  eval fields: {}
  command snippet: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENG

=== exp_hopper_frozen_s0_ext ===
  conclusion: negative
  hypothesis: Extending frozen_s0 from 105K to 150K will show eval_return recovery with ve_ratio declining, confirming frozen_s0's degenerate CIVO at 95K is transie
  eval fields: {'eval_return_final': 0.56, 'eval_return_peak': 3.58, 'eval_return_peak_step': 85000}
  command snippet: python train.py --config hopper_frozen_s0 --steps 160000

=== exp_hopper_baseline ===
  conclusion: success
  hypothesis: Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value ov
  eval fields: {'eval_final': 96.43, 'eval_return_trajectory': {'5000': 0.06, '15000': 1.04, '25000': 1.7, '35000': 6.55, '45000': 19.09, '55000': 22.52, '65000': 3.5, '75000': 62.2, '85000': 67.62, '95000': 86.47, '105000': 96.43}}
  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 10

=== exp_097_cheetah_008d_s3 ===
  conclusion: success
  hypothesis: C1 trigger seed 3: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 Cheetah 上的第四个 seed（s3）。当前 onset rate 2/3（s0 NVE=4.1×✓, s1 NVE=0.517✗, s2 NVE=
  eval fields: {'eval_final': 61.7, 'eval_final_pct_baseline': -86, 'baseline_eval_return': 446.1}
  command snippet: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENG

=== exp_100_walker_008a_s1 ===
  conclusion: success
  hypothesis: Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 Walker 008a 第 2 seed。与 exp_008a_no_subsample_dt2 (
  eval fields: {'eval_return_trajectory': {'5000': 31, '15000': 168.77, '25000': 158.03, '35000': 202.91, '45000': 305.98, '55000': 457.28, '65000': 628.82, '75000': 686.98, '85000': 656.64, '95000': 717.74, '105000': 750.59}, 'eval_final': 750.59, 'eval_final_pct_baseline': -18, 'baseline_eval_return': 915.67}
  command snippet: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENG

=== rssm_fidelity_v2 ===
  conclusion: success
  hypothesis: RSSM fidelity v2 分析：对比 4 类模型（baseline/trained_dt_emb/no_dt_emb/frozen）在 dt=1 vs dt=2 下的 observation/reward reconstruction loss。使用 Walker checkpoint (n
  eval fields: {}
  command snippet: CUDA_VISIBLE_DEVICES=1 python analyze_rssm_fidelity_v2.py --device cuda:0

=== exp_057_frozen_dt_emb_walker_s2 ===
  conclusion: failed
  hypothesis: Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO 
  eval fields: {}
  command snippet: cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate bas

=== exp_051_stackcube_frozen_dt_emb_s0 ===
  conclusion: failed
  hypothesis: Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish
  eval fields: {}
  command snippet: CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -

=== exp_049_stackcube_civo_trigger_s0 ===
  conclusion: failed
  hypothesis: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion（Walker/Cheetah）推广到 mani
  eval fields: {}
  command snippet: python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False

=== exp_081_008e_v3_walker_s2 ===
  conclusion: success
  hypothesis: Trained dt_emb with dt=1 imagination and subsample ON (max_dt=2) does not trigger CIVO in Walker Walk, as the value function sees only single-step pre
  eval fields: {'eval_return_105K': 597.1}
  command snippet: python train.py --config 008e_v3 --env walker_walk --seed 2

=== exp_073_008f_walker_s4 ===
  conclusion: success
  hypothesis: Removing dt_embedding (dt_embed_dim=0) in the 008f control config prevents CIVO onset because the agent cannot form temporally-conditioned value predi
  eval fields: {'eval_return_final': 289.3, 'eval_return_peak': 486.5, 'eval_return_peak_step': 75000}
  command snippet: python train.py --config 008f --seed 4

=== exp_069_008f_walker_repro_s1 ===
  conclusion: success
  hypothesis: Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk. With no learned temporal embedding, the value network cannot develop t
  eval fields: {'eval_return_final': 237.8, 'eval_return_final_step': 105000, 'eval_return_peak': 390.1, 'eval_return_peak_step': 95000, 'eval_return_trajectory': {'5K': 30.5, '15K': 158.7, '25K': 180.8, '35K': 250.3, '45K': 293.6, '55K': 272.2, '65K': 328.1, '75K': 244.8, '85K': 382.5, '95K': 390.1, '105K': 237.8}}
  command snippet: python train.py --configs dmc_vision --task dmc_walker_walk --seed 1 --logdir logdir/exp_069_008f_walker_repro_s1

=== exp_055_peginsertion_civo_trigger_s1 ===
  conclusion: success
  hypothesis: PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，162.5K 时仍 1.94）。如果 s1 也触发持续 CIVO → PegInsertion 是最严重的 CIVO 环境（比 Sta
  eval fields: {'eval_final': 11.44, 'eval_final_step': 212500}
  command snippet: python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --com

=== exp_048_cheetah_civo_extension ===
  conclusion: success
  hypothesis: Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 
  eval fields: {'eval_final': 23.423}
  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --dev

=== exp_047_frozen_dt_emb_walker_s1 ===
  conclusion: success
  hypothesis: Freezing dt_emb in Walker Walk (seed 1) prevents sustained CIVO collapse, replicating exp_042 (seed 0, NVE=0.19) finding that removing dt conditioning
  eval fields: {'eval_final': 144.22, 'eval_final_step': 215000}
  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --dev

=== exp_046_frozen_dt_emb_cheetah ===
  conclusion: success
  hypothesis: Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_04
  eval fields: {'eval_final': 150.5}
  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --dev

=== exp_048_stackcube_civo_trigger_s0 ===
  conclusion: killed
  hypothesis: ManiSkill Phase 1 scout: CIVO trigger config (trained dt_emb + subsample ON + H=8) on StackCube-v1 manipulation task. Tests whether CIVO generalizes b
  eval fields: {}
  command snippet: python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False

=== exp_045_treatment_extension_008d_s3 ===
  conclusion: success
  hypothesis: CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation
  eval fields: {'eval_final': 867.6}
  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --dev

=== exp_036_dual_critic_pickcube ===
  conclusion: negative
  hypothesis: Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention gener
  eval fields: {'eval_return_final': 27.7, 'eval_return_peak': 27.7, 'eval_return_peak_step': 202500, 'eval_return_trajectory': {'2.5K': 2, '12.5K': 17.5, '22.5K': 17.5, '32.5K': 11.6, '42.5K': 15.6, '52.5K': 11.7, '62.5K': 18.8, '72.5K': 5.4, '82.5K': 22.5, '92.5K': 18.1, '102.5K': 8.4, '112.5K': 7.1, '122.5K': 9.1, '132.5K': 12.8, '142.5K': 14, '152.5K': 13.1, '162.5K': 16.2, '172.5K': 19.7, '182.5K': 16.8, '192.5K': 13.7, '202.5K': 27.7}}
  command snippet: python train.py --task ManiSkill_PickCube-v1 --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horiz

=== exp_034_dual_critic_cheetah ===
  conclusion: negative
  hypothesis: Dual-critic on Cheetah Run: TCN failed at all σ on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a
  eval fields: {'eval_return_peak': 315.7, 'eval_return_peak_step': 45000, 'eval_return_final': 97.5, 'eval_return_trajectory': {'5K': 8.3, '15K': 27.8, '25K': 108.7, '35K': 110, '45K': 315.7, '55K': 34.5, '65K': 81.5, '75K': 183, '85K': 88.4, '95K': 41, '105K': 27.2, '115K': 45.9, '125K': 58.7, '135K': 71.6, '145K': 61.9, '155K': 52.1, '165K': 153.8, '175K': 104.9, '185K': 101.4, '195K': 115.3, '205K': 101.5, '215K': 97.5}}
  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_034_dual_critic_cheetah -

=== exp_029d_tcn_walker_s3_sigma02 ===
  conclusion: negative
  hypothesis: Fourth TCN σ=0.2 seed to match 4 baseline seeds for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwa
  eval fields: {'eval_return_final': 104.5, 'eval_return_peak': 349.6, 'eval_return_peak_step': 95000, 'eval_return_105K': 71.8, 'eval_return_trajectory': {'5K': 31.7, '15K': 159.1, '25K': 155.7, '35K': 190.8, '45K': 137.1, '55K': 210.7, '65K': 189.5, '75K': 253.2, '85K': 259.5, '95K': 349.6, '105K': 71.8, '115K': 69.8, '125K': 61.5, '135K': 141.8, '145K': 98.7, '155K': 88.9, '165K': 86.2, '175K': 123.5, '185K': 153.7, '195K': 68.8, '205K': 63.7, '215K': 104.5}}
  command snippet: python train.py --config walker_walk_tcn --seed 3 --tcn_sigma 0.2

=== exp_025_obs_sgs_walker_s1 ===
  conclusion: success
  hypothesis: Obs-decoder stop-gradient on symlog (SGS) prevents CIVO in Walker by breaking the value→decoder→representation gradient pathway, keeping NVE below 1.5
  eval fields: {'final_eval_return': 726.41}
  command snippet: python dreamer.py --configs dmc_vision --task dmc_walker_walk --obs_decoder_sgs true --seed 1

=== exp_025_obs_sgs_walker_s4 ===
  conclusion: negative
  hypothesis: Blocking observation-decoder gradients via stop-gradient (SGS) on Walker will prevent early-onset CIVO by decoupling representation learning from valu
  eval fields: {'final_eval_return': 241.47}
  command snippet: python train.py --configs walker_obs_sgs --seed 4

=== exp_026_obs_sgs_cheetah_s1 ===
  conclusion: negative
  hypothesis: Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value 
  eval fields: {'final_eval_return': 38.26}
  command snippet: python train.py --configs cheetah_obs_sgs --seed 1

=== exp_026_obs_sgs_cheetah_s0 ===
  conclusion: negative
  hypothesis: Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value 
  eval fields: {'final_eval_return': 38.76}
  command snippet: python train.py --configs cheetah_obs_sgs --seed 0

=== exp_025_obs_sgs_walker_s3 ===
  conclusion: negative
  hypothesis: Observation-decoder SGS regularization will prevent CIVO collapse by grounding value estimates through auxiliary reconstruction loss, maintaining heal
  eval fields: {'eval_return_105k': 818.58, 'eval_return_135k': 66.95, 'eval_return_145k': 43.75, 'eval_return_175k': 193.92, 'eval_return_215k': 590.17}
  command snippet: python3 train.py --config configs/exp_025_obs_sgs_walker_s3.yaml

=== exp_001_baseline_s4_extended ===
  conclusion: success
  hypothesis: Extending baseline S4 training from 250k to 520k steps will show whether eval_return plateaus or continues improving, establishing the convergence pro
  eval fields: {'final_eval_step': 512000, 'final_eval_return': 938.86}
  command snippet: python train.py (extended from 250k to 520k steps)

=== exp_008e_v3_s4 ===
  conclusion: success
  hypothesis: C6 dual-pathway (trained dt_emb + subsample ON, gate_fixed_dt=1, gate_subsample_max_dt=2, H=15) will maintain stable training without value-overestima
  eval fields: {'final_eval_return': 899.33, 'peak_eval_return': 899.33}
  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_s4 --steps 105000

=== exp_010b_cheetah_civo_trigger_s0 ===
  conclusion: success
  hypothesis: CIVO (value overestimation collapse) in Cheetah Run with dt_emb + subsample ON + H=8 is reproducible across seeds. Seed=0 should exhibit NVE>1.5× and 
  eval fields: {'peak_eval_return': 247.77, 'final_eval_return': 0.83}
  command snippet: python train.py --config cheetah_civo_trigger --seed 0

=== exp_016d_sgs_walker_s1 ===
  conclusion: failed
  hypothesis: Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心（plan_016）。修复 eval video deadlock (D056) 后重试
  eval fields: {}
  command snippet: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizo

=== exp_005_event_gated_v4 ===
  conclusion: negative
  hypothesis: 
  eval fields: {'final_eval_return': 98.84, 'peak_eval_return': 541.18, 'eval_return_85K': 212.34, 'eval_return_105K': 276.08, 'eval_return_115K': 25.67, 'eval_return_145K': 98.84}
  command snippet: python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000

=== exp_001_baseline ===
  conclusion: success
  hypothesis: 
  eval fields: {'final_eval_return': 970.4, 'eval_return_last10_mean': 950.9, 'eval_return_last10_std': 10.5}
  command snippet: python train.py --configs walker_walk --run.steps 512000
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "e16926dd-d822-4968-beb2-0dd1ed2a7892",
  "tool_use_result": {
    "stdout": "=== exp_walker_no_dt_emb_s0 ===\n  conclusion: killed\n  hypothesis: \n  eval fields: {}\n  command snippet: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENG\n\n=== exp_hopper_frozen_s0_ext ===\n  conclusion: negative\n  hypothesis: Extending frozen_s0 from 105K to 150K will show eval_return recovery with ve_ratio declining, confirming frozen_s0's degenerate CIVO at 95K is transie\n  eval fields: {'eval_return_final': 0.56, 'eval_return_peak': 3.58, 'eval_return_peak_step': 85000}\n  command snippet: python train.py --config hopper_frozen_s0 --steps 160000\n\n=== exp_hopper_baseline ===\n  conclusion: success\n  hypothesis: Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value ov\n  eval fields: {'eval_final': 96.43, 'eval_return_trajectory': {'5000': 0.06, '15000': 1.04, '25000': 1.7, '35000': 6.55, '45000': 19.09, '55000': 22.52, '65000': 3.5, '75000': 62.2, '85000': 67.62, '95000': 86.47, '105000': 96.43}}\n  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 10\n\n=== exp_097_cheetah_008d_s3 ===\n  conclusion: success\n  hypothesis: C1 trigger seed 3: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 Cheetah 上的第四个 seed（s3）。当前 onset rate 2/3（s0 NVE=4.1×✓, s1 NVE=0.517✗, s2 NVE=\n  eval fields: {'eval_final': 61.7, 'eval_final_pct_baseline': -86, 'baseline_eval_return': 446.1}\n  command snippet: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENG\n\n=== exp_100_walker_008a_s1 ===\n  conclusion: success\n  hypothesis: Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 Walker 008a 第 2 seed。与 exp_008a_no_subsample_dt2 (\n  eval fields: {'eval_return_trajectory': {'5000': 31, '15000': 168.77, '25000': 158.03, '35000': 202.91, '45000': 305.98, '55000': 457.28, '65000': 628.82, '75000': 686.98, '85000': 656.64, '95000': 717.74, '105000': 750.59}, 'eval_final': 750.59, 'eval_final_pct_baseline': -18, 'baseline_eval_return': 915.67}\n  command snippet: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENG\n\n=== rssm_fidelity_v2 ===\n  conclusion: success\n  hypothesis: RSSM fidelity v2 分析：对比 4 类模型（baseline/trained_dt_emb/no_dt_emb/frozen）在 dt=1 vs dt=2 下的 observation/reward reconstruction loss。使用 Walker checkpoint (n\n  eval fields: {}\n  command snippet: CUDA_VISIBLE_DEVICES=1 python analyze_rssm_fidelity_v2.py --device cuda:0\n\n=== exp_057_frozen_dt_emb_walker_s2 ===\n  conclusion: failed\n  hypothesis: Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO \n  eval fields: {}\n  command snippet: cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate bas\n\n=== exp_051_stackcube_frozen_dt_emb_s0 ===\n  conclusion: failed\n  hypothesis: Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish\n  eval fields: {}\n  command snippet: CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -\n\n=== exp_049_stackcube_civo_trigger_s0 ===\n  conclusion: failed\n  hypothesis: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion（Walker/Cheetah）推广到 mani\n  eval fields: {}\n  command snippet: python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False\n\n=== exp_081_008e_v3_walker_s2 ===\n  conclusion: success\n  hypothesis: Trained dt_emb with dt=1 imagination and subsample ON (max_dt=2) does not trigger CIVO in Walker Walk, as the value function sees only single-step pre\n  eval fields: {'eval_return_105K': 597.1}\n  command snippet: python train.py --config 008e_v3 --env walker_walk --seed 2\n\n=== exp_073_008f_walker_s4 ===\n  conclusion: success\n  hypothesis: Removing dt_embedding (dt_embed_dim=0) in the 008f control config prevents CIVO onset because the agent cannot form temporally-conditioned value predi\n  eval fields: {'eval_return_final': 289.3, 'eval_return_peak': 486.5, 'eval_return_peak_step': 75000}\n  command snippet: python train.py --config 008f --seed 4\n\n=== exp_069_008f_walker_repro_s1 ===\n  conclusion: success\n  hypothesis: Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk. With no learned temporal embedding, the value network cannot develop t\n  eval fields: {'eval_return_final': 237.8, 'eval_return_final_step': 105000, 'eval_return_peak': 390.1, 'eval_return_peak_step': 95000, 'eval_return_trajectory': {'5K': 30.5, '15K': 158.7, '25K': 180.8, '35K': 250.3, '45K': 293.6, '55K': 272.2, '65K': 328.1, '75K': 244.8, '85K': 382.5, '95K': 390.1, '105K': 237.8}}\n  command snippet: python train.py --configs dmc_vision --task dmc_walker_walk --seed 1 --logdir logdir/exp_069_008f_walker_repro_s1\n\n=== exp_055_peginsertion_civo_trigger_s1 ===\n  conclusion: success\n  hypothesis: PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，162.5K 时仍 1.94）。如果 s1 也触发持续 CIVO → PegInsertion 是最严重的 CIVO 环境（比 Sta\n  eval fields: {'eval_final': 11.44, 'eval_final_step': 212500}\n  command snippet: python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --com\n\n=== exp_048_cheetah_civo_extension ===\n  conclusion: success\n  hypothesis: Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio \n  eval fields: {'eval_final': 23.423}\n  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --dev\n\n=== exp_047_frozen_dt_emb_walker_s1 ===\n  conclusion: success\n  hypothesis: Freezing dt_emb in Walker Walk (seed 1) prevents sustained CIVO collapse, replicating exp_042 (seed 0, NVE=0.19) finding that removing dt conditioning\n  eval fields: {'eval_final': 144.22, 'eval_final_step': 215000}\n  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --dev\n\n=== exp_046_frozen_dt_emb_cheetah ===\n  conclusion: success\n  hypothesis: Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_04\n  eval fields: {'eval_final': 150.5}\n  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --dev\n\n=== exp_048_stackcube_civo_trigger_s0 ===\n  conclusion: killed\n  hypothesis: ManiSkill Phase 1 scout: CIVO trigger config (trained dt_emb + subsample ON + H=8) on StackCube-v1 manipulation task. Tests whether CIVO generalizes b\n  eval fields: {}\n  command snippet: python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False\n\n=== exp_045_treatment_extension_008d_s3 ===\n  conclusion: success\n  hypothesis: CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation\n  eval fields: {'eval_final': 867.6}\n  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --dev\n\n=== exp_036_dual_critic_pickcube ===\n  conclusion: negative\n  hypothesis: Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention gener\n  eval fields: {'eval_return_final': 27.7, 'eval_return_peak': 27.7, 'eval_return_peak_step': 202500, 'eval_return_trajectory': {'2.5K': 2, '12.5K': 17.5, '22.5K': 17.5, '32.5K': 11.6, '42.5K': 15.6, '52.5K': 11.7, '62.5K': 18.8, '72.5K': 5.4, '82.5K': 22.5, '92.5K': 18.1, '102.5K': 8.4, '112.5K': 7.1, '122.5K': 9.1, '132.5K': 12.8, '142.5K': 14, '152.5K': 13.1, '162.5K': 16.2, '172.5K': 19.7, '182.5K': 16.8, '192.5K': 13.7, '202.5K': 27.7}}\n  command snippet: python train.py --task ManiSkill_PickCube-v1 --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horiz\n\n=== exp_034_dual_critic_cheetah ===\n  conclusion: negative\n  hypothesis: Dual-critic on Cheetah Run: TCN failed at all σ on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a\n  eval fields: {'eval_return_peak': 315.7, 'eval_return_peak_step': 45000, 'eval_return_final': 97.5, 'eval_return_trajectory': {'5K': 8.3, '15K': 27.8, '25K': 108.7, '35K': 110, '45K': 315.7, '55K': 34.5, '65K': 81.5, '75K': 183, '85K': 88.4, '95K': 41, '105K': 27.2, '115K': 45.9, '125K': 58.7, '135K': 71.6, '145K': 61.9, '155K': 52.1, '165K': 153.8, '175K': 104.9, '185K': 101.4, '195K': 115.3, '205K': 101.5, '215K': 97.5}}\n  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_034_dual_critic_cheetah -\n\n=== exp_029d_tcn_walker_s3_sigma02 ===\n  conclusion: negative\n  hypothesis: Fourth TCN σ=0.2 seed to match 4 baseline seeds for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwa\n  eval fields: {'eval_return_final': 104.5, 'eval_return_peak': 349.6, 'eval_return_peak_step': 95000, 'eval_return_105K': 71.8, 'eval_return_trajectory': {'5K': 31.7, '15K': 159.1, '25K': 155.7, '35K': 190.8, '45K': 137.1, '55K': 210.7, '65K': 189.5, '75K': 253.2, '85K': 259.5, '95K': 349.6, '105K': 71.8, '115K': 69.8, '125K': 61.5, '135K': 141.8, '145K': 98.7, '155K': 88.9, '165K': 86.2, '175K': 123.5, '185K': 153.7, '195K': 68.8, '205K': 63.7, '215K': 104.5}}\n  command snippet: python train.py --config walker_walk_tcn --seed 3 --tcn_sigma 0.2\n\n=== exp_025_obs_sgs_walker_s1 ===\n  conclusion: success\n  hypothesis: Obs-decoder stop-gradient on symlog (SGS) prevents CIVO in Walker by breaking the value→decoder→representation gradient pathway, keeping NVE below 1.5\n  eval fields: {'final_eval_return': 726.41}\n  command snippet: python dreamer.py --configs dmc_vision --task dmc_walker_walk --obs_decoder_sgs true --seed 1\n\n=== exp_025_obs_sgs_walker_s4 ===\n  conclusion: negative\n  hypothesis: Blocking observation-decoder gradients via stop-gradient (SGS) on Walker will prevent early-onset CIVO by decoupling representation learning from valu\n  eval fields: {'final_eval_return': 241.47}\n  command snippet: python train.py --configs walker_obs_sgs --seed 4\n\n=== exp_026_obs_sgs_cheetah_s1 ===\n  conclusion: negative\n  hypothesis: Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value \n  eval fields: {'final_eval_return': 38.26}\n  command snippet: python train.py --configs cheetah_obs_sgs --seed 1\n\n=== exp_026_obs_sgs_cheetah_s0 ===\n  conclusion: negative\n  hypothesis: Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value \n  eval fields: {'final_eval_return': 38.76}\n  command snippet: python train.py --configs cheetah_obs_sgs --seed 0\n\n=== exp_025_obs_sgs_walker_s3 ===\n  conclusion: negative\n  hypothesis: Observation-decoder SGS regularization will prevent CIVO collapse by grounding value estimates through auxiliary reconstruction loss, maintaining heal\n  eval fields: {'eval_return_105k': 818.58, 'eval_return_135k': 66.95, 'eval_return_145k': 43.75, 'eval_return_175k': 193.92, 'eval_return_215k': 590.17}\n  command snippet: python3 train.py --config configs/exp_025_obs_sgs_walker_s3.yaml\n\n=== exp_001_baseline_s4_extended ===\n  conclusion: success\n  hypothesis: Extending baseline S4 training from 250k to 520k steps will show whether eval_return plateaus or continues improving, establishing the convergence pro\n  eval fields: {'final_eval_step': 512000, 'final_eval_return': 938.86}\n  command snippet: python train.py (extended from 250k to 520k steps)\n\n=== exp_008e_v3_s4 ===\n  conclusion: success\n  hypothesis: C6 dual-pathway (trained dt_emb + subsample ON, gate_fixed_dt=1, gate_subsample_max_dt=2, H=15) will maintain stable training without value-overestima\n  eval fields: {'final_eval_return': 899.33, 'peak_eval_return': 899.33}\n  command snippet: python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_s4 --steps 105000\n\n=== exp_010b_cheetah_civo_trigger_s0 ===\n  conclusion: success\n  hypothesis: CIVO (value overestimation collapse) in Cheetah Run with dt_emb + subsample ON + H=8 is reproducible across seeds. Seed=0 should exhibit NVE>1.5× and \n  eval fields: {'peak_eval_return': 247.77, 'final_eval_return': 0.83}\n  command snippet: python train.py --config cheetah_civo_trigger --seed 0\n\n=== exp_016d_sgs_walker_s1 ===\n  conclusion: failed\n  hypothesis: Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心（plan_016）。修复 eval video deadlock (D056) 后重试\n  eval fields: {}\n  command snippet: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizo\n\n=== exp_005_event_gated_v4 ===\n  conclusion: negative\n  hypothesis: \n  eval fields: {'final_eval_return': 98.84, 'peak_eval_return': 541.18, 'eval_return_85K': 212.34, 'eval_return_105K': 276.08, 'eval_return_115K': 25.67, 'eval_return_145K': 98.84}\n  command snippet: python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000\n\n=== exp_001_baseline ===\n  conclusion: success\n  hypothesis: \n  eval fields: {'final_eval_return': 970.4, 'eval_return_last10_mean': 950.9, 'eval_return_last10_std': 10.5}\n  command snippet: python train.py --configs walker_walk --run.steps 512000",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now I need to find the remaining experiments that weren't in the first 32 results. Let me also check if there are more experiments. The registry shows 32 experiments total. Let me now look for the missing ones - I need to identify experiments for each Table 2 row group. Let me also check for experiments that I haven't seen yet - the registry showed 32/32 so that's all.

Let me now look more carefully at what experiments exist but weren't printed in the first set. I see 32 experiments. Let me now map them.

But wait, I'm missing many experiments. The table mentions:
- Untreated: 10 seeds


- Reward-only SGS: 2 seeds
- Full-pathway SGS: 3 seeds
- Obs-decoder SGS: 6 seeds
- RAVE: 2 seeds
- TCN σ=0.1: 1 seed
- TCN σ=0.2: 6 seeds
- TCN σ=0.5: 3 seeds
- TCN σ=1.0: 1 seed
- Wide single: 2 seeds
- Narrow dual (min): 2 seeds
- Wide dual (min): 4 seeds
- Embedding frozen: 7 seeds
- Embedding removed: 6 seeds

That's way more than 32 total seeds across all these variants, so I'm clearly missing a lot of experiments in the registry.

The issue is that I filtered by `status: "DONE"` and got 32 results, but the conclusion (success/negative/failed/killed) is stored separately. Many of the experiments I'm looking for might have different status values entirely. Let me broaden my search and pull all experiments regardless of status to see what's actually available. I'm realizing I need to query the full experiment registry to see all available experiments across different methods and statuses, not just this filtered subset.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "db2e557c-880c-4482-9569-2934b5e95e04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aoqn8eWKm4UgkcsDdq9F7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6228,
      "cache_read_input_tokens": 52307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6228
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

_source line 25_

Registry 只有 32 个 DONE 实验，可能遗漏了其他状态的。获取全部实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "0f029fee-6b5e-40f1-8dbf-9fd8034ff1f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aoqn8eWKm4UgkcsDdq9F7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6228,
      "cache_read_input_tokens": 52307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6228
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

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BBLXW3zd3CYaqZvFxYgnSH`</summary>

```json
{
  "fields": [
    "*"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "c16cc11a-7323-4d72-a476-41a6bc5034c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aoqn8eWKm4UgkcsDdq9F7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6228,
      "cache_read_input_tokens": 52307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6228
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

_source line 27 · 2026-05-29T00:35:05.012Z_

<details><summary>↩ Tool result · `toolu_01BBLXW3zd3CYaqZvFxYgnSH`</summary>

```text
Error: result (67,219 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/mcp-agent-ml-research-read_registry-1780014904997.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/mcp-agent-ml-research-read_registry-1780014904997.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "8ee7efbe-7910-426e-a142-1d39b89110bb",
  "tool_use_result": {
    "content": "Error: result (67,219 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/mcp-agent-ml-research-read_registry-1780014904997.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/mcp-agent-ml-research-read_registry-1780014904997.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_walker_no_dt_emb_s1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T11:14:39.780Z\", \"updated_at\": \"2026-05-27T11:15:17.396Z\", \"hypothesis\": \"Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk seed=1. With no learned temporal embedding, the value network cannot develop compounding overestimation. This extends no_dt_emb evidence from seed=0 (exp_008f) and seed=1 (exp_069) to validate robustness.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-51268\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"105000 steps\", \"model_name\": \"dreamerv3\", \"seed\": 1, \"checkpoint_source\": \"none (train from scratch)\", \"eval_data\": \"dmc_walker_walk (built-in env)\"}}, \"exp_walker_no_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T11:10:24.895Z\", \"updated_at\": \"2026-05-27T11:14:46.202Z\", \"parent\": \"exp_008f\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-51268\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"105000 steps\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"checkpoint_source\": \"none (train from scratch)\", \"eval_data\": \"dmc_walker_walk (built-in env)\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-27T11:14:46.202Z\"}, \"exp_hopper_frozen_s0_ext\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T10:47:14.544Z\", \"updated_at\": \"2026-05-27T10:48:10.979Z\", \"conclusion\": \"negative\", \"metrics\": {\"eval_return_final\": 0.56, \"eval_return_peak\": 3.58, \"eval_return_peak_step\": 85000, \"ve_ratio_final\": 15.08, \"ve_ratio_peak\": 4335664.27, \"ve_ratio_peak_step\": 105000, \"value_mean_final\": 8.46, \"civo_alerts\": 2, \"civo_alert_steps\": [65000, 105000], \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"total_steps\": 160000, \"recovery\": false}, \"spec\": {\"checkpoint_path\": \"logdir/exp_hopper_frozen_s0/latest.pt\", \"log_path\": \"logdir/exp_hopper_frozen_s0/metrics.jsonl\", \"command\": \"python train.py --config hopper_frozen_s0 --steps 160000\", \"server\": \"westd-51268\", \"data_path\": \"Hopper-v4\", \"data_count\": 160000, \"model_name\": \"dreamer_v3_frozen_dt_emb\", \"seed\": 0}, \"hypothesis\": \"Extending frozen_s0 from 105K to 150K will show eval_return recovery with ve_ratio declining, confirming frozen_s0's degenerate CIVO at 95K is transient instability during severe learning delay rather than a permanent structural failure caused by the frozen dt_embedding.\", \"completed_at\": \"2026-05-27T10:48:10.979Z\"}, \"exp_hopper_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T05:51:24.680Z\", \"updated_at\": \"2026-05-27T05:52:01.157Z\", \"metrics\": {\"step\": 105000, \"eval_final\": 96.43, \"eval_return_trajectory\": {\"5000\": 0.06, \"15000\": 1.04, \"25000\": 1.7, \"35000\": 6.55, \"45000\": 19.09, \"55000\": 22.52, \"65000\": 3.5, \"75000\": 62.2, \"85000\": 67.62, \"95000\": 86.47, \"105000\": 96.43}, \"ve_ratio_trajectory\": {\"15000\": 0.08, \"25000\": 0.098, \"35000\": 0.166, \"45000\": 0.19, \"55000\": 0.279, \"65000\": 3.479, \"75000\": 0.341, \"85000\": 0.502, \"95000\": 0.517, \"105000\": 0.559}, \"nve_peak\": 3.48, \"nve_peak_step\": 65000, \"nve_final\": 0.559, \"civo_onset\": false, \"civo_alert_count\": 0, \"value_mean_final\": 53.9, \"target_mean_final\": 54.2, \"training_steps\": 105000, \"update_count\": 25099, \"fps\": 11}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_baseline/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_baseline.log\", \"hypothesis\": \"Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE < 1.5×). Source: C1/C2 third-environment verification (D160).\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0\", \"server\": \"westd-51268\", \"data_path\": \"dmc_hopper_hop\", \"data_count\": 105000, \"model_name\": \"DreamerV3 baseline (dt=1, no gate)\", \"seed\": 0}, \"completed_at\": \"2026-05-27T05:52:01.157Z\"}, \"exp_097_cheetah_008d_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:03:25.871Z\", \"updated_at\": \"2026-05-26T11:32:48.497Z\", \"hypothesis\": \"C1 trigger seed 3: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 Cheetah 上的第四个 seed（s3）。当前 onset rate 2/3（s0 NVE=4.1×✓, s1 NVE=0.517✗, s2 NVE=138.7×✓）。s3 完成后可计算完整 onset rate（n=4）。如果 onset ≥3/4 → 高 onset rate 支持 CIVO 是 systematic phenomenon；如果 2/4 → 50% onset rate 仍有意义但需讨论。\", \"parent\": \"exp_078_cheetah_008d_s0\", \"notes\": \"重新提交到 westd-51268 cuda:0。原 bjb1 提交 (PID 324959) 已死（服务器无卡）。exp_094 同配置在 westd 跑了 1.72h 后因 SSH 断连失败，检查其 checkpoint 是否可复用。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_097_cheetah_008d_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu_ids\": [0], \"pid\": 3794, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (trained dt_emb)\", \"seed\": 3, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_097_cheetah_008d_s3/train.log\", \"checkpoint_path\": \"logdir/exp_097_cheetah_008d_s3/latest.pt\"}, \"metrics\": {\"step\": 105000, \"nve_peak\": 2.3, \"nve_peak_step\": 45000, \"nve_final\": 0.3, \"civo_onset\": true, \"civo_onset_step\": 45000, \"civo_pattern\": \"transient→degraded\", \"eval_final\": 61.7, \"eval_final_pct_baseline\": -86, \"baseline_eval_return\": 446.1, \"gate_dt_2_frac\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T11:32:48.497Z\"}, \"exp_100_walker_008a_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:39:24.456Z\", \"updated_at\": \"2026-05-26T07:52:52.927Z\", \"hypothesis\": \"Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 Walker 008a 第 2 seed。与 exp_008a_no_subsample_dt2 (s0) 和 exp_074_008a_walker_s3 (s3) 共同建立 C3 value suppression 多 seed 证据。训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练，预期无 CIVO。plan_013。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_100_walker_008a_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"server\": \"westd-51268\", \"gpu_ids\": [1], \"pid\": 5591, \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (trained dt_emb, unexposed)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_100_walker_008a_s1/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_100_walker_008a_s1/latest.pt\"}, \"metrics\": {\"step\": 105000, \"eval_return_trajectory\": {\"5000\": 31, \"15000\": 168.77, \"25000\": 158.03, \"35000\": 202.91, \"45000\": 305.98, \"55000\": 457.28, \"65000\": 628.82, \"75000\": 686.98, \"85000\": 656.64, \"95000\": 717.74, \"105000\": 750.59}, \"ve_ratio_trajectory\": {\"15000\": 0.035, \"25000\": 0.206, \"35000\": 0.279, \"45000\": 0.261, \"55000\": 0.248, \"65000\": 0.234, \"75000\": 0.26, \"85000\": 0.315, \"95000\": 0.325, \"105000\": 0.328}, \"value_mean_trajectory\": {\"15000\": 5.98, \"25000\": 32.58, \"35000\": 56.55, \"45000\": 79.94, \"55000\": 113.33, \"65000\": 147.14, \"75000\": 178.73, \"85000\": 206.95, \"95000\": 233.17, \"105000\": 246.06}, \"nve_peak\": 0.328, \"nve_final\": 0.328, \"civo_onset\": false, \"eval_final\": 750.59, \"eval_final_pct_baseline\": -18, \"baseline_eval_return\": 915.67, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T07:52:45.733Z\", \"notes\": \"C3 Walker 008a s1 完成。训练正常结束(105K steps)。eval_return@105K=750.59 (baseline 915.67, -18.0%)。ve_ratio 全程 0.035-0.328，NVE_peak=0.328，远低于 τ=1.5×，civo/alert 全程 0.0，无 CIVO onset。Value suppression 确认（value_mean 持续低于 eval_return）。与 parent s0 (eval@105K=777.66, -15.1%, ve_ratio 0.37-0.54) 一致：s1 性能略低但趋势相同，两个 seed 均无 CIVO 且呈现 value suppression，C3 Walker 008a 2-seed 证据闭合。gate_dt 全程固定为 2.0 (100% dt_2_frac)，符合 gate_fixed_dt=2 配置。\"}, \"rssm_fidelity_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:47:46.584Z\", \"updated_at\": \"2026-05-26T03:47:59.871Z\", \"hypothesis\": \"RSSM fidelity v2 分析：对比 4 类模型（baseline/trained_dt_emb/no_dt_emb/frozen）在 dt=1 vs dt=2 下的 observation/reward reconstruction loss。使用 Walker checkpoint (n=800)。结果：trained_dt_emb reward ratio 1.50×, obs ratio 1.44×; baseline obs ratio 1.55×; no_dt_emb gap 最小 (1.23×/1.16×)。\", \"conclusion\": \"success\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python analyze_rssm_fidelity_v2.py --device cuda:0\", \"server\": \"westd-51268\", \"data_path\": \"Walker logdirs (exp_008d/009d/009c/084)\", \"data_count\": 800, \"model_name\": \"RSSM fidelity analysis v2\", \"seed\": 0, \"checkpoint_path\": \"analysis_rssm_fidelity_v2.json\", \"log_path\": \"N/A (analysis task)\"}, \"completed_at\": \"2026-05-26T03:47:59.871Z\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:26:00.391Z\", \"updated_at\": \"2026-05-26T03:03:45.406Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"N/A - bjb1-45299 lost GPU\", \"checkpoint_path\": \"N/A - bjb1-45299 lost GPU\", \"failure_reason\": \"bjb1-45299 server lost GPU allocation, experiment terminated\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T03:03:45.406Z\"}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:42:39.309Z\", \"updated_at\": \"2026-05-26T03:03:44.692Z\", \"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks\", \"parent\": \"exp_049\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"maniskill_StackCube-v1 (online RL)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, StackCube s0)\", \"seed\": 0, \"log_path\": \"N/A - bjb1-45299 lost GPU\", \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"maniskill_StackCube-v1 (online eval)\", \"checkpoint_path\": \"N/A - bjb1-45299 lost GPU\", \"failure_reason\": \"bjb1-45299 server lost GPU allocation, experiment terminated\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T03:03:44.692Z\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:14:38.578Z\", \"updated_at\": \"2026-05-26T03:03:42.946Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion（Walker/Cheetah）推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack），比 PickCube 更难。如果触发 CIVO → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"parent\": \"exp_048_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"N/A - bjb1-45299 lost GPU\", \"checkpoint_path\": \"N/A - bjb1-45299 lost GPU\", \"failure_reason\": \"bjb1-45299 server lost GPU allocation, experiment terminated\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T03:03:42.946Z\"}, \"exp_081_008e_v3_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T15:42:24.765Z\", \"updated_at\": \"2026-05-25T15:43:10.949Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 597.1, \"vs_baseline\": \"-34.8%\", \"vs_baseline_pct\": 65.2, \"baseline_105K\": 915.67, \"ve_ratio_peak\": 0.6, \"ve_ratio_final\": 0.5, \"NVE_est_peak\": 0.8, \"NVE_est_final\": 0.7, \"gate_dt_mean\": 1, \"gate_dt_1_frac\": 1, \"civo_alert_count\": 0, \"training_steps\": 105000, \"update_count\": 25099, \"value_mean_final\": 295}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_081_008e_v3_walker_s2/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"spec\": {\"command\": \"python train.py --config 008e_v3 --env walker_walk --seed 2\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3_008e_v3\", \"seed\": 2}, \"hypothesis\": \"Trained dt_emb with dt=1 imagination and subsample ON (max_dt=2) does not trigger CIVO in Walker Walk, as the value function sees only single-step predictions that match the world model's training distribution, preventing value inflation even with learned temporal embeddings.\", \"completed_at\": \"2026-05-25T15:43:10.949Z\"}, \"exp_078_cheetah_008d_s0\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:20:34.290Z\", \"updated_at\": \"2026-05-25T11:20:38.124Z\"}, \"exp_077_cheetah_baseline_s0\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:20:33.734Z\", \"updated_at\": \"2026-05-25T11:20:37.784Z\"}, \"exp_079_frozen_dt_emb_walker_s0\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:20:33.307Z\", \"updated_at\": \"2026-05-25T11:20:36.856Z\"}, \"exp_073_008f_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:52:07.413Z\", \"updated_at\": \"2026-05-25T09:52:34.845Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 289.3, \"eval_return_peak\": 486.5, \"eval_return_peak_step\": 75000, \"ve_ratio_max\": 0.5, \"civo_alert_max\": 0, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"total_env_steps\": 112000, \"total_updates\": 25099}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_073_008f_walker_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\", \"spec\": {\"command\": \"python train.py --config 008f --seed 4\", \"server\": \"westd-19154\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamer_v3_008f\", \"seed\": 4}, \"hypothesis\": \"Removing dt_embedding (dt_embed_dim=0) in the 008f control config prevents CIVO onset because the agent cannot form temporally-conditioned value predictions that compound imagination-driven overestimation. With fixed dt=2 and no temporal embedding, value error ratio should remain below the 1.5x CIVO threshold across seeds.\", \"completed_at\": \"2026-05-25T09:52:34.845Z\"}, \"exp_072_008e_v3_walker_s5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:51:50.268Z\", \"updated_at\": \"2026-05-25T09:52:00.215Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_trajectory\": {\"5K\": 29.4, \"15K\": 251.1, \"25K\": 423, \"35K\": 511, \"45K\": 600.1, \"55K\": 649, \"65K\": 697.2, \"75K\": 727.3, \"85K\": 710.3, \"95K\": 803.9, \"105K\": 853.1}, \"ve_ratio_trajectory\": {\"15K\": 0, \"25K\": 0.1, \"35K\": 0.2, \"45K\": 0.3, \"55K\": 0.3, \"65K\": 0.4, \"75K\": 0.5, \"85K\": 0.6, \"95K\": 0.6, \"105K\": 0.6}, \"value_mean_trajectory\": {\"5K\": 0, \"15K\": 4.6, \"25K\": 33.2, \"35K\": 88.8, \"45K\": 154, \"55K\": 223.2, \"65K\": 296.9, \"75K\": 364.3, \"85K\": 418.5, \"95K\": 464.6, \"105K\": 520.8}, \"nve_trajectory\": {\"15K\": 0.02, \"25K\": 0.08, \"35K\": 0.17, \"45K\": 0.26, \"55K\": 0.34, \"65K\": 0.43, \"75K\": 0.5, \"85K\": 0.59, \"95K\": 0.58, \"105K\": 0.61}, \"final_eval_return\": 853.1, \"peak_eval_return\": 853.1, \"peak_eval_step\": 105000, \"final_value_mean\": 520.8, \"final_ve_ratio\": 0.6, \"final_nve\": 0.61, \"final_actor_entropy\": -5.1, \"gate_dt_1_frac\": 1, \"civo_alert_max\": 0, \"civo_detected\": false, \"baseline_ratio\": 0.932}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_072_008e_v3_walker_s5/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_072_008e_v3_walker_s5.log\", \"server\": \"westd-19154\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 5 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\"}}, \"exp_069_008f_walker_repro_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:20:25.632Z\", \"updated_at\": \"2026-05-25T07:21:13.407Z\", \"hypothesis\": \"Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk. With no learned temporal embedding, the value network cannot develop the compounding overestimation pattern that causes CIVO collapse. This seed=1 run extends the evidence from exp_008f (seed=0).\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"spec\": {\"command\": \"python train.py --configs dmc_vision --task dmc_walker_walk --seed 1 --logdir logdir/exp_069_008f_walker_repro_s1\", \"server\": \"westd-19154\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 0, \"model_name\": \"dreamerv2_no_dt_embed_h8\", \"seed\": 1, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_walker_walk_online\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_069_008f_walker_repro_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T07:20:58.159Z\", \"metrics\": {\"eval_return_final\": 237.8, \"eval_return_final_step\": 105000, \"eval_return_peak\": 390.1, \"eval_return_peak_step\": 95000, \"steps_completed\": 112000, \"eval_steps\": 105000, \"civo_triggered\": false, \"civo_alert_count\": 0, \"ve_ratio_max\": 0.447, \"ve_ratio_max_step\": 105000, \"ve_ratio_final\": 0.447, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"value_mean_final\": 106.3, \"target_mean_final\": 106.4, \"value_loss_final\": 0.99, \"seed\": 1, \"eval_return_trajectory\": {\"5K\": 30.5, \"15K\": 158.7, \"25K\": 180.8, \"35K\": 250.3, \"45K\": 293.6, \"55K\": 272.2, \"65K\": 328.1, \"75K\": 244.8, \"85K\": 382.5, \"95K\": 390.1, \"105K\": 237.8}, \"ve_ratio_trajectory\": {\"15K\": 0.021, \"25K\": 0.111, \"35K\": 0.171, \"95K\": 0.275, \"105K\": 0.447}, \"note\": \"C2 causal control: no dt_embedding, fixed dt=2. No CIVO triggered. ve_ratio stayed <0.5 throughout. Late eval dip (390→238) is normal Walker variance, not CIVO-driven (value_mean≈target_mean, no overestimation).\"}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:16:11.755Z\", \"updated_at\": \"2026-05-23T23:34:24.080Z\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1.log\"}, \"hypothesis\": \"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，162.5K 时仍 1.94）。如果 s1 也触发持续 CIVO → PegInsertion 是最严重的 CIVO 环境（比 StackCube 自修复更难），支持 severity-dependent narrative；如果不触发 → seed-specific 异常。\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"checkpoint_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/latest.pt\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1.log\", \"metrics\": {\"total_steps\": 222400, \"ve_ratio_max\": 3.08, \"ve_ratio_max_step\": 92500, \"ve_ratio_final\": 0.5, \"ve_ratio_final_step\": 212500, \"eval_peak\": 24.05, \"eval_peak_step\": 112500, \"eval_final\": 11.44, \"eval_final_step\": 212500, \"civo_triggered\": true, \"civo_self_corrected\": \"partial\", \"civo_onset_step\": 32500, \"civo_peak_step\": 92500, \"ve_ratio_trajectory\": {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}, \"eval_trajectory\": {\"2500\": 2.01, \"12500\": 10.12, \"22500\": 11.47, \"32500\": 12.01, \"42500\": 10.13, \"52500\": 10.31, \"62500\": 9.02, \"72500\": 10.07, \"82500\": 8.78, \"92500\": 7.24, \"102500\": 9.2, \"112500\": 24.05, \"122500\": 16.46, \"132500\": 13.15, \"142500\": 20.44, \"152500\": 23.4, \"162500\": 9.07, \"172500\": 9.46, \"182500\": 8.51, \"192500\": 7.81, \"202500\": 8.58, \"212500\": 11.44}, \"note\": \"CIVO triggered (ve_ratio 3.08@92.5K), less severe than s0 (10.05). Partial self-correction to 0.50 by 212.5K. Eval poor throughout (~10-24), PegInsertion is hard task.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T23:34:24.080Z\"}, \"exp_054_pickcube_frozen_s0\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:16:08.927Z\", \"updated_at\": \"2026-05-23T05:16:21.605Z\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"data_path\": \"ManiSkill PickCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, PickCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PickCube-v1 (online eval)\"}, \"hypothesis\": \"Frozen dt_emb control for PickCube-v1 resolves circular classification problem. exp_019b showed NVE 3.78× but was classified as TN without frozen control to confirm. If frozen prevents value overestimation → confirms exp_019b was genuine CIVO (reclassify as TP); if frozen shows similar NVE → confirms TN classification (overestimation is task-intrinsic, not dt_emb-dependent).\", \"parent\": \"exp_019b_pickcube_civo_trigger\"}, \"exp_053_peginsertion_frozen_s0\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:44:48.898Z\", \"updated_at\": \"2026-05-23T03:44:56.702Z\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, PegInsertion)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\"}, \"hypothesis\": \"Frozen dt_emb prevents CIVO on PegInsertionSide-v1 (contact-rich manipulation), establishing dt_emb causality across all 3 ManiSkill tasks. exp_050 shows PegInsertion CIVO (ve_ratio 3.2@143K), exp_051 shows StackCube frozen prevents CIVO (ve_ratio 0.2). If PegInsertion frozen also prevents → complete manipulation-domain causal evidence; if not → contact-rich dynamics override frozen mitigation.\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\"}, \"exp_052_stackcube_civo_trigger_s1\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:26:49.825Z\", \"updated_at\": \"2026-05-22T21:26:59.557Z\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\"}, \"hypothesis\": \"StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 CIVO（ve_ratio 3.27）。如果 s1 也触发 → CIVO 在 manipulation 领域可复现，非 seed-specific；如果不触发 → seed-dependent，需更多 seeds。\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\"}, \"exp_048_cheetah_civo_extension\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:40.050Z\", \"updated_at\": \"2026-05-22T21:17:46.852Z\", \"hypothesis\": \"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → \\\"severity determines recoverability\\\" narrative, strongest paper defense. If it does → CIVO is universally transient regardless of severity.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}, \"metrics\": {\"eval_final\": 23.423, \"eval_peak\": 32.835, \"eval_peak_step\": 252000, \"ve_ratio_initial_measured\": 6.135, \"ve_ratio_initial_measured_step\": 122000, \"ve_ratio_inherited_from_exp010b\": 46.34, \"ve_ratio_peak_in_run\": 24.112, \"ve_ratio_peak_step\": 162000, \"ve_ratio_final\": 1.803, \"nve_inherited\": 70.64, \"nve_peak_in_run\": 36.76, \"nve_final\": 2.75, \"baseline_ve_ratio\": 0.656, \"total_steps\": 312000, \"last_eval_step\": 302000, \"civo_self_corrected\": \"partial\", \"civo_reduction_pct\": 96.1, \"civo_correction_duration_steps\": 197000, \"gate_collapsed\": true, \"gate_dt_final\": 2, \"gate_dt_2_frac_final\": 1}, \"checkpoint_path\": \"logdir/exp_048_cheetah_civo_extension/checkpoint_302000.pt\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:17:46.852Z\"}, \"exp_047_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:42:12.914Z\", \"updated_at\": \"2026-05-22T19:01:30.894Z\", \"hypothesis\": \"Freezing dt_emb in Walker Walk (seed 1) prevents sustained CIVO collapse, replicating exp_042 (seed 0, NVE=0.19) finding that removing dt conditioning blocks the overestimation feedback loop\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 282452, \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\"}, \"metrics\": {\"eval_peak\": 408.79, \"eval_peak_step\": 125000, \"eval_final\": 144.22, \"eval_final_step\": 215000, \"ve_ratio_peak\": 1.099, \"ve_ratio_peak_step\": 75000, \"ve_ratio_final\": 0.277, \"nve_peak\": 1.71, \"nve_peak_step\": 95000, \"nve_final_105k\": 0.56, \"total_steps\": 225000, \"note\": \"Transient NVE>1.5x at 75K-95K with full self-correction by 105K. Late eval decline (408->144) NOT CIVO-driven (ve_ratio=0.28). No sustained collapse.\"}, \"checkpoint_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:50:46.948Z\"}, \"exp_050_peginsertion_civo_trigger_s0\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:34:35.889Z\", \"updated_at\": \"2026-05-22T18:34:39.170Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill PegInsertionSide-v1 manipulation 任务上是否触发 CIVO。PegInsertion 是高精度接触任务，与 StackCube（多阶段）和 PickCube（单阶段）形成 manipulation 难度梯度。如果触发 CIVO → CIVO 在 manipulation 领域普遍存在；如果不触发 → CIVO 可能与任务的 reward 结构相关。\"}, \"exp_046_frozen_dt_emb_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:40:43.182Z\", \"updated_at\": \"2026-05-22T18:32:34.105Z\", \"hypothesis\": \"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation. Source: D133 + exp_042 result + R1-N4 cross-environment concern.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 281513, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_046_frozen_dt_emb_cheetah/train.log\"}, \"metrics\": {\"eval_final\": 150.5, \"eval_peak\": 207.4, \"eval_peak_step\": 145000, \"ve_ratio_peak\": 0.4, \"ve_ratio_final\": 0.1, \"nve_peak\": 1.35, \"nve_peak_step\": 45000, \"nve_final\": 0.17, \"total_steps\": 224000, \"civo_alert_count\": 0, \"eval_trajectory\": \"5K:8.3, 15K:110, 35K:160, 95K:181, 105K:206, 115K:46, 145K:207, 155K:161, 215K:150.5\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:31:00.933Z\"}, \"exp_048_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:44:55.613Z\", \"updated_at\": \"2026-05-22T17:14:16.564Z\", \"hypothesis\": \"ManiSkill Phase 1 scout: CIVO trigger config (trained dt_emb + subsample ON + H=8) on StackCube-v1 manipulation task. Tests whether CIVO generalizes beyond locomotion (Walker/Cheetah) to manipulation domains. exp_019b showed transient CIVO on PickCube; StackCube is harder (multi-stage). If CIVO triggers → extends cross-domain evidence; if not → supports locomotion-specific scope.\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 87609, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"/tmp/exp_048.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-22T17:14:16.564Z\"}, \"exp_045_treatment_extension_008d_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:40:52.894Z\", \"updated_at\": \"2026-05-22T15:44:50.990Z\", \"hypothesis\": \"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 70945, \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}, \"metrics\": {\"eval_final\": 867.6, \"eval_peak\": 869.7, \"eval_peak_step\": 242000, \"ve_ratio_final\": 0.05, \"ve_ratio_peak\": 4.91, \"ve_ratio_peak_step\": 132000, \"nve_final\": 0.052, \"total_steps\": 312000, \"self_correction_onset\": 142000, \"finding\": \"CIVO self-correction: ve_ratio 4.91→0.05, eval 35→868 over 170K steps\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\", \"completed_at\": \"2026-05-22T15:44:50.990Z\"}, \"exp_040_dual_critic_cheetah_s1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:40:43.166Z\", \"updated_at\": \"2026-05-22T09:40:43.166Z\", \"metrics\": {\"eval_final\": 41, \"eval_peak\": 256.4, \"eval_peak_step\": 25000, \"nve_peak\": 0.21, \"v1_final\": 8.84, \"v2_final\": 8.84}}, \"exp_036_dual_critic_pickcube\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T19:45:02.066Z\", \"updated_at\": \"2026-05-21T19:45:46.721Z\", \"spec\": {\"command\": \"python train.py --task ManiSkill_PickCube-v1 --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 0 --steps 200000\", \"server\": \"bjb1-45299\", \"data_path\": \"ManiSkill_PickCube-v1\", \"data_count\": 0, \"model_name\": \"dreamerv3_dual_critic\", \"seed\": 0}, \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"parent\": \"exp_032_dual_critic_walker\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_036_dual_critic_pickcube\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 212447, \"total_env_steps\": 212447, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"eval_return_peak_step\": 202500, \"ve_ratio_peak\": 2.3, \"ve_ratio_peak_step\": 32500, \"ve_ratio_final\": 0.2, \"civo_alerts\": 0, \"v1_v2_max_divergence\": 0, \"v1_v2_correlated\": true, \"CIVO_prevented\": \"vacuous_no_civo_in_baseline\", \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"exit_code\": 0, \"eval_return_trajectory\": {\"2.5K\": 2, \"12.5K\": 17.5, \"22.5K\": 17.5, \"32.5K\": 11.6, \"42.5K\": 15.6, \"52.5K\": 11.7, \"62.5K\": 18.8, \"72.5K\": 5.4, \"82.5K\": 22.5, \"92.5K\": 18.1, \"102.5K\": 8.4, \"112.5K\": 7.1, \"122.5K\": 9.1, \"132.5K\": 12.8, \"142.5K\": 14, \"152.5K\": 13.1, \"162.5K\": 16.2, \"172.5K\": 19.7, \"182.5K\": 16.8, \"192.5K\": 13.7, \"202.5K\": 27.7}, \"ve_ratio_trajectory\": {\"12.5K\": 0.2, \"22.5K\": 1, \"32.5K\": 2.3, \"42.5K\": 1.4, \"52.5K\": 1.4, \"62.5K\": 0.6, \"72.5K\": 1.6, \"82.5K\": 0.3, \"92.5K\": 0.3, \"102.5K\": 0.6, \"112.5K\": 0.7, \"122.5K\": 0.5, \"132.5K\": 0.4, \"142.5K\": 0.3, \"152.5K\": 0.4, \"162.5K\": 0.3, \"172.5K\": 0.3, \"182.5K\": 0.3, \"192.5K\": 0.4, \"202.5K\": 0.2}, \"value1_mean_trajectory\": {\"2.5K\": 0, \"12.5K\": 3.8, \"22.5K\": 17.9, \"32.5K\": 26.9, \"42.5K\": 21.2, \"52.5K\": 16.1, \"62.5K\": 11.6, \"72.5K\": 8.7, \"82.5K\": 7.2, \"92.5K\": 6, \"102.5K\": 5.3, \"112.5K\": 5.1, \"122.5K\": 5, \"132.5K\": 4.9, \"142.5K\": 4.9, \"152.5K\": 5.3, \"162.5K\": 5.7, \"172.5K\": 5.6, \"182.5K\": 5.6, \"192.5K\": 5.6, \"202.5K\": 5.8}, \"baseline_comparison\": {\"exp_019a_v2_vanilla_baseline_final\": 58.6, \"exp_019b_civo_config_baseline_final\": 26.6, \"exp_031_tcn_sigma02_final\": 17.2, \"exp_031b_tcn_sigma05_final\": 25.5}, \"conclusion_detail\": \"CIVO never manifested on PickCube (with or without dual-critic). ve_ratio peaked at 2.3 early (32.5K) and self-corrected — same pattern as TCN experiments (peak 3.7, 3.3). Eval 27.7 is indistinguishable from CIVO-config baseline (26.6). The subsample+dt_emb config itself degrades PickCube from 58.6 to ~27, and dual-critic does not recover this gap. Hypothesis rejected: PickCube is CIVO-immune at this training scale, making it a poor test for intervention generality.\"}, \"completed_at\": \"2026-05-21T19:45:46.721Z\"}, \"exp_039_narrow_dual_critic_walker_s1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T16:11:40.426Z\", \"updated_at\": \"2026-05-21T16:11:47.123Z\", \"hypothesis\": \"Narrow dual-critic Walker seed 1 verification: exp_035 s0 showed CIVO triggered (NVE 2.75) but full recovery (eval 697.8). If s1 also fully recovers → \\\"min operation enables recovery even with insufficient capacity\\\" conclusion is robust across seeds. Critical for 2×2 factorial interpretation.\", \"parent\": \"exp_035_narrow_dual_critic_walker\"}, \"exp_038_dual_critic_walker_s2\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:18:00.025Z\", \"updated_at\": \"2026-05-21T12:18:19.475Z\", \"hypothesis\": \"Dual-critic Walker seed 2 reproduction: exp_032 (s0, eval 787.7) and exp_032b (s1, eval 551.8) show high variance (CV=25%). Third seed provides IQM statistical power for CoRL reviewer scrutiny. If s2 also prevents CIVO (NVE < 1.5) → 3/3 seeds confirm dual-critic robustness on Walker.\", \"parent\": \"exp_032_dual_critic_walker\", \"spec\": {\"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0}}, \"exp_037_wide_critic_cheetah\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:16:44.078Z\", \"updated_at\": \"2026-05-21T12:18:05.444Z\", \"hypothesis\": \"Wide single critic on Cheetah: exp_034 dual-critic achieved only 31% eval recovery on Cheetah (partial CIVO suppression). exp_033 wide-critic on Walker showed self-repair (eval 408 > pre-CIVO peak). If Cheetah wide-critic recovery rate also > 31% → confirms \\\"capacity = recovery\\\" mechanism generalizes across environments, and wide-critic outperforms dual-critic on severe CIVO environments.\", \"parent\": \"exp_034_dual_critic_cheetah\", \"spec\": {\"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1}}, \"exp_034_dual_critic_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:09:08.035Z\", \"updated_at\": \"2026-05-21T12:09:56.881Z\", \"metrics\": {\"final_step\": 215000, \"total_env_steps\": 224000, \"eval_return_peak\": 315.7, \"eval_return_peak_step\": 45000, \"eval_return_final\": 97.5, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 0.1, \"civo_alerts\": 2, \"civo_alert_steps\": [95000, 105000], \"v1_v2_correlated\": true, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"exit_code\": 0, \"eval_return_trajectory\": {\"5K\": 8.3, \"15K\": 27.8, \"25K\": 108.7, \"35K\": 110, \"45K\": 315.7, \"55K\": 34.5, \"65K\": 81.5, \"75K\": 183, \"85K\": 88.4, \"95K\": 41, \"105K\": 27.2, \"115K\": 45.9, \"125K\": 58.7, \"135K\": 71.6, \"145K\": 61.9, \"155K\": 52.1, \"165K\": 153.8, \"175K\": 104.9, \"185K\": 101.4, \"195K\": 115.3, \"205K\": 101.5, \"215K\": 97.5}, \"ve_ratio_trajectory\": {\"15K\": 0.1, \"25K\": 0.1, \"35K\": 0.2, \"45K\": 0.1, \"55K\": 1.8, \"65K\": 0.7, \"75K\": 0.3, \"85K\": 0.5, \"95K\": 1, \"105K\": 1.6, \"115K\": 0.9, \"125K\": 0.6, \"135K\": 0.4, \"145K\": 0.4, \"155K\": 0.4, \"165K\": 0.1, \"175K\": 0.2, \"185K\": 0.2, \"195K\": 0.1, \"205K\": 0.1, \"215K\": 0.1}, \"value1_mean_trajectory\": {\"15K\": 1.8, \"25K\": 10.9, \"35K\": 23.7, \"45K\": 39, \"55K\": 60.5, \"65K\": 59.3, \"75K\": 52.6, \"85K\": 46.7, \"95K\": 41.7, \"105K\": 43.4, \"115K\": 39.3, \"125K\": 33.8, \"135K\": 28.5, \"145K\": 24.6, \"155K\": 21.5, \"165K\": 19.2, \"175K\": 17.8, \"185K\": 16.7, \"195K\": 15.7, \"205K\": 14.8, \"215K\": 14.2}, \"conclusion_detail\": \"CIVO triggered but partially mitigated. Two CIVO alerts (95K, 105K), peak ve_ratio=1.8 at 55K. Eval crashed from peak 315.7 to 27.2 (105K), recovered to 97.5. Dual-critic provided 40x reduction in overestimation vs baseline (ve_ratio 1.8 vs NVE 70.64) and prevented catastrophic collapse (eval 97.5 vs 0.83). But CIVO not fully suppressed — hypothesis of cross-environment generality not supported. v1≈v2 throughout (no critic disagreement).\"}, \"conclusion\": \"negative\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_034_dual_critic_cheetah --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --dual_critic True\", \"server\": \"bjb1-45299\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 0, \"model_name\": \"dreamerv3_dual_critic\", \"seed\": 0, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/checkpoint.pt\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_cheetah_run\"}, \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"parent\": \"exp_032_dual_critic_walker\", \"completed_at\": \"2026-05-21T12:09:56.881Z\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:43:05.327Z\", \"updated_at\": \"2026-05-21T03:38:07.906Z\", \"metrics\": {\"final_step\": 215000, \"total_env_steps\": 224000, \"eval_return_final\": 104.5, \"eval_return_peak\": 349.6, \"eval_return_peak_step\": 95000, \"eval_return_105K\": 71.8, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 3, \"ve_ratio_peak_step\": 105000, \"civo_blowup\": true, \"civo_blowup_step\": 105000, \"eval_return_trajectory\": {\"5K\": 31.7, \"15K\": 159.1, \"25K\": 155.7, \"35K\": 190.8, \"45K\": 137.1, \"55K\": 210.7, \"65K\": 189.5, \"75K\": 253.2, \"85K\": 259.5, \"95K\": 349.6, \"105K\": 71.8, \"115K\": 69.8, \"125K\": 61.5, \"135K\": 141.8, \"145K\": 98.7, \"155K\": 88.9, \"165K\": 86.2, \"175K\": 123.5, \"185K\": 153.7, \"195K\": 68.8, \"205K\": 63.7, \"215K\": 104.5}, \"ve_ratio_trajectory\": {\"15K\": 0, \"25K\": 0.2, \"35K\": 0.3, \"45K\": 0.7, \"55K\": 0.6, \"65K\": 0.9, \"75K\": 0.8, \"85K\": 0.9, \"95K\": 0.7, \"105K\": 3, \"115K\": 2.5, \"125K\": 2.4, \"135K\": 0.9, \"145K\": 1.1, \"155K\": 1.1, \"165K\": 0.9, \"175K\": 0.6, \"185K\": 0.4, \"195K\": 0.8, \"205K\": 0.7, \"215K\": 0.4}, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python train.py --config walker_walk_tcn --seed 3 --tcn_sigma 0.2\", \"server\": \"bjb1-40020\", \"data_path\": \"walker_walk\", \"data_count\": 0, \"model_name\": \"dreamer_tcn_sigma02\", \"seed\": 3}, \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"completed_at\": \"2026-05-21T03:38:07.906Z\"}, \"exp_029b_tcn_walker_s2_sigma02\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:43:04.635Z\", \"updated_at\": \"2026-05-20T19:43:04.636Z\", \"metrics\": {\"step\": 80000, \"eval_return_5K\": 30.5, \"eval_return_15K\": 168.4, \"eval_return_25K\": 159.6, \"eval_return_35K\": 168.1, \"eval_return_45K\": 171.5, \"eval_return_55K\": 177.7, \"eval_return_65K\": 106.6, \"eval_return_75K\": 64, \"ve_ratio_75K\": 1.65, \"ve_ratio_alert\": true, \"eval_peak\": 177.7, \"eval_peak_step\": 55000}}, \"exp_025_obs_sgs_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:40:59.914Z\", \"updated_at\": \"2026-05-20T02:41:29.954Z\", \"spec\": {\"command\": \"python dreamer.py --configs dmc_vision --task dmc_walker_walk --obs_decoder_sgs true --seed 1\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"data_count\": 0, \"model_name\": \"dreamerv3-obs-sgs\", \"seed\": 1}, \"hypothesis\": \"Obs-decoder stop-gradient on symlog (SGS) prevents CIVO in Walker by breaking the value→decoder→representation gradient pathway, keeping NVE below 1.5× baseline throughout training.\", \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/checkpoint.ckpt\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 215000, \"final_eval_return\": 726.41, \"peak_ve_ratio\": 0.8313, \"peak_ve_ratio_step\": 95000, \"peak_NVE_approx\": 1.28, \"ve_ratio_5K\": 0, \"ve_ratio_25K\": 0.1585, \"ve_ratio_45K\": 0.478, \"ve_ratio_65K\": 0.5932, \"ve_ratio_75K\": 0.5522, \"ve_ratio_85K\": 0.6419, \"ve_ratio_95K\": 0.8313, \"ve_ratio_105K\": 0.5093, \"ve_ratio_115K\": 0.4117, \"ve_ratio_125K\": 0.3476, \"ve_ratio_135K\": 0.2809, \"ve_ratio_145K\": 0.1883, \"ve_ratio_155K\": 0.1842, \"ve_ratio_165K\": 0.1099, \"ve_ratio_175K\": 0.0905, \"ve_ratio_185K\": 0.1088, \"ve_ratio_195K\": 0.2013, \"ve_ratio_205K\": 0.0725, \"ve_ratio_215K\": 0.0563, \"conclusion_detail\": \"CIVO prevented. Peak NVE ~1.28x at 95K (baseline ~0.648 interpolated), well below 1.5x threshold. ve_ratio monotonically declines from 95K onward to 0.056 at 215K. Obs-decoder SGS Walker seed 1 is 1/4 healthy prevention seed.\"}, \"completed_at\": \"2026-05-20T02:41:29.954Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:00:40.376Z\", \"updated_at\": \"2026-05-20T02:01:23.024Z\", \"hypothesis\": \"Blocking observation-decoder gradients via stop-gradient (SGS) on Walker will prevent early-onset CIVO by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/checkpoint.pt\", \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"spec\": {\"command\": \"python train.py --configs walker_obs_sgs --seed 4\", \"server\": \"bjb1-45299\", \"data_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"data_count\": 0, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 4}, \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 215000, \"final_eval_return\": 241.47, \"final_value_mean\": 34.3, \"final_ve_ratio\": 0.1421, \"peak_ve_ratio\": 6.0622, \"peak_ve_step\": 75000, \"ve_trajectory\": {\"5000\": 0, \"15000\": 0.0206, \"25000\": 0.1623, \"35000\": 0.7183, \"45000\": 0.67, \"55000\": 1.2924, \"65000\": 2.1521, \"75000\": 6.0622, \"85000\": 4.0813, \"95000\": 2.0202, \"105000\": 1.5704, \"115000\": 2.1303, \"125000\": 1.2078, \"135000\": 1.2884, \"145000\": 1.2645, \"155000\": 0.6109, \"165000\": 0.6521, \"175000\": 0.5908, \"185000\": 0.3178, \"195000\": 0.2701, \"205000\": 0.4087, \"215000\": 0.1421}, \"conclusion_detail\": \"Obs-decoder SGS failed to prevent early-onset CIVO on Walker seed 4. Severe CIVO collapse 55K-115K with peak ve_ratio=6.06 at 75K (eval crashed from 179 at 25K to 34 at 75K). Value overestimation gradually decayed through second half of training (1.26@145K → 0.14@215K) and eval eventually recovered to 241.5@215K. However, the SGS intervention did not prevent the CIVO onset — the recovery was driven by natural value decay over extended training, not by the SGS mechanism.\"}, \"completed_at\": \"2026-05-20T02:01:23.024Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:38:04.002Z\", \"updated_at\": \"2026-05-20T01:38:47.743Z\", \"hypothesis\": \"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\", \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/checkpoint.pt\", \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"spec\": {\"command\": \"python train.py --configs cheetah_obs_sgs --seed 1\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"data_count\": 0, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 1}, \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 105000, \"final_eval_return\": 38.26, \"final_value_mean\": 37.84, \"final_ve_ratio\": 0.9891, \"peak_ve_ratio\": 11.8091, \"peak_ve_step\": 75000, \"ve_trajectory\": {\"5000\": 0.0001, \"15000\": 0.0262, \"25000\": 0.0657, \"35000\": 0.1056, \"45000\": 0.979, \"55000\": 7.3924, \"65000\": 10.8375, \"75000\": 11.8091, \"85000\": 7.5096, \"95000\": 5.7255, \"105000\": 0.9891}, \"conclusion_detail\": \"Obs-decoder SGS failed on Cheetah seed 1: severe CIVO collapse 45K-95K, peak ve_ratio=11.81 at 75K. Eval_return crashed from 271.9 (35K) to 3.65 (75K). Late ve_ratio recovery to ~1.0 at 105K but eval_return (38.3) remained 86% below pre-collapse peak. Consistent with s0 result — SGS intervention is counterproductive on Cheetah, amplifying rather than suppressing CIVO.\"}, \"completed_at\": \"2026-05-20T01:38:47.743Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:32:40.958Z\", \"updated_at\": \"2026-05-20T01:33:21.724Z\", \"hypothesis\": \"Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse by decoupling representation learning from value overestimation pathways. If obs-decoder is a primary driver of CIVO, SGS should reduce ve_ratio below the 5-seed normalized threshold.\", \"spec\": {\"command\": \"python train.py --configs cheetah_obs_sgs --seed 0\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"data_count\": 0, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 0}, \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/checkpoint.pt\", \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 105000, \"final_eval_return\": 38.76, \"final_value_mean\": 51.16, \"final_ve_ratio\": 1.3199, \"peak_ve_ratio\": 8.5607, \"peak_ve_step\": 65000, \"ve_trajectory\": {\"5000\": 0.0001, \"15000\": 0.0244, \"25000\": 0.094, \"35000\": 0.177, \"45000\": 0.3098, \"55000\": 0.9939, \"65000\": 8.5607, \"75000\": 1.2188, \"85000\": 0.9696, \"95000\": 1.486, \"105000\": 1.3199}, \"conclusion_detail\": \"Obs-decoder SGS failed on Cheetah: full CIVO collapse at 65K (ve_ratio=8.56, NVE=21.85x 5-seed normalized). Partial recovery by 75K but performance remained degraded (eval_return=38.8 vs baseline ~160). Consistent with compensatory amplification — blocking obs decoder gradient worsened CIVO vs untreated baseline (010b NVE=8.27x). SGS intervention is counterproductive on Cheetah.\"}, \"completed_at\": \"2026-05-20T01:33:21.724Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:48:33.067Z\", \"updated_at\": \"2026-05-20T00:49:00.531Z\", \"hypothesis\": \"Observation-decoder SGS regularization will prevent CIVO collapse by grounding value estimates through auxiliary reconstruction loss, maintaining healthy NVE ratios throughout training.\", \"spec\": {\"command\": \"python3 train.py --config configs/exp_025_obs_sgs_walker_s3.yaml\", \"server\": \"bjb1-45299\", \"data_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"data_count\": 215000, \"model_name\": \"dreamer_obs_sgs\", \"seed\": 3}, \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"conclusion\": \"negative\", \"metrics\": {\"final_step\": 215000, \"eval_return_105k\": 818.58, \"ve_ratio_105k\": 0.5621, \"eval_return_135k\": 66.95, \"ve_ratio_135k\": 5.4659, \"eval_return_145k\": 43.75, \"ve_ratio_145k\": 6.8121, \"eval_return_175k\": 193.92, \"ve_ratio_175k\": 0.8274, \"eval_return_215k\": 590.17, \"ve_ratio_215k\": 0.1365, \"peak_ve_ratio\": 6.8121, \"peak_ve_step\": 145000, \"conclusion_detail\": \"Obs-decoder SGS delayed CIVO onset (healthy at 105K, NVE=0.56x) but failed to prevent late collapse (135K NVE=5.47x, peak 6.81x at 145K, partial recovery to 0.83x at 175K). Final eval_return recovered to 590 but value_mean collapsed to 80.6 (ve_ratio=0.14x). Late-onset CIVO variant.\"}, \"completed_at\": \"2026-05-20T00:49:00.531Z\"}, \"exp_001_baseline_s4_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:03:24.044Z\", \"updated_at\": \"2026-05-19T23:03:47.714Z\", \"spec\": {\"command\": \"python train.py (extended from 250k to 520k steps)\", \"server\": \"bjb1-45299\", \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/\", \"data_count\": 0, \"model_name\": \"dreamer_s4_baseline\", \"seed\": 4}, \"hypothesis\": \"Extending baseline S4 training from 250k to 520k steps will show whether eval_return plateaus or continues improving, establishing the convergence profile for NVE robustness analysis.\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/checkpoint.ckpt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/train_extended.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:03:46.304Z\", \"metrics\": {\"final_step\": 520000, \"final_eval_step\": 512000, \"final_eval_return\": 938.86, \"total_eval_checkpoints\": 52}}, \"exp_008e_v3_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:35:59.034Z\", \"updated_at\": \"2026-05-18T11:36:30.618Z\", \"metrics\": {\"eval_trajectory\": {\"5K\": 30.91, \"15K\": 343.66, \"25K\": 450.28, \"35K\": 527.44, \"45K\": 652.29, \"55K\": 717.96, \"65K\": 736.58, \"75K\": 751.73, \"85K\": 818.75, \"95K\": 835.34, \"105K\": 899.33}, \"value_trajectory\": {\"5K\": 0.002, \"15K\": 5.03, \"25K\": 46.89, \"35K\": 112.41, \"45K\": 186.9, \"55K\": 264.08, \"65K\": 343.83, \"75K\": 413.29, \"85K\": 467.89, \"95K\": 523.46, \"105K\": 547.4}, \"actor_entropy_trajectory\": {\"5K\": 8.19, \"15K\": 0.856, \"25K\": -2.478, \"35K\": -3.568, \"45K\": -4.167, \"55K\": -4.515, \"65K\": -4.7, \"75K\": -4.646, \"85K\": -5.029, \"95K\": -5.103, \"105K\": -5.084}, \"ve_ratio_trajectory\": {\"15K\": 0.0146, \"25K\": 0.1041, \"35K\": 0.2131, \"45K\": 0.2865, \"55K\": 0.3678, \"65K\": 0.4667, \"75K\": 0.5497, \"85K\": 0.5714, \"95K\": 0.6266, \"105K\": 0.6087}, \"nve_trajectory\": {\"15K\": 0.022, \"25K\": 0.16, \"35K\": 0.328, \"45K\": 0.441, \"55K\": 0.567, \"65K\": 0.719, \"75K\": 0.847, \"85K\": 0.88, \"95K\": 0.965, \"105K\": 0.938}, \"final_eval_return\": 899.33, \"peak_eval_return\": 899.33, \"peak_eval_step\": 105000, \"final_value_mean\": 547.4, \"final_ve_ratio\": 0.6087, \"final_nve\": 0.938, \"gate_dt_mean\": 1, \"gate_dt_1_frac\": 1, \"gate_dt_std\": 0, \"gate_empirical_entropy\": 0}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15 --checkpoint_every 25000\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3\", \"seed\": 4}, \"hypothesis\": \"C6 dual-pathway (trained dt_emb + subsample ON, gate_fixed_dt=1, gate_subsample_max_dt=2, H=15) will maintain stable training without value-overestimation collapse across multiple seeds on Walker Walk 105K, validating that the subsample pathway does not introduce systematic instability.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"completed_at\": \"2026-05-18T11:36:30.618Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:08:57.636Z\", \"updated_at\": \"2026-05-18T05:09:31.471Z\", \"hypothesis\": \"CIVO (value overestimation collapse) in Cheetah Run with dt_emb + subsample ON + H=8 is reproducible across seeds. Seed=0 should exhibit NVE>1.5× and eval return collapse similar to seed=1 (NVE=8.27×).\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"python train.py --config cheetah_civo_trigger --seed 0\", \"server\": \"bjb1-45299\", \"data_path\": \"dm_control/cheetah_run\", \"data_count\": 0, \"model_name\": \"dreamerv3_event_gated\", \"seed\": 0, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dm_control/cheetah_run\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T05:09:28.232Z\", \"metrics\": {\"final_step\": 112000, \"peak_eval_return\": 247.77, \"peak_eval_step\": 35000, \"final_eval_return\": 0.83, \"final_NVE\": 70.64, \"first_civo_alert_step\": 95000, \"first_civo_alert_NVE\": 6.34, \"value_mean_at_105k\": 58.58, \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"gate_dt_2_frac\": 1}}, \"exp_016d_sgs_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:29:07.960Z\", \"updated_at\": \"2026-05-16T01:43:55.477Z\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心（plan_016）。修复 eval video deadlock (D056) 后重试\", \"parent\": \"exp_008d_subsample_on_h8\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"server\": \"bjb1-45299\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"dreamerv3-sgs\", \"seed\": 1, \"checkpoint_source\": \"exp_008d_subsample_on_h8\", \"eval_data\": \"dmc_walker_walk\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:43:55.477Z\"}, \"exp_005_event_gated_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:53:45.066Z\", \"updated_at\": \"2026-05-13T21:54:17.129Z\", \"conclusion\": \"negative\", \"failure_reason\": \"结构性失败(D009): return最终47.4(baseline 5%), gate激活后return单调下降无恢复。85K/105K registry数据已修正为metrics.jsonl实际值(212.3/276.1, 旧值319.3/337.8系误录)。\", \"metrics\": {\"step\": 145000, \"final_eval_return\": 98.84, \"peak_eval_return\": 541.18, \"peak_eval_step\": 55000, \"eval_return_85K\": 212.34, \"eval_return_105K\": 276.08, \"eval_return_115K\": 25.67, \"eval_return_145K\": 98.84}, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --gate_enabled True\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3-event-gated-v4\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v5_s1\"}, \"completed_at\": \"2026-05-13T21:54:17.129Z\"}, \"exp_001_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:57:32.713Z\", \"updated_at\": \"2026-05-13T21:53:44.698Z\", \"conclusion\": \"success\", \"metrics\": {\"step\": 512000, \"final_eval_return\": 970.4, \"eval_return_last10_mean\": 950.9, \"eval_return_last10_std\": 10.5, \"fps\": 7.59}, \"spec\": {\"command\": \"python train.py --configs walker_walk --run.steps 512000\", \"server\": \"bjb1-45299\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"dreamerv3-baseline\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\"}, \"completed_at\": \"2026-05-13T20:58:00.944Z\"}}, \"count\": 46, \"total\": 46, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1668}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01HW8E85pGWpw9zJsDR71jGx`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results && python3 << 'PYEOF'\nimport json\n\nwith open(\"mcp-agent-ml-research-read_registry-1780014904997.txt\") as f:\n    raw = json.loads(f.read())\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\nprint(f\"Total experiments: {len(experiments)}\")\nprint()\n\n# Print all experiments with key info for mapping\nfor eid, exp in sorted(experiments.items()):\n    hyp = exp.get(\"hypothesis\", \"\")\n    conclusion = exp.get(\"conclusion\", \"\")\n    status = exp.get(\"status\", \"\")\n    metrics = exp.get(\"metrics\", {})\n    \n    # Find eval_return - check multiple possible keys\n    eval_val = None\n    for k in [\"eval_return_mean\", \"eval_return_final\", \"eval_final\", \"final_eval_return\", \"eval_return_105K\", \"eval_return_105k\"]:\n        if k in metrics:\n            eval_val = (k, metrics[k])\n            break\n    \n    print(f\"{eid}: status={status}, concl={conclusion}, eval={eval_val}\")\n    # Show hypothesis keywords for mapping\n    keywords = []\n    hyp_lower = hyp.lower()\n    for kw in [\"008d\", \"008f\", \"008a\", \"008e\", \"sgs\", \"reward\", \"full\", \"obs\", \"rave\", \"tcn\", \"wide\", \"narrow\", \"dual\", \"frozen\", \"removed\", \"dt_embed_dim=0\", \"no_dt_emb\"]:\n        if kw in hyp_lower:\n            keywords.append(kw)\n    if keywords:\n        print(f\"  keywords: {keywords}\")\n    print(f\"  hyp: {hyp[:100]}\")\n    print()\nPYEOF\n",
  "description": "Parse all experiments and extract mapping keywords"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "1db7be8f-34ff-4e66-a162-3c0e44e6ee76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSc2vkKJBoDVadfFAyUFz9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 58535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1241
      },
      "output_tokens": 62,
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

_source line 29 · 2026-05-29T00:35:14.592Z_

<details><summary>↩ Tool result · `toolu_01HW8E85pGWpw9zJsDR71jGx`</summary>

```text
Total experiments: 46

exp_001_baseline: status=DONE, concl=success, eval=('final_eval_return', 970.4)
  hyp: 

exp_001_baseline_s4_extended: status=DONE, concl=success, eval=('final_eval_return', 938.86)
  hyp: Extending baseline S4 training from 250k to 520k steps will show whether eval_return plateaus or con

exp_005_event_gated_v4: status=DONE, concl=negative, eval=('final_eval_return', 98.84)
  hyp: 

exp_008e_v3_s4: status=DONE, concl=success, eval=('final_eval_return', 899.33)
  keywords: ['dual']
  hyp: C6 dual-pathway (trained dt_emb + subsample ON, gate_fixed_dt=1, gate_subsample_max_dt=2, H=15) will

exp_010b_cheetah_civo_trigger_s0: status=DONE, concl=success, eval=('final_eval_return', 0.83)
  hyp: CIVO (value overestimation collapse) in Cheetah Run with dt_emb + subsample ON + H=8 is reproducible

exp_016d_sgs_walker_s1: status=DONE, concl=failed, eval=None
  keywords: ['sgs', 'reward']
  hyp: Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心（plan_

exp_025_obs_sgs_walker_s1: status=DONE, concl=success, eval=('final_eval_return', 726.41)
  keywords: ['sgs', 'obs']
  hyp: Obs-decoder stop-gradient on symlog (SGS) prevents CIVO in Walker by breaking the value→decoder→repr

exp_025_obs_sgs_walker_s3: status=DONE, concl=negative, eval=('eval_return_105k', 818.58)
  keywords: ['sgs', 'obs']
  hyp: Observation-decoder SGS regularization will prevent CIVO collapse by grounding value estimates throu

exp_025_obs_sgs_walker_s4: status=DONE, concl=negative, eval=('final_eval_return', 241.47)
  keywords: ['sgs', 'obs']
  hyp: Blocking observation-decoder gradients via stop-gradient (SGS) on Walker will prevent early-onset CI

exp_026_obs_sgs_cheetah_s0: status=DONE, concl=negative, eval=('final_eval_return', 38.76)
  keywords: ['sgs', 'obs']
  hyp: Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse

exp_026_obs_sgs_cheetah_s1: status=DONE, concl=negative, eval=('final_eval_return', 38.26)
  keywords: ['sgs', 'obs']
  hyp: Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse

exp_029b_tcn_walker_s2_sigma02: status=PREPARING, concl=, eval=None
  hyp: 

exp_029d_tcn_walker_s3_sigma02: status=DONE, concl=negative, eval=('eval_return_final', 104.5)
  keywords: ['tcn']
  hyp: Fourth TCN σ=0.2 seed to match 4 baseline seeds for statistical comparison. Current TCN seeds: s0=91

exp_034_dual_critic_cheetah: status=DONE, concl=negative, eval=('eval_return_final', 97.5)
  keywords: ['tcn', 'dual']
  hyp: Dual-critic on Cheetah Run: TCN failed at all σ on Cheetah. If dual-critic suppresses CIVO on Cheeta

exp_036_dual_critic_pickcube: status=DONE, concl=negative, eval=('eval_return_final', 27.7)
  keywords: ['tcn', 'dual']
  hyp: Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO o

exp_037_wide_critic_cheetah: status=ALLOCATED, concl=, eval=None
  keywords: ['wide', 'dual']
  hyp: Wide single critic on Cheetah: exp_034 dual-critic achieved only 31% eval recovery on Cheetah (parti

exp_038_dual_critic_walker_s2: status=ALLOCATED, concl=, eval=None
  keywords: ['dual']
  hyp: Dual-critic Walker seed 2 reproduction: exp_032 (s0, eval 787.7) and exp_032b (s1, eval 551.8) show 

exp_039_narrow_dual_critic_walker_s1: status=PREPARING, concl=, eval=None
  keywords: ['full', 'narrow', 'dual']
  hyp: Narrow dual-critic Walker seed 1 verification: exp_035 s0 showed CIVO triggered (NVE 2.75) but full 

exp_040_dual_critic_cheetah_s1: status=PREPARING, concl=, eval=('eval_final', 41)
  hyp: 

exp_045_treatment_extension_008d_s3: status=DONE, concl=success, eval=('eval_final', 867.6)
  hyp: CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K wil

exp_046_frozen_dt_emb_cheetah: status=DONE, concl=success, eval=('eval_final', 150.5)
  keywords: ['frozen']
  hyp: Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Chee

exp_047_frozen_dt_emb_walker_s1: status=DONE, concl=success, eval=('eval_final', 144.22)
  hyp: Freezing dt_emb in Walker Walk (seed 1) prevents sustained CIVO collapse, replicating exp_042 (seed 

exp_048_cheetah_civo_extension: status=DONE, concl=success, eval=('eval_final', 23.423)
  hyp: Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery

exp_048_stackcube_civo_trigger_s0: status=DONE, concl=killed, eval=None
  hyp: ManiSkill Phase 1 scout: CIVO trigger config (trained dt_emb + subsample ON + H=8) on StackCube-v1 m

exp_049_stackcube_civo_trigger_s0: status=DONE, concl=failed, eval=None
  hyp: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 C

exp_050_peginsertion_civo_trigger_s0: status=QUEUED, concl=, eval=None
  keywords: ['reward']
  hyp: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill PegInsertionSide-v1 manipulation 任务上

exp_051_stackcube_frozen_dt_emb_s0: status=DONE, concl=failed, eval=None
  keywords: ['frozen']
  hyp: Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trai

exp_052_stackcube_civo_trigger_s1: status=QUEUED, concl=, eval=None
  hyp: StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 

exp_053_peginsertion_frozen_s0: status=QUEUED, concl=, eval=None
  keywords: ['frozen']
  hyp: Frozen dt_emb prevents CIVO on PegInsertionSide-v1 (contact-rich manipulation), establishing dt_emb 

exp_054_pickcube_frozen_s0: status=QUEUED, concl=, eval=None
  keywords: ['frozen']
  hyp: Frozen dt_emb control for PickCube-v1 resolves circular classification problem. exp_019b showed NVE 

exp_055_peginsertion_civo_trigger_s1: status=DONE, concl=success, eval=('eval_final', 11.44)
  hyp: PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，162.5K 时仍 1.94）。如

exp_057_frozen_dt_emb_walker_s2: status=DONE, concl=failed, eval=None
  keywords: ['frozen']
  hyp: Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量

exp_069_008f_walker_repro_s1: status=DONE, concl=success, eval=('eval_return_final', 237.8)
  keywords: ['008f', 'dt_embed_dim=0']
  hyp: Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk. With no learned temp

exp_072_008e_v3_walker_s5: status=PREPARING, concl=success, eval=('final_eval_return', 853.1)
  hyp: 

exp_073_008f_walker_s4: status=DONE, concl=success, eval=('eval_return_final', 289.3)
  keywords: ['008f', 'dt_embed_dim=0']
  hyp: Removing dt_embedding (dt_embed_dim=0) in the 008f control config prevents CIVO onset because the ag

exp_077_cheetah_baseline_s0: status=ALLOCATED, concl=, eval=None
  hyp: 

exp_078_cheetah_008d_s0: status=ALLOCATED, concl=, eval=None
  hyp: 

exp_079_frozen_dt_emb_walker_s0: status=ALLOCATED, concl=, eval=None
  hyp: 

exp_081_008e_v3_walker_s2: status=DONE, concl=success, eval=('eval_return_105K', 597.1)
  hyp: Trained dt_emb with dt=1 imagination and subsample ON (max_dt=2) does not trigger CIVO in Walker Wal

exp_097_cheetah_008d_s3: status=DONE, concl=success, eval=('eval_final', 61.7)
  hyp: C1 trigger seed 3: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 Cheetah 上的第四个 seed（s3）。当前 o

exp_100_walker_008a_s1: status=DONE, concl=success, eval=('eval_final', 750.59)
  keywords: ['008a']
  hyp: Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 

exp_hopper_baseline: status=DONE, concl=success, eval=('eval_final', 96.43)
  hyp: Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO ver

exp_hopper_frozen_s0_ext: status=DONE, concl=negative, eval=('eval_return_final', 0.56)
  keywords: ['frozen']
  hyp: Extending frozen_s0 from 105K to 150K will show eval_return recovery with ve_ratio declining, confir

exp_walker_no_dt_emb_s0: status=DONE, concl=killed, eval=None
  hyp: 

exp_walker_no_dt_emb_s1: status=RUNNING, concl=, eval=None
  keywords: ['008f', 'dt_embed_dim=0', 'no_dt_emb']
  hyp: Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk seed=1. With no learn

rssm_fidelity_v2: status=DONE, concl=success, eval=None
  keywords: ['reward', 'obs', 'frozen', 'no_dt_emb']
  hyp: RSSM fidelity v2 分析：对比 4 类模型（baseline/trained_dt_emb/no_dt_emb/frozen）在 dt=1 vs dt=2 下的 observation/
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "bf25fe1d-0b97-451e-9735-f3df8e72f8bd",
  "tool_use_result": {
    "stdout": "Total experiments: 46\n\nexp_001_baseline: status=DONE, concl=success, eval=('final_eval_return', 970.4)\n  hyp: \n\nexp_001_baseline_s4_extended: status=DONE, concl=success, eval=('final_eval_return', 938.86)\n  hyp: Extending baseline S4 training from 250k to 520k steps will show whether eval_return plateaus or con\n\nexp_005_event_gated_v4: status=DONE, concl=negative, eval=('final_eval_return', 98.84)\n  hyp: \n\nexp_008e_v3_s4: status=DONE, concl=success, eval=('final_eval_return', 899.33)\n  keywords: ['dual']\n  hyp: C6 dual-pathway (trained dt_emb + subsample ON, gate_fixed_dt=1, gate_subsample_max_dt=2, H=15) will\n\nexp_010b_cheetah_civo_trigger_s0: status=DONE, concl=success, eval=('final_eval_return', 0.83)\n  hyp: CIVO (value overestimation collapse) in Cheetah Run with dt_emb + subsample ON + H=8 is reproducible\n\nexp_016d_sgs_walker_s1: status=DONE, concl=failed, eval=None\n  keywords: ['sgs', 'reward']\n  hyp: Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心（plan_\n\nexp_025_obs_sgs_walker_s1: status=DONE, concl=success, eval=('final_eval_return', 726.41)\n  keywords: ['sgs', 'obs']\n  hyp: Obs-decoder stop-gradient on symlog (SGS) prevents CIVO in Walker by breaking the value→decoder→repr\n\nexp_025_obs_sgs_walker_s3: status=DONE, concl=negative, eval=('eval_return_105k', 818.58)\n  keywords: ['sgs', 'obs']\n  hyp: Observation-decoder SGS regularization will prevent CIVO collapse by grounding value estimates throu\n\nexp_025_obs_sgs_walker_s4: status=DONE, concl=negative, eval=('final_eval_return', 241.47)\n  keywords: ['sgs', 'obs']\n  hyp: Blocking observation-decoder gradients via stop-gradient (SGS) on Walker will prevent early-onset CI\n\nexp_026_obs_sgs_cheetah_s0: status=DONE, concl=negative, eval=('final_eval_return', 38.76)\n  keywords: ['sgs', 'obs']\n  hyp: Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse\n\nexp_026_obs_sgs_cheetah_s1: status=DONE, concl=negative, eval=('final_eval_return', 38.26)\n  keywords: ['sgs', 'obs']\n  hyp: Blocking observation-decoder gradients via stop-gradient (SGS) on Cheetah will prevent CIVO collapse\n\nexp_029b_tcn_walker_s2_sigma02: status=PREPARING, concl=, eval=None\n  hyp: \n\nexp_029d_tcn_walker_s3_sigma02: status=DONE, concl=negative, eval=('eval_return_final', 104.5)\n  keywords: ['tcn']\n  hyp: Fourth TCN σ=0.2 seed to match 4 baseline seeds for statistical comparison. Current TCN seeds: s0=91\n\nexp_034_dual_critic_cheetah: status=DONE, concl=negative, eval=('eval_return_final', 97.5)\n  keywords: ['tcn', 'dual']\n  hyp: Dual-critic on Cheetah Run: TCN failed at all σ on Cheetah. If dual-critic suppresses CIVO on Cheeta\n\nexp_036_dual_critic_pickcube: status=DONE, concl=negative, eval=('eval_return_final', 27.7)\n  keywords: ['tcn', 'dual']\n  hyp: Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO o\n\nexp_037_wide_critic_cheetah: status=ALLOCATED, concl=, eval=None\n  keywords: ['wide', 'dual']\n  hyp: Wide single critic on Cheetah: exp_034 dual-critic achieved only 31% eval recovery on Cheetah (parti\n\nexp_038_dual_critic_walker_s2: status=ALLOCATED, concl=, eval=None\n  keywords: ['dual']\n  hyp: Dual-critic Walker seed 2 reproduction: exp_032 (s0, eval 787.7) and exp_032b (s1, eval 551.8) show \n\nexp_039_narrow_dual_critic_walker_s1: status=PREPARING, concl=, eval=None\n  keywords: ['full', 'narrow', 'dual']\n  hyp: Narrow dual-critic Walker seed 1 verification: exp_035 s0 showed CIVO triggered (NVE 2.75) but full \n\nexp_040_dual_critic_cheetah_s1: status=PREPARING, concl=, eval=('eval_final', 41)\n  hyp: \n\nexp_045_treatment_extension_008d_s3: status=DONE, concl=success, eval=('eval_final', 867.6)\n  hyp: CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K wil\n\nexp_046_frozen_dt_emb_cheetah: status=DONE, concl=success, eval=('eval_final', 150.5)\n  keywords: ['frozen']\n  hyp: Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Chee\n\nexp_047_frozen_dt_emb_walker_s1: status=DONE, concl=success, eval=('eval_final', 144.22)\n  hyp: Freezing dt_emb in Walker Walk (seed 1) prevents sustained CIVO collapse, replicating exp_042 (seed \n\nexp_048_cheetah_civo_extension: status=DONE, concl=success, eval=('eval_final', 23.423)\n  hyp: Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery\n\nexp_048_stackcube_civo_trigger_s0: status=DONE, concl=killed, eval=None\n  hyp: ManiSkill Phase 1 scout: CIVO trigger config (trained dt_emb + subsample ON + H=8) on StackCube-v1 m\n\nexp_049_stackcube_civo_trigger_s0: status=DONE, concl=failed, eval=None\n  hyp: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 C\n\nexp_050_peginsertion_civo_trigger_s0: status=QUEUED, concl=, eval=None\n  keywords: ['reward']\n  hyp: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill PegInsertionSide-v1 manipulation 任务上\n\nexp_051_stackcube_frozen_dt_emb_s0: status=DONE, concl=failed, eval=None\n  keywords: ['frozen']\n  hyp: Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trai\n\nexp_052_stackcube_civo_trigger_s1: status=QUEUED, concl=, eval=None\n  hyp: StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 \n\nexp_053_peginsertion_frozen_s0: status=QUEUED, concl=, eval=None\n  keywords: ['frozen']\n  hyp: Frozen dt_emb prevents CIVO on PegInsertionSide-v1 (contact-rich manipulation), establishing dt_emb \n\nexp_054_pickcube_frozen_s0: status=QUEUED, concl=, eval=None\n  keywords: ['frozen']\n  hyp: Frozen dt_emb control for PickCube-v1 resolves circular classification problem. exp_019b showed NVE \n\nexp_055_peginsertion_civo_trigger_s1: status=DONE, concl=success, eval=('eval_final', 11.44)\n  hyp: PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，162.5K 时仍 1.94）。如\n\nexp_057_frozen_dt_emb_walker_s2: status=DONE, concl=failed, eval=None\n  keywords: ['frozen']\n  hyp: Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量\n\nexp_069_008f_walker_repro_s1: status=DONE, concl=success, eval=('eval_return_final', 237.8)\n  keywords: ['008f', 'dt_embed_dim=0']\n  hyp: Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk. With no learned temp\n\nexp_072_008e_v3_walker_s5: status=PREPARING, concl=success, eval=('final_eval_return', 853.1)\n  hyp: \n\nexp_073_008f_walker_s4: status=DONE, concl=success, eval=('eval_return_final', 289.3)\n  keywords: ['008f', 'dt_embed_dim=0']\n  hyp: Removing dt_embedding (dt_embed_dim=0) in the 008f control config prevents CIVO onset because the ag\n\nexp_077_cheetah_baseline_s0: status=ALLOCATED, concl=, eval=None\n  hyp: \n\nexp_078_cheetah_008d_s0: status=ALLOCATED, concl=, eval=None\n  hyp: \n\nexp_079_frozen_dt_emb_walker_s0: status=ALLOCATED, concl=, eval=None\n  hyp: \n\nexp_081_008e_v3_walker_s2: status=DONE, concl=success, eval=('eval_return_105K', 597.1)\n  hyp: Trained dt_emb with dt=1 imagination and subsample ON (max_dt=2) does not trigger CIVO in Walker Wal\n\nexp_097_cheetah_008d_s3: status=DONE, concl=success, eval=('eval_final', 61.7)\n  hyp: C1 trigger seed 3: CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 Cheetah 上的第四个 seed（s3）。当前 o\n\nexp_100_walker_008a_s1: status=DONE, concl=success, eval=('eval_final', 750.59)\n  keywords: ['008a']\n  hyp: Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 \n\nexp_hopper_baseline: status=DONE, concl=success, eval=('eval_final', 96.43)\n  hyp: Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO ver\n\nexp_hopper_frozen_s0_ext: status=DONE, concl=negative, eval=('eval_return_final', 0.56)\n  keywords: ['frozen']\n  hyp: Extending frozen_s0 from 105K to 150K will show eval_return recovery with ve_ratio declining, confir\n\nexp_walker_no_dt_emb_s0: status=DONE, concl=killed, eval=None\n  hyp: \n\nexp_walker_no_dt_emb_s1: status=RUNNING, concl=, eval=None\n  keywords: ['008f', 'dt_embed_dim=0', 'no_dt_emb']\n  hyp: Removing dt_embedding (dt_embed_dim=0) prevents CIVO triggering in Walker Walk seed=1. With no learn\n\nrssm_fidelity_v2: status=DONE, concl=success, eval=None\n  keywords: ['reward', 'obs', 'frozen', 'no_dt_emb']\n  hyp: RSSM fidelity v2 分析：对比 4 类模型（baseline/trained_dt_emb/no_dt_emb/frozen）在 dt=1 vs dt=2 下的 observation/",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
The registry has 46 experiments but many are not DONE or are failed/killed. I'm missing many experiments that are referenced in Table 2. The table shows experiments like:
- Reward-only SGS (2 seeds)
- Full-pathway SGS (3 seeds)
- RAVE (2 seeds)
- TCN σ=0.1 (1 seed)
- TCN σ=0.2 (6 seeds) - I only see 1 done TCN seed
- TCN σ=0.5 (3 seeds)


- TCN σ=1.0 (1 seed)
- Wide single (2 seeds)
- Narrow dual (min) (2 seeds)
- Wide dual (min) (4 seeds)
- Embedding frozen (7 seeds)
- Embedding removed (6 seeds)

Many of these experiments must be in older registries or using different naming conventions, or they were run before the registry was set up. I should check if there's a paper data file or supplementary materials with the already-computed statistics for these experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "29f7c6d4-0682-4ef7-b492-3237ac73e4ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bmX88evSE3h2DoiqHHwGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 59776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 31_

Registry 缺少很多实验（TCN、RAVE、wide/narrow 等）。这些可能在其他数据源。搜索项目中已有的分析数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "5b45d934-bf4a-4337-ae73-ff400917c5af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bmX88evSE3h2DoiqHHwGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 59776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 32_

<details open><summary>🔧 Tool call — Agent · `toolu_01UXNsjtiVw79JPYjKmkkQ7L`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment data files",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon, search for files that contain compiled experiment results, analysis data, or metrics summaries. I'm looking for data about these intervention experiments: TCN (sigma 0.1/0.2/0.5/1.0), RAVE, reward-only SGS, full-pathway SGS, obs-decoder SGS, wide/narrow/dual critic, frozen embedding, removed embedding, and the untreated (008d) baseline seeds.\n\nCheck:\n1. `artifacts/` directory for any CSV, JSON, or analysis files\n2. `docs/paper/` for any data tables or appendix files\n3. Any analysis scripts or notebooks\n4. Any `memory.md`, `ideas.md`, or report files in the project\n5. Log directories or summary files\n\nSearch \"very thorough\" breadth. I need the eval_return values for all these experiments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "7270708d-784e-4b23-8b43-c734141f6ed3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bmX88evSE3h2DoiqHHwGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 59776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Find experiment data files",
  "task_type": "local_agent",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon, search for files that contain compiled experiment results, analysis data, or metrics summaries. I'm looking for data about these intervention experiments: TCN (sigma 0.1/0.2/0.5/1.0), RAVE, reward-only SGS, full-pathway SGS, obs-decoder SGS, wide/narrow/dual critic, frozen embedding, removed embedding, and the untreated (008d) baseline seeds.\n\nCheck:\n1. `artifacts/` directory for any CSV, JSON, or analysis files\n2. `docs/paper/` for any data tables or appendix files\n3. Any analysis scripts or notebooks\n4. Any `memory.md`, `ideas.md`, or report files in the project\n5. Log directories or summary files\n\nSearch \"very thorough\" breadth. I need the eval_return values for all these experiments.",
  "uuid": "a6edecaa-5b8e-4d02-b7a5-cd7070230ad9",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


## Round 1

## Round 1

214 recorded events


### User

_source line 34 · 2026-05-29T00:35:29.250Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon, search for files that contain compiled experiment results, analysis data, or metrics summaries. I'm looking for data about these intervention experiments: TCN (sigma 0.1/0.2/0.5/1.0), RAVE, reward-only SGS, full-pathway SGS, obs-decoder SGS, wide/narrow/dual critic, frozen embedding, removed embedding, and the untreated (008d) baseline seeds.

Check:
1. `artifacts/` directory for any CSV, JSON, or analysis files
2. `docs/paper/` for any data tables or appendix files
3. Any analysis scripts or notebooks
4. Any `memory.md`, `ideas.md`, or report files in the project
5. Log directories or summary files

Search "very thorough" breadth. I need the eval_return values for all these experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "e2b98c1f-1495-44b9-898e-dca9f314c7b9"
}
```

</details>

---


### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 19410,
    "tool_uses": 1,
    "duration_ms": 2092
  },
  "last_tool_name": "Bash",
  "uuid": "b5b5ef88-b3c6-4a81-8250-b48e57ea5100",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01GTTtKMTTyGg1Xiz4UT1Rd2`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -type f -name \"*.csv\" -o -name \"*.json\" -o -name \"*.pkl\" -o -name \"*.npz\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d4bbf999-d065-479f-a839-6070186a2b6f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RELajnYiv66BAcoKuxpDx9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19401,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19401,
        "ephemeral_1h_input_tokens": 0
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

_source line 37 · 2026-05-29T00:35:31.413Z_

<details><summary>↩ Tool result · `toolu_01GTTtKMTTyGg1Xiz4UT1Rd2`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_becker_ehmck_citation_20260524T080610_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_figure_fig2_three_fixes_20260515T111131_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_nve_sensitivity_20260515T125303_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_deploy_exp_040_041_verified_20260522T025925_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_exp_087_frozen_dt_emb_cheetah_s1_20260525T184359_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_check_step-50k_20260513T042653_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_status_all-4-exp-progress_20260522T054357_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_check_gpu-health-bjb1-45299_20260525T084700_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_exp_hopper_trained_s0_ext_20260527T080108_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_actor-entropy-timeseries_20260526T115350_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_kill_exp005_fix_registry_20260513T215230_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_check_both_experiments_progress_20260513T183531_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_pivot-gate-mechanisms_20260513T214027_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_related-work-expansion_20260516T194613_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_fix-step-sync_20260513T065713_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_cleanup_008e_logdir_20260514T042132_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_verify_template_switch_status_20260524T102143_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_fix-dt-bugs-and-submit-exp004_20260513T100837_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_gpu-progress-check_20260515T093919_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_cheetah_tcn_and_ablation_configs_20260520T082823_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_fix_bootstrap-ci-sgs-full_20260516T184606_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_010b-nve-calculation_20260517T203521_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_verify_sgs_flag_and_015b_progress_20260515T143126_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_bootstrap-ci_20260516T154234_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related_work_section_20260513T175837_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_cleanup_kill_stackcube_remnant_20260522T163124_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_claim-strength-audit_20260516T075150_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_civo-detector-impl_20260517T074410_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_results-draft_20260516T051130_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_exp_083_cheetah_baseline_s1_20260525T162954_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "3aec5693-026c-4468-9663-57dc398e2f26"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 22182,
    "tool_uses": 2,
    "duration_ms": 4754
  },
  "last_tool_name": "Bash",
  "uuid": "a535b320-54f6-4bb5-bd39-553e1adb206d",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01XBdbT3scGGdR451tSSsM6g`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/ 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a850625c-d75a-4e68-9968-3f0151370ccc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YE1wDgd53eYd6946JDLWDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2768,
      "cache_read_input_tokens": 19401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2768,
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

_source line 40 · 2026-05-29T00:35:34.074Z_

<details><summary>↩ Tool result · `toolu_01XBdbT3scGGdR451tSSsM6g`</summary>

```text
total 2788
drwxr-xr-x 96 ubuntu ubuntu  12288 May 28 14:04 .
drwxr-xr-x 10 ubuntu ubuntu   4096 May 29 00:32 ..
-rw-r--r--  1 ubuntu ubuntu   2533 May 14 04:11 008e_dryrun_check.md
-rw-r--r--  1 ubuntu ubuntu  19572 May 14 19:05 009b_literature_search.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 22:21 016e
drwxr-xr-x  5 ubuntu ubuntu   4096 May 16 11:10 018
-rw-r--r--  1 ubuntu ubuntu   7286 May 16 11:10 018_prewrite_two_versions.md
-rw-r--r--  1 ubuntu ubuntu   1153 May 16 15:23 018v2_server_check.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 19:30 019a
-rw-r--r--  1 ubuntu ubuntu   3331 May 16 05:21 019a_dryrun_report.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 19:30 019b
drwxr-xr-x  7 ubuntu ubuntu   4096 May 14 09:51 _project
-rw-r--r--  1 ubuntu ubuntu   7129 May 24 18:17 actor_entropy_analysis.md
-rw-r--r--  1 ubuntu ubuntu  26934 May 26 12:26 actor_entropy_comparison.pdf
-rw-r--r--  1 ubuntu ubuntu 123893 May 26 12:26 actor_entropy_comparison.png
-rw-r--r--  1 ubuntu ubuntu    998 May 15 10:51 actor_loss_timeseries.json
drwxr-xr-x  2 ubuntu ubuntu   4096 May 17 22:54 analysis
-rw-r--r--  1 ubuntu ubuntu   8486 May 15 14:51 analysis_actor_entropy_plan031.md
-rw-r--r--  1 ubuntu ubuntu   4529 May 17 10:52 analysis_civo_detector_pickcube_backtest.md
-rw-r--r--  1 ubuntu ubuntu  13728 May 26 03:31 analysis_rssm_fidelity_v2.json
-rw-r--r--  1 ubuntu ubuntu   3575 May 14 11:00 analysis_rssm_prediction_quality.json
-rw-r--r--  1 ubuntu ubuntu   2620 May 26 05:46 analysis_rssm_standardized_cheetah.json
-rw-r--r--  1 ubuntu ubuntu   5388 May 26 05:46 analysis_rssm_standardized_walker.json
-rw-r--r--  1 ubuntu ubuntu   5738 May 22 04:49 auroc_label_fix_recompute.py
-rw-r--r--  1 ubuntu ubuntu   4470 May 22 04:50 auroc_label_fix_report.md
-rw-r--r--  1 ubuntu ubuntu   1120 May 22 04:49 auroc_label_fix_result.json
-rw-r--r--  1 ubuntu ubuntu   6157 May 14 03:42 bernoulli_st_pessimism_designs.md
-rw-r--r--  1 ubuntu ubuntu   1481 May 17 03:57 bootstrap_ci_n3.json
-rw-r--r--  1 ubuntu ubuntu   3248 May 16 20:37 bootstrap_ci_results.json
drwxr-xr-x  2 ubuntu ubuntu   4096 May 16 20:38 bootstrap_cis
-rw-r--r--  1 ubuntu ubuntu   3999 May 16 20:38 bootstrap_cis.json
-rw-r--r--  1 ubuntu ubuntu   2617 May 24 13:37 camera_ready_checklist.md
-rw-r--r--  1 ubuntu ubuntu   1842 May 21 16:14 check_037_038_status.md
-rw-r--r--  1 ubuntu ubuntu   3803 May 14 03:18 checkpoint_monitor.py
-rw-r--r--  1 ubuntu ubuntu  47869 May 17 02:28 civo_detector_retrospective.json
-rw-r--r--  1 ubuntu ubuntu   8048 May 16 07:54 claim_strength_audit.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 20 09:06 code
-rw-r--r--  1 ubuntu ubuntu   9694 May 28 01:13 code_correction_history.md
-rw-r--r--  1 ubuntu ubuntu  15418 May 13 01:11 code_survey_dreamerv3.md
-rw-r--r--  1 ubuntu ubuntu   6650 May 20 09:10 contingency_framing_B_C.md
-rw-r--r--  1 ubuntu ubuntu  13797 May 16 01:49 d061_literature_linkage.md
-rw-r--r--  1 ubuntu ubuntu   8190 May 25 16:12 d152_code_evolution_report.md
drwxr-xr-x  2 ubuntu ubuntu   4096 May 17 10:47 data
drwxr-xr-x  2 ubuntu ubuntu   4096 May 17 07:49 drafts
drwxr-xr-x 10 ubuntu ubuntu   4096 May 20 21:59 dream_reports
-rw-r--r--  1 ubuntu ubuntu 233173 May 26 11:57 dt_embedding_cosine_similarity.png
-rw-r--r--  1 ubuntu ubuntu  10916 May 13 03:32 eval_mvp.py
drwxr-xr-x  3 ubuntu ubuntu   4096 May 13 02:05 exp_001_baseline
-rw-r--r--  1 ubuntu ubuntu   3138 May 19 18:23 exp_001_baseline_s1_ve_profile_full.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "31a2506e-bf35-4013-840b-b0ef1e8d8e14"
}
```

</details>

---


### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 23966,
    "tool_uses": 3,
    "duration_ms": 7649
  },
  "last_tool_name": "Bash",
  "uuid": "4e7b612b-e548-4a19-b44d-908a5719af14",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01GL15hG1gJducBYY4CfJW6w`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -type f \\( -name \"*results*\" -o -name \"*metrics*\" -o -name \"*eval*\" -o -name \"*return*\" \\) 2>/dev/null | grep -E \"\\.(csv|json|txt|md)$\" | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ea5ab2e0-b0d8-456f-8ff6-b987902457a9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J1UjmAdEdqfDsKrZL58uY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1778,
      "cache_read_input_tokens": 22169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1778,
        "ephemeral_1h_input_tokens": 0
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

_source line 43 · 2026-05-29T00:35:36.993Z_

<details><summary>↩ Tool result · `toolu_01GL15hG1gJducBYY4CfJW6w`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_results-draft_20260516T051130_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_check_exp_050_172k_metrics_20260523T053608_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_results-seed3-integrate_20260517T061803_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_results_tex_f6_fix_20260525T161849_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_exp_006_full_metrics_20260514T004608_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_results_tex_fix_cheetah_20260525T155535_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_monitor_008e_v3_s1_metrics_20260514T220108_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_maniskill3-eval-scripts_20260516T032426_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_results-tex-streamline_20260517T104711_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_results-causal-matrix_20260516T075402_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_integrate-plan031-032-results_20260514T142844_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_008e_v3_fresh_metrics_20260514T071355_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_mvp_eval_script_20260513T193419_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_cross-env-results-draft_20260516T170904_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_negative-results-insight_20260524T183247_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_metrics-aggregation_20260515T043938_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_metrics-aggregation_20260515T041903_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_008f_fresh_metrics_20260514T071350_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_008f_35k_eval_capture_20260514T062318_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_check_exp_005_100K_eval_20260513T203143_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_auto_eval_checkpoint_monitor_20260514T031718_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_diagnose_008e_and_metrics_20260514T041721_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_rssm_v3_results_pickup_20260526T055256_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_monitor_016e_009d_metrics_20260515T221733_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_infra_bjb1-metrics-rescue_20260526T034545_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_008f_35k_metrics_20260514T062046_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_fix_appendix-eval-data_20260524T021344_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_exp_006_metrics_20260513T233959_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_exp_029b_metrics_rescue_20260520T225918_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_seed3-results-patch_20260517T045911_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_walker-results-aggregation_20260514T185728_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_diag_009g_eval_check_20260515T190127_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_exp_016e_sgs_metrics_20260515T221814_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_appendix_008e_s5_eval_fix_20260525T165455_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_analysis_exp_088_metrics_nve_update_20260525T210814_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_monitor_exp_005_exp_001_metrics_check_20260513T183904_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_008e_v3_metrics_20260514T062054_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_check_all_running_metrics_20260514T040636_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_s4-launch-and-eval-check_20260519T172737_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_results-integration_20260516T195701_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "36b0ab51-d27d-4987-b5b7-cec2ad6cbc6e"
}
```

</details>

---


### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 26475,
    "tool_uses": 4,
    "duration_ms": 9961
  },
  "last_tool_name": "Bash",
  "uuid": "fb4bf666-d7cf-4724-b4cf-2af0242dac20",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01UVJvzsm34D5Xvzn1L19aAC`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/*.md 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "59a1fe41-c10e-4dbb-a9e8-eeaa0f4ebf94",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XGvng7ZvjrqgiqWS9ZaMge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2507,
      "cache_read_input_tokens": 23947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2507,
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

_source line 46 · 2026-05-29T00:35:39.278Z_

<details><summary>↩ Tool result · `toolu_01UVJvzsm34D5Xvzn1L19aAC`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu  14K May 29 00:33 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/AGENTS.md
-rw------- 1 ubuntu ubuntu 4.4K May 29 00:32 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/ROADMAP.md
-rw-r--r-- 1 ubuntu ubuntu 9.5K May 28 23:01 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md
-rw-r--r-- 1 ubuntu ubuntu  55K May 27 17:14 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md
-rw-r--r-- 1 ubuntu ubuntu 6.1K May 28 22:58 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/report.md
-rw-r--r-- 1 ubuntu ubuntu  11K May 22 04:47 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/scenario_patches.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "c88a676d-235e-426c-a6f4-7f68249cd578"
}
```

</details>

---


### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading report.md",
  "usage": {
    "total_tokens": 26980,
    "tool_uses": 5,
    "duration_ms": 11960
  },
  "last_tool_name": "Read",
  "uuid": "e2f41347-5c32-4384-8167-f016b7175d1a",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_016AYMikV8RgYEpYhYSdwdFt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "0a41ab27-e63a-41ad-8cbf-75aa6451f447",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LJFXevKtB83YF12R3Typcv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 26454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 49 · 2026-05-29T00:35:41.221Z_

<details><summary>↩ Tool result · `toolu_016AYMikV8RgYEpYhYSdwdFt`</summary>

```text
1	# Handover — 2026-05-28
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| exp_humanoid_baseline_s0 | Humanoid Walk baseline (dt=1, no gate) establishes reference performance for 21-DoF environment CIVO verification. Expect stable training without value overestimation (NVE < 2.0×). Source: post-D171 scope expansion. | — | — | — |
9	
10	## 待处理
11	- exp_quadruped_008d_s0: Quadruped Walk trained dt_emb + gate + subsample ON (008d config: gate_fixed_dt=2, gate_subsample_max_dt=2, H=8), seed=0 — tests whether CIVO onset generalizes to 12-DoF four-legged morphology distinct from Walker/Cheetah single-spine. Expect NVE > 2.0× if CIVO is morphology-independent. Source: post-D171 scope expansion.（等待人工审批）
12	- exp_humanoid_008d_s0: Humanoid Walk trained dt_emb + gate + subsample ON (008d config: gate_fixed_dt=2, gate_subsample_max_dt=2, H=8), seed=0 — tests whether CIVO onset generalizes to highest-DoF (21) DMC locomotion environment. Expect NVE > 2.0× if CIVO is DoF-independent. Source: post-D171 scope expansion.（等待人工审批）
13	- exp_walker_no_dt_emb_s0: dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 0 will NOT show CIVO (NVE<1.5), replicating 008f causal control. This confirms removing dt_embedding prevents CIVO, strengthening C2 (trained dt_emb is necessary condition). Source: D164 Walker priority, replaces killed exp_009f.（已分配 ? GPU:?，等待提交）
14	
15	## 近期结论
16	- **exp_quadruped_baseline_s0** (failed): Quadruped Walk baseline (dt=1, no gate) establishes reference performance for 12-DoF four-legged environment CIVO verification. Expect stable training without value overestimation (NVE < 2.0×). Source: post-D171 scope expansion.
17	- **exp_walker_no_dt_emb_s1** (success): dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 1 will NOT show CIVO (NVE<1.5), replicating 008f causal control from seed 0. Confirms removing dt_embedding prevents CIVO, strengthening C2 (trained dt_emb is necessary condition). Source: D164 Walker priority, plan_012 C2 multi-seed. Replaces killed exp_009f_008f_walker_s1. ← 基于 exp_008f_no_dt_embed_subsample_on_h8
18	  [exp_walker_no_dt_emb_s1 analysis report](/api/workspace-files/projects/event-gated-adaptive-horizon/artifacts/exp_walker_no_dt_emb_s1/report/analysis_43d981.md)
19	- **exp_walker_008d_s7_r2** (failed): Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=7 — C2 onset rate rebuttal reserve. Retry after GPU collision bug. Fixed: --device cuda:1 + EGL=1. Source: D172 Tier 2. ← 基于 exp_008d_subsample_on_h8
20	
21	## 趋势
22	成功 103 / 负向 43 / 失败 22 / 共 208
23	NVE_105K: 0.88 ↓（近 3 次 success）
24	civo_alert: 0 →（近 3 次 success）
25	
26	## 下一步
27	（无活跃 idea，请通过 ideas.md 添加）
28	
29	## 资源状态
30	westd-51268: 空闲 cuda:0, cuda:1
31	
32	## 告警
33	- 016e: 已被终止 — unknown
34	- exp_002_event_gated: 训练失败 — unknown
35	- exp_006: 已被终止 — unknown
36	- exp_008a: 已被终止 — unknown
37	- exp_008a_untrained_s1: 已被终止 — unknown
38	- exp_008a_untrained_s2: 已被终止 — unknown
39	- exp_008c: 已被终止 — unknown
40	- exp_008d: 已被终止 — unknown
41	- exp_008d_civo_trigger_s2: 已被终止 — unknown
42	- exp_008e_subsample_on_dt1_h15: 已被终止 — unknown
43	- exp_008e_subsample_on_fixed_dt1: 已被终止 — unknown
44	- exp_008e_v2_subsample_on_dt1_h15: 已被终止 — unknown
45	- exp_008f_s2: 已被终止 — unknown
46	- exp_009c_s2: 已被终止 — unknown
47	- exp_009d_baseline_walker_s1: 已被终止 — unknown
48	- exp_009f_008f_walker_s1: 已被终止 — unknown
49	- exp_009g_008f_walker_s0: 已被终止 — unknown
50	- exp_009h_008f_walker_s0: 训练失败 — unknown
51	- exp_016_sgs_walker_s1: 训练失败 — unknown
52	- exp_016b_sgs_walker_s1: 训练失败 — unknown
53	- exp_016c_sgs_walker_s1: 训练失败 — unknown
54	- exp_016d_sgs_walker_s1: 训练失败 — unknown
55	- exp_017_subsample_off_trained_dt_emb: 已被终止 — unknown
56	- exp_018_full_sgs_walker_s1: 已被终止 — unknown
57	- exp_019a_pickcube_baseline: 已被终止 — unknown
58	- exp_022_untrained_dt_emb_learned_gate: 已被终止 — unknown
59	- exp_024_cheetah_no_dt_emb_s0: 已被终止 — unknown
60	- exp_025_obs_sgs_walker_s1: 训练失败 — unknown
61	- exp_025_obs_sgs_walker_s3: 训练失败 — unknown
62	- exp_025_obs_sgs_walker_s4: 训练失败 — unknown
63	- exp_026_obs_sgs_cheetah_s0: 训练失败 — unknown
64	- exp_026_obs_sgs_cheetah_s1: 训练失败 — unknown
65	- exp_075_cheetah_civo_trigger_s2: 已被终止 — unknown
66	- exp_076_cheetah_civo_trigger_s3: 已被终止 — unknown
67	- exp_079_frozen_dt_emb_walker_s0: 已被终止 — unknown
68	- exp_089_cheetah_no_dt_emb_s1: 训练失败 — unknown
69	- exp_090_cheetah_no_dt_emb_s2: 训练失败 — unknown
70	- exp_088: 已被终止 — unknown
71	- exp_094_cheetah_008d_s3: 训练失败 — unknown
72	- exp_095_cheetah_no_dt_emb_s3: 训练失败 — unknown
73	- exp_095_cheetah_008a_s0: 已被终止 — unknown
74	- exp_093: 已被终止 — unknown
75	- exp_094: 已被终止 — unknown
76	- exp_096_cheetah_008a_s0: 训练失败 — unknown
77	- exp_098_cheetah_008a_s0: 已被终止 — unknown
78	- exp_099_cheetah_008a_s1: 已被终止 — unknown
79	- exp_101_rssm_prediction_quality: 已被终止 — unknown
80	- exp_102_cheetah_008a_s0: 已被终止 — unknown
81	- exp_103_cheetah_008a_s1: 已被终止 — unknown
82	- exp_hopper_trained_s1: 已被终止 — unknown
83	- exp_hopper_frozen_s1: 已被终止 — unknown
84	- exp_104_hopper_baseline_s0: 已被终止 — unknown
85	- exp_105_hopper_trained_s0: 已被终止 — unknown
86	- exp_106_hopper_trained_s1: 已被终止 — unknown
87	- exp_107_hopper_frozen_s0: 已被终止 — unknown
88	- exp_108_hopper_frozen_s1: 已被终止 — unknown
89	- exp_cheetah_008a_s3: 训练失败 — unknown
90	- exp_walker_008d_s6: 训练失败 — unknown
91	- exp_walker_008d_s7: 训练失败 — unknown
92	- exp_walker_008d_s6_r2: 训练失败 — unknown
93	- exp_walker_008d_s7_r2: 训练失败 — unknown
94	- exp_quadruped_baseline_s0: 训练失败 — unknown
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "cefaac7c-953a-4590-b0cf-c405da5c43b1"
}
```

</details>

---


### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading memory.md",
  "usage": {
    "total_tokens": 29885,
    "tool_uses": 6,
    "duration_ms": 14219
  },
  "last_tool_name": "Read",
  "uuid": "29ad6201-cc42-4a09-93e5-9d82622b48ce",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01QRv4W2JnS9xFPrSCXSQ89K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "646f0829-f911-450e-bfc6-79644702ebec",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HFYc3MfvEaoJJMitj7kLVz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2900,
      "cache_read_input_tokens": 26949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2900,
        "ephemeral_1h_input_tokens": 0
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

_source line 52 · 2026-05-29T00:35:43.489Z_

<details><summary>↩ Tool result · `toolu_01QRv4W2JnS9xFPrSCXSQ89K`</summary>

```text
1	# Memory — event-gated-adaptive-horizon
2	
3	> 非 metrics 性质的决策原因、约束、经验教训。Metrics 查 registry。
4	
5	## westd-51268 GPU 变更 (2026-05-28)
6	- **2026-05-28**: nvidia-smi 仅返回 1 张 GPU。cuda:1 不存在，Quadruped 实验两次 EGL 失败。
7	- 此前（~2026-05-27）同服务器 cuda:1 多次成功运行实验（cheetah_008a_s0, hopper_no_dt_emb_s0 等）
8	- 原因不明（可能服务器端重配）。D175 实验改为 cuda:0 单 GPU 串行
9	- **提交实验前必须 nvidia-smi 验证实际 GPU 数量，不能假设与 project config 一致**
10	
11	## D175 环境扩展串行流水线 (2026-05-28)
12	- 顺序：humanoid_baseline_s0 → humanoid_008d_s0 → quadruped_baseline_s0 → quadruped_008d_s0
13	- 全部在 westd-51268 cuda:0 串行，预估总 wall time ~25h
14	- 每个完成后 cron 回调触发下一个提交
15	- 步数：200K（原有实验 105K，新环境加倍以确保 baseline 收敛）
16	
17	## Hopper 三配置失败模式对比（2026-05-27, 完整图谱）
18	
19	**核心发现**：Hopper 所有 gated config 均表现 severe learning delay，但失败模式各不同：
20	
21	| 配置 | eval_return_final | 恢复? | 失败模式 |
22	|------|-------------------|-------|---------|
23	| trained dt_emb (s0_ext, 150K) | 81.58 | ✅ 是 | 延迟学习→短暂 ve_ratio 升高→自纠正恢复 |
24	| frozen dt_emb (s0_ext, 160K) | 0.56 | ❌ 否 | gate 锁死(entropy=0)→phantom value 膨胀→结构性不可恢复 |
25	| no_dt_emb (s0, 105K) | 10.76 | ❌ 严重延迟 | entropy 维持最大值到 55K，value 发育受阻(baseline 的 4.3%)，无 CIVO |
26	| baseline (无 gate) | 96.43 | — | 正常学习 |
27	
28	**结论**：gate+dt=2+subsample 机制导致 Hopper severe learning delay，与 dt_emb 类型无关。三种 gated config 失败严重程度：frozen > no_dt_emb > trained（trained 可恢复）。支持 D162 重分类。Hopper 不支持 CIVO 跨环境普遍性 claim。
29	
30	**Delayed CIVO 假设已被证伪**（trained_s0_ext, NEGATIVE）：
31	- 原假设：trained_s0 的 ve_ratio 指数上升是 delayed CIVO onset
32	- 实际：延长到 150K 后 ve_ratio 下降、eval_return 恢复到 81.58
33	- 结论：是 transient instability during severe learning delay，非真正 CIVO
34	
35	**frozen_s0_ext 关键 insight**（NEGATIVE）：
36	- frozen dt_emb 锁死 gate（entropy=0, 永久 dt=2），无自适应 horizon
37	- value_mean 持续膨胀（4.34→8.46）但 eval_return ≈ 0（phantom value overestimation）
38	- **与 trained 的区别**：可学习的 dt_emb 既是 CIVO 触发条件，也是自纠正的必要条件
39	
40	**分析约束（仍然有效）**：
41	1. ve_ratio 伪信号: 25K 时 ve_ratio=67750（除零膨胀），必须用 MIN_STEP=35K
42	2. NVE 判断不能只用 tau=2.0 二值判断，必须看完整曲线 + value_mean 趋势 + civo/alert（D165: 阈值从 1.5 正式调整为 2.0）
43	
44	## NVE 阈值决策 (D165, 2026-05-27)
45	
46	**正式阈值：τ=2.0×**（从 1.5 上调）。依据：
47	- 34 experiments (8 CIVO + 26 No-CIVO)，CIVO 最小 NVE peak=3.78, No-CIVO 最大=1.88
48	- 间隔 [1.89, 3.77] 内任何阈值完美分类
49	- τ=2.0 实现 F1=1.0（τ=1.5 有 3 FP，F1=0.842）
50	- 3 个假阳性全为 frozen/no_dt_emb 正常波动
51	
52	## RSSM v3 标准化方法论（2026-05-26，论文唯一权威）
53	
54	**方法论锁定**：v3 standardized 为 RSSM prediction gap 唯一权威数据来源。v1/v2/dry-run 数据废弃。
55	
56	- script: analyze_rssm_standardized.py (v3_standardized)
57	- method: sequential_rollout（dt=1 一步 img_step vs dt=2 两步连续 img_step）
58	- seed=42, n_samples=1000, obs_keys=height(1)+orientations(14)+velocity(9)
59	- 位置：westd-51268:/root/autodl-tmp/event-gated-adaptive-horizon/
60	
61	**Walker v3 结果**：
62	
63	| Model | dt1 obs_mse | dt2 obs_mse | obs ratio | dt1 reward_mae | dt2 reward_mae | reward ratio |
64	|---|---|---|---|---|---|---|
65	| baseline (exp_009d) | 9.60 | 15.11 | 1.57× | 0.0294 | 0.0458 | 1.56× |
66	| trained_dt_emb (exp_008d) | 25.71 | 34.60 | 1.35× | 0.0530 | 0.0865 | 1.63× |
67	| no_dt_emb (exp_009c, 20ep) | 19.82 | 20.67 | 1.04× | 0.0611 | 0.0789 | 1.29× |
68	| frozen_dt_emb (exp_084) | 16.33 | 24.03 | 1.47× | 0.3482 | 0.3561 | 1.02× |
69	
70	**关键**: trained_dt_emb 有最高 reward ratio (1.63×)，但 obs ratio (1.35×) 低于 baseline (1.57×)。CIVO root cause 在 reward head dt=2 generalization，非 obs prediction。
71	
72	**Cheetah v3 结果**（2026-05-26 完成）：
73	
74	| Model | dt1 obs_mse | dt2 obs_mse | obs ratio | dt1 reward_mae | dt2 reward_mae | reward ratio |
75	|---|---|---|---|---|---|---|
76	| trained_dt_emb (exp_097, v3 standardized) | 5.26 | 4.90 | 0.93× | 0.1410 | 0.1405 | 1.00× |
77	| no_dt_emb (Cheetah, 112ep) | — | — | 1.02× | — | — | 1.005× |
78	
79	**跨环境差异（重要发现）**：Cheetah trained_dt_emb reward gap = 1.00×（无 fidelity gap），而 Walker = 1.63×。Cheetah 仍有 3/4 CIVO onset。RSSM fidelity gap 可能不是 CIVO 唯一/主要驱动因素（至少在 Cheetah 环境）。
80	
81	## Cheetah 008d CIVO 跨 seed 完整图谱（2026-05-26, 4/4 seeds 完成）
82	
83	| Seed | NVE Peak | Onset Step | Pattern | Eval Final | Eval%Baseline |
84	|------|----------|------------|---------|------------|---------------|
85	| s0 (exp_078) | 2.3×@75K | 45K | sustained→self_correcting | 119.5 | 28% |
86	| s1 (exp_088) | 0.31× | — | no onset | 309.3 | 72% |
87	| s2 (exp_091) | 127.6×@95K | 45K | collapse | 2.5 | 0.6% |
88	| s3 (exp_097) | 2.3×@45K | 45K | transient→degraded | 61.7 | 14% |
89	
90	**Onset rate**: 3/4 (75%)。跨环境 onset rate: Walker 3/3 + Cheetah 3/4 = 6/7 (86%)。
91	
92	**三种 CIVO 后果模式**（新发现，2026-05-26）：
93	1. **sustained→self_correcting** (s0): NVE 缓升缓降，eval 部分恢复但远低于 baseline
94	2. **collapse** (s2): NVE 爆发性增长 (>100×)，eval 归零不可恢复
95	3. **transient→degraded** (s3, 新): NVE 脉冲后自修复（0.3@final），但 eval 持续下滑（192.5@75K → 61.7@105K），actor_entropy 升至 -0.7 → **CIVO 造成不可逆 policy 损伤，即使 ve_ratio 恢复正常**
96	
97	**关键 insight**: ve_ratio 恢复 ≠ policy 恢复。CIVO 的 policy 损伤是不可逆的，这强化了 "需要预防（frozen/removed dt_emb）而非依赖自修复" 的 narrative。
98	
99	**Onset timing 一致性**: 3 个 onset seed 全部在 45K step，与 Walker onset 区间 (35K-45K) 一致。暗示 onset 与 world model 训练阶段拐点相关。
100	
101	## CLI flag 服务器差异 (2026-05-25) — 已解决
102	- **2026-05-26 更新**: westd-51268 已从 bjb1 rsync 代码，两边一致使用 `--gate_dt_embed_dim`
103	- 教训: 不要跨服务器复制命令模板，提交前验证参数名
104	
105	## NVE baseline 计算注意事项 (2026-05-25)
106	- Cheetah baseline 必须用 step-matched ve_ratio（不是固定值）
107	- exp_077 和 exp_083 的 ve_ratio trajectory 差异较大（peak 0.955 vs 0.6）
108	- 使用 mean baseline 更稳健，但需标注两个 seed 的值
109	
110	## Actor Entropy 详细分析 (2026-05-26, Worker B 完成, plan_031 DONE)
111	- trained_dt_emb 在 15K 步时 entropy 降到 -0.76（no_dt_emb 同步骤 ~+1.0）
112	- **exp_097 entropy 时序**: -4.91@35K → -0.69@105K（剧烈回弹），证明 CIVO 造成不可逆策略退化
113	- 图表: artifacts/actor_entropy_comparison.pdf (art_20260526_efebc4)
114	
115	## dt_embedding Cosine Similarity 分析 (2026-05-26, Worker C 完成)
116	
117	**核心发现**: trained dt_emb 将 dt=1 和 dt=2 编码为几乎相反的方向。
118	
119	| 配置 | cos(dt1, dt2) | 解读 |
120	|------|--------------|------|
121	| trained Walker (3 seeds) | -0.655 ~ -0.903 | 强反相关 |
122	| trained Cheetah (2 seeds) | -0.684 ~ -0.803 | 跨环境一致 |
123	| frozen Walker/Cheetah | -0.150 ~ 0.203 | 随机初始化附近 |
124	
125	**训练动态**: 前 25K 步 cosine 急剧下降到 -0.9，与 CIVO onset (35-45K) 时间窗口重合。
126	图表: artifacts/dt_embedding_cosine_similarity.png (art_20260526_07e8c8)
127	
128	## Value Distribution vs Returns 分析 (2026-05-26, Worker D 完成)
129	
130	**核心发现**: CIVO 的关键病理指标是 V(s)-G_t correlation，不是 bias magnitude。
131	- **008d**: correlation=-0.20 = delusional critic
132	- **008a**: correlation=0.54 = 有 bias 但保持正相关
133	图表: artifacts/value_vs_returns.pdf (art_20260526_8d21ad)
134	
135	## RSSM 时序 Fidelity 数据 (2026-05-26, Worker A 发现, plan_030 DONE)
136	- **exp_066b Walker proxy 数据**: reward ratio 0.89×@20K → 1.22×@35K → 1.53×@50K → 1.80×@65K
137	- gap 出现先于 CIVO onset → 支持"RSSM fidelity gap 为 Walker CIVO 传导路径"的 D158 叙事
138	
139	## 服务器迁移 (2026-05-26)
140	- bjb1-45299 无卡，数据已迁移到 westd-51268
141	- westd-51268: 原 2×RTX PRO 6000 Blackwell (96GB), CUDA 13.2。**2026-05-28 起仅 1 张可见**
142	- westd 数据盘重启后清空，代码通过 rsync 从 bjb1 恢复
143	
144	## DreamerV3 进程退出行为 (2026-05-27)
145	- [失败模式] 进程生命周期：DreamerV3 进程在达到 --steps 限制后可能不会立即退出，继续执行已启动的 data collection episodes。exp_cheetah_008a_s3 配置 --steps=105000，105K eval 正常完成后进程继续运行到 112K 才被 SIGTERM → 修复方案：非真实失败，105K 数据完整可用。后续提交新实验到同 GPU 前，cron/submission 系统会自动清理旧进程。注意此类 SIGTERM 退出的实验需检查日志确认 eval 数据是否已完成。
146	- [失败模式] EGL 渲染 segfault：008d config (subsample ON + gate_fixed_dt=2 + H=8) 在 westd-51268 上连续 4 次失败（s6/s7 原始 + r2 retry）。进程在 step 15000 "Start evaluation." 后静默崩溃，日志无 Traceback/OOM/CUDA error，疑似 MuJoCo EGL 渲染层 segfault。s6_r2 (cuda:0) 和 s7_r2 (cuda:1) 相同模式，排除单卡硬件问题。若未来需要重跑 008d 额外 seed，应先排查 EGL 驱动兼容性或换用 osmesa 渲染后端。
147	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "665f9942-dd8d-4270-818a-0b4cf784b3ed"
}
```

</details>

---


### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 34634,
    "tool_uses": 7,
    "duration_ms": 16766
  },
  "last_tool_name": "Bash",
  "uuid": "b33bcd7e-423e-4429-a454-1741bad48405",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01BLj2TLPgzgsJ879EpB5WaQ`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts -type f -name \"*.csv\" -o -name \"*summary*\" -o -name \"*table*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "f3a0d7f6-5f87-4887-a215-f80cc5a8ab95",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ENDPMgN7B2o3LSJGn3Ksof",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 4747,
      "cache_read_input_tokens": 29849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4747,
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

_source line 55 · 2026-05-29T00:35:46.092Z_

<details><summary>↩ Tool result · `toolu_01BLj2TLPgzgsJ879EpB5WaQ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_threshold_sensitivity.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/temporal_causality_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table_37b680.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/ablation_mechanism_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/summary_table.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_4seed_robustness_analysis.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/cross_env_civo_comparison.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/metrics_table.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/paper_figure_data_summary.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/bootstrap_ci_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_trajectories.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/actor_entropy_value_calibration_summary.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/bootstrap_cis_summary.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/learning_curves.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/metrics_table.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/table1_integrity_check.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/bootstrap_ci_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/table5_full_validation.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/metrics_summary_table.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/seed_label_diff_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/literature_survey_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/bootstrap_ci_summary_67aaf7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/chart/value_distribution_summary.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_064_value_distribution/data/results_summary.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/value_distribution_summary.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/value_distribution_summary.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/scripts/generate_detector_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_001_baseline_s3_ve_profile_full.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_001_baseline_s4_ve_profile_full.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_001_baseline_s2_ve_profile_full.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_001_baseline_s1_ve_profile_full.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_066_timeseries_rssm_fidelity/data/exp_066_analysis_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/supplementary/analysis/nve_4seed_robustness_summary.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/supplementary/analysis/baseline_4seed_mean_ve_ratio.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/tables
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/tables/temporal_causality_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/tables/cross_env_civo_comparison.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/tables/ablation_mechanism_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures_data/summary_table.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures_data/nve_trajectories.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures_data/learning_curves.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/metrics_summary_table.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/table5_validation
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/table5_validation/table5_full_validation.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_001_baseline_s2_ext_ve_ratio_profile.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/seed_label_diff_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature_survey_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_065/data/results_summary.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/detector_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/metrics_table.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/metrics_table.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/table1_integrity_check.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/exp_020_c6_summary.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/detector_table.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "7dec181a-29dc-4bc5-a2cd-56829a809ffe"
}
```

</details>

---


### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading artifacts/_project/data/summary_table.csv",
  "usage": {
    "total_tokens": 37373,
    "tool_uses": 8,
    "duration_ms": 19080
  },
  "last_tool_name": "Read",
  "uuid": "a8116b6a-ad13-4fec-bf07-116efd6d5b04",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_011CW7L4rhn4AkVEWUW3dXpf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/summary_table.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "eec2a0a8-4d6c-444f-b8a3-29597604d28f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N4P38WxSk8axbz9P9Mdxv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2737,
      "cache_read_input_tokens": 34596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2737,
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

_source line 58 · 2026-05-29T00:35:48.338Z_

<details><summary>↩ Tool result · `toolu_011CW7L4rhn4AkVEWUW3dXpf`</summary>

```text
1	exp_id,config_label,hypothesis,conclusion,final_eval_return,peak_eval_return,final_ve_ratio,final_nve,vs_baseline_pct,seed,total_steps
2	exp_001_baseline,baseline (seed 0),DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model,success,970.41,970.41,0.656,1.0,0.0,1,512000
3	exp_009a_baseline_walker_s2,baseline (seed 2),Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）,,948.4,966.9,,,-0.52,2,448000
4	exp_006_fixed_dt2,dt=2 fixed (006),诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。,negative,132.86,485.3,2.722,4.8348,-78.42,1,65000
5	exp_007_fixed_dt4,dt=4 fixed (007),诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。,negative,152.49,176.9,0.061,0.151,-75.63,1,55000
6	exp_005_event_gated_v4,learned gate (005),,negative,98.84,541.18,,,-89.40,1,145000
7	exp_008d_subsample_on_h8,trained dt_emb H=8 (008d) seed 0/1,,negative,82.75,167.22,1.666,4.1238,-86.78,1,55000
8	exp_009b_008d_walker_s2,trained dt_emb H=8 (008d) seed 2,Walker Walk trained dt_emb + subsample ON + H=8 seed 2 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）,negative,267.93,278.54,0.251,0.38,-70.74,2,105000
9	exp_008f_no_dt_embed_subsample_on_h8,no dt_emb (008f) seed 0/1,"C2 confound control：隔离 dt_embedding conditioning vs RSSM learned dt=2 dynamics。subsample ON + dt=2 imagination + H=8（与 008d 完全一致），但 gate_dt_embed_dim=0（去掉 dt_embedding 条件输入）。如果 008f 崩塌（v/e >50%）→ 根因是 RSSM 的 dt=2 训练数据导致 dynamics 偏差，不是 dt_embedding per se。如果 008f 稳定（v/e <35%）→ 确认 dt_embedding conditioning 是 delusional critic 的直接原因。对照：008d（dt_embed_dim>0, v/e 15.5%→41.2%→69.3% 崩塌）vs 008c（subsample OFF, untrained dt_emb, v/e 稳定 ~22-33%）。",success,503,503,0.1952,0.3,-45.08,1,105000
10	exp_009c_008f_walker_s2,no dt_emb (008f) seed 2,Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）,negative,148.34,359.14,0.75,1.14,-83.80,2,105000
11	exp_008c_no_subsample_dt2_h8,untrained dt_emb dt=2 H=8 (008c),隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。,negative,240.86,241.87,0.328,0.5826,-60.89,1,68000
12	exp_008a_no_subsample_dt2,untrained dt_emb dt=2 H=15 (008a),隔离 subsample 效应：subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。,success,777.66,777.66,0.386,0.59,-15.07,1,112000
13	exp_008e_v3_walker_s1,dt=1 imag (008e_v3) seed 1,Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）,success,869.9,869.9,0.527,0.8034,-5.00,1,112000
14	exp_008e_v3_walker_s2,dt=1 imag (008e_v3) seed 2,Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证,,435.1,435.1,0.507,0.9005,-29.36,2,68000
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d0807e66-cbe1-495d-af33-4de71bfac2ad"
}
```

</details>

---


### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading artifacts/_project/data/metrics_table.csv",
  "usage": {
    "total_tokens": 37374,
    "tool_uses": 9,
    "duration_ms": 19168
  },
  "last_tool_name": "Read",
  "uuid": "a5b21af6-de92-43af-b53e-bf04dd4f0edf",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01CGMGQoz67ibqL8sWhnCWKc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/metrics_table.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "cd447858-d659-4b1c-b6ca-3308c729720e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N4P38WxSk8axbz9P9Mdxv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2737,
      "cache_read_input_tokens": 34596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2737,
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

_source line 61 · 2026-05-29T00:35:48.425Z_

<details><summary>↩ Tool result · `toolu_01CGMGQoz67ibqL8sWhnCWKc`</summary>

```text
1	exp_id,gate_enabled,subsample,fixed_dt,imag_horizon,dt_embed_dim,seed,status,eval_final,eval_peak,ve_35k,ve_45k,ve_65k,ve_105k,nve_35k,nve_45k,nve_65k,nve_105k,gate_dt_mean_final,gate_dt_1_frac_final,claims
2	exp_001_baseline,OFF,OFF,1,15,N/A,1,done/success,970.41,970.41,0.2412,0.3310,0.5629,0.6564,1.00,1.00,1.00,1.00,N/A,N/A,ref
3	exp_009a_baseline_s2,OFF,OFF,1,15,N/A,2,running,948.42,966.94,0.3056,0.3629,0.4737,0.6447,1.27,1.10,0.84,0.98,N/A,N/A,ref
4	exp_008a,ON,OFF,2,15,32,1,done/success,777.66,777.66,0.1571,0.2342,0.3719,0.3861,0.65,0.71,0.66,0.59,2.0,0.0,C3
5	exp_008c,ON,OFF,2,8,32,1,done/negative,240.86,241.87,0.2184,0.2537,0.3278,,0.91,0.77,0.58,,2.0,0.0,C3
6	exp_008d,ON,ON,2,8,32,1,done/negative,82.75,167.22,0.4113,0.6929,,,1.71,2.09,,,2.0,0.0,"C1,C2"
7	exp_008e_v3,ON,ON,1,15,32,1,done/success,869.88,869.88,0.2270,0.2895,0.4048,0.5264,0.94,0.87,0.72,0.80,1.0,1.0,C6
8	exp_008f,ON,ON,2,8,0,1,done/success,503.21,503.21,0.1755,0.2753,0.2067,0.1952,0.73,0.83,0.37,0.30,2.0,0.0,"C1,C2"
9	exp_009b_008d_s2,ON,ON,2,8,32,2,done/negative,267.93,278.54,0.2986,0.5359,0.5303,0.2511,1.24,1.62,0.94,0.38,2.0,0.0,"C1,C2"
10	exp_009c_008f_s2,ON,ON,2,8,0,2,done/negative,148.34,359.14,0.1915,0.2373,0.2978,0.7499,0.79,0.72,0.53,1.14,2.0,0.0,"C1,C2"
11	exp_008e_v3_s2,ON,ON,1,15,32,2,running,435.09,435.09,0.2489,0.3509,0.5067,,1.03,1.06,0.90,,1.0,1.0,C6
12	exp_006_fixed_dt2,ON,OFF,2,15,32,1,done/negative,132.86,485.33,0.3113,0.5331,2.7224,,1.29,1.61,4.84,,2.0,0.0,diagnostic
13	exp_007_fixed_dt4,ON,OFF,4,15,32,1,done/negative,152.49,176.90,,,,,,,,4.0,,diagnostic
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "2c901623-ff88-4773-b1cd-4c63c4592ebd"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading artifacts/_project/data/cross_env_civo_comparison.csv",
  "usage": {
    "total_tokens": 37375,
    "tool_uses": 10,
    "duration_ms": 19426
  },
  "last_tool_name": "Read",
  "uuid": "4b32a03c-a009-4119-ad23-38d179534885",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_014UdSjYYJycvibffRLzeDtZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/cross_env_civo_comparison.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "f6d044d6-0f50-432a-a00b-205e9150374d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N4P38WxSk8axbz9P9Mdxv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2737,
      "cache_read_input_tokens": 34596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2737,
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

_source line 64 · 2026-05-29T00:35:48.682Z_

<details><summary>↩ Tool result · `toolu_014UdSjYYJycvibffRLzeDtZ`</summary>

```text
1	Environment,Configuration,Eval Return (mean),Eval Return (std),Seeds (eval),NVE Peak (max),Seeds (NVE),CIVO,Source Experiments
2	Walker Walk,Baseline (dt=1),787.7,230.8,4,—,—,—,"exp_001_baseline (s0=915.67), exp_001_baseline_s2 (443.46), exp_001_baseline_s3 (869.03), exp_001_baseline_s4 (922.80)"
3	Walker Walk,Trigger (trained dt_emb),140.6,111.5,3,4.72,5,Yes (5/5),"exp_008d (s0: eval@112K=58.5), exp_008d_civo_trigger_s3 (267.6), exp_059_walker_trained_s5 (95.8); NVE: s1=4.13 s2=1.62 s3=1.53 s4=4.62 s5=4.72"
4	Walker Walk,Control (no dt_emb),373.8,111.9,3,1.41,4,No (0/4),"exp_008f (s0=503), exp_009c_s3 (311.92), exp_008f_s4 (306.50); NVE: s0=0.30 s1=0.81 s3=0.52 s4=1.41"
5	Cheetah Run,Baseline (dt=1),593.9,60.4,5,—,—,—,"exp_023a (624.7), exp_023b (520.3), exp_023_s2 (645.4), exp_023_s3 (642.13), exp_023_s4 (537.03)"
6	Cheetah Run,Trigger (trained dt_emb),26.3,36.0,2,70.64,2,Yes (2/2),"exp_010b_s0 (eval=0.83 NVE=70.64), exp_010b_s1 (eval=51.7 NVE=8.27)"
7	Cheetah Run,Control (no dt_emb),86.9,13.6,2,0.20,2,No (0/2),"exp_024b_s0 (eval=96.5 NVE=0.20), exp_024b_s1 (eval=77.3 NVE=0.10)"
8	Cartpole Swingup,Baseline (dt=1),673.3,142.0,3,—,—,—,"exp_060 s0=809.4 s1=684.4 s2=526.1"
9	Cartpole Swingup,Trigger (trained dt_emb),236.3,29.7,3,0.06,3,No (0/3),"exp_061 s0=211.1 (VE=0.058) s1=269.0 (VE=0.040) s2=228.9 (VE=0.043)"
10	Cartpole Swingup,Control (no dt_emb),—,—,0,—,—,—,exp_062 (RUNNING)
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "1acb9b96-4911-4447-bae9-84e745c62d48"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading artifacts/nve_experiment_data.csv",
  "usage": {
    "total_tokens": 41268,
    "tool_uses": 11,
    "duration_ms": 23148
  },
  "last_tool_name": "Read",
  "uuid": "b995662d-abb0-40ed-b8c0-285486a239d0",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_017uW1FfL1pvqWUkpr9obXGr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "6a27cd57-3ebc-41e1-b0ab-721b393be30c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SxVk4zWkBeUjVb9qamK1sL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 37333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3884,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 67 · 2026-05-29T00:35:52.405Z_

<details><summary>↩ Tool result · `toolu_017uW1FfL1pvqWUkpr9obXGr`</summary>

```text
1	exp_id,nve_peak,ground_truth,env,config_type
2	exp_008d/009e (Walker s1),4.13,1,Walker,trained
3	exp_009b (Walker s2),1.62,1,Walker,trained
4	exp_008d_s3 (Walker s3),1.53,1,Walker,trained
5	exp_008d_s4 (Walker s4),4.62,1,Walker,trained
6	exp_059 (Walker s5),4.72,1,Walker,trained
7	exp_048 (Cheetah s0),70.64,1,Cheetah,trained
8	exp_010b (Cheetah s1),8.27,1,Cheetah,trained
9	exp_008f (Walker s0 no_dt_emb),1.02,0,Walker,no_dt_emb
10	exp_009c (Walker s2 no_dt_emb),1.26,0,Walker,no_dt_emb
11	exp_008f_s3 (Walker s3 no_dt_emb),1.2,0,Walker,no_dt_emb
12	exp_008f_s4 (Walker s4 no_dt_emb),1.41,0,Walker,no_dt_emb
13	exp_009c_s3 (Walker s3 no_dt_emb #2),0.52,0,Walker,no_dt_emb
14	exp_042 (Walker s0 frozen),0.194,0,Walker,frozen
15	exp_047 (Walker s1 frozen),1.71,0,Walker,frozen
16	exp_057 (Walker s2 frozen),1.88,0,Walker,frozen
17	exp_046 (Cheetah s0 frozen),1.35,0,Cheetah,frozen
18	exp_058 (Cheetah s1 frozen),0.78,0,Cheetah,frozen
19	exp_024b_s0 (Cheetah s0 no_dt_emb),0.2,0,Cheetah,no_dt_emb
20	exp_024b_s1 (Cheetah s1 no_dt_emb),0.1,0,Cheetah,no_dt_emb
21	exp_060 (Cartpole baseline),1.0,0,Cartpole,baseline
22	exp_061 (Cartpole trained dt_emb),0.9,0,Cartpole,trained
23	exp_062 (Cartpole no_dt_emb),1.0,0,Cartpole,no_dt_emb
24	exp_001_s1 (Walker baseline),1.0,0,Walker,baseline
25	exp_001_s2 (Walker baseline),1.13,0,Walker,baseline
26	exp_001_s3 (Walker baseline),1.05,0,Walker,baseline
27	exp_001_s4 (Walker baseline),0.95,0,Walker,baseline
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d89377a5-eaf0-4601-ad4a-7300defb036e"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 41272,
    "tool_uses": 12,
    "duration_ms": 23385
  },
  "last_tool_name": "Bash",
  "uuid": "832b04a8-0ff4-4589-a87e-7c74e393ac41",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Bash · `toolu_016hQaMBmvKcDzQz8gvoRqt8`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper -type f -name \"*.tex\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "66530be3-c684-4816-8489-4589a2a15efd",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SxVk4zWkBeUjVb9qamK1sL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 37333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3884,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 70 · 2026-05-29T00:35:52.700Z_

<details><summary>↩ Tool result · `toolu_016hQaMBmvKcDzQz8gvoRqt8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/temporal_causality_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table_37b680.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_threshold_sensitivity.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/ablation_mechanism_table.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "38c7839a-43d4-4f2a-9e0c-534cc8163e5b"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading artifacts/_project/paper/ablation_mechanism_table.tex",
  "usage": {
    "total_tokens": 42636,
    "tool_uses": 13,
    "duration_ms": 26040
  },
  "last_tool_name": "Read",
  "uuid": "b9adab06-4ff4-4dbe-ba27-a08772186949",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01VY1xC4AnVWfPZ98GNn2xox`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/ablation_mechanism_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "cbf66ddb-d660-4cd0-885b-5f49a63456f1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LK2dhNkmAwrYRWYQUBLkMV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 41217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1358,
        "ephemeral_1h_input_tokens": 0
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

_source line 73 · 2026-05-29T00:35:55.297Z_

<details><summary>↩ Tool result · `toolu_01VY1xC4AnVWfPZ98GNn2xox`</summary>

```text
1	% Table A: CIVO Mechanism Evidence Summary
2	% Data sources: exp_063 (RSSM fidelity), exp_064 (value distribution),
3	%               exp_065 (dt_emb cosine), NVE threshold sensitivity analysis
4	\begin{table}[t]
5	\centering
6	\caption{CIVO mechanism evidence summary. Each row quantifies one link in the
7	causal chain from \texttt{dt\_emb} representation collapse to value
8	overestimation. CIVO config uses trained \texttt{dt\_emb} with
9	\texttt{gate\_enabled} (exp\_008d); Control uses no \texttt{dt\_emb}
10	(exp\_008f). NVE diagnostic is computed over $n{=}32$ seeds across Walker and
11	Cheetah.%
12	\label{tab:mechanism-evidence}}
13	\small
14	\begin{tabular}{@{}llccc@{}}
15	\toprule
16	Analysis & Metric & CIVO Config & Control & Ratio \\
17	\midrule
18	\texttt{dt\_emb} representation\textsuperscript{a}
19	  & $\cos(\mathbf{e}_1, \mathbf{e}_2)$
20	  & $-0.94$ to $-0.70$
21	  & $-0.15$ to $+0.07$
22	  & --- \\
23	RSSM fidelity gap\textsuperscript{b}
24	  & Reward MAE ($\text{dt}{=}2$ / $\text{dt}{=}1$)
25	  & $2.695\times$
26	  & $1.483\times$
27	  & $1.82\times$ \\
28	RSSM fidelity gap\textsuperscript{b}
29	  & Obs MSE ($\text{dt}{=}2$ / $\text{dt}{=}1$)
30	  & $1.560\times$
31	  & $1.505\times$
32	  & $1.04\times$ \\
33	Value calibration\textsuperscript{c}
34	  & $V / V^{\text{MC}}$ (median)
35	  & $3.40$
36	  & $1.05$
37	  & $3.24\times$ \\
38	Value calibration\textsuperscript{c}
39	  & $V / V^{\text{MC}}$ (mean)
40	  & $7.80$
41	  & $2.58$
42	  & $3.02\times$ \\
43	NVE diagnostic\textsuperscript{d}
44	  & AUROC ($n{=}32$)
45	  & \multicolumn{2}{c}{$0.961$}
46	  & --- \\
47	NVE diagnostic\textsuperscript{d}
48	  & F1 @ $1.5\times$
49	  & \multicolumn{2}{c}{$0.880$}
50	  & --- \\
51	\bottomrule
52	\end{tabular}
53	
54	\vspace{2pt}
55	{\footnotesize
56	\textsuperscript{a}exp\_065: cosine similarity between trained $\mathbf{e}_{\text{dt}=1}$ and $\mathbf{e}_{\text{dt}=2}$ embeddings (3 seeds); frozen embeddings serve as control.
57	\textsuperscript{b}exp\_063: single-step RSSM prediction quality, baseline\_s1 vs exp\_008d.
58	\textsuperscript{c}exp\_064: value distribution at $t{=}105\text{K}$; exp\_008d (CIVO) vs exp\_008f (no \texttt{dt\_emb}).
59	\textsuperscript{d}NVE threshold analysis over 32 Walker + Cheetah seeds; optimal threshold $= 1.5\times$.
60	}
61	\end{table}
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "e5005d41-5ae4-4395-a354-8ddb246ebe2c"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading artifacts/_project/data/nve_4seed_robustness_analysis.csv",
  "usage": {
    "total_tokens": 42639,
    "tool_uses": 14,
    "duration_ms": 26410
  },
  "last_tool_name": "Read",
  "uuid": "6c6894c6-c3c9-421e-bf1c-b5921851a32b",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_01PZAcB4GZdyPXPW4m93uk4U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_4seed_robustness_analysis.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "c4d5a448-976c-4fc2-84e7-5c8f44059a16",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LK2dhNkmAwrYRWYQUBLkMV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 41217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1358,
        "ephemeral_1h_input_tokens": 0
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

_source line 76 · 2026-05-29T00:35:55.674Z_

<details><summary>↩ Tool result · `toolu_01PZAcB4GZdyPXPW4m93uk4U`</summary>

```text
1	exp_id,ground_truth,peak_step_s1,peak_nve_s1,peak_step_4seed,peak_nve_4seed,peak_ve_ratio,class_s1,class_4seed,flip,method
2	exp_006_fixed_dt2,CIVO,65000,4.836189,65000,4.522167,2.7224,CIVO,CIVO,False,direct
3	exp_008d_subsample_on_h8,CIVO,55000,4.129242,55000,3.544652,1.6663,CIVO,CIVO,False,direct
4	exp_008e_v3_walker_s2,no-CIVO,105000,3.780128,105000,3.681979,2.4813,CIVO,CIVO,False,rescaled
5	exp_009b_008d_walker_s2,CIVO,45000,1.619005,45000,1.229276,0.5359,CIVO,no-CIVO,True,direct
6	exp_001_baseline,no-CIVO,35000,1.0,75000,1.208832,0.7194,no-CIVO,no-CIVO,False,direct
7	exp_008f_no_dt_embed_subsample_on_h8,no-CIVO,55000,0.970092,55000,0.832822,0.3915,no-CIVO,no-CIVO,False,direct
8	exp_008e_v3_walker_s1,no-CIVO,35000,0.941125,75000,0.879575,0.2270,no-CIVO,no-CIVO,False,rescaled
9	exp_008a_no_subsample_dt2,no-CIVO,55000,0.932205,75000,0.900323,0.5358,no-CIVO,no-CIVO,False,direct
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "bb4767a3-ea71-4927-aad4-88c9af5ec4d5"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 42642,
    "tool_uses": 15,
    "duration_ms": 26557
  },
  "last_tool_name": "Bash",
  "uuid": "6770384a-7257-4ad8-8a2e-94cd1b68058b",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01CQi68p2HoEcLusBdTiZd4v`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/ | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "be68f775-9efe-4261-86a9-11612922eec3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LK2dhNkmAwrYRWYQUBLkMV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 41217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1358,
        "ephemeral_1h_input_tokens": 0
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

_source line 79 · 2026-05-29T00:35:55.895Z_

<details><summary>↩ Tool result · `toolu_01CQi68p2HoEcLusBdTiZd4v`</summary>

```text
total 452K
-rw-r--r-- 1 ubuntu ubuntu  744 May 14 09:43 actor_entropy_value_calibration_summary.txt
-rw-r--r-- 1 ubuntu ubuntu 3.7K May 15 10:49 actor_loss_data.json
-rw-r--r-- 1 ubuntu ubuntu  714 May 16 20:31 additional_figure_data_index.md
-rw-r--r-- 1 ubuntu ubuntu  14K May 26 03:31 analysis_rssm_fidelity_v2.json
-rw-r--r-- 1 ubuntu ubuntu 2.6K May 26 05:46 analysis_rssm_standardized_cheetah.json
-rw-r--r-- 1 ubuntu ubuntu 5.3K May 26 05:46 analysis_rssm_standardized_walker.json
-rw-r--r-- 1 ubuntu ubuntu  301 May 19 23:15 baseline_4seed_meta.txt
-rw-r--r-- 1 ubuntu ubuntu 3.2K May 16 20:37 bootstrap_ci_results.json
-rw-r--r-- 1 ubuntu ubuntu 5.2K May 16 20:39 bootstrap_ci_summary.md
-rw-r--r-- 1 ubuntu ubuntu 3.5K May 16 23:50 bootstrap_cis.json
-rw-r--r-- 1 ubuntu ubuntu 4.0K May 16 18:58 bootstrap_cis_8db708.json
-rw-r--r-- 1 ubuntu ubuntu  327 May 16 13:31 bootstrap_cis_summary.txt
-rw-r--r-- 1 ubuntu ubuntu 6.5K May 17 07:32 civo_detector_prospective_results.json
-rw-r--r-- 1 ubuntu ubuntu  47K May 17 02:28 civo_detector_retrospective.json
-rw-r--r-- 1 ubuntu ubuntu  47K May 17 02:28 civo_detector_retrospective_5b51de.json
-rw-r--r-- 1 ubuntu ubuntu 1.4K May 25 03:41 cross_env_civo_comparison.csv
-rw-r--r-- 1 ubuntu ubuntu 1.3K May 25 03:41 cross_env_civo_comparison.tex
-rw-r--r-- 1 ubuntu ubuntu  14K May 17 05:10 detector_formal_validation_v3.json
-rw-r--r-- 1 ubuntu ubuntu  14K May 17 05:10 detector_formal_validation_v3_9f711c.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "90a3bd36-cad2-4277-87bf-4db1221e19ca"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running grep -r \"TCN\\|RAVE\\|SGS\\|critic\\|reward-only\\|wid…",
  "usage": {
    "total_tokens": 45257,
    "tool_uses": 16,
    "duration_ms": 29672
  },
  "last_tool_name": "Bash",
  "uuid": "ec8e3905-1ba5-4db8-9dc1-f3191d09b3f2",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_017s1FBwo2Gahf42fVkTWWVj`</summary>

```json
{
  "command": "grep -r \"TCN\\|RAVE\\|SGS\\|critic\\|reward-only\\|wide\\|narrow\\|dual\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon --include=\"*.csv\" --include=\"*.json\" --include=\"*.md\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d51f9809-392d-4c6e-83c6-7ccaa38922fd",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JqsuxrUskqDV6kZgDk8Cz3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2609,
      "cache_read_input_tokens": 42575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2609,
        "ephemeral_1h_input_tokens": 0
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

_source line 82 · 2026-05-29T00:35:59.003Z_

<details><summary>↩ Tool result · `toolu_017s1FBwo2Gahf42fVkTWWVj`</summary>

```text
&lt;persisted-output>
Output too large (51.7KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2cc17247-5799-4eaa-a6da-169e7b334e68/tool-results/blvge4m2p.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md:We appreciate this important question. Our claim is precisely scoped to "imagination-based actor-critic architectures with learned temporal embeddings," and we deliberately avoid generalizing to all reinforcement learning methods. The TAWM comparison directly isolates the role of feedback architecture: TAWM uses the same RSSM world model but replaces imagination-based bootstrapping with re-planning, and CIVO does not manifest. This result demonstrates that the failure originates in the feedback loop of imagined rollouts rather than in RSSM per se. At the mechanistic level, CIVO requires three structural ingredients: (1) temporal embeddings that co-adapt with the value function through shared gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from a shared representation. These conditions are defined functionally and are not tied to any specific network topology. We identify transformer-based world models as an explicit future direction in Section 7, and we believe the diagnostic contribution of this paper, identifying and characterizing a previously undocumented failure mode, holds independent value from exhaustive architectural enumeration.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md:## Q5: SGS Sample Size (n=2)
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "e14521e3-9f5d-4f0d-ae6b-e5067296696f"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running grep -r \"exp_0[0-9][0-9]\\|TCN\\|RAVE\\|008d\\|SGS\" /…",
  "usage": {
    "total_tokens": 45916,
    "tool_uses": 17,
    "duration_ms": 31982
  },
  "last_tool_name": "Bash",
  "uuid": "dee734ff-e46b-4fe6-8393-9b4f3e74fadf",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01Qumf1mthse8DzjJWffeXR5`</summary>

```json
{
  "command": "grep -r \"exp_0[0-9][0-9]\\|TCN\\|RAVE\\|008d\\|SGS\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/*.csv 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "3b026bd8-c57b-4d15-82ae-780042eed2cd",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P2HMfGE6ppsXszDQm1CBFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 45184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 653,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 85 · 2026-05-29T00:36:01.298Z_

<details><summary>↩ Tool result · `toolu_01Qumf1mthse8DzjJWffeXR5`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_008d/009e (Walker s1),4.13,1,Walker,trained
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_009b (Walker s2),1.62,1,Walker,trained
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_008d_s3 (Walker s3),1.53,1,Walker,trained
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_008d_s4 (Walker s4),4.62,1,Walker,trained
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_059 (Walker s5),4.72,1,Walker,trained
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_048 (Cheetah s0),70.64,1,Cheetah,trained
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_010b (Cheetah s1),8.27,1,Cheetah,trained
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_008f (Walker s0 no_dt_emb),1.02,0,Walker,no_dt_emb
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_009c (Walker s2 no_dt_emb),1.26,0,Walker,no_dt_emb
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_008f_s3 (Walker s3 no_dt_emb),1.2,0,Walker,no_dt_emb
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_008f_s4 (Walker s4 no_dt_emb),1.41,0,Walker,no_dt_emb
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_009c_s3 (Walker s3 no_dt_emb #2),0.52,0,Walker,no_dt_emb
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_042 (Walker s0 frozen),0.194,0,Walker,frozen
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_047 (Walker s1 frozen),1.71,0,Walker,frozen
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_057 (Walker s2 frozen),1.88,0,Walker,frozen
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_046 (Cheetah s0 frozen),1.35,0,Cheetah,frozen
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_058 (Cheetah s1 frozen),0.78,0,Cheetah,frozen
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_024b_s0 (Cheetah s0 no_dt_emb),0.2,0,Cheetah,no_dt_emb
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_024b_s1 (Cheetah s1 no_dt_emb),0.1,0,Cheetah,no_dt_emb
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv:exp_060 (Cartpole baseline),1.0,0,Cartpole,baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "eea58dfb-bc2e-41de-b66e-a51ff43b3999"
}
```

</details>

---


### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 47462,
    "tool_uses": 18,
    "duration_ms": 36072
  },
  "last_tool_name": "Bash",
  "uuid": "39503780-1d07-4683-9515-759622af2764",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01Cn7Vjte9C7dKfN91rbcFcs`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -type f -name \"*registry*\" -o -name \"*experiments*\" 2>/dev/null | grep -E \"\\.(json|csv|yaml|txt)$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "6b5d02da-a7c6-4837-8cc6-74d80bfefd49",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lez6LyNoiyF1fb1Kk9MAEr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1538,
      "cache_read_input_tokens": 45837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1538,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 88 · 2026-05-29T00:36:05.425Z_

<details><summary>↩ Tool result · `toolu_01Cn7Vjte9C7dKfN91rbcFcs`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_kill_exp005_fix_registry_20260513T215230_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_check_both_experiments_progress_20260513T183531_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_kill-overrun-and-close-registry_20260527T172152_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_snapshot_all_experiments_final_20260520_20260520T110322_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_diagnose_recover_failed_experiments_20260518T021421_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_diagnose_stuck-experiments_20260514T220302_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_check-extended-experiments_20260519T131054_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_registry_backfill_082_083_20260525T180757_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_verify-experiments-post-restart_20260527T133711_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_data_registry_nve_step_matched_fix_20260524T085146_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_diagnose_stuck-experiments-urgent_20260514T220552_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_registry_roadmap_cleanup_20260525T180519_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_registry_fix_nve_step_matched_20260524T085046_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_gpu-stack-experiments_20260518T235332_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_check-3-experiments-status_20260519T021343_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_restart-killed-experiments_20260519T021842_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_ops_registry-fix-and-monitor_20260518T161554_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_check_status_and_registry_align_20260523T141209_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_check_all-experiments-health_20260524T233413_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260516T115400/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260516T115400/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260516T115400/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260515T004704/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260515T004704/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260515T004704/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260516T172011/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260516T172011/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260516T172011/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260520T155150/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260520T155150/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260520T155150/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260520T210241/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260520T210241/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260516T133210/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260516T133210/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260516T133210/best/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "14b8928a-71b9-4e94-9a8f-cda6e72beb62"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running wc -l /home/ubuntu/.agent-ml-research-idea_gen_05…",
  "usage": {
    "total_tokens": 49982,
    "tool_uses": 19,
    "duration_ms": 38499
  },
  "last_tool_name": "Bash",
  "uuid": "ba85360c-a449-48e1-9dd5-62d49103c1b2",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_01JVsMTLdQa3qoB4wUTwED6F`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d8dd71ab-5f7c-477b-b897-72f799453f3a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CZkv9TKDni48VkwUkfW2wv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2519,
      "cache_read_input_tokens": 47375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2519,
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

_source line 91 · 2026-05-29T00:36:07.811Z_

<details><summary>↩ Tool result · `toolu_01JVsMTLdQa3qoB4wUTwED6F`</summary>

```text
11382 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ebe6988e-67f9-42c0-ac27-56d58113bb1e"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running grep -A 30 \"exp_id: exp_008d\\|exp_id: exp_008f\\|e…",
  "usage": {
    "total_tokens": 50133,
    "tool_uses": 20,
    "duration_ms": 40935
  },
  "last_tool_name": "Bash",
  "uuid": "28296238-56cc-44e2-b658-1f4fbc2778d9",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01PoBPGXCQZk1pqNC2ub7Sfs`</summary>

```json
{
  "command": "grep -A 30 \"exp_id: exp_008d\\|exp_id: exp_008f\\|exp_id: exp_084\\|exp_id: exp_042\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml | head -150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ea35f637-762b-409e-addf-9e3b55e2f6d1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5iJ5LEwMLxRqLg76FYJjo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 149,
      "cache_read_input_tokens": 49894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 149,
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

_source line 94 · 2026-05-29T00:36:10.243Z_

<details><summary>↩ Tool result · `toolu_01PoBPGXCQZk1pqNC2ub7Sfs`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "2f9f754e-2dd8-4996-85d3-f9b9bfe9b359"
}
```

</details>

---


### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running head -200 /home/ubuntu/.agent-ml-research-idea_ge…",
  "usage": {
    "total_tokens": 50301,
    "tool_uses": 21,
    "duration_ms": 42605
  },
  "last_tool_name": "Bash",
  "uuid": "cb5dd869-1807-458f-ab90-30aa236328a6",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Bash · `toolu_01NLPvyoeKzkk3NV2SKTvdds`</summary>

```json
{
  "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "5bda21d7-f70e-43dd-bba4-4af7e08da25c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0137g5mGiAspfQmskWZMC368",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 50043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 167,
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

_source line 97 · 2026-05-29T00:36:11.915Z_

<details><summary>↩ Tool result · `toolu_01NLPvyoeKzkk3NV2SKTvdds`</summary>

```text
baseline: null
experiments:
  016e:
    completed_at: '2026-05-16T01:39:17.916Z'
    conclusion: killed
    created_at: '2026-05-15T22:21:09.251Z'
    notes: 重复条目，权威数据在 exp_016e_sgs_walker_s1 (DONE/negative)。此条目为 NVE 诊断过程中误创建的冗余记录。
    retry_count: 0
    status: DONE
    updated_at: '2026-05-16T01:39:17.916Z'
  exp_001_baseline:
    completed_at: '2026-05-13T15:23:24.593Z'
    conclusion: success
    created_at: '2026-05-13T02:09:53.875Z'
    extra:
      hook_events:
      - action: agent
        event: on_failed
        ts: '2026-05-13T15:23:25.663340+00:00'
      - action: agent
        event: on_failed
        ts: '2026-05-13T21:47:19.804301+00:00'
      previous_failure:
        conclusion: failed
        metrics:
          eval_return_205K: 907.1
          eval_return_215K: 919.8
          fps: 8.3
          step: 245000
          train_return_244K: 935-976
    failure_reason: 误报：cron 检测到进程退出但实际是正常完成（512K步）。已核实 checkpoint 229MB 有效。
    hypothesis: Vanilla DreamerV3 on Walker Walk converges to stable high-return policy
      (>900) within 500K steps, establishing the performance ceiling for all gated
      variants.
    latest_metrics:
      checked_at: '2026-05-13'
      eta_hours: 1.8
      eval_return: 953.37
      eval_step: 445000
      fps: 7.29
      pid: 9409
      prev_eval_return: 964.96
      process_status: running
      step: 452000
      steps_remaining: 48000
      train_return_latest: 958.07
      train_return_range:
      - 917
      - 985.8
      uptime: 16h35m
    metrics:
      data_source_ve: from training logs metrics.jsonl
      eval_return_last10_mean: 950.9
      eval_return_peak: 970.41
      eval_return_peak_step: 505000
      eval_trajectory:
        105K: 915.67
        115K: 919.81
        125K: 921.37
        135K: 900
        145K: 932.16
        155K: 933.34
        15K: 206.61
        165K: 907.98
        175K: 918.87
        185K: 954.69
        195K: 936.09
        205K: 949.24
        215K: 913.4
        225K: 962.44
        235K: 937.24
        245K: 934.42
        255K: 948.45
        25K: 395.27
        265K: 925.09
        275K: 931.51
        285K: 925.75
        295K: 936.3
        305K: 939.33
        315K: 948.42
        325K: 967.75
        335K: 942.41
        345K: 969.83
        355K: 941.11
        35K: 388.47
        365K: 935.76
        375K: 918.24
        385K: 937.98
        395K: 955.38
        405K: 937.83
        415K: 948.99
        425K: 954.64
        435K: 964.96
        445K: 953.37
        455K: 945.84
        45K: 513.77
        465K: 947.81
        475K: 947.66
        485K: 930.6
        495K: 944.73
        505K: 970.41
        55K: 625.73
        5K: 31.77
        65K: 615.86
        75K: 596.28
        85K: 713.93
        95K: 871.06
      final: true
      step: 512000
      value_eval_ratio_105K: 0.656
      value_eval_ratio_25K: 0.087
      value_eval_ratio_35K: 0.241
      value_eval_ratio_45K: 0.331
      value_eval_ratio_55K: 0.404
      value_eval_ratio_65K: 0.563
      value_eval_ratio_75K: 0.719
      value_eval_ratio_85K: 0.701
      value_eval_ratio_95K: 0.632
      value_eval_ratio_stable: ~69-72% from 135K+
    reproduce:
      finished_at: '2026-05-13T21:47:18.966Z'
    retry_count: 1
    spec:
      command: python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk
        --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device
        cuda:0
      data_count: 500000
      data_path: DMC Walker Walk (dm_control built-in)
      gpu:
      - cuda:0
      gpu_id: 0
      hypothesis: DreamerV3 baseline on DMC Walker Walk for comparison with event-gated
        model
      log_path: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1
      model_name: DreamerV3 (original, gate_enabled=false)
      pid: 9409
      seed: 1
      server: bjb1-45299
    status: DONE
    updated_at: '2026-05-17T02:54:24.099Z'
  exp_001_baseline_s2:
    completed_at: '2026-05-18T21:40:09.329Z'
    conclusion: success
    created_at: '2026-05-18T16:05:17.571Z'
    hypothesis: Walker Walk baseline additional seed for tighter evaluation return
      CI.
    metrics:
      current_step: 112000
      eval_return_105k: 443.46
      target_steps: 105000
      value_mean_105k: 329.16
      ve_ratio_105k: 0.742
    parent: exp_001_baseline
    retry_count: 0
    spec:
      checkpoint_path: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2
      log_path: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2/metrics.jsonl
    status: DONE
    updated_at: '2026-05-18T21:40:09.329Z'
  exp_001_baseline_s2_extended:
    completed_at: '2026-05-19T17:44:27.212Z'
    conclusion: success
    created_at: '2026-05-19T04:10:10.948Z'
    hypothesis: Walker Walk baseline seed=2 extended to 505K. Tests whether low eval
      (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7,
      s3=869.0 at 105K.
    metrics:
      eval_return_at_105K: 443.5
      eval_return_final: 945.7
      eval_return_peak: 962.6
      total_steps: 512000
      value_mean_at_105K: 329.16
      value_mean_plateau: 665
      ve_ratio_at_105K: 0.7422
      ve_ratio_converged_range: 0.69-0.77
    parent: exp_001_baseline_s2
    retry_count: 0
    spec:
      checkpoint_path: logdir/exp_001_baseline_s2/latest.pt
      checkpoint_source: logdir/exp_001_baseline_s2/latest.pt
      command: CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
        MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults
        dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0
        --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2
      data_count: 0
      data_path: logdir/exp_001_baseline_s2
      eval_data: dmc_walker_walk (online eval)
      gpu: cuda:1
      log_path: logdir/exp_001_baseline_s2/train_extended.log
      model_name: dreamerv3
      resumed_from_step: 112000
      seed: 2
      server: bjb1-45299
      target_steps: 505000
      tmux_session: exp_s2_ext
    status: DONE
    updated_at: '2026-05-19T17:44:27.212Z'
  exp_001_baseline_s3:
    completed_at: '2026-05-19T04:08:45.989Z'
    conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "37f5b37f-b05b-48d1-a754-5ca2a402a17c"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running grep \"exp_id: exp_\" /home/ubuntu/.agent-ml-resear…",
  "usage": {
    "total_tokens": 52882,
    "tool_uses": 22,
    "duration_ms": 45388
  },
  "last_tool_name": "Bash",
  "uuid": "0fbdff45-80d5-4ac5-ad5c-624d6b6d2f5c",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_01LosXz9G3Nd4bbtZ5h2CoRy`</summary>

```json
{
  "command": "grep \"exp_id: exp_\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "f4a26653-f025-4735-a203-46d2edf91db0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GehLjP7yaFKhfjws9JNkQj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2579,
      "cache_read_input_tokens": 50210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2579,
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

_source line 100 · 2026-05-29T00:36:14.714Z_

<details><summary>↩ Tool result · `toolu_01LosXz9G3Nd4bbtZ5h2CoRy`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "6051a81b-ec32-4f32-85e5-70b667d7e04c"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running grep -i \"sigma\\|tcn\\|rave\\|sgs\" /home/ubuntu/.age…",
  "usage": {
    "total_tokens": 53032,
    "tool_uses": 23,
    "duration_ms": 47386
  },
  "last_tool_name": "Bash",
  "uuid": "9b7a3a36-42de-433a-9c01-551e3b0c27ff",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 102_

<details open><summary>🔧 Tool call — Bash · `toolu_01DtcK5HFBhCS9y2hxEMeQAk`</summary>

```json
{
  "command": "grep -i \"sigma\\|tcn\\|rave\\|sgs\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "127779fe-e04d-4d4d-95ef-f77483cc85c1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J5skSorCKurQ4Q1ikJKRfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 141,
      "cache_read_input_tokens": 52789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 141,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 103 · 2026-05-29T00:36:16.694Z_

<details><summary>↩ Tool result · `toolu_01DtcK5HFBhCS9y2hxEMeQAk`</summary>

```text
    notes: 重复条目，权威数据在 exp_016e_sgs_walker_s1 (DONE/negative)。此条目为 NVE 诊断过程中误创建的冗余记录。
  exp_016_sgs_walker_s1:
    hypothesis: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample
    log_path: ~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log
    notes: 'Director 调整优先级：017 先于 016。cuda:1 释放后先跑 017，017 完成后再跑 016。SGS 诊断 bug 已修复（models.py
        --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False
        --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False
      log_path: ~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log
  exp_016b_sgs_walker_s1:
    hypothesis: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample
      梯度通路（plan_016, 论文 method section 核心）。重跑 016_sgs，修复 EGL device mismatch（+MUJOCO_EGL_DEVICE_ID=1）
    log_path: ~/runs/event-gated-adaptive-horizon/exp_016b_sgs_walker_s1.log
        dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1
        dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1
      model_name: DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)
      note: Rerun of 016_sgs with EGL fix (MUJOCO_EGL_DEVICE_ID=1). Original 016 failed
        due to EGL device mismatch, not SGS code issue.
  exp_016c_sgs_walker_s1:
    hypothesis: Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed
        dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1
      model_name: DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)
  exp_016d_sgs_walker_s1:
        dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1
      model_name: dreamerv3-sgs
  exp_016e_sgs_walker_s1:
    checkpoint_path: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/latest.pt
    hypothesis: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample
    log_path: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/
      data_source: metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K
          interpretation: SGS preserves ~1.0-1.3 nats higher entropy through 35-55K,
      sgs_verdict: SGS delays CIVO onset ~50K steps by preserving entropy, yields
    notes: 'logdir 路径修正：实际数据在 logdir/exp_016e_sgs_walker_s1（非 spec 中的 exp_016d）。SGS
      **⚠️ 关键发现（Full-SGS 梯度验证）：reward loss 对 dt_emb.weight 的梯度贡献为 0。016e 的 reward_dt_emb_detach
      height=0.76, cont=0.27）。016e 与 008d 的差异（onset 延迟、更高峰值）应归因于随机变异或其他实验条件差异，不是 SGS
      Full-SGS（detach 所有 non-KL head 梯度）移除 93% dt_emb 梯度（1.624→0.119），是真正的测试。'
        dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016e_sgs_walker_s1
      logdir: logdir/exp_016e_sgs_walker_s1
      model_name: dreamerv3-sgs
  exp_018_full_sgs_s2:
    checkpoint_path: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_s2/checkpoint.pt
    hypothesis: Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives
      without collapse, SGS is a robust intervention mechanism for deployment.
    log_path: ~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log
      1.66× at 95K (35K+ window). Full-SGS did NOT prevent collapse in seed 2 — contradicts
      018v2 (seed 1) which avoided collapse. This invalidates SGS_full as a reliable
      sustained. n=2 for SGS_full now shows collapse_rate=0.5.'
    parent: exp_018v2_full_sgs_walker_s1
        2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every
        25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2"
        2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "67850346-b373-4904-8a04-71631bd7ddf4"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running grep -E \"exp_id:\\s+\" /home/ubuntu/.agent-ml-resea…",
  "usage": {
    "total_tokens": 54853,
    "tool_uses": 24,
    "duration_ms": 50040
  },
  "last_tool_name": "Bash",
  "uuid": "389dbdde-f846-467a-9387-8625b37263b1",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nh9S1aDjm3FZF7wdrd7GFH`</summary>

```json
{
  "command": "grep -E \"exp_id:\\s+\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml | sed 's/.*exp_id: //' | sort | uniq | grep -E \"0[0-9]{2}\" | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "49fe4714-8029-4c40-9e39-071523dac39b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014DurrTViLqiV7Gp5NvBdN2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1815,
      "cache_read_input_tokens": 52930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1815,
        "ephemeral_1h_input_tokens": 0
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

_source line 106 · 2026-05-29T00:36:19.363Z_

<details><summary>↩ Tool result · `toolu_01Nh9S1aDjm3FZF7wdrd7GFH`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "617e260d-cc91-409c-9dbe-ce620b5ef0bf"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running grep \"^  exp_\" /home/ubuntu/.agent-ml-research-id…",
  "usage": {
    "total_tokens": 55019,
    "tool_uses": 25,
    "duration_ms": 52199
  },
  "last_tool_name": "Bash",
  "uuid": "f57c32e0-ee71-4249-8c0e-72b44df443d7",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 108_

<details open><summary>🔧 Tool call — Bash · `toolu_01LX1CrwAznwgKz7B3TJXoKH`</summary>

```json
{
  "command": "grep \"^  exp_\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml | sed 's/:$//' | sed 's/^  //' | sort | head -120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d80a2075-2817-4337-b941-dffa0707beaa",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016GqHv12UYzFeF4SJaASDEr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 54745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 164,
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

_source line 109 · 2026-05-29T00:36:21.517Z_

<details><summary>↩ Tool result · `toolu_01LX1CrwAznwgKz7B3TJXoKH`</summary>

```text
exp_001_baseline
exp_001_baseline_s2
exp_001_baseline_s2_extended
exp_001_baseline_s3
exp_001_baseline_s3_extended
exp_001_baseline_s4
exp_001_baseline_s4_extended
exp_002_event_gated
exp_003_event_gated_v2
exp_004_event_gated_v3
exp_005_event_gated_v4
exp_006
exp_006_fixed_dt2
exp_007_fixed_dt4
exp_008a
exp_008a_cheetah_unexposed_s0
exp_008a_cheetah_unexposed_s1
exp_008a_no_subsample_dt2
exp_008a_unexposed_s1
exp_008a_unexposed_s2
exp_008a_untrained_s1
exp_008a_untrained_s2
exp_008c
exp_008c_no_subsample_dt2_h8
exp_008d
exp_008d_civo_trigger_s2
exp_008d_civo_trigger_s3
exp_008d_civo_trigger_s4
exp_008d_subsample_on_h8
exp_008e_subsample_on_dt1_h15
exp_008e_subsample_on_fixed_dt1
exp_008e_v2_subsample_on_dt1_h15
exp_008e_v3_s3
exp_008e_v3_s4
exp_008e_v3_subsample_on_dt1_h15
exp_008e_v3_walker_s1
exp_008e_v3_walker_s2
exp_008f_no_dt_embed_subsample_on_h8
exp_008f_s2
exp_008f_s3_no_dt_embed_walker
exp_008f_s4
exp_009a_baseline_walker_s2
exp_009b_008d_walker_s2
exp_009c_008f_walker_s2
exp_009c_s2
exp_009c_s3
exp_009d_baseline_walker_s0
exp_009d_baseline_walker_s1
exp_009e_008d_walker_s1
exp_009f_008f_walker_s1
exp_009g_008f_walker_s0
exp_009h_008f_walker_s0
exp_010a_cheetah_baseline_s1
exp_010b_cheetah_civo_trigger
exp_010b_cheetah_civo_trigger_s0
exp_015b_frozen_dt_emb
exp_016_sgs_walker_s1
exp_016b_sgs_walker_s1
exp_016c_sgs_walker_s1
exp_016d_sgs_walker_s1
exp_016e_sgs_walker_s1
exp_017_subsample_off_trained_dt_emb
exp_018_full_sgs_s2
exp_018_full_sgs_walker_s1
exp_018v2_full_sgs_walker_s1
exp_019a_pickcube_baseline
exp_019a_v2_pickcube_baseline
exp_019b_pickcube_civo_trigger
exp_020_vanilla_dreamerv3_s2
exp_021_full_sgs_cheetah_s1
exp_022_untrained_dt_emb_learned_gate
exp_022b_no_curriculum
exp_023_cheetah_baseline_s2
exp_023_cheetah_baseline_s3
exp_023_cheetah_baseline_s4
exp_023_cheetah_baseline_s4_extended
exp_023a_cheetah_baseline_s0
exp_023b_cheetah_baseline_s1
exp_024_cheetah_no_dt_emb_s0
exp_024b_cheetah_no_dt_emb_s0
exp_024b_cheetah_no_dt_emb_s1
exp_025_obs_sgs_walker_s1
exp_025_obs_sgs_walker_s2
exp_025_obs_sgs_walker_s3
exp_025_obs_sgs_walker_s4
exp_026_obs_sgs_cheetah_s0
exp_026_obs_sgs_cheetah_s1
exp_027_tcn_walker_s0
exp_027_tcn_walker_s0_sigma02
exp_027_tcn_walker_s1
exp_028_rave_walker_s0
exp_028_rave_walker_s0_ceil15
exp_029a_tcn_walker_s1_sigma02
exp_029b_tcn_walker_s2_sigma02
exp_029c_tcn_walker_s0_sigma01
exp_029d_tcn_walker_s3_sigma02
exp_030a_tcn_cheetah_s0_sigma02
exp_030b_tcn_cheetah_s0_sigma05
exp_030c_tcn_cheetah_s0_sigma10
exp_031_tcn_pickcube_s0_sigma02
exp_031b_tcn_pickcube_s0_sigma05
exp_032_dual_critic_walker
exp_032b_dual_critic_walker_s1
exp_033_wide_critic_walker
exp_034
exp_034_dual_critic_cheetah
exp_035_narrow_dual_critic_walker
exp_036_dual_critic_pickcube
exp_037_wide_critic_cheetah
exp_038_dual_critic_walker_s2
exp_039_narrow_dual_critic_walker_s1
exp_040_wide_dual_critic_cheetah
exp_041_dual_critic_walker_s3
exp_042_frozen_dt_emb_walker
exp_043_008f_walker_s1
exp_044_gradient_stop_walker
exp_045_treatment_extension_008d_s3
exp_046_frozen_dt_emb_cheetah
exp_047_frozen_dt_emb_walker_s1
exp_048_cheetah_civo_extension
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "7f07e2f9-d309-4579-9a1f-0b3e0b63afa8"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running grep -A 50 \"exp_027.*tcn\\|exp_028.*rave\\|exp_029.…",
  "usage": {
    "total_tokens": 56715,
    "tool_uses": 26,
    "duration_ms": 55690
  },
  "last_tool_name": "Bash",
  "uuid": "09473396-9b8a-40cd-96d5-00a941b842cd",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 111_

<details open><summary>🔧 Tool call — Bash · `toolu_01CiRi69hhfi3rYtLzMmhGRu`</summary>

```json
{
  "command": "grep -A 50 \"exp_027.*tcn\\|exp_028.*rave\\|exp_029.*tcn\\|exp_030.*tcn\\|exp_031.*tcn\\|exp_032.*dual\\|exp_033.*wide\\|exp_035.*narrow\\|exp_042.*frozen\\|exp_084.*frozen\\|exp_087.*frozen\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml | grep -E \"(exp_id:|hypothesis:|eval_return|metrics:|conclusion:)\" | head -150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "141bc5f5-cfff-4195-8596-c0dc6b1e342f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011wix2sfSKvDYoyTQN7tHDX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 54909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 112 · 2026-05-29T00:36:25.017Z_

<details><summary>↩ Tool result · `toolu_01CiRi69hhfi3rYtLzMmhGRu`</summary>

```text
    conclusion: negative
    hypothesis: 'Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5)
    metrics:
      eval_return_105K: 95.5
      eval_return_112K: 99.5
      eval_return_15K: 154.6
      eval_return_25K: 223.6
      eval_return_35K: 240
      eval_return_45K: 101.2
      eval_return_55K: 70
      eval_return_5K: 37.4
      eval_return_65K: 95.1
      eval_return_75K: 189.2
      eval_return_85K: 36
      eval_return_95K: 166.4
    conclusion: success
    hypothesis: 'TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding
    metrics:
      eval_return_105K: 236.4
      eval_return_115K: 543.8
      eval_return_125K: 458.4
      eval_return_135K: 496.7
      eval_return_145K: 542.7
      eval_return_155K: 660.5
      eval_return_15K: 150.6
      eval_return_165K: 653.3
      eval_return_175K: 821.1
      eval_return_185K: 560.5
      eval_return_195K: 567.9
      eval_return_205K: 558.7
      eval_return_215K: 551
      eval_return_25K: 199.4
      eval_return_35K: 278.2
      eval_return_45K: 315.6
      eval_return_55K: 278.6
      eval_return_5K: 35.6
      eval_return_65K: 331
      eval_return_75K: 293.1
      eval_return_85K: 363.9
      eval_return_95K: 171.4
    conclusion: negative
    hypothesis: 'TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different
    metrics:
      eval_return:
    conclusion: negative
    hypothesis: 'Reality-Anchored Value Estimation (RAVE): cap imagination critic
    metrics:
          eval_return: 29
          eval_return: 105.3
          eval_return: 191.9
          eval_return: 204.6
          eval_return: 197.7
          eval_return: 193
          eval_return: 37.4
          eval_return: 79.8
          eval_return: 44.5
          eval_return: 57.7
          eval_return: 25.9
    conclusion: negative
    hypothesis: 'RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value
    metrics:
      eval_return_105K: 76.2
      eval_return_115K: 41.2
      eval_return_125K: 36.6
      eval_return_135K: 39.1
      eval_return_15K: 99.4
      eval_return_25K: 155.3
      eval_return_35K: 180.1
      eval_return_45K: 166.9
      eval_return_55K: 131
      eval_return_5K: 31.6
      eval_return_65K: 91.5
      eval_return_75K: 120.9
      eval_return_85K: 137.3
      eval_return_95K: 70.2
    conclusion: success
    hypothesis: 'TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02
    metrics:
      eval_return_105K: 319.4
      eval_return_115K: 345.5
      eval_return_125K: 401
      eval_return_135K: 307.8
      eval_return_145K: 380.8
      eval_return_155K: 307.3
      eval_return_15K: 137.7
      eval_return_165K: 320.3
      eval_return_175K: 159
      eval_return_185K: 278.2
      eval_return_195K: 301.2
      eval_return_205K: 204.6
      eval_return_215K: 161.3
      eval_return_25K: 180.9
      eval_return_35K: 124
      eval_return_45K: 124.2
      eval_return_55K: 133.9
      eval_return_5K: 36.7
      eval_return_65K: 169.7
      eval_return_75K: 171.2
      eval_return_85K: 151.8
      eval_return_95K: 180.3
    conclusion: negative
    hypothesis: 'TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%.
    metrics:
      eval_return_105K: 31.97
      eval_return_115K: 35.45
      eval_return_125K: 33.04
      eval_return_135K: 42.47
      eval_return_145K: 51.66
      eval_return_155K: 56.5
      eval_return_15K: 168.41
      eval_return_165K: 44.9
      eval_return_25K: 159.56
      eval_return_35K: 168.05
      eval_return_45K: 171.51
      eval_return_55K: 177.67
      eval_return_5K: 30.46
      eval_return_65K: 106.57
      eval_return_75K: 64.01
      eval_return_85K: 62.82
      eval_return_95K: 44.66
    conclusion: negative
    hypothesis: 'σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2
    metrics:
      eval_return_105K: 204.7
      eval_return_115K: 296.4
      eval_return_125K: 232.3
      eval_return_135K: 247.4
      eval_return_145K: 323.1
      eval_return_155K: 359.7
      eval_return_15K: 99.1
      eval_return_165K: 490.7
      eval_return_175K: 246.2
      eval_return_185K: 220.6
      eval_return_195K: 212.8
      eval_return_205K: 256.9
      eval_return_215K: 328.3
      eval_return_25K: 140.7
      eval_return_35K: 155.7
      eval_return_45K: 160.9
      eval_return_55K: 254.8
      eval_return_5K: 35.6
      eval_return_65K: 268.7
      eval_return_75K: 295.5
      eval_return_85K: 220.8
      eval_return_95K: 188.6
    conclusion: negative
    hypothesis: 'Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443,
    metrics:
      eval_return_105K: 71.8
      eval_return_115K: 69.8
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "2dbcb2f7-8aed-4cac-870d-f3d6e67ddb09"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running for exp in \"exp_027\" \"exp_028\" \"exp_029\" \"exp_030…",
  "usage": {
    "total_tokens": 58857,
    "tool_uses": 27,
    "duration_ms": 59510
  },
  "last_tool_name": "Bash",
  "uuid": "18a41cc7-dd50-47fd-adfb-b2539f238aec",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 114_

<details open><summary>🔧 Tool call — Bash · `toolu_01ThucP7Hiz1NMNWWmAaaUxY`</summary>

```json
{
  "command": "for exp in \"exp_027\" \"exp_028\" \"exp_029\" \"exp_030\" \"exp_031\" \"exp_032\" \"exp_033\" \"exp_034\" \"exp_035\" \"exp_036\" \"exp_037\" \"exp_038\" \"exp_040\" \"exp_041\" \"exp_042\" \"exp_084\" \"exp_087\"; do\n  echo \"=== $exp ===\"\n  grep -A 30 \"^  $exp\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml | grep -E \"hypothesis:|conclusion:|eval_return.*105|eval_return.*final|eval_return_peak\" | head -5\ndone 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "0ca7c7b0-8fad-4bed-a577-59b6cf76a110",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EzM1s69BqPYSmRQR9bbaBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2140,
      "cache_read_input_tokens": 56597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2140,
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

_source line 115 · 2026-05-29T00:36:28.945Z_

<details><summary>↩ Tool result · `toolu_01ThucP7Hiz1NMNWWmAaaUxY`</summary>

```text
=== exp_027 ===
    conclusion: negative
    hypothesis: 'Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5)
      eval_return_105K: 95.5
    conclusion: success
    hypothesis: 'TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding
=== exp_028 ===
    conclusion: negative
    hypothesis: 'Reality-Anchored Value Estimation (RAVE): cap imagination critic
          eval_return: 105.3
    conclusion: negative
    hypothesis: 'RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value
=== exp_029 ===
    conclusion: success
    hypothesis: 'TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02
      eval_return_105K: 319.4
    conclusion: negative
    hypothesis: 'TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%.
=== exp_030 ===
    conclusion: negative
    hypothesis: 'TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether
    conclusion: negative
    hypothesis: Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the
      eval_return_105K: 104.4
=== exp_031 ===
    conclusion: negative
    hypothesis: TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination
    conclusion: negative
    hypothesis: 'PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed
=== exp_032 ===
    conclusion: success
    hypothesis: Dual-critic (min of two independent critics for actor loss) will suppress
    conclusion: success
    hypothesis: 'Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and
=== exp_033 ===
    conclusion: success
    hypothesis: 'Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic)
=== exp_034 ===
    conclusion: negative
    hypothesis: Dual-critic (min of two independent critics) will prevent CIVO in
    conclusion: negative
    hypothesis: 'Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on
=== exp_035 ===
    conclusion: success
    hypothesis: 'Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline
=== exp_036 ===
    conclusion: negative
    hypothesis: 'Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube.
      eval_return_final: 27.7
      eval_return_peak: 27.7
=== exp_037 ===
    conclusion: negative
    hypothesis: 'Wide single critic on Cheetah: if capacity=recovery generalizes from
      eval_return_final: 146.1
      eval_return_peak: 350.1
=== exp_038 ===
    conclusion: negative
    hypothesis: Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7)
      eval_return_final: 120.9
      eval_return_peak: 354
      eval_return_peak_step: 155000
=== exp_040 ===
    hypothesis: Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上
=== exp_041 ===
    hypothesis: D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse
=== exp_042 ===
    hypothesis: dt_embedding training (not its mere existence) is a necessary condition
=== exp_084 ===
    hypothesis: Frozen dt_embedding (requires_grad=False, random init) with subsample
=== exp_087 ===
    hypothesis: Frozen dt_embedding (requires_grad=False, random init) with subsample
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "3df6372c-374f-4483-9c3b-da333a1b4c1e"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading artifacts/figures_data/summary_table.csv",
  "usage": {
    "total_tokens": 60213,
    "tool_uses": 28,
    "duration_ms": 62540
  },
  "last_tool_name": "Read",
  "uuid": "0d8e53f4-5700-4af5-a6e6-89947b4b248e",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Read · `toolu_01W1cR9rsBt9HY2JpUTpoyRx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures_data/summary_table.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "fefc16e5-b6f4-4178-b2ab-dbb4388c7cef",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HWFpCkcw8cVxdRCuVkiVnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 58737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1354,
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

_source line 118 · 2026-05-29T00:36:31.805Z_

<details><summary>↩ Tool result · `toolu_01W1cR9rsBt9HY2JpUTpoyRx`</summary>

```text
1	exp_id,config_label,hypothesis,conclusion,final_eval_return,peak_eval_return,final_ve_ratio,final_nve,vs_baseline_pct,seed,total_steps
2	exp_001_baseline,baseline (seed 0),DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model,success,970.41,970.41,0.656,1.0,0.0,1,512000
3	exp_009a_baseline_walker_s2,baseline (seed 2),Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）,,948.4,966.9,,,-0.52,2,448000
4	exp_006_fixed_dt2,dt=2 fixed (006),诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。,negative,132.86,485.3,2.722,4.8348,-78.42,1,65000
5	exp_007_fixed_dt4,dt=4 fixed (007),诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。,negative,152.49,176.9,0.061,0.151,-75.63,1,55000
6	exp_005_event_gated_v4,learned gate (005),,negative,98.84,541.18,,,-89.40,1,145000
7	exp_008d_subsample_on_h8,trained dt_emb H=8 (008d) seed 0/1,,negative,82.75,167.22,1.666,4.1238,-86.78,1,55000
8	exp_009b_008d_walker_s2,trained dt_emb H=8 (008d) seed 2,Walker Walk trained dt_emb + subsample ON + H=8 seed 2 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）,negative,267.93,278.54,0.251,0.38,-70.74,2,105000
9	exp_008f_no_dt_embed_subsample_on_h8,no dt_emb (008f) seed 0/1,"C2 confound control：隔离 dt_embedding conditioning vs RSSM learned dt=2 dynamics。subsample ON + dt=2 imagination + H=8（与 008d 完全一致），但 gate_dt_embed_dim=0（去掉 dt_embedding 条件输入）。如果 008f 崩塌（v/e >50%）→ 根因是 RSSM 的 dt=2 训练数据导致 dynamics 偏差，不是 dt_embedding per se。如果 008f 稳定（v/e <35%）→ 确认 dt_embedding conditioning 是 delusional critic 的直接原因。对照：008d（dt_embed_dim>0, v/e 15.5%→41.2%→69.3% 崩塌）vs 008c（subsample OFF, untrained dt_emb, v/e 稳定 ~22-33%）。",success,503,503,0.1952,0.3,-45.08,1,105000
10	exp_009c_008f_walker_s2,no dt_emb (008f) seed 2,Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）,negative,148.34,359.14,0.75,1.14,-83.80,2,105000
11	exp_008c_no_subsample_dt2_h8,untrained dt_emb dt=2 H=8 (008c),隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。,negative,240.86,241.87,0.328,0.5826,-60.89,1,68000
12	exp_008a_no_subsample_dt2,untrained dt_emb dt=2 H=15 (008a),隔离 subsample 效应：subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。,success,777.66,777.66,0.386,0.59,-15.07,1,112000
13	exp_008e_v3_walker_s1,dt=1 imag (008e_v3) seed 1,Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）,success,869.9,869.9,0.527,0.8034,-5.00,1,112000
14	exp_008e_v3_walker_s2,dt=1 imag (008e_v3) seed 2,Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证,,435.1,435.1,0.507,0.9005,-29.36,2,68000
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "2af2f730-5af6-4015-a6c5-92c0c2446023"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 62172,
    "tool_uses": 29,
    "duration_ms": 65970
  },
  "last_tool_name": "Bash",
  "uuid": "be58f43c-ca2c-40fe-b7c9-1452ca883622",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 120_

<details open><summary>🔧 Tool call — Bash · `toolu_01KXRzK93dRLduLRYrbiTHSm`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -name \"*intervention*\" -o -name \"*ablation*\" -o -name \"*treatment*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "9c623d5e-e0e0-4c07-98bc-86b4cd3cf38e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014JBMa4Nui3Sd4A9hxceH9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1949,
      "cache_read_input_tokens": 60091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1949,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 121 · 2026-05-29T00:36:35.308Z_

<details><summary>↩ Tool result · `toolu_01KXRzK93dRLduLRYrbiTHSm`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_cheetah_tcn_and_ablation_configs_20260520T082823_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_ablation-latex-table_20260524T232728.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_deploy_exp_045_treatment_extension_20260522T094126.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_cheetah_tcn_and_ablation_configs_20260520T082823.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_ablation-latex-table_20260524T232728_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_deploy_exp_045_treatment_extension_20260522T094126_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_deploy_exp_045_treatment_extension_20260522T094126.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_deploy_exp_045_treatment_extension_20260522T094126.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/checkpoints/exp_045_treatment_extension_008d_s3_RUNNING_20260522T154128.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/checkpoints/exp_045_treatment_extension_008d_s3_DONE_20260522T154143.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/ablation_mechanism_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/tables/ablation_mechanism_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/ablation_commands.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a1565490-dc69-403a-a37d-d9d4b5960c72"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running cat /home/ubuntu/.agent-ml-research-idea_gen_0509…",
  "usage": {
    "total_tokens": 63031,
    "tool_uses": 30,
    "duration_ms": 68739
  },
  "last_tool_name": "Bash",
  "uuid": "56323e85-e486-4ea3-b74e-be5377a77922",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 123_

<details open><summary>🔧 Tool call — Bash · `toolu_01QcL1aF7WP4To1Hrec7Kv8o`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_code_ablation-latex-table_20260524T232728_result.json | head -200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "b2913fed-34f9-46c5-8fed-2e506450b16e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018X6mZcYpz5bierQUk3qcKV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 62040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 857,
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

_source line 124 · 2026-05-29T00:36:38.066Z_

<details><summary>↩ Tool result · `toolu_01QcL1aF7WP4To1Hrec7Kv8o`</summary>

```text
{
  "raw": "两个 LaTeX 表格已生成并注册：\n\n**Table A** (`ablation_mechanism_table.tex`) — CIVO 机制证据汇总，7 行数据：\n- dt_emb cosine: trained $-0.94{\\sim}-0.70$ vs frozen $-0.15{\\sim}+0.07$ (exp_065)\n- RSSM fidelity: reward MAE gap $2.695\\times$ vs baseline $1.483\\times$ (exp_063)\n- Value calibration: V/MC median $3.40$ vs control $1.05$ (exp_064)\n- NVE: AUROC $0.961$, F1@1.5x $= 0.880$\n\n**Table B** (`temporal_causality_table.tex`) — 时序因果关系：\n- Return crash 60-80K → entropy rise 95K+，lag 15-35K steps\n- Entropy drift rate $1.14{-}2.11$ nats/10K (collapsed) vs $0.07{-}0.22$ (healthy)，$10{-}20\\times$ 差异\n\n每个数字均在 footnote 中标注了来源实验 ID。Paper Agent 可直接 `\\input{tables/ablation_mechanism_table.tex}` 引用。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "6d9295cb-9345-4580-84f6-92b492f1a85a"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running python3 << 'PYEOF'\nimport yaml\nimport json\n\nwith open…",
  "usage": {
    "total_tokens": 63528,
    "tool_uses": 31,
    "duration_ms": 74784
  },
  "last_tool_name": "Bash",
  "uuid": "481a4d68-9534-4dc0-9f27-48a811d8535e",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 126_

<details open><summary>🔧 Tool call — Bash · `toolu_01QvgiLL7QUzkfNvaVZeQM3E`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\nimport json\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\n# Target experiments\ntargets = ['exp_027_tcn_walker_s0', 'exp_027_tcn_walker_s0_sigma02', 'exp_028_rave_walker_s0',\n           'exp_029a_tcn_walker_s1_sigma02', 'exp_029b_tcn_walker_s2_sigma02', 'exp_029c_tcn_walker_s0_sigma01',\n           'exp_030a_tcn_cheetah_s0_sigma02', 'exp_030b_tcn_cheetah_s0_sigma05', 'exp_030c_tcn_cheetah_s0_sigma10',\n           'exp_031_tcn_pickcube_s0_sigma02', 'exp_031b_tcn_pickcube_s0_sigma05',\n           'exp_032_dual_critic_walker', 'exp_032b_dual_critic_walker_s1',\n           'exp_033_wide_critic_walker', 'exp_034_dual_critic_cheetah',\n           'exp_035_narrow_dual_critic_walker', 'exp_036_dual_critic_pickcube',\n           'exp_037_wide_critic_cheetah', 'exp_038_dual_critic_walker_s2', 'exp_040_wide_dual_critic_cheetah',\n           'exp_041_dual_critic_walker_s3', 'exp_042_frozen_dt_emb_walker',\n           'exp_084_frozen_walker_s1', 'exp_087_frozen_cheetah_s1']\n\nfor exp_id in targets:\n    if exp_id in registry.get('experiments', {}):\n        exp = registry['experiments'][exp_id]\n        metrics = exp.get('metrics', {})\n        eval_final = metrics.get('eval_return_final') or metrics.get('final')\n        eval_105k = metrics.get('eval_return_105K') or metrics.get('eval_return_105k')\n        eval_peak = metrics.get('eval_return_peak') or metrics.get('peak')\n        conclusion = exp.get('conclusion', 'unknown')\n        print(f\"{exp_id:45s} | Final: {str(eval_final):10s} | 105K: {str(eval_105k):10s} | Peak: {str(eval_peak):10s} | {conclusion}\")\nPYEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a790aca9-1038-439d-9e1d-1a6f0260cd9d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01766RtcEqgoHBrWvrN53eeP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 62897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
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

_source line 127 · 2026-05-29T00:36:44.849Z_

<details><summary>↩ Tool result · `toolu_01QvgiLL7QUzkfNvaVZeQM3E`</summary>

```text
exp_027_tcn_walker_s0                         | Final: None       | 105K: 95.5       | Peak: None       | negative
exp_027_tcn_walker_s0_sigma02                 | Final: None       | 105K: 236.4      | Peak: None       | success
exp_028_rave_walker_s0                        | Final: None       | 105K: None       | Peak: None       | negative
exp_029a_tcn_walker_s1_sigma02                | Final: None       | 105K: 319.4      | Peak: None       | success
exp_029b_tcn_walker_s2_sigma02                | Final: None       | 105K: 31.97      | Peak: None       | negative
exp_029c_tcn_walker_s0_sigma01                | Final: None       | 105K: 204.7      | Peak: None       | negative
exp_030a_tcn_cheetah_s0_sigma02               | Final: None       | 105K: None       | Peak: None       | negative
exp_030b_tcn_cheetah_s0_sigma05               | Final: None       | 105K: 104.4      | Peak: None       | negative
exp_030c_tcn_cheetah_s0_sigma10               | Final: None       | 105K: 122.5      | Peak: None       | negative
exp_031_tcn_pickcube_s0_sigma02               | Final: None       | 105K: None       | Peak: None       | negative
exp_031b_tcn_pickcube_s0_sigma05              | Final: None       | 105K: None       | Peak: None       | negative
exp_032_dual_critic_walker                    | Final: None       | 105K: None       | Peak: None       | success
exp_032b_dual_critic_walker_s1                | Final: None       | 105K: None       | Peak: None       | success
exp_033_wide_critic_walker                    | Final: None       | 105K: None       | Peak: None       | success
exp_034_dual_critic_cheetah                   | Final: None       | 105K: None       | Peak: None       | negative
exp_035_narrow_dual_critic_walker             | Final: None       | 105K: None       | Peak: None       | success
exp_036_dual_critic_pickcube                  | Final: 27.7       | 105K: None       | Peak: 27.7       | negative
exp_037_wide_critic_cheetah                   | Final: 146.1      | 105K: None       | Peak: 350.1      | negative
exp_038_dual_critic_walker_s2                 | Final: 120.9      | 105K: None       | Peak: 354        | negative
exp_040_wide_dual_critic_cheetah              | Final: None       | 105K: None       | Peak: None       | success
exp_041_dual_critic_walker_s3                 | Final: 544        | 105K: None       | Peak: 761.1      | success
exp_042_frozen_dt_emb_walker                  | Final: None       | 105K: None       | Peak: None       | success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "05717855-0b17-4bbd-9e02-a740bdc90b6f"
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
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubu…",
  "usage": {
    "total_tokens": 65092,
    "tool_uses": 32,
    "duration_ms": 84868
  },
  "last_tool_name": "Bash",
  "uuid": "4b7001d9-eeff-4165-ae35-5872db90a256",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 129_

<details open><summary>🔧 Tool call — Bash · `toolu_01DzzNeQJ2kiS1gxrLWap8Kh`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\n# Key intervention experiments by category\nexperiments = {\n    \"TCN (Temporal Conditioning Noise)\": [\n        ('exp_027_tcn_walker_s0', 'σ=0.5, Walker'),\n        ('exp_027_tcn_walker_s0_sigma02', 'σ=0.2, Walker'),\n        ('exp_029c_tcn_walker_s0_sigma01', 'σ=0.1, Walker s0'),\n        ('exp_029a_tcn_walker_s1_sigma02', 'σ=0.2, Walker s1'),\n        ('exp_029b_tcn_walker_s2_sigma02', 'σ=0.2, Walker s2'),\n        ('exp_030a_tcn_cheetah_s0_sigma02', 'σ=0.2, Cheetah'),\n        ('exp_030b_tcn_cheetah_s0_sigma05', 'σ=0.5, Cheetah'),\n        ('exp_030c_tcn_cheetah_s0_sigma10', 'σ=1.0, Cheetah'),\n    ],\n    \"RAVE (Reality-Anchored Value Estimation)\": [\n        ('exp_028_rave_walker_s0', 'RAVE Walker'),\n    ],\n    \"Dual Critic\": [\n        ('exp_032_dual_critic_walker', 'Dual Critic Walker s0'),\n        ('exp_032b_dual_critic_walker_s1', 'Dual Critic Walker s1'),\n        ('exp_034_dual_critic_cheetah', 'Dual Critic Cheetah'),\n        ('exp_038_dual_critic_walker_s2', 'Dual Critic Walker s2'),\n        ('exp_041_dual_critic_walker_s3', 'Dual Critic Walker s3'),\n    ],\n    \"Wide Critic\": [\n        ('exp_033_wide_critic_walker', 'Wide Single Critic Walker'),\n        ('exp_037_wide_critic_cheetah', 'Wide Single Critic Cheetah'),\n    ],\n    \"Narrow Critic\": [\n        ('exp_035_narrow_dual_critic_walker', 'Narrow Dual Critic Walker'),\n    ],\n    \"Frozen/Removed Embedding\": [\n        ('exp_042_frozen_dt_emb_walker', 'Frozen dt_emb Walker'),\n        ('exp_084_frozen_walker_s1', 'Frozen Walker s1'),\n        ('exp_087_frozen_cheetah_s1', 'Frozen Cheetah s1'),\n    ],\n    \"Untreated Baseline (008d)\": [\n        ('exp_008d', '008d Baseline seed 0'),\n        ('exp_009b_008d_walker_s2', '008d Baseline seed 2'),\n    ]\n}\n\nprint(\"INTERVENTION EXPERIMENT RESULTS SUMMARY\")\nprint(\"=\" * 100)\n\nfor category, exps in experiments.items():\n    print(f\"\\n{category}\")\n    print(\"-\" * 100)\n    \n    for exp_id, label in exps:\n        if exp_id in registry.get('experiments', {}):\n            exp = registry['experiments'][exp_id]\n            metrics = exp.get('metrics', {})\n            \n            # Get eval return values\n            eval_traj = metrics.get('eval_trajectory', {})\n            eval_105k = metrics.get('eval_return_105K') or metrics.get('eval_return_105k') or eval_traj.get('105K')\n            eval_peak = metrics.get('eval_return_peak')\n            eval_final = metrics.get('final') or eval_traj.get('final')\n            \n            conclusion = exp.get('conclusion', 'unknown')\n            hypothesis = exp.get('hypothesis', '')[:80]\n            \n            print(f\"  {exp_id:40s} | {label:40s}\")\n            print(f\"    105K: {str(eval_105k):10s} | Peak: {str(eval_peak):10s} | Conclusion: {conclusion}\")\n            if eval_traj:\n                steps = sorted([int(k) for k in eval_traj.keys() if k.isdigit()])\n                if steps:\n                    print(f\"    Trajectory (sample): {', '.join(f'{s}K: {eval_traj[str(s)]:.1f}' for s in steps[-5:])}\")\nPYEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "5d32533a-5478-4e59-84fa-03baadeb89bf",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017keJMFAZHSKxFDDiVDK3yv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1556,
      "cache_read_input_tokens": 63392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1556,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 130 · 2026-05-29T00:36:55.099Z_

<details><summary>↩ Tool result · reported error · `toolu_01DzzNeQJ2kiS1gxrLWap8Kh`</summary>

```text
Exit code 1
INTERVENTION EXPERIMENT RESULTS SUMMARY
====================================================================================================

TCN (Temporal Conditioning Noise)
----------------------------------------------------------------------------------------------------
  exp_027_tcn_walker_s0                    | σ=0.5, Walker                           
    105K: 95.5       | Peak: None       | Conclusion: negative
  exp_027_tcn_walker_s0_sigma02            | σ=0.2, Walker                           
    105K: 236.4      | Peak: None       | Conclusion: success
  exp_029c_tcn_walker_s0_sigma01           | σ=0.1, Walker s0                        
    105K: 204.7      | Peak: None       | Conclusion: negative
  exp_029a_tcn_walker_s1_sigma02           | σ=0.2, Walker s1                        
    105K: 319.4      | Peak: None       | Conclusion: success
  exp_029b_tcn_walker_s2_sigma02           | σ=0.2, Walker s2                        
    105K: 31.97      | Peak: None       | Conclusion: negative
  exp_030a_tcn_cheetah_s0_sigma02          | σ=0.2, Cheetah                          
    105K: None       | Peak: None       | Conclusion: negative
  exp_030b_tcn_cheetah_s0_sigma05          | σ=0.5, Cheetah                          
    105K: 104.4      | Peak: None       | Conclusion: negative
  exp_030c_tcn_cheetah_s0_sigma10          | σ=1.0, Cheetah                          
    105K: 122.5      | Peak: None       | Conclusion: negative

RAVE (Reality-Anchored Value Estimation)
----------------------------------------------------------------------------------------------------
  exp_028_rave_walker_s0                   | RAVE Walker                             
    105K: {'eval_return': 29, 'value_mean': 92.2, 've_ratio': 3.183} | Peak: None       | Conclusion: negative

Dual Critic
----------------------------------------------------------------------------------------------------
  exp_032_dual_critic_walker               | Dual Critic Walker s0                   
    105K: None       | Peak: None       | Conclusion: success
Traceback (most recent call last):
  File "&lt;stdin>", line 60, in &lt;module>
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a5e432bc-d9a1-4305-b87c-847efd4c8296",
  "tool_use_result": "Error: Exit code 1\nINTERVENTION EXPERIMENT RESULTS SUMMARY\n====================================================================================================\n\nTCN (Temporal Conditioning Noise)\n----------------------------------------------------------------------------------------------------\n  exp_027_tcn_walker_s0                    | σ=0.5, Walker                           \n    105K: 95.5       | Peak: None       | Conclusion: negative\n  exp_027_tcn_walker_s0_sigma02            | σ=0.2, Walker                           \n    105K: 236.4      | Peak: None       | Conclusion: success\n  exp_029c_tcn_walker_s0_sigma01           | σ=0.1, Walker s0                        \n    105K: 204.7      | Peak: None       | Conclusion: negative\n  exp_029a_tcn_walker_s1_sigma02           | σ=0.2, Walker s1                        \n    105K: 319.4      | Peak: None       | Conclusion: success\n  exp_029b_tcn_walker_s2_sigma02           | σ=0.2, Walker s2                        \n    105K: 31.97      | Peak: None       | Conclusion: negative\n  exp_030a_tcn_cheetah_s0_sigma02          | σ=0.2, Cheetah                          \n    105K: None       | Peak: None       | Conclusion: negative\n  exp_030b_tcn_cheetah_s0_sigma05          | σ=0.5, Cheetah                          \n    105K: 104.4      | Peak: None       | Conclusion: negative\n  exp_030c_tcn_cheetah_s0_sigma10          | σ=1.0, Cheetah                          \n    105K: 122.5      | Peak: None       | Conclusion: negative\n\nRAVE (Reality-Anchored Value Estimation)\n----------------------------------------------------------------------------------------------------\n  exp_028_rave_walker_s0                   | RAVE Walker                             \n    105K: {'eval_return': 29, 'value_mean': 92.2, 've_ratio': 3.183} | Peak: None       | Conclusion: negative\n\nDual Critic\n----------------------------------------------------------------------------------------------------\n  exp_032_dual_critic_walker               | Dual Critic Walker s0                   \n    105K: None       | Peak: None       | Conclusion: success\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 60, in &lt;module>\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---


### System

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubu…",
  "usage": {
    "total_tokens": 66983,
    "tool_uses": 33,
    "duration_ms": 96531
  },
  "last_tool_name": "Bash",
  "uuid": "89607fd0-c2fe-40f3-b398-0cf5f5ed0e51",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 132_

<details open><summary>🔧 Tool call — Bash · `toolu_01RmSfduKZT2byuvqZrNcFm3`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\n# Comprehensive list of intervention experiments\nintervention_exps = {\n    \"TCN σ=0.5\": [\n        'exp_027_tcn_walker_s0',\n        'exp_027_tcn_walker_s1',\n        'exp_030b_tcn_cheetah_s0_sigma05',\n    ],\n    \"TCN σ=0.2\": [\n        'exp_027_tcn_walker_s0_sigma02',\n        'exp_029a_tcn_walker_s1_sigma02',\n        'exp_029b_tcn_walker_s2_sigma02',\n        'exp_030a_tcn_cheetah_s0_sigma02',\n    ],\n    \"TCN σ=0.1\": [\n        'exp_029c_tcn_walker_s0_sigma01',\n    ],\n    \"TCN σ=1.0\": [\n        'exp_030c_tcn_cheetah_s0_sigma10',\n    ],\n    \"RAVE\": [\n        'exp_028_rave_walker_s0',\n        'exp_028_rave_walker_s0_ceil15',\n    ],\n    \"Dual Critic\": [\n        'exp_032_dual_critic_walker',\n        'exp_032b_dual_critic_walker_s1',\n        'exp_034_dual_critic_cheetah',\n        'exp_038_dual_critic_walker_s2',\n        'exp_041_dual_critic_walker_s3',\n        'exp_040_wide_dual_critic_cheetah',\n    ],\n    \"Wide Single Critic\": [\n        'exp_033_wide_critic_walker',\n        'exp_037_wide_critic_cheetah',\n    ],\n    \"Narrow Dual Critic\": [\n        'exp_035_narrow_dual_critic_walker',\n    ],\n    \"Reward-Only SGS\": [\n        'exp_016e_sgs_walker_s1',\n    ],\n    \"Full-Pathway SGS\": [\n        'exp_018v2_full_sgs_walker_s1',\n        'exp_018_full_sgs_s2',\n        'exp_021_full_sgs_cheetah_s1',\n    ],\n    \"Obs-Decoder SGS\": [\n        'exp_025_obs_sgs_walker_s1',\n        'exp_025_obs_sgs_walker_s2',\n        'exp_026_obs_sgs_cheetah_s0',\n    ],\n    \"Frozen Embedding\": [\n        'exp_042_frozen_dt_emb_walker',\n        'exp_084_frozen_walker_s1',\n        'exp_087_frozen_cheetah_s1',\n        'exp_046_frozen_dt_emb_cheetah',\n        'exp_047_frozen_dt_emb_walker_s1',\n        'exp_057_frozen_walker_s2',\n        'exp_058_frozen_cheetah_s1',\n    ],\n    \"Removed Embedding (008f)\": [\n        'exp_008f_no_dt_embed_subsample_on_h8',\n        'exp_008f_s2',\n        'exp_008f_s3_no_dt_embed_walker',\n        'exp_008f_s4',\n    ],\n    \"Untreated Baseline (008d)\": [\n        'exp_008d',\n        'exp_008d_civo_trigger_s2',\n        'exp_008d_civo_trigger_s3',\n        'exp_008d_civo_trigger_s4',\n        'exp_009b_008d_walker_s2',\n    ]\n}\n\nprint(\"\\n\" + \"=\" * 120)\nprint(\"COMPREHENSIVE INTERVENTION EXPERIMENT EVALUATION RETURNS\")\nprint(\"=\" * 120)\n\nfor category, exp_ids in intervention_exps.items():\n    print(f\"\\n{category}\")\n    print(\"-\" * 120)\n    \n    for exp_id in exp_ids:\n        if exp_id in registry.get('experiments', {}):\n            exp = registry['experiments'][exp_id]\n            metrics = exp.get('metrics', {})\n            \n            eval_105k = metrics.get('eval_return_105K') or metrics.get('eval_return_105k')\n            eval_peak = metrics.get('eval_return_peak')\n            eval_final = metrics.get('eval_return_final')\n            conclusion = exp.get('conclusion', 'unknown')\n            \n            # Extract eval trajectory if available\n            eval_traj = metrics.get('eval_trajectory', {})\n            traj_str = \"\"\n            if isinstance(eval_traj, dict) and eval_traj:\n                steps = sorted([int(k) for k in eval_traj.keys() if str(k).isdigit()])\n                if steps:\n                    traj_str = \" | Trajectory: \" + \", \".join(f\"{s}K:{eval_traj.get(str(s), 'N/A'):.1f}\" for s in steps[-4:])\n            \n            print(f\"  {exp_id:50s} | 105K: {str(eval_105k)[:8]:8s} | Peak: {str(eval_peak)[:8]:8s} | Final: {str(eval_final)[:8]:8s} | {conclusion:10s}{traj_str}\")\n        else:\n            print(f\"  {exp_id:50s} | NOT FOUND IN REGISTRY\")\n\nPYEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "72c78803-4e65-4bfd-8917-8285bcec3f8c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0173QnLnfurZRuVvt8vjRTxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1880,
      "cache_read_input_tokens": 64948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1880,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 133 · 2026-05-29T00:37:06.636Z_

<details><summary>↩ Tool result · `toolu_01RmSfduKZT2byuvqZrNcFm3`</summary>

```text
========================================================================================================================
COMPREHENSIVE INTERVENTION EXPERIMENT EVALUATION RETURNS
========================================================================================================================

TCN σ=0.5
------------------------------------------------------------------------------------------------------------------------
  exp_027_tcn_walker_s0                              | 105K: 95.5     | Peak: None     | Final: None     | negative  
  exp_027_tcn_walker_s1                              | 105K: None     | Peak: None     | Final: None     | negative  
  exp_030b_tcn_cheetah_s0_sigma05                    | 105K: 104.4    | Peak: None     | Final: None     | negative  

TCN σ=0.2
------------------------------------------------------------------------------------------------------------------------
  exp_027_tcn_walker_s0_sigma02                      | 105K: 236.4    | Peak: None     | Final: None     | success   
  exp_029a_tcn_walker_s1_sigma02                     | 105K: 319.4    | Peak: None     | Final: None     | success   
  exp_029b_tcn_walker_s2_sigma02                     | 105K: 31.97    | Peak: None     | Final: None     | negative  
  exp_030a_tcn_cheetah_s0_sigma02                    | 105K: None     | Peak: None     | Final: None     | negative  

TCN σ=0.1
------------------------------------------------------------------------------------------------------------------------
  exp_029c_tcn_walker_s0_sigma01                     | 105K: 204.7    | Peak: None     | Final: None     | negative  

TCN σ=1.0
------------------------------------------------------------------------------------------------------------------------
  exp_030c_tcn_cheetah_s0_sigma10                    | 105K: 122.5    | Peak: None     | Final: None     | negative  

RAVE
------------------------------------------------------------------------------------------------------------------------
  exp_028_rave_walker_s0                             | 105K: None     | Peak: None     | Final: None     | negative  
  exp_028_rave_walker_s0_ceil15                      | 105K: 76.2     | Peak: None     | Final: None     | negative  

Dual Critic
------------------------------------------------------------------------------------------------------------------------
  exp_032_dual_critic_walker                         | 105K: None     | Peak: None     | Final: None     | success   
  exp_032b_dual_critic_walker_s1                     | 105K: None     | Peak: None     | Final: None     | success   
  exp_034_dual_critic_cheetah                        | 105K: None     | Peak: None     | Final: None     | negative  
  exp_038_dual_critic_walker_s2                      | 105K: None     | Peak: 354      | Final: 120.9    | negative  
  exp_041_dual_critic_walker_s3                      | 105K: None     | Peak: 761.1    | Final: 544      | success   
  exp_040_wide_dual_critic_cheetah                   | 105K: None     | Peak: None     | Final: None     | success   

Wide Single Critic
------------------------------------------------------------------------------------------------------------------------
  exp_033_wide_critic_walker                         | 105K: None     | Peak: None     | Final: None     | success   
  exp_037_wide_critic_cheetah                        | 105K: None     | Peak: 350.1    | Final: 146.1    | negative  

Narrow Dual Critic
------------------------------------------------------------------------------------------------------------------------
  exp_035_narrow_dual_critic_walker                  | 105K: None     | Peak: None     | Final: None     | success   

Reward-Only SGS
------------------------------------------------------------------------------------------------------------------------
  exp_016e_sgs_walker_s1                             | 105K: None     | Peak: None     | Final: None     | negative  

Full-Pathway SGS
------------------------------------------------------------------------------------------------------------------------
  exp_018v2_full_sgs_walker_s1                       | 105K: None     | Peak: 499.6    | Final: 448.3    | negative  
  exp_018_full_sgs_s2                                | 105K: None     | Peak: None     | Final: None     | negative  
  exp_021_full_sgs_cheetah_s1                        | 105K: None     | Peak: None     | Final: 221.5    | negative  

Obs-Decoder SGS
------------------------------------------------------------------------------------------------------------------------
  exp_025_obs_sgs_walker_s1                          | 105K: None     | Peak: None     | Final: None     | failed    
  exp_025_obs_sgs_walker_s2                          | 105K: None     | Peak: None     | Final: None     | negative  
  exp_026_obs_sgs_cheetah_s0                         | 105K: None     | Peak: None     | Final: None     | failed    

Frozen Embedding
------------------------------------------------------------------------------------------------------------------------
  exp_042_frozen_dt_emb_walker                       | 105K: None     | Peak: None     | Final: None     | success   
  exp_084_frozen_walker_s1                           | NOT FOUND IN REGISTRY
  exp_087_frozen_cheetah_s1                          | NOT FOUND IN REGISTRY
  exp_046_frozen_dt_emb_cheetah                      | 105K: None     | Peak: None     | Final: None     | success   
  exp_047_frozen_dt_emb_walker_s1                    | 105K: None     | Peak: None     | Final: None     | success   
  exp_057_frozen_walker_s2                           | NOT FOUND IN REGISTRY
  exp_058_frozen_cheetah_s1                          | NOT FOUND IN REGISTRY

Removed Embedding (008f)
------------------------------------------------------------------------------------------------------------------------
  exp_008f_no_dt_embed_subsample_on_h8               | 105K: None     | Peak: None     | Final: None     | success   
  exp_008f_s2                                        | 105K: None     | Peak: None     | Final: None     | killed    
  exp_008f_s3_no_dt_embed_walker                     | 105K: None     | Peak: None     | Final: 363.8    | success   
  exp_008f_s4                                        | 105K: 306.5    | Peak: None     | Final: None     | negative  

Untreated Baseline (008d)
------------------------------------------------------------------------------------------------------------------------
  exp_008d                                           | 105K: None     | Peak: None     | Final: None     | killed    
  exp_008d_civo_trigger_s2                           | 105K: None     | Peak: None     | Final: None     | killed    
  exp_008d_civo_trigger_s3                           | 105K: None     | Peak: 451.7    | Final: 267.6    | success   
  exp_008d_civo_trigger_s4                           | 105K: None     | Peak: None     | Final: None     | success   
  exp_009b_008d_walker_s2                            | 105K: None     | Peak: None     | Final: None     | negative
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "78cb16be-20ba-4752-bbd9-bcae8140a5d0"
}
```

</details>

---


### System

_source line 134_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubu…",
  "usage": {
    "total_tokens": 70351,
    "tool_uses": 34,
    "duration_ms": 103123
  },
  "last_tool_name": "Bash",
  "uuid": "69f8f26f-bec7-4a0f-8660-4c65ce4d6e71",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 135_

<details open><summary>🔧 Tool call — Bash · `toolu_01PMVgv1Z5EFgQgf3U82o5wk`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\n# Target experiments with full eval return data\ntargets = [\n    'exp_027_tcn_walker_s0',\n    'exp_027_tcn_walker_s0_sigma02',\n    'exp_028_rave_walker_s0',\n    'exp_029a_tcn_walker_s1_sigma02',\n    'exp_029b_tcn_walker_s2_sigma02',\n    'exp_029c_tcn_walker_s0_sigma01',\n    'exp_030a_tcn_cheetah_s0_sigma02',\n    'exp_030b_tcn_cheetah_s0_sigma05',\n    'exp_030c_tcn_cheetah_s0_sigma10',\n    'exp_031_tcn_pickcube_s0_sigma02',\n    'exp_032_dual_critic_walker',\n    'exp_033_wide_critic_walker',\n    'exp_035_narrow_dual_critic_walker',\n    'exp_042_frozen_dt_emb_walker',\n    'exp_008f_no_dt_embed_subsample_on_h8',\n    'exp_008d',\n]\n\nprint(\"EXPERIMENT DETAILS WITH FULL METRICS\")\nprint(\"=\" * 150)\n\nfor exp_id in targets:\n    if exp_id in registry.get('experiments', {}):\n        exp = registry['experiments'][exp_id]\n        metrics = exp.get('metrics', {})\n        \n        # Get various eval return fields\n        for key in sorted(metrics.keys()):\n            if 'eval_return' in key.lower():\n                val = metrics[key]\n                print(f\"{exp_id:45s} | {key:35s}: {val}\")\n        print()\n\nPYEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "5bc235d1-9dbc-445e-931c-cc73f6657373",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R3JjYFQhyZ5KrZuzsLNAuV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 3363,
      "cache_read_input_tokens": 66828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3363,
        "ephemeral_1h_input_tokens": 0
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

_source line 136 · 2026-05-29T00:37:13.231Z_

<details><summary>↩ Tool result · `toolu_01PMVgv1Z5EFgQgf3U82o5wk`</summary>

```text
EXPERIMENT DETAILS WITH FULL METRICS
======================================================================================================================================================
exp_027_tcn_walker_s0                         | eval_return_105K                   : 95.5
exp_027_tcn_walker_s0                         | eval_return_112K                   : 99.5
exp_027_tcn_walker_s0                         | eval_return_15K                    : 154.6
exp_027_tcn_walker_s0                         | eval_return_25K                    : 223.6
exp_027_tcn_walker_s0                         | eval_return_35K                    : 240
exp_027_tcn_walker_s0                         | eval_return_45K                    : 101.2
exp_027_tcn_walker_s0                         | eval_return_55K                    : 70
exp_027_tcn_walker_s0                         | eval_return_5K                     : 37.4
exp_027_tcn_walker_s0                         | eval_return_65K                    : 95.1
exp_027_tcn_walker_s0                         | eval_return_75K                    : 189.2
exp_027_tcn_walker_s0                         | eval_return_85K                    : 36
exp_027_tcn_walker_s0                         | eval_return_95K                    : 166.4

exp_027_tcn_walker_s0_sigma02                 | eval_return_105K                   : 236.4
exp_027_tcn_walker_s0_sigma02                 | eval_return_115K                   : 543.8
exp_027_tcn_walker_s0_sigma02                 | eval_return_125K                   : 458.4
exp_027_tcn_walker_s0_sigma02                 | eval_return_135K                   : 496.7
exp_027_tcn_walker_s0_sigma02                 | eval_return_145K                   : 542.7
exp_027_tcn_walker_s0_sigma02                 | eval_return_155K                   : 660.5
exp_027_tcn_walker_s0_sigma02                 | eval_return_15K                    : 150.6
exp_027_tcn_walker_s0_sigma02                 | eval_return_165K                   : 653.3
exp_027_tcn_walker_s0_sigma02                 | eval_return_175K                   : 821.1
exp_027_tcn_walker_s0_sigma02                 | eval_return_185K                   : 560.5
exp_027_tcn_walker_s0_sigma02                 | eval_return_195K                   : 567.9
exp_027_tcn_walker_s0_sigma02                 | eval_return_205K                   : 558.7
exp_027_tcn_walker_s0_sigma02                 | eval_return_215K                   : 551
exp_027_tcn_walker_s0_sigma02                 | eval_return_25K                    : 199.4
exp_027_tcn_walker_s0_sigma02                 | eval_return_35K                    : 278.2
exp_027_tcn_walker_s0_sigma02                 | eval_return_45K                    : 315.6
exp_027_tcn_walker_s0_sigma02                 | eval_return_55K                    : 278.6
exp_027_tcn_walker_s0_sigma02                 | eval_return_5K                     : 35.6
exp_027_tcn_walker_s0_sigma02                 | eval_return_65K                    : 331
exp_027_tcn_walker_s0_sigma02                 | eval_return_75K                    : 293.1
exp_027_tcn_walker_s0_sigma02                 | eval_return_85K                    : 363.9
exp_027_tcn_walker_s0_sigma02                 | eval_return_95K                    : 171.4


exp_029a_tcn_walker_s1_sigma02                | eval_return_105K                   : 319.4
exp_029a_tcn_walker_s1_sigma02                | eval_return_115K                   : 345.5
exp_029a_tcn_walker_s1_sigma02                | eval_return_125K                   : 401
exp_029a_tcn_walker_s1_sigma02                | eval_return_135K                   : 307.8
exp_029a_tcn_walker_s1_sigma02                | eval_return_145K                   : 380.8
exp_029a_tcn_walker_s1_sigma02                | eval_return_155K                   : 307.3
exp_029a_tcn_walker_s1_sigma02                | eval_return_15K                    : 137.7
exp_029a_tcn_walker_s1_sigma02                | eval_return_165K                   : 320.3
exp_029a_tcn_walker_s1_sigma02                | eval_return_175K                   : 159
exp_029a_tcn_walker_s1_sigma02                | eval_return_185K                   : 278.2
exp_029a_tcn_walker_s1_sigma02                | eval_return_195K                   : 301.2
exp_029a_tcn_walker_s1_sigma02                | eval_return_205K                   : 204.6
exp_029a_tcn_walker_s1_sigma02                | eval_return_215K                   : 161.3
exp_029a_tcn_walker_s1_sigma02                | eval_return_25K                    : 180.9
exp_029a_tcn_walker_s1_sigma02                | eval_return_35K                    : 124
exp_029a_tcn_walker_s1_sigma02                | eval_return_45K                    : 124.2
exp_029a_tcn_walker_s1_sigma02                | eval_return_55K                    : 133.9
exp_029a_tcn_walker_s1_sigma02                | eval_return_5K                     : 36.7
exp_029a_tcn_walker_s1_sigma02                | eval_return_65K                    : 169.7
exp_029a_tcn_walker_s1_sigma02                | eval_return_75K                    : 171.2
exp_029a_tcn_walker_s1_sigma02                | eval_return_85K                    : 151.8
exp_029a_tcn_walker_s1_sigma02                | eval_return_95K                    : 180.3

exp_029b_tcn_walker_s2_sigma02                | eval_return_105K                   : 31.97
exp_029b_tcn_walker_s2_sigma02                | eval_return_115K                   : 35.45
exp_029b_tcn_walker_s2_sigma02                | eval_return_125K                   : 33.04
exp_029b_tcn_walker_s2_sigma02                | eval_return_135K                   : 42.47
exp_029b_tcn_walker_s2_sigma02                | eval_return_145K                   : 51.66
exp_029b_tcn_walker_s2_sigma02                | eval_return_155K                   : 56.5
exp_029b_tcn_walker_s2_sigma02                | eval_return_15K                    : 168.41
exp_029b_tcn_walker_s2_sigma02                | eval_return_165K                   : 44.9
exp_029b_tcn_walker_s2_sigma02                | eval_return_25K                    : 159.56
exp_029b_tcn_walker_s2_sigma02                | eval_return_35K                    : 168.05
exp_029b_tcn_walker_s2_sigma02                | eval_return_45K                    : 171.51
exp_029b_tcn_walker_s2_sigma02                | eval_return_55K                    : 177.67
exp_029b_tcn_walker_s2_sigma02                | eval_return_5K                     : 30.46
exp_029b_tcn_walker_s2_sigma02                | eval_return_65K                    : 106.57
exp_029b_tcn_walker_s2_sigma02                | eval_return_75K                    : 64.01
exp_029b_tcn_walker_s2_sigma02                | eval_return_85K                    : 62.82
exp_029b_tcn_walker_s2_sigma02                | eval_return_95K                    : 44.66

exp_029c_tcn_walker_s0_sigma01                | eval_return_105K                   : 204.7
exp_029c_tcn_walker_s0_sigma01                | eval_return_115K                   : 296.4
exp_029c_tcn_walker_s0_sigma01                | eval_return_125K                   : 232.3
exp_029c_tcn_walker_s0_sigma01                | eval_return_135K                   : 247.4
exp_029c_tcn_walker_s0_sigma01                | eval_return_145K                   : 323.1
exp_029c_tcn_walker_s0_sigma01                | eval_return_155K                   : 359.7
exp_029c_tcn_walker_s0_sigma01                | eval_return_15K                    : 99.1
exp_029c_tcn_walker_s0_sigma01                | eval_return_165K                   : 490.7
exp_029c_tcn_walker_s0_sigma01                | eval_return_175K                   : 246.2
exp_029c_tcn_walker_s0_sigma01                | eval_return_185K                   : 220.6
exp_029c_tcn_walker_s0_sigma01                | eval_return_195K                   : 212.8
exp_029c_tcn_walker_s0_sigma01                | eval_return_205K                   : 256.9
exp_029c_tcn_walker_s0_sigma01                | eval_return_215K                   : 328.3
exp_029c_tcn_walker_s0_sigma01                | eval_return_25K                    : 140.7
exp_029c_tcn_walker_s0_sigma01                | eval_return_35K                    : 155.7
exp_029c_tcn_walker_s0_sigma01                | eval_return_45K                    : 160.9
exp_029c_tcn_walker_s0_sigma01                | eval_return_55K                    : 254.8
exp_029c_tcn_walker_s0_sigma01                | eval_return_5K                     : 35.6
exp_029c_tcn_walker_s0_sigma01                | eval_return_65K                    : 268.7
exp_029c_tcn_walker_s0_sigma01                | eval_return_75K                    : 295.5
exp_029c_tcn_walker_s0_sigma01                | eval_return_85K                    : 220.8
exp_029c_tcn_walker_s0_sigma01                | eval_return_95K                    : 188.6

exp_030a_tcn_cheetah_s0_sigma02               | eval_return_35K                    : 299.5
exp_030a_tcn_cheetah_s0_sigma02               | eval_return_55K                    : 31.9

exp_030b_tcn_cheetah_s0_sigma05               | eval_return_105K                   : 104.4
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_115K                   : 137.7
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_125K                   : 211.7
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_135K                   : 97.2
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_145K                   : 79.4
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_155K                   : 76.8
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_15K                    : 78.3
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_165K                   : 77.5
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_175K                   : 85.7
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_185K                   : 68.7
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_195K                   : 77.6
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_25K                    : 219.3
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_35K                    : 296.5
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_45K                    : 32.8
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_55K                    : 6
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_5K                     : 8.3
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_65K                    : 71.2
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_75K                    : 23.3
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_85K                    : 34
exp_030b_tcn_cheetah_s0_sigma05               | eval_return_95K                    : 143.6

exp_030c_tcn_cheetah_s0_sigma10               | eval_return_105K                   : 122.5
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_115K                   : 162.2
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_125K                   : 148.5
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_135K                   : 138.4
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_145K                   : 100.4
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_155K                   : 144.3
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_15K                    : 87.5
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_165K                   : 130.9
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_175K                   : 66.4
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_185K                   : 47.2
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_195K                   : 56.5
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_205K                   : 49.7
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_215K                   : 47.2
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_25K                    : 166.3
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_35K                    : 371.7
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_45K                    : 144.0
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_55K                    : 266.0
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_5K                     : 8.3
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_65K                    : 197.0
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_75K                    : 107.8
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_85K                    : 95.8
exp_030c_tcn_cheetah_s0_sigma10               | eval_return_95K                    : 72.8

exp_031_tcn_pickcube_s0_sigma02               | eval_return_132K                   : 23.45
exp_031_tcn_pickcube_s0_sigma02               | eval_return_152K                   : 23.1
exp_031_tcn_pickcube_s0_sigma02               | eval_return_192K                   : 11.6






exp_008d                                      | eval_return_15K                    : 153.7
exp_008d                                      | eval_return_25K                    : 167.2
exp_008d                                      | eval_return_35K                    : 146.3
exp_008d                                      | eval_return_5K                     : 31
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ae28dc80-c948-4bff-921b-cd7b8dba6382"
}
```

</details>

---


### System

_source line 137_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running python3 << 'PYEOF'\nimport yaml\nimport json\n\nwith open…",
  "usage": {
    "total_tokens": 75480,
    "tool_uses": 35,
    "duration_ms": 117783
  },
  "last_tool_name": "Bash",
  "uuid": "67e35338-ae07-4f23-ae34-13690b795850",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 138_

<details open><summary>🔧 Tool call — Bash · `toolu_01JHdFxwryB6tbdxcZe9jVG4`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\nimport json\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\n# Comprehensive intervention experiment mapping\ninterventions = {\n    \"TCN (Temporal Conditioning Noise) - σ=0.5\": [\n        'exp_027_tcn_walker_s0',\n        'exp_030b_tcn_cheetah_s0_sigma05',\n    ],\n    \"TCN - σ=0.2\": [\n        'exp_027_tcn_walker_s0_sigma02',\n        'exp_029a_tcn_walker_s1_sigma02',\n        'exp_029b_tcn_walker_s2_sigma02',\n        'exp_030a_tcn_cheetah_s0_sigma02',\n    ],\n    \"TCN - σ=0.1\": [\n        'exp_029c_tcn_walker_s0_sigma01',\n    ],\n    \"TCN - σ=1.0\": [\n        'exp_030c_tcn_cheetah_s0_sigma10',\n    ],\n    \"RAVE (Reality-Anchored Value Estimation)\": [\n        'exp_028_rave_walker_s0',\n    ],\n    \"Reward-Only SGS\": [\n        'exp_016e_sgs_walker_s1',\n    ],\n    \"Full-Pathway SGS\": [\n        'exp_018v2_full_sgs_walker_s1',\n        'exp_021_full_sgs_cheetah_s1',\n    ],\n    \"Obs-Decoder SGS\": [\n        'exp_025_obs_sgs_walker_s1',\n        'exp_026_obs_sgs_cheetah_s0',\n    ],\n    \"Dual Critic\": [\n        'exp_032_dual_critic_walker',\n        'exp_032b_dual_critic_walker_s1',\n        'exp_034_dual_critic_cheetah',\n        'exp_038_dual_critic_walker_s2',\n        'exp_040_wide_dual_critic_cheetah',\n        'exp_041_dual_critic_walker_s3',\n    ],\n    \"Wide Single Critic\": [\n        'exp_033_wide_critic_walker',\n        'exp_037_wide_critic_cheetah',\n    ],\n    \"Narrow Dual Critic\": [\n        'exp_035_narrow_dual_critic_walker',\n    ],\n    \"Frozen dt_Embedding\": [\n        'exp_042_frozen_dt_emb_walker',\n        'exp_046_frozen_dt_emb_cheetah',\n        'exp_047_frozen_dt_emb_walker_s1',\n    ],\n    \"Removed dt_Embedding (008f controls)\": [\n        'exp_008f_no_dt_embed_subsample_on_h8',\n        'exp_008f_s3_no_dt_embed_walker',\n        'exp_008f_s4',\n    ],\n    \"Untreated Baseline (008d)\": [\n        'exp_008d',\n        'exp_008d_civo_trigger_s3',\n        'exp_009b_008d_walker_s2',\n    ],\n}\n\nprint(\"\\n\" + \"=\" * 140)\nprint(\"COMPILED INTERVENTION EXPERIMENT RESULTS - eval_return AT 105K STEPS\")\nprint(\"=\" * 140)\nprint(f\"{'Intervention':50s} | {'Exp_ID':50s} | {'Eval@105K':10s} | {'Peak':10s} | {'Conclusion':12s} | Baseline\")\nprint(\"-\" * 140)\n\nbaseline_values = {\n    'Walker Walk': 787.7,  # Baseline from memory\n    'Cheetah Run': 593.9,\n    'PickCube': None,\n}\n\nfor category, exp_ids in interventions.items():\n    print(f\"\\n{category}:\")\n    \n    for exp_id in exp_ids:\n        if exp_id in registry.get('experiments', {}):\n            exp = registry['experiments'][exp_id]\n            metrics = exp.get('metrics', {})\n            \n            eval_105k = metrics.get('eval_return_105K') or metrics.get('eval_return_105k')\n            eval_peak = metrics.get('eval_return_peak')\n            conclusion = exp.get('conclusion', 'unknown')\n            \n            # Determine baseline for this experiment\n            if 'cheetah' in exp_id.lower():\n                baseline = baseline_values['Cheetah Run']\n            elif 'pickcube' in exp_id.lower():\n                baseline = baseline_values['PickCube']\n            else:\n                baseline = baseline_values['Walker Walk']\n            \n            pct_of_baseline = \"\"\n            if eval_105k and baseline:\n                pct_of_baseline = f\"({eval_105k/baseline*100:.1f}%)\"\n            \n            print(f\"  {category[:48]:48s} | {exp_id:50s} | {str(eval_105k)[:10]:10s} | {str(eval_peak)[:10]:10s} | {conclusion:12s} | {pct_of_baseline}\")\n\nprint(\"\\n\" + \"=\" * 140)\nprint(\"BASELINE EVAL_RETURN VALUES FOR REFERENCE\")\nprint(\"=\" * 140)\nprint(\"Walker Walk baseline (no gate): ~788-969 (mean across seeds)\")\nprint(\"Cheetah Run baseline (no gate): ~594-642 (mean across seeds)\")\nprint(\"008d untreated (trained dt_emb + gate): ~83-268 (severe CIVO collapse)\")\nprint(\"008f removed embedding (no dt_emb control): ~306-503 (stable, no CIVO)\")\n\nPYEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "3982c15c-f40a-42b7-8f57-d1335a304b49",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RBjbLv6noo4sgrzAyruXgM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 5127,
      "cache_read_input_tokens": 70191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5127,
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

_source line 139 · 2026-05-29T00:37:27.917Z_

<details><summary>↩ Tool result · `toolu_01JHdFxwryB6tbdxcZe9jVG4`</summary>

```text
============================================================================================================================================
COMPILED INTERVENTION EXPERIMENT RESULTS - eval_return AT 105K STEPS
============================================================================================================================================
Intervention                                       | Exp_ID                                             | Eval@105K  | Peak       | Conclusion   | Baseline
--------------------------------------------------------------------------------------------------------------------------------------------

TCN (Temporal Conditioning Noise) - σ=0.5:
  TCN (Temporal Conditioning Noise) - σ=0.5        | exp_027_tcn_walker_s0                              | 95.5       | None       | negative     | (12.1%)
  TCN (Temporal Conditioning Noise) - σ=0.5        | exp_030b_tcn_cheetah_s0_sigma05                    | 104.4      | None       | negative     | (17.6%)

TCN - σ=0.2:
  TCN - σ=0.2                                      | exp_027_tcn_walker_s0_sigma02                      | 236.4      | None       | success      | (30.0%)
  TCN - σ=0.2                                      | exp_029a_tcn_walker_s1_sigma02                     | 319.4      | None       | success      | (40.5%)
  TCN - σ=0.2                                      | exp_029b_tcn_walker_s2_sigma02                     | 31.97      | None       | negative     | (4.1%)
  TCN - σ=0.2                                      | exp_030a_tcn_cheetah_s0_sigma02                    | None       | None       | negative     | 

TCN - σ=0.1:
  TCN - σ=0.1                                      | exp_029c_tcn_walker_s0_sigma01                     | 204.7      | None       | negative     | (26.0%)

TCN - σ=1.0:
  TCN - σ=1.0                                      | exp_030c_tcn_cheetah_s0_sigma10                    | 122.5      | None       | negative     | (20.6%)

RAVE (Reality-Anchored Value Estimation):
  RAVE (Reality-Anchored Value Estimation)         | exp_028_rave_walker_s0                             | None       | None       | negative     | 

Reward-Only SGS:
  Reward-Only SGS                                  | exp_016e_sgs_walker_s1                             | None       | None       | negative     | 

Full-Pathway SGS:
  Full-Pathway SGS                                 | exp_018v2_full_sgs_walker_s1                       | None       | 499.6      | negative     | 
  Full-Pathway SGS                                 | exp_021_full_sgs_cheetah_s1                        | None       | None       | negative     | 

Obs-Decoder SGS:
  Obs-Decoder SGS                                  | exp_025_obs_sgs_walker_s1                          | None       | None       | failed       | 
  Obs-Decoder SGS                                  | exp_026_obs_sgs_cheetah_s0                         | None       | None       | failed       | 

Dual Critic:
  Dual Critic                                      | exp_032_dual_critic_walker                         | None       | None       | success      | 
  Dual Critic                                      | exp_032b_dual_critic_walker_s1                     | None       | None       | success      | 
  Dual Critic                                      | exp_034_dual_critic_cheetah                        | None       | None       | negative     | 
  Dual Critic                                      | exp_038_dual_critic_walker_s2                      | None       | 354        | negative     | 
  Dual Critic                                      | exp_040_wide_dual_critic_cheetah                   | None       | None       | success      | 
  Dual Critic                                      | exp_041_dual_critic_walker_s3                      | None       | 761.1      | success      | 

Wide Single Critic:
  Wide Single Critic                               | exp_033_wide_critic_walker                         | None       | None       | success      | 
  Wide Single Critic                               | exp_037_wide_critic_cheetah                        | None       | 350.1      | negative     | 

Narrow Dual Critic:
  Narrow Dual Critic                               | exp_035_narrow_dual_critic_walker                  | None       | None       | success      | 

Frozen dt_Embedding:
  Frozen dt_Embedding                              | exp_042_frozen_dt_emb_walker                       | None       | None       | success      | 
  Frozen dt_Embedding                              | exp_046_frozen_dt_emb_cheetah                      | None       | None       | success      | 
  Frozen dt_Embedding                              | exp_047_frozen_dt_emb_walker_s1                    | None       | None       | success      | 

Removed dt_Embedding (008f controls):
  Removed dt_Embedding (008f controls)             | exp_008f_no_dt_embed_subsample_on_h8               | None       | None       | success      | 
  Removed dt_Embedding (008f controls)             | exp_008f_s3_no_dt_embed_walker                     | None       | None       | success      | 
  Removed dt_Embedding (008f controls)             | exp_008f_s4                                        | 306.5      | None       | negative     | (38.9%)

Untreated Baseline (008d):
  Untreated Baseline (008d)                        | exp_008d                                           | None       | None       | killed       | 
  Untreated Baseline (008d)                        | exp_008d_civo_trigger_s3                           | None       | 451.7      | success      | 
  Untreated Baseline (008d)                        | exp_009b_008d_walker_s2                            | None       | None       | negative     | 

============================================================================================================================================
BASELINE EVAL_RETURN VALUES FOR REFERENCE
============================================================================================================================================
Walker Walk baseline (no gate): ~788-969 (mean across seeds)
Cheetah Run baseline (no gate): ~594-642 (mean across seeds)
008d untreated (trained dt_emb + gate): ~83-268 (severe CIVO collapse)
008f removed embedding (no dt_emb control): ~306-503 (stable, no CIVO)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "660d578d-5a38-45f7-9090-f46fae0632e7"
}
```

</details>

---


### System

_source line 140_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Running ls -lah /home/ubuntu/.agent-ml-research-idea_gen_…",
  "usage": {
    "total_tokens": 78693,
    "tool_uses": 36,
    "duration_ms": 121371
  },
  "last_tool_name": "Bash",
  "uuid": "eaf2fdc6-07e9-490a-870c-267349515763",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 141_

<details open><summary>🔧 Tool call — Bash · `toolu_01GsVTxGjtdFTNz9ZnL27xhY`</summary>

```json
{
  "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/ 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "9a1b7fcb-9e33-4a6b-b1ac-a0b620f7eadf",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DFVRZQezxPrLyfHwoVbX8y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 3205,
      "cache_read_input_tokens": 75318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3205,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 142 · 2026-05-29T00:37:30.683Z_

<details><summary>↩ Tool result · `toolu_01GsVTxGjtdFTNz9ZnL27xhY`</summary>

```text
total 276K
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 17 22:54 .
drwxr-xr-x 96 ubuntu ubuntu  12K May 28 14:04 ..
-rw-r--r--  1 ubuntu ubuntu 2.6K May 16 17:24 018v2_civo_analysis.json
-rw-r--r--  1 ubuntu ubuntu 8.7K May 17 11:57 actor_entropy_data.json
-rw-r--r--  1 ubuntu ubuntu 2.1K May 17 22:54 cheetah_integration_template.md
-rw-r--r--  1 ubuntu ubuntu 5.5K May 16 20:27 civo_decomposition_data.json
-rw-r--r--  1 ubuntu ubuntu 6.6K May 17 04:11 civo_detector_full_retrospective_v3.json
-rw-r--r--  1 ubuntu ubuntu 6.5K May 17 07:32 civo_detector_prospective_results.json
-rw-r--r--  1 ubuntu ubuntu  26K May 17 05:34 detector_formal_validation_v3.json
-rw-r--r--  1 ubuntu ubuntu 1.3K May 17 05:36 detector_table.md
-rw-r--r--  1 ubuntu ubuntu 1.4K May 17 05:36 detector_table.tex
-rw-r--r--  1 ubuntu ubuntu 3.5K May 17 03:33 detector_threshold_analysis.json
-rw-r--r--  1 ubuntu ubuntu 4.6K May 16 20:27 entropy_dynamics_data.json
-rw-r--r--  1 ubuntu ubuntu  836 May 17 20:36 exp_010b_nve_calculation.json
-rw-r--r--  1 ubuntu ubuntu 2.0K May 17 20:39 exp_010b_peak_nve_calculation.json
-rw-r--r--  1 ubuntu ubuntu 8.9K May 17 15:19 exp_019b_analysis.json
-rw-r--r--  1 ubuntu ubuntu 1.3K May 16 19:32 exp_020_c6_summary.txt
-rw-r--r--  1 ubuntu ubuntu  11K May 17 14:03 exp_022b_analysis.json
-rw-r--r--  1 ubuntu ubuntu 3.3K May 16 22:12 gradient_decomposition_008d.json
-rw-r--r--  1 ubuntu ubuntu 3.9K May 16 22:36 gradient_decomposition_008d_corrected.json
-rw-r--r--  1 ubuntu ubuntu 4.3K May 17 17:04 gradient_decomposition_verification.json
-rw-r--r--  1 ubuntu ubuntu 2.7K May 16 18:50 gradient_evolution_018v2.json
-rw-r--r--  1 ubuntu ubuntu 1.6K May 15 05:02 metrics_table.csv
-rw-r--r--  1 ubuntu ubuntu 5.4K May 15 05:02 metrics_table.md
-rw-r--r--  1 ubuntu ubuntu 6.1K May 17 04:03 negative_cases_ve_data.json
-rw-r--r--  1 ubuntu ubuntu  14K May 17 04:06 negative_experiment_retrospective.md
-rw-r--r--  1 ubuntu ubuntu 4.3K May 17 12:55 nve_sensitivity_audit_note.md
-rw-r--r--  1 ubuntu ubuntu 6.2K May 17 12:54 nve_threshold_sensitivity.json
-rw-r--r--  1 ubuntu ubuntu  11K May 16 19:34 nve_trajectories_for_figure.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "74b60804-4e3b-49b5-9138-f17c2b1cc736"
}
```

</details>

---


### System

_source line 143_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "description": "Reading artifacts/analysis/negative_experiment_retrospective.md",
  "usage": {
    "total_tokens": 79845,
    "tool_uses": 37,
    "duration_ms": 124079
  },
  "last_tool_name": "Read",
  "uuid": "e12530c7-7ce7-49f5-b435-96952fafcd1f",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool call

_source line 144_

<details open><summary>🔧 Tool call — Read · `toolu_01DCuM5u83ikJbi9tDgv8ZW8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/negative_experiment_retrospective.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "6ffd5211-bd01-4be6-a2c9-c0d53f664f30",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M4ytaFHXR4HqxYGAhsftDM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1150,
      "cache_read_input_tokens": 78523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1150,
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

_source line 145 · 2026-05-29T00:37:33.339Z_

<details><summary>↩ Tool result · `toolu_01DCuM5u83ikJbi9tDgv8ZW8`</summary>

```text
1	# Negative Experiment Retrospective
2	
3	**Date**: 2026-05-17
4	**Purpose**: Manager 要求复盘所有 negative 实验，检查是否有被遗漏的方法改进线索。
5	
6	---
7	
8	## 逐实验复盘
9	
10	### Line 1: Learned Gate (003→004→005)
11	
12	#### exp_003_event_gated_v2
13	- **证伪说明了什么**: imagination 中 gate 输出 dt∈{1,...,8} 无约束，而 RSSM 只在 subsample curriculum 限定的 dt 上训练过。对未见大 dt 的预测是噪声 → progressive poisoning。
14	- **当时怎么处理**: 修复 dt clipping + logits masking，进入 v3 (004)。
15	- **回头看对不对**: 正确。这是明确的实现 bug，不是方法问题。
16	- **Parent**: exp_001_baseline (implicit)
17	
18	#### exp_004_event_gated_v3
19	- **证伪说明了什么**: gate_loss 爆炸 — compute_gate_targets 用 gate_max_dt=8 但 logits masking 用 effective_max_dt，cross-entropy ~3e8。
20	- **当时怎么处理**: 统一 effective_max_dt 为唯一 dt 来源，进入 v4 (005)。
21	- **回头看对不对**: 正确。又一个实现 bug。
22	- **Parent**: exp_003_event_gated_v2
23	
24	#### exp_005_event_gated_v4 ⭐ (Director 重点关注)
25	- **证伪说明了什么**: 3 轮 bug 修复后，gate 机制本身 PASS（entropy/H_eff/structure 全达标），但 hard categorical gate + variable-rate imagination 与 actor-critic 优化存在**结构性冲突**。gate_scale>0.5 后 return 不可恢复地下降（541→99）。
26	- **当时怎么处理**: 放弃 "learned gate" 整条线。转向诊断 CIVO 现象。
27	- **回头看对不对**: **值得重新审视。** 005 的问题链是：learned gate → variable dt imagination → RSSM 对高 dt 预测不准 → value overestimation → collapse。但 005 用的是 **trained dt_emb**。根据后续发现（C2: trained dt_emb 是 CIVO 必要条件），如果用 **untrained dt_emb (dim=0) + learned gate**，gate 仍可选择 dt，但不会触发 CIVO。这个组合**从未测试过**。
28	- **Parent**: exp_004_event_gated_v3 → 补为 exp_001_baseline
29	
30	**遗漏线索**: untrained dt_emb + learned gate 是未探索的方法变体。008f 证明 dim=0 消除 CIVO；005 证明 gate 本身能学到有意义的 dt pattern。两者组合可能同时获得 adaptive horizon 的好处和 CIVO safety。
31	
32	---
33	
34	### Line 2: Fixed-dt Diagnostics (006→007)
35	
36	#### exp_006_fixed_dt2
37	- **证伪说明了什么**: fixed dt=2（无 learned gate）也崩了。这排除了 "gate 学习机制是问题根源" 的假设。问题在 dt=2 **imagination** 本身（RSSM 在 dt=2 上预测不准 → value 过估 → collapse）。这就是后来命名为 CIVO 的现象。
38	- **当时怎么处理**: 这个 negative 实际上是**关键发现** — 它把问题定位从 "gate 坏了" 缩窄到 "dt>1 imagination 有毒"。启动 008 系列消融。
39	- **回头看对不对**: 完全正确。006 是项目转折点，从 "做方法" 转向 "理解失败"。
40	- **Parent**: exp_005_event_gated_v4
41	
42	#### exp_007_fixed_dt4
43	- **证伪说明了什么**: dt=4 太粗（action temporal resolution 不足），不是 CIVO 而是简单的 under-learning。Value 被抑制（v/e 6-13%），与 dt=2 的 over-estimation 完全相反。
44	- **当时怎么处理**: 确定 dt sweet spot ∈ {1,2}，后续只测 dt=2。
45	- **回头看对不对**: 正确。dt=4 的失败模式不同，不提供 CIVO 诊断信息。
46	- **Parent**: exp_006_fixed_dt2
47	
48	---
49	
50	### Line 3: Subsample/Horizon (008c)
51	
52	#### exp_008c_no_subsample_dt2_h8
53	- **证伪说明了什么**: subsample OFF + dt=2 imagination + H=8 → plateau at 60% baseline（无 collapse，但学习极慢）。与 008a (H=15, 也无 collapse 但 NVE 低) 对比 → H=8 和 H=15 在 subsample OFF 时都不崩，说明 subsample ON (mixed dt training data) 是 CIVO 的关键 co-factor。
54	- **当时怎么处理**: 结论纳入 2×2 消融矩阵，锁定 "trained dt_emb + subsample ON" 为 CIVO 必要条件组合。
55	- **回头看对不对**: 正确，但有遗漏。008c 虽然不崩但性能差（60% baseline），说明 subsample OFF + dt=2 imagination 也不是好方案。这个 negative 暗示：**如果想用 dt>1 imagination，必须找到一种不触发 CIVO 的 dt_emb 方案**（后来 008f dim=0 做到了 85% baseline）。
56	- **Parent**: exp_008d_subsample_on_h8 → 应为 exp_006_fixed_dt2（都是 dt=2 imagination 系列）
57	
58	---
59	
60	### Line 4: Multi-seed Replication (009b, 009c, 009e)
61	
62	#### exp_009b_008d_walker_s2
63	- **证伪说明了什么**: CIVO onset (NVE=2.05×) 在 seed=2 上复现，但没有 collapse（self-correction）。证伪了 "CIVO 必然导致 collapse" 的强假设，建立了 "CIVO onset is deterministic, collapse is stochastic" 的核心洞察。
64	- **当时怎么处理**: 修正叙事 — collapse rate stochastic, NVE diagnostic universal。
65	- **回头看对不对**: 完全正确。这个 negative 比一个 success 更有价值 — 它精确揭示了 CIVO 的概率性质。
66	- **Parent**: exp_008d_subsample_on_h8 ✓
67	
68	#### exp_009c_008f_walker_s2
69	- **证伪说明了什么**: dt_embed_dim=0 seed=2 在 75K 后持续下降（359→148），不复现 008f seed=1 的 zigzag 恢复（→503）。说明 no_dt_emb 方案的性能有 seed 依赖性，不如 seed=1 暗示的那么好。
70	- **当时怎么处理**: 接受 cross-seed 不一致，但保留 C2 结论（NVE<1.5× universal 跨 seed）。
71	- **回头看对不对**: 部分正确。NVE 指标确实 universal (<1.5×)，但 **performance level** 有 seed 依赖。论文报告 008f 系列时应该用 multi-seed mean 而非 cherry-pick seed=1。实际上，seed=2 的 148@105K (15% baseline) 比 trained dt_emb 还差 — 这暗示 **no_dt_emb 方案在某些 seed 上 performance 很差，作为方法贡献需要谨慎 claim**。
72	- **Parent**: exp_008f_no_dt_embed_subsample_on_h8 ✓
73	
74	#### exp_009e_008d_walker_s1
75	- **证伪说明了什么**: 名义上是 seed=1 复现 008d，实际上因为 009e 与 008d 共享 seed=1，不是独立观测。后来发现配置可能有问题（D071）。
76	- **当时怎么处理**: 不计入独立样本，启动 008d_civo_trigger_s3 (seed=3) 作为第三独立 seed。
77	- **回头看对不对**: 正确。重复 seed 无统计意义。
78	- **Parent**: exp_008d_subsample_on_h8 ✓
79	
80	---
81	
82	### Line 5: Frozen dt_emb (015b)
83	
84	#### exp_015b_frozen_dt_emb
85	- **证伪说明了什么**: Frozen（存在但不训练）dt_emb → gradient starvation（actor_loss→0），不是 CIVO。NVE 短暂升到 1.45× 然后自修正。说明 CIVO 需要 dt_emb **actively training**（不断学习 dt-specific representations），仅存在不够。
86	- **当时怎么处理**: 纳入 2×2 矩阵结论：trained=CIVO, frozen=gradient starvation, dim=0=safe。
87	- **回头看对不对**: 正确。精确隔离了 "训练" vs "存在" 的因果效应。
88	- **Parent**: exp_008d_subsample_on_h8 ✓
89	
90	---
91	
92	### Line 6: SGS Interventions (016e→018v2→018_s2)
93	
94	#### exp_016e_sgs_walker_s1
95	- **证伪说明了什么**: Reward-only SGS (detach dt_emb in reward head) 是 architectural no-op — reward gradient 通过 reward head 本身就不经 dt_emb（梯度分解确认 reward gradient to dt_emb ≈ 0）。016e 与 008d 的差异（onset timing）纯属 cross-seed variation。
96	- **当时怎么处理**: 撤回 "SGS delays collapse" 解读。确认 reward pathway 不是 CIVO 根因。
97	- **回头看对不对**: 正确。016e 的真正贡献是揭示梯度结构（reward ≠ 通向 dt_emb 的通路），缩小 viable intervention 搜索空间。
98	- **Parent**: exp_008d_subsample_on_h8 ✓
99	
100	#### exp_018v2_full_sgs_walker_s1 ⭐ (Director 重点关注)
101	- **证伪说明了什么**: Full-SGS (detach ALL decoder gradients from dt_emb) seed=1 — NVE peak=1.66× (CIVO onset), 但 105K 时未完全 collapse (eval=448, 46% baseline)。Late collapse detected @112K。CIVO reduction 79% vs 008d 但未完全消除。
102	- **当时怎么处理**: 与 018_s2 合并判断为 "SGS 不可靠" (collapse_rate=0.5)。结论：CIVO 是 representation-level，切梯度不够。
103	- **回头看对不对**: **诊断可能不够深。** 考虑：
104	  1. 018v2 的 NVE=1.66× 远低于 008d 的 4.12×（79% reduction）— SGS **确实大幅抑制了 CIVO**
105	  2. 018v2 eval=448 vs 008d eval=83 — SGS 使 performance 从 8.6% 恢复到 46% baseline
106	  3. Collapse 在 112K 才开始（vs 008d 的 60K），晚了 52K 步
107	  4. **可能的解释**: SGS 消除了 gradient-mediated CIVO（主通路），但 representation-level co-adaptation 仍通过 KL loss 的 implicit gradient 绕路。如果我们同时 freeze dt_emb + SGS，可能完全消除？但 015b 证明 freeze 导致 gradient starvation...
108	  5. **更可能的解释**: dt_emb 通过 world model 的 shared encoder 间接影响 value function，即使 decoder 梯度被切。World model 训练时 dt_emb concatenated 到 state，这本身改变了 latent space geometry。
109	- **Parent**: exp_008d_subsample_on_h8 ✓
110	
111	#### exp_018_full_sgs_s2
112	- **证伪说明了什么**: Full-SGS seed=2 完全 collapse (eval=40.8@105K)。与 018v2 seed=1 (eval=448) 形成鲜明对比 → SGS 的保护效果 seed-dependent。
113	- **当时怎么处理**: 确认 SGS 不可作为可靠 intervention。降级为 informative negative。
114	- **回头看对不对**: 正确决策。但没有深挖**为什么 seed=2 崩而 seed=1 不崩**。可能原因：seed=2 的 replay buffer sampling sequence 恰好在早期产生更多 dt=2 transitions，加速 dt_emb representation specialization，overwhelm SGS 的保护。
115	- **Parent**: exp_018v2_full_sgs_walker_s1 ✓
116	
117	---
118	
119	### Line 7: Pathway B (008e_v3_s2)
120	
121	#### exp_008e_v3_walker_s2
122	- **证伪说明了什么**: trained dt_emb + subsample ON + **dt=1 imagination** + H=15 seed=2 也崩溃了（715→137@105K）。这证伪了 C6 原假设 "dt=1 imagination prevents collapse"。崩溃机制是 Pathway B (Imagination-Reality Divergence)，不是 CIVO。
123	- **当时怎么处理**: 识别为第二种崩溃机制（Pathway B），与 CIVO (Pathway A) 分离。用 exp_020 matched-seed 控制确认 trained dt_emb 是 Pathway B 的必要条件。
124	- **回头看对不对**: 完全正确。这个 negative 导致发现第二种失败模式，丰富了论文故事。
125	- **Parent**: exp_008e_v3_subsample_on_dt1_h15 ✓
126	
127	---
128	
129	## 被遗漏的方法改进线索
130	
131	### 线索 1: untrained dt_emb + learned gate（高优先级）
132	
133	**推理链**:
134	- 005 证明 learned gate 能产生有意义的 dt pattern (entropy/structure PASS)
135	- 005 失败因为 trained dt_emb → CIVO
136	- 008f 证明 dt_embed_dim=0 消除 CIVO，但牺牲了所有 dt-conditioning 信息
137	- **未测试**: dt_embed_dim=0 (或 untrained/fixed embedding) + learned Gumbel gate
138	
139	**预期**: Gate 根据 state 选择 dt（保留 adaptive horizon 能力），但 world model 不通过 trained embedding 学习 dt-specific representations（避免 CIVO）。Gate 的 decision 直接用于 subsample step selection，而非通过 embedding 间接影响 RSSM。
140	
141	**风险**: 无 dt embedding 时，RSSM 无法区分 dt=1 和 dt=2 transitions → gate 选择的 dt>1 imagination 步骤可能仍然不准。但 008f 已证明这种配置至少达到 85% baseline（seed=1）。
142	
143	**实验设计**: 与 005 相同配置，仅 `--gate_dt_embed_dim 0`（如果参数存在）或等价实现。
144	
145	### 线索 2: 008f 作为方法贡献（需谨慎）
146	
147	**现状**: 008f (no dt_emb, subsample ON) seed=1 达到 503@105K (52% baseline)，是所有 dt>1 配置中最高的。
148	**但**: seed=2 (009c) 只有 148@105K (15% baseline)，seed=3 (008f_s3) 结论=success 但具体数字需确认。
149	
150	**评估**: 如果 multi-seed mean 显著高于 trained dt_emb 的 21.3% (C1)，则 "remove trained dt_emb" 确实是一个 practical mitigation — 不是 intervention（不修复 CIVO），而是 avoidance（不触发 CIVO）。
151	
152	**论文定位**: 与 detector 互补 — detector 检测 CIVO onset，dim=0 是 preventive architecture choice。
153	
154	### 线索 3: SGS + 更短训练
155	
156	018v2 在 105K 时 eval=448 (46% baseline)，到 112K 才开始 late collapse。如果训练到 80K 停止（by detector trigger），SGS 可能在 "检测窗口内" 是有效的 — 即 SGS 将 CIVO onset 延迟足够久让 detector 有时间触发。这可以作为 "detector + SGS 联合方案" 的 story，但需要更多数据支撑。
157	
158	---
159	
160	## 推导链修正
161	
162	| exp_id | 当前 parent | 修正 parent | 原因 |
163	|--------|-----------|-----------|------|
164	| exp_005_event_gated_v4 | exp_001_baseline | **exp_004_event_gated_v3** | 005 是 004 修复后的重试 |
165	| exp_004_event_gated_v3 | (无) | **exp_003_event_gated_v2** | 004 是 003 bug fix 后的重试 |
166	| exp_003_event_gated_v2 | (无) | **exp_001_baseline** | 首个 gate 实验基于 baseline |
167	| exp_008c_no_subsample_dt2_h8 | (无) | **exp_006_fixed_dt2** | 008c 是 006 的 subsample OFF 对照 |
168	| exp_007_fixed_dt4 | (无) | **exp_006_fixed_dt2** | 007 是 006 的 dt=4 对照 |
169	| exp_006_fixed_dt2 | exp_005_event_gated_v4 | ✓ 已正确 | — |
170	
171	---
172	
173	## 总结
174	
175	### 方法贡献候选（按优先级）
176	1. **CIVO Online Detector** — 当前主线，进行中
177	2. **Architecture Avoidance (dim=0)** — 已有数据但 multi-seed 不一致，需更多 seed
178	3. **Adaptive dt without trained embedding** — 未测试，最有方法新颖性但需新实验
179	
180	### 被正确关闭的线
181	- Learned Gumbel gate + trained dt_emb → 结构性 CIVO，正确关闭
182	- dt=4 → 太粗，无 CIVO 但性能差，正确关闭
183	- Reward-only SGS → architectural no-op，正确关闭
184	- Full-SGS as reliable intervention → collapse_rate=0.5，正确降级
185	
186	### 诊断不够深的
187	- **018v2 vs 018_s2 的 seed 差异**：为什么 seed=1 延迟 52K 步而 seed=2 正常速度 collapse？未深挖 replay buffer 中 dt>1 transition 的分布差异。
188	- **009c 的 performance decline**：no_dt_emb seed=2 为什么在 75K 后持续下降？这是否暗示 subsample ON 本身（非 dt_emb）也有 subtle 负面效应？
189	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "0b5d317f-4584-42a4-bdd8-d89c08138f9d"
}
```

</details>

---


### System

_source line 146_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a1f1cb7eaf4b2bda8",
  "tool_use_id": "toolu_01UXNsjtiVw79JPYjKmkkQ7L",
  "status": "completed",
  "output_file": "",
  "summary": "Find experiment data files",
  "usage": {
    "total_tokens": 85901,
    "tool_uses": 37,
    "duration_ms": 139854
  },
  "uuid": "adb9fd4f-171b-42df-b177-04b8b7ac5cbf",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68"
}
```

---


### Tool result

_source line 147 · 2026-05-29T00:37:49.109Z_

<details><summary>↩ Tool result · `toolu_01UXNsjtiVw79JPYjKmkkQ7L`</summary>

```text
Perfect! Now I have all the comprehensive data. Let me create a final summary document:

## Summary

I've completed a very thorough search of the event-gated-adaptive-horizon project and located comprehensive compiled experiment results. Here are the key findings:

### **Main Data Sources Located:**

1. **Registry File** (11,382 lines): `/registry.yaml` - Contains complete experiment metadata for all 200+ runs
2. **Summary Tables** in `/artifacts/_project/data/`:
   - `summary_table.csv` - Compiled eval_return values
   - `metrics_table.csv` - Multi-step evaluation trajectories
   - `cross_env_civo_comparison.csv` - Cross-environment intervention results
   - `nve_4seed_robustness_analysis.csv` - Robustness across seeds
3. **Analysis Files**: `/artifacts/analysis/` contains detailed negative experiment retrospectives and detector validation data
4. **Memory & Reports**: Project-level memory.md and report.md with key metrics

### **Intervention Experiment Results (eval_return@105K steps):**

#### **TCN (Temporal Conditioning Noise)**
- **σ=0.5 (Walker)**: 95.5 (12% baseline) — FAILED
- **σ=0.2 (Walker s0)**: 236.4 (30% baseline) — success
- **σ=0.2 (Walker s1)**: 319.4 (40% baseline) — success  
- **σ=0.2 (Walker s2)**: 32.0 (4% baseline) — FAILED
- **σ=0.1 (Walker)**: 204.7 (26% baseline) — FAILED
- **σ=0.2 (Cheetah)**: Incomplete data
- **σ=0.5 (Cheetah)**: 104.4 (18% baseline) — FAILED
- **σ=1.0 (Cheetah)**: 122.5 (21% baseline) — FAILED

#### **RAVE (Reality-Anchored Value Estimation)**
- **exp_028_rave_walker_s0**: Data incomplete — FAILED

#### **SGS Variants**
- **Reward-Only SGS (016e)**: Data incomplete, conclusion negative
- **Full-Pathway SGS (018v2)**: Peak 499.6, Final 448.3 (46% baseline) — Delayed collapse but ultimately FAILED
- **Full-Pathway SGS (018_s2)**: Complete collapse — FAILED
- **Obs-Decoder SGS**: Training failed across seeds

#### **Dual Critic**
- **exp_032 (Walker s0)**: Success (metrics incomplete in registry)
- **exp_032b (Walker s1)**: Success
- **exp_034 (Cheetah)**: Negative
- **exp_038 (Walker s2)**: Final 120.9, Peak 354 — FAILED
- **exp_041 (Walker s3)**: Final 544, Peak 761.1 — Success
- **exp_040 (Cheetah dual)**: Success

#### **Wide/Narrow Critic**
- **Wide Single Critic (Walker)**: Success
- **Wide Single Critic (Cheetah)**: Final 146.1, Peak 350.1 — FAILED
- **Narrow Dual Critic (Walker)**: Success

#### **Frozen dt_Embedding**
- **exp_042 (Walker)**: Success (no CIVO triggered)
- **exp_046 (Cheetah)**: Success
- **exp_047 (Walker s1)**: Success

#### **Removed Embedding (008f controls - "causal control")**
- **exp_008f seed 0**: Final 503 — Success (52% baseline)
- **exp_008f seed 3**: Final 363.8 — Success
- **exp_008f seed 4**: Final 306.5@105K (39% baseline) — Negative

#### **Untreated Baseline (008d - CIVO trigger)**
- **exp_008d seed 0**: Killed
- **exp_008d_civo_trigger_s3**: Final 267.6, Peak 451.7 — Success (shows CIVO)
- **exp_009b_008d seed 2**: Negative (CIVO onset ~2.0×)

### **Key Baseline Values:**
- Walker Walk baseline (no gate): ~788-969 eval_return
- Cheetah Run baseline (no gate): ~594-642 eval_return
- 008d untreated (CIVO): ~83-268 (severe collapse)
- 008f removed embedding: ~306-503 (stable, no CIVO)

### **File Locations for Raw Data:**

- `/artifacts/_project/data/summary_table.csv` - Primary compiled results
- `/artifacts/_project/data/cross_env_civo_comparison.csv` - Intervention summary
- `/artifacts/_project/paper/ablation_mechanism_table.tex` - Paper tables with mechanism evidence
- `/artifacts/nve_experiment_data.csv` - NVE diagnostic values (32 seeds)
- `/artifacts/figures_data/` - Learning curves and trajectories
- `/artifacts/analysis/negative_experiment_retrospective.md` - Detailed analysis of all negative results

All eval_return data for the intervention experiments you mentioned (TCN σ values, RAVE, SGS variants, dual/wide/narrow critics, frozen/removed embedding, and 008d baseline seeds) is compiled and available in the locations above.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "3d7a513b-c27a-46f3-b218-520c429769b5",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon, search for files that contain compiled experiment results, analysis data, or metrics summaries. I'm looking for data about these intervention experiments: TCN (sigma 0.1/0.2/0.5/1.0), RAVE, reward-only SGS, full-pathway SGS, obs-decoder SGS, wide/narrow/dual critic, frozen embedding, removed embedding, and the untreated (008d) baseline seeds.\n\nCheck:\n1. `artifacts/` directory for any CSV, JSON, or analysis files\n2. `docs/paper/` for any data tables or appendix files\n3. Any analysis scripts or notebooks\n4. Any `memory.md`, `ideas.md`, or report files in the project\n5. Log directories or summary files\n\nSearch \"very thorough\" breadth. I need the eval_return values for all these experiments.",
    "agentId": "a1f1cb7eaf4b2bda8",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the comprehensive data. Let me create a final summary document:\n\n## Summary\n\nI've completed a very thorough search of the event-gated-adaptive-horizon project and located comprehensive compiled experiment results. Here are the key findings:\n\n### **Main Data Sources Located:**\n\n1. **Registry File** (11,382 lines): `/registry.yaml` - Contains complete experiment metadata for all 200+ runs\n2. **Summary Tables** in `/artifacts/_project/data/`:\n   - `summary_table.csv` - Compiled eval_return values\n   - `metrics_table.csv` - Multi-step evaluation trajectories\n   - `cross_env_civo_comparison.csv` - Cross-environment intervention results\n   - `nve_4seed_robustness_analysis.csv` - Robustness across seeds\n3. **Analysis Files**: `/artifacts/analysis/` contains detailed negative experiment retrospectives and detector validation data\n4. **Memory & Reports**: Project-level memory.md and report.md with key metrics\n\n### **Intervention Experiment Results (eval_return@105K steps):**\n\n#### **TCN (Temporal Conditioning Noise)**\n- **σ=0.5 (Walker)**: 95.5 (12% baseline) — FAILED\n- **σ=0.2 (Walker s0)**: 236.4 (30% baseline) — success\n- **σ=0.2 (Walker s1)**: 319.4 (40% baseline) — success  \n- **σ=0.2 (Walker s2)**: 32.0 (4% baseline) — FAILED\n- **σ=0.1 (Walker)**: 204.7 (26% baseline) — FAILED\n- **σ=0.2 (Cheetah)**: Incomplete data\n- **σ=0.5 (Cheetah)**: 104.4 (18% baseline) — FAILED\n- **σ=1.0 (Cheetah)**: 122.5 (21% baseline) — FAILED\n\n#### **RAVE (Reality-Anchored Value Estimation)**\n- **exp_028_rave_walker_s0**: Data incomplete — FAILED\n\n#### **SGS Variants**\n- **Reward-Only SGS (016e)**: Data incomplete, conclusion negative\n- **Full-Pathway SGS (018v2)**: Peak 499.6, Final 448.3 (46% baseline) — Delayed collapse but ultimately FAILED\n- **Full-Pathway SGS (018_s2)**: Complete collapse — FAILED\n- **Obs-Decoder SGS**: Training failed across seeds\n\n#### **Dual Critic**\n- **exp_032 (Walker s0)**: Success (metrics incomplete in registry)\n- **exp_032b (Walker s1)**: Success\n- **exp_034 (Cheetah)**: Negative\n- **exp_038 (Walker s2)**: Final 120.9, Peak 354 — FAILED\n- **exp_041 (Walker s3)**: Final 544, Peak 761.1 — Success\n- **exp_040 (Cheetah dual)**: Success\n\n#### **Wide/Narrow Critic**\n- **Wide Single Critic (Walker)**: Success\n- **Wide Single Critic (Cheetah)**: Final 146.1, Peak 350.1 — FAILED\n- **Narrow Dual Critic (Walker)**: Success\n\n#### **Frozen dt_Embedding**\n- **exp_042 (Walker)**: Success (no CIVO triggered)\n- **exp_046 (Cheetah)**: Success\n- **exp_047 (Walker s1)**: Success\n\n#### **Removed Embedding (008f controls - \"causal control\")**\n- **exp_008f seed 0**: Final 503 — Success (52% baseline)\n- **exp_008f seed 3**: Final 363.8 — Success\n- **exp_008f seed 4**: Final 306.5@105K (39% baseline) — Negative\n\n#### **Untreated Baseline (008d - CIVO trigger)**\n- **exp_008d seed 0**: Killed\n- **exp_008d_civo_trigger_s3**: Final 267.6, Peak 451.7 — Success (shows CIVO)\n- **exp_009b_008d seed 2**: Negative (CIVO onset ~2.0×)\n\n### **Key Baseline Values:**\n- Walker Walk baseline (no gate): ~788-969 eval_return\n- Cheetah Run baseline (no gate): ~594-642 eval_return\n- 008d untreated (CIVO): ~83-268 (severe collapse)\n- 008f removed embedding: ~306-503 (stable, no CIVO)\n\n### **File Locations for Raw Data:**\n\n- `/artifacts/_project/data/summary_table.csv` - Primary compiled results\n- `/artifacts/_project/data/cross_env_civo_comparison.csv` - Intervention summary\n- `/artifacts/_project/paper/ablation_mechanism_table.tex` - Paper tables with mechanism evidence\n- `/artifacts/nve_experiment_data.csv` - NVE diagnostic values (32 seeds)\n- `/artifacts/figures_data/` - Learning curves and trajectories\n- `/artifacts/analysis/negative_experiment_retrospective.md` - Detailed analysis of all negative results\n\nAll eval_return data for the intervention experiments you mentioned (TCN σ values, RAVE, SGS variants, dual/wide/narrow critics, frozen/removed embedding, and 008d baseline seeds) is compiled and available in the locations above."
      }
    ],
    "totalDurationMs": 139857,
    "totalTokens": 87066,
    "totalToolUseCount": 37,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 6055,
      "cache_read_input_tokens": 79673,
      "output_tokens": 1338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6055
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 1338,
          "cache_read_input_tokens": 79673,
          "cache_creation_input_tokens": 6055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6055,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 0,
      "bashCount": 27,
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


### Assistant

_source line 148_

<details><summary>Logged reasoning block</summary>

```text
Good, there are several data sources. Let me look at the key files: `summary_table.csv`, `cross_env_civo_comparison.csv`, and the `registry.yaml` directly. Let me get the comprehensive eval_return data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "cc0eac7d-0382-461a-b33d-95df6c5faba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193L1onhUT4FzEm4NSu6jfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2005,
      "cache_read_input_tokens": 63866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2005
      },
      "output_tokens": 22,
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

_source line 149_

找到多个数据源。读取关键汇总文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "f553a847-c9fc-4200-bd67-336c0c1c958c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193L1onhUT4FzEm4NSu6jfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2005,
      "cache_read_input_tokens": 63866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2005
      },
      "output_tokens": 22,
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

_source line 150_

<details open><summary>🔧 Tool call — Bash · `toolu_01F1Gi2S5G43sReWFizDA5hL`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/ 2>/dev/null && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/ 2>/dev/null",
  "description": "List data directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "250f4b8c-a152-4b06-b8eb-1ec5cfb6ccec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193L1onhUT4FzEm4NSu6jfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2005,
      "cache_read_input_tokens": 63866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2005
      },
      "output_tokens": 22,
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

_source line 151 · 2026-05-29T00:37:54.652Z_

<details><summary>↩ Tool result · `toolu_01F1Gi2S5G43sReWFizDA5hL`</summary>

```text
actor_entropy_value_calibration_summary.txt
actor_loss_data.json
additional_figure_data_index.md
analysis_rssm_fidelity_v2.json
analysis_rssm_standardized_cheetah.json
analysis_rssm_standardized_walker.json
baseline_4seed_meta.txt
bootstrap_ci_results.json
bootstrap_ci_summary.md
bootstrap_cis.json
bootstrap_cis_8db708.json
bootstrap_cis_summary.txt
civo_detector_prospective_results.json
civo_detector_retrospective.json
civo_detector_retrospective_5b51de.json
cross_env_civo_comparison.csv
cross_env_civo_comparison.tex
detector_formal_validation_v3.json
detector_formal_validation_v3_9f711c.json
detector_threshold_analysis.json
gradient_decomposition_008d.json
gradient_decomposition_008d_corrected.json
gradient_decomposition_verification.json
learning_curves.csv
literature_map.yaml
metrics_table.csv
negative_cases_ve_data.json
nve_4seed_robustness_analysis.csv
nve_baseline_unification_log.md
nve_threshold_analysis.py
nve_threshold_sensitivity.json
nve_threshold_sensitivity.md
nve_threshold_sensitivity_20aa79.json
nve_threshold_v2_index.txt
nve_threshold_v3_ci_supplement.txt
nve_threshold_v3_ci_supplement_d054.txt
nve_threshold_v3_index.txt
nve_trajectories.csv
nve_trajectories_for_figure.json
paper_data_walker_walk_index.md
paper_figure_data_summary.txt
pickcube_ve_trajectory.json
results.json
rssm_fidelity_data.json
summary_table.csv
three_way_dt_emb_comparison.md
threshold_sensitivity.json
---
008e_dryrun_check.md
009b_literature_search.md
016e
018
018_prewrite_two_versions.md
018v2_server_check.md
019a
019a_dryrun_report.md
019b
_project
actor_entropy_analysis.md
actor_entropy_comparison.pdf
actor_entropy_comparison.png
actor_loss_timeseries.json
analysis
analysis_actor_entropy_plan031.md
analysis_civo_detector_pickcube_backtest.md
analysis_rssm_fidelity_v2.json
analysis_rssm_prediction_quality.json
analysis_rssm_standardized_cheetah.json
analysis_rssm_standardized_walker.json
auroc_label_fix_recompute.py
auroc_label_fix_report.md
auroc_label_fix_result.json
bernoulli_st_pessimism_designs.md
bootstrap_ci_n3.json
bootstrap_ci_results.json
bootstrap_cis
bootstrap_cis.json
camera_ready_checklist.md
check_037_038_status.md
checkpoint_monitor.py
civo_detector_retrospective.json
claim_strength_audit.md
code
code_correction_history.md
code_survey_dreamerv3.md
contingency_framing_B_C.md
d061_literature_linkage.md
d152_code_evolution_report.md
data
drafts
dream_reports
dt_embedding_cosine_similarity.png
eval_mvp.py
exp_001_baseline
exp_001_baseline_s1_ve_profile_full.csv
exp_001_baseline_s2_ext_ve_ratio_profile.csv
exp_001_baseline_s2_ve_profile_full.csv
exp_001_baseline_s3_ve_profile_full.csv
exp_001_baseline_s4_ve_profile_full.csv
exp_002_event_gated
exp_005_event_gated_v4
exp_006
exp_006_fixed_dt2
exp_008d_civo_trigger_s3
exp_008d_subsample_on_h8
exp_008e_v3_subsample_on_dt1_h15_s2
exp_008e_v3_walker_s2
exp_008f_s3
exp_009b_008d_walker_s2
exp_010a_cheetah_baseline_s1
exp_015
exp_018_full_sgs_walker_s1
exp_018v2_full_sgs_walker_s1
exp_019b_final_analysis.md
exp_019b_pickcube_civo_trigger
exp_021_full_sgs_cheetah_s1
exp_022_untrained_dt_emb_learned_gate
exp_022b
exp_023a_cheetah_baseline_s0
exp_023b_cheetah_baseline_s1
exp_024b_cheetah_no_dt_emb_s0
exp_027_tcn_walker_s0
exp_027_tcn_walker_s0_analysis.md
exp_031b_tcn_pickcube_s0_sigma05
exp_032_dual_critic_walker
exp_032b_dual_critic_walker_s1
exp_033_wide_critic_walker
exp_034
exp_034_dual_critic_cheetah
exp_035
exp_035_narrow_dual_critic_walker
exp_036_dual_critic_pickcube
exp_047_diagnosis.md
exp_061_cartpole_civo_trigger
exp_063_rssm_fidelity
exp_064_value_distribution
exp_065
exp_065_dt_emb_cosine
exp_066
exp_066_timeseries_rssm_fidelity
exp_067_frozen_dt_emb_walker_plan015
exp_069_008f_walker_repro_s1
exp_070_008e_v3_walker_s0
exp_071_008f_walker_s3
exp_072_008e_v3_walker_s5
exp_073_008f_walker_s4
exp_078_cheetah_008d_s0
exp_080_008e_v3_walker_s1
exp_081_008e_v3_walker_s2
exp_082_cheetah_no_dt_emb_s0
exp_083_cheetah_baseline_s1
exp_084_frozen_dt_emb_walker_s0
exp_085_frozen_dt_emb_walker_s1
exp_086_frozen_dt_emb_cheetah_s0
exp_086_orphan_cleanup_v2_report.md
exp_087_frozen_dt_emb_cheetah_s1
exp_101
exp_cheetah_008a_s0
exp_cheetah_008a_s1
exp_hopper_frozen_s0
exp_hopper_frozen_s0_ext
exp_hopper_no_dt_emb_s0
exp_hopper_trained_s0_ext
exp_walker_no_dt_emb_s1
figures
figures_data
framing_b_reaudit_diff.md
frozen_dt_emb_narrative_prep.md
gen_bib.py
gpu_deployment_plan_20260521.md
gradient_stopping_code_audit.md
hopper_comprehensive_analysis_draft.md
icml_compliance_results.md
imagination_reward_analysis.md
implementation_design.md
literature
literature_gap_analysis_20260514.md
literature_map.yaml
literature_scan_20260515.md
literature_sgs_survey.md
literature_survey_summary.md
manifest.yaml
maniskill3_cuda_workaround.md
maniskill3_dreamer_integration.md
maniskill3_integration_report.md
method_framingB_reaudit_v2.md
method_section_draft.md
metrics_summary_table.md
narrative_audit.md
negative_pattern_analysis.md
negative_results_insights.md
negative_results_taxonomy.md
nve_experiment_data.csv
nve_loeo_crossval_report.md
nve_roc_curve.pdf
nve_roc_curve.png
nve_sensitivity_analysis.md
nve_threshold_analysis.json
nve_threshold_analysis_v3.py
nve_threshold_prf.pdf
nve_threshold_prf.png
nve_threshold_sensitivity.csv
nve_threshold_sensitivity.json
nve_threshold_sensitivity.md
nve_threshold_sensitivity.py
nve_threshold_sensitivity.tex
nve_threshold_v3_ci_supplement_d054.json
paper_data_audit_20260526.md
paper_drafts
paper_figures
paper_section_audit.md
paper_sections
pessimism_mechanism_design.md
pickcube_ve_trajectory.json
pivot_gate_survey.md
plan_030_rssm_quality
plan_031_actor_entropy
plan_033
plan_033_dt_emb_cosine
plan_034_nve_threshold
plot_figures.py
preflight_008e_v3_s2.md
progress_check_20260515.md
progress_check_20260525.md
rebuttal_draft.md
rebuttal_prep.md
rebuttal_prep_r7.md
reference_audit_results.md
related_work_draft.md
related_work_expansion.md
related_work_expansion.yaml
related_work_refs.yaml
report_server_status.md
review_issues.yaml
review_reports
review_round_3
review_round_4
review_round_5
review_round_6
review_round_7
rssm_fidelity_analysis.md
rssm_prediction_quality_analysis.json
scripts
seed_label_diff_summary.md
sgs_implementation_report.md
signed_reward_error.md
submission_checklist.md
submission_checklist_v2.md
supplement_completeness_results.md
supplementary
supplementary.zip
supplementary_checklist.md
supplementary_framework.md
table5_validation
tables
three_way_dt_emb_comparison.md
training_progress_check_20260514.md
value_distribution_analysis.md
value_vs_returns.json
value_vs_returns.pdf
value_vs_returns.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "60e344ee-6a68-401a-bf4a-850f76c4794b",
  "tool_use_result": {
    "stdout": "actor_entropy_value_calibration_summary.txt\nactor_loss_data.json\nadditional_figure_data_index.md\nanalysis_rssm_fidelity_v2.json\nanalysis_rssm_standardized_cheetah.json\nanalysis_rssm_standardized_walker.json\nbaseline_4seed_meta.txt\nbootstrap_ci_results.json\nbootstrap_ci_summary.md\nbootstrap_cis.json\nbootstrap_cis_8db708.json\nbootstrap_cis_summary.txt\ncivo_detector_prospective_results.json\ncivo_detector_retrospective.json\ncivo_detector_retrospective_5b51de.json\ncross_env_civo_comparison.csv\ncross_env_civo_comparison.tex\ndetector_formal_validation_v3.json\ndetector_formal_validation_v3_9f711c.json\ndetector_threshold_analysis.json\ngradient_decomposition_008d.json\ngradient_decomposition_008d_corrected.json\ngradient_decomposition_verification.json\nlearning_curves.csv\nliterature_map.yaml\nmetrics_table.csv\nnegative_cases_ve_data.json\nnve_4seed_robustness_analysis.csv\nnve_baseline_unification_log.md\nnve_threshold_analysis.py\nnve_threshold_sensitivity.json\nnve_threshold_sensitivity.md\nnve_threshold_sensitivity_20aa79.json\nnve_threshold_v2_index.txt\nnve_threshold_v3_ci_supplement.txt\nnve_threshold_v3_ci_supplement_d054.txt\nnve_threshold_v3_index.txt\nnve_trajectories.csv\nnve_trajectories_for_figure.json\npaper_data_walker_walk_index.md\npaper_figure_data_summary.txt\npickcube_ve_trajectory.json\nresults.json\nrssm_fidelity_data.json\nsummary_table.csv\nthree_way_dt_emb_comparison.md\nthreshold_sensitivity.json\n---\n008e_dryrun_check.md\n009b_literature_search.md\n016e\n018\n018_prewrite_two_versions.md\n018v2_server_check.md\n019a\n019a_dryrun_report.md\n019b\n_project\nactor_entropy_analysis.md\nactor_entropy_comparison.pdf\nactor_entropy_comparison.png\nactor_loss_timeseries.json\nanalysis\nanalysis_actor_entropy_plan031.md\nanalysis_civo_detector_pickcube_backtest.md\nanalysis_rssm_fidelity_v2.json\nanalysis_rssm_prediction_quality.json\nanalysis_rssm_standardized_cheetah.json\nanalysis_rssm_standardized_walker.json\nauroc_label_fix_recompute.py\nauroc_label_fix_report.md\nauroc_label_fix_result.json\nbernoulli_st_pessimism_designs.md\nbootstrap_ci_n3.json\nbootstrap_ci_results.json\nbootstrap_cis\nbootstrap_cis.json\ncamera_ready_checklist.md\ncheck_037_038_status.md\ncheckpoint_monitor.py\ncivo_detector_retrospective.json\nclaim_strength_audit.md\ncode\ncode_correction_history.md\ncode_survey_dreamerv3.md\ncontingency_framing_B_C.md\nd061_literature_linkage.md\nd152_code_evolution_report.md\ndata\ndrafts\ndream_reports\ndt_embedding_cosine_similarity.png\neval_mvp.py\nexp_001_baseline\nexp_001_baseline_s1_ve_profile_full.csv\nexp_001_baseline_s2_ext_ve_ratio_profile.csv\nexp_001_baseline_s2_ve_profile_full.csv\nexp_001_baseline_s3_ve_profile_full.csv\nexp_001_baseline_s4_ve_profile_full.csv\nexp_002_event_gated\nexp_005_event_gated_v4\nexp_006\nexp_006_fixed_dt2\nexp_008d_civo_trigger_s3\nexp_008d_subsample_on_h8\nexp_008e_v3_subsample_on_dt1_h15_s2\nexp_008e_v3_walker_s2\nexp_008f_s3\nexp_009b_008d_walker_s2\nexp_010a_cheetah_baseline_s1\nexp_015\nexp_018_full_sgs_walker_s1\nexp_018v2_full_sgs_walker_s1\nexp_019b_final_analysis.md\nexp_019b_pickcube_civo_trigger\nexp_021_full_sgs_cheetah_s1\nexp_022_untrained_dt_emb_learned_gate\nexp_022b\nexp_023a_cheetah_baseline_s0\nexp_023b_cheetah_baseline_s1\nexp_024b_cheetah_no_dt_emb_s0\nexp_027_tcn_walker_s0\nexp_027_tcn_walker_s0_analysis.md\nexp_031b_tcn_pickcube_s0_sigma05\nexp_032_dual_critic_walker\nexp_032b_dual_critic_walker_s1\nexp_033_wide_critic_walker\nexp_034\nexp_034_dual_critic_cheetah\nexp_035\nexp_035_narrow_dual_critic_walker\nexp_036_dual_critic_pickcube\nexp_047_diagnosis.md\nexp_061_cartpole_civo_trigger\nexp_063_rssm_fidelity\nexp_064_value_distribution\nexp_065\nexp_065_dt_emb_cosine\nexp_066\nexp_066_timeseries_rssm_fidelity\nexp_067_frozen_dt_emb_walker_plan015\nexp_069_008f_walker_repro_s1\nexp_070_008e_v3_walker_s0\nexp_071_008f_walker_s3\nexp_072_008e_v3_walker_s5\nexp_073_008f_walker_s4\nexp_078_cheetah_008d_s0\nexp_080_008e_v3_walker_s1\nexp_081_008e_v3_walker_s2\nexp_082_cheetah_no_dt_emb_s0\nexp_083_cheetah_baseline_s1\nexp_084_frozen_dt_emb_walker_s0\nexp_085_frozen_dt_emb_walker_s1\nexp_086_frozen_dt_emb_cheetah_s0\nexp_086_orphan_cleanup_v2_report.md\nexp_087_frozen_dt_emb_cheetah_s1\nexp_101\nexp_cheetah_008a_s0\nexp_cheetah_008a_s1\nexp_hopper_frozen_s0\nexp_hopper_frozen_s0_ext\nexp_hopper_no_dt_emb_s0\nexp_hopper_trained_s0_ext\nexp_walker_no_dt_emb_s1\nfigures\nfigures_data\nframing_b_reaudit_diff.md\nfrozen_dt_emb_narrative_prep.md\ngen_bib.py\ngpu_deployment_plan_20260521.md\ngradient_stopping_code_audit.md\nhopper_comprehensive_analysis_draft.md\nicml_compliance_results.md\nimagination_reward_analysis.md\nimplementation_design.md\nliterature\nliterature_gap_analysis_20260514.md\nliterature_map.yaml\nliterature_scan_20260515.md\nliterature_sgs_survey.md\nliterature_survey_summary.md\nmanifest.yaml\nmaniskill3_cuda_workaround.md\nmaniskill3_dreamer_integration.md\nmaniskill3_integration_report.md\nmethod_framingB_reaudit_v2.md\nmethod_section_draft.md\nmetrics_summary_table.md\nnarrative_audit.md\nnegative_pattern_analysis.md\nnegative_results_insights.md\nnegative_results_taxonomy.md\nnve_experiment_data.csv\nnve_loeo_crossval_report.md\nnve_roc_curve.pdf\nnve_roc_curve.png\nnve_sensitivity_analysis.md\nnve_threshold_analysis.json\nnve_threshold_analysis_v3.py\nnve_threshold_prf.pdf\nnve_threshold_prf.png\nnve_threshold_sensitivity.csv\nnve_threshold_sensitivity.json\nnve_threshold_sensitivity.md\nnve_threshold_sensitivity.py\nnve_threshold_sensitivity.tex\nnve_threshold_v3_ci_supplement_d054.json\npaper_data_audit_20260526.md\npaper_drafts\npaper_figures\npaper_section_audit.md\npaper_sections\npessimism_mechanism_design.md\npickcube_ve_trajectory.json\npivot_gate_survey.md\nplan_030_rssm_quality\nplan_031_actor_entropy\nplan_033\nplan_033_dt_emb_cosine\nplan_034_nve_threshold\nplot_figures.py\npreflight_008e_v3_s2.md\nprogress_check_20260515.md\nprogress_check_20260525.md\nrebuttal_draft.md\nrebuttal_prep.md\nrebuttal_prep_r7.md\nreference_audit_results.md\nrelated_work_draft.md\nrelated_work_expansion.md\nrelated_work_expansion.yaml\nrelated_work_refs.yaml\nreport_server_status.md\nreview_issues.yaml\nreview_reports\nreview_round_3\nreview_round_4\nreview_round_5\nreview_round_6\nreview_round_7\nrssm_fidelity_analysis.md\nrssm_prediction_quality_analysis.json\nscripts\nseed_label_diff_summary.md\nsgs_implementation_report.md\nsigned_reward_error.md\nsubmission_checklist.md\nsubmission_checklist_v2.md\nsupplement_completeness_results.md\nsupplementary\nsupplementary.zip\nsupplementary_checklist.md\nsupplementary_framework.md\ntable5_validation\ntables\nthree_way_dt_emb_comparison.md\ntraining_progress_check_20260514.md\nvalue_distribution_analysis.md\nvalue_vs_returns.json\nvalue_vs_returns.pdf\nvalue_vs_returns.png",
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

_source line 152_

<details open><summary>🔧 Tool call — Read · `toolu_01JxEk7REqpTz39MAtxMdmmF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/summary_table.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "aefdad60-2894-4aeb-904f-7644d04d2996",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Wmoii5abcVZJrQGSg3otg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 65871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2865
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

_source line 153 · 2026-05-29T00:37:57.644Z_

<details><summary>↩ Tool result · `toolu_01JxEk7REqpTz39MAtxMdmmF`</summary>

```text
1	exp_id,config_label,hypothesis,conclusion,final_eval_return,peak_eval_return,final_ve_ratio,final_nve,vs_baseline_pct,seed,total_steps
2	exp_001_baseline,baseline (seed 0),DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model,success,970.41,970.41,0.656,1.0,0.0,1,512000
3	exp_009a_baseline_walker_s2,baseline (seed 2),Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）,,948.4,966.9,,,-0.52,2,448000
4	exp_006_fixed_dt2,dt=2 fixed (006),诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。,negative,132.86,485.3,2.722,4.8348,-78.42,1,65000
5	exp_007_fixed_dt4,dt=4 fixed (007),诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。,negative,152.49,176.9,0.061,0.151,-75.63,1,55000
6	exp_005_event_gated_v4,learned gate (005),,negative,98.84,541.18,,,-89.40,1,145000
7	exp_008d_subsample_on_h8,trained dt_emb H=8 (008d) seed 0/1,,negative,82.75,167.22,1.666,4.1238,-86.78,1,55000
8	exp_009b_008d_walker_s2,trained dt_emb H=8 (008d) seed 2,Walker Walk trained dt_emb + subsample ON + H=8 seed 2 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）,negative,267.93,278.54,0.251,0.38,-70.74,2,105000
9	exp_008f_no_dt_embed_subsample_on_h8,no dt_emb (008f) seed 0/1,"C2 confound control：隔离 dt_embedding conditioning vs RSSM learned dt=2 dynamics。subsample ON + dt=2 imagination + H=8（与 008d 完全一致），但 gate_dt_embed_dim=0（去掉 dt_embedding 条件输入）。如果 008f 崩塌（v/e >50%）→ 根因是 RSSM 的 dt=2 训练数据导致 dynamics 偏差，不是 dt_embedding per se。如果 008f 稳定（v/e <35%）→ 确认 dt_embedding conditioning 是 delusional critic 的直接原因。对照：008d（dt_embed_dim>0, v/e 15.5%→41.2%→69.3% 崩塌）vs 008c（subsample OFF, untrained dt_emb, v/e 稳定 ~22-33%）。",success,503,503,0.1952,0.3,-45.08,1,105000
10	exp_009c_008f_walker_s2,no dt_emb (008f) seed 2,Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）,negative,148.34,359.14,0.75,1.14,-83.80,2,105000
11	exp_008c_no_subsample_dt2_h8,untrained dt_emb dt=2 H=8 (008c),隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。,negative,240.86,241.87,0.328,0.5826,-60.89,1,68000
12	exp_008a_no_subsample_dt2,untrained dt_emb dt=2 H=15 (008a),隔离 subsample 效应：subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。,success,777.66,777.66,0.386,0.59,-15.07,1,112000
13	exp_008e_v3_walker_s1,dt=1 imag (008e_v3) seed 1,Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）,success,869.9,869.9,0.527,0.8034,-5.00,1,112000
14	exp_008e_v3_walker_s2,dt=1 imag (008e_v3) seed 2,Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证,,435.1,435.1,0.507,0.9005,-29.36,2,68000
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "b0859ff3-f4f0-4933-aa3d-43b76ce518ae",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/summary_table.csv",
      "content": "exp_id,config_label,hypothesis,conclusion,final_eval_return,peak_eval_return,final_ve_ratio,final_nve,vs_baseline_pct,seed,total_steps\nexp_001_baseline,baseline (seed 0),DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model,success,970.41,970.41,0.656,1.0,0.0,1,512000\nexp_009a_baseline_walker_s2,baseline (seed 2),Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）,,948.4,966.9,,,-0.52,2,448000\nexp_006_fixed_dt2,dt=2 fixed (006),诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。,negative,132.86,485.3,2.722,4.8348,-78.42,1,65000\nexp_007_fixed_dt4,dt=4 fixed (007),诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。,negative,152.49,176.9,0.061,0.151,-75.63,1,55000\nexp_005_event_gated_v4,learned gate (005),,negative,98.84,541.18,,,-89.40,1,145000\nexp_008d_subsample_on_h8,trained dt_emb H=8 (008d) seed 0/1,,negative,82.75,167.22,1.666,4.1238,-86.78,1,55000\nexp_009b_008d_walker_s2,trained dt_emb H=8 (008d) seed 2,Walker Walk trained dt_emb + subsample ON + H=8 seed 2 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）,negative,267.93,278.54,0.251,0.38,-70.74,2,105000\nexp_008f_no_dt_embed_subsample_on_h8,no dt_emb (008f) seed 0/1,\"C2 confound control：隔离 dt_embedding conditioning vs RSSM learned dt=2 dynamics。subsample ON + dt=2 imagination + H=8（与 008d 完全一致），但 gate_dt_embed_dim=0（去掉 dt_embedding 条件输入）。如果 008f 崩塌（v/e >50%）→ 根因是 RSSM 的 dt=2 训练数据导致 dynamics 偏差，不是 dt_embedding per se。如果 008f 稳定（v/e <35%）→ 确认 dt_embedding conditioning 是 delusional critic 的直接原因。对照：008d（dt_embed_dim>0, v/e 15.5%→41.2%→69.3% 崩塌）vs 008c（subsample OFF, untrained dt_emb, v/e 稳定 ~22-33%）。\",success,503,503,0.1952,0.3,-45.08,1,105000\nexp_009c_008f_walker_s2,no dt_emb (008f) seed 2,Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）,negative,148.34,359.14,0.75,1.14,-83.80,2,105000\nexp_008c_no_subsample_dt2_h8,untrained dt_emb dt=2 H=8 (008c),隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。,negative,240.86,241.87,0.328,0.5826,-60.89,1,68000\nexp_008a_no_subsample_dt2,untrained dt_emb dt=2 H=15 (008a),隔离 subsample 效应：subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。,success,777.66,777.66,0.386,0.59,-15.07,1,112000\nexp_008e_v3_walker_s1,dt=1 imag (008e_v3) seed 1,Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）,success,869.9,869.9,0.527,0.8034,-5.00,1,112000\nexp_008e_v3_walker_s2,dt=1 imag (008e_v3) seed 2,Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证,,435.1,435.1,0.507,0.9005,-29.36,2,68000\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  }
}
```

</details>

---


### Tool call

_source line 154_

<details open><summary>🔧 Tool call — Read · `toolu_01Qvq6oMj3duhr8kKuk1XAtS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/cross_env_civo_comparison.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ae4e1912-4c0d-41c9-9084-26a1b4eaade4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Wmoii5abcVZJrQGSg3otg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 65871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2865
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

_source line 155 · 2026-05-29T00:37:58.034Z_

<details><summary>↩ Tool result · `toolu_01Qvq6oMj3duhr8kKuk1XAtS`</summary>

```text
1	Environment,Configuration,Eval Return (mean),Eval Return (std),Seeds (eval),NVE Peak (max),Seeds (NVE),CIVO,Source Experiments
2	Walker Walk,Baseline (dt=1),787.7,230.8,4,—,—,—,"exp_001_baseline (s0=915.67), exp_001_baseline_s2 (443.46), exp_001_baseline_s3 (869.03), exp_001_baseline_s4 (922.80)"
3	Walker Walk,Trigger (trained dt_emb),140.6,111.5,3,4.72,5,Yes (5/5),"exp_008d (s0: eval@112K=58.5), exp_008d_civo_trigger_s3 (267.6), exp_059_walker_trained_s5 (95.8); NVE: s1=4.13 s2=1.62 s3=1.53 s4=4.62 s5=4.72"
4	Walker Walk,Control (no dt_emb),373.8,111.9,3,1.41,4,No (0/4),"exp_008f (s0=503), exp_009c_s3 (311.92), exp_008f_s4 (306.50); NVE: s0=0.30 s1=0.81 s3=0.52 s4=1.41"
5	Cheetah Run,Baseline (dt=1),593.9,60.4,5,—,—,—,"exp_023a (624.7), exp_023b (520.3), exp_023_s2 (645.4), exp_023_s3 (642.13), exp_023_s4 (537.03)"
6	Cheetah Run,Trigger (trained dt_emb),26.3,36.0,2,70.64,2,Yes (2/2),"exp_010b_s0 (eval=0.83 NVE=70.64), exp_010b_s1 (eval=51.7 NVE=8.27)"
7	Cheetah Run,Control (no dt_emb),86.9,13.6,2,0.20,2,No (0/2),"exp_024b_s0 (eval=96.5 NVE=0.20), exp_024b_s1 (eval=77.3 NVE=0.10)"
8	Cartpole Swingup,Baseline (dt=1),673.3,142.0,3,—,—,—,"exp_060 s0=809.4 s1=684.4 s2=526.1"
9	Cartpole Swingup,Trigger (trained dt_emb),236.3,29.7,3,0.06,3,No (0/3),"exp_061 s0=211.1 (VE=0.058) s1=269.0 (VE=0.040) s2=228.9 (VE=0.043)"
10	Cartpole Swingup,Control (no dt_emb),—,—,0,—,—,—,exp_062 (RUNNING)
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "1509bf0e-09e4-4201-9684-d0da63becca2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/cross_env_civo_comparison.csv",
      "content": "Environment,Configuration,Eval Return (mean),Eval Return (std),Seeds (eval),NVE Peak (max),Seeds (NVE),CIVO,Source Experiments\nWalker Walk,Baseline (dt=1),787.7,230.8,4,—,—,—,\"exp_001_baseline (s0=915.67), exp_001_baseline_s2 (443.46), exp_001_baseline_s3 (869.03), exp_001_baseline_s4 (922.80)\"\nWalker Walk,Trigger (trained dt_emb),140.6,111.5,3,4.72,5,Yes (5/5),\"exp_008d (s0: eval@112K=58.5), exp_008d_civo_trigger_s3 (267.6), exp_059_walker_trained_s5 (95.8); NVE: s1=4.13 s2=1.62 s3=1.53 s4=4.62 s5=4.72\"\nWalker Walk,Control (no dt_emb),373.8,111.9,3,1.41,4,No (0/4),\"exp_008f (s0=503), exp_009c_s3 (311.92), exp_008f_s4 (306.50); NVE: s0=0.30 s1=0.81 s3=0.52 s4=1.41\"\nCheetah Run,Baseline (dt=1),593.9,60.4,5,—,—,—,\"exp_023a (624.7), exp_023b (520.3), exp_023_s2 (645.4), exp_023_s3 (642.13), exp_023_s4 (537.03)\"\nCheetah Run,Trigger (trained dt_emb),26.3,36.0,2,70.64,2,Yes (2/2),\"exp_010b_s0 (eval=0.83 NVE=70.64), exp_010b_s1 (eval=51.7 NVE=8.27)\"\nCheetah Run,Control (no dt_emb),86.9,13.6,2,0.20,2,No (0/2),\"exp_024b_s0 (eval=96.5 NVE=0.20), exp_024b_s1 (eval=77.3 NVE=0.10)\"\nCartpole Swingup,Baseline (dt=1),673.3,142.0,3,—,—,—,\"exp_060 s0=809.4 s1=684.4 s2=526.1\"\nCartpole Swingup,Trigger (trained dt_emb),236.3,29.7,3,0.06,3,No (0/3),\"exp_061 s0=211.1 (VE=0.058) s1=269.0 (VE=0.040) s2=228.9 (VE=0.043)\"\nCartpole Swingup,Control (no dt_emb),—,—,0,—,—,—,exp_062 (RUNNING)\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---


### Assistant

_source line 156_

<details><summary>Logged reasoning block</summary>

```text
The `cross_env_civo_comparison.csv` has some useful baselines, but it doesn't have the intervention-level data I need for Table 2. I need to look at the `nve_experiment_data.csv` and possibly the raw metrics from the artifacts directory for each experiment. Let me also look at the registry.yaml which might have all experiments.

Let me focus on getting the eval_return data for each Table 2 group. I need to find data for experiments that are not in the main registry. 

I should dig into the individual experiment artifact directories to find the detailed metrics I'm missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a0926ab4-6118-4ab1-a96a-e4b9845c527b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nfgcswn7oVTd1qXHiPUAEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2761,
      "cache_read_input_tokens": 68736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2761
      },
      "output_tokens": 24,
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

_source line 157_

<details open><summary>🔧 Tool call — Read · `toolu_01GiPrvaSdS3MiY75PX4rdwx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "29309045-5853-4866-9427-8e81a3c01d2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nfgcswn7oVTd1qXHiPUAEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2761,
      "cache_read_input_tokens": 68736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2761
      },
      "output_tokens": 24,
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

_source line 158 · 2026-05-29T00:38:04.326Z_

<details><summary>↩ Tool result · `toolu_01GiPrvaSdS3MiY75PX4rdwx`</summary>

```text
1	exp_id,nve_peak,ground_truth,env,config_type
2	exp_008d/009e (Walker s1),4.13,1,Walker,trained
3	exp_009b (Walker s2),1.62,1,Walker,trained
4	exp_008d_s3 (Walker s3),1.53,1,Walker,trained
5	exp_008d_s4 (Walker s4),4.62,1,Walker,trained
6	exp_059 (Walker s5),4.72,1,Walker,trained
7	exp_048 (Cheetah s0),70.64,1,Cheetah,trained
8	exp_010b (Cheetah s1),8.27,1,Cheetah,trained
9	exp_008f (Walker s0 no_dt_emb),1.02,0,Walker,no_dt_emb
10	exp_009c (Walker s2 no_dt_emb),1.26,0,Walker,no_dt_emb
11	exp_008f_s3 (Walker s3 no_dt_emb),1.2,0,Walker,no_dt_emb
12	exp_008f_s4 (Walker s4 no_dt_emb),1.41,0,Walker,no_dt_emb
13	exp_009c_s3 (Walker s3 no_dt_emb #2),0.52,0,Walker,no_dt_emb
14	exp_042 (Walker s0 frozen),0.194,0,Walker,frozen
15	exp_047 (Walker s1 frozen),1.71,0,Walker,frozen
16	exp_057 (Walker s2 frozen),1.88,0,Walker,frozen
17	exp_046 (Cheetah s0 frozen),1.35,0,Cheetah,frozen
18	exp_058 (Cheetah s1 frozen),0.78,0,Cheetah,frozen
19	exp_024b_s0 (Cheetah s0 no_dt_emb),0.2,0,Cheetah,no_dt_emb
20	exp_024b_s1 (Cheetah s1 no_dt_emb),0.1,0,Cheetah,no_dt_emb
21	exp_060 (Cartpole baseline),1.0,0,Cartpole,baseline
22	exp_061 (Cartpole trained dt_emb),0.9,0,Cartpole,trained
23	exp_062 (Cartpole no_dt_emb),1.0,0,Cartpole,no_dt_emb
24	exp_001_s1 (Walker baseline),1.0,0,Walker,baseline
25	exp_001_s2 (Walker baseline),1.13,0,Walker,baseline
26	exp_001_s3 (Walker baseline),1.05,0,Walker,baseline
27	exp_001_s4 (Walker baseline),0.95,0,Walker,baseline
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "39dbb4e8-43a6-4ac7-8e3c-4259ff612854",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_experiment_data.csv",
      "content": "exp_id,nve_peak,ground_truth,env,config_type\nexp_008d/009e (Walker s1),4.13,1,Walker,trained\nexp_009b (Walker s2),1.62,1,Walker,trained\nexp_008d_s3 (Walker s3),1.53,1,Walker,trained\nexp_008d_s4 (Walker s4),4.62,1,Walker,trained\nexp_059 (Walker s5),4.72,1,Walker,trained\nexp_048 (Cheetah s0),70.64,1,Cheetah,trained\nexp_010b (Cheetah s1),8.27,1,Cheetah,trained\nexp_008f (Walker s0 no_dt_emb),1.02,0,Walker,no_dt_emb\nexp_009c (Walker s2 no_dt_emb),1.26,0,Walker,no_dt_emb\nexp_008f_s3 (Walker s3 no_dt_emb),1.2,0,Walker,no_dt_emb\nexp_008f_s4 (Walker s4 no_dt_emb),1.41,0,Walker,no_dt_emb\nexp_009c_s3 (Walker s3 no_dt_emb #2),0.52,0,Walker,no_dt_emb\nexp_042 (Walker s0 frozen),0.194,0,Walker,frozen\nexp_047 (Walker s1 frozen),1.71,0,Walker,frozen\nexp_057 (Walker s2 frozen),1.88,0,Walker,frozen\nexp_046 (Cheetah s0 frozen),1.35,0,Cheetah,frozen\nexp_058 (Cheetah s1 frozen),0.78,0,Cheetah,frozen\nexp_024b_s0 (Cheetah s0 no_dt_emb),0.2,0,Cheetah,no_dt_emb\nexp_024b_s1 (Cheetah s1 no_dt_emb),0.1,0,Cheetah,no_dt_emb\nexp_060 (Cartpole baseline),1.0,0,Cartpole,baseline\nexp_061 (Cartpole trained dt_emb),0.9,0,Cartpole,trained\nexp_062 (Cartpole no_dt_emb),1.0,0,Cartpole,no_dt_emb\nexp_001_s1 (Walker baseline),1.0,0,Walker,baseline\nexp_001_s2 (Walker baseline),1.13,0,Walker,baseline\nexp_001_s3 (Walker baseline),1.05,0,Walker,baseline\nexp_001_s4 (Walker baseline),0.95,0,Walker,baseline\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---


### Tool call

_source line 159_

<details open><summary>🔧 Tool call — Read · `toolu_01S5XNt696N4Mhp4bPK61VTt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/metrics_table.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "4928bcf9-5a56-4b69-aec7-683aac3e8d54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nfgcswn7oVTd1qXHiPUAEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2761,
      "cache_read_input_tokens": 68736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2761
      },
      "output_tokens": 24,
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

_source line 160 · 2026-05-29T00:38:04.609Z_

<details><summary>↩ Tool result · `toolu_01S5XNt696N4Mhp4bPK61VTt`</summary>

```text
1	exp_id,gate_enabled,subsample,fixed_dt,imag_horizon,dt_embed_dim,seed,status,eval_final,eval_peak,ve_35k,ve_45k,ve_65k,ve_105k,nve_35k,nve_45k,nve_65k,nve_105k,gate_dt_mean_final,gate_dt_1_frac_final,claims
2	exp_001_baseline,OFF,OFF,1,15,N/A,1,done/success,970.41,970.41,0.2412,0.3310,0.5629,0.6564,1.00,1.00,1.00,1.00,N/A,N/A,ref
3	exp_009a_baseline_s2,OFF,OFF,1,15,N/A,2,running,948.42,966.94,0.3056,0.3629,0.4737,0.6447,1.27,1.10,0.84,0.98,N/A,N/A,ref
4	exp_008a,ON,OFF,2,15,32,1,done/success,777.66,777.66,0.1571,0.2342,0.3719,0.3861,0.65,0.71,0.66,0.59,2.0,0.0,C3
5	exp_008c,ON,OFF,2,8,32,1,done/negative,240.86,241.87,0.2184,0.2537,0.3278,,0.91,0.77,0.58,,2.0,0.0,C3
6	exp_008d,ON,ON,2,8,32,1,done/negative,82.75,167.22,0.4113,0.6929,,,1.71,2.09,,,2.0,0.0,"C1,C2"
7	exp_008e_v3,ON,ON,1,15,32,1,done/success,869.88,869.88,0.2270,0.2895,0.4048,0.5264,0.94,0.87,0.72,0.80,1.0,1.0,C6
8	exp_008f,ON,ON,2,8,0,1,done/success,503.21,503.21,0.1755,0.2753,0.2067,0.1952,0.73,0.83,0.37,0.30,2.0,0.0,"C1,C2"
9	exp_009b_008d_s2,ON,ON,2,8,32,2,done/negative,267.93,278.54,0.2986,0.5359,0.5303,0.2511,1.24,1.62,0.94,0.38,2.0,0.0,"C1,C2"
10	exp_009c_008f_s2,ON,ON,2,8,0,2,done/negative,148.34,359.14,0.1915,0.2373,0.2978,0.7499,0.79,0.72,0.53,1.14,2.0,0.0,"C1,C2"
11	exp_008e_v3_s2,ON,ON,1,15,32,2,running,435.09,435.09,0.2489,0.3509,0.5067,,1.03,1.06,0.90,,1.0,1.0,C6
12	exp_006_fixed_dt2,ON,OFF,2,15,32,1,done/negative,132.86,485.33,0.3113,0.5331,2.7224,,1.29,1.61,4.84,,2.0,0.0,diagnostic
13	exp_007_fixed_dt4,ON,OFF,4,15,32,1,done/negative,152.49,176.90,,,,,,,,4.0,,diagnostic
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "6e307764-df08-4e9a-89fa-d3ea9db27903",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/metrics_table.csv",
      "content": "exp_id,gate_enabled,subsample,fixed_dt,imag_horizon,dt_embed_dim,seed,status,eval_final,eval_peak,ve_35k,ve_45k,ve_65k,ve_105k,nve_35k,nve_45k,nve_65k,nve_105k,gate_dt_mean_final,gate_dt_1_frac_final,claims\nexp_001_baseline,OFF,OFF,1,15,N/A,1,done/success,970.41,970.41,0.2412,0.3310,0.5629,0.6564,1.00,1.00,1.00,1.00,N/A,N/A,ref\nexp_009a_baseline_s2,OFF,OFF,1,15,N/A,2,running,948.42,966.94,0.3056,0.3629,0.4737,0.6447,1.27,1.10,0.84,0.98,N/A,N/A,ref\nexp_008a,ON,OFF,2,15,32,1,done/success,777.66,777.66,0.1571,0.2342,0.3719,0.3861,0.65,0.71,0.66,0.59,2.0,0.0,C3\nexp_008c,ON,OFF,2,8,32,1,done/negative,240.86,241.87,0.2184,0.2537,0.3278,,0.91,0.77,0.58,,2.0,0.0,C3\nexp_008d,ON,ON,2,8,32,1,done/negative,82.75,167.22,0.4113,0.6929,,,1.71,2.09,,,2.0,0.0,\"C1,C2\"\nexp_008e_v3,ON,ON,1,15,32,1,done/success,869.88,869.88,0.2270,0.2895,0.4048,0.5264,0.94,0.87,0.72,0.80,1.0,1.0,C6\nexp_008f,ON,ON,2,8,0,1,done/success,503.21,503.21,0.1755,0.2753,0.2067,0.1952,0.73,0.83,0.37,0.30,2.0,0.0,\"C1,C2\"\nexp_009b_008d_s2,ON,ON,2,8,32,2,done/negative,267.93,278.54,0.2986,0.5359,0.5303,0.2511,1.24,1.62,0.94,0.38,2.0,0.0,\"C1,C2\"\nexp_009c_008f_s2,ON,ON,2,8,0,2,done/negative,148.34,359.14,0.1915,0.2373,0.2978,0.7499,0.79,0.72,0.53,1.14,2.0,0.0,\"C1,C2\"\nexp_008e_v3_s2,ON,ON,1,15,32,2,running,435.09,435.09,0.2489,0.3509,0.5067,,1.03,1.06,0.90,,1.0,1.0,C6\nexp_006_fixed_dt2,ON,OFF,2,15,32,1,done/negative,132.86,485.33,0.3113,0.5331,2.7224,,1.29,1.61,4.84,,2.0,0.0,diagnostic\nexp_007_fixed_dt4,ON,OFF,4,15,32,1,done/negative,152.49,176.90,,,,,,,,4.0,,diagnostic\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---


### Assistant

_source line 161_

<details><summary>Logged reasoning block</summary>

```text
These summary files don't have the intervention-level data I need for Table 2. The main registry has 46 experiments, but many important ones (TCN, RAVE, SGS, dual/wide/narrow critic, etc.) might be recorded in older artifact directories or in the full registry.yaml.

Let me search for the full registry.yaml that may contain all experiments, and also look at specific experiment artifact directories for the missing data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "19f11f30-b2b1-44df-a58c-acdc848dbf33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UY15XtTFuxXr7rwoiuSDtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2247,
      "cache_read_input_tokens": 71497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2247
      },
      "output_tokens": 36,
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

_source line 162_

<details open><summary>🔧 Tool call — Bash · `toolu_012CgQ3D2JcWyPTMmLi5TQpY`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -name \"registry.yaml\" -o -name \"registry.json\" 2>/dev/null | head -5",
  "description": "Find registry files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "84eb03a2-b3ee-4d05-8dff-09e0954e242a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UY15XtTFuxXr7rwoiuSDtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2247,
      "cache_read_input_tokens": 71497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2247
      },
      "output_tokens": 36,
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

_source line 163 · 2026-05-29T00:38:09.862Z_

<details><summary>↩ Tool result · `toolu_012CgQ3D2JcWyPTMmLi5TQpY`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "4704c484-ce9a-441f-a487-01a3b79efb7e",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml",
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

_source line 164_

<details open><summary>🔧 Tool call — Bash · `toolu_016NUm9ZS1euLzzUR9G4FnFD`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_027_tcn_walker_s0/ 2>/dev/null && echo \"---TCN---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_032_dual_critic_walker/ 2>/dev/null && echo \"---DUAL---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_033_wide_critic_walker/ 2>/dev/null && echo \"---WIDE---\"",
  "description": "Check experiment artifact directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "5d79dde8-6ed7-4220-b2c8-b5b9f645f9af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UY15XtTFuxXr7rwoiuSDtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2247,
      "cache_read_input_tokens": 71497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2247
      },
      "output_tokens": 36,
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

_source line 165 · 2026-05-29T00:38:12.081Z_

<details><summary>↩ Tool result · `toolu_016NUm9ZS1euLzzUR9G4FnFD`</summary>

```text
report
---TCN---
report
---DUAL---
report
---WIDE---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "4bcfb29c-99ba-4800-8bda-3c6bb607397e",
  "tool_use_result": {
    "stdout": "report\n---TCN---\nreport\n---DUAL---\nreport\n---WIDE---",
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

_source line 166_

<details open><summary>🔧 Tool call — Bash · `toolu_01RPvwfh3EvjAMX39oCivi1r`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml",
  "description": "Check registry.yaml size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d24c7e28-ac3d-4b52-a70c-34928975713a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YAWYVL9eL6NngTgw1Tey7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 73744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 583
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

_source line 167 · 2026-05-29T00:38:15.377Z_

<details><summary>↩ Tool result · `toolu_01RPvwfh3EvjAMX39oCivi1r`</summary>

```text
11382 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "13a70023-9537-4a8f-acc9-f0d58e717eef",
  "tool_use_result": {
    "stdout": "11382 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml",
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

_source line 168_

<details open><summary>🔧 Tool call — Bash · `toolu_01LDeCFdEqbEjMK9NvwR5y8z`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open(\"registry.yaml\") as f:\n    reg = yaml.safe_load(f)\n\n# Find all experiment IDs\nexperiments = reg.get(\"experiments\", reg)\nif not isinstance(experiments, dict):\n    print(f\"Top-level keys: {list(reg.keys())[:20]}\")\nelse:\n    print(f\"Total experiments: {len(experiments)}\")\n    \n    # Search for intervention experiments\n    target_keywords = {\n        \"tcn\": [], \"rave\": [], \"reward_sgs\": [], \"full_sgs\": [], \"obs_sgs\": [],\n        \"wide\": [], \"narrow\": [], \"dual_critic\": [],\n        \"frozen\": [], \"no_dt_emb\": [], \"008d\": [], \"008f\": [],\n        \"008a\": [], \"008e\": []\n    }\n    \n    for eid, exp in experiments.items():\n        eid_lower = eid.lower()\n        hyp = str(exp.get(\"hypothesis\", \"\")).lower()\n        concl = exp.get(\"conclusion\", \"\")\n        status = exp.get(\"status\", \"\")\n        metrics = exp.get(\"metrics\", {}) or {}\n        \n        # Get eval_return\n        eval_val = None\n        for k in [\"eval_return_mean\", \"eval_return_final\", \"eval_final\", \"final_eval_return\", \n                   \"eval_return_105K\", \"eval_return_105k\", \"peak_eval_return\", \"eval_return_peak\"]:\n            if k in metrics:\n                eval_val = metrics[k]\n                break\n        \n        # Categorize\n        cats = []\n        if \"tcn\" in eid_lower or \"tcn\" in hyp:\n            cats.append(\"tcn\")\n        if \"rave\" in eid_lower or \"rave\" in hyp:\n            cats.append(\"rave\")\n        if (\"sgs\" in eid_lower or \"sgs\" in hyp) and (\"reward\" in eid_lower or \"reward\" in hyp):\n            cats.append(\"reward_sgs\")\n        if (\"sgs\" in eid_lower or \"sgs\" in hyp) and (\"full\" in eid_lower or \"full\" in hyp):\n            cats.append(\"full_sgs\")\n        if (\"sgs\" in eid_lower or \"sgs\" in hyp) and (\"obs\" in eid_lower or \"obs\" in hyp):\n            cats.append(\"obs_sgs\")\n        if \"wide\" in eid_lower or \"wide\" in hyp:\n            cats.append(\"wide\")\n        if \"narrow\" in eid_lower or \"narrow\" in hyp:\n            cats.append(\"narrow\")\n        if \"dual_critic\" in eid_lower or \"dual-critic\" in eid_lower or \"dual critic\" in hyp or \"dual_critic\" in hyp:\n            cats.append(\"dual_critic\")\n        if \"frozen\" in eid_lower or \"frozen\" in hyp or \"freeze\" in hyp:\n            cats.append(\"frozen\")\n        if \"no_dt_emb\" in eid_lower or \"dt_embed_dim=0\" in hyp or \"008f\" in eid_lower or \"no dt_emb\" in hyp:\n            cats.append(\"no_dt_emb\")\n        if \"008d\" in eid_lower or (\"008d\" in hyp and \"trigger\" in hyp):\n            cats.append(\"008d\")\n        \n        if cats:\n            print(f\"\\n{eid}: status={status}, concl={concl}\")\n            print(f\"  categories: {cats}\")\n            print(f\"  eval_val: {eval_val}\")\n            # Check for sigma in TCN\n            if \"tcn\" in cats:\n                sigma = None\n                for s in [\"0.1\", \"0.2\", \"0.5\", \"1.0\"]:\n                    if s in str(exp.get(\"hypothesis\", \"\")) or f\"sigma{s}\" in eid_lower or f\"sigma0{s[0]}\" in eid_lower:\n                        sigma = s\n                        break\n                if not sigma:\n                    # Try command\n                    cmd = str(exp.get(\"spec\", {}).get(\"command\", \"\"))\n                    for s in [\"0.1\", \"0.2\", \"0.5\", \"1.0\"]:\n                        if f\"tcn_sigma {s}\" in cmd or f\"sigma={s}\" in cmd or f\"sigma0{s.replace('.','')}\" in cmd:\n                            sigma = s\n                            break\n                print(f\"  TCN sigma: {sigma}\")\n            print(f\"  hyp: {str(exp.get('hypothesis',''))[:120]}\")\nPYEOF\n",
  "description": "Parse registry.yaml for all intervention experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ade9e0ff-1bd8-4040-8191-65bb7bcb4a88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yZsRF2Y7ztWcCRKAX4tmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 74327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
      },
      "output_tokens": 61,
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

_source line 169 · 2026-05-29T00:38:33.548Z_

<details><summary>↩ Tool result · `toolu_01LDeCFdEqbEjMK9NvwR5y8z`</summary>

```text
Total experiments: 213

exp_008a_untrained_s1: status=DONE, concl=killed
  categories: ['frozen']
  eval_val: None
  hyp: (cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板

exp_008a_untrained_s2: status=DONE, concl=killed
  categories: ['frozen']
  eval_val: None
  hyp: (cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板

exp_008d: status=DONE, concl=killed
  categories: ['008d']
  eval_val: None
  hyp: 

exp_008d_civo_trigger_s2: status=DONE, concl=killed
  categories: ['008d']
  eval_val: None
  hyp: Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 b

exp_008d_civo_trigger_s3: status=DONE, concl=success
  categories: ['008d']
  eval_val: 267.6
  hyp: Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming C

exp_008d_civo_trigger_s4: status=DONE, concl=success
  categories: ['008d']
  eval_val: None
  hyp: Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Reb

exp_008d_subsample_on_h8: status=DONE, concl=success
  categories: ['008d']
  eval_val: None
  hyp: Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestim

exp_008f_no_dt_embed_subsample_on_h8: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: None
  hyp: Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as 

exp_008f_s2: status=DONE, concl=killed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.

exp_008f_s3_no_dt_embed_walker: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 363.8
  hyp: Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=

exp_008f_s4: status=DONE, concl=negative
  categories: ['no_dt_emb']
  eval_val: 306.5
  hyp: Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 0

exp_009b_008d_walker_s2: status=DONE, concl=negative
  categories: ['008d']
  eval_val: None
  hyp: Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_008d (s0, collapse confirmed at ~55K, NVE

exp_009c_008f_walker_s2: status=DONE, concl=negative
  categories: ['no_dt_emb']
  eval_val: None
  hyp: Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）

exp_009c_s3: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 311.92
  hyp: Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=3. Additional seed for 009c (seed=2 

exp_009e_008d_walker_s1: status=DONE, concl=negative
  categories: ['008d']
  eval_val: None
  hyp: Trained dt_emb + subsample ON in Walker Walk seed 1 will replicate CIVO onset (NVE>1.5) as seen in seed 0. Source: plan_

exp_009f_008f_walker_s1: status=DONE, concl=killed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: dt_embed_dim=0 + subsample ON in Walker Walk seed 1 will NOT show CIVO (NVE<1.5), replicating causal control from seed 0

exp_009g_008f_walker_s0: status=DONE, concl=killed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009f（seed=1 与 p

exp_009h_008f_walker_s0: status=DONE, concl=failed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009g（EGL device

exp_010b_cheetah_civo_trigger: status=DONE, concl=success
  categories: ['008d']
  eval_val: 51.7
  hyp: Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO

exp_015b_frozen_dt_emb: status=DONE, concl=negative
  categories: ['frozen']
  eval_val: 204.2
  hyp: Walker Walk frozen dt_emb + subsample ON + dt=2 imagination + H=8 seed 1 — 2×2 消融矩阵: 隔离 dt_emb 训练 vs 存在的因果效应。如果 freeze 后

exp_016_sgs_walker_s1: status=DONE, concl=failed
  categories: ['reward_sgs']
  eval_val: None
  hyp: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt

exp_016b_sgs_walker_s1: status=DONE, concl=failed
  categories: ['reward_sgs']
  eval_val: None
  hyp: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt

exp_016c_sgs_walker_s1: status=DONE, concl=failed
  categories: ['reward_sgs']
  eval_val: None
  hyp: Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心。GPU 1 清理+验证通过后重启（plan_016

exp_016d_sgs_walker_s1: status=DONE, concl=failed
  categories: ['reward_sgs']
  eval_val: None
  hyp: Selective Gradient Stopping (reward_dt_emb_detach) blocks reward-gradient pathway to dt_emb, preventing CIVO-inducing co

exp_016e_sgs_walker_s1: status=DONE, concl=negative
  categories: ['reward_sgs']
  eval_val: 31.73
  hyp: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CI

exp_018_full_sgs_s2: status=DONE, concl=negative
  categories: ['full_sgs']
  eval_val: None
  hyp: Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mec

exp_018_full_sgs_walker_s1: status=DONE, concl=killed
  categories: ['full_sgs', 'obs_sgs']
  eval_val: 915.7
  hyp: Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerabili

exp_018v2_full_sgs_walker_s1: status=DONE, concl=negative
  categories: ['reward_sgs', 'full_sgs', 'obs_sgs']
  eval_val: 448.3
  hyp: Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways

exp_019a_pickcube_baseline: status=DONE, concl=killed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中

exp_020_vanilla_dreamerv3_s2: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 836.5
  hyp: Vanilla DreamerV3 (no dt_emb, no subsample, no gate) seed 2 — Pathway B 控制实验：验证 008e_v3_s2 的 eval-driven collapse 是否需要 t

exp_021_full_sgs_cheetah_s1: status=DONE, concl=negative
  categories: ['full_sgs']
  eval_val: 221.5
  hyp: Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE

exp_022_untrained_dt_emb_learned_gate: status=DONE, concl=killed
  categories: ['frozen']
  eval_val: 189.1
  hyp: Frozen dt_emb (random init, no gradients) prevents CIVO by blocking the trained-embedding-driven value overestimation fe

exp_022b_no_curriculum: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 300.7
  hyp: Frozen dt_emb (random init, no gradients) + learned gate WITHOUT curriculum (phase1=0, phase2=0, gate fully unlocked fro

exp_024_cheetah_no_dt_emb_s0: status=DONE, concl=killed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO

exp_024b_cheetah_no_dt_emb_s0: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 96.5
  hyp: Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO

exp_024b_cheetah_no_dt_emb_s1: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 77.3
  hyp: Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb

exp_025_obs_sgs_walker_s1: status=DONE, concl=failed
  categories: ['reward_sgs', 'obs_sgs']
  eval_val: None
  hyp: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preser

exp_025_obs_sgs_walker_s2: status=DONE, concl=negative
  categories: ['reward_sgs', 'obs_sgs']
  eval_val: None
  hyp: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preser

exp_025_obs_sgs_walker_s3: status=DONE, concl=failed
  categories: ['reward_sgs', 'obs_sgs']
  eval_val: None
  hyp: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preser

exp_025_obs_sgs_walker_s4: status=DONE, concl=failed
  categories: ['reward_sgs', 'obs_sgs']
  eval_val: None
  hyp: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preser

exp_026_obs_sgs_cheetah_s0: status=DONE, concl=failed
  categories: ['obs_sgs']
  eval_val: None
  hyp: Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second envir

exp_026_obs_sgs_cheetah_s1: status=DONE, concl=failed
  categories: ['obs_sgs']
  eval_val: None
  hyp: Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second envir

exp_027_tcn_walker_s0: status=DONE, concl=negative
  categories: ['tcn', 'obs_sgs']
  eval_val: 95.5
  TCN sigma: 0.5
  hyp: Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces

exp_027_tcn_walker_s0_sigma02: status=DONE, concl=success
  categories: ['tcn']
  eval_val: 236.4
  TCN sigma: 0.2
  hyp: TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.

exp_027_tcn_walker_s1: status=DONE, concl=negative
  categories: ['tcn']
  eval_val: None
  TCN sigma: 0.5
  hyp: TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenom

exp_028_rave_walker_s0: status=DONE, concl=negative
  categories: ['rave']
  eval_val: None
  hyp: Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA o

exp_028_rave_walker_s0_ceil15: status=DONE, concl=negative
  categories: ['rave']
  eval_val: 76.2
  hyp: RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter con

exp_029a_tcn_walker_s1_sigma02: status=DONE, concl=success
  categories: ['tcn']
  eval_val: 319.4
  TCN sigma: 0.2
  hyp: TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval rea

exp_029b_tcn_walker_s2_sigma02: status=DONE, concl=negative
  categories: ['tcn']
  eval_val: 31.97
  TCN sigma: 0.2
  hyp: TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%. Third seed resolves whether high variance is systema

exp_029c_tcn_walker_s0_sigma01: status=DONE, concl=negative
  categories: ['tcn']
  eval_val: 328.3
  TCN sigma: 0.1
  hyp: σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimu

exp_029d_tcn_walker_s3_sigma02: status=DONE, concl=negative
  categories: ['tcn']
  eval_val: 104.5
  TCN sigma: 0.2
  hyp: Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443, s3=869, s4=923@105K) for statistical comparison. Curren

exp_030a_tcn_cheetah_s0_sigma02: status=DONE, concl=negative
  categories: ['tcn']
  eval_val: None
  TCN sigma: 0.2
  hyp: TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Ch

exp_030b_tcn_cheetah_s0_sigma05: status=DONE, concl=negative
  categories: ['tcn']
  eval_val: 104.4
  TCN sigma: 0.2
  hyp: Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose

exp_030c_tcn_cheetah_s0_sigma10: status=DONE, concl=negative
  categories: ['tcn']
  eval_val: 47.2
  TCN sigma: 0.5
  hyp: TCN σ=1.0 on Cheetah tests whether higher noise amplitude further suppresses CIVO. σ=0.5 (exp_030b) was negative with NV

exp_031_tcn_pickcube_s0_sigma02: status=DONE, concl=negative
  categories: ['tcn']
  eval_val: None
  TCN sigma: 0.2
  hyp: TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill Pick

exp_031b_tcn_pickcube_s0_sigma05: status=DONE, concl=negative
  categories: ['tcn']
  eval_val: None
  TCN sigma: 0.2
  hyp: PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed with NVE peak 3.71. σ=0.5 tests whether higher nois

exp_032_dual_critic_walker: status=DONE, concl=success
  categories: ['dual_critic', '008d']
  eval_val: 739.7
  hyp: Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses

exp_032b_dual_critic_walker_s1: status=DONE, concl=success
  categories: ['dual_critic']
  eval_val: 516
  hyp: Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust arch

exp_033_wide_critic_walker: status=DONE, concl=success
  categories: ['wide']
  eval_val: None
  hyp: Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rathe

exp_034_dual_critic_cheetah: status=DONE, concl=negative
  categories: ['tcn', 'dual_critic']
  eval_val: 97.5
  TCN sigma: 0.2
  hyp: Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (whe

exp_035_narrow_dual_critic_walker: status=DONE, concl=success
  categories: ['wide', 'narrow', 'dual_critic']
  eval_val: 697.8
  hyp: Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect fro

exp_036_dual_critic_pickcube: status=DONE, concl=negative
  categories: ['tcn', 'dual_critic']
  eval_val: 27.7
  TCN sigma: 0.2
  hyp: Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → archite

exp_037_wide_critic_cheetah: status=DONE, concl=negative
  categories: ['wide']
  eval_val: 146.1
  hyp: Wide single critic on Cheetah: if capacity=recovery generalizes from Walker (exp_033, NVE 4.75→self-repair, eval 408) to

exp_038_dual_critic_walker_s2: status=DONE, concl=negative
  categories: ['dual_critic']
  eval_val: 120.9
  hyp: Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention 

exp_039_narrow_dual_critic_walker_s1: status=DONE, concl=success
  categories: ['narrow', 'dual_critic']
  eval_val: 592.7
  hyp: Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow 

exp_040_wide_dual_critic_cheetah: status=DONE, concl=success
  categories: ['wide', 'dual_critic']
  eval_val: None
  hyp: Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust

exp_041_dual_critic_walker_s3: status=DONE, concl=success
  categories: ['dual_critic']
  eval_val: 544
  hyp: D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO

exp_042_frozen_dt_emb_walker: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 612.45
  hyp: dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init,

exp_043_008f_walker_s1: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 673.73
  hyp: Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb ab

exp_044_gradient_stop_walker: status=DONE, concl=success
  categories: ['reward_sgs']
  eval_val: 538.6
  hyp: Reviewer Q2 直接回应：gradient stopping（detach dt_emb gradient to reward head）是否能阻断 CIVO 的 reward-critic feedback loop。基于 008

exp_046_frozen_dt_emb_cheetah: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 150.5
  hyp: Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending t

exp_047_frozen_dt_emb_walker_s1: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 144.22
  hyp: Frozen dt_emb Walker seed 1: 增强 exp_042 (s0, NVE=0.19) 的统计力度。 如果 s1 也 NVE<1.5 且无持续 CIVO → frozen dt_emb mitigation 跨 see

exp_045_treatment_extension_008d_s3: status=DONE, concl=success
  categories: ['008d']
  eval_val: 867.6
  hyp: CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or 

exp_051_stackcube_frozen_dt_emb_s0: status=DONE, concl=negative
  categories: ['frozen']
  eval_val: 45.3
  hyp: Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_

exp_053_peginsertion_frozen_s0: status=DONE, concl=success
  categories: ['frozen']
  eval_val: None
  hyp: Freezing dt_emb in PegInsertionSide-v1 (contact-rich manipulation) prevents CIVO while maintaining task performance, est

exp_054_pickcube_frozen_s0: status=DONE, concl=success
  categories: ['frozen']
  eval_val: None
  hyp: PickCube frozen dt_emb baseline (fixed_dt=2, subsample ON, H=8)。验证 CIVO frozen 配置在最简单 manipulation task 上的表现。如果 eval ret

exp_056_peginsertion_frozen_s1: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 4.37
  hyp: D143 混合机制假说验证——PegInsertion frozen dt_emb 跨 seed 可复现性。exp_053 (s0) 显示 frozen 在 82.5K 回落到 1.82 而 trained 攀升到 10.05，s1 验证这

exp_057_frozen_dt_emb_walker_s2: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 123.94
  hyp: Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → fr

exp_058_frozen_dt_emb_cheetah_s1: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 80.46
  hyp: Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Ch

exp_062_cartpole_control: status=DONE, concl=negative
  categories: ['no_dt_emb']
  eval_val: None
  hyp: dt_embed_dim=0 + subsample ON + H=8 在 Cartpole Swingup 上不触发 CIVO（NVE < 1.5x），因果控制实验验证移除 dt_emb 是否阻止 CIVO 在第三个环境中泛化。与 exp

exp_057: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 123.9
  hyp: Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。

exp_067_frozen_dt_emb_walker_plan015: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 281.5
  hyp: Frozen (requires_grad=False) dt_embedding + subsample ON + dt=2 + H=8 在 Walker Walk 上不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIV

exp_068_008d_walker_repro_s1: status=DONE, concl=success
  categories: ['008d']
  eval_val: 39.1
  hyp: Reproducing 008d config (trained dt_emb + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will trigger CIVO (NVE > 1.5x

exp_069_008f_walker_repro_s1: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 237.8
  hyp: Reproducing 008f config (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will NOT trigger C

exp_071_008f_walker_s3: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 311.9
  hyp: Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=3。当前 008f 2 seeds 结果分歧（s1=success eval=

exp_073_008f_walker_s4: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 289.3
  hyp: Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=4。当前 008f 0/3 CIVO onset，扩到 seed=4 进一步巩

exp_078_cheetah_008d_s0: status=DONE, concl=success
  categories: ['008d']
  eval_val: 119.5
  hyp: Trained dt_embedding with subsample ON + dt=2 + H=8 on Cheetah Run triggers CIVO — cross-environment validation (C2) tha

exp_079_frozen_dt_emb_walker_s0: status=DONE, concl=killed
  categories: ['frozen']
  eval_val: None
  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk does not trigger CI

exp_082_cheetah_no_dt_emb_s0: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 83.2
  hyp: Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_e

exp_084_frozen_dt_emb_walker_s0: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 281.48
  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk does not trigger CI

exp_085_frozen_dt_emb_walker_s1: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 69.26
  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk seed=1 does not tri

exp_086_frozen_dt_emb_cheetah_s0: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 53.3
  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Cheetah Run does not trigger CI

exp_087_frozen_dt_emb_cheetah_s1: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 186.9
  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Cheetah Run seed=1 does not tri

exp_088_cheetah_008d_s1: status=DONE, concl=negative
  categories: ['008d']
  eval_val: 309.3
  hyp: Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed)。预期触发 C

exp_089_cheetah_no_dt_emb_s1: status=DONE, concl=failed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_

exp_090_cheetah_no_dt_emb_s2: status=DONE, concl=failed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_

exp_091_cheetah_008d_s2: status=DONE, concl=success
  categories: ['008d']
  eval_val: 2.5
  hyp: Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed) 和 exp_

exp_092_cheetah_no_dt_emb_s1: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 77.3
  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_

exp_093_cheetah_no_dt_emb_s2: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 151.2
  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_

exp_094_cheetah_008d_s3: status=DONE, concl=failed
  categories: ['008d']
  eval_val: None
  hyp: Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=3 — 第 4 个 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed)。与 

exp_095_cheetah_no_dt_emb_s3: status=DONE, concl=failed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=3 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_

exp_097_cheetah_008d_s3: status=DONE, concl=success
  categories: ['008d']
  eval_val: 61.7
  hyp: Cheetah with fixed dt=2 and subsample_max_dt=2 (008d config, seed 3) will reproduce the CIVO trigger pattern seen in Wal

rssm_fidelity_v2: status=DONE, concl=success
  categories: ['frozen']
  eval_val: None
  hyp: RSSM standardized prediction quality analysis: trained dt_emb models have higher reward prediction gap (dt2/dt1 ratio) t

exp_hopper_trained_s0: status=DONE, concl=success
  categories: ['008d']
  eval_val: 3.26
  hyp: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K ste

exp_hopper_frozen_s0: status=DONE, concl=success
  categories: ['frozen']
  eval_val: 0
  hyp: Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the n

exp_hopper_frozen_s1: status=DONE, concl=killed
  categories: ['frozen']
  eval_val: None
  hyp: Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the n

exp_105_hopper_trained_s0: status=DONE, concl=killed
  categories: ['008d']
  eval_val: None
  hyp: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K ste

exp_106_hopper_trained_s1: status=DONE, concl=killed
  categories: ['008d']
  eval_val: None
  hyp: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K ste

exp_107_hopper_frozen_s0: status=DONE, concl=killed
  categories: ['frozen']
  eval_val: None
  hyp: Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE &lt; 1.5× throughout), confirming causal role of trained 

exp_108_hopper_frozen_s1: status=DONE, concl=killed
  categories: ['frozen']
  eval_val: None
  hyp: Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE &lt; 1.5× throughout), second seed for mitigation confirm

exp_hopper_no_dt_emb_s0: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 10.759
  hyp: Removing dt_embedding entirely (dt_embed_dim=0) while keeping gate+dt=2+subsample ON will still show severe learning del

exp_hopper_frozen_s0_ext: status=DONE, concl=negative
  categories: ['frozen']
  eval_val: 0.5608
  hyp: Extending frozen_s0 from 105K→150K will show eval_return recovery (rising like trained_s0_ext: 3.26→81.58) with ve_ratio

exp_walker_no_dt_emb_s0: status=ALLOCATED, concl=killed
  categories: ['no_dt_emb']
  eval_val: None
  hyp: dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 0 will NOT show CIVO (NVE<1.5), replicating 008f causal control. 

exp_walker_no_dt_emb_s1: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 468.83
  hyp: dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 1 will NOT show CIVO (NVE<1.5), replicating 008f causal control f

exp_walker_008f_s0: status=DONE, concl=success
  categories: ['no_dt_emb']
  eval_val: 139.54
  hyp: dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 0 will NOT show CIVO (NVE<2.0), replicating 008f causal control f

exp_walker_008d_s6: status=DONE, concl=failed
  categories: ['narrow', '008d']
  eval_val: None
  hyp: Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=6 — C2 onset rate rebu

exp_walker_008d_s7: status=DONE, concl=failed
  categories: ['narrow', '008d']
  eval_val: None
  hyp: Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=7 — C2 onset rate rebu

exp_walker_008d_s6_r2: status=DONE, concl=failed
  categories: ['008d']
  eval_val: None
  hyp: Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=6 — C2 onset rate rebu

exp_walker_008d_s7_r2: status=DONE, concl=failed
  categories: ['008d']
  eval_val: None
  hyp: Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=7 — C2 onset rate rebu

exp_humanoid_008d_s0: status=PENDING, concl=
  categories: ['008d']
  eval_val: None
  hyp: Humanoid Walk trained dt_emb + gate + subsample ON (008d config: gate_fixed_dt=2, gate_subsample_max_dt=2, H=8), seed=0 

exp_quadruped_008d_s0: status=PENDING, concl=
  categories: ['008d']
  eval_val: None
  hyp: Quadruped Walk trained dt_emb + gate + subsample ON (008d config: gate_fixed_dt=2, gate_subsample_max_dt=2, H=8), seed=0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "8f9c5035-9379-4ea9-92dd-ea4c00bf9a5b",
  "tool_use_result": {
    "stdout": "Total experiments: 213\n\nexp_008a_untrained_s1: status=DONE, concl=killed\n  categories: ['frozen']\n  eval_val: None\n  hyp: (cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\n\nexp_008a_untrained_s2: status=DONE, concl=killed\n  categories: ['frozen']\n  eval_val: None\n  hyp: (cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\n\nexp_008d: status=DONE, concl=killed\n  categories: ['008d']\n  eval_val: None\n  hyp: \n\nexp_008d_civo_trigger_s2: status=DONE, concl=killed\n  categories: ['008d']\n  eval_val: None\n  hyp: Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 b\n\nexp_008d_civo_trigger_s3: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: 267.6\n  hyp: Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming C\n\nexp_008d_civo_trigger_s4: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: None\n  hyp: Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Reb\n\nexp_008d_subsample_on_h8: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: None\n  hyp: Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestim\n\nexp_008f_no_dt_embed_subsample_on_h8: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as \n\nexp_008f_s2: status=DONE, concl=killed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.\n\nexp_008f_s3_no_dt_embed_walker: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 363.8\n  hyp: Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=\n\nexp_008f_s4: status=DONE, concl=negative\n  categories: ['no_dt_emb']\n  eval_val: 306.5\n  hyp: Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 0\n\nexp_009b_008d_walker_s2: status=DONE, concl=negative\n  categories: ['008d']\n  eval_val: None\n  hyp: Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_008d (s0, collapse confirmed at ~55K, NVE\n\nexp_009c_008f_walker_s2: status=DONE, concl=negative\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\n\nexp_009c_s3: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 311.92\n  hyp: Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=3. Additional seed for 009c (seed=2 \n\nexp_009e_008d_walker_s1: status=DONE, concl=negative\n  categories: ['008d']\n  eval_val: None\n  hyp: Trained dt_emb + subsample ON in Walker Walk seed 1 will replicate CIVO onset (NVE>1.5) as seen in seed 0. Source: plan_\n\nexp_009f_008f_walker_s1: status=DONE, concl=killed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: dt_embed_dim=0 + subsample ON in Walker Walk seed 1 will NOT show CIVO (NVE<1.5), replicating causal control from seed 0\n\nexp_009g_008f_walker_s0: status=DONE, concl=killed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009f（seed=1 与 p\n\nexp_009h_008f_walker_s0: status=DONE, concl=failed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009g（EGL device\n\nexp_010b_cheetah_civo_trigger: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: 51.7\n  hyp: Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO\n\nexp_015b_frozen_dt_emb: status=DONE, concl=negative\n  categories: ['frozen']\n  eval_val: 204.2\n  hyp: Walker Walk frozen dt_emb + subsample ON + dt=2 imagination + H=8 seed 1 — 2×2 消融矩阵: 隔离 dt_emb 训练 vs 存在的因果效应。如果 freeze 后\n\nexp_016_sgs_walker_s1: status=DONE, concl=failed\n  categories: ['reward_sgs']\n  eval_val: None\n  hyp: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt\n\nexp_016b_sgs_walker_s1: status=DONE, concl=failed\n  categories: ['reward_sgs']\n  eval_val: None\n  hyp: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt\n\nexp_016c_sgs_walker_s1: status=DONE, concl=failed\n  categories: ['reward_sgs']\n  eval_val: None\n  hyp: Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心。GPU 1 清理+验证通过后重启（plan_016\n\nexp_016d_sgs_walker_s1: status=DONE, concl=failed\n  categories: ['reward_sgs']\n  eval_val: None\n  hyp: Selective Gradient Stopping (reward_dt_emb_detach) blocks reward-gradient pathway to dt_emb, preventing CIVO-inducing co\n\nexp_016e_sgs_walker_s1: status=DONE, concl=negative\n  categories: ['reward_sgs']\n  eval_val: 31.73\n  hyp: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CI\n\nexp_018_full_sgs_s2: status=DONE, concl=negative\n  categories: ['full_sgs']\n  eval_val: None\n  hyp: Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mec\n\nexp_018_full_sgs_walker_s1: status=DONE, concl=killed\n  categories: ['full_sgs', 'obs_sgs']\n  eval_val: 915.7\n  hyp: Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerabili\n\nexp_018v2_full_sgs_walker_s1: status=DONE, concl=negative\n  categories: ['reward_sgs', 'full_sgs', 'obs_sgs']\n  eval_val: 448.3\n  hyp: Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways\n\nexp_019a_pickcube_baseline: status=DONE, concl=killed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中\n\nexp_020_vanilla_dreamerv3_s2: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 836.5\n  hyp: Vanilla DreamerV3 (no dt_emb, no subsample, no gate) seed 2 — Pathway B 控制实验：验证 008e_v3_s2 的 eval-driven collapse 是否需要 t\n\nexp_021_full_sgs_cheetah_s1: status=DONE, concl=negative\n  categories: ['full_sgs']\n  eval_val: 221.5\n  hyp: Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE\n\nexp_022_untrained_dt_emb_learned_gate: status=DONE, concl=killed\n  categories: ['frozen']\n  eval_val: 189.1\n  hyp: Frozen dt_emb (random init, no gradients) prevents CIVO by blocking the trained-embedding-driven value overestimation fe\n\nexp_022b_no_curriculum: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 300.7\n  hyp: Frozen dt_emb (random init, no gradients) + learned gate WITHOUT curriculum (phase1=0, phase2=0, gate fully unlocked fro\n\nexp_024_cheetah_no_dt_emb_s0: status=DONE, concl=killed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO\n\nexp_024b_cheetah_no_dt_emb_s0: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 96.5\n  hyp: Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO\n\nexp_024b_cheetah_no_dt_emb_s1: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 77.3\n  hyp: Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb\n\nexp_025_obs_sgs_walker_s1: status=DONE, concl=failed\n  categories: ['reward_sgs', 'obs_sgs']\n  eval_val: None\n  hyp: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preser\n\nexp_025_obs_sgs_walker_s2: status=DONE, concl=negative\n  categories: ['reward_sgs', 'obs_sgs']\n  eval_val: None\n  hyp: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preser\n\nexp_025_obs_sgs_walker_s3: status=DONE, concl=failed\n  categories: ['reward_sgs', 'obs_sgs']\n  eval_val: None\n  hyp: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preser\n\nexp_025_obs_sgs_walker_s4: status=DONE, concl=failed\n  categories: ['reward_sgs', 'obs_sgs']\n  eval_val: None\n  hyp: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preser\n\nexp_026_obs_sgs_cheetah_s0: status=DONE, concl=failed\n  categories: ['obs_sgs']\n  eval_val: None\n  hyp: Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second envir\n\nexp_026_obs_sgs_cheetah_s1: status=DONE, concl=failed\n  categories: ['obs_sgs']\n  eval_val: None\n  hyp: Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second envir\n\nexp_027_tcn_walker_s0: status=DONE, concl=negative\n  categories: ['tcn', 'obs_sgs']\n  eval_val: 95.5\n  TCN sigma: 0.5\n  hyp: Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces\n\nexp_027_tcn_walker_s0_sigma02: status=DONE, concl=success\n  categories: ['tcn']\n  eval_val: 236.4\n  TCN sigma: 0.2\n  hyp: TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.\n\nexp_027_tcn_walker_s1: status=DONE, concl=negative\n  categories: ['tcn']\n  eval_val: None\n  TCN sigma: 0.5\n  hyp: TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenom\n\nexp_028_rave_walker_s0: status=DONE, concl=negative\n  categories: ['rave']\n  eval_val: None\n  hyp: Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA o\n\nexp_028_rave_walker_s0_ceil15: status=DONE, concl=negative\n  categories: ['rave']\n  eval_val: 76.2\n  hyp: RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter con\n\nexp_029a_tcn_walker_s1_sigma02: status=DONE, concl=success\n  categories: ['tcn']\n  eval_val: 319.4\n  TCN sigma: 0.2\n  hyp: TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval rea\n\nexp_029b_tcn_walker_s2_sigma02: status=DONE, concl=negative\n  categories: ['tcn']\n  eval_val: 31.97\n  TCN sigma: 0.2\n  hyp: TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%. Third seed resolves whether high variance is systema\n\nexp_029c_tcn_walker_s0_sigma01: status=DONE, concl=negative\n  categories: ['tcn']\n  eval_val: 328.3\n  TCN sigma: 0.1\n  hyp: σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimu\n\nexp_029d_tcn_walker_s3_sigma02: status=DONE, concl=negative\n  categories: ['tcn']\n  eval_val: 104.5\n  TCN sigma: 0.2\n  hyp: Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443, s3=869, s4=923@105K) for statistical comparison. Curren\n\nexp_030a_tcn_cheetah_s0_sigma02: status=DONE, concl=negative\n  categories: ['tcn']\n  eval_val: None\n  TCN sigma: 0.2\n  hyp: TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Ch\n\nexp_030b_tcn_cheetah_s0_sigma05: status=DONE, concl=negative\n  categories: ['tcn']\n  eval_val: 104.4\n  TCN sigma: 0.2\n  hyp: Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose\n\nexp_030c_tcn_cheetah_s0_sigma10: status=DONE, concl=negative\n  categories: ['tcn']\n  eval_val: 47.2\n  TCN sigma: 0.5\n  hyp: TCN σ=1.0 on Cheetah tests whether higher noise amplitude further suppresses CIVO. σ=0.5 (exp_030b) was negative with NV\n\nexp_031_tcn_pickcube_s0_sigma02: status=DONE, concl=negative\n  categories: ['tcn']\n  eval_val: None\n  TCN sigma: 0.2\n  hyp: TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill Pick\n\nexp_031b_tcn_pickcube_s0_sigma05: status=DONE, concl=negative\n  categories: ['tcn']\n  eval_val: None\n  TCN sigma: 0.2\n  hyp: PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed with NVE peak 3.71. σ=0.5 tests whether higher nois\n\nexp_032_dual_critic_walker: status=DONE, concl=success\n  categories: ['dual_critic', '008d']\n  eval_val: 739.7\n  hyp: Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses\n\nexp_032b_dual_critic_walker_s1: status=DONE, concl=success\n  categories: ['dual_critic']\n  eval_val: 516\n  hyp: Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust arch\n\nexp_033_wide_critic_walker: status=DONE, concl=success\n  categories: ['wide']\n  eval_val: None\n  hyp: Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rathe\n\nexp_034_dual_critic_cheetah: status=DONE, concl=negative\n  categories: ['tcn', 'dual_critic']\n  eval_val: 97.5\n  TCN sigma: 0.2\n  hyp: Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (whe\n\nexp_035_narrow_dual_critic_walker: status=DONE, concl=success\n  categories: ['wide', 'narrow', 'dual_critic']\n  eval_val: 697.8\n  hyp: Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect fro\n\nexp_036_dual_critic_pickcube: status=DONE, concl=negative\n  categories: ['tcn', 'dual_critic']\n  eval_val: 27.7\n  TCN sigma: 0.2\n  hyp: Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → archite\n\nexp_037_wide_critic_cheetah: status=DONE, concl=negative\n  categories: ['wide']\n  eval_val: 146.1\n  hyp: Wide single critic on Cheetah: if capacity=recovery generalizes from Walker (exp_033, NVE 4.75→self-repair, eval 408) to\n\nexp_038_dual_critic_walker_s2: status=DONE, concl=negative\n  categories: ['dual_critic']\n  eval_val: 120.9\n  hyp: Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention \n\nexp_039_narrow_dual_critic_walker_s1: status=DONE, concl=success\n  categories: ['narrow', 'dual_critic']\n  eval_val: 592.7\n  hyp: Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow \n\nexp_040_wide_dual_critic_cheetah: status=DONE, concl=success\n  categories: ['wide', 'dual_critic']\n  eval_val: None\n  hyp: Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust\n\nexp_041_dual_critic_walker_s3: status=DONE, concl=success\n  categories: ['dual_critic']\n  eval_val: 544\n  hyp: D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO\n\nexp_042_frozen_dt_emb_walker: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 612.45\n  hyp: dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init,\n\nexp_043_008f_walker_s1: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 673.73\n  hyp: Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb ab\n\nexp_044_gradient_stop_walker: status=DONE, concl=success\n  categories: ['reward_sgs']\n  eval_val: 538.6\n  hyp: Reviewer Q2 直接回应：gradient stopping（detach dt_emb gradient to reward head）是否能阻断 CIVO 的 reward-critic feedback loop。基于 008\n\nexp_046_frozen_dt_emb_cheetah: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 150.5\n  hyp: Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending t\n\nexp_047_frozen_dt_emb_walker_s1: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 144.22\n  hyp: Frozen dt_emb Walker seed 1: 增强 exp_042 (s0, NVE=0.19) 的统计力度。 如果 s1 也 NVE<1.5 且无持续 CIVO → frozen dt_emb mitigation 跨 see\n\nexp_045_treatment_extension_008d_s3: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: 867.6\n  hyp: CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or \n\nexp_051_stackcube_frozen_dt_emb_s0: status=DONE, concl=negative\n  categories: ['frozen']\n  eval_val: 45.3\n  hyp: Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_\n\nexp_053_peginsertion_frozen_s0: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: None\n  hyp: Freezing dt_emb in PegInsertionSide-v1 (contact-rich manipulation) prevents CIVO while maintaining task performance, est\n\nexp_054_pickcube_frozen_s0: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: None\n  hyp: PickCube frozen dt_emb baseline (fixed_dt=2, subsample ON, H=8)。验证 CIVO frozen 配置在最简单 manipulation task 上的表现。如果 eval ret\n\nexp_056_peginsertion_frozen_s1: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 4.37\n  hyp: D143 混合机制假说验证——PegInsertion frozen dt_emb 跨 seed 可复现性。exp_053 (s0) 显示 frozen 在 82.5K 回落到 1.82 而 trained 攀升到 10.05，s1 验证这\n\nexp_057_frozen_dt_emb_walker_s2: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 123.94\n  hyp: Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → fr\n\nexp_058_frozen_dt_emb_cheetah_s1: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 80.46\n  hyp: Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Ch\n\nexp_062_cartpole_control: status=DONE, concl=negative\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: dt_embed_dim=0 + subsample ON + H=8 在 Cartpole Swingup 上不触发 CIVO（NVE < 1.5x），因果控制实验验证移除 dt_emb 是否阻止 CIVO 在第三个环境中泛化。与 exp\n\nexp_057: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 123.9\n  hyp: Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。\n\nexp_067_frozen_dt_emb_walker_plan015: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 281.5\n  hyp: Frozen (requires_grad=False) dt_embedding + subsample ON + dt=2 + H=8 在 Walker Walk 上不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIV\n\nexp_068_008d_walker_repro_s1: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: 39.1\n  hyp: Reproducing 008d config (trained dt_emb + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will trigger CIVO (NVE > 1.5x\n\nexp_069_008f_walker_repro_s1: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 237.8\n  hyp: Reproducing 008f config (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will NOT trigger C\n\nexp_071_008f_walker_s3: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 311.9\n  hyp: Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=3。当前 008f 2 seeds 结果分歧（s1=success eval=\n\nexp_073_008f_walker_s4: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 289.3\n  hyp: Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=4。当前 008f 0/3 CIVO onset，扩到 seed=4 进一步巩\n\nexp_078_cheetah_008d_s0: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: 119.5\n  hyp: Trained dt_embedding with subsample ON + dt=2 + H=8 on Cheetah Run triggers CIVO — cross-environment validation (C2) tha\n\nexp_079_frozen_dt_emb_walker_s0: status=DONE, concl=killed\n  categories: ['frozen']\n  eval_val: None\n  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk does not trigger CI\n\nexp_082_cheetah_no_dt_emb_s0: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 83.2\n  hyp: Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_e\n\nexp_084_frozen_dt_emb_walker_s0: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 281.48\n  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk does not trigger CI\n\nexp_085_frozen_dt_emb_walker_s1: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 69.26\n  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk seed=1 does not tri\n\nexp_086_frozen_dt_emb_cheetah_s0: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 53.3\n  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Cheetah Run does not trigger CI\n\nexp_087_frozen_dt_emb_cheetah_s1: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 186.9\n  hyp: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Cheetah Run seed=1 does not tri\n\nexp_088_cheetah_008d_s1: status=DONE, concl=negative\n  categories: ['008d']\n  eval_val: 309.3\n  hyp: Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed)。预期触发 C\n\nexp_089_cheetah_no_dt_emb_s1: status=DONE, concl=failed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_\n\nexp_090_cheetah_no_dt_emb_s2: status=DONE, concl=failed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_\n\nexp_091_cheetah_008d_s2: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: 2.5\n  hyp: Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed) 和 exp_\n\nexp_092_cheetah_no_dt_emb_s1: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 77.3\n  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_\n\nexp_093_cheetah_no_dt_emb_s2: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 151.2\n  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_\n\nexp_094_cheetah_008d_s3: status=DONE, concl=failed\n  categories: ['008d']\n  eval_val: None\n  hyp: Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=3 — 第 4 个 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed)。与 \n\nexp_095_cheetah_no_dt_emb_s3: status=DONE, concl=failed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=3 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_\n\nexp_097_cheetah_008d_s3: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: 61.7\n  hyp: Cheetah with fixed dt=2 and subsample_max_dt=2 (008d config, seed 3) will reproduce the CIVO trigger pattern seen in Wal\n\nrssm_fidelity_v2: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: None\n  hyp: RSSM standardized prediction quality analysis: trained dt_emb models have higher reward prediction gap (dt2/dt1 ratio) t\n\nexp_hopper_trained_s0: status=DONE, concl=success\n  categories: ['008d']\n  eval_val: 3.26\n  hyp: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K ste\n\nexp_hopper_frozen_s0: status=DONE, concl=success\n  categories: ['frozen']\n  eval_val: 0\n  hyp: Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the n\n\nexp_hopper_frozen_s1: status=DONE, concl=killed\n  categories: ['frozen']\n  eval_val: None\n  hyp: Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the n\n\nexp_105_hopper_trained_s0: status=DONE, concl=killed\n  categories: ['008d']\n  eval_val: None\n  hyp: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K ste\n\nexp_106_hopper_trained_s1: status=DONE, concl=killed\n  categories: ['008d']\n  eval_val: None\n  hyp: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K ste\n\nexp_107_hopper_frozen_s0: status=DONE, concl=killed\n  categories: ['frozen']\n  eval_val: None\n  hyp: Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE &lt; 1.5× throughout), confirming causal role of trained \n\nexp_108_hopper_frozen_s1: status=DONE, concl=killed\n  categories: ['frozen']\n  eval_val: None\n  hyp: Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE &lt; 1.5× throughout), second seed for mitigation confirm\n\nexp_hopper_no_dt_emb_s0: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 10.759\n  hyp: Removing dt_embedding entirely (dt_embed_dim=0) while keeping gate+dt=2+subsample ON will still show severe learning del\n\nexp_hopper_frozen_s0_ext: status=DONE, concl=negative\n  categories: ['frozen']\n  eval_val: 0.5608\n  hyp: Extending frozen_s0 from 105K→150K will show eval_return recovery (rising like trained_s0_ext: 3.26→81.58) with ve_ratio\n\nexp_walker_no_dt_emb_s0: status=ALLOCATED, concl=killed\n  categories: ['no_dt_emb']\n  eval_val: None\n  hyp: dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 0 will NOT show CIVO (NVE<1.5), replicating 008f causal control. \n\nexp_walker_no_dt_emb_s1: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 468.83\n  hyp: dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 1 will NOT show CIVO (NVE<1.5), replicating 008f causal control f\n\nexp_walker_008f_s0: status=DONE, concl=success\n  categories: ['no_dt_emb']\n  eval_val: 139.54\n  hyp: dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 0 will NOT show CIVO (NVE<2.0), replicating 008f causal control f\n\nexp_walker_008d_s6: status=DONE, concl=failed\n  categories: ['narrow', '008d']\n  eval_val: None\n  hyp: Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=6 — C2 onset rate rebu\n\nexp_walker_008d_s7: status=DONE, concl=failed\n  categories: ['narrow', '008d']\n  eval_val: None\n  hyp: Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=7 — C2 onset rate rebu\n\nexp_walker_008d_s6_r2: status=DONE, concl=failed\n  categories: ['008d']\n  eval_val: None\n  hyp: Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=6 — C2 onset rate rebu\n\nexp_walker_008d_s7_r2: status=DONE, concl=failed\n  categories: ['008d']\n  eval_val: None\n  hyp: Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=7 — C2 onset rate rebu\n\nexp_humanoid_008d_s0: status=PENDING, concl=\n  categories: ['008d']\n  eval_val: None\n  hyp: Humanoid Walk trained dt_emb + gate + subsample ON (008d config: gate_fixed_dt=2, gate_subsample_max_dt=2, H=8), seed=0 \n\nexp_quadruped_008d_s0: status=PENDING, concl=\n  categories: ['008d']\n  eval_val: None\n  hyp: Quadruped Walk trained dt_emb + gate + subsample ON (008d config: gate_fixed_dt=2, gate_subsample_max_dt=2, H=8), seed=0",
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

_source line 170_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me map each Table 2 row to the registry experiments and extract eval_return values. Let me compile the full picture.

From the comprehensive data, here's my mapping:

**1. Untreated (10 seeds) - 008d config (trained dt_emb + subsample ON + dt=2 + H=8)**
These are Walker + Cheetah 008d experiments:
- Walker 008d seeds: exp_008d_subsample_on_h8 (s0/1, eval=82.75), exp_009b_008d_walker_s2 (s2, eval=267.93), exp_008d_civo_trigger_s3 (s3, eval=267.6), exp_008d_civo_trigger_s4 (s4, ?), exp_059_walker_trained_s5 (s5, eval=95.8

), exp_068_008d_walker_repro_s1 (s1, eval=39.1)
- Cheetah: exp_010b_cheetah_civo_trigger_s0 (eval=0.83), exp_010b_cheetah_civo_trigger (s1, eval=51.7), exp_078_cheetah_008d_s0 (eval=119.5), exp_088_cheetah_008d_s1 (eval=309.3), exp_091_cheetah_008d_s2 (eval=2.5), exp_097_cheetah_008d_s3 (eval=61.7)

I'm noticing the table labels don't quite match up with what I'm seeing in the experiment names, so let me recheck the groupings. Looking at the table structure more carefully, the "Untreated" row with 10 seeds represents the baseline CIVO trigger experiments combining both Walker and Cheetah results, where 0 out of 10 seeds achieved prevention, meaning all 10 triggered CIVO. The other rows show different interventions tested on top of this base configuration, with their respective seed counts and prevention rates.

Now I need to systematically map the available evaluation returns from the registry and artifact reports to reconstruct which specific experiments fall into each group, starting with the ones I can identify from the summary table and then filling in gaps by checking individual experiment reports. Looking at the cross-environment CSV data, I can see the Walker Walk Trigger experiments have 3 seeds with a mean eval of 140.6, while the Cheetah Run Trigger only has 2 seeds. But the NVE data shows 7 total seeds, not the 10 mentioned in the table, so some of the newer experiments like 068, 078, 088, 091, and 097 might be part of that official count.

The paper data is locked at D171, so I need to preserve the existing numbers and just add the eval_return standard deviations. Rather than manually tracking each experiment, I should write a script to parse the full registry and compute statistics for each Table 2 group, then cross-reference with the seed counts to identify any discrepancies. Since many registry experiments are missing eval_return values, I'll need to check the individual artifact reports for the gaps and look for a comprehensive audit file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "8d45f9d2-9040-45b8-8144-6138bc299791",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YD2axNASiG7qfQAkU2GW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13052,
      "cache_read_input_tokens": 74486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13052
      },
      "output_tokens": 26,
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

_source line 171_

有 213 个实验，但很多缺少 eval_return。让我搜索论文中已编译的完整数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "4a087002-63dc-4430-8cd5-cd457474269d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YD2axNASiG7qfQAkU2GW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13052,
      "cache_read_input_tokens": 74486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13052
      },
      "output_tokens": 26,
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

_source line 172_

<details open><summary>🔧 Tool call — Bash · `toolu_0165JZiPtFvAeqGQMPS5Ev5K`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_data_audit_20260526.md 2>/dev/null | head -100",
  "description": "Check paper data audit file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ae23ba9e-9a10-41e1-9af3-aef8d501dc40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YD2axNASiG7qfQAkU2GW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13052,
      "cache_read_input_tokens": 74486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13052
      },
      "output_tokens": 26,
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

_source line 173 · 2026-05-29T00:39:07.794Z_

<details><summary>↩ Tool result · `toolu_0165JZiPtFvAeqGQMPS5Ev5K`</summary>

```text
# Paper Data Audit (Pre-Lockdown)

**Date**: 2026-05-26 | **Deadline**: ICML 2026 data lockdown 2026-05-27
**RUNNING experiments**: exp_097_cheetah_008d_s3 (C2 4th seed), exp_100_walker_008a_s1 (C3 2nd seed)
**PREPARING**: rssm_fidelity_v2, exp_101_rssm_prediction_quality (supplementary, not claim-blocking)

---

## Claim C1: Variable-rate imagination consistently degrades performance

### 支撑实验

| exp_id | env | config | seed | eval_peak | eval_final | conclusion |
|--------|-----|--------|------|-----------|------------|------------|
| exp_001_baseline | Walker | dt=1 baseline | 1 | 970.4 | ~951 | ✅ reference |
| exp_006_fixed_dt2 | Walker | dt=2, subsample ON, trained dt_emb, H=15 | 1 | 485.3 | ~135 (collapse) | ❌ collapse |
| exp_007_fixed_dt4 | Walker | dt=4 | 1 | 176.9 | 144.4@45K | ❌ severe degradation |
| exp_005_event_gated_v4 | Walker | learned gate | 1 | 541.2 | ~99@145K | ❌ collapse |
| exp_008d_subsample_on_h8 | Walker | dt=2, subsample ON, trained dt_emb, H=8 | 1 | 167.2 | 82.8 | ❌ collapse |
| exp_077_cheetah_baseline_s0 | Cheetah | dt=1 baseline | 0 | 448.1 | 448.1 | ✅ reference |
| exp_083_cheetah_baseline_s1 | Cheetah | dt=1 baseline | 1 | 466.0 | 444.0 | ✅ reference |
| exp_078_cheetah_008d_s0 | Cheetah | dt=2, trained dt_emb | 0 | 213.7 | 119.5 | ❌ degraded |
| exp_088_cheetah_008d_s1 | Cheetah | dt=2, trained dt_emb | 1 | 309.3 | 309.3 | ❌ degraded (no collapse) |
| exp_091_cheetah_008d_s2 | Cheetah | dt=2, trained dt_emb | 2 | 213.8 | 2.5 | ❌ catastrophic collapse |

### 证据充分性: ✅ Strong
- 3 dt>1 configurations (fixed dt=2, fixed dt=4, learned gate) all degrade in Walker
- Cross-environment: Cheetah 3/3 seeds degrade vs baseline (eval 119-309 vs baseline 444-466)
- No positive result for variable-rate imagination in any configuration
- Seeds: Walker 1 seed per config (sufficient for pattern), Cheetah 3 seeds for trained dt_emb
- **无缺口**

---

## Claim C2: Trained dt_embedding creates CIVO susceptibility (stochastic onset)

### 支撑实验 — Trained dt_emb (onset expected)

| exp_id | env | seed | NVE_peak | NVE_final | eval_peak | eval_final | CIVO onset? |
|--------|-----|------|----------|-----------|-----------|------------|-------------|
| exp_008d / exp_009e | Walker | 0/1 | 4.13@55K | 1.03 | 167→131 | 131 | ✅ sustained collapse |
| exp_009b | Walker | 2 | 1.62@45K | 0.38@105K | — | 268 | ✅ onset, self-corrected |
| exp_008d_civo_trigger_s3 | Walker | 3 | 1.53 | 1.53 | 451.7 | 267.6 | ✅ borderline onset |
| exp_008d_civo_trigger_s4 | Walker | 4 | 4.62 | — | — | — | ✅ onset |
| exp_059_walker_trained_s5 | Walker | 5 | 4.72 | 1.22 | — | 95.8 | ✅ onset, self-correcting |
| exp_078_cheetah_008d_s0 | Cheetah | 0 | 4.10@75K | — | 213.7 | 119.5 | ✅ onset |
| exp_088_cheetah_008d_s1 | Cheetah | 1 | 0.517 | — | 309.3 | 309.3 | ❌ no onset |
| exp_091_cheetah_008d_s2 | Cheetah | 2 | 138.7@95K | — | 213.8 | 2.5 | ✅ extreme onset |
| **exp_097_cheetah_008d_s3** | **Cheetah** | **3** | **—** | **—** | **—** | **—** | **🔄 RUNNING** |

**Walker onset rate**: 5/5 (100%)
**Cheetah onset rate**: 2/3 completed (67%), exp_097 pending → will be 2/4 or 3/4

### 支撑实验 — Frozen dt_emb (control, onset NOT expected)

| exp_id | env | seed | NVE_peak | eval_final | CIVO onset? |
|--------|-----|------|----------|------------|-------------|
| exp_042 | Walker | 0 | 0.194 | 612.5 | ❌ |
| exp_067 | Walker | 0 | 0.40 | 281.5 | ❌ |
| exp_047 | Walker | 1 | 1.71 (transient) | 144.2 | ❌ (self-corrected) |
| exp_057 | Walker | 2 | 1.88 (transient) | 123.9 | ❌ (self-corrected) |
| exp_084 | Walker | 0 | — | 334.1 | ❌ |
| exp_085 | Walker | 1 | — | 281.5 | ❌ |
| exp_046 | Cheetah | 0 | 1.35 | 150.5 | ❌ |
| exp_058 | Cheetah | 1 | 0.78 | 80.5 | ❌ |
| exp_086 | Cheetah | 0 | — (ve<0.2) | 326.4 | ❌ |
| exp_087 | Cheetah | 1 | — (ve<0.2) | 310.1 | ❌ |

**Frozen onset rate**: 0/10 (0%) — no sustained NVE>1.5×

### 支撑实验 — No dt_emb (control)

| exp_id | env | seed | NVE_peak | eval_final | CIVO onset? |
|--------|-----|------|----------|------------|-------------|
| exp_069 | Walker | 1 | 0.66 | 237.8 | ❌ |
| exp_043 | Walker | 1 | 0.808 | — | ❌ |
| exp_082 | Cheetah | 0 | 1.58 (transient) | 83.2 | ❌ |
| exp_092 | Cheetah | 1 | 0.99 | 77.3 | ❌ |
| exp_093 | Cheetah | 2 | 0.98 | 151.2 | ❌ |
| exp_024b_s0 | Cheetah | 0 | 0.20 | 96.5 | ❌ |
| exp_024b_s1 | Cheetah | 1 | 0.10 | 77.3 | ❌ |

**No-dt_emb onset rate**: 0/7 (0%)

### 证据充分性: ✅ Strong
- **Necessity robustly confirmed**: trained 7/8 onset vs frozen 0/10 vs removed 0/7 (Fisher exact p < 0.001)
- Three-way causal design rules out "embedding presence" — only gradient training creates susceptibility
- Cross-env: Walker 5/5, Cheetah 2/3 onset
- **exp_097 (RUNNING)**: 4th Cheetah seed. Current onset rate 2/3. Completion adds data point but does NOT change claim direction — necessity already confirmed. Even if s3 = no onset (2/4), cross-env onset rate remains ~70% (7/9)
- **无关键缺口**

---

## Claim C3: Untrained dt_embedding prevents optimistic drift (value suppression)

### 支撑实验

| exp_id | env | seed | eval_peak | eval_final | NVE range | ve suppression? |
|--------|-----|------|-----------|------------|-----------|-----------------|
| exp_008a_no_subsample_dt2 | Walker | 0 | 777.7 | 572.2@105K | 0.59–0.93× | ✅ |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "c8a4f315-f848-4cb9-94e7-c01963bcafd5",
  "tool_use_result": {
    "stdout": "# Paper Data Audit (Pre-Lockdown)\n\n**Date**: 2026-05-26 | **Deadline**: ICML 2026 data lockdown 2026-05-27\n**RUNNING experiments**: exp_097_cheetah_008d_s3 (C2 4th seed), exp_100_walker_008a_s1 (C3 2nd seed)\n**PREPARING**: rssm_fidelity_v2, exp_101_rssm_prediction_quality (supplementary, not claim-blocking)\n\n---\n\n## Claim C1: Variable-rate imagination consistently degrades performance\n\n### 支撑实验\n\n| exp_id | env | config | seed | eval_peak | eval_final | conclusion |\n|--------|-----|--------|------|-----------|------------|------------|\n| exp_001_baseline | Walker | dt=1 baseline | 1 | 970.4 | ~951 | ✅ reference |\n| exp_006_fixed_dt2 | Walker | dt=2, subsample ON, trained dt_emb, H=15 | 1 | 485.3 | ~135 (collapse) | ❌ collapse |\n| exp_007_fixed_dt4 | Walker | dt=4 | 1 | 176.9 | 144.4@45K | ❌ severe degradation |\n| exp_005_event_gated_v4 | Walker | learned gate | 1 | 541.2 | ~99@145K | ❌ collapse |\n| exp_008d_subsample_on_h8 | Walker | dt=2, subsample ON, trained dt_emb, H=8 | 1 | 167.2 | 82.8 | ❌ collapse |\n| exp_077_cheetah_baseline_s0 | Cheetah | dt=1 baseline | 0 | 448.1 | 448.1 | ✅ reference |\n| exp_083_cheetah_baseline_s1 | Cheetah | dt=1 baseline | 1 | 466.0 | 444.0 | ✅ reference |\n| exp_078_cheetah_008d_s0 | Cheetah | dt=2, trained dt_emb | 0 | 213.7 | 119.5 | ❌ degraded |\n| exp_088_cheetah_008d_s1 | Cheetah | dt=2, trained dt_emb | 1 | 309.3 | 309.3 | ❌ degraded (no collapse) |\n| exp_091_cheetah_008d_s2 | Cheetah | dt=2, trained dt_emb | 2 | 213.8 | 2.5 | ❌ catastrophic collapse |\n\n### 证据充分性: ✅ Strong\n- 3 dt>1 configurations (fixed dt=2, fixed dt=4, learned gate) all degrade in Walker\n- Cross-environment: Cheetah 3/3 seeds degrade vs baseline (eval 119-309 vs baseline 444-466)\n- No positive result for variable-rate imagination in any configuration\n- Seeds: Walker 1 seed per config (sufficient for pattern), Cheetah 3 seeds for trained dt_emb\n- **无缺口**\n\n---\n\n## Claim C2: Trained dt_embedding creates CIVO susceptibility (stochastic onset)\n\n### 支撑实验 — Trained dt_emb (onset expected)\n\n| exp_id | env | seed | NVE_peak | NVE_final | eval_peak | eval_final | CIVO onset? |\n|--------|-----|------|----------|-----------|-----------|------------|-------------|\n| exp_008d / exp_009e | Walker | 0/1 | 4.13@55K | 1.03 | 167→131 | 131 | ✅ sustained collapse |\n| exp_009b | Walker | 2 | 1.62@45K | 0.38@105K | — | 268 | ✅ onset, self-corrected |\n| exp_008d_civo_trigger_s3 | Walker | 3 | 1.53 | 1.53 | 451.7 | 267.6 | ✅ borderline onset |\n| exp_008d_civo_trigger_s4 | Walker | 4 | 4.62 | — | — | — | ✅ onset |\n| exp_059_walker_trained_s5 | Walker | 5 | 4.72 | 1.22 | — | 95.8 | ✅ onset, self-correcting |\n| exp_078_cheetah_008d_s0 | Cheetah | 0 | 4.10@75K | — | 213.7 | 119.5 | ✅ onset |\n| exp_088_cheetah_008d_s1 | Cheetah | 1 | 0.517 | — | 309.3 | 309.3 | ❌ no onset |\n| exp_091_cheetah_008d_s2 | Cheetah | 2 | 138.7@95K | — | 213.8 | 2.5 | ✅ extreme onset |\n| **exp_097_cheetah_008d_s3** | **Cheetah** | **3** | **—** | **—** | **—** | **—** | **🔄 RUNNING** |\n\n**Walker onset rate**: 5/5 (100%)\n**Cheetah onset rate**: 2/3 completed (67%), exp_097 pending → will be 2/4 or 3/4\n\n### 支撑实验 — Frozen dt_emb (control, onset NOT expected)\n\n| exp_id | env | seed | NVE_peak | eval_final | CIVO onset? |\n|--------|-----|------|----------|------------|-------------|\n| exp_042 | Walker | 0 | 0.194 | 612.5 | ❌ |\n| exp_067 | Walker | 0 | 0.40 | 281.5 | ❌ |\n| exp_047 | Walker | 1 | 1.71 (transient) | 144.2 | ❌ (self-corrected) |\n| exp_057 | Walker | 2 | 1.88 (transient) | 123.9 | ❌ (self-corrected) |\n| exp_084 | Walker | 0 | — | 334.1 | ❌ |\n| exp_085 | Walker | 1 | — | 281.5 | ❌ |\n| exp_046 | Cheetah | 0 | 1.35 | 150.5 | ❌ |\n| exp_058 | Cheetah | 1 | 0.78 | 80.5 | ❌ |\n| exp_086 | Cheetah | 0 | — (ve<0.2) | 326.4 | ❌ |\n| exp_087 | Cheetah | 1 | — (ve<0.2) | 310.1 | ❌ |\n\n**Frozen onset rate**: 0/10 (0%) — no sustained NVE>1.5×\n\n### 支撑实验 — No dt_emb (control)\n\n| exp_id | env | seed | NVE_peak | eval_final | CIVO onset? |\n|--------|-----|------|----------|------------|-------------|\n| exp_069 | Walker | 1 | 0.66 | 237.8 | ❌ |\n| exp_043 | Walker | 1 | 0.808 | — | ❌ |\n| exp_082 | Cheetah | 0 | 1.58 (transient) | 83.2 | ❌ |\n| exp_092 | Cheetah | 1 | 0.99 | 77.3 | ❌ |\n| exp_093 | Cheetah | 2 | 0.98 | 151.2 | ❌ |\n| exp_024b_s0 | Cheetah | 0 | 0.20 | 96.5 | ❌ |\n| exp_024b_s1 | Cheetah | 1 | 0.10 | 77.3 | ❌ |\n\n**No-dt_emb onset rate**: 0/7 (0%)\n\n### 证据充分性: ✅ Strong\n- **Necessity robustly confirmed**: trained 7/8 onset vs frozen 0/10 vs removed 0/7 (Fisher exact p < 0.001)\n- Three-way causal design rules out \"embedding presence\" — only gradient training creates susceptibility\n- Cross-env: Walker 5/5, Cheetah 2/3 onset\n- **exp_097 (RUNNING)**: 4th Cheetah seed. Current onset rate 2/3. Completion adds data point but does NOT change claim direction — necessity already confirmed. Even if s3 = no onset (2/4), cross-env onset rate remains ~70% (7/9)\n- **无关键缺口**\n\n---\n\n## Claim C3: Untrained dt_embedding prevents optimistic drift (value suppression)\n\n### 支撑实验\n\n| exp_id | env | seed | eval_peak | eval_final | NVE range | ve suppression? |\n|--------|-----|------|-----------|------------|-----------|-----------------|\n| exp_008a_no_subsample_dt2 | Walker | 0 | 777.7 | 572.2@105K | 0.59–0.93× | ✅ |",
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

_source line 174_

<details open><summary>🔧 Tool call — Bash · `toolu_01WYNJ6tnGtSutH9NSJe1k43`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/tables/ 2>/dev/null",
  "description": "Check tables directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "4964e8a1-5e63-4366-b688-fcbe8615ccb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YD2axNASiG7qfQAkU2GW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13052,
      "cache_read_input_tokens": 74486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13052
      },
      "output_tokens": 26,
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

_source line 175 · 2026-05-29T00:39:08.286Z_

<details><summary>↩ Tool result · `toolu_01WYNJ6tnGtSutH9NSJe1k43`</summary>

```text
ablation_mechanism_table.tex
cross_env_civo_comparison.csv
cross_env_civo_comparison.tex
temporal_causality_table.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "124436e5-6a2d-47a8-9aa2-f6d4f19f8e0c",
  "tool_use_result": {
    "stdout": "ablation_mechanism_table.tex\ncross_env_civo_comparison.csv\ncross_env_civo_comparison.tex\ntemporal_causality_table.tex",
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

_source line 176_

<details><summary>Logged reasoning block</summary>

```text
Excellent! The paper data audit has very comprehensive data. Now let me continue reading it to get the data for the intervention hierarchy table (Table 2). I need to find data specifically about the intervention experiments.

Let me also check the existing paper tables and the experiment reports for missing eval_return values.

Let me construct a complete mapping. The key challenge is that Table 2's "Untreated" row (10 seeds) and other rows need eval_return values. The audit shows me:

For "Untreated" (trained dt_emb, CIVO trigger):
- Walker s0/1: eval_final = 131 (from exp_008d / exp_009e)  


- Walker s2: eval_final = 268 (exp_009b)
- Walker s3: eval_final = 267.6 (exp_008d_civo_trigger_s3)
- Walker s4: eval_final = ? (exp_008d_civo_trigger_s4 - not listed)
- Walker s5: eval_final = 95.8 (exp_059_walker_trained_s5)
- Cheetah s0: eval_final = 119.5 (exp_078)
- Cheetah s1: eval_final = 309

.3 (exp_088)
- Cheetah s2: eval_final = 2.5 (exp_091)
- Cheetah s3: eval_final = 61.7 (exp_097)

Let me verify the seed count here. Walker has 6 seeds across different experiments, and Cheetah has 4 seeds, totaling 10. The experiments span both older runs and newer ones, with some using the CIVO trigger setup and others using different training approaches.

Looking at the NVE data more carefully, I'm seeing some experiments are relabeled versions of the same run—like exp_008d/009e both refer to Walker s1 with an NVE value of 4.13. The other Walker seeds show varying performance: s2 at 1.62, s3 at 1.53, s4 at 4.62, and s5 at 4.72. For Cheetah, the older experiments show higher NVE values (exp_048 at 70.64, exp_010b at 8.27), but the newer audit data reveals exp_078 with a much lower NVE of 4, suggesting there's been significant variation or improvement in the experimental setup.

The newer Cheetah experiments (exp_078, 088, 091, 097) show a wide range of results—from 0.517 to 138.7—which is puzzling given they appear to be from the same experimental series. I'm trying to reconcile this with Table 2's 10 seeds, which likely splits between 5 Walker and 5 Cheetah runs, but the actual experiment counts don't quite line up with what I'm seeing in the data. I'm noticing a discrepancy—exp_088 s1 shows an NVE of 0.517, which would fall below the 2.0x prevention threshold, yet the table indicates 0 out of 10 seeds were protected. Let me reconsider which seeds make up this group of 10: the 5 Walker seeds plus the older Cheetah experiments (exp_010b s0 and s1 with very high NVE values), and potentially three newer Cheetah seeds, though exp_088 s1's low NVE value complicates this accounting. I'm trying to figure out what combination of experiments makes up those 10 untreated seeds. It could be Walker plus Cheetah plus possibly PickCube, or maybe it includes the original exp_008d subsample separately. Looking at the NVE values more carefully, I can identify the five Walker seeds by their experiment IDs and NVE scores, and I'm starting to map out the Cheetah seeds the same way.

The issue is that the NVE data shows only 7 trigger seeds total, but the table claims 10—which suggests the newer Cheetah experiments were added after the NVE audit was completed. Rather than trying to reconcile all these discrepancies, I'll take a more direct approach: parse the full registry programmatically to extract all eval_return values for each group in Table 2, then compute the statistics from that complete dataset.

Writing registry parser...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "6cdd079a-2e77-4ae8-8803-d8d212a69b15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2JWp7gJiQRPBz3vEQw8u4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4475,
      "cache_read_input_tokens": 87538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4475
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
