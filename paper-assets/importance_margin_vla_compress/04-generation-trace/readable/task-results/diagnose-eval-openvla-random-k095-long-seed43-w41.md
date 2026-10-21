# diagnose eval openvla random k095 long seed43 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_random_k095_long_seed43_w41_20260528T064436_result.json`
- **Structured JSON:** [`48e0686b6fd88d219a5c.json`](../../sessions/48/48e0686b6fd88d219a5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论已明确。

**实验没有失败，仍在正常运行。**

- **PID 700644**（bash -c wrapper）已退出——这是你看到的"进程消失"。但实际的 **python 进程 PID 700653** 仍在运行，GPU 1 利用率 91%，stdout (fd/1) 仍连接到日志文件。
- 日志最后更新 14:42:00（打印 Task 2 标题），距今约 5 分钟。Task 2 正在跑前 10 个 episode，按 1.1 eps/min 速率约需 9 分钟才会打印下一行进度。这是正常的打印间隔。
- 磁盘 36% 使用率，GPU 显存充裕（16GB / 98GB），无 OOM/kill 系统日志。

**注意**：GPU 1 上 14:37 新加了一个 pi05 random k0.7 seed46 实验 (PID 744884, 10.7GB)，两个进程共用 GPU 1 约 27GB / 98GB，空间足够但可能略微拖慢推理速度。

```json
{"root_cause":"误报——bash wrapper PID 700644 退出，但 python 子进程 PID 700653 仍在 GPU 1 正常运行（91% util, fd/1 → log file）。日志停在 Task 2 标题是因为还没到下一个 10-episode 打印点。","error_type":"infrastructure","fix_steps":["无需修复，等待约 4 分钟后检查日志是否出现 Task 2 的 Ep 10/50 行即可确认"],"can_auto_fix":false,"resubmit_safe":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "误报——bash wrapper PID 700644 退出，但 python 子进程 PID 700653 仍在 GPU 1 正常运行（91% util, fd/1 → log file）。日志停在 Task 2 标题是因为还没到下一个 10-episode 打印点。",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，等待约 4 分钟后检查日志是否出现 Task 2 的 Ep 10/50 行即可确认"
    ],
    "can_auto_fix": false,
    "resubmit_safe": false
  }
}
```

</details>

---
