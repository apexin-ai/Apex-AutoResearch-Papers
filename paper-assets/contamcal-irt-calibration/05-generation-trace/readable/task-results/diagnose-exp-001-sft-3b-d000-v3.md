# diagnose exp 001 sft 3B d000 v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_3B_d000_v3_20260515T190929_result.json`
- **Structured JSON:** [`4c64a564eeafae1cf2ad.json`](../../sessions/4c/4c64a564eeafae1cf2ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。**训练没有失败，是误报。**

进程树：
```
PID 597174 (已死) ← 监控追踪的 PID，只是启动用的 bash shell，立即退出
  └─ PID 597178 (alive, PPID=1) ← timeout 43200 wrapper
       └─ PID 597179 (alive, 99% CPU, 13868MiB GPU4) ← 实际训练进程
            ├─ PID 597466 (dataloader worker)
            ├─ PID 597467 (dataloader worker)
            ├─ PID 597468 (dataloader worker)
            └─ PID 597469 (dataloader worker)
```

监控系统追踪了 PID 597174（启动时的临时 bash shell），该进程 spawn 了 `timeout` wrapper 后即退出。cron 连续 5 次检测 597174 不存在，误判为失败。实际训练进程 597179 一直在 GPU 4 上正常运行，当前进度 ~56%（step 1746/3125）。

checkpoint 目录为空是因为 `save_strategy=epoch`，第一次存储要到 epoch 1.0（当前 epoch 0.26）。

```json
{"root_cause":"监控追踪了错误的PID(597174=临时bash shell)，实际训练进程PID 597179仍在GPU4正常运行(13868MiB, step 1746/3125, 56%)","error_type":"infrastructure","fix_steps":["将实验状态从failed改回running","更新监控PID为597179(实际python进程)或597178(timeout wrapper)","修复提交脚本使其记录实际python进程PID而非启动shell PID"],"can_auto_fix":true,"has_checkpoint":false,"checkpoint_path":"无(save_strategy=epoch,首次保存在epoch 1.0,当前epoch 0.26)"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "监控追踪了错误的PID(597174=临时bash shell)，实际训练进程PID 597179仍在GPU4正常运行(13868MiB, step 1746/3125, 56%)",
    "error_type": "infrastructure",
    "fix_steps": [
      "将实验状态从failed改回running",
      "更新监控PID为597179(实际python进程)或597178(timeout wrapper)",
      "修复提交脚本使其记录实际python进程PID而非启动shell PID"
    ],
    "can_auto_fix": true,
    "has_checkpoint": false,
    "checkpoint_path": "无(save_strategy=epoch,首次保存在epoch 1.0,当前epoch 0.26)"
  }
}
```

</details>

---
