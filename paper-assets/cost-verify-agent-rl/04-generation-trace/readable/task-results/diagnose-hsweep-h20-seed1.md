# diagnose hsweep h20 seed1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_hsweep_h20_seed1_20260518T184044_result.json`
- **Structured JSON:** [`fe284661fe2e51e34ca5.json`](../../sessions/fe/fe284661fe2e51e34ca5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。

**cgroup OOM kill**: `memory.oom_control` 显示 **oom_kill: 24**（容器历史累计 24 次 OOM kill），cgroup 内存限制 **~220GB** (`236223201280` bytes)。

关键证据链：
1. cgroup 限制 220GB，Ray 配置 memory=202GB + object_store=30GB，加上 FSDP `optimizer_offload: True`（把优化器状态卸载到 CPU RAM）+ vLLM 推理引擎 + 40+ Ray worker 进程 → 超限
2. Raylet (PID 72438) 被 cgroup SIGKILL，无法写任何错误日志（raylet.err 为空）
3. Worker 在 `02:30:22` 检测到 raylet 失联："Shutting down the core worker because the local raylet failed"
4. 整个进程树级联崩溃，训练在 step 0（首次 rollout 阶段）就死了，checkpoint 目录为空

```json
{"root_cause":"cgroup OOM kill: container memory limit 220GB exceeded. cgroup memory.oom_control shows oom_kill=24 (cumulative). Raylet PID 72438 was SIGKILL'd at ~02:30. Evidence: raylet.err empty, worker log shows 'Shutting down the core worker because the local raylet failed. Raylet pid: 72438'. FSDP optimizer_offload=True + Ray object_store_memory=30GB + 44 CPU workers + vLLM engine exceeded 220GB cgroup limit during first rollout.","error_type":"resource","fix_steps":["Reduce Ray object_store_memory from 30GB (e.g. 16GB)","Set optimizer_offload=False (keep optimizer on GPU if VRAM allows, or reduce model parallelism overhead)","Reduce number of Ray workers/env_groups (currently train.env_groups=16 x group_size=8 = 128 parallel envs)","Consider running on westd-47453 which has 4x96GB GPUs and likely higher memory cgroup limit","Monitor with: watch -n5 'cat /sys/fs/cgroup/memory/memory.usage_in_bytes' during next run"],"can_auto_fix":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "cgroup OOM kill: container memory limit 220GB exceeded. cgroup memory.oom_control shows oom_kill=24 (cumulative). Raylet PID 72438 was SIGKILL'd at ~02:30. Evidence: raylet.err empty, worker log shows 'Shutting down the core worker because the local raylet failed. Raylet pid: 72438'. FSDP optimizer_offload=True + Ray object_store_memory=30GB + 44 CPU workers + vLLM engine exceeded 220GB cgroup limit during first rollout.",
    "error_type": "resource",
    "fix_steps": [
      "Reduce Ray object_store_memory from 30GB (e.g. 16GB)",
      "Set optimizer_offload=False (keep optimizer on GPU if VRAM allows, or reduce model parallelism overhead)",
      "Reduce number of Ray workers/env_groups (currently train.env_groups=16 x group_size=8 = 128 parallel envs)",
      "Consider running on westd-47453 which has 4x96GB GPUs and likely higher memory cgroup limit",
      "Monitor with: watch -n5 'cat /sys/fs/cgroup/memory/memory.usage_in_bytes' during next run"
    ],
    "can_auto_fix": false
  }
}
```

</details>

---
