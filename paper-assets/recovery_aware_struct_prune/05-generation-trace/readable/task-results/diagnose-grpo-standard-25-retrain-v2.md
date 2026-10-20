# diagnose grpo standard 25 retrain v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_standard_25_retrain_v2_20260523T192103_result.json`
- **Structured JSON:** [`301037b05f8da41f702d.json`](../../sessions/30/301037b05f8da41f702d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现：

**进程仍在运行。** PID 156633 存活，当前训练到 step 35/100，~26s/step，GPU 0 占用 55824 MiB。

**OOM 发生在 step 0**（log 第 35-69 行），bitsandbytes 8-bit Adam 初始化 optimizer state 时分配 66 MiB 失败（GPU 仅剩 62.56 MiB free）。模型 + ref_model 已占满 ~54.52 GiB / 94.97 GiB。但进程未死，训练恢复后继续推进。

**Cron EXIT_CODE=1 是误报。** 退出文件 `/tmp/agent-ml-exit/grpo_standard_25_retrain_v2.exit` 内容为 `1|2026-05-23T19:15:58Z`（OOM 发生时刻），但 wrapper 进程 (156624) 和 Python 进程 (156633) 均存活。监控系统可能从日志中的 traceback 或 stale exit file 误判了状态。

**额外观察：** 命令行传入 `--beta 0.04`，但日志显示 `beta=0.01`，存在参数不一致。

```json
{"root_cause":"CUDA OOM at step 0 during bitsandbytes optimizer init_state (66 MiB allocation failed, only 62.56 MiB free on 95GB GPU with model+ref_model consuming 54.52 GiB), but process recovered and training is progressing. Cron EXIT_CODE=1 is false alarm from stale exit file.","error_type":"resource","fix_steps":["无需修复——进程存活，训练正在 35/100 步正常推进","监控到 exit file 为 stale，训练完成后 EXIT trap 会覆盖","确认 --beta 0.04 vs log beta=0.01 是否符合预期"],"can_auto_fix":false,"process_still_alive":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "CUDA OOM at step 0 during bitsandbytes optimizer init_state (66 MiB allocation failed, only 62.56 MiB free on 95GB GPU with model+ref_model consuming 54.52 GiB), but process recovered and training is progressing. Cron EXIT_CODE=1 is false alarm from stale exit file.",
    "error_type": "resource",
    "fix_steps": [
      "无需修复——进程存活，训练正在 35/100 步正常推进",
      "监控到 exit file 为 stale，训练完成后 EXIT trap 会覆盖",
      "确认 --beta 0.04 vs log beta=0.01 是否符合预期"
    ],
    "can_auto_fix": false,
    "process_still_alive": true
  }
}
```

</details>

---
