# diagnose cqa1 triple failure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1-triple-failure_20260526T093253_result.json`
- **Structured JSON:** [`4415c4f1b52e16515444.json`](../../sessions/44/4415c4f1b52e16515444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。所有证据明确：

**根因**：GPU 3/4/5 被之前手动启动的 tmux 会话（pi05-obj-s44, pi05-long-s43, pi05-long-s44，13:54 创建）占用。agent 管理的 3 个实验（pi05-adaptive-object-s44-cqa1, pi05-adaptive-long-s43-cqa1, pi05-adaptive-long-s44-cqa1）尝试在已占用的 GPU 上启动，CUDA OOM 立即崩溃——无日志、无退出文件、进程从未成活。

**关键事实**：
- 服务器上有 **6 个 tmux 会话和 6 个 python 进程**，全部 6 张 GPU 满载
- 3 个 agent 管理的存活实验（GPU 0/1/2）正常运行
- GPU 3/4/5 上跑的是**手动启动的同任务实验**（pi05-obj-s44 等），也在正常推进
- 系统 RAM 充足（1TB 总量，877GB 可用），磁盘正常（14%/4%）
- 不是 OOM killer、不是磁盘满、不是系统问题——纯粹是 GPU 冲突

```json
{"root_cause":"GPU 3/4/5 被手动启动的 tmux 会话 (pi05-obj-s44, pi05-long-s43, pi05-long-s44, 13:54创建) 占用，agent 管理的 3 个实验无法分配 GPU 显存立即崩溃（无日志无退出文件）","error_type":"resource","fix_steps":["等待手动实验 pi05-obj-s44/pi05-long-s43/pi05-long-s44 自然结束（正在跑最后几个 task）","或 kill 手动实验释放 GPU 3/4/5 后重跑","重跑时确认 GPU 3/4/5 空闲再启动"],"can_auto_fix":true,"surviving_exps_healthy":true,"available_gpus":[]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "GPU 3/4/5 被手动启动的 tmux 会话 (pi05-obj-s44, pi05-long-s43, pi05-long-s44, 13:54创建) 占用，agent 管理的 3 个实验无法分配 GPU 显存立即崩溃（无日志无退出文件）",
    "error_type": "resource",
    "fix_steps": [
      "等待手动实验 pi05-obj-s44/pi05-long-s43/pi05-long-s44 自然结束（正在跑最后几个 task）",
      "或 kill 手动实验释放 GPU 3/4/5 后重跑",
      "重跑时确认 GPU 3/4/5 空闲再启动"
    ],
    "can_auto_fix": true,
    "surviving_exps_healthy": true,
    "available_gpus": []
  }
}
```

</details>

---
