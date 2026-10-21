# diagnose exp 003

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-003_20260521T102232_result.json`
- **Structured JSON:** [`e542cf867a3ca5d61df5.json`](../../sessions/e5/e542cf867a3ca5d61df5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。`trainer_state.json` 确认 `global_step: 8000`。

**结论：exp-003 训练正常完成，Cron 报告是误报。**

时间线：
- `exp003_restart.log`（May 18 23:05）：更早的失败尝试，因网络不可达无法从 HF 下载 `microsoft/deberta-v3-base` 而崩溃
- `exp003_v2.log`（May 19 00:51 → May 20 05:55）：成功启动的运行，日志在 step 3760 后停止写入（stdout 缓冲/fd 断开），但训练继续执行
- Checkpoint 持续保存到 8000（May 21 18:12），`final/` 目录包含完整 adapter model
- 进程正常退出后 Cron 5次检测到进程不存在，因缺少 sentinel 文件/W&B 心跳，误判为失败

```json
{"last_step": 8000, "max_checkpoint": 8000, "ckpt_8000_exists": true, "root_cause": "训练正常完成全部8000步(trainer_state.json确认global_step=8000)。exp003_v2.log在step 3760后停止写入(stdout fd断开)但训练未中断。Cron因无completion sentinel/W&B心跳而误报process dead。", "error_type": "normal_completion", "gpu_released": true, "fix_steps": ["无需修复——训练已正常完成", "建议: 训练脚本结尾添加sentinel文件(如touch .done)防止Cron误报", "可直接使用checkpoint-8000或final/进行后续评估"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "last_step": 8000,
    "max_checkpoint": 8000,
    "ckpt_8000_exists": true,
    "root_cause": "训练正常完成全部8000步(trainer_state.json确认global_step=8000)。exp003_v2.log在step 3760后停止写入(stdout fd断开)但训练未中断。Cron因无completion sentinel/W&B心跳而误报process dead。",
    "error_type": "normal_completion",
    "gpu_released": true,
    "fix_steps": [
      "无需修复——训练已正常完成",
      "建议: 训练脚本结尾添加sentinel文件(如touch .done)防止Cron误报",
      "可直接使用checkpoint-8000或final/进行后续评估"
    ]
  }
}
```

</details>

---
