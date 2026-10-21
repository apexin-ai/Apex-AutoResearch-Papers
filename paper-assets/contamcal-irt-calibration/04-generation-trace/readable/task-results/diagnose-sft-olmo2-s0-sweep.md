# diagnose sft olmo2 s0 sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_olmo2_s0_sweep_20260520T032029_result.json`
- **Structured JSON:** [`a60a9568fdaff13a0e78.json`](../../sessions/a6/a60a9568fdaff13a0e78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**实验没有失败，Cron 报告是误报。**

根因：日志文件 `sft_olmo2_s0_sweep.log` 在 09:19 停止更新（12KB，最后可见 step 139/3125），但这是 **tqdm + nohup 输出缓冲** 导致的假象。实际训练正常完成：

- **d000**: 09:14 开始 → 10:56 完成（`.done` + `train_config.json` 均存在）
- **d005**: PID 261133 于 10:56 启动，当前在 GPU 2 运行（67GB VRAM, 93% util），`lora_adapter/` 目录已创建但尚空（未到首个 save point）
- **d025/d050/d100**: 排队等待（sweep 顺序 000→005→025→050→100）

Cron 误判原因：log 文件因 tqdm `\r` 进度条 + nohup 缓冲机制停止刷新，监控系统看到日志 2h 无更新 + 无 W&B sentinel → 误判为 dead。

```json
{"root_cause":"Log file output buffering: tqdm progress bars with nohup redirection caused log to freeze at step 139 (09:19) while training continued normally. Cron monitor saw stale log + no W&B sentinel and falsely reported process dead.","error_type":"infrastructure","fix_steps":["No fix needed - experiment is running normally","To prevent future false alarms: add PYTHONUNBUFFERED=1 to sweep script, or add periodic heartbeat writes to a separate sentinel file","Consider adding nvidia-smi GPU utilization check to cron monitor as secondary liveness signal"],"can_auto_fix":true,"completed_dosages":["d000"],"missing_dosages":["d005 (in progress ~25%)","d025","d050","d100"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Log file output buffering: tqdm progress bars with nohup redirection caused log to freeze at step 139 (09:19) while training continued normally. Cron monitor saw stale log + no W&B sentinel and falsely reported process dead.",
    "error_type": "infrastructure",
    "fix_steps": [
      "No fix needed - experiment is running normally",
      "To prevent future false alarms: add PYTHONUNBUFFERED=1 to sweep script, or add periodic heartbeat writes to a separate sentinel file",
      "Consider adding nvidia-smi GPU utilization check to cron monitor as secondary liveness signal"
    ],
    "can_auto_fix": true,
    "completed_dosages": [
      "d000"
    ],
    "missing_dosages": [
      "d005 (in progress ~25%)",
      "d025",
      "d050",
      "d100"
    ]
  }
}
```

</details>

---
