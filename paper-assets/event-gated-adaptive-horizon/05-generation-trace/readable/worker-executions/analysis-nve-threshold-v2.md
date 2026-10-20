# analysis nve threshold v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_analysis_nve_threshold_v2_20260525T201901.log`
- **Structured JSON:** [`04587445af8281d334b7.json`](../../sessions/04/04587445af8281d334b7.json)

## Before a recorded user message

55 recorded events

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
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "105ffba8-2527-4cd9-98b6-150facd53629",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779752400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a9f5eca3-8946-44b0-af27-777bc5dccd8c",
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task:

1. Read all experiments from the registry
2. Extract NVE data for all experiments including the previously missing ones (exp_084, exp_085, exp_086, exp_087)
3. Compute two methods of NVE threshold analysis
4. Implement combined diagnostic criteria
5. Compute NVE_median_last5
6. Write analysis report and register artifact

Let me start by reading the registry and understanding the data structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "9f22bbe1-b5df-471f-87db-68472c7226c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019umjbJZu3vLRbJdf9AxWpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12122,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12122
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

### Assistant

_source line 5_

我来执行 NVE 阈值分析 V2。先读取 registry 和项目文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "be9aa31d-bd36-422b-879d-9801fae3084f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019umjbJZu3vLRbJdf9AxWpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12122,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12122
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DNwdUbccxEJ1269xh1ynGe`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
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
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "5c6f0183-3ddd-468a-ba2d-557ba12032f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019umjbJZu3vLRbJdf9AxWpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12122,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12122
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

_source line 7 · 2026-05-25T20:19:21.591Z_

<details><summary>↩ Tool result · `toolu_01DNwdUbccxEJ1269xh1ynGe`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "4ae85011-a459-4fd0-a697-e2a7628b3ce5",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01HwbkRoVJfrCDzDWuVe4ShL`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
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
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "2257de5f-dc20-457c-8900-ad3c0743a599",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5ZNEDLuCiHciJazAo6esj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1212,
      "cache_read_input_tokens": 23963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1212
      },
      "output_tokens": 44,
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

_source line 9 · 2026-05-25T20:19:25.445Z_

<details><summary>↩ Tool result · `toolu_01HwbkRoVJfrCDzDWuVe4ShL`</summary>

```text
Error: result (375,931 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "e1f54dd7-50d0-440e-a499-4eea9972470c",
  "tool_use_result": {
    "content": "Error: result (375,931 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_090_cheetah_no_dt_emb_s2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T20:15:41.571Z\", \"updated_at\": \"2026-05-25T20:17:44.601Z\", \"hypothesis\": \"Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_embedding 完全移除后预期无 CIVO，加强 C2 cross-env causal control 多 seed 证据基础。plan_022。\", \"parent\": \"exp_082_cheetah_no_dt_emb_s0\", \"spec\": {\"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (dt_embed_dim=0, Cheetah causal control)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && git pull && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_090_cheetah_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"307484\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_090_cheetah_no_dt_emb_s2.log\", \"eval_data\": \"dmc_cheetah_run (online eval)\"}}, \"exp_086_frozen_dt_emb_cheetah_s0\": {\"status\": \"ANALYZING\", \"retry_count\": 1, \"created_at\": \"2026-05-25T16:24:01.866Z\", \"updated_at\": \"2026-05-25T20:17:42.278Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Cheetah Run does not trigger CIVO — cross-environment validation that dt_emb TRAINING is CIVO necessary condition. Paired with exp_078 (trained dt_emb, NVE=4.1×). Re-run after orphan process incident.\", \"parent\": \"exp_078_cheetah_008d_s0\", \"completed_at\": \"2026-05-25T18:08:31.088Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T20:17:39.670Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T18:08:47.611867+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T20:17:50.028253+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_086_frozen_dt_emb_cheetah_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"westd-19154\", \"gpu_ids\": [0], \"pid\": \"40743\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FrozenDtEmb_SubsampleON_Dt2_H8\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\"}}, \"exp_089_cheetah_no_dt_emb_s1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T20:15:40.357Z\", \"updated_at\": \"2026-05-25T20:17:40.651Z\", \"hypothesis\": \"Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_embedding 完全移除后预期无 CIVO，加强 C2 cross-env causal control 多 seed 证据基础。plan_022。\", \"parent\": \"exp_082_cheetah_no_dt_emb_s0\", \"spec\": {\"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (dt_embed_dim=0, Cheetah causal control)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && git pull && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_089_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"307263\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_089_cheetah_no_dt_emb_s1.log\", \"eval_data\": \"dmc_cheetah_run (online eval)\"}}, \"exp_009b_008d_walker_s2\": {\"account\": \"root\", \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 1 sustained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x→2.09x→4.12x) and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold (at 35K+ steps) is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009b_008d_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T18:51:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:25.186Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T18:47:21.873692+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_008d (s0, collapse confirmed at ~55K, NVE=1.67×@55K). 预期在 ~55K 步内触发 CIVO collapse，验证 trained dt_emb 导致的 delusional critic collapse 的跨 seed 可复现性。plan_011。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009b_008d_walker_s2.log\", \"metrics\": {\"ve_ratio_peak\": 0.5703, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 0.25, \"ve_ratio_final_step\": 105000, \"nve_peak\": 1.62, \"nve_peak_step\": 45000, \"nve_peak_note\": \"step-matched s1 baseline @45K = 0.331; arithmetic peak @25K=2.04x excluded (baseline<0.1)\", \"nve_classification\": \"onset_self_correcting\"}, \"notes\": \"D032: Collapse NOT reproduced in seed 2. nve peaked 2.05x@25K (transient) then self-corrected to 0.38x@105K. Eval rose to 268. Contrast: seed 1 had SUSTAINED nve>1.5x at 35K+ (1.71x→2.09x→4.12x) → collapse to 83. Key finding: nve>1.5x threshold (35K+ steps) is reliable trained dt_emb marker (2/2 seeds), but collapse is stochastic (1/2). Framing proposal submitted to Director.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"887053\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-14T18:47:20.636Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, trained dt_embed)\", \"seed\": 2, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T19:54:21.605Z\"}, \"exp_009e_008d_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T11:26:52.478Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T11:09:15.367Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_008d (s0, collapse confirmed at ~55K, NVE=1.67×@55K). 预期在 ~55K 步内触发 CIVO collapse，验证 trained dt_emb 导致的 delusional critic collapse 的跨 seed 可复现性。plan_011。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/metrics.jsonl\", \"metrics\": {\"ve_ratio_peak\": 1.6663, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 1.03, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.13, \"nve_peak_step\": 55000, \"nve_peak_note\": \"step-matched s1 baseline @55K = 0.4035; paper onset NVE @45K = 2.09x\", \"nve_classification\": \"onset_collapse\"}, \"notes\": \"008d extended replication (same seed=1, 009e extends 008d from 55K to 105K). Eval trajectory 5K-55K identical to 008d (deterministic). Collapse confirmed at 105K: eval 131.08, nve@55K=4.12x (normalized). 65K bounce to 250 was transient, not recovery. actor_loss flipped positive @85K. Independent collapse rate = 1/2 (seed 1 collapsed, seed 2 self-corrected), NOT 2/3 — 008d and 009e are the same seed.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 119108, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009e_008d_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.43, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009e_008d_walker_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8\", \"pid\": \"119108\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:01:00Z\", \"wall_clock_seconds\": 19552.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T19:54:20.393Z\"}, \"exp_085_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T16:17:10.446Z\", \"updated_at\": \"2026-05-25T19:52:18.635Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk seed=1 does not trigger CIVO — multi-seed validation that dt_emb TRAINING is the necessary condition for CIVO onset. Current code version (fb56c860a+).\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_085_frozen_dt_emb_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"296781\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_085_frozen_dt_emb_walker_s1.log\", \"submitted_at\": \"2026-05-25T16:17:29.039Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"dreamerv3\", \"seed\": 1, \"checkpoint_source\": \"none (fresh training)\", \"eval_data\": \"dmc_walker_walk\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_085_frozen_dt_emb_walker_s1/latest.pt\", \"wall_clock_seconds\": 12139.0, \"gpu_hours\": 3.37}, \"reproduce\": {\"finished_at\": \"2026-05-25T19:31:38.872Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T19:31:47.198579+00:00\"}]}, \"metrics\": {\"eval_return_final\": 69.26, \"eval_return_best\": 281.53, \"best_step\": 65000, \"total_steps\": 105000, \"NVE_final\": 0.08, \"NVE_peak\": 0.31, \"gate_pattern\": \"100% dt=2 locked\", \"civo_alert\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T19:39:48.059Z\"}, \"exp_084_frozen_dt_emb_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T15:58:38.310Z\", \"updated_at\": \"2026-05-25T19:52:17.020Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk does not trigger CIVO — proving dt_emb TRAINING (not mere presence) is the necessary condition for CIVO onset. Re-run on current code version (fb56c860a+), replacing killed exp_079.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && git pull && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_084_frozen_dt_emb_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"296484\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_084_frozen_dt_emb_walker_s0.log\", \"submitted_at\": \"2026-05-25T16:17:20.106Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"dreamerv3\", \"seed\": 0, \"checkpoint_source\": \"none (fresh training)\", \"eval_data\": \"dmc_walker_walk\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_084_frozen_dt_emb_walker_s0/latest.pt\", \"wall_clock_seconds\": 12145.7, \"gpu_hours\": 3.37}, \"reproduce\": {\"finished_at\": \"2026-05-25T19:31:18.394Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T19:31:26.293176+00:00\"}]}, \"metrics\": {\"eval_return_final\": 281.48, \"eval_return_best\": 334.06, \"best_step\": 95000, \"total_steps\": 112000, \"NVE_final\": 0.31, \"NVE_peak\": 0.37, \"gate_pattern\": \"100% dt=2 locked\", \"civo_alert\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T19:39:45.775Z\"}, \"exp_088_cheetah_008d_s1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:50:48.276Z\", \"updated_at\": \"2026-05-25T18:51:30.295Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_088_cheetah_008d_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"42804\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_088_cheetah_008d_s1.log\", \"submitted_at\": \"2026-05-25T18:50:47.731Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [1], \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO trigger config, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\"}, \"hypothesis\": \"Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed)。预期触发 CIVO，验证 Cheetah CIVO onset 的跨 seed 可复现性。plan_021。\", \"parent\": \"exp_078_cheetah_008d_s0\"}, \"exp_082_cheetah_no_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T13:12:29.199Z\", \"updated_at\": \"2026-05-25T18:49:20.158Z\", \"hypothesis\": \"Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_emb 是 Cheetah CIVO 的必要条件。与 exp_078 (trained dt_emb, CIVO trigger) 构成因果对。plan_022。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_082_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_embed_dim 0\\\"\", \"server\": \"westd-19154\", \"gpu_ids\": [0], \"pid\": \"N/A\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (dt_embed_dim=0, Cheetah causal control)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\"}, \"pid\": \"29479\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_082_cheetah_no_dt_emb_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_082_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-25T16:21:37.237Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T16:21:43.091656+00:00\"}]}, \"metrics\": {\"eval_return_final\": 83.2, \"eval_return_peak\": 239.3, \"eval_return_peak_step\": 45000, \"eval_trajectory\": {\"5K\": 6.8, \"15K\": 32.2, \"25K\": 108.4, \"35K\": 119.4, \"45K\": 239.3, \"55K\": 157, \"65K\": 180.1, \"75K\": 178.6, \"85K\": 84.2, \"95K\": 57.7, \"105K\": 83.2}, \"ve_ratio_final\": 0.616, \"ve_ratio_peak\": 0.955, \"ve_ratio_peak_step\": 95000, \"ve_ratio_trajectory\": {\"15K\": 0.038, \"25K\": 0.069, \"35K\": 0.132, \"45K\": 0.103, \"55K\": 0.237, \"65K\": 0.268, \"75K\": 0.311, \"85K\": 0.724, \"95K\": 0.955, \"105K\": 0.616}, \"nve_peak\": 1.58, \"nve_peak_step\": 95000, \"nve_peak_note\": \"eval-variance-driven (eval=57.7, value=55.1, ve_ratio<1.0), NOT value overestimation\", \"nve_trajectory_35Kplus\": {\"35K\": 1.49, \"45K\": 0.59, \"55K\": 0.96, \"65K\": 0.55, \"75K\": 0.55, \"85K\": 0.98, \"95K\": 1.58, \"105K\": 1.02}, \"nve_classification\": \"no_civo\", \"civo\": false, \"civo_alert\": 0, \"civo_alert_steps\": [], \"value_mean_final\": 51.3, \"value_mean_95K\": 55.1, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"baseline_ref\": \"exp_077_cheetah_baseline_s0\", \"baseline_eval_105K\": 448.1, \"eval_pct_baseline\": \"18.6%\", \"causal_pair\": \"exp_078_cheetah_008d_s0\", \"causal_variable\": \"dt_embed_dim (082=0 vs 078=trained)\", \"total_steps\": 112000, \"total_env_steps\": 105000}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_082_cheetah_no_dt_emb_s0\", \"completed_at\": \"2026-05-25T16:27:45.939Z\"}, \"exp_087_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T16:29:59.272Z\", \"updated_at\": \"2026-05-25T18:45:37.694Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Cheetah Run seed=1 does not trigger CIVO — multi-seed cross-environment validation that dt_emb TRAINING is CIVO necessary condition. Paired with exp_086 (frozen s0) and exp_078 (trained, NVE=4.1×).\", \"parent\": \"exp_086_frozen_dt_emb_cheetah_s0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_087_frozen_dt_emb_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"36195\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_087_frozen_dt_emb_cheetah_s1.log\", \"submitted_at\": \"2026-05-25T16:30:22.662Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 1, \"model_name\": \"DreamerV3+FrozenDtEmb_SubsampleON_Dt2_H8\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\", \"wall_clock_seconds\": 8115.0, \"gpu_hours\": 2.25}, \"reproduce\": {\"finished_at\": \"2026-05-25T18:42:02.488Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T18:42:10.415795+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_087_frozen_dt_emb_cheetah_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_087_frozen_dt_emb_cheetah_s1.log\", \"metrics\": {\"eval_return_105K\": 186.9, \"eval_return_peak\": 310.1, \"eval_return_peak_step\": \"75K\", \"eval_trajectory\": {\"5K\": 13.5, \"15K\": 90.2, \"25K\": 199.3, \"35K\": 165.7, \"45K\": 299.2, \"55K\": 207.2, \"65K\": 196.8, \"75K\": 310.1, \"85K\": 246.8, \"95K\": 57.9, \"105K\": 186.9}, \"ve_ratio_105K\": 0.1, \"ve_ratio_peak\": 0.2, \"ve_ratio_peak_step\": \"95K\", \"civo_alert\": 0, \"NVE\": 0.33, \"NVE_baseline\": \"exp_083_cheetah_baseline_s1\", \"NVE_baseline_ve_ratio_peak\": 0.6, \"nve_classification\": \"no_civo\", \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"total_steps\": 112000, \"model_loss_105K\": 2.4}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T18:45:37.694Z\"}, \"exp_083_cheetah_baseline_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T14:14:00.361Z\", \"updated_at\": \"2026-05-25T18:09:32.066Z\", \"hypothesis\": \"Cheetah Run dt=1 baseline seed=1。多 seed baseline 用于更稳健的 NVE 归一化，与 exp_077 (seed=0, eval=448.1) 构成 calibration 对。plan_020 第二个 seed。\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_083_cheetah_baseline_s1 --steps 105000 --seed 1 --compile False --device cuda:0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"30581\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_083_cheetah_baseline_s1.log\", \"submitted_at\": \"2026-05-25T14:28:23.155Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 1, \"model_name\": \"DreamerV3_baseline_dt1\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"wall_clock_seconds\": 7365.2, \"gpu_hours\": 2.05}, \"reproduce\": {\"finished_at\": \"2026-05-25T16:28:26.304Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T16:28:32.490600+00:00\"}]}, \"metrics\": {\"eval_return_105K\": 444, \"eval_trajectory\": {\"5K\": 11.6, \"15K\": 76.4, \"25K\": 300.2, \"35K\": 372.3, \"45K\": 384.2, \"55K\": 395.4, \"65K\": 446.1, \"75K\": 440.5, \"85K\": 409, \"95K\": 466, \"105K\": 444}, \"ve_ratio_105K\": 0.6, \"ve_ratio_peak\": 0.6, \"ve_ratio_peak_step\": \"85K\", \"civo_alert\": 0, \"model_loss_105K\": 1.6}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_083_cheetah_baseline_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_083_cheetah_baseline_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T16:31:08.314Z\", \"parent\": \"exp_077_cheetah_baseline_s0\"}, \"exp_078_cheetah_008d_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:24.844Z\", \"updated_at\": \"2026-05-25T18:06:40.922Z\", \"hypothesis\": \"Trained dt_embedding with subsample ON + dt=2 + H=8 on Cheetah Run triggers CIVO — cross-environment validation (C2) that CIVO is not Walker-specific. Paired with exp_077 (baseline) for NVE calculation.\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"submitted_at\": \"2026-05-25T11:21:50.283Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11948.1, \"gpu_hours\": 3.32}, \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-25T14:27:13.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T14:27:19.359689+00:00\"}]}, \"metrics\": {\"eval_return_final\": 119.5, \"eval_return_peak\": 213.7, \"eval_return_peak_step\": 35000, \"eval_trajectory\": {\"5K\": 8.3, \"15K\": 41.3, \"25K\": 170, \"35K\": 213.7, \"45K\": 148.9, \"55K\": 64.5, \"65K\": 36.8, \"75K\": 26.1, \"85K\": 26.7, \"95K\": 32.5, \"105K\": 119.5}, \"ve_ratio_final\": 0.291, \"ve_ratio_peak\": 2.318, \"ve_ratio_peak_step\": 75000, \"ve_ratio_trajectory\": {\"15K\": 0.039, \"25K\": 0.056, \"35K\": 0.11, \"45K\": 0.295, \"55K\": 0.908, \"65K\": 1.72, \"75K\": 2.318, \"85K\": 2.022, \"95K\": 1.366, \"105K\": 0.291}, \"nve_peak\": 4.1, \"nve_peak_step\": 75000, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.7, \"nve_trajectory_35Kplus\": {\"35K\": 1.24, \"45K\": 1.7, \"55K\": 3.66, \"65K\": 3.55, \"75K\": 4.1, \"85K\": 2.74, \"95K\": 2.26, \"105K\": 0.48}, \"nve_classification\": \"onset_self_correcting\", \"civo\": true, \"civo_alert\": 1, \"civo_alert_steps\": [55000, 65000], \"civo_sustained_range\": \"45K-95K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 105000, \"value_mean_peak\": 63.3, \"value_mean_peak_step\": 65000, \"value_mean_final\": 34.8, \"delta_ve_peak\": 0.814, \"delta_ve_peak_step\": 65000, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"baseline_ref\": \"exp_077_cheetah_baseline_s0\", \"baseline_eval_105K\": 448.1, \"eval_pct_baseline\": \"26.7%\", \"total_steps\": 112000, \"total_env_steps\": 105000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_078_cheetah_008d_s0/latest.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T14:40:58.408Z\"}, \"exp_077_cheetah_baseline_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:21.685Z\", \"updated_at\": \"2026-05-25T18:06:38.886Z\", \"hypothesis\": \"Cheetah Run dt=1 baseline seed=0. Establishes NVE normalization denominator for Cheetah CIVO experiments. Paired with exp_078 (trained dt_emb CIVO trigger) and exp_083 (baseline seed=1).\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"submitted_at\": \"2026-05-25T11:21:44.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10257.0, \"gpu_hours\": 2.85}, \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-25T14:07:47.479Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T14:07:53.264245+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 448.1, \"eval_trajectory\": {\"5K\": 12.2, \"15K\": 18.4, \"25K\": 182.9, \"35K\": 356, \"45K\": 377.2, \"55K\": 441, \"65K\": 317.3, \"75K\": 340.9, \"85K\": 309.3, \"95K\": 418.4, \"105K\": 448.1}, \"ve_ratio_105K\": 0.611, \"ve_ratio_peak\": 0.739, \"ve_ratio_peak_step\": \"85K\", \"civo_alert\": 0, \"model_loss_105K\": 1.83, \"total_steps\": 112000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_077_cheetah_baseline_s0/latest.pt\", \"completed_at\": \"2026-05-25T14:12:41.181Z\"}, \"exp_079_frozen_dt_emb_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:27.865Z\", \"updated_at\": \"2026-05-25T18:06:36.594Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk does not trigger CIVO — proving dt_emb TRAINING is the necessary condition for CIVO onset. Duplicate of exp_067, killed before completion.\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"parent\": \"exp_067_frozen_dt_emb_walker_plan015\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_079_frozen_dt_emb_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"283090\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_079_frozen_dt_emb_walker_s0.log\", \"submitted_at\": \"2026-05-25T11:21:37.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 392.1, \"gpu_hours\": 0.11}, \"pid\": \"283090\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_079_frozen_dt_emb_walker_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_079_frozen_dt_emb_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T11:28:10.029Z\"}, \"exp_081_008e_v3_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T12:09:44.566Z\", \"updated_at\": \"2026-05-25T15:49:23.869Z\", \"hypothesis\": \"Trained dt_emb with dt=1 imagination + subsample ON (max_dt=2) + H=15 does not trigger CIVO on Walker Walk — multi-seed validation seed=2 of C6 mitigation config 008e_v3\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_081_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"285949\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"submitted_at\": \"2026-05-25T12:10:38.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 2, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\", \"wall_clock_seconds\": 13125.4, \"gpu_hours\": 3.65}, \"reproduce\": {\"finished_at\": \"2026-05-25T15:37:00.120Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T15:37:06.073794+00:00\"}]}, \"metrics\": {\"eval_return_105k\": 597.1, \"ve_ratio_105k\": 0.5, \"civo_alert\": 0, \"gate_dt_1_frac\": 1, \"baseline_pct\": 64.2, \"train_return_112k_mean\": 583.8}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_081_008e_v3_walker_s2/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-25T15:49:23.870Z\"}, \"exp_080_008e_v3_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:30:20.594Z\", \"updated_at\": \"2026-05-25T15:49:21.640Z\", \"hypothesis\": \"Trained dt_emb with dt=1 imagination + subsample ON (max_dt=2) + H=15 does not trigger CIVO on Walker Walk — multi-seed validation seed=1 of C6 mitigation config 008e_v3\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_080_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"283925\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_080_008e_v3_walker_s1.log\", \"submitted_at\": \"2026-05-25T11:30:51.090Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 1, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\", \"wall_clock_seconds\": 15510.5, \"gpu_hours\": 4.31}, \"reproduce\": {\"finished_at\": \"2026-05-25T15:44:00.217Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T15:44:06.170688+00:00\"}]}, \"metrics\": {\"eval_return_105k\": 876.7, \"ve_ratio_105k\": 0.6, \"civo_alert\": 0, \"gate_dt_1_frac\": 1, \"baseline_pct\": 94.3, \"train_return_112k_mean\": 926.8}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_080_008e_v3_walker_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_080_008e_v3_walker_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T15:49:21.640Z\"}, \"exp_074_008a_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:08:57.028Z\", \"updated_at\": \"2026-05-25T12:08:22.221Z\", \"hypothesis\": \"Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_074_008a_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"274730\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_074_008a_walker_s3.log\", \"submitted_at\": \"2026-05-25T09:09:28.652Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10733.6, \"gpu_hours\": 2.98}, \"pid\": \"274730\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_074_008a_walker_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_074_008a_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T12:04:22.816Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:04:34.186555+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 855.9, \"civo_ve_ratio_final\": 0.3, \"civo_alert\": 0, \"value_mean_105K\": 295.2, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"model_loss_105K\": 3.8, \"eval_trajectory\": {\"5K\": 36.1, \"15K\": 281, \"25K\": 389.8, \"35K\": 303.8, \"45K\": 437.3, \"55K\": 411.3, \"65K\": 566.4, \"75K\": 513.9, \"85K\": 645.9, \"95K\": 776.6, \"105K\": 855.9}, \"four_seed_summary\": {\"mean_eval_return\": 791, \"std_eval_return\": 102.2, \"all_civo_alert_0\": true, \"seeds_completed\": 4}}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_074_008a_walker_s3/latest.pt\", \"completed_at\": \"2026-05-25T12:08:22.221Z\"}, \"exp_076_cheetah_civo_trigger_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:03:42.328Z\", \"updated_at\": \"2026-05-25T10:48:15.566Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=2: trained dt_emb + subsample ON + dt=2 + H=8。将 Cheetah CIVO trigger 扩展到第 3 个独立 seed，巩固跨环境 claim 统计力度。来源: plan_021 扩展。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_076_cheetah_civo_trigger_s3 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"19953\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_076_cheetah_civo_trigger_s3.log\", \"submitted_at\": \"2026-05-25T10:44:40.370Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 215.2, \"gpu_hours\": 0.06}, \"pid\": \"19953\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_076_cheetah_civo_trigger_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_076_cheetah_civo_trigger_s3 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T10:48:15.566Z\"}, \"exp_075_cheetah_civo_trigger_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:03:40.222Z\", \"updated_at\": \"2026-05-25T10:48:13.465Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=1: trained dt_emb + subsample ON + dt=2 + H=8 on westd-19154。复现 exp_010b 配置（原 seed=1 在 bjb1-45299），跨服务器验证 Cheetah CIVO 可复现性。来源: plan_021 扩展。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_075_cheetah_civo_trigger_s2 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"19788\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_075_cheetah_civo_trigger_s2.log\", \"submitted_at\": \"2026-05-25T10:44:34.345Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 219.1, \"gpu_hours\": 0.06}, \"pid\": \"19788\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_075_cheetah_civo_trigger_s2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_075_cheetah_civo_trigger_s2 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T10:48:13.465Z\"}, \"exp_071_008f_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:03:48.097Z\", \"updated_at\": \"2026-05-25T10:42:39.889Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=3。当前 008f 2 seeds 结果分歧（s1=success eval=503, s2=negative eval=148），增加 seed 缩窄 causal control 稳定性估计。来源: plan_012 扩展。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_071_008f_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"265628\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_071_008f_walker_s3.log\", \"submitted_at\": \"2026-05-25T07:04:24.723Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13095.2, \"gpu_hours\": 3.64}, \"pid\": \"265628\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_071_008f_walker_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_071_008f_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T10:05:58.573Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T10:06:05.930693+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 311.9, \"eval_return_peak\": 457.7, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.7, \"gate_dt_mean_final\": 2, \"civo_alert\": 0, \"value_loss_final\": 1, \"actor_entropy_final\": -4.6, \"model_loss_final\": 4.5}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_071_008f_walker_s3\", \"completed_at\": \"2026-05-25T10:42:39.889Z\"}, \"exp_073_008f_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:30:42.251Z\", \"updated_at\": \"2026-05-25T10:00:42.604Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=4。当前 008f 0/3 CIVO onset，扩到 seed=4 进一步巩固 control 组统计。来源: plan_012 扩展。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_073_008f_walker_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"11670\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\", \"submitted_at\": \"2026-05-25T07:31:11.391Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8971.2, \"gpu_hours\": 2.49}, \"pid\": \"11670\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_073_008f_walker_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-25T09:48:03.882Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T09:48:13.191417+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_073_008f_walker_s4\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 289.3, \"eval_return_peak\": 486.5, \"eval_return_peak_step\": 75000, \"ve_ratio_final\": 0.5, \"ve_ratio_peak\": 0.5, \"nve_peak\": 0.76, \"civo_alert\": 0, \"civo\": false, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"gate_empirical_entropy\": 0, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 33.2}, {\"step\": 15000, \"eval_return\": 128.3}, {\"step\": 25000, \"eval_return\": 165.3}, {\"step\": 35000, \"eval_return\": 284.5}, {\"step\": 45000, \"eval_return\": 272.5}, {\"step\": 55000, \"eval_return\": 406.7}, {\"step\": 65000, \"eval_return\": 379.5}, {\"step\": 75000, \"eval_return\": 486.5}, {\"step\": 85000, \"eval_return\": 352.6}, {\"step\": 95000, \"eval_return\": 297.7}, {\"step\": 105000, \"eval_return\": 289.3}]}, \"completed_at\": \"2026-05-25T10:00:42.604Z\"}, \"exp_072_008e_v3_walker_s5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:24:08.174Z\", \"updated_at\": \"2026-05-25T10:00:39.306Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=5。当前 5 seeds 测试 collapse rate=2/5 (40%)，加 seed=5 缩窄置信区间。来源: plan_016 扩展。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_072_008e_v3_walker_s5 --steps 105000 --seed 5 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"11116\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_072_008e_v3_walker_s5.log\", \"submitted_at\": \"2026-05-25T07:24:40.695Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9358.6, \"gpu_hours\": 2.6}, \"pid\": \"11116\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_072_008e_v3_walker_s5.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_072_008e_v3_walker_s5 --steps 105000 --seed 5 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-25T09:47:34.147Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T09:47:39.804739+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_072_008e_v3_walker_s5\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 853.1, \"eval_return_peak\": 853.1, \"eval_return_peak_step\": 105000, \"ve_ratio_final\": 0.6, \"nve_final\": 0.61, \"nve_peak\": 0.61, \"nve_peak_step\": 105000, \"civo_alert\": 0, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -5.1, \"value_mean_final\": 520.8, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 29.4}, {\"step\": 15000, \"eval_return\": 251.1}, {\"step\": 25000, \"eval_return\": 423}, {\"step\": 35000, \"eval_return\": 511}, {\"step\": 45000, \"eval_return\": 600.1}, {\"step\": 55000, \"eval_return\": 649}, {\"step\": 65000, \"eval_return\": 697.2}, {\"step\": 75000, \"eval_return\": 727.3}, {\"step\": 85000, \"eval_return\": 710.3}, {\"step\": 95000, \"eval_return\": 803.9}, {\"step\": 105000, \"eval_return\": 853.1}]}, \"completed_at\": \"2026-05-25T10:00:39.306Z\"}, \"exp_070_008e_v3_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:07:49.050Z\", \"updated_at\": \"2026-05-25T08:54:47.019Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=0。当前 4 unique seeds 测试结果 collapse rate=2/4 (50%)，加 seed=0 缩窄置信区间。来源: plan_016 扩展。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_070_008e_v3_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"260999\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_070_008e_v3_walker_s0.log\", \"submitted_at\": \"2026-05-25T05:29:11.281Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12335.7, \"gpu_hours\": 3.43}, \"pid\": \"260999\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_070_008e_v3_walker_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_070_008e_v3_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T08:50:11.463Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T08:50:17.078252+00:00\"}]}, \"metrics\": {\"eval_return\": 148, \"peak_eval_return\": 232.5, \"peak_eval_step\": 55000, \"ve_ratio_105k\": 0.8, \"nve_peak\": 0.8, \"nve_peak_step\": 95000, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -3.7, \"value_mean_final\": 122.1, \"failure_mode\": \"non-CIVO learning failure (never reached baseline performance)\", \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 37.4}, {\"step\": 15000, \"eval_return\": 93.2}, {\"step\": 25000, \"eval_return\": 178.8}, {\"step\": 35000, \"eval_return\": 221.6}, {\"step\": 45000, \"eval_return\": 230.9}, {\"step\": 55000, \"eval_return\": 232.5}, {\"step\": 65000, \"eval_return\": 194}, {\"step\": 75000, \"eval_return\": 175.2}, {\"step\": 85000, \"eval_return\": 218.6}, {\"step\": 95000, \"eval_return\": 139.6}, {\"step\": 105000, \"eval_return\": 148}], \"ve_ratio_trajectory\": [{\"step\": 15000, \"ve\": 0}, {\"step\": 25000, \"ve\": 0.1}, {\"step\": 35000, \"ve\": 0.2}, {\"step\": 45000, \"ve\": 0.3}, {\"step\": 55000, \"ve\": 0.4}, {\"step\": 65000, \"ve\": 0.5}, {\"step\": 75000, \"ve\": 0.6}, {\"step\": 85000, \"ve\": 0.5}, {\"step\": 95000, \"ve\": 0.8}, {\"step\": 105000, \"ve\": 0.8}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_070_008e_v3_walker_s0/latest.pt\", \"conclusion\": \"negative\", \"notes\": \"Seed 0 FAILED but NOT via CIVO. eval_return peaked at 232.5@55K (far below baseline ~500+), declined to 148@105K. ve_ratio stayed healthy throughout (max 0.8, never triggered CIVO alert). Gate locked dt=1. This is a distinct failure mode from seeds 2,3 (which had CIVO collapse with NVE>3.7x). Agent never reached high performance — learning stagnated early. Cross-seed 008e_v3 summary: 5 seeds tested, 2 success (s1=870, s4=899), 2 CIVO collapse (s2=137 NVE=3.78, s3=93 NVE=4.02), 1 non-CIVO failure (s0=148 NVE=0.8). CIVO collapse rate: 2/5=40%. Overall failure rate: 3/5=60%.\", \"completed_at\": \"2026-05-25T08:54:47.019Z\"}, \"exp_069_008f_walker_repro_s1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-25T03:49:41.282Z\", \"updated_at\": \"2026-05-25T07:28:33.676Z\", \"hypothesis\": \"Reproducing 008f config (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will NOT trigger CIVO (NVE < 1.5x) because removing dt_emb eliminates the temporal abstraction mismatch that drives value error amplification\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"failure_reason\": \"bjb1-40020 服务器不可达（SSH 连接 port 40020 on 106.120.183.117 失败），进程无法监控，未产生有效 W&B metrics\", \"completed_at\": \"2026-05-25T04:17:38.829Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T04:17:43.081459+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T07:17:09.809673+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_069_008f_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"4590\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\", \"submitted_at\": \"2026-05-25T05:04:10.980Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8662.7, \"gpu_hours\": 2.41}, \"pid\": \"4590\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_069_008f_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-25T07:17:02.903Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_069_008f_walker_repro_s1/latest.pt\", \"metrics\": {\"eval_return_final\": 237.8, \"eval_return_peak\": 390.1, \"eval_return_peak_step\": 95000, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.4, \"ve_ratio_peak_step\": 105000, \"nve_final_105k\": 0.61, \"nve_peak\": 0.66, \"nve_peak_step\": 75000, \"civo_alert\": false, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 30.5, \"15k\": 158.7, \"25k\": 180.8, \"35k\": 250.3, \"45k\": 293.6, \"55k\": 272.2, \"65k\": 328.1, \"75k\": 244.8, \"85k\": 382.5, \"95k\": 390.1, \"105k\": 237.8}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.1, \"35k\": 0.2, \"45k\": 0.2, \"55k\": 0.3, \"65k\": 0.3, \"75k\": 0.4, \"85k\": 0.3, \"95k\": 0.3, \"105k\": 0.4}}, \"conclusion\": \"success\"}, \"exp_068_008d_walker_repro_s1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-25T03:49:39.539Z\", \"updated_at\": \"2026-05-25T07:28:31.319Z\", \"hypothesis\": \"Reproducing 008d config (trained dt_emb + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will trigger CIVO (NVE > 1.5x) because trained dt_emb enables value error amplification through temporal abstraction mismatch\", \"parent\": \"exp_008d_subsample_on_h8\", \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 40020 on 106.120.183.117\", \"completed_at\": \"2026-05-25T04:18:15.954Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T04:18:20.002698+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T07:23:04.341146+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_068_008d_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"4425\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_068_008d_walker_repro_s1.log\", \"submitted_at\": \"2026-05-25T05:04:05.168Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8666.2, \"gpu_hours\": 2.41}, \"pid\": \"4425\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_068_008d_walker_repro_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_068_008d_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-25T07:22:57.100Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_068_008d_walker_repro_s1/latest.pt\", \"metrics\": {\"eval_return_final\": 39.1, \"eval_return_peak\": 192.4, \"eval_return_peak_step\": 55000, \"ve_ratio_final\": 2.7, \"ve_ratio_peak\": 4.6, \"ve_ratio_peak_step\": 85000, \"nve_final_105k\": 4.12, \"nve_peak_85k\": 6.57, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.81, \"civo_alert\": true, \"civo_alert_step\": 85000, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 31, \"15k\": 146.5, \"25k\": 174.1, \"35k\": 189.6, \"45k\": 142.2, \"55k\": 192.4, \"65k\": 114.4, \"75k\": 106.6, \"85k\": 33.4, \"95k\": 26.9, \"105k\": 39.1}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.2, \"35k\": 0.3, \"45k\": 0.6, \"55k\": 0.6, \"65k\": 1.3, \"75k\": 1.6, \"85k\": 4.6, \"95k\": 4.6, \"105k\": 2.7}}, \"conclusion\": \"success\"}, \"exp_067_frozen_dt_emb_walker_plan015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T03:49:37.736Z\", \"updated_at\": \"2026-05-25T06:59:24.006Z\", \"hypothesis\": \"Frozen (requires_grad=False) dt_embedding + subsample ON + dt=2 + H=8 在 Walker Walk 上不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIVO 的必要条件（而非 dt_emb 的存在本身）。来源: plan_015。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-25T03:51:43.628Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_067_frozen_dt_emb_walker_plan015 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T06:54:52.150Z\", \"training_hours\": 3.05}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_067_frozen_dt_emb_walker_plan015 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"255883\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_067_frozen_dt_emb_walker_plan015.log\", \"submitted_at\": \"2026-05-25T03:52:29.860Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11214.1, \"gpu_hours\": 3.12}, \"pid\": \"255883\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_067_frozen_dt_emb_walker_plan015.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T06:54:57.723176+00:00\"}]}, \"metrics\": {\"eval_final\": 281.5, \"eval_peak\": 334.1, \"eval_peak_step\": 95000, \"nve_peak\": 0.4, \"nve_final\": 0.2, \"civo_alert\": 0, \"total_env_steps\": 112000, \"update_count\": 25099, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_067_frozen_dt_emb_walker_plan015/latest.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T06:59:24.006Z\"}, \"exp_066b_timeseries_rssm_fidelity_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:34:14.574Z\", \"updated_at\": \"2026-05-25T04:35:12.673Z\", \"hypothesis\": \"RSSM fidelity gap (dt=2 prediction error > dt=1) emerges before value overestimation in seed=1, replicating the causal chain found in exp_066 seed=0 and confirming cross-seed robustness of the fidelity→VE mechanism.\", \"parent\": \"exp_066_timeseries_rssm_fidelity\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066b_timeseries_rssm_fidelity_s1 --steps 60000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 5000\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"252133\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_066b_timeseries_rssm_fidelity_s1.log\", \"submitted_at\": \"2026-05-25T02:38:44.421Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6988.3, \"gpu_hours\": 1.94}, \"pid\": \"252133\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_066b_timeseries_rssm_fidelity_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066b_timeseries_rssm_fidelity_s1 --steps 60000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 5000\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T04:18:02.308Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T04:18:10.617905+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066b_timeseries_rssm_fidelity_s1/checkpoint_65000.pt\", \"metrics\": {\"seed\": 1, \"steps_completed\": 65000, \"eval_return_peak\": 201.9, \"eval_return_peak_step\": 45000, \"eval_return_final\": 160.7, \"civo_alert_step\": 55000, \"ve_ratio_final\": 0.724, \"fidelity_gap_timeseries\": {\"ss_ratio_10K\": 0.887, \"ss_ratio_15K\": 1.017, \"ss_ratio_20K\": 1.216, \"ss_ratio_25K\": 1.532, \"ss_ratio_30K\": 1.374, \"ss_ratio_35K\": 1.486, \"ss_ratio_40K\": 1.428, \"ss_ratio_45K\": 1.38, \"ss_ratio_50K\": 1.468, \"ss_ratio_55K\": 1.517, \"ss_ratio_60K\": 1.799, \"ss_ratio_65K\": 1.756}, \"ve_ratio_timeseries\": {\"12K\": 0.012, \"15K\": 0.033, \"24K\": 0.118, \"25K\": 0.193, \"35K\": 0.269, \"45K\": 0.358, \"52K\": 0.495, \"55K\": 0.71, \"64K\": 0.724}, \"fidelity_gap_onset_step\": 15000, \"ve_onset_step\": 24000, \"temporal_lead_steps\": 9000, \"causal_direction\": \"fidelity_gap_leads_ve\", \"cross_seed_comparison\": {\"s0_ss_ratio_65K\": 1.678, \"s1_ss_ratio_65K\": 1.756, \"s0_fidelity_onset\": 20000, \"s1_fidelity_onset\": 15000, \"s0_ve_onset\": 30000, \"s1_ve_onset\": 24000, \"s0_temporal_lead\": 10000, \"s1_temporal_lead\": 9000, \"pattern_consistent\": true}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T04:35:12.673Z\"}, \"exp_062_cartpole_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:01:08.858Z\", \"updated_at\": \"2026-05-25T03:45:35.194Z\", \"hypothesis\": \"dt_embed_dim=0 + subsample ON + H=8 在 Cartpole Swingup 上不触发 CIVO（NVE < 1.5x），因果控制实验验证移除 dt_emb 是否阻止 CIVO 在第三个环境中泛化。与 exp_061 配对形成因果对比。\", \"spec\": {\"command\": \"bash -c 'for SEED in 0 1 2; do python -u dreamer.py --configs defaults dmc_proprio --task dmc_cartpole_swingup --logdir logdir/exp_062_cartpole_control_s${SEED} --steps 105000 --seed $SEED --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000; done'\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"pid\": \"473913\", \"log_path\": \"bjb1-40020:~/runs/event-gated-adaptive-horizon/exp_062_cartpole_control.log\", \"submitted_at\": \"2026-05-24T16:26:50.780Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cartpole_swingup\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (dt_embed_dim=0, control, Cartpole Swingup)\", \"seed\": \"0,1,2\", \"gpu_ids\": [0], \"checkpoint_path\": \"bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_062_cartpole_control_s0/checkpoint.pt\", \"wall_clock_seconds\": 40686.6, \"gpu_hours\": 11.3}, \"metrics\": {\"seeds\": {\"s0\": {\"eval_return\": 230.4, \"ve_ratio_peak\": 0.069, \"ve_ratio_final\": 0.056, \"value_mean\": 12.9, \"civo_detected\": false}, \"s1\": {\"eval_return\": 255.3, \"ve_ratio_peak\": 0.079, \"ve_ratio_final\": 0.04, \"value_mean\": 10.2, \"civo_detected\": false}, \"s2\": {\"eval_return\": 248.8, \"ve_ratio_peak\": 0.065, \"ve_ratio_final\": 0.048, \"value_mean\": 11.8, \"civo_detected\": false}}, \"mean_eval_return\": 244.8, \"mean_ve_ratio_peak\": 0.071, \"civo_detected_any\": false, \"steps_completed\": 112000}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-25T03:44:57.338Z\"}, \"exp_061_cartpole_civo_trigger\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-24T16:01:07.009Z\", \"updated_at\": \"2026-05-25T03:18:38.759Z\", \"hypothesis\": \"Trained dt_emb (d=32) + subsample ON + H=8 + dt=2 imagination 在 Cartpole Swingup 上触发 CIVO（NVE > 1.5x），验证 CIVO 是否跨 locomotion 子类环境泛化（Walker/Cheetah 已确认，Cartpole 是第三个 DMC locomotion 环境）。与 exp_062 配对形成因果对比。\", \"spec\": {\"command\": \"bash -c '... --device cuda:0 ...'\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"226158\", \"log_path\": \"bjb1-45299:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_061_cartpole_civo_trigger_s{0,1,2}/\", \"submitted_at\": \"2026-05-24T16:50:56.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cartpole_swingup\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO trigger, Cartpole Swingup)\", \"seed\": \"0,1,2\", \"gpu_ids\": [1], \"checkpoint_path\": \"bjb1-45299:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_061_cartpole_civo_trigger_s{0,1,2}/latest.pt\", \"wall_clock_seconds\": 39600, \"gpu_hours\": 11}, \"conclusion\": \"negative\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"s0_eval_return_final\": 211.1, \"s0_eval_return_peak\": 247.8, \"s0_value_mean_final\": 9.229, \"s0_ve_ratio_peak\": 0.058, \"s0_train_return_final\": 199.2, \"s1_eval_return_final\": 269, \"s1_eval_return_peak\": 328.1, \"s1_value_mean_final\": 9.323, \"s1_ve_ratio_peak\": 0.04, \"s1_train_return_final\": 188.7, \"s2_eval_return_final\": 228.9, \"s2_eval_return_peak\": 245.9, \"s2_value_mean_final\": 9.46, \"s2_ve_ratio_peak\": 0.043, \"s2_train_return_final\": 258.9, \"civo_detected\": false, \"civo_alert_any_seed\": false, \"ve_ratio_max_all_seeds\": 0.058, \"vs_baseline_eval_mean\": \"-56.3%\", \"baseline_exp060_eval_s2_105K\": 557}, \"completed_at\": \"2026-05-25T03:18:38.759Z\"}, \"exp_008d_subsample_on_h8\": {\"completed_at\": \"2026-05-14T04:50:52.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:46:57.960Z\", \"hypothesis\": \"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\", \"metrics\": {\"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"baseline_35K\": 400, \"baseline_45K\": 443, \"data_source_45K\": \"from training logs metrics.jsonl\", \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"step\": 55000, \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\"}, \"parent\": \"exp_005_event_gated_v4\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008d_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.48, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8)\", \"pid\": \"109519\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T02:21:59.852Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8932.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T02:41:05.620Z\", \"notes\": \"RSSM fidelity analysis (exp_063, 55K checkpoint only): dt=2/dt=1 single-step reward MAE ratio = 2.695x (vs exp_066 s0's 1.37x at same step). Larger fidelity gap correlates with worse VE (1.666 vs 0.621). No intermediate checkpoints exist — cannot directly verify 25K fidelity gap for this seed. Cross-seed pattern consistent: VE trajectory matches s0 (low at 25K, collapse by 55K). See artifact art_20260525_e45921.\"}, \"exp_066_timeseries_rssm_fidelity\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-24T21:07:53.125Z\", \"updated_at\": \"2026-05-25T02:33:00.783Z\", \"hypothesis\": \"Trained dt_embedding causes RSSM fidelity degradation (dt=2 vs dt=1 reward MAE gap) that progressively worsens during training, and its temporal evolution precedes or synchronizes with NVE (value overestimation) rise, establishing a temporal causal chain: RSSM fidelity gap → value overestimation.\", \"parent\": \"exp_063_rssm_fidelity\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-24T22:27:54.087Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/dreamerv3-torch && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066_timeseries_rssm_fidelity_s0 --steps 60000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 999999\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-24T22:28:15.966Z\", \"training_hours\": 0.01}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-24T22:28:19.155Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T22:28:24.279787+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066_timeseries_rssm_fidelity_s0 --steps 60000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 5000'\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"pid\": 490622, \"fix_note\": \"eval_every changed from 999999 to 5000 — checkpoint saving is coupled to eval loop, 999999 prevented checkpoints from being saved\", \"checkpoint_path\": \"bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066_timeseries_rssm_fidelity_s0/checkpoint.pt\", \"log_path\": \"bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066_timeseries_rssm_fidelity_s0/\"}, \"conclusion\": \"success\", \"metrics\": {\"ss_ratio_10K\": 1.047, \"ss_ratio_30K\": 1.247, \"ss_ratio_65K\": 1.678, \"ol_ratio_30K_peak\": 1.446, \"ol_ratio_35K_peak\": 1.509, \"ve_ratio_final\": 1.399, \"fidelity_gap_onset_step\": 20000, \"ve_onset_step\": 30000, \"temporal_lead_steps\": 10000, \"pearson_ss_ve\": 0.807, \"pearson_ss_ve_p\": 0.0015, \"pearson_ol_ve\": 0.425, \"pearson_ol_ve_p\": 0.169, \"ss_monotonicity\": 0.73, \"ol_monotonicity\": 0.73, \"ve_monotonicity\": 0.82, \"causal_direction\": \"fidelity_gap_leads_ve\", \"conclusion\": \"success\"}}, \"exp_060_cartpole_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:01:05.099Z\", \"updated_at\": \"2026-05-25T01:25:39.711Z\", \"hypothesis\": \"Cartpole Swingup (DMC) baseline dt=1 建立 v/e ratio 校准基线，用于 CIVO 诊断阈值在第三个 DMC 环境的验证。预期 NVE 保持在 1.0x 附近，无 CIVO 现象。\", \"spec\": {\"command\": \"bash -c 'for SEED in 0 1 2; do python -u dreamer.py --configs defaults dmc_proprio --task dmc_cartpole_swingup --logdir logdir/exp_060_cartpole_baseline_s${SEED} --steps 105000 --seed $SEED --compile False --device cuda:0 --checkpoint_every 25000; done'\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"223294\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_060_cartpole_baseline.log\", \"submitted_at\": \"2026-05-24T16:26:42.610Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cartpole_swingup\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (vanilla baseline, Cartpole Swingup)\", \"seed\": \"0,1,2\", \"gpu_ids\": [0], \"wall_clock_seconds\": 32337.1, \"gpu_hours\": 8.98}, \"conclusion\": \"success\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"train_return_s0\": 809.4, \"train_return_s1\": 684.4, \"train_return_s2\": 526.1, \"eval_return_s2_105K\": 557}, \"checkpoint_path\": \"bjb1-45299:/root/dreamerv3-torch/logdir/exp_060_cartpole_baseline_s{0,1,2}/latest.pt\", \"log_path\": \"bjb1-45299:/root/dreamerv3-torch/logdir/exp_060_cartpole_baseline_s{0,1,2}/metrics.jsonl\", \"completed_at\": \"2026-05-25T01:25:39.711Z\"}, \"exp_065_dt_emb_cosine\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:48:47.693Z\", \"updated_at\": \"2026-05-24T20:54:51.678Z\", \"hypothesis\": \"分析 trained dt_embedding 中 dt=1 vs dt=2 向量的 cosine similarity 及其训练过程演化。如果 cosine sim 高（接近 1）→ dt_emb 未学到有意义区分，CIVO 来自微小差异被 downstream 放大；如果 cosine sim 低 → dt_emb 学到了显著不同的表征，CIVO 来自 dt=2 表征本身的偏差。\", \"conclusion\": \"success\", \"checkpoint_path\": \"logdir/exp_065_dt_emb_cosine/results.json\", \"log_path\": \"bjb1-45299:/root/dreamerv3-torch/logdir/exp_065_dt_emb_cosine/\", \"completed_at\": \"2026-05-24T20:52:24.863Z\", \"metrics\": {\"trained_cosine_sim_range\": \"-0.94 to -0.70\", \"frozen_cosine_sim_range\": \"-0.15 to +0.07\", \"trained_trend\": \"strong negative (near-opposite directions)\", \"frozen_trend\": \"near-zero constant\", \"conclusion\": \"dt=1 and dt=2 embeddings learn nearly opposite representations; CIVO from dt=2 representation bias, not amplified micro-differences\"}}, \"exp_064_value_distribution\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T19:23:05.483Z\", \"updated_at\": \"2026-05-24T20:14:50.460Z\", \"hypothesis\": \"V(s) vs Monte Carlo return 分布对比：trained dt_emb (exp_008d collapsed) 的 value estimate 在 dt=2 imagination 步骤系统性高估，而 untrained/absent dt_emb (exp_008f control) 和 baseline (exp_001) 的 value 分布与 MC return 紧密跟踪。直观展示 CIVO 的 value divergence 位置和形态。\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-24T19:56:27.179Z\"}, \"spec\": {\"command\": \"python scripts/value_distribution_analysis.py --device cuda:0\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_001_baseline + logdir/exp_008d + logdir/exp_008f\", \"data_count\": 500, \"model_name\": \"DreamerV3 (baseline + collapsed + control checkpoints)\", \"seed\": 0, \"gpu_ids\": [1], \"checkpoint_path\": \"logdir/exp_064_value_distribution/\", \"log_path\": \"logdir/exp_064_value_distribution/results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"baseline_bias\": 344.85, \"baseline_rmse\": 371.73, \"baseline_overest_pct\": 100, \"baseline_v_mc_ratio\": 3.31, \"civo_bias\": 108.99, \"civo_rmse\": 112.36, \"civo_overest_pct\": 100, \"civo_v_mc_ratio\": 7.8, \"civo_v_mc_median\": 3.4, \"control_bias\": -6.51, \"control_rmse\": 57.93, \"control_overest_pct\": 52.5, \"control_v_mc_ratio\": 2.58, \"control_v_mc_median\": 1.05}, \"completed_at\": \"2026-05-24T20:14:50.460Z\"}, \"exp_063_rssm_fidelity\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:12:47.163Z\", \"updated_at\": \"2026-05-24T19:21:37.837Z\", \"hypothesis\": \"RSSM 在 dt=2 transitions 上的 observation/reward reconstruction loss 显著高于 dt=1，量化 fidelity gap 作为 trained dt_emb 导致 delusional critic 的机械性基础。从 exp_001 (baseline) 和 exp_008d (collapsed) 的已有 checkpoint 提取，对比 dt=1 vs dt=2 prediction quality。\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-24T18:53:48.781Z\"}, \"spec\": {\"command\": \"python scripts/rssm_fidelity_analysis.py --device cuda:0\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_001_baseline + logdir/exp_008d_subsample_on_h8\", \"data_count\": 500, \"model_name\": \"DreamerV3 RSSM (baseline + collapsed checkpoints)\", \"seed\": 0, \"gpu_ids\": [1], \"checkpoint_path\": \"logdir/exp_063_rssm_fidelity/results.json\", \"log_path\": \"logdir/exp_063_rssm_fidelity/results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"baseline_dt1_obs_mse\": 13.7, \"baseline_dt2_obs_mse\": 20.62, \"baseline_dt2_dt1_ratio_obs\": 1.505, \"baseline_dt2_dt1_ratio_reward\": 1.483, \"collapsed_dt1_obs_mse\": 26.93, \"collapsed_dt2_single_obs_mse\": 42.02, \"collapsed_dt2_single_reward_mae\": 0.146, \"collapsed_dt2_dt1_ratio_obs\": 1.56, \"collapsed_dt2_dt1_ratio_reward\": 2.695, \"collapsed_single_vs_chained_obs\": 1.138, \"collapsed_single_vs_chained_reward\": 1.926}, \"completed_at\": \"2026-05-24T19:21:37.837Z\"}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:30:00.000Z\", \"updated_at\": \"2026-05-24T16:53:23.046Z\", \"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks. If frozen prevents CIVO → extends Walker/Cheetah frozen finding to manipulation; if not → domain-specific factors override dt_emb mechanism.\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\", \"checkpoint_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\"}, \"metrics\": {\"eval_final\": 45.3, \"eval_final_step\": 212500, \"eval_peak\": 45.3, \"eval_peak_step\": 212500, \"ve_ratio_final\": 0.1, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.3, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-62K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 82500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 7.1, \"eval_dip_step\": 42500}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T08:48:40.404Z\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:14:38.578Z\", \"updated_at\": \"2026-05-24T16:53:19.032Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"parent\": \"exp_048_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_049_stackcube_civo_trigger_s0/train.log\"}, \"metrics\": {\"eval_final\": 34.88, \"eval_final_step\": 212500, \"eval_peak\": 35.89, \"eval_peak_step\": 182500, \"ve_ratio_final\": 0.186, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 5.048, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"total_episodes\": 1112, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-72K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 112500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 4.93, \"eval_dip_step\": 62500}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/checkpoint_202500.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/metrics.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:23:01.339Z\"}, \"exp_057\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:49:35.310Z\", \"updated_at\": \"2026-05-24T16:50:44.968Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。\", \"parent\": \"\", \"spec\": {\"command\": \"python train.py --env walker --frozen_dt_emb --seed 2\", \"server\": \"bjb1-45299\", \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"data_count\": 225000, \"seed\": 2, \"model_name\": \"dreamer_frozen_dt_emb\"}, \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\", \"metrics\": {\"eval_return_peak\": 221.7, \"eval_return_peak_step\": 195000, \"eval_return_final\": 123.9, \"eval_return_final_step\": 215000, \"nve_peak\": 1.3, \"nve_peak_step\": 115000, \"nve_final\": 0.2, \"civo_alert\": 0, \"civo_sustained\": false, \"civo_transient\": true, \"civo_transient_range\": \"115k-145k\", \"train_steps\": 225000, \"gate_dt_mean\": 2}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T16:50:44.968Z\"}, \"exp_008d_civo_trigger_s4\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/latest.pt\", \"completed_at\": \"2026-05-18T05:17:45.132Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:43.972Z\", \"hypothesis\": \"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/metrics.jsonl\", \"metrics\": {\"ve_ratio_peak\": 3.0294, \"ve_ratio_peak_step\": 105000, \"ve_ratio_final\": 3.0294, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.62, \"nve_peak_step\": 105000, \"nve_peak_note\": \"step-matched s1 baseline @105K = 0.6564\", \"nve_classification\": \"onset_collapse\"}, \"parent\": \"exp_008d_civo_trigger_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 4 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s4\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk_online\", \"gpu\": \"cuda:0\", \"model_name\": \"DreamerV3-walker-civo-trigger\", \"pid\": \"715124\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:41.239Z\"}, \"exp_059_walker_trained_s5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T07:46:59.075Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 5 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir logdir/exp_059_walker_trained_s5\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"186176\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_059_walker_trained_s5.log\", \"submitted_at\": \"2026-05-24T03:15:40.649Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11526.3, \"gpu_hours\": 3.2}, \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"pid\": \"186176\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_059_walker_trained_s5.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 5 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir logdir/exp_059_walker_trained_s5\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-24T06:20:56.680Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T06:21:01.777871+00:00\"}]}, \"metrics\": {\"ve_ratio_peak\": 3.3075, \"ve_ratio_peak_step\": \"85K\", \"nve_peak\": 4.72, \"nve_peak_note\": \"step-matched s1 baseline @85K = 0.7007\", \"nve_classification\": \"onset_collapse\", \"nve_classification_note\": \"Reclassified from onset_self_correcting: NVE self-corrected but eval=95.8 (10.5% of baseline 913) indicates irreversible policy damage. Collapse†.\", \"nve_final\": 1.22, \"nve_final_note\": \"0.8/0.656 (step-matched s1 baseline @105K)\", \"eval_final\": 95.8, \"eval_baseline\": 913, \"eval_pct_baseline\": \"10.5%\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_059_walker_trained_s5/checkpoint.pt\", \"completed_at\": \"2026-05-24T06:27:46.992Z\", \"notes\": \"CIVO-positive under step-matched NVE (peak ≈ 5.0×). Self-correcting outcome (ve_ratio 3.3@85K → 0.8@105K in ~10K steps). Supports 5/5 Walker trained CIVO onset. Gate locked at dt=2 throughout (entropy=0).\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:25:00.000Z\", \"updated_at\": \"2026-05-24T02:17:41.318Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\"}, \"completed_at\": \"2026-05-23T23:30:00.000Z\", \"metrics\": {\"total_steps\": 225000, \"ve_ratio_peak\": 1.283, \"ve_ratio_peak_step\": 115000, \"ve_ratio_final\": 0.177, \"ve_ratio_final_step\": 215000, \"nve_peak\": 1.88, \"nve_peak_step\": 115000, \"nve_classification\": \"transient\", \"eval_return_final\": 123.94, \"eval_return_final_step\": 215000, \"eval_return_peak\": 221.72, \"eval_return_peak_step\": 195000}}, \"exp_058_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:10:49.773Z\", \"updated_at\": \"2026-05-24T00:30:00.000Z\", \"hypothesis\": \"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\", \"parent\": \"exp_046_frozen_dt_emb_cheetah\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 164830, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:30:00.000Z\", \"metrics\": {\"total_steps\": 224000, \"ve_ratio_peak\": 0.231, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.107, \"ve_ratio_final_step\": 215000, \"eval_return_final\": 80.46, \"eval_return_final_step\": 215000, \"eval_return_peak\": 191.74, \"eval_return_peak_step\": 25000, \"nve_peak\": 0.78, \"nve_peak_step\": 45000, \"nve_classification\": \"no_civo\", \"note\": \"Cheetah frozen s1. NVE=0.78× (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\"}}, \"exp_056_peginsertion_frozen_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:02:23.683Z\", \"updated_at\": \"2026-05-24T00:00:00.000Z\", \"hypothesis\": \"D143 混合机制假说验证——PegInsertion frozen dt_emb 跨 seed 可复现性。exp_053 (s0) 显示 frozen 在 82.5K 回落到 1.82 而 trained 攀升到 10.05，s1 验证这个分叉是否可复现。如果 s1 也回落 → frozen 稳健阻止 dt_emb 放大；如果不回落 → seed-dependent。\", \"parent\": \"exp_053_peginsertion_frozen_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 346430, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_056_peginsertion_frozen_s1/train.log\", \"checkpoint_path\": \"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:00:00.000Z\", \"metrics\": {\"total_steps\": 222500, \"ve_ratio_peak\": 11.321, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 1.193, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 4.37, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.42, \"eval_return_peak_step\": 132500, \"nve_classification\": \"burst\", \"note\": \"Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 — frozen does NOT suppress ManiSkill transients.\", \"ve_ratio_trajectory\": {\"12500\": 0.316, \"22500\": 0.975, \"32500\": 1.839, \"42500\": 1.966, \"52500\": 5.422, \"62500\": 4.047, \"72500\": 8.408, \"82500\": 11.321, \"92500\": 3.724, \"102500\": 3.034, \"112500\": 2.204, \"122500\": 2.425, \"132500\": 0.842, \"142500\": 2.194, \"152500\": 2.203, \"162500\": 0.651, \"172500\": 1.085, \"182500\": 1.07, \"192500\": 0.467, \"202500\": 0.708, \"212500\": 1.193}}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:50:00.000Z\", \"updated_at\": \"2026-05-23T23:38:30.000Z\", \"hypothesis\": \"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，最终自修复到 0.379@212.5K）。如果 s1 也触发持续 CIVO → PegInsertion CIVO 可复现；如果不触发 → seed-specific 异常。\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 345223, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\"}, \"ve_ratio_peak\": \"3.08@92500\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T23:38:25.428Z\", \"metrics\": {\"total_steps\": 222400, \"ve_ratio_peak\": 3.08, \"ve_ratio_peak_step\": 92500, \"ve_ratio_final\": 0.498, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 11.44, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.05, \"eval_return_peak_step\": 112500, \"nve_classification\": \"transient\", \"civo_triggered\": true, \"civo_self_corrected\": \"partial\", \"note\": \"CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 — severity seed-dependent.\", \"ve_ratio_trajectory\": {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2.0, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}}, \"checkpoint_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/checkpoint_222500.pt\"}, \"exp_054_pickcube_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:47:24.310Z\", \"updated_at\": \"2026-05-23T18:08:00.000Z\", \"hypothesis\": \"PickCube frozen dt_emb baseline (fixed_dt=2, subsample ON, H=8)。验证 CIVO frozen 配置在最简单 manipulation task 上的表现。如果 eval return 稳定高于 random → frozen dt_emb 在 easy task 上不影响学习；如果性能差 → frozen dt_emb 有问题。\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 133956, \"data_path\": \"ManiSkill PickCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PickCube-v1 (online eval)\", \"log_path\": \"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.81@62500\", \"eval_final\": 10.26, \"eval_final_step\": 212500, \"ve_ratio_final\": 0.583, \"ve_ratio_final_step\": 212500}, \"exp_053_peginsertion_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:23:10.381Z\", \"updated_at\": \"2026-05-23T15:00:00.000Z\", \"hypothesis\": \"Freezing dt_emb in PegInsertionSide-v1 (contact-rich manipulation) prevents CIVO while maintaining task performance, establishing that dt_emb freezing generalizes as CIVO prevention across task domains. If frozen prevents CIVO here → extends StackCube/locomotion frozen finding to insertion tasks; if CIVO still appears → freezing insufficient for contact-rich tasks.\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 123495, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\", \"checkpoint_path\": \"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.10@52500\", \"eval_final\": 5.89, \"ve_ratio_final\": 0.202, \"ve_ratio_final_step\": 212500}, \"exp_050_peginsertion_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:38:33.441Z\", \"updated_at\": \"2026-05-23T08:51:11.592Z\", \"hypothesis\": \"Fixed-dt=2 gate with CIVO trigger on PegInsertionSide-v1 (contact-rich manipulation) will demonstrate that temporal abstraction benefits extend beyond locomotion to precise insertion tasks, where event-gated horizons can skip redundant approach phases while preserving fine-grained control near contact.\", \"spec\": {\"command\": \"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\", \"server\": \"bjb1-40020\", \"data_path\": \"ManiSkill PegInsertionSide-v1 (state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\", \"seed\": 0, \"pid\": 304736, \"gpu_ids\": [0], \"log_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\", \"checkpoint_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0\"}, \"metrics\": {\"ve_ratio_peak\": 10.05, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 0.379, \"ve_ratio_final_step\": 212500, \"civo_self_corrected\": true, \"civo_correction_delay_steps\": 130000, \"eval_final\": 20.86, \"eval_final_step\": 212500, \"eval_peak\": 20.86, \"eval_peak_step\": 212500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:30:00.000Z\"}, \"exp_052_stackcube_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:26:49.825Z\", \"updated_at\": \"2026-05-23T07:45:47.966Z\", \"hypothesis\": \"StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 CIVO（ve_ratio 3.27）。如果 s1 也触发 → CIVO 在 manipulation 领域可复现，非 seed-specific；如果不触发 → seed-dependent，需更多 seeds。\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 103781, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/train.log\"}, \"metrics\": {\"eval_final\": 29.458, \"eval_final_step\": 212500, \"eval_peak\": 39.873, \"eval_peak_step\": 162500, \"ve_ratio_final\": 0.133, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.67, \"ve_ratio_peak_step\": 52500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"checkpoint_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/checkpoint_202500.pt\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/metrics.jsonl\", \"completed_at\": \"2026-05-23T07:45:47.966Z\"}, \"exp_048_cheetah_civo_extension\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:40.050Z\", \"updated_at\": \"2026-05-22T21:18:00.000Z\", \"hypothesis\": \"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → severity determines recoverability narrative. If it does → CIVO is universally transient regardless of severity.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}, \"metrics\": {\"eval_final\": 23.4, \"eval_final_step\": 302000, \"eval_peak\": 32.8, \"eval_peak_step\": 252000, \"ve_ratio_initial\": 46.3, \"ve_ratio_peak\": 24.112, \"ve_ratio_peak_step\": 162000, \"ve_ratio_final\": 1.803, \"nve_initial\": 70.64, \"nve_peak_secondary\": 36.76, \"nve_final\": 2.75, \"total_steps\": 312000, \"civo_self_corrected\": false, \"civo_correction_pct\": 96, \"secondary_burst_step\": 152000, \"secondary_burst_nve\": 36.47, \"gate_collapsed\": true}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/checkpoint_300000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:18:00.000Z\"}, \"exp_047_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:03:31.428Z\", \"updated_at\": \"2026-05-22T19:01:30.894Z\", \"hypothesis\": \"Frozen dt_emb Walker seed 1: 增强 exp_042 (s0, NVE=0.19) 的统计力度。 如果 s1 也 NVE<1.5 且无持续 CIVO → frozen dt_emb mitigation 跨 seed robust。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"dreamer_gated_frozen_dt_emb\", \"seed\": 1, \"eval_data\": \"dmc_walker_walk (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T18:56:07.648Z\"}, \"metrics\": {\"eval_final\": 144.22, \"eval_final_step\": 215000, \"eval_peak\": 408.79, \"eval_peak_step\": 125000, \"ve_ratio_peak\": 1.099, \"ve_ratio_peak_step\": 75000, \"ve_ratio_final\": 0.277, \"nve_peak\": 1.71, \"nve_peak_step\": 95000, \"nve_final_105k\": 0.56, \"total_steps\": 225000}, \"checkpoint_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T19:01:30.894Z\"}, \"exp_046_frozen_dt_emb_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:41:53.934Z\", \"updated_at\": \"2026-05-22T18:32:34.105Z\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"hypothesis\": \"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-22T10:42:06.985Z\", \"finished_at\": \"2026-05-22T18:27:00.000Z\"}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"seed\": 0, \"model_name\": \"dreamerv3-cheetah-frozen-dt-emb\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"metrics\": {\"eval_final\": 150.5, \"eval_peak\": 207.4, \"eval_peak_step\": 145000, \"ve_ratio_peak\": 0.4, \"ve_ratio_final\": 0.1, \"nve_peak\": 1.35, \"nve_peak_step\": 45000, \"nve_final\": 0.17, \"total_steps\": 224000, \"civo_alert_count\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:31:00.933Z\"}, \"exp_044_gradient_stop_walker\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:03:45.656Z\", \"updated_at\": \"2026-05-22T16:08:22.684Z\", \"hypothesis\": \"Reviewer Q2 直接回应：gradient stopping（detach dt_emb gradient to reward head）是否能阻断 CIVO 的 reward-critic feedback loop。基于 008d 配置（trained dt_emb + subsample ON + H=8），仅阻断 dt_emb→reward_head 梯度路径。如果 gradient stopping 有效（NVE<1.5）→ 最简干预方案成立，推翻我们之前 SGS 1/17 的结论（SGS 阻断所有梯度 vs 这里只阻断 dt_emb→reward 路径）。如果无效 → 直接证据证明 gradient-level intervention 不足以解决 CIVO，支撑 Intervention Hierarchy 中 gradient-level 最弱的结论。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"68371\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"submitted_at\": \"2026-05-22T09:08:10.295Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"DMC Walker Walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + reward_dt_emb_detach\", \"seed\": 0, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 25212.4, \"gpu_hours\": 7.0}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:04:32.082Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:04:36.793540+00:00\"}]}, \"metrics\": {\"eval_final\": 538.6, \"eval_peak\": 561.2, \"eval_peak_step\": 185000, \"eval_civo_trough\": 44.3, \"eval_civo_trough_step\": 95000, \"ve_ratio_peak\": 4.4, \"ve_ratio_peak_step\": 95000, \"ve_ratio_final\": 0.1, \"civo_onset_step\": 85000, \"civo_resolved_step\": 125000, \"civo_duration_steps\": 40000, \"total_steps\": 224000, \"pre_civo_peak\": 545.6, \"pre_civo_peak_step\": 75000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_044_gradient_stop_walker/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:08:22.684Z\"}, \"exp_045_treatment_extension_008d_s3\": {\"created_at\": \"2026-05-22T09:40:52.894Z\", \"updated_at\": \"2026-05-22T15:41:43.036Z\", \"status\": \"DONE\", \"retry_count\": 0, \"hypothesis\": \"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": \"70945\", \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_final\": 867.6, \"eval_peak\": 869.7, \"eval_peak_step\": 242000, \"nve_peak\": 4.91, \"nve_peak_step\": 132000, \"nve_final\": 0.052, \"ve_ratio_final\": 0.052, \"total_steps\": 312000, \"civo_alerts\": 0, \"civo_self_corrected\": true, \"civo_correction_step\": 142000, \"eval_trajectory\": {\"112000\": 58.5, \"122000\": 41.8, \"132000\": 35.1, \"142000\": 350.2, \"152000\": 646.4, \"162000\": 482.3, \"172000\": 600.4, \"182000\": 600.5, \"192000\": 699.5, \"202000\": 684.3, \"212000\": 758.6, \"222000\": 744.6, \"232000\": 745.4, \"242000\": 869.7, \"252000\": 721.6, \"262000\": 820.6, \"272000\": 716.2, \"282000\": 755.6, \"292000\": 843, \"302000\": 867.6}, \"ve_ratio_trajectory\": {\"122000\": 4.77, \"132000\": 4.91, \"142000\": 0.43, \"152000\": 0.21, \"162000\": 0.25, \"172000\": 0.18, \"182000\": 0.16, \"192000\": 0.13, \"202000\": 0.12, \"212000\": 0.1, \"222000\": 0.1, \"232000\": 0.09, \"242000\": 0.07, \"252000\": 0.08, \"262000\": 0.07, \"272000\": 0.08, \"282000\": 0.07, \"292000\": 0.06, \"302000\": 0.05}}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/train.log\", \"completed_at\": \"2026-05-22T15:41:43.036Z\"}, \"exp_043_008f_walker_s1\": {\"created_at\": \"2026-05-22T02:35:37.558Z\", \"hypothesis\": \"Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\"trained dt_emb → CIVO\\\"。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"model_name\": \"DreamerV3 (no dt_emb, 008f control)\", \"pid\": \"250627\", \"seed\": 1, \"server\": \"bjb1-40020\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:38:36.474Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"metrics\": {\"eval_final\": 673.73, \"eval_peak\": 673.73, \"eval_peak_step\": 215000, \"nve_peak\": 0.808, \"nve_peak_step\": 105000, \"nve_final\": 0.123, \"civo_alert\": false, \"total_steps\": 224000, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"note\": \"No CIVO (peak NVE 0.808, well below 1.5). Gate fixed at dt=2. Seed 1 replicates seed 0 finding: dt_emb absence prevents CIVO.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:38:36.474Z\"}, \"exp_042_frozen_dt_emb_walker\": {\"created_at\": \"2026-05-22T02:13:59.183Z\", \"hypothesis\": \"dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb.\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"model_name\": \"DreamerV3 + frozen dt_emb\", \"pid\": \"251336\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:29:26.337Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"metrics\": {\"eval_final\": 612.45, \"eval_peak\": 682.38, \"eval_peak_step\": 205000, \"nve_peak\": 0.194, \"nve_final\": 0.051, \"civo_alert\": false, \"total_steps\": 224000, \"total_train_episodes\": 224}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:29:26.337Z\"}, \"exp_040_wide_dual_critic_cheetah\": {\"created_at\": \"2026-05-21T19:50:49.909Z\", \"hypothesis\": \"Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\", \"pid\": \"52397\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T19:51:11.519Z\", \"submitted_via\": \"submit_training_job\", \"seed\": 1, \"wall_clock_seconds\": 49438.9, \"gpu_hours\": 13.73}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:37:44.547Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:35:07.693Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:35:10.404Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:35:14.583680+00:00\"}]}}, \"exp_041_dual_critic_walker_s3\": {\"created_at\": \"2026-05-21T19:50:54.290Z\", \"hypothesis\": \"D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\", \"pid\": \"51103\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-22T02:38:20.728Z\", \"submitted_via\": \"submit_training_job\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/checkpoint.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 23112.0, \"gpu_hours\": 6.42}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:04:44.715Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:00:53.721Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:00:58.393731+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_peak\": 761.1, \"eval_return_final\": 544, \"eval_return_peak_step\": 165000, \"nve_peak\": 1.5, \"nve_final\": 0.1, \"civo_prevented\": true, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": false, \"steps\": 215000, \"note\": \"CIVO prevented (NVE≤1.5), no non-CIVO collapse. Eval stays 486-761 after peak. Non-CIVO collapse rate confirmed 1/4 (only s2).\"}, \"completed_at\": \"2026-05-22T09:03:32.751Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\"}, \"exp_039_narrow_dual_critic_walker_s1\": {\"completed_at\": \"2026-05-22T02:35:33.617Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T16:31:40.055Z\", \"hypothesis\": \"Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\", \"metrics\": {\"civo_recovery\": true, \"eval_return_final\": 592.7, \"note\": \"Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean≈645. Recovery 2/2.\", \"nve_peak\": 2.19, \"recovery_confirmed\": true}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\"\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 10.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\", \"pid\": \"198771\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T16:31:39.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 36234.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:35:33.617Z\"}, \"exp_038_dual_critic_walker_s2\": {\"completed_at\": \"2026-05-22T02:11:36.842Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:35.293Z\", \"hypothesis\": \"Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments.\", \"metrics\": {\"civo_alert\": 0, \"civo_prevented\": true, \"eval_return_collapse\": 99.6, \"eval_return_collapse_step\": 175000, \"eval_return_final\": 120.9, \"eval_return_peak\": 354, \"eval_return_peak_step\": 155000, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": true, \"note\": \"CIVO prevented (NVE≤0.3) but non-CIVO eval collapse at 175k (354→99.6). Different failure mode from value overestimation.\", \"nve_final\": 0.248, \"nve_peak\": 0.3, \"steps\": 224000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-22T02:07:51.177Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...dual_critic walker s2...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 13.88, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\", \"model_name\": \"DreamerV3 + Dual Critic (wide)\", \"pid\": \"175633\", \"seed\": 2, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T12:18:34.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 49982.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:11:36.842Z\"}, \"exp_037_wide_critic_cheetah\": {\"completed_at\": \"2026-05-21T19:45:52.311Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:33.040Z\", \"hypothesis\": \"Wide single critic on Cheetah: if capacity=recovery generalizes from Walker (exp_033, NVE 4.75→self-repair, eval 408) to Cheetah (high CIVO, baseline NVE ~70.64), then Recovery mechanism works across CIVO severity levels. Combined with exp_034 (dual-critic Cheetah, NVE 1.75, eval 97.5), establishes that both Prevention and Recovery are environment-dependent.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 146.1, \"eval_return_peak\": 350.1, \"gate_dt_2_frac\": 1, \"nve_final\": 0.1, \"nve_peak\": 3.6, \"steps\": 224000}, \"parent\": \"exp_033_wide_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...wide_critic cheetah...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.46, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Wide Single Critic\", \"pid\": \"14487\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T12:18:32.619Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26839.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:52.311Z\"}, \"exp_036_dual_critic_pickcube\": {\"completed_at\": \"2026-05-21T19:45:31.290Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T08:43:18.481296+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T19:38:29.196731+00:00\"}]}, \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"gate_dt_2_frac\": 1, \"nve_final\": 0.2, \"nve_peak\": 2.3, \"steps\": 212447}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T19:38:24.346Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 11.03, \"gpu_id\": 0, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"2476\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T08:43:44.544357+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 39706.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:31.290Z\"}, \"exp_035_narrow_dual_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_035_narrow_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T16:11:39.130025+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:47:55.131429+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T16:08:03.906985+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect from parameter count. If CIVO suppressed → min operation itself prevents overestimation cascade. If CIVO persists → parameter count is the key factor. Combined with exp_033 (wide single critic) forms 2×2 factorial: {single,dual} × {normal,scaled} → mechanism decomposition.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"metrics\": {\"actor_entropy_final\": -0.19, \"civo_alert_window\": \"65K-85K\", \"civo_prevented\": false, \"civo_recovery\": true, \"director_override\": \"Director ruled success: CIVO recovery (33.8→697.8) is the success criterion, not prevention\", \"eval_at_215K\": 697.8, \"eval_at_85K\": 33.8, \"eval_final\": 697.8, \"eval_peak\": 697.8, \"eval_trough\": 33.8, \"nve_final\": 0.066, \"nve_peak\": 2.75, \"nve_peak_step\": 85000, \"recovery_from\": 33.8, \"recovery_to\": 697.8, \"total_steps\": 215000, \"train_return_final_range\": \"708-806\", \"v1_v2_gap_max\": 0.08, \"v1_v2_gap_typical\": 0.01}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T16:07:58.973Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T07:48:17.595Z\", \"training_hours\": 8.33}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 8.31, \"gpu_id\": 1, \"hyperparams\": {\"critic_hidden\": 256, \"critic_layers\": 2, \"critic_params_each\": 525000, \"critic_params_total\": 1050000, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"narrow_dual_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\", \"pid\": \"162900\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T07:56:05.926445+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29900.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:14:26.099Z\"}, \"exp_034\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/\", \"completed_at\": \"2026-05-21T12:18:09.552Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:17:29.760Z\", \"hypothesis\": \"Dual-critic (min of two independent critics) will prevent CIVO in Cheetah Run by providing pessimistic value estimates, as it did in Walker Walk (exp_032). If value overestimation is environment-universal, the same mechanism should work across DMC tasks.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"CIVO_prevented\": false, \"civo_trigger_steps\": [55000, 105000], \"final_NVE\": 0.144, \"final_eval_return\": 97.5, \"max_NVE\": 1.753, \"peak_eval_return\": 315.7, \"total_steps\": 215000, \"v1_v2_max_divergence\": 0.004}, \"retry_count\": 0, \"spec\": {\"command\": \"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:18:09.552Z\"}, \"exp_034_dual_critic_cheetah\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah\", \"completed_at\": \"2026-05-21T12:14:19.189109+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T05:50:59.612345+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:46.032647+00:00\"}]}, \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"baseline_eval_final\": 0.83, \"baseline_nve_peak\": 70.64, \"civo_alert_steps\": [95000, 105000], \"civo_alerts\": 2, \"civo_prevented\": false, \"dual_wave_civo\": true, \"eval_final\": 97.5, \"eval_final_step\": 215000, \"eval_peak\": 315.7, \"eval_peak_step\": 45000, \"eval_vs_peak_pct\": 31, \"gate_dt2_frac\": 1, \"gate_entropy\": 0, \"v1_v2_gap\": \"<0.2 (min operation has no pessimism effect)\", \"value_mean_final\": 14.2, \"value_mean_peak\": 60.5, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:37.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"993925\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T05:51:51.325323+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:15:03.481Z\"}, \"exp_033_wide_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"logdir/exp_033_wide_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T12:08:15.252Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T03:45:53.644963+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:31.184962+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rather than pessimistic min operation, then a single critic with 2× parameters should also suppress CIVO. If wide-critic fails (CIVO persists) but dual-critic succeeds → min operation has implicit regularization effect beyond pessimism.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"metrics\": {\"civo_alert_step\": 105000, \"civo_alert_ve_ratio\": 1.958, \"civo_instability_duration_steps\": 75000, \"critic_params\": 2886911, \"eval_reward_final\": 407.9, \"eval_reward_peak\": 194.8, \"eval_reward_trough\": 31.8, \"value_loss_final\": 1.4, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 4.7}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:26.400Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T03:46:14.882Z\", \"training_hours\": 8.27}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.25, \"gpu_id\": 0, \"hyperparams\": {\"critic_hidden\": 1024, \"critic_layers\": 2, \"critic_params\": 2886911, \"dual_critic\": false, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"wide_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"model_name\": \"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\", \"pid\": \"151860\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T03:52:59.702597+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29715.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:08:15.252Z\"}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031b_tcn_pickcube_s0_sigma05/latest.pt\", \"completed_at\": \"2026-05-21T08:43:18.481253+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:46:39.136363+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T08:41:51.310620+00:00\"}]}, \"failure_reason\": \"NVE late-stage decline is floor effect (value signal collapse), not CIVO recovery. Eval flat 25-29 throughout — agent never learned meaningful manipulation. Confirmed by Reviewer. TCN PickCube: 0/2 (σ=0.2 and σ=0.5 both failed).\", \"hypothesis\": \"PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed with NVE peak 3.71. σ=0.5 tests whether higher noise amplitude can suppress CIVO in ManiSkill PickCube. Combined with σ=0.2 data, establishes dose-response curve for robotics manipulation domain.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"metrics\": {\"eval_reward_final\": 25.5, \"eval_reward_last5_avg\": 25.9, \"eval_reward_peak\": 29.1, \"nve_final\": 0.2, \"nve_peak\": 3.3, \"nve_peak_step\": 42500, \"nve_suppressed_from_step\": 72500, \"total_episodes\": 1062, \"total_steps\": 212400}, \"parent\": \"exp_031_tcn_pickcube_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T08:41:45.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"model_name\": \"DreamerV3 + TCN σ=0.5\", \"pid\": \"968495\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T22:33:14.695383+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T08:50:22.853581+00:00\"}, \"exp_032_dual_critic_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T07:47:55.131382+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:58:31.008200+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T07:45:13.742811+00:00\"}]}, \"hypothesis\": \"Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses 008d CIVO-trigger config (trained dt_emb + multi-rate exposure). If NVE stays below 1.5× and eval matches baseline, dual-critic is an effective architecture-level intervention.\", \"metrics\": {\"baseline_eval\": 900, \"civo_prevented\": true, \"eval_final\": 739.7, \"eval_final_step\": 215000, \"eval_peak\": 787.7, \"eval_peak_step\": 205000, \"eval_vs_baseline_pct\": 87.5, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"note\": \"CIVO prevented 2/2 seeds. v1≈v2 → mechanism is implicit value regularization, not min-of-two pessimism.\", \"nve_final\": 0.1, \"nve_peak\": 1.1, \"nve_peak_step\": 95000, \"v1_v2_gap\": \"<0.1% (min operation has no pessimism effect)\"}, \"parent\": \"exp_008d_civo_trigger_s2\", \"reproduce\": {\"finished_at\": \"2026-05-21T07:45:08.395Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"pid\": \"124556\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T23:19:57.690519+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:52:13.265445+00:00\"}, \"exp_032b_dual_critic_walker_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032b_dual_critic_walker_s1/latest.pt\", \"completed_at\": \"2026-05-21T05:50:59.612299+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T23:22:08.787456+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T05:48:16.069863+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust architecture-level CIVO intervention, strengthening Intervention Hierarchy evidence.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032b_dual_critic_walker_s1.log\", \"metrics\": {\"actor_loss_late\": \"≈0 (gradient signal weak)\", \"baseline_eval\": 900, \"director_override\": \"CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.\", \"eval_criterion_pass\": false, \"eval_trajectory\": \"75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516\", \"eval_vs_baseline_pct\": 57, \"final_eval_return\": 516, \"final_nve\": 0.1, \"gate_dt2_frac\": 1.0, \"nve_criterion_pass\": true, \"nve_trajectory\": \"15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1\", \"peak_eval_return\": 551.8, \"peak_nve\": 1.4, \"total_steps\": 224000, \"total_updates\": 52599, \"training_hours\": 6.42, \"value1_value2_gap\": \"<0.5 (min operation has no pessimism effect)\"}, \"notes\": \"NVE well controlled (peak 1.4 < 1.5, no CIVO), but eval only 57% of baseline (516 vs ~900). Dual-critic suppresses value overestimation at cost of policy performance. Gate collapsed to dt=2 throughout. Two critics converge to near-identical values, min operation ineffective.\", \"parent\": \"exp_032_dual_critic_walker\", \"pid\": \"973387\", \"reproduce\": {\"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032b_dual_critic_walker_s1\\\"\", \"finished_at\": \"2026-05-21T05:48:11.173Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-20T23:22:55.338Z\", \"training_hours\": 6.42}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0}, \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"seed\": 1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:55:05.353975+00:00\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"completed_at\": \"2026-05-21T03:39:24.356918+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:33:03.633Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T03:32:52.751412+00:00\"}]}, \"failure_reason\": \"Sudden CIVO blowup: NVE appeared healthy at 95K (0.666, declining from 0.855@85K), then catastrophic spike to 3.0@105K. Eval collapsed 349.6→71.8. Late-stage NVE recovery to 0.4@215K = value adaptation (eval stayed at 104.5, never recovered). TCN σ=0.2 Walker: 2/4 seeds CIVO failure (s2: NVE 2.77, s3: NVE 3.0).\", \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443, s3=869, s4=923@105K) for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"metrics\": {\"civo_onset_step\": 105000, \"civo_pattern\": \"sudden blowup (healthy 0.67@95K → 3.0@105K)\", \"eval_final\": 104.5, \"eval_last_step\": 215000, \"eval_peak\": 349.6, \"eval_peak_step\": 95000, \"eval_return_105K\": 71.8, \"eval_return_115K\": 69.8, \"eval_return_125K\": 61.5, \"eval_return_135K\": 141.8, \"eval_return_145K\": 98.66, \"eval_return_155K\": 88.86, \"eval_return_15K\": 159.1, \"eval_return_165K\": 86.22, \"eval_return_175K\": 123.53, \"eval_return_185K\": 153.71, \"eval_return_195K\": 68.84, \"eval_return_205K\": 63.71, \"eval_return_215K\": 104.5, \"eval_return_25K\": 155.7, \"eval_return_35K\": 190.8, \"eval_return_45K\": 137.1, \"eval_return_55K\": 210.7, \"eval_return_5K\": 31.7, \"eval_return_65K\": 189.5, \"eval_return_75K\": 253.2, \"eval_return_85K\": 259.5, \"eval_return_95K\": 349.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"nve_peak\": 3.0, \"nve_peak_step\": 105000, \"step\": 224000, \"value_mean_105K\": 218.37, \"value_mean_215K\": 42.55, \"value_mean_95K\": 232.74, \"ve_ratio_105K\": 3.0, \"ve_ratio_115K\": 2.5, \"ve_ratio_125K\": 2.4, \"ve_ratio_135K\": 0.9, \"ve_ratio_145K\": 1.141, \"ve_ratio_155K\": 1.06, \"ve_ratio_165K\": 0.91, \"ve_ratio_175K\": 0.556, \"ve_ratio_185K\": 0.396, \"ve_ratio_195K\": 0.78, \"ve_ratio_205K\": 0.747, \"ve_ratio_215K\": 0.4, \"ve_ratio_45K\": 0.695, \"ve_ratio_55K\": 0.598, \"ve_ratio_65K\": 0.863, \"ve_ratio_75K\": 0.791, \"ve_ratio_85K\": 0.9, \"ve_ratio_95K\": 0.7}, \"parent\": \"exp_029b_tcn_walker_s2_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T03:32:47.021Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"pid\": \"109826\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T19:33:48.032Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:39:24.356963+00:00\"}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031_tcn_pickcube_s0_sigma02\", \"completed_at\": \"2026-05-20T23:52:48.308Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T12:09:56.923Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T23:50:00.801433+00:00\"}]}, \"hypothesis\": \"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\", \"metrics\": {\"eval_peak\": 28.6, \"eval_peak_step\": 162500, \"eval_return_132K\": 23.45, \"eval_return_152K\": 23.1, \"eval_return_192K\": 11.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0, \"step\": 195600, \"train_return_range\": \"18-25\", \"ve_ratio_latest\": 0.18, \"ve_ratio_peak\": 3.71}, \"parent\": \"exp_019b_pickcube_civo_trigger\", \"reproduce\": {\"finished_at\": \"2026-05-20T23:49:56.649Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"none(train_from_scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"data_count\": \"200000(online)\", \"data_path\": \"maniskill_PickCube-v1\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 11.17, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"908459\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 40206.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:52:48.308Z\"}, \"exp_029b_tcn_walker_s2_sigma02\": {\"completed_at\": \"2026-05-20T22:58:31.008151+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:55:13.731Z\", \"failure_reason\": \"CIVO confirmed: NVE accelerated 1.01→1.65→2.77@105K (008d-like pattern), eval collapsed 177.7→32.0. Late-stage NVE decline to 1.06@155K = value adaptation to collapsed policy, NOT CIVO self-recovery (eval remained at 56.5, never recovered). Killed at 156K to free GPU for dual-critic experiment.\", \"hypothesis\": \"TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%. Third seed resolves whether high variance is systematic or s1 is outlier.\", \"metrics\": {\"civo_onset_step\": 65000, \"eval_last_step\": 165000, \"eval_peak\": 177.67, \"eval_peak_step\": 55000, \"eval_return_105K\": 31.97, \"eval_return_115K\": 35.45, \"eval_return_125K\": 33.04, \"eval_return_135K\": 42.47, \"eval_return_145K\": 51.66, \"eval_return_155K\": 56.5, \"eval_return_15K\": 168.41, \"eval_return_165K\": 44.9, \"eval_return_25K\": 159.56, \"eval_return_35K\": 168.05, \"eval_return_45K\": 171.51, \"eval_return_55K\": 177.67, \"eval_return_5K\": 30.46, \"eval_return_65K\": 106.57, \"eval_return_75K\": 64.01, \"eval_return_85K\": 62.82, \"eval_return_95K\": 44.66, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"late_stage_nve_decline\": \"value adaptation (value_mean 108→55), not recovery (eval stayed 32-57)\", \"nve_peak\": 2.765, \"nve_peak_step\": 105000, \"step\": 168000, \"value_mean_105K\": 88.38, \"value_mean_165K\": 55.03, \"value_mean_55K\": 103.62, \"ve_ratio_105K\": 2.765, \"ve_ratio_115K\": 2.326, \"ve_ratio_125K\": 2.278, \"ve_ratio_135K\": 1.648, \"ve_ratio_145K\": 1.234, \"ve_ratio_155K\": 1.061, \"ve_ratio_15K\": 0.03, \"ve_ratio_165K\": 1.226, \"ve_ratio_25K\": 0.174, \"ve_ratio_35K\": 0.335, \"ve_ratio_45K\": 0.477, \"ve_ratio_55K\": 0.583, \"ve_ratio_65K\": 1.014, \"ve_ratio_75K\": 1.65, \"ve_ratio_85K\": 1.623, \"ve_ratio_95K\": 2.109}, \"parent\": \"exp_029a_tcn_walker_s1_sigma02\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\", \"pid\": \"75543\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T16:56:24.781Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:58:31.008195+00:00\"}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"completed_at\": \"2026-05-20T22:34:07.916411+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:26:11.800Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T22:28:30.207347+00:00\"}]}, \"hypothesis\": \"TCN σ=1.0 on Cheetah tests whether higher noise amplitude further suppresses CIVO. σ=0.5 (exp_030b) was negative with NVE peaking at 10.67@55K then declining. σ=1.0 should provide stronger temporal regularization. If NVE stays below 1.5 throughout training and eval_return ≥ baseline → TCN generalizes to Cheetah with appropriate σ scaling.\", \"metrics\": {\"baseline_eval_avg\": 548, \"eval_final\": 47.2, \"eval_peak\": 371.7, \"eval_peak_step\": 35000, \"eval_return_105K\": 122.5, \"eval_return_115K\": 162.2, \"eval_return_125K\": 148.5, \"eval_return_135K\": 138.4, \"eval_return_145K\": 100.4, \"eval_return_155K\": 144.3, \"eval_return_15K\": 87.5, \"eval_return_165K\": 130.9, \"eval_return_175K\": 66.4, \"eval_return_185K\": 47.2, \"eval_return_195K\": 56.5, \"eval_return_205K\": 49.7, \"eval_return_215K\": 47.2, \"eval_return_25K\": 166.3, \"eval_return_35K\": 371.7, \"eval_return_45K\": 144.0, \"eval_return_55K\": 266.0, \"eval_return_5K\": 8.3, \"eval_return_65K\": 197.0, \"eval_return_75K\": 107.8, \"eval_return_85K\": 95.8, \"eval_return_95K\": 72.8, \"eval_vs_baseline\": \"8.6%\", \"gate_dt2_frac\": 1.0, \"gate_dt_mean\": 2.0, \"gate_entropy\": 0.0, \"step\": 224000, \"ve_ratio_max\": 0.4}, \"parent\": \"\", \"reproduce\": {\"finished_at\": \"2026-05-20T22:28:26.022Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\", \"command\": \"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\", \"data_count\": 210000, \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\", \"model_name\": \"dreamerv3\", \"pid\": \"920968\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T16:49:48.464Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:34:07.916452+00:00\"}, \"exp_029c_tcn_walker_s0_sigma01\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:09:50.913Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T19:30:34.687287+00:00\"}]}, \"hypothesis\": \"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\", \"metrics\": {\"eval_final\": 328.3, \"eval_peak\": 490.7, \"eval_peak_step\": \"165K\", \"eval_return_105K\": 204.7, \"eval_return_115K\": 296.4, \"eval_return_125K\": 232.3, \"eval_return_135K\": 247.4, \"eval_return_145K\": 323.1, \"eval_return_155K\": 359.7, \"eval_return_15K\": 99.1, \"eval_return_165K\": 490.7, \"eval_return_175K\": 246.2, \"eval_return_185K\": 220.6, \"eval_return_195K\": 212.8, \"eval_return_205K\": 256.9, \"eval_return_215K\": 328.3, \"eval_return_25K\": 140.7, \"eval_return_35K\": 155.7, \"eval_return_45K\": 160.9, \"eval_return_55K\": 254.8, \"eval_return_5K\": 35.6, \"eval_return_65K\": 268.7, \"eval_return_75K\": 295.5, \"eval_return_85K\": 220.8, \"eval_return_95K\": 188.6, \"nve_final\": 0.1, \"nve_max\": 1.0218, \"nve_max_step\": \"95K\", \"total_steps\": 224000, \"ve_ratio_105K\": 0.761, \"ve_ratio_115K\": 0.4514, \"ve_ratio_125K\": 0.4899, \"ve_ratio_135K\": 0.3995, \"ve_ratio_145K\": 0.2667, \"ve_ratio_155K\": 0.2, \"ve_ratio_15K\": 0.0306, \"ve_ratio_165K\": 0.1, \"ve_ratio_175K\": 0.3, \"ve_ratio_185K\": 0.3, \"ve_ratio_195K\": 0.3, \"ve_ratio_205K\": 0.2, \"ve_ratio_215K\": 0.1, \"ve_ratio_25K\": 0.1606, \"ve_ratio_35K\": 0.3162, \"ve_ratio_45K\": 0.4807, \"ve_ratio_55K\": 0.4368, \"ve_ratio_65K\": 0.5432, \"ve_ratio_75K\": 0.6211, \"ve_ratio_85K\": 0.9533, \"ve_ratio_95K\": 1.0218}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T19:30:28.923Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\", \"checkpoint_source\": \"from_scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"model_name\": \"dreamer\", \"pid\": \"59395\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:53:26.097Z\"}, \"exp_029a_tcn_walker_s1_sigma02\": {\"completed_at\": \"2026-05-20T16:47:18.789Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T08:31:29.514Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T16:47:29.902718+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\", \"metrics\": {\"current_step\": 215000, \"eval_last10_mean\": 282.15, \"eval_peak\": 401, \"eval_peak_step\": \"125K\", \"eval_return_105K\": 319.4, \"eval_return_115K\": 345.5, \"eval_return_125K\": 401, \"eval_return_135K\": 307.8, \"eval_return_145K\": 380.8, \"eval_return_155K\": 307.3, \"eval_return_15K\": 137.7, \"eval_return_165K\": 320.3, \"eval_return_175K\": 159, \"eval_return_185K\": 278.2, \"eval_return_195K\": 301.2, \"eval_return_205K\": 204.6, \"eval_return_215K\": 161.3, \"eval_return_25K\": 180.9, \"eval_return_35K\": 124, \"eval_return_45K\": 124.2, \"eval_return_55K\": 133.9, \"eval_return_5K\": 36.7, \"eval_return_65K\": 169.7, \"eval_return_75K\": 171.2, \"eval_return_85K\": 151.8, \"eval_return_95K\": 180.3, \"nve_final\": 0.1864, \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_15K\": 0.0248, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007}, \"notes\": \"Cron 误报: process exited without sentinel/W&B, 但实验已正常完成 (215K/210K target). NVE max 0.6428@55K (CIVO suppressed), eval peak 401@125K (45% baseline). 对比 parent s0: s0 eval 达 baseline, s1 仅 45% → 高 seed 方差暴露 TCN 脆弱性. 结论 conclusion=success 不变.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T16:47:17.713Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"50924\", \"seed\": 1, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:53:36.867Z\"}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"completed_at\": \"2026-05-20T16:49:02.778Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:07:53.975Z\", \"hypothesis\": \"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\", \"metrics\": {\"current_step\": 195000, \"eval_return_105K\": 104.4, \"eval_return_115K\": 137.7, \"eval_return_125K\": 211.7, \"eval_return_135K\": 97.2, \"eval_return_145K\": 79.4, \"eval_return_155K\": 76.8, \"eval_return_15K\": 78.3, \"eval_return_165K\": 77.5, \"eval_return_175K\": 85.7, \"eval_return_185K\": 68.7, \"eval_return_195K\": 77.6, \"eval_return_25K\": 219.3, \"eval_return_35K\": 296.5, \"eval_return_45K\": 32.8, \"eval_return_55K\": 6, \"eval_return_5K\": 8.3, \"eval_return_65K\": 71.2, \"eval_return_75K\": 23.3, \"eval_return_85K\": 34, \"eval_return_95K\": 143.6, \"nve_final\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_15K\": 0.0202, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253}, \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:49:02.778Z\"}, \"exp_027_tcn_walker_s1\": {\"completed_at\": \"2026-05-20T12:38:02.085Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T05:51:53.479Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T12:35:42.576855+00:00\"}]}, \"hypothesis\": \"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\", \"metrics\": {\"eval_last10_mean\": 233.1, \"eval_peak\": 364.9, \"eval_peak_step\": 75000, \"eval_return\": {\"105000\": 216.7, \"115000\": 318.9, \"125000\": 309.1, \"135000\": 216.1, \"145000\": 175.4, \"15000\": 140.5, \"155000\": 171, \"165000\": 209.5, \"175000\": 120.4, \"185000\": 355.4, \"195000\": 183.3, \"205000\": 240.2, \"215000\": 350.8, \"25000\": 163.6, \"35000\": 153, \"45000\": 136.8, \"5000\": 31, \"55000\": 158.3, \"65000\": 298.5, \"75000\": 364.9, \"85000\": 134, \"95000\": 94.6}, \"nve_final\": 0.1476, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"total_steps\": 215000, \"ve_ratio\": {\"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"15000\": 0.0246, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367}}, \"parent\": \"exp_027_tcn_walker_s0\", \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:38.092Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:45:31.028Z\"}, \"exp_027_tcn_walker_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:19:31.331Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:25:32.533Z\", \"hypothesis\": \"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\", \"metrics\": {\"eval_last10_mean\": 587.1, \"eval_peak\": 821.1, \"eval_peak_step\": \"175K\", \"eval_return_105K\": 236.4, \"eval_return_115K\": 543.8, \"eval_return_125K\": 458.4, \"eval_return_135K\": 496.7, \"eval_return_145K\": 542.7, \"eval_return_155K\": 660.5, \"eval_return_15K\": 150.6, \"eval_return_165K\": 653.3, \"eval_return_175K\": 821.1, \"eval_return_185K\": 560.5, \"eval_return_195K\": 567.9, \"eval_return_205K\": 558.7, \"eval_return_215K\": 551, \"eval_return_25K\": 199.4, \"eval_return_35K\": 278.2, \"eval_return_45K\": 315.6, \"eval_return_55K\": 278.6, \"eval_return_5K\": 35.6, \"eval_return_65K\": 331, \"eval_return_75K\": 293.1, \"eval_return_85K\": 363.9, \"eval_return_95K\": 171.4, \"nve_final\": 0.0955, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"total_steps\": 215000, \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_15K\": 0.0192, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081}, \"parent\": \"exp_027_tcn_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"data_count\": 215000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:06:21.855Z\"}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:10:00.827Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T09:24:38.711Z\", \"hypothesis\": \"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\", \"metrics\": {\"current_step\": 64000, \"eval_return_35K\": 299.5, \"eval_return_55K\": 31.9, \"note\": \"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\", \"target_steps\": 210000, \"ve_ratio_55K\": 1.903}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"checkpoint_source\": \"from_scratch\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:10:00.827Z\"}, \"exp_027_tcn_walker_s0\": {\"analysis_summary\": \"TCN (σ=0.5 noise on dt_embedding) FAILED to suppress CIVO. NVE breached 1.5× threshold 3 times: 55K(1.68×), 65K(1.54×), 85K(3.97×). Peak NVE 3.97× at 85K is HIGHER than typical CIVO, suggesting TCN destabilizes value learning. Eval peaked at 240 (35K), then collapsed to avg 117 in latter half — far below 450 target. Gate remained fixed at dt=2 throughout (zero entropy). The noise magnitude was insufficient to decorrelate critic estimates from dt conditioning. Training reached 120K/210K planned. Hypothesis falsified: forward-pass noise at σ=0.5 does not prevent critic from exploiting dt-specific value structure.\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s0/latest.pt\", \"completed_at\": \"2026-05-20T09:24:09.016Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:51.820Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T06:06:34.898602+00:00\"}]}, \"hypothesis\": \"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"metrics\": {\"eval_return_105K\": 95.5, \"eval_return_112K\": 99.5, \"eval_return_15K\": 154.6, \"eval_return_25K\": 223.6, \"eval_return_35K\": 240, \"eval_return_45K\": 101.2, \"eval_return_55K\": 70, \"eval_return_5K\": 37.4, \"eval_return_65K\": 95.1, \"eval_return_75K\": 189.2, \"eval_return_85K\": 36, \"eval_return_95K\": 166.4, \"final_step\": 120000, \"gate_dt_entropy\": 0, \"gate_dt_mean\": 2, \"last_5_eval_avg\": 117.3, \"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"peak_eval\": 240, \"peak_eval_step\": \"35K\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.916, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T06:06:30.806Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"pid\": \"888715\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11433.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:24:09.016Z\"}, \"exp_028_rave_walker_s0_ceil15\": {\"completed_at\": \"2026-05-20T08:31:12.389Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T03:25:34.045Z\", \"hypothesis\": \"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\", \"metrics\": {\"current_step\": 135000, \"eval_return_105K\": 76.2, \"eval_return_115K\": 41.2, \"eval_return_125K\": 36.6, \"eval_return_135K\": 39.1, \"eval_return_15K\": 99.4, \"eval_return_25K\": 155.3, \"eval_return_35K\": 180.1, \"eval_return_45K\": 166.9, \"eval_return_55K\": 131, \"eval_return_5K\": 31.6, \"eval_return_65K\": 91.5, \"eval_return_75K\": 120.9, \"eval_return_85K\": 137.3, \"eval_return_95K\": 70.2, \"target_steps\": 210000, \"ve_ratio_105K\": 0.984, \"ve_ratio_115K\": 1.513, \"ve_ratio_125K\": 1.462, \"ve_ratio_135K\": 1.171, \"ve_ratio_15K\": 0.03, \"ve_ratio_25K\": 0.128, \"ve_ratio_35K\": 0.247, \"ve_ratio_45K\": 0.428, \"ve_ratio_55K\": 0.737, \"ve_ratio_65K\": 1.294, \"ve_ratio_75K\": 0.937, \"ve_ratio_85K\": 0.727, \"ve_ratio_95K\": 1.28}, \"parent\": \"exp_028_rave_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"model_name\": \"dreamerv3_rave_ceil15\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\", \"pid\": \"38372\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:31:12.389Z\"}, \"exp_028_rave_walker_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/checkpoint.ckpt\", \"completed_at\": \"2026-05-20T06:14:31.720Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:53.882Z\", \"hypothesis\": \"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/\", \"metrics\": {\"current_steps\": 105000, \"eval_trajectory\": {\"105K\": {\"eval_return\": 29, \"value_mean\": 92.2, \"ve_ratio\": 3.183}, \"15K\": {\"eval_return\": 105.3, \"value_mean\": 2.93, \"ve_ratio\": 0.028}, \"25K\": {\"eval_return\": 191.9, \"value_mean\": 24.4, \"ve_ratio\": 0.127}, \"35K\": {\"eval_return\": 204.6, \"ve_ratio\": 0.267}, \"45K\": {\"eval_return\": 197.7, \"ve_ratio\": 0.439}, \"55K\": {\"eval_return\": 193, \"ve_ratio\": 0.62}, \"5K\": {\"eval_return\": 37.4, \"value_mean\": 0.001}, \"65K\": {\"eval_return\": 79.8, \"ve_ratio\": 1.832}, \"75K\": {\"eval_return\": 44.5, \"ve_ratio\": 3.415}, \"85K\": {\"eval_return\": 57.7, \"ve_ratio\": 2.126}, \"95K\": {\"eval_return\": 25.9, \"value_mean\": 105.87, \"ve_ratio\": 4.086}}, \"note\": \"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\"}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"model_name\": \"dreamerv3_rave_ceil20\", \"pid\": \"879636\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12005.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T06:14:31.720Z\"}, \"exp_025_obs_sgs_walker_s2\": {\"completed_at\": \"2026-05-20T03:14:06.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-19T16:39:26.941Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T03:14:13.011509+00:00\"}]}, \"failure_reason\": \"Reclassified: experiment completed 224K/210K steps normally. Cron misclassified as failed due to missing W&B sentinel. Actual result is negative — obs-decoder SGS suppressed CIVO (ve_ratio 0.8-1.4) but eval collapsed to ~90 (baseline ~930).\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"metrics\": {\"eval_return_215K\": 89.6, \"target_steps\": 210000, \"train_steps_completed\": 224000, \"ve_ratio_175K\": 1.2, \"ve_ratio_185K\": 1.4, \"ve_ratio_215K\": 0.8}, \"notes\": \"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:14:07.466Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7989\", \"seed\": 2, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s2\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:17:26.061Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"completed_at\": \"2026-05-20T03:02:46.556Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:29.171Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16346\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:46.556Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"completed_at\": \"2026-05-20T03:02:43.170Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:27.608Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16208\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s0\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:43.170Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"completed_at\": \"2026-05-20T03:02:39.948Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:29.810Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"851593\", \"seed\": 4, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s4\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:39.948Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"completed_at\": \"2026-05-20T03:02:36.670Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:28.402Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"847597\", \"seed\": 3, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s3\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:36.670Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"completed_at\": \"2026-05-20T03:02:32.583Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:25.583Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7833\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:32.583Z\"}, \"exp_001_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T23:06:42.122Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:31.737Z\", \"hypothesis\": \"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\", \"metrics\": {\"convergence_mean_250k_plus\": 935, \"final_eval_return\": 938.86, \"final_step\": 520000, \"peak_eval_return\": 960.6}, \"parent\": \"exp_001_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 112000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T23:06:42.122Z\"}, \"exp_001_baseline_s3_extended\": {\"completed_at\": \"2026-05-19T21:23:44.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:30.382Z\", \"hypothesis\": \"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\", \"metrics\": {\"eval_profile\": {\"102000\": 869.03, \"112000\": 898.89, \"120000\": 898.38, \"130000\": 837.74, \"140000\": 876.64, \"15000\": 224.27, \"150000\": 899.47, \"160000\": 922.77, \"170000\": 925.77, \"180000\": 912.89, \"190000\": 915.07, \"200000\": 894.77, \"210000\": 899.79, \"220000\": 951.18, \"230000\": 930.56, \"240000\": 910.47, \"25000\": 329.99, \"250000\": 914.02, \"260000\": 931.33, \"270000\": 954.65, \"280000\": 928.01, \"290000\": 947.4, \"300000\": 853.32, \"310000\": 906.35, \"320000\": 847.16, \"330000\": 934.78, \"340000\": 921.08, \"35000\": 413.12, \"350000\": 922.63, \"360000\": 844.99, \"370000\": 911.36, \"380000\": 917.73, \"390000\": 937.21, \"400000\": 928, \"410000\": 945.88, \"420000\": 897.2, \"430000\": 949.45, \"440000\": 937.28, \"45000\": 332.69, \"450000\": 924.24, \"460000\": 967.25, \"470000\": 940.55, \"480000\": 936.24, \"490000\": 944.67, \"5000\": 42.15, \"500000\": 957.09, \"510000\": 947.68, \"55000\": 519.91, \"65000\": 667.42, \"72000\": 771.33, \"82000\": 772.88, \"92000\": 854.6}, \"final_eval_return\": 947.68, \"final_step\": 520000, \"final_train_return_avg\": 945.4}, \"parent\": \"exp_001_baseline_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s3/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s3/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_001_baseline_s3/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 120000, \"seed\": 3, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s3_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:23:44.025Z\"}, \"exp_001_baseline_s2_extended\": {\"completed_at\": \"2026-05-19T17:44:27.212Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:10:10.948Z\", \"hypothesis\": \"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\", \"metrics\": {\"eval_return_at_105K\": 443.5, \"eval_return_final\": 945.7, \"eval_return_peak\": 962.6, \"total_steps\": 512000, \"value_mean_at_105K\": 329.16, \"value_mean_plateau\": 665, \"ve_ratio_at_105K\": 0.7422, \"ve_ratio_converged_range\": \"0.69-0.77\"}, \"parent\": \"exp_001_baseline_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s2/latest.pt\", \"checkpoint_source\": \"logdir/exp_001_baseline_s2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\", \"data_count\": 0, \"data_path\": \"logdir/exp_001_baseline_s2\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s2/train_extended.log\", \"model_name\": \"dreamerv3\", \"resumed_from_step\": 112000, \"seed\": 2, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s2_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:44:27.212Z\"}, \"exp_023_cheetah_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T09:02:40.466Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T06:27:42.161Z\", \"hypothesis\": \"Cheetah Run baseline seed=4 extended to 300K. Tests whether eval drop at 194K→204K (537→302) is transient fluctuation or permanent collapse. Informs baseline stability and NVE normalization robustness.\", \"metrics\": {\"eval_302k\": 580, \"eval_peak_ext\": 642.3, \"eval_peak_ext_step\": 272000, \"note\": \"延长到 300K 确认非 collapse。eval 恢复到 642 peak@272K，200K-300K 区间震荡上行 (301-642 range)，194K→204K 骤降为 transient fluctuation。\"}, \"parent\": \"exp_023_cheetah_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_023_cheetah_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_023_cheetah_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"300000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_023_cheetah_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 212000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 300000, \"tmux_session\": \"exp_023_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:02:40.466Z\"}, \"exp_001_baseline_s4\": {\"completed_at\": \"2026-05-19T09:00:10.632Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:47:01.105Z\", \"hypothesis\": \"Walker Walk baseline seed=4. Fourth seed for 4-seed baseline CI. Tests whether s2 (443.5) is outlier or bimodal distribution (s1=915.7, s3=869.0).\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 922.8, \"peak_eval\": 922.8, \"peak_eval_step\": 105000, \"target_steps\": 105000, \"value_mean_final\": 576.1, \"ve_ratio_105k\": 0.624}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:00:10.632Z\"}, \"exp_023_cheetah_baseline_s4\": {\"completed_at\": \"2026-05-19T06:26:03.295Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:02.288Z\", \"hypothesis\": \"Cheetah Run baseline seed=4. Fourth seed for tighter eval return CI and NVE normalization robustness.\", \"metrics\": {\"current_step\": 212000, \"eval_return_194k\": 537.03, \"eval_return_204k\": 301.69, \"note\": \"Cheetah baseline s4. Large eval drop 194K→204K (537→302). ve_ratio>1 indicates value overestimation at final step.\", \"peak_eval\": 537.03, \"peak_eval_step\": 194000, \"target_steps\": 200000, \"value_mean_204k\": 339.14, \"ve_ratio_204k\": 1.124}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"200K env steps\", \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"dmc_cheetah_run eval episodes\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774033, \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:26:03.295Z\"}, \"exp_023_cheetah_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:47.459Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:49:33.229Z\", \"hypothesis\": \"Cheetah Run baseline seed=3. Extends 023a/023b/023_s2 (3 seeds) to 4 seeds for tighter eval return CI.\", \"metrics\": {\"current_step\": 204000, \"eval_return_202k\": 642.13, \"peak_eval\": 685.93, \"peak_eval_step\": 172000, \"target_steps\": 200000, \"value_mean_final\": 445.42, \"ve_ratio_final\": 0.694}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3\", \"checkpoint_source\": \"N/A\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 3 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s3\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"768897\", \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:47.459Z\"}, \"exp_001_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:45.989Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:03.635Z\", \"hypothesis\": \"Walker Walk baseline seed=3. Third seed for tighter baseline eval CI.\", \"metrics\": {\"current_step\": 120000, \"eval_return_102k\": 869.03, \"peak_eval\": 898.89, \"peak_eval_step\": 112000, \"target_steps\": 105000, \"value_mean_final\": 622.2, \"ve_ratio_final\": 0.692}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"105K env steps\", \"data_path\": \"dmc_walker_walk (online RL)\", \"eval_data\": \"dmc_walker_walk eval episodes\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774106, \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:45.989Z\"}, \"exp_023_cheetah_baseline_s2\": {\"completed_at\": \"2026-05-19T00:13:55.909Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:14.249Z\", \"hypothesis\": \"Cheetah Run baseline additional seed for tighter CI. Extends 023a/023b (2 seeds) to 3 seeds.\", \"metrics\": {\"current_step\": 205000, \"eval_return_final\": 645.4, \"note\": \"Cheetah Run baseline seed=2. Third baseline seed for NVE normalization.\", \"target_steps\": 200000}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 2 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s2\\\"\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.13, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"753786\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:05:57.478Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29278.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:13:55.909Z\"}, \"exp_008f_s4\": {\"completed_at\": \"2026-05-18T23:18:51.672Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T18:41:00.894Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 008f control (existing seeds: 1/008f, 2/009c, 3/008f_s3). C2 causal contrast robustness.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_105k\": 306.5, \"note\": \"No CIVO. No-dt-emb control seed=4. Peak NVE 1.41x @85K (transient), settles to 0.58x @105K.\", \"nve_105k\": 0.58, \"peak_eval\": 487.5, \"peak_eval_step\": 55000, \"peak_nve\": 1.41, \"peak_nve_step\": 85000}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:18:51.672Z\"}, \"exp_009c_s3\": {\"completed_at\": \"2026-05-18T21:40:10.763Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T17:12:00.539Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=3. Additional seed for 009c (seed=2 NVE 1.14x at 105K on upward trajectory); tests whether NVE rise is reproducible across independent seeds or stochastic.\", \"metrics\": {\"current_step\": 108000, \"eval_return_105k\": 311.92, \"note\": \"eval peaked at 55-65K (~457) then declined to 311.92. NVE 0.52x (no CIVO). 009c seed=2 NVE 1.14x not reproduced.\", \"nve_105k\": 0.52, \"target_steps\": 105000, \"value_mean_105k\": 120.27, \"ve_ratio_105k\": 0.386}, \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:10.762Z\"}, \"exp_001_baseline_s2\": {\"completed_at\": \"2026-05-18T21:40:09.329Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:17.571Z\", \"hypothesis\": \"Walker Walk baseline additional seed for tighter evaluation return CI.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 443.46, \"target_steps\": 105000, \"value_mean_105k\": 329.16, \"ve_ratio_105k\": 0.742}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:09.329Z\"}, \"exp_008f_s2\": {\"completed_at\": \"2026-05-18T18:41:05.369Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:16.527Z\", \"hypothesis\": \"No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.58, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754063\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:00.248Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9305.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:41:05.369Z\"}, \"exp_008a_cheetah_unexposed_s1\": {\"completed_at\": \"2026-05-18T18:20:00.278Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:13.377Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=1. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 504.38, \"nve_105k\": 0.478, \"target_steps\": 105000, \"value_mean_105k\": 156.97, \"ve_ratio_105k\": 0.3112}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:20:00.278Z\"}, \"exp_008a_cheetah_unexposed_s0\": {\"completed_at\": \"2026-05-18T18:19:58.491Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:12.052Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=0. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 532.35, \"nve_105k\": 0.49, \"target_steps\": 105000, \"value_mean_105k\": 169.98, \"ve_ratio_105k\": 0.3193}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:19:58.491Z\"}, \"exp_009c_s2\": {\"completed_at\": \"2026-05-18T17:12:05.307Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:19.850Z\", \"hypothesis\": \"No-dt-emb H=15 additional seed. 009c seed=2 showed NVE 1.14x at 105K on upward trajectory; additional seed tests if this is reproducible or stochastic.\", \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.1, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754639\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:05.850Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3959.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:12:05.307Z\"}, \"exp_008e_v3_s4\": {\"completed_at\": \"2026-05-18T11:33:57.033Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:54:56.392Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:31:45.212576+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=4. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"civo\": false, \"eval_return\": 899.3, \"nve_note\": \"Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K\", \"nve_peak\": 0.99, \"nve_peak_step\": 95000, \"ve_ratio_105k\": 0.609}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:31:41.800Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s4.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:45.880Z\"}, \"exp_008e_v3_s3\": {\"completed_at\": \"2026-05-18T11:24:41.197Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T02:54:54.691Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:20:58.896484+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=3. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"actor_entropy_final\": -4.892, \"collapse_onset\": \"85K-95K\", \"eval_return\": 92.7, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"nve_note\": \"Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02\", \"nve_peak\": 4.02, \"nve_peak_step\": 105000, \"peak_eval\": 520.4, \"peak_step\": 85000, \"ve_ratio_105k\": 2.635}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:20:55.020Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s3.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:43.665Z\"}, \"exp_008a_unexposed_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/latest.pt\", \"completed_at\": \"2026-05-18T08:16:42.716Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:56.020Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:12:12.866455+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=1. 直接复现 008a_no_subsample_dt2 配置（eval=778, V-recovery, no CIVO）。C3 reproducibility rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.0028, \"civo_ve_ratio_final\": 0.43, \"eval_return_15k\": 167.12, \"eval_return_25k\": 139.94, \"eval_return_35k\": 394.15, \"eval_return_45k\": 414.32, \"eval_return_55k\": 441.48, \"eval_return_5k\": 31, \"eval_return_65k\": 491.74, \"eval_return_75k\": 452.34, \"eval_return_85k\": 546.82, \"eval_return_95k\": 628.57, \"eval_return_final\": 630.91, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 272.13, \"total_steps\": 105000, \"value_mean_final\": 271.36}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:12:09.402Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk (online RL)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724312\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:15:06.654Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10896.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:16:42.716Z\"}, \"exp_008a_unexposed_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/latest.pt\", \"completed_at\": \"2026-05-18T08:10:06.059Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:57.340Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:07:33.602043+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.003, \"civo_ve_ratio_final\": 0.333, \"eval_return_55k\": 607.5, \"eval_return_65k\": 653.8, \"eval_return_75k\": 534.4, \"eval_return_85k\": 605.4, \"eval_return_95k\": 819.4, \"eval_return_final\": 899.4, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"value_mean_final\": 299.4}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:07:27.087Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.84, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724965\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10239.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:10:17.263Z\"}, \"exp_008a_untrained_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:51.398Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：C3 rebuttal 应复现 008a (unexposed trained dt_emb, subsample OFF) 而非 015b (frozen)。替换为 exp_008a_unexposed_s1/s2。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_008a_untrained_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:53.011Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：同上。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\", \"completed_at\": \"2026-05-18T05:11:15.900Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:47.702Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + H=8. 第二 seed 复现 Cheetah CIVO (NVE>1.5×)，加强跨环境因果论证统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/metrics.jsonl\", \"metrics\": {\"civo\": true, \"civo_onset_step\": \"65K\", \"detector_alert_step\": \"95K\", \"eval_return_105K\": 0.83, \"eval_return_peak\": 247.77, \"eval_return_peak_step\": \"35K\", \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"nve_105K\": 70.64, \"nve_95K\": 6.34}, \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run (online RL)\", \"gpu\": \"cuda:1\", \"model_name\": \"DreamerV3-cheetah-civo-trigger\", \"pid\": \"715412\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:11:15.900Z\"}, \"exp_024b_cheetah_no_dt_emb_s0\": {\"completed_at\": \"2026-05-18T02:00:15.236Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:50:34.104Z\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角。\", \"metrics\": {\"civo\": false, \"eval_return_final\": 96.5, \"nve_peak\": 0.2}, \"notes\": \"No CIVO (NVE peak <0.2×). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. eval 96.5 = 17.6% of baseline (548.3). Cheetah causal triangle seed 1 complete. Director confirmed results in D089.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s0/latest.pt\", \"checkpoint_source\": \"N/A-training-from-scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run-online-eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s0.log\", \"model_name\": \"DreamerV3-cheetah-no-dt-emb\", \"pid\": \"705742\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:15.808Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11279.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:00:17.832Z\"}, \"exp_024b_cheetah_no_dt_emb_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-18T01:56:17.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:51:53.604Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T01:52:09.175571+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb 是 Cheetah CIVO 必要条件），加强因果三角的统计力度。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"metrics\": {\"baseline_pct\": 14.1, \"civo\": false, \"eval_return_final\": 77.3, \"eval_return_peak\": 129.6, \"gate_dt_2_frac\": 1, \"nve_peak\": 0.1, \"peak_step\": 15000}, \"notes\": \"No CIVO (NVE peak 0.10×, civo_alert=0 throughout). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. Gate locked at dt=2 (gate_dt_2_frac=1.0), eval 77.3 = 14% of baseline (548.3). Low performance expected: dt_embed_dim=0 removes temporal abstraction capability. Cheetah causal triangle seed 2 complete.\", \"parent\": \"exp_024_cheetah_no_dt_emb_s0\", \"pid\": \"706158\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-18T01:52:05.296Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/latest.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"pid\": \"706158\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:30.631Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11026.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:56:17.025Z\"}, \"exp_024_cheetah_no_dt_emb_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T20:35:13.253Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T20:34:13.657Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T20:35:16.021173+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T22:57:54.400584+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角（023a/b baseline健康 + 010b CIVO collapse + 本实验 no-emb 健康）。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:57:48.608Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL)\", \"model_name\": \"DreamerV3-no-dt-emb\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:21:27.867Z\"}, \"exp_021_full_sgs_cheetah_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T22:49:15.021Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T20:24:30.695Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T22:45:35.442053+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE 8.63×, collapse)。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"metrics\": {\"baseline_pct\": 38.7, \"civo\": true, \"civo_type\": \"transient_self_correcting\", \"eval_return_final\": 221.5, \"nve_peak\": 9.94, \"nve_peak_step\": \"45K\", \"nve_sustained_55K_105K\": 0.338, \"vs_010b\": \"221.5 vs 51.7 (4.3x better)\"}, \"notes\": \"P0 priority (D070 最重要数据缺口). 018_s2 完成后立即上 cuda:0. 排序: 021 先 → 008d_s1 后. Director 2026-05-16 确认.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"pid\": \"696201\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:45:32.093Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T19:28:08.484Z\", \"training_hours\": 3.29}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_021_full_sgs_cheetah_s1/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.32, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"pid\": \"696201\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T19:30:02.581Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11952.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T22:57:30.295Z\"}, \"exp_023a_cheetah_baseline_s0\": {\"completed_at\": \"2026-05-17T20:34:04.841Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:19.690Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T20:31:37.915652+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate). Establishes Cheetah-specific baseline for NVE normalization and cross-environment validation. Comparison target for 010b (Cheetah CIVO trigger, NVE 8.27×).\", \"metrics\": {\"civo\": false, \"eval_return_final\": 624.7, \"eval_return_peak\": 624.7, \"peak_step\": 205000}, \"notes\": \"Healthy baseline. Last-5 eval mean=554.4. 185K瞬态VE spike(0.906)触发警报但20K步内恢复(205K:624.7)，非CIVO。双seed baseline均值: last-5=548.3, peak=598.8。未接W&B。\", \"reproduce\": {\"finished_at\": \"2026-05-17T20:31:34.777Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023a_cheetah_baseline_s0/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023a_cheetah_baseline_s0.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.66, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023a_cheetah_baseline_s0.log\", \"model_name\": \"DreamerV3\", \"pid\": \"683708\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T14:54:17.553Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20387.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:57.147Z\"}, \"exp_010b_cheetah_civo_trigger\": {\"completed_at\": \"2026-05-16T16:16:00.478Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:04:55.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T16:11:35.101384+00:00\"}]}, \"hypothesis\": \"Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO (NVE>1.5x)。若成立→回应 reviewer \\\"single environment\\\" concern。\", \"metrics\": {\"civo\": true, \"eval_return_final\": 51.7, \"eval_return_peak\": 321.9, \"nve_peak\": 8.27, \"nve_peak_step\": 65000, \"peak_step\": 35000}, \"parent\": \"exp_010a_cheetah_baseline_s1\", \"reproduce\": {\"finished_at\": \"2026-05-16T16:11:32.766Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger/latest.pt\", \"checkpoint_source\": \"N/A (training from scratch, parent is baseline reference)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dm_control cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL, not eval experiment)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010b_cheetah_civo_trigger.log\", \"model_name\": \"DreamerV3+dt_emb(trained)+subsample+H8\", \"pid\": \"585826\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:05:10.473Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11450.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:38.129Z\"}, \"exp_023b_cheetah_baseline_s1\": {\"completed_at\": \"2026-05-17T19:29:52.643Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:21.197Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T19:25:39.255677+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate), seed=1. Second seed for Cheetah baseline to establish robust NVE normalization across seeds.\", \"metrics\": {\"civo\": false, \"eval_return_final\": 520.3, \"eval_return_peak\": 572.9, \"peak_step\": 195000, \"ve_ratio_range\": \"0.5-0.7\"}, \"notes\": \"Healthy baseline. Last-5 eval mean=542.2 (for NVE normalization). 125K后进入500-573区间震荡，无collapse。待023a完成后取双seed均值作为Cheetah baseline。未接W&B，数据在本地logdir。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:25:34.295Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023b_cheetah_baseline_s1/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023b_cheetah_baseline_s1.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.5, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023b_cheetah_baseline_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"680126\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T13:59:45.409Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19807.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:46.627Z\"}, \"exp_019b_pickcube_civo_trigger\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019b_pickcube_civo_trigger/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:35:47.561Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:23:51.568Z\", \"error_summary\": \"KeyError in dreamer.py:421 — configs[\\\"maniskill\\\"] not found. Config block missing from dreamer.py.\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T03:35:50.727034+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T14:49:42.379952+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-17 04:01: Registry shows DONE(failed) from first attempt (KeyError transient). Actual state: RUNNING (PID 646809, step 8400+, started 11:39 UTC). Cron monitoring via submit_on_allocated tmux session. Will need manual status correction when cron detects completion.\"}}, \"failure_reason\": \"Traceback → Traceback (most recent call last): File \\\"/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py\\\", line 421, in &lt;module> recursive_update(defaults, configs[name]) ~~~~~~~^^^^^^ KeyError: 'maniskill'\", \"gpu\": \"cuda:0\", \"hypothesis\": \"PickCube-v1 CIVO trigger — trained dt_emb, subsample ON, dt=2 imagination, H=8. 预期触发 CIVO（trained dt_emb → NVE>1.5x → collapse），验证 CIVO 在 manipulation 环境是否成立\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019b_pickcube_civo_trigger.log\", \"metrics\": {\"baseline_eval_final\": 58.56, \"baseline_ratio\": 0.455, \"eval_return_final\": 26.64, \"eval_return_peak\": 26.9, \"eval_return_peak_step\": 132500, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"nve_final\": 0.065, \"nve_peak\": 3.78, \"nve_peak_step\": 52500, \"pattern\": \"transient_civo_then_value_collapse\", \"total_steps\": 200000, \"value_baseline_final\": 144.57, \"value_mean_final\": 4.26}, \"notes\": \"Cross-env CIVO confirmation + detector TN. Raw V/E peak=5.66 @52.5K (NVE=3.78× vs baseline). Transient CIVO: onset ~22.5K → peak 52.5K → deflation → eval partial recovery. Detector correctly doesn't trigger (oscillating V/E, max streak=2 < threshold=3). Eval final 26.64 vs baseline 58.56 = 45.5%. Value permanently collapsed (4.26 vs baseline 144.57). PickCube pattern: acute crisis + permanent damage, vs Walker sustained escalation.\", \"parent\": \"exp_019a_v2_pickcube_baseline\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 1 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_019b_pickcube_civo_trigger\\\"\", \"finished_at\": \"2026-05-17T14:49:39.328Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T03:25:03.091Z\", \"training_hours\": 11.41}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_ID=0 bash scripts/exp_019b_pickcube_civo_trigger.sh\", \"data_count\": \"online\", \"data_path\": \"maniskill_PickCube-v1 (state-based, online RL)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu_id\": \"cuda:0\", \"model_name\": \"DreamerV3 + trained dt_emb + gate (maniskill_state config)\", \"pid\": 649577, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T15:20:38.182Z\"}, \"exp_022b_no_curriculum\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022b_no_curriculum/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T14:01:23.413Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:49:08.181Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T13:56:29.726988+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) + learned gate WITHOUT curriculum (phase1=0, phase2=0, gate fully unlocked from step 0). Tests whether frozen dt_emb prevents CIVO (NVE < 1.5×) while allowing the gate to learn meaningful temporal abstraction (gate_dt_1_frac < 1.0). exp_022 was inconclusive because curriculum locked gate for the entire run; this rerun removes that confound.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"metrics\": {\"civo_alert_max\": 0, \"eval_return_105K\": 300.7, \"gate_dt_1_frac_105K\": 0.145, \"gate_dt_mean_105K\": 3.41, \"gate_entropy_ratio_105K\": 0.912, \"gate_near_uniform\": true, \"nve_peak\": 1.22, \"ve_ratio_105K\": 0.075, \"ve_ratio_peak\": 0.218}, \"notes\": \"Frozen dt_emb (random init, no gradients) successfully prevents CIVO: ve_ratio peaked 0.218 (NVE≈1.22×), civo_alert=0 throughout. Confirms C2 (trained dt_emb is necessary for CIVO). Gate converges to near-uniform distribution (entropy_ratio=0.912, no temporal coherence), eval_return=300.7 (32.8% of baseline@105K=915.7). Frozen random dt_emb is sufficient CIVO fix but insufficient for meaningful temporal abstraction — multi-rate imagination's inherent performance limitation.\", \"parent\": \"exp_022_untrained_dt_emb_learned_gate\", \"pid\": \"670554\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"finished_at\": \"2026-05-17T13:56:27.483Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.16, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"pid\": \"670554\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T10:51:56.898Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11366.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:20:12.115Z\"}, \"exp_022_untrained_dt_emb_learned_gate\": {\"completed_at\": \"2026-05-17T07:44:38.596Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T04:16:57.150Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T07:44:42.334281+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T10:47:17.307752+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Config error: used --configs dmc_vision (CNN+image, wrong modality) instead of dmc_proprio, and --compile True (torch.compile inductor crash). Killed and resubmitting with correct config.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) prevents CIVO by blocking the trained-embedding-driven value overestimation feedback loop, while the learned gate (Gumbel-softmax, receives gradients) retains adaptive horizon selection capability. If successful, this decouples temporal abstraction benefits from CIVO vulnerability.\", \"metrics\": {\"civo_alert\": 0, \"civo_ve_ratio_105K\": 0.4, \"eval_return_105K\": 189.1, \"eval_return_65K\": 493.1, \"eval_return_75K\": 573.8, \"final_eval_return\": 189.1, \"gate_collapsed\": true, \"gate_dt_1_frac\": 1, \"gate_entropy\": 0, \"peak_eval_return\": 573.8, \"train_return_112K\": 91.8}, \"notes\": \"INCONCLUSIVE: Gate never activated due to curriculum misconfiguration. phase1=50000 × action_repeat=2 = 100K logger steps, experiment only 105K total. gate_scale reached only 0.006, gate locked at dt=1 entire run. eval_return: 75K=573.8 → 105K=189.1 (collapsed without gate involvement). Rerun as exp_022b with curriculum disabled.\", \"parent\": \"exp_008f_s3_no_dt_embed_walker + exp_005_gate_arch (combines safe dt_emb from 008f with gate architecture from 005 series)\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:47:12.534Z\"}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022_untrained_dt_emb_learned_gate/checkpoint.ckpt\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --imag_horizon 8 --logdir ./logdir/exp_022_untrained_dt_emb_learned_gate\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, proprio obs)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022_untrained_dt_emb_learned_gate.log\", \"model_name\": \"DreamerV3 + frozen dt_emb (d=32) + learned gate (Gumbel-softmax)\", \"pid\": 661595, \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T07:47:20.391Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10901.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:56:34.274Z\"}, \"exp_019a_v2_pickcube_baseline\": {\"completed_at\": \"2026-05-16T21:07:12.193Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T20:12:22.372Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\"}}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Vanilla DreamerV3 on ManiSkill3 PickCube establishes a cross-environment baseline; if stable, subsequent CIVO trigger experiment (019b) can test whether CIVO generalizes beyond DMC Walker Walk.\", \"metrics\": {\"eval_return_final\": 69.43, \"eval_return_peak\": 69.7, \"eval_return_peak_step\": 162500, \"steps_completed\": 200248, \"value_mean_final\": 143.4, \"ve_ratio_final\": 2.07, \"ve_ratio_range\": \"1.05-3.56\"}, \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\", \"parent\": \"exp_001_baseline\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline/checkpoint.ckpt\", \"checkpoint_source\": \"auto-resume from logdir\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled False --seed 1 --steps 200000 --compile False --device cuda:1 --logdir ./logdir/exp_019a_v2_pickcube_baseline\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill3 PickCube-v1 (online RL)\", \"eval_data\": \"N/A - training experiment\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline\", \"model_name\": \"DreamerV3-S\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:44:41.396Z\"}, \"exp_007_fixed_dt4\": {\"account\": \"root\", \"checkpoint_path\": \"N/A - killed, dt=4 confirmed too coarse for locomotion (D013)\", \"completed_at\": \"2026-05-13T22:32:00.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T22:15:44.218Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T22:32:01.413690+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\"}}, \"failure_reason\": \"dt=4 confirmed too coarse for locomotion: eval_return 127@35K vs baseline 389 (-67.4%). model_loss comparable to baseline — RSSM can learn 4-step dynamics, but action temporal resolution too coarse for Walker Walk. Confirms dt sweet spot ∈ {1,2}. See D013.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。\", \"metrics\": {\"baseline_45K\": 443, \"eval_return_15K\": 129.6, \"eval_return_25K\": 176.9, \"eval_return_35K\": 126.7, \"eval_return_45K\": 144.41, \"eval_return_55K\": 152.49, \"eval_return_5K\": 31, \"model_loss_15K\": 6.337, \"model_loss_25K\": 5.089, \"model_loss_35K\": 4.755, \"model_loss_5K\": 17.927, \"peak_return\": 176.9, \"peak_step\": \"25K\", \"step\": 48000, \"trend\": \"peak 176.9@25K, low plateau ~127-152; value extremely suppressed (v/e 6-13%), NOT delusional critic but severe learning failure\", \"value_eval_ratio_45K\": 0.126, \"value_eval_ratio_55K\": 0.061, \"value_mean_45K\": 18.26, \"value_mean_55K\": 9.28, \"vs_baseline_45K\": \"-67.4%\"}, \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\", \"parent\": \"exp_006_fixed_dt2\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"finished_at\": \"2026-05-13T22:32:00.443Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v2_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt4_v2_s1\", \"model_name\": \"DreamerV3+FixedDt4 (gate_fixed_dt=4, no learned gate, init_dt fix applied)\", \"pid\": \"90354\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.869Z\"}, \"exp_008c_no_subsample_dt2_h8\": {\"completed_at\": \"2026-05-14T04:09:46.829Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T01:33:31.413Z\", \"hypothesis\": \"隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。\", \"metrics\": {\"actor_loss_55K\": -0.082, \"actor_loss_65K\": -0.053, \"baseline_65K\": 616, \"data_source_35K\": \"from training logs metrics.jsonl\", \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.55, \"eval_return_55K\": 241.87, \"eval_return_65K\": 240.86, \"step\": 68000, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_35K\": 0.218, \"value_eval_ratio_55K\": 0.291, \"value_eval_ratio_65K\": 0.328, \"value_mean_35K\": 40.43, \"value_mean_55K\": 70.32, \"value_mean_65K\": 78.96, \"verdict_65K\": \"PLATEAU\", \"vs_baseline_65K\": \"-60.9%\"}, \"parent\": \"exp_006_fixed_dt2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008c_fixed_dt2_no_subsample_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.53, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=1, imag_horizon=8)\", \"pid\": \"107021\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:47.540Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9119.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.359Z\"}, \"exp_003_event_gated_v2\": {\"completed_at\": \"2026-05-13T09:58:31.673Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T04:52:22.660Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T09:58:32.493437+00:00\"}]}, \"failure_reason\": \"Return 崩塌至 baseline 13%。根因：_imagine 中 gate dt 无约束（输出 dt∈{1,...,8}），而 subsample curriculum 限制训练数据 dt≤effective_max_dt。RSSM 对未训练的大 dt 预测为噪声，progressive poisoning 导致 actor/critic 不可恢复。需修复 dt clipping + logits masking 后从头训练。\", \"metrics\": {\"eval_return_105K\": 92.3, \"eval_return_115K\": 118.7, \"fps\": 6.52, \"gate_dt_1_frac_116K\": 0.218, \"gate_dt_mean_116K\": 2.67, \"gate_dt_std_116K\": 1.46, \"gate_empirical_entropy_116K\": 1.655, \"gate_entropy_ratio_116K\": 0.796, \"gate_scale_116K\": 0.61, \"mvp_C1_return\": \"FAIL (0.13)\", \"mvp_C2_entropy\": \"PASS (1.655)\", \"mvp_C3_heff\": \"PASS (2.667x)\", \"mvp_C4_structure\": \"PASS (autocorr=0.652)\", \"return_ratio_105K\": 0.1, \"return_ratio_115K\": 0.13, \"step\": 120000}, \"parent\": \"exp_001_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-13T09:58:31.205Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"logdir/event_gated_s1_v2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1_v2 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Subsample curriculum prevents early destabilization while event gate learns meaningful variable-rate stepping\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v2 (final fix: env step sync + threshold 25K/75K)\", \"pid\": 27009, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:35.459Z\"}, \"exp_004_event_gated_v3\": {\"completed_at\": \"2026-05-13T15:23:26.384Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T10:05:16.227Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:27.393422+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_15K\": 153.86, \"fps\": 8.1, \"gate_dt_mean_15K\": 1, \"gate_scale_15K\": 0, \"step\": 20000}}}, \"failure_reason\": \"gate_loss 爆炸 bug：compute_gate_targets 使用 gate_max_dt=8 生成 target 分布但 logits masking 使用 effective_max_dt，cross-entropy loss ≈ 3e8。eval_return@125K=352 vs baseline@335K=942，ratio=0.37。第三次 train/imagine distribution mismatch。\", \"hypothesis\": \"修复 imagination dt 约束后（logits masking + clamp safety net），event gate 在 train/imagine 分布同步条件下能产生有意义的 variable-rate stepping 且 return ≥ 80% baseline\", \"parent\": \"exp_003_event_gated_v2\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A - killed due to gate_loss explosion bug\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v4_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.19, \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v4_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v3 (dt clipping + logits masking + dt alignment fix)\", \"pid\": 36645, \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T10:12:04.157Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:34.482Z\"}, \"exp_005_event_gated_v4\": {\"checkpoint_path\": \"N/A - killed due to structural failure of hard Gumbel gate\", \"completed_at\": \"2026-05-13T22:15:21.359Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T16:08:06.061Z\", \"failure_reason\": \"Hard Gumbel gate 结构性失败。3轮 bug 修复后仍崩塌：eval_return 峰值 541.18@55K → 持续下降 → 98.84@145K（baseline 同期 950.9）。Gate 机制有效（entropy/H_eff/structure 全 PASS），但 hard categorical gate + variable-rate imagination 与 actor-critic 优化存在结构性冲突。gate_scale>0.5 后 return 不可恢复。\", \"hypothesis\": \"Event-gated adaptive horizon (learned gate activation for dt selection) improves sample efficiency over fixed-horizon DreamerV3 by dynamically extending imagination when beneficial.\", \"latest_metrics\": {\"alert\": \"return_declining_at_phase2_onset\", \"baseline_at_65K\": 615.9, \"checked_at\": \"2026-05-13\", \"eval_return\": 465.67, \"eval_return_trajectory\": {\"15K\": 153.9, \"25K\": 254.2, \"35K\": 290.8, \"45K\": 443, \"55K\": 541.2, \"5K\": 31, \"65K\": 465.7}, \"fps\": 6.69, \"gap_vs_baseline\": -150.2, \"gate_dt_1_frac\": 0.965, \"gate_dt_2_frac\": 0.035, \"gate_dt_mean\": 1.035, \"gate_dt_std\": 0.036, \"gate_empirical_entropy\": 0.0499, \"gate_entropy_bonus\": 0.0865, \"gate_entropy_ratio\": 0.072, \"gate_loss\": 0.00663, \"gate_scale\": 0.10004, \"phase2_status\": \"gate刚进入phase2 (gate_scale=0.1), dt=1占比96.5%, gate几乎未激活。eval_return在55K→65K出现14%下降(541→466), 与phase2启动时机吻合, 类似exp_003崩塌前兆。但baseline同期也有小幅回调(626→616, -1.6%), 且gate尚未真正激活, 需继续观察75K数据确认是正常波动还是collapse。\", \"pid\": 51721, \"prev_eval_return\": 541.18, \"process_status\": \"running\", \"step\": 65000, \"train_return_latest\": 569.8, \"train_return_range\": [535.4, 602.1], \"uptime\": \"2h31m\"}, \"metrics\": {\"baseline_at_145K\": \"~950\", \"eval_return_105K\": 276.08, \"eval_return_145K\": 98.84, \"eval_return_15K\": 153.9, \"eval_return_35K\": 290.8, \"eval_return_55K\": 541.18, \"eval_return_5K\": 31, \"eval_return_65K\": 465.67, \"eval_return_85K\": 212.34, \"final_return\": 98.84, \"fps\": 6.69, \"gate_dt_mean_105K\": 2.054, \"gate_dt_std_105K\": 0.907, \"gate_entropy_105K\": 1.255, \"gate_scale_105K\": 0.5, \"note\": \"85K/105K metrics corrected from 319.3/337.8 to 212.34/276.08\", \"peak_return\": 541.18, \"peak_step\": \"55K\", \"return_ratio_final\": 0.104, \"step\": 145000}, \"parent\": \"exp_004_event_gated_v3\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 6.12, \"hypothesis\": \"修复 gate_target/masking 维度不匹配 + effective_max_dt 单一来源架构 + 全量审计后，event gate return >= 80% baseline\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_005_event_gated_v4.log\", \"model_name\": \"DreamerV3+EventGate_v4\", \"pid\": \"51721\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T16:08:11.913Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 22029.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:33.514Z\"}, \"exp_008d_civo_trigger_s3\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s3/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:24:26.004Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T00:25:47.784Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T03:18:40.430236+00:00\"}]}, \"hypothesis\": \"Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming CIVO onset is systematic across seeds regardless of replay sampling sequence (seed bug fix verification).\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"metrics\": {\"baseline_eval_105K\": 915.67, \"collapse_onset_step\": 95000, \"collapse_type\": \"late-onset\", \"eval_return_final\": 267.6, \"eval_return_final_step\": 105000, \"eval_return_peak\": 451.7, \"eval_return_peak_step\": 95000, \"nve_final\": 1.53, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.5, \"nve_peak\": 1.53, \"nve_peak_step\": 105000, \"nve_sustained_45K_55K\": true, \"total_steps\": 112000, \"train_return_final_avg\": 138, \"train_return_final_range\": \"82-214\", \"value_mean_final\": 268.4, \"vs_baseline_105K\": \"-70.8%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:18:37.221Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint, new logdir)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 3 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s3\\\"\", \"data_count\": 105000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"635744\", \"seed\": 3, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T00:25:59.245Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10706.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:24:26.004Z\"}, \"exp_018v2_full_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018v2_full_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-16T17:24:44.481Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T13:42:15.786Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T17:17:46.576638+00:00\"}]}, \"hypothesis\": \"Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways creating dt-specific representations, thereby preventing CIVO onset and collapse.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"metrics\": {\"civo_reduction_pct\": 79, \"eval_return_final\": 448.3, \"eval_return_final_step\": 105000, \"eval_return_peak\": 499.6, \"eval_return_peak_step\": 75000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"late_collapse_detected\": true, \"late_collapse_step\": 112000, \"nve_final\": 1.34, \"nve_mean_45k_105k\": 1.23, \"nve_peak\": 1.66, \"nve_peak_step\": 95000, \"total_steps\": 112000, \"total_updates\": 25099, \"value_loss_final\": 0.6}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-16T17:17:44.050Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (training from scratch, parent is predecessor not checkpoint source)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 1 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018v2_full_sgs_walker_s1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, no static dataset)\", \"eval_data\": \"dmc_walker_walk eval episodes (online)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.49, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"589564\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:55:10.231Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12574.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:18.423Z\"}, \"exp_018_full_sgs_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_s2/checkpoint.pt\", \"completed_at\": \"2026-05-16T23:47:49.458Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T19:33:26.266Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mechanism for deployment.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"notes\": \"CIVO collapse confirmed: eval 40.8@105K (from peak ~488@75K). NVE peaked 1.66× at 95K (35K+ window). Full-SGS did NOT prevent collapse in seed 2 — contradicts 018v2 (seed 1) which avoided collapse. This invalidates SGS_full as a reliable CIVO prevention method. Key difference from 018v2: 018_s2 collapsed while 018v2 sustained. n=2 for SGS_full now shows collapse_rate=0.5.\", \"parent\": \"exp_018v2_full_sgs_walker_s1\", \"pid\": \"612876\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.04, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"pid\": \"612876\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T19:45:40.838Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 14528.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:37.385Z\"}, \"exp_008f_no_dt_embed_subsample_on_h8\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8/latest.pt\", \"completed_at\": \"2026-05-14T09:32:53.461Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:51:27.592Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:30:42.170428+00:00\"}]}, \"hypothesis\": \"Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as the necessary causal factor for CIVO.\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"trained dt_embedding → value overestimation → actor exploitation → collapse. Without dt_embedding, value self-corrects.\", \"current_step\": 105000, \"eval_checkpoints\": {\"105K\": {\"eval_return\": 503, \"normalized_ve\": 0.3, \"value_mean\": 98.2}, \"15K\": {\"eval_return\": 182.03, \"value_mean\": 2.989, \"ve_ratio\": 0.01642}, \"25K\": {\"baseline_ve\": 0.087, \"eval_return\": 196.78, \"normalized_ve\": 1.02, \"value_mean\": 17.507, \"ve_ratio\": 0.089}, \"35K\": {\"baseline_ve\": 0.241, \"eval_return\": 206.67, \"normalized_ve\": 0.73, \"value_mean\": 36.279, \"ve_ratio\": 0.176}, \"45K\": {\"baseline_ve\": 0.331, \"eval_return\": 194.08, \"normalized_ve\": 0.83, \"value_mean\": 53.429, \"ve_ratio\": 0.275}, \"55K\": {\"baseline_ve\": 0.404, \"eval_return\": 173.45, \"normalized_ve\": 0.97, \"value_mean\": 67.899, \"ve_ratio\": 0.391}, \"5K\": {\"eval_return\": 30.49, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, \"65K\": {\"eval_return\": 375, \"normalized_ve\": 0.37}, \"75K\": {\"eval_return\": 324, \"normalized_ve\": 0.42}, \"85K\": {\"eval_return\": 246, \"normalized_ve\": 0.65, \"value_mean\": 111.8}, \"95K\": {\"eval_return\": 319, \"normalized_ve\": 0.54}}, \"last_updated\": \"2026-05-14T09:50:00\", \"target_steps\": 105000, \"trend\": \"Zigzag recovery with high variance: eval 207→194→173@55K→375→324→246→319→503@105K. NOT a clean V-shape — high inter-eval variance throughout. Value self-corrected: peaked 111.8@85K then declined to 98.2@105K. Normalized v/e: 0.97x@55K→0.37x@65K→0.65x@85K→0.30x@105K. Key contrast with 008d: value only accelerates (69.3%@45K) vs 008f value self-corrects.\", \"verdict\": \"SUCCESS - zigzag recovery to 503@105K, normalized v/e=0.30x, C2 confirmed\", \"vs_baseline_105K\": \"-45.1%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:30:41.254Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_embed_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.68, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"pid\": \"127761\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:51:55.020Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16858.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:33.517Z\"}, \"exp_016d_sgs_walker_s1\": {\"completed_at\": \"2026-05-15T19:35:10.508Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:29:41.130Z\", \"failure_reason\": \"Same hang as 016c — SummaryWriter.flush() deadlock after add_video with moviepy 2.x. try/except insufficient because flush() blocks on incomplete async video encode. Fix: Logger.video() → no-op.\", \"hypothesis\": \"Selective Gradient Stopping (reward_dt_emb_detach) blocks reward-gradient pathway to dt_emb, preventing CIVO-inducing co-adaptation while preserving task performance.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"第5次启动。两项修复生效：MUJOCO_EGL_DEVICE_ID=1 + logger.video注释。旧PID 526153已自行退出。\", \"pid\": 526939, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:28.152Z\"}, \"exp_001_baseline\": {\"completed_at\": \"2026-05-13T15:23:24.593Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T02:09:53.875Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:25.663340+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:47:19.804301+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_205K\": 907.1, \"eval_return_215K\": 919.8, \"fps\": 8.3, \"step\": 245000, \"train_return_244K\": \"935-976\"}}}, \"failure_reason\": \"误报：cron 检测到进程退出但实际是正常完成（512K步）。已核实 checkpoint 229MB 有效。\", \"hypothesis\": \"Vanilla DreamerV3 on Walker Walk converges to stable high-return policy (>900) within 500K steps, establishing the performance ceiling for all gated variants.\", \"latest_metrics\": {\"checked_at\": \"2026-05-13\", \"eta_hours\": 1.8, \"eval_return\": 953.37, \"eval_step\": 445000, \"fps\": 7.29, \"pid\": 9409, \"prev_eval_return\": 964.96, \"process_status\": \"running\", \"step\": 452000, \"steps_remaining\": 48000, \"train_return_latest\": 958.07, \"train_return_range\": [917, 985.8], \"uptime\": \"16h35m\"}, \"metrics\": {\"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_last10_mean\": 950.9, \"eval_return_peak\": 970.41, \"eval_return_peak_step\": 505000, \"eval_trajectory\": {\"105K\": 915.67, \"115K\": 919.81, \"125K\": 921.37, \"135K\": 900, \"145K\": 932.16, \"155K\": 933.34, \"15K\": 206.61, \"165K\": 907.98, \"175K\": 918.87, \"185K\": 954.69, \"195K\": 936.09, \"205K\": 949.24, \"215K\": 913.4, \"225K\": 962.44, \"235K\": 937.24, \"245K\": 934.42, \"255K\": 948.45, \"25K\": 395.27, \"265K\": 925.09, \"275K\": 931.51, \"285K\": 925.75, \"295K\": 936.3, \"305K\": 939.33, \"315K\": 948.42, \"325K\": 967.75, \"335K\": 942.41, \"345K\": 969.83, \"355K\": 941.11, \"35K\": 388.47, \"365K\": 935.76, \"375K\": 918.24, \"385K\": 937.98, \"395K\": 955.38, \"405K\": 937.83, \"415K\": 948.99, \"425K\": 954.64, \"435K\": 964.96, \"445K\": 953.37, \"455K\": 945.84, \"45K\": 513.77, \"465K\": 947.81, \"475K\": 947.66, \"485K\": 930.6, \"495K\": 944.73, \"505K\": 970.41, \"55K\": 625.73, \"5K\": 31.77, \"65K\": 615.86, \"75K\": 596.28, \"85K\": 713.93, \"95K\": 871.06}, \"final\": true, \"step\": 512000, \"value_eval_ratio_105K\": 0.656, \"value_eval_ratio_25K\": 0.087, \"value_eval_ratio_35K\": 0.241, \"value_eval_ratio_45K\": 0.331, \"value_eval_ratio_55K\": 0.404, \"value_eval_ratio_65K\": 0.563, \"value_eval_ratio_75K\": 0.719, \"value_eval_ratio_85K\": 0.701, \"value_eval_ratio_95K\": 0.632, \"value_eval_ratio_stable\": \"~69-72% from 135K+\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:47:18.966Z\"}, \"retry_count\": 1, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"hypothesis\": \"DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"pid\": 9409, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:24.099Z\"}, \"exp_008d_civo_trigger_s2\": {\"completed_at\": \"2026-05-17T00:24:10.180Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T19:32:16.790Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 bootstrap CI 闭合 trained_dt_emb condition (现有: seed 0 = 008d, seed 2 = 009b)。注意: 原名 s2 但实际需跑 seed=1 (避免与 009b seed=2 重复)。\", \"notes\": \"Killed by Director order: seed bug confirmed. --seed 1 was parsed incorrectly, producing bit-for-bit identical results to seed=0. PID 628482 killed. Will resubmit after seed bug fix with seed=3.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint loaded)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/event-gated-adaptive-horizon && python train.py --configs dmc_vision --task dmc_walker_walk --logdir ./logdir/008d_civo_trigger_s2 --seed 1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --steps 120000\", \"data_count\": 120000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.57, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s2.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"628477\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T22:49:55.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 5654.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T00:24:10.180Z\"}, \"exp_008f_s3_no_dt_embed_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_s3_no_dt_embed_walker/checkpoint.ckpt\", \"completed_at\": \"2026-05-16T20:09:51.135Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:04:28.878Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=2，需 ≥3）。预期 NVE<1.5×，无 CIVO。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"metrics\": {\"collapse\": false, \"eval_return_final\": 363.8, \"nve_peak\": \"< 1.5x\"}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"601233\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"pid\": \"601233\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T17:21:24.538Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10106.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:09:51.135Z\"}, \"exp_020_vanilla_dreamerv3_s2\": {\"completed_at\": \"2026-05-16T19:43:57.604Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:23:55.837Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T19:40:49.938571+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Vanilla DreamerV3 (no dt_emb, no subsample, no gate) seed 2 — Pathway B 控制实验：验证 008e_v3_s2 的 eval-driven collapse 是否需要 trained dt_emb 作为必要条件。如果 vanilla s2 稳定 → C6 成立 (trained dt_emb 是 Pathway B 必要条件)。如果也崩溃 → Pathway B 是 DreamerV3 inherent fragility。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"metrics\": {\"collapse\": false, \"comparison_with_parent\": {\"c6_confirmed\": true, \"delta\": \"vanilla stable (836.5) vs trained dt_emb collapsed (136.96)\", \"parent_collapsed\": true, \"parent_eval_105K\": 136.96, \"parent_id\": \"exp_008e_v3_walker_s2\", \"parent_nve_105K\": 3.78}, \"eval_trajectory\": [{\"eval_return\": 41.2, \"step\": 5000}, {\"eval_return\": 534.1, \"step\": 55000}, {\"eval_return\": 688.9, \"step\": 65000}, {\"eval_return\": 596.2, \"step\": 95000}, {\"eval_return\": 836.5, \"step\": 105000}], \"final_eval_return\": 836.5, \"final_value_mean\": 539.3, \"peak_eval_return\": 836.5, \"peak_eval_step\": 105000, \"train_return_range_108K\": \"511-808\", \"ve_ratio_105K\": 0.645}, \"notes\": \"Pathway B 控制实验 (D6)。vanilla config: dt_embed_dim=0, subsample OFF, H=15, seed=2, 105K steps, Walker Walk。排队等 010b 完成后在 cuda:0 提交。命令: dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 2 --compile True --device cuda:0 --imag_horizon 15\", \"parent\": \"exp_008e_v3_walker_s2\", \"pid\": \"596344\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-16T19:40:47.795Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"logdir/exp_020_vanilla_dreamerv3_s2/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"pid\": \"596344\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T16:45:55.371Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:43:57.604Z\"}, \"exp_019a_pickcube_baseline\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T13:43:00.745Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T03:23:50.639Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中的适用性\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"notes\": \"ManiSkill3 Phase 1. 排队等 cuda:1 (010a 完成后). --compile False --device cuda:1. maniskill_state config.\", \"pid\": \"586751\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T12:00:04.473Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (killed before completion)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.37, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"pid\": \"586751\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:20:56.230Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1324.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:43:00.745Z\"}, \"exp_018_full_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T12:43:09.226Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T23:30:39.991Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T12:40:17.132664+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerability is representation-level; if eliminated → obs decoder gradient is root cause.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_walker_s1.log\", \"metrics\": {\"eval_return_final\": 915.7, \"eval_return_final_step\": 105000, \"eval_return_peak\": 915.7, \"eval_return_peak_step\": 105000, \"nve_peak\": 0.72, \"nve_peak_step\": 75000, \"nve_sustained_avg\": 0.55, \"nve_sustained_max\": 0.72, \"total_steps\": 112000, \"train_return_final_avg\": 899.4, \"value_mean_final\": 601.1}, \"notes\": \"⚠️ INVALID: 训练命令缺失 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8。gate_enabled=false → dt_embedding 未创建 → full_sgs 是空操作 → 实际等同 vanilla baseline。所有基于此实验的 claim (CIVO elimination, gradient-level vulnerability) 需要 018v2 重新验证。\", \"parent\": \"exp_016e_sgs_walker_s1\", \"pid\": \"577467\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_018_full_sgs_walker_s1 --steps 105000 --full_sgs True --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T12:40:14.687Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T09:50:18.238Z\", \"training_hours\": 2.83}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:42:11.339Z\"}, \"exp_010a_cheetah_baseline_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/latest.pt\", \"completed_at\": \"2026-05-16T12:01:01.080Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:27.101Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T11:59:12.312213+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log\", \"metrics\": {\"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"final_step\": 524000, \"total_eval_episodes\": 52, \"train_return_last\": 716}, \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"pid\": \"536890\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T11:59:09.914Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T22:48:05.456Z\", \"training_hours\": 13.18}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:01:11.169Z\"}, \"exp_009d_baseline_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T12:10:01.788Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:55:00.039Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:10:04.203907+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:24:17.652463+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T09:48:44.475703+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 0 — 第三独立 baseline seed，建立 v/e 校准参考（plan_010）\", \"metrics\": {\"eval_return\": 927.6, \"eval_return_at_508K\": 927.6, \"eval_return_peak\": 950.96, \"eval_return_peak_step\": 398000, \"note\": \"COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K\", \"step\": 508000}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\", \"parent\": \"exp_001_baseline\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T09:48:42.388Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T12:06:19.592Z\", \"training_hours\": 21.71}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/checkpoint.ckpt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/metrics.jsonl\", \"model_name\": \"DreamerV3_baseline\", \"pid\": \"149703\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:50:34.506Z\"}, \"exp_017_subsample_off_trained_dt_emb\": {\"completed_at\": \"2026-05-16T04:46:30.361Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T10:44:24.756Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample OFF + dt=2 imagination + H=15 seed 1 — 2×2 消融矩阵: 隔离 subsample 训练数据的因果效应。与 008a (untrained dt_emb, subsample OFF) 唯一差异是 dt_emb trained vs untrained。如果 017 崩而 008a 不崩 → 确认 trained dt_emb 是 CIVO 根因，即使训练数据全为 dt=1（plan_017, C2）\", \"notes\": \"D044: 取消。008a 配置验证确认 017 与 008a 完全重复（trained dt_emb + subsample OFF + H=15 + seed 1）。008a 的\\\"untrained\\\"含义是\\\"dt_emb 存在但未接触 dt>1 数据\\\"，不是 frozen/absent。2×2 矩阵已由 008a/008d/008f/015b 闭合。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:46:30.361Z\"}, \"016e\": {\"completed_at\": \"2026-05-16T01:39:17.916Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T22:21:09.251Z\", \"notes\": \"重复条目，权威数据在 exp_016e_sgs_walker_s1 (DONE/negative)。此条目为 NVE 诊断过程中误创建的冗余记录。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:39:17.916Z\"}, \"exp_016e_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T22:31:16.457Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T19:35:20.242Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016）。第五次重试，修复 Logger.video() → no-op 彻底消除 SummaryWriter.add_video/flush 死锁\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/\", \"metrics\": {\"actor_loss_sign_flip_step\": 95000, \"civo_catastrophic_step\": 95000, \"civo_detected\": true, \"civo_nve_peak\": 10.42, \"civo_nve_peak_step\": 95000, \"civo_onset_step\": 85000, \"civo_severity\": \"catastrophic\", \"current_step\": 100000, \"data_source\": \"metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25\", \"deep_analysis\": {\"016e_vs_008d_entropy_comparison\": {\"15K\": {\"008d\": 0.481, \"016e\": 1.049, \"delta\": 0.568}, \"25K\": {\"008d\": -1.862, \"016e\": -1.554, \"delta\": 0.308}, \"35K\": {\"008d\": -3.465, \"016e\": -2.118, \"delta\": 1.347}, \"45K\": {\"008d\": -4.575, \"016e\": -3.455, \"delta\": 1.12}, \"55K\": {\"008d\": -4.879, \"016e\": -3.617, \"delta\": 1.262}, \"interpretation\": \"SGS preserves ~1.0-1.3 nats higher entropy through 35-55K, enabling better exploration\"}, \"016e_vs_008d_value_at_crash\": {\"008d\": {\"disconnect_ratio\": 1.67, \"eval_return\": 82.75, \"value_mean\": 137.88}, \"016e\": {\"disconnect_ratio\": 6.58, \"eval_return\": 31.73, \"value_mean\": 208.88}, \"interpretation\": \"016e value completely decoupled from reality; 008d still weakly correlated\"}, \"actor_loss_sign_flip\": {\"008d_min_actor_loss\": -0.073, \"008d_never_flipped\": true, \"016e_flip_step\": 95000, \"016e_flip_value\": 0.014, \"interpretation\": \"sign flip = value critic drives actor toward worse actions, triggering catastrophic collapse\"}, \"train_return_collapse_timeline\": {\"100K\": [109, 111, 102, 108], \"88K\": [140, 145, 116, 116], \"92K\": [50, 29, 34, 75], \"96K\": [86, 41, 50, 101], \"interpretation\": \"collapse visible in train_return by 92K; partial recovery by 100K but far below peak\"}}, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, {\"eval_return\": 140.3, \"step\": 15000, \"value_mean\": 3.1, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 141.75, \"nve\": 1.86, \"step\": 25000, \"value_mean\": 22.97, \"ve_ratio\": 0.162}, {\"baseline_ve\": 0.241, \"eval_return\": 173.01, \"nve\": 1.28, \"step\": 35000, \"value_mean\": 53.55, \"ve_ratio\": 0.309}, {\"baseline_ve\": 0.331, \"eval_return\": 184.03, \"nve\": 1.4, \"step\": 45000, \"value_mean\": 85.32, \"ve_ratio\": 0.464}, {\"baseline_ve\": 0.404, \"eval_return\": 153.79, \"nve\": 1.86, \"step\": 55000, \"value_mean\": 115.63, \"ve_ratio\": 0.752}, {\"baseline_ve\": 0.563, \"eval_return\": 324.3, \"nve\": 0.83, \"step\": 65000, \"value_mean\": 152.3, \"ve_ratio\": 0.469}, {\"baseline_ve\": 0.719, \"eval_return\": 326.67, \"nve\": 0.81, \"step\": 75000, \"value_mean\": 190.04, \"ve_ratio\": 0.582}, {\"baseline_ve\": 0.701, \"eval_return\": 256.21, \"nve\": 1.2, \"step\": 85000, \"value_mean\": 215.39, \"ve_ratio\": 0.841}, {\"baseline_ve\": 0.632, \"eval_return\": 31.73, \"nve\": 10.42, \"step\": 95000, \"value_mean\": 208.88, \"ve_ratio\": 6.583}], \"final_eval_return\": 31.73, \"final_eval_step\": 95000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 326.67, \"peak_eval_step\": 75000, \"reward_dt_emb_detach\": true, \"sgs_verdict\": \"SGS delays CIVO onset ~50K steps by preserving entropy, yields 2x higher peak (327 vs 167), but does NOT prevent collapse. Collapse is more severe (NVE 10.42x vs 4.12x) due to accumulated value overestimation. Root cause is value dynamics, not reward-head gradient contamination.\", \"target_steps\": 105000}, \"notes\": \"logdir 路径修正：实际数据在 logdir/exp_016e_sgs_walker_s1（非 spec 中的 exp_016d）。SGS 崩溃确认@95K: eval 31.7, ve_ratio=6.59x, NVE=10.42x。\\n\\n**⚠️ 关键发现（Full-SGS 梯度验证）：reward loss 对 dt_emb.weight 的梯度贡献为 0。016e 的 reward_dt_emb_detach 实际上是 no-op——完全无效干预。** 真正的 dt_emb 梯度来源是 decoder heads（orientations=1.11, velocity=0.90, height=0.76, cont=0.27）。016e 与 008d 的差异（onset 延迟、更高峰值）应归因于随机变异或其他实验条件差异，不是 SGS 干预效果。\\n\\nFull-SGS（detach 所有 non-KL head 梯度）移除 93% dt_emb 梯度（1.624→0.119），是真正的测试。\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016e_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"logdir\": \"logdir/exp_016e_sgs_walker_s1\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"logdir 修正: 实际数据在 exp_016e（非 016d）\", \"pid\": 527392, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:30:11.433Z\"}, \"exp_016c_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:26:05.863Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:12:09.799Z\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer). EGL fix confirmed working: eval at step 5000 completed successfully (eval_return=31.0). OOM occurred during training loop startup after eval. Likely system RAM OOM (replay buffer + model + eval concurrent memory peak).\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心。GPU 1 清理+验证通过后重启（plan_016）\", \"metrics\": {\"egl_fix_verified\": true, \"eval_return_5K\": 31, \"step\": 5000}, \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"GPU 1 cleanup + CUDA/dm_control verification passed. logdir shared with 016b (fresh start).\", \"pid\": \"524244\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:24.104Z\"}, \"exp_009h_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:08:12.013Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:03:10.534Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:08:15.731787+00:00\"}]}, \"failure_reason\": \"误杀: Director 基于 Reviewer 错误诊断下令 kill（认为 zombie PID 522009 导致 eval deadlock），但日志证明 EGL fix (MUJOCO_EGL_DEVICE_ID=1) 已生效，eval 正常运行中 (iter=500, t=95.9s)。EGL fix 确认有效。\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009g（EGL device mismatch 修复：+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009h_008f_walker_s0.log\", \"notes\": \"日志显示进程正常完成 prefill → 到达 step 5000 → eval 正在运行（500 iter, 96s, 正常产出 debug 行）→ 被外部 SIGHUP (EXIT_CODE=129) 终止。非渲染死锁，非 OOM。诊断 Worker 排查外部终止原因中。009f/009g/009h 连续 3 次失败，分别因 seed 重复、EGL mismatch、外部 SIGHUP。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"522450\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T19:08:09.836Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"note\": \"EGL fix: MUJOCO_EGL_DEVICE_ID=1 to match physical GPU 1. 008f series seeds: 1(008f), 2(009c), 0(009h)\", \"pid\": \"522450\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:18:24.685Z\"}, \"exp_016b_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:10:52.235Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:08:00.667Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:10:53.928926+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016, 论文 method section 核心）。重跑 016_sgs，修复 EGL device mismatch（+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016b_sgs_walker_s1.log\", \"notes\": \"Restarted after GPU 1 cleanup. Old PID 523536 killed during GPU reset attempt. New PID 524244. GPU 1 diagnostics: no ECC/Xid errors, reset not supported (AutoDL container) but cleanup successful. CUDA + dm_control verification passed in 3s.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 524244, \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T19:10:51.013Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"Rerun of 016_sgs with EGL fix (MUJOCO_EGL_DEVICE_ID=1). Original 016 failed due to EGL device mismatch, not SGS code issue.\", \"pid\": \"523536\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:11:46.897Z\"}, \"exp_009g_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:59:55.315Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T18:54:23.385Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:59:59.820061+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM). Root cause: MUJOCO_GL=egl defaults to EGL device 0 while CUDA_VISIBLE_DEVICES=1 binds CUDA to GPU 1, causing cross-GPU context conflict and eval deadlock at step 5000.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009f（seed=1 与 parent 008f 重复）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009g_008f_walker_s0.log\", \"notes\": \"Hung at first eval (step 5000) due to osmesa rendering deadlock in dm_control render_executor thread. Same root cause as exp_016. Fixed by switching MUJOCO_GL to egl in dreamer.py.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"517413\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:59:53.840Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"note\": \"Replaces exp_009f which had seed=1 duplicating parent 008f. 008f series seeds: 1(008f), 2(009c), 0(009g)\", \"pid\": \"517413\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:03:53.591Z\"}, \"exp_009f_008f_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:46:03.293Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:15.806Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:46:05.155411+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:52:15.790170+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Seed duplication: 009f used seed=1 same as parent 008f, producing deterministic repeat (prefill returns identical). Killed by Director order.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 1 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"516110\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:52:12.322Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T18:44:58.143Z\", \"training_hours\": 0.12}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.07, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"pid\": \"516110\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:47:48.525Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 265.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:54:04.806Z\"}, \"exp_016_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:43:52.455Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:30:32.999Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:43:57.605618+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路。预期：不崩溃，nve < 1.5x baseline；imagination dt=2/dt=1 reward ratio 从 008d 的 2.90x 大幅下降（plan_016, 论文 method section 核心）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"notes\": \"Director 调整优先级：017 先于 016。cuda:1 释放后先跑 017，017 完成后再跑 016。SGS 诊断 bug 已修复（models.py L388-417 删除），dry-run 通过。[2026-05-15 18:43] PID 514422 hung: GPU 1 利用率 0%, 显存 794 MiB, metrics.jsonl 停 step=5000 持续 2.5h+。已 kill，Worker 诊断根因+修复+重启中。\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"514417\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T18:43:51.025Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"pid\": \"514417\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:36:15.693Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 456.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:43:52.455Z\"}, \"exp_015b_frozen_dt_emb\": {\"completed_at\": \"2026-05-15T12:12:25.846Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T10:21:05.572Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T18:27:09.189680+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次提交。首次失败原因: --device cuda:1 但 CUDA_VISIBLE_DEVICES=1 后进程内只有 cuda:0。已修正为 --device cuda:0。PID 144831, 从头开始 (step=0)。预计 ~5h 完成 105K steps。\"}}, \"hypothesis\": \"Walker Walk frozen dt_emb + subsample ON + dt=2 imagination + H=8 seed 1 — 2×2 消融矩阵: 隔离 dt_emb 训练 vs 存在的因果效应。如果 freeze 后不崩 → 确认 CIVO 根因是 dt_emb 训练而非结构存在（plan_015B, D041）\", \"metrics\": {\"actor_entropy_105K\": -4.855, \"actor_loss_105K\": 0.000179, \"collapse_mechanism\": \"gradient_starvation_from_frozen_dt_emb\", \"data_source\": \"worker SSH final analysis 2026-05-15T18:30\", \"eval_return_105K\": 204.2, \"eval_return_15K\": 167.9, \"eval_return_25K\": 171.8, \"eval_return_35K\": 201.6, \"eval_return_45K\": 122.3, \"eval_return_55K\": 105.8, \"eval_return_5K\": 31, \"eval_return_65K\": 160.3, \"eval_return_75K\": 80, \"eval_return_85K\": 183.5, \"eval_return_95K\": 238.4, \"final_eval\": 204.2, \"final_step\": 112000, \"gate_dt_1_frac\": 0, \"gate_dt_mean\": 2, \"nve_105K\": 0.42, \"nve_85K\": 0.467, \"nve_95K\": 0.394, \"summary\": \"NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss→0 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence\", \"value_mean_105K\": 56.212, \"value_std_105K\": 13.818}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD + MUJOCO_GL=egl + --device cuda:0 (CUDA_VISIBLE_DEVICES=1 隔离)。cuda:1, seed=1, 105K steps ~5h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:27:07.138Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_015b_frozen_dt_emb --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_015b_frozen_dt_emb.log\", \"pid\": \"149991\", \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:38:42.380Z\"}, \"exp_008a_no_subsample_dt2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample/latest.pt\", \"completed_at\": \"2026-05-14T06:16:58.196Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:33:27.311Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T06:15:01.796655+00:00\"}]}, \"hypothesis\": \"隔离 subsample 效应：trained dt_emb (unexposed to dt>1 data due to subsample OFF) + subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。\", \"metrics\": {\"baseline_105K\": 915.67, \"baseline_55K\": 625.7, \"baseline_65K\": 616, \"data_source\": \"from training logs metrics.jsonl\", \"eval_return_105K\": 777.66, \"eval_return_35K\": 500.84, \"eval_return_45K\": 563.41, \"eval_return_55K\": 487.92, \"eval_return_65K\": 608, \"eval_return_75K\": 469.93, \"eval_return_85K\": 583.73, \"eval_return_95K\": 572.24, \"nan_count\": 0, \"normalized_ve_105K\": 0.59, \"normalized_ve_55K\": 0.93, \"normalized_ve_65K\": 0.66, \"normalized_ve_75K\": 0.75, \"normalized_ve_85K\": 0.68, \"normalized_ve_95K\": 0.79, \"step\": 112000, \"trend\": \"Two V-shaped recoveries: 501→563→488→608→470→584→572→778; v/e suppressed 38-54% (normalized 0.59-0.79x baseline); no collapse at 105K\", \"value_eval_ratio_105K\": 0.386, \"value_eval_ratio_55K\": 0.376, \"value_eval_ratio_65K\": 0.372, \"value_eval_ratio_75K\": 0.536, \"value_eval_ratio_85K\": 0.475, \"value_eval_ratio_95K\": 0.497, \"value_mean_105K\": 300.27, \"value_mean_55K\": 183.5, \"value_mean_65K\": 226.1, \"value_mean_75K\": 251.78, \"value_mean_85K\": 277.36, \"value_mean_95K\": 284.28, \"verdict_105K\": \"NEW_PEAK_V_RECOVERY\", \"verdict_65K\": \"RECOVERED_NEW_HIGH\", \"vs_baseline_105K\": \"-15.1%\", \"vs_baseline_65K\": \"-1.3%\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T06:15:00.119Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.65, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (gate_fixed_dt=2, gate_subsample_max_dt=1, H=15)\", \"pid\": \"106942\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:46.034Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16752.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:50:59.046Z\"}, \"exp_009d_baseline_walker_s1\": {\"completed_at\": \"2026-05-15T11:54:55.153Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:14.363Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 1 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"notes\": \"⚠️ seed=1 与 exp_001_baseline 相同，eval 轨迹确定性复现。不构成独立 seed。如需第三 baseline seed 应 kill 并用 --seed 0 或 --seed 3 重跑。待 Director 决策。\", \"parent\": \"exp_001_baseline\", \"pid\": 122271, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009d_baseline_walker_s1.log\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:35:00Z\", \"wall_clock_seconds\": 19195.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:54:55.153Z\"}, \"exp_009a_baseline_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:33:12.892Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:24.247Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/\", \"metrics\": {\"cross_seed_ve_stable\": \"seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72\", \"eval_return_peak\": 966.94, \"eval_return_peak_step\": 395000, \"eval_trajectory\": [{\"eval_return\": 41.21, \"step\": 5000}, {\"eval_return\": 106.01, \"step\": 15000}, {\"eval_return\": 325.33, \"step\": 25000}, {\"eval_return\": 354.49, \"step\": 35000}, {\"eval_return\": 498.01, \"step\": 45000}, {\"eval_return\": 534.13, \"step\": 55000}, {\"eval_return\": 688.87, \"step\": 65000}, {\"eval_return\": 656.85, \"step\": 75000}, {\"eval_return\": 618.73, \"step\": 85000}, {\"eval_return\": 596.24, \"step\": 95000}, {\"eval_return\": 836.51, \"step\": 105000}, {\"eval_return\": 804.79, \"step\": 115000}, {\"eval_return\": 865.48, \"step\": 125000}, {\"eval_return\": 876.08, \"step\": 135000}, {\"eval_return\": 869.18, \"step\": 145000}, {\"eval_return\": 778.99, \"step\": 155000}, {\"eval_return\": 864.03, \"step\": 165000}, {\"eval_return\": 850.53, \"step\": 175000}, {\"eval_return\": 907.31, \"step\": 185000}, {\"eval_return\": 873.49, \"step\": 195000}, {\"eval_return\": 887.02, \"step\": 205000}, {\"eval_return\": 956.04, \"step\": 215000}, {\"eval_return\": 892.09, \"step\": 225000}, {\"eval_return\": 914.78, \"step\": 235000}, {\"eval_return\": 950.32, \"step\": 245000}, {\"eval_return\": 936.9, \"step\": 255000}, {\"eval_return\": 937.27, \"step\": 265000}, {\"eval_return\": 934.78, \"step\": 275000}, {\"eval_return\": 960.2, \"step\": 285000}, {\"eval_return\": 947.46, \"step\": 295000}, {\"eval_return\": 937.8, \"step\": 305000}, {\"eval_return\": 948.66, \"step\": 315000}, {\"eval_return\": 930.61, \"step\": 325000}, {\"eval_return\": 919.23, \"step\": 335000}, {\"eval_return\": 816.18, \"step\": 345000}, {\"eval_return\": 932.45, \"step\": 355000}, {\"eval_return\": 943.13, \"step\": 365000}, {\"eval_return\": 952.86, \"step\": 375000}, {\"eval_return\": 942.31, \"step\": 385000}, {\"eval_return\": 966.94, \"step\": 395000}, {\"eval_return\": 948.01, \"step\": 405000}, {\"eval_return\": 957.06, \"step\": 415000}, {\"eval_return\": 939.37, \"step\": 425000}, {\"eval_return\": 963.65, \"step\": 435000}, {\"eval_return\": 948.42, \"step\": 445000}, {\"eval_return\": 937.72, \"step\": 455000}, {\"eval_return\": 939.54, \"step\": 465000}, {\"eval_return\": 965.94, \"step\": 475000}, {\"eval_return\": 916.74, \"step\": 485000}, {\"eval_return\": 945.58, \"step\": 495000}, {\"eval_return\": 957.87, \"step\": 505000}], \"final_eval_return\": 957.87, \"final_eval_step\": 505000, \"final_value_mean\": 665.17, \"final_ve_ratio\": 0.694, \"last10_mean\": 947.19, \"n_evals\": 51, \"total_steps\": 505000, \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 25000, \"value_mean\": 45.78}, {\"step\": 55000, \"value_mean\": 253.49}, {\"step\": 105000, \"value_mean\": 539.34}, {\"step\": 155000, \"value_mean\": 633.42}, {\"step\": 205000, \"value_mean\": 658.92}, {\"step\": 255000, \"value_mean\": 663.87}, {\"step\": 305000, \"value_mean\": 663.86}, {\"step\": 355000, \"value_mean\": 663.78}, {\"step\": 405000, \"value_mean\": 663.95}, {\"step\": 455000, \"value_mean\": 664.42}, {\"step\": 505000, \"value_mean\": 665.17}], \"ve_ratio_trajectory\": [{\"step\": 25000, \"ve\": 0.141}, {\"step\": 55000, \"ve\": 0.475}, {\"step\": 105000, \"ve\": 0.645}, {\"step\": 155000, \"ve\": 0.813}, {\"step\": 205000, \"ve\": 0.743}, {\"step\": 255000, \"ve\": 0.709}, {\"step\": 305000, \"ve\": 0.708}, {\"step\": 355000, \"ve\": 0.712}, {\"step\": 405000, \"ve\": 0.7}, {\"step\": 455000, \"ve\": 0.709}, {\"step\": 505000, \"ve\": 0.694}], \"ve_stable_range\": \"0.69-0.72 from 235K+\", \"vs_exp001_105K\": \"836.51 vs 915.67 (-8.6%)\", \"vs_exp001_final\": \"957.87 vs 970.41 (-1.3%)\", \"vs_exp001_last10\": \"947.19 vs 950.90 (-0.4%)\", \"vs_exp001_peak\": \"966.94 vs 970.41 (-0.4%)\"}, \"notes\": \"Baseline seed 2 完成。与 exp_001 (seed 0/1) 高度一致: peak 966.94 vs 970.41 (-0.4%), last10 mean 947.19 vs 950.90 (-0.4%), v/e stable 0.69-0.72 匹配。105K 处 836.51 比 seed 0/1 的 915.67 低 8.6%，但 215K+ 后完全收敛。345K 有一个 dip 到 816 但迅速恢复。baseline 跨 seed 一致性确认。\", \"pid\": \"142508\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009a_baseline_walker_s2 --steps 500000 --seed 2 --compile False --device cuda:0\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:08.969Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:33:16.385Z\"}, \"exp_008e_v3_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:00:20.816Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T14:29:53.738Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/\", \"metrics\": {\"actor_entropy_collapse_signature\": \"entropy rose from -5.21@85K to -3.83@105K (policy destabilizing during collapse)\", \"actor_entropy_trajectory\": [{\"actor_entropy\": 8.239, \"step\": 5000}, {\"actor_entropy\": 2.352, \"step\": 15000}, {\"actor_entropy\": 0.17, \"step\": 25000}, {\"actor_entropy\": -3.498, \"step\": 35000}, {\"actor_entropy\": -4.915, \"step\": 45000}, {\"actor_entropy\": -5.121, \"step\": 55000}, {\"actor_entropy\": -5.135, \"step\": 65000}, {\"actor_entropy\": -5.224, \"step\": 75000}, {\"actor_entropy\": -5.208, \"step\": 85000}, {\"actor_entropy\": -4.529, \"step\": 95000}, {\"actor_entropy\": -3.828, \"step\": 105000}], \"baseline_105K\": 915.67, \"collapse_confirmed\": \"105K (nve=3.78x, eval 715→137)\", \"collapse_onset\": \"95K (nve jumped from 0.68x to 1.34x)\", \"eval_trajectory\": [{\"eval_return\": 39.27, \"step\": 5000}, {\"eval_return\": 180.85, \"step\": 15000}, {\"eval_return\": 211.82, \"step\": 25000}, {\"eval_return\": 320.39, \"step\": 35000}, {\"eval_return\": 356.93, \"step\": 45000}, {\"eval_return\": 418.32, \"step\": 55000}, {\"eval_return\": 435.09, \"step\": 65000}, {\"eval_return\": 576.54, \"step\": 75000}, {\"eval_return\": 715.21, \"step\": 85000}, {\"eval_return\": 452.43, \"step\": 95000}, {\"eval_return\": 136.96, \"step\": 105000}], \"final_eval_return\": 136.96, \"final_nve\": 3.78, \"final_value_mean\": 339.84, \"final_ve_ratio\": 2.481, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"peak_eval_return\": 715.21, \"peak_eval_step\": 85000, \"train_return_108K\": \"19-23 (random policy level)\", \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 15000, \"value_mean\": 3.91}, {\"step\": 25000, \"value_mean\": 30.27}, {\"step\": 35000, \"value_mean\": 79.75}, {\"step\": 45000, \"value_mean\": 125.25}, {\"step\": 55000, \"value_mean\": 172.89}, {\"step\": 65000, \"value_mean\": 220.47}, {\"step\": 75000, \"value_mean\": 272.64}, {\"step\": 85000, \"value_mean\": 339.3}, {\"step\": 95000, \"value_mean\": 384.39}, {\"step\": 105000, \"value_mean\": 339.84}], \"ve_ratio_trajectory\": [{\"nve\": 1.64, \"step\": 25000, \"ve\": 0.143}, {\"nve\": 1.03, \"step\": 35000, \"ve\": 0.249}, {\"nve\": 1.06, \"step\": 45000, \"ve\": 0.351}, {\"nve\": 1.02, \"step\": 55000, \"ve\": 0.413}, {\"nve\": 0.9, \"step\": 65000, \"ve\": 0.507}, {\"nve\": 0.66, \"step\": 75000, \"ve\": 0.473}, {\"nve\": 0.68, \"step\": 85000, \"ve\": 0.474}, {\"nve\": 1.34, \"step\": 95000, \"ve\": 0.85}, {\"nve\": 3.78, \"step\": 105000, \"ve\": 2.481}], \"vs_baseline_105K\": \"-85.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"C6 seed 2 COLLAPSED. Delusional critic collapse at 85K→105K despite gate_dt_mean=1.0 locked throughout. eval peaked 715@85K then crashed to 137@105K (v/e=2.48, nve=3.78x). Cross-seed: seed 0=869.9 (healthy), seed 1=869.9 (healthy), seed 2=137 (collapsed). Collapse is stochastic (1/3 seeds) even in dt=1 imagination config. Subsample ON training data (dt=2 transitions) appears sufficient to trigger delusional critic in some seeds. Train returns at 108K=19-23 (random policy).\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"43437\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.23, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log\", \"pid\": \"43437\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T00:46:45.424Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18815.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:24:21.709Z\"}, \"exp_008e_v3_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T00:44:53.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T14:29:53.120Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/\", \"metrics\": {\"eval_trajectory\": [{\"eval_return\": 31, \"step\": 5000}, {\"eval_return\": 131.2, \"step\": 15000}, {\"eval_return\": 155.7, \"step\": 25000}, {\"eval_return\": 276.5, \"step\": 35000}, {\"eval_return\": 382.2, \"step\": 45000}, {\"eval_return\": 486.8, \"step\": 55000}, {\"eval_return\": 580.7, \"step\": 65000}, {\"eval_return\": 574.1, \"step\": 75000}, {\"eval_return\": 657.3, \"step\": 85000}, {\"eval_return\": 851.9, \"step\": 95000}, {\"eval_return\": 869.9, \"step\": 105000}], \"exit_code\": 0, \"final_eval_return\": 869.9, \"final_value_mean\": 457.9, \"gate_dt_1_frac\": 1, \"total_steps\": 112000, \"ve_ratio_105k\": 0.527}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"Crown jewel C6 seed 1 SUCCESS. eval_return=869.9@105K, v/e=0.527 (healthy, no delusional critic). Gate locked dt=1 throughout. Trajectory: 31→131→156→276→382→487→581→574→657→852→870. Consistent with seed 0, confirms trained dt_emb + dt=1 imagination is safe.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"898127\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.92, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s1.log\", \"pid\": \"898127\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T18:49:27.945Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 21325.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:44:53.439Z\"}, \"exp_006\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T00:49:02.944Z\", \"metrics\": {\"baseline_return_at_55k\": 625.7, \"deficit_pct\": -42.4, \"deficit_vs_baseline_at_55k\": -265.3, \"eval_return\": {\"15000\": 256.9, \"25000\": 321.4, \"35000\": 485.3, \"45000\": 477, \"5000\": 31, \"55000\": 360.4}, \"gate_dt_mean\": 2, \"latest_return\": 360.4, \"latest_step\": 55000, \"model_loss_at_55k\": 4.853, \"peak_return\": 485.3, \"peak_step\": 35000}, \"notes\": \"早期条目，权威数据在 exp_006_fixed_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.922Z\"}, \"exp_008a\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:07:59.793Z\", \"metrics\": {\"eval_return_15K\": 167.2, \"eval_return_25K\": 230.8, \"eval_return_35K\": 500.8, \"eval_return_45K\": 563.4, \"eval_return_55K\": 487.9, \"eval_return_5K\": 31, \"eval_return_65K\": \"pending (eval in progress)\", \"step\": 65000, \"train_return_64K_avg\": 556.6, \"trend\": \"peaked @45K=563, dipped to @55K=488, 65K eval in progress; train returns @64K healthy (~557)\", \"value_eval_ratio_55K\": \"37.6%\", \"value_mean_55K\": 183.5}, \"notes\": \"早期条目，权威数据在 exp_008a_no_subsample_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.075Z\"}, \"exp_008c\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:02.608Z\", \"metrics\": {\"eval_return_15K\": 171.3, \"eval_return_25K\": 192.4, \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.6, \"eval_return_55K\": 241.9, \"eval_return_5K\": 31, \"eval_return_65K\": 240.9, \"step\": 68000, \"train_return_68K_avg\": 245.1, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_65K\": \"32.8%\", \"value_mean_65K\": 79}, \"notes\": \"早期条目，权威数据在正式命名实验中。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:52.611Z\"}, \"exp_008d\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:05.136Z\", \"metrics\": {\"eval_return_15K\": 153.7, \"eval_return_25K\": 167.2, \"eval_return_35K\": 146.3, \"eval_return_5K\": 31, \"step\": 40000, \"train_return_40K_avg\": 119.3, \"trend\": \"declining — train_return @40K avg=119 below @35K eval=146, value/eval=41.1% not yet >50% but train performance dropping\", \"value_eval_ratio_35K\": \"41.1%\", \"value_mean_35K\": 60.2}, \"notes\": \"早期条目，权威数据在 exp_008d_subsample_on_h8。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:51.696Z\"}, \"exp_008e_v2_subsample_on_dt1_h15\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:26:39.732Z\", \"notes\": \"已被 exp_008e_v3_subsample_on_dt1_h15 取代，进程已死。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v2_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v2_subsample_on_dt1_h15.log\", \"pid\": \"125392\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:27:30.720Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:49.814Z\"}, \"exp_rssm_fidelity_analysis\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T11:09:52.237Z\", \"hypothesis\": \"RSSM prediction quality analysis: 比较 baseline/008d/008f 在 dt=1 vs dt=2 transitions 上的 obs_MSE 和 reward_MAE，量化 RSSM fidelity gap (plan_030)\", \"metrics\": {\"008d_trained_dtEmb\": {\"dt1_obs_mse\": 41.31, \"dt1_reward_mae\": 0.0568, \"dt2_obs_mse\": 53.67, \"dt2_reward_mae\": 0.1579, \"obs_gap\": 1.3, \"reward_gap\": 2.78}, \"008f_no_dtEmb\": {\"dt1_obs_mse\": 8.01, \"dt1_reward_mae\": 0.7469, \"dt2_obs_mse\": 22.04, \"dt2_reward_mae\": 0.7526, \"obs_gap\": 2.75, \"reward_gap\": 1.01}, \"baseline\": {\"dt1_obs_mse\": 13.49, \"dt1_reward_mae\": 0.0102, \"dt2_obs_mse\": 27.5, \"dt2_reward_mae\": 0.0159, \"obs_gap\": 2.04, \"reward_gap\": 1.56}}, \"notes\": \"分析实验，非训练实验。conclusion=success，状态从 PREPARING 修正为 DONE（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:48.642Z\"}, \"exp_008e_v3_subsample_on_dt1_h15\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15/latest.pt\", \"completed_at\": \"2026-05-14T09:07:47.319Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:29:31.656Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:05:44.288431+00:00\"}]}, \"hypothesis\": \"B+ confound control：subsample ON + untrained dt_emb + dt=1 imagination + H=15。验证 subsample ON 训练数据（含 dt=2 transitions）是否本身导致性能下降，即使 imagination 只用 dt=1。对照 008a（subsample OFF）和 baseline。如果 008e_v3 性能接近 baseline → subsample ON 本身无害。如果下降 → subsample ON 改变了 RSSM dynamics。\", \"metrics\": {\"baseline_105K\": 915.67, \"current_step\": 112000, \"eval_return\": {\"105K\": 869.88, \"15K\": 131.2, \"25K\": 155.69, \"35K\": 276.47, \"45K\": 382.22, \"55K\": 486.84, \"5K\": 31, \"65K\": 580.67, \"75K\": 574.09, \"85K\": 657.31, \"95K\": 851.86}, \"fps\": 7.01, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"last_updated\": \"2026-05-14T09:09:00\", \"normalized_ve\": {\"105K\": 0.8, \"25K\": 1.93, \"35K\": 0.94, \"45K\": 0.88, \"55K\": 0.87, \"65K\": 0.72, \"75K\": 0.73, \"85K\": 0.76, \"95K\": 0.75}, \"target_steps\": 105000, \"value_eval_ratio\": {\"105K\": 0.527, \"25K\": 0.168, \"35K\": 0.227, \"45K\": 0.29, \"55K\": 0.35, \"65K\": 0.405, \"75K\": 0.523, \"85K\": 0.534, \"95K\": 0.476}, \"value_mean\": {\"105K\": 457.93, \"25K\": 26.19, \"35K\": 62.76, \"45K\": 110.67, \"55K\": 170.09, \"65K\": 235.05, \"75K\": 300.51, \"85K\": 351.33, \"95K\": 405.25}, \"verdict\": \"SUCCESS - 95% baseline, normalized v/e stable 0.72-0.80x, B+ hypothesis confirmed\", \"vs_baseline_105K\": \"-5.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:05:42.563Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 4.64, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, untrained dt_emb)\", \"pid\": \"126110\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:29:31.600Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16695.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:46:00.840Z\"}, \"exp_009c_008f_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T22:15:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:26.154Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T14:15:58.982844+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_008f_walker_s2.log\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 does NOT replicate seed 1's zigzag recovery. 008f seed 1 peaked at 503@105K with rising trend; seed 2 peaked at 359@75K then declined to 148@105K. The adaptive horizon mechanism's benefit appears seed-dependent and not robust.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 30.37, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0.0013, \"ve_ratio\": null}, {\"baseline_ve\": null, \"eval_return\": 157.15, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 3.057, \"ve_ratio\": 0.019}, {\"baseline_ve\": 0.087, \"eval_return\": 168.75, \"normalized_ve\": 1.26, \"step\": 25000, \"value_mean\": 18.536, \"ve_ratio\": 0.11}, {\"baseline_ve\": 0.241, \"eval_return\": 178.94, \"normalized_ve\": 0.79, \"step\": 35000, \"value_mean\": 34.263, \"ve_ratio\": 0.191}, {\"baseline_ve\": 0.331, \"eval_return\": 211.08, \"normalized_ve\": 0.72, \"step\": 45000, \"value_mean\": 50.099, \"ve_ratio\": 0.237}, {\"baseline_ve\": 0.404, \"eval_return\": 238.91, \"normalized_ve\": 0.66, \"step\": 55000, \"value_mean\": 63.267, \"ve_ratio\": 0.265}, {\"baseline_ve\": 0.563, \"eval_return\": 244.15, \"normalized_ve\": 0.53, \"step\": 65000, \"value_mean\": 72.717, \"ve_ratio\": 0.298}, {\"baseline_ve\": 0.719, \"eval_return\": 359.14, \"normalized_ve\": 0.33, \"step\": 75000, \"value_mean\": 83.91, \"ve_ratio\": 0.234}, {\"baseline_ve\": 0.701, \"eval_return\": 227.43, \"normalized_ve\": 0.6, \"step\": 85000, \"value_mean\": 96.071, \"ve_ratio\": 0.422}, {\"baseline_ve\": 0.632, \"eval_return\": 190.94, \"normalized_ve\": 0.9, \"step\": 95000, \"value_mean\": 108.29, \"ve_ratio\": 0.567}, {\"baseline_ve\": 0.656, \"eval_return\": 148.34, \"normalized_ve\": 1.14, \"step\": 105000, \"value_mean\": 111.247, \"ve_ratio\": 0.75}], \"target_steps\": 105000, \"trend\": \"Peak 359@75K then monotonic decline to 148@105K; no recovery pattern unlike 008f seed 1's zigzag recovery to 503\", \"verdict\": \"NEGATIVE - no delusional critic (normalized v/e < 1.5x) but persistent decline after 75K; cross-seed consistency with 008f seed 1 NOT confirmed\", \"vs_baseline_105K\": \"-83.8%\"}, \"notes\": \"D031 排期修正: 009c 延长 200K 降优先级，排在 009e/009f 之后。cuda:1 排期: 009b → 008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。105K 指标: eval=148.34, value=111.25, nve=1.14x。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"140980\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_008f_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-14T14:15:57.425Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:10.835Z\", \"training_hours\": 6.95}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:34:24.161Z\"}, \"exp_006_fixed_dt2\": {\"account\": \"root\", \"completed_at\": \"2026-05-14T01:13:11.533Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T21:10:58.851Z\", \"extra\": {\"audit_commit\": \"6159e46\", \"bugs_fixed\": \"_effective_max_dt not synced in fixed_dt mode; hardcoded curriculum phases ignoring config\", \"curriculum_audit\": \"Curriculum does NOT apply in fixed_dt mode (models.py:200-205). gate_fixed_dt>0 bypasses _update_gate_schedule(). subsample_variable_dt receives effective_max_dt=2.0 from step 0, training data is 58.5% dt=1 + 41.5% dt=2 throughout. Actual train/imagine mismatch: mixed dt training vs pure dt=2 imagination.\"}, \"gpu\": \"cuda:0\", \"hypothesis\": \"诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。\", \"latest_metrics\": {\"checked_at\": \"2026-05-14\", \"eval_return\": 485.3, \"eval_return_trajectory\": {\"15K\": 256.9, \"25K\": 321.4, \"35K\": 485.3, \"5K\": 31}, \"eval_step\": 35000, \"fps\": 6.6, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"grad_norm\": 8.6, \"pid\": 85029, \"prev_eval_return\": 321.4, \"process_status\": \"running\", \"step\": 36000}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_006_fixed_dt2.log\", \"metrics\": {\"baseline_35K\": 388.5, \"baseline_45K\": 513.8, \"baseline_55K\": 625.7, \"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_15K\": 256.9, \"eval_return_25K\": 321.4, \"eval_return_35K\": 485.3, \"eval_return_45K\": 477, \"eval_return_55K\": 360.4, \"eval_return_5K\": 31, \"eval_return_65K\": 132.86, \"fps\": 6.5, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"model_loss_15K\": 7.593, \"model_loss_25K\": 5.633, \"model_loss_35K\": 5.229, \"model_loss_45K\": 5.023, \"model_loss_55K\": 4.9, \"model_loss_5K\": 20.738, \"peak_return\": 485.3, \"peak_step\": \"35K\", \"step\": 65000, \"trend\": \"inverted-V: peak 485@35K, collapsing to 133@65K; v/e accelerating: 31.1%→53.3%→93.3%→272% (value 2.7x eval_return at 65K)\", \"value_eval_ratio_35K\": 0.311, \"value_eval_ratio_45K\": 0.533, \"value_eval_ratio_55K\": 0.933, \"value_eval_ratio_65K\": 2.722, \"value_mean_35K\": 151.1, \"value_mean_45K\": 254.29, \"value_mean_55K\": 336.44, \"value_mean_65K\": 361.69, \"vs_baseline_55K\": \"-42.4%\"}, \"parent\": \"exp_005_event_gated_v4\", \"pid\": \"85029\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-13T22:12:00.446Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"N/A - negative result, fixed dt=2 collapsed to 132.9@65K (21.6% baseline)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"failure_reason\": \"fixed dt=2 崩塌：训练分布混合（58.5% dt=1 + 41.5% dt=2 log-uniform）+ 想象纯 dt=2 条件下，eval_return 从 peak 485@35K 持续下降至 132.9@65K（baseline 同期 615.9）。与 learned gate 变体一致的崩塌模式。代码审计确认 curriculum 不生效（gate_fixed_dt>0 跳过 _update_gate_schedule）。\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt2_v1_s1\", \"model_name\": \"DreamerV3+FixedDt2 (gate_fixed_dt=2, no learned gate)\", \"pid\": \"85029\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T10:20:11.722Z\"}, \"exp_008e_subsample_on_fixed_dt1\": {\"checkpoint_path\": \"N/A - killed, duplicate registry entry, logdir contaminated by dual-process write\", \"completed_at\": \"2026-05-14T04:21:47.956Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:07.303Z\", \"failure_reason\": \"重复 registry 条目 + logdir 被两个进程交叉写入导致 tfevents/metrics.jsonl 损坏。Director 指令清理后以 exp_008e_subsample_on_dt1_h15 为准重跑。\", \"hypothesis\": \"验证 Reviewer D020 因果假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（delusional critic），即使 actor 不用 dt=2 imagination。对照：008a (subsample OFF, dt=2 imag) value/eval=37.6%@55K vs exp_006 (subsample ON, dt=2 imag) 53.3%。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.19, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"121636\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:22.915Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 685.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:58.056Z\"}, \"exp_008e_subsample_on_dt1_h15\": {\"checkpoint_path\": \"N/A - killed, logdir contaminated by duplicate process cross-write\", \"completed_at\": \"2026-05-14T04:21:48.584Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:37.655Z\", \"hypothesis\": \"验证 Reviewer D020 delusional critic 假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（即使 actor 不用 dt=2 imagination）。对照：008a（subsample OFF，dt=2 imagination）和 006（subsample ON，dt=2 imagination）。\", \"notes\": \"重复进程：与 exp_008e_subsample_on_fixed_dt1 命令完全相同，共享同一 logdir，导致 tfevents 文件互相污染。Kill PID 122038，保留 PID 121636。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.18, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"122038\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:46.045Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 662.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:57.658Z\"}, \"exp_002_event_gated\": {\"completed_at\": \"2026-05-13T04:50:14.987Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T02:09:54.240Z\", \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"kill_reason\": \"Phase 1 subsample 设计缺陷：subsample_variable_dt 在 Phase 1 (gate_scale=0) 也生效，RSSM 用 variable-Δt 数据训练但 imagination 只用 Δt=1，return 恶化到 baseline 的 25%。手动 kill 后部署 subsample curriculum 补丁并重启为 exp_003。\", \"retry_count\": 0, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1 --steps 500000 --seed 1 --compile False --device cuda:1 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM (K=8, τ=5→0.5, λ_H=0.1→0.01)\", \"pid\": 9769, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T04:52:18.089Z\"}}, \"count\": 166, \"total\": 166, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6191}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The registry output is very large (375K characters). I need to extract the relevant experiment data. Let me use bash with jq to query the specific experiments I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "096cb7c9-6a25-454d-8ec6-80c6d5a108e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AzHpvAtx1HKkd6b94bTUhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 25175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 476
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

### Assistant

_source line 11_

Registry 数据太大，用 jq 提取关键信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "2851b66b-dfa4-4252-a4c3-7007847dd401",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AzHpvAtx1HKkd6b94bTUhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 25175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 476
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

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01MKF424158Ckc4oN96PNwts`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n\n# List all experiments with key fields\nfor exp in result:\n    eid = exp.get('exp_id', 'N/A')\n    status = exp.get('status', 'N/A')\n    conclusion = exp.get('conclusion', 'N/A')\n    metrics = exp.get('metrics', {})\n    nve_peak = metrics.get('nve_peak') or metrics.get('NVE_peak') or metrics.get('ve_ratio_peak')\n    print(f'{eid} | status={status} | conclusion={conclusion} | nve_peak={nve_peak}')\n\" 2>&1 | head -60\n",
  "description": "Extract experiment list with key fields from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "6a91d3b6-d628-4ade-b901-03dc80113a11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AzHpvAtx1HKkd6b94bTUhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 25175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 476
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

_source line 13 · 2026-05-25T20:19:35.776Z_

<details><summary>↩ Tool result · `toolu_01MKF424158Ckc4oN96PNwts`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    eid = exp.get('exp_id', 'N/A')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "bfccf091-d32b-465c-bb2e-b95f996dc04f",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    eid = exp.get('exp_id', 'N/A')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01HHNDi1Qj5X9KbRuggppmpq`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = data['result']\n# Check type\nprint(type(result))\nif isinstance(result, str):\n    print(result[:500])\n\" 2>&1\n",
  "description": "Check registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "c1465fc4-ebfb-4ea0-925a-2ea8041b28e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFuEpKULfgV4GWqjwTFojR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 25651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 15 · 2026-05-25T20:19:41.138Z_

<details><summary>↩ Tool result · `toolu_01HHNDi1Qj5X9KbRuggppmpq`</summary>

```text
&lt;class 'str'>
{"success": true, "data": {"experiments": {"exp_090_cheetah_no_dt_emb_s2": {"status": "RUNNING", "retry_count": 0, "created_at": "2026-05-25T20:15:41.571Z", "updated_at": "2026-05-25T20:17:44.601Z", "hypothesis": "Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_embedding 完全移除后预期无 CIVO，加强 C2 cross-env causal control 多 seed 证据基础。plan_022。", "parent": "exp_082_cheetah_no_dt_emb_s0", "spec": {"data_path": "dmc_cheetah_run", "dat
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "385bbb10-7e5c-4b2b-986d-22107df770e4",
  "tool_use_result": {
    "stdout": "&lt;class 'str'>\n{\"success\": true, \"data\": {\"experiments\": {\"exp_090_cheetah_no_dt_emb_s2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T20:15:41.571Z\", \"updated_at\": \"2026-05-25T20:17:44.601Z\", \"hypothesis\": \"Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_embedding 完全移除后预期无 CIVO，加强 C2 cross-env causal control 多 seed 证据基础。plan_022。\", \"parent\": \"exp_082_cheetah_no_dt_emb_s0\", \"spec\": {\"data_path\": \"dmc_cheetah_run\", \"dat",
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

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01QU2jubqmjurSVSbaHing2b`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\nfor eid, exp in exps.items():\n    status = exp.get('status', 'N/A')\n    conclusion = exp.get('conclusion', '')\n    metrics = exp.get('metrics', {})\n    nve_peak = metrics.get('nve_peak') or metrics.get('NVE_peak') or metrics.get('ve_ratio_peak')\n    ve_peak = metrics.get('ve_ratio_peak')\n    print(f'{eid} | status={status} | conclusion={conclusion[:40] if conclusion else \\\"\\\"} | nve_peak={nve_peak} | ve_ratio_peak={ve_peak}')\n\" 2>&1\n",
  "description": "Extract all experiments with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "cb3ab3e0-fcc9-473a-b643-67eba360019f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPgUhrr1fettHk8uZnzoWB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 491,
      "cache_read_input_tokens": 26157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 491
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

_source line 17 · 2026-05-25T20:19:46.513Z_

<details><summary>↩ Tool result · `toolu_01QU2jubqmjurSVSbaHing2b`</summary>

```text
exp_090_cheetah_no_dt_emb_s2 | status=RUNNING | conclusion= | nve_peak=None | ve_ratio_peak=None
exp_086_frozen_dt_emb_cheetah_s0 | status=ANALYZING | conclusion= | nve_peak=None | ve_ratio_peak=None
exp_089_cheetah_no_dt_emb_s1 | status=RUNNING | conclusion= | nve_peak=None | ve_ratio_peak=None
exp_009b_008d_walker_s2 | status=DONE | conclusion=negative | nve_peak=1.62 | ve_ratio_peak=0.5703
exp_009e_008d_walker_s1 | status=DONE | conclusion=negative | nve_peak=4.13 | ve_ratio_peak=1.6663
exp_085_frozen_dt_emb_walker_s1 | status=DONE | conclusion=success | nve_peak=0.31 | ve_ratio_peak=None
exp_084_frozen_dt_emb_walker_s0 | status=DONE | conclusion=success | nve_peak=0.37 | ve_ratio_peak=None
exp_088_cheetah_008d_s1 | status=RUNNING | conclusion= | nve_peak=None | ve_ratio_peak=None
exp_082_cheetah_no_dt_emb_s0 | status=DONE | conclusion=success | nve_peak=1.58 | ve_ratio_peak=0.955
exp_087_frozen_dt_emb_cheetah_s1 | status=DONE | conclusion=success | nve_peak=0.2 | ve_ratio_peak=0.2
exp_083_cheetah_baseline_s1 | status=DONE | conclusion=success | nve_peak=0.6 | ve_ratio_peak=0.6
exp_078_cheetah_008d_s0 | status=DONE | conclusion=success | nve_peak=4.1 | ve_ratio_peak=2.318
exp_077_cheetah_baseline_s0 | status=DONE | conclusion=success | nve_peak=0.739 | ve_ratio_peak=0.739
exp_079_frozen_dt_emb_walker_s0 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_081_008e_v3_walker_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_080_008e_v3_walker_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_074_008a_walker_s3 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_076_cheetah_civo_trigger_s3 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_075_cheetah_civo_trigger_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_071_008f_walker_s3 | status=DONE | conclusion=success | nve_peak=0.7 | ve_ratio_peak=0.7
exp_073_008f_walker_s4 | status=DONE | conclusion=success | nve_peak=0.76 | ve_ratio_peak=0.5
exp_072_008e_v3_walker_s5 | status=DONE | conclusion=success | nve_peak=0.61 | ve_ratio_peak=None
exp_070_008e_v3_walker_s0 | status=DONE | conclusion=negative | nve_peak=0.8 | ve_ratio_peak=None
exp_069_008f_walker_repro_s1 | status=DONE | conclusion=success | nve_peak=0.66 | ve_ratio_peak=0.4
exp_068_008d_walker_repro_s1 | status=DONE | conclusion=success | nve_peak=4.6 | ve_ratio_peak=4.6
exp_067_frozen_dt_emb_walker_plan015 | status=DONE | conclusion=success | nve_peak=0.4 | ve_ratio_peak=None
exp_066b_timeseries_rssm_fidelity_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_062_cartpole_control | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_061_cartpole_civo_trigger | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_008d_subsample_on_h8 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_066_timeseries_rssm_fidelity | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_060_cartpole_baseline | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_065_dt_emb_cosine | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_064_value_distribution | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_063_rssm_fidelity | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_051_stackcube_frozen_dt_emb_s0 | status=DONE | conclusion=negative | nve_peak=4.3 | ve_ratio_peak=4.3
exp_049_stackcube_civo_trigger_s0 | status=DONE | conclusion=success | nve_peak=5.048 | ve_ratio_peak=5.048
exp_057 | status=DONE | conclusion=success | nve_peak=1.3 | ve_ratio_peak=None
exp_008d_civo_trigger_s4 | status=DONE | conclusion=success | nve_peak=4.62 | ve_ratio_peak=3.0294
exp_059_walker_trained_s5 | status=DONE | conclusion=success | nve_peak=4.72 | ve_ratio_peak=3.3075
exp_057_frozen_dt_emb_walker_s2 | status=DONE | conclusion=success | nve_peak=1.88 | ve_ratio_peak=1.283
exp_058_frozen_dt_emb_cheetah_s1 | status=DONE | conclusion=success | nve_peak=0.78 | ve_ratio_peak=0.231
exp_056_peginsertion_frozen_s1 | status=DONE | conclusion=success | nve_peak=11.321 | ve_ratio_peak=11.321
exp_055_peginsertion_civo_trigger_s1 | status=DONE | conclusion=success | nve_peak=3.08 | ve_ratio_peak=3.08
exp_054_pickcube_frozen_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_053_peginsertion_frozen_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_050_peginsertion_civo_trigger_s0 | status=DONE | conclusion=success | nve_peak=10.05 | ve_ratio_peak=10.05
exp_052_stackcube_civo_trigger_s1 | status=DONE | conclusion=success | nve_peak=4.67 | ve_ratio_peak=4.67
exp_048_cheetah_civo_extension | status=DONE | conclusion=success | nve_peak=24.112 | ve_ratio_peak=24.112
exp_047_frozen_dt_emb_walker_s1 | status=DONE | conclusion=success | nve_peak=1.71 | ve_ratio_peak=1.099
exp_046_frozen_dt_emb_cheetah | status=DONE | conclusion=success | nve_peak=1.35 | ve_ratio_peak=0.4
exp_044_gradient_stop_walker | status=DONE | conclusion=success | nve_peak=4.4 | ve_ratio_peak=4.4
exp_045_treatment_extension_008d_s3 | status=DONE | conclusion=success | nve_peak=4.91 | ve_ratio_peak=None
exp_043_008f_walker_s1 | status=DONE | conclusion=success | nve_peak=0.808 | ve_ratio_peak=None
exp_042_frozen_dt_emb_walker | status=DONE | conclusion=success | nve_peak=0.194 | ve_ratio_peak=None
exp_040_wide_dual_critic_cheetah | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_041_dual_critic_walker_s3 | status=DONE | conclusion=success | nve_peak=1.5 | ve_ratio_peak=None
exp_039_narrow_dual_critic_walker_s1 | status=DONE | conclusion=success | nve_peak=2.19 | ve_ratio_peak=None
exp_038_dual_critic_walker_s2 | status=DONE | conclusion=negative | nve_peak=0.3 | ve_ratio_peak=None
exp_037_wide_critic_cheetah | status=DONE | conclusion=negative | nve_peak=3.6 | ve_ratio_peak=None
exp_036_dual_critic_pickcube | status=DONE | conclusion=negative | nve_peak=2.3 | ve_ratio_peak=None
exp_035_narrow_dual_critic_walker | status=DONE | conclusion=success | nve_peak=2.75 | ve_ratio_peak=None
exp_034 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_034_dual_critic_cheetah | status=DONE | conclusion=negative | nve_peak=1.8 | ve_ratio_peak=1.8
exp_033_wide_critic_walker | status=DONE | conclusion=success | nve_peak=4.7 | ve_ratio_peak=4.7
exp_031b_tcn_pickcube_s0_sigma05 | status=DONE | conclusion=negative | nve_peak=3.3 | ve_ratio_peak=None
exp_032_dual_critic_walker | status=DONE | conclusion=success | nve_peak=1.1 | ve_ratio_peak=None
exp_032b_dual_critic_walker_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_029d_tcn_walker_s3_sigma02 | status=DONE | conclusion=negative | nve_peak=3.0 | ve_ratio_peak=None
exp_031_tcn_pickcube_s0_sigma02 | status=DONE | conclusion=negative | nve_peak=3.71 | ve_ratio_peak=3.71
exp_029b_tcn_walker_s2_sigma02 | status=DONE | conclusion=negative | nve_peak=2.765 | ve_ratio_peak=None
exp_030c_tcn_cheetah_s0_sigma10 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_029c_tcn_walker_s0_sigma01 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_029a_tcn_walker_s1_sigma02 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_030b_tcn_cheetah_s0_sigma05 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_027_tcn_walker_s1 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_027_tcn_walker_s0_sigma02 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_030a_tcn_cheetah_s0_sigma02 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_027_tcn_walker_s0 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_028_rave_walker_s0_ceil15 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_028_rave_walker_s0 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_025_obs_sgs_walker_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_026_obs_sgs_cheetah_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_026_obs_sgs_cheetah_s0 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_025_obs_sgs_walker_s4 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_025_obs_sgs_walker_s3 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_025_obs_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_001_baseline_s4_extended | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_001_baseline_s3_extended | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_001_baseline_s2_extended | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_023_cheetah_baseline_s4_extended | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_001_baseline_s4 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_023_cheetah_baseline_s4 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_023_cheetah_baseline_s3 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_001_baseline_s3 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_023_cheetah_baseline_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_008f_s4 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_009c_s3 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_001_baseline_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_008f_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_008a_cheetah_unexposed_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_008a_cheetah_unexposed_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_009c_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_008e_v3_s4 | status=DONE | conclusion=success | nve_peak=0.99 | ve_ratio_peak=None
exp_008e_v3_s3 | status=DONE | conclusion=negative | nve_peak=4.02 | ve_ratio_peak=None
exp_008a_unexposed_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_008a_unexposed_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_008a_untrained_s1 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_008a_untrained_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_010b_cheetah_civo_trigger_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_024b_cheetah_no_dt_emb_s0 | status=DONE | conclusion=success | nve_peak=0.2 | ve_ratio_peak=None
exp_024b_cheetah_no_dt_emb_s1 | status=DONE | conclusion=success | nve_peak=0.1 | ve_ratio_peak=None
exp_024_cheetah_no_dt_emb_s0 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_021_full_sgs_cheetah_s1 | status=DONE | conclusion=negative | nve_peak=9.94 | ve_ratio_peak=None
exp_023a_cheetah_baseline_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_010b_cheetah_civo_trigger | status=DONE | conclusion=success | nve_peak=8.27 | ve_ratio_peak=None
exp_023b_cheetah_baseline_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_019b_pickcube_civo_trigger | status=DONE | conclusion=success | nve_peak=3.78 | ve_ratio_peak=None
exp_022b_no_curriculum | status=DONE | conclusion=success | nve_peak=1.22 | ve_ratio_peak=0.218
exp_022_untrained_dt_emb_learned_gate | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_019a_v2_pickcube_baseline | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_007_fixed_dt4 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_008c_no_subsample_dt2_h8 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_003_event_gated_v2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_004_event_gated_v3 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_005_event_gated_v4 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_008d_civo_trigger_s3 | status=DONE | conclusion=success | nve_peak=1.53 | ve_ratio_peak=None
exp_018v2_full_sgs_walker_s1 | status=DONE | conclusion=negative | nve_peak=1.66 | ve_ratio_peak=None
exp_018_full_sgs_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_008f_no_dt_embed_subsample_on_h8 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_016d_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_001_baseline | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_008d_civo_trigger_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_008f_s3_no_dt_embed_walker | status=DONE | conclusion=success | nve_peak=< 1.5x | ve_ratio_peak=None
exp_020_vanilla_dreamerv3_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_019a_pickcube_baseline | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_018_full_sgs_walker_s1 | status=DONE | conclusion=killed | nve_peak=0.72 | ve_ratio_peak=None
exp_010a_cheetah_baseline_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_009d_baseline_walker_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_017_subsample_off_trained_dt_emb | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
016e | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_016e_sgs_walker_s1 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_016c_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_009h_008f_walker_s0 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_016b_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_009g_008f_walker_s0 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_009f_008f_walker_s1 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_016_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
exp_015b_frozen_dt_emb | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_008a_no_subsample_dt2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_009d_baseline_walker_s1 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_009a_baseline_walker_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_008e_v3_walker_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_008e_v3_walker_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_006 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_008a | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_008c | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_008d | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_008e_v2_subsample_on_dt1_h15 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_rssm_fidelity_analysis | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_008e_v3_subsample_on_dt1_h15 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None
exp_009c_008f_walker_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_006_fixed_dt2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None
exp_008e_subsample_on_fixed_dt1 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_008e_subsample_on_dt1_h15 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None
exp_002_event_gated | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "8d51abcb-d97d-47eb-b717-455783823c19",
  "tool_use_result": {
    "stdout": "exp_090_cheetah_no_dt_emb_s2 | status=RUNNING | conclusion= | nve_peak=None | ve_ratio_peak=None\nexp_086_frozen_dt_emb_cheetah_s0 | status=ANALYZING | conclusion= | nve_peak=None | ve_ratio_peak=None\nexp_089_cheetah_no_dt_emb_s1 | status=RUNNING | conclusion= | nve_peak=None | ve_ratio_peak=None\nexp_009b_008d_walker_s2 | status=DONE | conclusion=negative | nve_peak=1.62 | ve_ratio_peak=0.5703\nexp_009e_008d_walker_s1 | status=DONE | conclusion=negative | nve_peak=4.13 | ve_ratio_peak=1.6663\nexp_085_frozen_dt_emb_walker_s1 | status=DONE | conclusion=success | nve_peak=0.31 | ve_ratio_peak=None\nexp_084_frozen_dt_emb_walker_s0 | status=DONE | conclusion=success | nve_peak=0.37 | ve_ratio_peak=None\nexp_088_cheetah_008d_s1 | status=RUNNING | conclusion= | nve_peak=None | ve_ratio_peak=None\nexp_082_cheetah_no_dt_emb_s0 | status=DONE | conclusion=success | nve_peak=1.58 | ve_ratio_peak=0.955\nexp_087_frozen_dt_emb_cheetah_s1 | status=DONE | conclusion=success | nve_peak=0.2 | ve_ratio_peak=0.2\nexp_083_cheetah_baseline_s1 | status=DONE | conclusion=success | nve_peak=0.6 | ve_ratio_peak=0.6\nexp_078_cheetah_008d_s0 | status=DONE | conclusion=success | nve_peak=4.1 | ve_ratio_peak=2.318\nexp_077_cheetah_baseline_s0 | status=DONE | conclusion=success | nve_peak=0.739 | ve_ratio_peak=0.739\nexp_079_frozen_dt_emb_walker_s0 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_081_008e_v3_walker_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_080_008e_v3_walker_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_074_008a_walker_s3 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_076_cheetah_civo_trigger_s3 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_075_cheetah_civo_trigger_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_071_008f_walker_s3 | status=DONE | conclusion=success | nve_peak=0.7 | ve_ratio_peak=0.7\nexp_073_008f_walker_s4 | status=DONE | conclusion=success | nve_peak=0.76 | ve_ratio_peak=0.5\nexp_072_008e_v3_walker_s5 | status=DONE | conclusion=success | nve_peak=0.61 | ve_ratio_peak=None\nexp_070_008e_v3_walker_s0 | status=DONE | conclusion=negative | nve_peak=0.8 | ve_ratio_peak=None\nexp_069_008f_walker_repro_s1 | status=DONE | conclusion=success | nve_peak=0.66 | ve_ratio_peak=0.4\nexp_068_008d_walker_repro_s1 | status=DONE | conclusion=success | nve_peak=4.6 | ve_ratio_peak=4.6\nexp_067_frozen_dt_emb_walker_plan015 | status=DONE | conclusion=success | nve_peak=0.4 | ve_ratio_peak=None\nexp_066b_timeseries_rssm_fidelity_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_062_cartpole_control | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_061_cartpole_civo_trigger | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_008d_subsample_on_h8 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_066_timeseries_rssm_fidelity | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_060_cartpole_baseline | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_065_dt_emb_cosine | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_064_value_distribution | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_063_rssm_fidelity | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_051_stackcube_frozen_dt_emb_s0 | status=DONE | conclusion=negative | nve_peak=4.3 | ve_ratio_peak=4.3\nexp_049_stackcube_civo_trigger_s0 | status=DONE | conclusion=success | nve_peak=5.048 | ve_ratio_peak=5.048\nexp_057 | status=DONE | conclusion=success | nve_peak=1.3 | ve_ratio_peak=None\nexp_008d_civo_trigger_s4 | status=DONE | conclusion=success | nve_peak=4.62 | ve_ratio_peak=3.0294\nexp_059_walker_trained_s5 | status=DONE | conclusion=success | nve_peak=4.72 | ve_ratio_peak=3.3075\nexp_057_frozen_dt_emb_walker_s2 | status=DONE | conclusion=success | nve_peak=1.88 | ve_ratio_peak=1.283\nexp_058_frozen_dt_emb_cheetah_s1 | status=DONE | conclusion=success | nve_peak=0.78 | ve_ratio_peak=0.231\nexp_056_peginsertion_frozen_s1 | status=DONE | conclusion=success | nve_peak=11.321 | ve_ratio_peak=11.321\nexp_055_peginsertion_civo_trigger_s1 | status=DONE | conclusion=success | nve_peak=3.08 | ve_ratio_peak=3.08\nexp_054_pickcube_frozen_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_053_peginsertion_frozen_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_050_peginsertion_civo_trigger_s0 | status=DONE | conclusion=success | nve_peak=10.05 | ve_ratio_peak=10.05\nexp_052_stackcube_civo_trigger_s1 | status=DONE | conclusion=success | nve_peak=4.67 | ve_ratio_peak=4.67\nexp_048_cheetah_civo_extension | status=DONE | conclusion=success | nve_peak=24.112 | ve_ratio_peak=24.112\nexp_047_frozen_dt_emb_walker_s1 | status=DONE | conclusion=success | nve_peak=1.71 | ve_ratio_peak=1.099\nexp_046_frozen_dt_emb_cheetah | status=DONE | conclusion=success | nve_peak=1.35 | ve_ratio_peak=0.4\nexp_044_gradient_stop_walker | status=DONE | conclusion=success | nve_peak=4.4 | ve_ratio_peak=4.4\nexp_045_treatment_extension_008d_s3 | status=DONE | conclusion=success | nve_peak=4.91 | ve_ratio_peak=None\nexp_043_008f_walker_s1 | status=DONE | conclusion=success | nve_peak=0.808 | ve_ratio_peak=None\nexp_042_frozen_dt_emb_walker | status=DONE | conclusion=success | nve_peak=0.194 | ve_ratio_peak=None\nexp_040_wide_dual_critic_cheetah | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_041_dual_critic_walker_s3 | status=DONE | conclusion=success | nve_peak=1.5 | ve_ratio_peak=None\nexp_039_narrow_dual_critic_walker_s1 | status=DONE | conclusion=success | nve_peak=2.19 | ve_ratio_peak=None\nexp_038_dual_critic_walker_s2 | status=DONE | conclusion=negative | nve_peak=0.3 | ve_ratio_peak=None\nexp_037_wide_critic_cheetah | status=DONE | conclusion=negative | nve_peak=3.6 | ve_ratio_peak=None\nexp_036_dual_critic_pickcube | status=DONE | conclusion=negative | nve_peak=2.3 | ve_ratio_peak=None\nexp_035_narrow_dual_critic_walker | status=DONE | conclusion=success | nve_peak=2.75 | ve_ratio_peak=None\nexp_034 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_034_dual_critic_cheetah | status=DONE | conclusion=negative | nve_peak=1.8 | ve_ratio_peak=1.8\nexp_033_wide_critic_walker | status=DONE | conclusion=success | nve_peak=4.7 | ve_ratio_peak=4.7\nexp_031b_tcn_pickcube_s0_sigma05 | status=DONE | conclusion=negative | nve_peak=3.3 | ve_ratio_peak=None\nexp_032_dual_critic_walker | status=DONE | conclusion=success | nve_peak=1.1 | ve_ratio_peak=None\nexp_032b_dual_critic_walker_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_029d_tcn_walker_s3_sigma02 | status=DONE | conclusion=negative | nve_peak=3.0 | ve_ratio_peak=None\nexp_031_tcn_pickcube_s0_sigma02 | status=DONE | conclusion=negative | nve_peak=3.71 | ve_ratio_peak=3.71\nexp_029b_tcn_walker_s2_sigma02 | status=DONE | conclusion=negative | nve_peak=2.765 | ve_ratio_peak=None\nexp_030c_tcn_cheetah_s0_sigma10 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_029c_tcn_walker_s0_sigma01 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_029a_tcn_walker_s1_sigma02 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_030b_tcn_cheetah_s0_sigma05 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_027_tcn_walker_s1 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_027_tcn_walker_s0_sigma02 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_030a_tcn_cheetah_s0_sigma02 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_027_tcn_walker_s0 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_028_rave_walker_s0_ceil15 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_028_rave_walker_s0 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_025_obs_sgs_walker_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_026_obs_sgs_cheetah_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_026_obs_sgs_cheetah_s0 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_025_obs_sgs_walker_s4 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_025_obs_sgs_walker_s3 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_025_obs_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_001_baseline_s4_extended | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_001_baseline_s3_extended | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_001_baseline_s2_extended | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_023_cheetah_baseline_s4_extended | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_001_baseline_s4 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_023_cheetah_baseline_s4 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_023_cheetah_baseline_s3 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_001_baseline_s3 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_023_cheetah_baseline_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_008f_s4 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_009c_s3 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_001_baseline_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_008f_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_008a_cheetah_unexposed_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_008a_cheetah_unexposed_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_009c_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_008e_v3_s4 | status=DONE | conclusion=success | nve_peak=0.99 | ve_ratio_peak=None\nexp_008e_v3_s3 | status=DONE | conclusion=negative | nve_peak=4.02 | ve_ratio_peak=None\nexp_008a_unexposed_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_008a_unexposed_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_008a_untrained_s1 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_008a_untrained_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_010b_cheetah_civo_trigger_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_024b_cheetah_no_dt_emb_s0 | status=DONE | conclusion=success | nve_peak=0.2 | ve_ratio_peak=None\nexp_024b_cheetah_no_dt_emb_s1 | status=DONE | conclusion=success | nve_peak=0.1 | ve_ratio_peak=None\nexp_024_cheetah_no_dt_emb_s0 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_021_full_sgs_cheetah_s1 | status=DONE | conclusion=negative | nve_peak=9.94 | ve_ratio_peak=None\nexp_023a_cheetah_baseline_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_010b_cheetah_civo_trigger | status=DONE | conclusion=success | nve_peak=8.27 | ve_ratio_peak=None\nexp_023b_cheetah_baseline_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_019b_pickcube_civo_trigger | status=DONE | conclusion=success | nve_peak=3.78 | ve_ratio_peak=None\nexp_022b_no_curriculum | status=DONE | conclusion=success | nve_peak=1.22 | ve_ratio_peak=0.218\nexp_022_untrained_dt_emb_learned_gate | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_019a_v2_pickcube_baseline | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_007_fixed_dt4 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_008c_no_subsample_dt2_h8 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_003_event_gated_v2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_004_event_gated_v3 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_005_event_gated_v4 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_008d_civo_trigger_s3 | status=DONE | conclusion=success | nve_peak=1.53 | ve_ratio_peak=None\nexp_018v2_full_sgs_walker_s1 | status=DONE | conclusion=negative | nve_peak=1.66 | ve_ratio_peak=None\nexp_018_full_sgs_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_008f_no_dt_embed_subsample_on_h8 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_016d_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_001_baseline | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_008d_civo_trigger_s2 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_008f_s3_no_dt_embed_walker | status=DONE | conclusion=success | nve_peak=< 1.5x | ve_ratio_peak=None\nexp_020_vanilla_dreamerv3_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_019a_pickcube_baseline | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_018_full_sgs_walker_s1 | status=DONE | conclusion=killed | nve_peak=0.72 | ve_ratio_peak=None\nexp_010a_cheetah_baseline_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_009d_baseline_walker_s0 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_017_subsample_off_trained_dt_emb | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\n016e | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_016e_sgs_walker_s1 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_016c_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_009h_008f_walker_s0 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_016b_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_009g_008f_walker_s0 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_009f_008f_walker_s1 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_016_sgs_walker_s1 | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None\nexp_015b_frozen_dt_emb | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_008a_no_subsample_dt2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_009d_baseline_walker_s1 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_009a_baseline_walker_s2 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_008e_v3_walker_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_008e_v3_walker_s1 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_006 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_008a | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_008c | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_008d | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_008e_v2_subsample_on_dt1_h15 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_rssm_fidelity_analysis | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_008e_v3_subsample_on_dt1_h15 | status=DONE | conclusion=success | nve_peak=None | ve_ratio_peak=None\nexp_009c_008f_walker_s2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_006_fixed_dt2 | status=DONE | conclusion=negative | nve_peak=None | ve_ratio_peak=None\nexp_008e_subsample_on_fixed_dt1 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_008e_subsample_on_dt1_h15 | status=DONE | conclusion=killed | nve_peak=None | ve_ratio_peak=None\nexp_002_event_gated | status=DONE | conclusion=failed | nve_peak=None | ve_ratio_peak=None",
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
Now I need to identify which experiments have NVE data and can be used for the threshold analysis. Let me get the detailed metrics for experiments that have nve_peak values, and also get the ve_ratio time series data. Let me first check what metrics data structure looks like for the relevant experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "f3cf433f-9285-4fb9-819a-a49c424521ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDzRaG1WrEWGUTKzDQUASe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6940,
      "cache_read_input_tokens": 26648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6940
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

_source line 19_

Now let me get detailed metrics for experiments with NVE data, including the ve_ratio time series.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "1cd78a6a-8296-4443-80dc-5ef037cec504",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDzRaG1WrEWGUTKzDQUASe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6940,
      "cache_read_input_tokens": 26648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6940
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

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01EwCdXkGNjLCn2Uti5tHhmo`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get experiments with nve_peak data\nfor eid, exp in exps.items():\n    metrics = exp.get('metrics', {})\n    nve_peak = metrics.get('nve_peak') or metrics.get('NVE_peak')\n    if nve_peak is not None and nve_peak != '< 1.5x':\n        # Also check for ve_ratio time series\n        ve_keys = [k for k in metrics.keys() if 've_ratio' in k.lower() or 'nve' in k.lower() or 've_' in k.lower()]\n        spec = exp.get('spec', {})\n        env = 'walker' if 'walker' in eid.lower() else ('cheetah' if 'cheetah' in eid.lower() else ('pickcube' if 'pickcube' in eid.lower() else ('peginsertion' if 'peg' in eid.lower() else ('stackcube' if 'stack' in eid.lower() else 'unknown'))))\n        \n        # Determine experiment type\n        is_frozen = 'frozen' in eid.lower()\n        is_no_dt = 'no_dt' in eid.lower()\n        is_baseline = 'baseline' in eid.lower()\n        is_civo = 'civo' in eid.lower() or '008d' in eid.lower() or '008e_v3' in eid.lower()\n        \n        if is_frozen:\n            exp_type = 'frozen'\n        elif is_no_dt:\n            exp_type = 'no_dt_emb'\n        elif is_baseline:\n            exp_type = 'baseline'\n        elif is_civo:\n            exp_type = 'civo_treatment'\n        else:\n            exp_type = 'other'\n        \n        conclusion = exp.get('conclusion', '')\n        print(f'{eid} | env={env} | type={exp_type} | conclusion={conclusion} | nve_peak={nve_peak} | ve_ratio_peak={metrics.get(\\\"ve_ratio_peak\\\")} | ve_keys={ve_keys}')\n\" 2>&1\n",
  "description": "Extract NVE experiments with detailed categorization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "bf72bb18-3aa0-481e-8212-0da21ee24665",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDzRaG1WrEWGUTKzDQUASe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6940,
      "cache_read_input_tokens": 26648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6940
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

_source line 21 · 2026-05-25T20:20:04.452Z_

<details><summary>↩ Tool result · `toolu_01EwCdXkGNjLCn2Uti5tHhmo`</summary>

```text
exp_009b_008d_walker_s2 | env=walker | type=civo_treatment | conclusion=negative | nve_peak=1.62 | ve_ratio_peak=0.5703 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']
exp_009e_008d_walker_s1 | env=walker | type=civo_treatment | conclusion=negative | nve_peak=4.13 | ve_ratio_peak=1.6663 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']
exp_085_frozen_dt_emb_walker_s1 | env=walker | type=frozen | conclusion=success | nve_peak=0.31 | ve_ratio_peak=None | ve_keys=['NVE_final', 'NVE_peak']
exp_084_frozen_dt_emb_walker_s0 | env=walker | type=frozen | conclusion=success | nve_peak=0.37 | ve_ratio_peak=None | ve_keys=['NVE_final', 'NVE_peak']
exp_082_cheetah_no_dt_emb_s0 | env=cheetah | type=no_dt_emb | conclusion=success | nve_peak=1.58 | ve_ratio_peak=0.955 | ve_keys=['ve_ratio_final', 've_ratio_peak', 've_ratio_peak_step', 've_ratio_trajectory', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_trajectory_35Kplus', 'nve_classification']
exp_078_cheetah_008d_s0 | env=cheetah | type=civo_treatment | conclusion=success | nve_peak=4.1 | ve_ratio_peak=2.318 | ve_keys=['ve_ratio_final', 've_ratio_peak', 've_ratio_peak_step', 've_ratio_trajectory', 'nve_peak', 'nve_peak_step', 'nve_onset_step', 'nve_onset_value', 'nve_trajectory_35Kplus', 'nve_classification', 'delta_ve_peak', 'delta_ve_peak_step']
exp_073_008f_walker_s4 | env=walker | type=other | conclusion=success | nve_peak=0.76 | ve_ratio_peak=0.5 | ve_keys=['ve_ratio_final', 've_ratio_peak', 'nve_peak']
exp_072_008e_v3_walker_s5 | env=walker | type=civo_treatment | conclusion=success | nve_peak=0.61 | ve_ratio_peak=None | ve_keys=['ve_ratio_final', 'nve_final', 'nve_peak', 'nve_peak_step']
exp_070_008e_v3_walker_s0 | env=walker | type=civo_treatment | conclusion=negative | nve_peak=0.8 | ve_ratio_peak=None | ve_keys=['ve_ratio_105k', 'nve_peak', 'nve_peak_step', 've_ratio_trajectory']
exp_069_008f_walker_repro_s1 | env=walker | type=other | conclusion=success | nve_peak=0.66 | ve_ratio_peak=0.4 | ve_keys=['ve_ratio_final', 've_ratio_peak', 've_ratio_peak_step', 'nve_final_105k', 'nve_peak', 'nve_peak_step', 've_ratio_trajectory']
exp_067_frozen_dt_emb_walker_plan015 | env=walker | type=frozen | conclusion=success | nve_peak=0.4 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_final']
exp_057 | env=unknown | type=other | conclusion=success | nve_peak=1.3 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_final']
exp_008d_civo_trigger_s4 | env=unknown | type=civo_treatment | conclusion=success | nve_peak=4.62 | ve_ratio_peak=3.0294 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']
exp_059_walker_trained_s5 | env=walker | type=other | conclusion=success | nve_peak=4.72 | ve_ratio_peak=3.3075 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 'nve_peak', 'nve_peak_note', 'nve_classification', 'nve_classification_note', 'nve_final', 'nve_final_note']
exp_057_frozen_dt_emb_walker_s2 | env=walker | type=frozen | conclusion=success | nve_peak=1.88 | ve_ratio_peak=1.283 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_classification']
exp_058_frozen_dt_emb_cheetah_s1 | env=cheetah | type=frozen | conclusion=success | nve_peak=0.78 | ve_ratio_peak=0.231 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_classification']
exp_047_frozen_dt_emb_walker_s1 | env=walker | type=frozen | conclusion=success | nve_peak=1.71 | ve_ratio_peak=1.099 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 'nve_peak', 'nve_peak_step', 'nve_final_105k']
exp_046_frozen_dt_emb_cheetah | env=cheetah | type=frozen | conclusion=success | nve_peak=1.35 | ve_ratio_peak=0.4 | ve_keys=['ve_ratio_peak', 've_ratio_final', 'nve_peak', 'nve_peak_step', 'nve_final']
exp_045_treatment_extension_008d_s3 | env=unknown | type=civo_treatment | conclusion=success | nve_peak=4.91 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_final', 've_ratio_final', 've_ratio_trajectory']
exp_043_008f_walker_s1 | env=walker | type=other | conclusion=success | nve_peak=0.808 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_final']
exp_042_frozen_dt_emb_walker | env=walker | type=frozen | conclusion=success | nve_peak=0.194 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_final']
exp_041_dual_critic_walker_s3 | env=walker | type=other | conclusion=success | nve_peak=1.5 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_final']
exp_039_narrow_dual_critic_walker_s1 | env=walker | type=other | conclusion=success | nve_peak=2.19 | ve_ratio_peak=None | ve_keys=['nve_peak']
exp_038_dual_critic_walker_s2 | env=walker | type=other | conclusion=negative | nve_peak=0.3 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak']
exp_037_wide_critic_cheetah | env=cheetah | type=other | conclusion=negative | nve_peak=3.6 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak']
exp_036_dual_critic_pickcube | env=pickcube | type=other | conclusion=negative | nve_peak=2.3 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak']
exp_035_narrow_dual_critic_walker | env=walker | type=other | conclusion=success | nve_peak=2.75 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak', 'nve_peak_step']
exp_031b_tcn_pickcube_s0_sigma05 | env=pickcube | type=other | conclusion=negative | nve_peak=3.3 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak', 'nve_peak_step', 'nve_suppressed_from_step']
exp_032_dual_critic_walker | env=walker | type=other | conclusion=success | nve_peak=1.1 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak', 'nve_peak_step']
exp_029d_tcn_walker_s3_sigma02 | env=walker | type=other | conclusion=negative | nve_peak=3.0 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 've_ratio_105K', 've_ratio_115K', 've_ratio_125K', 've_ratio_135K', 've_ratio_145K', 've_ratio_155K', 've_ratio_165K', 've_ratio_175K', 've_ratio_185K', 've_ratio_195K', 've_ratio_205K', 've_ratio_215K', 've_ratio_45K', 've_ratio_55K', 've_ratio_65K', 've_ratio_75K', 've_ratio_85K', 've_ratio_95K']
exp_029b_tcn_walker_s2_sigma02 | env=walker | type=other | conclusion=negative | nve_peak=2.765 | ve_ratio_peak=None | ve_keys=['late_stage_nve_decline', 'nve_peak', 'nve_peak_step', 've_ratio_105K', 've_ratio_115K', 've_ratio_125K', 've_ratio_135K', 've_ratio_145K', 've_ratio_155K', 've_ratio_15K', 've_ratio_165K', 've_ratio_25K', 've_ratio_35K', 've_ratio_45K', 've_ratio_55K', 've_ratio_65K', 've_ratio_75K', 've_ratio_85K', 've_ratio_95K']
exp_008e_v3_s4 | env=unknown | type=civo_treatment | conclusion=success | nve_peak=0.99 | ve_ratio_peak=None | ve_keys=['nve_note', 'nve_peak', 'nve_peak_step', 've_ratio_105k']
exp_008e_v3_s3 | env=unknown | type=civo_treatment | conclusion=negative | nve_peak=4.02 | ve_ratio_peak=None | ve_keys=['nve_note', 'nve_peak', 'nve_peak_step', 've_ratio_105k']
exp_024b_cheetah_no_dt_emb_s0 | env=cheetah | type=no_dt_emb | conclusion=success | nve_peak=0.2 | ve_ratio_peak=None | ve_keys=['nve_peak']
exp_024b_cheetah_no_dt_emb_s1 | env=cheetah | type=no_dt_emb | conclusion=success | nve_peak=0.1 | ve_ratio_peak=None | ve_keys=['nve_peak']
exp_021_full_sgs_cheetah_s1 | env=cheetah | type=other | conclusion=negative | nve_peak=9.94 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_sustained_55K_105K']
exp_010b_cheetah_civo_trigger | env=cheetah | type=civo_treatment | conclusion=success | nve_peak=8.27 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step']
exp_019b_pickcube_civo_trigger | env=pickcube | type=civo_treatment | conclusion=success | nve_peak=3.78 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak', 'nve_peak_step']
exp_022b_no_curriculum | env=unknown | type=other | conclusion=success | nve_peak=1.22 | ve_ratio_peak=0.218 | ve_keys=['nve_peak', 've_ratio_105K', 've_ratio_peak']
exp_008d_civo_trigger_s3 | env=unknown | type=civo_treatment | conclusion=success | nve_peak=1.53 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_onset_step', 'nve_onset_value', 'nve_peak', 'nve_peak_step', 'nve_sustained_45K_55K']
exp_018v2_full_sgs_walker_s1 | env=walker | type=other | conclusion=negative | nve_peak=1.66 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_mean_45k_105k', 'nve_peak', 'nve_peak_step']
exp_018_full_sgs_walker_s1 | env=walker | type=other | conclusion=killed | nve_peak=0.72 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_sustained_avg', 'nve_sustained_max']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "9da3116c-aa9c-4607-a6e1-c254dd78e665",
  "tool_use_result": {
    "stdout": "exp_009b_008d_walker_s2 | env=walker | type=civo_treatment | conclusion=negative | nve_peak=1.62 | ve_ratio_peak=0.5703 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']\nexp_009e_008d_walker_s1 | env=walker | type=civo_treatment | conclusion=negative | nve_peak=4.13 | ve_ratio_peak=1.6663 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']\nexp_085_frozen_dt_emb_walker_s1 | env=walker | type=frozen | conclusion=success | nve_peak=0.31 | ve_ratio_peak=None | ve_keys=['NVE_final', 'NVE_peak']\nexp_084_frozen_dt_emb_walker_s0 | env=walker | type=frozen | conclusion=success | nve_peak=0.37 | ve_ratio_peak=None | ve_keys=['NVE_final', 'NVE_peak']\nexp_082_cheetah_no_dt_emb_s0 | env=cheetah | type=no_dt_emb | conclusion=success | nve_peak=1.58 | ve_ratio_peak=0.955 | ve_keys=['ve_ratio_final', 've_ratio_peak', 've_ratio_peak_step', 've_ratio_trajectory', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_trajectory_35Kplus', 'nve_classification']\nexp_078_cheetah_008d_s0 | env=cheetah | type=civo_treatment | conclusion=success | nve_peak=4.1 | ve_ratio_peak=2.318 | ve_keys=['ve_ratio_final', 've_ratio_peak', 've_ratio_peak_step', 've_ratio_trajectory', 'nve_peak', 'nve_peak_step', 'nve_onset_step', 'nve_onset_value', 'nve_trajectory_35Kplus', 'nve_classification', 'delta_ve_peak', 'delta_ve_peak_step']\nexp_073_008f_walker_s4 | env=walker | type=other | conclusion=success | nve_peak=0.76 | ve_ratio_peak=0.5 | ve_keys=['ve_ratio_final', 've_ratio_peak', 'nve_peak']\nexp_072_008e_v3_walker_s5 | env=walker | type=civo_treatment | conclusion=success | nve_peak=0.61 | ve_ratio_peak=None | ve_keys=['ve_ratio_final', 'nve_final', 'nve_peak', 'nve_peak_step']\nexp_070_008e_v3_walker_s0 | env=walker | type=civo_treatment | conclusion=negative | nve_peak=0.8 | ve_ratio_peak=None | ve_keys=['ve_ratio_105k', 'nve_peak', 'nve_peak_step', 've_ratio_trajectory']\nexp_069_008f_walker_repro_s1 | env=walker | type=other | conclusion=success | nve_peak=0.66 | ve_ratio_peak=0.4 | ve_keys=['ve_ratio_final', 've_ratio_peak', 've_ratio_peak_step', 'nve_final_105k', 'nve_peak', 'nve_peak_step', 've_ratio_trajectory']\nexp_067_frozen_dt_emb_walker_plan015 | env=walker | type=frozen | conclusion=success | nve_peak=0.4 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_final']\nexp_057 | env=unknown | type=other | conclusion=success | nve_peak=1.3 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_final']\nexp_008d_civo_trigger_s4 | env=unknown | type=civo_treatment | conclusion=success | nve_peak=4.62 | ve_ratio_peak=3.0294 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']\nexp_059_walker_trained_s5 | env=walker | type=other | conclusion=success | nve_peak=4.72 | ve_ratio_peak=3.3075 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 'nve_peak', 'nve_peak_note', 'nve_classification', 'nve_classification_note', 'nve_final', 'nve_final_note']\nexp_057_frozen_dt_emb_walker_s2 | env=walker | type=frozen | conclusion=success | nve_peak=1.88 | ve_ratio_peak=1.283 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_classification']\nexp_058_frozen_dt_emb_cheetah_s1 | env=cheetah | type=frozen | conclusion=success | nve_peak=0.78 | ve_ratio_peak=0.231 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_classification']\nexp_047_frozen_dt_emb_walker_s1 | env=walker | type=frozen | conclusion=success | nve_peak=1.71 | ve_ratio_peak=1.099 | ve_keys=['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 'nve_peak', 'nve_peak_step', 'nve_final_105k']\nexp_046_frozen_dt_emb_cheetah | env=cheetah | type=frozen | conclusion=success | nve_peak=1.35 | ve_ratio_peak=0.4 | ve_keys=['ve_ratio_peak', 've_ratio_final', 'nve_peak', 'nve_peak_step', 'nve_final']\nexp_045_treatment_extension_008d_s3 | env=unknown | type=civo_treatment | conclusion=success | nve_peak=4.91 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_final', 've_ratio_final', 've_ratio_trajectory']\nexp_043_008f_walker_s1 | env=walker | type=other | conclusion=success | nve_peak=0.808 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_final']\nexp_042_frozen_dt_emb_walker | env=walker | type=frozen | conclusion=success | nve_peak=0.194 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_final']\nexp_041_dual_critic_walker_s3 | env=walker | type=other | conclusion=success | nve_peak=1.5 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_final']\nexp_039_narrow_dual_critic_walker_s1 | env=walker | type=other | conclusion=success | nve_peak=2.19 | ve_ratio_peak=None | ve_keys=['nve_peak']\nexp_038_dual_critic_walker_s2 | env=walker | type=other | conclusion=negative | nve_peak=0.3 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak']\nexp_037_wide_critic_cheetah | env=cheetah | type=other | conclusion=negative | nve_peak=3.6 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak']\nexp_036_dual_critic_pickcube | env=pickcube | type=other | conclusion=negative | nve_peak=2.3 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak']\nexp_035_narrow_dual_critic_walker | env=walker | type=other | conclusion=success | nve_peak=2.75 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak', 'nve_peak_step']\nexp_031b_tcn_pickcube_s0_sigma05 | env=pickcube | type=other | conclusion=negative | nve_peak=3.3 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak', 'nve_peak_step', 'nve_suppressed_from_step']\nexp_032_dual_critic_walker | env=walker | type=other | conclusion=success | nve_peak=1.1 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak', 'nve_peak_step']\nexp_029d_tcn_walker_s3_sigma02 | env=walker | type=other | conclusion=negative | nve_peak=3.0 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 've_ratio_105K', 've_ratio_115K', 've_ratio_125K', 've_ratio_135K', 've_ratio_145K', 've_ratio_155K', 've_ratio_165K', 've_ratio_175K', 've_ratio_185K', 've_ratio_195K', 've_ratio_205K', 've_ratio_215K', 've_ratio_45K', 've_ratio_55K', 've_ratio_65K', 've_ratio_75K', 've_ratio_85K', 've_ratio_95K']\nexp_029b_tcn_walker_s2_sigma02 | env=walker | type=other | conclusion=negative | nve_peak=2.765 | ve_ratio_peak=None | ve_keys=['late_stage_nve_decline', 'nve_peak', 'nve_peak_step', 've_ratio_105K', 've_ratio_115K', 've_ratio_125K', 've_ratio_135K', 've_ratio_145K', 've_ratio_155K', 've_ratio_15K', 've_ratio_165K', 've_ratio_25K', 've_ratio_35K', 've_ratio_45K', 've_ratio_55K', 've_ratio_65K', 've_ratio_75K', 've_ratio_85K', 've_ratio_95K']\nexp_008e_v3_s4 | env=unknown | type=civo_treatment | conclusion=success | nve_peak=0.99 | ve_ratio_peak=None | ve_keys=['nve_note', 'nve_peak', 'nve_peak_step', 've_ratio_105k']\nexp_008e_v3_s3 | env=unknown | type=civo_treatment | conclusion=negative | nve_peak=4.02 | ve_ratio_peak=None | ve_keys=['nve_note', 'nve_peak', 'nve_peak_step', 've_ratio_105k']\nexp_024b_cheetah_no_dt_emb_s0 | env=cheetah | type=no_dt_emb | conclusion=success | nve_peak=0.2 | ve_ratio_peak=None | ve_keys=['nve_peak']\nexp_024b_cheetah_no_dt_emb_s1 | env=cheetah | type=no_dt_emb | conclusion=success | nve_peak=0.1 | ve_ratio_peak=None | ve_keys=['nve_peak']\nexp_021_full_sgs_cheetah_s1 | env=cheetah | type=other | conclusion=negative | nve_peak=9.94 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_sustained_55K_105K']\nexp_010b_cheetah_civo_trigger | env=cheetah | type=civo_treatment | conclusion=success | nve_peak=8.27 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step']\nexp_019b_pickcube_civo_trigger | env=pickcube | type=civo_treatment | conclusion=success | nve_peak=3.78 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_peak', 'nve_peak_step']\nexp_022b_no_curriculum | env=unknown | type=other | conclusion=success | nve_peak=1.22 | ve_ratio_peak=0.218 | ve_keys=['nve_peak', 've_ratio_105K', 've_ratio_peak']\nexp_008d_civo_trigger_s3 | env=unknown | type=civo_treatment | conclusion=success | nve_peak=1.53 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_onset_step', 'nve_onset_value', 'nve_peak', 'nve_peak_step', 'nve_sustained_45K_55K']\nexp_018v2_full_sgs_walker_s1 | env=walker | type=other | conclusion=negative | nve_peak=1.66 | ve_ratio_peak=None | ve_keys=['nve_final', 'nve_mean_45k_105k', 'nve_peak', 'nve_peak_step']\nexp_018_full_sgs_walker_s1 | env=walker | type=other | conclusion=killed | nve_peak=0.72 | ve_ratio_peak=None | ve_keys=['nve_peak', 'nve_peak_step', 'nve_sustained_avg', 'nve_sustained_max']",
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

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. I need to also look at the specific experiments mentioned (exp_084, exp_085, exp_087, exp_086) and their detailed metrics. Let me also check for ve_ratio trajectory data and the new experiments' detailed info.

Let me also check for exp_087 and exp_086 metrics, and look at what additional NVE-related metrics are available.

Let me also get the ve_ratio time series data for the specific experiments. Many experiments have `ve_ratio_trajectory` or `ve_ratio_*K` keys. Let me extract that data.

Now let me think about the classification task:


I need to establish ground truth labels for CIVO positive cases. The experiments with treatment configs like 008d and 008e_v3 that used trained dt_emb and civo_trigger showed performance collapse, so those should be marked as true positives, while the frozen dt_emb experiments should be negative since frozen embeddings shouldn't trigger interference.

Now I'm pulling the full metrics from the key experiments, especially the ve_ratio time series data to verify which ones actually exhibited CIVO behavior.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "21663143-681a-4c3a-8c4c-8719792b6b94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UXmrt71hE2RPLeYdnkTR1K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4660,
      "cache_read_input_tokens": 33588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4660
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

Now let me extract detailed metrics including trajectory data for experiments with NVE values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "b825d07f-adf7-496b-8735-1d8d886b54f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UXmrt71hE2RPLeYdnkTR1K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4660,
      "cache_read_input_tokens": 33588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4660
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

<details open><summary>🔧 Tool call — Bash · `toolu_017UQkd9RgYrQBPjUdEzehCs`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get full metrics for experiments with NVE data\ntarget_exps = []\nfor eid, exp in exps.items():\n    metrics = exp.get('metrics', {})\n    nve_peak = metrics.get('nve_peak') or metrics.get('NVE_peak')\n    if nve_peak is not None and nve_peak != '< 1.5x':\n        target_exps.append(eid)\n\n# Print full metrics for key experiments\nfor eid in ['exp_084_frozen_dt_emb_walker_s0', 'exp_085_frozen_dt_emb_walker_s1', 'exp_087_frozen_dt_emb_cheetah_s1', 'exp_086_frozen_dt_emb_cheetah_s0']:\n    exp = exps.get(eid)\n    if exp:\n        print(f'=== {eid} ===')\n        print(f'status: {exp.get(\\\"status\\\")}')\n        print(f'conclusion: {exp.get(\\\"conclusion\\\")}')\n        print(f'metrics: {json.dumps(exp.get(\\\"metrics\\\", {}), indent=2)}')\n        print()\n\" 2>&1\n",
  "description": "Extract detailed metrics for new experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "acf4697b-28c6-4b25-a904-ab89879d1d63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UXmrt71hE2RPLeYdnkTR1K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4660,
      "cache_read_input_tokens": 33588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4660
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

_source line 25 · 2026-05-25T20:20:26.417Z_

<details><summary>↩ Tool result · `toolu_017UQkd9RgYrQBPjUdEzehCs`</summary>

```text
=== exp_084_frozen_dt_emb_walker_s0 ===
status: DONE
conclusion: success
metrics: {
  "eval_return_final": 281.48,
  "eval_return_best": 334.06,
  "best_step": 95000,
  "total_steps": 112000,
  "NVE_final": 0.31,
  "NVE_peak": 0.37,
  "gate_pattern": "100% dt=2 locked",
  "civo_alert": false
}

=== exp_085_frozen_dt_emb_walker_s1 ===
status: DONE
conclusion: success
metrics: {
  "eval_return_final": 69.26,
  "eval_return_best": 281.53,
  "best_step": 65000,
  "total_steps": 105000,
  "NVE_final": 0.08,
  "NVE_peak": 0.31,
  "gate_pattern": "100% dt=2 locked",
  "civo_alert": false
}

=== exp_087_frozen_dt_emb_cheetah_s1 ===
status: DONE
conclusion: success
metrics: {
  "eval_return_105K": 186.9,
  "eval_return_peak": 310.1,
  "eval_return_peak_step": "75K",
  "eval_trajectory": {
    "5K": 13.5,
    "15K": 90.2,
    "25K": 199.3,
    "35K": 165.7,
    "45K": 299.2,
    "55K": 207.2,
    "65K": 196.8,
    "75K": 310.1,
    "85K": 246.8,
    "95K": 57.9,
    "105K": 186.9
  },
  "ve_ratio_105K": 0.1,
  "ve_ratio_peak": 0.2,
  "ve_ratio_peak_step": "95K",
  "civo_alert": 0,
  "NVE": 0.33,
  "NVE_baseline": "exp_083_cheetah_baseline_s1",
  "NVE_baseline_ve_ratio_peak": 0.6,
  "nve_classification": "no_civo",
  "gate_dt_mean": 2,
  "gate_dt_2_frac": 1,
  "gate_empirical_entropy": 0,
  "total_steps": 112000,
  "model_loss_105K": 2.4
}

=== exp_086_frozen_dt_emb_cheetah_s0 ===
status: ANALYZING
conclusion: None
metrics: {}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "52f6eeb1-83a9-45e5-9264-c1688a3dacc5",
  "tool_use_result": {
    "stdout": "=== exp_084_frozen_dt_emb_walker_s0 ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"eval_return_final\": 281.48,\n  \"eval_return_best\": 334.06,\n  \"best_step\": 95000,\n  \"total_steps\": 112000,\n  \"NVE_final\": 0.31,\n  \"NVE_peak\": 0.37,\n  \"gate_pattern\": \"100% dt=2 locked\",\n  \"civo_alert\": false\n}\n\n=== exp_085_frozen_dt_emb_walker_s1 ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"eval_return_final\": 69.26,\n  \"eval_return_best\": 281.53,\n  \"best_step\": 65000,\n  \"total_steps\": 105000,\n  \"NVE_final\": 0.08,\n  \"NVE_peak\": 0.31,\n  \"gate_pattern\": \"100% dt=2 locked\",\n  \"civo_alert\": false\n}\n\n=== exp_087_frozen_dt_emb_cheetah_s1 ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"eval_return_105K\": 186.9,\n  \"eval_return_peak\": 310.1,\n  \"eval_return_peak_step\": \"75K\",\n  \"eval_trajectory\": {\n    \"5K\": 13.5,\n    \"15K\": 90.2,\n    \"25K\": 199.3,\n    \"35K\": 165.7,\n    \"45K\": 299.2,\n    \"55K\": 207.2,\n    \"65K\": 196.8,\n    \"75K\": 310.1,\n    \"85K\": 246.8,\n    \"95K\": 57.9,\n    \"105K\": 186.9\n  },\n  \"ve_ratio_105K\": 0.1,\n  \"ve_ratio_peak\": 0.2,\n  \"ve_ratio_peak_step\": \"95K\",\n  \"civo_alert\": 0,\n  \"NVE\": 0.33,\n  \"NVE_baseline\": \"exp_083_cheetah_baseline_s1\",\n  \"NVE_baseline_ve_ratio_peak\": 0.6,\n  \"nve_classification\": \"no_civo\",\n  \"gate_dt_mean\": 2,\n  \"gate_dt_2_frac\": 1,\n  \"gate_empirical_entropy\": 0,\n  \"total_steps\": 112000,\n  \"model_loss_105K\": 2.4\n}\n\n=== exp_086_frozen_dt_emb_cheetah_s0 ===\nstatus: ANALYZING\nconclusion: None\nmetrics: {}",
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vjj2c7moDFUpZJX89jc5eK`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get experiments with trajectory data for time series analysis\ntrajectory_exps = {}\nfor eid, exp in exps.items():\n    metrics = exp.get('metrics', {})\n    nve_peak = metrics.get('nve_peak') or metrics.get('NVE_peak')\n    if nve_peak is None or nve_peak == '< 1.5x':\n        continue\n    \n    # Check for ve_ratio trajectory or step-wise ve_ratio data\n    traj = metrics.get('ve_ratio_trajectory')\n    nve_traj = metrics.get('nve_trajectory_35Kplus')\n    \n    # Also collect ve_ratio_*K keys\n    step_ve = {}\n    for k, v in metrics.items():\n        if k.startswith('ve_ratio_') and k[-1] == 'K':\n            step_ve[k] = v\n    \n    if traj or nve_traj or step_ve:\n        print(f'=== {eid} ===')\n        if traj:\n            print(f'  ve_ratio_trajectory: {json.dumps(traj)}')\n        if nve_traj:\n            print(f'  nve_trajectory_35Kplus: {json.dumps(nve_traj)}')\n        if step_ve:\n            print(f'  step_ve_ratios: {json.dumps(step_ve)}')\n        \n        # Also get eval trajectory if available\n        eval_traj = metrics.get('eval_trajectory') or metrics.get('eval_return_trajectory')\n        if eval_traj:\n            print(f'  eval_trajectory: {json.dumps(eval_traj)}')\n        print()\n\" 2>&1\n",
  "description": "Extract ve_ratio trajectory data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "75bbd50d-019b-4f35-8a6b-605ba0cc86d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDmhXd3zDwH5zQDZUSNqcU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1759,
      "cache_read_input_tokens": 38248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1759
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

_source line 27 · 2026-05-25T20:20:39.746Z_

<details><summary>↩ Tool result · `toolu_01Vjj2c7moDFUpZJX89jc5eK`</summary>

```text
=== exp_082_cheetah_no_dt_emb_s0 ===
  ve_ratio_trajectory: {"15K": 0.038, "25K": 0.069, "35K": 0.132, "45K": 0.103, "55K": 0.237, "65K": 0.268, "75K": 0.311, "85K": 0.724, "95K": 0.955, "105K": 0.616}
  nve_trajectory_35Kplus: {"35K": 1.49, "45K": 0.59, "55K": 0.96, "65K": 0.55, "75K": 0.55, "85K": 0.98, "95K": 1.58, "105K": 1.02}
  eval_trajectory: {"5K": 6.8, "15K": 32.2, "25K": 108.4, "35K": 119.4, "45K": 239.3, "55K": 157, "65K": 180.1, "75K": 178.6, "85K": 84.2, "95K": 57.7, "105K": 83.2}

=== exp_078_cheetah_008d_s0 ===
  ve_ratio_trajectory: {"15K": 0.039, "25K": 0.056, "35K": 0.11, "45K": 0.295, "55K": 0.908, "65K": 1.72, "75K": 2.318, "85K": 2.022, "95K": 1.366, "105K": 0.291}
  nve_trajectory_35Kplus: {"35K": 1.24, "45K": 1.7, "55K": 3.66, "65K": 3.55, "75K": 4.1, "85K": 2.74, "95K": 2.26, "105K": 0.48}
  eval_trajectory: {"5K": 8.3, "15K": 41.3, "25K": 170, "35K": 213.7, "45K": 148.9, "55K": 64.5, "65K": 36.8, "75K": 26.1, "85K": 26.7, "95K": 32.5, "105K": 119.5}

=== exp_070_008e_v3_walker_s0 ===
  ve_ratio_trajectory: [{"step": 15000, "ve": 0}, {"step": 25000, "ve": 0.1}, {"step": 35000, "ve": 0.2}, {"step": 45000, "ve": 0.3}, {"step": 55000, "ve": 0.4}, {"step": 65000, "ve": 0.5}, {"step": 75000, "ve": 0.6}, {"step": 85000, "ve": 0.5}, {"step": 95000, "ve": 0.8}, {"step": 105000, "ve": 0.8}]
  eval_trajectory: [{"step": 5000, "eval_return": 37.4}, {"step": 15000, "eval_return": 93.2}, {"step": 25000, "eval_return": 178.8}, {"step": 35000, "eval_return": 221.6}, {"step": 45000, "eval_return": 230.9}, {"step": 55000, "eval_return": 232.5}, {"step": 65000, "eval_return": 194}, {"step": 75000, "eval_return": 175.2}, {"step": 85000, "eval_return": 218.6}, {"step": 95000, "eval_return": 139.6}, {"step": 105000, "eval_return": 148}]

=== exp_069_008f_walker_repro_s1 ===
  ve_ratio_trajectory: {"15k": 0, "25k": 0.1, "35k": 0.2, "45k": 0.2, "55k": 0.3, "65k": 0.3, "75k": 0.4, "85k": 0.3, "95k": 0.3, "105k": 0.4}
  eval_trajectory: {"5k": 30.5, "15k": 158.7, "25k": 180.8, "35k": 250.3, "45k": 293.6, "55k": 272.2, "65k": 328.1, "75k": 244.8, "85k": 382.5, "95k": 390.1, "105k": 237.8}

=== exp_045_treatment_extension_008d_s3 ===
  ve_ratio_trajectory: {"122000": 4.77, "132000": 4.91, "142000": 0.43, "152000": 0.21, "162000": 0.25, "172000": 0.18, "182000": 0.16, "192000": 0.13, "202000": 0.12, "212000": 0.1, "222000": 0.1, "232000": 0.09, "242000": 0.07, "252000": 0.08, "262000": 0.07, "272000": 0.08, "282000": 0.07, "292000": 0.06, "302000": 0.05}
  eval_trajectory: {"112000": 58.5, "122000": 41.8, "132000": 35.1, "142000": 350.2, "152000": 646.4, "162000": 482.3, "172000": 600.4, "182000": 600.5, "192000": 699.5, "202000": 684.3, "212000": 758.6, "222000": 744.6, "232000": 745.4, "242000": 869.7, "252000": 721.6, "262000": 820.6, "272000": 716.2, "282000": 755.6, "292000": 843, "302000": 867.6}

=== exp_029d_tcn_walker_s3_sigma02 ===
  step_ve_ratios: {"ve_ratio_105K": 3.0, "ve_ratio_115K": 2.5, "ve_ratio_125K": 2.4, "ve_ratio_135K": 0.9, "ve_ratio_145K": 1.141, "ve_ratio_155K": 1.06, "ve_ratio_165K": 0.91, "ve_ratio_175K": 0.556, "ve_ratio_185K": 0.396, "ve_ratio_195K": 0.78, "ve_ratio_205K": 0.747, "ve_ratio_215K": 0.4, "ve_ratio_45K": 0.695, "ve_ratio_55K": 0.598, "ve_ratio_65K": 0.863, "ve_ratio_75K": 0.791, "ve_ratio_85K": 0.9, "ve_ratio_95K": 0.7}

=== exp_029b_tcn_walker_s2_sigma02 ===
  step_ve_ratios: {"ve_ratio_105K": 2.765, "ve_ratio_115K": 2.326, "ve_ratio_125K": 2.278, "ve_ratio_135K": 1.648, "ve_ratio_145K": 1.234, "ve_ratio_155K": 1.061, "ve_ratio_15K": 0.03, "ve_ratio_165K": 1.226, "ve_ratio_25K": 0.174, "ve_ratio_35K": 0.335, "ve_ratio_45K": 0.477, "ve_ratio_55K": 0.583, "ve_ratio_65K": 1.014, "ve_ratio_75K": 1.65, "ve_ratio_85K": 1.623, "ve_ratio_95K": 2.109}

=== exp_022b_no_curriculum ===
  step_ve_ratios: {"ve_ratio_105K": 0.075}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "f2a5d704-b773-4ef1-9761-2dc01c94ea05",
  "tool_use_result": {
    "stdout": "=== exp_082_cheetah_no_dt_emb_s0 ===\n  ve_ratio_trajectory: {\"15K\": 0.038, \"25K\": 0.069, \"35K\": 0.132, \"45K\": 0.103, \"55K\": 0.237, \"65K\": 0.268, \"75K\": 0.311, \"85K\": 0.724, \"95K\": 0.955, \"105K\": 0.616}\n  nve_trajectory_35Kplus: {\"35K\": 1.49, \"45K\": 0.59, \"55K\": 0.96, \"65K\": 0.55, \"75K\": 0.55, \"85K\": 0.98, \"95K\": 1.58, \"105K\": 1.02}\n  eval_trajectory: {\"5K\": 6.8, \"15K\": 32.2, \"25K\": 108.4, \"35K\": 119.4, \"45K\": 239.3, \"55K\": 157, \"65K\": 180.1, \"75K\": 178.6, \"85K\": 84.2, \"95K\": 57.7, \"105K\": 83.2}\n\n=== exp_078_cheetah_008d_s0 ===\n  ve_ratio_trajectory: {\"15K\": 0.039, \"25K\": 0.056, \"35K\": 0.11, \"45K\": 0.295, \"55K\": 0.908, \"65K\": 1.72, \"75K\": 2.318, \"85K\": 2.022, \"95K\": 1.366, \"105K\": 0.291}\n  nve_trajectory_35Kplus: {\"35K\": 1.24, \"45K\": 1.7, \"55K\": 3.66, \"65K\": 3.55, \"75K\": 4.1, \"85K\": 2.74, \"95K\": 2.26, \"105K\": 0.48}\n  eval_trajectory: {\"5K\": 8.3, \"15K\": 41.3, \"25K\": 170, \"35K\": 213.7, \"45K\": 148.9, \"55K\": 64.5, \"65K\": 36.8, \"75K\": 26.1, \"85K\": 26.7, \"95K\": 32.5, \"105K\": 119.5}\n\n=== exp_070_008e_v3_walker_s0 ===\n  ve_ratio_trajectory: [{\"step\": 15000, \"ve\": 0}, {\"step\": 25000, \"ve\": 0.1}, {\"step\": 35000, \"ve\": 0.2}, {\"step\": 45000, \"ve\": 0.3}, {\"step\": 55000, \"ve\": 0.4}, {\"step\": 65000, \"ve\": 0.5}, {\"step\": 75000, \"ve\": 0.6}, {\"step\": 85000, \"ve\": 0.5}, {\"step\": 95000, \"ve\": 0.8}, {\"step\": 105000, \"ve\": 0.8}]\n  eval_trajectory: [{\"step\": 5000, \"eval_return\": 37.4}, {\"step\": 15000, \"eval_return\": 93.2}, {\"step\": 25000, \"eval_return\": 178.8}, {\"step\": 35000, \"eval_return\": 221.6}, {\"step\": 45000, \"eval_return\": 230.9}, {\"step\": 55000, \"eval_return\": 232.5}, {\"step\": 65000, \"eval_return\": 194}, {\"step\": 75000, \"eval_return\": 175.2}, {\"step\": 85000, \"eval_return\": 218.6}, {\"step\": 95000, \"eval_return\": 139.6}, {\"step\": 105000, \"eval_return\": 148}]\n\n=== exp_069_008f_walker_repro_s1 ===\n  ve_ratio_trajectory: {\"15k\": 0, \"25k\": 0.1, \"35k\": 0.2, \"45k\": 0.2, \"55k\": 0.3, \"65k\": 0.3, \"75k\": 0.4, \"85k\": 0.3, \"95k\": 0.3, \"105k\": 0.4}\n  eval_trajectory: {\"5k\": 30.5, \"15k\": 158.7, \"25k\": 180.8, \"35k\": 250.3, \"45k\": 293.6, \"55k\": 272.2, \"65k\": 328.1, \"75k\": 244.8, \"85k\": 382.5, \"95k\": 390.1, \"105k\": 237.8}\n\n=== exp_045_treatment_extension_008d_s3 ===\n  ve_ratio_trajectory: {\"122000\": 4.77, \"132000\": 4.91, \"142000\": 0.43, \"152000\": 0.21, \"162000\": 0.25, \"172000\": 0.18, \"182000\": 0.16, \"192000\": 0.13, \"202000\": 0.12, \"212000\": 0.1, \"222000\": 0.1, \"232000\": 0.09, \"242000\": 0.07, \"252000\": 0.08, \"262000\": 0.07, \"272000\": 0.08, \"282000\": 0.07, \"292000\": 0.06, \"302000\": 0.05}\n  eval_trajectory: {\"112000\": 58.5, \"122000\": 41.8, \"132000\": 35.1, \"142000\": 350.2, \"152000\": 646.4, \"162000\": 482.3, \"172000\": 600.4, \"182000\": 600.5, \"192000\": 699.5, \"202000\": 684.3, \"212000\": 758.6, \"222000\": 744.6, \"232000\": 745.4, \"242000\": 869.7, \"252000\": 721.6, \"262000\": 820.6, \"272000\": 716.2, \"282000\": 755.6, \"292000\": 843, \"302000\": 867.6}\n\n=== exp_029d_tcn_walker_s3_sigma02 ===\n  step_ve_ratios: {\"ve_ratio_105K\": 3.0, \"ve_ratio_115K\": 2.5, \"ve_ratio_125K\": 2.4, \"ve_ratio_135K\": 0.9, \"ve_ratio_145K\": 1.141, \"ve_ratio_155K\": 1.06, \"ve_ratio_165K\": 0.91, \"ve_ratio_175K\": 0.556, \"ve_ratio_185K\": 0.396, \"ve_ratio_195K\": 0.78, \"ve_ratio_205K\": 0.747, \"ve_ratio_215K\": 0.4, \"ve_ratio_45K\": 0.695, \"ve_ratio_55K\": 0.598, \"ve_ratio_65K\": 0.863, \"ve_ratio_75K\": 0.791, \"ve_ratio_85K\": 0.9, \"ve_ratio_95K\": 0.7}\n\n=== exp_029b_tcn_walker_s2_sigma02 ===\n  step_ve_ratios: {\"ve_ratio_105K\": 2.765, \"ve_ratio_115K\": 2.326, \"ve_ratio_125K\": 2.278, \"ve_ratio_135K\": 1.648, \"ve_ratio_145K\": 1.234, \"ve_ratio_155K\": 1.061, \"ve_ratio_15K\": 0.03, \"ve_ratio_165K\": 1.226, \"ve_ratio_25K\": 0.174, \"ve_ratio_35K\": 0.335, \"ve_ratio_45K\": 0.477, \"ve_ratio_55K\": 0.583, \"ve_ratio_65K\": 1.014, \"ve_ratio_75K\": 1.65, \"ve_ratio_85K\": 1.623, \"ve_ratio_95K\": 2.109}\n\n=== exp_022b_no_curriculum ===\n  step_ve_ratios: {\"ve_ratio_105K\": 0.075}",
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_017hHzCRHySW4SZ2ndJysjcc`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get full metrics dump for specific additional experiments we need\nfor eid in ['exp_009b_008d_walker_s2', 'exp_009e_008d_walker_s1', 'exp_059_walker_trained_s5', \n            'exp_008d_civo_trigger_s4', 'exp_008d_civo_trigger_s3', 'exp_008e_v3_s4', 'exp_008e_v3_s3',\n            'exp_057_frozen_dt_emb_walker_s2', 'exp_047_frozen_dt_emb_walker_s1', 'exp_046_frozen_dt_emb_cheetah',\n            'exp_058_frozen_dt_emb_cheetah_s1', 'exp_042_frozen_dt_emb_walker', 'exp_067_frozen_dt_emb_walker_plan015',\n            'exp_087_frozen_dt_emb_cheetah_s1',\n            'exp_077_cheetah_baseline_s0', 'exp_083_cheetah_baseline_s1', 'exp_071_008f_walker_s3']:\n    exp = exps.get(eid)\n    if exp:\n        metrics = exp.get('metrics', {})\n        print(f'=== {eid} ===')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n        print(f'  nve_peak: {metrics.get(\\\"nve_peak\\\") or metrics.get(\\\"NVE_peak\\\")}')\n        print(f'  nve_final: {metrics.get(\\\"nve_final\\\") or metrics.get(\\\"NVE_final\\\")}')\n        print(f'  ve_ratio_peak: {metrics.get(\\\"ve_ratio_peak\\\")}')\n        print(f'  ve_ratio_final: {metrics.get(\\\"ve_ratio_final\\\")}')\n        print(f'  nve_classification: {metrics.get(\\\"nve_classification\\\")}')\n        # Get eval data\n        eval_best = metrics.get('eval_return_best') or metrics.get('eval_return_peak')\n        eval_final = metrics.get('eval_return_final') or metrics.get('eval_return_105K')\n        print(f'  eval_best: {eval_best}, eval_final: {eval_final}')\n        # NVE note\n        nve_note = metrics.get('nve_peak_note') or metrics.get('nve_note')\n        if nve_note:\n            print(f'  nve_note: {nve_note}')\n        print()\n\" 2>&1\n",
  "description": "Extract detailed metrics for classification-relevant experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "86b4f0be-b5ea-4944-ad35-125ceeff988b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKzQfHsEtXVn1izbYSjtaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2764,
      "cache_read_input_tokens": 40007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2764
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

_source line 29 · 2026-05-25T20:20:56.904Z_

<details><summary>↩ Tool result · `toolu_017hHzCRHySW4SZ2ndJysjcc`</summary>

```text
=== exp_009b_008d_walker_s2 ===
  conclusion: negative
  nve_peak: 1.62
  nve_final: None
  ve_ratio_peak: 0.5703
  ve_ratio_final: 0.25
  nve_classification: onset_self_correcting
  eval_best: None, eval_final: None
  nve_note: step-matched s1 baseline @45K = 0.331; arithmetic peak @25K=2.04x excluded (baseline<0.1)

=== exp_009e_008d_walker_s1 ===
  conclusion: negative
  nve_peak: 4.13
  nve_final: None
  ve_ratio_peak: 1.6663
  ve_ratio_final: 1.03
  nve_classification: onset_collapse
  eval_best: None, eval_final: None
  nve_note: step-matched s1 baseline @55K = 0.4035; paper onset NVE @45K = 2.09x

=== exp_059_walker_trained_s5 ===
  conclusion: success
  nve_peak: 4.72
  nve_final: 1.22
  ve_ratio_peak: 3.3075
  ve_ratio_final: None
  nve_classification: onset_collapse
  eval_best: None, eval_final: None
  nve_note: step-matched s1 baseline @85K = 0.7007

=== exp_008d_civo_trigger_s4 ===
  conclusion: success
  nve_peak: 4.62
  nve_final: None
  ve_ratio_peak: 3.0294
  ve_ratio_final: 3.0294
  nve_classification: onset_collapse
  eval_best: None, eval_final: None
  nve_note: step-matched s1 baseline @105K = 0.6564

=== exp_008d_civo_trigger_s3 ===
  conclusion: success
  nve_peak: 1.53
  nve_final: 1.53
  ve_ratio_peak: None
  ve_ratio_final: None
  nve_classification: None
  eval_best: 451.7, eval_final: 267.6

=== exp_008e_v3_s4 ===
  conclusion: success
  nve_peak: 0.99
  nve_final: None
  ve_ratio_peak: None
  ve_ratio_final: None
  nve_classification: None
  eval_best: None, eval_final: None
  nve_note: Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K

=== exp_008e_v3_s3 ===
  conclusion: negative
  nve_peak: 4.02
  nve_final: None
  ve_ratio_peak: None
  ve_ratio_final: None
  nve_classification: None
  eval_best: None, eval_final: None
  nve_note: Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02

=== exp_057_frozen_dt_emb_walker_s2 ===
  conclusion: success
  nve_peak: 1.88
  nve_final: None
  ve_ratio_peak: 1.283
  ve_ratio_final: 0.177
  nve_classification: transient
  eval_best: 221.72, eval_final: 123.94

=== exp_047_frozen_dt_emb_walker_s1 ===
  conclusion: success
  nve_peak: 1.71
  nve_final: None
  ve_ratio_peak: 1.099
  ve_ratio_final: 0.277
  nve_classification: None
  eval_best: None, eval_final: None

=== exp_046_frozen_dt_emb_cheetah ===
  conclusion: success
  nve_peak: 1.35
  nve_final: 0.17
  ve_ratio_peak: 0.4
  ve_ratio_final: 0.1
  nve_classification: None
  eval_best: None, eval_final: None

=== exp_058_frozen_dt_emb_cheetah_s1 ===
  conclusion: success
  nve_peak: 0.78
  nve_final: None
  ve_ratio_peak: 0.231
  ve_ratio_final: 0.107
  nve_classification: no_civo
  eval_best: 191.74, eval_final: 80.46

=== exp_042_frozen_dt_emb_walker ===
  conclusion: success
  nve_peak: 0.194
  nve_final: 0.051
  ve_ratio_peak: None
  ve_ratio_final: None
  nve_classification: None
  eval_best: None, eval_final: None

=== exp_067_frozen_dt_emb_walker_plan015 ===
  conclusion: success
  nve_peak: 0.4
  nve_final: 0.2
  ve_ratio_peak: None
  ve_ratio_final: None
  nve_classification: None
  eval_best: None, eval_final: None

=== exp_087_frozen_dt_emb_cheetah_s1 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 0.2
  ve_ratio_final: None
  nve_classification: no_civo
  eval_best: 310.1, eval_final: 186.9

=== exp_077_cheetah_baseline_s0 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 0.739
  ve_ratio_final: None
  nve_classification: None
  eval_best: None, eval_final: 448.1

=== exp_083_cheetah_baseline_s1 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 0.6
  ve_ratio_final: None
  nve_classification: None
  eval_best: None, eval_final: 444

=== exp_071_008f_walker_s3 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 0.7
  ve_ratio_final: 0.4
  nve_classification: None
  eval_best: 457.7, eval_final: 311.9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "59448aeb-0417-47d2-ab05-dcbbeca763cc",
  "tool_use_result": {
    "stdout": "=== exp_009b_008d_walker_s2 ===\n  conclusion: negative\n  nve_peak: 1.62\n  nve_final: None\n  ve_ratio_peak: 0.5703\n  ve_ratio_final: 0.25\n  nve_classification: onset_self_correcting\n  eval_best: None, eval_final: None\n  nve_note: step-matched s1 baseline @45K = 0.331; arithmetic peak @25K=2.04x excluded (baseline<0.1)\n\n=== exp_009e_008d_walker_s1 ===\n  conclusion: negative\n  nve_peak: 4.13\n  nve_final: None\n  ve_ratio_peak: 1.6663\n  ve_ratio_final: 1.03\n  nve_classification: onset_collapse\n  eval_best: None, eval_final: None\n  nve_note: step-matched s1 baseline @55K = 0.4035; paper onset NVE @45K = 2.09x\n\n=== exp_059_walker_trained_s5 ===\n  conclusion: success\n  nve_peak: 4.72\n  nve_final: 1.22\n  ve_ratio_peak: 3.3075\n  ve_ratio_final: None\n  nve_classification: onset_collapse\n  eval_best: None, eval_final: None\n  nve_note: step-matched s1 baseline @85K = 0.7007\n\n=== exp_008d_civo_trigger_s4 ===\n  conclusion: success\n  nve_peak: 4.62\n  nve_final: None\n  ve_ratio_peak: 3.0294\n  ve_ratio_final: 3.0294\n  nve_classification: onset_collapse\n  eval_best: None, eval_final: None\n  nve_note: step-matched s1 baseline @105K = 0.6564\n\n=== exp_008d_civo_trigger_s3 ===\n  conclusion: success\n  nve_peak: 1.53\n  nve_final: 1.53\n  ve_ratio_peak: None\n  ve_ratio_final: None\n  nve_classification: None\n  eval_best: 451.7, eval_final: 267.6\n\n=== exp_008e_v3_s4 ===\n  conclusion: success\n  nve_peak: 0.99\n  nve_final: None\n  ve_ratio_peak: None\n  ve_ratio_final: None\n  nve_classification: None\n  eval_best: None, eval_final: None\n  nve_note: Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K\n\n=== exp_008e_v3_s3 ===\n  conclusion: negative\n  nve_peak: 4.02\n  nve_final: None\n  ve_ratio_peak: None\n  ve_ratio_final: None\n  nve_classification: None\n  eval_best: None, eval_final: None\n  nve_note: Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02\n\n=== exp_057_frozen_dt_emb_walker_s2 ===\n  conclusion: success\n  nve_peak: 1.88\n  nve_final: None\n  ve_ratio_peak: 1.283\n  ve_ratio_final: 0.177\n  nve_classification: transient\n  eval_best: 221.72, eval_final: 123.94\n\n=== exp_047_frozen_dt_emb_walker_s1 ===\n  conclusion: success\n  nve_peak: 1.71\n  nve_final: None\n  ve_ratio_peak: 1.099\n  ve_ratio_final: 0.277\n  nve_classification: None\n  eval_best: None, eval_final: None\n\n=== exp_046_frozen_dt_emb_cheetah ===\n  conclusion: success\n  nve_peak: 1.35\n  nve_final: 0.17\n  ve_ratio_peak: 0.4\n  ve_ratio_final: 0.1\n  nve_classification: None\n  eval_best: None, eval_final: None\n\n=== exp_058_frozen_dt_emb_cheetah_s1 ===\n  conclusion: success\n  nve_peak: 0.78\n  nve_final: None\n  ve_ratio_peak: 0.231\n  ve_ratio_final: 0.107\n  nve_classification: no_civo\n  eval_best: 191.74, eval_final: 80.46\n\n=== exp_042_frozen_dt_emb_walker ===\n  conclusion: success\n  nve_peak: 0.194\n  nve_final: 0.051\n  ve_ratio_peak: None\n  ve_ratio_final: None\n  nve_classification: None\n  eval_best: None, eval_final: None\n\n=== exp_067_frozen_dt_emb_walker_plan015 ===\n  conclusion: success\n  nve_peak: 0.4\n  nve_final: 0.2\n  ve_ratio_peak: None\n  ve_ratio_final: None\n  nve_classification: None\n  eval_best: None, eval_final: None\n\n=== exp_087_frozen_dt_emb_cheetah_s1 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 0.2\n  ve_ratio_final: None\n  nve_classification: no_civo\n  eval_best: 310.1, eval_final: 186.9\n\n=== exp_077_cheetah_baseline_s0 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 0.739\n  ve_ratio_final: None\n  nve_classification: None\n  eval_best: None, eval_final: 448.1\n\n=== exp_083_cheetah_baseline_s1 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 0.6\n  ve_ratio_final: None\n  nve_classification: None\n  eval_best: None, eval_final: 444\n\n=== exp_071_008f_walker_s3 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 0.7\n  ve_ratio_final: 0.4\n  nve_classification: None\n  eval_best: 457.7, eval_final: 311.9",
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

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I need to get additional data including more experiments with metrics. Let me also look at ManipSuite experiments and others.

Let me also get some missing experiments' data:
- exp_087 has NVE=0.33 in its metrics (as "NVE" key), not "nve_peak" - I found this earlier
- exp_051_stackcube_frozen_dt_emb_s0 
- exp_049_stackcube_civo_trigger_s0
- exp_052_stackcube_civo_trigger_s1
- exp_050, exp_055, exp_056 (PegInsertion)


- exp_048 (cheetah civo extension)
- exp_044 (gradient stop)
- exp_033 (wide critic)

I need to pull the full metrics for all remaining experiments with NVE values and assign labels, then cross-reference which ones belong to plan_034 V1 to calculate the delta against the existing V1 analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "09d14b2e-d576-4044-a1ee-84c6e50103e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WHEAmSZoLGN2aEH4CRrXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2653,
      "cache_read_input_tokens": 42771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2653
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

Let me check the existing V1 analysis and get remaining experiment metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "c1854b8a-23bf-4cb7-a057-649e5140d2e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WHEAmSZoLGN2aEH4CRrXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2653,
      "cache_read_input_tokens": 42771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2653
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

<details open><summary>🔧 Tool call — Glob · `toolu_01WGNTX9CLe8MkME6Y5zeePJ`</summary>

```json
{
  "pattern": "**/plan_034*/**",
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
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "ef6ce7d1-ca1a-4ab8-800c-46511163048c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WHEAmSZoLGN2aEH4CRrXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2653,
      "cache_read_input_tokens": 42771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2653
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

_source line 33 · 2026-05-25T20:21:08.005Z_

<details><summary>↩ Tool result · `toolu_01WGNTX9CLe8MkME6Y5zeePJ`</summary>

```text
artifacts/plan_034_nve_threshold/nve_threshold_analysis.py
artifacts/plan_034_nve_threshold/plot_nve_figures.py
artifacts/plan_034_nve_threshold/fig_roc_curve.pdf
artifacts/plan_034_nve_threshold/fig_roc_curve.png
artifacts/plan_034_nve_threshold/fig_threshold_prf.pdf
artifacts/plan_034_nve_threshold/fig_threshold_prf.png
artifacts/plan_034_nve_threshold/loco_cv_analysis.py
artifacts/plan_034_nve_threshold/loco_cv_results.md
artifacts/plan_034_nve_threshold/analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "ca09816c-24dc-4d5b-a1b6-76f022611b39",
  "tool_use_result": {
    "filenames": [
      "artifacts/plan_034_nve_threshold/nve_threshold_analysis.py",
      "artifacts/plan_034_nve_threshold/plot_nve_figures.py",
      "artifacts/plan_034_nve_threshold/fig_roc_curve.pdf",
      "artifacts/plan_034_nve_threshold/fig_roc_curve.png",
      "artifacts/plan_034_nve_threshold/fig_threshold_prf.pdf",
      "artifacts/plan_034_nve_threshold/fig_threshold_prf.png",
      "artifacts/plan_034_nve_threshold/loco_cv_analysis.py",
      "artifacts/plan_034_nve_threshold/loco_cv_results.md",
      "artifacts/plan_034_nve_threshold/analysis.md"
    ],
    "durationMs": 15,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01FG1uckSK2i32NnACqge1mb`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get remaining experiments with NVE data\nfor eid in ['exp_051_stackcube_frozen_dt_emb_s0', 'exp_049_stackcube_civo_trigger_s0',\n            'exp_052_stackcube_civo_trigger_s1', 'exp_048_cheetah_civo_extension',\n            'exp_050_peginsertion_civo_trigger_s0', 'exp_055_peginsertion_civo_trigger_s1',\n            'exp_053_peginsertion_frozen_s0', 'exp_056_peginsertion_frozen_s1',\n            'exp_044_gradient_stop_walker', 'exp_033_wide_critic_walker',\n            'exp_034_dual_critic_cheetah', 'exp_010b_cheetah_civo_trigger',\n            'exp_019b_pickcube_civo_trigger', 'exp_021_full_sgs_cheetah_s1',\n            'exp_031_tcn_pickcube_s0_sigma02', 'exp_031b_tcn_pickcube_s0_sigma05']:\n    exp = exps.get(eid)\n    if exp:\n        metrics = exp.get('metrics', {})\n        print(f'=== {eid} ===')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n        print(f'  nve_peak: {metrics.get(\\\"nve_peak\\\") or metrics.get(\\\"NVE_peak\\\")}')\n        print(f'  nve_final: {metrics.get(\\\"nve_final\\\") or metrics.get(\\\"NVE_final\\\")}')\n        print(f'  ve_ratio_peak: {metrics.get(\\\"ve_ratio_peak\\\")}')\n        print(f'  nve_classification: {metrics.get(\\\"nve_classification\\\")}')\n        # look for trajectory\n        traj = metrics.get('ve_ratio_trajectory') or metrics.get('nve_trajectory_35Kplus')\n        if traj:\n            print(f'  trajectory: {json.dumps(traj)}')\n        print()\n\" 2>&1\n",
  "description": "Get remaining experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "af217ac7-c4a2-42ea-b6ef-4477e0146cf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WHEAmSZoLGN2aEH4CRrXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2653,
      "cache_read_input_tokens": 42771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2653
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

_source line 35 · 2026-05-25T20:21:19.802Z_

<details><summary>↩ Tool result · `toolu_01FG1uckSK2i32NnACqge1mb`</summary>

```text
=== exp_051_stackcube_frozen_dt_emb_s0 ===
  conclusion: negative
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 4.3
  nve_classification: onset_self_correcting

=== exp_049_stackcube_civo_trigger_s0 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 5.048
  nve_classification: onset_self_correcting

=== exp_052_stackcube_civo_trigger_s1 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 4.67
  nve_classification: None

=== exp_048_cheetah_civo_extension ===
  conclusion: success
  nve_peak: None
  nve_final: 2.75
  ve_ratio_peak: 24.112
  nve_classification: None

=== exp_050_peginsertion_civo_trigger_s0 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 10.05
  nve_classification: None

=== exp_055_peginsertion_civo_trigger_s1 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 3.08
  nve_classification: transient
  trajectory: {"12500": 0.19, "22500": 0.81, "32500": 1.35, "42500": 2.0, "52500": 2.39, "62500": 2.85, "72500": 2.28, "82500": 2.48, "92500": 3.08, "102500": 2.51, "112500": 0.91, "122500": 1.21, "132500": 1.36, "142500": 0.75, "152500": 0.55, "162500": 1.17, "172500": 0.96, "182500": 0.94, "192500": 0.9, "202500": 0.73, "212500": 0.5}

=== exp_053_peginsertion_frozen_s0 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: None
  nve_classification: None

=== exp_056_peginsertion_frozen_s1 ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 11.321
  nve_classification: burst
  trajectory: {"12500": 0.316, "22500": 0.975, "32500": 1.839, "42500": 1.966, "52500": 5.422, "62500": 4.047, "72500": 8.408, "82500": 11.321, "92500": 3.724, "102500": 3.034, "112500": 2.204, "122500": 2.425, "132500": 0.842, "142500": 2.194, "152500": 2.203, "162500": 0.651, "172500": 1.085, "182500": 1.07, "192500": 0.467, "202500": 0.708, "212500": 1.193}

=== exp_044_gradient_stop_walker ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 4.4
  nve_classification: None

=== exp_033_wide_critic_walker ===
  conclusion: success
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 4.7
  nve_classification: None

=== exp_034_dual_critic_cheetah ===
  conclusion: negative
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 1.8
  nve_classification: None

=== exp_010b_cheetah_civo_trigger ===
  conclusion: success
  nve_peak: 8.27
  nve_final: None
  ve_ratio_peak: None
  nve_classification: None

=== exp_019b_pickcube_civo_trigger ===
  conclusion: success
  nve_peak: 3.78
  nve_final: 0.065
  ve_ratio_peak: None
  nve_classification: None

=== exp_021_full_sgs_cheetah_s1 ===
  conclusion: negative
  nve_peak: 9.94
  nve_final: None
  ve_ratio_peak: None
  nve_classification: None

=== exp_031_tcn_pickcube_s0_sigma02 ===
  conclusion: negative
  nve_peak: None
  nve_final: None
  ve_ratio_peak: 3.71
  nve_classification: None

=== exp_031b_tcn_pickcube_s0_sigma05 ===
  conclusion: negative
  nve_peak: 3.3
  nve_final: 0.2
  ve_ratio_peak: None
  nve_classification: None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "d0836dd1-f906-44a3-be5c-0aff8f61338e",
  "tool_use_result": {
    "stdout": "=== exp_051_stackcube_frozen_dt_emb_s0 ===\n  conclusion: negative\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 4.3\n  nve_classification: onset_self_correcting\n\n=== exp_049_stackcube_civo_trigger_s0 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 5.048\n  nve_classification: onset_self_correcting\n\n=== exp_052_stackcube_civo_trigger_s1 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 4.67\n  nve_classification: None\n\n=== exp_048_cheetah_civo_extension ===\n  conclusion: success\n  nve_peak: None\n  nve_final: 2.75\n  ve_ratio_peak: 24.112\n  nve_classification: None\n\n=== exp_050_peginsertion_civo_trigger_s0 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 10.05\n  nve_classification: None\n\n=== exp_055_peginsertion_civo_trigger_s1 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 3.08\n  nve_classification: transient\n  trajectory: {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2.0, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}\n\n=== exp_053_peginsertion_frozen_s0 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: None\n  nve_classification: None\n\n=== exp_056_peginsertion_frozen_s1 ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 11.321\n  nve_classification: burst\n  trajectory: {\"12500\": 0.316, \"22500\": 0.975, \"32500\": 1.839, \"42500\": 1.966, \"52500\": 5.422, \"62500\": 4.047, \"72500\": 8.408, \"82500\": 11.321, \"92500\": 3.724, \"102500\": 3.034, \"112500\": 2.204, \"122500\": 2.425, \"132500\": 0.842, \"142500\": 2.194, \"152500\": 2.203, \"162500\": 0.651, \"172500\": 1.085, \"182500\": 1.07, \"192500\": 0.467, \"202500\": 0.708, \"212500\": 1.193}\n\n=== exp_044_gradient_stop_walker ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 4.4\n  nve_classification: None\n\n=== exp_033_wide_critic_walker ===\n  conclusion: success\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 4.7\n  nve_classification: None\n\n=== exp_034_dual_critic_cheetah ===\n  conclusion: negative\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 1.8\n  nve_classification: None\n\n=== exp_010b_cheetah_civo_trigger ===\n  conclusion: success\n  nve_peak: 8.27\n  nve_final: None\n  ve_ratio_peak: None\n  nve_classification: None\n\n=== exp_019b_pickcube_civo_trigger ===\n  conclusion: success\n  nve_peak: 3.78\n  nve_final: 0.065\n  ve_ratio_peak: None\n  nve_classification: None\n\n=== exp_021_full_sgs_cheetah_s1 ===\n  conclusion: negative\n  nve_peak: 9.94\n  nve_final: None\n  ve_ratio_peak: None\n  nve_classification: None\n\n=== exp_031_tcn_pickcube_s0_sigma02 ===\n  conclusion: negative\n  nve_peak: None\n  nve_final: None\n  ve_ratio_peak: 3.71\n  nve_classification: None\n\n=== exp_031b_tcn_pickcube_s0_sigma05 ===\n  conclusion: negative\n  nve_peak: 3.3\n  nve_final: 0.2\n  ve_ratio_peak: None\n  nve_classification: None",
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

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01AsKRNQPmit55s1Jv3G2Ud1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "8893ab4a-5585-4a59-ba2c-a0d92686ce2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fRz1qQxxuJ6v1RM6LfiPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2725,
      "cache_read_input_tokens": 45424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2725
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

_source line 37 · 2026-05-25T20:21:26.369Z_

<details><summary>↩ Tool result · `toolu_01AsKRNQPmit55s1Jv3G2Ud1`</summary>

```text
1	# NVE Threshold Sensitivity Analysis
2	
3	**Updated: 2026-05-25** (added exp_078, exp_082, exp_084, exp_085, exp_087; total N=61)
4	
5	## 数据集
6	
7	样本总数: 61 (Collapsed: 25, Healthy: 36)
8	
9	| exp_id | env | config | seed | ground_truth | peak_nve | nve_source |
10	|--------|-----|--------|------|-------------|----------|------------|
11	| exp_006_fixed_dt2 | walker | 006_fixed_dt2 | 1 | CIVO(1) | 4.835 | computed ve_ratio/baseline at 65K |
12	| exp_008a_cheetah_unexposed_s0 | cheetah | 008a_unexposed | 0 | Healthy(0) | 0.490 | max(nve_105k) |
13	| exp_008a_cheetah_unexposed_s1 | cheetah | 008a_unexposed | 1 | Healthy(0) | 0.478 | max(nve_105k) |
14	| exp_008a_no_subsample_dt2 | walker | 008a_unexposed | 1 | Healthy(0) | 0.930 | max(normalized_ve) |
15	| exp_008a_unexposed_s1 | walker | 008a_unexposed | 1 | Healthy(0) | 0.598 | computed |
16	| exp_008a_unexposed_s2 | walker | 008a_unexposed | 2 | Healthy(0) | 0.463 | computed |
17	| exp_008d_civo_trigger_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 1.530 | metrics.nve_peak |
18	| exp_008d_civo_trigger_s4 | walker | 008d_civo_trigger | 4 | CIVO(1) | 4.620 | metrics.nve_peak |
19	| exp_008d_subsample_on_h8 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.124 | computed |
20	| exp_008e_v3_s3 | walker | 008e_v3_mitigation | 3 | CIVO(1) | 4.020 | metrics.nve_peak |
21	| exp_008e_v3_s4 | walker | 008e_v3_mitigation | 4 | Healthy(0) | 0.990 | metrics.nve_peak |
22	| exp_008e_v3_subsample_on_dt1_h15 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 1.930 | max(normalized_ve) at 25K |
23	| exp_008e_v3_walker_s1 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 0.803 | computed |
24	| exp_008e_v3_walker_s2 | walker | 008e_v3_mitigation | 2 | CIVO(1) | 3.780 | max(final_nve) |
25	| exp_008f_no_dt_embed_subsample_on_h8 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 1.020 | max(normalized_ve) at 25K |
26	| exp_008f_s3_no_dt_embed_walker | walker | 008f_no_dt_emb | 3 | Healthy(0) | 1.490 | metrics.nve_peak (parsed '< 1.5x') |
27	| exp_008f_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 1.410 | metrics.peak_nve |
28	| exp_009b_008d_walker_s2 | walker | 008d_civo_trigger | 2 | CIVO(1) | 1.620 | metrics.nve_peak |
29	| exp_009c_s3 | walker | other | 3 | Healthy(0) | 0.520 | max(nve_105k) |
30	| exp_009e_008d_walker_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.130 | metrics.nve_peak |
31	| exp_010b_cheetah_civo_trigger | cheetah | 008d_civo_trigger | 1 | CIVO(1) | 8.270 | metrics.nve_peak |
32	| exp_010b_cheetah_civo_trigger_s0 | cheetah | 008d_civo_trigger | 0 | CIVO(1) | 70.640 | max(nve_105K) |
33	| exp_015b_frozen_dt_emb | walker | frozen_dt_emb | 1 | Healthy(0) | 0.467 | max(nve_85K) |
34	| exp_020_vanilla_dreamerv3_s2 | walker | baseline | 2 | Healthy(0) | 0.983 | computed |
35	| exp_021_full_sgs_cheetah_s1 | cheetah | sgs | 1 | CIVO(1) | 9.940 | metrics.nve_peak |
36	| exp_024b_cheetah_no_dt_emb_s0 | cheetah | 008f_no_dt_emb | 0 | Healthy(0) | 0.200 | metrics.nve_peak |
37	| exp_024b_cheetah_no_dt_emb_s1 | cheetah | 008f_no_dt_emb | 1 | Healthy(0) | 0.100 | metrics.nve_peak |
38	| exp_027_tcn_walker_s0 | walker | tcn | 0 | CIVO(1) | 3.965 | metrics.peak_nve |
39	| exp_027_tcn_walker_s0_sigma02 | walker | tcn | 0 | Healthy(0) | 0.908 | metrics.nve_max |
40	| exp_027_tcn_walker_s1 | walker | tcn | 1 | CIVO(1) | 1.637 | metrics.nve_max |
41	| exp_029a_tcn_walker_s1_sigma02 | walker | tcn | 1 | Healthy(0) | 0.643 | metrics.nve_max |
42	| exp_029b_tcn_walker_s2_sigma02 | walker | tcn | 2 | CIVO(1) | 2.765 | metrics.nve_peak |
43	| exp_029d_tcn_walker_s3_sigma02 | walker | tcn | 3 | CIVO(1) | 3.000 | metrics.nve_peak |
44	| exp_030b_tcn_cheetah_s0_sigma05 | cheetah | tcn | 0 | CIVO(1) | 10.666 | metrics.nve_max |
45	| exp_031b_tcn_pickcube_s0_sigma05 | pickcube | tcn | 0 | CIVO(1) | 3.300 | metrics.nve_peak |
46	| exp_032_dual_critic_walker | walker | dual_critic | 0 | Healthy(0) | 1.100 | metrics.nve_peak |
47	| exp_032b_dual_critic_walker_s1 | walker | dual_critic | 1 | Healthy(0) | 1.400 | metrics.peak_nve |
48	| exp_034_dual_critic_cheetah | cheetah | dual_critic | 0 | CIVO(1) | 4.500 | computed |
49	| exp_036_dual_critic_pickcube | cheetah | dual_critic | 0 | CIVO(1) | 2.300 | metrics.nve_peak |
50	| exp_037_wide_critic_cheetah | cheetah | other | 0 | CIVO(1) | 3.600 | metrics.nve_peak |
51	| exp_042_frozen_dt_emb_walker | walker | frozen_dt_emb | 0 | Healthy(0) | 0.194 | metrics.nve_peak |
52	| exp_043_008f_walker_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.808 | metrics.nve_peak |
53	| exp_045_treatment_extension_008d_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 4.910 | metrics.nve_peak |
54	| exp_046_frozen_dt_emb_cheetah | cheetah | frozen_dt_emb | 0 | Healthy(0) | 1.350 | metrics.nve_peak |
55	| exp_047_frozen_dt_emb_walker_s1 | walker | frozen_dt_emb | 1 | Healthy(0) | 1.710 | metrics.nve_peak |
56	| exp_048_cheetah_civo_extension | cheetah | other | 0 | CIVO(1) | 2.750 | max(nve_final) |
57	| exp_057_frozen_dt_emb_walker_s2 | walker | frozen_dt_emb | 2 | Healthy(0) | 1.880 | metrics.nve_peak |
58	| exp_058_frozen_dt_emb_cheetah_s1 | cheetah | frozen_dt_emb | 1 | Healthy(0) | 0.780 | metrics.nve_peak |
59	| exp_059_walker_trained_s5 | walker | trained_dt_emb | 5 | CIVO(1) | 4.720 | metrics.nve_peak |
60	| exp_067_frozen_dt_emb_walker_plan015 | walker | frozen_dt_emb | 0 | Healthy(0) | 0.400 | metrics.nve_peak |
61	| exp_068_008d_walker_repro_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.120 | max(nve_final_105k) |
62	| exp_069_008f_walker_repro_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.660 | metrics.nve_peak |
63	| exp_070_008e_v3_walker_s0 | walker | 008e_v3_mitigation | 0 | Healthy(0) | 0.800 | metrics.nve_peak |
64	| exp_071_008f_walker_s3 | walker | 008f_no_dt_emb | 3 | Healthy(0) | 0.974 | computed ve_ratio_peak/baseline |
65	| exp_072_008e_v3_walker_s5 | walker | 008e_v3_mitigation | 5 | Healthy(0) | 0.610 | metrics.nve_peak |
66	| exp_073_008f_walker_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 0.760 | metrics.nve_peak |
67	| exp_078_cheetah_008d_s0 | cheetah | 008d_civo_trigger | 0 | CIVO(1) | 4.100 | metrics.nve_peak |
68	| exp_082_cheetah_no_dt_emb_s0 | cheetah | 008f_no_dt_emb | 0 | Healthy(0) | 1.580 | metrics.nve_peak (eval-variance-driven) |
69	| exp_084_frozen_dt_emb_walker_s0 | walker | frozen_dt_emb | 0 | Healthy(0) | 0.370 | metrics.nve_peak |
70	| exp_085_frozen_dt_emb_walker_s1 | walker | frozen_dt_emb | 1 | Healthy(0) | 0.310 | metrics.nve_peak |
71	| exp_087_frozen_dt_emb_cheetah_s1 | cheetah | frozen_dt_emb | 1 | Healthy(0) | 0.299 | computed ve_ratio/baseline |
72	
73	## Threshold Analysis
74	
75	### θ = 1.3×
76	- **Accuracy: 86.9%** (53/61)
77	- Precision: 75.8% | Recall: 100.0% | **F1: 0.862**
78	- TP=25, FP=8, TN=28, FN=0
79	- FP: exp_082_cheetah_no_dt_emb_s0 (1.58), exp_046_frozen_dt_emb_cheetah (1.35), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88), exp_047_frozen_dt_emb_walker_s1 (1.71), exp_008f_s3_no_dt_embed_walker (1.49), exp_008f_s4 (1.41), exp_032b_dual_critic_walker_s1 (1.40)
80	- FN: none
81	
82	### θ = 1.5× (recommended)
83	- **Accuracy: 93.4%** (57/61)
84	- Precision: 86.2% | Recall: 100.0% | **F1: 0.926**
85	- TP=25, FP=4, TN=32, FN=0
86	- FP: exp_082_cheetah_no_dt_emb_s0 (1.58, eval-variance-driven, NOT value overestimation), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88, transient), exp_047_frozen_dt_emb_walker_s1 (1.71, transient)
87	- FN: none
88	
89	### θ = 1.7×
90	- **Accuracy: 90.2%** (55/61)
91	- Precision: 88.0% | Recall: 88.0% | **F1: 0.880**
92	- TP=22, FP=3, TN=33, FN=3
93	- FP: exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88), exp_047_frozen_dt_emb_walker_s1 (1.71)
94	- FN: exp_027_tcn_walker_s1 (1.64), exp_009b_008d_walker_s2 (1.62), exp_008d_civo_trigger_s3 (1.53)
95	
96	### θ = 2.0×
97	- **Accuracy: 95.1%** (58/61)
98	- Precision: 100.0% | Recall: 88.0% | **F1: 0.936**
99	- TP=22, FP=0, TN=36, FN=3
100	- FP: none
101	- FN: exp_027_tcn_walker_s1 (1.64), exp_009b_008d_walker_s2 (1.62), exp_008d_civo_trigger_s3 (1.53)
102	
103	### 汇总
104	
105	| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |
106	|-----------|----------|-----------|--------|------|-----|-----|
107	| 1.3× | 86.9% | 75.8% | 100% | 0.862 | 8 | 0 |
108	| **1.5×** | **93.4%** | **86.2%** | **100%** | **0.926** | 4 | 0 |
109	| 1.7× | 90.2% | 88.0% | 88.0% | 0.880 | 3 | 3 |
110	| 2.0× | 95.1% | 100% | 88.0% | 0.936 | 0 | 3 |
111	
112	## AUROC
113	
114	**AUROC = 0.9889** (N=61, 25 positive, 36 negative)
115	
116	NVE_peak 作为连续分数对 CIVO 的区分力极强。
117	
118	**NVE 分布:**
119	- CIVO collapsed (25): min=1.530, median=4.100, max=70.640, mean=6.954
120	- Healthy (36): min=0.100, median=0.800, max=1.930, mean=0.845
121	
122	**Overlap zone:** NVE ∈ [1.530, 1.930]
123	- 重叠 collapsed (3): exp_008d_s3 (1.530), exp_009b_s2 (1.620), exp_027_tcn_s1 (1.637)
124	- 重叠 healthy (4): exp_082_cheetah_no_dt_emb (1.580), exp_047_frozen_walker_s1 (1.710), exp_057_frozen_walker_s2 (1.880), exp_008e_v3_dt1_h15 (1.930)
125	
126	**Data-optimal threshold (Youden's J):** θ ≈ 1.51×, J = 0.889
127	
128	## 推荐 threshold
129	
130	**推荐阈值: NVE ≥ 1.5×** (F1 = 0.926, AUROC = 0.989)
131	
132	理由：
133	1. **100% recall**: 不漏掉任何 CIVO 实验。漏检比误报代价更高——未检出的 CIVO 导致无效训练浪费 GPU 小时。
134	2. **最佳 F1**: 1.5× 在四个候选 threshold 中 F1 第二高（0.926 vs 2.0× 的 0.936），但 recall 从 88%→100% 的提升价值大于 precision 从 100%→86% 的下降。
135	3. **4 个 FP 均可解释**: 2 个 frozen dt_emb transient spike（自然消退，非病理性）、1 个 eval-variance-driven（非 value overestimation）、1 个 mitigation config 早期 spike。
136	4. **Youden's J 最优点**: 统计最优切分在 θ≈1.51×，与 1.5× 一致。
137	5. **与论文定义一致**: 原论文使用 NVE≥1.5× 作为 CIVO onset 标准。
138	
139	**Decision rule:**
140	- θ=1.5× for **screening** (maximize sensitivity, catch all CIVO early)
141	- θ=2.0× for **confirmation** (zero false positives, but misses 3 self-correcting CIVO seeds)
142	
143	## 方法论说明
144	
145	### NVE 计算方法
146	
147	NVE (Normalized Value-Eval ratio) = experiment_ve_ratio / baseline_ve_ratio_at_same_step
148	
149	- Walker Walk baseline: exp_001_baseline (seed 1) per-step VE ratios: 25K=0.087, 35K=0.241, 45K=0.331, 55K=0.404, 65K=0.563, 75K=0.719, 85K=0.701, 95K=0.632, 105K=0.656
150	- Cheetah Run baseline: approximate VE trajectory from exp_023a/023b: 25K=0.1, 35K=0.2, 45K=0.3, 55K=0.4, 65K=0.5, 75K=0.55, 85K=0.6, 95K=0.65, 105K=0.65
151	- 取 peak NVE (训练过程中最大 NVE) 作为分类特征
152	- NVE 数据提取优先级: nve_peak > nve_max > normalized_ve > ve_ratio/baseline
153	
154	### Ground Truth 标注
155	
156	- **CIVO(1)** (25 个): 明确 CIVO collapse 证据 (VE 持续加速, eval 显著下降, nve_classification=onset_collapse)
157	- **Healthy(0)** (36 个): 无 CIVO 迹象 (VE 稳定, eval 保持或增长)
158	- **EXCLUDE**: conclusion=killed/failed (技术故障), 无 NVE 数据, 纯 baseline (用于归一化), 分类模糊
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "333e8b18-dff7-4ded-a1e9-66298ec17b70",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis.md",
      "content": "# NVE Threshold Sensitivity Analysis\n\n**Updated: 2026-05-25** (added exp_078, exp_082, exp_084, exp_085, exp_087; total N=61)\n\n## 数据集\n\n样本总数: 61 (Collapsed: 25, Healthy: 36)\n\n| exp_id | env | config | seed | ground_truth | peak_nve | nve_source |\n|--------|-----|--------|------|-------------|----------|------------|\n| exp_006_fixed_dt2 | walker | 006_fixed_dt2 | 1 | CIVO(1) | 4.835 | computed ve_ratio/baseline at 65K |\n| exp_008a_cheetah_unexposed_s0 | cheetah | 008a_unexposed | 0 | Healthy(0) | 0.490 | max(nve_105k) |\n| exp_008a_cheetah_unexposed_s1 | cheetah | 008a_unexposed | 1 | Healthy(0) | 0.478 | max(nve_105k) |\n| exp_008a_no_subsample_dt2 | walker | 008a_unexposed | 1 | Healthy(0) | 0.930 | max(normalized_ve) |\n| exp_008a_unexposed_s1 | walker | 008a_unexposed | 1 | Healthy(0) | 0.598 | computed |\n| exp_008a_unexposed_s2 | walker | 008a_unexposed | 2 | Healthy(0) | 0.463 | computed |\n| exp_008d_civo_trigger_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 1.530 | metrics.nve_peak |\n| exp_008d_civo_trigger_s4 | walker | 008d_civo_trigger | 4 | CIVO(1) | 4.620 | metrics.nve_peak |\n| exp_008d_subsample_on_h8 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.124 | computed |\n| exp_008e_v3_s3 | walker | 008e_v3_mitigation | 3 | CIVO(1) | 4.020 | metrics.nve_peak |\n| exp_008e_v3_s4 | walker | 008e_v3_mitigation | 4 | Healthy(0) | 0.990 | metrics.nve_peak |\n| exp_008e_v3_subsample_on_dt1_h15 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 1.930 | max(normalized_ve) at 25K |\n| exp_008e_v3_walker_s1 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 0.803 | computed |\n| exp_008e_v3_walker_s2 | walker | 008e_v3_mitigation | 2 | CIVO(1) | 3.780 | max(final_nve) |\n| exp_008f_no_dt_embed_subsample_on_h8 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 1.020 | max(normalized_ve) at 25K |\n| exp_008f_s3_no_dt_embed_walker | walker | 008f_no_dt_emb | 3 | Healthy(0) | 1.490 | metrics.nve_peak (parsed '< 1.5x') |\n| exp_008f_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 1.410 | metrics.peak_nve |\n| exp_009b_008d_walker_s2 | walker | 008d_civo_trigger | 2 | CIVO(1) | 1.620 | metrics.nve_peak |\n| exp_009c_s3 | walker | other | 3 | Healthy(0) | 0.520 | max(nve_105k) |\n| exp_009e_008d_walker_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.130 | metrics.nve_peak |\n| exp_010b_cheetah_civo_trigger | cheetah | 008d_civo_trigger | 1 | CIVO(1) | 8.270 | metrics.nve_peak |\n| exp_010b_cheetah_civo_trigger_s0 | cheetah | 008d_civo_trigger | 0 | CIVO(1) | 70.640 | max(nve_105K) |\n| exp_015b_frozen_dt_emb | walker | frozen_dt_emb | 1 | Healthy(0) | 0.467 | max(nve_85K) |\n| exp_020_vanilla_dreamerv3_s2 | walker | baseline | 2 | Healthy(0) | 0.983 | computed |\n| exp_021_full_sgs_cheetah_s1 | cheetah | sgs | 1 | CIVO(1) | 9.940 | metrics.nve_peak |\n| exp_024b_cheetah_no_dt_emb_s0 | cheetah | 008f_no_dt_emb | 0 | Healthy(0) | 0.200 | metrics.nve_peak |\n| exp_024b_cheetah_no_dt_emb_s1 | cheetah | 008f_no_dt_emb | 1 | Healthy(0) | 0.100 | metrics.nve_peak |\n| exp_027_tcn_walker_s0 | walker | tcn | 0 | CIVO(1) | 3.965 | metrics.peak_nve |\n| exp_027_tcn_walker_s0_sigma02 | walker | tcn | 0 | Healthy(0) | 0.908 | metrics.nve_max |\n| exp_027_tcn_walker_s1 | walker | tcn | 1 | CIVO(1) | 1.637 | metrics.nve_max |\n| exp_029a_tcn_walker_s1_sigma02 | walker | tcn | 1 | Healthy(0) | 0.643 | metrics.nve_max |\n| exp_029b_tcn_walker_s2_sigma02 | walker | tcn | 2 | CIVO(1) | 2.765 | metrics.nve_peak |\n| exp_029d_tcn_walker_s3_sigma02 | walker | tcn | 3 | CIVO(1) | 3.000 | metrics.nve_peak |\n| exp_030b_tcn_cheetah_s0_sigma05 | cheetah | tcn | 0 | CIVO(1) | 10.666 | metrics.nve_max |\n| exp_031b_tcn_pickcube_s0_sigma05 | pickcube | tcn | 0 | CIVO(1) | 3.300 | metrics.nve_peak |\n| exp_032_dual_critic_walker | walker | dual_critic | 0 | Healthy(0) | 1.100 | metrics.nve_peak |\n| exp_032b_dual_critic_walker_s1 | walker | dual_critic | 1 | Healthy(0) | 1.400 | metrics.peak_nve |\n| exp_034_dual_critic_cheetah | cheetah | dual_critic | 0 | CIVO(1) | 4.500 | computed |\n| exp_036_dual_critic_pickcube | cheetah | dual_critic | 0 | CIVO(1) | 2.300 | metrics.nve_peak |\n| exp_037_wide_critic_cheetah | cheetah | other | 0 | CIVO(1) | 3.600 | metrics.nve_peak |\n| exp_042_frozen_dt_emb_walker | walker | frozen_dt_emb | 0 | Healthy(0) | 0.194 | metrics.nve_peak |\n| exp_043_008f_walker_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.808 | metrics.nve_peak |\n| exp_045_treatment_extension_008d_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 4.910 | metrics.nve_peak |\n| exp_046_frozen_dt_emb_cheetah | cheetah | frozen_dt_emb | 0 | Healthy(0) | 1.350 | metrics.nve_peak |\n| exp_047_frozen_dt_emb_walker_s1 | walker | frozen_dt_emb | 1 | Healthy(0) | 1.710 | metrics.nve_peak |\n| exp_048_cheetah_civo_extension | cheetah | other | 0 | CIVO(1) | 2.750 | max(nve_final) |\n| exp_057_frozen_dt_emb_walker_s2 | walker | frozen_dt_emb | 2 | Healthy(0) | 1.880 | metrics.nve_peak |\n| exp_058_frozen_dt_emb_cheetah_s1 | cheetah | frozen_dt_emb | 1 | Healthy(0) | 0.780 | metrics.nve_peak |\n| exp_059_walker_trained_s5 | walker | trained_dt_emb | 5 | CIVO(1) | 4.720 | metrics.nve_peak |\n| exp_067_frozen_dt_emb_walker_plan015 | walker | frozen_dt_emb | 0 | Healthy(0) | 0.400 | metrics.nve_peak |\n| exp_068_008d_walker_repro_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.120 | max(nve_final_105k) |\n| exp_069_008f_walker_repro_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.660 | metrics.nve_peak |\n| exp_070_008e_v3_walker_s0 | walker | 008e_v3_mitigation | 0 | Healthy(0) | 0.800 | metrics.nve_peak |\n| exp_071_008f_walker_s3 | walker | 008f_no_dt_emb | 3 | Healthy(0) | 0.974 | computed ve_ratio_peak/baseline |\n| exp_072_008e_v3_walker_s5 | walker | 008e_v3_mitigation | 5 | Healthy(0) | 0.610 | metrics.nve_peak |\n| exp_073_008f_walker_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 0.760 | metrics.nve_peak |\n| exp_078_cheetah_008d_s0 | cheetah | 008d_civo_trigger | 0 | CIVO(1) | 4.100 | metrics.nve_peak |\n| exp_082_cheetah_no_dt_emb_s0 | cheetah | 008f_no_dt_emb | 0 | Healthy(0) | 1.580 | metrics.nve_peak (eval-variance-driven) |\n| exp_084_frozen_dt_emb_walker_s0 | walker | frozen_dt_emb | 0 | Healthy(0) | 0.370 | metrics.nve_peak |\n| exp_085_frozen_dt_emb_walker_s1 | walker | frozen_dt_emb | 1 | Healthy(0) | 0.310 | metrics.nve_peak |\n| exp_087_frozen_dt_emb_cheetah_s1 | cheetah | frozen_dt_emb | 1 | Healthy(0) | 0.299 | computed ve_ratio/baseline |\n\n## Threshold Analysis\n\n### θ = 1.3×\n- **Accuracy: 86.9%** (53/61)\n- Precision: 75.8% | Recall: 100.0% | **F1: 0.862**\n- TP=25, FP=8, TN=28, FN=0\n- FP: exp_082_cheetah_no_dt_emb_s0 (1.58), exp_046_frozen_dt_emb_cheetah (1.35), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88), exp_047_frozen_dt_emb_walker_s1 (1.71), exp_008f_s3_no_dt_embed_walker (1.49), exp_008f_s4 (1.41), exp_032b_dual_critic_walker_s1 (1.40)\n- FN: none\n\n### θ = 1.5× (recommended)\n- **Accuracy: 93.4%** (57/61)\n- Precision: 86.2% | Recall: 100.0% | **F1: 0.926**\n- TP=25, FP=4, TN=32, FN=0\n- FP: exp_082_cheetah_no_dt_emb_s0 (1.58, eval-variance-driven, NOT value overestimation), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88, transient), exp_047_frozen_dt_emb_walker_s1 (1.71, transient)\n- FN: none\n\n### θ = 1.7×\n- **Accuracy: 90.2%** (55/61)\n- Precision: 88.0% | Recall: 88.0% | **F1: 0.880**\n- TP=22, FP=3, TN=33, FN=3\n- FP: exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88), exp_047_frozen_dt_emb_walker_s1 (1.71)\n- FN: exp_027_tcn_walker_s1 (1.64), exp_009b_008d_walker_s2 (1.62), exp_008d_civo_trigger_s3 (1.53)\n\n### θ = 2.0×\n- **Accuracy: 95.1%** (58/61)\n- Precision: 100.0% | Recall: 88.0% | **F1: 0.936**\n- TP=22, FP=0, TN=36, FN=3\n- FP: none\n- FN: exp_027_tcn_walker_s1 (1.64), exp_009b_008d_walker_s2 (1.62), exp_008d_civo_trigger_s3 (1.53)\n\n### 汇总\n\n| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |\n|-----------|----------|-----------|--------|------|-----|-----|\n| 1.3× | 86.9% | 75.8% | 100% | 0.862 | 8 | 0 |\n| **1.5×** | **93.4%** | **86.2%** | **100%** | **0.926** | 4 | 0 |\n| 1.7× | 90.2% | 88.0% | 88.0% | 0.880 | 3 | 3 |\n| 2.0× | 95.1% | 100% | 88.0% | 0.936 | 0 | 3 |\n\n## AUROC\n\n**AUROC = 0.9889** (N=61, 25 positive, 36 negative)\n\nNVE_peak 作为连续分数对 CIVO 的区分力极强。\n\n**NVE 分布:**\n- CIVO collapsed (25): min=1.530, median=4.100, max=70.640, mean=6.954\n- Healthy (36): min=0.100, median=0.800, max=1.930, mean=0.845\n\n**Overlap zone:** NVE ∈ [1.530, 1.930]\n- 重叠 collapsed (3): exp_008d_s3 (1.530), exp_009b_s2 (1.620), exp_027_tcn_s1 (1.637)\n- 重叠 healthy (4): exp_082_cheetah_no_dt_emb (1.580), exp_047_frozen_walker_s1 (1.710), exp_057_frozen_walker_s2 (1.880), exp_008e_v3_dt1_h15 (1.930)\n\n**Data-optimal threshold (Youden's J):** θ ≈ 1.51×, J = 0.889\n\n## 推荐 threshold\n\n**推荐阈值: NVE ≥ 1.5×** (F1 = 0.926, AUROC = 0.989)\n\n理由：\n1. **100% recall**: 不漏掉任何 CIVO 实验。漏检比误报代价更高——未检出的 CIVO 导致无效训练浪费 GPU 小时。\n2. **最佳 F1**: 1.5× 在四个候选 threshold 中 F1 第二高（0.926 vs 2.0× 的 0.936），但 recall 从 88%→100% 的提升价值大于 precision 从 100%→86% 的下降。\n3. **4 个 FP 均可解释**: 2 个 frozen dt_emb transient spike（自然消退，非病理性）、1 个 eval-variance-driven（非 value overestimation）、1 个 mitigation config 早期 spike。\n4. **Youden's J 最优点**: 统计最优切分在 θ≈1.51×，与 1.5× 一致。\n5. **与论文定义一致**: 原论文使用 NVE≥1.5× 作为 CIVO onset 标准。\n\n**Decision rule:**\n- θ=1.5× for **screening** (maximize sensitivity, catch all CIVO early)\n- θ=2.0× for **confirmation** (zero false positives, but misses 3 self-correcting CIVO seeds)\n\n## 方法论说明\n\n### NVE 计算方法\n\nNVE (Normalized Value-Eval ratio) = experiment_ve_ratio / baseline_ve_ratio_at_same_step\n\n- Walker Walk baseline: exp_001_baseline (seed 1) per-step VE ratios: 25K=0.087, 35K=0.241, 45K=0.331, 55K=0.404, 65K=0.563, 75K=0.719, 85K=0.701, 95K=0.632, 105K=0.656\n- Cheetah Run baseline: approximate VE trajectory from exp_023a/023b: 25K=0.1, 35K=0.2, 45K=0.3, 55K=0.4, 65K=0.5, 75K=0.55, 85K=0.6, 95K=0.65, 105K=0.65\n- 取 peak NVE (训练过程中最大 NVE) 作为分类特征\n- NVE 数据提取优先级: nve_peak > nve_max > normalized_ve > ve_ratio/baseline\n\n### Ground Truth 标注\n\n- **CIVO(1)** (25 个): 明确 CIVO collapse 证据 (VE 持续加速, eval 显著下降, nve_classification=onset_collapse)\n- **Healthy(0)** (36 个): 无 CIVO 迹象 (VE 稳定, eval 保持或增长)\n- **EXCLUDE**: conclusion=killed/failed (技术故障), 无 NVE 数据, 纯 baseline (用于归一化), 分类模糊\n",
      "numLines": 159,
      "startLine": 1,
      "totalLines": 159
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have the V1 analysis. It already has 61 data points including exp_084, exp_085, exp_087. But exp_086 is in ANALYZING status with no metrics.

Let me now check what the Reviewer's concern is. The Reviewer said exp_084 NVE_peak=2.25 and exp_085 NVE_peak=3.0, but registry shows NVE_peak=0.37 and 0.31. This is because the Reviewer might be using raw ve_ratio_peak instead of step-matched NVE.

Wait, but exp_084 and exp_085 don't have ve_ratio_peak in the registry either. 

So the distinction is that Method A uses step-matched NVE (the ratio of ve_ratio to baseline_ve_ratio at the same step), which is what's already in the registry, while Method B would use the raw peak from the ve_ratio time series directly. Since these experiments don't have ve_ratio_peak values stored, the Reviewer's numbers of 2.25 and 3.0 must come from a different calculation method that I need to understand. I see the discrepancy now — the Reviewer's reported NVE values (2.25 and 3.0) don't match what's in the registry (0.37 and 0.31), which suggests they're using a different calculation method, likely the raw ve_ratio_peak instead of the step-matched normalized approach. For Method A, I'll use the registry's step-matched NVE values, and for Method B, I'll apply the raw ve_ratio_peak values where they're available, noting which experiments lack that data.

Now I need to focus on the core deliverables: verifying the dataset size (V1 had 61 experiments, need to confirm if exp_086 should be included), running both calculation methods, establishing the combined diagnostic criteria using time series data, computing the NVE_median_last5 auxiliary metric, and compiling the analysis report. Let me first check which experiments actually have trajectory data available versus which ones don't, since that'll determine what I can include in the time series analysis.

Looking at this more carefully, V1 already incorporated exp_078, exp_082, exp_084, exp_085, and exp_087 when it was updated on 2026-05-25, bringing the total to 61 experiments. The task mentions these were missing initially, but they're already in the current dataset. Since exp_086 is still in ANALYZING status with no metrics available, I'll exclude it and stick with the 61 experiments from V1.

For the combined diagnostic approach, I'll apply Method A (step-matched NVE) and Method B (raw ve_ratio_peak) across the dataset, then layer on the three diagnostic conditions. The challenge is that only some experiments have complete trajectory data, so I'll need to document which ones can be fully evaluated against all three conditions and which have limitations.

Writing analysis script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "3563e356-995f-49ae-aaf6-9acf0359f19d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmsqenTJjLF5UX4yUdLVsK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5831,
      "cache_read_input_tokens": 48149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5831
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

_source line 39_

Now I have all the data needed. Let me also get the remaining experiment details for full metrics extraction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "9cdeb547-fd9a-4ade-a918-5b35c996a2b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmsqenTJjLF5UX4yUdLVsK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5831,
      "cache_read_input_tokens": 48149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5831
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Ketzperxd6wmjyab4o2QC5`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/43c73d77-52ad-4826-98f1-2bd47073d289/tool-results/mcp-agent-ml-research-read_registry-1779740365429.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get full metrics for experiments that have various nve-relevant keys\nfor eid in ['exp_006_fixed_dt2', 'exp_008a_cheetah_unexposed_s0', 'exp_008a_cheetah_unexposed_s1',\n            'exp_008a_no_subsample_dt2', 'exp_008a_unexposed_s1', 'exp_008a_unexposed_s2',\n            'exp_008d_subsample_on_h8', 'exp_008e_v3_subsample_on_dt1_h15',\n            'exp_008e_v3_walker_s1', 'exp_008e_v3_walker_s2',\n            'exp_008f_no_dt_embed_subsample_on_h8', 'exp_008f_s3_no_dt_embed_walker', 'exp_008f_s4',\n            'exp_009c_s3', 'exp_010b_cheetah_civo_trigger_s0',\n            'exp_015b_frozen_dt_emb', 'exp_020_vanilla_dreamerv3_s2',\n            'exp_027_tcn_walker_s0', 'exp_027_tcn_walker_s1',\n            'exp_027_tcn_walker_s0_sigma02', 'exp_029a_tcn_walker_s1_sigma02',\n            'exp_030b_tcn_cheetah_s0_sigma05',\n            'exp_032b_dual_critic_walker_s1', 'exp_068_008d_walker_repro_s1']:\n    exp = exps.get(eid)\n    if exp:\n        metrics = exp.get('metrics', {})\n        ve_keys = {k:v for k,v in metrics.items() if 've_ratio' in k.lower() or 'nve' in k.lower() or 've_' in k.lower() or 'peak_nve' in k.lower() or 'nve_max' in k.lower()}\n        if ve_keys:\n            print(f'{eid}: {json.dumps(ve_keys)}')\n\" 2>&1\n",
  "description": "Extract ve_ratio data for V1 experiments missing Method B data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "f4fb3ecc-b70a-45b9-b140-20c0bcdbdb88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmsqenTJjLF5UX4yUdLVsK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5831,
      "cache_read_input_tokens": 48149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5831
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

_source line 41 · 2026-05-25T20:22:13.715Z_

<details><summary>↩ Tool result · `toolu_01Ketzperxd6wmjyab4o2QC5`</summary>

```text
exp_008a_cheetah_unexposed_s0: {"nve_105k": 0.49, "ve_ratio_105k": 0.3193}
exp_008a_cheetah_unexposed_s1: {"nve_105k": 0.478, "ve_ratio_105k": 0.3112}
exp_008a_no_subsample_dt2: {"normalized_ve_105K": 0.59, "normalized_ve_55K": 0.93, "normalized_ve_65K": 0.66, "normalized_ve_75K": 0.75, "normalized_ve_85K": 0.68, "normalized_ve_95K": 0.79}
exp_008a_unexposed_s1: {"civo_delta_ve_final": -0.0028, "civo_ve_ratio_final": 0.43}
exp_008a_unexposed_s2: {"civo_delta_ve_final": -0.003, "civo_ve_ratio_final": 0.333}
exp_008e_v3_walker_s1: {"ve_ratio_105k": 0.527}
exp_008e_v3_walker_s2: {"final_nve": 3.78, "final_ve_ratio": 2.481, "ve_ratio_trajectory": [{"nve": 1.64, "step": 25000, "ve": 0.143}, {"nve": 1.03, "step": 35000, "ve": 0.249}, {"nve": 1.06, "step": 45000, "ve": 0.351}, {"nve": 1.02, "step": 55000, "ve": 0.413}, {"nve": 0.9, "step": 65000, "ve": 0.507}, {"nve": 0.66, "step": 75000, "ve": 0.473}, {"nve": 0.68, "step": 85000, "ve": 0.474}, {"nve": 1.34, "step": 95000, "ve": 0.85}, {"nve": 3.78, "step": 105000, "ve": 2.481}]}
exp_008f_s3_no_dt_embed_walker: {"nve_peak": "< 1.5x"}
exp_008f_s4: {"nve_105k": 0.58, "peak_nve": 1.41, "peak_nve_step": 85000}
exp_009c_s3: {"nve_105k": 0.52, "ve_ratio_105k": 0.386}
exp_010b_cheetah_civo_trigger_s0: {"nve_105K": 70.64, "nve_95K": 6.34}
exp_015b_frozen_dt_emb: {"nve_105K": 0.42, "nve_85K": 0.467, "nve_95K": 0.394}
exp_020_vanilla_dreamerv3_s2: {"ve_ratio_105K": 0.645}
exp_027_tcn_walker_s0: {"nve_breach_count": 3, "nve_breach_steps": "55K(1.68), 65K(1.54), 85K(3.97)", "peak_nve": 3.965, "peak_nve_step": "85K", "ve_ratio_105K": 0.916, "ve_ratio_15K": 0.02, "ve_ratio_25K": 0.11, "ve_ratio_35K": 0.235, "ve_ratio_45K": 0.86, "ve_ratio_55K": 1.679, "ve_ratio_65K": 1.544, "ve_ratio_75K": 0.831, "ve_ratio_85K": 3.965, "ve_ratio_95K": 0.675}
exp_027_tcn_walker_s1: {"nve_final": 0.1476, "nve_max": 1.6367, "nve_max_step": 95000, "ve_ratio": {"105000": 0.6444, "115000": 0.4021, "125000": 0.38, "135000": 0.5078, "145000": 0.8469, "15000": 0.0246, "155000": 0.8568, "165000": 0.5393, "175000": 0.7355, "185000": 0.211, "195000": 0.3513, "205000": 0.2376, "215000": 0.1476, "25000": 0.1416, "35000": 0.3585, "45000": 0.6101, "55000": 0.7092, "65000": 0.4875, "75000": 0.4902, "85000": 1.4104, "95000": 1.6367}}
exp_027_tcn_walker_s0_sigma02: {"nve_final": 0.0955, "nve_max": 0.9081, "nve_max_step": "95K", "ve_ratio_105K": 0.5625, "ve_ratio_115K": 0.2105, "ve_ratio_125K": 0.2182, "ve_ratio_135K": 0.1764, "ve_ratio_145K": 0.143, "ve_ratio_155K": 0.106, "ve_ratio_15K": 0.0192, "ve_ratio_165K": 0.0979, "ve_ratio_175K": 0.0729, "ve_ratio_185K": 0.1048, "ve_ratio_195K": 0.1026, "ve_ratio_205K": 0.0995, "ve_ratio_215K": 0.0955, "ve_ratio_25K": 0.0961, "ve_ratio_35K": 0.1875, "ve_ratio_45K": 0.3009, "ve_ratio_55K": 0.5231, "ve_ratio_65K": 0.5654, "ve_ratio_75K": 0.611, "ve_ratio_85K": 0.4665, "ve_ratio_95K": 0.9081}
exp_029a_tcn_walker_s1_sigma02: {"nve_final": 0.1864, "nve_max": 0.6428, "nve_max_step": "55K", "ve_ratio_105K": 0.1554, "ve_ratio_115K": 0.1348, "ve_ratio_125K": 0.116, "ve_ratio_135K": 0.1449, "ve_ratio_145K": 0.1088, "ve_ratio_155K": 0.1287, "ve_ratio_15K": 0.0248, "ve_ratio_165K": 0.1142, "ve_ratio_175K": 0.2138, "ve_ratio_185K": 0.121, "ve_ratio_195K": 0.1075, "ve_ratio_205K": 0.1503, "ve_ratio_215K": 0.1864, "ve_ratio_25K": 0.1165, "ve_ratio_35K": 0.3574, "ve_ratio_45K": 0.5147, "ve_ratio_55K": 0.6428, "ve_ratio_65K": 0.4777, "ve_ratio_75K": 0.398, "ve_ratio_85K": 0.4033, "ve_ratio_95K": 0.3007}
exp_030b_tcn_cheetah_s0_sigma05: {"nve_final": 0.1534, "nve_max": 10.6657, "nve_max_step": "55K", "ve_ratio_105K": 0.2686, "ve_ratio_115K": 0.1789, "ve_ratio_125K": 0.1037, "ve_ratio_135K": 0.2153, "ve_ratio_145K": 0.2478, "ve_ratio_155K": 0.2392, "ve_ratio_15K": 0.0202, "ve_ratio_165K": 0.202, "ve_ratio_175K": 0.1591, "ve_ratio_185K": 0.1834, "ve_ratio_195K": 0.1534, "ve_ratio_25K": 0.0636, "ve_ratio_35K": 0.1238, "ve_ratio_45K": 1.9141, "ve_ratio_55K": 10.6657, "ve_ratio_65K": 0.8371, "ve_ratio_75K": 1.9823, "ve_ratio_85K": 1.0946, "ve_ratio_95K": 0.2253}
exp_032b_dual_critic_walker_s1: {"final_nve": 0.1, "nve_criterion_pass": true, "nve_trajectory": "15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1", "peak_nve": 1.4}
exp_068_008d_walker_repro_s1: {"ve_ratio_final": 2.7, "ve_ratio_peak": 4.6, "ve_ratio_peak_step": 85000, "nve_final_105k": 4.12, "nve_peak_85k": 6.57, "nve_onset_step": 45000, "nve_onset_value": 1.81, "ve_ratio_trajectory": {"15k": 0, "25k": 0.2, "35k": 0.3, "45k": 0.6, "55k": 0.6, "65k": 1.3, "75k": 1.6, "85k": 4.6, "95k": 4.6, "105k": 2.7}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "d943f4fb-58ec-47bd-b912-f0faf0e56204",
  "tool_use_result": {
    "stdout": "exp_008a_cheetah_unexposed_s0: {\"nve_105k\": 0.49, \"ve_ratio_105k\": 0.3193}\nexp_008a_cheetah_unexposed_s1: {\"nve_105k\": 0.478, \"ve_ratio_105k\": 0.3112}\nexp_008a_no_subsample_dt2: {\"normalized_ve_105K\": 0.59, \"normalized_ve_55K\": 0.93, \"normalized_ve_65K\": 0.66, \"normalized_ve_75K\": 0.75, \"normalized_ve_85K\": 0.68, \"normalized_ve_95K\": 0.79}\nexp_008a_unexposed_s1: {\"civo_delta_ve_final\": -0.0028, \"civo_ve_ratio_final\": 0.43}\nexp_008a_unexposed_s2: {\"civo_delta_ve_final\": -0.003, \"civo_ve_ratio_final\": 0.333}\nexp_008e_v3_walker_s1: {\"ve_ratio_105k\": 0.527}\nexp_008e_v3_walker_s2: {\"final_nve\": 3.78, \"final_ve_ratio\": 2.481, \"ve_ratio_trajectory\": [{\"nve\": 1.64, \"step\": 25000, \"ve\": 0.143}, {\"nve\": 1.03, \"step\": 35000, \"ve\": 0.249}, {\"nve\": 1.06, \"step\": 45000, \"ve\": 0.351}, {\"nve\": 1.02, \"step\": 55000, \"ve\": 0.413}, {\"nve\": 0.9, \"step\": 65000, \"ve\": 0.507}, {\"nve\": 0.66, \"step\": 75000, \"ve\": 0.473}, {\"nve\": 0.68, \"step\": 85000, \"ve\": 0.474}, {\"nve\": 1.34, \"step\": 95000, \"ve\": 0.85}, {\"nve\": 3.78, \"step\": 105000, \"ve\": 2.481}]}\nexp_008f_s3_no_dt_embed_walker: {\"nve_peak\": \"< 1.5x\"}\nexp_008f_s4: {\"nve_105k\": 0.58, \"peak_nve\": 1.41, \"peak_nve_step\": 85000}\nexp_009c_s3: {\"nve_105k\": 0.52, \"ve_ratio_105k\": 0.386}\nexp_010b_cheetah_civo_trigger_s0: {\"nve_105K\": 70.64, \"nve_95K\": 6.34}\nexp_015b_frozen_dt_emb: {\"nve_105K\": 0.42, \"nve_85K\": 0.467, \"nve_95K\": 0.394}\nexp_020_vanilla_dreamerv3_s2: {\"ve_ratio_105K\": 0.645}\nexp_027_tcn_walker_s0: {\"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"ve_ratio_105K\": 0.916, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675}\nexp_027_tcn_walker_s1: {\"nve_final\": 0.1476, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"ve_ratio\": {\"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"15000\": 0.0246, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367}}\nexp_027_tcn_walker_s0_sigma02: {\"nve_final\": 0.0955, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_15K\": 0.0192, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081}\nexp_029a_tcn_walker_s1_sigma02: {\"nve_final\": 0.1864, \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_15K\": 0.0248, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007}\nexp_030b_tcn_cheetah_s0_sigma05: {\"nve_final\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_15K\": 0.0202, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253}\nexp_032b_dual_critic_walker_s1: {\"final_nve\": 0.1, \"nve_criterion_pass\": true, \"nve_trajectory\": \"15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1\", \"peak_nve\": 1.4}\nexp_068_008d_walker_repro_s1: {\"ve_ratio_final\": 2.7, \"ve_ratio_peak\": 4.6, \"ve_ratio_peak_step\": 85000, \"nve_final_105k\": 4.12, \"nve_peak_85k\": 6.57, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.81, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.2, \"35k\": 0.3, \"45k\": 0.6, \"55k\": 0.6, \"65k\": 1.3, \"75k\": 1.6, \"85k\": 4.6, \"95k\": 4.6, \"105k\": 2.7}}",
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

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough data to do the comprehensive analysis. Let me now build the analysis Python script that:

1. Defines all 61 experiments with their data
2. Computes Method A (step-matched NVE) analysis - already have these values
3. Computes Method B (raw ve_ratio_peak) analysis - using ve_ratio_peak values where available
4. Implements combined diagnostic criteria
5. Computes NVE_median_last5

For Method B, I need raw ve_ratio_peak values. For experiments without explicit ve_ratio_peak, I can compute from trajectory data.


For the combined diagnostic, I'll focus on the experiments that have time series data available. Looking at what I have, several experiments include ve_ratio trajectories and nve trajectories that I can work with to extract the necessary metrics. Now I'm looking at which experiments have the trajectory data I need. I've got about 17 total, but for the diagnostic criteria I'm working with, I need to think carefully about what each condition requires — some only need peak values while others need the full time series to detect trends and sustained violations. Since most of my experiments have trajectory data, I can apply all three conditions rather than just the peak-based one.

For the report, I'll run both methods on all 61 experiments, then apply the combined diagnostic to just the subset with trajectory data, and flag which experiments are missing that information. For Method B specifically, I need to extract the raw ve_ratio_peak values — pulling directly from the registry where available, or computing the maximum from the trajectory data when that's all I have.

Compiling the Method B dataset... Now I'm looking at the performance metrics for additional experiments across different tasks and configurations, comparing results like the cheetah baseline variants, stackcube experiments with various trigger mechanisms, and peg insertion trials with different approaches.

I need to handle the missing ve_ratio_peak values strategically—pulling from trajectory data where available, computing from NVE and baseline ratios when necessary, and noting gaps where neither exists. Rather than manually patching each experiment, I'll write a script that systematically builds the complete dataset, applies both diagnostic methods, and generates a comprehensive report. , 55K=0.4, 65K=0.5, 75K=0.55, 85K=0.6, 95K=0.65, 105K=0.65, plus the baseline scores for both environments. Now I need to build out the comprehensive analysis script that covers all six components: recomputing Method A with a single threshold, pulling trajectory data for the diagnostic, implementing Method B using ve_ratio_peak, extracting the ve_ratio trajectories, and calculating NVE_median_last5 across the dataset.

I only have trajectory data for about 17 of the 61 experiments, which limits the combined diagnostic analysis, but I'll work with what's available. Writing a Python script to generate the full report seems like the most efficient path forward.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "9cedccb4-cfaa-4c4b-9784-096001f70ab8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gp1dXRiTefiC32XNxEyt8C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4777,
      "cache_read_input_tokens": 53980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4777
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

_source line 43_

Now I have all the data. Let me build the comprehensive analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "0bb4b44d-e47c-4099-924d-48047a42c63f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gp1dXRiTefiC32XNxEyt8C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4777,
      "cache_read_input_tokens": 53980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4777
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

<details open><summary>🔧 Tool call — Write · `toolu_01MeoBZqBn9VwsiKBg5z9Btu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis_v2.py",
  "content": "#!/usr/bin/env python3\n\"\"\"NVE Threshold Sensitivity Analysis V2 — with combined diagnostic criteria and dual methods.\"\"\"\n\nimport json\nimport math\nfrom collections import OrderedDict\n\n# ============================================================\n# Walker baseline VE ratio per step (from exp_001_baseline s1)\n# ============================================================\nWALKER_BASELINE_VE = {\n    15: 0.02, 25: 0.087, 35: 0.241, 45: 0.331, 55: 0.404,\n    65: 0.563, 75: 0.719, 85: 0.701, 95: 0.632, 105: 0.656,\n}\nCHEETAH_BASELINE_VE = {\n    15: 0.02, 25: 0.1, 35: 0.2, 45: 0.3, 55: 0.4,\n    65: 0.5, 75: 0.55, 85: 0.6, 95: 0.65, 105: 0.65,\n}\n\nWALKER_BASELINE_EVAL = 915.67\nCHEETAH_BASELINE_EVAL = 446.1\n\n# ============================================================\n# Dataset: 61 experiments from V1 with ground truth labels\n# ============================================================\n# Format: (exp_id, env, config, ground_truth_civo, nve_peak_methodA,\n#          ve_ratio_peak_methodB, nve_trajectory_dict, eval_trajectory_dict)\n# nve_trajectory: {step_K: nve_value} or None\n# ve_ratio_trajectory: {step_K: raw_ve_ratio} or None\n\nexperiments = [\n    # --- CIVO positive (25) ---\n    {\"id\": \"exp_006_fixed_dt2\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.835,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008d_civo_trigger_s3\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 1.530,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008d_civo_trigger_s4\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.620,\n     \"ve_ratio_peak\": 3.0294, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008d_subsample_on_h8\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.124,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_s3\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.020,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_walker_s2\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 3.780,\n     \"ve_ratio_peak\": 2.481,\n     \"nve_traj\": {25: 1.64, 35: 1.03, 45: 1.06, 55: 1.02, 65: 0.90, 75: 0.66, 85: 0.68, 95: 1.34, 105: 3.78},\n     \"ve_traj\": {25: 0.143, 35: 0.249, 45: 0.351, 55: 0.413, 65: 0.507, 75: 0.473, 85: 0.474, 95: 0.85, 105: 2.481},\n     \"eval_traj\": None},\n    {\"id\": \"exp_009b_008d_walker_s2\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 1.620,\n     \"ve_ratio_peak\": 0.5703, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_009e_008d_walker_s1\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.130,\n     \"ve_ratio_peak\": 1.6663, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_010b_cheetah_civo_trigger\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 8.270,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_010b_cheetah_civo_trigger_s0\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 70.640,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_021_full_sgs_cheetah_s1\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 9.940,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_027_tcn_walker_s0\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 3.965,\n     \"ve_ratio_peak\": 3.965,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.02, 25: 0.11, 35: 0.235, 45: 0.86, 55: 1.679, 65: 1.544, 75: 0.831, 85: 3.965, 95: 0.675, 105: 0.916},\n     \"eval_traj\": None},\n    {\"id\": \"exp_027_tcn_walker_s1\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 1.637,\n     \"ve_ratio_peak\": 1.6367,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.0246, 25: 0.1416, 35: 0.3585, 45: 0.6101, 55: 0.7092, 65: 0.4875, 75: 0.4902, 85: 1.4104, 95: 1.6367, 105: 0.6444},\n     \"eval_traj\": None},\n    {\"id\": \"exp_029b_tcn_walker_s2_sigma02\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 2.765,\n     \"ve_ratio_peak\": 2.765,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.03, 25: 0.174, 35: 0.335, 45: 0.477, 55: 0.583, 65: 1.014, 75: 1.65, 85: 1.623, 95: 2.109, 105: 2.765},\n     \"eval_traj\": None},\n    {\"id\": \"exp_029d_tcn_walker_s3_sigma02\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 3.000,\n     \"ve_ratio_peak\": 3.0,\n     \"nve_traj\": None,\n     \"ve_traj\": {45: 0.695, 55: 0.598, 65: 0.863, 75: 0.791, 85: 0.9, 95: 0.7, 105: 3.0},\n     \"eval_traj\": None},\n    {\"id\": \"exp_030b_tcn_cheetah_s0_sigma05\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 10.666,\n     \"ve_ratio_peak\": 10.6657,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.0202, 25: 0.0636, 35: 0.1238, 45: 1.9141, 55: 10.6657, 65: 0.8371, 75: 1.9823, 85: 1.0946, 95: 0.2253, 105: 0.2686},\n     \"eval_traj\": None},\n    {\"id\": \"exp_031b_tcn_pickcube_s0_sigma05\", \"env\": \"pickcube\", \"gt\": 1, \"nve_peak\": 3.300,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_034_dual_critic_cheetah\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 4.500,\n     \"ve_ratio_peak\": 1.8, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_036_dual_critic_pickcube\", \"env\": \"pickcube\", \"gt\": 1, \"nve_peak\": 2.300,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_037_wide_critic_cheetah\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 3.600,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_045_treatment_extension_008d_s3\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.910,\n     \"ve_ratio_peak\": 4.91,\n     \"nve_traj\": None,\n     \"ve_traj\": {122: 4.77, 132: 4.91, 142: 0.43, 152: 0.21, 162: 0.25, 172: 0.18, 182: 0.16, 192: 0.13, 202: 0.12, 212: 0.1, 222: 0.1, 232: 0.09, 242: 0.07, 252: 0.08, 262: 0.07, 272: 0.08, 282: 0.07, 292: 0.06, 302: 0.05},\n     \"eval_traj\": {112: 58.5, 122: 41.8, 132: 35.1, 142: 350.2, 152: 646.4, 162: 482.3, 172: 600.4, 182: 600.5, 192: 699.5, 202: 684.3, 212: 758.6, 222: 744.6, 232: 745.4, 242: 869.7, 252: 721.6, 262: 820.6, 272: 716.2, 282: 755.6, 292: 843, 302: 867.6}},\n    {\"id\": \"exp_048_cheetah_civo_extension\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 2.750,\n     \"ve_ratio_peak\": 24.112, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_059_walker_trained_s5\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.720,\n     \"ve_ratio_peak\": 3.3075, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_068_008d_walker_repro_s1\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.120,\n     \"ve_ratio_peak\": 4.6,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0, 25: 0.2, 35: 0.3, 45: 0.6, 55: 0.6, 65: 1.3, 75: 1.6, 85: 4.6, 95: 4.6, 105: 2.7},\n     \"eval_traj\": None},\n    {\"id\": \"exp_078_cheetah_008d_s0\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 4.100,\n     \"ve_ratio_peak\": 2.318,\n     \"nve_traj\": {35: 1.24, 45: 1.7, 55: 3.66, 65: 3.55, 75: 4.1, 85: 2.74, 95: 2.26, 105: 0.48},\n     \"ve_traj\": {15: 0.039, 25: 0.056, 35: 0.11, 45: 0.295, 55: 0.908, 65: 1.72, 75: 2.318, 85: 2.022, 95: 1.366, 105: 0.291},\n     \"eval_traj\": {5: 8.3, 15: 41.3, 25: 170, 35: 213.7, 45: 148.9, 55: 64.5, 65: 36.8, 75: 26.1, 85: 26.7, 95: 32.5, 105: 119.5}},\n\n    # --- Healthy (36) ---\n    {\"id\": \"exp_008a_cheetah_unexposed_s0\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.490,\n     \"ve_ratio_peak\": 0.3193, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008a_cheetah_unexposed_s1\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.478,\n     \"ve_ratio_peak\": 0.3112, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008a_no_subsample_dt2\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.930,\n     \"ve_ratio_peak\": 0.93,  # max of normalized_ve series\n     \"nve_traj\": None,\n     \"ve_traj\": {55: 0.93, 65: 0.66, 75: 0.75, 85: 0.68, 95: 0.79, 105: 0.59},\n     \"eval_traj\": None},\n    {\"id\": \"exp_008a_unexposed_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.598,\n     \"ve_ratio_peak\": 0.43, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008a_unexposed_s2\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.463,\n     \"ve_ratio_peak\": 0.333, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_s4\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.990,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_subsample_on_dt1_h15\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.930,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.803,\n     \"ve_ratio_peak\": 0.527, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.020,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008f_s3_no_dt_embed_walker\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.490,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008f_s4\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.410,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_009c_s3\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.520,\n     \"ve_ratio_peak\": 0.386, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_015b_frozen_dt_emb\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.467,\n     \"ve_ratio_peak\": None,\n     \"nve_traj\": {85: 0.467, 95: 0.394, 105: 0.42},\n     \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_020_vanilla_dreamerv3_s2\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.983,\n     \"ve_ratio_peak\": 0.645, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_024b_cheetah_no_dt_emb_s0\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.200,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_024b_cheetah_no_dt_emb_s1\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.100,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_027_tcn_walker_s0_sigma02\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.908,\n     \"ve_ratio_peak\": 0.9081,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.0192, 25: 0.0961, 35: 0.1875, 45: 0.3009, 55: 0.5231, 65: 0.5654, 75: 0.611, 85: 0.4665, 95: 0.9081, 105: 0.5625},\n     \"eval_traj\": None},\n    {\"id\": \"exp_029a_tcn_walker_s1_sigma02\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.643,\n     \"ve_ratio_peak\": 0.6428,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.0248, 25: 0.1165, 35: 0.3574, 45: 0.5147, 55: 0.6428, 65: 0.4777, 75: 0.398, 85: 0.4033, 95: 0.3007, 105: 0.1554},\n     \"eval_traj\": None},\n    {\"id\": \"exp_032_dual_critic_walker\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.100,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_032b_dual_critic_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.400,\n     \"ve_ratio_peak\": None,\n     \"nve_traj\": {15: 0.0, 25: 0.2, 35: 0.4, 45: 0.8, 55: 0.7, 65: 0.7, 75: 0.7, 85: 1.4, 95: 0.7, 105: 0.5},\n     \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_042_frozen_dt_emb_walker\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.194,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_043_008f_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.808,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_046_frozen_dt_emb_cheetah\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 1.350,\n     \"ve_ratio_peak\": 0.4, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_047_frozen_dt_emb_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.710,\n     \"ve_ratio_peak\": 1.099, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_057_frozen_dt_emb_walker_s2\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.880,\n     \"ve_ratio_peak\": 1.283, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_058_frozen_dt_emb_cheetah_s1\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.780,\n     \"ve_ratio_peak\": 0.231, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_067_frozen_dt_emb_walker_plan015\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.400,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_069_008f_walker_repro_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.660,\n     \"ve_ratio_peak\": 0.4,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0, 25: 0.1, 35: 0.2, 45: 0.2, 55: 0.3, 65: 0.3, 75: 0.4, 85: 0.3, 95: 0.3, 105: 0.4},\n     \"eval_traj\": {5: 30.5, 15: 158.7, 25: 180.8, 35: 250.3, 45: 293.6, 55: 272.2, 65: 328.1, 75: 244.8, 85: 382.5, 95: 390.1, 105: 237.8}},\n    {\"id\": \"exp_070_008e_v3_walker_s0\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.800,\n     \"ve_ratio_peak\": 0.8,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0, 25: 0.1, 35: 0.2, 45: 0.3, 55: 0.4, 65: 0.5, 75: 0.6, 85: 0.5, 95: 0.8, 105: 0.8},\n     \"eval_traj\": {5: 37.4, 15: 93.2, 25: 178.8, 35: 221.6, 45: 230.9, 55: 232.5, 65: 194, 75: 175.2, 85: 218.6, 95: 139.6, 105: 148}},\n    {\"id\": \"exp_071_008f_walker_s3\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.974,\n     \"ve_ratio_peak\": 0.7, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_072_008e_v3_walker_s5\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.610,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_073_008f_walker_s4\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.760,\n     \"ve_ratio_peak\": 0.5, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_082_cheetah_no_dt_emb_s0\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 1.580,\n     \"ve_ratio_peak\": 0.955,\n     \"nve_traj\": {35: 1.49, 45: 0.59, 55: 0.96, 65: 0.55, 75: 0.55, 85: 0.98, 95: 1.58, 105: 1.02},\n     \"ve_traj\": {15: 0.038, 25: 0.069, 35: 0.132, 45: 0.103, 55: 0.237, 65: 0.268, 75: 0.311, 85: 0.724, 95: 0.955, 105: 0.616},\n     \"eval_traj\": {5: 6.8, 15: 32.2, 25: 108.4, 35: 119.4, 45: 239.3, 55: 157, 65: 180.1, 75: 178.6, 85: 84.2, 95: 57.7, 105: 83.2}},\n    {\"id\": \"exp_084_frozen_dt_emb_walker_s0\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.370,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_085_frozen_dt_emb_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.310,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_087_frozen_dt_emb_cheetah_s1\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.299,\n     \"ve_ratio_peak\": 0.2, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n]\n\n\ndef compute_nve_from_ve(ve_traj, env):\n    \"\"\"Compute NVE trajectory from raw ve_ratio trajectory.\"\"\"\n    baseline = WALKER_BASELINE_VE if env == \"walker\" else CHEETAH_BASELINE_VE\n    nve = {}\n    for step_k, ve in sorted(ve_traj.items()):\n        bl = baseline.get(step_k)\n        if bl and bl > 0.05:  # skip very early steps where baseline near 0\n            nve[step_k] = ve / bl\n    return nve\n\n\ndef check_condition_b(nve_series, threshold):\n    \"\"\"Check if NVE > threshold for >= 2 consecutive eval points.\"\"\"\n    sorted_steps = sorted(nve_series.keys())\n    consecutive = 0\n    for step in sorted_steps:\n        if nve_series[step] > threshold:\n            consecutive += 1\n            if consecutive >= 2:\n                return True\n        else:\n            consecutive = 0\n    return False\n\n\ndef check_condition_c_from_nve(nve_series):\n    \"\"\"Check if NVE shows upward trend.\n    Simplified: check if there's a window where NVE increases for >= 2 consecutive steps.\n    \"\"\"\n    sorted_steps = sorted(nve_series.keys())\n    vals = [nve_series[s] for s in sorted_steps]\n    for i in range(len(vals) - 1):\n        if vals[i + 1] > vals[i] * 1.1:  # 10% increase\n            return True\n    return False\n\n\ndef check_condition_c_with_eval(nve_series, eval_series):\n    \"\"\"Check if NVE uptrend accompanies eval decline.\"\"\"\n    nve_steps = sorted(nve_series.keys())\n    eval_steps = sorted(eval_series.keys())\n    common_steps = sorted(set(nve_steps) & set(eval_steps))\n    if len(common_steps) < 3:\n        return check_condition_c_from_nve(nve_series)\n\n    for i in range(len(common_steps) - 1):\n        s1, s2 = common_steps[i], common_steps[i + 1]\n        nve_up = nve_series[s2] > nve_series[s1] * 1.05\n        eval_down = eval_series[s2] < eval_series[s1] * 0.9\n        if nve_up and eval_down:\n            return True\n    return False\n\n\ndef compute_auroc(scores, labels):\n    \"\"\"Compute AUROC using trapezoidal rule.\"\"\"\n    pairs = sorted(zip(scores, labels), key=lambda x: -x[0])\n    n_pos = sum(labels)\n    n_neg = len(labels) - n_pos\n    if n_pos == 0 or n_neg == 0:\n        return float('nan')\n    tp, fp = 0, 0\n    prev_tp, prev_fp = 0, 0\n    auc = 0.0\n    prev_score = None\n    for score, label in pairs:\n        if score != prev_score and prev_score is not None:\n            auc += (fp - prev_fp) * (tp + prev_tp) / 2.0\n            prev_tp, prev_fp = tp, fp\n        if label == 1:\n            tp += 1\n        else:\n            fp += 1\n        prev_score = score\n    auc += (fp - prev_fp) * (tp + prev_tp) / 2.0\n    return auc / (n_pos * n_neg)\n\n\ndef threshold_analysis(scores_labels, thresholds):\n    \"\"\"Run threshold analysis for given scores and labels.\"\"\"\n    results = {}\n    for t in thresholds:\n        tp = fp = tn = fn = 0\n        fp_list = []\n        fn_list = []\n        for exp_id, score, label in scores_labels:\n            pred = 1 if score >= t else 0\n            if pred == 1 and label == 1:\n                tp += 1\n            elif pred == 1 and label == 0:\n                fp += 1\n                fp_list.append((exp_id, score))\n            elif pred == 0 and label == 0:\n                tn += 1\n            else:\n                fn += 1\n                fn_list.append((exp_id, score))\n        total = tp + fp + tn + fn\n        acc = (tp + tn) / total if total > 0 else 0\n        prec = tp / (tp + fp) if (tp + fp) > 0 else 0\n        rec = tp / (tp + fn) if (tp + fn) > 0 else 0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0\n        results[t] = {\n            \"acc\": acc, \"prec\": prec, \"rec\": rec, \"f1\": f1,\n            \"tp\": tp, \"fp\": fp, \"tn\": tn, \"fn\": fn,\n            \"fp_list\": fp_list, \"fn_list\": fn_list,\n        }\n    return results\n\n\ndef combined_diagnostic(exp, threshold):\n    \"\"\"Apply combined A+B+C diagnostic. Returns (positive, reasons).\"\"\"\n    nve_peak = exp[\"nve_peak\"]\n\n    # Condition A: NVE_peak > threshold\n    cond_a = nve_peak >= threshold\n\n    # Get NVE trajectory\n    nve_traj = exp.get(\"nve_traj\")\n    ve_traj = exp.get(\"ve_traj\")\n    eval_traj = exp.get(\"eval_traj\")\n\n    if nve_traj is None and ve_traj is not None:\n        nve_traj = compute_nve_from_ve(ve_traj, exp[\"env\"])\n\n    has_traj = nve_traj is not None and len(nve_traj) >= 3\n\n    if not has_traj:\n        # Without trajectory, can only apply condition A\n        # Return A-only result with note\n        return cond_a, \"A_only (no trajectory data)\"\n\n    # Condition B: NVE > threshold for >= 2 consecutive eval points\n    cond_b = check_condition_b(nve_traj, threshold)\n\n    # Condition C: NVE uptrend precedes/accompanies eval decline\n    if eval_traj is not None:\n        cond_c = check_condition_c_with_eval(nve_traj, eval_traj)\n    else:\n        cond_c = check_condition_c_from_nve(nve_traj)\n\n    positive = cond_a and cond_b and cond_c\n    reasons = f\"A={'Y' if cond_a else 'N'} B={'Y' if cond_b else 'N'} C={'Y' if cond_c else 'N'}\"\n    return positive, reasons\n\n\ndef compute_median_last5(nve_traj):\n    \"\"\"Compute median of last 5 NVE values.\"\"\"\n    if nve_traj is None or len(nve_traj) == 0:\n        return None\n    sorted_vals = [nve_traj[k] for k in sorted(nve_traj.keys())]\n    last5 = sorted_vals[-5:] if len(sorted_vals) >= 5 else sorted_vals\n    last5_sorted = sorted(last5)\n    n = len(last5_sorted)\n    if n % 2 == 1:\n        return last5_sorted[n // 2]\n    return (last5_sorted[n // 2 - 1] + last5_sorted[n // 2]) / 2\n\n\n# ============================================================\n# Main Analysis\n# ============================================================\n\nprint(\"=\" * 80)\nprint(\"NVE Threshold Sensitivity Analysis V2\")\nprint(\"=\" * 80)\n\n# --- Dataset summary ---\nn_total = len(experiments)\nn_civo = sum(1 for e in experiments if e[\"gt\"] == 1)\nn_healthy = sum(1 for e in experiments if e[\"gt\"] == 0)\nn_with_ve_peak = sum(1 for e in experiments if e[\"ve_ratio_peak\"] is not None)\nn_with_traj = sum(1 for e in experiments if e.get(\"ve_traj\") or e.get(\"nve_traj\"))\n\nprint(f\"\\nDataset: N={n_total} (CIVO={n_civo}, Healthy={n_healthy})\")\nprint(f\"Method B coverage: {n_with_ve_peak}/{n_total} have ve_ratio_peak\")\nprint(f\"Trajectory coverage: {n_with_traj}/{n_total} have time series data\")\n\n# --- Method A: Step-matched NVE ---\nprint(\"\\n\" + \"=\" * 80)\nprint(\"METHOD A: Step-matched NVE (nve_peak)\")\nprint(\"=\" * 80)\n\nmethod_a_data = [(e[\"id\"], e[\"nve_peak\"], e[\"gt\"]) for e in experiments]\nthresholds = [1.3, 1.5, 1.7, 2.0]\n\nprint(\"\\n### Single Threshold\")\nresults_a = threshold_analysis(method_a_data, thresholds)\nfor t in thresholds:\n    r = results_a[t]\n    print(f\"\\nθ = {t:.1f}×:\")\n    print(f\"  Acc={r['acc']:.1%} Prec={r['prec']:.1%} Rec={r['rec']:.1%} F1={r['f1']:.3f}\")\n    print(f\"  TP={r['tp']} FP={r['fp']} TN={r['tn']} FN={r['fn']}\")\n    if r['fp_list']:\n        print(f\"  FP: {', '.join(f'{x[0]}({x[1]:.2f})' for x in r['fp_list'])}\")\n    if r['fn_list']:\n        print(f\"  FN: {', '.join(f'{x[0]}({x[1]:.2f})' for x in r['fn_list'])}\")\n\nscores_a = [e[\"nve_peak\"] for e in experiments]\nlabels = [e[\"gt\"] for e in experiments]\nauroc_a = compute_auroc(scores_a, labels)\nprint(f\"\\nAUROC (Method A): {auroc_a:.4f}\")\n\n# --- Method A combined diagnostic ---\nprint(\"\\n### Combined Diagnostic (A+B+C)\")\nfor t in thresholds:\n    tp = fp = tn = fn = 0\n    a_only_count = 0\n    fp_list = []\n    fn_list = []\n    for e in experiments:\n        positive, reasons = combined_diagnostic(e, t)\n        if \"A_only\" in reasons:\n            a_only_count += 1\n        if positive and e[\"gt\"] == 1:\n            tp += 1\n        elif positive and e[\"gt\"] == 0:\n            fp += 1\n            fp_list.append((e[\"id\"], e[\"nve_peak\"], reasons))\n        elif not positive and e[\"gt\"] == 0:\n            tn += 1\n        else:\n            fn += 1\n            fn_list.append((e[\"id\"], e[\"nve_peak\"], reasons))\n    total = tp + fp + tn + fn\n    acc = (tp + tn) / total if total > 0 else 0\n    prec = tp / (tp + fp) if (tp + fp) > 0 else 0\n    rec = tp / (tp + fn) if (tp + fn) > 0 else 0\n    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0\n    print(f\"\\nθ = {t:.1f}× (A_only fallback: {a_only_count}/{n_total}):\")\n    print(f\"  Acc={acc:.1%} Prec={prec:.1%} Rec={rec:.1%} F1={f1:.3f}\")\n    print(f\"  TP={tp} FP={fp} TN={tn} FN={fn}\")\n    if fp_list:\n        print(f\"  FP: {', '.join(f'{x[0]}({x[1]:.2f}, {x[2]})' for x in fp_list)}\")\n    if fn_list:\n        print(f\"  FN: {', '.join(f'{x[0]}({x[1]:.2f}, {x[2]})' for x in fn_list)}\")\n\n\n# --- Method B: Raw ve_ratio_peak ---\nprint(\"\\n\" + \"=\" * 80)\nprint(\"METHOD B: Raw ve_ratio_peak\")\nprint(\"=\" * 80)\n\nmethod_b_exps = [e for e in experiments if e[\"ve_ratio_peak\"] is not None]\nn_b = len(method_b_exps)\nn_b_civo = sum(1 for e in method_b_exps if e[\"gt\"] == 1)\nn_b_healthy = sum(1 for e in method_b_exps if e[\"gt\"] == 0)\nprint(f\"\\nSubset with ve_ratio_peak: N={n_b} (CIVO={n_b_civo}, Healthy={n_b_healthy})\")\n\nmethod_b_data = [(e[\"id\"], e[\"ve_ratio_peak\"], e[\"gt\"]) for e in method_b_exps]\nthresholds_b = [0.8, 1.0, 1.3, 1.5, 2.0]\n\nprint(\"\\n### Single Threshold\")\nresults_b = threshold_analysis(method_b_data, thresholds_b)\nfor t in thresholds_b:\n    r = results_b[t]\n    print(f\"\\nθ = {t:.1f}×:\")\n    print(f\"  Acc={r['acc']:.1%} Prec={r['prec']:.1%} Rec={r['rec']:.1%} F1={r['f1']:.3f}\")\n    print(f\"  TP={r['tp']} FP={r['fp']} TN={r['tn']} FN={r['fn']}\")\n    if r['fp_list']:\n        print(f\"  FP: {', '.join(f'{x[0]}({x[1]:.3f})' for x in r['fp_list'])}\")\n    if r['fn_list']:\n        print(f\"  FN: {', '.join(f'{x[0]}({x[1]:.3f})' for x in r['fn_list'])}\")\n\nscores_b = [e[\"ve_ratio_peak\"] for e in method_b_exps]\nlabels_b = [e[\"gt\"] for e in method_b_exps]\nauroc_b = compute_auroc(scores_b, labels_b)\nprint(f\"\\nAUROC (Method B): {auroc_b:.4f}\")\n\n# --- Method B combined diagnostic ---\nprint(\"\\n### Combined Diagnostic (A+B+C) — using ve_ratio_peak as threshold basis\")\nfor t in thresholds_b:\n    tp = fp = tn = fn = 0\n    for e in method_b_exps:\n        # For method B combined, we use ve_ratio_peak for condition A\n        # and ve_ratio trajectory for conditions B and C\n        ve_peak = e[\"ve_ratio_peak\"]\n        cond_a = ve_peak >= t\n\n        ve_traj = e.get(\"ve_traj\")\n        has_traj = ve_traj is not None and len(ve_traj) >= 3\n\n        if not has_traj:\n            positive = cond_a\n        else:\n            sorted_steps = sorted(ve_traj.keys())\n            vals = [ve_traj[s] for s in sorted_steps]\n            # Condition B: ve_ratio > threshold for >= 2 consecutive\n            consec = 0\n            cond_b = False\n            for v in vals:\n                if v >= t:\n                    consec += 1\n                    if consec >= 2:\n                        cond_b = True\n                        break\n                else:\n                    consec = 0\n            # Condition C: uptrend\n            cond_c = False\n            for i in range(len(vals) - 1):\n                if vals[i + 1] > vals[i] * 1.1:\n                    cond_c = True\n                    break\n            positive = cond_a and cond_b and cond_c\n\n        if positive and e[\"gt\"] == 1:\n            tp += 1\n        elif positive and e[\"gt\"] == 0:\n            fp += 1\n        elif not positive and e[\"gt\"] == 0:\n            tn += 1\n        else:\n            fn += 1\n    total = tp + fp + tn + fn\n    acc = (tp + tn) / total if total > 0 else 0\n    prec = tp / (tp + fp) if (tp + fp) > 0 else 0\n    rec = tp / (tp + fn) if (tp + fn) > 0 else 0\n    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0\n    print(f\"\\nθ = {t:.1f}×:\")\n    print(f\"  Acc={acc:.1%} Prec={prec:.1%} Rec={rec:.1%} F1={f1:.3f}\")\n    print(f\"  TP={tp} FP={fp} TN={tn} FN={fn}\")\n\n\n# --- NVE_median_last5 ---\nprint(\"\\n\" + \"=\" * 80)\nprint(\"NVE_median_last5 Auxiliary Metric\")\nprint(\"=\" * 80)\n\nmedian_results = []\nfor e in experiments:\n    nve_traj = e.get(\"nve_traj\")\n    ve_traj = e.get(\"ve_traj\")\n    if nve_traj is None and ve_traj is not None:\n        nve_traj = compute_nve_from_ve(ve_traj, e[\"env\"])\n    if nve_traj is not None and len(nve_traj) >= 3:\n        med = compute_median_last5(nve_traj)\n        label = \"CIVO\" if e[\"gt\"] == 1 else \"Healthy\"\n        correct = (med > 1.0 and e[\"gt\"] == 1) or (med <= 1.0 and e[\"gt\"] == 0)\n        median_results.append((e[\"id\"], label, med, correct))\n\nprint(f\"\\nExperiments with sufficient trajectory data: {len(median_results)}\")\nprint(f\"\\n{'exp_id':<45} {'type':<8} {'median_last5':>12} {'correct':>8}\")\nprint(\"-\" * 75)\nfor eid, label, med, correct in median_results:\n    print(f\"{eid:<45} {label:<8} {med:>12.3f} {'✓' if correct else '✗':>8}\")\n\n# Summary stats\ncivo_meds = [m for _, l, m, _ in median_results if l == \"CIVO\"]\nhealthy_meds = [m for _, l, m, _ in median_results if l == \"Healthy\"]\nif civo_meds:\n    print(f\"\\nCIVO median_last5: min={min(civo_meds):.3f}, median={sorted(civo_meds)[len(civo_meds)//2]:.3f}, max={max(civo_meds):.3f}\")\nif healthy_meds:\n    print(f\"Healthy median_last5: min={min(healthy_meds):.3f}, median={sorted(healthy_meds)[len(healthy_meds)//2]:.3f}, max={max(healthy_meds):.3f}\")\ncorrect_count = sum(1 for _, _, _, c in median_results if c)\nprint(f\"Accuracy: {correct_count}/{len(median_results)} = {correct_count/len(median_results):.1%}\")\n\n\n# --- Distribution analysis ---\nprint(\"\\n\" + \"=\" * 80)\nprint(\"Distribution Analysis\")\nprint(\"=\" * 80)\n\ncivo_nve = sorted([e[\"nve_peak\"] for e in experiments if e[\"gt\"] == 1])\nhealthy_nve = sorted([e[\"nve_peak\"] for e in experiments if e[\"gt\"] == 0])\n\nprint(f\"\\nMethod A NVE_peak distribution:\")\nprint(f\"  CIVO (N={len(civo_nve)}): min={min(civo_nve):.3f}, median={civo_nve[len(civo_nve)//2]:.3f}, max={max(civo_nve):.3f}, mean={sum(civo_nve)/len(civo_nve):.3f}\")\nprint(f\"  Healthy (N={len(healthy_nve)}): min={min(healthy_nve):.3f}, median={healthy_nve[len(healthy_nve)//2]:.3f}, max={max(healthy_nve):.3f}, mean={sum(healthy_nve)/len(healthy_nve):.3f}\")\n\ncivo_ve = sorted([e[\"ve_ratio_peak\"] for e in experiments if e[\"gt\"] == 1 and e[\"ve_ratio_peak\"] is not None])\nhealthy_ve = sorted([e[\"ve_ratio_peak\"] for e in experiments if e[\"gt\"] == 0 and e[\"ve_ratio_peak\"] is not None])\n\nif civo_ve and healthy_ve:\n    print(f\"\\nMethod B ve_ratio_peak distribution:\")\n    print(f\"  CIVO (N={len(civo_ve)}): min={min(civo_ve):.3f}, median={civo_ve[len(civo_ve)//2]:.3f}, max={max(civo_ve):.3f}, mean={sum(civo_ve)/len(civo_ve):.3f}\")\n    print(f\"  Healthy (N={len(healthy_ve)}): min={min(healthy_ve):.3f}, median={healthy_ve[len(healthy_ve)//2]:.3f}, max={max(healthy_ve):.3f}, mean={sum(healthy_ve)/len(healthy_ve):.3f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "1e77c98e-adea-4040-b06a-c8ccb0445ea7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gp1dXRiTefiC32XNxEyt8C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4777,
      "cache_read_input_tokens": 53980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4777
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

_source line 45 · 2026-05-25T20:25:29.583Z_

<details><summary>↩ Tool result · `toolu_01MeoBZqBn9VwsiKBg5z9Btu`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis_v2.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "4b677251-782c-430f-887e-d1d94fc8029e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis_v2.py",
    "content": "#!/usr/bin/env python3\n\"\"\"NVE Threshold Sensitivity Analysis V2 — with combined diagnostic criteria and dual methods.\"\"\"\n\nimport json\nimport math\nfrom collections import OrderedDict\n\n# ============================================================\n# Walker baseline VE ratio per step (from exp_001_baseline s1)\n# ============================================================\nWALKER_BASELINE_VE = {\n    15: 0.02, 25: 0.087, 35: 0.241, 45: 0.331, 55: 0.404,\n    65: 0.563, 75: 0.719, 85: 0.701, 95: 0.632, 105: 0.656,\n}\nCHEETAH_BASELINE_VE = {\n    15: 0.02, 25: 0.1, 35: 0.2, 45: 0.3, 55: 0.4,\n    65: 0.5, 75: 0.55, 85: 0.6, 95: 0.65, 105: 0.65,\n}\n\nWALKER_BASELINE_EVAL = 915.67\nCHEETAH_BASELINE_EVAL = 446.1\n\n# ============================================================\n# Dataset: 61 experiments from V1 with ground truth labels\n# ============================================================\n# Format: (exp_id, env, config, ground_truth_civo, nve_peak_methodA,\n#          ve_ratio_peak_methodB, nve_trajectory_dict, eval_trajectory_dict)\n# nve_trajectory: {step_K: nve_value} or None\n# ve_ratio_trajectory: {step_K: raw_ve_ratio} or None\n\nexperiments = [\n    # --- CIVO positive (25) ---\n    {\"id\": \"exp_006_fixed_dt2\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.835,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008d_civo_trigger_s3\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 1.530,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008d_civo_trigger_s4\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.620,\n     \"ve_ratio_peak\": 3.0294, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008d_subsample_on_h8\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.124,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_s3\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.020,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_walker_s2\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 3.780,\n     \"ve_ratio_peak\": 2.481,\n     \"nve_traj\": {25: 1.64, 35: 1.03, 45: 1.06, 55: 1.02, 65: 0.90, 75: 0.66, 85: 0.68, 95: 1.34, 105: 3.78},\n     \"ve_traj\": {25: 0.143, 35: 0.249, 45: 0.351, 55: 0.413, 65: 0.507, 75: 0.473, 85: 0.474, 95: 0.85, 105: 2.481},\n     \"eval_traj\": None},\n    {\"id\": \"exp_009b_008d_walker_s2\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 1.620,\n     \"ve_ratio_peak\": 0.5703, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_009e_008d_walker_s1\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.130,\n     \"ve_ratio_peak\": 1.6663, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_010b_cheetah_civo_trigger\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 8.270,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_010b_cheetah_civo_trigger_s0\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 70.640,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_021_full_sgs_cheetah_s1\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 9.940,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_027_tcn_walker_s0\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 3.965,\n     \"ve_ratio_peak\": 3.965,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.02, 25: 0.11, 35: 0.235, 45: 0.86, 55: 1.679, 65: 1.544, 75: 0.831, 85: 3.965, 95: 0.675, 105: 0.916},\n     \"eval_traj\": None},\n    {\"id\": \"exp_027_tcn_walker_s1\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 1.637,\n     \"ve_ratio_peak\": 1.6367,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.0246, 25: 0.1416, 35: 0.3585, 45: 0.6101, 55: 0.7092, 65: 0.4875, 75: 0.4902, 85: 1.4104, 95: 1.6367, 105: 0.6444},\n     \"eval_traj\": None},\n    {\"id\": \"exp_029b_tcn_walker_s2_sigma02\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 2.765,\n     \"ve_ratio_peak\": 2.765,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.03, 25: 0.174, 35: 0.335, 45: 0.477, 55: 0.583, 65: 1.014, 75: 1.65, 85: 1.623, 95: 2.109, 105: 2.765},\n     \"eval_traj\": None},\n    {\"id\": \"exp_029d_tcn_walker_s3_sigma02\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 3.000,\n     \"ve_ratio_peak\": 3.0,\n     \"nve_traj\": None,\n     \"ve_traj\": {45: 0.695, 55: 0.598, 65: 0.863, 75: 0.791, 85: 0.9, 95: 0.7, 105: 3.0},\n     \"eval_traj\": None},\n    {\"id\": \"exp_030b_tcn_cheetah_s0_sigma05\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 10.666,\n     \"ve_ratio_peak\": 10.6657,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.0202, 25: 0.0636, 35: 0.1238, 45: 1.9141, 55: 10.6657, 65: 0.8371, 75: 1.9823, 85: 1.0946, 95: 0.2253, 105: 0.2686},\n     \"eval_traj\": None},\n    {\"id\": \"exp_031b_tcn_pickcube_s0_sigma05\", \"env\": \"pickcube\", \"gt\": 1, \"nve_peak\": 3.300,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_034_dual_critic_cheetah\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 4.500,\n     \"ve_ratio_peak\": 1.8, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_036_dual_critic_pickcube\", \"env\": \"pickcube\", \"gt\": 1, \"nve_peak\": 2.300,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_037_wide_critic_cheetah\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 3.600,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_045_treatment_extension_008d_s3\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.910,\n     \"ve_ratio_peak\": 4.91,\n     \"nve_traj\": None,\n     \"ve_traj\": {122: 4.77, 132: 4.91, 142: 0.43, 152: 0.21, 162: 0.25, 172: 0.18, 182: 0.16, 192: 0.13, 202: 0.12, 212: 0.1, 222: 0.1, 232: 0.09, 242: 0.07, 252: 0.08, 262: 0.07, 272: 0.08, 282: 0.07, 292: 0.06, 302: 0.05},\n     \"eval_traj\": {112: 58.5, 122: 41.8, 132: 35.1, 142: 350.2, 152: 646.4, 162: 482.3, 172: 600.4, 182: 600.5, 192: 699.5, 202: 684.3, 212: 758.6, 222: 744.6, 232: 745.4, 242: 869.7, 252: 721.6, 262: 820.6, 272: 716.2, 282: 755.6, 292: 843, 302: 867.6}},\n    {\"id\": \"exp_048_cheetah_civo_extension\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 2.750,\n     \"ve_ratio_peak\": 24.112, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_059_walker_trained_s5\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.720,\n     \"ve_ratio_peak\": 3.3075, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_068_008d_walker_repro_s1\", \"env\": \"walker\", \"gt\": 1, \"nve_peak\": 4.120,\n     \"ve_ratio_peak\": 4.6,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0, 25: 0.2, 35: 0.3, 45: 0.6, 55: 0.6, 65: 1.3, 75: 1.6, 85: 4.6, 95: 4.6, 105: 2.7},\n     \"eval_traj\": None},\n    {\"id\": \"exp_078_cheetah_008d_s0\", \"env\": \"cheetah\", \"gt\": 1, \"nve_peak\": 4.100,\n     \"ve_ratio_peak\": 2.318,\n     \"nve_traj\": {35: 1.24, 45: 1.7, 55: 3.66, 65: 3.55, 75: 4.1, 85: 2.74, 95: 2.26, 105: 0.48},\n     \"ve_traj\": {15: 0.039, 25: 0.056, 35: 0.11, 45: 0.295, 55: 0.908, 65: 1.72, 75: 2.318, 85: 2.022, 95: 1.366, 105: 0.291},\n     \"eval_traj\": {5: 8.3, 15: 41.3, 25: 170, 35: 213.7, 45: 148.9, 55: 64.5, 65: 36.8, 75: 26.1, 85: 26.7, 95: 32.5, 105: 119.5}},\n\n    # --- Healthy (36) ---\n    {\"id\": \"exp_008a_cheetah_unexposed_s0\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.490,\n     \"ve_ratio_peak\": 0.3193, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008a_cheetah_unexposed_s1\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.478,\n     \"ve_ratio_peak\": 0.3112, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008a_no_subsample_dt2\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.930,\n     \"ve_ratio_peak\": 0.93,  # max of normalized_ve series\n     \"nve_traj\": None,\n     \"ve_traj\": {55: 0.93, 65: 0.66, 75: 0.75, 85: 0.68, 95: 0.79, 105: 0.59},\n     \"eval_traj\": None},\n    {\"id\": \"exp_008a_unexposed_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.598,\n     \"ve_ratio_peak\": 0.43, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008a_unexposed_s2\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.463,\n     \"ve_ratio_peak\": 0.333, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_s4\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.990,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_subsample_on_dt1_h15\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.930,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008e_v3_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.803,\n     \"ve_ratio_peak\": 0.527, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.020,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008f_s3_no_dt_embed_walker\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.490,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_008f_s4\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.410,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_009c_s3\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.520,\n     \"ve_ratio_peak\": 0.386, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_015b_frozen_dt_emb\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.467,\n     \"ve_ratio_peak\": None,\n     \"nve_traj\": {85: 0.467, 95: 0.394, 105: 0.42},\n     \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_020_vanilla_dreamerv3_s2\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.983,\n     \"ve_ratio_peak\": 0.645, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_024b_cheetah_no_dt_emb_s0\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.200,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_024b_cheetah_no_dt_emb_s1\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.100,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_027_tcn_walker_s0_sigma02\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.908,\n     \"ve_ratio_peak\": 0.9081,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.0192, 25: 0.0961, 35: 0.1875, 45: 0.3009, 55: 0.5231, 65: 0.5654, 75: 0.611, 85: 0.4665, 95: 0.9081, 105: 0.5625},\n     \"eval_traj\": None},\n    {\"id\": \"exp_029a_tcn_walker_s1_sigma02\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.643,\n     \"ve_ratio_peak\": 0.6428,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0.0248, 25: 0.1165, 35: 0.3574, 45: 0.5147, 55: 0.6428, 65: 0.4777, 75: 0.398, 85: 0.4033, 95: 0.3007, 105: 0.1554},\n     \"eval_traj\": None},\n    {\"id\": \"exp_032_dual_critic_walker\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.100,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_032b_dual_critic_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.400,\n     \"ve_ratio_peak\": None,\n     \"nve_traj\": {15: 0.0, 25: 0.2, 35: 0.4, 45: 0.8, 55: 0.7, 65: 0.7, 75: 0.7, 85: 1.4, 95: 0.7, 105: 0.5},\n     \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_042_frozen_dt_emb_walker\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.194,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_043_008f_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.808,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_046_frozen_dt_emb_cheetah\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 1.350,\n     \"ve_ratio_peak\": 0.4, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_047_frozen_dt_emb_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.710,\n     \"ve_ratio_peak\": 1.099, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_057_frozen_dt_emb_walker_s2\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 1.880,\n     \"ve_ratio_peak\": 1.283, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_058_frozen_dt_emb_cheetah_s1\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.780,\n     \"ve_ratio_peak\": 0.231, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_067_frozen_dt_emb_walker_plan015\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.400,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_069_008f_walker_repro_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.660,\n     \"ve_ratio_peak\": 0.4,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0, 25: 0.1, 35: 0.2, 45: 0.2, 55: 0.3, 65: 0.3, 75: 0.4, 85: 0.3, 95: 0.3, 105: 0.4},\n     \"eval_traj\": {5: 30.5, 15: 158.7, 25: 180.8, 35: 250.3, 45: 293.6, 55: 272.2, 65: 328.1, 75: 244.8, 85: 382.5, 95: 390.1, 105: 237.8}},\n    {\"id\": \"exp_070_008e_v3_walker_s0\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.800,\n     \"ve_ratio_peak\": 0.8,\n     \"nve_traj\": None,\n     \"ve_traj\": {15: 0, 25: 0.1, 35: 0.2, 45: 0.3, 55: 0.4, 65: 0.5, 75: 0.6, 85: 0.5, 95: 0.8, 105: 0.8},\n     \"eval_traj\": {5: 37.4, 15: 93.2, 25: 178.8, 35: 221.6, 45: 230.9, 55: 232.5, 65: 194, 75: 175.2, 85: 218.6, 95: 139.6, 105: 148}},\n    {\"id\": \"exp_071_008f_walker_s3\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.974,\n     \"ve_ratio_peak\": 0.7, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_072_008e_v3_walker_s5\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.610,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_073_008f_walker_s4\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.760,\n     \"ve_ratio_peak\": 0.5, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_082_cheetah_no_dt_emb_s0\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 1.580,\n     \"ve_ratio_peak\": 0.955,\n     \"nve_traj\": {35: 1.49, 45: 0.59, 55: 0.96, 65: 0.55, 75: 0.55, 85: 0.98, 95: 1.58, 105: 1.02},\n     \"ve_traj\": {15: 0.038, 25: 0.069, 35: 0.132, 45: 0.103, 55: 0.237, 65: 0.268, 75: 0.311, 85: 0.724, 95: 0.955, 105: 0.616},\n     \"eval_traj\": {5: 6.8, 15: 32.2, 25: 108.4, 35: 119.4, 45: 239.3, 55: 157, 65: 180.1, 75: 178.6, 85: 84.2, 95: 57.7, 105: 83.2}},\n    {\"id\": \"exp_084_frozen_dt_emb_walker_s0\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.370,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_085_frozen_dt_emb_walker_s1\", \"env\": \"walker\", \"gt\": 0, \"nve_peak\": 0.310,\n     \"ve_ratio_peak\": None, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n    {\"id\": \"exp_087_frozen_dt_emb_cheetah_s1\", \"env\": \"cheetah\", \"gt\": 0, \"nve_peak\": 0.299,\n     \"ve_ratio_peak\": 0.2, \"nve_traj\": None, \"ve_traj\": None, \"eval_traj\": None},\n]\n\n\ndef compute_nve_from_ve(ve_traj, env):\n    \"\"\"Compute NVE trajectory from raw ve_ratio trajectory.\"\"\"\n    baseline = WALKER_BASELINE_VE if env == \"walker\" else CHEETAH_BASELINE_VE\n    nve = {}\n    for step_k, ve in sorted(ve_traj.items()):\n        bl = baseline.get(step_k)\n        if bl and bl > 0.05:  # skip very early steps where baseline near 0\n            nve[step_k] = ve / bl\n    return nve\n\n\ndef check_condition_b(nve_series, threshold):\n    \"\"\"Check if NVE > threshold for >= 2 consecutive eval points.\"\"\"\n    sorted_steps = sorted(nve_series.keys())\n    consecutive = 0\n    for step in sorted_steps:\n        if nve_series[step] > threshold:\n            consecutive += 1\n            if consecutive >= 2:\n                return True\n        else:\n            consecutive = 0\n    return False\n\n\ndef check_condition_c_from_nve(nve_series):\n    \"\"\"Check if NVE shows upward trend.\n    Simplified: check if there's a window where NVE increases for >= 2 consecutive steps.\n    \"\"\"\n    sorted_steps = sorted(nve_series.keys())\n    vals = [nve_series[s] for s in sorted_steps]\n    for i in range(len(vals) - 1):\n        if vals[i + 1] > vals[i] * 1.1:  # 10% increase\n            return True\n    return False\n\n\ndef check_condition_c_with_eval(nve_series, eval_series):\n    \"\"\"Check if NVE uptrend accompanies eval decline.\"\"\"\n    nve_steps = sorted(nve_series.keys())\n    eval_steps = sorted(eval_series.keys())\n    common_steps = sorted(set(nve_steps) & set(eval_steps))\n    if len(common_steps) < 3:\n        return check_condition_c_from_nve(nve_series)\n\n    for i in range(len(common_steps) - 1):\n        s1, s2 = common_steps[i], common_steps[i + 1]\n        nve_up = nve_series[s2] > nve_series[s1] * 1.05\n        eval_down = eval_series[s2] < eval_series[s1] * 0.9\n        if nve_up and eval_down:\n            return True\n    return False\n\n\ndef compute_auroc(scores, labels):\n    \"\"\"Compute AUROC using trapezoidal rule.\"\"\"\n    pairs = sorted(zip(scores, labels), key=lambda x: -x[0])\n    n_pos = sum(labels)\n    n_neg = len(labels) - n_pos\n    if n_pos == 0 or n_neg == 0:\n        return float('nan')\n    tp, fp = 0, 0\n    prev_tp, prev_fp = 0, 0\n    auc = 0.0\n    prev_score = None\n    for score, label in pairs:\n        if score != prev_score and prev_score is not None:\n            auc += (fp - prev_fp) * (tp + prev_tp) / 2.0\n            prev_tp, prev_fp = tp, fp\n        if label == 1:\n            tp += 1\n        else:\n            fp += 1\n        prev_score = score\n    auc += (fp - prev_fp) * (tp + prev_tp) / 2.0\n    return auc / (n_pos * n_neg)\n\n\ndef threshold_analysis(scores_labels, thresholds):\n    \"\"\"Run threshold analysis for given scores and labels.\"\"\"\n    results = {}\n    for t in thresholds:\n        tp = fp = tn = fn = 0\n        fp_list = []\n        fn_list = []\n        for exp_id, score, label in scores_labels:\n            pred = 1 if score >= t else 0\n            if pred == 1 and label == 1:\n                tp += 1\n            elif pred == 1 and label == 0:\n                fp += 1\n                fp_list.append((exp_id, score))\n            elif pred == 0 and label == 0:\n                tn += 1\n            else:\n                fn += 1\n                fn_list.append((exp_id, score))\n        total = tp + fp + tn + fn\n        acc = (tp + tn) / total if total > 0 else 0\n        prec = tp / (tp + fp) if (tp + fp) > 0 else 0\n        rec = tp / (tp + fn) if (tp + fn) > 0 else 0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0\n        results[t] = {\n            \"acc\": acc, \"prec\": prec, \"rec\": rec, \"f1\": f1,\n            \"tp\": tp, \"fp\": fp, \"tn\": tn, \"fn\": fn,\n            \"fp_list\": fp_list, \"fn_list\": fn_list,\n        }\n    return results\n\n\ndef combined_diagnostic(exp, threshold):\n    \"\"\"Apply combined A+B+C diagnostic. Returns (positive, reasons).\"\"\"\n    nve_peak = exp[\"nve_peak\"]\n\n    # Condition A: NVE_peak > threshold\n    cond_a = nve_peak >= threshold\n\n    # Get NVE trajectory\n    nve_traj = exp.get(\"nve_traj\")\n    ve_traj = exp.get(\"ve_traj\")\n    eval_traj = exp.get(\"eval_traj\")\n\n    if nve_traj is None and ve_traj is not None:\n        nve_traj = compute_nve_from_ve(ve_traj, exp[\"env\"])\n\n    has_traj = nve_traj is not None and len(nve_traj) >= 3\n\n    if not has_traj:\n        # Without trajectory, can only apply condition A\n        # Return A-only result with note\n        return cond_a, \"A_only (no trajectory data)\"\n\n    # Condition B: NVE > threshold for >= 2 consecutive eval points\n    cond_b = check_condition_b(nve_traj, threshold)\n\n    # Condition C: NVE uptrend precedes/accompanies eval decline\n    if eval_traj is not None:\n        cond_c = check_condition_c_with_eval(nve_traj, eval_traj)\n    else:\n        cond_c = check_condition_c_from_nve(nve_traj)\n\n    positive = cond_a and cond_b and cond_c\n    reasons = f\"A={'Y' if cond_a else 'N'} B={'Y' if cond_b else 'N'} C={'Y' if cond_c else 'N'}\"\n    return positive, reasons\n\n\ndef compute_median_last5(nve_traj):\n    \"\"\"Compute median of last 5 NVE values.\"\"\"\n    if nve_traj is None or len(nve_traj) == 0:\n        return None\n    sorted_vals = [nve_traj[k] for k in sorted(nve_traj.keys())]\n    last5 = sorted_vals[-5:] if len(sorted_vals) >= 5 else sorted_vals\n    last5_sorted = sorted(last5)\n    n = len(last5_sorted)\n    if n % 2 == 1:\n        return last5_sorted[n // 2]\n    return (last5_sorted[n // 2 - 1] + last5_sorted[n // 2]) / 2\n\n\n# ============================================================\n# Main Analysis\n# ============================================================\n\nprint(\"=\" * 80)\nprint(\"NVE Threshold Sensitivity Analysis V2\")\nprint(\"=\" * 80)\n\n# --- Dataset summary ---\nn_total = len(experiments)\nn_civo = sum(1 for e in experiments if e[\"gt\"] == 1)\nn_healthy = sum(1 for e in experiments if e[\"gt\"] == 0)\nn_with_ve_peak = sum(1 for e in experiments if e[\"ve_ratio_peak\"] is not None)\nn_with_traj = sum(1 for e in experiments if e.get(\"ve_traj\") or e.get(\"nve_traj\"))\n\nprint(f\"\\nDataset: N={n_total} (CIVO={n_civo}, Healthy={n_healthy})\")\nprint(f\"Method B coverage: {n_with_ve_peak}/{n_total} have ve_ratio_peak\")\nprint(f\"Trajectory coverage: {n_with_traj}/{n_total} have time series data\")\n\n# --- Method A: Step-matched NVE ---\nprint(\"\\n\" + \"=\" * 80)\nprint(\"METHOD A: Step-matched NVE (nve_peak)\")\nprint(\"=\" * 80)\n\nmethod_a_data = [(e[\"id\"], e[\"nve_peak\"], e[\"gt\"]) for e in experiments]\nthresholds = [1.3, 1.5, 1.7, 2.0]\n\nprint(\"\\n### Single Threshold\")\nresults_a = threshold_analysis(method_a_data, thresholds)\nfor t in thresholds:\n    r = results_a[t]\n    print(f\"\\nθ = {t:.1f}×:\")\n    print(f\"  Acc={r['acc']:.1%} Prec={r['prec']:.1%} Rec={r['rec']:.1%} F1={r['f1']:.3f}\")\n    print(f\"  TP={r['tp']} FP={r['fp']} TN={r['tn']} FN={r['fn']}\")\n    if r['fp_list']:\n        print(f\"  FP: {', '.join(f'{x[0]}({x[1]:.2f})' for x in r['fp_list'])}\")\n    if r['fn_list']:\n        print(f\"  FN: {', '.join(f'{x[0]}({x[1]:.2f})' for x in r['fn_list'])}\")\n\nscores_a = [e[\"nve_peak\"] for e in experiments]\nlabels = [e[\"gt\"] for e in experiments]\nauroc_a = compute_auroc(scores_a, labels)\nprint(f\"\\nAUROC (Method A): {auroc_a:.4f}\")\n\n# --- Method A combined diagnostic ---\nprint(\"\\n### Combined Diagnostic (A+B+C)\")\nfor t in thresholds:\n    tp = fp = tn = fn = 0\n    a_only_count = 0\n    fp_list = []\n    fn_list = []\n    for e in experiments:\n        positive, reasons = combined_diagnostic(e, t)\n        if \"A_only\" in reasons:\n            a_only_count += 1\n        if positive and e[\"gt\"] == 1:\n            tp += 1\n        elif positive and e[\"gt\"] == 0:\n            fp += 1\n            fp_list.append((e[\"id\"], e[\"nve_peak\"], reasons))\n        elif not positive and e[\"gt\"] == 0:\n            tn += 1\n        else:\n            fn += 1\n            fn_list.append((e[\"id\"], e[\"nve_peak\"], reasons))\n    total = tp + fp + tn + fn\n    acc = (tp + tn) / total if total > 0 else 0\n    prec = tp / (tp + fp) if (tp + fp) > 0 else 0\n    rec = tp / (tp + fn) if (tp + fn) > 0 else 0\n    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0\n    print(f\"\\nθ = {t:.1f}× (A_only fallback: {a_only_count}/{n_total}):\")\n    print(f\"  Acc={acc:.1%} Prec={prec:.1%} Rec={rec:.1%} F1={f1:.3f}\")\n    print(f\"  TP={tp} FP={fp} TN={tn} FN={fn}\")\n    if fp_list:\n        print(f\"  FP: {', '.join(f'{x[0]}({x[1]:.2f}, {x[2]})' for x in fp_list)}\")\n    if fn_list:\n        print(f\"  FN: {', '.join(f'{x[0]}({x[1]:.2f}, {x[2]})' for x in fn_list)}\")\n\n\n# --- Method B: Raw ve_ratio_peak ---\nprint(\"\\n\" + \"=\" * 80)\nprint(\"METHOD B: Raw ve_ratio_peak\")\nprint(\"=\" * 80)\n\nmethod_b_exps = [e for e in experiments if e[\"ve_ratio_peak\"] is not None]\nn_b = len(method_b_exps)\nn_b_civo = sum(1 for e in method_b_exps if e[\"gt\"] == 1)\nn_b_healthy = sum(1 for e in method_b_exps if e[\"gt\"] == 0)\nprint(f\"\\nSubset with ve_ratio_peak: N={n_b} (CIVO={n_b_civo}, Healthy={n_b_healthy})\")\n\nmethod_b_data = [(e[\"id\"], e[\"ve_ratio_peak\"], e[\"gt\"]) for e in method_b_exps]\nthresholds_b = [0.8, 1.0, 1.3, 1.5, 2.0]\n\nprint(\"\\n### Single Threshold\")\nresults_b = threshold_analysis(method_b_data, thresholds_b)\nfor t in thresholds_b:\n    r = results_b[t]\n    print(f\"\\nθ = {t:.1f}×:\")\n    print(f\"  Acc={r['acc']:.1%} Prec={r['prec']:.1%} Rec={r['rec']:.1%} F1={r['f1']:.3f}\")\n    print(f\"  TP={r['tp']} FP={r['fp']} TN={r['tn']} FN={r['fn']}\")\n    if r['fp_list']:\n        print(f\"  FP: {', '.join(f'{x[0]}({x[1]:.3f})' for x in r['fp_list'])}\")\n    if r['fn_list']:\n        print(f\"  FN: {', '.join(f'{x[0]}({x[1]:.3f})' for x in r['fn_list'])}\")\n\nscores_b = [e[\"ve_ratio_peak\"] for e in method_b_exps]\nlabels_b = [e[\"gt\"] for e in method_b_exps]\nauroc_b = compute_auroc(scores_b, labels_b)\nprint(f\"\\nAUROC (Method B): {auroc_b:.4f}\")\n\n# --- Method B combined diagnostic ---\nprint(\"\\n### Combined Diagnostic (A+B+C) — using ve_ratio_peak as threshold basis\")\nfor t in thresholds_b:\n    tp = fp = tn = fn = 0\n    for e in method_b_exps:\n        # For method B combined, we use ve_ratio_peak for condition A\n        # and ve_ratio trajectory for conditions B and C\n        ve_peak = e[\"ve_ratio_peak\"]\n        cond_a = ve_peak >= t\n\n        ve_traj = e.get(\"ve_traj\")\n        has_traj = ve_traj is not None and len(ve_traj) >= 3\n\n        if not has_traj:\n            positive = cond_a\n        else:\n            sorted_steps = sorted(ve_traj.keys())\n            vals = [ve_traj[s] for s in sorted_steps]\n            # Condition B: ve_ratio > threshold for >= 2 consecutive\n            consec = 0\n            cond_b = False\n            for v in vals:\n                if v >= t:\n                    consec += 1\n                    if consec >= 2:\n                        cond_b = True\n                        break\n                else:\n                    consec = 0\n            # Condition C: uptrend\n            cond_c = False\n            for i in range(len(vals) - 1):\n                if vals[i + 1] > vals[i] * 1.1:\n                    cond_c = True\n                    break\n            positive = cond_a and cond_b and cond_c\n\n        if positive and e[\"gt\"] == 1:\n            tp += 1\n        elif positive and e[\"gt\"] == 0:\n            fp += 1\n        elif not positive and e[\"gt\"] == 0:\n            tn += 1\n        else:\n            fn += 1\n    total = tp + fp + tn + fn\n    acc = (tp + tn) / total if total > 0 else 0\n    prec = tp / (tp + fp) if (tp + fp) > 0 else 0\n    rec = tp / (tp + fn) if (tp + fn) > 0 else 0\n    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0\n    print(f\"\\nθ = {t:.1f}×:\")\n    print(f\"  Acc={acc:.1%} Prec={prec:.1%} Rec={rec:.1%} F1={f1:.3f}\")\n    print(f\"  TP={tp} FP={fp} TN={tn} FN={fn}\")\n\n\n# --- NVE_median_last5 ---\nprint(\"\\n\" + \"=\" * 80)\nprint(\"NVE_median_last5 Auxiliary Metric\")\nprint(\"=\" * 80)\n\nmedian_results = []\nfor e in experiments:\n    nve_traj = e.get(\"nve_traj\")\n    ve_traj = e.get(\"ve_traj\")\n    if nve_traj is None and ve_traj is not None:\n        nve_traj = compute_nve_from_ve(ve_traj, e[\"env\"])\n    if nve_traj is not None and len(nve_traj) >= 3:\n        med = compute_median_last5(nve_traj)\n        label = \"CIVO\" if e[\"gt\"] == 1 else \"Healthy\"\n        correct = (med > 1.0 and e[\"gt\"] == 1) or (med <= 1.0 and e[\"gt\"] == 0)\n        median_results.append((e[\"id\"], label, med, correct))\n\nprint(f\"\\nExperiments with sufficient trajectory data: {len(median_results)}\")\nprint(f\"\\n{'exp_id':<45} {'type':<8} {'median_last5':>12} {'correct':>8}\")\nprint(\"-\" * 75)\nfor eid, label, med, correct in median_results:\n    print(f\"{eid:<45} {label:<8} {med:>12.3f} {'✓' if correct else '✗':>8}\")\n\n# Summary stats\ncivo_meds = [m for _, l, m, _ in median_results if l == \"CIVO\"]\nhealthy_meds = [m for _, l, m, _ in median_results if l == \"Healthy\"]\nif civo_meds:\n    print(f\"\\nCIVO median_last5: min={min(civo_meds):.3f}, median={sorted(civo_meds)[len(civo_meds)//2]:.3f}, max={max(civo_meds):.3f}\")\nif healthy_meds:\n    print(f\"Healthy median_last5: min={min(healthy_meds):.3f}, median={sorted(healthy_meds)[len(healthy_meds)//2]:.3f}, max={max(healthy_meds):.3f}\")\ncorrect_count = sum(1 for _, _, _, c in median_results if c)\nprint(f\"Accuracy: {correct_count}/{len(median_results)} = {correct_count/len(median_results):.1%}\")\n\n\n# --- Distribution analysis ---\nprint(\"\\n\" + \"=\" * 80)\nprint(\"Distribution Analysis\")\nprint(\"=\" * 80)\n\ncivo_nve = sorted([e[\"nve_peak\"] for e in experiments if e[\"gt\"] == 1])\nhealthy_nve = sorted([e[\"nve_peak\"] for e in experiments if e[\"gt\"] == 0])\n\nprint(f\"\\nMethod A NVE_peak distribution:\")\nprint(f\"  CIVO (N={len(civo_nve)}): min={min(civo_nve):.3f}, median={civo_nve[len(civo_nve)//2]:.3f}, max={max(civo_nve):.3f}, mean={sum(civo_nve)/len(civo_nve):.3f}\")\nprint(f\"  Healthy (N={len(healthy_nve)}): min={min(healthy_nve):.3f}, median={healthy_nve[len(healthy_nve)//2]:.3f}, max={max(healthy_nve):.3f}, mean={sum(healthy_nve)/len(healthy_nve):.3f}\")\n\ncivo_ve = sorted([e[\"ve_ratio_peak\"] for e in experiments if e[\"gt\"] == 1 and e[\"ve_ratio_peak\"] is not None])\nhealthy_ve = sorted([e[\"ve_ratio_peak\"] for e in experiments if e[\"gt\"] == 0 and e[\"ve_ratio_peak\"] is not None])\n\nif civo_ve and healthy_ve:\n    print(f\"\\nMethod B ve_ratio_peak distribution:\")\n    print(f\"  CIVO (N={len(civo_ve)}): min={min(civo_ve):.3f}, median={civo_ve[len(civo_ve)//2]:.3f}, max={max(civo_ve):.3f}, mean={sum(civo_ve)/len(civo_ve):.3f}\")\n    print(f\"  Healthy (N={len(healthy_ve)}): min={min(healthy_ve):.3f}, median={healthy_ve[len(healthy_ve)//2]:.3f}, max={max(healthy_ve):.3f}, mean={sum(healthy_ve)/len(healthy_ve):.3f}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_018NtfMcuCwVuJviH4WRG18j`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold && python3 analysis_v2.py 2>&1",
  "description": "Run NVE threshold analysis V2",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "bd133a80-92ee-4a14-adba-0bceba00d80d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XB3qYZ5TmHxvJnYhFFE1wm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15782,
      "cache_read_input_tokens": 58757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15782
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

_source line 47 · 2026-05-25T20:25:33.030Z_

<details><summary>↩ Tool result · `toolu_018NtfMcuCwVuJviH4WRG18j`</summary>

```text
================================================================================
NVE Threshold Sensitivity Analysis V2
================================================================================

Dataset: N=61 (CIVO=25, Healthy=36)
Method B coverage: 35/61 have ve_ratio_peak
Trajectory coverage: 17/61 have time series data

================================================================================
METHOD A: Step-matched NVE (nve_peak)
================================================================================

### Single Threshold

θ = 1.3×:
  Acc=86.9% Prec=75.8% Rec=100.0% F1=0.862
  TP=25 FP=8 TN=28 FN=0
  FP: exp_008e_v3_subsample_on_dt1_h15(1.93), exp_008f_s3_no_dt_embed_walker(1.49), exp_008f_s4(1.41), exp_032b_dual_critic_walker_s1(1.40), exp_046_frozen_dt_emb_cheetah(1.35), exp_047_frozen_dt_emb_walker_s1(1.71), exp_057_frozen_dt_emb_walker_s2(1.88), exp_082_cheetah_no_dt_emb_s0(1.58)

θ = 1.5×:
  Acc=93.4% Prec=86.2% Rec=100.0% F1=0.926
  TP=25 FP=4 TN=32 FN=0
  FP: exp_008e_v3_subsample_on_dt1_h15(1.93), exp_047_frozen_dt_emb_walker_s1(1.71), exp_057_frozen_dt_emb_walker_s2(1.88), exp_082_cheetah_no_dt_emb_s0(1.58)

θ = 1.7×:
  Acc=90.2% Prec=88.0% Rec=88.0% F1=0.880
  TP=22 FP=3 TN=33 FN=3
  FP: exp_008e_v3_subsample_on_dt1_h15(1.93), exp_047_frozen_dt_emb_walker_s1(1.71), exp_057_frozen_dt_emb_walker_s2(1.88)
  FN: exp_008d_civo_trigger_s3(1.53), exp_009b_008d_walker_s2(1.62), exp_027_tcn_walker_s1(1.64)

θ = 2.0×:
  Acc=95.1% Prec=100.0% Rec=88.0% F1=0.936
  TP=22 FP=0 TN=36 FN=3
  FN: exp_008d_civo_trigger_s3(1.53), exp_009b_008d_walker_s2(1.62), exp_027_tcn_walker_s1(1.64)

AUROC (Method A): 0.9889

### Combined Diagnostic (A+B+C)

θ = 1.3× (A_only fallback: 45/61):
  Acc=90.2% Prec=80.6% Rec=100.0% F1=0.893
  TP=25 FP=6 TN=30 FN=0
  FP: exp_008e_v3_subsample_on_dt1_h15(1.93, A_only (no trajectory data)), exp_008f_s3_no_dt_embed_walker(1.49, A_only (no trajectory data)), exp_008f_s4(1.41, A_only (no trajectory data)), exp_046_frozen_dt_emb_cheetah(1.35, A_only (no trajectory data)), exp_047_frozen_dt_emb_walker_s1(1.71, A_only (no trajectory data)), exp_057_frozen_dt_emb_walker_s2(1.88, A_only (no trajectory data))

θ = 1.5× (A_only fallback: 45/61):
  Acc=91.8% Prec=88.5% Rec=92.0% F1=0.902
  TP=23 FP=3 TN=33 FN=2
  FP: exp_008e_v3_subsample_on_dt1_h15(1.93, A_only (no trajectory data)), exp_047_frozen_dt_emb_walker_s1(1.71, A_only (no trajectory data)), exp_057_frozen_dt_emb_walker_s2(1.88, A_only (no trajectory data))
  FN: exp_008e_v3_walker_s2(3.78, A=Y B=N C=Y), exp_029d_tcn_walker_s3_sigma02(3.00, A=Y B=N C=Y)

θ = 1.7× (A_only fallback: 45/61):
  Acc=86.9% Prec=87.0% Rec=80.0% F1=0.833
  TP=20 FP=3 TN=33 FN=5
  FP: exp_008e_v3_subsample_on_dt1_h15(1.93, A_only (no trajectory data)), exp_047_frozen_dt_emb_walker_s1(1.71, A_only (no trajectory data)), exp_057_frozen_dt_emb_walker_s2(1.88, A_only (no trajectory data))
  FN: exp_008d_civo_trigger_s3(1.53, A_only (no trajectory data)), exp_008e_v3_walker_s2(3.78, A=Y B=N C=Y), exp_009b_008d_walker_s2(1.62, A_only (no trajectory data)), exp_027_tcn_walker_s1(1.64, A=N B=Y C=Y), exp_029d_tcn_walker_s3_sigma02(3.00, A=Y B=N C=Y)

θ = 2.0× (A_only fallback: 45/61):
  Acc=91.8% Prec=100.0% Rec=80.0% F1=0.889
  TP=20 FP=0 TN=36 FN=5
  FN: exp_008d_civo_trigger_s3(1.53, A_only (no trajectory data)), exp_008e_v3_walker_s2(3.78, A=Y B=N C=Y), exp_009b_008d_walker_s2(1.62, A_only (no trajectory data)), exp_027_tcn_walker_s1(1.64, A=N B=Y C=Y), exp_029d_tcn_walker_s3_sigma02(3.00, A=Y B=N C=Y)

================================================================================
METHOD B: Raw ve_ratio_peak
================================================================================

Subset with ve_ratio_peak: N=35 (CIVO=15, Healthy=20)

### Single Threshold

θ = 0.8×:
  Acc=80.0% Prec=70.0% Rec=93.3% F1=0.800
  TP=14 FP=6 TN=14 FN=1
  FP: exp_008a_no_subsample_dt2(0.930), exp_027_tcn_walker_s0_sigma02(0.908), exp_047_frozen_dt_emb_walker_s1(1.099), exp_057_frozen_dt_emb_walker_s2(1.283), exp_070_008e_v3_walker_s0(0.800), exp_082_cheetah_no_dt_emb_s0(0.955)
  FN: exp_009b_008d_walker_s2(0.570)

θ = 1.0×:
  Acc=91.4% Prec=87.5% Rec=93.3% F1=0.903
  TP=14 FP=2 TN=18 FN=1
  FP: exp_047_frozen_dt_emb_walker_s1(1.099), exp_057_frozen_dt_emb_walker_s2(1.283)
  FN: exp_009b_008d_walker_s2(0.570)

θ = 1.3×:
  Acc=97.1% Prec=100.0% Rec=93.3% F1=0.966
  TP=14 FP=0 TN=20 FN=1
  FN: exp_009b_008d_walker_s2(0.570)

θ = 1.5×:
  Acc=97.1% Prec=100.0% Rec=93.3% F1=0.966
  TP=14 FP=0 TN=20 FN=1
  FN: exp_009b_008d_walker_s2(0.570)

θ = 2.0×:
  Acc=88.6% Prec=100.0% Rec=73.3% F1=0.846
  TP=11 FP=0 TN=20 FN=4
  FN: exp_009b_008d_walker_s2(0.570), exp_009e_008d_walker_s1(1.666), exp_027_tcn_walker_s1(1.637), exp_034_dual_critic_cheetah(1.800)

AUROC (Method B): 0.9700

### Combined Diagnostic (A+B+C) — using ve_ratio_peak as threshold basis

θ = 0.8×:
  Acc=85.7% Prec=81.2% Rec=86.7% F1=0.839
  TP=13 FP=3 TN=17 FN=2

θ = 1.0×:
  Acc=85.7% Prec=85.7% Rec=80.0% F1=0.828
  TP=12 FP=2 TN=18 FN=3

θ = 1.3×:
  Acc=91.4% Prec=100.0% Rec=80.0% F1=0.889
  TP=12 FP=0 TN=20 FN=3

θ = 1.5×:
  Acc=88.6% Prec=100.0% Rec=73.3% F1=0.846
  TP=11 FP=0 TN=20 FN=4

θ = 2.0×:
  Acc=77.1% Prec=100.0% Rec=46.7% F1=0.636
  TP=7 FP=0 TN=20 FN=8

================================================================================
NVE_median_last5 Auxiliary Metric
================================================================================

Experiments with sufficient trajectory data: 16

exp_id                                        type     median_last5  correct
---------------------------------------------------------------------------
exp_008e_v3_walker_s2                         CIVO            0.900        ✗
exp_027_tcn_walker_s0                         CIVO            1.396        ✓
exp_027_tcn_walker_s1                         CIVO            0.982        ✗
exp_029b_tcn_walker_s2_sigma02                CIVO            2.315        ✓
exp_029d_tcn_walker_s3_sigma02                CIVO            1.284        ✓
exp_030b_tcn_cheetah_s0_sigma05               CIVO            1.674        ✓
exp_068_008d_walker_repro_s1                  CIVO            4.116        ✓
exp_078_cheetah_008d_s0                       CIVO            2.740        ✓
exp_008a_no_subsample_dt2                     Healthy         1.043        ✗
exp_015b_frozen_dt_emb                        Healthy         0.420        ✓
exp_027_tcn_walker_s0_sigma02                 Healthy         0.857        ✓
exp_029a_tcn_walker_s1_sigma02                Healthy         0.554        ✓
exp_032b_dual_critic_walker_s1                Healthy         0.700        ✓
exp_069_008f_walker_repro_s1                  Healthy         0.533        ✓
exp_070_008e_v3_walker_s0                     Healthy         0.888        ✓
exp_082_cheetah_no_dt_emb_s0                  Healthy         0.980        ✓

CIVO median_last5: min=0.900, median=1.674, max=4.116
Healthy median_last5: min=0.420, median=0.857, max=1.043
Accuracy: 13/16 = 81.2%

================================================================================
Distribution Analysis
================================================================================

Method A NVE_peak distribution:
  CIVO (N=25): min=1.530, median=4.100, max=70.640, mean=6.954
  Healthy (N=36): min=0.100, median=0.800, max=1.930, mean=0.845

Method B ve_ratio_peak distribution:
  CIVO (N=15): min=0.570, median=3.000, max=24.112, mean=4.722
  Healthy (N=20): min=0.200, median=0.527, max=1.283, mean=0.600
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "6b6231be-cd5e-448f-9bab-c4141a8b2e37",
  "tool_use_result": {
    "stdout": "================================================================================\nNVE Threshold Sensitivity Analysis V2\n================================================================================\n\nDataset: N=61 (CIVO=25, Healthy=36)\nMethod B coverage: 35/61 have ve_ratio_peak\nTrajectory coverage: 17/61 have time series data\n\n================================================================================\nMETHOD A: Step-matched NVE (nve_peak)\n================================================================================\n\n### Single Threshold\n\nθ = 1.3×:\n  Acc=86.9% Prec=75.8% Rec=100.0% F1=0.862\n  TP=25 FP=8 TN=28 FN=0\n  FP: exp_008e_v3_subsample_on_dt1_h15(1.93), exp_008f_s3_no_dt_embed_walker(1.49), exp_008f_s4(1.41), exp_032b_dual_critic_walker_s1(1.40), exp_046_frozen_dt_emb_cheetah(1.35), exp_047_frozen_dt_emb_walker_s1(1.71), exp_057_frozen_dt_emb_walker_s2(1.88), exp_082_cheetah_no_dt_emb_s0(1.58)\n\nθ = 1.5×:\n  Acc=93.4% Prec=86.2% Rec=100.0% F1=0.926\n  TP=25 FP=4 TN=32 FN=0\n  FP: exp_008e_v3_subsample_on_dt1_h15(1.93), exp_047_frozen_dt_emb_walker_s1(1.71), exp_057_frozen_dt_emb_walker_s2(1.88), exp_082_cheetah_no_dt_emb_s0(1.58)\n\nθ = 1.7×:\n  Acc=90.2% Prec=88.0% Rec=88.0% F1=0.880\n  TP=22 FP=3 TN=33 FN=3\n  FP: exp_008e_v3_subsample_on_dt1_h15(1.93), exp_047_frozen_dt_emb_walker_s1(1.71), exp_057_frozen_dt_emb_walker_s2(1.88)\n  FN: exp_008d_civo_trigger_s3(1.53), exp_009b_008d_walker_s2(1.62), exp_027_tcn_walker_s1(1.64)\n\nθ = 2.0×:\n  Acc=95.1% Prec=100.0% Rec=88.0% F1=0.936\n  TP=22 FP=0 TN=36 FN=3\n  FN: exp_008d_civo_trigger_s3(1.53), exp_009b_008d_walker_s2(1.62), exp_027_tcn_walker_s1(1.64)\n\nAUROC (Method A): 0.9889\n\n### Combined Diagnostic (A+B+C)\n\nθ = 1.3× (A_only fallback: 45/61):\n  Acc=90.2% Prec=80.6% Rec=100.0% F1=0.893\n  TP=25 FP=6 TN=30 FN=0\n  FP: exp_008e_v3_subsample_on_dt1_h15(1.93, A_only (no trajectory data)), exp_008f_s3_no_dt_embed_walker(1.49, A_only (no trajectory data)), exp_008f_s4(1.41, A_only (no trajectory data)), exp_046_frozen_dt_emb_cheetah(1.35, A_only (no trajectory data)), exp_047_frozen_dt_emb_walker_s1(1.71, A_only (no trajectory data)), exp_057_frozen_dt_emb_walker_s2(1.88, A_only (no trajectory data))\n\nθ = 1.5× (A_only fallback: 45/61):\n  Acc=91.8% Prec=88.5% Rec=92.0% F1=0.902\n  TP=23 FP=3 TN=33 FN=2\n  FP: exp_008e_v3_subsample_on_dt1_h15(1.93, A_only (no trajectory data)), exp_047_frozen_dt_emb_walker_s1(1.71, A_only (no trajectory data)), exp_057_frozen_dt_emb_walker_s2(1.88, A_only (no trajectory data))\n  FN: exp_008e_v3_walker_s2(3.78, A=Y B=N C=Y), exp_029d_tcn_walker_s3_sigma02(3.00, A=Y B=N C=Y)\n\nθ = 1.7× (A_only fallback: 45/61):\n  Acc=86.9% Prec=87.0% Rec=80.0% F1=0.833\n  TP=20 FP=3 TN=33 FN=5\n  FP: exp_008e_v3_subsample_on_dt1_h15(1.93, A_only (no trajectory data)), exp_047_frozen_dt_emb_walker_s1(1.71, A_only (no trajectory data)), exp_057_frozen_dt_emb_walker_s2(1.88, A_only (no trajectory data))\n  FN: exp_008d_civo_trigger_s3(1.53, A_only (no trajectory data)), exp_008e_v3_walker_s2(3.78, A=Y B=N C=Y), exp_009b_008d_walker_s2(1.62, A_only (no trajectory data)), exp_027_tcn_walker_s1(1.64, A=N B=Y C=Y), exp_029d_tcn_walker_s3_sigma02(3.00, A=Y B=N C=Y)\n\nθ = 2.0× (A_only fallback: 45/61):\n  Acc=91.8% Prec=100.0% Rec=80.0% F1=0.889\n  TP=20 FP=0 TN=36 FN=5\n  FN: exp_008d_civo_trigger_s3(1.53, A_only (no trajectory data)), exp_008e_v3_walker_s2(3.78, A=Y B=N C=Y), exp_009b_008d_walker_s2(1.62, A_only (no trajectory data)), exp_027_tcn_walker_s1(1.64, A=N B=Y C=Y), exp_029d_tcn_walker_s3_sigma02(3.00, A=Y B=N C=Y)\n\n================================================================================\nMETHOD B: Raw ve_ratio_peak\n================================================================================\n\nSubset with ve_ratio_peak: N=35 (CIVO=15, Healthy=20)\n\n### Single Threshold\n\nθ = 0.8×:\n  Acc=80.0% Prec=70.0% Rec=93.3% F1=0.800\n  TP=14 FP=6 TN=14 FN=1\n  FP: exp_008a_no_subsample_dt2(0.930), exp_027_tcn_walker_s0_sigma02(0.908), exp_047_frozen_dt_emb_walker_s1(1.099), exp_057_frozen_dt_emb_walker_s2(1.283), exp_070_008e_v3_walker_s0(0.800), exp_082_cheetah_no_dt_emb_s0(0.955)\n  FN: exp_009b_008d_walker_s2(0.570)\n\nθ = 1.0×:\n  Acc=91.4% Prec=87.5% Rec=93.3% F1=0.903\n  TP=14 FP=2 TN=18 FN=1\n  FP: exp_047_frozen_dt_emb_walker_s1(1.099), exp_057_frozen_dt_emb_walker_s2(1.283)\n  FN: exp_009b_008d_walker_s2(0.570)\n\nθ = 1.3×:\n  Acc=97.1% Prec=100.0% Rec=93.3% F1=0.966\n  TP=14 FP=0 TN=20 FN=1\n  FN: exp_009b_008d_walker_s2(0.570)\n\nθ = 1.5×:\n  Acc=97.1% Prec=100.0% Rec=93.3% F1=0.966\n  TP=14 FP=0 TN=20 FN=1\n  FN: exp_009b_008d_walker_s2(0.570)\n\nθ = 2.0×:\n  Acc=88.6% Prec=100.0% Rec=73.3% F1=0.846\n  TP=11 FP=0 TN=20 FN=4\n  FN: exp_009b_008d_walker_s2(0.570), exp_009e_008d_walker_s1(1.666), exp_027_tcn_walker_s1(1.637), exp_034_dual_critic_cheetah(1.800)\n\nAUROC (Method B): 0.9700\n\n### Combined Diagnostic (A+B+C) — using ve_ratio_peak as threshold basis\n\nθ = 0.8×:\n  Acc=85.7% Prec=81.2% Rec=86.7% F1=0.839\n  TP=13 FP=3 TN=17 FN=2\n\nθ = 1.0×:\n  Acc=85.7% Prec=85.7% Rec=80.0% F1=0.828\n  TP=12 FP=2 TN=18 FN=3\n\nθ = 1.3×:\n  Acc=91.4% Prec=100.0% Rec=80.0% F1=0.889\n  TP=12 FP=0 TN=20 FN=3\n\nθ = 1.5×:\n  Acc=88.6% Prec=100.0% Rec=73.3% F1=0.846\n  TP=11 FP=0 TN=20 FN=4\n\nθ = 2.0×:\n  Acc=77.1% Prec=100.0% Rec=46.7% F1=0.636\n  TP=7 FP=0 TN=20 FN=8\n\n================================================================================\nNVE_median_last5 Auxiliary Metric\n================================================================================\n\nExperiments with sufficient trajectory data: 16\n\nexp_id                                        type     median_last5  correct\n---------------------------------------------------------------------------\nexp_008e_v3_walker_s2                         CIVO            0.900        ✗\nexp_027_tcn_walker_s0                         CIVO            1.396        ✓\nexp_027_tcn_walker_s1                         CIVO            0.982        ✗\nexp_029b_tcn_walker_s2_sigma02                CIVO            2.315        ✓\nexp_029d_tcn_walker_s3_sigma02                CIVO            1.284        ✓\nexp_030b_tcn_cheetah_s0_sigma05               CIVO            1.674        ✓\nexp_068_008d_walker_repro_s1                  CIVO            4.116        ✓\nexp_078_cheetah_008d_s0                       CIVO            2.740        ✓\nexp_008a_no_subsample_dt2                     Healthy         1.043        ✗\nexp_015b_frozen_dt_emb                        Healthy         0.420        ✓\nexp_027_tcn_walker_s0_sigma02                 Healthy         0.857        ✓\nexp_029a_tcn_walker_s1_sigma02                Healthy         0.554        ✓\nexp_032b_dual_critic_walker_s1                Healthy         0.700        ✓\nexp_069_008f_walker_repro_s1                  Healthy         0.533        ✓\nexp_070_008e_v3_walker_s0                     Healthy         0.888        ✓\nexp_082_cheetah_no_dt_emb_s0                  Healthy         0.980        ✓\n\nCIVO median_last5: min=0.900, median=1.674, max=4.116\nHealthy median_last5: min=0.420, median=0.857, max=1.043\nAccuracy: 13/16 = 81.2%\n\n================================================================================\nDistribution Analysis\n================================================================================\n\nMethod A NVE_peak distribution:\n  CIVO (N=25): min=1.530, median=4.100, max=70.640, mean=6.954\n  Healthy (N=36): min=0.100, median=0.800, max=1.930, mean=0.845\n\nMethod B ve_ratio_peak distribution:\n  CIVO (N=15): min=0.570, median=3.000, max=24.112, mean=4.722\n  Healthy (N=20): min=0.200, median=0.527, max=1.283, mean=0.600",
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

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the analysis results. Let me write the V2 analysis report. I also need to check what's interesting:

1. Method A single threshold results match V1 perfectly
2. Method A combined diagnostic has more FN due to requiring B+C (but most experiments fall back to A-only because they lack trajectory data)
3. Method B: AUROC=0.97 (slightly lower than A's 0.989), best at θ=1.3× with F1=0.966
4. NVE_median_last5: 81.2% accuracy, separates well


5. Method A clearly outperforms for CIVO detection with its superior AUROC, though the combined diagnostic would theoretically be stronger if trajectory data were available across more experiments—right now it's limited to just 16 cases where it can eliminate false positives from frozen experiments, while the NVE median metric effectively validates that frozen cases are correctly identified as negative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "a2269bd1-5796-4c8a-9099-982772fb60b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFRrNybeRU2YiJbitL8Nd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3647,
      "cache_read_input_tokens": 74539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3647
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

_source line 49_

All analysis results collected. Now writing the V2 report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "c66c327e-63f1-4106-96f7-55500e6851db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFRrNybeRU2YiJbitL8Nd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3647,
      "cache_read_input_tokens": 74539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3647
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

_source line 50_

<details open><summary>🔧 Tool call — Write · `toolu_01EsBNoydbcHZYrYin8u4Gpw`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis_v2.md",
  "content": "# NVE Threshold Sensitivity Analysis V2\n\n**Updated: 2026-05-25** — 组合诊断标准 + 双方法对比\n\n## 数据集更新\n\n- V1 数据点数: 61\n- V2 数据点数: 61 (Collapsed: 25, Healthy: 36)\n- 新增实验: 无额外新增 (V1 已包含 exp_084/085/087; exp_086 status=ANALYZING, 无 metrics, 排除)\n- Method B 覆盖: 35/61 有 ve_ratio_peak\n- 时间序列覆盖: 17/61 有逐 checkpoint NVE 轨迹数据\n\n### Reviewer 指出的 NVE 数值差异\n\n| exp_id | Reviewer 声称 NVE_peak | Registry NVE_peak (Method A) | Registry ve_ratio_peak (Method B) |\n|--------|----------------------|------------------------------|-----------------------------------|\n| exp_084_frozen_dt_emb_walker_s0 | 2.25 | 0.37 | N/A |\n| exp_085_frozen_dt_emb_walker_s1 | 3.0 | 0.31 | N/A |\n\n**分析**: Reviewer 的值与 registry 不匹配。Registry 使用 step-matched NVE (ve_ratio / baseline_ve_ratio_at_same_step)，Reviewer 可能使用了 raw V(s)/E_return 或不同的 baseline 归一化。两实验的 step-matched NVE 远低于 1.0，明确归类为 Healthy (无 CIVO)。两种方法下这些 frozen 实验都是 true negative。\n\n---\n\n## Method A: Step-matched NVE\n\nNVE = experiment_ve_ratio / baseline_ve_ratio_at_same_step\n\n### 单一阈值\n\n| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |\n|-----------|----------|-----------|--------|------|-----|-----|\n| 1.3× | 86.9% | 75.8% | 100% | 0.862 | 8 | 0 |\n| **1.5×** | **93.4%** | **86.2%** | **100%** | **0.926** | 4 | 0 |\n| 1.7× | 90.2% | 88.0% | 88.0% | 0.880 | 3 | 3 |\n| 2.0× | 95.1% | 100% | 88.0% | 0.936 | 0 | 3 |\n\n**AUROC = 0.9889**\n\nθ=1.5× FP (4): exp_082_cheetah_no_dt_emb_s0 (1.58, eval-variance-driven), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88, transient), exp_047_frozen_dt_emb_walker_s1 (1.71, transient)\n\nθ=2.0× FN (3): exp_008d_civo_trigger_s3 (1.53), exp_009b_008d_walker_s2 (1.62), exp_027_tcn_walker_s1 (1.64)\n\nNVE_peak 分布:\n- CIVO (25): min=1.530, median=4.100, max=70.640, mean=6.954\n- Healthy (36): min=0.100, median=0.800, max=1.930, mean=0.845\n- Overlap zone: NVE ∈ [1.530, 1.930], 含 3 CIVO + 4 Healthy\n\n### 组合诊断标准\n\n条件 A: NVE_peak ≥ τ\n条件 B: NVE > τ 持续 ≥2 个连续 eval 点 (排除瞬态 spike)\n条件 C: NVE 上升趋势 (≥10% 增幅)\n判定 CIVO positive 需 A ∧ B ∧ C 同时满足。无轨迹数据时回退到条件 A only。\n\n| Threshold | Accuracy | Precision | Recall | F1 | FP | FN | A_only fallback |\n|-----------|----------|-----------|--------|------|-----|-----|----------------|\n| 1.3× | 90.2% | 80.6% | 100% | 0.893 | 6 | 0 | 45/61 |\n| 1.5× | 91.8% | 88.5% | 92.0% | 0.902 | 3 | 2 | 45/61 |\n| 1.7× | 86.9% | 87.0% | 80.0% | 0.833 | 3 | 5 | 45/61 |\n| 2.0× | 91.8% | 100% | 80.0% | 0.889 | 0 | 5 | 45/61 |\n\n**关键发现**: 组合标准在 θ=1.3× 消除了 2 个 FP (exp_032b_dual_critic_walker_s1 和 exp_082_cheetah_no_dt_emb_s0 — 因 B 条件未满足而正确排除)。但引入新 FN (exp_008e_v3_walker_s2: B=N, 因 NVE 仅在末段突增而非持续; exp_029d_tcn_walker_s3_sigma02: B=N)。\n\n当 74% 实验缺少轨迹数据时，组合诊断相比单一阈值优势有限。\n\n---\n\n## Method B: Raw ve_ratio peak\n\n直接用 ve_ratio_peak (未除以 baseline) 作为分类分数。\n\n可用子集: N=35 (CIVO=15, Healthy=20)\n\n### 单一阈值\n\n| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |\n|-----------|----------|-----------|--------|------|-----|-----|\n| 0.8× | 80.0% | 70.0% | 93.3% | 0.800 | 6 | 1 |\n| 1.0× | 91.4% | 87.5% | 93.3% | 0.903 | 2 | 1 |\n| **1.3×** | **97.1%** | **100%** | **93.3%** | **0.966** | 0 | 1 |\n| 1.5× | 97.1% | 100% | 93.3% | 0.966 | 0 | 1 |\n| 2.0× | 88.6% | 100% | 73.3% | 0.846 | 0 | 4 |\n\n**AUROC = 0.9700**\n\nθ=1.3× FN (1): exp_009b_008d_walker_s2 (ve_ratio_peak=0.570, 但 step-matched NVE=1.62)\n\nve_ratio_peak 分布:\n- CIVO (15): min=0.570, median=3.000, max=24.112, mean=4.722\n- Healthy (20): min=0.200, median=0.527, max=1.283, mean=0.600\n\n### 组合诊断标准\n\n| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |\n|-----------|----------|-----------|--------|------|-----|-----|\n| 0.8× | 85.7% | 81.2% | 86.7% | 0.839 | 3 | 2 |\n| 1.0× | 85.7% | 85.7% | 80.0% | 0.828 | 2 | 3 |\n| 1.3× | 91.4% | 100% | 80.0% | 0.889 | 0 | 3 |\n| 1.5× | 88.6% | 100% | 73.3% | 0.846 | 0 | 4 |\n| 2.0× | 77.1% | 100% | 46.7% | 0.636 | 0 | 8 |\n\n---\n\n## NVE_median_last5 辅助指标\n\n对有轨迹数据的 16 个实验，取最后 5 个 checkpoint 的 NVE 中位数。\n\n| exp_id | type | NVE_median_last5 | label | correct? |\n|--------|------|-----------------|-------|----------|\n| exp_008e_v3_walker_s2 | CIVO | 0.900 | CIVO | ✗ |\n| exp_027_tcn_walker_s0 | CIVO | 1.396 | CIVO | ✓ |\n| exp_027_tcn_walker_s1 | CIVO | 0.982 | CIVO | ✗ |\n| exp_029b_tcn_walker_s2_sigma02 | CIVO | 2.315 | CIVO | ✓ |\n| exp_029d_tcn_walker_s3_sigma02 | CIVO | 1.284 | CIVO | ✓ |\n| exp_030b_tcn_cheetah_s0_sigma05 | CIVO | 1.674 | CIVO | ✓ |\n| exp_068_008d_walker_repro_s1 | CIVO | 4.116 | CIVO | ✓ |\n| exp_078_cheetah_008d_s0 | CIVO | 2.740 | CIVO | ✓ |\n| exp_008a_no_subsample_dt2 | Healthy | 1.043 | Healthy | ✗ |\n| exp_015b_frozen_dt_emb | Healthy | 0.420 | Healthy | ✓ |\n| exp_027_tcn_walker_s0_sigma02 | Healthy | 0.857 | Healthy | ✓ |\n| exp_029a_tcn_walker_s1_sigma02 | Healthy | 0.554 | Healthy | ✓ |\n| exp_032b_dual_critic_walker_s1 | Healthy | 0.700 | Healthy | ✓ |\n| exp_069_008f_walker_repro_s1 | Healthy | 0.533 | Healthy | ✓ |\n| exp_070_008e_v3_walker_s0 | Healthy | 0.888 | Healthy | ✓ |\n| exp_082_cheetah_no_dt_emb_s0 | Healthy | 0.980 | Healthy | ✓ |\n\n**分布统计**:\n- CIVO (8): min=0.900, median=1.674, max=4.116\n- Healthy (8): min=0.420, median=0.857, max=1.043\n- Accuracy: 13/16 = 81.2% (阈值=1.0)\n\n**误判分析**:\n- exp_008e_v3_walker_s2: median_last5=0.900 (CIVO, 误判为 Healthy) — NVE 末段才突增 (105K=3.78)，最后 5 点中前 4 个 < 1.0\n- exp_027_tcn_walker_s1: median_last5=0.982 (CIVO, 边界误判) — 自我修正型 CIVO\n- exp_008a_no_subsample_dt2: median_last5=1.043 (Healthy, 轻微超 1.0) — eval-variance-driven，非 CIVO\n\n**结论**: NVE_median_last5 有判别力但弱于 NVE_peak。预期 \"frozen 实验 median ≈ 0.5\" 在 exp_015b (0.420) 上验证成功。Healthy 组 median 整体 < 1.0，CIVO 组 median > 1.0 (6/8)。\n\n---\n\n## 单一阈值 vs 组合标准对比\n\n### Method A 对比\n\n| 指标 | 单一阈值 θ=1.5× | 组合标准 θ=1.5× | 单一阈值 θ=2.0× | 组合标准 θ=2.0× |\n|------|----------------|----------------|----------------|----------------|\n| Accuracy | **93.4%** | 91.8% | **95.1%** | 91.8% |\n| Precision | 86.2% | **88.5%** | **100%** | **100%** |\n| Recall | **100%** | 92.0% | **88.0%** | 80.0% |\n| F1 | **0.926** | 0.902 | **0.936** | 0.889 |\n| FP | 4 | **3** | **0** | **0** |\n| FN | **0** | 2 | **3** | 5 |\n\n### Method A vs Method B (最佳阈值)\n\n| 指标 | Method A θ=1.5× (N=61) | Method B θ=1.3× (N=35) |\n|------|------------------------|------------------------|\n| AUROC | **0.989** | 0.970 |\n| F1 | 0.926 | **0.966** |\n| Precision | 86.2% | **100%** |\n| Recall | **100%** | 93.3% |\n| FP | 4 | **0** |\n| FN | **0** | 1 |\n\n---\n\n## 推荐\n\n### 1. 主推 Method A (step-matched NVE), θ=1.5×\n\n- AUROC=0.989, 最高判别力\n- 100% recall — 不漏检任何 CIVO\n- 4 个 FP 全部可解释 (frozen transient spike + eval-variance-driven)\n- 与原论文 NVE 定义一致\n\n### 2. 组合诊断标准当前不推荐作为主分类器\n\n- 74% 实验缺少轨迹数据，导致大量 A_only 回退\n- 有轨迹数据时确实能消除 FP (exp_082 被正确排除)，但同时引入新 FN\n- **建议**: 作为 θ=1.5× 筛查后的二次确认，而非独立分类器\n\n### 3. Method B 作为补充验证\n\n- ve_ratio_peak 不受 baseline 选择偏差影响\n- 在 θ=1.3× 达到 100% precision + 96.6% F1 (N=35 子集)\n- exp_009b 是唯一 FN (ve_ratio_peak=0.570, 但 step-matched NVE=1.62)，说明 baseline normalization 对低幅 CIVO 更敏感\n\n### 4. Decision rule (更新)\n\n```\nif NVE_peak >= 1.5×:\n    → FLAG as potential CIVO\n    if trajectory_data_available:\n        if NVE > 1.5× for >= 2 consecutive checkpoints AND uptrend present:\n            → CONFIRM as CIVO\n        else:\n            → LIKELY transient spike, monitor but do not kill\n    else:\n        → TREAT as CIVO (conservative)\n        \nif NVE_peak >= 2.0×:\n    → DEFINITE CIVO (zero FP at this threshold)\n```\n\n### 5. Reviewer 关注点回应\n\n- **exp_084 (NVE=0.37) 和 exp_085 (NVE=0.31)**: 两种方法下均为 true negative。Reviewer 声称的 2.25/3.0 值与 registry 不符，可能使用了未经 baseline 归一化的 raw V/E 比值。frozen dt_emb 实验的 NVE 远低于任何阈值，不会产生假阳性。\n- **θ=2.0× 的 precision**: 在 Method A 单一阈值下仍为 100% (FP=0)，Reviewer 的 false positive 担忧未被数据支持。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "9fc04777-2dad-4d4f-b911-647640b98a48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFRrNybeRU2YiJbitL8Nd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3647,
      "cache_read_input_tokens": 74539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3647
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

_source line 51 · 2026-05-25T20:26:58.641Z_

<details><summary>↩ Tool result · `toolu_01EsBNoydbcHZYrYin8u4Gpw`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis_v2.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "84f62480-772a-437c-879b-e01f71c01711",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis_v2.md",
    "content": "# NVE Threshold Sensitivity Analysis V2\n\n**Updated: 2026-05-25** — 组合诊断标准 + 双方法对比\n\n## 数据集更新\n\n- V1 数据点数: 61\n- V2 数据点数: 61 (Collapsed: 25, Healthy: 36)\n- 新增实验: 无额外新增 (V1 已包含 exp_084/085/087; exp_086 status=ANALYZING, 无 metrics, 排除)\n- Method B 覆盖: 35/61 有 ve_ratio_peak\n- 时间序列覆盖: 17/61 有逐 checkpoint NVE 轨迹数据\n\n### Reviewer 指出的 NVE 数值差异\n\n| exp_id | Reviewer 声称 NVE_peak | Registry NVE_peak (Method A) | Registry ve_ratio_peak (Method B) |\n|--------|----------------------|------------------------------|-----------------------------------|\n| exp_084_frozen_dt_emb_walker_s0 | 2.25 | 0.37 | N/A |\n| exp_085_frozen_dt_emb_walker_s1 | 3.0 | 0.31 | N/A |\n\n**分析**: Reviewer 的值与 registry 不匹配。Registry 使用 step-matched NVE (ve_ratio / baseline_ve_ratio_at_same_step)，Reviewer 可能使用了 raw V(s)/E_return 或不同的 baseline 归一化。两实验的 step-matched NVE 远低于 1.0，明确归类为 Healthy (无 CIVO)。两种方法下这些 frozen 实验都是 true negative。\n\n---\n\n## Method A: Step-matched NVE\n\nNVE = experiment_ve_ratio / baseline_ve_ratio_at_same_step\n\n### 单一阈值\n\n| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |\n|-----------|----------|-----------|--------|------|-----|-----|\n| 1.3× | 86.9% | 75.8% | 100% | 0.862 | 8 | 0 |\n| **1.5×** | **93.4%** | **86.2%** | **100%** | **0.926** | 4 | 0 |\n| 1.7× | 90.2% | 88.0% | 88.0% | 0.880 | 3 | 3 |\n| 2.0× | 95.1% | 100% | 88.0% | 0.936 | 0 | 3 |\n\n**AUROC = 0.9889**\n\nθ=1.5× FP (4): exp_082_cheetah_no_dt_emb_s0 (1.58, eval-variance-driven), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88, transient), exp_047_frozen_dt_emb_walker_s1 (1.71, transient)\n\nθ=2.0× FN (3): exp_008d_civo_trigger_s3 (1.53), exp_009b_008d_walker_s2 (1.62), exp_027_tcn_walker_s1 (1.64)\n\nNVE_peak 分布:\n- CIVO (25): min=1.530, median=4.100, max=70.640, mean=6.954\n- Healthy (36): min=0.100, median=0.800, max=1.930, mean=0.845\n- Overlap zone: NVE ∈ [1.530, 1.930], 含 3 CIVO + 4 Healthy\n\n### 组合诊断标准\n\n条件 A: NVE_peak ≥ τ\n条件 B: NVE > τ 持续 ≥2 个连续 eval 点 (排除瞬态 spike)\n条件 C: NVE 上升趋势 (≥10% 增幅)\n判定 CIVO positive 需 A ∧ B ∧ C 同时满足。无轨迹数据时回退到条件 A only。\n\n| Threshold | Accuracy | Precision | Recall | F1 | FP | FN | A_only fallback |\n|-----------|----------|-----------|--------|------|-----|-----|----------------|\n| 1.3× | 90.2% | 80.6% | 100% | 0.893 | 6 | 0 | 45/61 |\n| 1.5× | 91.8% | 88.5% | 92.0% | 0.902 | 3 | 2 | 45/61 |\n| 1.7× | 86.9% | 87.0% | 80.0% | 0.833 | 3 | 5 | 45/61 |\n| 2.0× | 91.8% | 100% | 80.0% | 0.889 | 0 | 5 | 45/61 |\n\n**关键发现**: 组合标准在 θ=1.3× 消除了 2 个 FP (exp_032b_dual_critic_walker_s1 和 exp_082_cheetah_no_dt_emb_s0 — 因 B 条件未满足而正确排除)。但引入新 FN (exp_008e_v3_walker_s2: B=N, 因 NVE 仅在末段突增而非持续; exp_029d_tcn_walker_s3_sigma02: B=N)。\n\n当 74% 实验缺少轨迹数据时，组合诊断相比单一阈值优势有限。\n\n---\n\n## Method B: Raw ve_ratio peak\n\n直接用 ve_ratio_peak (未除以 baseline) 作为分类分数。\n\n可用子集: N=35 (CIVO=15, Healthy=20)\n\n### 单一阈值\n\n| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |\n|-----------|----------|-----------|--------|------|-----|-----|\n| 0.8× | 80.0% | 70.0% | 93.3% | 0.800 | 6 | 1 |\n| 1.0× | 91.4% | 87.5% | 93.3% | 0.903 | 2 | 1 |\n| **1.3×** | **97.1%** | **100%** | **93.3%** | **0.966** | 0 | 1 |\n| 1.5× | 97.1% | 100% | 93.3% | 0.966 | 0 | 1 |\n| 2.0× | 88.6% | 100% | 73.3% | 0.846 | 0 | 4 |\n\n**AUROC = 0.9700**\n\nθ=1.3× FN (1): exp_009b_008d_walker_s2 (ve_ratio_peak=0.570, 但 step-matched NVE=1.62)\n\nve_ratio_peak 分布:\n- CIVO (15): min=0.570, median=3.000, max=24.112, mean=4.722\n- Healthy (20): min=0.200, median=0.527, max=1.283, mean=0.600\n\n### 组合诊断标准\n\n| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |\n|-----------|----------|-----------|--------|------|-----|-----|\n| 0.8× | 85.7% | 81.2% | 86.7% | 0.839 | 3 | 2 |\n| 1.0× | 85.7% | 85.7% | 80.0% | 0.828 | 2 | 3 |\n| 1.3× | 91.4% | 100% | 80.0% | 0.889 | 0 | 3 |\n| 1.5× | 88.6% | 100% | 73.3% | 0.846 | 0 | 4 |\n| 2.0× | 77.1% | 100% | 46.7% | 0.636 | 0 | 8 |\n\n---\n\n## NVE_median_last5 辅助指标\n\n对有轨迹数据的 16 个实验，取最后 5 个 checkpoint 的 NVE 中位数。\n\n| exp_id | type | NVE_median_last5 | label | correct? |\n|--------|------|-----------------|-------|----------|\n| exp_008e_v3_walker_s2 | CIVO | 0.900 | CIVO | ✗ |\n| exp_027_tcn_walker_s0 | CIVO | 1.396 | CIVO | ✓ |\n| exp_027_tcn_walker_s1 | CIVO | 0.982 | CIVO | ✗ |\n| exp_029b_tcn_walker_s2_sigma02 | CIVO | 2.315 | CIVO | ✓ |\n| exp_029d_tcn_walker_s3_sigma02 | CIVO | 1.284 | CIVO | ✓ |\n| exp_030b_tcn_cheetah_s0_sigma05 | CIVO | 1.674 | CIVO | ✓ |\n| exp_068_008d_walker_repro_s1 | CIVO | 4.116 | CIVO | ✓ |\n| exp_078_cheetah_008d_s0 | CIVO | 2.740 | CIVO | ✓ |\n| exp_008a_no_subsample_dt2 | Healthy | 1.043 | Healthy | ✗ |\n| exp_015b_frozen_dt_emb | Healthy | 0.420 | Healthy | ✓ |\n| exp_027_tcn_walker_s0_sigma02 | Healthy | 0.857 | Healthy | ✓ |\n| exp_029a_tcn_walker_s1_sigma02 | Healthy | 0.554 | Healthy | ✓ |\n| exp_032b_dual_critic_walker_s1 | Healthy | 0.700 | Healthy | ✓ |\n| exp_069_008f_walker_repro_s1 | Healthy | 0.533 | Healthy | ✓ |\n| exp_070_008e_v3_walker_s0 | Healthy | 0.888 | Healthy | ✓ |\n| exp_082_cheetah_no_dt_emb_s0 | Healthy | 0.980 | Healthy | ✓ |\n\n**分布统计**:\n- CIVO (8): min=0.900, median=1.674, max=4.116\n- Healthy (8): min=0.420, median=0.857, max=1.043\n- Accuracy: 13/16 = 81.2% (阈值=1.0)\n\n**误判分析**:\n- exp_008e_v3_walker_s2: median_last5=0.900 (CIVO, 误判为 Healthy) — NVE 末段才突增 (105K=3.78)，最后 5 点中前 4 个 < 1.0\n- exp_027_tcn_walker_s1: median_last5=0.982 (CIVO, 边界误判) — 自我修正型 CIVO\n- exp_008a_no_subsample_dt2: median_last5=1.043 (Healthy, 轻微超 1.0) — eval-variance-driven，非 CIVO\n\n**结论**: NVE_median_last5 有判别力但弱于 NVE_peak。预期 \"frozen 实验 median ≈ 0.5\" 在 exp_015b (0.420) 上验证成功。Healthy 组 median 整体 < 1.0，CIVO 组 median > 1.0 (6/8)。\n\n---\n\n## 单一阈值 vs 组合标准对比\n\n### Method A 对比\n\n| 指标 | 单一阈值 θ=1.5× | 组合标准 θ=1.5× | 单一阈值 θ=2.0× | 组合标准 θ=2.0× |\n|------|----------------|----------------|----------------|----------------|\n| Accuracy | **93.4%** | 91.8% | **95.1%** | 91.8% |\n| Precision | 86.2% | **88.5%** | **100%** | **100%** |\n| Recall | **100%** | 92.0% | **88.0%** | 80.0% |\n| F1 | **0.926** | 0.902 | **0.936** | 0.889 |\n| FP | 4 | **3** | **0** | **0** |\n| FN | **0** | 2 | **3** | 5 |\n\n### Method A vs Method B (最佳阈值)\n\n| 指标 | Method A θ=1.5× (N=61) | Method B θ=1.3× (N=35) |\n|------|------------------------|------------------------|\n| AUROC | **0.989** | 0.970 |\n| F1 | 0.926 | **0.966** |\n| Precision | 86.2% | **100%** |\n| Recall | **100%** | 93.3% |\n| FP | 4 | **0** |\n| FN | **0** | 1 |\n\n---\n\n## 推荐\n\n### 1. 主推 Method A (step-matched NVE), θ=1.5×\n\n- AUROC=0.989, 最高判别力\n- 100% recall — 不漏检任何 CIVO\n- 4 个 FP 全部可解释 (frozen transient spike + eval-variance-driven)\n- 与原论文 NVE 定义一致\n\n### 2. 组合诊断标准当前不推荐作为主分类器\n\n- 74% 实验缺少轨迹数据，导致大量 A_only 回退\n- 有轨迹数据时确实能消除 FP (exp_082 被正确排除)，但同时引入新 FN\n- **建议**: 作为 θ=1.5× 筛查后的二次确认，而非独立分类器\n\n### 3. Method B 作为补充验证\n\n- ve_ratio_peak 不受 baseline 选择偏差影响\n- 在 θ=1.3× 达到 100% precision + 96.6% F1 (N=35 子集)\n- exp_009b 是唯一 FN (ve_ratio_peak=0.570, 但 step-matched NVE=1.62)，说明 baseline normalization 对低幅 CIVO 更敏感\n\n### 4. Decision rule (更新)\n\n```\nif NVE_peak >= 1.5×:\n    → FLAG as potential CIVO\n    if trajectory_data_available:\n        if NVE > 1.5× for >= 2 consecutive checkpoints AND uptrend present:\n            → CONFIRM as CIVO\n        else:\n            → LIKELY transient spike, monitor but do not kill\n    else:\n        → TREAT as CIVO (conservative)\n        \nif NVE_peak >= 2.0×:\n    → DEFINITE CIVO (zero FP at this threshold)\n```\n\n### 5. Reviewer 关注点回应\n\n- **exp_084 (NVE=0.37) 和 exp_085 (NVE=0.31)**: 两种方法下均为 true negative。Reviewer 声称的 2.25/3.0 值与 registry 不符，可能使用了未经 baseline 归一化的 raw V/E 比值。frozen dt_emb 实验的 NVE 远低于任何阈值，不会产生假阳性。\n- **θ=2.0× 的 precision**: 在 Method A 单一阈值下仍为 100% (FP=0)，Reviewer 的 false positive 担忧未被数据支持。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01X4y4vViPQFn8QfYcRVCvQV`</summary>

```json
{
  "name": "NVE Threshold Analysis V2",
  "type": "report",
  "description": "NVE 阈值灵敏度分析 V2 — 双方法 (step-matched NVE + raw ve_ratio_peak) + 组合诊断标准 (A+B+C) + NVE_median_last5 辅助指标。N=61, AUROC=0.989 (Method A), 推荐 θ=1.5× 筛查 + θ=2.0× 确认。",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis_v2.md",
  "tags": [
    "nve",
    "threshold",
    "civo",
    "plan_034",
    "v2"
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
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "41a9eff5-46a9-42e2-b38e-410eed80cef7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMreXxHj2CndcBfbM1VX8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4868,
      "cache_read_input_tokens": 78186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4868
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

_source line 53 · 2026-05-25T20:27:05.807Z_

<details><summary>↩ Tool result · `toolu_01X4y4vViPQFn8QfYcRVCvQV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_828490\", \"name\": \"NVE Threshold Analysis V2\", \"type\": \"report\", \"description\": \"NVE 阈值灵敏度分析 V2 — 双方法 (step-matched NVE + raw ve_ratio_peak) + 组合诊断标准 (A+B+C) + NVE_median_last5 辅助指标。N=61, AUROC=0.989 (Method A), 推荐 θ=1.5× 筛查 + θ=2.0× 确认。\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/analysis_v2.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T20:27:05.305006+00:00\", \"tags\": [\"nve\", \"threshold\", \"civo\", \"plan_034\", \"v2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "10bdc747-1bfd-4116-91cc-70de12f959a8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260525_828490\\\", \\\"name\\\": \\\"NVE Threshold Analysis V2\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"NVE 阈值灵敏度分析 V2 — 双方法 (step-matched NVE + raw ve_ratio_peak) + 组合诊断标准 (A+B+C) + NVE_median_last5 辅助指标。N=61, AUROC=0.989 (Method A), 推荐 θ=1.5× 筛查 + θ=2.0× 确认。\\\", \\\"path\\\": \\\"projects/event-gated-adaptive-horizon/artifacts/_project/report/analysis_v2.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"event-gated-adaptive-horizon\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-25T20:27:05.305006+00:00\\\", \\\"tags\\\": [\\\"nve\\\", \\\"threshold\\\", \\\"civo\\\", \\\"plan_034\\\", \\\"v2\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_828490\", \"name\": \"NVE Threshold Analysis V2\", \"type\": \"report\", \"description\": \"NVE 阈值灵敏度分析 V2 — 双方法 (step-matched NVE + raw ve_ratio_peak) + 组合诊断标准 (A+B+C) + NVE_median_last5 辅助指标。N=61, AUROC=0.989 (Method A), 推荐 θ=1.5× 筛查 + θ=2.0× 确认。\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/analysis_v2.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T20:27:05.305006+00:00\", \"tags\": [\"nve\", \"threshold\", \"civo\", \"plan_034\", \"v2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

分析完成。报告已写入 `artifacts/plan_034_nve_threshold/analysis_v2.md` 并注册为 `art_20260525_828490`。

核心结论:

**Method A (step-matched NVE)** 仍是最佳分类器 (AUROC=0.989)。θ=1.5× 维持 100% recall，4 个 FP 均可解释 (frozen transient + eval-variance)。θ=2.0× 维持 100% precision (FP=0)。

**组合诊断标准** 在有轨迹数据的子集上能消除部分 FP (如 exp_082 被正确排除)，但 74% 实验缺少轨迹数据导致大量 A_only 回退，整体 F1 反而下降。建议作为二次确认而非独立分类器。

**Method B (raw ve_ratio_peak)** AUROC=0.970，在 θ=1.3× 达到 100% precision / F1=0.966 (N=35 子集)。不受 baseline 选择偏差影响，适合作为补充验证。

**Reviewer 关注点**: exp_084 NVE=0.37、exp_085 NVE=0.31，两种方法下均为 true negative。Reviewer 声称的 2.25/3.0 与 registry 数据不符，可能使用了不同的归一化方法。θ=2.0× 的 precision 仍为 100%。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "uuid": "2be7814c-e641-4182-aaaa-a296dc3ee053",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hLgRAWzNT43Qp32vyrcBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 83054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
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

_source line 55_

分析完成。报告已写入 `artifacts/plan_034_nve_threshold/analysis_v2.md` 并注册为 `art_20260525_828490`。

核心结论:

**Method A (step-matched NVE)** 仍是最佳分类器 (AUROC=0.989)。θ=1.5× 维持 100% recall，4 个 FP 均可解释 (frozen transient + eval-variance)。θ=2.0× 维持 100% precision (FP=0)。

**组合诊断标准** 在有轨迹数据的子集上能消除部分 FP (如 exp_082 被正确排除)，但 74% 实验缺少轨迹数据导致大量 A_only 回退，整体 F1 反而下降。建议作为二次确认而非独立分类器。

**Method B (raw ve_ratio_peak)** AUROC=0.970，在 θ=1.3× 达到 100% precision / F1=0.966 (N=35 子集)。不受 baseline 选择偏差影响，适合作为补充验证。

**Reviewer 关注点**: exp_084 NVE=0.37、exp_085 NVE=0.31，两种方法下均为 true negative。Reviewer 声称的 2.25/3.0 与 registry 数据不符，可能使用了不同的归一化方法。θ=2.0× 的 precision 仍为 100%。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 485591,
  "duration_api_ms": 484198,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "43c73d77-52ad-4826-98f1-2bd47073d289",
  "total_cost_usd": 1.554835,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 71932,
    "cache_read_input_tokens": 736138,
    "output_tokens": 29404,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 71932,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 425,
        "cache_read_input_tokens": 83054,
        "cache_creation_input_tokens": 719,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 719
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1891,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001991,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 29404,
      "cacheReadInputTokens": 736138,
      "cacheCreationInputTokens": 71932,
      "webSearchRequests": 0,
      "costUSD": 1.5528439999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6bdd74b2-0180-4642-b5e9-a7871629e373"
}
```

</details>

---
